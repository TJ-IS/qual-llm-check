---
otero_id: 8800
otero_key: "YM34F7GP"
title: "Counterfeit product detection: Bridging the gap between design science and behavioral science in information systems research"
authors: "Hayden Wimmer; Victoria Y. Yoon"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.09.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Counterfeit product detection: Bridging the gap between design science and behavioral science in information systems research

Hayden Wimmer, Victoria Y. Yoon

![](/api/attachments/YM34F7GP/fulltext/images/948ed42bc37e72630302c948d2e5bb9984ac0fccee020c738b65b01c4afb9505.jpg)

<table><tr><td>PII:</td><td>S0167-9236(17)30172-0</td></tr><tr><td>DOI:</td><td>doi:10.1016/j.dss.2017.09.005</td></tr><tr><td>Reference:</td><td>DECSUP 12876</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>16 January 2017</td></tr><tr><td>Revised date:</td><td>18 September 2017</td></tr><tr><td>Accepted date:</td><td>19 September 2017</td></tr></table>

Please cite this article as: Hayden Wimmer, Victoria Y. Yoon , Counterfeit product detection: Bridging the gap between design science and behavioral science in information systems research. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), doi:10.1016/j.dss.2017.09.005

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

Title Page

# Counterfeit Product Detection: Bridging the Gap between Design Science and Behavioral Science in Information Systems Research

Hayden Wimmer

Department of Information Technology

Georgia Southern University

P.O. Box 8150 Statesboro, GA 30460

hwimmer@georgiasouthern.edu

Victoria Y. Yoon\*

Department of Information Systems

Virginia Commonwealth University

301 W. Main St. P. O. Box 844000

Richmond, VA 23284-4000

vyyoon@vcu.edu

\* Corresponding Author

## Abstract

In IS research, there is a dichotomy where design science and behavioral science are distinct research paradigms. IS researchers should view these paradigms as complementary with research drawing upon the strengths of both, yet few have done so. This work demonstrates how design science and behavioral science can be united in IS research via counterfeit product detection based on product reviews in an online marketplace. Product authenticity in the online marketplace is a common issue plaguing consumers. The decision process involved in determining product authenticity is lengthy and complex. Despite the pressing need for an automatic authenticity rating system for online shopping, little research has been done to develop such a system and assess its effects on consumer purchase behavior. To respond to this need, our study develops a design artifact, called OnCDS, to automatically calculate the likelihood that a product is counterfeit based on online customer reviews. Drawing upon lexicon-based sentiment analysis approaches and TF-IDF as kernel theories for our design, we employ web scraping, natural language processing, and topic analysis methods to process customer reviews and calculate the counterfeit score of a product. In assessing the effects of OnCDS on consumer behavior, we develop a research model that encompasses trust and perceived risk based on the valence framework. Results show that our design artifact’s efficacy is validated and that the counterfeit score affects perceived risk and trust, which in turn influences attitude toward purchase.

Keywords: Counterfeit, Design Science, Behavioral Science, Trust, Risk, Attitude

## Counterfeit Product Detection: Bridging the Gap between Design Science and Behavioral Science in Information Systems Research

## 1 Introduction

Counterfeit goods, specifically luxury goods, comprise a rapidly expanding industry [2]. Counterfeiting has expanded and flourished in part due to the demand for luxury goods [12]. Pervasive counterfeit goods in the marketplace devalue product branding and have a significant negative impact on the global economy. According to estimates from the Organization for Economic Co-operation and Development (OECD), international trade on counterfeit and pirated goods accounted for USD 461 billion in 2013 [67], which is approximately 2.5% of world trade. These estimates unfortunately represent a substantial increase from those in 2008. A similar OECD study in 2008 reported that counterfeit and pirated products were worth USD 200 billion, which is about 1.9% of world trade. The 2009 report created by the organization Business Action to Stop Counterfeiting and Piracy (BASCAP) estimates that USD 62 billion is lost annually from tax revenue due to counterfeiting and piracy. Moreover, the BASCAP report also states that there is a USD 20 billion increase in related crimes and a USD 14.5 billion in lost lives cost, all of which is augmented by USD 100 million in additional healthcare services required for fake products (e.g. medications) [5]. Compounding the issue is the fact that purchasers of counterfeit goods often feel the goods are comparable to authentic brand goods and are unaware of the potential negative effects that purchasing counterfeit products has on the economy [66].

Online marketplaces, such as Amazon.com and eBay, have low barriers to entry and thus are more vulnerable for counterfeit products than traditional brick and mortar establishments. Fraudsters can easily assume different or multiple identities, making them difficult to trace [19]. The advent of technology has produced conditions which can be exploited by criminals [64]. Further, counterfeit products are frequently sold via legitimate websites [93]. One such example is the premium brand Tiffany & Co. The company launched, and subsequently lost, a lawsuit against eBay due to the large amount of its counterfeit merchandise on eBay’s online auction website [39]. Tiffany & Co. had employees purchase

325 items from eBay listed as Tiffany & Co. products and determined that 75% of the items were counterfeit [14]. EBay implemented buyer protections against counterfeit products; however, they are still exchanged on a worldwide basis. Amazon is not only a seller but has evolved into an online marketplace that brings sellers from across the world together on the Amazon platform to sell their products alongside Amazon’s products on Amazon.com [3]. According to Martin [61] of Entrepreneur.com, Amazon is not market and sell their products. On the downside, in 2017, the number of scams on Amazon.com ncreased, fraudulent sellers were prevalent, and fraudulent sellers absconded with massive profits [82].

Counterfeit goods in the online marketplace are a serious issue plaguing consumers. The decision-making process involved in determining the authenticity of a product is lengthy and complex. A consumer must review a large volume of qualitative information, such as product and seller reviews, to determine the authenticity of a product. Sellers can easily enter and leave the online marketplace, thereby adding factors into an already complex decision process. Web crawlers, application programming interfaces, natural language processing, and topic analysis may be employed to support the consumer’s decision-making process by automatically rating the authenticity of products in online marketplaces, such as Amazon. Further, authenticity ratings may improve trust in the product, thereby increasing its sales. While literature presents abundant research on e-commerce, they focus largely on consumer behavior and purchasing counterfeit products, remaining in the realm of behavioral research. Unfortunately, a dichotomy exists within IS research with design science and behavioral research viewed as distinct research paradigms. IS researchers should view these paradigms as complementary with research drawing upon the strengths of both. Despite the usefulness and potential benefits of an automatic authenticity rating system in online shopping, few research has proposed such a system and empirically evaluated its effects on consumer purchase behavior, which bridges the two IS research paradigms

To fill in this gap, this study develops an automatic counterfeit scoring system, called Online Counterfeit Detection Score (OnCDS), to support the consumer’s decision making process by identifying counterfeit goods based on consumer product reviews and empirically tests its utility using a research

# ACCEPTED MANUSCRIPT

model drawn upon the valence framework [76] in consumer behavior. The design science research methods [46, 74] and information systems design theory [36] provide the guidelines for designing OnCDS. Adopting lexicon-based sentiment analysis and Term Frequency/Inverse Document Frequency (TF-IDF) as kernel theories for our study, we employ web scraping, natural language processing, and topic analysis to process customer reviews from an online marketplace and calculate the counterfeit scores of products. We instantiate our design artifact and evaluate its performance with human subjects recruited from Amazon Mechanical Turk. Additionally, we empirically test our research model that hypothesizes the effect of our design artifact on consumer purchase attitude. Results show that the counterfeit score affects trust and perceived risks, which in turn affect attitude toward purchase. Few prior studies have performed behavioral research to assess the utilities of a proposed design artifact. As a result, this study significantly contributes to IS literature by not only developing an automatic counterfeit scoring system based on consumer product reviews, but also by demonstrating how two IS research paradigms, design science and behavioral research, can be united to raise research rigor and relevance.

The remainder of this paper is organized as follows. Section 2 provides the literature review, followed by the discussion on the dichotomy in IS research in Section 3. Section 4 presents the theoretical details, and its performance evaluation. Section 6 explains our behavioral research methods to empirically test the effects of our proposed artifact on consumer behavior and the test results. Section 7 presents the discussion of study implications and offers conclusions and future research directions.

## 2 Literature Review

## 2.1 Counterfeit Goods

In many cases, consumers seek to purchase counterfeit goods for a reason, such as lower price or as a substitute for the original, with the online marketplace becoming the dominant marketplace for purchasing counterfeit goods [80]. In fact, the demand for counterfeit goods is driven by the demand for the actual luxury good [75] and the success of a brand [59]. Some goods are more easily replicated than others, such as textiles over luxury watches. Different types of counterfeit goods garner different profit margins. Different strategies have emerged from the perspective of the counterfeiter: dis-aggregators, imitators, fraudsters, desperados, and smugglers [84]. Dis-aggregators sell products without complexity, which are, therefore, easily manufactured (e.g. textiles). Imitators produce goods that are visually similar to actual brand-named goods. Fraudsters seek to deceive consumers and sell goods that are visually similar to the original; however, they are non-functional or not functionally equivalent. Desperados are similar to fraudsters but more brazen and will counterfeit goods which may endanger the consumer (e.g. pharmaceuticals). Smugglers sell authentic goods but seek to evade taxes or levies or sell stolen merchandise.

Besides the aforementioned business strategies, counterfeit products may be classified into one of 4 categories: knock-offs, reverse-engineered products, product overruns, and genuine products which are faulty or imperfect [9]. Knock-offs are products that closely resemble the original; however, they lack in quality or performance. Product overruns occur when a manufacturer, typically an outsourcer, continues production after termination of the contract with the brand owner. Reverse-engineered products occur when a product is reverse-engineered and a reproduction is created from the original product that closely matches the original in quality and performance. Often a product suffers a defect during the manufacturing process and therefore does not meet the quality expectations of the brand holder. These are genuine products which are labeled as flawed or imperfect.

## 2.2 Counterfeit Goods Detection

Scenarios and research exist which may aid in detecting the fraudulent products. For example, research has shown that when a retailer conceals its physical address, it is fraudulent 50% of the time [8]. However, a gap exists in research on the ways which counterfeiters market their products online and the methods for detecting counterfeit goods over authentic products [93]. In currency from the United States, safeguards such as denomination strips are embedded into the currency to aid in counterfeit detection. Similarly, researchers have embedded physical safeguards into products, such as RFID tags [81]; however, these methods are only effective if a consumer has physical access to the product and are

# ACCEPTED MANUSCRIPT

therefore not effective in an online marketplace. Decision aids, such as recommender systems, have been shown to increase intent to purchase by providing interactive decision aids during the purchase process [45, 48]. Website design may also increase trust [42]. Trust in an online auction house, such as eBay, or marketplace such as Amazon may increase with improved design. Internet auction fraud is one of the fastest growing Internet crimes and presents a challenge to consumers during the decision making process of purchasing a product. However, to our best knowledge, no design artifact to aid in detecting counterfeit products exists. In response to this need, this research aims to develop an automatic counterfeit detection, following the design science research guidelines [46, 74] and to empirically test its effect on consumer purchase behavior.

## 3 Duality in IS Research

A duality exists in Information Systems research between design and science. Instead of viewing the aforesaid as competing research models, they should be viewed as complementary. Currently, there is a need for research that bridges the gap between design an science. Dualities exist within design-science research where the science has overtaken design [6]. First, the three levels of the design framework are proposed as 1) designing with research, 2) research into design, and 3) design as a research methodology. Next, three overarching guidelines are proposed. Guideline 1, design as the means or the end in the activities, focuses on the role of design in research. Guideline 2, design as the product, subject, or vehicle, guides the role of design in the outcomes of the research. Guideline 3, design and knowledge contribution, directs whether the design knowledge is central or secondary. Guidelines are set forth at each level. The relationship between design and research is proposed in order to set a future direction for design science research.

Extending Baskerville, Kaul and Storey [6], Baskerville, Kaul and Storey [7] further refines direction for design science research with the advent of genres of inquiry [7]. Dualities in design science research are defined as 1) knowledge goals of design versus science and 2) knowledge scope of nomothetic versus idiographic. The first duality stems from the contradictory goals of design and science

# ACCEPTED MANUSCRIPT

[30]. Design focuses on the creation of an artifact while science is designed to produce new knowledge. Although these two focuses are often considered separate activities, they should be considered complementary. Duality 2 is the difference between nomothetic and idiographic knowledge. Nomothetic knowledge is generalized theories and concepts that can be applied to many cases [37] whereas idiographic knowledge is more specific studying individuals, groups, or cases [15].

The duality of knowledge production in design versus science is a key focus of this work. Ideally, design research and design science first lay down the solid theoretical foundation, then proceed to the creation of an artifact drawn on kernel theories, and finally extend to studying the artifact’s effect on classic IS behavioral research [89]. This paper addresses the duality in IS research by first defining the theoretical framework and developing a research model drawn upon a consumer behavioral theory. The artifact is then created and iteratively refined based on kernel theories. A research model is also empirically tested to assess the outcome of interest for our design – the effects of the counterfeit score on attitude towards purchasing a product. Our research approach of developing a theoretical framework and research model, constructing a design artifact, validating the artifact, then extending into behavioral research takes IS research full circle from formulating a research model drawn upon theoretical framework, the situated implementation of a design artifact, to development of theory that can guide future research. Following Baskerville, Kaul and Storey [7], we address knowledge moments in each of the genres of inquiry.

## 4 Theoretical Framework and Research Hypotheses

## 4.1 Information Systems Design Theory (ISDT)

Many design science researchers have emphasized the importance for design theories to help govern the design process [35, 36, 91]. Our research aims to construct a novel IS artifact that can assist consumers in determining the authenticity of a product. In doing so, we follow the design science research methods [35, 36, 46] to ensure the research rigor and legitimacy. Specifically, drawing upon Information Systems Design Theory (ISDT) [36] that suggests the eight critical components, we develop our design

artifact and evaluate its utility. The eight components of an ISDT are: (1) purpose and scope, (2) constructs, (3) principles of form and function, (4) artifact mutability, (5) testable propositions, (6) justificatory knowledge, (7) principles of implementation, and (8) expository instantiation. The first component suggests that the purpose and scope of design should be clearly specified. The second component, constructs, refers to the entities of interest drawn upon the theories. The third component, principles of forms and functions, describes the architecture and functions of a design product or method. The fourth component, artifact mutability, describes the degree of artifact change anticipated by the theory. The fifth component refers to testable propositions or hypotheses about a design artifact to be developed. The sixth component, justifiable knowledge (also called kernel theories), presents the theories from the natural, social, or design sciences that govern design specifications. The seventh component, principles of implementation, describes the process in which a design is brought into material being in the form of either product or method. The eighth component is a physical instance of the artifact ―for the he aforementioned eight components of ISDT govern the process of capturing, articulating, justifying, and communicating our design knowledge. Table 1 presents the summary of the eight components of ISDT in the context of our study. The subsequent sections have detailed discussions on each component in our study.

<table><tr><td colspan="2">Table 1: Eight Components of Information Systems Design Theory(Adapted from Gregor and Jones [36])</td></tr><tr><td>Component</td><td>Description</td></tr><tr><td>Purpose and Scope</td><td>Our design artifact aims to assist consumers in detecting counterfeit products from online marketplaces by providing a product counterfeit score that indicates the likelihood of a product being counterfeit based on consumer product reviews.</td></tr><tr><td>Constructs</td><td>Drawing on the theories in academic literature, entities of interest are identified:Lexicon-based sentiment analysis and TF-IDF (online product views, adjective terms, dictionary, index, topics, ranking; discussed in Section 4.2)Valence Framework on shopping (trust, perceived risks, attitude toward purchase; discussed in Section 4.3)</td></tr><tr><td>Principles of form and function</td><td>The architecture of the proposed design artifact includes the methods for:Web scrapingNatural Language processingIndexing and topic analysisRanking calculation</td></tr><tr><td>Artifact</td><td>Our artifact is generalizable and can be adapted to any web browser that supports</td></tr><tr><td>mutability</td><td>extensions or plugins. The modular approach ensures the artifact can be adapted to various marketplaces via updating the required components.</td></tr><tr><td>Testable propositions</td><td>Drawing on the valence framework on consumer behavior, we posit the four hypotheses. (discussed in Section 4.3)</td></tr><tr><td>Justificatory knowledge</td><td>The kernel theories of our design are TF-IDF and lexicon-based sentiment analysis approaches.</td></tr><tr><td>Principles of implementation</td><td>We describe the implementation process of the proposed design artifact using online reviews from the Amazon.com marketplace. We also offer several recommendations for implementation.</td></tr><tr><td>Expository instantiation.</td><td>The proposed design artifact is implemented in a simulated yet realistic online shopping environment using a Chrome add-on, OpenNLP, Apache Lucene , Java, etc.</td></tr></table>

## 4.2 Kernel Theory

The significance of kernel theory, which informs artifact development, cannot be overemphasized [35, 36, 78]. Gregor and Hevner [35] stress that design knowledge should include kernel theory since such a theory explains why an artifact is designed as it is and why it works. Kernel theories can be the theories from natural, social, or design sciences. Given a lack of prior work for the design and development of automatic counterfeit detecting systems, we turn to information retrieval and text mining literature, specifically Term Frequency/Inverse Document Frequency (TF-IDF) and sentiment analysis, for kernel theories. TF-IDF is a statistical measure that represents the importance of a term T within a document. The value, which is a product of TF and IDF, is calculated by counting the frequency of the term T in an individual document (TF) as opposed to a corpus of documents (IDF) [60]. TF and IDF are defined as:

$$
T F (t) = \sum_ {i = 1} ^ {n u m T e r m s} (t)
$$

$$
I D F (t) = \log (\frac {n u m d o c s}{\sum_ {i = 1} ^ {n u m D o c s} (t)})
$$

The TF-IDF value increases proportionally to the frequency of a term T in an individual document and is offset by the occurrence of the term T in the collection of documents. Such TF-IDF informs our method for weighting the keywords in calculating counterfeit scores.

Sentiment analysis is the process of systematically identifying the semantic orientation of opinions expressed in text materials and generally categorizes the expressed opinion in the binary

# ACCEPTED MANUSCRIPT

distinction of positive vs. negative [70]. Such sentiment analysis would properly inform the construction of our design artifact that aims to automatically detect counterfeit products based on consumers’ textbased product reviews. Sentiment analysis techniques can be largely categorized into two approaches [85]. First, the statistical or machine learning approach is a supervised approach that builds classifiers based on labeled instances of texts or sentences [71]. As a supervised method, the machine learning approaches perform well if large labeled instances are available for training and validating classifiers [77]. Further, when working with dynamic content, such as online consumer reviews, the amount of time required to both update the training set and retrain the classifiers could be considerable [77]. Second, the lexicon-based sentiment approach identifies the orientation for a document based on the semantic orientation of words or phrases in the document [88]. Specifically, the lexicon-based approaches use dictionaries of words annotated with the polarity (positive vs. negative) of each word and its strength. The dictionaries for lexicon-based approaches can be constructed manually or start with a small number of seed words that automatically extend the list of words [85]. Further, lexicon-based approaches focus on using adjectives as indicators of the semantic polarity of text [85]. In determining the sentiment of any given text, all adjectives are extracted and annotated with their semantic orientation scores. These scores are then aggregated into a single value to indicate the semantic orientation of the given text [85]. Such lexicon-based approaches outperform statistical or machine learning approaches when a training data set is not substantially large enough to ―accumulate the necessary feature frequency information‖ [92] (p.275). Considering its effectiveness and efficiency, we adopt lexicon-based sentiment analysis approaches as the underlying theory for this study and follow their guidelines for our design process.

## 4.3 Consumer Behavior and Testable Hypotheses

Our proposed design artifact, OnCDS, is novel; thus, no prior literature informs the selection of outcomes of interest in measuring its utility. As part of our effort to strengthen the relevancy of our study, we conduct extensive literature review in the fields of consumer behavior as well as information systems. Among the many relevant constructs in literature, we find that consumer attitude is the most appropriate construct for our study. Drawing upon the theory of reasoned action (TRA) [28], the theory of planned

behavior (TPB) [1], and the technology acceptance model (TAM) [21], many researchers study the factors affecting attitude and its impact on intention to purchase [13, 24, 49, 56]. Another stream of research also focuses on the attitude construct. One such example is from Shih [83] where TAM was extended via replacing behavioral intention with attitude and adding perceived performance and relevance. Furthering the importance of attitude, Van der Heijden, Verhagen and Creemers [90] combine constructs from TPB of attitude in consumer behavior, we select OnCDS’ impact on consumer purchase attitude as the outcome of interest for our design and measure it as the utility of our design artifact.

Literature on consumer attitude and the valence framework [76] provide the theoretical foundations for investing consumer purchase attitude in this study. The valence framework [76] explains that consumers consider both positive and negative aspects of behavioral beliefs. Accordingly, consumers make decisions to maximize the net valence resulting from perceived risks and perceived benefits of adoption behavior. Kim, Ferrin and Rao [52] use the valence framework as a theoretical lens to explain consumer online shopping behavior. Based on the valence framework, Lu, Cao, Wang and Yang [58] report that the online banking adoption is influenced by both positive and negative behavioral beliefs. Yang, Lu, Gupta, Cao and Zhang [95] also confirm that the valence framework is an appropriate model to explain mobile commerce adoption behavior. Further, Kim, Ferrin and Rao [52] adapt the valence framework to include trust and the role of trust and risk on purchase intentions. Gefen, Karahanna and Straub [31] examine a myriad of trust conceptualizations and learn that trust is as important as TAM constructs in predicting behavioral intention. Similarly, TPB augmented by trust is explored by George [33], where trust plays a role in predicting online purchase behavior. In a similar light, within TPB, trust is shown to affect both behavioral control and attitude [73].

Drawing on the valence framework [76], we develop the research model for this study, as shown in Figure 1. The valence framework posits that consumers see a product as having both positive and negative attributes and decisions maximize net valence [76] (p 238). Our model is designed to be highly generalizable and is based on this concept of positive and negative attributes. In the context of detecting counterfeit products, we argue that the trustworthiness of a product is a positive attribute, the perceived risk of a product is a negative attribute, and these two factors would affect the attitude of a consumer who wants to maximize net valence. Advancing our model, we posit that counterfeit scores would affect customer attitude toward purchasing products through trust and perceived risks. Mayer, Davis and Schoorman [62] define trust as the willingness of a party to be vulnerable to the actions of another party based on the expectation that the other party will perform the action. One construct that many previous research presented as an important antecedent of trust is information quality. Consumer affected by other people's opinions when purchasing products; thus, they tend to depend on information from word-of-mouth communication [38]. Therefore, the information content in electronic word of mouth (eWOM) communication is regarded as a sign that assists consumers in making purchase decisions [69]. The empirical study conducted by Nicolaou and McKnight [65] finds that perceived information quality is a factor affecting trust belief. Eid [25] also reports that the quality of information about products that are provided by a website has a positive effect on consumer trust. Similarly, Kim, Xu and Koh [54] examine the relationship between the information quality on a website and trust. Further, Pan and Chiou [69] argue that the type of information regarding products influences consumer trust behavior. Important dimensions of information quality are relevance and usefulness [23]. Counterfeit scores will be quite relevant and useful to have when making purchase decisions. So, we argue that a counterfeit score on a product likely influences a consumer’s trust in the product. Consumers are likely to lose trust in products that are not authentic since counterfeit products have a reputation of being inferior. Based on this discussion, we posit:

$\mathbf { H } _ { 1 } \mathbf { \cdot }$ The counterfeit score has a negative effect on the trust in the product.

Perceived risk is the degree to which a consumer perceives a negative outcome [27]. Kim, Ferrin and Rao [52] show that information quality is an antecedent of perceived risk. The study by Ha [38] reports that positive eWOM can decrease perceived risks for brand purchases by consumers. Similarly, Nicolaou and McKnight [65] also report that perceived information quality influences perceived risks. Berthon, Hulbert and Pitt [11] argue that assurance of a product’s quality reduces perceived risks. Our

# ACCEPTED MANUSCRIPT

counterfeit score is an indicator of product quality, likely influencing perceived risks. Further, Featherman and Pavlou [27] identify financial risk as one dimension of perceived risks. A counterfeit score indicates the likelihood of a product being inauthentic. An inauthentic product likely carries a financial risk, and our counterfeit score, which alerts a consumer to this risk, will be very useful to prevent this. Considering empirical evidence for information quality being a factor affecting perceived risks and our counterfeit rfeit scores would likely affect the risk on a product perceived by a consumer. We posit that the higher a counterfeit score, the higher the perceived risk of a product. Based on this discussion, we hypothesize:

$\mathbf { H } _ { 2 } \colon$ The counterfeit score has a positive effect on perceived risks of purchasing a product.

Trust has been linked to intent to purchase and attitudinal loyalty [47]. A higher degree of trust improves willingness to participate in e-commerce transactions [20]. A consumer’s reluctance to purchase is oftentimes attributed to a lack of trust in online merchants or markets. Consumers will only engage in an e-commerce transaction if the level of trust in the seller xceeds a personal trust threshold [87]. Increasing trust can facilitate online purchases by overcoming perceptions of risk and uncertainty and spawned research into Trust Building Models [43]. While behavioral intention is the final construct in TPB, oftentimes research seeks to identify the constructs affecting intention. Wu and Chen [94] combine TAM and TPB via augmenting PU and PEOU with trust to influence attitude. Trust is also shown to reduce perceived risk [72] and thereby increases intent to purchase. Additionally, the study done by Gefen, Rao and Tractinsky [32] demonstrates trust’s effects on intent to purchase. Grazioli and Jarvenpaa [34] also report that trust affects attitude towards shopping at an online store, which in turn influences the actual purchase, demonstrating the importance of the attitude construct. Also focusing on the attitude construct, Chakraborty, Lee, Bagchi-Sen, Upadhyaya and Rao [16] found trusting belief had a positive effect on e-commerce attitude. Based on this discussion, we propose:

$\mathbf { H } _ { 3 } { \mathrm { : } }$ Trust has a positive effect on a consumer’s attitude toward purchasing a product.

Many prior studies have provided empirical evidence for the negative effect of perceived risks on a consumer’s willingness to conduct transactions on the Web [63]. Kim, Ferrin and Rao [52] demonstrate that perceived risk, trust, and perceived benefit have an effect on behavioral intention to purchase. Similarly, Kim and Kim [55] show that perceived risk affects purchase intention, and consumer trust affects both perceived risk and purchase intention. The study done by Pavlou and Fygenson [73] also reports that product value positively influences attitude toward product purchasing from a Web vendor. This indicates that the perceived high-risk product would not have high value, negatively affecting consumer purchase attitude. Further, Jarvenpaa, Tractinsky and Saarinen [50] and Jarvenpaa, Tractinsky and Vitale [51] show that perceived risk has a negative effect on attitude. The work of Grazioli and Jarvenpaa [34] reports that perceived risk affects attitude towards shopping at an online store, which in turn influences the actual purchase. Additionally, Leonard [57] focuses on predictors of attitude from both the perspective of the buyer and seller and reports perceived risk as a predictor of attitude toward purchasing or selling. Moreover, Chakraborty, Lee, Bagchi-Sen, Upadhyaya and Rao [16] find perceived risks have a negative effect on attitude toward e-commerce. Based on this, we posit:

H<sub>4</sub>: Perceived risk has a negative effect on a consumer’s attitude toward purchasing a product.

![](/api/attachments/YM34F7GP/fulltext/images/44a13fa8cf7fce5f2294c948d530bc5db74550685b39b8730200f0a88a7f3145.jpg)  
Figure 1: Behavioral Research Model

## 5 Design Artifact – Automatic Counterfeit Detection Framework: OnCDS

From lexicon-based semantic analysis approaches, we develop our design artifact, called Online Counterfeit Detection Score (OnCDS). Figure 2 shows the architecture of our OnCDS, which consists of five components: Web Crawler, Text Corpus Preparation, Natural Language Processing, Indexing and Topic Analysis, and Ranking System and Calculation. Equipped with these components, OnCDS processes customer reviews from an online marketplace and automatically assigns a score to a product, indicating the likelihood that the product is counterfeit. As the consumer browses the online marketplace, a browser add-on facilitates communicating with the online marketplace, and OnCDS ultimately returns a

# ACCEPTED MANUSCRIPT

counterfeit score to the consumer. OnCDS is a robust, complex, and sophisticated system for calculating counterfeit scores; thus, we adopt a component-based, modular design to facilitate easy upgrading and expanding components. The components are currently developed on the Chrome Browser and Amazon marketplace; however, the modular design facilitates expanding to other marketplaces or supporting additional web browsers. Similar extensions could be developed for Firefox or other marketplaces, such as eBay, and could be adapted by altering the appropriate component. Additionally, improvement of the counterfeit lexicon, modifications to the natural language processing, or modification of the scoring mechanism is possible. Following is a detailed description of each component.

![](/api/attachments/YM34F7GP/fulltext/images/e575b3f920fea46314cfb734e0aa8e244a5455fb6d7d08c5ea9ea49087c69e59.jpg)  
Figure 2 –OnCDS System Architecture

## 5.1 Component: Web Scraper and Text Corpus Preparation

Written as a browser extension, the Web Scraper component performs the multi-step process using bootstrap, jQuery, and java script. The first step is to extract the URL into a string value for parsing. The current URL in the browser is then parsed to locate and extract the product identifier for further

operations. The product identifier is used to generate a new HTTP request, and the HTTP request for the product reviews is sent to the online marketplace webserver. The returned HTML response contains all the reviews for the product. Our method iteratively retrieves each review in the response, and each review is formatted as plain text to prepare it for the Text Corpus Preparation component. While this work currently uses the web scraper in Chrome, the method could be adapted to work with any browser since it is developed using standard Java Script and operates on URLs, as opposed to a specific API. The formatted reviews are then transmitted to the Text Corpus Preparation Component. t Corpus Preparation component accepts text from the Web Scraper. The document is pars a separate document for each of the top 10 reviews received. The separation of reviews from a single text document into a corpus of documents is required for further processing of OnCDS where calculations are based on a document count.

## 5.2 Component: Natural Language Processing

OnCDS uses the Natural Language Processing component to parse the customer reviews as informed by lexicon-based sentiment analysis. The parsed sentences are then tokenized into words. Nouns and verbs are identified as part of the tokenization cess. The component then compares the tokenized words with an imported list of English language stop words to improve the counterfeit score calculation. The English language is crowded with words that do not provide context or value to one’s understanding. Stop words have very little meaning in the context of a sentence. In Natural Language Processing (NLP), stop words are commonly removed before processing [79]. Common stop words include ―the,‖ ―about,‖ and ―of.‖ The occurrence of stop words is usually greater than other more substantial and meaningful words. In a customer review document, OnCDS performs calculations based on the occurrence of words; therefore, removing stop words aids in the accuracy of the calculation. In addition to accuracy, efficiency is improved by reducing the amount of words that must be processed in subsequent components. Once stop words are removed, the remaining text is written. This is repeated for each customer review. Once completed, the corpus remains in the original form but without the stop words. The processed corpus is transmitted to the Indexing and Topic Analysis component. While other dimensions of information are

available, such as seller and product ratings, OnCDS focuses solely on counterfeit product detection and does not seek to replace current product and seller ratings. A negatively reviewed seller may be selling authentic products and, similarly, a negatively reviewed product may be authentic. OnCDS adds another dimension of information, a counterfeit score, to augment the available ratings metrics by detecting a product’s authenticity to support the consumer’s decision making process.

## 5.3 Component: Indexing and Topic Analysis

Our kernel theory, TF-IDF, guides us to employing document and term frequencies in a custom calculation for our counterfeit score. Drawing on the process of TF-IDF, Indexing and Topic analysis begins by creating a searchable index based on the pre-processed document corpus from the NLP component. Input to the component is a document corpus of processed reviews. First, each document is read into the system and all text is parsed. An index of documents and the terms contained in each document is generated. The index is searchable and can be used to count how frequently a term occurs in a document or over the entire corpus. Second, the index wi l be searched for terms that indicate inauthentic products by way of a synonym relationship to ―counterfeit‖ or ―fake.‖ The system examines each work and determines if it is a synonym, and, if so, implements a counter mechanism. Third, all terms are ranked, counted, and their document frequency recorded. The rankings, document frequency, and count are passed to the Ranking System and Calculation component for generating the counterfeit score.

## 5.4 Component: Ranking System and Calculation

The core of OnCDS lies with its method to calculate a counterfeit score based on the processed customer reviews and output from Indexing and Topic Analysis. Based on the component approach, the calculation of the score can be improved or altered when necessary without affecting system operations. The online marketplace maintains customer reviews to prevent a customer from submitting multiple reviews or a single review from being overly negative. The calculation, as described, relies on the online merchant to perform basic diligence in maintaining reviews to prevent a reviewer from gaming the system to either improve or negatively impact the score. In the event that these conditions are not met, the

component can be altered with additional intelligence to combat a single reviewer from manipulating the score. Our calculations are borrowed from information processing techniques, such as TFIDF, where we count term frequencies and document frequencies [79].

Let ontology WNO = the WordNet ontology and set S = the set of all synonyms of the term ―counterfeit‖ extracted from the WordNet ontology [68] such that $\mathsf { S } \subset \mathsf { W N O }$ and $\mathsf { S } = \{ \mathsf { S } 1 , \mathsf { S } 2 , . . . , \mathsf { S } \mathsf { n } \}$

Equation1: Counting the document frequency over the corpus

$$
\sum_ {i = 1} ^ {\text {numDocs}} \text {DocFrequency} (S _ {i})
$$

Equation 2: Counting the total number of counterfeit terms over the corpus

$$
\sum_ {i = 1} ^ {\text { numDocs }} \text { Occurance } (S _ {i})
$$

Equation 3 calculates the score based on equations 1 and 2, as well as the total number of documents. Equations 1 and 2 are denoted as X and Y, respectively. The common logarithm is employed as a log transformation to reduce the skewedness of data [26]. Further, the log transformation method is useful in normalizing the scores and scale.

Equation 3: Calculating counterfeit score

(( )⁄ )

Equation 4 translates the score to a percentage. The score indicates the likelihood that a product is counterfeit with 0 (0%) being the lowest likelihood that a product is counterfeit and 10 (100%) the highest likelihood that a product is counterfeit.

Equation 4: Converting counterfeit score to a 10 point scale

$$
\log ((x * y) / \text {numDocs}) * 1 0 0
$$

Finally, the Ranking System and Calculation component submits a counterfeit score to the Web Scraper component to be displayed for the consumer.

Figure 3 shows sample consumer reviews taken from an online merchant, which indicates that a product may be inauthentic. Using the aforementioned method, the counterfeit score is calculated. Figure 4 shows how our counterfeit score may be displayed along the product description on Amazon.com. The counterfeit score on Figure 4 is displayed on a 10-point scale with a color bar which progresses from green to red as the score increases: a 9.5 (out of 10) counterfeit score and the color bar showing the likelihood of a product being counterfeit.

![](/api/attachments/YM34F7GP/fulltext/images/2e65d257b3d61259a6353971ee23211e51d7b28f6b40315eb1dd6aee8b668086.jpg)  
Figure 3: Sample Reviews of a Suspicious Product

![](/api/attachments/YM34F7GP/fulltext/images/3340b193537d1ab8bce98012b52e0b5b194647aefe628fd57a014710c6b68a3e.jpg)  
Figure 4: Sample Counterfeit Score Display

# ACCEPTED MANUSCRIPT

## 5.5 Instance Development

OnCDS is flexible enough to permit a myriad of potential implementations. We recommend that the browser plug-in/extension be developed for a well-adopted web browser, such as Chrome or Firefox, which supports customization via extensions. Similarly, to increase the adoption of OnCDS it should be developed for marketplaces that are commonly accepted and have customer reviews such as Amazon or eBay. The detailed implementation depends on the marketplace chosen and the quality and availability of customer reviews. Additional NLP or altering of the counterfeit score calculation may be required based on the quality and availability of reviews. OnCDS facilitates this via a component-based architecture so that each component is independent and can be customized. Java provides the most flexibility with a plethora of libraries available to alleviate detailed development of natural language processing or an indexing system. OnCDS could be developed in any language that has libraries for NLP and Apache Lucene. Finally, we recommend employing a cloud-based hosting service such as Heroku, Amazon Web Services, or Microsoft Azure.

Our current implementation of OnCDS begins with a Chrome add-on for the Web Scraper component. The Chrome add-on employs Bootstrap, CSS, and HTML provide the basic development their Chrome web browser. Next, the users navigate to the Amazon.com product page for which they want to view the counterfeit score. Then, they activate the add-on by clicking on its icon within Chrome. The Web Scraper parses the URL in the address bar and extracts the product identifier, also known as the Amazon Standard Identification Number (ASIN). The Web Scraper generates an HTML request using JavaScript, retrieves the product reviews from Amazon, and transmits it to the core of OnCDS, which is written in Java and can be hosted on any Java Enabled service (e.g. Heroku). Each review is parsed into a separate text file that is advanced to the next stage of natural language processing.

The Natural Language Processing component employs Open-NLP from the Apache Foundation [4]. The Indexing and Topic Analysis component is built on top of the Apache Lucene project [44] and coded in Java. Lucene version 4 is utilized in the implementation of OnCDS. The corpus of text

documents, which have been processed and prepared in the previous steps, serves as the input. The corpus is read into Lucene where an index is constructed. From the index, all terms are ranked, counted, and their document frequency is recorded. The rankings, document frequency, and count serve as input to the Ranking System and Calculation.

The Ranking System and Calculation, like its counterparts, is coded in Java. The rankings, count, and document frequency are all input into Equations 1-4, and the counterfeit score is generated. The counterfeit terms are those that are counted and employed as input. Once the calculations are complete, the results are returned to the Web Scraper component, a Chrome add-on, which displays the counterfeit score to the consumer, as presented in Figure 4.

## 5.6 Instance Validation

Similar to the evaluation in Taboada, Brooke, Tofiloski, Voll and Stede [85], our work employs human subjects recruited from Amazon Mechanical Turk in validating our artifact. A survey was administered with 51 respondents. The demographic information is displayed in Table 2.

<table><tr><td colspan="2">Age</td></tr><tr><td>8%</td><td>18-24</td></tr><tr><td>40%</td><td>25-34</td></tr><tr><td>30%</td><td>35-44</td></tr><tr><td>15%</td><td>45-54</td></tr><tr><td>8%</td><td>55-64</td></tr></table>

<table><tr><td colspan="2">Education</td></tr><tr><td>1%</td><td>&lt; High School</td></tr><tr><td>10%</td><td>High School</td></tr><tr><td>25%</td><td>Some College</td></tr><tr><td>14%</td><td>2 Year Degree</td></tr><tr><td>42%</td><td>4 Year Degree</td></tr><tr><td>7%</td><td>Professional Degree</td></tr></table>

<table><tr><td colspan="2">Marital Status</td></tr><tr><td>43%</td><td>Married/ Live Together</td></tr><tr><td>2%</td><td>Widowed</td></tr><tr><td>9%</td><td>Divorced</td></tr><tr><td>1%</td><td>Separated</td></tr><tr><td>44%</td><td>Never Married</td></tr></table>

<table><tr><td colspan="2">Job Field</td></tr><tr><td>6%</td><td>Homemaker</td></tr><tr><td>29%</td><td>Computing/ IT</td></tr><tr><td>24%</td><td>Business/ Finance</td></tr><tr><td>3%</td><td>Engineering</td></tr><tr><td>5%</td><td>Health/ Medical</td></tr><tr><td>6%</td><td>Student</td></tr><tr><td>3%</td><td>Disabled</td></tr><tr><td>25%</td><td>Other</td></tr></table>

<table><tr><td colspan="2">Race</td></tr><tr><td>82%</td><td>Caucasian</td></tr><tr><td>5%</td><td>African American</td></tr><tr><td>9%</td><td>Asian</td></tr><tr><td>4%</td><td>Other</td></tr></table>

<table><tr><td colspan="2">Gender</td></tr><tr><td>50%</td><td>Male</td></tr><tr><td>50%</td><td>Female</td></tr></table>

Table 2: Demographic Information of Study Participants

# ACCEPTED MANUSCRIPT

To rigorously validate the efficacy of our design artifact, we employed human subjects and sentiment analysis. First, human subject survey respondents were asked to view a product and read the exact same product reviews that were processed by OnCDS, which are similar to the ones in Figure 3. They were then presented with a counterfeit score on a 10-point scale and a green-to-red colored bar, as shown in Figure 4. They were asked to choose, on a 5-point scale, their agreement level with OnCDS’ counterfeit rating based on consumer product reviews. The respondents could choose strongly agree (5) through strongly disagree (1), indicating the level of their agreement with the OnCDS score. Results of the counterfeit score validation are presented in Table 3.1. The means for all three products are 4.55, 4.71, and 4.47 on a 5-point Likert scale, which are very high. Further, 49 out of 51 survey participants (96%) agreed with our counterfeit scores for all three products.

In the second phase of instance validation, we compared the results of the OnCDS calculation with sentiment analysis techniques. While negative or positive sentiment does not indicate a counterfeit or authentic product respectively, a counterfeit product will likely have a negative sentiment. We employed sentiment analysis via Python and NTLK and verified the sentiment from an online source (sentiment.vivekn.com). In all tested cases, negative sentiment corresponded with a high counterfeit score and vice-versa as demonstrated in Table 3.2. OnCDS does not aim to test for negative or poor-quality products, but detects counterfeit products as its name implies.

The results of our two-phase validations clearly indicate that OnCDS is able of automatically quantifying the likelihood of a product being counterfeit from text-based product reviews, confirming the achievement of our design’s intended outcome. Having validated OnCDS, we proceeded to examine the effect of our proposed design artifact on a consumer’s attitude when purchasing a product.

<table><tr><td></td><td>Product 1</td><td>Product 2</td><td>Product 3</td></tr><tr><td>Mean</td><td>4.55</td><td>4.71</td><td>4.47</td></tr><tr><td>Standard Deviation</td><td>0.73</td><td>0.54</td><td>0.73</td></tr><tr><td>Agree + Strongly Agree</td><td>49</td><td>49</td><td>49</td></tr><tr><td>Percentage of Agree + Strongly Agree</td><td>96%</td><td>96%</td><td>96%</td></tr></table>

Table 3.1: Results from Counterfeit Score Validation

<table><tr><td rowspan="2"></td><td colspan="2">Subjectivity</td><td colspan="2">Polarity</td><td colspan="2">Results</td></tr><tr><td>Positive</td><td>Negative</td><td>Positive</td><td>Negative</td><td>Sentiment</td><td>Counterfeit Score</td></tr><tr><td>Product 1</td><td>0.2</td><td>0.8</td><td>0.2</td><td>0.8</td><td>Negative</td><td>9.5</td></tr><tr><td>Product 2</td><td>0.2</td><td>0.8</td><td>0.2</td><td>0.8</td><td>Negative</td><td>8.7</td></tr><tr><td>Product 3</td><td>0.2</td><td>0.8</td><td>0.5</td><td>0.5</td><td>Positive</td><td>0</td></tr></table>

Table 3.2 – Sentiment Analysis compared to Counterfeit Score of Surveyed Products

## 6 Behavioral Research Method and Results

## 6.1 Operationalization of Constructs

This study adapts instruments that were validated in previous studies to test the hypotheses presented in Section 4.3. All latent constructs in this study use multi-items measured using 7-point Likert scales anchored at 1 for ―strongly disagree‖ to 7 for ―strongly agree.‖ Table 4 presents the operationalization of the constructs. An underlying assumption for SEM is reflexive constructs [17]; however, the partial least squares approach to SEM can model formative indicators [18]. Trust and attitude are considered reflexive constructs with perceived risk as a formative construct as adapted from [52] and [53].

<table><tr><td>Construct</td><td>Measurement Item</td><td>Adapted from</td></tr><tr><td>Perceived Risk</td><td>It is likely that this product would not be of value for money.It is likely that purchasing this product would involve more financial risk (i.e. fraud) when compared with other products.Please rate your overall perception of risk from purchasing this product.</td><td>[86] and [52]</td></tr><tr><td>Trust</td><td>This product is trustworthy.This product gives the impression that it keeps promises and commitments.I believe that this product has my best interests in mind.</td><td>[52]</td></tr><tr><td>Attitude toward product purchase</td><td>For me, purchasing this product would be a good idea.For me, purchasing this product would be very desirable.Buying this product would be a pleasant or a wise idea.</td><td>[73] and [33]</td></tr></table>

Table 4: Operationalization of Constructs

## 6.2 Data Collection

Surveys were administered using the Qualtrics online survey platform. Respondents were recruited via the Amazon Mechanical Turk Human Intelligence Platform. Respondents first answered basic demographic questions; Table 5 presents the demographic information of the respondents. Next,

# ACCEPTED MANUSCRIPT

participants viewed multiple products with a range of counterfeit scores, as shown in Figure 4. Each product was accompanied by an image, similar to Figure 4, with its counterfeit score. Participants responded to the questions in Table 4 for each product, rendering 200 data observations covering 3 products with counterfeit scores ranging from 0 to 9.5. All data was downloaded in CSV form and imported to SPSS to test for outliers. Outliers were removed via Mahalanobis Distance [22]. Mahalanobis Distance was calculated via linear regression and saved as a new variable (MAHALANOBIS\_DISTANCE). Next, the Chi Square function was utilized to determine the significance (P value) of the Mahalanobis distance via the SPSS formula: 1-CDF.ChiSQ (MAHALANOBIS\_DISTANCE, Degrees of Freedom). Instances with a p < .001 are considered significant and outliers. These 30 records were removed, leaving 282 data observations.

![](/api/attachments/YM34F7GP/fulltext/images/f0383f3883141ae258b656dbd9663a371d663cfa7345c87cd932489c13bbf8fe.jpg)  
Table 5: Demographic Information of Study Participants

## 6.3 Data Analysis and Results

Structural equation modeling (SEM), which is considered a second-generation multivariate technique, is employed for testing our research model. Two types of SEM commonly employed are covariance-based SEM and partial least squares (PLS). Covariance-based SEM is primarily a

confirmatory technique whereas PLS-SEM is best suited for exploratory research [41]; therefore, this research employs PLS based structural equation modeling. All measured variables comprised their latent variables via a reflexive measurement model with the entire model being a reflexive-formative type model. Data analysis was performed using partial least squares (PLS) via the SMART-PLS software.

## 6.3.1 Measurement Model

Before testing the structure model, we evaluate the measurement model. The first step examines all loadings and states, per Hair Jr, Hult, Ringle and Sarstedt [41] (p 105), that an indicator’s outer loading should be greater than its loading on all other constructs. Table 6 shows the outer loadings of the measured variables onto the latent constructs. Each measured variable loads highest on its latent construct, thereby demonstrating discriminate validity. Since this method is considered a liberal approach to discriminate validity [40], we advance to a more conservative approach to assess discriminate validity, the Fornell-Larcker criterion [41]. The Fornell-Larcker criterion [29] compares the square root of each latent construct’s AVE (average variance explained) with the latent variable correlations and states that the square root of the AVE should be greater than the correlation with any other construct. Table 7 shows the results of the Fornell-Larcker criterion with the square root of AVE in bold. It is noted that the square root of each latent construct’s AVE is greater than its correlation with other latent constructs, thereby meeting the required criterion. The data meets both requirements of discriminate validity. Reliability was measured using Cronbach’s Alpha and composite reliability. All Cronbach’s Alpha and composite reliability scores exceeded the minimum cutoff of 0.70, as shown in Table 8 [10]. Similarly, all constructs had an AVE exceeding 0.5, indicating adequate internal consistency [29].

<table><tr><td colspan="3">Outer Loadings</td></tr><tr><td>Construct</td><td>Indicator</td><td>Loading</td></tr><tr><td rowspan="3">Attitude</td><td>A1</td><td>0.956</td></tr><tr><td>A2</td><td>0.958</td></tr><tr><td>A3</td><td>0.963</td></tr><tr><td rowspan="3">Perceived Risks</td><td>PR1</td><td>0.800</td></tr><tr><td>PR2</td><td>0.932</td></tr><tr><td>PR3</td><td>0.983</td></tr></table>

<table><tr><td colspan="4">Fornell-Larker Criterion</td></tr><tr><td></td><td>A</td><td>PR</td><td>T</td></tr><tr><td>A</td><td>0.959</td><td></td><td></td></tr><tr><td>PR</td><td>-0.669</td><td>NA*</td><td></td></tr><tr><td>T</td><td>0.893</td><td>-0.647</td><td>0.940</td></tr><tr><td colspan="4">*Bold = square root of AVE* Remaining are latent variable correlations</td></tr></table>

<table><tr><td rowspan="3" colspan="2">Trust</td><td>T1</td><td>0.949</td><td rowspan="3"></td><td rowspan="3" colspan="2">*NA—Does not apply for the formative measures</td></tr><tr><td>T2</td><td>0.950</td></tr><tr><td>T2</td><td>0.922</td></tr><tr><td colspan="7">Table 6: Factor and Outer Loadings</td></tr><tr><td rowspan="4"></td><td></td><td>Cronbach&#x27;s Alpha</td><td colspan="2">rho_A</td><td>Composite Reliability</td><td>AVE</td></tr><tr><td>A</td><td>0.957</td><td colspan="2">0.957</td><td>0.972</td><td>0.920</td></tr><tr><td>PR*</td><td>NA</td><td colspan="2">NA</td><td>NA</td><td>NA</td></tr><tr><td>T</td><td>0.935</td><td colspan="2">0.937</td><td>0.958</td><td>0.884</td></tr><tr><td colspan="7">Table 8: Reliability of Constructs* indicates formative measurement* The internal consistency is not applicable to formative items since they need not covary [17].</td></tr></table>

## 6.3.2 Structural Model

Figure 5 shows the results of PLS-SEM. The coefficient of determination, or $\mathbf { R } ^ { 2 } ,$ is a measure of the predictive accuracy of a model. Values of $\mathbf { R } ^ { 2 }$ exceeding 0.75 are considered substantial, 0.50 are moderate, and 0.25 is considered weak [40]. $\mathsf { R } ^ { 2 }$ values for attitude, perceived risk, and trust are 0.81, 0.64, and 0.63, respectively, indicating substantial to moderate predictability.

![](/api/attachments/YM34F7GP/fulltext/images/57ceb9577369960bcfa92255f8d6998b5a57e5f3113f7f6c68f44cd20336f2b8.jpg)  
Figure 5: Results of Partial Least Squares Structural Equation Model

Testing hypotheses in PLS-SEM requires a bootstrapping technique that draws random samples with replacement to estimate the path model multiple times. Per recommendations, results are based on a bootstrapping of 5000 samples [41]. In H1, we argued that the counterfeit score has a negative effect on the trust in the product. Our study results provide strong support for this assertion; the path coefficient is -0.795 and $\mathrm { p } < 0 . 0 0 1$ . H2 states that the counterfeit score has a positive effect on the perceived risks of purchasing a product. The path coefficient is 0.801 and $\mathrm { p } < 0 . 0 0 1$ , indicating that the score influences perceived risks of purchasing a product, strongly supporting hypothesis 2. In H3, we proposed that trust has a positive effect on a consumer’s attitude toward purchasing a product. The study results provide strong empirical support for this hypothesis since the path coefficient is 0.792 and $\mathrm { p } < 0 . 0 0 1$ . H4 states that perceived risk has a negative effect on a consumer’s attitude toward purchasing a product. The study results support this assertion; path coefficient is -0.156 and $\mathrm { p } < 0 . 0 5$ . In conclusion, the results support all hypotheses postulated in this study.

<table><tr><td>Hypothesis</td><td>Original Sample</td><td>Sample Mean</td><td>Standard Deviation</td><td>T Statistics</td><td>P Values</td><td>Significance</td></tr><tr><td>H1: Score -&gt; T</td><td>-0.795</td><td>-0.796</td><td>0.038</td><td>20.913</td><td>0.000</td><td>***0.001</td></tr><tr><td>H2: Score -&gt; PR</td><td>0.801</td><td>0.806</td><td>0.042</td><td>19.243</td><td>0.000</td><td>***0.001</td></tr><tr><td>H3: T -&gt; A</td><td>0.792</td><td>0.791</td><td>0.054</td><td>14.619</td><td>0.000</td><td>***0.001</td></tr><tr><td>H4: PR -&gt; A</td><td>-0.156</td><td>-0.157</td><td>0.064</td><td>2.437</td><td>-0.0156</td><td>**0.050</td></tr></table>

Table 8: Hypotheses Testing Results. Note: <sup>\*\*\*</sup>p<0.001; <sup>\*\*</sup>p<0.05.

## 7 Discussion and Conclusions

While design and behavioral science are often viewed as distinct research paradigms, researchers should consider them complimentary and draw upon the strengths of both. Few researchers have attempted to unite these research paradigms, thereby leaving a gap in the current literature. To fill this and behavioral science by first drawing upon the duality and developing a theoretical framework with a testable hypothesis based on the valence framework. Next, we advance to presenting OnCDS, a situated design artifact following the principles of design science and based on kernel theory. Following presentation of OnCDS, we present our behavioral research method and results of our structural equation model demonstrating its effect on a consumer’s attitude toward purchasing a product.

OnCDS is designed to support the consumer’s decision-making process via influencing net valence as attitude through a positive attribute, trust, and a negative attribute, perceived risk. The proliferation of deceptive counterfeit goods via online marketplaces, such as Amazon and eBay, has introduced a particularly burdensome decision-making process for consumers. The consumers need to spend more time in the information search step, reading product and seller reviews to determine the product’s authenticity. The decision process involved in detecting counterfeit products is lengthy and complex. Assisting online consumers in this process is the objective of this study. While current measures exist, namely product and seller reviews, they do not account for a product’s authenticity as an authentic product may have negative reviews and a seller selling authentic goods may have a negative rating. We identified a need for an additional dimension to support the consumer’s decision-making process and created a process to automatically detect counterfeit products in the online marketplace. In achieving our objective, we have made significant contributions to advancing IS literature.

Theoretical implications of this work are threefold. The first contribution is a situated design science artifact, called OnCDS, drawn on solid theoretical foundations. Gregor and Hevner [35] state the three levels of design science contributions. In this work, the first contribution level of design science, a novel artifact as a situated implementation, is realized with OnCDS. It uses web scraping, natural language processing, and topic analysis to process customer reviews from an online marketplace and calculates a counterfeit score based on customer feedback. We present a detailed method on how these approaches can be utilized to calculate the likelihood of a product being counterfeit. Further, the development of the artifact follows a component-based modular design, facilitating easy changes for components, without affecting system operations, as well as easy extensions for incorporating new browsers and methods. This study evaluates the performance of OnCDS with human subjects. Our validation results show that OnCDS is capable of automatically processing text-based online product reviews and calculating the counterfeit score of a product.

The second contribution of this work is the development of a behavioral research model, which extends classic information systems theory in the context of counterfeit products on online shopping. Drawn on the valence framework, we adapted trust, perceived risk, and attitude constructs into our model. The results of our testing demonstrate that displaying a counterfeit score in an online marketplace affects perceived risk and trust, which in turn impact the attitude construct. Empirical evidence of our design artifact affecting attitude towards purchase clearly show that our design successfully obtains the outcome of interest.

The third contribution of this work is bridging the gap between design science and behavioral research by empirically testing the outcome of our proposed design artifact with human subjects. The problem addressed is to aid customers in determining the authenticity of a product in an online marketplace. In doing so, this work articulates how the research methods and guidelines of both design science and behavioral research can be united for the development of a design artifact and the rigorous evaluation of its utility.

Following Baskerville, Kaul and Storey [7], we demonstrate knowledge moments following the genres of inquiry. First, nomothetic science may result when requirements of an artifact or its behaviors are studied. In this work, a theoretical behavioral model is studied to examine the resulting behaviors from a design artifact. Second, idiographic design is one of the most common forms of design science and is frequently in the form of an instantiation of an artifact, which is realized via our presented design artifact and subsequent validation. The nature of idiographic knowledge states that the design artifact is the mechanism by which behavior is studied. Our design artifact is applied to classic behavioral research to test a developed theory, thereby satisfying the third genre of inquiry of designs science. The final genre of inquiry, nomothetic design will be addressed in future research and is a limitation of this work.

Implications for practice include supporting a consumer’s decision process via alleviating the issue of determining a product’s authenticity. Online marketplaces have long employed trust seals and other mechanisms to improve consumer confidence in the marketplace. This research has illustrated yet another dimension to influencing consumer trust in products via implementing an automated counterfeit score. Practitioners can expand upon or further refine the counterfeit score calculation to improve accuracy or adaptation into their online marketplace or website. Furthermore, understanding how perceived risk and trust can influence a consumer’s attitude toward a purchase can aid in improving sales and overall perceptions of an online marketplace or website.

Limitations of our artifact are that a malicious or disgruntled customer could influence the score via inserting keywords into their review. While the document frequency and the online marketplace’s publication of customer reviews mitigate this concern to some extent, a more through mechanism for

# ACCEPTED MANUSCRIPT

dealing with score manipulation would be useful. Furthermore, we rely on the online marketplace to accurately provide top reviews; however, OnCDS should be expanded to include additional positive and negative reviews. OnCDS was validated with human subjects using a few products, which may not fully account for the large variety of different product characteristics and reviews. Our future work, advancing to level 2 of design science research encompassing design theory, will include an extensive validation of OnCDS with a large number of both authentic and counterfeit products to more rigorously assess its performance. From a behavioral perspective, our proposed theoretical model is general in nature. Further refinement of the model and determining the composition of the latent exogenous and endogenous constructs would be helpful to better understand supporting the decisions of customers. Additionally, improving intent to purchase via increasing trust in the marketplace, product, and vendor is a future direction for improvement.

Future research will focus on both design science and behavioral information systems research. One future aim is to address the missing nomothetic design genre of inquiry. In this stream of future research, the design science level of contrition will increase from level 1 of a situated artifact to level 2 where design theory is developed as the goals of nomothetic design are addressed. From a behavioral standpoint, future directions will investigate the counterfeit score on improving trust in the website/online marketplace, vendor, and product. Similarly, we will improve the presentation of the counterfeit score as well as its usability dimensions and test antecedents, specifically information quality as it relates to the counterfeit score, to additional constructs such as perceived usefulness in our theoretical model.

## 8 References

[1] I. Ajzen, The theory of planned behavior, Organizational behavior and human decision processes, 50(2) (1991) 179-211.

[2] L. Alcock, P. Chen, H. Ch’ng, S. Hodson, Counterfeiting: tricks and trends, Journal of Brand Management, 11(2) (2003) 133-136.

[3] amazon.com, Sell on Amazon, in, (2017).

[4] J. Baldridge, The opennlp project, URL: http://opennlp. apache. org/index. html,(accessed 2 February 2012), (2005).

[5] BASCAP, The Impact of Counterfeiting on Governments and Consumers, in, (Business Action to Stop Counterfeiting and Piracy, London, 2009).

[6] R. Baskerville, M. Kaul, V. Storey, Unpacking the duality of design science, (2011).

[7] R.L. Baskerville, M. Kaul, V.C. Storey, Genres of inquiry in design-science research: Justification and evaluation of knowledge production, Mis Quarterly, 39(3) (2015) 541-564.

[8] R. Bate, K. Hess, Assessing website pharmacy drug quality: safer than you think?, PloS one, 5(8) (2010) e12199.

[9] B. Berman, Strategies to detect and reduce counterfeiting activity, Business Horizons, 51(3) (2008) 191-199.

[10] I. Bernstein, Psychometric Theory (3rd.), New York, NY, US: McGraw Hill, (1994).

[11] P. Berthon, J.M. Hulbert, L.F. Pitt, Brand management prognostications, Sloan Management Review, 40(2) (1999) 53.

[12] P.H. Bloch, R.F. Bush, L. Campbell, Consumer ―accomplices‖ in product counterfeiting: a demand side investigation, Journal of Consumer Marketing, 10(4) (1993) 27-36.

[13] G. Bock, Behavioral intention formation in knowledge sharing: Examining the roles of extrinsic motivators, social-psychological forces, and organizational climate, MIS Quarterly, 29(1) (2005) 87-111.

[14] C. Bray, Tiffany Calls Out EBay on Sales, in: The Wall Street Journal, (New York, 2007).

[15] A. Bullock, O. Stallybrass, S. Trombley, B. Eadie, The Fontana dictionary of modern thought, (Cambridge Univ Press, 1977).

[16] R. Chakraborty, J. Lee, S. Bagchi-Sen, S. Upadhyaya, H.R. Rao, Online shopping intention in the context of data breach in online retail stores: An examination of older and younger adults, Decision Support Systems, 83(2016) 47-56.

[17] W.W. Chin, Commentary: Issues and opinion on structural equation modeling, MIS Quarterly, 22(1) (1998) 7-16.

[18] W.W. Chin, The partial least squares approach to structural equation modeling, Modern methods for business research, 295(2) (1998) 295-336.

[19] C.E.H. Chua, J. Wareham, D. Robey, The role of online trading communities in managing internet auction fraud, MIS Quarterly, (2007) 759-781.

[20] B.J. Corbitt, T. Thanasankit, H. Yi, Trust and e-commerce: a study of consumer perceptions, Electronic Commerce Research and Applications, 2(3) (2003) 203-215.

[21] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS quarterly, (1989) 319-340.

[22] R. De Maesschalck, D. Jouan-Rimbaud, D.L. Massart, The mahalanobis distance, Chemometrics and intelligent laboratory systems, 50(1) (2000) 1-18.

[23] W.H. DeLone, E.R. McLean, Information systems success: The quest for the dependent variable, Information systems research, 3(1) (1992) 60-95.

[24] T. Dinev, Q. Hu, The centrality of awareness in the formation of user behavioral intention toward protective information technologies, Journal of the Association for Information Systems, 8(7) (2007) 386.

[25] M.I. Eid, Determinants of e-commerce customer satisfaction, trust, and loyalty in Saudi Arabia, Journal of electronic commerce research, 12(1) (2011) 78.

## ACCEPTED MANUSCRIPT

[26] EMC Education, Data Science and Big Data Analytics: Discovering, Analyzing, Visualizing and Presenting Data, (2015).

[27] M.S. Featherman, P.A. Pavlou, Predicting e-services adoption: a perceived risk facets perspective, International journal of human-computer studies, 59(4) (2003) 451-474.

[28] M. Fishbein, A theory of reasoned action: some applications and implications, (1979).

[29] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, Journal of marketing research, (1981) 39-50.

[30] P. Galle, P. Kroes, Science and design: identical twins?, Design Studies, 35(3) (2014) 201-231.

[31] D. Gefen, E. Karahanna, D.W. Straub, Trust and TAM in online shopping: an integrated model, MIS quarterly, 27(1) (2003) 51-90.

[32] D. Gefen, V.S. Rao, N. Tractinsky, The conceptualization of trust, risk and their electronic commerce: the need for clarifications, in: System Sciences, 2003. Proceedings of the 36th Annual Hawaii International Conference on, (IEEE, 2003), pp. 10 pp.

[33] J.F. George, The theory of planned behavior and Internet purchasing, Internet research, 14(3) (2004) 198- 212.

[34] S. Grazioli, S.L. Jarvenpaa, Perils of Internet fraud: An empirical investigation of deception and trust with experienced Internet consumers, Systems, Man and Cybernetics, Part A: Systems and Humans, IEEE Transactions on, 30(4) (2000) 395-410.

[35] S. Gregor, A.R. Hevner, Positioning and presenting design science research for maximum impact, MIS quarterly, 37(2) (2013) 337-356.

[36] S. Gregor, D. Jones, The anatomy of a design theory, Journal of the Association for Information Systems, 8(5) (2007) 312.

[37] E.G. Guba, Criteria for assessing the trustworthiness of naturalistic inquiries, ECTJ, 29(2) (1981) 75-91.

[38] H.-Y. Ha, Factors influencing consumer perceptions of brand trust online, Journal of Product & Brand Management, 13(5) (2004) 329-342.

[39] K. Hafner, Tiffany and eBay in fight over fakes, The New York Times, (2007).

[40] J.F. Hair, C.M. Ringle, M. Sarstedt, PLS-SEM: Indeed a silver bullet, Journal of Marketing theory and Practice, 19(2) (2011) 139-152.

[41] J.F. Hair Jr, G.T.M. Hult, C. Ringle, M. Sarstedt, A primer on partial least squares structural equation modeling (PLS-SEM), (Sage Publications, 2016).

[42] W. Hampton-Sosa, M. Koufaris, The effect of web site perceptions on initial trust in the owner company, International Journal of Electronic Commerce, 10(1) (2005) 55-81.

[43] D. Harrison McKnight, V. Choudhury, C. Kacmar, The impact of initial consumer trust on intentions to transact with a web site: a trust building model, The Journal of Strategic Information Systems, 11(3) (2002) 297-323.

[44] E. Hatcher, O. Gospodnetic, M. McCandless, Lucene in action, in, (Manning Publications Greenwich, CT, 2004).

[45] G. Häubl, V. Trifts, Consumer decision making in online shopping environments: The effects of interactive decision aids, Marketing science, 19(1) (2000) 4-21.

[46] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q., 28(1) (2004) 75-105.

[47] I.B. Hong, H. Cho, The impact of consumer trust on attitudinal loyalty and purchase intentions in B2C emarketplaces: Intermediary trust vs. seller trust, International Journal of Information Management, 31(5) (2011) 469-479.

[48] R.E. Hostler, V.Y. Yoon, Z. Guo, T. Guimaraes, G. Forgionne, Assessing the impact of recommender agents on on-line consumer unplanned purchase behavior, Information & Management, 48(8) (2011) 336-343.

[49] C.M. Jackson, S. Chow, R.A. Leitch, Toward an understanding of the behavioral intention to use an information system, Decision sciences, 28(2) (1997) 357-389.

[50] S.L. Jarvenpaa, N. Tractinsky, L. Saarinen, Consumer trust in an internet store: a cross‐ cultural validation, Journal of Computer‐ Mediated Communication, 5(2) (1999) 0-0.

## ACCEPTED MANUSCRIPT

[51] S.L. Jarvenpaa, N. Tractinsky, M. Vitale, Consumer trust in an Internet store, Information Technology and Management, 1(1) (2000) 45-71.

[52] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: The role of trust, perceived risk, and their antecedents, Decision support systems, 44(2) (2008) 544-564.

[53] D.J. Kim, D.L. Ferrin, H.R. Rao, Trust and satisfaction, two stepping stones for successful e-commerce relationships: A longitudinal exploration, Information systems research, 20(2) (2009) 237-257.

[54] H.-W. Kim, Y. Xu, J. Koh, A comparison of online trust building factors between potential customers and repeat customers, Journal of the Association for Information Systems, 5(10) (2004) 13.

[55] Y.H. Kim, Y.H. Kim, A study of online transaction self-efficacy, consumer trust, and uncertainty reduction in electronic commerce transaction, in: System Sciences, 2005. HICSS'05. Proceedings of the 38th Annual Hawaii International Conference on, (IEEE, 2005), pp. 170c-170c.

[56] Y.-F. Kuo, S.-N. Yen, Towards an understanding of the behavioral intention to use 3G mobile value-added services, Computers in Human Behavior, 25(1) (2009) 103-110.

[57] L.N. Leonard, Attitude influencers in C2C e-commerce: Buying and selling, Journal of Computer Information Systems, 52(3) (2012) 11-17.

[58] Y. Lu, Y. Cao, B. Wang, S. Yang, A study on factors that affect users’ behavioral intention to transfer usage from the offline to the online channel, Computers in Human Behavior, 27(1) (2011) 355-364.

[59] C. Maldonado, E.C. Hume, Attitudes toward counterfeit products: An ethical perspective, Journal of Legal, Ethical and Regulatory Issues, 8(2) (2005) 105-117.

[60] C.D. Manning, P. Raghavan, H. Schütze, Scoring, term weighting and the vector space model, Introduction to information retrieval, 100(2008) 2-4.

[61] C. Martin, 5 Myths About Selling on Amazon, in, (Entrepreneur, 2017).

[62] R.C. Mayer, J.H. Davis, F.D. Schoorman, An integrative model of organizational trust, Academy of management review, 20(3) (1995) 709-734.

[63] D.H. McKnight, V. Choudhury, C. Kacmar, The impact of initial consumer trust on intentions to transact with a web site: a trust building model, The Journal of Strategic Information Systems, 11(3) (2002) 297- 323.

[64] G.R. Newman, R.V. Clarke, Superhighway robbery, (Routledge, 2013).

[65] A.I. Nicolaou, D.H. McKnight, Perceived information quality in data exchanges: Effects on risk, trust, and intention to use, Information systems research, 17(4) (2006) 332-351.

[66] P.S. Norum, A. Cuno, Analysis of the demand for counterfeit goods, Journal of Fashion Marketing and Management, 15(1) (2011) 27-40.

[67] OECD, Trade on Counterfeit and Pirated Goods: Trade in Counterfeit and Pirated Goods: Mapping the Economic Impact, in, (2016), pp. 11.

[68] P. Oram, WordNet: An electronic lexical database, Applied Psycholinguistics, (2001) 131-134.

[69] L.-Y. Pan, J.-S. Chiou, How much can you trust online information? Cues for perceived trustworthiness of consumer-generated online information, Journal of Interactive Marketing, 25(2) (2011) 67-74.

[70] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends® in Information Retrieval, 2(1–2) (2008) 1-135.

[71] B. Pang, L. Lee, S. Vaithyanathan, Thumbs up?: sentiment classification using machine learning techniques, in: Proceedings of the ACL-02 conference on Empirical methods in natural language processing-Volume 10, (Association for Computational Linguistics, 2002), pp. 79-86.

[72] P.A. Pavlou, Consumer acceptance of electronic commerce: integrating trust and risk with the technology acceptance model, International journal of electronic commerce, 7(3) (2003) 101-134.

[73] P.A. Pavlou, M. Fygenson, Understanding and predicting electronic commerce adoption: An extension of the theory of planned behavior, MIS quarterly, (2006) 115-143.

[74] K. Peffers, T. Tuunanen, M. Rothenberger, S. Chatterjee, A Design Science Research Methodology for Information Systems Research, Journal of Management Information Systems, 24(3) (2007) 45-77.

[75] E. Penz, B. Stottinger, Forget the" real" thing-take the copy! An explanatory model for the volitional purchase of counterfeit products, Advances in consumer research, 32(2005) 568.

[76] J.P. Peter, L.X. Tarpey Sr, A comparative analysis of three consumer decision strategies, Journal of consumer research, 2(1) (1975) 29-37.

[77] R. Prabowo, M. Thelwall, Sentiment analysis: A combined approach, Journal of Informetrics, 3(2) (2009) 143-157.

[78] J. Pries-Heje, R. Baskerville, The design theory nexus, MIS quarterly, (2008) 731-755.

[79] A. Rajaraman, J.D. Ullman, Mining of massive datasets, (Cambridge University Press, 2011).

[80] A. Randon, Counterfeit luxury goods online: an investigation of consumer perceptions, International Journal of Marketing Studies, 4(2) (2012) p74.

[81] M.Q. Saeed, Z. Bilal, C.D. Walter, An NFC based consumer-level counterfeit detection framework, in: Privacy, Security and Trust (PST), 2013 Eleventh Annual International Conference on, (IEEE, 2013), pp. 135-142.

[82] W. Shepard, Amazon Scams On The Rise In 2017 As Fraudulent Sellers Run Amok And Profit Big, in: Forbes (Ed.), (2017).

[83] H.-P. Shih, Extended technology acceptance model of Internet utilization behavior, Information & Management, 41(6) (2004) 719-729.

[84] T. Staake, F. Thiesse, E. Fleisch, Business strategies in the counterfeit market, Journal of Business Research, 65(5) (2012) 658-665.

[85] M. Taboada, J. Brooke, M. Tofiloski, K. Voll, M. Stede, Lexicon-based methods for sentiment analysis, Computational linguistics, 37(2) (2011) 267-307.

[86] B. Tan, Understanding consumer ethical decision making with respect to purchase of pirated software, Journal of consumer marketing, 19(2) (2002) 96-111.

[87] Y.-H. Tan, W. Thoen, Formal aspects of a generic model of trust for electronic commerce, Decision Support Systems, 33(3) (2002) 233-246.

[88] P.D. Turney, Thumbs up or thumbs down?: semantic orientation applied to unsupervised classification of reviews, in: Proceedings of the 40th annual meeting on association for computational linguistics, (Association for Computational Linguistics, 2002), pp. 417-424.

[89] V. Vaishnavi, W. Kuechler, Design research in information systems, (2004).

[90] H. Van der Heijden, T. Verhagen, M. Creemers, Understanding online purchase intentions: contributions from technology and trust perspectives, European journal of information systems, 12(1) (2003) 41-48.

[91] J.G. Walls, G.R. Widmeyer, O.A. El Sawy, Building an information system design theory for vigilant EIS, Information systems research, 3(1) (1992) 36-59.

[92] H. Wang, L. Liu, W. Song, J. Lu, Feature-based sentiment analysis approach for product reviews, Journal of Software, 9(2) (2014) 274-279.

[93] J.M. Wilson, R. Fenoff, Distinguishing Counterfeit From Authentic Product Retailers in the Virtual Marketplace, International Criminal Justice Review, 24(1) (2014) 39-58.

[94] L. Wu, J.-L. Chen, An extension of trust and TAM model with TPB in the initial adoption of on-line tax: an empirical study, International Journal of Human-Computer Studies, 62(6) (2005) 784-808.

[95] S. Yang, Y. Lu, S. Gupta, Y. Cao, R. Zhang, Mobile payment services adoption across time: An empirical study of the effects of behavioral beliefs, social influences, and personal traits, Computers in Human Behavior, 28(1) (2012) 129-142.

Hayden Wimmer is Assistant Professor in the Department of Information Technology at Georgia Southern University. He received his M.S. and Ph.D. from the University of Maryland Baltimore County and his M.B.A. from the Pennsylvania State University. He has multiple journal publications related to multi-agent systems, artificial intelligence, data science, and I.S. education; and serves in various editorial capacities including co-editor in chief, board member, and reviewer of various journals and conferences.

Victoria Yoon is Professor in the Department of Information Systems at the Virginia Commonwealth University. Her primary research area has been the application of intelligent technologies, such as Semantic Web, Ontology, and Multi-Agent Systems, to business decision-making in organizations as well as technical and social issues surrounding those technologies. She has published articles in such leading journals as MIS Quarterly, Decision Support Systems, Communications of the ACM, and Journal of Management Information Systems. She is a senior editor of Decision Support Systems and also serves on the editorial review board of Journal of Database Management and International Journal of Decision Support Systems Technologies.

## Highlights

 This paper presents a design artifact to support the consumer’s decision-making process in an online marketplace by automatically identifying counterfeit products.

Our design artifact, called Online Counterfeit Detection Score (OnCDS), employs web scraping, natural language processing, and topic analysis to process online customer review.

 We evaluate its utility in terms of accuracy of counterfeit scores and the effect of a counterfeit score on a consumer’s attitude on purchasing a product.

 Results show that the design artifact’s efficacy is validated and that the counterfeit score affects perceived usefulness, perceived risk, trust, and attitude toward purchase.
