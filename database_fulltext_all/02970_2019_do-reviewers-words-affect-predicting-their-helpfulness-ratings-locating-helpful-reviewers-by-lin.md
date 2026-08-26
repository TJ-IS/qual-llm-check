---
otero_id: 2970
otero_key: "9SPC426X"
title: "Do reviewers’ words affect predicting their helpfulness ratings? Locating helpful reviewers by linguistics styles"
authors: "Sheng-Tun Li; Thuong-Thi Pham; Hui-Chi Chuang"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.06.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Do reviewers’ words a<sup>f</sup>ect predicting their helpfulness ratings? Locating helpful reviewers by linguistics styles

Sheng-Tun Li<sup>a,⁎</sup>, Thuong-Thi Pham<sup>b</sup>, Hui-Chi Chuang

<sup>a</sup> Institute of Information Management & Department of Industrial and Information Management, National Cheng Kung University, No.01 Da-Hsueh Road, East Area, Tainan City, 701, Taiwan

<sup>b</sup> Institute of Information Management, National Cheng Kung University, No.01 Da-Hsueh Road, East Area, Tainan City, 701, Taiwan

## A R T I C L E I N F O

Keywords: Helpful reviewers Online review Language use Social relation Electronic word-of-mouth

## A B S T R A C T

Locating helpful reviewers in opinion-sharing communities is an important issue. Numerous studies that examine this using social relations have some shortcomings. This study investigates language use, di<sup>f</sup>ering from person to person, and develops a novel prediction model to alleviate the problems. We identify four stylistic aspects and explore their impacts on predicting reviewers’ helpfulness ratings. The analyses show that the proposed model can more accurately locate helpful reviewers than the baseline model. In addition, reviewers’ words impact more than social relations do, although a combination of these will boost prediction performance to a greater extent than one alone.

## 1. Introduction

The rapid growth of e-commerce stores (e.g., amazon.com, walmart.com, nike.com, and levi.com) has led to an increase in the number of online forums hosted by retailers or manufacturers that allow customers to share their opinions regarding retailers or manufacturers to help in the purchase decision-making process. To provide dedicated platforms for customers to discuss and exchange knowledge and experiences after purchase and use, many third-party product review sites (e.g., epinions.com, rateitall.com, and ZDNET.com) also o<sup>f</sup>er a variety of opinion forums [1 4]. The product reviewers in such forums provide customers with an extensive amount of information, giving them the opportunity to make more informed decisions; in addition, the broad range of opinions available from many di<sup>f</sup>erent sources may overwhelm customers. Compounding this issue is that the quality of the reviews varies immensely, thereby causing even greater confusion. Moreover, to most customers, the search process is both time consuming and frustrating. Not only do they need to sift through seemingly endless information provided by innumerable reviewers but also identify helpful reviews and reviewers they can listen to [1]. Besides very professional and reliable reviewers, there are some subjective and biased ones; thus, there is a need to identify the former in order to avoid the latter.

To achieve this, we need a classi<sup>fi</sup>cation system that discriminates more and less helpful reviewers [1,3] in a period of time, say quarterly or yearly. For example, a label of “Top-1000” reviewer is displayed right next to the name of each such reviewer on Amazon. Similarly, Yelp does an annual ranking of its top reviewers and gives them certi<sup>fi</sup>cation as such. Sites can give medals or certi<sup>fi</sup>cates to good reviewers to recognize their contributions in consistently providing helpful in formation in online communities [5], and these helpful reviewers have signi<sup>fi</sup>cant in<sup>fl</sup>uences on di<sup>f</sup>erent responses among recipients [6,7]. Hart-Davidson et al. [8] pointed out that helpfulness is a measure of the quality of an online review based on some criteria and is a desirable feature that both a review and reviewer should be helpful. A reviewer can be considered as helpful if he or she consistently o<sup>f</sup>ers helpful reviews. Lee et al. [7] in their work of pro<sup>fi</sup>ling helpful travel reviewers found that the reviewers can be of any age and gender, travel often, have more experiences, and actively post reviews. When asked for hotel reviews, they tend to give lower ratings. Hsiao et al. [9] predicted the reviewers’ helpfulness ratings by examining their review behaviors and trust networks.

In general, such a classi<sup>fi</sup>cation system can be realized by two approaches: (1) a simplistic approach that estimates a review’s helpfulness based on its explicit helpfulness ratings and (2) an approach that uses explicit helpfulness ratings on an available training set to train a model/ classi<sup>fi</sup>er that predicts if a review or reviewer is helpful based on the review features. The explicit user-rating of reviews has salient features such as simplicity and practical feasibility, but comes with some pro blems such as sparseness [1,10], a winner’s circle bias [11], and skewness [12]. Several studies have thus been conducted to investigate how the evaluation of a reviewer is managed. For example, the prediction system by Ku et al. [1] constructed a web of trust (WoT) from a network of reviewers and readers in an opinion-sharing community and analyzed its structure by employing social network analysis to derive the impact factors pertaining to the helpfulness ratings of reviewers. However, the basic concept of this method is based on social relations among members; thus, the method could be manipulated [13,14]. Furthermore, review ratings could not be calculated when there are no paths from the source to any people who have rated the focal product [15]; thus, it clearly cannot function in such an environment. Finally, the formation of a WoT requires members to identify others they trust in addition to providing product ratings, which might limit the applicability of the model.

The ways in which a reviewer’s contribution can be earned include quanti<sup>fi</sup>able knowledge of a domain, quality content, or social networks [16]. In response to concerns about using a social network approach, such as applying the WoT in estimating a reviewer’s helpfulness rating, this study turns to the factor of domain knowledge and quality content. Human knowledge is in general expressed in language [17], and re viewers with good domain knowledge tend to write higher quality reviews and provide more useful information to readers; thus, they receive higher evaluations by other members and so become more helpful [16,18]. As stated in previous studies, written language is an intangible asset [2], which varies from person to person [3], thus making it dif-<sup>fi</sup>cult to manipulate. Language usage has been shown to have a signi<sup>fi</sup>cant in<sup>fl</sup>uence on helpfulness ratings. It plays a very important role in this process between the reviewer and reviewee and in<sup>fl</sup>uences the readers’ cognition and behavior [5]. Li and Zhan [19] found that the perceived helpfulness of reviews and reviewers is signi<sup>fi</sup>cantly impacted by language styles, organizational structure, and other content features of online product reviews. Kim et al. [20] examined the di<sup>f</sup>erent classes of language-use features most important to capture review helpfulness. Zhang and Varadaraja [21] proposed a method of text sentiment analysis to predict the utility of product reviews by capturing linguistic phenomena.

Therefore, this study is devoted to develop a prediction model, named L<sup>2</sup>HR (Linguistics-based Locator for Helpful Reviewers) by applying the language-use approach to overcome the shortcomings of the social-relation based approach. The model is trained by using a history of available explicit user ratings to allow the automatic identi<sup>fi</sup>cation and prediction of helpful reviewers. The research question of this study is thus “Does reviewers’ language usage have an impact on predicting their helpfulness ratings?” We examine the research question by testing the proposed model L<sup>2</sup>HR, the baseline model, and a hybrid one, to compare their performance in predicting helpful reviewers in an opinion-sharing forum. The results show that L<sup>2</sup>HR performs better than WoT; thus, a person’s words, especially her/his linguistic style, have a greater impact on predicting the helpfulness rating. However, the hybrid model performs better than each of these two methods alone; therefore, a reviewer would be categorized as more helpful if she or he knows how to combine these two aspects, linguistic style and social relations.

The remainder of this paper is organized as follows. Section 2 provides the theoretical foundation on which this study is grounded. Section 3 then introduces the proposed L<sup>2</sup>HR model with respect to its ability to characterize reviewers’ helpfulness ratings accurately. Next, Section 4 describes the empirical design and evaluation of the proposed linguistic model. Finally, the conclusions of this work are presented in Section 5, along with recommendations for future research.

## 2. Theoretical foundation

Previous studies stated that writing is a stable, reliable, and personalized trait, and it has thus been reported that text analysis programs can be used to link natural language characteristics to personality measures [22–25]. Language use is considered a psychological marker, and one of the many methods to analyze it is the word count approach, which exists for both the analysis of content (what is being said) and linguistics style (how it is being said) [21]. Moreover, individuals express their knowledge and ideas by their own distinct styles, with lin guistic style being unique from person to person [3,22,24]; as such, linguistic style can be used as a re<sup>fl</sup>ection of individual di<sup>f</sup>erences. Because linguistic style is persistent for each person and does not change from text to text, this study will be characterizing the style of each reviewer, and not of each review. In this study, we consider four stylistic aspects of language use, namely credibility, readability, evidentiality, and LIWC factors, identi<sup>fi</sup>ed by a comphensive survey of the related literature, to predict reviewers’ helpfulness ratings.

## 2.1. Credibility

Reviews reveal not only the quality of a person’s writing but also how they share knowledge with others; therefore, it can be said that the quality of reviews represents the expertise of the contributing author [1]. From our literature survey, in some cases, credibility has been deemed one of the important characters of reviewers’ ratings. For example, Rubin and Liddy [18] took credibility into consideration and compiled a list of indicators to assess the credibility of blogs, which consisted of several main categories: the blogger’s expertise and o<sup>fl</sup>ine identity disclosure, the blogger’s pro<sup>fi</sup>le and value system, information quality, and appeals and triggers of a personal nature. The study included both text and member-oriented features, with the most important being the concept of evidentiality, which is a mode of knowing, in the category of blogger expertise. Metzger [26] pointed out that credibility is a multifaceted concept with two primary dimensions, which were utilized to improve the information retrieval process in his research. Customers tend to vote for reviewers having source cred ibility; as a result, their helpfulness ratings are increased [26]. Based on the framework presented by Rubin and Liddy [18], Weerkamp and Rijke [27] considered various credibility textual indicators to improve the quality of information retrieval and found that they had a signi<sup>fi</sup>cant positive impact on topical post-retrieval e<sup>f</sup>ectiveness. The studies proposed eleven credibility indicators that are textual in nature including capitalization, emoticons, shouting, spelling errors, length, timeliness, semantics, spam and comments, regularity, and consistency. In this study, we focused on indicators that can be derived from reviewers’ reviews and are more related to the linguistic styles of the reviewers, namely capitalization, emoticons, shouting, and misspelling, which a<sup>f</sup>ect reviewer’s helpfulness rating.

## 2.2. Readability

Although there are di<sup>f</sup>erent de<sup>fi</sup>nitions given in the literature, in general, readability is what makes some texts easier to read than others [28]. It was stated as the level to which a reading text can improve the readers’ comprehension, retention, and reading speed [29]. By focusing on the issue of writing style, Klare [30] de<sup>fi</sup>ned readability as “the ease of understanding or comprehension due to the style of writing,” rather than other issues such as content, coherence, and organization. From the viewpoint of the interaction between the text and readers in terms of known characteristics including reading skill, prior knowledge, and motivation, McLaughlin [31] de<sup>fi</sup>ned readability as “the degree to which a given class of people <sup>fi</sup>nds certain reading matter compelling and comprehensible.”

In the context of online sharing communities, the analysis of a reviewer’s readability can identify the indicators of readability that can improve the helpfulness of reviews, thereby increasing the reviewer’s helpfulness recognition [29]. Liu and Park [32] investigated the impact of readability in terms of what makes an online review receive votes. The <sup>fi</sup>ndings indicated that less-readable reviews were more likely to receive votes. Similar recent works on the correlation of readability to the analysis of online reviews include [4,33,34]. Our work follows the above de<sup>fi</sup>nitions, in particular [29] to explore the impact of readability on estimating the reviewers’ helpfulness ratings by analyzing their linguistic styles. Moreover, it is expected that helpful reviewers tend to write more readable reviews to impact members’ willingness to give a positive rating.

## 2.3. Evidentiality

Chafe [35] de<sup>fi</sup>ned evidentiality as the linguistic representation of evidence for a statement and its use as an explicit linguistic system to encode the quality of information; accordingly, it o<sup>f</sup>ers obvious and straightforward evidence for text trustworthiness detection [36,37]. Palmer [38] de<sup>fi</sup>ned evidentiality as a subcategory of modality. Mod ality refers to modal markers, such as English modal verbs (e.g., can, may, and must), and is treated as a single grammatical category in linguistics. More broadly, evidentiality is de<sup>fi</sup>ned as the expression of a speaker’s attitude toward the information being presented [35]. The linguistic de<sup>fi</sup>nition of evidentiality has two dimensions, i.e., as a label to indicate the source of information about narrated events [37], and more narrowly de<sup>fi</sup>ned, as the evidence through which information is acquired [39]. We can thus infer that evidentiality has two main functions: indicating the source of knowledge and indicating the speakers’ degree of certainty about their statement. These functions can be detailed as follows:

(1) Information can be acquired based on observation, hearsay, in ference, and memory.

(2) The speaker’s degree of certainty, including certain propositional attitudes (e.g., think and guess) and adverbials (e.g., certainly and surely), also implies epistemic models (e.g., may and ought to).

Su et al. [36] proposed a linguistic model of evidentiality, in which the concept was incorporated into a machine learning-based text classi<sup>fi</sup>cation framework. Along with their results, evidential information provides important clues that can be used in predicting the values of a text. Accordingly, evidentiality should be able to be adapted to the evaluation of review helpfulness and prediction of helpful reviewers.

## 2.4. LIWC factors

The words people use in their daily lives reveal important aspects of their personality traits. With advances in computer technology, text analysis now enables researchers to reliably and quickly assess features of what people say, as well as subtleties in their linguistic styles. It was recently con<sup>fi</sup>rmed by Wang and Karimi [40] that linguistic style, especially writing style, signi<sup>fi</sup>cantly a<sup>f</sup>ects review helpfulness. Various text analysis tools have been developed that link natural word use to personality. Linguistic Inquiry and Word Count (LIWC) is one such tool [41]. LIWC utilizes a psychological word count approach by counting words within a given text sample irrespective of the context in which the words occur, to track the stylistic aspects of the language employed.

LIWC analyzes the content of a text <sup>fi</sup>le based on its dictionary containing more than 4800 words grouped into over 70 categories, which are in turn consolidated into four dimensions: linguistic (e.g., articles, prepositions, and pronouns), psychological processes (e.g., positive and negative emotion categories), relativity-related words (e.g., time, verb tense, and space), and traditional content dimensions (e.g., sex, death, home, and occupation). Each word may be assigned to more than one category. With text scanning and recognition, LIWC generates the percentage of each category the text belongs to. In the linguistic dimension, 15 most promising features were factorized as four LIWC factors and labeled as Immediacy, Making Distinctions, Social Past, and Rationalization [3].

LIWC allows researchers to explore textual linguistic features, such as the quantity of pronouns and the number of positive and negative emotion words that occur in text-based data. Thus, in online sharing communities, it helps to <sup>fi</sup>nd reviewers who write good quality contents, and impacts on reviewers’ helpfulness ratings [42]. In addition, Peng et al. [43] analyzed LIWC features in review contents and found a signi<sup>fi</sup>cant impact of review length and emotional intensity on the helpfulness of review and reviewers. Hence, in this study, we adopted the four LIWC factors when analyzing linguistic styles to predict reviewers’ helpfulness ratings.

## 2.5. Summary

In this study, the above four stylistic aspects of a reviewer’s language usage in written reviews are considered for di<sup>f</sup>erentiating high and low helpful reviewers. Their impact on the categorization of reviewers is assessed by explanatory statistical modeling, i.e., logistic regression. In the following, the well-recognized classi<sup>fi</sup>cation method, support vector machine (SVM), is adopted to perform predictions to validate its e<sup>f</sup>ectiveness. The proposed model is then compared with the baseline model, WoT, which has already been well established in the study of identifying helpful reviewers, as well as a hybrid model using both L<sup>2</sup>HR and WoT. We also consider another important factor, namely product type, which in<sup>fl</sup>uences the intention of writing reviews within opinion-sharing forums [5]. Two representatives of experience and search products, movies [44] and electronics [45], respectively, are used for the experiments.

Our proposed model di<sup>f</sup>ers from the work on WoT [1], which adopted a reviewer’s social network to estimate his/her helpfulness ratings. Our model also di<sup>f</sup>ers from the one proposed by Ghose and Ipeirotis [29], which analyzed reviewers’ writing styles to build a mode of predicting the helpfulness of a review and examining its impact on sales, rather than predicting reviewers’ helpfulness ratings. Moreover, inspired by the work on WoT, this study examines the research question “Does reviewers’ language usage have an impact on predicting their helpfulness ratings?” Exploring the answer to this question would help readers and stakeholders to truly understand which factors signi<sup>fi</sup>cantly a<sup>f</sup>ect reviewers’ helpfulness ratings, and thus, they can focus on and strengthen these while writing their reviews.

![](/api/attachments/9SPC426X/fulltext/images/e4cbe22f078cb24497087a1fb56b317319d068db3e160aa5fae7c5a0cca3b53a.jpg)  
Fig. 1. The system framework of the proposed L<sup>2</sup>HR.

![](/api/attachments/9SPC426X/fulltext/images/050509d6fcde51dc3c61f4f6e8d83aac894e7952386128055caa2167d3894c28.jpg)  
Fig. 2. The high-level algorithm of the prediction model.

## 3. Research methodology

The system framework of $L ^ { 2 } H R$ is outlined in Fig. 1, and the high level algorithm of the prediction model is shown in Fig. 2. Functionally speaking, the construction procedure of $L ^ { 2 } H R$ is divided into three main tasks. The <sup>fi</sup>rst is to retrieve and preprocess review database including text of reviews from the opinion-sharing community; the second is to extract and assess the language features of reviews by explanatory statistic modeling in order to generate the signi<sup>fi</sup>cant features and prepare labels for a reviewer’s helpfulness rating; and, the third step is to train the helpfulness-rating classi<sup>fi</sup>er in order to predict reviewers helpfulness rating (high or low). Each system component is described in detail as follows.

## 3.1. Web crawling

The purpose of this step is to collect the relevant data, namely reviews and reviewers, for use in the experiment. To this end, a web crawler was designed to retrieve up-to-date product information (for both electronic goods and movie categories) and reviews from Epinion.com. The gathered product information is further parsed and extracted by using regular expressions, which is a widely used approach for extracting words related to speci<sup>fi</sup>c patterns from online content. In this manner, detailed information from the site that is needed in our model and the baseline model can be identi<sup>fi</sup>ed, namely the intensity and average intensity of trustors (readers who give trust scores), the degree of reviewers devoted to a speci<sup>fi</sup>c category (see Fig. 3, for an example of this), and the average product ratings. The retrieved reviews and product information are then stored in the Review database.

## 3.2. Data preprocessing

This step focuses on the procedure used to formalize the content of the reviews so that the retrieved reviews can be analyzed. First, tables, <sup>fi</sup>gures, and non-textual elements are removed from the collection of reviews to build a raw text corpus for processing. Next, tokenization i applied to divide reviews into analytical units. Di<sup>f</sup>ering from traditional text mining in which stop words are treated as useless, and often removed, in our approach, every term in English has a di<sup>f</sup>erent syn tactical form based on its role and usage in di<sup>f</sup>erent contexts. In addition, the writing style is in<sup>fl</sup>uenced by the ratio of the number of stop words to the total number of words; therefore, because di<sup>f</sup>erent authors have di<sup>f</sup>erent writing styles, the frequency of stop words will be di<sup>f</sup>erent [46,47]. Furthermore, the word count of function words is used in the subsequent analysis, and thus, stop and stemming words are also included in the analysis.

## 3.3. Label preparation

In order to facilitate the assessment of stylistic aspects by logistic regression and training the classi<sup>fi</sup>er, the reviewers under investigation must be labeled as belonging to either high or low helpful groups in advance. The labeling task can be done by using a gold standard dataset (if it already exists for related domain) or manual processing. For example, Jin and Liu [48] carried out a manual score evaluation using six full-time <sup>fi</sup>nal year undergraduate students. In the study conducted by Ghose and Ipeirotis [29], two human coders were asked to analyze the contents of a sample of 1000 reviews. This problem can also be solved by ranking and categorizing the helpfulness ratings the reviewers receive from peer evaluations [1,49–51]. We adopted this approach because the baseline model [1] is used for performance comparison. However, other labeling ways can also be applicable to the proposed system. Note that label preparation is needed only during model construction for training; once the trained model is deployed, L<sup>2</sup>HR automatically predicts a reviewer’s helpfulness rating upon his/her new reviews collected and analyzed.

## 3.4. Extraction of stylistic features

According to the discussion in Section 2, linguistic style is persistent for each person and is invariant from text to text, therefore, four stylistic aspects were adopted to characterize the style of each reviewer. As a reviewer tends to write more than one review in online communities (a set of reviews), we need to aggregate their reviews to predict his/her helpfulness rating in a period of time. The extraction of stylistic features of each reviewer is implemented and detailed as follows.

## 3.4.1. Credibility

In this study, credibility was calculated based on four indicators from the framework proposed by Weerkamp and Rijke [27], namely capitalization, emoticons, shouting, and misspelling. First, the proper use of capitalization represents a good linguistic style, which contributes to a sense of credibility. Second, emoticons, one of nonverbal cues for communicating emotions [52,53], refer to the excessive use of western style emoticons (e.g., :-) and :-D), which denote a less credible linguistic style. To count the proportion of emoticons, we utilize SentiStrength, a sentiment analysis program [54]. SentiStrength is designed for the sentiment analysis of social network texts and has been applied to analyze Twitter comments [54]. The SentiStrength tool has also been used in [55] for assessing emotional positive and negative scores for a review to understand the correlation between the emotional scores and the helpfulness votes. Third, words written in all capitals are considered shouting, which is indicative of non-credible writing. Finally, misspellings are analyzed because a credible reviewer ought to be able to write without many such errors, and thus, the more spelling errors that occur, the less credible we consider a text to be.

Given a review, each indicator of credibility is estimated by the pattern de<sup>fi</sup>ned in Eq. (1):

$$
X _ {i} = n (x) \cdot | x | ^ {- 1}\tag{1}
$$

where $X _ { i }$ is the score of indicator i, while n x( ) and x are de<sup>fi</sup>ned in Table 1 below. All values of each indicator for the reviews posted by a reviewer were aggregated to obtain the average value.

## 3.4.2. Readability

To assess the readability of a text, di<sup>f</sup>erent readability formulas have been proposed over the last 80 years [28]. In this study, we use the Flesch reading ease test [56], which is the most widely used formula and one of the most tested and reliable [28] ones, to calculate the readability score for every review, where a higher score indicates that the text is easier to read than those with lower scores. The U.S. government uses this method as the standard test of readability for its documents and forms and requires that life insurance policies have a Flesch reading ease score of 45 or greater. For comparison purposes, the average score of a 6th grade student’s assignment ranges from 60 to 70, while the score of Reader s Digest magazine is around 65.

![](/api/attachments/9SPC426X/fulltext/images/ee660cfe014931b70596562a3669e943dbb9307831ba3a4b142b6747803ffe63.jpg)  
Fig. 3. Web of trust of a reviewer.

Table 1  
Calculations of credibility.

<table><tr><td>Credibility</td><td>n(x)</td><td>|x|</td></tr><tr><td>Capitalization</td><td>Number of sentences starting with a capital</td><td>Number of sentences</td></tr><tr><td>Emoticon</td><td>Number of emoticons</td><td>Post length in words</td></tr><tr><td>Shouting</td><td>Number of all caps words</td><td>Post length in words</td></tr><tr><td>Misspelling</td><td>Number of misspelled words</td><td>Post length in words</td></tr></table>

The formula for the Flesch Reading Ease Score (FRES) [56] test is

shown in Eq. (2):

$$
\begin{array}{c} \text {Flesh Readibility Score = 206.835 - 1.015\left(\frac {total words}{total sentences}\right)} \\ - 8 4. 6 \Big (\frac {t o t a l s y l l a b l e s}{t o t a l w o r d s} \Big) \end{array}\tag{2}
$$

All FRES scores for the reviews written by a reviewer were ag gregated to obtain her/his average value.

## 3.4.3. Evidentiality

Evidentiality is based on a hierarchy, which forms a continuum, running from the highest to the lowest. Many hierarchical schemes have been proposed by researchers. This study adopted the four evidentiality categories proposed by Su et al.[36], as shown in Table 2. The evidentiality score for a review is de<sup>fi</sup>ned by Eq. (3):

$$
E v i d e n t i a l i t y = n (x) \cdot | x | ^ {- 1}\tag{3}
$$

where n x( ) is the number of evidentiality words in the review and x is the review length in words. All scores for the reviews by a reviewer were aggregated to obtain the average value.

Table 2  
Categories and items in evidentiality.

<table><tr><td></td><td>Absolute</td><td>High</td><td>Moderate</td><td>Low</td></tr><tr><td>Attributive/ modal adverb</td><td>Certainly, sure, of course, definitely, absolutely, undoubtedly</td><td>Clearly, obviously, apparently, really, always</td><td>Seemingly, probably</td><td>Maybe, personally, perhaps, possibly, presumably</td></tr><tr><td>Lexical verb</td><td>Report, certain</td><td>Believe, see</td><td>Seem, think, sound, remember, observe</td><td>Doubt, wish, wonder, infer, assume, forecast, fell, heard, hearsay</td></tr><tr><td>Auxiliary verb</td><td></td><td>Must</td><td>Ought, should, would, could, can</td><td>May, might</td></tr><tr><td>Epistemic adjective</td><td>Definite</td><td></td><td>Possible, likely, unlikely, probable, positive, potential</td><td>Not sure, doubtful</td></tr></table>

Table 3  
LIWC factors and subcategories.

<table><tr><td>LIWC factors</td><td>Subcategories</td><td>Examples</td></tr><tr><td rowspan="5">Immediacy</td><td>First-person singular</td><td>I, me, mine</td></tr><tr><td>Articles</td><td>A, an, the</td></tr><tr><td>Words of more than six letters</td><td>Is, does, hearShould, would, could</td></tr><tr><td>Present tense</td><td></td></tr><tr><td>Discrepancies</td><td></td></tr><tr><td rowspan="4">Making Distinctions</td><td>Exclusive</td><td>But, without, exclude</td></tr><tr><td>Tentative</td><td>Someone, something, sort of, somewhat</td></tr><tr><td>Negations</td><td></td></tr><tr><td>Inclusive</td><td>No, not, neverAnd, with, include</td></tr><tr><td rowspan="3">The Social Past</td><td>Past tense</td><td>Went, ran, had</td></tr><tr><td>Social</td><td>Mate, talk, they, child</td></tr><tr><td>Positive emotion</td><td>Love, nice, sweet</td></tr><tr><td rowspan="3">Rationalization</td><td>Insight</td><td>Think, know, consider</td></tr><tr><td>Causation</td><td>Because, effect, hence</td></tr><tr><td>Negative emotion</td><td>Hurt, ugly, nasty</td></tr></table>

## 3.4.4. LIWC factors

To analyze the language use of reviewers, we adopted the LIWC word-count approach, which was developed by Pennebaker and King [3]. Four relaiable LIWC factors, namely Immediacy, Making Distinctions, Social Past, and Rationalization, are used to help in character izing reviewers’ helpfulness ratings, which are themsleves composed of 15 subcategories in the linguistic dimension. Table 3 illustrates the factors, subcategories, and some representatives in each category.

Given a review, each LIWC factor is estimated by Eq. (4):

$$
X _ {i} = n (x) \cdot | x | ^ {- 1}\tag{4}
$$

where $X _ { i }$ is the score of LIWC factor i, n x( ) is the number of words appearing in all the subcategories of factor $i ,$ and x is the review length in words. A reviewer’s LIWC score for factor i is obtained by taking the average of the sum of scores for all the reviews he/she posted.

## 3.5. Explanatory statistic modeling on reviewers’ helpfulness ratings

Logistic regression, an explanatory statistical modeling method, is a form of regression used when the dependent variable is a binary <sup>fi</sup>eld and the independent variables are of any type. The method can be used to determine the e<sup>f</sup>ect size of independent variables on the dependent one and estimate how well independent variables explain or predict a nominally dependent variable; it can also be employed to rank the relative importance of independent variables and understand the impact of covariate control variables. Logistic regression applies maximum likelihood estimation after transforming the dependent variable into a logit variable.

In order to check the overall model <sup>fi</sup>t, this study used the following three measures. (1) The omnibus test of signi<sup>fi</sup>cance, which assesses whether at least one independent variable is capable of predicting the dependent variable. (2) The Hosmer-Lemeshow test, which is a statis tical test for goodness of <sup>fi</sup>t for the logistic regression model. A large chi-squared value (with low p-value < 0.05) indicates poor <sup>fi</sup>t, while a small value (with high p-value closer to 1) indicates a good model <sup>fi</sup>t. Nonsigni<sup>fi</sup>cance represents adequate goodness of <sup>fi</sup>t. Furthermore, (3) the Cox and Snell and Nagelkerke $R ^ { 2 } { \mathrm { , } }$ , which is a measure of predictive power, and thus indicative of how well the model, can predict the dependent variable based on the independent variables, where the higher the value, the better the goodness of <sup>fi</sup>t.

## 3.6. Prediction of reviewers’ helpfulness ratings

To facilitate the prediction of reviewers’ ratings, this study adopted an SVM, which is a supervised learning machine for pattern classi<sup>fi</sup>- cation and nonlinear regression developed by Vapnik et al. [57]. The

SVM has been widely used in many <sup>fi</sup>elds, including text mining [58]. In most cases, the generalization performance of SVM-based classi<sup>fi</sup>ers either matches or is signi<sup>fi</sup>cantly superior to those derived by other classi<sup>fi</sup>cation methods. This study employed LibSVM scripts (easy.py and grid.py) developed by Lin and Chang [59]. The kernel function is the default radial basis function (RBF), which has the following ad vantages: (1) it is capable of classifying nonlinear and high dimensional data and (2) the adjustment of only two arguments, gamma (-g) and cost (-c), leads to good performance with regard to predictions. We set the range of both arguments from $2 ^ { - 1 0 }$ to $\bar { 2 ^ { 1 0 } }$ and found the best performance by grid search. The prediction performance was evaluated in terms of well-known accuracy, recall, precision, and F-measures in machine learning [59].

## 4. Experiment and analysis

In this section, we <sup>fi</sup>rst explain the data collection and preprocessing procedures, followed by the experimental design. Then, we discuss the results of the explanatory statistical modeling with an emphasis on the stylistic features that can be used to identify reviewers’ helpfulness ratings. Finally, we evaluate the prediction performance of the proposed model to validate its e<sup>f</sup>ectiveness.

## 4.1. Data collection and data preprocessing

Following Ku et al. [1], we targeted a third-party product review website, Epinions.com, for our experiment. In their study, they de<sup>fi</sup>ned a valid reviewer of a given product category as a person who had submitted at least <sup>fi</sup>ve reviews in the focal category so that the problem of sparsity can be alleviated. In this manner, we collected 1541 and 1685 valid reviewers from the electronics and movies categories from July 1999 to Mar. 2013 and from Sept. 1999 to Mar. 2013, respectively.

Table 4 shows the descriptive statistics of both datasets. The <sup>fi</sup>rst quartile (Q1) is de<sup>fi</sup>ned as the middle number between the smallest number and median of the dataset, while the third quartile (Q3) is the middle value between the median and the highest value of the dataset. The values of Q1 and Q3 indicate that the distributions of average words are slightly skewed to the right in both datasets. Because electronics can be considered a search product requiring detailed information about speci<sup>fi</sup>cations and functionality, reviewers tend to write long reviews (average length = 1002.9 words) to introduce or comment on the product. On the other hand, movies are a kind of experience product for which reviewers are likely to express their own impressions or feelings after watching. Therefore, the average word length (770.2) of movie reviews is less than that of for electronics.

Table 5 presents the correlation tables for both products. It indicates that the stylistic features are mostly only slightly correlated with each other and thus are considered independent. Also following Ku et al. [1], the helpfulness ratings of reviewers were determined from the help fulness score of reviews. On the Epinions.com website, the helpfulness score represents readers’ evaluations of the quality of the product reviews. Speci<sup>fi</sup>cally, reviews can be categorized as “very helpful,” “helpful,” “somewhat helpful,” or “not helpful.” The four helpfulness levels were converted into numerical scales 3, 2, 1 and −2, respec tively. The helpfulness score of each review posted by a reviewer was

Descriptive statistics of both datasets.

<table><tr><td>Reviews description</td><td>Electronics</td><td>Movies</td></tr><tr><td>Total reviews</td><td>12283</td><td>8703</td></tr><tr><td>Average reviews per reviewer</td><td>9.86</td><td>6.38</td></tr><tr><td>Mean number of words</td><td>1002.9</td><td>770.2</td></tr><tr><td>Median</td><td>679.5</td><td>706</td></tr><tr><td>Q1</td><td>329</td><td>507</td></tr><tr><td>Q3</td><td>1340</td><td>955</td></tr></table>

Table 5  
Correlation tables for (a) electronics and (b) movies.

<table><tr><td>(a)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1. Capitalization</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Emoticons</td><td>0.172</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Shouting</td><td>0.496</td><td>0.120</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Misspelling</td><td>0.372</td><td>0.041</td><td>0.261</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Readability</td><td>-0.094</td><td>-0.052</td><td>-0.131</td><td>-0.113</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Evidentiality</td><td>0.462</td><td>0.164</td><td>0.496</td><td>0.407</td><td>-0.300</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>7. Make distinctions</td><td>-0.026</td><td>0.031</td><td>-0.067</td><td>0.029</td><td>-0.035</td><td>0.173</td><td>1</td><td></td><td></td><td></td></tr><tr><td>8. Immediacy</td><td>0.486</td><td>0.160</td><td>0.467</td><td>0.461</td><td>-0.251</td><td>0.755</td><td>0.103</td><td>1</td><td></td><td></td></tr><tr><td>9. Social past</td><td>-0.238</td><td>-0.063*</td><td>-0.328</td><td>-0.028</td><td>0.301</td><td>-0.229</td><td>0.227</td><td>-0.133</td><td>1</td><td></td></tr><tr><td>10. Rationalization</td><td>0.068</td><td>0.040</td><td>0.043</td><td>0.077</td><td>-0.284</td><td>0.272</td><td>0.143</td><td>0.248</td><td>-0.030</td><td>1</td></tr><tr><td>(b)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>1. Capitalization</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Emoticons</td><td>0.056</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Shouting</td><td>0.180</td><td>0.066</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Misspelling</td><td>0.225</td><td>0.020</td><td>0.110</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Readability</td><td>0.057</td><td>0.072</td><td>-0.043</td><td>-0.221</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Evidentiality</td><td>0.264</td><td>0.061</td><td>0.160</td><td>0.450</td><td>-0.345</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>7. Make distinctions</td><td>0.042</td><td>0.057</td><td>-0.002</td><td>-0.005</td><td>0.236</td><td>0.151</td><td>1</td><td></td><td></td><td></td></tr><tr><td>8. Immediacy</td><td>0.324</td><td>0.109</td><td>0.151</td><td>0.267</td><td>-0.186</td><td>0.636</td><td>0.091</td><td>1</td><td></td><td></td></tr><tr><td>9. Social past</td><td>-0.051</td><td>0.060</td><td>-0.076</td><td>-0.158</td><td>0.545</td><td>-0.208</td><td>0.159</td><td>-0.120</td><td>1</td><td></td></tr><tr><td>10. Rationalization</td><td>0.076</td><td>0.052</td><td>0.047</td><td>0.104</td><td>-0.152</td><td>0.268</td><td>0.062</td><td>0.250</td><td>-0.087</td><td>1</td></tr></table>

Table 6  
Summary of reviewers labeled as high or low helpfulness ones.

<table><tr><td rowspan="3">Product</td><td rowspan="3">Total reviewers</td><td colspan="3">Low helpfulness scores</td><td colspan="3">High helpfulness scores</td></tr><tr><td rowspan="2">Number of reviewers</td><td colspan="2">Helpfulness score</td><td rowspan="2">Number of reviewers</td><td colspan="2">Helpfulness score</td></tr><tr><td>Min</td><td>Max</td><td>Min</td><td>Max</td></tr><tr><td>Electronics</td><td>1243</td><td>619</td><td>-1</td><td>2.2</td><td>624</td><td>2.71</td><td>3</td></tr><tr><td>Movies</td><td>1365</td><td>686</td><td>1.9</td><td>2.5</td><td>679</td><td>2.93</td><td>3</td></tr></table>

Table 7  
Logistic regression results of L<sup>2</sup>H $L ^ { 2 } H R$ for the electronics dataset.

<table><tr><td></td><td>B</td><td>S.E.</td><td>Wald</td><td>Sig.</td><td>Exp(B)</td></tr><tr><td colspan="6">Variables</td></tr><tr><td>Shouting</td><td>.047</td><td>.020</td><td>5.367</td><td>.021*</td><td>1.049</td></tr><tr><td>Misspelling</td><td>-.075</td><td>.031</td><td>5.965</td><td>.015*</td><td>.928</td></tr><tr><td>Readability</td><td>-.023</td><td>.010</td><td>4.969</td><td>.026*</td><td>.977</td></tr><tr><td>Evidentiality</td><td>.298</td><td>.029</td><td>109.314</td><td>.000***</td><td>1.347</td></tr><tr><td>Making distinctions</td><td>-.558</td><td>.166</td><td>11.336</td><td>.001**</td><td>.573</td></tr><tr><td>Immediacy</td><td>.114</td><td>.030</td><td>14.038</td><td>.000***</td><td>1.121</td></tr><tr><td>Social past</td><td>-.330</td><td>.101</td><td>10.777</td><td>.001**</td><td>.719</td></tr><tr><td>Rationalization</td><td>-.523</td><td>.210</td><td>6.207</td><td>.013*</td><td>.593</td></tr><tr><td>Constant</td><td>1.498</td><td>.969</td><td>2.388</td><td>.122</td><td>4.473</td></tr></table>

Notes: -2LL=1103.177; Cox and Snell $R ^ { 2 } { = } 0 . 3 9 3 ;$ Nagelkerke $R ^ { 2 } { = } 0 . 5 2 4 ;$ Omnibus test: $X _ { ( d f = 8 ) } ^ { 2 } = 6 1 9 . 9 6 7$ $( p \textless 0 . 0 0 1 )$  
\*\* and \*\*\* indicate signi<sup>fi</sup>cance at the 5%, 1% and 0.1% levels, respectively. ，

calculated, after which his/her overall helpfulness score was determined by taking the average of all his/her reviews. After sorting reviewers by the overall helpfulness score, the top 40% were marked as the high helpfulness group, while the bottom 40% were considered the low helpfulness group. The middle part of the dataset was eliminated in order to minimize e<sup>f</sup>ects of possibly biased peer evaluations [1]. As a result, 1243 and 1365 valid reviewers from the electronics and movies categories, respectively, were used in the following experiment. Based on the categorization of reviewers into the high and low helpfulness groups, the electronics dataset included 624 high and 619 low help fulness reviewers, while the movies dataset had 679 high and 686 low helpfulness rating reviewers. Table 6 presents a statistical summary of the datasets used in the subsequent analysis.

In the following, we discuss the evaluation comparison of our proposed L<sup>2</sup>HR model and the baseline model (WoT) [1], in which <sup>fi</sup>ve variables were considered to analyze their relationship with the grouping of reviewers. The <sup>fi</sup>ve variables include trust intensity, average trust intensity of trustors, degree of review focus in the target category, average product rating in the target category, and number of reviews in the target category. It should be noted that the last variable was excluded from our experiment because it did not have any signi<sup>fi</sup>cant e<sup>f</sup>ect on helpfulness classi<sup>fi</sup>cation as shown in [1].

## 4.2. Explanatory statistical analysis

## 4.2.1. Analytic results

We <sup>fi</sup>rst used logistic regression to examine the relationships of stylistic features with the binary dependent variable, indicating the category a reviewer is assigned to for the dataset of electronics. Using the backward stepwise (Wald) method, the experimental results obtained by L<sup>2</sup>HR are shown in Table 7. Moreover, the numbers indicate that the statistical results of the Cox and Snell $R ^ { 2 } { \mathrm { , } }$ , and Nagelkerke $R ^ { 2 }$ values are 0.393 and 0.524, respectively, thus indicating a satisfactory explanatory power of the logistic regression model. The results also show that the omnibus test of overall <sup>fi</sup>t $( X ^ { 2 } = 6 1 9 . 9 6 7$ and $p \ : < \ : 0 . 0 0 1 )$ is highly signi<sup>fi</sup>cant, which indicates that the goodness of <sup>fi</sup>t of the model is acceptable. The signi<sup>fi</sup>cance levels for the Wald statistic show that the following eight predictors have signi<sup>fi</sup>cant in<sup>fl</sup>uence on reviewers’ helpfulness categorization: shouting $( p < 0 . 0 5 )$ , misspelling $( p < 0 . 0 5 )$ , readability $( p < 0 . 0 5 )$ , evidentiality $( p < 0 . 0 0 1 )$ , making distinctions $( p < 0 . 0 1 )$ immediacy $( p < 0 . 0 0 1 )$ social past $( p < 0 . 0 1 )$ , and rationalization $( p < 0 . 0 5 )$ . The results show that shouting, immediacy, and evidentiality positively impact reviewers categorization, with evidentiality having more explanatory power, which means that it can be used to explain the results successfully. In addition, other factors, namely misspelling, readability, making distinctions, social past, and rationalization, were found to have negative impacts on helpfulness categorization.

Table 8  
Logistic regression results of L<sup>2</sup>HR for the movies dataset.

<table><tr><td></td><td>B</td><td>S.E.</td><td>Wald</td><td>Sig.</td><td>Exp(B)</td></tr><tr><td colspan="6">Variables</td></tr><tr><td>Capitalization</td><td>.153</td><td>.055</td><td>7.676</td><td>.006**</td><td>1.166</td></tr><tr><td>Readability</td><td>-.081</td><td>.010</td><td>61.785</td><td>.000***</td><td>.922</td></tr><tr><td>Evidentiality</td><td>.496</td><td>.029</td><td>291.05</td><td>.000***</td><td>1.642</td></tr><tr><td>Making distinctions</td><td>-.660</td><td>.167</td><td>15.554</td><td>.000***</td><td>.517</td></tr><tr><td>Constant</td><td>2.976</td><td>.747</td><td>15.865</td><td>.000***</td><td>19.607</td></tr></table>

Note: $- 2 \mathrm { L L } = 9 6 4 . 0 4 7 ;$ Cox and Snell $R ^ { 2 } = 0 . 4 9 3 ;$ Nagelkerke $R ^ { 2 } { = } 0 . 6 5 8 ;$ Omnibus test: $X _ { ( d f = 4 ) } ^ { 2 } = 9 2 8 . 2 0 9$ (p < 0.001).  
\*, \*\* and \*\*\* indicate signi<sup>fi</sup>cance at the 5%, 1% and 0.1% levels, respectively. 4

Next, we focus on our study’s experience product, movies. As in the previous experiment with electronics, we used the backward stepwise method of logistic regression to analyze the explanatory power of our proposed L<sup>2</sup>HR model and the baseline model (WoT) [1]. The results are presented in Table 8, which shows the statistical results in terms of the Cox and Snell $R ^ { 2 }$ and Nagelkerke $R ^ { 2 }$ values, which are 0.493 and 0.658, respectively, suggesting the satisfactory explanatory power of the lo gistic regression model. The omnibus test of overall <sup>fi</sup>t $( X ^ { 2 } = 9 2 8 . 2 0 9$ and $\mathsf { p } < 0 . 0 0 1 )$ is highly signi<sup>fi</sup>cant, thus indicating an acceptable goodness of <sup>fi</sup>t of the model. The signi<sup>fi</sup>cance levels for the Wald statistics show that the four predictors are signi<sup>fi</sup>cant: capitalization $( \mathbf { p } < 0 . 0 1 )$ , readability $( \mathbf { p } < 0 . 0 0 1 )$ , evidentiality $( \mathbf { p } _ { \mathbf { \lambda } } < \mathbf { \lambda } 0 . 0 0 1 )$ ), and making distinctions $( \mathbf { p } < 0 . 0 0 1 )$

## 4.2.2. Discussions

From the analytical results, we found dissimilarities within the datasets between independent and dependent variables. It was found that for the electronics dataset (search product), the eight independent variables had consistent correlations with the dependent variable. More speci<sup>fi</sup>cally, three of the eight independent variables, namely shouting, immediacy, and evidentiality, were positively correlated with high helpfulness. However, misspelling, making distinctions, social past, rationalization, and readability were negatively correlated with high helpfulness. Moreover, the Wald statistic for evidentiality emerged as the highest among all independent variables, which suggests that it has the greatest explanatory power. With regard to the movies dataset (experience product), the four independent variables had consistent correlations with the dependent variable. In particular, capitalization and evidentiality were positively correlated with high helpfulness; however, readability and making distinctions were negatively corre lated with high helpfulness.

In both datasets, readability and making distinctions were negatively correlated with high helpfulness; however, evidentiality had a highly positive correlation with high helpfulness. These <sup>fi</sup>ndings are consistent with earlier works [29,32], which indicated that less-read able reviews are more likely to receive helpful votes. Therefore, the Flesch index might be negatively correlated with a reviewer’s help fulness rating.

For electronics, immediacy was positively related to helpfulness ratings. We also found that helpful reviewers tend to use more immediacy words, which can linguistically express their attitudes as well as provide more indications of the nature of the evidence being presented. This concept is consistent with a study by Fast and Funder [60], who showed that authors with a higher immediacy factor tend to write more articles that are highly intellectual and open to experience. Another noteworthy <sup>fi</sup>nding was that misspelling, social past, and rationalization were negatively related to high helpfulness ratings, which is also consistent with the results of Weerkamp and Rijke [27]. This con<sup>fi</sup>rms that using poor spelling, more past tense, positive and negative social emotion, and causation will often decrease the credibility of information, thus leading to a worse helpfulness. One additional interesting point is the <sup>fi</sup>nding that shouting was positively related to helpfulness ratings, which is inconsistent with the results of Weerkamp and Rijke [27], who showed that using constant shouting $\left( \mathbf { e . g . } \right.$ , using all capitals) is considered an indicator of low-credibility information. A possible explanation for this is that more helpful reviewers tend to have shouting or attention-seeking behavior to make reviews themselves more prominent and therefore attract readers’ attention more and as a result become more helpful.

For the movies dataset, capitalization was positively correlated with helpfulness rating. On this point, our <sup>fi</sup>nding is consistent with that of Weerkamp and Rijke [27], who stated that capitalization could be considered an indicator of a good writing style that adds a sense of credibility. In other words, in readers’ eyes, using capitalization correctly can represent not only good writing skills but also attention to detail, both of which could translate into a reviewer developing better helpfulness.

## 4.3. Prediction analysis

## 4.3.1. Analytic results

Now that the explanatory analytic results have identi<sup>fi</sup>ed the sig ni<sup>fi</sup>cant stylistic features that determine reviewers’ helpfulness ratings, we investigate the prediction ability of the proposed model. The data sets were partitioned chronologically into training and test sets in a ratio of 2:1 in order to evaluate the out-of-sample prediction performance. The well-known LibSVM Library [59] with the default RBF kernel function was adopted for the experiment. Grid search was used in the training process to <sup>fi</sup>nd the optimal parameters, hyperparameter $C ,$ and the kernel parameter σ. The prediction performance was evaluated by conducting a ten-fold cross-validation. Once the optimal parameters were established, the prediction performance was assessed using the test data. We averaged the results over 30 trials to make a fair comparison of both the proposed $L ^ { 2 } H R$ and WoT models.

First, we inspect the performance di<sup>f</sup>erence on L<sup>2</sup>HR by considering all the stylistic features and then only the signi<sup>fi</sup>cant ones. Table 9 illustrates the comparison results, which demonstrate that using only the signi<sup>fi</sup>cant features is better than using all the features in most performance measures, except for precision in the electronics category. The superiority was further con<sup>fi</sup>rmed by carrying out a pairwise t-test analysis $( p < 0 . 0 5$ and $p \ : < \ : 0 . 0 1 )$ , with signi<sup>fi</sup>cant di<sup>f</sup>erences denoted by an ‘\*’ in the table. The result veri<sup>fi</sup>es the theoretical and practical contributions of explanatory statistical analysis made to the stylistic aspects considered in this study.

Table 10 summarizes the comparison of the average classi<sup>fi</sup>cation performance and indicates that our proposed L<sup>2</sup>HR model outperform the WoT model in all measures on a larger scale when predicting

## Table 9

Prediction comparison by L<sup>2</sup>HR by using all the stylistic features and only signi<sup>fi</sup>cant features (in%).

<table><tr><td></td><td>Classifier</td><td>Accuracy</td><td>Recall</td><td>Precision</td><td>F-measure</td></tr><tr><td rowspan="2">Electronics</td><td>All features</td><td>78.83</td><td>75.60</td><td>80.92</td><td>78.04</td></tr><tr><td>Significant features</td><td> $79.73^*$ </td><td> $77.67^*$ </td><td>80.82</td><td> $79.17^*$ </td></tr><tr><td rowspan="2">Movies</td><td>All features</td><td>84.85</td><td>82.81</td><td>86.28</td><td>84.41</td></tr><tr><td>Significant features</td><td> $85.72^{**}$ </td><td> $84.69^*$ </td><td>86.54</td><td> $85.55^{**}$ </td></tr></table>

\* and \*\* indicate signi<sup>fi</sup>cance at the 5% and 1% levels, respectively.

Table 10  
Average prediction performance of L<sup>2</sup>HR and WoT (in%).

<table><tr><td></td><td>Classifier</td><td>Accuracy</td><td>Recall</td><td>Precision</td><td>F-measure</td></tr><tr><td rowspan="2">Electronics</td><td> $L^2HR$ </td><td>79.73***</td><td>77.67**</td><td>80.82***</td><td>79.17***</td></tr><tr><td>WoT</td><td>74.04</td><td>74.80</td><td>73.88</td><td>74.28</td></tr><tr><td rowspan="2">Movies</td><td> $L^2HR$ </td><td>85.72***</td><td>84.69**</td><td>86.54***</td><td>85.55***</td></tr><tr><td>WoT</td><td>78.31</td><td>82.31</td><td>76.34</td><td>79.02</td></tr></table>

\* and \*\* indicate signi<sup>fi</sup>cance at the 5% and 1% levels, respectively.

reviewers’ helpfulness ratings. The superiority was also con<sup>fi</sup>rmed a statistically signi<sup>fi</sup>cant $( p < 0 . 0 1$ and $p \ : < \ : 0 . 0 0 1 )$ . The L<sup>2</sup>HR model thus provides a more e<sup>f</sup>ective mechanism to predict helpful reviewers.

It is understood that biased helpfulness votes and fake reviewers could exist in an opinion-sharing community, which may lead to an unreliable evaluation score. As mentioned in the data preprocessing procedure, reviewers were separated into high and low helpfulness groups before training according to whether their average helpfulness scores were in the top or bottom 40%, respectively. Purposely excluding the middle 20% of reviewers may help to reduce the e<sup>f</sup>ects of possibly unreliable reader evaluations [1]. Moreover, it is essential to explore the impact of the threshold percentile on the prediction performance; therefore, a sensitivity analysis was performed. From Table 11 (a) and (b), it can be known that the smaller the threshold percentile, the better is the prediction performance for L<sup>2</sup>HR and WoT models in both datasets. This is because a stricter proportion of data extracted from the top and bottom average helpfulness scores leads to reducing more the impact of unreliable evaluations and the discrimination problem becoming simpler. In addition, Table 11(a) and (b) show that L<sup>2</sup>HR outperforms WoT consistently and signi<sup>fi</sup>cantly for all threshold values by a pairwise t-test analysis. From the result, we can conclude that re viewers’ words have more impact on locating helpful reviewers.

It has been suggested that combining members’ data exhausts in text, member actions, and social network data could lead to a more complete understanding of member behavior online [61]. In this experiment, we examined how good the prediction performance can be by the hybridization of social relations and language usage. Table 12 il lustrates the performance achieved by the hybridized method for both datasets. By referring to Tables 11 and 12, one may <sup>fi</sup>nd that the hybrid method outperforms L<sup>2</sup>HR in all measures in the cases of electronics and movies. It should be noted, however, that L<sup>2</sup>HR and the hybrid method perform better than WoT in both cases, which indicates that considering

## Table 11

Comparison with di<sup>f</sup>erent threshold values for electronics and movies datasets (in%).

<table><tr><td colspan="6">(a) electronics case</td></tr><tr><td>Threshold</td><td>Classifier</td><td>Accuracy</td><td>Recall</td><td>Precision</td><td>F-measure</td></tr><tr><td rowspan="2">20%</td><td> $L^2HR$ </td><td>87.53</td><td>83.57</td><td>91.03</td><td>87.06</td></tr><tr><td>WoT</td><td>77.61</td><td>75.29</td><td>79.40</td><td>77.21</td></tr><tr><td rowspan="2">30%</td><td> $L^2HR$ </td><td>82.92</td><td>77.45</td><td>85.63</td><td>81.16</td></tr><tr><td>WoT</td><td>76.66</td><td>75.98</td><td>74.59</td><td>75.15</td></tr><tr><td rowspan="2">40%</td><td> $L^2HR$ </td><td>79.73</td><td>77.67</td><td>80.82</td><td>79.17</td></tr><tr><td>WoT</td><td>74.04</td><td>74.80</td><td>73.88</td><td>74.28</td></tr></table>

<table><tr><td>Threshold</td><td>Classifier</td><td>Accuracy</td><td>Recall</td><td>Precision</td><td>F-measure</td></tr><tr><td rowspan="2">20%</td><td> $L^{2}HR$ </td><td>86.36</td><td>88.82</td><td>88.56</td><td>88.35</td></tr><tr><td>WoT</td><td>80.62</td><td>84.95</td><td>82.10</td><td>83.40</td></tr><tr><td rowspan="2">30%</td><td> $L^{2}HR$ </td><td>85.79</td><td>85.29</td><td>87.05</td><td>85.83</td></tr><tr><td>WoT</td><td>79.38</td><td>82.85</td><td>78.39</td><td>80.32</td></tr><tr><td rowspan="2">40%</td><td> $L^{2}HR$ </td><td>85.72</td><td>84.69</td><td>86.54</td><td>85.55</td></tr><tr><td>WoT</td><td>78.31</td><td>82.31</td><td>76.34</td><td>79.02</td></tr></table>

Table 12  
Average performance of hybridizing L<sup>2</sup>HR with WoT by SVM (in%).

<table><tr><td>Dataset</td><td>Threshold</td><td>Accuracy</td><td>Recall</td><td>Precision</td><td>F-measure</td></tr><tr><td rowspan="3">Electronics</td><td>20%</td><td>90.53</td><td>88.49</td><td>92.22</td><td>90.26</td></tr><tr><td>30%</td><td>87.58</td><td>83.86</td><td>89.51</td><td>86.56</td></tr><tr><td>40%</td><td>84.33</td><td>82.37</td><td>85.77</td><td>83.99</td></tr><tr><td rowspan="3">Movies</td><td>20%</td><td>89.72</td><td>89.08</td><td>92.50</td><td>90.73</td></tr><tr><td>30%</td><td>89.33</td><td>87.16</td><td>91.07</td><td>89.06</td></tr><tr><td>40%</td><td>88.67</td><td>86.69</td><td>90.30</td><td>88.44</td></tr></table>

both the linguistic style of reviewers’ words and their social relations is more e<sup>f</sup>ective than considering only the latter alone when the aim is to predict helpful reviewers.

## 4.3.2. Discussions

As proposed in previous studies [5,62], the types of products will impact the perceived importance of various information sources on the Internet. The experimental <sup>fi</sup>ndings in this study showed that a greater prediction performance was achieved with the movies dataset than that with the electronics one, for both prediction models. It is interesting to note that the performance for the movies was better than that for the electronics dataset. This result could be attributed to movie reviewers tending to express their feelings after watching a movie in a more subjective way; whereas, for a search product, writers are more likely to focus objectively on the details of the product itself. This <sup>fi</sup>nding is consistent with those of prior studies [1,63,64], which can be explained by the fact that the perceived bene<sup>fi</sup>ts of collecting online information for search and experience products are di<sup>f</sup>erent, with the latter relying more heavily on customer reviews. It has been reported that in terms of reviews, the primary aspect of search products (e.g., electronics) is that all related information can be scrutinized before any buying decision is made; this contrasts sharply with that for experience products (e.g. movies), for which related information can be known to buyers only after the purchase [65]. Therefore, consumers rely more on extrinsic clues to judge the quality of experience products compared to search products [66]. For example, the information needed to select a movie is more abstract and experience oriented than that needed to select a smartphone. Consequently, the recommendations of others are much more essential and meaningful for experience products than search products.

## 5. Conclusions and future work

The huge amount of information that is now available online makes it important to <sup>fi</sup>nd helpful reviewers that customers can listen to make their purchase decisions. Most existing studies have suggested that customers should follow advices from reviewers who have high helpfulness ratings; nevertheless, some have also noted the limitations existing in the social-relation approach toward identifying such reviewers. To alleviate the problems, this study proposed L<sup>2</sup>HR, by integrating the language usage approach and SVM in machine learning, a prediction model for automatically identifying helpful reviewers. An explanatory statistical analysis was performed to investigate the impact of stylistic aspects of a reviewer’s language usage so as to improve the prediction e<sup>f</sup>ectiveness. A performance comparison was conducted on its baseline model, namely WoT, the most recent and representative work using social relation [1]. The experimental results con<sup>fi</sup>rm the superiority of L<sup>2</sup>HR in achieving the research goal. In addition, better prediction results were obtained for the movies dataset than those for the electronics one for both models. This <sup>fi</sup>nding is consistent with previous studies, which have explained that consumers of experience products tend to share their experiences using more natural intrinsic writing styles than those of search products; accordingly, product type impacts the perceived importance of reviews.

The results show that the L<sup>2</sup>HR model performs better than the WoT model; thus, a person’s language usage, and especially linguistic style, has a signi<sup>fi</sup>cant impact on locating helpful reviewers. The hybrid model performs better than either of the methods used individually; thus, a reviewer’s helpfulness rating would be better if they know how to combine these two factors together.

With the e<sup>f</sup>ectiveness of the proposed model found in this work, we suggest the following important theoretical and practical implications.

## 5.1. Theoretical contribution and managerial implications

In terms of theoretical contribution, our study successfully identi <sup>fi</sup>ed and predicted reviewers’ helpfulness ratings using the language usage approach. Our proposed model thus contributes to theoretical research by presenting a new model to track helpful reviewers, using their stylistic aspects of language usage to alleviate the shortcomings in traditional social relation. Thus, this study extends earlier studies with its applications of computation linguistics and machine learning for verifying the e<sup>f</sup>ects of the proposed model. The other contribution is that which reviewers’ linguistics styles are signi<sup>fi</sup>cantly important with regard to their helpfulness ratings. This <sup>fi</sup>nding would help both readers and stakeholders to better understand which factors of language features have the greatest impact on reviewers’ helpfulness ratings; therefore, they can focus on these elements when producing reviews.

The proposed model also has signi<sup>fi</sup>cant managerial implications, as the identi<sup>fi</sup>cation of helpful reviewers based on their stylistic aspects in written language enables potential customers to quickly <sup>fi</sup>nd reliable information in order to make purchase decisions, while avoiding re views written by less helpful reviewers. First, our linguistic model can help manufacturers and retailers to <sup>fi</sup>nd helpful reviewers who can help spread product information rapidly in opinion-sharing communities, thus supporting marketing campaigns. Firms could therefore adopt marketing strategies based on in<sup>fl</sup>uential reviewers. For example, before launching products, manufacturers could o<sup>f</sup>er helpful reviewers the chance to try the new items, as any favorable evaluations would positively in<sup>fl</sup>uence other reviewers’ attitudes towards the products and thus increase sales. Moreover, <sup>fi</sup>rms should pay attention to the nega tive opinions expressed by the reviewers, as these can spread even faster and tend to have even more in<sup>fl</sup>uence than positive ones. Acknowledging the importance of reviewers by establishing a list of high helpful reviewers on opinion-sharing communities can also moti vate people to write higher quality reviews in order to contribute their expertise and experience to an online sharing-opinion forum. Second, with regard to reviewers, understanding which stylistic features in<sup>fl</sup>u ence their helpfulness ratings can help them adjust their writing style. Using the word-based categories of each aspect of each product type, reviewers can produce texts with more shouting, correct capitalization, immediacy, and evidentiality and fewer instances of misspelling, making distinctions, using social past, rationalization, and a lower readability, thus raising their helpfulness ratings. In addition, our study also found that di<sup>f</sup>erent product types have signi<sup>fi</sup>cant e<sup>f</sup>ects on the accuracy of the prediction of reviewers’ helpfulness ratings. This suggests that one may take product type into consideration to evaluate reviewer s helpfulness ratings when using the proposed L<sup>2</sup>HR model.

## 5.2. Limitations and future research directions

The present system relied on a machine learning paradigm for designing the SVM-based classi<sup>fi</sup>er. The method of preparing the labels for the high/low helpfulness rating groups followed the baseline model [1] as well as some representative models [49–51], which employed member-evaluated helpfulness scores provided by an opinion-sharing community to discriminate two groups of reviewers. Unfortunately, the dataset may also have the problems of biased helpfulness votes, fake reviewers, etc., thereby rendering the evaluation score unreliable. We addressed this issue in Section 4.3.2 in an attempt to reduce the e<sup>f</sup>ects of possibly unreliable reader evaluations. Nevertheless, the proposed system framework can easily incorporate other labeling methods, such as manual evaluation by human experts. It is recommended that future work include this consideration to render a more reliable system.

Next, in this study, the problem of predicting helpful reviewers is framed as predicting the helpfulness class of reviewers by considering personal-level linguistic features because linguistic style is an intangible asset, varying from person to person; therefore, it can be used as a re-<sup>fl</sup>ection of individual di<sup>f</sup>erences. However, the problem can also be framed as predicting review-level helpfulness from which reviewerlevel helpfulness can be simply derived. Therefore, an interesting future work is worthy to be explored: will review- and personal-level based feature extraction impact the prediction result? If a gold standard of ranking helpful reviewers exists, one may utilize ranking statistics to objectively evaluate both approaches so that a more e<sup>f</sup>ective locating system can be achieved. Furthermore, as associate editor advised, it should not be the issue of choosing personal-level or review-level features but the one of letting the data decide how much of the variance to put on the person and how much on each individual review. Toward this, multilevel models (hierarchical linear models) are worthy of in vestigation further.

Third, in order to identify the stable characteristics of reviewers, we adopted a word count approach of stylistic features to characterize reviewers’ helpfulness, and thus did not consider sentiment because content words may vary signi<sup>fi</sup>cantly when the topic changes. For members who wish to search for speci<sup>fi</sup>c products or reviews with positive sentiments, it is necessary to consider both content words and sentiment analysis in the future. Fourth, similar to reviews, writing styles can also be faked because reviewers might know how to better attract readers’ attention by utilizing speci<sup>fi</sup>c linguistic styles. How to screen fake stylistic patterns could be an interesting research topic. Finally, future studies should consider more product types and baseline models in the identi<sup>fi</sup>cation helpful reviewers to ensure that the proposed model is more reliable.

## Acknowledgments

This study was supported in part by the Ministry of Science and Technology, Taiwan, under contract NSC102-2410-H-006-054. The authors would like to commemorate Wen-Chi Chang for her contribution on the initial stage of the experiment. She passed away before the paper was completed.

## References

[1] Y.C. Ku, C.P. Wei, H.W. Hsiao. To whom should I listen? Finding reputable reviewers in opinion-sharing communities, Decis. Supp. Syst. 53 (2012) 534 542.

[2] G.M. Entwistle, F. Phillips, Relevance, reliability, and the earnings quality debate, Issues Account, Educ, 18 (2003) 79–92

[4] Y.H. Hu, K. Chen, Predicting hotel review helpfulness: the impact of review visibility, and interaction between hotel stars and review ratings, Int. J. Inf. Manage. 36 (2016) 929 944.

[5] S.M. Mudambi, D. Schuff, What makes a helpful online review? A study of customer reviews on amazon.com. MIS Q. 34 (2010) 185–200

[6] C. Forman, A. Ghose, B. Wiesenfeld, Examining the relationship between reviews and sales: the role of reviewer identity disclosure in electronic markets, Inf. Syst. Res. 19 (2008) 291–313.

[7] H.A. Lee, R. Law, J. Murphy, Helpful reviewers in TripAdvisor, an online trave community, Jo. Travel Tour, Market, 28 (2011) 675–688

[8] W. Hart-Davidson, M. McLeod, C. Klerkx, M. Wojcik, A method for measuring helpfulness in online peer review, Proceedings of the 28th ACM International Conference on Design of Communication, ACM, 2010, pp. 115–121.

[9] H.W. Hsiao, C.P. Wei, Y.C. Ku, L.A.C. Ng, Predicting the helpfulness of online product reviewers: a data mining approach, PACIS (2012) 134.

[10] Y. Lu, P. Tsaparas, A. Ntoulas, L. Polanyi, Exploiting social context for review quality prediction. Proceedings of the 19th International Conference on World Wide Web (2010).

[11] J. Liu, Y. Cao, C.Y. Lin, Y. Huang, M. Zhou, Low-quality product review detection in opinion summarization, Proceedings of the Joint Conference on Empirical Methods in Natural Language Processing and Computational Natural Language Learning (EMNLP-CoNLL) (2007) 334–342

[12] N. Ma, E.-P. Lim, V.-A. Nguyen, A. Sun, H. Liu, Trust relationship prediction using online product review data Proceedings of the 1st, ACM International Workshop or

Complex Networks Meet Information & Knowledge Management, ACM, 2009, pp. 47 54.

[13] M. Patel, Mining and predicting reviews to micro-reviews and detection of manipulated reviews for E-commerce websites, Int. J. Emerg. Technol. Comput. Sci. 2 (2017).

[14] I.E. Vermeulen, D. Seegers, Tried and tested: the impact of online hotel reviews on consumer consideration, Tour. Manage. 30 (2009) 123–127.

[15] J. Golbeck, Semantic Web interaction through trust network recommender systems, Int. Symp. Wearable Comput. 11 (2005).

[16] E.G. Toms, A.R. Taves, Measuring user perceptions of web site reputation, Inf. Process. Manage. 40 (2004) 291–317.

[17] M. Steedman, On becoming a discipline, Comput. Linguist. 34 (2008) 137–144.

[18] V. Rubin, E. Liddy, Assessing credibility of weblogs, Proceedings of the AAAI Spring Symposium: Computational Approaches to Analyzing Weblogs (CAAW) (2006).

[19] J. Li, L. Zhan, Online persuasion: how the written word drives WOM: Evidence from consumer-generated product reviews, J. Advert. Res. 51 (2011) 239–257.

[20] S.M. Kim, P. Pantel, C.T.M. Pennacchiotti, Automatically assessing review helpfulness, Proceedings of the 2006 Conference on Empirical Methods in Natural Language Processing, Sydney, Australia, Association for Computational Linguistics, 2006, pp. 423–430.

[21] Z. Zhang, B. Varadarajan, Utility scoring of product reviews, Proceedings of the 15th ACM International Conference on Information and Knowledge Management, ACM, 2006, pp. 51–57.

[22] J.M. Dewaele, A. Furnham, Personality and speech production: a pilot study of second language learners, Pers. Individ. Di<sup>f</sup>. 28 (2000) 355–365.

[23] C.J. Groom, J.W. Pennebaker, Words, J. Res. Pers. 36 (2002) 615–621.

[24] J.W. Pennebaker, T. Lay, Language use and personality during crises: analyses of mayor rudolph giuliani's press conferences, J. Res. Pers. 36 (2002) 271–282.

[25] F. Mairesse, M.A. Walker, M.R. Mehl, R.K. Moore, Using linguistic cues for the automatic recognition of personality in conversation and text, J. Artif. Intell. Res 30 (2007) 457 500.

[26] M.J. Metzger, Making sense of credibility on the web: models for evaluating online information and recommendations for future research, J. Am. Soc. Inf. Sci. Technol. 58 (2007) 2078–2091.

[27] W. Weerkamp, M.D. Rijke, Credibility improves topical blog post retrieval, Proceedings of ACL-08: HLT (2008).

[28] W.H. DuBay, The Principles of Readability, Impact Information, (2004) Available at http://www.nald.ca/library/research/readab/readab.pdf

[29] A. Ghose, P.G. Ipeirotis, Estimating the helpfulness and economic impact of product reviews: mining text and reviewer characteristics, IEEE Trans. Knowl. Data Eng. 23 (2011).1498–1512

[30] G.R. Klare, The Measurement of Readability, (1963) Ames.

[31] G.H. McLaughlin, SMOG grading – a new readability formula, J. Read. 22 (1969) 639 646.

[32] Z. Liu, S. Park, What makes a useful online review? Implication for travel produc websites. Tour. Manage, 47 (2015) 140–151.

[33] N. Kor<sup>fi</sup>atis, E. García-Bariocanal, S. Sánchez-Alonso, Evaluating content quality and helpfulness of online product reviews: the interplay of review helpfulness vs. review content, Electron. Comm. Res. Appl. 11 (2012) 205 217.

[34] A. Agnihotri, S. Bhattacharya, Online review helpfulness: role of qualitative factors, Psychol, Market, 33 (2016) 1006–1017.

[35] W. Chafe, Evidentiality in English conversation and academic writing, in: W.L. Chafe, J. Nichols (Eds.), Evidentiality: the Linguistic Coding of Epistemology, Ablex Publishing Corporation, 1986, pp. 261–272.

[36] Q. Su, C.R. Huang, H.K.Y. Chen, Evidentiality for text trustworthiness detection, Proceedings of the 2010 Workshop on NLP and Linguistics: Finding the Common Ground, Uppsala, Sweden, Association for Computational Linguistics, 2010, pp. 10–17.

[37] R. Jakobson, Shifters and verbal categories, On Language, Harvard University Press, Cambridge, MA, 1990, pp. 386–392.

[38] F.R. Palmer, Mood and Modality, Cambridge University Press, 2001.

[39] S. DeLancey, The mirative and evidentiality, J. Pragmat. 33 (2001) 369–382.

[40] F. Wang, S. Karimi, Linguistic Style and Online Review Helpfulness, (2017).

[41] J.W. Pennebaker, R.J. Booth, M.E. Francis, Linguistic inquiry and word count: LIWC [Computer software], Austin, TX: liwc.net, (2007).

[42] Y. Liang, B.N. DeAngelis, D.D. Clare, S.M. Dorros, T.R. Levine, Message characteristics in online product reviews and consumer ratings of helpfulness, Southern Commun. J. 79 (2014) 468–483.

[43] C.-H. Peng, D. Yin, C.-P. Wei, H. Zhang, How and when review length and emotional intensity influence review helpfulness: Empirical evidence from Epinions. com, (2014).

[44] H.C. Chiu, Y.C. Hsieh, C.Y. Kao, Website quality and customer's behavioural intention: an exploratory study of the role of information asymmetry, Total Qual. Manage, Bus, Excell, 16 (2005) 185–197.

[45] C. Lovelock, Services marketing: people, technology, strategy in: t. edition. (Ed.), New Jersey: Prentice Hall, 2001.

[46] D. Biber, B. Gray, Challenging stereotypes about academic writing: complexity elaboration, explicitness, J. Engl. Acad. Purposes 9 (2010) 2–20.

[47] M. Moohebat, R.G. Raj, S.B.A. Kareem, D. Thorleuchter, Identifying ISI-indexed articles by their lexical usage: a text analysis approach, J. Assoc. Inf. Sci. Technol. 66 (2015) 501–511.

[48] J. Jin, Y. Liu, How to interpret the helpfulness of online product reviews: bridging the needs between customers and designers, Proceedings of the 2nd International Workshop on Search and Mining User-Generated Contents, New York: ACM Press, 2010, pp. 87 94.

[49] N. Hu, L. Liu, J.J. Zhang, Do online reviews a<sup>f</sup>ect product sales? The role of reviewe characteristics and temporal e<sup>f</sup>ects, Inf. Technol. Manage. 9 (2008) 201–214.

[50] T.L. Ngo-Ye, A.P. Sinha, The in<sup>fl</sup>uence of reviewer engagement characteristics on online review helpfulness: a text regression model, Decis. Supp. Syst. 61 (2014) 47–58.

[51] A. Levi, O. Mokryn, The social aspect of voting for useful reviews, Behavioral-Cultural Modeling, and Prediction, International Conference on Social Computing (2014) 293–300.

[52] R.B. Harris, D. Paradice, An investigation of the computer-mediated communication of emotions, J. Appl. Sci. Res. 3 (2007) 2081 2090.

[53] V. Griskevicius, N.J. Goldstein, C.R. Mortensen, J.M. Sundie, R.B. Cialdini, D.T. Kenrick. Fear and loving in las vegas: evolution, emotion, and persuasion, J Market .Res. 46 (2009) 384 395.

[54] M. Thelwall, K. Buckley, G. Paltoglou, D. Cai, A. Kappas, Sentiment strength detection in short informal text, J. Am. Soc. Inf. Sci. Technol. 61 (2010) 2544 2558.

[55] D. Garcia, F. Schweitzer, Emotions in product reviews-empirics and models in: privacy, security, risk and trust (PASSAT). 2011 JEEE Third Inernational Conference on Social Computing (SocialCom) (2011) 483 488.

[56] R. Flesch, A new readability yardstick, J. Appl. Psychol. 32 (1948) 221 233.

[57] V.N. Vapnik, Statistical learning theory, in: W. New York (Ed.), (1998).

[58] S.T. Li, C.C. Chen, A regularized monotonic fuzzy support vector machine model for data mining with prior knowledge, JEEE Trans. Fuzzy Syst. 23 (2015) 1713–1727

[59] C.J. Lin, C.C. Chang, LIBSVM – A library for support vector machines, https://www. csie.ntu.edu.tw/∼cjlin/libsvm/. (2014).

[60] L.A. Fast, D.C. Funder, Personality as manifest in word use: correlations with self-report, acquaintance report, and behavior, J. Pers. Soc. Psychol. 94 (2008) 334–346.

[61] M. Xia, C. Zhai, B. Tan, Y. Lu, Q. Mei, You are what you write-Understanding user online behavior through text mining, Social Mediating Technologies Workshop, CHI, Boston, 2009.

[62] D. Jurafsky, J.H. Martin, Speech and Language Processing: An Introduction to Natural Language Processing, Speech Recognition, and Computational Linguistics, 2nd edition, (2009).

[63] L.T. Bei, E.Y.I. Chen, R. Widdows, Consumers' online information search behavior and the phenomenon of search vs. experience products, J. Fam. Econ. Issues 25 (2004) 449–467.

[64] C.J. Beukeboom, M. Tanis, I.E. Vermeulen, The language of extraversion: extraverted people talk more abstractly, introverts are more concrete, J. Lang. Soc. Psychol. (2012).

[65] P. Nelson, Information and consumer behavior, J. Polit. Econ. 78 (1970) 311.

[66] V.A. Zeithaml, Consumer perceptions of price, quality, and value: a means-end model and synthesis of evidence, J. Market. 52 (1988) 2 22.

![](/api/attachments/9SPC426X/fulltext/images/b6982d009867e70bf76b3561d4abbcdf5a2edb26ff44ab92b9e257be7f968ba6.jpg)

Sheng-Tun Li received his PhD degree in computer science from University of Houston, University Park, Texas, USA, in 1995. He is currently a distinguished professor in the Department of Industrial and Information Management & Institute of Information Management at National Cheng Kung University. Taiwan Dr. Li is author/co-author of nine IT-re lated textbooks including two translated, over 70 journal papers, and numerous conference papers. His work has been appeared in IEEE Transactions on Fuzzy Systems, IEEE Transactions on Systems, Man, and Cybernetics-Part B, Fuzzy Sets and Systems, Information Sciences, Omega The International Journal of Management Science, Knowledge-Based Systems Journal of Information Science. Technovation etc. He is a holder of one IT-related patent. His research interests include arti<sup>fi</sup>cial intelligence, business intelligence, data mining, text mining, and fuzzy time series.

![](/api/attachments/9SPC426X/fulltext/images/7a1082af9887bf5c5d37e161566d03580b572f1a791cee1c1f91d84fe9354c99.jpg)

Thuong-Thi Pham received her MS degree in Institute of Information Management from Shu-Te University, Taiwan, in 2010. She is currently a doctoral candidate in the Department of Industrial and Information Management & Institute of Information Management at National Cheng Kung University, Taiwan. She has recently been conducting research in developing user-oriented co-creation recommendation systems, reputation models, and business intelligence based on text mining, fuzzy time series, and linguistic styles.

![](/api/attachments/9SPC426X/fulltext/images/2f6c399ea5ff8135b8988f8929eef1188ae3e884c73beb265a1b7187cef6b496.jpg)

Hui-Chi Chuang received her BS degree in Department of Information Management from National United University, Taiwan, in 2011 and MS degree in Institute of Information Management from National Cheng Kung University, Taiwan, in 2013. Currently, she is a doctoral candidate with the Institute of Information Management at National Cheng Kung University. Her research interests include text mining, fuzzy time series, and business intelligence.
