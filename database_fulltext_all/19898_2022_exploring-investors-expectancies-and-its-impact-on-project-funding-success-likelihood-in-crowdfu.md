---
otero_id: 19898
otero_key: "DM82PVHW"
title: "Exploring investors' expectancies and its impact on project funding success likelihood in crowdfunding by using text analytics and Bayesian networks"
authors: "Francis Joseph Costello; Kun Chang Lee"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113695"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Exploring investors' expectancies and its impact on project funding success likelihood in crowdfunding by using text analytics and Bayesian networks

![](/api/attachments/DM82PVHW/fulltext/images/dceeb9fdccc005e7904d177488030f9e16e49a441bca46cc75c44697616c0f92.jpg)

Francis Joseph Costello <sup>a</sup>, Kun Chang Lee <sup>a,b,\*</sup>

<sup>a</sup> SKK Business School, Sungkyunkwan University, Seoul 03063, Republic of Korea <sup>b</sup> Department of Health Sciences & Technology, Samsung Advanced Institute for Health Sciences & Technology (SAIHST), Sungkyunkwan University, Seoul 06355, Republic of Korea

## A R T I C L E I N F O

Keywords: Crowdfunding Entrepreneurial Narratives Language expectancy theory Theory of Vagueness Text analytics Bayesian networks

## A B S T R A C T

Crowdfunding has become immensely popular today, allowing entrepreneurs to present innovative ideas to a broad audience of potential investors. However, due to the online nature of crowdfunding, investors have to use clues only available on the website to decide on whether to invest or not. Grounded in language expectancy theory (LET), we proposed and tested hypotheses suggesting that, when no knowledge of the entrepreneur is available, investors have to use language expectancy as a way to inform them on their investment decisions. Furthermore, we propose that communication content in entrepreneurial narratives such as vague communi cation and linguistics affect the quality of information leading to a violation of language expectancy. We also postulate that this will manifest in affect intensity and in two-sided persuasion. We separated the description and risks and challenges (R&C) sections from Kickstarter and performed discrete analyses with regressions to further test two-sidedness. Next, we sought to understand causal knowledge of the underlying target class by imple menting a Bayesian Network to find the conditional probability of the variables before attempting to find a nearoptimal probability of funding success using a genetic algorithm. We found robust support for our hypotheses and helped shed light on which information is received and interpreted by investors leading to a greater like lihood of funding success. Overall, this approach sheds new light on the role of language within crowdfunding literature.

## 1. Introduction

These days, crowdfunding platforms such as Kickstarter offer en trepreneurs and artists a novel and vital means of procuring finance for new innovative ideas [1]. Although many success stories exist, perfect ing a proposal is not easy; 63% of all Kickstarter projects fail [2]. Rea sons can manifest from the online nature of crowdfunding, whereby separation of entrepreneurs and investors means that information asymmetries occur [3]. Confronted with uncertainty, investors must evaluate a project based on only the information provided. Thus, nascent challenges in establishing credibility exist in abundance. Another potential reason for this lies in the initial financing stages; in vestors must rely on intangible cues, such as descriptions, to compre hend the product idea. Thus, entrepreneurial narratives have been proposed as a vital part of a crowdfunding proposal [1,4–6]. Entrepre neurial narratives deliver a personalized account of the projects' vision while articulating the investment prospects. It also provides insight into the person behind the project to potential investors. Accordingly, it reasons to say that the projects' narrative communicative style is as important as the idea itself in persuading investors of the entrepreneurs' credibility [6]. What entrepreneurs communicate (hereafter communi cation content) has been shown to play an essential role in crowdfunding proposals. Hence, the exploration of language is gaining increased in terest in entrepreneurship literature [7,8].

Much of the prior work concerning communication content has highlighted aspects that potential investors can use as signals of entre preneurial credibility. For example, examinations on the quality of the information provided on a product [9], social networks of the entre preneurs [10–12], and privacy cues [13]. More recently, the verbal content of project proposals has been studied to help understand communication content [1,4,11]. However, following an extensive re view on communication content in crowdfunding literature (Table A.1), we found three omissions in the current literature: (1) an understanding of the use of vague language in influencing crowdfunding success, (2) a distinct analysis on both the description and the R&C section, (3) and lastly, a method for optimizing the combination of features that will result in the highest probable causes of project success.

Our study addresses these with a novel method for extracting and analyzing vagueness<sup>1</sup> within textual data obtained from Kickstarter. Vagueness is a language used in everyday discourse that signals that the communicator does not have the sufficient knowledge or understanding necessary for effective communication [14]. Prior literature on competitive dynamics has shown that vagueness can help to confuse rival firms [15] and prevent market entry [16]. Despite this, analysis of its individual effects, mainly when used within entrepreneurial narra tives, is unexplored. For example, suppose vague stylistic language is present. In that case, it is reasonable to assume that entrepreneurs lack the required knowledge to portray a credible case that deserves rational attention from potential investors. Consequently, investors will avoid these entrepreneurial ideas due to issues of credibility.

Another issue of credibility arises due to the nature of online tech nology. Platforms do not facilitate direct face-to-face communication between two parties. When such a barrier exists, literature has shown that the two-sidedness proposition should be utilized. For example, Jensen et al. [17] showed increased credibility in anonymous product reviews when positive and negative aspects were presented. Conse quently, we posit that crowdfunding investors will also utilize the twosidedness of the entrepreneurs' argument to assist in their decisionmaking—more recent proposals on Kickstarter force users to consider the R&C of their projects. Doing so opens an avenue in which to assess the two-sidedness proposition within crowdfunding research directly. Although prior studies have explicitly stated the collection of R&C data [1,18], a discrete analytical investigation of each section was not made. This is problematic as prior research has shown that linguistic style [7], language preferences [8], and semantics [19,20] can all influence funding success and that differences in these variables should naturally exist upon further investigation. Such an analysis can provide unique implications on how investors interpret each side of the entrepreneurial narrative.

Lastly, this is the first paper to analyze communication content with a probabilistic Bayesian network-based decision support mechanism (BNM) to the best of our knowledge. Specifically, we use the significant variables found within multiple regression analyses to identify proba bilistic causal features to help predict funding success. Usually, such a task requires expert knowledge to analyze causal relationships on the target variable. However, in the BNM method, we implemented an evolutionary search heuristic based on a Genetic algorithm (GA) to machine-learn these probabilistic causal features. This approach allows for an near-optimal explanation based on a thorough and concise exploration of the features causing the most probable cause of funding success [21]. In this work, we focus on the communication content embedded within Kickstarter entrepreneurial narratives by implement ing a persuasion model that focuses on the language expectancies of investors. We follow and expand upon prior work investigating lin guistics and language preferences in entrepreneurial narratives [7,8] by exploring textual vagueness and the two-sidedness proposition. The theoretical approach, hypotheses, method, and results are explored in the following sections.

## 2. Crowdfunding and entrepreneurial narratives

Crowdfunding is immensely popular today, allowing entrepreneurs to present innovative ideas to a broad audience of potential investors. In addition, this medium provides a novel avenue for entrepreneurs to take their ideas to the crowd directly [22], moving the source of finance from traditional means to everyday people [3]. Multiple reward avenues for investing within crowdfunding exist, including reward-, equity-, lending-, and donation-based [18]. This study investigates a rewardbased platform: Kickstarter. Kickstarter allows a wide variety of pro jects, including arts and design, technology, and games. If an investor backs an entrepreneur in reward-based crowdfunding, they will receive a non-financial reward in exchange for the monetary contribution [18] if the project is successful [23]. To date, just under 200,000 projects have been funded successfully on Kickstarter, amounting to just under 19 million total backers and over 5 billion dollars of investment [24].

Online crowdfunding is a moderately recent yet growing phenome non. While studies first focused on the overarching phenomenon and basic mechanisms [10,12], recent literature has investigated more nuanced features of the funding process. As a result, scholars now investigate questions surrounding investor experience and roles, infor mation provision mechanisms, informational value [3,22,23], culture and geography [25], and privacy assurances [13]. More recently, re searchers have explored the role of language [26], including entrepre neurial narratives. For instance, it has been shown that project success can be influenced by entrepreneurial narratives such as narcissism [4], positive tones [1,11], ongoing journey vs. results-in-progress [28], subjectivity vs. objectivity [6], as well as entrepreneurial vs. project idea narratives [5]. Other studies have also used lexicon-based dictionaries that explore constructs such as monetary evidence, female and social aspects, and affect-based tones [8,28–30].

In general, crowdfunding literature has drawn parallels with tradi tional investment processes using extant theories such as signaling theory [1,3,6,30] and market mechanism [22]. However, crowdfunding investors are typically laypersons without formal investment training. Furthermore, their investments amount to small financial capital compared to traditional sources. The nature of crowdfunding suggests that backers of crowdfunding projects are not investing in means that make sense within more traditional investment literature. Given this, the use of traditional entrepreneurial and investment theories may not provide the fundamental principles needed to understand crowdfund ing, requiring the search for an alternative theoretical lens.

## 3. Theory and hypotheses

## 3.1. Language expectancy theory and credibility

In this study, LET is utilized to provide the foundational inquiry surrounding language used in entrepreneurial narratives seen in crowdfunding campaigns [31]. LET is premised on the assumption that individuals have certain expectations formed by observing specific language behavior that is rule-based. Such expectations are grounded in interpersonal, social, and cultural norms [7,32], leading to expectations developing based on appropriate communication styles [31,32]. Upon viewing language, ones' experiences and expectations can affect the individuals' acceptance or rejection of a persuasive message [33,34]. However, LET also postulates that expectations are not unique to any individual but rather to specific communicators that can aggregate into groups, i.e., online shoppers [17] or investors [7].

LET views some groups as privileged to use specific language and remain more persuasive over other groups based on group identities. For instance, privileged groups may use more aggressive language that ranges in low to high intensity and remain persuasive, whereas the same cannot be said for nonprivileged groups [31,32,34]. This range in ones ability to persuade based on techniques fitting to their group identity is known as a senders' bandwidth [17,35]. When persuasive language is used outside of this bandwidth, an expectancy violation is committed and can manifest in two forms: negative and positive violations [33,34]. Negative violation of expectations reduces the credibility of the communication sender resulting in less persuasion and attitude change. Conversely, positive violations garner credibility, foster persuasion, and increase the likelihood of the communication receiver adopting the advocated attitude [32].

LET within crowdfunding provides a unique yet distant application of the theory from its traditional beginnings. Online crowdfunding constrains users to know little about each persons' characteristics, and there is no guarantee of the entrepreneurs' true intentions. The only known facts are that entrepreneurs were sufficiently motivated to pro pose an idea looking for financial support. Importantly, as no knowledge on which group identity an entrepreneur belongs to is known on crowdfunding, operationalizing sender bandwidth on known group identity is not feasible.

In the absence of knowing, high and low intensity and aggressive or non-aggressive language traits cannot readily explain expectancy vio lations of entrepreneurial narratives. At this point, expectancy can only arise from the accepted norms in the language itself. Jensen et al. [17] validated this notion, showing that anonymous product reviews' twosidedness and affect intensity provided language expectancy viola tions. Like Jensen et al. [17], we assume a narrow bandwidth will be afforded for persuasion resulting in a higher chance of language ex pectancy violations that affect credibility. Prior crowdfunding literature has proposed that linguistics used by social and commercial entrepre neurs [7] and the language preferences of investors [8] can violate ex pectations. Furthermore, [7,8] show that the language properties of an entrepreneurs' narrative can play a significant role in influencing in vestors' judgment of credibility. Based on LET, we explore four communication content features that we propose influence investors expectations: vague communication, linguistic features, affect intensity, and two-sided persuasion.

## 3.2. Vague communication

Based on the Theory of Vagueness, vagueness appears when “borderline cases” of language is used, making such language “doubtful” or “ill-defined.” Consequently, the use of such language makes it impossible to assert or deny its application [36]. Hiller further defines vagueness as a psychological construct representing the ‘state of mind of a communicator who does not sufficiently command the facts, knowledge, or understanding required for maximally effective commu nication [14]. The pioneering work of vagueness originates in the edu cation field, where Miller and his colleagues' observations in lecturing led to the development of the vagueness dictionary [14]. However, the theory of vagueness has its roots in semantics and epistemology [37]. Therefore, the study of vagueness within crowdfunding communication content is of value too. Although the evolutionary reasons for using vague language are unclear [36], vague language is still persistent and plentiful in everyday discourse, providing valid grounds for further scholarly inquiry enveloping entrepreneurial narratives. In essence, too much vagueness in a crowdfunding proposal may confuse the projects vision. In addition, the presence of vague language could signal to the investor that the entrepreneur lacks the required knowledge needed for a successful implementation of the idea. This is problematic given that credibility suggests the source is knowledgeable [30], and thus, vague language may have a critical influence on the likelihood of obtaining investment.

Examples of vagueness include qualifiers before numbers, nonnumerical terms to refer to indefinite amounts, and approximation. It also encompasses language such as bluffing that shifts comprehensions responsibility onto the reader. Vague language exerts more demands on the receiver of such communication to translate the given information, even in noncomplex language [15,16]. In this study, we interpret vagueness as a contributor to information quality. We posit that the vaguer the language presented, the greater the likelihood that the quality of the information presented will decrease. As an investor, this will make reading the entrepreneurial narrative a more cognitive task, and thus, grasping the context needed to make an informed decision will decrease. An investor will have a negative language expectancy viola tion resulting in reduced attitudinal change and no investment. Thus,

H1. : High use of vague language in entrepreneurial narratives will reduce the likelihood of investment in online crowdfunding.

## 3.3. Linguistic features

Linguistic features used within communication content can play an essential role in entrepreneurial narratives. Linguistic features are a direct way for potential investors to get close to the entrepreneur while remaining anonymous. As they are not dependent on the entrepreneurs expectations on what the investors may or may not expect, entrepre neurs have flexibility in their linguistic style by carefully planning and rehearsing their proposal [7]. Effective use of linguistic features can signal entrepreneurs' care in formulating their ideas to help reassure investors that they are capable and driven to deliver on their promise [38]. Furthermore, the correct use of linguistics can help build a rela tionship with an audience and keep investors engaged in the content [7,8,38]. The effective use of linguistics has been seen in P2P lending, where appropriate linguistics led to enhanced persuasion and increased lending behavior [39]. In addition, research on fraud detection showed that non-fraudulent financial disclosures had higher lexical word di versity, suggesting that particular linguistics can be more credible [40]. Following prior crowdfunding research [7] we also adopt the notion that linguistic styles used by entrepreneurs on crowdfunding platforms will impact an investment decision. Therefore, through the lens of LET, we examine three linguistic features: descriptive language, paragraph structure, and reading ease.

Within crowdfunding entrepreneurial narratives, entrepreneurs are tasked with explaining their product. It has been shown that the greater use of descriptive language can contribute to the reader's ability to obtain integrated information as a more detailed description of an object can be made [41]. For example, research within online shopping has shown that when reviews display more detailed information about products, consumers deem this more informative and of greater quality [42]. The same notion can be applied to crowdfunding. Any entrepre neurs who do an exhausting job detailing their product to potential in vestors will make more informed decisions based on integrated information. It reasons to say, compared with entrepreneurs that do not use much descriptive language, ones that do will be favored by informed investors creating a positive expectancy violation based on greater in formation quality. The result of this positive language expectancy violation will be increased attitudinal change by the investor. Therefore, we hypothesize:

H2a. : High use of descriptive language in entrepreneurial narratives will increase the likelihood of investment in online crowdfunding

Paragraph structure is determined by how much information an entrepreneur provides in their communication content. This information is an essential tool for the entrepreneur as nearly all projects on crowdfunding are at the beginning stages of their life cycle and thus are usually unproven and intangible to the potential investors. Thus, the information provided on the crowdfunding page is the primary source of factual information an investor can use. Providing information that potential investors can evaluate the project with will be vital for credi bility [43]. If more information is provided, then it is expected that potential investors will positively react to more factual information within the communication content. We posit that this will lead to a positive language expectancy violation and increase the persuasiveness of the narrative. The result will be increased project funding, and therefore, we hypothesize:

H2b. : Longer paragraph structure in entrepreneurial narratives will in crease the likelihood of investment in online crowdfunding.

In communication research, it is well known that simple language than complex language can be more effective for persuasiveness. It has been shown that comprehension of language that matches that of the reader's ability plays a crucial role in engaging the reader [33] and can provide greater credibility even in circumstances of anonymity [17]. Research has shown that language complexity is an important feature in communication interpretability and persuasiveness [44]. In crowd funding, entrepreneurs are unaware of who the potential investors are. Nonetheless, they should assume that they have a good grasp of lin guistic complexity based on formal education. If an entrepreneur were to present their project with poor readability, it would be hard to follow, disengaging a potential investor. For instance, if a potential investor has high cognitive complexity and sees poor use of language within communication content, it will likely result in a negative language ex pectancy violation. As linguistics and linguistic complexity have evolved through social norms, we postulate that any departure from these, especially to a more linguistically complex investor, will result in a negative language expectancy violation, reducing the persuasiveness of the entrepreneurs' arguement [33]. This will reduce the entrepreneur's investment opportunity and hence:

H2c. : Low reading ease in entrepreneurial narratives will reduce the likelihood of investment in online crowdfunding.

## 3.4. Affect intensity

Affect intensity can be defined as the number of emotion-laden words used within the text. Affect is defined within a spectrum that ranges from very negative to very positive sentiment. Previous crowd funding research has shown that affect intensity within the descriptions of entrepreneurial narratives can have mixed effects. For example, Zhou et al. [43] found that positive affect intensity had a more significant impact, whereas Jiang et al. [45] found that positive and negative affect significantly influenced crowdfunding success. In this study, the role of affect cannot be overestimated. The direct use or absence of affect is not the direct cause of persuasion, and in isolation, will not promote entrepreneurial credibility. Instead, it combines the preordained ex pectations determined by the online setting and context and how these are violated using affect within entrepreneurial narratives [17]. Accordingly, it is conceptually reasonable to assume that the description and R&C section will have varied expectations of sentimental language. This is because the description section is used for shining light on the entrepreneurial idea to gain interest and positive reactions from in vestors. In contrast, the R&C section is designed for entrepreneurs to display potential adverse outcomes. Investigation into fraudulent doc uments has shown that when more positive sentiment is used within serious documents. it is usually because the communicator wants to hide any negative aspects [40]. Within the crowdfunding R&C section, en trepreneurs are asked to provide serious deliberation on potential negative aspects of the project and how they can deal with them if they arise. Therefore, we suggest that the description section will allow for a narrow bandwidth for positive affect. Thus, a positive language expec tancy violation will occur if this is present within the communication content. For the R&C section, we suggest no such luxury will be affor ded. If the R&C section is too positively toned, investors will have a negative language expectancy violation as the argument will be less credible leading to no investment. We therefore hypothesize:

H3a. : Positive affect intensity in the project description will increase the likelihood of investment in online crowdfunding.

H3b. : Positive affect intensity in the risk and challenges will lead to a decreased likelihood of investment in online crowdfunding.

## 3.5. Two-sided persuasion

The introduction of the R&C section within the Kickstarter platform was a direct attempt to nudge entrepreneurs into thinking about, deliberating on, and finally presenting any potential issues that could arise in a project. Within Kickstarter, the description is the positive as pects of the entrepreneurial idea, whereas the R&C is the potential negative aspects. Together they form a two-sided persuasive argument for investors. Research on product reviews in IS [17] and marketing [46] has shown that two-sided messages represent a central form of persua sive communication. When viewers of communication do not know the communicators' reputation or other credibility signals (like in crowd funding), relying on two-sided arguments can help designate the communicator as credible [17].

Prior crowdfunding research has explored the role of semantical topics. For instance, Jiang et al. [45] explored narratives from the Chi nese platform dreamore and found greater funding success when en trepreneurs talked about dreams and creative aspects of the idea. Lee and Sohn [20] also explored semantic topics seen in crowdfunded software projects on Kickstarter. This study provided good information to aspiring software entrepreneurs on which topics to explore in the description section. Despite this, no crowdfunding research has shed light on the effect of specific semantic topics in the R&C section. This study attempts to identify the semantic topics that create a successful two-sided argument within entrepreneurial narratives. We postulate that compared to a one-sided entrepreneurial narrative; the use of compelling semantic topics that present a two-sided argument will be positively evaluated by potential investors. Thus, those entrepreneurs who move away from a one-sided message may increase the likelihood of a positive violation of a potential investor's expectations. This lan guage expectancy violation would then increase credibility attributed to the entrepreneur's arguement, and thus we hypothesize:

H4. : Semantic topics that display effective two-sidedness in the risks and challenges section will increase the likelihood of investment.

## 4. Dataset and methods

This paper used a text analytical framework to understand the effects of communication content within entrepreneurial narratives on crowd funding success (see Fig. 1). Specifically, data was crawled from Kickstarter between 2015 and 2020 and then cleaned into an experi mental dataset. Next, vagueness, linguistic, affect intensity, and se mantic topics were all extracted from the text. Next, the projects' success or failure was analyzed using logistic regression, while ordinary least squares regression was employed for examining the continuous variable of funding percent. Lastly, a Bayesian network analysis was employed for understanding causal knowledge of funding percent.

## 4.1. Data engineering

## 4.1.1. Data crawling and preprocessing

First, we collected Kickstarter URLs from webrobots.com.<sup>2</sup> We removed duplicates from this list, as well as variables that provided no information. Further, only projects with either a success or failure status were retained. For the textual data, the following preprocessing steps were necessary: (1) Projects that had no textual data were removed; (2) projects with less than five words in both the description and R&C section were dropped from the analysis; and (3) non-English projects were identified and dropped using langdetect.<sup>3</sup> The final dataset included 28,103 projects, 17,598 failed, and 10,496 successful.

![](/api/attachments/DM82PVHW/fulltext/images/f448aa88c5e165535cef18dfbcfa9f812141ac5b1cbcc8ef3ddf975e5a0d940a.jpg)  
Fig. 1. Text analytical framework used within this study.

## 4.1.2. Hiller's vagueness dictionary, contranyms, and polysemy

We employed Hiller's communication vagueness dictionary [14] to extract vague communication from the text. This included the extended vague categories proposed in [47]. The final lexicon consisted of 377 words that help form vague communication within the English language (see Table 1). Two further categories were used for detecting vagueness, namely contranyms and polysemy. Contranyms are words that have two contradictory meanings and produced a lexicon consisting of 176 words [47]. Polysemy is a form of lexical ambiguity that leads to vagueness. These word forms have distinct meanings and cannot be used in the same sentence [48]. Finally, we included words that have twelve or more meanings providing a 517-word lexicon.

Scores based on these lexicons were extracted with our proposed adaption of the TF-IDF algorithm. First, Eq. (1) shows the term fre quency TF of a vague word t in the vagueness lexicon V, and the number of vague words t within each document $t \in d$ was calculated given the length of each document. Next, the total occurrence of t within the corpus was calculated in Eq. (2) before the inverse document frequency was calculated in Eq. (3). Lastly, the scores were calculated using Eq. (4). Based on this measurement, we operationalized the vagueness scores as the percentage of vagueness within one given document (i.e., one en trepreneur's entrepreneurial narrative). We took a ratio of how promi nent this was compared to the number consistent in the whole corpus. Thus, vagueness is operationalized as the amount of vague language used within communicative content compared to other entrepreneurs.

$$
T F _ {-} V _ {(t, d)} = \left(\frac {\text { count   of } t \in d}{\text { length   of } d}\right)\tag{1}
$$

$$
D F _ {t} = \text { occurrence   of } t \in D\tag{2}
$$

$$
I D F _ {t} = \operatorname{Log} \left(\frac {\text { Number   of   Documents }}{D F _ {t}}\right)\tag{3}
$$

Vagueness score = TF V\*(IDF\*100)

(4)

## 4.1.3. Linguistic style

Descriptive language is the amount of descriptive content provided to the potential investor. It is measured by counting the number of notional words, including verbs, adverbs, and nouns contained within a crowd funding page. Following previous work [41], we also implemented parts-of-speech (POS) tagging to extract and count the number of notional words. As this approach identifies the number of unique words that fit within these categories, the more descriptive language can be operationalized as an entrepreneurial narrative with a more significant number of these words.

Paragraph structure is the measure of how many sentences occur in each passage of text. This was operationalized by counting one sentence every time a full stop appeared. Thus, a higher number for paragraph structure represents that the passage of text has more information quantity for investors to process on an entrepreneurial narrative. Para graph structure, however, does not provide information on the amount of information within a given sentence. As a result, we needed to employ further measures to rectify this issue.

Reading ease attempts to understand the complexity of a documents vocabulary and its syntax within a sentence. If a given text has poor readability, this could increase the cognitive capacity needed to un derstand the information presented. We determine how readable a given crowdfunding project is by employing the Flesch reading-ease test (see Eq. (5)) to the entrepreneurial narratives. This score can be operation alized whereby a higher score indicates textual information that is generally easier to read. Thus, entrepreneurial narratives that demon strate a higher score will help remove any unnecessary cognitive re quirements for understanding the communication content of an entrepreneur on crowdfunding.

Table 1 Hiller's vagueness dictionary.

<table><tr><td>Category</td><td>Number of entries in the dictionary</td><td>Examples</td></tr><tr><td>Ambiguous designations</td><td>52</td><td>All of them, all this</td></tr><tr><td>Negated intensifiers</td><td>55</td><td>Doesn&#x27;t seem, not all</td></tr><tr><td>Approximations</td><td>37</td><td>Almost, a while</td></tr><tr><td>Bluff and recovery</td><td>54</td><td>In any case, like all</td></tr><tr><td>Admission of error</td><td>20</td><td>Chances are, not sure</td></tr><tr><td>Indefinite amount</td><td>41</td><td>As little as, a lot</td></tr><tr><td>Multiplicity</td><td>35</td><td>Among other things</td></tr><tr><td>Probability and possibility</td><td>32</td><td>Likelihood, may well</td></tr><tr><td>Reservations</td><td>37</td><td>Seems, can be said</td></tr><tr><td>Anaphors</td><td>14</td><td>Former, such</td></tr><tr><td>Total Vagueness</td><td>377</td><td></td></tr></table>

$$
2 0 6. 8 3 5 - 1. 0 1 5 \left(\frac {\text { total   words }}{\text { total   sentences }}\right) - 8 4. 6 \left(\frac {\text { total   syllables }}{\text { total   words }}\right)\tag{5}
$$

## 4.1.4. Affect

Affect intensity was calculated by using the popular tool known as VADER.<sup>4</sup> As stated by the authors, VADER leverages the advantages of parsimonious rule-based modeling and is readily generalized to multiple domains. Further, it requires no training data [49] and provides affect intensity on a scale from − 0.99 to 0.99, allowing enough variance in text for analysis to be used without moderation to the scores.

## 4.1.5. Semantic features

Following [50], we implemented the popular Latent Dirichlet Allo cation (LDA) model [51]. Before using LDA, the text was analyzed using the coherence value to discover the degree of semantic similarity be tween words with high scores within models containing topics ranging from 2 to 400 [52]. Then, using the optimized number of topics for this dataset, we applied the LDA model [51]. The probability that a docu ment includes a given topic is given as the vector's weight based on the extracted topic's words and their associated weights within a given topic. After running the coherence value, we obtained an optimum of 16 topics (coherence: 0.4633). We then ran the LDA model using 16 topics as N and obtained the dominance percentage of each topic relative to each document. Next, we manually summarized topics obtained based on their clarity to the task (see Table 2) and used the dominance per centage to measure its influence in each document. This provided three data points, one for each topic in the dataset. Lastly, each topic obtained was then labeled to represent a semantic topic in each project R&C: “External needs,” “design and development,” and “production delays.”

## 4.1.6. Controls

Following prior work that used entrepreneurial narratives as their primary data (i.e., [1,4,7,11]) and other prominent crowdfunding research (i.e.. [5.53]). we controlled for the two factors that are used to provide direct information about the idea itself: images and videos. Therefore, image present and video present were created as dummy variables whereby present was set to one, and anything else was set to zero. Our rationale is that images and videos are the two other primary sources of information that an investor can use to gain essential infor mation on the entrepreneurial idea itself and were deemed necessary within our regression models.

## 4.1.7. Bayesian network-based decision support mechanism (BNM)

The use of BNM has the following advantage over the regression analyses in providing a more rigorous analysis based on causal knowl edge underlying the target node. Implementing BNM moves the analysis away from the rigid nature of regression models to one whereby causal knowledge can be found in a nonlinear fashion. Specifically, Bayesian networks allow data to be probabilistically altered, so that hypothesis testing on the target node is possible. A near-optimal configuration can be found through multiple trials that will probabilistically suggest how much the communication content needs to be adjusted before achieving the highest likelihood of funding success. This can be viewed as the amount needed to create a positive language expectancy violation. As a result, they are more persuaded by the entrepreneurs' credibility and invest in the project. The use of Bayesian networks has been effectively demonstrated in complex business decision-making [54], healthcare issues [55], and public health [56].

The first step of the BNM is to extract the significant data points from the regression analysis. Next, discretization of the continuous data is necessary. The BNM used an intuitive approach based on a genetic al gorithm (GA) to find various discretization bins. The GA attempted to maximize the R<sup>2</sup> between the discretized and its corresponding contin uous variables. Thus, besides the two binary variables (i.e., image and video present), all continuous independent variables used were dis cretized into four distinct bins to represent the node of that feature within the network. Next, we computed a given node's conditional probability based upon values assigned to other nodes within the data space: a directed acyclic graph is created. In this, nodes represent domain variables, and arcs between nodes represent probabilistic de pendencies [57]. Given the probability that B is not equal to zero in the Bayes theorem, the conditional and marginal probabilities of A and B's are first calculated (see Eq. (6)). Next, the network's joint probability distribution is calculated to produce evidence of probable outcomes before the chain rule is applied to the joint probabilities of the network created (see Eq. (7)). Following [58], we used the Kullback-Leibler (KL) Divergence metric to learn the network. The KL Divergence allows two probability distributions to be compared [58]. If we represent two probability distributions as A and B, it is possible to calculate the strength of the direct relationship between two of the nodes (see Eq. (8)).

$$
P [ A | B ] = P (A) ^ {*} \frac {P [ B | A ]}{P [ B ]}\tag{6}
$$

$$
P (x _ {i}, \dots , x _ {n}) = \prod_ {i} P (x _ {i} | p a _ {i})\tag{7}
$$

$$
D _ {K L} (A (X) \| B (X)) = \sum_ {X} A (X) \log_ {2} \frac {A (X)}{B (X)}\tag{8}
$$

In our study, we chose the Sons and Spouses (SS) network architec ture. Based on the tree-augmented Naïve Bayes architecture, the SS model allows spouses of son nodes to be considered for analysis [55]. A GA was used to automatically hypothesize outcomes through the learned SS network until a near-optimal network was found. In a Bayesian network, GAs work in the following way: A population is chosen, and all data points' quality is examined. Then, children are produced from selected parents. These children have a probability near zero so that they can “mutate.” After a selection criterion, individuals are removed from the population, also known as an iteration or gener ation [55,59]. In a Bayesian network, children are selected based on two operators: Crossover and mutation. Mutation is responsible for exploring and avoiding local optima, while crossover attempts to increase the population's quality. Next, a reduction helps identify an optimum solu tion in a small number of iterations.

To identify the GA's best solution within the Bayesian network, we used the generalized Bayes factor (GBF). This measurement serves as a criterion to assess a solution's strength compared to other solutions found. Thus, the GBF of a given explanation x of all possible explana tions x given the evidence e [21] (see Eq. (9)) allows two competing solutions to be tested. However, as Bayesian networks are based on more than one piece of evidence, the chain rule also has to be applied to the GBF, in which a new explanation of y must be considered (see Eq. (10))

Table 2  
Semantic topics from risks and challenges text.

<table><tr><td colspan="2">T1 External needs</td><td colspan="2">T2 Design &amp; development</td><td colspan="2">T3 Production delays</td></tr><tr><td>Use-0.007</td><td>Take-0.004</td><td>Challenge-0.053</td><td>Year-0.008</td><td>Challenge-0.027</td><td>Production-0.009</td></tr><tr><td>Weather-0.006</td><td>Construction-0.004</td><td>Learn-0.046</td><td>Already-0.008</td><td>Make-0.023</td><td>Take-0.009</td></tr><tr><td>Also-0.005</td><td>Permit-0.004</td><td>Risk-0.045</td><td>Publish-0.007</td><td>Project-0.021</td><td>Help-0.008</td></tr><tr><td>Could-0.005</td><td>Location-0.004</td><td>Accountability-0.042</td><td>Create-0.006</td><td>Time-0.018</td><td>Know-0.008</td></tr><tr><td>Food-0.005</td><td>May-0.004</td><td>Project-0.020</td><td>Complete-0.006</td><td>Risk-0.017</td><td>Complete-0.007</td></tr><tr><td>Year-0.005</td><td>Building-0.004</td><td>Work-0.014</td><td>Content-0.006</td><td>Learn-0.016</td><td>Big-0.006</td></tr><tr><td>Equipment-0.004</td><td>Need-0.003</td><td>Team-0.013</td><td>Develop-0.005</td><td>Work-0.014</td><td>Come-0.006</td></tr><tr><td>Day-0.004</td><td>Local-0.003</td><td>Experience-0.013</td><td>Software-0.005</td><td>Get-0.012</td><td>Thing-0.006</td></tr><tr><td>Build-0.004</td><td>Area-0.003</td><td>Development-0.011</td><td>Release-0.005</td><td>Accountability-0.011</td><td>Need-0.006</td></tr><tr><td>Risk-0.004</td><td>Place-0.003</td><td>Design-0.008</td><td>Build-0.004</td><td>Go-0.010</td><td>May-0.006</td></tr></table>

and then updated for analysis with the chain rule, in which $e _ { 1 }$ indicates that the evidence is valid based on multiple pieces of evidence (see Eq. (11)) [21].

$$
G B F (\boldsymbol {x}; \boldsymbol {e}) \equiv \frac {\boldsymbol {P} (\boldsymbol {e} | \boldsymbol {x})}{\boldsymbol {P} (\boldsymbol {e} | \overline {{\boldsymbol {x}}})}\tag{9}
$$

$$
G B F (\mathbf {y}; \mathbf {e} | \mathbf {x}) \equiv \frac {\mathbf {P} (\mathbf {e} | \mathbf {y} , \mathbf {x})}{\mathbf {P} (\mathbf {e} | \bar {\mathbf {y}} , \mathbf {x})}\tag{10}
$$

$$
G B F (\boldsymbol {x}; e _ {1}, e _ {2}, \dots , e _ {n}) = G B F (\boldsymbol {x}; e _ {1}) \prod_ {i = 2} ^ {n} G B F (\boldsymbol {x}; e _ {i} | e _ {1}, e _ {2}, \dots , e _ {i - 1})\tag{11}
$$

## 5. Data analysis and results

## 5.1. Summary statistics

A summary of the descriptive statistics is presented in Table $^ { 3 , }$ Approximately 37% of the projects were successful and accounted for just over ten thousand projects. Further, the percent of funding averaged 167% $( L o g = 0 . 9 4 ) _ { \it \Omega }$ , just under double the funding amount requested. Further analysis showed that successful projects also varied greatly in their success, with a 5048% variance in funding percent found $( L o g =$ 1.30). In this research, we employed two models for regression analyses. Model 1.1 included vagueness and linguistic features and was applied to both the description and R&C sections. Model 1.2 added semantic fea tures and was analyzed on the R&C section. Model 1.1 was the primary analysis used to compare both the description and the R&C. Model 1.2 offers a test of appropriate semantic topics within the two-sidedness proposition.

First, the results showed that the descriptive features demonstrated a consistently positive relationship with the project status and funding success. This finding concurred with prior literature (i.e., [53]) and was deemed adequate controls.

The effect of Vagueness was associated negatively with both project success and the percent of funding. When vagueness was found in both the project description $( \mathrm { M 1 . 1 } \colon \beta = - 0 . 0 2 2 , p = 0 . 0 1 )$ and R&C section $( \mathbf { M 1 . 1 : } \beta = - 0 . 0 1 0 , p = 0 . 0 0 1 ; \mathbf { M 1 . 2 : } \beta = - 0 . 0 0 7 , p = 0 . 0 1 )$ , the project had a significantly lower probability of success. For funding percent, vagueness was also found to be associated negatively with receiving a greater amount of funding when present in both the project description (M1.1: coef. $= - 0 . 0 1 2 , p = 0 . 0 5 )$ and R&C section (M1.1: coef. = $- 0 . 0 1 7 , p = 0 . 0 1 ;$ ; M1.2: coef. = − 0.012, p = 0.05). The polysemy score was seen to have the greatest effect of all of the vagueness metrics. This was also associated negatively with project status for both the project description $( \mathrm { M 1 . 1 } ; \beta = - 0 . 0 4 4 , p = 0 . 0 0 1 )$ and R&C section $( \mathbf { M 1 . 1 : } \beta =$ $- 0 . 0 3 6 , p = 0 . 0 0 1 ; \mathrm { M 1 . 2 } \colon \beta = - 0 . 0 2 7 , p = 0 . 0 0 1 ) . \ \beta$ A smaller effect on funding percent was seen for the project description (M1.1: coef. = $- 0 . 0 1 3 , p = 0 . 0 5 )$ and R&C section $( \mathrm { M 1 . 1 } \colon \mathrm { c o e f . } = - 0 . 0 7 5 , p = 0 . 0 0 1 ;$ M1.2: coef. = − 0.058, p = 0.001). The effect of contranyms was also negatively associated with project status when found within the project description $( \mathrm { M 1 . 1 } ; \beta = - 0 . 0 7 0 , p = 0 . 0 0 1 )$ and R&C section $( \mathbf { M 1 . 1 : } \beta =$ − 0.017, p = 0.001; M1.2: $\beta = - 0 . 0 0 8 , p = 0 . 0 0 1 )$ . Less evidence was seen for funding percent, as significant effects were only seen for project description (M1.1: coef. $= - 0 . 0 3 0 , p = 0 . 0 5 )$ and R&C model 1.1 (M1.1: $\mathbf { c o e f . } = - 0 . 0 2 2 , p = 0 . 0 0 1 )$ . This finding supports H1 and was in the hypothesized direction.

The effect observed for linguistic features showed some interesting findings. When descriptive language was used in project descriptions, the results showed a positive effect on both the project status (M1.1: β = $0 . 0 0 2 , p = 0 . 0 0 1 )$ and funding percent $( \mathrm { M 1 . 1 } \mathrm { : } \mathrm { c o e f . } = 0 . 1 9 2 , p = 0 . 0 0 1 )$ However, in the R&C section, descriptive language affected funding success negatively (M1.1: $\beta = - 0 . 0 0 2 , p = 0 . 0 5 )$ or was insignificant. This finding supports H2a in the descriptive section of entrepreneurial narratives but was not hypothesized in this direction or significant for the R&C section.

The paragraph structure findings within the description section fails to support H2b. Interestingly, for the R&C section, paragraph structure did exert a significant effect, not in the hypothesized direction. This was found in both the project status $( \mathbf { M 1 . 1 : } \beta = 0 . 0 2 8 , p = 0 . 0 1 ; \mathbf { M 1 . 1 : } \beta =$ $0 . 0 3 0 , p = 0 . 0 0 1 )$ ) and funding percent $( \mathrm { M 1 . 1 } \colon \mathrm { c o e f . } = 0 . 0 3 7 , p = 0 . 0 1 $ ; M1.2: coef. $= 0 . 0 3 4 , p = 0 . 0 1 )$ . Thus, H2b was not supported. We also found that reading ease exerted a significant positive effect on project success (M1.1: $\beta = 0 . 0 0 2 , p = 0 . 0 0 1 )$ and funding percent (M1.1: coef. = $0 . 0 2 2 , p = 0 . 0 0 1 )$ . Thus, H2c was supported for the description section. Reading ease was found to have mixed effects within the R&C section. As shown in Table $^ { 4 , }$ a positive (M1.1: $\beta = 0 . 0 0 3 , p = 0 . 0 1 )$ and negative effect (M1.2: $\beta = - 0 . 0 0 5 , p = 0 . 0 0 1 )$ was found to be associated with project success. The same mixed associations were obtained for funding percent in both of the models $( \mathbf { M 1 . 1 } \colon \mathrm { c o e f . } = - 0 . 0 2 1 , p = 0 . 0 1 ;$ ; M1.2: coef $\dot { \cdot } = - 0 . 0 3 3 , p = 0 . 0 0 1 )$ ). Due to the mixed nature of the results H2c was not supported for the R&C section.

As hypothesized, affect was associated positively with the project description for both status (M1.1: $\beta = 0 . 2 7 4 , p = 0 . 0 0 1 )$ and funding percent (M1.1: coef. = 0.039, p = 0.001), while the opposite effect was found for the R&C section, in which affect had a negative effect on both project status $( \mathrm { M 1 . 1 } \colon \beta = - 0 . 3 1 1 p = 0 . 0 0 1 ; \mathrm { M 1 . 1 } \colon \beta = - 2 6 2 , p = 0 . 0 0 1 )$ and percent of funding (M1.1: coef. = − 0.044, p = 0.001; M1.2: coef. = 0.039, $p = 0 . 0 0 1 )$ . We therefore accepted H3a and H3b.

The remaining hypotheses were tested on just the R&C section. We found that T1, “external needs,” was related negatively with project success. The effect was more pronounced in the project status (M1.2: β $= - 1 . 3 5 4 , p = 0 . 0 0 1 \mathrm { ] }$ ) than the funding percent (M1.2: $\mathrm { c o e f . } = - 0 . 0 6 4 , p$ $= 0 . 0 0 1 )$ . For T2, “design and development,” a strong positive associa tion was found for both project status (M1.2: $\beta = 3 . 0 5 3 , p = 0 . 0 0 1 )$ and funding percent (M1.2: coef. = 0.134, p = 0.001). T3, “production de lays,” exerted a positive significant effect with project status $( \mathbf { M 1 . 2 : } \beta =$ $0 . 8 9 8 , p = 0 . 0 0 1 )$ and funding percent (M1.2: coef. = 0.036, p = 0.001). H4 was accepted for T2 and T3 only.

## 5.2. Bayesian Network-based project success likelihood analysis

Using the funding percent dependent variable, we attempted to find the most probable variables that increase funding success. As the percent of funding is a continuous variable, it can be separated further based on certain thresholds. For use within the BNM, the mean of successful projects' funding percent was obtained and used as a threshold. Below this mean represented a successful project, and above this mean repre sented a highly successful project. This created three discretized bins within the Bayesian network target node: “failed” (N = 17,612; avg. funding = 8.79%), “successful” $( N = 9 4 6 5 ;$ avg. funding = 146.14%), and “highly successful” (N = 1017; avg. funding = 3101.33%). With this new class node created, model architectures were learned using the Sons and Spouses network (see an example in Fig. 2).

Descriptive statistics of the variables.

<table><tr><td rowspan="2">Variables</td><td colspan="4">Project description</td><td colspan="4">Risks and challenges</td></tr><tr><td>Min</td><td>Max</td><td>Mean</td><td>St. Dev</td><td>Min</td><td>Max</td><td>Mean</td><td>St. Dev</td></tr><tr><td colspan="9">Dependent variables</td></tr><tr><td>Status</td><td>0</td><td>1</td><td>0.37</td><td>0.48</td><td>0</td><td>1</td><td>0.37</td><td>0.48</td></tr><tr><td>Percentage of funding (Log)</td><td>-5</td><td>5.83</td><td>0.94</td><td>1.30</td><td>-5</td><td>5.83</td><td>0.94</td><td>1.30</td></tr><tr><td colspan="9">Descriptive features</td></tr><tr><td>Image presence</td><td>0</td><td>1</td><td>0.59</td><td>0.49</td><td>0</td><td>1</td><td>0.59</td><td>0.49</td></tr><tr><td>Video presence</td><td>0</td><td>1</td><td>0.69</td><td>0.46</td><td>0</td><td>1</td><td>0.69</td><td>0.46</td></tr><tr><td colspan="9">Vagueness</td></tr><tr><td>Vagueness score</td><td>0</td><td>75.70</td><td>1.73</td><td>2.69</td><td>0</td><td>234.2</td><td>4.07</td><td>7.74</td></tr><tr><td>Polysemy score</td><td>0</td><td>458.7</td><td>4.04</td><td>7.81</td><td>0</td><td>415.1</td><td>11.62</td><td>13.56</td></tr><tr><td>Contranyms score</td><td>0</td><td>94.04</td><td>2.19</td><td>3.20</td><td>0</td><td>241.2</td><td>4.73</td><td>7.69</td></tr><tr><td colspan="9">Linguistic features</td></tr><tr><td>Descriptive language</td><td>2</td><td>1720</td><td>291.6</td><td>269.3</td><td>1</td><td>1455</td><td>48.65</td><td>45.25</td></tr><tr><td>Paragraph structure</td><td>1</td><td>245</td><td>24.57</td><td>24.29</td><td>1</td><td>98</td><td>4.65</td><td>3.76</td></tr><tr><td>Reading ease</td><td>-213</td><td>106.7</td><td>52.05</td><td>26.36</td><td>-220</td><td>111.6</td><td>56.71</td><td>20.01</td></tr><tr><td colspan="9">Affect</td></tr><tr><td>Sentiment</td><td>-0.99</td><td>0.99</td><td>0.85</td><td>0.36</td><td>-0.99</td><td>0.99</td><td>0.39</td><td>0.54</td></tr><tr><td colspan="9">Semantic features</td></tr><tr><td>T1 External needs</td><td></td><td></td><td></td><td></td><td>0</td><td>0.97</td><td>0.08</td><td>0.13</td></tr><tr><td>T2 Design &amp; development</td><td></td><td></td><td></td><td></td><td>0</td><td>0.98</td><td>0.13</td><td>0.20</td></tr><tr><td>T3 Production delays</td><td></td><td></td><td></td><td></td><td>0</td><td>0.99</td><td>0.28</td><td>0.27</td></tr></table>

Next, based on a GA search heuristic, the best solution of causal knowledge was obtained and used for hypothesis testing on multiple best solutions (See Fig. 3). Fig. 3a, b and c show the best solutions based on the highest GBF score. First, Fig. 3a shows the result of the project description. The best solution showed that if the project presentation maintains these features, high success could increase from 3.62% to 32.38%. Further, the result showed that the failed projects could decrease to 28.29%, while the success rate could increase to 39.33%. Next, Fig. 3b provides the best solution for M1.1 in the R&C section. If the presentation features are adhered to in this fashion, the likelihood of success will increase from 3.62% to 24.00%. Once again, this is a highly significant increase and could help entrepreneurs obtain a higher funding percent. Lastly, we analyzed M1.2 of the R&C section to include the semantic features. As seen in Fig. 3c, the results reduced the likeli hood of failure altogether. Furthermore, success could potentially rise to 85.52%. Although these results are not just depending on all the features within this study, a significant effect is possible when certain commu nication content is correctly adjusted.

## 6. Discussion and conclusions

This paper builds on communication content literature by exploring entrepreneurial narratives within crowdfunding. Our study attempted to answer some open questions that still surround the use of language embedded within entrepreneurial narratives. Based on the language expectancy theory (LET), this paper argues that the language used within entrepreneurial narratives can contribute to an entrepreneur's perception of credibility, resulting in showing varied amounts of persuasiveness towards an investor. Within each entrepreneurial narrative context (both description and risks and challenges (R&C)), our study showed that certain expectations from investors in terms of the communication content used by entrepreneurs was significantly influ ential upon the investor's investment decision.

Among various interesting findings, this papers' first main finding suggested that using vague language in the entrepreneurial narratives was associated with negative project success. Firstly, as proposed in vagueness theory [14,60], when a communicator uses too much vague language, it is indicative of a communicator who does not sufficiently command the facts, knowledge, or understanding required for effective communication. We found that entrepreneurs with higher levels of vague language in their communication had a significantly less likeli hood of receiving funding. Following the LET principles, we believe this is because potential investors see vague language as less persuasive due to a lack of clarity and presentation of poor-quality information. At this point, we postulate that investors have a negative language expectancy violation and choose not to invest. Next. evidence of the role that lin: guistic features can have on investment likelihood. In line with prior crowdfunding research [7], our results suggest that linguistic features can positively and negatively violate investors' expectations. As we posited, we believe this influences investors' credibility assessment of an entrepreneur resulting in less investment.

Affect intensity was found to influence entrepreneurial narratives in two distinct ways. Positive affect increased funding success in project descriptions, whereas the opposite effect was found for the R&C section. This finding conceptually makes sense when we consider each section's role in influencing the tone of the entrepreneurial narrative. Thus, ex pectations of this section were found to contribute differently to project success. Lastly, following the two-sidedness propositions, semantic topics were extracted from the R&C section. Prior work has explored the positive semantic topics within project descriptions (i.e., [20,45]); however, as we propose, credible arguments stem from including some negatives in entrepreneurial narratives. Our findings suggest that entrepreneurial narratives that explore the potential issue of design and development alongside production delays can provide effective twosidedness. In turn, this leads to a positive language expectancy viola tion resulting in increased investment.

## 6.1. Theoretical and practical implications

This research builds on prior crowdfunding literature that views entrepreneurial narratives and communication content as a leading reason for the success or failure of a project $[ 1 , 4 , 6 - 8 , 1 1 , 2 7 , 2 8 , 3 0 , 4 5 ]$ Additionally, this work has followed on from work employing LET. For instance, Parhankangas and Renko [7] found that the linguistic style used among commercial and social entrepreneurs violated investors' language expectancies in various ways. Du et al. [8] used a machine

<sup>\*</sup> p < 0.001.

Table 4  
Results of logistic regression and ordinary least squares regression

<table><tr><td rowspan="3"></td><td colspan="3">Project status (Log)</td><td colspan="3">Funding percent (OLS)</td></tr><tr><td>Description</td><td colspan="2">Risks and challenges</td><td>Description</td><td colspan="2">Risks and challenges</td></tr><tr><td>Model 1.1</td><td>Model 1.1</td><td>Model 1.2</td><td>Model 1.1</td><td>Model 1.1</td><td>Model 1.2</td></tr><tr><td>AdjR2</td><td></td><td></td><td></td><td>0.297</td><td>0.298</td><td>0.294</td></tr><tr><td>AIC</td><td>27,989.21</td><td>29,231.82</td><td>27,520.68</td><td></td><td></td><td></td></tr><tr><td>VIF</td><td>1.02–6.46</td><td>1.02–5.47</td><td>1.02–6.46</td><td>1.09–7.50</td><td>1.02–5.53</td><td>1.02–5.63</td></tr><tr><td>Image presence</td><td>1.027*** (2.74)</td><td>1.675*** (5.34)</td><td>1.839*** (4.19)</td><td>0.274***</td><td>0.370***</td><td>0.366***</td></tr><tr><td>Video presence</td><td>1.400*** (4.06)</td><td>1.576*** (4.83)</td><td>1.432*** (6.29)</td><td>0.203***</td><td>0.235***</td><td>0.210***</td></tr><tr><td>Vagueness score</td><td>-0.022** (0.98)</td><td>-0.010*** (0.99)</td><td>-0.007** (0.99)</td><td>-0.012*</td><td>-0.017**</td><td>-0.012*</td></tr><tr><td>Polysemy Score</td><td>-0.044*** (0.96)</td><td>-0.036*** (0.97)</td><td>-0.027*** (0.97)</td><td>-0.013*</td><td>-0.075***</td><td>-0.058***</td></tr><tr><td>Contranyms Score</td><td>-0.070*** (0.93)</td><td>-0.017*** (0.98)</td><td>-0.008*** (0.99)</td><td>-0.030*</td><td>-0.022***</td><td>-0.007</td></tr><tr><td>Descriptive language</td><td>0.002*** (1.00)</td><td>-0.002* (1.00)</td><td>0.001 (1.00)</td><td>0.192***</td><td>-0.015</td><td>0.019</td></tr><tr><td>Paragraph structure</td><td>-0.001 (1.00)</td><td>0.028** (1.03)</td><td>0.030*** (1.03)</td><td>0.005</td><td>0.037**</td><td>0.034**</td></tr><tr><td>Reading ease</td><td>0.002*** (1.00)</td><td>0.003** (1.00)</td><td>-0.005*** (1.00)</td><td>0.022***</td><td>-0.021**</td><td>0.033***</td></tr><tr><td>Sentiment</td><td>0.274*** (1.32)</td><td>-0.311*** (0.73)</td><td>-0.262*** (0.77)</td><td>0.039***</td><td>-0.044***</td><td>-0.039***</td></tr><tr><td>T1 External needs</td><td></td><td></td><td>-1.354*** (0.26)</td><td></td><td></td><td>-0.064***</td></tr><tr><td>T2 Design &amp; development</td><td></td><td></td><td>3.053*** (21.19)</td><td></td><td></td><td>0.134***</td></tr><tr><td>T3 Production delays</td><td></td><td></td><td>0.898*** (2.45)</td><td></td><td></td><td>0.036***</td></tr></table>

Notes: Odds ration obtained from the logistic regression are seen in parentheses.  
p < 0.01.

![](/api/attachments/DM82PVHW/fulltext/images/fddb5d11d3d6ed27931c3a71e0fe8e777b365afb0180530729b5e6b8a64b2174.jpg)  
Fig. 2. Example of the Sons and Spouses network employed for building the Bayesian network for project description funding percent (model 1.1).

learning approach to assess linguistic features that caused funding suc cess. In contrast, we suggest that language vagueness and two-sidedness are also factors that contribute to crowdfunding success. Also, unlike previous work, we further tested known attributes, such as linguistic features and affect, using separate data points that represented the two distinct sections now found in Kickstarter entrepreneurial narratives.

We contribute to the existing literature on LET. Previous LET studies have highlighted message features, such as language preference, in tensity, and linguistic features [7,8,17]. We suggest that language ex pectations can also be influenced using vague language. Our results draw attention to the negative role vague language can have in language that is supposed to come from a more knowledgeable communicator than the receiver on the given topic. As information asymmetry is a complex problem for many online platforms, we show that vague lan guage will likely negatively violate language expectations of the communication receivers.

Next, we have pioneered an analysis to understand the specific communication content needed on both sides of the argument to maximize funding success likelihood. By identifying the semantic topics within the Kickstarter R&C section, we have built on prior LET research using the two-sidedness proposition [17] and extended its use to crowdfunding research. Our findings indicate that two-sidedness is also an effective tool for crowdfunding entrepreneurs that may help persuade investors to invest in the entrepreneur. Furthermore, such findings inform other platforms that they should actively encourage their users to be more balanced in their argumentation.

Prior research using LET has shown that when group identity is un known [17], language expectancies, by proxy, can only stem from the language itself. Therefore, cultural norms and expectations are placed on the accepted norms within written language. For this reason, we included the tests of linguistic features and affect. Compared with prior crowdfunding literature, we have shown that these two variables are still predictors of crowdfunding success, however, dependent on the entrepreneurial section. Evidence of this was found whereby language affect was found to have a positive relationship within the description, yet a negative relationship within the R&C section. Theoretically, this suggests that the context of entrepreneurial narrative can play an influencing role in the types of expectations investors have when reading a crowdfunding pitch online.

From a practical perspective, our results have provided evidence of the importance of particular language used by entrepreneurs and how this has positive and negative consequences on the likelihood of receiving investment. Moreover, we have shown that even if an entre preneur has a good idea, the way they present the idea through the careful choice of specific language may also be important in determining investment. Evidence of this was found in two regression analyses and also in a Bayesian network-based analysis. As Bayesian networks pro vide causal knowledge of the underlying target class, the use of this tool can guide entrepreneurs in effectively presenting their ideas to enhance the likelihood of investment. We identified a near-optimal solution of funding success using a genetic algorithm within a learned Bayesian network model. We imagine that using this Bayesian network and ge netic algorithm methodology can also optimize effective feedback as an entrepreneur is preparing a page. Much like grammar and spelling checks embedded in a word processor, a similar tool can be built as a decision support mechanism to aid entrepreneurs.

## 6.2. Limitations and future research directions

Despite this study's merits, clear limitations exist. First, although our analysis relates to crowdfunding and entrepreneurial literature, our data limits the generalizability to just the Kickstarter platform. Second, although Kickstarter is a leader in crowdfunding, future work will have to strive to test our findings on other platforms. This leads to a further limitation. Finally, at present, Kickstarter is the only platform to include the R&C section specifically. Thus, creative ways to test the two-sided persuasion proposition on other platforms will be needed.

a  
![](/api/attachments/DM82PVHW/fulltext/images/532d5c5d8f79dfa4b999e65ff16abcb2b0e2527eb07b49025900a8bd81b19903.jpg)  
Fig. 3. a. Results from a What-if analysis based on the proposed best solution for the project description. \*Generalized Bayes Factor obtained from the genetic al gorithm search heuristic = 8.9441. b. Results from a What-if analysis based on the proposed best solution for the project risks and challenges section (M1.1). \*Gener alized Bayes Factor obtained from the genetic algorithm search heuristic = 6.6325. c. Results from a What-if analysis based on the proposed best solution for the project risks and challenges section (M1.2). \*Generalized Bayes Factor obtained from the genetic algorithm search heuristic = 27.6244.

b  
![](/api/attachments/DM82PVHW/fulltext/images/b937a1742d175161f72ff3706d14a06c5ba16e3e0bcc11e4df36d1a24a0ecb40.jpg)

![](/api/attachments/DM82PVHW/fulltext/images/2cd32d8a8fa51b7f0adc3eba9cdd25b9bec6d58d1d775e95210071d7a1289401.jpg)

Next, the method for extracting the vague scores can only be used with English texts. Accordingly, its use and results may be suitable only for English-based platforms, meaning these scores' findings may only generalize to cultures that use English for their entrepreneurial narra tives. Future work could adapt the framework to include other Latinbased languages. However, languages that fall outside of this may be harder to adopt. Further, we did not test for cause-and-effect relations in the Bayesian networks. Thus, the results obtained remain probabilistic and, therefore, should be interpreted and applied with care. Finally, any of the recommendations should be recognized as likelihoods rather than facts. Future research could examine cause-and-effect relations by building and analyzing such networks manually and testing relation ships one-by-one.

## Credit author statement

Francis Joseph Costello contributd to methdology, data analysis, researh model, and draft writing. Kun Chang Lee initiated the research model and secured research funding for this study. Kun Chang Lee also helped with statistical and theoretical interpretations, and conducted review writing and project management, etc.

## Acknowledgments

This paper was supported by the SKKU Excellence in Research Award Research Fund, Sungkyunkwan University, 2020.

## Appendix A

Table A.1  
Prior research papers on crowdfunding project presentation.

<table><tr><td rowspan="2">Citation</td><td rowspan="2"></td><td colspan="3">Methodology</td><td colspan="2">Two-sided persuasion</td><td colspan="4">Textual features explored</td></tr><tr><td>Regression</td><td>Machine learning</td><td>Bayesian network</td><td>Description</td><td>Risks and challenges</td><td>Vagueness</td><td>Linguistic features</td><td>Affect intensity</td><td>Semantic features</td></tr><tr><td rowspan="2">[11]</td><td>This study</td><td>✓</td><td></td><td>✓</td><td>✓</td><td> $\checkmark *$ </td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>Journal of Business Venturing</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[1]</td><td>Journal of Business Venturing</td><td>✓</td><td></td><td></td><td>✓</td><td> $\checkmark **$ </td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[4]</td><td>Journal of Business Venturing</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[8]</td><td>JASIST</td><td></td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>[38]</td><td>Strategic Entrepreneurship Journal</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[45]</td><td>Electronic Commerce Research and Applications</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td></tr><tr><td>[30]</td><td>Group &amp; Organization Management</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[20]</td><td>Decision Support Systems Information and Management</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>[9]</td><td>Information and Management</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[28]</td><td>Information and Management</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[27]</td><td>Strategic Organization</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[29]</td><td>ACM - CSCW 2014</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[7]</td><td>Journal of Business Venturing</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr><tr><td>[5]</td><td>Decision Support Systems</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[6]</td><td>Computers in Human Behavior</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[61]</td><td>IET Software</td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td></tr><tr><td>[19]</td><td>Decision Support Systems Information Systems Research</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td></tr><tr><td>[18]</td><td>Information Systems Frontiers</td><td>✓</td><td></td><td></td><td>✓</td><td> $\checkmark ***$ </td><td></td><td>✓</td><td></td><td></td></tr><tr><td>[43]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td></td></tr></table>

A discrete analysis was made on this section on risks and challenges as a test of two-sidedness.  
<sup>\*\*</sup> This study obtained data from the risks and challenges section but combined it with the description data and then combined it with another obtained dataset which only contained description data.  
This study used the length of the risks and challenges section as a control variable only.

## References

[1] A.H. Anglin, J.C. Short, W. Drover, R.M. Stevenson, A.F. McKenny, T.H. Allison, The power of positivity? The influence of positive psychological capital language on crowdfunding performance, J. Bus. Ventur. 33 (2018) 470–492.

[2] R. Joshua, Three essential keys to crowdfunding success, Forbes. (2020) 1–4. https ://www.forbes.com/sites/forbesbusinesscouncil/2020/08/07/three-essentialkeys-to-crowdfunding-success/. (Accessed 20 July 2021).

[3] K. Kim, S. Viswanathan, The experts in the crowd: the role of experienced investors in a crowdfunding market, MIS O. Manage, Inform. Syst. 43 (2019) 347–372.

[4] A.H. Anglin, M.T. Wolfe, J.C. Short, A.F. McKenny, R.J. Pidduck, Narcissistic rhetoric and crowdfunding performance: a social role theory perspective, J. Bus. Ventur, 33 (2018) 780–812

[5] W. Wang, W. Chen, K. Zhu, H. Wang, Emphasizing the entrepreneur or the idea? The impact of text content emphasis on investment decisions in crowdfunding, Decis, Support, Syst, 136 (2020) 113341.

[6] W. Wang, L. He, Y.J. Wu, M. Goh, Signaling persuasion in crowdfunding entrepreneurial narratives: the subjectivity ys objectivity debate, Comput. Hum Behav, 114 (2021) 106576.

[7] A. Parhankangas, M. Renko, Linguistic style and crowdfunding success among social and commercial entrepreneurs, J. Bus. Ventur. 32 (2017) 215–236.

[8] O. Du, J. Li. Y. Du, G.A. Wang, W. Fan, Predicting crowdfunding project success

[9] T.P. Liang, S.P.J. Wu, C. Chi Huang, Why funders invest in crowdfunding projects: role of trust from the dual-process perspective, Inf. Manag. 56 (2019) 70–84.

[10] H. Zheng, D. Li, J. Wu, Y. Xu, The role of multidimensional social capital in crowdfunding: a comparative study in China and US, Inf. Manag. 51 (2014) 488–496.

[11] T.H. Allison, B.C. Davis, J.W. Webb, J.C. Short, Persuasion in crowdfunding: an elaboration likelihood model of crowdfunding performance, J. Bus. Ventur. 32 (2017) 707–725.

[12] G. Burtch, A. Ghose, S. Wattal, An empirical examination of the antecedents and consequences of contribution patterns in crowd-funded markets, Inf. Syst. Res. 24 (2013) 499–519.

[13] G. Burtch, A. Ghose, S. Wattal, The hidden cost of accommodating crowdfunder privacy preferences: a randomized field experiment, Manag. Sci. 61 (2015) 949–962.

[14] J.H. Hiller, Verbal response indicators of conceptual vagueness, Am. Educ. Res. J. 8 (1971) 151–161.

[15] W. Guo, M. Sengul, T. Yu, Rivals’ negative earnings surprises, language signals, and firms' competitive actions, Acad. Manag. J. 63 (2020) 637–659.

[16] W. Guo, T. Yu, J. Gimeno, Language and competition: communication vagueness, interpretation difficulties, and market entry, Acad. Manag. J. 60 (2017) 2073-2098.

[17] M.L. Jensen, J.M. Averbeck, Z. Zhang, K.B. Wright, Credibility of anonymous online product reviews: a language expectancy perspective, J. Manag. Inf. Syst. 30 (2013) 293–324.

[18] L. Yang, Z. Wang, J. Hahn, Scarcity strategy in crowdfunding: an empirica exploration of reward limits, Inf. Syst. Res. 31 (2020) 1107–1131.

[19] H. Yuan, R.Y.K. Lau, W. Xu, The determinants of crowdfunding success: a semantic text analytics approach, Decis. Support. Syst. 91 (2016) 67–76.

[20] W.S. Lee, S.Y. Sohn, Discovering emerging business ideas based on crowdfunded software projects, Decis. Support. Syst. 116 (2019) 102–113.

[21] C. Yuan, H. Lim, T.C. Lu, Most relevant explanation in bayesian networks, J. Artif. Intell, Res, 42 (2011) 309–352.

[22] G. Burtch, Y. Hong, D. Liu, The role of provision points in online crowdfunding, J. Manag. Inf. Syst. 35 (2018) 117–144.

[23] P. Roma, E. Gal-Or, R.R. Chen, Reward-based crowdfunding campaigns: informational value and access to venture capital, Inf. Syst. Res. 29 (2018) 679–697.

[24] Kickstarter, Stats, Kickstarter. https://www.kickstarter.com/help/stats, 2020. (Accessed 5 December 2020).

[25] G. Burtch, A. Ghose, S. Wattal, Cultural differences and geography as determinants of online prosocial lending, MIS Q. 38 (2014) 773–794.

[26] J. Cornelissen, J. Clarke, Imagining and rationalizing opportunities: inductive reasoning and the creation and justification of new ventures. Acad. Manag. Rey. 35 (2010) 539–557.

[27] S. Manning, T.A. Bejarano, Convincing the crowd: entrepreneurial storytelling in crowdfunding campaigns, Strateg, Organ. 15 (2017) 194–219

[28] A. Majumdar, I. Bose, My words for your pizza: an analysis of persuasive narratives in online crowdfunding, Inf. Manag. 55 (2018) 781–794.

[29] T. Mitra, E. Gilbert, The language that gets people to give, in: Proceedings of the 17th ACM Conference on Computer Supported Cooperative Work & Social Computing, ACM, New York, NY, USA, 2014, pp. 49–61.

[30] P.H. Kim, M. Buffart, G. Croidieu, TMI: signaling credible claims in crowdfunding campaign narratives, Group Org. Manag. 41 (2016) 717–750.

[311 M. Burgoon, S.B. Jones, D. Stewart. Toward a message-centered theory of persuasion: three empirical investigations of language intensity, Hum. Commun. Res. 1 (1975) 240–256.

[32] M. Burgoon, M.D. Miller, M. Cohen, C.L. Montgomery, An empirical test of a model of resistance to persuasion Hum Commun Res. 5 (1978) 27–39

[33] J.M. Averbeck, C. Miller, Expanding language expectancy theory: the suasory effects of lexical complexity and syntactic complexity on effective message design, Commun. Stud. 65 (2014) 72–95.

[34] J.M. Averbeck, Irony and language expectancy theory: evaluations of expectancy

[35] G. Craciun, K. Moore, Credibility of negative online product reviews: reviewer gender, reputation and emotion effects, Comput. Hum. Behav. 97 (2019) 104–115.

[36] R. Keefe, Theories of Vagueness, Cambridge University Press, Cambridge, 2000.

[37] R. Dietz, Vagueness and Rationality in Language Use and Cognition, Springer International Publishing, Cham. 2019.

[38] H. Gafni, D. Marom, O. Sade, Are the life and death of an early-stage venture indeed in the power of the tongue? Lessons from online crowdfunding pitches, Strateg. Entrep. J. 13 (2019) 3–23.

[39] L. Larrimore, L. Jiang, J. Larrimore, D. Markowitz, S. Gorski, Peer to peer lending: the relationship between language features, trustworthiness, and persuasion success, J. Appl. Commun. Res. 39 (2011) 19–37.

[40] S.L. Humpherys, K.C. Moffitt, M.B. Burns, J.K. Burgoon, W.F. Felix, Identification of fraudulent financial statements using linguistic credibility analysis, Decis. Support. Syst. 50 (2011) 585–594.

[41] L. Zhang, Q. Yan, L. Zhang, A computational framework for understanding antecedents of guests’ perceived trust towards hosts on Airbnb, Decis. Support Syst. 115 (2018) 105–116.

[42] C.C. Chen, Y. de Tseng, Quality evaluation of product reviews using an information quality framework. Decis. Support. Syst. 50 (2011) 755–768.

[43] M.J. Zhou, B. Lu, W.P. Fan, G.A. Wang, Project description and crowdfunding success: an exploratory study. Inf. Syst. Front. 20 (2018) 259–274.

[44] A. Bailin, A. Grafstein, Readability: Text and Context, Palgrave Macmillan UK, London, 2016.

[45] C. Jiang, R. Han, Q. Xu, Y. Liu, The impact of soft information extracted from descriptive text on crowdfunding performance, Electron. Commer. Res. Appl. 43 (2020) 101002.

[46] A.E. Crowley, W.D. Hoyer, An integrative framework for understanding two-sided persuasion, J. Consum. Res. 20 (1994) 561.

[47] R. Hogenraad, Smoke and mirrors: tracing ambiguity in texts, in: Digital Scholarship in the Humanities 33, 2018, pp. 297–315.

[48] J. Quilty-Dunn, Polysemy and thought: toward a generative theory of concepts, Mind Lang. (2020) 1–28, https://doi.org/10.1111/mila.1232828QUILTY-DUNN (mila.12328).

[49] C. Hutto, E. Gilbert, VADER: a parsimonious rule-based model for sentimen analysis of social media text, in: Proceedings of the International AAAI Conference on Web and Social Media, Ann Arbor, Michigan, 2014, p. 10.

[50] L. Zhang, Q. Yan, L. Zhang, A text analytics framework for understanding the relationships among host self-description, trust perception and purchase behavior on Airbnb, Decis. Support. Syst. 133 (2020) 113288.

[51] D.M. Blei, A.Y. Ng, M.I. Jordan, Latent dirichlet allocation, J. Mach. Learn. Res. 3 (Jan) (2003) 993–1022.

[52] D. Newman, J.H. Lau, K. Grieser, T. Baldwin, Automatic evaluation of topic coherence, in: NAACL, HLT 2010 - Human Language Technologies: The 2010 Annual Conference of the North American Chapter of the Association fo Computational Linguistics, Proceedings of the Main Conference, 2010, pp. 100–108.

[53] M. Raab, S. Schlauderer, S. Overhage, T. Friedrich, More than a feeling: investigating the contagious effect of facial emotional expressions on investment decisions in reward-based crowdfunding, Decis. Support. Syst. 135 (2020) 113326.

[54] M.H. Hahn, K.C. Lee, N.Y. Jo, Scenario-based management of individual creativity, Comput. Hum. Behav. 42 (2015) 36–46.

[55] F.J. Costello, C. Kim, C.M. Kang, K.C. Lee, Identifying high-risk factors of depression in middle-aged persons with a novel sons and spouses Bavesian network model. Healthcare. 8 (2020) 562

[56] C. Kim, F.J. Costello, K.C. Lee, Y. Li, C. Li, Predicting factors affecting adolescent obesity using general bavesian network and what-if analysis. Int. J. Environ. Res Public Health 16 (2019) 1–18.

[57] I.H. Witten, E. Frank, M.A. Hall, C. Pal, Data Mining: Practical Machine Learning Tools and Techniques. Fourth edn. Morgan Kaufmann Publishers Inc. 2016

[58] O.M. Cliff, M. Prokopenko, R. Fitch, Minimising the kullback-leibler divergence for model selection in distributed nonlinear systems. Entropy. 20 (2018) 1–28

[59] P. Larranaga, Structure learning of bayesian networks by genetic algorithms: a performance analysis of control parameters, IEEE Trans. Pattern Anal. Mach. Intell. 18 (1996) 912–926.

[60] J.H. Hiller, D.R. Marcotte. T. Martin. Opinionation, vagueness, and specificity distinctions: essay traits measured by computer, Am. Educ. Res. J. 6 (1969) 271–286.

[61] W. Wang, K. Zhu, H. Wang, Y.C.J. Wu, The impact of sentiment orientations on successful crowdfunding campaigns through text analytics, IET Softw. 11 (2017) 229-238.

Francis Joseph Costello is now pursuing his PhD degee at SKK Business School, Sung kyunkwan University (Seoul, South Korea). He has been actively engaged in a number of serious studies about internet security, neuroscience-based decision making analysis, big data analytics using AI methods, and creativity analysis, etc.

Kun Chang Lee holds a distinguished professorship at SKK Business School, Sungkyunk wan University (Seoul. South Korea). His main research interests lie in neuro-science analysis of decision-making processes, health analytics, big data analysis using deep learning algorithms, and psychophysiological analysis of business decision-making per formance, etc.
