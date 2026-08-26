---
otero_id: 6568
otero_key: "RY9KTUDV"
title: "A domain-feature enhanced classification model for the detection of Chinese phishing e-Business websites"
authors: "Dongsong Zhang; Zhijun Yan; Hansi Jiang; Taeha Kim"
year: "2014"
journal: "Information & Management"
doi: "10.1016/j.im.2014.08.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A domain-feature enhanced classification model for the detection of Chinese phishing e-Business websites

![](/api/attachments/RY9KTUDV/fulltext/images/d105ee9bbb75bb9d3c46a1b0599446e9cd3ed30525873327268d4adc16233979.jpg)

Dongsong Zhang <sup>a,b</sup>, Zhijun Yan <sup>b,</sup>\*, Hansi Jiang <sup>b</sup>, Taeha Kim <sup>c,</sup>\*\*

<sup>a</sup> Department of Information Systems, University of Maryland, Baltimore County, 1000 Hilltop Circle, Baltimore, MD 21250, USA <sup>b</sup> School of Management & Economics, Beijing Institute of Technology, 5 South Zhongguancun Street, Haidian District, Beijing 100081, China <sup>c</sup> Department of Management Information Systems, College of Business & Economics, Chung-Ang University, 84 HeukSeok-Ro, Dongjak-Gu, Seoul, Korea 156-756

## A R T I C L E I N F O

Article history: Received 1 November 2013 Received in revised form 24 May 2014 Accepted 2 August 2014 Available online 12 August 2014

Keywords: Phishing websites E-business Classification Detection Feature vectors

## A B S T R A C T

We propose a novel classification model that consists of features of website URLs and content for automatically detecting Chinese phishing e-Business websites. The model incorporates several unique domain-specific features of Chinese e-Business websites. We evaluated the proposed model using four different classification algorithms and approximately 3,000 Chinese e-Business websites. The results show that the Sequential Minimal Optimization (SMO) algorithm performs the best. The proposed model outperforms two baseline models in detection precision, recall, and F-measure. The results of a sensitivity analysis demonstrate that domain-specific features have the most significant impact on the detection of Chinese phishing e-Business websites.

\- 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

The past decade has seen a remarkable growth of e-Business worldwide. The convenience of e-Business, however, exposes consumers to a variety of security and privacy concerns. Among them, phishing, a form of online identity theft associated with both social engineering and technical subterfuge, is a major threat. Phishing is best understood as distinct methods identity thieves use to illegally obtain online users’ personal information by enticing unwitting users to give out their identity or financial information either unknowingly or under false impressions or by deceiving users to allow unauthorized access to their computers and personal data.

There has been an increasing number of phishing e-Business websites that aim to acquire consumers’ personal and sensitive information illegally for financial gains or to mislead consumers into conducting business transactions that will never be fulfilled by masquerading a phishing website as a trustworthy e-Business website [19]. Phishing e-Business websites pose a considerable threat not only to e-Business but also to Internet security and consumer privacy. According to APWG’s (Anti-Phishing Working Group) Phishing Activity Trends Report for the first quarter of 2012 [6], there were 56,859 unique phishing websites detected in February alone. Phishing e-Business websites seriously affect the development of online financial services and e-Commerce, endanger public interests, and negatively affect public interests in e-Commerce. Therefore, developing effective approaches to detecting phishing e-Business websites is critical to mitigating this threat and its associated financial losses [12].

There are two common types of phishing attacks in e-Business. One is to create fake e-Business websites that look very similar to real, authentic e-Business websites in terms of domain names and Web content. Once the deceived consumers mistakenly log into a phishing website, their user name and password can be stolen and used by criminals to log into the authentic website for illegal financial gain. These phishing websites (e.g., the left website in Fig. 1) are called spoof sites.

Another type of phishing website is referred to as a concocted site, which is a phishing website without an authentic counterpart. For example, criminals may post fake product sales information on fake websites, then disappear after receiving the consumer’s payment. Although public awareness of phishing websites has been steadily increasing over the years, the number of phishing websites and the resultant damage have grown at an even faster pace. According to the Anti-Phishing Alliance of China, 24,535 new Chinese phishing websites emerged in 2012, and 60 million Chinese online users became victims of phishing websites and suffered a loss of US\$4.64 billion between July 2011 and June 2012. More than 60% of Chinese phishing websites have been e-Business websites.

![](/api/attachments/RY9KTUDV/fulltext/images/6a4610e75fa9b5d9efb56a98bd546c132719fc173a6f57cfa65cd01e7ebe6863.jpg)  
Fig. 1. Fake (left) versus authentic (right) Chinese e-Business websites.

Detecting phishing e-Business websites successfully is a major goal of anti-phishing, but it is a challenging task due to the authentic appearance of phishing websites. Phishing websites are often professional-looking and sophisticated in terms of design and appearance, making their detection difficult [2,25,37]. In Jagatic et al.’s [23] and Wu et al.’s [39] studies, 60% and 72% of participants provided personal information to fake websites, respectively, due to their inability to identify them as phishing websites.

There have been a variety of approaches to phishing website detection. Some approaches are based on the recognition of the content and URL of a website (e.g., [18,21,34]); some segment a website into images and then analyze those images (e.g., [10,14,42]); and others use third-party search engines (e.g., [22]). However, these existing approaches have various limitations, such as reliance on prior knowledge about authentic websites and the lack of taking unique features of a particular domain into consideration. The vast majority of current approaches are generic approaches to phishing website detection instead of domain-specific approaches.

Compared with general phishing websites, there are unique features of Chinese e-Business websites that make existing approaches to general phishing website detection either not applicable or ineffective. For example, some current detection methods examine certain features of a website, such as whether its URL contains keywords such as ‘eBay’ and ‘PayPal’, which are rarely included in the URL of Chinese e-Business websites. Second, China’s Ministry of Information Industry requires every legitimate e-Business to register the domain name of its website, and the registry of those domain names is accessible by the public. Third, there is special content on Chinese e-Business websites that may not exist in other e-Business websites, let alone general phishing websites. For example, there are several e-Business certificates available in China. Although it is not required, many Chinese e-Businesses post their certificate information on their websites, aiming to gain more trust from online consumers. The examples of domain-specific features described above could be potentially helpful in the detection of phishing Chinese e-Business websites, but they have never been examined. Therefore, existing approaches to generic phishing website detection may not be effective for the detection of Chinese phishing e-Business websites.

To cope with the increasing problem of Chinese phishing e-Business websites and address the limitations of existing detection approaches, we propose a new classification model for detecting those websites. The overarching research question of this study is: Can the incorporation of domain-specific features into a phishing e-Business website detection model improve the detection performance in comparison with a generic detection model? There are three contributions of this study. First, previous studies on phishing website detection mainly focused on building generic models. As a result, the models developed only included general features of websites. In reality, however, phishing websites in different domains may exhibit different unique characteristics, making generic detection models potentially less effective. There has been little research on phishing website detection for a specific domain. In the proposed model, we incorporate domain-specific features that reflect unique characteristics of Chinese e-Business websites in addition to some generic website features adopted from previous research. Our model neither requires user expertise and prior knowledge about authentic websites nor consults centralized whitelists or blacklists to determine whether a target website is a phishing website. It can be used to detect both types of phishing attacks introduced earlier. Second, although China has witnessed the fastest growth of phishing e-Business websites and has suffered formidable financial losses attributable to those websites, there has been little research on how to build effective models for detecting those websites. In this study, we have built and empirically evaluated the proposed model with approximately three thousand authentic and phishing Chinese e-Business websites using four different machine learning algorithms. Third, we conducted a sensitivity analysis on the influence of individual predictive features in the model on detection performance to identify the most influential features in order to make the model more parsimonious, which has rarely been done in previous studies. Such an evaluation approach offers new insights for further improving a detection model.

The rest of the paper will be organized as follows. Section 2 introduces related work on the automated detection of phishing websites and the limitations of existing approaches. Then, in Section 3, we propose a new classification model for the detection of Chinese phishing e-Business websites that integrates features of both the URL and the content of the websites, including unique domain-specific features and general website features. Section 4 describes the evaluation of the proposed model, followed by major findings. Finally, the implications of this study will be discussed and conclusions offered in Section 5.

## 2. Related work

Automated phishing detection systems have emerged as an essential mechanism for combating phishing websites. Because most phishing attacks steal sensitive user information by masquerading as trustworthy websites, the most widely used detection techniques are based on website analysis. There are a variety of cues that have been examined in prior research for building tools for phishing website detection. These cues include features extracted from the textual content of websites (e.g., concocted word phrases, lexical measures such as average sentence length, spelling), URLs (e.g., HTTPS, number of slashes), image metadata (e.g., name, extension, and format of images) and image pixels (e.g., pixel colors), and hyperlinks (e.g., concocted links, number of in/out links) [2]. We categorize existing approaches to phishing website detection into four groups: blacklist based, visual similarity based, website URL and content feature based, and thirdparty search engine based, which will be introduced in the rest of this section.

## 2.1. The blacklist based approach

The blacklist based approach (e.g., [33,36]) relies on a list of URLs of known phishing websites. If the URL of a target website matches the URL of one of those known phishing websites in a blacklist, it will be labeled as a phishing website. PhishNet [33], for example, uses an approximate matching algorithm to dissect a URL into multiple components that are matched individually against those of known phishing website URLs in a blacklist. Although the blacklist based approach is the simplest method, it lacks the capability to detect new phishing websites. In addition, blacklists vary in the coverage of phishing websites and require constant updates [36].

## 2.2. The visual similarity based approach

The visual similarity based approach (e.g., [14]) treats phishing website detection as an image-matching problem. It normally divides the content of a website into a number of images. Then, it analyzes and compares the similarity between the visual characteristics of those image blocks and those of actual authentic websites registered with an anti-phishing system. This method is motivated by the perception that a website consists of multiple blocks. The characteristics and distribution of such blocks in a website determine the visual characteristics of the website [10]. For example, Liu et al.’s [28] method assesses visual similarities between a target website and actual websites in terms of blocks, layout, and overall style of websites. The block-level similarity is calculated as a weighted average of visual similarities of all matched block pairs between two websites. The overall style similarity is defined as the correlation coefficient of websites’ histograms of style features (e.g., content, color, block boundary, font).

Chen et al. [13] propose an image-based anti-phishing scheme based on discriminative key point features within websites. A point in an image is considered a key point if it can still be detected after the image undergoes various changes, such as shifting, lighting variation, color transformation, or format conversion. Chen et al.’s invariant content descriptor, called Contrast Context Histogram (CCH), computes the visual similarity degree between target and authentic websites.

The obvious constraint of a visual similarity based approach lies in its reliance on comparing a target website against an authentic, real website, which may not always exist or be known in advance. More importantly, many phishing websites are intended to look similar to real websites, causing visual similarity based approaches to have difficulty differentiating phishing websites from their authentic counterparts.

## 2.3. The URL and content feature based approach

The URL and content feature based approach (e.g., [15,18,21,27]) focuses on analyzing the characteristics of the URL and the content of a target website. URL features that have been examined include IP addresses contained in a URL [7,18,41]; length [21]; the number of ‘‘.’’ and ‘‘-’’ included in a URL [21,41]; the appearance of certain keywords [21,29]; Unicode [18]; URL port numbers [18]; and the inclusion of ‘‘@’’ [4,18,41]. Huang et al. [21] build an SVM (Support Vector Machine) classification model that uses a feature vector consisting of three types of features. Specifically, structure features include the inclusion of an IP address, the length of a hostname, the number of dots in a URL, and the number of dashes in a hostname. Lexical features include whether a URL contains keywords such as HTTP, confirm, banking, secure, ebayisapi, and webscr. Brand name features include the appearance of certain brand keywords in URLs, such as eBay, PayPal, sulake, facebook, orkut, mastercard, visa, warcraft, and bradesco. Ramanathan and Wechsler [34] use LDA (Latent Dirichlet Allocation) and AdaBoost to build a classifier for phishing website detection using normal and fake topics identified from the content of authentic and phishing websites, respectively.

A major challenge posed to the URL and content feature based approach is the difficulty in determining influential URL features and content features that can be used as effective cues for detection. Although it is the most adopted approach, most developed detection models are generic and do not take domain-specific features and knowledge into consideration. Some detection cues identified and used in prior research are either not applicable or are uncommon for Chinese phishing e-Business websites.

## 2.4. The third-party search engine based approach

Another type of approach relies on third-party search engines to search for relevant information about a URL and then uses search results to make a detection decision. In this approach, the full URL of a target website will be used as a search query. The number of websites returned by a search engine and the rankings of those websites will be used for classification [22]. The assumption of this approach is that using the URL of a legitimate website as a search query should return a large number of websites, and that particular website should be ranked at the top. In contrast, using the URL of a phishing website should return no or very few results, and/or that particular website should not be ranked high. For example, CANTINA [41] makes use of the well-known TF-IDF (term frequency/inverse document frequency) scheme widely used in information retrieval and the Robust Hyperlinks algorithm for overcoming broken hyperlinks. It works as follows: given a website, it calculates a TF-IDF score for each term in that website. Then, it generates a lexical signature by taking five terms with the highest TF-IDF weights and then feeds this lexical signature into a search engine. If the domain name of a target website matches the domain name of any of the top N search results, the target website will be considered a legitimate website. Otherwise, it will be considered a phishing website. A major challenge faced by the third-party search engine based approach is that designers of phishing websites may use search engine optimization to make a phishing website rank high in search results.

Some hybrid methods have attempted to combine the visual similarity based approach and the URL and content feature based approach to improve the accuracy of phishing website detection [24]. For example, Zhang et al. [42] use the Hungarian algorithm to detect phishing websites. Their model includes text, image, and overall website features. The results show that the features of an overall website have the most significant effect on detection performance, followed by the features of images, with the features of text being the least important.

As introduced above, existing approaches to the automated detection of phishing websites have various weaknesses. Among them, the URL and content feature based approach is the most commonly used. Because the majority of Chinese e-Business companies are small companies that come and go, it makes it ineffective and practically impossible to create a blacklist or use a third-party search engine based approach for future detection. Most existing approaches focus on general phishing websites instead of phishing websites in a specific domain such as e-Business. Although China has witnessed rapid growth of phishing e-Business websites and has suffered from huge financial losses because of them in recent years, there has been little research on the automated detection of Chinese phishing e-Business websites. In addition, China differs from other countries in its regulation of e-Business websites. Previous studies, however, have not taken such domain features into consideration.

## 3. A classification model for Chinese phishing e-Business website detection

We argue that to detect phishing websites in a particular domain effectively, a detection model should incorporate domainspecific features. In this research, we aim to develop a new classification model that can detect Chinese phishing e-Business websites by incorporating unique domain features. The proposed model does not rely on any prior knowledge or assumptions on authentic websites. Given the constraints of individual detection methods discussed in the preceding section and the focus of this study, we decide to adopt the URL and content feature based approach in this study because it is not only the most commonly used approach but also allows easy incorporation and evaluation of new domain features.

## 3.1. The feature vector of the classification mode

By integrating new domain features of Chinese e-Business with some predictive website features that have been used in prior studies and that are applicable to Chinese phishing e-Business websites (e.g., [4,18,43]), we created a feature vector for the proposed model that consists of two parts: URL features and Web content features.

URL features include the following cues extracted from the URL of a target website:

F1: whether a URL contains an IP address. For example, a phishing website may use http://110.75.2.128 to replace the URL of the official homepage of Taobao.com, the largest C2C website in China. If the URL of a target website contains an IP address instead of a domain name, then this feature variable F1 will be assigned a value of 1; otherwise, it will be assigned a value of 0.

F2: whether a URL contains the symbol ‘@’. Phishing websites often insert @ into a URL that takes users to a website different from what they expect [4,18,41]. For example, the real website to which http://www.taobao.com@www.phishweb.com points is http://www.phishweb.com, not http://www.taobao.com. In our model, if a URL contains the symbol ‘@’, F2 will be assigned a value of 1; otherwise, it will be 0.

F3: whether the characters in a URL are coded in UNICODE. In comparison to a truthful website, a phishing website is more likely to use UNICODE in its URL (e.g., http://www.taobao.- com@%77%77%77%2E%70%68%69%73%68) to hide the URL of a truly intended website [18]. In our model, F3 will be assigned a value of 1 if the domain name of the URL of a target website contains characters encoded in UNICODE; otherwise, its value will be 0.

F4: the number of dots (‘.’) in a URL. Previous research suggests that the larger the number of dots in a URL, the higher the possibility the website is a phishing website [43].

F5: the number of suffixes (e.g., ‘‘.com’’ and ‘‘.cn’’) in a domain name [18]. http://www.boc.cn.1boc.com.cn is the URL of a phishing website in which the number of domain name suffixes is 2. Users generally catch a glimpse of the first part of a URL but likely miss the remaining part, which actually points to a phishing website.

F6: age of a domain name, which is represented by the number of days passed since a domain name was registered.

F7: expiration time of a domain name [7], which is represented by the number of days remaining before a domain name expires.

F8: whether the address of a DNS (Domain Name System) server is consistent with a URL. DNS server addresses can be obtained through whois domain name queries. If they match, the value of F8 will be 1; otherwise, it will be 0.

F9: information about website registration. By searching for a domain name of a website at the Chinese MII (Ministry of Information Industry) website, a detection system can find out whether a domain name is registered, registered by an individual or by an enterprise, and whether the registered site name and actual site denoted by the URL are consistent. For example, for www.taobao.com, the information retrieved from MII includes the following: the name of the register is ‘‘Zhejiang Taobao Network Ltd.’’; the register type is ‘‘enterprise’’; the license No. is ‘‘B2-200080224-1 Zhejiang’’; and the site name is ‘‘Taobao’’. In the proposed model, we use F9 to represent whether a domain name is registered (1) or not (0) in MII; F10 is used to represent whether a domain name applicant is an individual (0) or an enterprise (1); and F11 is used to represent whether a recorded website name and actual indicated site are consistent (1) or not (0).

Web content features are automatically extracted from the source code of a website and include the following:

F12: An ICP (Internet Content Provider) license number is a business license number issued by the Chinese Ministry of Industry and Information Technology. By law, any profit-driven e-Business should apply for and receive its ICP license before starting its business. Therefore, an ICP license number is a unique identifier of an e-Business. A Chinese e-Business may provide its ICP license number on its website. For example, the ICP number of www.taobao.com listed on its website is B2-200080224-1 Zhejiang, which matches the archived information retrieved by a domain name query. In our proposed model, we use F12 to represent whether an ICP license number listed on a website is consistent with the one retrieved by a domain name query. If the answer is yes, then F12 will be assigned a value of 1; otherwise, it will be 0.

F13: the number of void (null) links on a website. According to previous studies (e.g., [18]), a phishing website tends to have more void links than an authentic website.

![](/api/attachments/RY9KTUDV/fulltext/images/3de4a3619bbdcc50aaba989d6804fbc4b12e843457d6e2c873e0c7ed45490baf.jpg)  
Fig. 2. Examples of e-Commerce certificate links on an e-Business website.

F14: the number of out links on a website. It is normal for a website to have some out links, but when there are too many, it may increase the probability of a website being a phishing website.

F15: whether an e-Business website provides e-Commerce certificate information. An authentic business may post images of its e-Commerce certificate(s) at the bottom of its website, although such certificates are not mandatory for a Chinese e-Business. Such images (see Fig. 2) are normally hyperlinks that point to the certificate information of businesses archived by certain authorities. There are different Chinese e-Commerce certificates available, such as the Chinese e-Commerce website demonstration enterprise certificate issued by the Digital Service Center of the Chinese E-Commerce Association, the trusted site certificate issued by the Chinese Internet Network Information Center, and the online transaction security certificate issued by the Policy and Law Committee of the Chinese E-Commerce Association. In this study, we take into consideration all the existing major e-Commerce certificates. If a website does not provide any certificate link, the value of F15 will be set to 0; otherwise, it will be 1.

Among the fifteen variables included in the original model, F9, F10, F11, F12, and F15 are domain features of Chinese e-Business. They have never been included or examined in any prior phishing website detection models. Although other features included in our original detection model are generic features of websites and have been used in previous approaches to general phishing website detection, their impacts on and effectiveness in the detection of phishing websites in a specific domain (e.g., Chinese e-Business) have never been examined. Therefore, this research makes novel contributions to phishing website detection not only by incorporating new domain-specific features of websites in a detection model but also by examining the effectiveness of some popular generic features of websites for detecting domain-specific phishing websites.

## 3.2. Classification performance

We use precision (P), recall (R), and F1-measure (F) to evaluate the performance of detection models. For such a binary classifier (i.e., phishing or authentic), there are four possible classification results, as shown in Table 1:

Precision, also referred to as positive predictive value, is the percentage of correct detections that can be represented as $T P / ( T P + F P )$ . Recall measures the proportion of actual positives in the population being tested, which is represented as TP=ðTP þ FNÞ. The F1-measure is the harmonic mean of precision and recall, which is calculated as 2ð precision - recallÞ=ð precision þ recallÞ. The values of the precision, recall, and F1-measures all range from 0 to 1. Because of the incorporation of domain-specific features in the proposed model, we propose the following hypotheses:

H1. The proposed domain-feature enhanced model for the detection of Chinese phishing e-Business websites will outperform traditional URL and content feature based models with generic website features only in terms of precision.

H2. The proposed domain-feature enhanced model for the detection of Chinese phishing e-Business websites will outperform traditional URL and content feature based models with generic website features only in terms of recall.

Table 1 Classification scenarios.

<table><tr><td rowspan="2"></td><td colspan="2">True results</td></tr><tr><td>1</td><td>0</td></tr><tr><td colspan="3">Prediction</td></tr><tr><td>1</td><td>True positive (TP)</td><td>False positive (FP)</td></tr><tr><td>0</td><td>False negative (FN)</td><td>True negative (TN)</td></tr></table>

H3. The proposed domain-feature enhanced model for the detection of Chinese phishing e-Business websites will outperform traditional URL and content feature based models with generic website features only in terms of the F1-measure.

## 3.3. Classification algorithms

In this study, we initially use four different machine learning algorithms to train four classifiers for detecting Chinese phishing e-Business websites, aiming to choose the best classification model among them. These algorithms include Sequential Minimal Optimization, Logistic Regression, Naive Bayes classifier, and the Random Forests method. These algorithms have been used in previous studies on building classifiers for phishing website detection (e.g., [3,7,18,21]).

Sequential Minimal Optimization (SMO) is an algorithm for solving an optimization problem that arises during the training of Support Vector Machines (SVM) [11,31,32,40]. For a binary classification problem with a dataset $( x _ { 1 } , y _ { 1 } ) , \ldots , ( x _ { n } , y _ { n } ) ,$ , where x is an input vector and y is a binary class label, a soft-margin Support Vector Machine can be trained by solving a quadratic programming problem expressed as follows:

$$
\begin{array}{l} \max _ {\alpha} \sum_ {i = 1} ^ {n} \alpha_ {i} - \frac {1}{2} \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {i = 1} y _ {i} y _ {j} K (x _ {i}, x _ {j}) \alpha_ {i} \alpha_ {j} \\ \text { subject   to: } \quad 0 \leq \alpha_ {i} \leq C, \quad \text { for } i = 1, 2, \dots , n, \sum_ {i = 1} ^ {n} y _ {i} \alpha_ {i} = 0 \end{array}\tag{1}
$$

where C is an SVM hyperparameter and $K ( x _ { i } , x _ { j } )$ is a kernel function, both provided by the user; variables $\alpha _ { i }$ and $\alpha _ { j }$ are Lagrange multipliers. SMO breaks this optimization problem into a series of smallest possible sub-problems and then solves them analytically. Some researchers (e.g., [1,26]) have used this algorithm for detecting phishing websites.

Logistic Regression (LR) measures the relationship between a categorical dependent variable and one or multiple continuous independent variables by converting the dependent variable into probability scores [8]. An explanation of Logistic Regression begins with an explanation of the logistic function that can take any value as an input, whereas the output is confined to values between 0 and 1 [20]:

$$
\pi (x) = \frac {e ^ {(\beta_ {0} + \beta_ {1} x)}}{e ^ {(\beta_ {0} + \beta_ {1} x)} + 1} = \frac {1}{e ^ {- (\beta_ {0} + \beta_ {1} x)} + 1},\tag{2}
$$

$$
g (x) = \ln {\frac {\pi (x)}{1 - \pi (x)}} = \beta_ {0} + \beta_ {1} x,\tag{3}
$$

$$
\frac {\pi (x)}{1 - \pi (x)} = e ^ {(\beta_ {0} + \beta_ {1} x)}\tag{4}
$$

In the equations above, g(x) refers to the logit function of a given event x; pðxÞ is the probability of the event x; $\beta _ { 0 }$ is the intercept of the linear regression equation; and $\beta _ { 1 }$ is the regression coefficient.

![](/api/attachments/RY9KTUDV/fulltext/images/e49772ddc804f2cf780b5de6cada997bb6a85c3f5b771fe6d858ad066e22e01b.jpg)  
Fig. 3. Performance comparison of four classification algorithms.

Logistic Regression has been frequently used for detecting phishing websites (e.g., [17,29]).

A Naive Bayes classifier (NB) is a probabilistic model that applies Bayes’ theorem with a strong (naive) independence assumption [30]. A probability model for classification is a conditional model over a dependent class variable C with a small number of outcomes or classes, which is conditional on several feature variables, namely $F _ { 1 }$ through $F _ { n } \ [ 3 5 ]$ . A Naive Bayes classifier can be represented as follows:

$$
p (C | F _ {1}, \dots , F _ {n}) = \frac {p (C) p (F _ {1} , \dots , F _ {n} | C)}{p (F _ {1} , \dots , F _ {n})}\tag{5}
$$

The $" \mathrm { n a i v e } "$ conditional independence assumes that each feature $F _ { i }$ is conditionally independent of every other feature $F _ { j }$ $( j \neq i )$ given a class C. Almeida et al. [5] and Zhang et al. [43] have used this algorithm for detecting phishing websites.

Random Forests (RF) are ensemble classifiers that operate by constructing a number of decision trees at training time and output a class that is the mode of the classes generated by individual trees [9]. Random Forests are a type of recursive partitioning method. An ensemble of classification trees will be constructed based on random subsets of data using a subset of randomly restricted and selected predictors for each split in each classification tree. Some previous studies, such as Fette et al. [16] and Whittaker et al. [38], have used this algorithm for detecting phishing websites.

## 4. Evaluation

## 4.1. Data collection

To empirically evaluate the performance of the proposed model for the detection of Chinese phishing e-Business websites, we collected 1416 Chinese phishing e-Business websites from http:// www.315online.com.cn and http://www.anquan.org, which are third-party service platforms sponsored by the Policy and Law Committee of the Chinese E-Business Association. Both organizations collect and validate Chinese phishing e-Business websites reported by consumers. We also collected 1462 authentic Chinese e-Business websites. We used a tool called WebZIP to download the source codes of the collected websites and then developed a program to extract the proposed predictive features from the source codes automatically.

We divided the collected websites into a training data set and a testing data set. The former consisted of 1023 authentic websites and 991 phishing websites, and the latter consisted of 439 authentic websites and 425 phishing websites. We used Weka (Waikato Environment for Knowledge Analysis, http://www.cs.waikato.ac.nz ml/weka), a data mining tool that provides a collection of machine learning algorithms, to train four models by using the four different classification algorithms introduced in the previous section.

## 4.2. Choosing the best classification model

Fig. 3 shows a comparison of the detection performance of the models trained by the SMO, Logistic Regression, Naive Bayes, and Random Forest algorithms. Of the four classifiers, the model trained with SMO performed the best in all three metrics at detecting both authentic and phishing e-Business websites. Therefore, we chose that model and compared its performance against two baselines.

## 4.3. Comparison of detection performance

To minimize the potential effect of machine learning algorithms on detection performance, we compared the performance of our model, called the CBML model (Chinese e-Business phishing website detection based on Machine Learning) against that of two baseline models with generic website URL and content features only. One was Abbasi et al.’s [2] phishing website detection model, and the other was He et al.’s [18] model. Both reported very high accuracies of phishing website detection. There are a few reasons why we selected these two models as baselines. First, we could not find any prior studies on models that were designed particularly for e-Business phishing website detection, let alone for Chinese phishing e-Business website detection. Second, our proposed model is a URL and Web content feature based approach, so it makes sense to use detection models that have also adopted this approach as benchmarks. Third, we want to select models that are reported to perform very well in phishing website detection. Fourth, baseline models should be recently published. The two selected baseline models satisfy all these criteria. Abbasi et al.’s [2] model consists of many cues grouped into five categories for phishing website detection, including URLs (e.g., # of ‘‘/’’, ‘‘-’’), web page text (e.g., grammar, lexical measures), source code, images (e.g., file size, file format), and linkage (e.g., number of total and absolute in-links and out-links). He et al.’s [18] model consists of thirteen predictive features extracted from both the URL and the content of a target website, such as whether a URL contains an IP address; whether the number of ‘‘.’’ in a URL is more than four; whether other URL ports are used instead of port 80; whether keywords such as ‘‘password’’ and ‘‘credit card’’ are included in the form of a website; and whether the links in a website are abnormal. Neither baseline model includes any domain-specific features included in the proposed model. Because our goal is to examine whether the incorporation of domain-specific features improves the detection performance of traditional URL and web content based approaches, using those two baseline methods is appropriate.

Table 2  
Comparison of detection performance of CBML versus the baseline models.

<table><tr><td>Measures</td><td>Mean of CBML (M1)</td><td>SD of CBML</td><td>Mean of He et al.&#x27;s model (M2)</td><td>SD of Huang et al&#x27;s model</td><td>Mean of Abbasi et al.&#x27;s model (M3)</td><td>SD of Abbasi et al.&#x27;s model</td><td>Mean diff. (M1-M2)</td><td>Mean diff. (M1-M3)</td></tr><tr><td>P (%)</td><td>94.27</td><td>2.09</td><td>81.7</td><td>6.2</td><td>92.31</td><td>2.25</td><td>12.6**</td><td>1.96*</td></tr><tr><td>R (%)</td><td>94.72</td><td>2</td><td>80.84</td><td>5.3</td><td>92.25</td><td>2.12</td><td>13.9**</td><td>2.47*</td></tr><tr><td>F (%)</td><td>94.47</td><td>.3</td><td>80.90</td><td>0.8</td><td>92.27</td><td>1.59</td><td>13.6**</td><td>2.2*</td></tr></table>

Note: ‘SD’ represents standard deviation.  
Statistically significant at the 0.05 level.  
本 Statistically significant at the 0.01 level.

To focus on the impact of selected features on detection performance while minimizing the confounding effects of different machine learning algorithms on performance, we trained both baseline models using the SMO algorithm and the same training data set. To test the statistical significance of potential differences in detection performance between the proposed model and the baseline models, we randomly divided all collected websites into 30 groups, with relatively balanced numbers of real and phishing websites in each group. Then, we trained the proposed model and the baseline models 30 times separately. Each time, we used a different group of websites as testing data and the remaining 29 groups as training data. In other words, we trained and tested the models with different training and testing data 30 times each.

After the entire training and testing process was completed, we conducted a pair-wise T-test to compare the precision, recall, and F1 measures of the proposed model (CBML) against those of the baseline models. The results shown in Table 2 demonstrate that our model significantly outperforms the two baseline models across all three performance metrics. These results indicate that our proposed feature set is significantly more effective at detecting Chinese phishing e-Business websites than the generic feature sets used in the baseline models. Therefore, all three hypotheses are supported.

## 4.4. Sensitivity analysis

One of the major objectives of this research is to examine the impact of domain-specific features on phishing website detection.

Table 3  
The performance of the pruned model with top seven features.

<table><tr><td></td><td>Precision</td><td>Recall</td><td>F-measure</td></tr><tr><td>Phishing websites</td><td>94.2%</td><td>94.3%</td><td>94.2%</td></tr><tr><td>Real websites</td><td>95.4%</td><td>96.5%</td><td>95.8%</td></tr></table>

Therefore, we also performed a sensitivity analysis on the proposed model to investigate the importance of each individual feature to detection performance. This analysis helps us identify and remove less important features from the original model to make it more parsimonious. Such a sensitivity analysis has rarely been performed in previous studies on phishing website detection.

We conducted the sensitivity analysis by applying RankSearch and ChiSquaredAttributeEval, an attribute evaluation algorithm available in Weka that evaluates the contribution of individual features by computing the value of the chi-squared statistic with respect to classification. The result shows that features F9 (information about website registration), F15 (e-Commerce certificate), F10 (the type of domain name applicant), F7 (expiration of the domain name), F6 (age of the domain name), F12 (the ICP license number), and F13 (the number of out links) in the proposed model are the top seven features (in a decreasing order of significance) that are most influential to the detection performance, with ranked values of 401.6, 356.5, 261.2, 206.4, 184.9, 98.4, and 40.0, respectively. Among them, F9, F15, F10 (i.e., the top 3) and F12 are domain-specific features.

To further validate the findings described above, we created and tested a new pruned classification model only consisting of the seven most influential features listed above and using the same training and testing website collections. The results demonstrate that although the pruned model only consists of half the features in the original model, it achieves very comparable precision, recall, and F-measure values, as shown in Table 3, indicating that the pruned model is still very effective. This reemphasizes the importance of incorporating domain-specific features for phishing website detection. The results also indicate that many of the popular general website features proposed in previous generic models are not necessarily effective at detecting phishing websites in a particular domain.

## 5. Discussion

With the rapid growth of e-Business, we have witnessed the equally rapid emergence of phishing e-Business websites, which have resulted in huge financial losses to consumers and businesses. Developing effective technological solutions to detect those websites in a timely manner has become critical. However, there has been little research on developing models specifically for detecting phishing e-Business websites, let alone Chinese phishing e-Business websites. Existing models developed for the detection of generic phishing websites may not be effective because they do not take specific domain characteristics into consideration.

In this research, we argue that it is important to incorporate domain features into a model for domain-specific phishing website detection. We propose a novel detection model for detecting Chinese phishing e-Business websites that takes into consideration several unique domain features of Chinese e-Business websites that have never been studied. We have built models with four different machine learning algorithms, selected the SMO-based model that achieved the best performance, analyzed the significance of individual features of the model to detection performance, and then pruned the model by removing less important features while achieving similar performance.

The empirical results of this study clearly demonstrate that domain-specific features can have a significant influence on the performance of a detection model. By incorporating such features, a domain-specific detection model can considerably outperform a generic detection model without domain features. Theoretically, such findings should be applicable to other domains as well. The result of the sensitivity analysis also shows that including many generic website features in a domain-specific model may not improve, or may even hurt, the detection performance.

This study provides several research and practical contributions. First, it proposes a new model and approach for phishing website detection with domain features that have never been studied. Second, a sensitivity analysis of the proposed model further demonstrates the importance of domain features to phishing website detection and enables us to simplify the model. It also shows that some previously proven features for generic phishing website detection are not effective at detecting domainspecific phishing e-Business websites. These results imply that when developing solutions for the detection of domain-specific phishing websites such as e-Business websites, we should take the context and characteristics of those websites into consideration. Instead of mainly focusing on developing models for generic phishing website detection, researchers and practitioners should put more effort into developing domain-specific models that can be more effective and useful. Third, although the proposed model is built for Chinese phishing e-Business website detection and may not be directly applicable to phishing websites in other domains that possess different domain features, the insights gained and the ideas behind the proposed approach should be helpful to researchers and practitioners.

This study has two limitations, which provide opportunities for future research. First, given the research objectives and complexity of processing websites, this study focuses on one specific domain only. It is necessary to validate the proposed approach in other domains as well in the future. Second, our latest model, like many previous studies, only uses ‘surface’ content features that do not involve any deep-level text analysis of website content. It might be interesting to explore whether a text analysis of website content at a certain semantic level provides additional useful cues for detecting phishing websites.

## Acknowledgements

This research is supported by National Natural Science Foundation of China (Award #s: 71128003, 70972006, 71272057). The views and conclusions contained in this document are those of the authors and should not be interpreted as representing official policies and opinions, either expressed or implied, of the funding agency.

## References

[1] J. Abawajy, A. Kelarev, A multi-tier ensemble construction of classifiers for phishing email detection and filtering, CSS’12 Proceedings of the 4th International Conference on Cyberspace Safety and Security, Berlin, Germany, 2012, pp. 48–56.

[2] A. Abbasi, Z. Zhang, D. Zimbra, H. Chen, Detecting fake Websites: the contribution of statistical learning theory, MIS Q. 34 (3), 2010, pp. 1–28.

[3] S. Abu-Nimeh, D. Nappa, X. Wang, S. Nair, A comparison of machine learning techniques for phishing detection, in: Proceedings of the Anti-phishing Working Groups 2nd Annual eCrime Researchers Summit, Pittsburgh, PA, USA, October 04 05, 2007, pp. 60–69.

[4] M. Aburrous, M.A. Hossain, F. Thabatah. K. Dahal. Intelligent phishing website detection system using fuzzy techniques, Information and Communication Technologies: From Theory to Applications. ICTTA, April 7–11, Damascus, Syria, 2008, pp. 1–6.

[5] T.A. Almeida, J. Almeida, A. Yamakami, Spam filtering: how the dimensionality reduction affects the accuracy of Naive Bayes classifiers, J. Internet Serv. Appl. 1 (3), 2011, pp. 183–200.

[6] Anti-Phishing Alliance of China, Annual Report, 2012 Available at: http:// en.apac.cn/news/201301/P020130122639769507177.pdf

[7] R. Basnet, S. Mukkamala, A.H. Sung, Detection of phishing attacks: a machine learning approach, Soft Comput. Appl. Ind. 226, 2008, pp. 373–383.

[8] M. Bhandari, A. Joensson, Clinical Research for Surgeons, Thieme Medical Publisher, 2009.

[9] L. Breiman, Random forests, Mach. Learn. 45 (1), 2001, pp. 5–32.

[10] J. Cao, M. Bo, J. Luo, L. Bo, A phishing web pages detection algorithm based on nested structure of earth mover’s distance (nested-EMD), Chin. J. Comput. 32 (5), 2009, pp. 922–929.

[11] C. Chang, C. Lin, LIBSVM: a library for support vector machines, ACM Trans. Intell. Syst. Technol. (TIST) 2 (3), 2011, Article 27.

[12] Y. Chen, The study on indicator system of website credibility evaluation, Netinfo Secur. 5, 2013, pp. 79–82.

[13] K. Chen, J. Chen, C. Huang, C. Chen, Fighting phishing with discriminative keypoint features, IEEE Internet Comput. 13 (3), 2009, pp. 56–63.

[14] T. Chen, S. Dick, J. Miller, Detecting visually similar Web pages: application to phishing detection, ACM Trans. Internet Technol. 10 (2), 2010, article #5.

[15] W. Chu, B. Zhu, F. Xue, X. Guan, Z. Cai, Protect sensitive sites from phishing attacks using features extractable from inaccessible phishing URLs, IEEE International Conference on Communications, June 9–13, 2013, pp. 1990–1994.

[16] I. Fette, N. Sadeh, A. Tomasic, Learning to detect phishing emails, in: Proceedings of the 16th International Conference on World Wide Web, Banff, Alberta, Canada, May 8–12, 2007, pp. 649–656.

[17] S. Garera, N. Provos, M. Chew, A. Rubin, A framework for detection and measurement of phishing attacks, in: Proceedings of the 2007 ACM Workshop on Recurring Malcode, Alexandria, VA, USA, November 2, 2007, pp. 1–8.

[18] G. He, F. Zou, D. Tan, M. Wang, Phishing detection system based on SVM active learning algorithm, Comput. Eng. 37 (19), 2011, pp. 126–128.

[19] A. Herzberg, A. Jbara, Security and identification indicators for browsers against spoofing and phishing attacks, ACM Transactions on Internet Technology 8 (4), 2008, pp. 1–36.

[20] W. Hosmer, L. Stanley, Applied Logistic Regression, John Wiley, 2000.

[21] H. Huang, L. Qian, Y. Wang, A SVM-based technique to detect phishing URLs, Inf. Technol. J. 11 (7), 2012, pp. 921–925.

[22] J. Huh, H. Kim, Phishing detection with popular search engines: simple and effective, 4th Canada-France MITACS Workshop on Foundations and Practice of Security, Paris, France, May 12–13, Springer Verlag, 2011 , pp. 194–207.

[23] T. Jagatic, N. Johnson, M. Jakobsson, F. Menczer, Social Phishing, Communications of the ACM 50 (10), 2007, pp. 94–100.

[24] J.S. White, J.N. Matthews, J.L. Stacy, A method for the automated detection of phishing websites through both site characteristics and image analysis, in: Proceedings of Cyber Sensing 2012, Baltimore, Maryland, USA, 2012.

[25] E. Levy, Criminals become tech savvy, IEEE Secur. Priv. 2 (2), 2004, pp. 65–68.

[26] G. L’Huillier, R. Weber, N. Figueroa, Online phishing classification using adversarial data mining and signaling games, in: Proceedings of the ACM SIGKDD Workshop on Cyber Security and Intelligence Informatics, Paris, France, 2009, pp. 33–42.

[27] M. Aburrous, M.A. Hossain, F. Thabatah, K. Dahal, Intelligent phishing website detection system using fuzzy techniques, in: Proceedings of 3rd International Conference on Information and Communication Technologies: from Theory to Applications, Damasus, April 7–11, 2008, pp. 1–6.

[28] W. Liu, X. Deng, G. Huang, A. Fu, An antiphishing strategy based on visual similarity assessment, IEEE Internet Comput. 10 (2), 2006, pp. 58–65.

[29] J. Ma, L.K. Saul, S. Savage, G.M. Voelker, Identifying suspicious URLs: an application of large-scale online learning, in: Proceedings of the 26th Annual International Conference on Machine Learning, Montreal, Canada, June 14–18, 2009, pp. 681–688.

[30] K.P. Murphy, Naive Bayes Classifiers, 2006 Available at: http://www.cs.ubc.ca/ murphyk/Teaching/CS340-Fall06/reading/NB.pdf.

[31] J. Platt, Sequential Minimal Optimization: A Fast Algorithm for Training Support Vector Machines, Technical Report, Microsoft Research 1998

[32] J. Platt, Fast Training of Support Vector Machines Using Sequential Minimal Optimization. MIT Press. 1999.

[33] P. Prakash, M. Kumar, R.R. Kompella, M. Gupta, Phishnet: predictive blacklisting to detect phishing attacks in: Proceedings of INFOCOM 2010 San Diego CA March 15-19 2010 pp. 1-5.

[34] V. Ramanathan, H. Wechsler. Phishing website detection using Latent Dirichlet Allocation and AdaBoost, 2012 IEEE International Conference on Intelligence and Security Informatics, Cyberspace, Border, and Immigration Securities (ISI 2012). Piscataway, NJ, USA, June 11–14, 2012, pp. 102–107.

[35] I. Rish, An empirical study of the naive Bayes classifier, in: Proceedings of IJCAI 2001 Workshop on Empirical Methods in Artificial Intelligence, Seattle, USA, August 4, 2001, pp. 41–46

[36] S. Sheng, B. Wardman, G. Warner, L. Cranor, I. Hong, C. Zhang, An empirical analysis of phishing blacklists, Sixth Conference on Email and Anti-Spam (CEAS), Mountain View, CA, July 16–17, 2009.

[37] B. Sullivan, Fake Escrow Site Scam Widens: Auction Winners Sometimes Lose \$40,000 at a Time, 2002 Available at: http://www.msnbc.msn.com/id/3078510/.

[38] C. Whittaker, B. Ryner, M. Nazif, Large-scale automatic classification of phishing pages, in: Proceedings of the 17th Annual Network and Distributed Security Symposium, San Diego, CA, USA, February 28–March 3, 2010.

[39] M. Wu, R.C. Miller, S.L. Garfunkel, Do security toolbars actually prevent phishing attacks? in: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Montre´ al, Canada, April 22–27, 2006, pp. 601–610.

[40] L. Zanni, T. Serafini, G. Zanghirati, Parallel software for training large scale support vector machines on multiprocessor systems, J. Mach. Learn. Res. 7, 2006, pp. 1467–1492.

[41] Y. Zhang, J. Hong, L. Cranor, CANTINA: a content-based approach to detecting phishing websites, in: Proceedings of the 16th International Conference on World Wide Web, Banff, Alberta, Canada, May 8–12, 2007, pp. 639–648.

[42] W. Zhang, Y. Zhou, L. Xu, B. Xu, A method of detecting phishing webpages based on Hungarian matching algorithm, Chin. J. Comput. 33 (10), 2010, pp. 1963–1975.

[43] H. Zhang, G. Liu, T. Chow, W. Liu, Textual and visual content-based antiphishing: a Bayesian approach, IEEE Trans. Neural Netw. 22 (10), 2011, pp. 1532–1546.

![](/api/attachments/RY9KTUDV/fulltext/images/a5b4c5c23f5d652bdb0556c05da78a00adab56156e845ed767f2f02a43fbfbbc.jpg)

Dr. Dongsong Zhang is a professor in the Department of Information Systems at University of Maryland, Baltimore County. He received a Ph.D. in Management Information Systems from the University of Arizona. His current research interests include context-aware mobile computing, computer-mediated collaboration and communication, social computing, and e-Business. He has published about 130 research articles in journals and conference proceedings, including premier journals such as MIS Quarterly, Journal of Management Information Systems (JMIS), IEEE Transactions on Knowledge and Data Engineering (TKDE), IEEE Transactions on Software Engineering, among others. He has received research grants and awards from National Science Foundation (NSF), National Institute of Health (NIH), National Natural Science Foundation of China, Chinese Academy of Sciences, Google Inc., the Royal Society of British, etc.

![](/api/attachments/RY9KTUDV/fulltext/images/e3a4de378b446b8424d11884fb07bb5407640eaa52871f59b428abb5f176e9d6.jpg)

![](/api/attachments/RY9KTUDV/fulltext/images/90cfb6b6d35fbdcec24105171e371f20480fe92265c78aacb695564b91d038a3.jpg)

![](/api/attachments/RY9KTUDV/fulltext/images/cf1af413b99e2789f239c629338f1b5d53f727b88851c2bef82db177e532edaa.jpg)

Dr. Zhijun Yan is a professor in the School of Management and Economics at Beijing Institute of Technology, China. His research interests include ecommerce, social network analysis, health informatics and complex systems. His research has appeared in Journal of Electronic Commerce Research, Transactions in International Information Systems, and many Chinese journals.

Hansi Jiang is a master student in the School of Management and Economics at Beijing Institute of Technology, China. His current research focuses on ecommerce and intelligent systems.

Taeha Kim is a professor in the College of Business and Economics at Chung-Ang University, Seoul, South Korea since 2009. He has previously been on the faculty at George Mason University since he received Ph.D. in MIS from the University of Arizona in 2002. He received MBA and BBA degrees from Seoul National University. His primary research interests include protection and distribution of digital products and strategic issues of IT investments.
