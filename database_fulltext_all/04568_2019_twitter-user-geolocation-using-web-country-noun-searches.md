---
otero_id: 4568
otero_key: "NH7R9BQ5"
title: "Twitter user geolocation using web country noun searches"
authors: "Paola Zola"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2019.03.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Twitter user geolocation using web country noun searches

Paola Zola<sup>a,⁎</sup>, Paulo Cortez<sup>b</sup>, Maurizio Carpita<sup>a</sup>

![](/api/attachments/NH7R9BQ5/fulltext/images/72f1f296873c091899bae364af0e75308f65ed9cd6bd68cf7ed05b012abc968f.jpg)

<sup>a</sup> Department of Economy and Management, University of Brescia, Brescia, Italy

<sup>b</sup> ALGORITMI Centre, Department of Information Systems, University of Minho, 4804-533 Guimarães, Portugal

## A R T I C L E I N F O

Keywords: Country geolocation Google Trends Machine learning Natural language processing Twitter

## A B S T R A C T

Several Web and social media analytics require user geolocation data. Although Twitter is a powerful source for social media analytics, its user geolocation is a nontrivial task. This paper presents a purely word distribution method for Twitter user country geolocation. In particular, we focus on the frequencies of tweet nouns and their statistical matches with Google Trends world country distributions (GTN method). Several experiments were conducted, using a recently created dataset of 744,830 tweets produced by 3298 users from 54 countries and written in 48 languages. Overall, the proposed GTN approach is competitive when compared with a state-of-theart world distribution geolocation method. To reduce the number of Google Trends queries, we also tested a machine learning variant (GTN2) that is capable of matching the GTN responses with an 80% accuracy while being much faster than GTN.

## 1. Introduction

Due to the expansion of the Internet, Web and social media analytics are becoming a key element of many decision support systems. Modern Web platforms, such as Twitter and Google Trends (GT), provide valuable big data that are easy to collect. Twitter is an important microblogging service with approximately 330 million active users that generate opinionated texts.<sup>1</sup> Twitter sentiment analysis has been used to predict stock markets [1], political elections [2], movie sales [3], and English Premier League soccer wins [4]. GT is another relevant Web source, providing Google statistics of search terms across diferent world regions. GT data-based analytics were used to predict flu trends [5], unemployment rates [6], consumer behavior [7], and the status of trending topics [8].

Several Web and social media analytics systems require user geographic location data. Examples include disaster early warning systems [9], property crime detection [10], event detection, epidemic dispersion, and news recommendations [11]. However, estimating the current location of a user is a nontrivial task for several microblogging services. For example, Twitter allows users to add profile locations and geographically tag their tweets, but the percentage of geotagged tweets is low [12,13] and Twitter user profile location data is often unreliable [14].

In this paper, we present a novel statistical approach for countrylevel location detection of Twitter users. This geolocation is potentially valuable in several decision support system applications, allowing them to easily filter users from a specific country. For instance, it can be used in Twitter sentiment analysis related to country commodity prices, such as steel, silver, or cotton prices.

Our approach assumes that people tend to write about news, events, and so on, from the country to which they are more related. It follows that, even if a user lives in country A, she/he might be more interested in news or information linked to another country B, so the potential information held in the user's tweet is likely to refer to country B. Consider the following examples related to two tweets about steel production:

1. “chinese steel rebar production reach the maximum over a year”; and

2. “downhill price for steel beams”.

Although it is clear for the first tweet example that the country of interest is China, for the second one it is not possible to link the information to a specific country. In contrast with the stock market domain, where easy identifiable cashtags<sup>2</sup> are common (for example, \$AAPL for Apple stocks) [1], commodity country-specific tweets tend to be similar to the second tweet example: unstructured and without an obvious geographic term, hashtag, or cashtag. Moreover, these tweets are often written in English, so they could be related to any country's market. It follows that our approach aims to associate a tweet with a highly probable country context when such a geographic context is not explicitly known to assist in country-level Twitter analytics.

To identify the unknown country, we analyze the word distribution of past user tweets. In contrast with previous studies that use specific geographical dictionaries, based on named-entity recognition (NER) modules [15], we consider generic nouns. As shown in Section 4.2, these nouns can incorporate geographic terms (like NER) but also non-geographic terms that are specific to a country. Examples of such nouns include “Brexit” (related to the United Kingdom), “Trump” (United States of America) and “cricket” (popular in Pakistan). In addition, because of cultural diferences, there are nouns that are used in distinct countries with diferent frequencies (for example, “thanks” in Table 9 and such information can potentially aid in country discrimination. Moreover, non-English users can tweet in their languages, and so non-English nouns (for example, “sono” and “stato” for Italy) can help in determining the country.

To take of this implicit information, we perform matching between frequent country-level GT and user tweets nouns (GTN). To the best of our knowledge, this is the first time that GT data has been used to detect geographical user information.

As a case study, we consider the steel production domain and recent Twitter data, which includes 744,830 tweets from 3298 users. Following an empirical design science research approach [16], we show that our GTN model is competitive when compared with a state-of-theart NER [15] (Section 4.1). To reduce the GT querying time, we also propose a GTN variant that uses machine learning (for example, deep multilayer perceptron and random forest) to learn the GT responses (Section 4.3). Finally, we demonstrate the applicability of GTN to nonsteel commodity domains using more recent Twitter data and a different but smaller sample of users (Section 4.4).

The contributions of the proposed approach include:

1. We perform a Twitter estimation of the most probable user country of interest when such explicit context is not known.

2. The estimation is based on generic nouns, retrieved from the user's historical tweets, which can include geographic words and other country-specific terms (including news, sports, religion, events, people, and native language nouns).

3. The proposed Google Trends nouns (GTN) method uses GT to solve a spatial detection task rather than a temporal task (as proposed in previous GT studies).

4. To reduce the GT query time, we proposed a second approach, termed GTN2, that uses machine learning.

5. We created a recent dataset related to the steel domain, which includes a conservative country estimate for 3298 users, to empirically compare GTN with a state-of-the-art NER.

The paper is organized as follows. Section 2 discusses the literature review related to social network location estimation methods. Section 3 details the country-level Twitter estimation methods. Section 4 presents and analyzes the experimental results. Finally, Section 5 summarizes the work, highlighting its main advantages, limitations, and future di rections.

## 2. Related work

Several studies have investigated Web and social network user location estimation. Before the rise of social networks, the Internet protocol (IP) address was the main element used for Web geotagging [17]. However, microblogs typically do not provide IP addresses. Moreover, the increasing use of virtual private networks (VPNs) reduces the reliability of IP address location.

Focusing on Twitter, user geographic estimation is a nontrivial task. Twitter location data can be directly retrieved by accessing geotagged tweets or user location field profiles. However, only a small fraction of tweets are geotagged. For example, the literature mentions low percentage values, varying from 0.42% [12] to 3.17% [13]. While mobile devices are increasingly used, users often switch of global positioning system (GPS), for privacy reasons or to save battery consumption. Moreover, although Twitter users can add a geographic reference to their profiles, the field is free text and often unreliable locations are used (for example, “in your heart” or “everywhere”). Hecht et al. [14] estimate that approximately 34% of Twitter users add nonrealistic text locations.

Table 1 summarizes the state-of-the-art research work on social network user location estimation, using chronological order and emphasizing the Twitter data source (data source column). There are three main types of social network user location estimation methods (type column):

1. Image recognition (IR): digital photos posted on social networks provide a vast amount of information, including location. For instance, Aulov et al. [18] studied the Deepwater horizon oil spill disaster in the Gulf of Mexico using Flickr photos and locating them to the desired area.

2. Friendship network (FN): the assumption is that the user's location can be inferred by the locations of her/his friendship network. Examples of work that followed this assumption are [19–21].

3. Word distribution (WD): related to our approach, it includes methods that are based on text analysis and word extraction. Some studies use existing NER modules, location indicative words (LIW), and gazetteers (geographic dictionaries) to extract locations from tweets (e.g., [15]). Other studies are based on tweet word frequencies, proposing methods to filter local words [12,22,23].

Some studies complement the previous methods with the use of additional features (AF), such as the location field from the user profile metadata [24,25] or the tweeted time zone [11]. Other studies combine the diferent types, such as: IR and WD [26]; WD and FN [27–31]; and WD, FN, and AF [25].

The related work can also be characterized by the text language, location target, discrimination level, search area of interest, computational algorithm, evaluation method (val.), and metric. The type of language is often associated with the search area. In most cases, the messages are written in English. Regarding the target, while some studies focus on where the tweet was written (e.g., [32,24,25]), the majority try to detect the user's home location (e.g., [12,27,34,29,31]). As for the discrimination level, there are two main approaches: detecting larger regions (e.g., countries or states) or smaller regions (e.g., cities, landmarks, geographic coordinates, or postal codes). Some fine-grained level detection methods (e.g., geographic coordinates) are often associated with a specific geographic area and events, such as natural disasters or emergency responses [18,36,24,39]. The location level often afects the type of evaluation metric used. Large region discrimination methods tend to perform multiclass tasks, so common classification metrics Witten2017 are often adopted (e.g., accuracy, precision, or recall). More diverse measures are used by the small region discrimination methods, including standard classification metrics (e.g., accuracy and precision), classification accuracy within a tolerance radius (Acc@R), or even regression metrics (e.g., root mean squared error). A wide variety of algorithms were adopted, including: approaches based on data frequency and statistics (e.g., information gain), generic machine learning models (e.g., neural network, support vector machine, or random forest), and specific geographic/Twitter-dependent methods (e.g., geocontext locator, geoparsing, or placemaker using tweet content). These algorithms were validated using either the simpler holdout (train and test split) or the more robust k-fold cross-validation.

The last row of Table 1 positions our work, which assumes a pure WD approach, a country-level detection, and multilingual tweets (mixed). The main novelty is the usage of generic nouns and GT source (the GTN method), as detailed in Section 3 and compared with a stateof-the-art WD method [15] in Section 4.

<sup>b</sup> Language: Chinese (ZH), English (EN), Hindi (HI), Italian (IT), Korean (KR), Portuguese (PT), Turkish (TR); mixed: combination of multiple languages. c Facebook (FB). Twitter (TW) Facebook (FB), Twitter (TW).

Summary of the related work.

<table><tr><td>Study</td><td> $Type^a$ </td><td> $Lang.^b$ </td><td> $Data^c$ source</td><td> $Tar.^d$ </td><td> $Level^e$ </td><td>Data  $period^f$ </td><td> $User size^f$ </td><td> $Data size^f$ </td><td> $Val.^g$ </td><td> $Area^h$ </td><td> $Algorithm^i$ </td><td> $Metric^j$ </td></tr><tr><td>Crandall et al. [26]</td><td>IR,WD</td><td>EN</td><td>Flickr</td><td>F</td><td>SP</td><td>ND</td><td>307 K</td><td>33 M</td><td>ND</td><td>W</td><td>BC,SVM</td><td>Acc</td></tr><tr><td>Backstrom et al. [19]</td><td>FN</td><td>EN</td><td>TW</td><td>U</td><td>SP</td><td>ND</td><td>2.9 M</td><td>ND</td><td>ND</td><td>USA</td><td>MLE</td><td>Acc@25mi</td></tr><tr><td>Cheng et al. [12]</td><td>WD</td><td>EN</td><td>TW</td><td>U</td><td>CI</td><td>2009-10</td><td>1 M</td><td>3 M</td><td>10CV</td><td>USA</td><td>MLE</td><td>Acc@100 ml</td></tr><tr><td>Davis et al. [20]</td><td>FN</td><td>PT</td><td>TW</td><td>T</td><td>CI</td><td>ND</td><td>25 K</td><td>ND</td><td>10CV</td><td>BR</td><td>DFS</td><td>P</td></tr><tr><td>Kinsella et al. [32]</td><td>WD</td><td></td><td>TW</td><td>T</td><td>CO,SP</td><td>2010</td><td>7 M</td><td>ND</td><td>5CV,HO</td><td>W</td><td>PM,KL,QL</td><td>Acc</td></tr><tr><td>Aulov et al. [18]</td><td>IR</td><td>EN</td><td>Flickr</td><td>F</td><td>SP</td><td>2010</td><td>ND</td><td>190</td><td>ND</td><td>MXG</td><td>GNOME</td><td>RMSE</td></tr><tr><td>Dalvi et al. [22]</td><td>WD</td><td>EN</td><td>TW</td><td>T</td><td>CI</td><td>2009-11</td><td>14 M</td><td>200 M</td><td>ND</td><td>USA</td><td>DM,LM</td><td>P,R</td></tr><tr><td>Li [27]</td><td>WD,FN</td><td>EN</td><td>TW</td><td>U</td><td>CI</td><td>2011</td><td>4.0 M</td><td>ND</td><td>5CV</td><td>USA</td><td>UDI</td><td>Acc</td></tr><tr><td>Chang et al. [33]</td><td>WD</td><td>EN</td><td>TW</td><td>U</td><td>CI</td><td>2009-10</td><td>136 K</td><td>9 M</td><td>HO</td><td>USA</td><td>GMM,LM,MLE</td><td>Acc</td></tr><tr><td>Compton et al. [34]</td><td>FN</td><td>EN</td><td>TW</td><td>U</td><td>CI</td><td>2012-14</td><td>110 M</td><td>ND</td><td>5CV,HO</td><td></td><td>TVM</td><td>ME (km)</td></tr><tr><td>Han et al. [35]</td><td>WD</td><td>ENMixed</td><td>TW</td><td>U</td><td>SP</td><td>2011-12</td><td>500 K1.4 M</td><td>38 M12 M</td><td>10CV</td><td>NAW</td><td>DFS</td><td>Acc@161 km</td></tr><tr><td>Mahmud et al. [11]</td><td>WD,AF</td><td>EN</td><td>TW</td><td>U</td><td>SP</td><td>2011</td><td>10 K</td><td>1 M</td><td>10CV</td><td>USA</td><td>HE</td><td>Acc@100mi</td></tr><tr><td>Middleton et al. [36]</td><td>WD</td><td>EN,TR,IT,PT</td><td>TW</td><td>T</td><td>SP</td><td>2011-13</td><td>ND</td><td>1.5 M</td><td>ND</td><td>USA</td><td>G</td><td>F1</td></tr><tr><td>Ryoo et al. [23]</td><td>WD</td><td>KR</td><td>TW</td><td>U</td><td>SP</td><td>2010-11</td><td>3.3 M</td><td>615 M</td><td>5CV</td><td>KR</td><td>PGM</td><td>Acc@10 km</td></tr><tr><td>Minot et al. [28]</td><td>FN,WD</td><td></td><td>TW</td><td>U</td><td>CI</td><td>2014</td><td>29 K</td><td>7.0 M</td><td>ND</td><td>AFR</td><td>SVM,CBF</td><td>Acc@10 km</td></tr><tr><td>Lee et al. [15]</td><td>WD</td><td>EN</td><td>TW</td><td>T</td><td>ST</td><td>2013-14</td><td>ND</td><td>113 K</td><td>10CV</td><td>USA</td><td>SVM,BC,RF</td><td>R</td></tr><tr><td>Rahimi et al. [21]</td><td>FN</td><td>EN</td><td>TW</td><td>U</td><td>SP</td><td>2011-12</td><td>9.5 K450 K1.4 M</td><td>380 K39 M12 M</td><td>HO</td><td>USAW</td><td>LP</td><td>Acc@161km</td></tr><tr><td>Rahimi et al. [29]</td><td>FN,WD</td><td>EN</td><td>TW</td><td>U</td><td>SP</td><td>2011-12</td><td>9.5 K450 K1.4 M</td><td>380 K39 M12 M</td><td>HO</td><td>USAW</td><td>LP</td><td>Acc@161 km</td></tr><tr><td>Rodrigues et al. [30]</td><td>FN,WD</td><td>PT</td><td>TW</td><td>U</td><td>CI</td><td>2010</td><td>12 K</td><td>2 M</td><td>10CV</td><td>BR</td><td>MM,BC,MRW</td><td>Acc</td></tr><tr><td>Kotzias et al. [37]</td><td>FN</td><td>EN</td><td>TW</td><td>U</td><td>CI</td><td>2013</td><td>43 K40K55 K</td><td>1.9 M1.3 M1.5 M</td><td>10CV</td><td>IRUKUSA</td><td>LDA</td><td>P</td></tr><tr><td>Laylavi et al. [24]</td><td>WD,AF</td><td>EN</td><td>TW</td><td>T</td><td>SP</td><td>2015</td><td>2 K</td><td>ND</td><td>ND</td><td>AUS</td><td>MELI</td><td>Acc@12.2 km</td></tr><tr><td>Singh et al. [38]</td><td>WD</td><td>ENHI</td><td>TW</td><td>T</td><td>SP</td><td>2015-16</td><td>ND</td><td>32 K</td><td>ND</td><td>IN</td><td>MM</td><td>Acc</td></tr><tr><td>Williams et al. [25]</td><td>WD, FN,AF</td><td>EN</td><td>TW</td><td>T</td><td>SP</td><td>2016</td><td>15 K</td><td>ND</td><td>ND</td><td>W</td><td>GCL</td><td>Acc@5 kmAcc@160 km</td></tr><tr><td rowspan="4">Quian et al. [31]</td><td rowspan="4">FN,WD</td><td rowspan="4">EN,ZH</td><td>TW</td><td rowspan="4">U</td><td rowspan="4">CO,CI</td><td rowspan="4">2011</td><td rowspan="4">1.5 M329 K1.0 M1 K</td><td rowspan="4">ND</td><td rowspan="4">HO</td><td rowspan="4">WUSA CHND</td><td rowspan="4">NN</td><td rowspan="4">Acc</td></tr><tr><td>TW</td></tr><tr><td>Weibo</td></tr><tr><td>FB</td></tr><tr><td>Avvenuti et al. [39]</td><td>WD</td><td>EN,IT</td><td>TW</td><td>T</td><td>SP</td><td>2011-15</td><td>ND</td><td>9 K2 K</td><td>ND</td><td>WIT</td><td>G</td><td>Acc</td></tr><tr><td rowspan="3">Rahimi et al. [40]</td><td rowspan="3">FN,WD</td><td rowspan="3">EN</td><td>TW</td><td rowspan="3">U</td><td rowspan="3">SP</td><td rowspan="3">2011-12</td><td rowspan="3">9.5 K450 K1.4 M</td><td rowspan="3">380 K39 M12 M</td><td rowspan="3">HO</td><td rowspan="3">USAUSAW</td><td rowspan="3">NNDCCA</td><td rowspan="3">Acc@161 km</td></tr><tr><td>TW</td></tr><tr><td>TW</td></tr><tr><td>This work</td><td>WD</td><td>Mixed</td><td>TW</td><td>U</td><td>CO</td><td>2017</td><td>49 K</td><td>21 M</td><td>10CV</td><td>W</td><td>GTN,GTN2</td><td>Acc, WF1</td></tr></table>

<sup>a</sup> Image recognition (IR), friendship network (FN), word distribution (WD), additional features (AF).  
<sup>d</sup> Target: Flickr picture location (F), tweet location (T), user's home location (U).  
<sup>e</sup> City (CI), country (CO), one of 50 states (ST), specific place (SP) from a region (e.g., coordinates, landmark or ZIP code).  
<sup>f</sup> Nondisclosed (ND), thousand (K), million (M); user and data size represent the initial collected values, before filtering.  
<sup>g</sup> Validation: n-fold cross validation (nCV), hold out (HO), nondisclosed (ND).  
<sup>h</sup> Africa (AFR), Australia (AUS), Brazil (BR), China (CH), India (IN), Ireland (IR), Italy (IT), Korea (KR), Mexican Gulf (MXG), nondisclosed (ND), North America (NA), United Kingdom (UK), United States of America (USA), World (W).  
<sup>i</sup> Bayesian classifier (BC), consensus-based fusion (CBF), data frequency or statistic (DFS)-based, deep canonical correlation analysis (DCCA), distance model (DM), geoparsing-based (G), geocontext locator (GCL), Gaussian mixture model (GMM), general NOAA oil modeling environment (GNOME), Google Trends nouns (GTN), Google Trends nouns and machine learning (GTN2), hierarchical ensemble (HE), Kullback-Leibler (KL) divergence, label propagation (LP), language model (LM), latent Dirichlet allocation (LDA), Markov model (MM), maximum likelihood (MLE)-based, multi rank walk (MRW), multi-elemental location inference (MELI), neural network (NN), placemaker (PM) using tweet content, probabilistic generative model (PGM), query likelihood (QL), random forest (RF), support vector machine (SVM), total variation minimization (TVM), unified discriminative influence (UDI) model.  
<sup>j</sup> Accuracy (Acc), accuracy using a radius of R (Acc@R, R in miles (mi) or kilometers (km)), F1-score (F1), mean error (ME), precision (P), recall (R), root mean square error (RMSE), weight averaging F1-score (WF1).

## 3. Data and methods

## 3.1. Data

Using automatic computational code (written in Python and R) and tools, we created a dataset with recent Twitter data to test the country geolocation methods. As an example in the decision support system application domain, we have targeted steel alloy. For the initial selection of users, we selected all tweets that included one of the keywords {“steel price”, “steel industry”, “steel production”}, from March to

November 2017. These queries resulted in 138,484 tweets, related to 49,203 users. Only a tiny fraction of the tweets (192) were geotagged. In addition, only 33,886 users had a filled location profile field. We note that, in this work, retweets are treated in the same manner as common tweets, because retweets might be helpful in identifying the user's country of interest $( \boldsymbol { \mathrm { e . g . } } ,$ retweets of a politician).

To set the ground truth, we designed a conservative procedure that discards a large number of users but is more reliable for comparing geolocation methods. The procedure is based on a strong double-source verification that considers both metadata (user profile location field) and LIW from historical user tweets. We considered the set of 33,886 users with some location profile data and retrieved up to a maximum of 3200 past tweets for each user. We then used OpenNLP [42] and the ggmap R package [43] tools to extract LIW from the historical tweets (OpenNLP) and obtain the Google Maps country for each LIW (ggmap).The most frequent country, computed over the full set of LIW for a given user, was then compared with the metadata information. After removing country mismatches, including metadata with slang and nonrealistic locations, the final ground truth dataset contains 3298 users and 744,830 tweets, representing an average of 226 tweets per user.

While all selected users have written at least one English term, from the set {“steel price”, “steel industry”, “steel production”}, the collected historical tweets were written by users from both native English speaking (e.g., Australia) and non-native English speaking (e.g., Spain) countries. Table 2 presents the percentage of tweets written in a specific language (tweets column) and the percentage of users per country (users column). Fig. 1 plots these last values visually on a world map (the higher the percentage, the darker is the country color). The language values were obtained by using the textcat R package [44]. The majority of the tweets were written in English (66.2%), followed by the German (18.8%) and Catalan (4.4%) languages.

As for the countries, most users come from anglophone countries, such as United States of America (USA) (45.7%), United Kingdom (UK) (12.3%), and Australia (6.4%). As for the non-anglophone countries, most users are from India (27.1%), while other countries are much less prevalent (e.g., Germany with 0.5%). In total, the dataset contains tweets written in 48 languages and users from 54 countries.

Only one state-of-the-art study performed a mixed-language tweet geolocation [35], as shown in Table 1. Our work does not separately consider datasets of tweets written in a specific language, because it is more trivial to identify the country when the language is distinctive of a nation $( \boldsymbol { \mathrm { e . g . } } ,$ , Japanese)

Table 2  
Dataset tweet languages and users per country.

<table><tr><td>Language</td><td>Tweets</td><td>Country</td><td>Users</td></tr><tr><td>English</td><td>66.2%</td><td>United States of America (USA)</td><td>45.7%</td></tr><tr><td>German</td><td>18.8%</td><td>India</td><td>27.1%</td></tr><tr><td>Catalan</td><td>4.4%</td><td>United Kingdom (UK)</td><td>12.3%</td></tr><tr><td>Danish</td><td>1.9%</td><td>Australia</td><td>6.4%</td></tr><tr><td>Nepali</td><td>1.3%</td><td>Canada</td><td>3.1%</td></tr><tr><td>Indonesian</td><td>1.1%</td><td>Germany</td><td>0.5%</td></tr><tr><td>Latin</td><td>0.9%</td><td>Pakistan</td><td>0.5%</td></tr><tr><td>Rumantsch</td><td>0.8%</td><td>South Africa</td><td>0.4%</td></tr><tr><td>Slovak</td><td>0.9%</td><td>China</td><td>0.3%</td></tr><tr><td>French</td><td>0.4%</td><td>France</td><td>0.3%</td></tr><tr><td>Esperanto</td><td>0.3%</td><td>Nigeria</td><td>0.3%</td></tr><tr><td>Swahili</td><td>0.3%</td><td>Spain</td><td>0.3%</td></tr><tr><td>Sanskrit</td><td>0.3%</td><td>Kenya</td><td>0.2%</td></tr><tr><td>Spanish</td><td>0.2%</td><td>Italy</td><td>0.2%</td></tr><tr><td>Romanian</td><td>0.2%</td><td>Mexico</td><td>0.2%</td></tr><tr><td>Swedish</td><td>0.2%</td><td>Finland</td><td>0.1%</td></tr><tr><td>Czech</td><td>0.2%</td><td>Ireland</td><td>0.1%</td></tr><tr><td>Malay</td><td>0.1%</td><td>Japan</td><td>0.1%</td></tr><tr><td>Hungarian</td><td>0.1%</td><td>Argentina</td><td>0.1%</td></tr><tr><td>Afrikaans</td><td>0.1%</td><td>Belgium</td><td>0.1%</td></tr><tr><td>Slovenian</td><td>0.1%</td><td>Brazil</td><td>0.1%</td></tr><tr><td>Dutch</td><td>0.1%</td><td>Colombia</td><td>0.1%</td></tr><tr><td>Tagalog</td><td>0.1%</td><td>Indonesia</td><td>0.1%</td></tr><tr><td>Basque</td><td>0.1%</td><td>Malaysia</td><td>0.1%</td></tr><tr><td>Others</td><td>0.6%</td><td>Others</td><td>1.2%</td></tr></table>

Following the work of [35], we adopted a mixed language approach, which is more natural for the geolocation of countries, because Twitter is a multilingual platform. Nevertheless, the values in Table 2 reflect the steel domain scenario. Therefore, most of the tweets are written in English, which is a geographically widespread language that is more dificult to geolocate [35], making this dataset challenging and interesting for comparing purely WD methods.

## 3.2. Google Trends nouns

As explained above, the proposed GTN WD approach uses only tweet nouns, because we assume they are the most representative part of speech able to identify diferent countries.

For user u, the GTN approach works by first identifying the sequence of the most frequent nouns ${ \bf n } _ { u } = { \bf \varphi } < n _ { 1 } , n _ { 2 } , \ldots , n _ { l _ { u } } >$ , in descending order and with a length of $l _ { u }$ elements. To obtain $\mathbf { n } _ { w }$ the tweets are first preprocessed by transforming the text to lowercase and removing English stopwords. The TextBlob Python module is then used to extract noun phrases and then the nouns. We note that the TextBlob module is faster than other tools [45].

For each noun $\boldsymbol { n } _ { i } \in \mathbf { n } _ { w }$ a GT query is executed by using the Pytrends Python module. To limit the number of queries, a fixed pruning threshold $( p )$ is used, such that $l _ { u } \le p$ for all u users. The GT query result for noun $n _ { i }$ is a sequence with integer confidence scores for an alphabetic list of countries C with a length of $l _ { c } = 2 5 0$ . The scores range from 0 (lowest confidence) to 100 (highest confidence). Let $\mathbf { G } _ { u }$ denote the GT confidence score matrix for user u with a size of $l _ { c } \times l _ { u } ,$ where each score is represented as $g _  c , $ for country $c \in C$ and the i-th most frequent noun. We test three strategies to weight the GT scores, resulting in the weighted confidence score matrix $\mathbf { S } _ { u } \left( l _ { c } \times l _ { u } \right)$ with the elements $\begin{array} { r } { \boldsymbol { s } _ { c , } } \end{array}$ (country, noun):

• Equal weights (EQ): no weights are used, and so $s _ { c , \ i } = g _ { c , \ i } .$

Internet usage (IU): weighted according to the fraction of Internet users for a specific country $c ~ ( w _ { c } )$ according to the World Bank statistics<sup>3</sup>:

$$
\forall c \in C, \forall i \in \{1,..., l _ {u} \}: s _ {c, i} = w _ {c} g _ {c, i}\tag{1}
$$

Nouns frequency (NF): weighted according to the order of the nouns (more frequent nouns have stronger weights):

$$
\forall c \in C, \forall i \in \{1,..., l _ {u} \}: s _ {c, i} = w _ {i} g _ {c, i}\tag{2}
$$

where $w _ { i } = ( l _ { u } - i + 1 ) / l _ { u } .$

Once the confidence score is computed, we explore two statistical approaches to estimate the most probable country $c _ { u }$ for user u:

Join frequency (JF) – based on the highest score country when summing all noun scores:

$$
\mathrm{c} _ {u} = \underset {c} {\operatorname{argmax}} \left(\sum_ {i = 1} ^ {l _ {u}} s _ {c, i}\right)\tag{3}
$$

Absolute frequency (AF) – selects the most common country (mode) when considering the highest score countries for all nouns:

$$
c _ {u} = M o d e (a r g m a x _ {c} (s _ {c, i}) \forall i \in \{1,..., l _ {u} \})\tag{4}
$$

where Mode denotes the mode of a set.

![](/api/attachments/NH7R9BQ5/fulltext/images/fd80ad153e37d46880dec08269fc1769800d802e6e777b7fe40cf3d77577e1b3.jpg)  
long  
Fig. 1. Percentage of users per country plotted on a world map.

## 3.3. Machine learning

In this paper, we use machine learning for three diferent goals: to obtain the benchmark geolocation method outputs (for comparison purposes with GTN); to access the quality of the proposed GTN; and to mimic the GTN responses. For all three goals, the input features consist of the classical bag-of-words (BoW) [46], in a total of 24,269 unique nouns for the 3298 users considered. The classifier output is the geolocation country but the target values depend on the machine learning goal. The first goal is detailed in Section 3.4. The second goal is applied during the error analysis procedure [47], to verify whether the GTN errors are solvable by machine learning. The third goal, termed the GTN2 method here, is used to reduce the number of GT queries. Similarly to other Web query geolocation methods (for example, based on Google Maps), GTN requires a substantial computational efort because of the large number of GT requests. To solve this problem, we use GTN as an oracle, providing the target classification responses for the machine learning methods

We explore four classification algorithms with powerful learning capabilities [48,49]: bagging (BG), random forest (RF), support vector machine (SVM), and a deep learning multilayer perceptron (MLP).

Breiman's bagging or bootstrap aggregation algorithm (BG) trains t independent classifiers on a given training set by sampling, with replacement, instances from the training set. The essential idea is to average noise and avoid overfitting by using unbiased models that reduce the variance [48]. Bagging is normally applied using decision trees as the individual weak learners, which corresponds to the BG model used in this work.

RF is a successful model that was proposed in 2001: it combines t decision trees based on bagging and random selection of input features [50]. RF tends to obtain good classification results even when using its default parameters and when no feature selection method is adopted [48]. In a recent large comparison study, the RF classifier was ranked as the best classifier among 17 of the main machine learning types of algorithms [51].

SVM are widely used in text classification [52]. The model is based on a maximized margin criterion [53]. For binary classification, the SVM algorithm can compute the best separating hyperplane in a feature space, which is defined by a kernel transformation. In this work, we adopt the linear kernel, because it is very fast and works well with highdimensional input features, which is the case with our nouns dataset. The model contains one hyperparameter (C) that controls the tradeof between fitting the errors and obtaining a smooth decision boundary. Because we have 54 class labels, we used the one-vs-rest multiclass classification, which involves training a single classifier per class [54].

Moreover, recent remarkable developments were proposed in the field of deep learning, leading to neural network architectures that obtained the best results in diverse competitions (for example, com puter vision and natural language processing) [55]. Such success revived the popularity of the MLP neural model. In this work, we assume a modern MLP representation, also known as deep feedforward neural network [49], with three hidden layers (with $h _ { 1 } , \ h _ { 2 } ,$ and $h _ { 3 }$ hidden nodes) that uses [55]: the ReLU activation function on all hidden units, the Softmax function on the output layer, a dropout regularization, and early stopping (to reduce overfitting).

All classifiers are evaluated by using an external 10-fold cross-validation scheme, as explained in Section 3.5. For each of the 10 crossvalidation iterations, the available data is divided into training data (90% of the instances) and test data (10%). The test data is used to measure the classification performance of the selected models. The training data is used to fit the machine learning models and to perform the hyperparameter selection. To reduce the bias towards a particular model [56], we apply the same hyperparameter selection procedure for BG, RF, SVM, and MLP. Using standard practice [47,48], the training data is further split into training and validation sets (internal holdout validation). The training set, with 80% of the training instances (0.8 × 0.9=0.72% of all available data), is used to fit the classifier. The validation set, with the other 20% of the training data examples (0.18% of all data), is used to monitor the best generalization capability, in terms of global classification accuracy, associated with a hyperparameter or set of hyperparameter values. After selecting the hyperparameters, the machine learning model is retrained with all training data.

To provide a fair comparison, we applied a grid search with 10 diferent hyperparameter combinations for each machine learning algorithm. For BG and RF, the number of trees ranged through t∈ {50, 100, 150, 200, 250, 300, 500, 1000, 1500, 3000}. For SVM the C parameter was searched using C∈ {0.01, 0.05, 0.1, 0.2, 0.5, 1, 5, 10, 50, 100}. For MLP, we tested ten diferent MLP models, which correspond to diferent combinations of numbers of hidden nodes and dropout values, as detailed in Table 3. The number of MLP inputs is large, because it includes all unique dataset nouns. Therefore, to reduce computational efort, and following what is suggested in [57], the MLP combinations assume a decreasing hidden layer size structure, where $h _ { 1 } > h _ { 2 } > h _ { 3 }$ . The other parameters were set to their default values, as implemented using the keras and sklearn Python modules.

Because the country classes are unbalanced (for example, 45.7% of users are from the USA, while only 0.1% are from Brazil; Table 2), we applied an oversampling procedure [58] to all training sets of the machine learning algorithms. The goal is to improve classifier performance for the minority classes by performing random sampling, with repetition, such that the training set becomes balanced. We note that we did not consider undersampling because some classes are very rare, and so undersampling would lead to very small training sets. In addition, the test sets retain the original unbalanced class distribution.

Table 3  
Diferent MLP models tested during the hyperparameter selection stage.

<table><tr><td>Model number</td><td>Hidden layer size 1 ( $h_1$ )</td><td>Hidden layer size 2 ( $h_2$ )</td><td>Hidden layer size 3 ( $h_3$ )</td><td>Dropout</td></tr><tr><td>1</td><td>200</td><td>100</td><td>70</td><td>0.4</td></tr><tr><td>2</td><td>200</td><td>100</td><td>70</td><td>0.3</td></tr><tr><td>3</td><td>300</td><td>150</td><td>50</td><td>0.4</td></tr><tr><td>4</td><td>300</td><td>100</td><td>50</td><td>0.4</td></tr><tr><td>5</td><td>500</td><td>200</td><td>100</td><td>0.4</td></tr><tr><td>6</td><td>500</td><td>200</td><td>50</td><td>0.4</td></tr><tr><td>7</td><td>200</td><td>150</td><td>50</td><td>0.4</td></tr><tr><td>8</td><td>200</td><td>150</td><td>50</td><td>0.3</td></tr><tr><td>9</td><td>500</td><td>150</td><td>70</td><td>0.4</td></tr><tr><td>10</td><td>500</td><td>100</td><td>50</td><td>0.4</td></tr></table>

## 3.4. Benchmark methods

For comparison purposes, we selected a recent WD geolocation benchmark method (BM) [15] that can be simulated using similar procedures and tools already used in this research. The BM method first uses an NER tool (Stanford CoreNLP<sup>4</sup>) to extract geolocation terms. The terms are fed to Google Maps to obtain the geographic coordinates. When Google Maps does not return a single country, this is considered an ambiguous case, which is then estimated by using a machine learning algorithm: naive Bayes, SVM, or RF. Using only training data (the BoW approach), the algorithm is fitted to the subset of unambiguous cases and then used to predict all ambiguous cases, including those from the test data. Because RF achieved the best results in [15], we adopt this learning classifier for BM. We also test a hybrid benchmark method (BM2), which works similarly to BM except that the ambiguous cases are estimated using GTN instead of the learning classifier (RF).

## 3.5. Evaluation

The created Twitter dataset is described in Section 3.1: it includes 3298 users (instances) related to 54 countries. The input features consist of 24,269 unique nouns. The countries were identified by the ground truth procedure that is based on a conservative double-source verification, which considers both metadata (user profile location field) and LIW, given all historical tweets (744,830 messages). The Twitter user country geolocation is modeled as a multiclass task (with 54 output labels), and so common classification performance metrics are adopted. The confusion matrix maps predicted values to actual values. From this matrix, several multiclass performance measures can be computed. For a particular class c, we use [41]: accuracy (Acc ), precision , recall , and F1-score .

To obtain a single performance measure from the multiclass results, we adopt global accuracy (Acc), which is widely used in classification tasks. The F1-score is a more reliable measure when the data are unbalanced, which is true in our case (as shown in Table 2). Therefore, we also compute a single global F1-score by performing a weight averaging operation (WF1), in which each F1-score is weighted proportionally to the class frequency in the data. The evaluation metrics were computed using the sklearn module.

GTN is a statistical approach that does not require training data.

Nevertheless, for comparison with the machine learning approaches (Table 12), we adopt the popular 10-fold cross-validation scheme (Section 2) in all comparison tests. The data are randomly split into ten equal-sized folds; then, using a rotation scheme, one fold is selected for testing and all of the others are used for training (if needed by the method). This result in 10 sets of predictions and desired values for each method. To aggregate the results, we average the k = 10 distinct classification performance results, and the statistical significance is obtained by applying the nonparametric Mann-Whitney test [59].

## 4. Results

## 4.1. Google Trends nouns results

We conducted preliminary experiments with GTN, to tune the method. The preliminary experiments considered a random subset of our data related to 267 users (8%). Adopting the EQ and JF methods, we first tested distinct pruning threshold values, which were based on some noun distribution statistics (median, sixth percentile, third quar tile, mean): p ∈ {112,156,298,770}. The best results (with an accuracy of 76.0%) were achieved for p = 298, which was fixed. Using the same preliminary sample, we then compared diferent weighting methods for the country confidence scores and country classification, in a total of six GTN models (Table 4). The best classification results were achieved by the first model, which uses EQ and JF, becoming the selected config uration for the GTN method.

The average 10-fold country geolocation results for GTN and benchmark methods are presented in Table 5. When analyzing both classification metrics, global accuracy (Acc) and weight-averaging F1- score (WF1), the comparison clearly favors GTN with respect to the state-of-the-art WD method (BM), showing a substantial diference (15.7 percentage points for Acc and 8.5 percentage points for WF1) that has statistical significance. The hybrid NER GTN method (BM2) provides better performance than BM, indicating that GTN handles the ambiguous cases better than RF. Nevertheless, GTN achieves the best overall results, with an improvement of 2.3 percentage points for Acc and 1.8 for WF1, although these are not statistically significant.

## 4.2. Error analysis

To better understand the errors produced by GTN, we performed an error analysis [47], in which we manually inspected a total of 638 Twitter user accounts related to GTN country misclassification examples. Table 6 the errors in terms of four main categories (error type column). There are 76 cases (11.9%) for which GTN provided the correct classification (error type A) when the conservative ground truth method (Section 3.1) was wrong. These cases are mostly related to user metadata with ambiguous geolocation terms that can refer to more than one anglophone country (for example, “Newport” city can refer to USA or UK; see Table 7). We have recomputed the classification performance for GTN, BM, and BM2 by using the manually adjusted 76 “true” cases. The results obtained are presented in Table 8, which confirms that the “true” classification performance for GTN is actually higher than the results shown in Table 5. In fact, in Table 8 the GTN achieves an Acc of 83.0% and a WF1 of 83.4%. We particularly note that GTN statistically outperforms both benchmark methods (BM and BM2) when adjusted to the “true” values. A common GTN error (type B) is an anglophone country mismatch (32.0%, e.g., UK or Canada instead of USA). There are also some errors (type C, 3.1%) related to proximate countries when considering the location (e.g., Belgium and Netherlands) or language $( \boldsymbol { \mathrm { e . g . , } }$ Portugal and Brazil). Most GTN mismatches (type D, 53.0%) are related to other mismatches not included in the previous error types. Table 7 reports some examples of the A, B, C, and D error types. In Table 7, the user name is omitted for privacy reasons.

To better exemplify how the nouns can be associated with countries, we present the distribution of the ten most frequent nouns used by the

Table 4  
Comparison of diferent GTN weighting and country classification strategies (bold denotes best value).

<table><tr><td>Model</td><td>Score weighting</td><td>Classification strategy</td><td>Acc</td></tr><tr><td>1</td><td>EQ</td><td>JF</td><td>76.0</td></tr><tr><td>2</td><td>EQ</td><td>AF</td><td>73.0</td></tr><tr><td>3</td><td>IU</td><td>JF</td><td>56.6</td></tr><tr><td>4</td><td>IU</td><td>AF</td><td>40.1</td></tr><tr><td>5</td><td>NF</td><td>JF</td><td>75.3</td></tr><tr><td>6</td><td>NF</td><td>AF</td><td>45.3</td></tr></table>

Table 5  
Country geolocation results (in %, best dataset values in bold).

<table><tr><td>Metric</td><td>BM</td><td>BM2</td><td>GTN</td></tr><tr><td>Acc</td><td>64.9</td><td>78.3</td><td> $80.6^{\circ}$ </td></tr><tr><td>WF1</td><td>72.8</td><td>79.5</td><td> $81.3^{\circ}$ </td></tr></table>

⋄ – Statistically significant under a pairwise comparison when compared with BM (p-value < 0.05).

Table 6  
Error analysis for GTN.

<table><tr><td>Error type</td><td>Number</td><td>Percentage</td></tr><tr><td>Correct classification (A)</td><td>76</td><td>11.9</td></tr><tr><td>Anglophone mismatch (B)</td><td>204</td><td>32.0</td></tr><tr><td>Close country by language or location (C)</td><td>20</td><td>3.1</td></tr><tr><td>Other mismatches (D)</td><td>338</td><td>53.0</td></tr><tr><td>Total</td><td>638</td><td>100.0</td></tr></table>

Table 7  
Examples of misclassified locations.

<table><tr><td>Error type</td><td>Lang.a</td><td>Metadata location</td><td>Ground truth</td><td>GTN</td><td>Manual assessment</td></tr><tr><td>A</td><td>EN</td><td>Newport</td><td>USA</td><td>UK</td><td>UK</td></tr><tr><td>A</td><td>EN</td><td>North East</td><td>USA</td><td>UK</td><td>UK</td></tr><tr><td>B</td><td>EN</td><td>Scotland</td><td>UK</td><td>USA</td><td>UK</td></tr><tr><td>C</td><td>NL</td><td>Mechelen</td><td>Belgium</td><td>Netherlands</td><td>Belgium</td></tr><tr><td>C</td><td>ES</td><td>Barcelona</td><td>Spain</td><td>Guatemala</td><td>Spain</td></tr><tr><td>C</td><td>EN</td><td>Suri</td><td>India</td><td>Bangladesh</td><td>India</td></tr><tr><td>C</td><td>PT</td><td>Portugal</td><td>Portugal</td><td>Brazil</td><td>Portugal</td></tr><tr><td>D</td><td>ES</td><td>Philadelphia</td><td>USA</td><td>Colombia</td><td>USA</td></tr></table>

Language: English (EN), Dutch (NL), Portuguese (PT), Spanish (ES).

## Table 8

Country geolocation results for the adjusted ground truth (in %, best dataset values in bold).

<table><tr><td>Metric</td><td>BM</td><td>BM2</td><td>GTN</td></tr><tr><td>Acc</td><td>63.6</td><td>79.1</td><td>83.0°</td></tr><tr><td>WF1</td><td>71.6</td><td>80.1</td><td>83.4°</td></tr></table>

⋄ – Statistically significant under a pairwise comparison when compared with BM and BM2 (p-value < 0.05).

GTN method to identify the country. Table 9 is related to a sample of four anglophone countries (Australia, Canada, UK, and USA), while Table 10 shows the most frequent nouns for four examples of non-anglophone countries (Finland, Italy, Pakistan, and Singapore). To create the tablets, we considered all nouns from all users that were correctly classified by the adjusted GTN model of Table 8. The respective classification accuracy (Acc) values for the selected country examples are: Australia – 80%, Canada – 32%, UK – 81%, USA – 94%, Finland – 75%, Italy – 100%, Pakistan – 74%, and Singapore – 100%.

Tables 9 and 10 show specific geographic terms that can be used to identify the country, working similarly to an NER tool. These include geographic nouns such as: “australia”, “sydney”, “canada”, “scotland” (Table 9); and “finland”, “oulu”, “pakistan” (Table 10). GTN also benefits from language diferences, as shown by the Italian examples of Table 10. However, even when considering the English language, there are also non-geographic terms (not used by NER) that do seem country specific and so can contribute added discrimination capability to GTN. For instance, “brexit” is associated with the UK, while “trump” is related to USA. For Pakistan there are several other examples of countryspecific terms, such as “maryamnsharif” (popular Pakistani politician), “cricket” (highly popular in the country), and “allah” (religion). A diferent interesting example is provided by the term “thanks”, which is used in three anglophone countries (Canada, UK, USA) but with different frequencies (e.g., 0.46% in Canada vs 0.22% in USA). This might be because of cultural diferences between countries. In contrast, there are other nouns that are often used with similar frequencies, such as “time” (0.39% for Canada and USA) and “year” (0.29% for Canada and 0.33% for USA). These generic nouns limit the GTN capability to discriminate between countries that use the same language, as shown by the anglophone errors of Table 6.

Following Table $^ { 6 , }$ we performed another error analysis step in which machine learning was used. We considered two machine learning error analysis setups:

• I – The 204 misclassified user examples who live in anglophone countries (Table 6) are removed from the dataset and are always used as the same test set in the 10 iterations of the 10-fold procedure. The remaining dataset examples pass through a 10-fold validation, to generate 10 training sets and learning models that are tested on the same 204 test set cases.

• II – Similar to the previous setup, except that the fixed test set is composed of all 638 − 76 = 562 “true” misclassified users (Table 6).

The machine learning models require a substantial computational efort because the nouns dataset is high-dimensional, with 24,269 features and 3298 instances. To reduce the computational efort, the hyperparameter selection is first applied to the dataset, from Section 3.1. The best hyperparameters for each classifier are then fixed and used in the 10-fold evaluation of all machine learning comparisons (setups I and II and experiments of Section 4.3). The hyperparameter selection procedure uses a 10-fold validation. During each 10-fold iteration, the training data is split using an internal holdout (80%/ 20%). For each learning algorithm, ten diferent models (described in Section 3.3) are trained. The best hyperparameter values are selected as the best 10-fold mean global accuracy (Acc) and this resulted in: BG – t = 300 trees, RF – t = 150 trees, SVM – C = 0.01, and MLP – model 7 of Table 3 (h = 200, h = 150, h = 50, dropout = 0.4).

The machine learning error analysis results are presented in Table 11.

The obtained classification measure values (WF1 and Acc) range from 21% (setup I, Acc, and RF) to 50.8% (setup I, WF1, and SVM). The best results were obtained by BG (setup I) and SVM (setup II). Globally, low performances were achieved, in particular, if compared with the machine learning results of Section 4.3. The machine learning dificulties in classifying both the anglophone misclassified users (setup I) and the GTN uncorrected responses (setup II) reinforce the competitiveness of the GTN approach.

## 4.3. Machine learning classification results

While the proposed GTN approach provides competitive country geolocation results (Table 5), it requires a substantial computational efort in terms of GT requests. During the experiments performed in this work, a total of 24,269 GT queries were executed: one for each distinct noun, requiring an average of 1.4 s for each GT query. Because there are 3298 users, the average user GTN response time is 10.3 s.

Table 9  
Most frequent nouns for four examples of anglophone countries.

<table><tr><td colspan="2">Australia</td><td colspan="2">Canada</td><td colspan="2">UK</td><td colspan="2">USA</td></tr><tr><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td></tr><tr><td>year</td><td>0.35%</td><td>canada</td><td>0.51%</td><td>time</td><td>0.46%</td><td>time</td><td>0.39%</td></tr><tr><td>time</td><td>0.31%</td><td>thanks</td><td>0.41%</td><td>people</td><td>0.42%</td><td>people</td><td>0.34%</td></tr><tr><td>people</td><td>0.30%</td><td>time</td><td>0.39%</td><td>news</td><td>0.34%</td><td>year</td><td>0.33%</td></tr><tr><td>australia</td><td>0.28%</td><td>year</td><td>0.29%</td><td>thanks</td><td>0.33%</td><td>news</td><td>0.26%</td></tr><tr><td>world</td><td>0.28%</td><td>business</td><td>0.29%</td><td>year</td><td>0.32%</td><td>trump</td><td>0.25%</td></tr><tr><td>news</td><td>0.26%</td><td>project</td><td>0.27%</td><td>work</td><td>0.29%</td><td>work</td><td>0.24%</td></tr><tr><td>work</td><td>0.24%</td><td>industry</td><td>0.27%</td><td>brexit</td><td>0.28%</td><td>world</td><td>0.23%</td></tr><tr><td>business</td><td>0.24%</td><td>news</td><td>0.24%</td><td>christmas</td><td>0.27%</td><td>life</td><td>0.22%</td></tr><tr><td>industry</td><td>0.22%</td><td>work</td><td>0.24%</td><td>scotland</td><td>0.26%</td><td>years</td><td>0.22%</td></tr><tr><td>sydney</td><td>0.21%</td><td>check</td><td>0.24%</td><td>government</td><td>0.24%</td><td>thanks</td><td>0.22%</td></tr></table>

Table 10  
Most frequent nouns for four examples of non-anglophone countries.

<table><tr><td colspan="2">Finland</td><td colspan="2">Italy</td><td colspan="2">Pakistan</td><td colspan="2">Singapore</td></tr><tr><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td><td>Word</td><td>Frequency</td></tr><tr><td>congratulations</td><td>0.34%</td><td>sono</td><td>0.50%</td><td>pakistan</td><td>1.16%</td><td>china</td><td>0.62%</td></tr><tr><td>camp</td><td>0.22%</td><td>perch</td><td>0.40%</td><td>maryamnsharif</td><td>0.73%</td><td>steel</td><td>0.62%</td></tr><tr><td>finland</td><td>0.22%</td><td>anche</td><td>0.40%</td><td>people</td><td>0.58%</td><td>price</td><td>0.47%</td></tr><tr><td>business</td><td>0.22%</td><td>stato</td><td>0.30%</td><td>allah</td><td>0.58%</td><td>prices</td><td>0.47%</td></tr><tr><td>thesis</td><td>0.22%</td><td>grande</td><td>0.30%</td><td>world</td><td>0.44%</td><td>time</td><td>0.47%</td></tr><tr><td>time</td><td>0.22%</td><td>posso</td><td>0.30%</td><td>cricket</td><td>0.44%</td><td>year</td><td>0.47%</td></tr><tr><td>seminar</td><td>0.22%</td><td>prima</td><td>0.30%</td><td>pakistani</td><td>0.44%</td><td>data</td><td>0.47%</td></tr><tr><td>technology</td><td>0.22%</td><td>bella</td><td>0.30%</td><td>morning</td><td>0.44%</td><td>report</td><td>0.47%</td></tr><tr><td>oulun</td><td>0.22%</td><td>bello</td><td>0.30%</td><td>imran</td><td>0.44%</td><td>conference</td><td>0.47%</td></tr><tr><td>oulu</td><td>0.22%</td><td>alla</td><td>0.30%</td><td>army</td><td>0.44%</td><td>trade</td><td>0.47%</td></tr></table>

To reduce the GTN request efort, we tested whether the GTN classification responses could be directly modeled as targets by the machine learning methods (the GTN2 method). The 10-fold average test results for GTN2 are shown in Table 12. The best values were achieved by the deep learning method (MLP), which outperforms other machine learning models for both classification metrics presenting a statistical significance when compared with BG, RF, and SVM (for Acc), and BG

Table 11  
Machine learning error analysis results (in %, best values in bold).

<table><tr><td colspan="9">Classification metric</td></tr><tr><td></td><td colspan="4">Acc</td><td colspan="4">WF1</td></tr><tr><td>Setup</td><td>BG</td><td>RF</td><td>SVM</td><td>MLP</td><td>BG</td><td>RF</td><td>SVM</td><td>MLP</td></tr><tr><td>I</td><td>41.7°</td><td>21.3</td><td>38.8</td><td>23.7</td><td>50.8°</td><td>29.7</td><td>45.5</td><td>28.8</td></tr><tr><td>II</td><td>40.2</td><td>31.2</td><td>43.1°</td><td>34.3</td><td>42.2</td><td>32.4</td><td>44.4°</td><td>30.0</td></tr></table>

⋄ - Statistically significant under a pairwise comparison when compared with other models (p-value < 0.05).

Table 12  
Country geolocation results for GTN2 (in %, best values in bold).

<table><tr><td>Metrics</td><td>BG</td><td>RF</td><td>SVM</td><td>MLP</td></tr><tr><td>Acc</td><td>61.3</td><td>69.6</td><td>73.8</td><td> $80.3^{\circ}$ </td></tr><tr><td>WF1</td><td>64.2</td><td>66.2</td><td>76.2</td><td> $77.4^{*}$ </td></tr></table>

– Statistically significant under a pairwise comparison when compared with RF, BG, and SVM (p-value < 0.05).

\* – Statistically significant under a pairwise comparison when compared with RF and BG (p-value < 0.05).

and RF (for WF1). MLP obtained a high-quality predictive performance (Acc of 80% and WF1 of 77%). Using an Intel Xeon E5 2.30-GHz computational server, the whole MLP training (for one 10-fold iteration) required approximately 1200 s and the MLP testing time is much faster, requiring approximately 3 ms per user. These results confirm that GTN2 is a valuable and computationally fast alternative to GTN. For future multiclass machine learning comparisons, the data used in this section has been made publicly available at https://github.com/ paolazola/Twitter-country-geolocation.

## 4.4. Demonstration application

To further demonstrate the applicability of GTN, we assume a decision scenario in which an analyst wants to distinguish the country of interest of Twitter users that tweet about commodity prices. New data was fetched during the first week of January 2019: this comprised the last 10 days of public tweets of users that typed at least one of the keywords {“copper commodity”, “sugar commodity”, “cotton commodity”, and “silver commodity”}. The original user sample was composed of 100 unique accounts. The Twitter profiles of these users were manually inspected, analyzing both the metadata and historical tweets, to detect the country of interest. This resulted in a set of 71 users with a clear country label. Although the sample is small, we note that a larger sample (concerning 3298 steel production-related users) and more robust validation (10-fold) was already tested in Section 4.1. Therefore, the goal of this demonstration is just to show, as a proof of concept, the potential applicability of GTN to other non-steel commodity domains (with other users and more recent Twitter data).

The GTN method was then applied (as detailed in Section 4.1) to estimate the country for the set of 71 users. Because the number of users is relatively small, the results are shown in terms of a three-class task that includes the two top countries of Table 2: “USA”, “India”, and “other”. The prediction results are shown in Table 13, in terms of the confusion matrix and individual class measures (the last three rows show $\operatorname { A c c } _ { c } ,$ prediction , and recall ). The obtained results show a very good classification performance for India (17 users, $\mathrm { A c c } _ { \mathrm { I n d i a } } = 9 0 . 1 \% ,$ preci $\mathrm { 3 i o n _ { I n d i a } = 1 0 0 . 0 \% , }$ $\mathrm { r e c a l l _ { I n d i a } } = 7 0 . 8 \% )$ and a reasonable classifi cation for USA (39 users, $\mathrm { A c c } _ { \mathrm { U S A } } { = } 6 7 . 6 \%$ , precision $_ { \mathrm { U S A } } = 5 3 . 8 \% ,$ , re-$\mathrm { c a l l } _ { \mathrm { U S A } } { = } 8 0 . 8 \% )$

Confusion matrix and classification measures for the GTN demonstration ex ample.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Target country</td></tr><tr><td>USA</td><td>India</td><td>Other</td><td>Total</td></tr><tr><td rowspan="7">GTN predictions</td><td>USA</td><td>21</td><td>0</td><td>5</td><td>26</td></tr><tr><td>India</td><td>6</td><td>17</td><td>1</td><td>24</td></tr><tr><td>other</td><td>12</td><td>0</td><td>9</td><td>21</td></tr><tr><td>Total</td><td>39</td><td>17</td><td>15</td><td>71</td></tr><tr><td> $Acc_c =$ </td><td>67.6%</td><td>90.1%</td><td>74.6%</td><td></td></tr><tr><td> $Precision_c =$ </td><td>53.8%</td><td>100.0%</td><td>60.0%</td><td></td></tr><tr><td> $Recall_c =$ </td><td>80.8%</td><td>70.8%</td><td>42.9%</td><td></td></tr></table>

## 5. Discussion and conclusions

With the expansion of the Internet, Web and social media analytics are a key tool of diverse decision support systems. Several of these social media analytic systems require user geographic location data. In this work, we propose a novel GTN approach to detect the most probable Twitter user country of interest when such context is not explicitly known. GTN is a purely word distribution method that does not require training data. It is based on the frequency of users' tweet nouns and GT country word distribution data. The main advantage of the GTN method, with respect to existing geographic dictionary models, is its ability to obtain information from generic and adaptable nouns, dynamically provided by GT, such as “Brexit”, “Trump”, or “cricket”. Moreover, using GT as source, the GTN method is able to benefit from country term frequency or language diferences. Conversely, the GTN has some limitations. For example, as shown in Table $^ { 7 , }$ there are popular generic nouns (e.g., “time” and “year”) that show a similar frequency of use in diferent countries. In addition, GTN assumes just one implicit country of interest, whereas some users might travel or tweet implicitly about more than one country.

Following a design science research methodology [16], we validated GTN empirically. Using a conservative procedure, we created a recent dataset with 3298 Twitter users from 54 countries with 744,830 tweets written in 48 languages. The obtained GTN results are of high quality (83% accuracy and weighted F1-score) and competitive when compared with a state-of-the-art word distribution method [15]. An error analysis was also performed on the GTN misclassifications, revealing diferent types of errors, such as mismatches between diferent anglophone countries (32% of the errors) and between countries that are similar or share a language or location (3%). Several experiments were conducted, using four machine learning classifiers: bagging (BG), random forest (RF), support vector machines (SVM), and a deep learning inspired multilayer perceptron (MLP). The experiments have shown that the GTN errors are dificult to outperform, confirming the value of the GTN responses. One limitation of GTN is its dependency on GT and the required GT request time. As an alternative, we tested the GTN2 approach, in which a machine learning method models the GTN responses. The best results were achieved by the GTN2 MLP model (80% accuracy and 78% weighted F1-score when modeling GTN), which is a much faster method than GTN. Finally, we have demonstrated the applicability of GTN to non-steel commodities (such as cotton), using more recent Twitter data and a diferent but smaller sample of users.

Because the percentage of geotagged tweets is small and Twitter user profile location data is frequently unreliable [12,14], as also shown in this study, the proposed GTN and GTN2 approaches can be valuable to support Web and social media analytic systems. In future work, we intend to apply GTN in real-world applications, such as for filtering country tweets related to a particular commodity price (for example, gold or wheat prices from Germany). In addition, we wish to complement GTN with extra geolocation features, such as friendship networks or user profile metadata, and investigate more fine-grained location levels. Finally, we plan to research whether feature selection filtering methods, such as pointwise mutual information [1], can be used to discard the GTN generic nouns that are used equally by diferent countries, thereby potentially improving the GTN performance. However, we note that such a filtering approach would require a GTN adaptation that involves a training set.

## Acknowledgments

Research carried out with the support of resources of Big and Open Data Innovation Laboratory (BODaI-Lab), University of Brescia, granted by Fondazione Cariplo and Regione Lombardia. The work of P. Cortez was supported by FCT - Fundação para a Ciência e Tecnologia within the Project Scope UID/CEC/00319/2019. We would also like to thank the anonymous reviewers for their helpful suggestions.

## References

[1] N. Oliveira, P. Cortez, N. Areal, Stock market sentiment lexicon acquisition using microblogging data and statistical measures, Decision Support Systems 85 (2016) 62–73, https://doi.org/10.1016/j.dss.2016.02.013 https://doi.org/10.1016/j.dss. 2016.02.013

[2] A. Tumasjan, T.O. Sprenger, P.G. Sandner, I.M. Welpe, Predicting elections with twitter: what 140 characters reveal about political sentiment, ICWSM 10 (1) (2010) 178–185.

[3] H. Rui, Y. Liu, A. Whinston, Whose and what chatter matters? The efect of tweets on movie sales. Decision Support Systems 554 (2013) 863–870

[4] R. Schumaker, A. Jarmoszko, C. Labedz, Predicting wins and spread in the premier league using a sentiment analysis of twitter, Decision Support Systems 88 (2016) 76–84, https://doi.org/10.1016/j.dss.2016.05.010 https://doi.org/10.1016/j.dss. 2016.05.010

[5] J. Ginsberg, M.H. Mohebbi, R.S. Patel, L. Brammer, M.S. Smolinski, L. Brilliant, Detecting influenza epidemics using search engine query data, Nature 457 (7232) (2009) 1012.

[6] H. Choi, H. Varian, Predicting Initial Claims for Unemployment Benefits, Google Inc, 2009, pp. 1–5.

[7] H. Choi, H. Varian, Predicting the present with google trends, Economic Record 88 (s1) (2012) 2–9.

[8] Z. Fang, C.C. Chen, A novel trend surveillance system using the information from web search engines, Decision Support Systems 88 (2016) 85–97, https://doi.org 10.1016/i.dss.2016.06.001https://doi.org/10.1016/i.dss.2016.06.001

[9] D. Wu, Y. Cui, Disaster early warning and damage assessment analysis using social media data and geo-location information, Decision Support Systems 111 (2018) 48–59. https://doi,org/10.1016/i.dss.2018.04.005 https://doi,org/10.1016/i.dss 2018.04.005

[1o], L. Vomfell. W.K. Härdle, S. Lessmann. Improving crime count forecasts using twitter

[11] J. Mahmud, J. Nichols, C. Drews, Home location identification of twitter users, ACM Transactions on Intelligent Systems and Technology (TIST) 53 (2014) 47

[12] Z. Cheng, J. Caverlee, K. Lee, You are where you tweet: a content-based approach to geo-locating twitter users, Proceedings of the 19th ACM International Conference on Information and Knowledge Management. ACM. 2010. pp. 759–768.

[13] F. Morstatter, J. Pfefer, H. Liu, K.M. Carley, Is the sample good enough? Comparing data from twitter's streaming API with twitter's firehose, in: E. Kiciman, N B Ellison B Hogan. P. Resnick L. Soboroff (Eds ) Proceedings of the Seventh International Conference on Weblogs and Social Media, ICWSM 2013, Cambridge, Massachusetts, USA, July 8–11, 2013, The AAAI Press, 2013, http://www.aaai.

[14] B. Hecht, L. Hong, B. Suh, E.H. Chi, Tweets from Justin Bieber's heart: the dynamics of the location field in user profiles. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ACM, 2011, pp. 237–246.

[15] S. Lee, M. Farag, T. Kanan, E.A. Fox, Read between the lines: a machine learning approach for disambiguating the geo-location of tweets, Proceedings of the 15th ACM/IEEE-CS Joint Conference on Digital Libraries. ACM. 2015, pp. 273–274.

[16] D. Arnott. G. Pervan. A critical analysis of decision support systems research revisited: the rise of design science, JIT 29 (4) (2014) 269–293, https://doi.org/10 1057/jit.2014.16 https://doi.org/10.1057/jit.2014.16.

[17] O. Buvukkokten, J. Cho, H. Garcia-Molina, L. Gravano, N. Shivakumar, Exploiting geographical location information of web pages, in: S. Cluet, T. Milo (Eds.), ACM SIGMOD Workshop on The Web and Databases, WebDB 1999, Philadelphia, Pennsylvania, USA, June 3–4, 1999. Informal Proceedings, INRIA, 1999, pp. 91–96

http://www-rocq.inria.fr/%7Ecluet/WEBDB/gravano.ps.

[18] O. Aulov, M. Halem, Human sensor networks for improved modeling of natura disasters, Proceedings of the IEEE 10010, 2012, pp. 2812–2823.

[19] L. Backstrom, E. Sun, C. Marlow, Find me if you can: improving geographical prediction with social and spatial proximity, Proceedings of the 19th Internationa Conference on World Wide Web, ACM, 2010, pp. 61–70.

[20] C.A. Davis Jr., G.L. Pappa, D.R.R. De Oliveira, F.D.L. Arcanjo, Inferring the location of twitter messages based on user relationships, Transactions in GIS 156 (2011) 735–751.

[21] A. Rahimi, T. Cohn, T. Baldwin, Twitter user geolocation using a unified text and network prediction model, arXiv preprint arXiv:1506.08259.

[22] N. Dalvi, R. Kumar, B. Pang, Object matching in tweets with spatial models, Proceedings of the Fifth ACM International Conference on Web Search and Data Mining, ACM, 2012, pp. 43–52.

[23] K. Ryoo, S. Moon, Inferring twitter user locations with 10 km accuracy, Proceedings of the 23rd International Conference on World Wide Web, ACM, 2014, pp. 643–648.

[24] F. Laylavi, A. Rajabifard, M. Kalantari, A multi-element approach to location inference of twitter: a case for emergency response, ISPRS International Journal of Geo-Information 55 (2016) 56.

[25] E. Williams, J. Gray, B. Dixon, Improving geolocation of social media posts, Pervasive and Mobile Computing 36 (2017) 68–79.

[26] D.J. Crandall, L. Backstrom, D. Huttenlocher, J. Kleinberg, Mapping the world's photos, Proceedings of the 18th International Conference on World Wide Web, ACM, 2009, pp. 761–770.

[27] R. Li, S. Wang, H. Deng, R. Wang, K.C.-C. Chang, Towards social user profiling: unified and discriminative influence model for inferring home locations, Proceedings of the 18th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM, 2012, pp. 1023–1031.

[28] A.S. Minot, A. Heier, D. King, O. Simek, N. Stanisha, Searching for twitter posts by location, Proceedings of the 2015 International Conference on the Theory of Information Retrieval. ACM. 2015, pp. 357–360.

[29] A. Rahimi, D. Vu, T. Cohn, T. Baldwin, Exploiting text and network context for geolocation of social media users, arXiv preprint arXiv:1506.04803.

[30] E. Rodrigues, R. Assunção, G.L. Pappa, D. Renno, W. Meira Jr., Exploring multiple evidence to infer users location in twitter, Neurocomputing 171 (2016) 30–38.

[31] Y. Qian, J. Tang, Z. Yang, B. Huang, W. Wei, K.M. Carley, A probabilistic framework for location inference from social media, arXiv preprint arXiv:1702.07281.

[32] S. Kinsella, V. Murdock, N. O'Hare, I'm eating a sandwich in Glasgow: modeling locations with tweets. Proceedings of the 3rd International Workshop on Search and Mining User-Generated Contents, ACM, 2011, pp. 61–68.

[33] H.-W. Chang, D. Lee, M. Eltaher, J. Lee, @ phillies tweeting from philly? Predicting twitter user locations with spatial word usage, in: Proceedings of the 2012 International Conference on Advances in Social Networks Analysis and Mining (ASONAM 2012), IEEE Computer Society, 2012, pp. 111–118.

[34] R. Compton, D. Jurgens, D. Allen, Geotagging one hundred million twitter accounts with total variation minimization, Big Data (Big Data), 2014 IEEE International Conference on, IEEE, 2014, pp. 393–401.

[35] B. Han, P. Cook, T. Baldwin, Text-based twitter user geolocation prediction, Journa of Artificial Intelligence Research 49 (2014) 451–500

[36] S.E. Middleton, L. Middleton, S. Modaferi, Real-time crisis mapping of natural disasters using social media, IEEE Intelligent Systems 292 (2014) 9–17.

[37] D. Kotzias, T. Lappas, D. Gunopulos, Home is where your friends are: utilizing the social graph to locate twitter users in a city. Information Systems 57 (2016) 77–87

[38] J.P. Singh, Y.K. Dwivedi, N.P. Rana, A. Kumar, K.K. Kapoor, Event classification and location prediction from tweets during disasters. Annals of Operations Research (2017) 1–21.

[39] M. Avvenuti, S. Cresci, L. Nizzoli, M. Tesconi, Gsp (geo-semantic-parsing): geo parsing and geotagging with machine learning on top of linked data, European Semantic Web Conference, Springer, 2018, pp. 17–32

[40] A. Rahimi, T. Cohn, T. Baldwin, Semi-supervised user geolocation via graph convolutional networks, arXiv preprint arXiv:1804.08049

[41] I. Witten, E. Frank, M. Hall, C. Pal, Data Mining: Practical Machine Learning Tools and Techniques, 4th edition, Morgan Kaufmann, San Francisco, CA, USA. 2017.

[42] J. Baldridge, The opennlp project, http://opennlp apache. org/index. html, (accessed 2 February 2012).

[43] D. Kahle, H. Wickham, ggmap: spatial visualization with ggplot2., R Journal 5 (1).

[44] I. Feinerer, C. Buchta, W. Geiger, J. Rauch, P. Mair, K. Hornik, The textcat package for n-gram based text categorization in r, Journal of Statistical Software 526 (2013) 1–17.

[45] S. Loria, P. Keen, M. Honnibal, R. Yankovsky, D. Karesh, E. Dempsey, et al., Textblob: simplified text processing, Secondary TextBlob: Simplified Text Processing.

[46] Y. Goldberg, Neural network methods for natural language processing, Synthesis Lectures on Human Language Technologies 10 (1) (2017) 1–309.

[47] A. Ng, Machine Learning Yearning, deeplearning.ai (2018).

[48] T. Hastie, R. Tibshirani, J. Friedman, The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2nd edition, Springer-Verlag, NY, USA, 2008

[49] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (7553) (2015) 436.

[50] L. Breiman, Random forests, Machine Learning 451 (2001) 5–32.

[51] M. Fernández-Delgado, E. Cernadas, S. Barro, D. Amorim, Do we need hundreds of classifiers to solve real world classification problems? The Journal of Machine Learning Research 151 (2014) 3133–3181.

[52] T. Joachims, Text categorization with support vector machines: learning with many relevant features, European Conference on Machine Learning, Springer, 1998, pp. 137–142.

[53] Z. Wang, X. Xue, Multi-class support vector machine, Support Vector Machine Applications, Springer, 2014, pp. 23–48.

[54] C.M. Bishop, Pattern recognition and machine learning, Information Science and Statistics, 5th edition, Springer, 2007, http://www.worldcat.org/oclc 71008143.

[55] I. Goodfellow, Y. Bengio, A. Courville, Deep Learning, 1 MIT press, Cambridge, 2016.

[56] D. Hand, Classifier technology and the illusion of progress, Statistical Science 21 (1) (2006) 1–15.

[57] S. Walczak, N. Cerpa, Heuristic principles for the design of artificial neural net works, Information & Software Technology 41 (2) (1999) 107–117, https://doi.org 10.1016/S0950-5849(98)00116-5.

[58] G.E. Batista, R.C. Prati, M.C. Monard, A study of the behavior of several methods for balancing machine learning training data. ACM SIGKDD explorations newsletter é (1) (2004) 20–29.

[59] M. Hollander, D.A. Wolfe, Nonparametric Statistical Methods, Wiley-Interscience, 1999.

![](/api/attachments/NH7R9BQ5/fulltext/images/5d850429522f7bcd61b6b99824b4f827768918494f0a3c4c54973e0acdaa25df.jpg)  
Paola Zola is a PhD student of Doctoral Program on Analytics for Economic and Business at the University of Brescia, Italy. She holds a Master of Finance and Risk Management and Bachelors degree in Finance at the same University. Her research interests include: natural language processing, social media and data mining, and time series forecasting.

![](/api/attachments/NH7R9BQ5/fulltext/images/f84952a259dd95941e62213b60c0a1ff7a8fead2439bbd7ebc3662dbb527be4f.jpg)

Paulo Cortez (Habilitation, PhD) is an Associate Professor at the Department of Information Systems, University of Minho Portugal He is also assistant director of the ALGORITMI R&D Centre. From 2012 to 2015, he was Vicepresident of the Portuguese Association for Artificial Intelligence (www.appia.pt). Currently, he is an Associate Editor of the journals Decision Support Systems (Elsevier) and Expert Systems (Wiley). His research, within the areas of Decision Support, Data Science, Machine Learning and Modern Optimization, has appeared in Journal of Heuristics, Decision Support Systems, Information Sciences and others (see http://www3.dsi.uminho.pt/pcortez).

![](/api/attachments/NH7R9BQ5/fulltext/images/7a5907016f7a56977db5dd9b46acd9898b8393e6810ea55c788df581f1f7dbb2.jpg)

Maurizio Carpita is a Professor of Statistics and Scientific Director of the DMS StatLab - Data Methods and Systems Statistical Laboratory of the Department of Economics and Management at the University of Brescia. Italy. He is a Co-Editor in chief of the EJASA - Electronic Journal of Applied Statistical Analysis (in Scopus and WoS), and has been an elected member of the Steering Committee 2010–2014 of Italian Statistical Society (SIS). His methodological research interests are descriptive and inferential statistics. latent variable and psychometric models. statistical methods and data mining tools for business intelligence. His studies are in the fields of the analysis of big data from telecom and Internet, assessment of the services quality and job satisfaction, testing of student performances (see www.unibs.

it/ugov/person/2655).
