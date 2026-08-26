---
otero_id: 16320
otero_key: "NPU8GXRE"
title: "Ontological analysis of web surf history to maximize the click-through probability of web advertisements"
authors: "Jason Deane; Praveen Pathak"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.04.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ontological analysis of web surf history to maximize the click-through probability of web advertisements

Jason Deane <sup>a,</sup>⁎, Praveen Pathak <sup>b,1</sup>

<sup>a</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech, Blacksburg, VA 24061, USA

<sup>b</sup> Information Systems and Operations Management Department, Warrington College of Business Administration, University of Florida, Gainesville, FL 32611-7169, USA

## a r t i c l e i n f o

Article history: Received 27 February 2007 Received in revised form 6 March 2009 Accepted 2 April 2009 Available online 8 April 2009

Keywords: Information retrieval Advertisement targeting Online advertisement

## a b s t r a c t

Due to an enormous in<sup>fl</sup>ux of capital over the past decade, the online advertising industry has become extremely robust and competitive. The difference between success and failure in such a competitive market often rests in the ability to deliver advertisements that are closely in line with a user's interests. In this work, we propose and test a new online advertisement targeting technique which adapts and utilizes several powerful and well tested information retrieval and lexical techniques to develop an estimate of a user's af<sup>fi</sup>nity for particular products and services based on an analysis of a user's web sur<sup>fi</sup>ng behavior. This new online ad targeting technique performs extremely well in our empirical tests

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

It is estimated that online advertisement revenues for the US alone will grow to \$18.9 billion by 2010 [29]. Motivated by this upward trend in Internet advertising demand, many companies (e.g., Google, Yahoo, AOL, WSJ, etc.) have adopted a business model which is heavily dependent upon the revenue stream generated from their online advertisement publishing activities [10]. Although the business process has many similarities with ad publishing in traditional media settings, the online environment, primarily due to its transactional transparency, offers some very unique opportunities and challenges. This online transparency leads to an enormous amount of customer data which continues to drive the popularity and the importance of ad targeting [17]. According to Kessler and Acoido of the USA Today, “Microsoft is one of many companies collecting and aggregating data in new ways so sophisticated that many customers may not even realize that they're being watched.” It is acknowledged that a user's web surf history is and will be a very important component of this ad targeting process, but to date the research community has not provided a clear and dominant way to utilize this data. The extant literature has instead focused primarily on the utilization of demographic data. In this work, we propose and test an online ad targeting technique which is based upon the analysis of a user's web sur<sup>fi</sup>ng habits. This technique shows great promise and can be used to complement other tools and in doing so offer an opportunity for online ad publishers to improve the ef<sup>fi</sup>ciency and effectiveness of their online ad scheduling process, thereby enhancing their revenue generation ability.

The paper is organized as follows. Section 2 provides some background information with respect to the online advertising industry and discusses the relevant literature. Section 3 provides an introduction to information retrieval, structural representation and lexical reference systems. Section 4 introduces and discusses in detail the proposed Ontological Analysis of Web Surf History (OAWSH) Model. Section 5 provides the results of our model tests. And lastly, Section 6 provides conclusion and projected areas of future related research.

## 2. Background

There are three primary participants in the online advertising process. At the top of the chain is the Advertiser. This is a company that enters into an agreement with a publisher in order to enlist the publisher's assistance in the serving of their online advertisements. The associated ads are delivered to users of the publisher's Web pages. The Publisher is a company that expends resources in an effort to publish online advertisements in order to generate revenue. The Customer/User is the individual who browses Web pages and is exposed to advertisements to which they may or may not respond. In its infancy, the online advertisement publishing industry adopted the CPM (cost per mille) pricing model which was developed by and is very popular in the traditional print and television media industries. The payment structure of the CPM model is based solely on the number of ad impressions served. The publisher is paid a set fee for each ad impression which is served to a user, regardless of its effectiveness. Under this model, the <sup>fi</sup>nancial reward mechanism motivates the publisher to focus primarily on only one thing; serving as many ad impressions as possible. Eager to improve their marketing ROI, it didn't take long for advertisers to question the appropriateness of this model.

In the print and television mediums, unlike the online medium, it is very dif<sup>fi</sup>cult to determine the effectiveness of a particular advertisement; therefore, the CPM model, from a risk sharing/motivational stand point, seems to make sense. However, this is not the case within the online setting. In the online medium, immediate post-ad exposure behavior by the user is often easily tracked. For instance, the advertiser and the publisher can normally tell instantaneously if the user clicks on the advertisement, sets up an account with the advertiser, makes a purchase from the advertiser, etc. This behavioral transparency has led many advertisers to question the ef<sup>fi</sup>cacy of application of the CPM pricing model for the online industry. The belief of many is that, based on the more open, bidirectional <sup>fl</sup>ow of information, it may be in everyone's best interest to instead have pricing directly tied to one or more of these user behaviors. As a result, several performance based pricing models such as CPC (cost per click), CPS (cost per sale) and CPA (cost per acquisition) have been developed and are extremely popular. These models are generally considered to provide a more equitable risk sharing relationship. In an effort to maximize the utilization of their most precious resource, advertising space, publishers must still attempt to serve as many ads as possible, but in addition they must now make a concerted effort to do it intelligently. This is very appealing to the advertisers, and has caused the popularity of performance based pricing models to increase substantially. As a result, publishers are now commonly faced with a much more challenging problem than they had faced in the recent past.

As a result of the migration towards performance based pricing models, many publishers now <sup>fi</sup>nd that a large portion of their revenue stream is dictated by the actions of the users. Accordingly, in an effort to maximize revenue, they are eager to increase the probability of occurrence of these targeted actions/behaviors (click, purchase, account set up, etc.). We assume that there is a direct relationship between the likelihood of a user taking action with respect to a particular advertisement and their level of interest for the given good or service which is being advertised. Based on this assumption, the obvious solution would be for publishers to serve users only advertisements for products and services for which they have sincere interest. Not surprisingly, this is easier said than done. It is worth noting that an advertiser's main concern is the conversion rate or the rate with which users ultimately make a purchase based on their exposure of the advertisement. Depending on the chosen pricing mechanism, this may or may not be a major concern for the ad publisher, but regardless if a performance based measure is used, the publisher must make every attempt to deliver ads that are of interest to the respective user.

Unfortunately for publishers, estimating a user's af<sup>fi</sup>nity for certain products and services can be a very challenging and controversial task. It is safe to assume that users and publishers have a common interest in that most users would also prefer to be exposed to ads for products and services for which they have an interest than to those that they do not. The real challenge comes in getting from point A to point B. How does a publisher gain an understanding of a user's interests? Extant literature in this area falls under the umbrella of personalization [20]. Personalization consists of three broad stages: 1. consumer preferences learning [34], 2. matching consumers with an appropriate offering, and 3. evaluation of such a matching process. Typically the literature on personalized advertisements has focused on segmenting consumers. A logit model was used by Bhatnagar et al. [3] to segment customers using their search behavior to present personalized advertisements. Raghu et al. [23] presented a model that dynamically pro<sup>fi</sup>les consumers' preferences using the theory of questionnaires. Using simulation they showed that information acquisition and search processes show a nonlinear behavior in information gained. Shahabi et al. [27] developed a distributed user tracking approach for accurate scalable, and implicit collection of data. In the speci<sup>fi</sup>c area of advertisement targeting, users' click streams have been used. Such clickthroughs capture users internet browsing habits in terms of keywords used for search, URL's clicked, time spent on a web page, geographical location of the user, user's browser and so on. Chatterjee et al. [7] used click stream data to develop an analytical approach to modeling consumer response to banner advertisement. They showed that the effect of repeated exposure to a particular banner advertisement is negative and non linear. Karuga et al. [16] developed an algorithm for customizing advertisements by changing content, copy, placement, animation, and other attributes. They used conjoint analysis and genetic algorithms for optimization. Xu et al. [32] develop Bayesian networks based on consumer survey results in an effort to develop personalized mobile advertisements. Langheinrich et al. [18] assume that every customer has recently entered search keyword(s) into a search engine and that the publisher has access to this list of keywords. They propose a simple iterative method to estimate the probability of click through $c _ { i j }$ for each ad/keyword pair based on historical click behavior. This is a very appealing approach, but unfortunately very few publishers have access to the necessary keyword data and it becomes extremely computationally complex as the number of ads and keywords grows. Chickering [8] proposes a system which maximizes the click-through rate given only advertisement frequency quotas. Instead of using keywords, they partition the ad slots into “predictive segments or clusters”. Each cluster/ad combination has an associated probability of click through. This is a very promising technique assuming that the keyword data is available.

In most of these studies the customers are treated as belonging to a segment and personalization involves personalizing advertisements for that customer segment. In cases where attempts have been made to personalize for an individual customer, click-through data such as audience segment, geography, browser type, operating system, and search keywords have been used. We propose a technique that is not constrained by the necessity of search keyword data. Our technique could either be used in conjunction with these techniques, if keyword data is available or in its place of it if it is not.

In all of these methods, privacy is a very sensitive subject that must be addressed with extreme caution. Users are very protective of their privacy and the ef<sup>fi</sup>ciency of their Web sur<sup>fi</sup>ng experience. Any effort on the part of a publisher which violates either without permission is very likely to have a depressing effect on corporate sentiment which may directly impact long term corporate revenue. Fortunately, despite their privacy concerns, users routinely grant the right to have their online behaviors tracked. This may seem somewhat surprising and the justi<sup>fi</sup>cation is often not straightforward. Many claim that it is primarily because users are not willing to take time to read the often lengthy ‘rights, rules and regulations’ agreements before they accept them. Others argue that users are instead knowledgeable and accepting of the potential research and application bene<sup>fi</sup>ts of taking such a step. Regardless of which of these opinions is closest to the truth, the resulting data can be extremely bene<sup>fi</sup>cial. As part of this research, we propose a framework to analyze the resulting raw html from a customer's recent click history using WordNet, a lexical database, and several information retrieval techniques. In doing so we are able to develop a characteristic array of interests for each user that otherwise would be very dif<sup>fi</sup>cult if not impossible to attain. This array is then used to develop an ad targeting strategy for each user. The basic intuition is that by analyzing a user's recent browsing history, we can improve our understanding of their current hobbies and interests.

Another closely related technique, content based ad targeting, is extremely popular in industry. In content based ad targeting, companies attempt to cluster users into a small number of buckets based on the content of the web pages they visit. As an example, the Wall Street Journal, based on sur<sup>fi</sup>ng habits, clusters their users into one of the following nine categories: car buffs, consumer techies, engaged investors, entrepreneurs, health nuts, the leisure-minded, mutual fund a<sup>fi</sup>cionados, opinion leaders and travel seekers. Once clustered, ads are then targeted to the users based on this categorization. The technique we propose is similar in that it also attempts to analyze and leverage a user's sur<sup>fi</sup>ng behavior; however, our technique is much more detailed in that it is based on a thorough analysis of the lexical content of a visited page instead of just the category to which that page has been assigned. In addition, the assignment of advertisements is performed on a per user basis instead of utilizing the clustering technique. To the best of our knowledge, no one else has speci<sup>fi</sup>cally recommended or tested this type of approach. Our goal is to provide those in industry with a viable alternative with which to address this dif<sup>fi</sup>cult challenge. Next, we provide a basic introduction to information retrieval, structural representation and WordNet, each of which is an important component of our model.

## 3. Information retrieval introduction

Information retrieval (IR) is an area of research which attempts to extract usable information from textual data [11]. IR has historically been employed in the <sup>fi</sup>eld of library sciences, but it has recently gained favor in many other <sup>fi</sup>elds including Internet search, cyber security and medicine [15]. The power of IR is its ability to handle textual information. IR has been applied in many domains, including document sorting, document retrieval, inference development and query response. We use IR techniques to leverage the textual representation of a user's html Web sur<sup>fi</sup>ng history in the creation of a weighted characteristic array for each user which, within the model, represents the user's current interests. We then create a similar array for each advertisement within the corpus and use a similarity measure to strategically create a schedule of user–advertisement assignments. By assigning ads based on the user–ad af<sup>fi</sup>nities, this should intuitively maximize the likelihood that a user will follow through and click on the ad. Next, we brie<sup>fl</sup>y introduce one of the most widely used techniques within IR, the vector space model.

## 3.1. Vector space model

A primary goal of traditional information retrieval is to select, from a corpus of documents, the subset which is most relevant to a user's stated topics of interest or query. A very powerful and popular method for achieving this task is the vector space model introduced by G. Salton in 1968 [25,26]. The process begins by transforming the documents and the query into a series of vectors, one vector for each document and one for the query. These vectors are then normalized and fed into a similarity measure to determine the relevance of each document. The power of this process is rooted in its ability to transform the textual aspects of the documents and queries into a series of quantitative representations. The vector space model is a theoretically well-grounded model which is easily interpreted based on its geometric properties. Initially a corpus of ‘n’ key terms is created based on the contents of the documents and the query. Subsequently for each document and the query, a weight is assigned for every term that appears in this corpus (this weight assignment process is very important and is therefore discussed in much more detail in the following section). This allows for each document and query to be represented as a vector of key term weights in n dimensional space. A query $q _ { j }$ and a document $d _ { k }$ would be represented as:

$$
\begin{array}{l} \vec {q _ {j}} = (w _ {1, j}, w _ {2, j},..., w _ {n, j}) \\ \vec {d _ {k}} = (w _ {1, k}, w _ {2, k},..., w _ {n, k}) \end{array}
$$

where n is the total number of terms in the collection and $w _ { i , k }$ represents the weight which is assigned to the term i for document k. Next, the vector space model evaluates the relative importance of document $d _ { k }$ to query $q _ { j }$ based on the degree of similarity between the two corresponding n dimensional vectors, $\overrightarrow { q _ { j } }$ and $\vec { d _ { k } } \left[ 2 4 \right]$ . There are a number of different ways to measure this similarity, but one simple, well-grounded similarity measure is the dot product of the two vectors. This technique gives the cosine of the angle θ between the vectors (see Fig. 1), and can be computed as follows:

![](/api/attachments/NPU8GXRE/fulltext/images/907b5bb8d7f95a8cdf84d3d2435d16410b54e55224091acae49656d7d1e3e244.jpg)  
Fig. 1. Geometric representation of the VSM.

$$
\operatorname{sim} \left(q _ {j}, d _ {k}\right) = \frac {\sum_ {i = 1} ^ {n} w _ {i , j} w _ {i , k}}{\sqrt {\sum_ {i = 1} ^ {n} \left(w _ {i , j}\right) ^ {2}} \sqrt {\sum_ {i = 1} ^ {n} \left(w _ {i , k}\right) ^ {2}}}.\tag{1}
$$

The chosen similarity score, also called the retrieval status value (RSV) is calculated for each document query combination and is used to rank the documents. A document's RSV score is used as a proxy measure of its relevance for a given query. The documents are ranked based on their RSV score and served to the user in descending order.

One of the most important steps in the vector space model is <sup>fi</sup>nding a good set of index term weights, w . The index term weights are responsible for providing an accurate estimation of the relative importance of the keywords within the collection. Without a good set of index term weights, the VSM looses its effectiveness very quickly. In their seminal work on this problem, Sparck Jones [28] introduced the TF–IDF function which is still the most widely used, and is considered by many to be the most useful, index weighting function. Although many content based features are available within the vector space model that may be used to compute the index term weights, the two that are most common, and the ones that are used in the TF–IDF function are the term frequency (tf) and the inverse document frequency (idf). The basic TF–IDF function is as follows: $w _ { i j } = ( t f ) _ { i j } { ^ { * } }$ log $\cdot \frac { N } { d f } .$ The term frequency, $t f _ { i j } ,$ is calculated by counting the frequency of occurrence of term i in document j. The larger the tf, the more important the term is considered to be in describing the document or query. The inverse document frequency is calculated as $( i d f ) _ { i j } = \log { \frac { N } { d f } }$ where N represents the total number of documents in the collection and $d f$ represents the total number of documents within which term j appears. The basic intuition behind the idf is that a keyword which appears in very few documents is likely to be of greater value in classifying those documents than would be a keyword which appears in all of the documents. The idf scores are assigned accordingly. The keyword which appears in every document is assigned an idf score of 0 while a keyword appearing in very few documents would receive a much higher idf score. By combining the two, the TF–IDF function gives the greatest weight to terms which occur with high frequency within a very small number of documents. We followed the common IR practice of removing stop words prior to our analysis. Stop words are those commonly occurring words that are of very limited informational value such as the, a, it, is, etc.

Although many ranking methods have been proposed as alternatives to VSM the general consensus is that VSM is as good as or better than all of its competitors [33]. Although no method has been able to take its place, several attempts to improve the basic vector space model are gaining in popularity. Two of these efforts which are of particular interest involve the inclusion of structural and lexical information within the model.

![](/api/attachments/NPU8GXRE/fulltext/images/d472f2d689c115fecc819f173e5af98e804db18ecae40765e7ee976abe546fef.jpg)  
Fig. 2. Process <sup>fl</sup>ow diagram of the OAWSH model.

## 3.2. Structural representation

The traditional VSM considers each document as a simple ‘bag of words’ leveraging only the resulting textual representation. This method has proven to be very useful and effective, but many researchers including Halasaz [14] hypothesized that there might be additional information which is overlooked by the basic VSM. This additional information is found in the basic structure of the document. The fundamental idea is that the ‘location’ in a document where a term appears may provide additional information as to how valuable that term may be in developing a characteristic representational vector for the document. Consider the basic structure of an HTML document as an example. An HTML document commonly consists of a series of independent sections such as the header, keywords, title, body, anchor, and abstract. From a structural representation point of view, a term which appears in the header might be more important than one which appears in the anchor. Alternatively, a term which appears in the body and in the anchor may be more important than one which just appears in the title. A number of researchers, including Navarro and Yates [21,22] and Burkowski [5], have developed alternative models which incorporate document structure into the term relevance calculation. Although many of these methods are criticized as being somewhat narrowly focused and lacking in generalizability, the general consensus acknowledges that this structural representation de<sup>fi</sup>nitely contains important information and should therefore be considered. Accordingly, we incorporate this type of information within our research model by assigning different weights to different sections of the html document as is described in Section 4.0.

## 3.3. WordNet

In the previous section, we describe the potential value of including structural information within the VSM model. Similarly, lexical information may also be very useful. The primary goal of a lexical reference system is to provide its users with word relationships. One such system which incorporates lexical analysis is WordNet. “WordNet is an online lexical reference system whose design is inspired by current psycholinguistic theories of human lexical memory. English nouns, verbs, adjectives and adverbs are organized into synonym sets, each representing one underlying lexical concept. Different relations link the synonym sets [35].” The most basic semantic relation upon which WordNet is built is the synonym [12]. Synsets, or sets of synonyms, form the basic building blocks for the system. For example, hat is included in the same synset (also called concepts within this work) with lid and chapeau. The current version of WordNet, version 2.1, includes 117,597 synsets [35]. Recently, lexical reference systems have been used within information retrieval for many different purposes including word sense disambiguation [1,2,31], and semantic tagging [9,19]; however, the use that is most pertinent to our research involves text selection. Many researchers, including Vorhees and Hou [30] and Gonzalo et al. [13], have shown that the text selection process can be vastly improved by utilizing a lexical reference system such as WordNet to enhance the process of developing a vector representation for documents and queries. We pool synonyms together into their respective ‘concepts’ instead of treating them independently. Researchers have shown that this process of combining synonyms enhances the performance of the traditional vector space model. This is accomplished by expanding the keyword indexing space to include synsets instead of being limited to just the terms. We follow this intuition within our model. Fellbaum [12] provides a much more thorough review of the system.

## 4. The ontological analysis of web surf history (OAWSH) model

The OAWSH model is based on an adapted VSM which incorporates lexical and structural information. To the best of our knowledge, this approach has never been considered for the online ad targeting problem. We are optimistic that the combination of these proven IR techniques will result in a powerful ad targeting model. We begin by giving a basic outline and process <sup>fl</sup>ow diagram of the model (refer to Fig. 2), and then provide a more thorough discussion of each step. In addition, for a very basic example, please refer to Appendix C.

The basic steps of the process are as follows:

1. Track a user's sur<sup>fi</sup>ng behavior for a predetermined period of time

2. Collect the corresponding html pages

3. Develop a characteristic array for the user by parsing their respective html pages using IR and lexical-based techniques

4. Develop a characteristic array for each advertisement

5. Using a similarity measure, <sup>fi</sup>nd the best ads to be served to the user

6. Serve a set of ads consisting of recommended and non-recommended ones and measure the effectiveness of the model.

4.1. Steps 1 & 2: tracking a user's surfing behavior and collecting HTML pages

We tracked the sur<sup>fi</sup>ng behavior of 68 students for a period of at least 2 h and captured their respective html <sup>fi</sup>les accordingly. The participants were instructed to upload a piece of tracking software to a computer that they would have sole access to over the following one week period. They were then asked to utilize the computer as they normally would. At the end of the week, each student forwarded the resulting log <sup>fi</sup>le which provided details of their web sur<sup>fi</sup>ng behavior in the form of a list of visited urls. 14 of the students failed to follow the instructions in one way or another, leaving us with 54 ‘users’ for the project. Students were chosen as the ‘users’ for this project based on their willingness to participate. They were offered extra credit in the courses taught by the researchers. One obvious concern is that the research project participants may have adapted their sur<sup>fi</sup>ng behavior as a result of the tracking software, but unfortunately in respect of their privacy we felt that being open and honest concerning the project was the only option. And although certain students may have curtailed their visitation of certain adult natured sites as a result of our visibility, we are very optimistic that other sur<sup>fi</sup>ng behavior was unaffected.

## 4.2. Steps 3 & 4: develop a characteristic array for each user and each advertisement

Developing a characteristic array for each user is a three step process. Due to the large volume of data, scripts written in PERL (Practical Extraction and Report Language) were used to automate each of these steps. First, we parse the set of html pages for a given user into a term vector. Second, we determine the relative importance of each term with respect to developing a characterization of the user's interests through their chosen html pages. To determine the relative term importance, we develop a model which is a variation of the basic model set forth by Cecchini [6] which incorporates the use of the vector space model and WordNet concepts.

## Model notation:

$w _ { i , u }$ the importance of term i on domain u

$s _ { z }$ weight factor assigned to structural element z

$t f _ { i , z , d }$ the frequency of term i in structural element z in document d $d l _ { d }$ the document length (total number of terms) of document d $N$ the number of html documents which are present in a user's domain u

$d f _ { i }$ the total number of documents within which term i appears $T$ total number of terms within a concept c

|c| the cardinality of concept c

Eq. (2), which calculates an estimate of the relative weight of each term i in user domain u, is composed of two distinct parts. It is to be noted that a user's domain u consists of all of the terms that were present in the set of html pages that are collected for that particular user.

$$
w _ {i, u} = \left. \left(\sum_ {d} \left(\frac {\sum_ {z} s _ {z} (t f _ {i , z , d})}{d l _ {d}}\right)\right) \left(\frac {d f _ {i}}{N}\right). \right.\tag{2}
$$

The <sup>fi</sup>rst part of Eq. (2) is a weighted term frequency calculation which is normalized by the document length and which incorporates an $s _ { z }$ term into the weight function. The $s _ { z } \mathrm { t e r m } , 0 { \le } s _ { z } { \le } 1$ , represents the relative weight which is assigned to structural element z of the html documents. This term allows us to employ structural analysis, as recommended by several researchers including Navarro and Yates [21,22] and Burkowski [5]. The primary structural elements of the associated html documents that are considered in our analysis are the keywords, body and title sections. Each of these sections is easily identi<sup>fi</sup>ed by its start and stop tags. The basic intuition behind structural analysis is that the terms found in one part of the document may hold more information than those which are found in other sections. For a particular weighting scheme the assignment of a higher weight to a particular section follows from an underlying assumption that the associated section will produce concepts which are of higher informational value than the alternative sections. For example in scheme 2 from Table 1, the keywords section is assigned the largest weight of .7; therefore, it receives considerably more prominence than the title and body sections. We test several different weighting schemes within our analysis, in an attempt to identify the best weighting combination. The tested weighted schemes are detailed in Table 1 below. Although it was not extremely prevalent, we did <sup>fi</sup>nd that a small percentage of the html documents did not have a keywords section. As a result we have provided a contingent weighting distribution for each of the schemes which overrides the original scheme in this situation.

Table 1 Structural element weighting schemes.

<table><tr><td></td><td>Title</td><td>Body</td><td>Keywords</td></tr><tr><td>Scheme 1</td><td>0.3</td><td>0.2</td><td>0.5</td></tr><tr><td>Scheme 1 if no KW section</td><td>0.7</td><td>0.3</td><td>0</td></tr><tr><td>Scheme 2</td><td>0.2</td><td>0.1</td><td>0.7</td></tr><tr><td>Scheme 2 if no KW section</td><td>0.7</td><td>0.3</td><td>0</td></tr><tr><td>Scheme 3</td><td>0.25</td><td>0.5</td><td>0.25</td></tr><tr><td>Scheme 3 if no KW section</td><td>0.3</td><td>0.7</td><td>0</td></tr></table>

Unlike the traditional IR task of separating documents based on their individual representations, we are instead attempting to develop one representation for the entire set of documents for a given user u. Given this objective, a term which appears in many of the documents is anticipated to have greater informative power than one which only appears in a small number of documents. This is the motivation behind the second term of Eq. (2), dfi . In Eq. (3), we generalize our term representation scheme by introducing the notion of concepts, c. Each concept, c, represents a synset and is composed of the $\{ i _ { 1 } ,$ i<sub>2</sub>,…, i } terms that make up that synset. Recall from our discussion of WordNet that a synset is composed of the chosen term and all of its synonyms. Considering concepts allows us to avoid over or under estimating the importance of a particular term by aligning it with its synonyms. Eq. (3) provides a concept weight by summing the weights for all terms i in the synset c.

$$
w _ {c, u} = \sum_ {i \in c} w _ {i, u}.\tag{3}
$$

In some cases, the same term may appear in more than one concept. We adopt a method introduced by Sacaleanu and Buitelaar [4] in Eq. (4) to facilitate the assignment of the term to one of the concepts in this situation. Eq. (4) includes an additional term <sup>T</sup> where c T is the total number of terms within a concept c and |c| is the cardinality of the concept.

$$
w _ {c, u} ^ {*} = \sum_ {i \in c} w _ {i, u} \frac {T}{| c |}.\tag{4}
$$

The term is assigned to the concept with the highest score from Eq. (4). This functional analysis will result in the interests of each user u being represented as:

$$
\overrightarrow {U _ {c , u}} = \left(w _ {1, u}, w _ {2, u},..., w _ {n, u}\right)
$$

where n is the total number of concepts in the domain of user u and $w _ { c , u }$ represents the weight which is assigned to concept c for user u.

The last step in this stage of the process is to develop a similar vector representation for each advertisement. This was completed semi-manually. First, we manually, based on our knowledge of the product or service, assigned descriptive terms to each advertisement. Terms, based on their perceived relative importance, may show up more than once in the descriptive arrays. Please see Appendix B for a representative sample list of the ads and their respective characteristic arrays.<sup>2</sup> Developing very good descriptive arrays for the advertisements is very important; therefore in practice we recommend that these keywords be provided by a marketing expert from the company whose product or service is being advertised. Next, WordNet was used to develop a concept representation for each of the advertisements. Finally, we assigned a relative importance weight to each concept for a given advertisement. This weight will represent the relative importance of that concept in describing the given advertised product or service. This process resulted in each advertisement being represented as:

$$
\overrightarrow {A _ {c , j}} = \left(w _ {1, j}, w _ {2, j}, \dots , w _ {n, j}\right)
$$

where n is the total number of concepts in the domain of advertisement j and $w _ { c , j }$ represents the weight which is assigned to concept c for advertisement j. Although manual development of vector representations is not uncommon, and in some cases offers improved accuracy, it is not the most ef<sup>fi</sup>cient [33]. It works well for our research, but it may not be a feasible alternative in a large scale operation; therefore, one extension to our work may be to attempt to automate this process for advertisements.

4.3. Step 5: using a chosen similarity measure, evaluate each ad/user combination

The goal of this model is to rate advertisements on their likelihood of being of interest to a particular user. We estimate this series of likelihoods based on the similarities of the respective user and advertisement vector representations via the vector space model [25,26]. Recall from Section 3.1 that the vector space model estimates the similarity between two n dimensional normalized vectors based on the size of the angle θ which separates them in n dimensional space. The measure θ is calculated by taking the dot product of the two vectors. In order for us to apply a similar technique, we <sup>fi</sup>rst need to adapt our advertisement vectors $\overrightarrow { A _ { c , j } }$ to include a term for each concept which is present in the user's domain space u. This is accomplished as follows:

$$
A _ {c, j} = \left\{ \begin{array}{l} w _ {c, j} \text {   if   concept   } c \text {   is   present   in   user   } j ^ {\prime} s \text {   domain   space   } u \\ 0 \text {   otherwise } \end{array} \right\} \text { for   } c = 1,..., n
$$

where n is the number of concepts in the domain space u of the user. Given the two n dimensional vectors $\overrightarrow { U _ { c , u } }$ and $\overrightarrow { A _ { c , k } }$ , we calculate their similarity as follows:

$$
\operatorname{sim} \left(\overrightarrow {U _ {c , u}}, \overrightarrow {A _ {c , k}}\right) = \frac {\sum_ {c = 1} ^ {n} w _ {c , u} w _ {c , k}}{\sqrt {\sum_ {c = 1} ^ {n} \left(w _ {c , u}\right) ^ {2}} \sqrt {\sum_ {c = 1} ^ {n} \left(w _ {c , k}\right) ^ {2}}}.\tag{5}
$$

This similarity score, also called the retrieval status value (RSV) is calculated for each ad/user combination and is used to rank the advertisements. An advertisement's RSV score is used as a proxy measure of its relevance for a particular user, the higher the score, the greater is the presumed relevance.

4.4. Step 6: serve the ads accordingly and measure the effectiveness of the model

The last phase of this part of our project is to evaluate the effectiveness of the model. We created a corpus of advertisements consisting of 100 arbitrarily chosen ads (for a partial list of the products and services which are represented by this corpus of advertisements please see Appendix B). From this corpus, each user was provided with a set of advertisements and asked to rate, on a scale of 1 to 5, their level of interest in the respective product or service, using the following scale:

Product/Service Ranking Scale

1- No interest

2- Little interest

3- Moderate interest

4- High interest

5- Very high interest.

Of the advertisements which were served to a given user, one subset was chosen randomly (20 ads), while the remaining ads, 20 for each scheme, were selected based on the similarity ranking functions described in Table 1 (the top 20% of ads for each weighting scheme were selected). The number of overlapping ads between categories differed considerably from user to user. Not surprisingly, there was noticeably more overlap between the different weighting schemes than there was with the randomly selected ads. Any ad which appeared in more than one category was only served once and its resulting rating contributed to the overall score of all of the categories within which it appeared.

Hypothesis. The IR based ad selection method will be more effective than the commonly used random model in selecting targeted ads from a given advertisement corpus with respect to the overall level of interest of the user base.

We manually analyzed the raw code from a sample of the user's html documents in an effort to develop a good set of initial structural weighting schemes. Results of the experiments and tests of the hypothesis are presented in the next section.

## 5. Results

In this section, we report the results of the experimental analysis of the proposed model. Each user was asked to rank their level of interest on a scale of 1 to 5 for a set of ads, some of which were selected randomly and the remainder of which was selected based on one of the three weighting schemes. As discussed in Section 4.0, within the framework of our ad targeting process, we tested three different weighting schemes in an effort to identify the best html structural element weighting combination. The tested schemes are detailed in Table 1.

The relative effectiveness of each of the advertisement selection methods was determined based on the mean score of the user rankings for the associated set of ads. Since the underlying structure of the ranking scale is such that a higher score indicates an increased level of interest, we are assuming that a method which selects a group of ads which have a higher mean user ranking score is more effective than the alternative. Throughout this section, we use the unpaired ttest to evaluate the statistical signi<sup>fi</sup>cance of the difference in means of user rankings between sets of selected ads. An important assumption of the t-test is that the dependent variable is normally distributed. In our analysis the student rankings represents the dependent variable and based on the results of the Q–Q plot in Fig. 3 this assumption has been met. In addition, utilization of the t-test requires a careful analysis of the respective variances of the compared data sets. We utilized Levene's test of equal variances with a signi<sup>fi</sup>cance level of .05 for this part of the analysis. If the signi<sup>fi</sup>cance level of the Levene's test is greater than or equal to .05, the ‘equal variances assumed’ row of the table is applicable; otherwise, the ‘equal variances not assumed’ row must be used to determine the signi<sup>fi</sup>cance of the associated t-test. In the essence of space, we have presented summarized t-test data within the paper, but for a sample version of the entire t-test table, please see Appendix A.

Normal Q-Q Plot of Student Rating  
![](/api/attachments/NPU8GXRE/fulltext/images/32d58c4607454f2ee751dbcbd985bdbc6254005a42391114471bc2645cbce70a.jpg)  
Fig. 3. Q–Q plot of student response values

We <sup>fi</sup>rst compare the effectiveness of the proposed IR based targeting method with a random selection process. The output of the IR Based Ad Targeting model is a set of weights/scores, one of which is assigned to each advertisement in the corpus. Based on the model design, a higher weight implies a greater <sup>fi</sup>t between the given product and the interests of the respective user; therefore, the ads are served to a given user in descending order of their weight/score. We acknowledge that depending on the size of a publisher's ad corpus and the length of sur<sup>fi</sup>ng time for a particular user, the percentage of ads which may be served to a user will vary; however, for this part of our experiment we assume that each user is served exactly 20% of our advertisement corpus which consists of 100 ads. Based on this assumption, the student rankings for the top 20 ads selected by each of the IR methods (one set for each weighting scheme) are compared with the rankings for 20 randomly selected ads. Table 2 provides a summary of the mean student rank values for each of the ad selection methods. The detailed t-test results for this analysis can be found in Table 3.

From these results, it is clear that the mean student rankings from each of the three weighting schemes is greater than the mean rankings of randomly served ads, at a signi<sup>fi</sup>cance level of .039 or less in each case. This provides strong support for our hypothesis. We certainly would have liked for the differential to have been a little higher, but given that the research participants were not actively involved in shopping behavior, we are very excited with the results. To further evaluate the effectiveness of the IR based ad targeting method, we subdivided the set of ads into groups of 20 based on the relative weight/score which was assigned by the IR based process. The top 20 ads were assigned an id of 5. The next 20 highest ranked ads were assigned an id of 4, and so on, with the lowest 20 ranked ads being assigned an id of 1. Table 4 provides a summary of the mean values of each weighting scheme/ad subset, and the detailed t-test results for this analysis, which compares the mean ranking in each category with the ranking in the top category (ad group 5) for each of the weighting schemes, can be found in Table 5.

Table 2  
Summary of mean student rankings for the 4 selection methods

<table><tr><td>Ad selection method</td><td>Mean student ranking</td></tr><tr><td>IR based method with weighting scheme 2</td><td>2.71</td></tr><tr><td>IR based method with weighting scheme 1</td><td>2.69</td></tr><tr><td>IR based method with weighting scheme 3</td><td>2.63</td></tr><tr><td>Random selection method</td><td>2.50</td></tr></table>

Table 3  
t-test results of the IR model.

<table><tr><td>Tested scheme</td><td>t value</td><td>Significance (2-tailed)</td></tr><tr><td>1</td><td>2.954</td><td>0.003</td></tr><tr><td>2</td><td>3.252</td><td>0.001</td></tr><tr><td>3</td><td>2.062</td><td>0.039</td></tr></table>

Table 4  
Summary of mean student rankings for the three weighting schemes.

<table><tr><td rowspan="2">Ad group</td><td>Scheme 1</td><td>Scheme 2</td><td>Scheme 3</td></tr><tr><td>Mean student ranking</td><td>Mean student ranking</td><td>Mean student ranking</td></tr><tr><td>Top 20 ads</td><td>2.69</td><td>2.71</td><td>2.63</td></tr><tr><td>Ads 21–40</td><td>2.54</td><td>2.52</td><td>2.64</td></tr><tr><td>Ads 41–60</td><td>2.37</td><td>2.29</td><td>2.38</td></tr><tr><td>Ads 61–80</td><td>2.38</td><td>2.40</td><td>2.32</td></tr><tr><td>Bottom 20 ads</td><td>1.99</td><td>2.01</td><td>2.09</td></tr></table>

The purpose of this part of the analysis is to determine, within each weighting scheme, whether the IR ad targeting methodology is successful in segmenting the corpus of ads into groups which have statistically signi<sup>fi</sup>cant differences in their mean rankings. If the methodology was ineffective, we would expect to see mean student rankings which are essentially the same for the top 20 ads, the next 20 ads, and so forth. But from Table 5 it is clear that from top to bottom for each of the three weighting schemes our method does a very good job of segmenting the ads with top 20 being the most effective and so on. These results are also very promising. The proposed model requires the development of a characteristic array for each user/advertising context. As is discussed brie<sup>fl</sup>y in Section 2, contextual on line advertisement targeting encompasses many forms including key word, pro<sup>fi</sup>le, content and clickstream targeting. In this work we focus solely on clickstream targeting. It is assumed, as is the case in targeted networks, that user clickstream data is readily available. This information is used to develop a characteristic array for each user. Although this work was limited to tests in only this type of ad targeting environment, based on the positive results, we expect that the model could be easily generalized to other forms of contextual advertising. For example, with essentially no adaptation, the model could be used for content targeting within which advertisements are displayed on a web page based primarily on that page's content. The only difference being that the advertisements would be targeted based on the analysis of the content of one web page instead of the hundreds that commonly represented a user's clickstream in the reported study. In fact, since our study utilizes a richer set of underlying data to train the model, we expect better targeted ads by our methodology as compared to those using only the content of one web page, but the same structural design could be utilized verbatim. Likewise, it would also be relatively simple to apply our model to keyword advertising. The search keywords that are supplied by the user could be used to directly develop the necessary characteristic arrays. The only caveat would be the need to develop a structured method by which to assign the necessary index term weights. The wealth of diverse semi-structured online data sources has given rise to a large array of contextual advertising scenarios. With very little adaptation, the proposed model, based on its strong performance and high level of generalizability, should be an appealing alternative in many of these different contextual ad targeting environments.

t-test results within weighting schemes.

<table><tr><td>Tested scheme</td><td>t value</td><td>Significance (2-tailed)</td></tr><tr><td>Scheme 1: top 20 ads vs. ads 21-40</td><td>1.699</td><td>0.090</td></tr><tr><td>Scheme 1: top 20 ads vs. ads 41-60</td><td>2.947</td><td>0.003</td></tr><tr><td>Scheme 1: top 20 ads vs. ads 61-80</td><td>2.856</td><td>0.004</td></tr><tr><td>Scheme 1: top 20 ads vs. bottom 20</td><td>6.662</td><td>0.000</td></tr><tr><td>Scheme 2: top 20 ads vs. ads 21-40</td><td>2.110</td><td>0.035</td></tr><tr><td>Scheme 2: top 20 ads vs. ads 41-60</td><td>3.997</td><td>0.000</td></tr><tr><td>Scheme 2: top 20 ads vs. ads 61-80</td><td>2.763</td><td>0.006</td></tr><tr><td>Scheme 2: top 20 ads vs. bottom 20</td><td>6.695</td><td>0.000</td></tr><tr><td>Scheme 3: top 20 ads vs. ads 21-40</td><td>-0.530</td><td>0.597</td></tr><tr><td>Scheme 3: top 20 ads vs. ads 41-60</td><td>2.221</td><td>0.027</td></tr><tr><td>Scheme 3: top 20 ads vs. ads 61-80</td><td>2.787</td><td>0.005</td></tr><tr><td>Scheme 3: top 20 ads vs. bottom 20</td><td>4.890</td><td>0.000</td></tr></table>

## 6. Conclusion and future research

The purpose of this research is to introduce a new online ad targeting technique and to test its effectiveness in selecting a subset of targeted ads from a given advertisement corpus with respect to the overall level of interest to a given user base. The ultimate goal is to provide online advertisement publishers with another viable ad scheduling tool. The most commonly used method in industry is the random selection process and according to industry representatives, publishers are eagerly awaiting new alternative techniques that offer improvement over this basic strategy.

Our OAWSH model performed exceptionally well across the board. With respect to the chosen evaluation measure, it outperformed the random selection process with all three weighting schemes. All of the associated t-tests are statistically signi<sup>fi</sup>cant at the .05 signi<sup>fi</sup>cance level. These results are very promising, but we wanted to extend our analysis of the technique a little further. Since the initial experiments focused only on the top 20% of the ads, we next turned our focus to the remaining 80%. Given that the OAWSH model assigns a relevance weight/score to every advertisement within the corpus, we wanted to see how the technique performed on those ads that did not appear at the top of the list. As is indicated by the summarized mean scores in Table 4, the technique once again performed well, with ads ranked higher by our model getting higher scores from students across all the <sup>fi</sup>ve groups of 20 ads. The overall trend of student rank responses was very consistent with the weights assigned by the model.

We have shown that the OAWSH model performed very well, and we are hopeful that it will prove to be bene<sup>fi</sup>cial to those in industry who are struggling with this very challenging problem. In addition, we are cautiously optimistic that with additional scrutiny and research by the academic community, we may offer improvement to the process. One potential area of focus is the structural component of the model. For this research, we limited our focus to only the most obvious structural components of the html documents, and to only a few weighting schemes. Expanding each of these to incorporate a more granular analysis of each html document may prove to be bene<sup>fi</sup>cial. In addition, we are con<sup>fi</sup>dent that the proposed model may be adapted to <sup>fi</sup>t in other advertising contexts and in doing so incorporate the use of additional sources of information such as keyword and demographic data. We hope that our work will provide the catalyst for additional improvements to the model.

## Appendix A. A sample version of the complete t-test table

<table><tr><td colspan="5">T test — scheme 1 &amp; random selection</td></tr><tr><td>Group statistics</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>N</td><td>Mean</td><td>Std. dev</td><td>Std. error</td></tr><tr><td>Scheme 1</td><td>943</td><td>2.69</td><td>1.388</td><td>0.045</td></tr><tr><td>Random</td><td>853</td><td>2.50</td><td>1.361</td><td>0.047</td></tr></table>

<table><tr><td rowspan="3"></td><td colspan="2">Levene&#x27;s test results</td><td colspan="7">t-test for equality of means</td></tr><tr><td rowspan="2">F</td><td rowspan="2">Sig.</td><td rowspan="2">t</td><td rowspan="2">df</td><td rowspan="2">Sig. (2-tailed)</td><td rowspan="2">Mean diff</td><td rowspan="2">Std. err</td><td colspan="2">95% conf interval</td></tr><tr><td>Lower</td><td>Upper</td></tr><tr><td>Equal var assumed</td><td>0.427</td><td>0.51</td><td>2.954</td><td>1794</td><td>0.003 **</td><td>0.19</td><td>0.065</td><td>0.065</td><td>0.319</td></tr><tr><td>Equal var not assumed</td><td></td><td></td><td>2.957</td><td>1782</td><td>0.003</td><td>0.19</td><td>0.065</td><td>0.065</td><td>0.319</td></tr></table>

Appendix B. A representative sample list of advertised products and services and a portion of their respective characteristic array

<table><tr><td>Ad #</td><td>Ad name</td><td>Keyword 1</td><td>Keyword 2</td><td>Keyword 3</td><td>Keyword 4</td><td>Keyword 5</td><td>Keyword 6</td><td>Keyword 7</td></tr><tr><td>1</td><td>Dell</td><td>computer</td><td>pda</td><td>computer</td><td>dell</td><td>dell</td><td>apple</td><td>pc</td></tr><tr><td>2</td><td>Target</td><td>target</td><td>target</td><td>clothes</td><td>shoe</td><td>electronic</td><td>buy</td><td>walmart</td></tr><tr><td>3</td><td>Masters</td><td>golf</td><td>golf</td><td>golf</td><td>golf</td><td>mickelson</td><td>woods</td><td>masters</td></tr><tr><td>4</td><td>Women's shoes</td><td>shoes</td><td>shoe</td><td>shoe</td><td>shoe</td><td>shoe</td><td>clothes</td><td>business</td></tr><tr><td>5</td><td>Vera Bradley bag</td><td>bag</td><td>bag</td><td>purse</td><td>pocketbook</td><td>purse</td><td>pocketbook</td><td>pocketbook</td></tr><tr><td>6</td><td>Pennzoil</td><td>oil</td><td>oil</td><td>car</td><td>care</td><td>oil</td><td>lube</td><td>lube</td></tr><tr><td>7</td><td>Nascar</td><td>race</td><td>race</td><td>race</td><td>racing</td><td>racing</td><td>goodyear</td><td>race</td></tr><tr><td>8</td><td>SUV</td><td>truck</td><td>automobile</td><td>car</td><td>truck</td><td>car</td><td>automobile</td><td>truck</td></tr><tr><td>9</td><td>Kohler faucets</td><td>faucet</td><td>bathroom</td><td>toilet</td><td>sink</td><td>faucet</td><td>remodel</td><td>faucet</td></tr><tr><td>10</td><td>Flat screen TV</td><td>television</td><td>tv</td><td>tv</td><td>screen</td><td>plasma</td><td>movie</td><td>sony</td></tr><tr><td>11</td><td>Gators football</td><td>football</td><td>football</td><td>gator</td><td>gator</td><td>football</td><td>sport</td><td>athletic</td></tr><tr><td>12</td><td>Computer</td><td>computer</td><td>computer</td><td>window</td><td>monitor</td><td>dell</td><td>dell</td><td>pc</td></tr><tr><td>13</td><td>Pedialyte</td><td>infant</td><td>dehydration</td><td>hang</td><td>over</td><td>toddler</td><td>baby</td><td>dehydrate</td></tr><tr><td>14</td><td>Gator Sport Shop</td><td>gator</td><td>gator</td><td>gator</td><td>florida</td><td>gators</td><td>florida</td><td>florida</td></tr><tr><td>15</td><td>Kodiak</td><td>dip</td><td>tobacco</td><td>nicotine</td><td>dip</td><td>tobacco</td><td>kodiak</td><td>tobacco</td></tr><tr><td>16</td><td>Cars</td><td>car</td><td>car</td><td>automobile</td><td>loan</td><td>jeep</td><td>car</td><td>jeep</td></tr><tr><td>17</td><td>Nordstrom</td><td>clothing</td><td>jean</td><td>shirt</td><td>shoe</td><td>gap</td><td>pant</td><td>shop</td></tr><tr><td>18</td><td>Flowers.com</td><td>flower</td><td>floral</td><td>floral</td><td>floral</td><td>flower</td><td>anniversary</td><td>birthday</td></tr><tr><td>19</td><td>HP</td><td>computer</td><td>printer</td><td>personal</td><td>computer</td><td>dell</td><td>electronic</td><td>dell</td></tr><tr><td>20</td><td>Home depot</td><td>depot</td><td>floor</td><td>home</td><td>home</td><td>depot</td><td>repair</td><td>lawn</td></tr><tr><td>21</td><td>Discover Card</td><td>travel</td><td>visa</td><td>discover</td><td>credit</td><td>debt</td><td>purchase</td><td>finance</td></tr><tr><td>22</td><td>Etrade</td><td>stocks</td><td>stock</td><td>investment</td><td>job</td><td>stock</td><td>trade</td><td>bond</td></tr><tr><td>23</td><td>US Air</td><td>hotel</td><td>vacation</td><td>travel</td><td>travel</td><td>ticket</td><td>delta</td><td>fly</td></tr><tr><td>24</td><td>USA Today</td><td>news</td><td>newspaper</td><td>classified</td><td>sport</td><td>leisure</td><td>news</td><td>today</td></tr><tr><td>25</td><td>Orkin</td><td>bug</td><td>exterminate</td><td>exterminator</td><td>bug</td><td>pest</td><td>pest</td><td>bug</td></tr></table>

## Appendix C. Simple example of OAWSH model

For this very simple example, we assume:

\- that the html document has only 2 parts; title and body

\- in this case, our user only visited one html page

\- there are only 3 advertisements in our corpus

\- our structural weighting strategy will be to give the head a weight of .7 and the body a weight of .3

\- we will not utilize the lexical database

\- in an effort to achieve simplicity we will not utilize the lexical database to aggregate over synonym sets for this example.

Step 1 — Track the user's surfing behavior

Step 2 — Collect the corresponding HTML code:

Title — The Leather Chair Store

Body — The leather chair store has every possible style and color of leather chair to <sup>fi</sup>t your needs.

Step 3: Develop a characteristic array for the user

Leather, Chair, Store, every, possible, style, color, <sup>fi</sup>t, your, needs

Step 4: Develop descriptive arrays for our advertisements

Ad 1: Qray, Magnet, Health, Golf, Bracelet

Ad 2: Sofa, Chair, Furniture, Leather, Wood

Ad 3: Leather, Jacket, Coat, Cold, Winter

Resulting Key term Corpus after removal of stop words:

Leather, Chair, Store, every, possible, style, color, <sup>fi</sup>t, your, needs, Qray, Magnet, Health, Golf, Bracelet, Sofa, Furniture, Wood, Jacket, Coat, Cold, Winter

Step 5: Using a similarity measure (basic dot product in this example), rank the ads for the user

Part A. Develop weight vectors for the user and the ads:

i. For our user (based on the one visited html page)

Leather — 1.3 (leather show up in the head once and the body twice; therefore, leather gets a weight of .7 + (.3⁎2)

{1.3, 1.3, 1.3, .3, .3, .3, .3, .3, .3, .3,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,}

For simplicity, each term will receive a weight of 1 if it shows up in the descriptive term list for the ad and a 0 otherwise.

ii. Ad 1

{0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0}

iii. Ad 2

{1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0}

iv. Ad 3

{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1}

Part B. Calculate similarity measures and rank ads accordingly

Ad 1 – Score=0 (rank last)

Ad 2 – Score=2.6 (rank best)

Ad 3 – Score=1.3 (rank second)

In this simple example, we would recommend serving ad 2 <sup>fi</sup>rst, ad 3 second and ad 1 last.

## References

[1] E. Agirre, D. Martinez, Exploring automatic word sense disambiguation with decision lists and the web, Semantic Annotation and Intelligent Annotation Workshop, 2000.

[2] S. Banerjee, T. Pedersen, An adapted lesk algorithm for word sense disambiguation using WordNet, Third International Conference on Intelligent Text Processing and Computational Linguistics, 2002.

[3] A. Bhatnagar, P. Papatla, Identifying locations for targeted advertisements on the internet, International Journal of Electronic Commerce 5 (3) (2001).

[4] P. Buiteclaar, B. Sacaleanu, Ranking and selecting synsets by domain relevance Proceedings of WorldNet and other Lexical Resources: Application, Extensions, and Customizations, 2001.

[5] F. Burkowski, Retrieval activities in a database consisting of heterogeneous collections of structured text, 15th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 1992.

[6] M. Cecchini, Quantifying the risk of <sup>fi</sup>nancial events using kernel methods and information retrieval, Decision and Information Sciences, University of Florida: Gainesville, FL, 2005.

[7] P. Chatterjee, D.L. Hoffman, T.P. Novak, Modeling the clickstream: implications for web-based advertising efforts, Marketing Science 22 (4) (2003).

[8] D. Chickering, D. Heckerman, Targeted advertising on the web with inventory management, Interfaces 33 (5) (2003).

[9] A. Cucchiarelli, P. Velardi, Automatic selection of class labels from a thesaurus for an effective semantic tagging of corpora, 5th Conference on Applied Natural Language Processing, 1997.

[10] M. Dawande, S. Kumar, C. Sriskandarajah, Performance bounds of algorithms for scheduling advertisements on a web page, Journal of Scheduling 6 (2003).

[11] W. Fan, M. Gordon, P. Pathak, On linear mixture of expert approaches to information retrieval, Decision Support Systems 42 (2) (2006).

[12] C. Fellbaum, WordNet: An Electronic Lexical Database, MIT Press, 1999.

[13] J. Gonzalo, F. Verdejo, I. Chugar, J. Cigarran, Indexing with WordNet synsets can improve text retrieval, Workshop on Usage of WordNet for NLP, 1998.

[14] F. Halasaz, Re<sup>fl</sup>ections on notecards: seven issues for the next generation of hypermedia systems, Communications of the ACM, 1988.

[15] A. Houston, H. Chen, B. Schatz, S. Hubbard, R. Sewell, T. Ng, Exploring the use of concept spaces to improve medical information retrieval, Decision Support Systems 30 (2) (2000).

[16] G. Karuga, A. Khraban, S. Nair, D. Rice, AdPalette: an algorithm for customizing online advertisements on the <sup>fl</sup>y, Decision Support Systems 32 (2001).

[17] Kessler, M. and B. Acohido, Data Miners Dig a Little Deeper, USA Today (2006).

[18] M. Langheinrich, et al., Unintrusive customization techniques for web advertising Computer Networks 31 (1999).

[19] R. Mihalcea, D. Moldovan, AutoASC — a system for automatic acquisition of sense tagged corpora, International Journal of Pattern Recognition and Arti<sup>fi</sup>cial Intelligence 14 (1) (2000).

[20] B. Murthi, S. Sarkar, The role of the management sciences in research on personalization, Management Science 49 (10) (2003).

[21] G. Navarro, R.B. Yates, Proximal nodes: a model to query document databases by content and structure, ACM Transactions on Of<sup>fi</sup>ce and Information Systems 15 (4) (1997).

[22] G. Navarro, R.B. Yates, A language for queries on structure and contents of textual databases, 18th Annual Int. ACM SIGIR Conference on Research and Development in Information Retrieval, 1995.

[23] T.S. Raghu, P. Kannan, H. Rao, A. Whinston, Dynamic pro<sup>fi</sup>ling of consumers for customized offerings over the internet: a model and analysis, Decision Support Systems 32 (2) (2001).

[24] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing and Management 24 (1988).

[25] G. Salton, M.E. Lesk, Computer evaluation of indexing and text processing, Journal of the ACM 15 (1) (1968).

[26] G.B. Salton, C., Automatic Text Processing, Addison Wesley, Reading, 1989

[27] C. Shahabi, F. Banaei-Kashani, Ef<sup>fi</sup>cient and anonymous web-usage mining for web personalization, INFORMS Journal on Computing 15 (2) (2003).

[28] K. Sparck Jones, A statistical interpretation of term speci<sup>fi</sup>city and its application in retrieval, Journal of Documentation 28 (1) (1972).

[29] G. Stein, US Online Advertising Forecast, 2005–2010, 2005.

[30] E.M. Vorhees, Y.H. Hou, Vector expansion in a large collection, First Text Retrieval Conference, NIST Special Publication, 1993.

[31] E.M. Vorhees, Using WordNet to disambiguate word sense for text retrieval, ACM SIGR Conference on Research and Development in Information Retrieval, 1993

[32] D. Xu, S. Liao, Q. Li, Combining empirical experimentation and modeling techniques: a design research approach for personalized mobile advertising applications, Decision Support Systems 44 (3) (2008).

[33] R.B. Yates, B.R. Neto, Modern Information Retrieval, Addison Wesley, Reading, 1999.

[34] S. Yuan, A personalized and integrative comparison-shopping engine and its applications, Decision Support Systems 34 (2) (2003).

[35] Wordnet. URL: http://wordnet.princeton.edu/.

![](/api/attachments/NPU8GXRE/fulltext/images/7c47830b573443013c8d99492691a039704264bdd8808bd9fac450659f9e57b7.jpg)  
Jason Deane is Assistant Professor of Business Information Technology in the Pamplin College of Business at Virginia Polytechnic Institute & State University. He received a Ph.D. in Decision and Information Sciences from the University of Florida, and an M.B.A. and B.S. in Business Administration from Virginia Tech. His current research interests are in the areas of arti<sup>fi</sup>cial intelligence, computer aided decision support systems, information system security, large scale optimization and information retrieval.

![](/api/attachments/NPU8GXRE/fulltext/images/b10bb453496e782918c7e4e335f4b3539fefeaaa19518e74b5c14beccf5e0cbf.jpg)

Dr. Praveen Pathak is an Assistant Professor of Decision and Information Sciences at the Warrington College of Business at the University of Florida. He received his PhD in Information Systems from the Ross School of Business, University of Michigan, Ann Arbor, in 2000. He also holds an MBA (PGDM) from the Indian Institute of Management, Calcutta, and an Engineering degree, B. Tech. (Hons.), from the Indian Institute of Technology, Kharagpur. His research interests include information retrieval, web mining, offshore outsourcing and business intelligence. His research has appeared in many journals such as Journal of Management Information Systems (JMIS), Decision Support Systems (DSS). IEEE Transactions on Knowledge and Data Engineering (TKDE), Information Processing and Management (IP&M), Journal of the American Society for Information Science and Technology (JASIST), and in leading information technology conferences such as ICIS, HICSS, WITS, and INFORMS.
