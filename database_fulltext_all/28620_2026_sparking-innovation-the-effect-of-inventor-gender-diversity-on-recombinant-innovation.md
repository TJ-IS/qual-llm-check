---
otero_id: 28620
otero_key: "JZFB984W"
title: "Sparking Innovation: The Effect of Inventor Gender Diversity on Recombinant Innovation"
authors: "Naveenkumar Ramaraju; Shagun Pant; Gautam Pant"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0343"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sparking Innovation: The Effect of Inventor Gender Diversity on Recombinant Innovation

Naveenkumar Ramaraju,<sup>a</sup> Shagun Pant,<sup>a</sup> Gautam Pant<sup>a,</sup>\*

<sup>a</sup> Department of Business Administration, Gies College of Business, University of Illinois at Urbana-Champaign, Champaign, Illinois 61820 \*Corresponding author

Contact: nr34@illinois.edu, https://orcid.org/0000-0002-2066-8257 (NR); spant@illinois.edu (SP); gpant@illinois.edu, https://orcid.org/0000-0001-7414-2325 (GP)

Received: June 9, 2023 Revised: March 30, 2024; January 19, 2025; April 18, 2025 Accepted: April 27, 2025 Published Online in Articles in Advance: June 5, 2025

https://doi.org/10.1287/isre.2023.0343

Copyright: © 2025 INFORMS

Abstract. Innovation, at its core, is a recombinant process that involves the blending of existing ideas to produce novel solutions. In this study, we examine the effect of gender diversity among patenting inventors on the recombinant intensity of firm innovation. To measure recombinant intensity, we propose an information artifact called SPaRK (Semantic Patent Recombinant Knowledge), which utilizes word embeddings from the patent text. We identify the impact of inventor gender diversity by leveraging the variation in the pro portion of female graduate students entering the local inventor labor market as an instrumental variable. Using a multisource data set derived from 1.8 million patents across 4,769 firms spanning 23 years, we find that gender diversity among a firm’s inventors positively impacts: (1) the firm’s future recombinant innovation; (2) the firm’s future innovation quantity, quality, and labor efficiency; and (3) the future innovation productivity of female inventors at the firm. In other words, heightened gender diversity benefits both firms and the female inventors they employ. Our mediation analysis reveals that cross-gender collaborations serve as a crucial mechanism through which increased gender diversity trans lates into enhanced recombinant innovation. At the same time, we find that although inventor gender diversity is generally beneficial for recombinant innovation at firms, it marginal impact depends on how central female inventors already are in the knowledge network.

History: Ram Gopal, Senior Editor; Yixin Lu, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0343.

Keywords: gender diversity • recombinant innovation • word embedding • text analytics

## 1. Introduction

In his seminal work, Schumpeter (1934) introduced the notion of recombinant innovation that emphasized how new ideas emerge through the recombination of existing ones. More recently, Kaplan and Vakili (2015) argue that “all innovations are based on some sort of recombination.” Prior studies suggest that highly recombinant innovations often yield breakthrough outcomes (Ahuja and Morris Lampert 2001, Sorenson and Fleming 2004, Strumsky and Lobo 2015). Also, the capacity to recombine ideas effectively is widely recognized as a critical determinant of a firm’s overall innovativeness (Galunic and Rodan 1998, Carnabuci and Operti 2013). However, not all innovations are equally recombinant, and measuring the level of recombination in an innovation is nontrivial. Moreover, although the literature has documented the importance and consequences of recombinant innovation, relatively few studies have identified the specific factors that enable firms to produce higher levels of recombination (Carnabuci and Operti 2013). One promising avenue lies in examining the gender diversity of inventors. Research on gender diversity often points to differences in information-processing styles and decision-making approaches between men and women (Meyers-Levy and Maheswaran 1991, Cahill 2006, Halpern 2011). These differences could enrich a firm’s capacity for tackling complex tasks that involve combining disparate ideas that are necessary for gen erating higher levels of recombinant innovations. Also, the historical underrepresentation of female inventors implies an untapped talent pool that could boost innovative capacity. Against this background, our study explores how gender diversity among inventors, a key workforce directly involved in innovation activities at firms, might affect firm-level innovation outcomes.

Despite the importance of recombinant innovation, prior research has not examined the relationship between inventor gender diversity and this important characteristic of firm innovation. This may be attributed, at least in part, to the lack of adequate measurement of the recombinant intensity of firm innovation.

Moreover, although inventors are the most relevant group of workers to study the role of gender diversity in affecting recombinant innovation, data on the gender of inventors is not readily available. In this paper, we address both the measurement and data-related hurdles that, we believe, have constrained past research on inventor gender diversity and recombinant innovation at firms. Specifically, to study this important relationship, we propose a novel machine learning-based information artifact that quantifies the level of recombinant innovation at firms by leveraging a large data set of 1.8 million patents across 4,769 firms spanning 23 years.

Patents are widely acknowledged as economic indi cators of innovation (Griliches 1998) and are extensively utilized in innovation research. They also represent tangible outputs of firm innovation that are validated by external entities like patent examiners. Patents have been regularly used to identify inventors and inventor mobility across firms (e.g., Li et al. 2014, Bell et al. 2019, Bhaskarabhatla et al. 2021). Existing studies also utilize patent metadata, such as technology subclasses and citations, to measure recombinant innovation (e.g., Trajtenberg et al. 1997, Hall et al. 2001, Keupp and Gassmann 2013, Strumsky and Lobo 2015). Technology subclasses for a patent are derived from the Cooperative Patent Classification (CPC) codes assigned to them by patent examiners. However, approaches relying on technology subclasses face severe limitations, particularly for patents that are assigned a single subclass, which accounts for over 50% of patents in our data set. In general, the reliance on metadata introduces issues of incompleteness and inconsistency.<sup>1</sup> Also, while existing measures aim to capture the rarity of combining knowledge domains within a patent, they fail to quantify the relative contributions of these domains. To address these issues, we introduce and utilize a novel information artifact called Semantic Patent Recombinant Knowledge (SPaRK), which measures the recombinant intensity of a patent. Unlike prior approaches that rely on patent technology codes, SPaRK offers a more nuanced and continuous measure of recombinant intensity. It captures both the novelty of knowledge recombination and the contributions of semantically diverse domains to a patent. Importantly, SPaRK achieves this solely by analyzing the text of patents, thus eliminating the reliance on metadata to measure recombinant innovation. Each patent is seen as drawing on knowledge from one or more domains with varying degrees of contribution. To create SPaRK, we analyze the text of over 6 million<sup>2</sup> patents and train custom word embeddings using a neural network architecture. The resulting word embeddings are vector representations of terms appearing in patents. These vectors span the semantic space derived from the patent text and, hence, encode the underlying innovation context.

Clusters of these term vectors represent knowledge domains, allowing us to calculate recombinant distances within the semantic innovation space. A higher value of SPaRK indicates an unusual recombination of knowledge from semantically disparate domains in a given patent. Hence, SPaRK reflects the recombinant intensity of the patent. We retrain SPaRK every year, enabling the model to dynamically adapt terms and cluster centers to reflect the evolution of the technology landscape accurately over time. We validate our pro posed SPaRK measure by demonstrating its superior association with the economic value of patents.

The process of combining existing ideas and technologies in novel ways (which would result in higher SPaRK values) may require diverse perspectives and varied approaches to information processing. For example, Carnabuci and Operti (2013) argue that in order to create recombinant innovation, firms need to make sense of unexplored interdependencies by broadening their perspectives. Prior literature in management (Meyers-Levy and Maheswaran 1991), psychology (Halpern 2011), and neuroscience (Cahill 2006) sug gests that men and women employ different cognitive techniques and information-processing strategies. Such differences in cognitive processing could lead to heterogeneous viewpoints and unusual combinations of ideas. Hence, it is important to study the role of gender diversity in affecting the level of recombinant innovation at firms.

Using our SPaRK measure, designed to capture unlikely combinations of domains and ideas, we investigate the impact of gender diversity among inventors on firms’ recombinant innovation. Specifically, we analyze gender diversity among a firm’s inventors over time to address the following questions: (i) What is the effect of inventor gender diversity on the recombinant intensity of firm innovation? (ii) What is the impact of inventor gender diversity on the firm’s innovation quantity, quality, and labor efficiency? (iii) Is inventor gender diversity beneficial for the innovation productivity of female inventors at the firm? (iv) Is inventor gender diversity beneficial for the financial performance of the firm? (v) What is the role of the nature of collaboration between inventors in the impact of inventor gender diversity on innovation outcomes? And (vi) how does the centrality of female inventors or the presence of a female board member moderate the relationship between inventor gender diversity and innovation outcomes? These questions have mostly gone unexamined, with the exception of a few limited studies related to question (ii). As outlined in Section 2.2, those investigations have failed to offer sufficient insights. Specifically, question (i) addresses the recombinant nature of firm innovation, whereas question (ii) focuses on other aspects, such as patent volume and citations. Past research, regardless of its focus on gender diversity, has primarily concentrated on the volume of innovation. However, the findings for innovation volume do not automatically apply to the recombinant nature of firm innovation (e.g., an increase in volume does not imply an increase in median SPaRK at firms). This distinction underscores the need for a separate line of inquiry.

Because hiring female inventors is an endogenous decision by firms, to identify the causal impact of inventor gender diversity on firm innovation, we propose the proportion of local (geographic area-level) female graduate students in the relevant field as an instrumental variable (IV). Such an IV will exploit the exogenous variation in gender diversity in the human capital relevant to the firm (same geographic area and field) to identify the effect of inventor gender diversity on firm outcomes. Using the proposed IV, we find that inventor gender diversity positively impacts innovation along the dimensions of recombinant innovation, innovation quantity, quality, and labor efficiency of innovation (patents per inventor) of the firm as a whole, as well as for female inventors at the firm. Our results indicate a strong positive effect of inventor gender diversity on both a firm’s knowledge combining capability and individual innovation productivity. Together, these results imply that increasing gender diversity amongst inventors is beneficial for female inventors, while simultaneously enhancing knowledge recombination and overall firm innovation output. Additionally, we shed light on the underlying mechanism of this effect by examining collaborations between female and male inventors as a mediator. The findings highlight the critical role of fostering cross-gender inventor collaborations within firms to unlock the innovation potential of a gender-diverse workforce, particularly in driving greater recombinant innovation. Moderation analysis further reveals that the positive effects of inventor gender diversity diminish in firms where female inventors are more central within the inventor network, suggesting that the distribution of influence within the collaboration network plays a critical role in shaping the outcomes of inventor gender diversity. Our findings from mediation and moderation analyses offer practical managerial insights on how firms can effectively leverage the gender diversity of their inventor workforce posthiring— an important, yet previously unexplored, aspect in the literature.

Our study makes several notable contributions to the existing literature. Firstly, this study is the first to discern the impact of gender diversity among patenting inventors on the recombinant intensity of firm innovation. Secondly, we propose a purely text-based information artifact to measure the recombinant intensity called SPaRK. We anticipate that the SPaRK measure will serve as an essential tool for addressing a significant gap in the innovation measurement literature and, hence, should be adopted in future innovation and other related studies. Abbasi et al. (2016) have noted that creating a novel artifact for prediction or description is a potential research avenue for big data and design science (Hevner et al. 2004). SPaRK serves as an example of such a contribution. It also contributes to the information systems literature by “understanding phenomena using Machine Learning” (Padmanabhan et al. 2022, p. vii), as it provides a new way to gauge knowledge recombination. Thirdly, the effect of gender diversity on different types of innovation outcomes (e.g., patents, new products) in the related literature is mixed and currently lacks clear identification strategies. To isolate the (causal) effect of inventor gender diversity at firms, we conduct a robust empirical analysis and propose using the proportion of female graduate students entering the local inventor labor market as an instrumental variable, providing a robust identification strategy. Additionally, we find that inventor gender diversity greatly enhances the innovative output of female inventors at firms. This is critical, as better performance of female inventors can reduce female inventor attrition and help attract a pipeline of future female inventors. This uplift in female inventor productivity can yield benefits beyond individual firms to the broader economy. Finally, we examine mechanisms that can guide organizations to structure their inventor work force for better innovation outcomes.

## 2. Background and Hypotheses 2.1. Theoretical Perspectives

Multiple theoretical frameworks may offer insights into how diversity (in general) might shape innovation outcomes. Two key theoretical perspectives in the related literature are the “value-in-diversity” perspective and the “social categorization” perspective. They provide contrasting views on the benefits and challenges of a diverse workforce. Research that looks into gender differences in information processing adds to these theories by suggesting a mechanism through which gender diversity might affect innovation—specifically, recombi nant innovation that involves synthesizing disparate ideas into novel solutions.

The value-in-diversity theory (Cox and Blake 1991) argues that diversity, including gender diversity, boosts problem-solving and creativity by bringing together people who differ in their perspectives and cognitive styles. This, in turn, can provide firms with net-added value and a competitive advantage in addressing complex challenges. In the context of firm innovation, the value-in-diversity theory would suggest that a genderdiverse workforce could lead to more innovative recombination of ideas. In a similar vein, Nielsen et al. (2017) argue that gender diversity provides an “innovation dividend” due to diverse perspectives and thoughts. Page (2017) argues that diversity enriches perspectives, and the “diversity bonus” is especially relevant for more complex and innovative work.

The literature on differences in information-processing styles between men and women provides a plausible mechanism for unlocking “value-in-diversity” through cross-gender collaborations. Studies suggest that there are differences in cognitive strategies and problemsolving approaches between genders (Meyers-Levy and Maheswaran 1991, Halpern 2011). For example, while processing information, women may draw from a comprehensive set of factors, whereas men focus on key elements. As a result, during cross-gender collaborations, the blending of these distinct cognitive styles could lead to more novel solutions. This is especially relevant to recombinant innovation, as the distinct informationprocessing approaches from gender-diverse inventors could enhance the ability to bridge semantically distant ideas.

In contrast to value-in-diversity theory, the social categorization perspective (Tajfel et al. 1979, Turner 2010) highlights the potential challenges of diversity. This theory posits that individuals categorize themselves and others into groups based on social identities such as gender. Such categorization could reduce the ability of diverse teams to be creative due to lower group cohesion, communication barriers, and conflict. Individuals may gravitate toward those who are like themselves and distance themselves from those who are different, potentially undermining teamwork and collaboration. Cox and Blake (1991) define the resources required to address these challenges and the investment required to maintain a diverse workforce as “cost-of-diversity.” Whereas the valuein-diversity perspective highlights the creative potential of diverse perspectives, the social categorization perspective suggests that social identity differences could undermine these benefits.

These competing theoretical lenses provide a foundation for the empirical exploration of the relationship between inventor gender diversity and firm innovation, specifically the recombinant intensity of that innovation. Although previous empirical literature has not looked at the specific relation between gender diversity and recombinant firm innovation, there are related studies on gender diversity and innovation. We will next describe several of the previous empirical studies, which, like the theoretical lenses above, provide mixed results.

## 2.2. Empirical Evidence

Many of the previous empirical studies can be grouped based on their alignment with value-in-diversity and social categorization theories. In line with the value-indiversity perspective, Yang and Konrad (2011) find that gender diversity of R&D teams is positively associated with their ability to introduce a new product, process, or service in a sample of Canadian firms. Similarly, D´ıaz-Garc´ıa et al. (2013) find a positive association between gender diversity in R&D teams and radical innovation in Spanish firms. Also, using census data from manufacturing firms in a coastal province in China, Xie et al. (2020) find a positive association between gender diversity in R&D teams and new product sales per unit R&D expenditure. All of these studies support the value-in-diversity perspective, showing potential evidence of enhanced creativity and problemsolving through gender-diverse teams.

In contrast, there are empirical studies that high light the challenges of diversity and support the social categorization theory. Cropley and Cropley (2017) observe a negative link between gender diversity and innovation capacity based on data from a survey at an Australian manufacturing firm. Cady and Valentine (1999) find that gender diversity had a negative impact on the quantity of innovative ideas generated by teams participating in technical contests within a division of a high-tech Fortune 500 company. Teruel and Segarra-Blasco (2022) find a negative relationship between gender diversity in R&D teams and patent generation in Spanish firms. Similarly, Halkos and Kitsos (2012) also find a negative association between the gender diversity of R&D teams and innovation in Greek firms.

There are studies that support neither of the two competing theoretical perspectives or find a more nuanced relationship between gender diversity and innovation. For example, An et al. (2021) find no relationship between gender-diverse boards and firm innovation (based on patent counts, citations, and mar ket value) for a large sample of U.S. firms. Ruiz-Jime´nez et al. (2016) document that gender diversity of top management teams has no direct relationship with innovation performance based on new products and services at small- and medium-sized enterprises in the Spanish technology-based sector. Similarly, Faems and Subramanian (2013) find no relationship between the number of patents granted and the gender diversity of R&D teams among firms in Singapore. Torchia et al. (2011) find that board gender diversity has a (positive) relationship with innovation only when women directors are above a “critical mass” (Kanter 1977). Ferna´ndez (2015) and Gonzalez-Moreno et al. (2018) find an inverted-U relationship between gender diversity and the ability to introduce a product, process, or service using a sample of Spanish firms. Studies outside the organizational context focusing on the effect of teamlevel gender diversity on scientific ideas have also found mixed results.<sup>3</sup>

The reasons for the conflicting empirical findings could be the small sample sizes (one or few firms in several studies), measurement issues, national differences, or varied industries or domains, as well as a lack of clear econometric identification. In this study, we focus on a large number of U.S. firms across industries, as U.S. firms have historically led in patent filings. Our key measurements are based on patents, which are legally and externally recognized as novel, nonobvious, and useful. This approach differs from relying on self-reported innovation by employees or managers, which can be prone to biases such as overconfidence and conflicts of interest (Han et al. 2024).

## 2.3. Hypotheses Development

Given the mixed empirical evidence and the theoretical tension that suggests both benefits and challenges of gender diversity, our study seeks to empirically untangle the relationship between inventor gender diversity with recombinant innovation and other outcomes for firms. Females are grossly underrepresented in STEM (Ding et al. 2006, Hunt et al. 2013) and consequently among firm inventors (only 7.4% in our data), which further warrants a robust empirical study. As noted, research on gender diversity highlights differing cognitive and decision-making styles between men and women, suggesting that such diversity can enhance recombinant innovation through varied perspectives. Thus, we hypothesize:

Hypothesis 1. Gender diversity among a firm’s inventors influences recombinant innovation and other facets of their innovative performance.

Nielsen et al. (2017) argue that the “innovation dividend” is realized when diverse teams are effectively managed to harness their varied perspectives. Similarly, Woolley et al. (2010) find that females in a group positively impact group intelligence. A central theoretical insight from this body of literature is that collaboration between male and female members serves as a critical mechanism for unlocking the value in diversity. Conversely, the negative effects suggested by the social categorization perspective (Tajfel et al. 1979, Turner 2010) arise from the formation of identity-based groups and the absence of diverse collaborations. Based on these arguments, we hypothesize:

Hypothesis 2. The effect of gender diversity among patenting inventors on firm innovation is mediated by female-male and female-female collaborations in patenting teams.

It is critical to further our understanding of whether it is female-male collaborations or female-female collaborations that mediate the relationship between diversity and innovation. The social categorization perspective suggests that people naturally gravitate to “similar others” (i.e., homophily), which means that female inventors might not always collaborate with male colleagues or get opportunities for such collaborations. Even if an increase in female inventors is shown to benefit innovation overall, it remains an open question how that benefit arises. Hypothesis 2 investigates a mediating mechanism (i.e., cross-gender or same-gender collaborations) that might explain why adding female inventors leads to improved innovation outcomes.

Ahuja et al. (2003) claim that the centrality of individuals affects their performance in R&D teams. Similarly, Paruchuri and Awate (2017) show that the knowledge network and the connectedness (centrality) of a group of inventors influence the innovation outcomes of firms. This suggests that the centrality of specific groups of inventors, particularly female inventors, could shape innovation outcomes. When female inventors are centrally positioned in the innovation network, they have a higher potential to diffuse diverse perspectives into the innovation network, thus unlocking the value in diversity, as suggested by theory. On the flip side, if female inventors are not central, their unique knowledge and viewpoints may remain on the periphery, which could diminish potential diversity benefits for innovation. Also, being central in the innovation network could signal acceptance within the male-dominated network. Such acceptance reduces the risk of “us versus them” subgrouping, as suggested by social categorization theory. In other words, central female inventors may effectively neutralize categorization barriers by being embedded in the heart of innovation networks within firms. Corporate boards also play a crucial role as central hubs for setting innovation agendas. The presence of women on these boards introduces diverse perspectives that have the potential to exert a meaningful, strategiclevel impact on firm innovation (Griffin et al. 2021). Taken together, women in central roles, either as inventors or as board members, could moderate the relationship between gender diversity and innovation outcomes. Based on this reasoning, we hypothesize:

Hypothesis 3. The relationship between gender diversity among patenting inventors and firm innovation is moderated by the centrality of female inventors or the presence of female board members at the firm.

Extant literature suggests that gender diversity influences the performance of women in the workplace. For example, a study by Bostwick and Weinberg (2022) finds that the absence of female peers in a cohort reduces the probability of women completing their PhD program on time. Similarly, Hunt (2016) documents a high rate of exit among women from fields such as engineering that are male-dominated. Consequently, increasing gender diversity among a firm’s inventors could foster a more supportive environment for female inventors. At the same time, the scarcity of women in STEM is well-documented due to hiring and retention barriers (Igbaria and Baroudi 1995, Richard 2000, Joseph et al. 2015, Langer et al. 2020). Thus, it is crucial to study if gender diversity has an impact on the performance of female inventors. Hence, we hypothesize:

Hypothesis 4. Gender diversity among a firm’s inventors influences recombinant innovation and other facets of innovative performance by female inventors.

## 3. Measuring Recombinant Innovation

Previous research has highlighted the recombination of existing knowledge as a key aspect of firm innovation (Fleming 2001, Keupp and Gassmann 2013, Kaplan and Vakili 2015, Strumsky and Lobo 2015). For example, Saldanha et al. (2020) and Dong and Yang (2019) examined how patents recombine knowledge to explore the role of information technology in fostering exploratory innovation. Whalen (2018) claims metadatabased approaches are commonly used in the literature to measure recombinant innovation. The two commonly used metadata are subclass of patent classifications (Trajtenberg et al. 1997, Strumsky and Lobo 2015) and patent citations (Hall et al. 2001). Metadata approaches are easy to implement but are prone to inconsistency and incompleteness. For instance, the U.S. Patent and Trademark Organization (USPTO) transitioned from the U.S. Patent Classification to the CPC patent classification system in 2013. Further, the USPTO has retroactively updated CPC codes of over 85% of patents postissuance. Relying on classification codes like CPC codes that change over time creates inconsistencies in measuring recombinant innovation over time. Compounding this issue, more than half of the patents analyzed in our study are assigned to a single technology subclass, making it challenging to assess recombination levels using current methodologies. Using patent citations to measure recombinant innovation also suffers from similar issues. For instance, citation patterns can be influenced by the patent examiner’s experience (Alca´cer et al. 2009), creating inconsistencies. In our data set, approximately 25% of citations reference nonpatent sources, such as journal articles, which lack rich metadata when compared with patent sources. Thus, reliance on patent citations results in an incomplete measure of recombinant innovation.

In recent years, innovation research has increasingly adopted natural language processing (NLP) techniques for analyzing patents. For example, Whalen (2018) employed Latent Semantic Analysis to create a semantic space based on patent text, measuring the semantic distance between a patent’s cited references. The use of metadata like citations along with text information to measure recombinant innovation still suffers from incompleteness and inconsistency. Although Whalen (2018) provides insights into the breadth of knowledge inputs underpinning the innovation, the breadth of input domains does not necessarily imply that their combination is novel. For example, some citations may be peripheral, whereas others are critical to the patent’s inventive value. To address these limitations, we propose a novel information artifact, SPaRK, a fully text-based measure of recombination. By utilizing innovation-related semantics from millions of patents, SPaRK offers a robust alternative to traditional metadata-based approaches, addressing issues of inconsistency and incompleteness.

## 3.1. Semantic Patent Recombinant Knowledge

The text of a patent abstract concisely describes the core innovation provided by the patent, as presented by its inventors. Hence, the semantic space spanned by the terms in a patent abstract should provide a clear view of the recombination of knowledge therein. We use abstracts and titles of about 6 million patents for our recombinant innovation measure that we call SPaRK. We preprocess the text to remove special characters and stop words. We convert all the words and phrases (constructed from frequent n-grams) to lowercase, except for abbreviations. We then assemble our patent vocabulary with all the words and phrases (we will refer to them as terms) that have occurred at least five times in the entire database. We construct the vector space representation of patent vocabulary as 128-dimension word embedding (vector) using the Word2Vec algorithm proposed by Mikolov et al. (2013).<sup>4</sup> We use a skip-gram model with a context window size of five words. The Word2vec representation of each term captures the semantics of the term by leveraging its context in the patent abstracts. Using this 128-dimension vector semantics trained from the patent database, we cluster the patent vocabulary into 250 groups (topics) using the K-means algorithm due to its scalability and ease of interpretation.<sup>5</sup> Because the cluster centers formed by the K-means algorithm vary based on initialization, we employ K-means++ initialization.<sup>6</sup> K-means++ helps us to choose the best centroid using a sampling technique. Because the technology landscape evolves over time, we only use the patents filed up to a given year to train our models. Also, because our panel data span 23 years (1994–2016), we trained a word-embedding model for each year and estimated 23 sets of cluster centers, each with 250 topics. By using one model per year, we allow terms as well as cluster centers (topics) to move and adapt retrospec tively to the technology space of that time. As such, our proposed measure, SPaRK, evolves with time.

Once cluster centers are determined, we can compute the recombinant innovation in a patent as the average (weighted) distance between various clusters (topics) identified within a patent. First, we identify the L distinct topics that are present within a focal patent’s text from the 250 topics. As noted earlier, not all identified topics contribute equally to the patent knowledge. So, we compute each topic’s relative contribution by using the number of terms from a topic used in a particular patent. Because not all terms appearing in a patent text are equally important, we compute the term frequency-inverse document frequency (TF-IDF) for each term in a given topic to adjust the importance of a term based on its relative usage in the patent corpus, as well as within the focal patent.<sup>7</sup> The TF-IDF of each term is also computed only using patents filed up to the filing year of the focal patent. We denote the relative contribution or cluster size (s ) of topic l as follows:

$$
\text { Topic   Contribution }, s _ {l} = \sum_ {i = 1} ^ {N} T F - I D F (t e r m _ {i}),
$$

where N denotes the number of terms that are present in the focal patent’s text from a given topic (l). Now, the total knowledge of the patent with L different topics is the sum of knowledge contributed by each of the l topics present in the patent. Total knowledge (T) can be denoted as:

$$
\text { Total   Knowledge }, T = \sum_ {l = 1} ^ {L} s _ {l}.
$$

We define the Semantic Patent Recombinant Knowledge of a patent as the average distance between all pairs of clusters, with each distance weighted by the knowledge contributed by the pair of clusters whose distance is measured. Let Z denote a set of pairs of clusters between which the distances need to be computed. Then, mathematically, we can write SPaRK as:

$$
S P a R K = \frac {1}{(L - 1) T} \sum_ {x, y \in \mathbb {Z}} (s _ {x} + s _ {y}) d _ {x, y},
$$

where L is the number of topics in a focal patent, T is the total knowledge as computed above, and $d _ { x , y }$ denotes the cosine distance between a pair of clusters x and y of size $s _ { x }$ and $s _ { y } ,$ respectively. Cosine distance $( d _ { x , y } )$ is given as:

$$
d _ {x, y} = 1 - \frac {u _ {x} . u _ {y}}{\| u _ {x} \| _ {2} \| u _ {y} \| _ {2}},
$$

where $u _ { x }$ and $u _ { y }$ are cluster centers of topics x and y in the word-embedding space.

In Figure 1, we illustrate an example of SPaRK with patent 4075334 from our data set. The abstract of the patent is “Iodinated compounds useful for photoscanning the adrenal glands.” For this patent, we have $L = 3$ clusters (topics) whose terms appear in the patent text (abstract and title). The area of the circles in Figure 1 correspond to the cluster sizes $( s _ { 1 } , s _ { 2 } , s _ { 3 } )$ of different clusters or topics that appear in the patent text, as indicated in the equation for $s _ { l }$ presented earlier. Also, the total knowledge or $T = s _ { 1 } + s _ { 2 } + s _ { 3 }$ . Finally, $d _ { 1 , 2 } , d _ { 1 , 3 } ,$ and $d _ { 2 , 3 }$ are cosine distances between pairs of clusters $\{ 1 , 2 \} , \{ 1 , 3 \} .$ , and $\{ 2 , 3 \} .$ , respectively. Note that in the illustration, we have three clusters, and each cluster’s knowledge contribution is used twice in the distance computation. ${ \mathrm { S o } } ,$ , we divide the weighted sum of knowledge by $( L - 1 ) T$ to ensure that the value of SPaRK is between zero and one. A SPaRK value of zero for a patent indicates no recombination of knowledge and that the patent had the contribution of a single cluster. The increasing value of SPaRK indicates the recombination of topics that are further apart and, hence, greater levels of recombinant innovation.

Figure 1. (Color online) SPaRK Illustration  
![](/api/attachments/JZFB984W/fulltext/images/f5f006427eca952f196b286627880ad467f7c8684aff6c7d2f15c8b4cca83d3e.jpg)  
Notes. The figure illustrates SPaRK for U.S. Patent 4075334 with abstract: “Iodinated compounds useful for photoscanning the adrenal glands.” After preprocessing, the abstract has five terms from three clusters. The size of each circle represents the relative importance of a topic (cluster) to the patent, with each color (or shade) showing the contribution of a specific term to the topic. SPaRK is measured as the weighted sum of the distance between topic centers. The width of a line represents the weight and is estimated based on the contribution of the topics (i.e., the size of the circles) it connects. The length of a line represents the rarity of the combination of two topics and is mea sured using the cosine distance between two topic centers.

Prior research measures the value of patents as the citations received (Trajtenberg 1990). Recently, Kogan et al. (2017) utilize “patent value” as the capital required to replace a patent using stock returns of a firm. We use both these measures of patent usefulness to compare and validate SPaRK as a measure that is superior to other measures of recombinant innovation. Patent-level analysis (Table 1) shows that SPaRK is positively associated with forward citations and patent value. As suggested in theory, SPaRK captures the positive relationship between the extent of recombination and its usefulness on both measures of patent usefulness. However, recombinant measures based on extant literature do not show such an association. As noted earlier, CPC subclass-based measures cannot be used when a patent is assigned to one CPC subclass only. A subsample analysis of such patents shows that

Table 1. SPaRK Validation

<table><tr><td rowspan="3">Recombinant measure</td><td colspan="2">All patents</td><td colspan="2">Patents with single CPC (51% of patents)</td></tr><tr><td colspan="2">Dependent variables</td><td colspan="2">Dependent variables</td></tr><tr><td>Patent value</td><td>Citations</td><td>Patent value</td><td>Citations</td></tr><tr><td>RPatent(Strumsky and Lobo 2015)</td><td>-0.009(0.117)</td><td>-0.0044(0.008)</td><td colspan="2">Not applicable</td></tr><tr><td>Tech. Distance(Trajtenberg et al. 1997)</td><td>-0.001(0.10)</td><td>0.005(0.004)</td><td colspan="2">Not applicable</td></tr><tr><td>Tech. Diversity(Hall et al. 2001)</td><td>-0.006(0.007)</td><td>-0.007**(0.004)</td><td>-0.007(0.007)</td><td>-0.0045(0.004)</td></tr><tr><td>SPaRK(this work)</td><td>0.493***(0.174)</td><td>0.146***(0.048)</td><td>0.547***(0.166)</td><td>0.299***(0.064)</td></tr></table>

Notes. We validate SPaRK by showing its association with a patent’s value and citations received by a patent. Although SPaRK shows a positive and significant association with both patent value and citations received, the other measures do not. Refer to Online Appendix Section A.2 for detailed discussion.  
\*\*Significance at 5%; \*\*\*significance at 1%.

SPaRK provides information on recombinant innovation, which is associated with patent usefulness, whereas traditional measures based on technology subclass assume there is no recombination in such patents.

## 4. Data and Variables

We leverage various data sources related to patents, inventors, firms, and graduate education. The data sources provide richness in our measurements, and we discuss the challenges for integration in Section 4.1. Section 4.2 describes the key variables that measure gender diversity and the instrumental variable. We discuss the outcome and control variables in Section 4.3.

## 4.1. Data

We construct our data from several sources like Compustat, the Center for Research in Security Prices (CRSP), BoardEx, the National Science Foundation (NSF; Survey on Science, Engineering, and Health Graduates), and Cooperative Patent Classification, along with the data made available by works from the related literature. We compute all variables at the firm-year level.

We use data from Bena et al. (2017) and Kogan et al. (2017), which map patents issued by USPTO to firms. We use inventor-disambiguated data from Li et al. (2014) to identify inventors associated with a patent and their names. We also utilize patent abstracts corresponding to a patent number in the same data. Because the gender of the inventors is not directly available in our data, we use the first name of the inventors to identify their gender by consolidating gender information from four gender-identification APIs (Application Programming Interfaces).<sup>8</sup> We validate our gender assignments using the first names and gender of 120,000 Olympic athletes from 1900 to 2016. We consider Olympic data as the gold standard for gender assignment validation due to the availability of gender for each ath lete and representation from the majority of countries, cultures, and ethnicities. We also use the gender information of 514 randomly selected inventors identified from LinkedIn as secondary validation data.<sup>9</sup> The Area Under the Receiver Operating Characteristic Curve is 0.986 and 0.987 for Olympics data and LinkedIn data, respectively. Using F-scores, we find that 0.58 is the ideal probability cut-off in both Olympics and LinkedIn data. Accordingly, an inventor is classified as female if their first name has a probability greater than 0.58 from our gender classifier. When the gender classifier fails to classify an inventor (1.5% of inventors), we assume that the inventor is male because most inventors in our data are males (about 90%).<sup>10</sup>

Next, we aggregate the patent and inventor data for each firm and then combine it with firm-level variables from Compustat, CRSP, and BoardEx for each year. In other words, the granularity of the data is at the firm-year level. Also, data from annual NSF surveys on graduate students at universities across different states in the United States are merged with the above firm-year data using the year and state in which the patenting firm is located (based on Compustat). The NSF survey data are used to compute an instrumental variable that allows for the identification of causal effects of interest. Our final data set spans the years 1994–2016 because the NSF survey data are available from 1994 onward and represent 1.8 million patents with 474,684 unique inventors and 4,769 firms. The final estimation panel spans 1998–2011 because we use five-year rolling windows where inventor gender diversity and other controls look five years back, while innovation outcomes are measured five years forward. Refer to Online Appendix Section A.4 for the summary statistics of all the variables discussed in this section.

4.2. Gender Diversity and Instrumental Variable We measure firm-level inventor gender diversity as the Female Proportion of inventors at a Firm (FPF), rolling over the last five years.<sup>11</sup> Hence, FPF for a firm i in the year t is computed as:

$$
F P F _ {i, t}
$$

Number of female inventors at a firm i in years t to t � 4 � Number of inventors at a firm i in years t to t � 4

Because patenting is viewed as the recombination and flow of various sources of advanced knowledge (Arora et al. 2014), potential recruits to work in R&D roles at a firm are expected to have a higher (likely, graduate) education. Hunt et al. (2013) attribute a lower share of female graduates from STEM as the reason for the underrepresentation of women in the innovation workforce. Hence, the female proportion of local graduate students in relevant fields can provide an exogenous variation to the gender diversity among inventors at a firm. We exploit this observation to propose a novel instrumental variable for inventor gender diversity. In particular, we propose an IV that measures the Female Proportion of Graduate (FPG) students in Science, Engineering, and Health over the last five years using the primary state where a firm is located and its neighboring states. We use this IV to identify the effects of gender diversity using FPF. In addition to addressing endogeneity concerns, IV can also help reduce bias arising from measurement error in FPF.<sup>12</sup> To minimize noise, FPG is aggregated based on the field. More specifically, we aggregate science and engineering (S&E) graduate students and separately aggregate graduate students in health (H) to form the IV.<sup>13</sup> We then map the field-specific IV value (S&E or H) to firms based on their industry as determined by the Standard Industrial Classification (SIC) code and its location as determined by the state in which the firm is primarily located. Hence, FPG for a firm i in year t is given as:

$$
F P G _ {i, t} = \frac {\text { Number   of   female   graduate   students   in   firm } i ^ {\prime} \text { s }}{\text { Region   and   industry   in   years } t \text { to } t - 4}
$$

The region in the above equation refers to the state where a firm is located and its bordering states. FPG is expected to affect the availability of female inventors in the local labor market, which in turn is likely to affect the firm-level (FPF) gender diversity of inventors. Our IV focuses on gender diversity among highly skilled local graduate students in science, engineering, and health. Hence, the proposed IV is relevant to the context of the highly skilled workforce of inventors. Also, our proposed IV is measured yearly, providing adequate exogenous variation for the panel data, thus making the effect of inventor gender diversity identifiable. We find that our IV is not weak statistically in support of its relevance. The proposed IV (FPG) is at the state-industry-year-level aggregated across universities. Our outcome variables and endogenous variable (FPF) are measured at a firm-year level. It is unlikely that enrollment patterns across universities in a state-industry can directly impact the innovation outcomes of individual firms in the state except from its influence on FPF. Female graduates (IV) are likely to contribute to an individual firm’s innovation only if they work for the firm. Because the IV is expected to affect the dependent variables only through FPF, FPG reasonably satisfies the exclusion criteria. We account for potential state-level confounders that could affect both the proposed instrument and innovation outcomes of a firm in Section 4.3.3.

## 4.3. Outcome and Control Variables

We compute all firm-level innovation variables over a five-year horizon into the future. We detail how we measure recombinant innovation through SPaRK, our main outcome of interest in Subsection 3.1. Measurement for traditional innovation outcomes and control variables are elaborated on in Subsections 4.3.2 and 4.3.3, respectively.

4.3.1. Recombinant Innovation. We measure the recombinant capability of a firm as the median value of SPaRK using the patents filed by a firm over the next five years.<sup>14</sup> We define this variable as Firm SPaRK. Similarly, to quantify recombinant innovation of female inventors, we construct Firm SPaRK \$ using patents filed by a firm in the next five years with a female inventor.

4.3.2. Innovation Quantity, Quality, and Labor Efficiency. We use four variables to measure innovation quantity, quality, and labor efficiency. The number of patents measures the quantity of innovation, and patents per inventor (PPI) measures the labor efficiency of innovation. The number of patents and the labor efficiency (PPI) have been used in previous studies (Joshi et al. 2010, Kleis et al. 2012, Xue et al. 2012, Saldanha et al. 2017) as innovation measures. These measures are computed for any given firm-year (i,t) by aggregating the number of patents and unique inventors employed at the firm (i) over the next five years (t + 1 to t + 5).

Whereas the innovation measures defined above capture the quantity and the labor efficiency of innovation, we use the number of citations and citations per patent (CPP) received by patents filed by a firm in the next five years to capture the quality of innovation. Because the number of times a patent is cited varies significantly by the field of innovation and the year in which a patent is filed, we scale the number of citations by CPC patent class at the subclass level (first four characters) and filing year. The scaling allows citation-based measures to be comparable across technology classes and over time. To quantify the female inventors’ innovation at a firm, we compute all four innovation measures specified above using patents with female inventors.

4.3.3. Control Variables. In line with extant literature (Hirshleifer et al. 2018), firm-level variables like total assets, cash, leverage, age of firm, tangibility, Herfindal index (hhi), R&D expenditure (RD), return on assets (ROA), and capex are computed for each year and are used to control for firm characteristics. In addition, we also control for the female proportion of executives (FPE) on the board of a firm. Further, we add four state-level control variables, including the state’s expenditure on R&D as a percentage of its GDP in the year, education attainment as the percentage of the population that obtained a graduate-level college degree from the state in the past five years, sales growth of all firms located in the state aggregated over the past five years, and whether the state has a governor from the Democratic party. The data to construct the firm-level control variables are from CRSP, Compustat, the NSF, the Census Bureau, and BoardEx. Table A.12 in the Online Appendix describes all firmlevel and state-level measures in detail.

## 5. Two-Stage Least Squares Model and Results

In this section, we empirically tease out the effect of gender diversity on a firm’s future innovation output. As detailed in Section 4.3, we capture different facets of innovation using five outcome variables: (1) Firm SPaRK, (2) PPI, (3) Patents, (4) CPP, and (5) Citations, all measured over a five-year horizon into the future. The median SPaRK value represents the ability of a firm to recombine knowledge, which we call Firm SPaRK. The number of patents (Patents) measures patenting quantity, and patents per inventor (PPI)

measures labor efficiency, while quality (or impact) is assessed by the number of scaled citations (Citations) and the scaled citations per patent (CPP). Patents and Citations are log-transformed due to their skewed distributions.

## 5.1. Inventor Gender Diversity and Firm Innovation

For identifying the effect of inventor gender diversity on future innovation, we use a two-stage least square regression (2SLS) design. The left-hand side of the second stage is one of the five innovation measures listed above, and the main variable of interest is the female proportion of inventors at the firm (FPF). We use the female proportion of graduate (FPG) students as an instrumental variable in the first stage. The complete 2SLS specification is as follows:

$$
y _ {i, t} = \alpha_ {i} ^ {s} + \alpha_ {t} ^ {s} + \widehat {\beta F P F} _ {i, t} + \pmb {\gamma} ^ {\prime} \pmb {X} _ {i, t} + u _ {i, t},\tag{Stage 2}
$$

$$
F P F _ {i, t} = \alpha_ {i} ^ {f} + \alpha_ {t} ^ {f} + \pmb {\phi} ^ {\prime} \pmb {X} _ {i, t} + \pi F P G _ {i, t} + v _ {i, t}.\tag{Stage 1}
$$

In the above model, i,t indicates a firm-year observation. We use firm-fixed effects and year-fixed effects in both the first stage $( \alpha _ { i } ^ { f } , \alpha _ { t } ^ { f } )$ as well as the second stage $( \alpha _ { i } ^ { s } , \alpha _ { t } ^ { s } )$ of the model. The variable, $y _ { i , t } ,$ is one of the five dependent variables listed above, measured over the next five years (t + 1 to t + 5). In contrast, $F P F _ { i , t }$ and $F P G _ { i , t }$ are computed over the last five years (t to t � 4), and $\widehat { F P F } _ { i , t }$ is the prediction of $F P F _ { i , t }$ from the first stage. Finally, $X _ { i , t }$ is a vector of firm-level and state-level control variables, as listed in Section 4.3.3. $\beta$ and π are unknown parameters of the treatment variable (FPF) and instrumental variable (FPG), respectively. Similarly, and $\gamma$ represent the vectors of unknown parameters of the control variables in the first and second stages of two-stage least square regression. $u _ { i , t }$ and $v _ { i , t }$ are error terms that represent unobserved effects. The main coefficient of interest is $\beta ,$ as it estimates the effect of the female proportion of the firm’s inventors $( F P F _ { i , t } )$ on the firm’s future innovation output.

Table 2 presents the key results of the above 2SLS estimation. A significantly large F-statistic (89 and 107)

Table 2. The 2SLS Results – Firm Innovation

<table><tr><td></td><td>Firm SPaRK(1)</td><td>PPI(2)</td><td>Patents (log)(3)</td><td>CPP(4)</td><td>Citations (log)(5)</td></tr><tr><td>FPF (FPG as IV)</td><td rowspan="2">0.321***(0.043)</td><td rowspan="2">5.638***(0.839)</td><td rowspan="2">24.54***(2.65)</td><td rowspan="2">1.445*(0.732)</td><td rowspan="2">14.999***(1.976)</td></tr><tr><td>2SLS robust SE</td></tr><tr><td>IV (F-statistic)</td><td>89</td><td>107</td><td>107</td><td>107</td><td>107</td></tr><tr><td>IV (p)</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>FPF (OLS β)</td><td rowspan="2">0.0037**(0.0018)</td><td rowspan="2">0.323***(0.0456)</td><td rowspan="2">1.06***(0.085)</td><td rowspan="2">0.102(0.0929)</td><td rowspan="2">0.894***(0.0949)</td></tr><tr><td>OLS SE</td></tr></table>

Notes. The effect of inventor gender diversity on firm innovation using 2SLS. Models (1) and (2)–(5) use 18,282 and 21,158 observations respectively. Robust standard errors clustered at the firm level are reported in parentheses. Online Appendix Tables A.14 and A.15 have ful results. All models include firm fixed effects, vear fixed effects, and control variables  
\*Significance at 10%; \*\*significance at 5%; \*\*\*significance at 1%.

Table 3. Firm Financial Performance and Inventor Gender Diversity

<table><tr><td></td><td colspan="4">Dependent variable</td></tr><tr><td>Financial outcomes(Controls = Yes)(Firm FE and Year FE = Yes)</td><td> $PC_{t5}$ (log)(1)</td><td> $ROA_{t5}$ (2)</td><td> $PM_{t5}$ (log)(3)</td><td> $MTB_{t5}$ (log)(4)</td></tr><tr><td>FPF (FPG as IV)</td><td>25.971***(4.097)</td><td>0.806**(0.371)</td><td>2.538***(0.831)</td><td>3.38***(1.369)</td></tr><tr><td>IV (F-statistic)</td><td>41</td><td>33</td><td>33</td><td>33</td></tr><tr><td>IV (p-value)</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Wu-Hausman (p-value)</td><td>&lt;0.001</td><td>0.0108</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Wald test (p-value)</td><td>&lt;0.001</td><td>0.0183</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>Observations</td><td>12,936</td><td>8,852</td><td>8,852</td><td>8,852</td></tr></table>

Notes. The effect of inventor gender diversity on financial outcomes measured at year (t + 5) using Patent Capita (PC), return-on-asset (ROA), profit margin (PM), and market-to-book (MTB) are shown. Robust standard errors clustered at the firm level are reported in parentheses. Variable definitions and full results are in the Online Appendix Tables A.12 and A.17, respectively. FE, fixed effects.  
\*\*Significance at 5%; \*\*\*significance at 1%.

and a p-value less than 0.001 for specifications with different dependent variables (i.e., the innovation measures in different columns of Table 2) from the first stage regression reject the null hypothesis that FPG (gender diversity among graduate students) is a weak instrument for FPF (firm inventor gender diversity).<sup>15</sup> Moreover, as discussed earlier, any effect of FPG on firm innovation is plausibly through FPF (exclusion restriction assumption). Hence, FPG can be used to tease out the causal effect of inventor gender diversity. Second-stage regression’s coefficient and p-value explain the impact of gender diversity on the future innovation output of a firm. As seen in Table 2, column (1), inventor gender diversity at the firm level (FPF) shows a positive and significant effect on Firm SPaRK,<sup>16</sup> which corroborates Hypothesis 1. Our findings substantiate the notion that gender diversity acts as a catalyst for sparking recombinant innovation within firms. Furthermore, Table 2, columns (2)–(5) show positive and significant coefficients for other measures of firm innovation, namely, PPI, Patents (log), CPP, and Citations (log), which further corroborate Hypothesis 1. Our analysis controls for several firm-level variables, including the female proportion of executives, suggesting that the impact of inventor gender diversity on innovation is distinct from any impact that female executives might bring to innovation. For completeness, we also show Fixed-Effect ordinary least squares (OLS) in the last two lines of Table 2, which largely agree with 2SLS. Further, our results are also robust to several estimation and identification checks, such as SIMEX (Simulation and Extrapolation; Online Appendix Section A.6), the difference-in-difference approach (Online Appendix Section A.7), dynamic panel models (Online Appendix Section A.8), and comparing the innovation outcomes of teams with different gender composition within a given firm-year (Online Appendix Section A.9).

These results suggest that having a gender-diverse inventor workforce (i.e., increasing FPF) positively and significantly impacts future firm innovation. This is in concordance with the value-in-diversity perspective we presented in Section 2.1. Also, the results indicate that the negative effects of social categorization (Tajfel et al. 1979, Turner 2010) can be avoided.<sup>17</sup> Given the broader social benefits of gender diversity, it is noteworthy that even statistically insignificant results for FPF would be encouraging, as they would suggest no detrimental effect on firm innovation. Accordingly, our positive and significant findings offer a robust case for cultivating gender diversity among inventors in firms, thereby reconciling the mixed theories and findings in the prior literature.

We also examine whether cost-of-diversity (Cox and Blake 1991) manifests in the financial performance of the firms. We measure the impact of gender diversity on financial performance using two-stage least squares with the proposed instrumental variable (FPG). We measure future financial performance after five years (t + 5) along four dimensions: capital required to replace the patents of a firm, defined as the patent capital (PC); operating performance using return on asset (ROA); profitability measured as profit margin (PM); and valuation from market-to-book (MTB). Our results in Table 3 show that our instrument is not weak and finds that inventor gender diversity has a positive and significant effect on all four measures. In other words, inventor gender diversity not only positively affects future innovation, but the positive impact also appears in the future financial outcomes of firms.

## 5.2. Inventor Gender Diversity and Female Innovation

In this section, we shift our focus to the innovation output of female inventors at firms. Similar to Section 5.1, we use a 2SLS design. However, as detailed in

Table 4. The 2SLS Results – Female Innovation

<table><tr><td></td><td>Firm SPaRK ♀(6)</td><td>PPI ♀(7)</td><td>Patents ♀ (log)(8)</td><td>CPP ♀(9)</td><td>Citations ♀ (log)(10)</td></tr><tr><td>FPF (FPG as IV)</td><td rowspan="2">0.521***(0.18)</td><td rowspan="2">3.304**(1.572)</td><td rowspan="2">10.93***(3.47)</td><td rowspan="2">1.034*(0.675)</td><td rowspan="2">8.701*(5.20)</td></tr><tr><td>2SLS Robust SE.</td></tr><tr><td>IV (F-statistic)</td><td>17.8</td><td>18.6</td><td>18.6</td><td>18.6</td><td>18.6</td></tr><tr><td>IV (p)</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td><td>&lt;0.001</td></tr><tr><td>FPF (OLS β)</td><td>0.003</td><td rowspan="2">0.397**(0.1817)</td><td rowspan="2">1.231***(0.1081)</td><td rowspan="2">-1.385***(0.203)</td><td rowspan="2">-1.263***(0.181)</td></tr><tr><td>OLS SE</td><td>(0.0041)</td></tr></table>

Notes. The effect of inventor gender diversity on female innovation using 2SLS. Models (6) and (7)–(10) use 8,466 and 10,509 observations respectively. Robust standard errors clustered at the firm level are reported in parentheses. Online Appendix Table A.16 have full results. All models include firm fixed effects, year fixed effects, and control variables.  
\*Significance at 10%; \*\*significance at 5%; \*\*\*significance at 1%.

Section 4.3, all of the dependent variables are now representing the innovation measures based only on the patents (from years t + 1 to t + 5) with a female inventor at the firm i. Specifically, the dependent variable, $y _ { i , t } ,$ can be one of the five measures: Firm SPaRK \$, female inventor labor efficiency (PPI \$), Patents \$ (log), CPP \$, and Citations \$ (log). The rest of the setup, including FPG as an instrument, remains the same. We estimate the model using firms with female inventors in the past five years.

The results are presented in Table 4. A high value of statistic (17.8 and 18.6) along with a p-value less than 0.001 for IV from the first-stage regression reject the null hypothesis that the female proportion of graduate (FPG) students is a weak instrument for the female proportion of inventors at a firm (FPF). Based on the estimated coefficients (β) of $F P F _ { i , t }$ from 2SLS, we find that the inventor gender diversity at the firm level has a positive and significant effect on all five dependent variables. The positive and significant coefficients for the variables, Firm SPaRK \$, PPI \$, Patents \$ (log), CPP \$, and Citations \$ (log) corroborate Hypothesis 4. This indicates that having a greater proportion of female inventors at a firm boosts the innovation output of female inventors (i.e., quantity, quality, labor efficiency), while enhancing their recombinant ability. OLS coefficients estimated with fixed-effects models are reported in the last two lines of Table 4. OLS estimates are consistent in direction with 2SLS for Firm SPaRK \$, PPI \$, and Patents \$ (log), but not for CPP \$ and Citations \$ (log). We note that OLS estimates are potentially biased due to endogeneity concerns. Overall, the results indicate that increasing gender diversity benefits both female inventors and firms.

## 6. Mediation Analysis

A female inventor hired by a firm could collaborate on a potential innovation in two ways. She can work with male inventors, leading to female-male collaborations (FMC). She can also collaborate with other female inventors at the firm resulting in femalefemale collaborations (FFC). As illustrated in Figure 2 and also discussed in Section 2.3, FMC and FFC can provide two different pathways mediating the effect of inventor gender diversity on firm innovation.

To tease out the role of the two types of collaborations illustrated in Figure 2, we define two parallel mediators: the number of female-female collaborations (FFC) during the past five years and female-male collaborations (FMC) during the past five years (both log-transformed). Similar to previous sections, we use the FPF to measure gender diversity at the firm level. To measure the future innovation performance of a firm, we use Firm SPaRK, Patents (log), labor efficiency measured using PPI, Citations (log), and CPP, all measured over the next five years (t + 1 to t + 5). Specifically, we are interested in the indirect effect $( \mu _ { T } . { \xi } _ { T } )$ of the path FPF-FMC-Future Innovation and the indirect effect $( \mu _ { B } . { \xi } _ { B } )$ of the path FPF-FFC-Future Innovation. We follow Preacher and Hayes (2008) and use 10,000 bootstraps to estimate the coefficients and the 95% confidence interval of the indirect effects and the direct effect.<sup>18</sup>

Our findings in Table 5 show that the mediation result is “Full Mediation” for Firm SPaRK; “Partial Mediation” for Patents (log) and Citations (log); and “No Mediation” for PPI and CPP. Because Full Mediation or Partial Mediation implies that the type of collaboration among inventors explains how gender diversity affects firms’ innovation outcomes, the results are strongly in line with Hypothesis 2, especially for Firm SPaRK. Further, for the Full Mediation and Partial Mediation, the cross-gender collaboration (FMC) pathway transmits a positive and significant effect. These results together underpin the theoretical insights on how cross-gender collaborations augment innovation, especially the recombinant intensity of firm innovation. However, such diversity, although beneficial, is not as critical for other aspects of firm innovation. Our mediation analysis sheds light on how gender diversity adds value by leveraging female-male collaborations.

Figure 2. Mediation Analysis Paths  
![](/api/attachments/JZFB984W/fulltext/images/dca19e6fa5a5b2bf680a5ad31ad2dc6afc7f46b2498374f820823e87777507e4.jpg)  
Note. The mediation analysis paths diagram shows female-male collaborations (FMC) as a mediator at the top with indirect path effect $\mu _ { T } . \xi _ { T }$ and female-female collaborations (FFC) as a mediator at the bottom with indirect path effec $\mu _ { B } . \xi _ { B }$

Table 5. Mediation Analysis Results

<table><tr><td rowspan="2">Dependent variable</td><td>FMC (log)</td><td>FFC (log)</td><td rowspan="2">Direct effect ( $c'$ )</td><td rowspan="2">Mediation result</td></tr><tr><td>Indirect effect ( $\mu_T.\xi_T$ )</td><td>Indirect effect ( $\mu_B.\xi_B$ )</td></tr><tr><td>Firm SPaRK</td><td>0.0056**[0.0009, 0.012]</td><td>0.004*[-1.28e-04, 0.008]</td><td>0.00797[-0.013, 0.029]</td><td>Full mediation31.9% by FMC</td></tr><tr><td>Patents (log)</td><td>0.0059***[0.004, 0.0079]</td><td>-0.0066***[-0.009, -0.004]</td><td>0.0665***[0.0525, 0.0804]</td><td>Partial9.04% by FMC</td></tr><tr><td>PPI</td><td>0.00023[-0.0006, 0.0011]</td><td>0.00017[-0.001, 0.0014]</td><td>0.0443***[0.0292, 0.0595]</td><td>No mediation</td></tr><tr><td>Citations (log)</td><td>0.0049***[0.0032, 0.0066]</td><td>-0.00526***[-0.00751, -0.003]</td><td>0.0475***[0.0348, 0.06]</td><td>Partial10.4% by FMC</td></tr><tr><td>CPP</td><td>0.0004[-0.0001, 0.0014]</td><td>-0.0005[-0.0021, 0.0012]</td><td>-0.0103[-0.0303, 0.0098]</td><td>No mediation</td></tr></table>

Notes. Indirect effects of two mediators: female-male collaborations (FMC) (log) and female-female collaborations (FFC) (log), the direct effect (c<sup>′</sup>), and the mediation result are reported. The 95% confidence intervals are in brackets. All analyses include controls, firm-fixed effects, and year-fixed effects. The last column shows the mediation result with proportion mediated by the mediators when applicable  
\*Significance at 10%; \*\*significance at 5%; \*\*\*significance at 1%.

## 7. Moderation Analysis

In this section, we examine the moderating impact of two factors: the centrality of female inventors and the presence of a female board member.

## 7.1. Centrality of Female Inventors as Moderator

We examine the role of centrality in the relationship between gender diversity and innovation outcomes using the degree-centrality of female inventors (DCF). The degree-centrality is measured from the network structure of inventors of a firm in the past five years. Specifically, the DCF measures the average number of connections (i.e., coinventor relationships) a female inventor has with male inventors within a firm. We set the indicator variable (DCFI) to one when the DCF of a firm is above the median DCF for the year. Using an interaction between FPF and DCFI in a fixed-effects regression with firm-fixed and year-fixed effects, we find that when female inventors’ centrality is above the median, the effect of gender diversity on innovation outcomes diminishes (see Table 6). This suggests that once female inventors are tightly embedded in key knowledge-exchange channels (as coinventors), the distinct perspectives and information-processing styles offered by more women might not translate into a proportionately larger boost to innovation.

## 7.2. Female Executives on Board as Moderator

Next, we examine if the presence of female executives on the board (FPEI) has any moderating role in the relationship between the gender diversity of inventors (FPF) at firms and the innovation outcomes of firms. Using an interaction between FPF and FPEI in a fixedeffects regression with firm-fixed and year-fixed effects, we find that female executives on the board (FPEI) exert a (negative) moderating influence only for recombinant innovation (Firm SPaRK) but not for other innovation outcomes (see Table 7). In other words, once female executives are positioned at the strategic level of the firm, possibly influencing the innovation processes, the marginal value of additional female inventors for recombinant intensity is diminished.

Table 6. Moderation Analysis – Centrality of Female Inventors

<table><tr><td></td><td></td><td>Firm SPaRK(1)</td><td>PPI(2)</td><td>Patents (log)(3)</td><td>CPP(4)</td><td>Citations (log)(5)</td></tr><tr><td rowspan="2">Role of Centrality of Female Inventors</td><td>FPF</td><td>0.733***(0.12)</td><td>12.869***(2.587)</td><td>59.33***(9.69)</td><td>3.27(3.34)</td><td>35.18***(6.49)</td></tr><tr><td>FPF:DCFI</td><td>-0.468***(0.079)</td><td>-7.88***(1.73)</td><td>-37.9***(6.49)</td><td>-1.99(2.23)</td><td>-21.97***(4.345)</td></tr></table>

Notes. This table shows the role of the centrality of female inventors on the effect of inventor gender diversity on firm innovation and female innovation using firm fixed effects and year fixed effects in the regression. Control variables are included for all models. Models (1) and (2)–(5) use 17,895 and 20,683 observations, respectively. Robust standard errors clustered at the firm leve are reported in parentheses.  
\*\*\*Significance at 1%.

Table 7. Moderation Analysis – Female on Board of Directors

<table><tr><td></td><td></td><td>Firm SPaRK(6)</td><td>PPI(7)</td><td>Patents (log)(8)</td><td>CPP(9)</td><td>Citations (log)(10)</td></tr><tr><td rowspan="2">Role of Femaleon Board</td><td>FPF</td><td>0.318***(0.0419)</td><td>5.64***(0.839)</td><td>24.54***(2.646)</td><td>1.45*(1.03)</td><td>14.99***(1.976)</td></tr><tr><td>FPF:FPEI</td><td>-0.067***(0.0232)</td><td>-0.114(0.488)</td><td>-0.422(1.514)</td><td>-1.197(0.777)</td><td>0.0042(1.19)</td></tr></table>

Notes. This table shows the role of the female board members on the effect of inventor gender diversity on firm innovation and female innovation using firm fixed effects and vear fixed effects in the regression. Control variables are included for all models Models (6) and (7)–(10) use 17,895 and 20,683 observations, respectively. Robust standard errors clustered at the firm level are reported in parentheses.  
\*Significance at 10%; \*\*\*significance at 1%.

Based on Sections 7.1 and 7.2, Hypothesis 3 is supported for all innovation outcomes when the centrality of female inventors is a moderator, but the hypothesis is only supported for recombinant innovation when the presence of a female executive is a moderator.

## 8. Conclusion

In this study, we analyze gender diversity among the most creative scientific workers at firms, namely, patenting inventors. As these individuals predominantly consist of highly skilled STEM workers, our study may provide lessons for the STEM workforce at large. Previous studies on the relationship between gender diversity and firm innovation, particularly gender diversity among R&D employees and at the board level, have produced inconsistent insights. Furthermore, the impact of inventor gender diversity on firms’ recombinant innovation, a critical aspect of innovation that can benefit from heterogeneous viewpoints, remains unexamined. The two competing theoretical viewpoints of value-in-diversity and social categorization highlight the benefits and challenges of gender diversity, respectively. Given these empirical and theoretical tensions, along with the gap in terms of understanding the role of inventor gender diversity on the recombinant intensity of firm innovation, our study brings clarity with the help of a unique data set with a large cross-section of firms over many years and millions of patents. Our results show that gender diversity among a firm’s inventors positively impacts the recombinant intensity and other facets of future firm innovation, such as quantity, quality, and labor efficiency. Our results show that inventor gender diversity positively impacts firms’ future financial performance, suggesting that the benefits of inventor gender diversity financially outweigh the cost of diversity discussed in the literature. We also find that inventor gender diversity has a strong positive effect on the innovation output of female inventors at firms. This is critical, as better performance of female inventors can prevent their exit from the field and also attract new female inventors. Such a self-propagating effect on the productivity of female inventors can benefit not only individual firms but the broader economy. The evidence we present is multifaceted and corroborated with multiple identification strategies. Our results add clarity to the conflicting views within the literature and corroborate the view that the diversity bonus exists for the most creative work.

To address challenges in measuring recombinant innovation, we propose a new text-based measure of recombinant intensity called SPaRK. SPaRK is a novel information artifact that captures the unexpected combination of knowledge domains in a patent, along with their relative contributions to the innovation. SPaRK utilizes recent advances in neural network architecture to capture semantics in text data, while customizing it to the innovation context. We believe that the measure will be useful in future innovation studies. Further, to resolve endogeneity concerns, our study exploits the variation in the gender diversity of the local labor market for prospective inventors as an instrument for inventor gender diversity. Specifically, we use the proportion of local female graduate students in related STEM fields as an IV. Our identification strategy utilizes a two-stage setting with the IV and, hence, allows for causal inferences.

Our study suggests that managers should strive for more gender-diverse inventors, even if it entails challenges and costs related to recruiting and management (Cox and Blake 1991), as it ultimately positively impacts firm innovation. We also find that it is the female-male collaborations that have a mediating effect on the relationship between diversity and innovation outcomes and not the female-female collaborations. This finding has important managerial implications, as it could help managers prioritize cross-gender collaborations. In other words, our results provide a clear and actionable insight for managers that when it comes to recombinant innovation, it is not just the “headcount” of female inventors that matters, but also whether those female inventors are collaborating across gender lines. Also, our moderation analysis suggests that hiring a more gender-diverse inventor workforce is especially relevant when female inventors are not centrally positioned in the firm’s knowledge network. Together, our mediation and moderation analyses enhance our theoretical understanding of how gender diversity impacts innovation with actionable managerial insights.

Given the well-established and widely accepted social benefits of gender diversity, even a statistically insignificant effect of inventor gender diversity on firm innovation would have been noteworthy, as it would nullify the private cost arguments presented in the literature. Because we find a consistently positive and significant impact of inventor gender diversity across a range of innovation measures, our study lends empirical support for efforts to enhance gender diversity in the STEM workforce. Our results demonstrate that gender diversity among inventors sparks innovation, especially of the recombinant type, within firms.

## Endnotes

<sup>1</sup> Refer to Section 3.1 for a detailed discussion on these issues.

<sup>2</sup> We train the embeddings on a larger USPTO corpus that goes beyond the 1.8 million firmlinked patents that enter our econometric panel.

<sup>3</sup> Whereas Yang et al. (2022) find that gender-diverse author teams receive more citations in subfields of medicine, Lerback et al. (2020) find a negative association with citations received in the earth science field.

<sup>4</sup> We do not use generic pretrained vectors such as those using Google News, as is sometimes done using Word2Vec.

<sup>5</sup> In Online Appendix Section A.1, we show that our findings are robust to different embedding sizes (64, 128, and 256), context window sizes (5, 10, 15), cluster sizes (200, 250, 300, and dynamic clusters over the years), and probabilistic clustering.

<sup>6</sup> We use the scikit-learn library implementation.

<sup>7</sup> Term frequency is the number of occurrences of a term in the focal patent. IDF is computed as the log-scaled fraction of the number of patents filed until the year to the number of patents in which the term appeared.

<sup>8</sup> The four APIs are genderize.io, gender-api.com, gender-guesser package in python, and gender package in R.

<sup>9</sup> Refer to Online Appendix Section A.3 for more details on the datacollection process.

<sup>10</sup> Our results are robust to excluding the unidentified inventors and to different probability cut-offs.

<sup>11</sup> We find consistent results with three- and seven-year windows. Results are also consistent with alternate definitions of gender diversity using Shannon entropy and Blau’s Index (Online Appendix Section A.5).

<sup>12</sup> Angrist and Pischke (2009, p. 53) argue that instrumental variables can be used to address both omitted variable bias and error in measurement of variables

<sup>13</sup> The choice of health (H) into a group while keeping science and engineering (S&E) together is based on clear availability one-to-one mapping of a field to a SIC code.

<sup>14</sup> Our results are similar using the average value instead of median. Refer to Online Appendix Table A.14.

<sup>15</sup> In a battery of unreported results, we find that our IV is a valid instrument using Stock and Yogo, using Cragg and Donald F-statistic, Kleibergen-Paap rank LM statistic, Anderson canonical LM statistic test, and bootstrap inference.

<sup>16</sup> Our results are consistent with CPC-based recombinant innovation as well (Online Appendix Table A.18).

<sup>17</sup> For robustness, we also test for “critical mass theory” (Kanter 1977) that suggests a positive effect of diversity only after a “critical mass” is achieved but do not find support for it (refer to Online Appendix Table A.19).

<sup>18</sup> Please refer to the Online Appendix Section A.10 for the detailed model specification.

## References

Abbasi A, Sarker S, Chiang RH (2016) Big data research in information systems: Toward an inclusive research agenda. J. Assoc. Inform. Systems 17(2):3.

Ahuja G, Morris Lampert C (2001) Entrepreneurship in the large corporation: A longitudinal study of how established firms create break through inventions. Strategic Management J. 22(6–7):521–543.

Ahuja MK, Galletta DF, Carley KM (2003) Individual centrality and performance in virtual R&D groups: An empirical study. Management Sci. 49(1):21–38.

Alca´cer J, Gittelman M, Sampat B (2009) Applicant and examiner citations in U.S. patents: An overview and analysis. Res. Polic 38(2):415–427.

An H, Chen CR, Wu Q, Zhang T (2021) Corporate innovation: Do diverse boards help? J. Financial Quant. Anal. 56(1):155–182.

Angrist JD, Pischke JS (2009) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton University Press, Princeton, NJ).

Arora A, Belenzon S, Rios LA (2014) Make, buy, organize: The interplay between research, external knowledge, and firm structure. Strategic Management J. 35(3):317–337.

Bell A, Chetty R, Jaravel X, Petkova N, Van Reenen J (2019) Who becomes an inventor in America? The importance of exposure to innovation. Quart. J. Econom. 134(2):647–713.

Bena J, Ferreira MA, Matos P, Pires P (2017) Are foreign investors locusts? The long-term effects of foreign institutional ownership. J. Financial Econom. 126(1):122–146.

Bhaskarabhatla A, Cabral L, Hegde D, Peeters T (2021) Are inventors or firms the engines of innovation? Management Sci. 67(6): 3899–3920.

Bostwick VK, Weinberg BA (2022) Nevertheless she persisted? Gender peer effects in doctoral STEM programs. J. Labor Econom. 40(2):397–436.

Cady SH, Valentine J (1999) Team innovation and perceptions of consideration: What difference does diversity make? Small Group Res. 30(6):730–750.

Cahill L (2006) Why sex matters for neuroscience. Nat. Rev. Neurosci. 7(6):477–484.

Carnabuci G, Operti E (2013) Where do firms’ recombinant capabili ties come from? Intraorganizational networks, knowledge, and firms’ ability to innovate through technological recombination. Strategic Management J. 34(13):1591–1613.

Cox TH, Blake S (1991) Managing cultural diversity: Implications for organizational competitiveness. Acad. Management Perspect. 5(3):45–56.

Cropley D, Cropley A (2017) Innovation capacity, organisational culture and gender. Eur. J. Innovation Management 20(3):493–510.

Ding WW, Murray F, Stuart TE (2006) Gender differences in patent ing in the academic life sciences. Science 313(5787):665–667.

D´ıaz-Garc´ıa C, Gonza´lez-Moreno A, Sa´ez-Mart´ınez FJ (2013) Gender diversity within R&D teams: Its impact on radicalness of innovation. Innovation 15(2):149–160.

Dong JQ, Yang CH (2019) Information technology and innovation outcomes: Is knowledge recombination the missing link? Eur. J. Inform. Systems 28(6):612–626.

Faems D, Subramanian AM (2013) R&D manpower and technological performance: The impact of demographic and task-related diversity. Res. Policy 42(9):1624–1633.

Ferna´ndez J (2015) The impact of gender diversity in foreign subsidiaries’ innovation outputs. Internat. J. Gender Entrepreneurship 7(2):148–167.

Fleming L (2001) Recombinant uncertainty in technological search. Management Sci. 47(1):117–132.

Galunic DC, Rodan S (1998) Resource recombinations in the firm: Knowledge structures and the potential for Schumpeterian innovation. Strategic Management J. 19(12):1193–1201.

Gonzalez-Moreno A, D´ıaz-Garc´ıa C, Sa´ez-Mart´ınez FJ (2018) R&D team composition and product innovation: Gender diversity makes a difference. Eur. J. Internat. Management 12(4):423–446.

Griffin D, Li K, Xu T (2021) Board gender diversity and corporate innovation: International evidence. J. Financial Quant. Anal. 56(1):123–154.

Griliches Z (1998) Patent statistics as economic indicators: A survey. R&D and Productivity: The Econometric Evidence (University of Chicago Press, Chicago), 287–343.

Halkos GE, Kitsos C (2012) Relative risk and innovation activities: The case of Greece. Innovation 14(1):156–159.

Hall B, Jaffe A, Trajtenberg M (2001) The NBER Patent Citation Data File: Lessons, insights and methodological tools. NBER Working Paper No. 8498, National Bureau of Economic Research, Cambridge, MA.

Halpern DF (2011) Sex Differences in Cognitive Abilities (Psychology Press, Hove, UK).

Han L, Tian Z, Wojan TR, Goetz SJ (2024) Testing biasedness of self reported microbusiness innovation in the annual business survey. PLoS One 19(1):e0296667.

Hevner AR, March ST, Park J, Ram S (2004) Design science in infor mation systems research. MIS Quart. 28(1):75–105.

Hirshleifer D, Hsu PH, Dongmei L (2018) Innovative originality, profitability, and stock returns. Rev. Financial Stud. 31(7): 2553-2605.

Hunt J (2016) Why do women leave science and engineering? ILR Rev. 69(1):199–226.

Hunt J, Garant JP, Herman H, Munroe DJ (2013) Why are women underrepresented amongst patentees? Res. Policy 42(4):831–843.

Igbaria M, Baroudi JJ (1995) The impact of job performance evaluations on career advancement prospects: An examination of gen der differences in the IS workplace. MIS Quart. 19(1):107–123.

Joseph D, Ang S, Slaughter SA (2015) Turnover or turnaway? Competing risks analysis of male and female IT professionals job mobility and relative pay gap. Inform. Systems Res. 26(1): 145–164.

Joshi KD, Chi L, Datta A, Han S (2010) Changing the competitive landscape: Continuous innovation through IT-enabled knowl edge capabilities. Inform. Systems Res. 21(3):472–495.

Kanter RM (1977) Men and Women of the Corporation (Basic Books, New York).

Kaplan S, Vakili K (2015) The double-edged sword of recombination in breakthrough innovation. Strategic Management J. 36(10):1435–1457.

Keupp MM, Gassmann O (2013) Resource constraints as triggers of radical innovation: Longitudinal evidence from the manufacturing sector. Res. Policy 42(8):1457–1468.

Kleis L, Chwelos P, Ramirez RV, Cockburn I (2012) Information technology and intangible output: The impact of IT investment on innovation productivity. Inform. Systems Res. 23(1):42–59.

Kogan L, Papanikolaou D, Seru A, Stoffman N (2017) Technological innovation, resource allocation, and growth. Quart. J. Econom. 132(2):665-712

Langer N, Gopal RD, Bapna R (2020) Onward and upward? An empirical investigation of gender and promotions in information technology services. Inform. Systems Res. 31(2):383–398.

Lerback J, Hanson B, Wooden P (2020) Association between author diversity and acceptance rates and citations in peerreviewed earth science manuscripts. Earth Space Sci. 7(5): e2019EA000946.

Li GC, Lai R, D’Amour A, Doolin DM, Sun Y, Torvik VI, Amy ZY, Fleming L (2014) Disambiguation and co-authorship network of the U.S. patent inventor database (1975–2010). Res. Polic 43(6):941–955

Meyers-Levy J, Maheswaran D (1991) Exploring differences in males’ and females’ processing strategies. J. Consumer Res. 18(1):63–70.

Mikolov T, Chen K, Corrado G, Dean J (2013) Efficient estimation of word representations in vector space. Preprint, submitted Sep tember 7, https://arxiv.org/abs/1301.3781.

Nielsen MW, Alegria S, Bo¨rjeson L, Etzkowitz H, Falk-Krzesinski HJ, Joshi A, Leahey E, Smith-Doerr L, Woolley AW, Schiebinger L (2017) Gender diversity leads to better science. Proc. Natl Acad. Sci. USA 114(8):1740–1742.

Padmanabhan B, Fang X, Sahoo N, Burton-Jones A (2022) Editor’s comments: Machine learning in information systems research. MIS Quart. 46(1):iii–xix.

Page SE (2017) The Diversity Bonus: How Great Teams Pay Off in th Knowledge Economy (Princeton University Press, Princeton, NJ).

Paruchuri S, Awate S (2017) Organizational knowledge networks and local search: The role of intra-organizational inventor networks. Strategic Management J. 38(3):657–675.

Preacher KJ, Hayes AF (2008) Asymptotic and resampling strategies for assessing and comparing indirect effects in multiple mediator models. Behav. Res. Methods 40(3):879–891.

Richard OC (2000) Racial diversity, business strategy, and firm performance: A resource-based view. Acad. Management J. 43(2): 164–177.

Ruiz-Jime´nez JM, Fuentes-Fuentes MdM, Ruiz-Arroyo M (2016) Knowledge combination capability and innovation: The effects of gender diversity on top management teams in technologybased firms. J. Bus. Ethics 135(3):503–515.

Saldanha TJ, Mithas S, Krishnan MS (2017) Leveraging customer involvement for fueling innovation. MIS Quart. 41(1):267–286.

Saldanha TJ, Sahaym A, Mithas S, Andrade-Rojas MG, Kathuria A, Lee HH (2020) Turning liabilities of global operations into assets: IT-enabled social integration capacity and exploratory innovation. Inform. Systems Res. 31(2):361–382.

Schumpeter JA (1934) The Theory of Economic Development: An Inquiry into Profits, Capital, Credit, Interest, and the Business Cycle (Har vard University Press, Cambridge, MA).

Sorenson O, Fleming L (2004) Science and the diffusion of knowl edge. Res. Policy 33(10):1615–1634.

Strumsky D, Lobo J (2015) Identifying the sources of technological novelty in the process of invention. Res. Policy 44(8):1445–1461.

Tajfel H, Turner JC (1979) An integrative theory of intergroup conflict. Austin WG, Worchel S, eds. The Social Psychology of Intergroup Relations (Brooks/Cole, Monterey, CA), 33–47.

Teruel M, Segarra-Blasco A (2022) Gender, occupational diversity of R&D teams and patents generation: An application to Spanish firms. R&D Management 52(3):517–529.

Torchia M, Calabro \` A, Huse M (2011) Women directors on corporate boards: From tokenism to critical mass. J. Bus. Ethics 102: 299–317.

Trajtenberg M (1990) A penny for your quotes: Patent citations and the value of innovations. RAND J. Econom. 21(1):172–187.

Trajtenberg M, Henderson R, Jaffe A (1997) University versus corporate patents: A window on the basicness of invention. Econom. Innovation New Tech. 5(1):19–50.

Turner JC (2010) Towards a cognitive redefinition of the social group. Research Colloquium on Social Identity of the European Laboratory of Social Psychology, Dec, 1978, Universite ´ de Haute Bretagne, Rennes, France (Psychology Press, Hove, UK), 15–40.

Whalen R (2018) Boundary spanning innovation and the patent system: Interdisciplinary challenges for a specialized examination system. Res. Policy 47(7):1334–1343.

Woolley AW, Chabris CF, Pentland A, Hashmi N, Malone TW (2010) Evidence for a collective intelligence factor in the perfor mance of human groups. Science 330(6004):686–688.

Xie L, Zhou J, Zong Q, Lu Q (2020) Gender diversity in R&D team and innovation efficiency: Role of the innovation context. Res. Policy 49(1):103885.

Xue L, Ray G, Sambamurthy V (2012) Efficiency or innovation How do industry environments moderate the effects of firms IT asset portfolios? MIS Quart. 36(2):509–528.

Yang Y, Konrad AM (2011) Diversity and organizational innovation: The role of employee involvement. J. Organ. Behav. 32(8):1062–1083.

Yang Y, Tian TY, Woodruff TK, Jones BF, Uzzi B (2022) Gender diverse teams produce more novel and higher-impact scientifi ideas. Proc. Natl. Acad. Sci. USA 119(36):e2200841119.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
