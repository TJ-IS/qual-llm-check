---
otero_id: 748
otero_key: "FBEF7CK9"
title: "An intelligent information agent for document title classification and filtering in document-intensive domains"
authors: "Dawei Song; Raymond Y.K. Lau; Peter D. Bruza; Kam-Fai Wong; Ding-Yi Chen"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.04.001"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2007) 251– 265

www.elsevier.com/locate/dss

# An intelligent information agent for document title classification and filtering in document-intensive domains

Dawei Song <sup>a,⁎</sup>, Raymond Y.K. Lau <sup>b</sup>, Peter D. Bruza <sup>c</sup>, Kam-Fai Wong <sup>d</sup>, Ding-Yi Chen <sup>e</sup>

<sup>a</sup> Knowledge Media Institute, The Open University, Walton Hall, Milton Keynes, MK7 6AA, United Kingdom

<sup>d</sup> Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Shatin, N.T., Hong Kong SAR, China <sup>e</sup> School of Information Technology and Electrical Engineering, The University of Queensland, QLD 4072, Australia

Received 30 January 2006; received in revised form 18 March 2007; accepted 8 April 2007 Available online 18 April 2007

## Abstract

Effective decision making is based on accurate and timely information. However, human decision makers are often overwhelmed by the huge amount of electronic data these days. The main contribution of this paper is the development of effective information agents which can autonomously classify and filter incoming electronic data on behalf of their human users. The proposed information agents are innovative because they can quickly classify electronic documents solely based on the short titles of these documents. Moreover, supervised learning is not required to train the classification models of these agents. Document classification is based on information inference conducted over a high dimensional semantic information space. What is more, a belief revision mechanism continuously maintains a set of user preferred information categories and filter documents with respect to these categories. Preliminary experimental results show that our document classification and filtering mechanism outperforms the Support Vector Machines (SVM) model which is regarded as one of the best performing classifiers. © 2007 Elsevier B.V. All rights reserved.

Keywords: Information inference; Information flow; Belief revision; Document classification; Information agents

## 1. Introduction

Effective decision making (e.g., selecting a stock portfolio for investment) is based on accurate and timely information, and in most cases based on a certain volume of timely information. With the rapid growth of the Internet, there has been ever expanding amount of electronic information available. As a result, decision makers often suffer from the so-called problem of information overload [18,21]. Accordingly, there is a pressing need for the development of intelligent information processing tools to alleviate the information overload problem, and hence to improve the effectiveness of decision making. In situations involving large amounts of incoming electronic information such as defence intelligence, it is increasingly more important for defence analysts to quickly decide whether certain information items should further be scrutinized (either by automatic or manual means) solely based on metadata elements such as title descriptions or brief captions. The reason is that it is too time consuming, or too cognitively demanding to process whole documents. Many of us also make such decisions daily while scanning the subject descriptions of emails, or the title captions in the result set from a search engine.

A human agent can quickly make the judgment that a web page title “Welcome to Penguin Books, U.K” refers to Penguin, the publisher. With reference to the text fragment “Linux Online: Why Linus chose a Penguin?”, a human agent may readily infer that “Linus” refers to Linus Torvalds, the inventor of Linux system, and the “penguin” mentioned here has to do with the Linux logo. Another text fragment “Antarctic Penguins”, on the other hand, would lead to the judgment that the text is referring to penguins, the birds. If we want to develop intelligent information processing systems to alleviate the problem of information overload, it is essential that these systems are capable of replicating the kind of approximate, associational inference mentioned above. It should be noted that humans generally excel in exercising intelligent information inference given short captions. Confounding information overload is the fact that a decision maker's interests may change over time due to the evolving nature of the decision making process (e.g., shifting from the interest of identifying suspected terrorist attacks to locating the sources of money laundering). An intelligent information processing system should therefore be able to track a user's changing interests and maintain an accurate profile of the user's preferences over time.

This paper proposes an intelligent information agent model for document classification and filtering in information intensive application domains. Intelligent information agents are computer programs situated in some environments (e.g., the World Wide Web) for autonomous and adaptive information retrieval and filtering on behalf of their human users [16]. The proposed agent-based information classification and filtering system comprises two main components – the classification module (i.e., the classification agent) and the belief revision module (i.e., the filtering agent). The former drives the use of information flow model for category learning and information classification based on document titles, and the latter determines which categories of documents are more likely corresponding to a user's most current information preferences by conducting non-monotonic reasoning [12]. The architecture of our document classification and filtering system is depicted in Fig. 1.

The proposed agent-based intelligent information processing system makes effective judgments what information fragments are “about”, or are not “about”, even when the fragments are brief or incomplete. The process of making such “aboutness” judgments has been referred to as information inference [4,31]. An information flow inference model has been developed to automatically discover the implicit information flows from the terse text fragments. These flows underpin the approximate, associational inferences mentioned earlier. More specifically, an information inference of Y from X reflects how strongly Y is informationally contained within X. Information is represented as vectors in a cognitively motivated high dimensional semantic space model, namely Hyperspace Analogue to Language (HAL) [5,20]. A combination heuristic is developed to render combinations of concepts, for example, noun compounds, into a single vector representation. Information inference can be performed on the HAL spaces via computing information flows between vectors or combination vectors. For example, “publisher” is an information flow derived from “Welcome to Penguin Books, U.K”. With information inference, the information classification agent can quickly classify the incoming documents into different categories, e.g., “publisher”, “birds”, “logo”, etc. according to short document titles rather than full text. After document classification, the filtering agent will deduce if certain categories of documents are relevant with respect to the user's specific interests. Such a deduction process is underpinned by non-monotonic reasoning. It has been argued that non-monotonic inference plays an important role in IR [37]. For example, beliefs about which search terms are relevant will grow non-monotonically in light of the documents seen during a search process.

![](/api/attachments/FBEF7CK9/fulltext/images/7b3db4f90a9abc662b2f47f66af7969551d6df7a0392fb53cf273bbe4be525d8.jpg)  
Fig. 1. Architecture of the intelligent classification and filtering system.

At a first glance, the functionality of our intelligent classification and filtering system is similar to that of a Text Categorization (TC) system which assigns a number of pre-defined category labels to documents. A number of statistical learning algorithms such as Knearest neighbor (KNN) [8], Naïve Bayes (NB) [23], Support Vector Machines (SVM) [14], and Neural Networks (NN) [22,23] have been investigated. These classifiers usually classify a document based on its full content and they require the availability of a large number of training documents to achieve a reasonable level of accuracy. Nevertheless, the characteristics of many real-world domains (e.g., defence intelligence) do not match the pre-requisite requirements of the traditional text categorization algorithms. The main contribution of this paper is the illustration of our novel intelligent information agents underpinned by information flow inference and belief revision; these agents specifically aim at autonomous information processing in data intensive domains such as e-mail scanning, Web page browsing, defence intelligence analysis, etc. where:

• Incoming documents need to be classified based on short descriptions (e.g., document titles);

• Labeled training data may not be available;

• A user's preferences (e.g., interests in categories like “publisher”, “birds”, “logo”, etc.) may change upon what the user has seen in the received documents over time.

The rest of the paper is organized as follows. In Section 2, an introduction to the information flow model and how it is applied to infer candidate information categories from document titles is illustrated. Section 3 proposes a belief revision mechanism for dynamic user profiling and adaptive information filtering. The effectiveness and efficiency of our intelligent information agent is evaluated in Section 4. Section 5 highlights the related research work for intelligent information agents. Finally, we offer concluding remarks and describe future direction of this work in Section 6.

## 2. Classifying document titles via information flow

This section introduces a model of information flow inference and illustrates how it can be applied to derive categories from unlabeled document titles. We begin with a vector representation of information, based on which an information flow computation is performed.

2.1. Knowledge representation via Hyperspace Analogue to Language

When humans encounter a new concept, they can draw the meaning of the concept via the accumulated experience of the contexts in which the concept appears. This opens the door to “learn” the meaning of a concept through how a concept appears within the context of other concepts. Following this idea, Burgess and Lund developed a representational model of semantic memory called Hyperspace Analogue to Language (HAL), which is a cognitively motivated and validated semantic space model built upon the term co-occurrence relationships derived from a corpus of text [5].

What HAL does is to generate a word-by-word cooccurrence matrix from a large text corpus via a L-sized sliding window; all the words occurring within the window are considered as co-occurring with each other. By moving the window across the text corpus, an accumulated co-occurrence matrix for all the words of a vocabulary is produced. The strength of association between two words is inversely proportional to their distance. Given two words, the weight of association between them is computed by (L − d + 1), whereas d is the distance between these words. After traversing the corpus, an accumulated co-occurrence matrix for all the words in a target vocabulary is produced. HAL is direction sensitive, that is, the co-occurrence information preceding and following a particular word is recorded by the corresponding row vector and column vector separately. By way of illustration, the HAL space for the example text “The effects of spreading pollution on the population of Atlantic salmon” is depicted in Table 1, assuming a 5-word window (L=5). As an illustration, the term “effects” appears ahead of “spreading” in the window and their distance is 2 words apart. The value of the cell (spreading, effects) is derived by: 5−2 +1=4. Table 1 also shows how the row vectors encode preceding word order and the column vectors encode posterior word order.

Table 1  
Example of a HAL space

<table><tr><td></td><td>the</td><td>effects</td><td>of</td><td>spreading</td><td>pollution</td><td>on</td><td>population</td><td>Atlantic</td><td>salmon</td></tr><tr><td>the</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td></td><td></td></tr><tr><td>effects</td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>of</td><td>8</td><td>5</td><td></td><td>1</td><td>2</td><td>3</td><td>5</td><td></td><td></td></tr><tr><td>spreading</td><td>3</td><td>4</td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>pollution</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>on</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>population</td><td>5</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td></td><td></td><td></td></tr><tr><td>Atlantic</td><td>3</td><td></td><td>5</td><td></td><td>1</td><td>2</td><td>4</td><td></td><td></td></tr><tr><td>salmon</td><td>2</td><td></td><td>4</td><td></td><td></td><td>1</td><td>3</td><td>5</td><td></td></tr></table>

The quality of HAL vectors is influenced by the window size; the longer the window, the higher the chance of representing spurious associations between terms. A window size of eight to ten has been used in various studies [4,5,30]. Accordingly, a window size of 10 is used in the experiments reported in this paper. Following the tradition of not keeping order information for the co-occurrence based approaches in information retrieval, our approach is to represent a word by a single vector which is the sum of its row and column vectors. It has been demonstrated in the IR literature that the use of HAL in this way produces good performance [5]. Furthermore, it is computationally more cost-effective than keeping the row and column vectors separately. This is particularly important when we are dealing with large collections. However, we would leave it as an open problem for future work to empirically verify whether representing a word as a unified vector gives a better performance than using the row and column vectors separately.

Formally, a concept (term) c is a vector: $c =$ $< w _ { c p _ { 1 } } , w _ { c p _ { 2 } } , \ldots , w _ { c p _ { n } } >$ where $p _ { 1 } , p _ { 2 } , . . . , p _ { n }$ are called the dimensions of c; n is the dimensionality of the HAL space, and $w _ { c p i }$ denotes the weight of $p _ { i }$ in the vector representation of c. In addition, it is useful to identify the so-called quality properties of a HAL vector. Intuitively, the quality properties of a concept or term c are those terms which often appear in the same context as c. A dimension is termed a property if its weight is greater than zero. A property $p _ { i }$ of a concept c is termed a quality property if $w _ { c p _ { i } } { > } \partial$ , where $\hat { o }$ is a non-zero threshold value (e.g., the average weight within that vector). To reduce noise in a vector derived from a large corpus, only certain quality properties are kept. Let $\mathrm { Q P } _ { \hat { \sigma } } ( c )$ denote the set of quality properties of concept c and $\mathrm { Q P } _ { \mu } ( c )$ be the set of quality properties above the mean of positive values. QP (c) is short for $\mathrm { Q P _ { 0 } } ( c )$ . HAL vectors are normalized to unit length before information flow computation. The following normalization method has been proposed in our previous work [30] for a dimension $p _ { j }$ in concept c<sub>i</sub>:

$$
w _ {c _ {i} p _ {j}} ^ {\prime} = \frac {w _ {c _ {i} p _ {j}}}{\sqrt {\sum_ {\mathrm{k}} w _ {c _ {i} p _ {k}} ^ {2}}}\tag{1}
$$

For example, the normalized HAL vector for “spreading” with reference to the above example is: spreading= bthe: 0.52, effects: 0.35, of: 0.52, pollution: 0.43, on: 0.35, population: 0.17N.

In natural language, word compounds often refer to a single underlying concept. As HAL represents words, it is necessary to address the question of how to represent a concept comprising more than one word. Thus we need to address the issue of concept combination, which has been recognized as a remarkable feature of human thinking [10]. From practical point of view, concept combination does not have to be limited to those syntactically valid phrases. A more general and flexible way of concept combination from arbitrary terms should be developed. A simple method is to sum up the vectors of the respective terms to form a compound. However, we apply a more sophisticated concept combination heuristic [4] to the information agent illustrated in this paper. It can be envisaged as a weighted addition of the underlying vectors paralleling the intuition that some terms are more dominant than others in a given concept combination. Dominance is determined by the specificity of a term. For example, “GATT (General Agreement on Tariffs & Trade) Talks” is more related to “GATT” than it is about “talks”.

Table 2  
Information flows from “GATT talks”

<table><tr><td>Degree of information flow</td><td>w</td></tr><tr><td>1.00</td><td>GATT</td></tr><tr><td>0.96</td><td>trade</td></tr><tr><td>0.96</td><td>agreement</td></tr><tr><td>0.86</td><td>world</td></tr><tr><td>0.85</td><td>negotiations</td></tr><tr><td>0.84</td><td>talks</td></tr><tr><td>0.82</td><td>set</td></tr><tr><td>0.82</td><td>states</td></tr><tr><td>0.81</td><td>EC</td></tr><tr><td>0.78</td><td>Japan</td></tr></table>

In order to deploy the information flow model in an experimental setting, the dominance of a term is determined by its inverse document frequency (idf) value. More specifically, terms can be ranked according to its idf. Assuming a ranking of terms: $t _ { 1 } , . . . , t _ { m } ( m > 1 )$ , terms $t _ { 1 }$ and $t _ { 2 }$ can be combined form a compound concept, denoted as $t _ { 1 } \oplus t _ { 2 }$ , whereby $t _ { 1 }$ dominates $t _ { 2 }$ (as it is higher in the ranking). For this combined concept, the degree of dominance is the mean idf scores of $t _ { 1 }$ and $t _ { 2 } .$ . The process recurses down the ranking resulting in the composed “concept” $( ( . . ( . \oplus t _ { 2 } ) \oplus t _ { 3 } ) \oplus . . . ) \oplus t _ { m } )$ . If there is only a single term $( m { = } 1 )$ , the normalized HAL vector is the same as the combination vector.

We will not give a more detailed description of the concept combination heuristic, which can be found in [4]. Its intuition is summarized as follows:

• Quality properties shared by both concepts are emphasized;

• The weights of the properties in the dominant concept are re-scaled higher;

• The resulting vector developed according to the combination heuristic is normalized to smooth out variations due to the different number of contexts the respective concepts appear in.

By way of illustration, we have the following vector “GATT talks”, which is a concept combination of the individual HAL vectors for “GATT” and “talks” derived from the Reuters-21578 corpus.

gatt ⊕ talks = bagreement: 0.282, agricultural: 0.106, body: 0.117, china: 0.121, council: 0.109, farm: 0.261, gatt: 0.279, member: 0.108, negotiations: 0.108, round: 0.312, rules: 0.134, talks: 0.360, tariffs: 0.114, trade: 0.432, world: 0.114N

To demonstrate the sensibleness of our concept combination heuristic, we show in the following a fragment of a Reuters article about GATT talks.

GATT OFFICIAL MEETS WITH U.S. FARM LEADERS.

The official in charge of agricultural matters in the new round of global trade talks is in Washington today and tomorrow to meet with congressional and Reagan administration officials. Aart de Zeeuw, chairman of the General Agreement on Tariffs and Trade's negotiating group on agriculture, met this morning with members of the House Agriculture Committee.

## 2.2. Computing information flow

Information inference determines the degree to which a concept $c _ { j }$ can be inferred “informationally” from another concept $c _ { i }$ or combination of a list of concepts $c _ { i 1 } \oplus _ { . . . } \oplus c _ { i k } ,$ denoted degree $( \oplus c _ { i } | ^ { - } c _ { j } )$ . For ease of exposition, $\oplus _ { c _ { i } }$ will be referred to as c because compound concepts are also concepts. A HAL vector is used to represent the information “state” [2] of a particular concept or combination of concepts with respect to a given corpus of text. The degree of information flow is directly related to the degree of inclusion between the respective information states represented by HAL vectors. Total inclusion leads to maximum information flow. The following example illustrates the inclusion between “GATT⊕ talks” and “trade” (Fig. 2).

The degree of inclusion is computed in terms of the ratio of the sum of weights of the intersecting quality properties of $c _ { i }$ and $c _ { j }$ to the sum of the weights of the quality properties of the source $c _ { i } .$

$$
\operatorname{degree} \left(c _ {i}, c _ {j}\right) = \frac {\sum_ {p _ {1} \in \left(\mathrm{QP} _ {\hat {c} _ {i}} \left(c _ {i}\right) \cap \mathrm{QP} \left(c _ {j}\right)\right)} w _ {c _ {i} p _ {l}} ^ {\prime}}{\sum_ {p _ {k} \in \mathrm{QP} _ {\hat {c} _ {i}} \left(c _ {i}\right)} w _ {c _ {i} p _ {k}} ^ {\prime}}.\tag{2}
$$

The above formula expresses that degree is a function with the vector pairs as its domain and the unit interval [0,1] as its range. The vector $c _ { i }$ is termed the source of the information flow and $c _ { j }$ the target. The higher the degree of inclusion of the source in the target, the higher the degree of the information flow. Note that all the dimensions in the target vector $c _ { j } , \mathrm { i . e . , Q P _ { 0 } } \left( c _ { j } \right)$ , are used. On the other hand, the parameter $\widehat { \cal O } _ { i }$ is used to select quality properties in the source vector. The underlying idea of this definition is to make sure that most of the important quality properties of $c _ { i }$ appear in $c _ { j }$ [31]. If $\widehat { \cal O } _ { i }$ is too low, there will be much noise leading to many irrelevant inferences (i.e., target vectors containing the noisy dimensions of the source vector). If it is too high, there will not be sufficient information in the source vector for deriving specific information flows. For the experiment depicted below, $\widehat { \cal O } _ { i }$ is set to be greater than the average positive dimensional weight within $c _ { i } ,$ i.e., $\mathrm { Q P } _ { \mu } ( c _ { i } )$ , which has been reported as the besting performing setting [31]. Table 2 shows an example of information flow computation where the weights represent the degree of information containment between GATT ⊕ talks and other terms in the vocabulary of the Reuters collection.

![](/api/attachments/FBEF7CK9/fulltext/images/f3aab464a171fcfea5dfc17ab2b472c773d79fcb9f3acd66b33e4f51f5d360e9.jpg)  
Fig. 2. An example of inclusion.

## 2.3. Classification via information flow

A HAL space can be produced from a text corpus, which may be dynamic – it could be expanded when new information comes in. The HAL vectors for the concepts embedded in the new data can then be updated accordingly. This module can be pre-processed and kept updated in the background. The HAL space features a module for driving information inference which is sensitive to the context of local data; the local contexts refer to the incoming document titles. Consider the terms $t _ { 1 } , . . . , t _ { m }$ being drawn from the title of an incoming document D. The concept combination heuristic can be used to obtain a combination vector of $t _ { 1 } \oplus t _ { 2 } \oplus . . . \oplus t _ { m } .$ The information flows from $t _ { 1 } \oplus t _ { 2 } \oplus . . . \oplus t _ { m }$ can be calculated. The top M information flows (ranked by association degree) can be taken as the candidate categories of D [32]. For the experiments reported below, M is set to be 80; previous experiments in query expansion via information flow shows that employing top 80 information flows produces the best results [4]. This parameter value will be applied to all the experiments reported in this paper. Fig. 3 illustrates this methodology.

By way of illustration, the concept “trade” is inferred from “GATT talks” with a high association degree of 0.96. Accordingly, the document titled “GATT talks” can be classified under the information category “trade”. Once a set of inferred candidate categories is assigned to a document title, these categories need to be evaluated with respect to the user's specific preferences in order to decide whether the categorized documents are desirable (i.e., relevant) or not. As a user's preferences may change over time, maintaining an updated user profile and determining whether a document is relevant or not is an important and challenging task. The next section will describe our belief revision based method to address such a problem.

## 3. Dynamic user profiling and document filtering

Although the classification module of our intelligent information agent can assign some ‘candidate categories to a document, the ultimate goal of the information agent is to deliver relevant documents to its users. Table 3 gives an example of the information categories assigned to ten documents and the final relevance judgments of these documents. The belief revision module determines which document categories are more likely corresponding to a user's information preferences based on non-monotonic reasoning. The intelligent agent then delivers the documents of those preferred categories to the user. In addition, the belief revision module maintains a set of information categories (i.e., a user profile) which are relevant with respect to the user's specific interests. The challenge here is that the set of categories is only relevant with respect to the user's interest to a certain degree because the user may not be sure which categories best described their interests. Accordingly, an intelligent information agent should be able to represent and reason about the uncertainty inherent in relevance prediction. A second challenge is that user's interests may change over time, and so the belief revision module is also responsible for revising the agent's beliefs about the user's changing preferences.

![](/api/attachments/FBEF7CK9/fulltext/images/21b9122d767ed962c303a126cebe4e6ad4847307eecb7ec8f8276ebe68869bc8.jpg)  
Fig. 3. Methodology for information flow based document title classification.

Table 3  
An example of category assignments

<table><tr><td> $Doc_1$ </td><td>business</td><td>commerce</td><td>finance</td><td>Relevant</td></tr><tr><td> $Doc_2$ </td><td>business</td><td>commerce</td><td>finance</td><td>Relevant</td></tr><tr><td> $Doc_3$ </td><td>business</td><td>economy finance</td><td>commerce</td><td>Relevant</td></tr><tr><td> $Doc_4$ </td><td>business</td><td>economy finance</td><td>commerce</td><td>Relevant</td></tr><tr><td> $Doc_5$ </td><td>business</td><td>economy finance</td><td>commerce</td><td>Relevant</td></tr><tr><td> $Doc_6$ </td><td>finance</td><td></td><td></td><td>Non-relevant</td></tr><tr><td> $Doc_7$ </td><td>computer finance</td><td>commerce</td><td></td><td>Non-relevant</td></tr><tr><td> $Doc_8$ </td><td>computer finance</td><td>commerce</td><td></td><td>Non-relevant</td></tr><tr><td> $Doc_9$ </td><td>computer internet</td><td>finance commerce</td><td></td><td>Non-relevant</td></tr><tr><td> $Doc_{10}$ </td><td>computer internet</td><td>finance commerce</td><td></td><td>Non-relevant</td></tr></table>

## 3.1. Representing users' information preferences

Conceptually, the list of possibly relevant information categories is represented by a set of beliefs in an agent's knowledge base. The changes of these beliefs are characterized by the corresponding belief functions under the guiding principle of minimal and consistent belief changes [1]. An agent's knowledge base is formalized by a belief state (set) K which consists of a set of beliefs. In particular, the AGM belief revision framework [1], which is one of the most influential works in the theory of belief revision, underpins the belief revision modules of our intelligent information agents. In this framework, belief revision processes are taken as the transitions among belief states. A belief state K is represented by a theory of a classical language L. Three principle types of belief state transitions are identified and modeled by the corresponding belief functions: Expansion $K _ { \alpha } ^ { + } ,$ , Contraction $K _ { \alpha } ^ { - }$ , and Revision $K _ { \alpha } ^ { * }$ . The AGM framework comprises sets of postulates to characterize these functions for consistent and minimal belief revision. In addition, the AGM framework also specifies the constructions of the belief functions based on various mechanisms. One of them is epistemic entrenchment (≤) [11]. It captures the notions of significance, firmness, or defeasibility of beliefs. If inconsistency arises after applying changes to a belief set, the least significant beliefs (i.e., beliefs with the lowest entrenchment degree) are given up in order to restore consistency. The belief revision module of our information agent employs the notion of epistemic entrenchment to represent a user's preferences over some information topics (categories), and utilizes the AGM belief revision function K<sup>⁎</sup> to revise the agent's beliefs about the user's current preferences.

For a computer-based implementation of the AGM belief revision functions, Williams proposed a finite representation of the epistemic entrenchment ordering $B _ { \leq }$ and an iterated belief revision strategy called Maxiadjustment [35,36]. An agent's belief is represented by a sentence α (e.g., “¬coffee”, “trade”, etc.) and the associated entrenchment degree B(α). Based on the Maxi-adjustment method, a more efficient Rapid Anytime Maxi-adjustment (RAM) method was developed to support real-world applications [17].

The RAM method is used to develop the belief revision module of the information agents reported in this paper. The details of the RAM algorithm can be found in [17].

## 3.2. Inducing a user's category preferences

A user's interests can be induced based on a set of documents with category labels assigned by the user. In particular, $D ^ { + }$ and $D ^ { - }$ denote the set of relevant categories and the set of non-relevant categories respectively. The sets $D ^ { + }$ and $D ^ { - }$ can be developed based on the user's direct or indirect relevance feedback (e.g., based on the viewing time of a category of documents). Essentially, three types of categories can be extracted. Positive categories represent what topics the user would like to retrieve; negative categories indicate the topics that the user does not want; neutral categories are not good indicators of user interests.

The following preference induction formula is used to characterise various types of categories and induce the corresponding preference values. It is developed based on the Keyword Classifier which was successfully applied to adaptive information filtering [15].

$$
\text { preference(cat) } = \omega \times \tanh (\frac {d f (\text { cat })}{\text { pos }} \times \Pr (\text { Rel } | \text { cat }))
$$

$$
\times \log_ {2} \frac {\operatorname* {P r} (\text { Rel } | \text { cat })}{\operatorname* {P r} (\text { Rel })} - \frac {d f (\text { cat })}{\text { neg }}
$$

$$
\times \operatorname * {P r} (\mathrm{Nrel} | \text { cat }) \times \log_ {2} \frac {\operatorname* {P r} (\mathrm{Nrel} | \text { cat })}{\operatorname* {P r} (\mathrm{Nrel})}\tag{3}
$$

– cat is a category descriptor.

– pos and neg are the learning thresholds for positive and negative categories respectively.

– tanh is the hyperbolic tangent function.

$\omega { < } 1$ is an adjustment factor for preference induction. $- \ P r ( \mathrm { R e l | c a t } ) = d f ( \mathrm { c a t _ { r e l } } ) / d f ( \mathrm { c a t } )$ is the estimated conditional probability that a category is relevant given that it contains the category descriptor cat. It is expressed as the fraction of the number of relevant documents which contain the category descriptor cat $( \mathrm { i . e . , ~ } d f$ $\left( \mathrm { c a t } _ { \mathrm { r e l } } \right) )$ over the total number of documents which contain the same category descriptor cat (i.e., df(cat)).

$- \ P r ( \mathrm { N r e l | c a t } ) = d f ( \mathrm { c a t _ { n r e l } } ) / d f ( \mathrm { c a t } )$ is the estimated conditional probability that a category is non-relevant if it contains the category descriptor cat.

$- \ \mathrm { P r } ( \mathrm { R e l } ) { = } | \mathrm { D } ^ { + } | / ( | \mathrm { D } ^ { + } | { + } | \mathrm { D } ^ { - } | )$ is the estimated probability that an arbitrary category is relevant.

A positive value of preference(cat) indicates that the underlying category descriptor cat represents a positive category, whereas a negative preference value implies that cat is associated with a negative category. If the absolute preference value of a descriptor is below a threshold λ, the descriptor represents a neutral category. A positive category descriptor is mapped to a positive literal such as $\ell$ , whereas a negative descriptor is mapped to a negated literal such as $\neg { \ell }$ . The entrenchment degree of a belief is computed according to:

$$
B (\alpha_ {\text { cat }}) = \left\{ \begin{array}{c c} \frac {| \text { preference(cat) } | - \lambda}{1 - \lambda} & \text { if   } | \text { preference(cat) } | > \lambda  . \\ 0 & \text { otherwise } \end{array} \right.\tag{4}
$$

Table 4 shows the results of applying the aforementioned preference induction method to the sample category descriptors depicted in Table 3. The last column shows the derived entrenchment degrees associated with the beliefs representing some category descriptors. It is assumed that the parameters $| D ^ { + } | = | D ^ { - } | = 5 , \beta = 0 . 9 5 ,$ λ = 0.3, pos = 5 and neg= 5 are used in the preference induction process. In general, these parameters are estimated based on empirical evaluation against some document collections. As the contents of $D ^ { + }$ and $D ^ { - }$ evolve driven by a user's changing preferences, the entrenchment degrees of corresponding beliefs are raised or lowered in the information agent's knowledge base. The changing epistemic entrenchment ordering of beliefs will then generate different non-monotonic consequence relations which underpin the agent's decisions about category relevance at various points of time.

## 3.3. Reasoning about relevant categories

To determine whether a document should be delivered to a user, the belief revision module first needs to infer if the categories assigned to a document title are relevant or not. More precisely, the degree of relevance of such a category is computed. If a category is not highly preferred by the user, it is less likely that the corresponding document will be recommended to the user. On the other hand, if a category is a preferred one, its degree of relevance will be used as the basis to compute the relevance scores of the documents. Conceptually, the agent's inference process is characterised by $K | \sim \alpha .$ , whereas K denotes the agent's knowledge base; α is a sentence representing one of the descriptors of the category assigned to a document title, and |∼ denotes the non-monotonic inference relation [12].

An entrenchment-based similarity measure $\mathrm { S i m } _ { B } ( \mathrm { U P } , C )$ is developed to approximate the semantic correspondence between a user profile UP and an information category C. The user profile UP is represented by the knowledge base K of an information agent. The similarity measure $\mathrm { S i m } _ { B }$ (UP,C) is defined by:

$$
\operatorname{Sim} _ {B} (\mathrm{UP}, C) = \frac {\sum_ {\ell \in C} [ B (\alpha_ {l}) - B (\alpha_ {\neg \ell}) ]}{| N |}.\tag{5}
$$

The above formula combines the advantages of quantitative ranking and symbolic reasoning in a single framework. The basic idea is that a category C is represented by a set of positive literals (category descriptors) $C { = } \{ \ell _ { 1 } , \ell _ { 2 } { , \ldots } , \ell _ { n } \}$ . If the agent's knowledge base

An example of induced epistemic entrenchment

<table><tr><td>Descriptor</td><td> $df(cat_{rel})$ </td><td> $df(cat_{nrel})$ </td><td>preference(cat)</td><td> $\alpha_{cat}$ </td><td> $B(\alpha_{cat})$ </td></tr><tr><td>business</td><td>5</td><td>0</td><td>0.724</td><td>business</td><td>0.605</td></tr><tr><td>computer</td><td>0</td><td>4</td><td>-0.631</td><td> $\neg$ computer</td><td>0.473</td></tr><tr><td>economy</td><td>3</td><td>0</td><td>0.510</td><td>economy</td><td>0.300</td></tr><tr><td>internet</td><td>0</td><td>2</td><td>-0.361</td><td> $\neg$ internet</td><td>0.087</td></tr><tr><td>commerce</td><td>5</td><td>4</td><td>0.266</td><td>-</td><td>-</td></tr><tr><td>finance</td><td>5</td><td>5</td><td>0</td><td>-</td><td>-</td></tr></table>

K logically entails an atom $\ell _ { i } , :$ a positive contribution is made to the overall similarity score because of the partial semantic correspondence between UP and C. On the other hand, if K implies the negation of a literal $\ell _ { i } { \in } C$ it shows the semantic distance between UP and C. Therefore, the similarity value is reduced by a certain degree. The cardinality of the set N defined by $N { = }$ $\{ \ell \in C | B ( \alpha _ { 1 } ) > 0 \land ( \alpha _ { - \ell } ) > 0 \}$ is used to derive the mean similarity value. Given an agent's knowledge base $K =$ {(¬computer, 0.6), (business, 0.5), (economy, 0.3), (¬internet, 0.2)}, and three categories $C _ { 1 } { = } \{ \mathrm { c o m p u t e r } ,$ internet}, $C _ { 2 } { = } \{ \mathrm { i n t e r n e t . }$ , business}, and $C _ { 3 } = \lbrace { \mathrm { b u s i n e s s } } ,$ economy}, the category similarity scores are as follows:

$$
\begin{array}{c} \operatorname{Sim} _ {B} (\mathrm{UP}, C _ {1}) = - 0. 4; \operatorname{Sim} _ {B} (\mathrm{UP}; C _ {2}) \\ = 0. 1 5; \operatorname{Sim} _ {B} (\mathrm{UP}; C _ {3}) = 0. 4. \end{array}
$$

The final retrieval status value RSV(Doc) for a document title Doc is defined by the product of its information flow score and its category similarity score with cosine normalization. If the retrieval status value of a title is greater than or equal to a pre-defined threshold, the corresponding document will be recommended to the user by the information agent.

$$
\begin{array}{l} \text { RSV(Doc) } \\ = \frac {\sum_ {C \in \text { Doc }} \text { Sim } _ {B} (\text { UP } , C) \times \text { IF(Doc } , C)}{\sqrt {\sum_ {C \in \text { Doc }} (\text { Sim } _ {B} (\text { UP } , C)) ^ {2}} \times \sqrt {\sum_ {C \in \text { Doc }} (\text { IF(Doc } , C)) ^ {2}}}. \end{array}\tag{6}
$$

Assuming that three document titles $\mathrm { D o c } _ { 1 } \colon ( ( C _ { 1 } , 0 . 3 )$ $( C _ { 3 } , 0 . 8 ) ) , \mathrm { D o c } _ { 2 } \colon ( ( C _ { 1 } , 0 . 7 ) , ( C _ { 2 } , 0 . 5 ) )$ , and Doc : $( ( C _ { 2 } , 0 . 4 )$ $( C _ { 3 } , 0 . 3 ) )$ ) are assigned to the categories $\left\{ C _ { 1 } , C _ { 2 } , C _ { 3 } \right\}$ by the classification module, the retrieval status values of these document titles with respect to the agent's current beliefs $K = \{ ( \neg \mathrm { c o m p u t e r } , 0 . 6 )$ , (business, 0.5), (economy, 0.3), (¬internet, 0.2)} regarding the user's preferences can be computed: $\mathrm { R S V ( D o c _ { 1 } ) } { = } 0 . 4 1 , \mathrm { R S V ( D o c _ { 2 } ) } { = } { - } 0 . 5 6 ,$ and $\mathrm { R S V } ( \mathrm { D o c } _ { 3 } ) { = } 0 . 4 7$ . In our example, the classification module is relatively certain that document title Doc is about the category $C _ { 1 }$ (computer and internet) because a high information flow score $\mathrm { I F } ( \mathrm { D o c } _ { 2 } , C _ { 1 } ) { = } 0 . 7$ is derived based on information inference. Nevertheless, the belief revision based user preference prediction module finds that $C _ { 1 }$ is less likely to be a user's favorite $( \mathrm { e . g . , S i m } _ { B } ( \mathrm { U P } , C _ { 1 } ) =$ $- 0 . 4 )$ . Therefore, the overall retrieval status value of document title Doc is less than that of the other document titles in our example. If the document delivery threshold of the intelligent information agent is set to 0.4, the agent will recommend document 1 and document 3 to the user and reject document 2. Such document dispatch decisions have taken into account the user's current information preferences as well as the semantic correspondence between document titles and the information topics (categories).

## 4. Experiments and results

The effectiveness of our intelligent information agent is evaluated empirically based on the Modified Lewis (“ModLewis”) Split of the Reuters-21578 corpus [19] which is a commonly used benchmark collection for text classification. This corpus consists of 13,625 training documents and 6188 test documents. The human indexers have identified 135 topics (categories) and labeled the training documents using these topics.

## 4.1. Experimental set-up

In our experiments, seventeen categories were selected from among the 135 topics. The training documents were extracted, and the pre-labeled topics were removed $( \mathrm { i . e . }$ there is not any explicit topic information in the training set). This training set was then used to construct a HAL space from which information flows could be computed. After removing stop words, the total vocabulary size of the training set was 35,860 terms. In addition, a collection of 1394 test documents, each of which contained at least one of the 17 selected topics, was formed. Similarly, the topic labels were removed from the test set. With respect to the 17 topics, only 14 of them were assigned to at least one test document. Among these 14 topics, five topics had more than 100 relevant documents and four topics had less than 10 relevant documents. The average number of relevant documents over the 14 topics was 107. We deliberately chose this set of topics because they varied from the most frequently used topics like “acquisition” (we use the real English word “acquisition” instead of the original topic “acq” for information flow computation) to some rarely used topics such as “rye” in the Reuters collection. Table 5 lists the selected topics and their relevance information:

A HAL space was constructed from the training documents using a window size of 10 words (L=10). Stemming was not performed during the HAL space construction. For each test document title, the title terms were combined into a single title vector using our concept combination heuristic described in Section 2.

## 4.2. Effectiveness of information flow based classification (IFC)

The aim of this experiment is to test the effectiveness of deriving categories directly from document titles by employing the information flow method. We only used the titles of the test documents. The average title length was 5.38 words. Concept combination was applied to each document title to build the concept corresponding to title. The top 80 Information flows with associated degrees were derived from each title vector. If a topic appeared in the list of information flows derived from a document title, it was assigned to this title.

## 4.3. Effectiveness of hybrid information flow based classification with belief revision (IFC + BR)

This experiment aims to evaluate the contribution of our belief revision module to the overall system effectiveness. We simulated the initial interests of 17 individual users by using the 17 Reuters topics (categories). The top 80 information flows from each category were also included in the simulated user profile. Our evaluation procedure was similar to the one employed by the TREC adaptive filtering task. For instance, after the IFC module assigned the category labels to a document title, these category labels were presented to the belief revision module. The belief revision module then conducted nonmonotonic inference (as described in Section 3.3) to predict the degree of relevance of these categories with respect to a simulated user profile. If the retrieval status value (RSV) of a document was above a pre-defined threshold, it would be dispatched to the user. After making the document dispatch decision, the belief revision module of our system could utilize the simulated user relevance feedback [26] to continuously refine a user profile. A relevance feedback file (as employed by the TREC adaptive filtering task) was used to capture simulated user relevance feedback. This file was developed in advance by parsing the category (topic) labels embedded in the Reuters news documents. With the relevance feedback and user profile revision processes, a more accurate representation of the user's interests could be developed over time. As a result, the precision of the proposed intelligent information agent could be enhanced. Given a specific document collection, the arrival sequence of the incoming document titles will not affect the overall precision of our system because the average precision measure does not take the temporal notion into account.

Table 5 Test topics (categories)

<table><tr><td>Topics</td><td>Number of relevant documents</td></tr><tr><td>acq (acquisition)</td><td>719</td></tr><tr><td>coconut</td><td>2</td></tr><tr><td>coffee</td><td>28</td></tr><tr><td>crude</td><td>189</td></tr><tr><td>grain</td><td>149</td></tr><tr><td>interest</td><td>133</td></tr><tr><td>nickel</td><td>1</td></tr><tr><td>oat</td><td>6</td></tr><tr><td>peseta</td><td>0</td></tr><tr><td>plywood</td><td>0</td></tr><tr><td>rice</td><td>24</td></tr><tr><td>rupiah</td><td>0</td></tr><tr><td>rye</td><td>1</td></tr><tr><td>ship</td><td>89</td></tr><tr><td>sugar</td><td>36</td></tr><tr><td>tea</td><td>4</td></tr><tr><td>trade</td><td>118</td></tr></table>

![](/api/attachments/FBEF7CK9/fulltext/images/37925083c4721a22d55be81dad52e50b68640e35aa95c0ed264596cef4aec624.jpg)  
Fig. 4. SVM: the objective decision function should be the one that separates the positive instances and negative instances with maximum distance.

## 4.4. Comparison with supervised classification approach: support vector machines (SVM)

For a performance comparison of our system with the state-of-the-art supervised learning approaches, we conducted a classification task using Support Vector Machines (SVM), which has been regarded as one of the best performing classifier [38]. SVM follows the structural risk minimization principle from statistical learning theory [14]. The purpose of structural risk minimization is to find a decision function with minimal test error. The decision functions are represented as hyperplanes. Fig. 4 shows the intuition of SVM [3]:

The stars indicate negative instances, and the circles indicate positive instances. The main objective of SVM is to find the decision function D(X) with minimal test error by maximizing the distance between the closest instances to the separating hyperplane (D(X)). In order to obtain the optimal separating hyperplane, one has to solve the following quadratic programming problem by minimizing the following function: $\scriptstyle \varPhi ( W ) = ( W \cdot W ) / 2$ Under the constraints of inequality type such as $y _ { i } =$ $[ ( x _ { i } \cdot W ) + b ] \geq 1 , i = 1 , 2 , . . . , \ell$ , this kind of problem can be solved by Lagrange methods [34]. One of the advantages of SVM is its capability of dealing with the nonlinear separable data set by mapping the data point to another vector space. The following example shows the basic idea of how SVM deals with the nonlinear separable case: there is no way to linearly separate the data set shown in Fig. 5. However, if we map the data points in dimensional space of $( x _ { 1 } x _ { 2 } , x _ { 2 } )$ as shown in Fig. 6, we can find a linear separation function for this data set.

SVM uses a kernel function to transform data set into another vector space. The kernel function represents the inner product of feature space (i.e., the transformed space). The frequently used kernel functions are polynomial function, Radial basis function (RBF), and sigmoid function. For the SVM implementation, we used Lib SVM [7] with the Radial Basis Function (RBF) kernel. The SVM type was set to nu-SVR in order to obtain a regression function for estimating the relevance between a document and a category. After the training documents were fed to SVM, the relevance between a test document and a category could be computed using the regression function generated by the SVM method. For simplicity, the detailed regression function is not shown here. In our experiment, the document/category labeling information was kept in the training set. Two sets of SVM experiments were conducted. The first experiment used full texts while the second experiment utilized titles only in the test set. Note that the SVM was expected to achieve a better result than our unsupervised approach, because the SVM experiment employed labeled training documents.

## 4.5. Experimental results

The major performance measures used in our experiments were Mean Average Precision (MAP) and Average Recall. Precision is the proportion of documents classified with a category that really belong to the category, whereas recall is the proportion of the documents belonging to a category that are actually assigned that category. The MAP is computed across 11 evenly spaced recall points $( 0 , 0 . 1 , 0 . 2 , . . . , 1 . 0 )$ for each category and then averaged over all the categories. The average recall is recall averaged over all the categories. In addition, we measured the efficiency of each system by recording the elapsed time of the classification tasks. All the experimental runs were based on the configuration of a single Pentium III 800 MHz CPU with 1 GB main memory. The experimental results are summarized in Table 6.

![](/api/attachments/FBEF7CK9/fulltext/images/d0ffd1598014c6b4921e59a8c613de42e246fbde599495fceb5d71785c736471.jpg)  
Fig. 5. Nonlinear separable data set.

![](/api/attachments/FBEF7CK9/fulltext/images/b5b049e71b9bc4f50bb81d8ae1ae622fe4065bb9b78e61803f11d52a2c6ae373.jpg)  
Fig. 6. After transformation.

## 4.6. Discussion

First of all, there is no substantial difference among the average recall achieved by all three approaches when classification is conducted based on document titles only. On the other hand, as an unsupervised learning approach, the IFC model performs reasonably well by achieving 77% of the mean average precision produced by the supervised SVM model when both models are applied to document titles only. However, the IFC model is much more efficient than the SVM model. The hybrid IFC and Belief Revision model (IFC+ BR) largely improves the mean average precision by +51% when compared with that achieved by the IFC model alone. This indicates that the belief revision mechanism is more precision-oriented rather than recall-oriented. The computational time of the hybrid (IFC + BR) model is longer due to the fact that belief revision is computationally expensive. However, the average time for processing a document (0.08 seconds) by the BR module is still acceptable and it is less than that consumed by the SVM model.

Table 6  
Experimental results

<table><tr><td>Models</td><td>Average precision</td><td>Average recall</td><td>Average elapsed time (per topic)</td></tr><tr><td>IFC (on test document titles)</td><td>0.461</td><td>0.858</td><td>28 s</td></tr><tr><td>IFC+BR (on test document titles)</td><td>0.698</td><td>0.861</td><td>116 s</td></tr><tr><td>SVM (on whole test documents)</td><td>0.818</td><td>0.977</td><td>420 s</td></tr><tr><td>SVM (on test document titles)</td><td>0.601</td><td>0.878</td><td>394 s</td></tr></table>

The hybrid (IFC+BR) model demonstrates a comparable effectiveness to the SVM model when full texts are used. Moreover, the hybrid (IFC+BR) model outperforms the SVM model if document titles are used. This result is noteworthy since our approach does not require any manually labeled training data as the SVM does. Furthermore, we have observed that the training process for SVM is computationally expensive (about three days in our experiments). As a consequence, our approach will be more feasible for data intensive domains where manual labeling of training data is almost impossible (even if it is possible for manual labeling, the training time consumed by SVM is prohibitively expensive). As the HAL space has an additive property, it can be built and enriched accumulatively without the need of additional pre-labeled training data.

## 5. Related work in intelligent information agents

WebWatcher [13] is an intelligent browsing agent which recommends hyperlinks to a user while the user is browsing the Web. When an agent is initialized, the user is asked to specify their information interests (i.e., a query) in terms of a set of keywords. Feature extraction is conducted by extracting words from a query or annotated hyperlink of a Web page with high TFIDF [28] scores. If there is a significant overlapping between a query and an annotated hyperlink measured in terms of the cosine similarity score of the corresponding TFIDF vectors, the WebWatcher agent will recommend the user to follow that particular hyperlink. One drawback of the WebWatcher agent is that a large number of labeled training Web documents must be available to train the WebWatcher agent before the agent can accurately recommend promising hyperlinks. Our intelligent information agent does not require labeled training documents to construct an effective classifier.

In order to alleviate the problem of information overload, a general architecture of intelligent information agents is proposed [33]. The main functionalities of the intelligent information agents include intelligent search, navigation guide, auto-notification, personal information management, and dynamic personalized Web page retrieval. The underlying document representations and classification modules of the intelligent information agents are based on the vector space model [28]. For instance, a Web document is represented by a vector of terms weights, and the match of a Web document with respect to a query is measured in terms of their inner product. A user profile consists of a set of categories representing a user's diverse interests; each category is indeed the mean vector computed based on a set of Web documents in which the user is interested. Similarly, Shaw et al. have proposed an agent-based architecture for intelligent information retrieval in a distributed heterogeneous information environment [29]. The prototype system is called AgentRAIDER. Their work mainly focuses on the architectural aspects of distributed intelligent information agents rather than the computational mechanisms which are used to develop such agents [29]. Our work presented in this paper illustrates both the architectural aspects and the computational details for the development of intelligent information agents. More specifically, we concentrate on document classification and dynamic user profiling among the other functionalities of intelligent information agents referred to in [29,33]. Our agent classification model is based on the novel information flow based inference method [30,31] rather than the commonly used vector space model. In addition, dynamic user profiling rather than static user profiling is supported by our intelligent information agents.

Fan et. al. have developed a two-stage model for personalized and intelligent information routing of online news [9]. At the first stage, persistent user queries are extracted from rated documents based on Robertson's Selection Value (RSV). At the second stage, genetic programming is applied to discover the optimal ranking function for individual user. Their system outperforms BM25 (Okapi) [27] and support vector machine (SVM) based routing models evaluated based on the TREC-AP and the TREC-Web datasets respectively. Nevertheless, as indicated in their paper [9], one limitation of the two-stage routing model is that supervised training data must be collected from the users. Moreover, a static rather than a dynamic user profile is assumed. Our research work alleviates these two problems.

Chan and Chong have developed an unsupervised classification model for non-textual Web information (e.g., images) retrieval [6]. Different image feature vectors have been constructed and evaluated. The particular unsupervised image classification model is developed based on the Kohonen self-organizing map (SOM). The performance of the SOM classification model is compared with that of the Hierarchical Agglomerative Clustering (HAC) based on hundreds of images. It is found that the SOM classification model can produce effective clusters of semantically related images. Our proposed information classification model is also based on unsupervised learning. However, it is developed according to a novel information inference mechanism and it is applied to textual data rather than image retrieval. Moreover, belief revision logic is employed to support dynamic user profiling in our approach.

Pazzani and Billsus [25] developed a learning information agent called Syskill & Webert which could learn a user profile for the identification of interesting web documents. A separate user profile was created for each individual information topic. Web documents were represented as Boolean feature vectors, and each feature had a binary value indicating if a particular keyword appeared in the document or not. Feature selection was conducted based on Expected Information Gain which tends to select words appearing more frequently in positive documents. The classification mechanism of Syskill & Webert was based on a naïve Bayesian classifier. Supervised learning was employed to train the classifier. Apart from the naïve Bayesian classifier, several other classification approaches such as Nearest Neighbor algorithm, Decision Trees, Rocchio's method, and Neural Networks were also evaluated. Our information flow based classification agents differ from the Syskill & Webert agents in that users rated training documents are not required to train the agents. As a result, our agents are more autonomous and they can operate with minimal human intervention.

Amalthaea is an adaptive multi-agent system for information discovery and filtering [24]. The agent system could learn a user's information preferences by examining the user's browsing history or obtaining direct relevance feedback from the user. Essentially, the vector space model was used to represent a user's information preferences as well as web documents. Based on genetic algorithms, the Amalthaea agents could evolve to adapt to the user's changing information needs. Moreover, the agents could explore the potential information topics not explicitly requested by the user by means of genetic operators such as mutation and cross-over. However, as described in their paper [24], it might take many generations of agent evolution before a user's information preferences could be learnt. Furthermore, for each generation of agent evolution, users needed to rate an exhaustive list of web documents. This is in fact a quite labor intensive and time consuming process.

## 6. Conclusions

This paper illustrates the development and evaluation of an agent-based document classification and filtering system. The document classification module of the agent employs an associational inference mechanism driven by information flow computation. In addition, the dynamic user profiling and filtering mechanism is underpinned by the AGM belief revision logic. It is demonstrated that the inferential capability of information flow computation is complementary to the non-monotonic reasoning capability of the belief revision module. By combining these two powerful mechanisms, the proposed intelligent information agents are highly autonomous and efficient since they can accurately classify electronic documents based on document titles only. Experimental results based on the Reuters-21578 corpus show that the proposed IFC classification module demonstrates comparable performance to the SVM model which is regarded as one of the best-performing supervised classification approaches. When the IFC module is combined with the belief revision module, our hybrid approach outperforms the SVM method in terms of both precision and efficiency. Unlike the SVM model, one major advantage of our document classification mechanism is that it does not require any pre-labeled training data. In the future, larger benchmark document collections will be used to further evaluate the effectiveness and efficiency of our intelligent information agents.

## Acknowledgements

This work is funded in part by the UK's Engineering and Physical Sciences Research Council (EPSRC), grant number EP/E002145/1 and Overseas Travel Grant number EP/E037402/1.

## References

[1] C.E. Alchourrón, P. Gärdenfors, D. Makinson, On the logic of theory change: partial meet contraction and revision functions, Journal of Symbolic Logic 50 (1985) 510–530.

[2] J. Barwise, J. Seligman, Information Flow: The Logic of Distributed Systems, Cambridge Tracts in Theoretical Computer Science 44 (1997).

[3] B.E. Boser, I. Guyon, V. Vapnik, ATraining Algorithm for Optimal Margin Classifiers, Proceedings of the 5th Annual Workshop on Computational Learning Theory, 1992, pp. 144–152.

[4] P.D. Bruza, D. Song, Inferring Query Models by Computing Information Flow, Proceedings of the 12th International Conference on Information and Knowledge Management (CIKM2002), 2002, pp. 260–269.

[5] C. Burgess, K. Livesay, K. Lund, Explorations in context space: words, sentences, discourse, Discourse Processes 25 (2&3) (1998) 211–257.

[6] S. Chan, M. Chong, Unsupervised clustering for nontextual web document classification, Decision Support Systems 37 (3) (2004) 377–396.

[7] C. Chang, C. Lin, LIBSVM: A Library for Support Vector Machines , 2001 Software available at http://www.csie.ntu.edu.tw/\~cjlin/libsvm.

[8] B.V. Dasarathy, Nearest Neighbor (NN) Norms: NN Pattern Classification Techniques, IEEE Computer Society Press, 1991.

[9] W. Fan, M. Gordon, P. Pathak, An integrated two-stage model for intelligent information routing, Decision Support Systems 42 (1) (2006) 362–374.

[10] P. Gärdenfors, Conceptual Spaces: The Geometry of Thought, MIT Press, 2000.

[11] P. Gärdenfors, D. Makinson, Revisions of Knowledge Systems Using Epistemic Entrenchment, Proceedings of the Second Conference on Theoretical Aspects of Reasoning About Knowledge, 1988, pp. 83–95.

[12] P. Gärdenfors, D. Makinson, Nonmonotonic inference based on expectations, Artificial Intelligence 65 (2) (1994) 197–245.

[13] T. Joachims, D. Freitag, T. Mitchell, Webwatcher: ATour Guide for the World Wide Web, Proceedings of the fifteenth International Joint Conference on Artificial Intelligence, 1997, pp. 770–775.

[14] T. Joachims, A Statistical Learning Model of Text Classification for Support Vector Machines, Proceedings of the 24th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, 2001, pp. 128–136.

[15] T. Kindo, H. Yoshida, T. Morimoto, T. Watanabe, Adaptive Personal Information Filtering System that Organises Personal Profiles Automatically, Proceedings of the Fifteenth International Joint Conference on Artificial Intelligence, 1997, pp. 716–721.

[16] R. Lau, The state of the art in adaptive information agents, International Journal on Artificial Intelligence Tools 11 (1) (2002) 19–61.

[17] R. Lau, Context Sensitive Text Mining and Belief Revision for Adaptive Information Retrieval, Proceedings of the 2nd IEEE/WIC International Conference on Web Intelligence (WI'03), October 13– 17, 2003, IEEE Press, Halifax, Canada, 2003, pp. 256–262.

[18] D. Levy, Users and Interaction Track: Memex and Hypertext: To Grow in Wisdom: Vannevar Bush, Information Overload, and the Life of Leisure, Proceedings of the 5th ACM/IEEE-CS Join Conference on Digital Libraries, 2005, pp. 281–286.

[19] D. Lewis, Reuters-21578 Corpus, http://www.daviddlewis.com resources/testcollections/reuters21578/2003.

[20] K. Lund, C. Burgess, Producing high-dimensional semantic spaces from lexical co-occurrence, Behavior Research Methods, Instruments, & Computers 28 (2) (1996) 203–208.

[21] P. Maes, Agents that reduce work and information overload, Communications of the ACM 37 (7) (1994) 31–40.

[22] F. Menczer, R. Belew, Adaptive retrieval agents: internalizing local context and scaling up to the Web, Machine Learning 39 (2–3) (2000) 203–242.

[23] T. Mitchell, Machine Learning, McGraw Hill, 1996.

[24] A. Moukas, P. Maes, Amalthaea: an evolving information filtering and discovery system for the WWW, Journal of Autonomous Agents and Multi-Agent Systems 1 (1) (1998) 59–88.

[25] M. Pazzani, D. Billsus, Learning and revising user profiles: the identification of interesting web sites, Machine Learning 27 (3) (1997) 313–331.

[26] J. Rocchio, Relevance feedback in information retrieval, in: G. Salton (Ed.), The SMART Retrieval System: Experiments in Automatic Document Processing, 1971, pp. 313–323.

[27] S.E. Robertson, S. Walker, K. Sparck-Jones, M.M. Hancock-Beaulieu, M. Gatford, OKAPI at TREC-3, Proceedings of the 3rd Text Retrieval Conference (TREC-3), 1995.

[28] G. Salton, M. McGill, Introduction to Modern Information Retrieval, McGraw-Hill, 1983.

[29] N. Shaw, A. Mian, S. Yadav, A comprehensive agent-based architecture for intelligent information retrieval in a distributed heterogeneous environment, Decision Support Systems 32 (4) (2002) 401–415.

[30] D. Song, P.D. Bruza, Discovering Information Flow Using a High Dimensional Conceptual Space, Proceedings of the 24th Annual International Conference on Research and Development in Information Retrieval (SIGIR'01), 2001, pp. 327–333.

[31] D. Song, P.D. Bruza, Towards a theory of context sensitive informational inference, Journal of American Society for Information Science and Technology 54 (4) (2003) 326–339.

[32] D. Song, P.D. Bruza, Z. Huang, R. Lau, Classifying Document Titles Based on Information Inference, Proceedings of the 14th International Symposium on Methodologies for Intelligent Systems (ISMIS'2003) Conference, 2003, pp. 297–306.

[33] H.-C. Tu, J. Hsiang, An architecture and category knowledge for intelligent information retrieval agents, Decision Support Systems 28 (3) (2000) 255–268.

[34] V. Vapnic, The Nature of Statistical Learning Theory, Springer, 1995.

[35] M.A. Williams, Iterated Theory Base Change: A Computational Model, Proceedings of the Fourteenth International Joint Conference on Artificial Intelligence (IJCAI'1995), 1995, pp. 1541–1547.

[36] M.A. Williams, Anytime Belief Revision, Proceedings of the Fifteenth International Joint Conference on Artificial Intelligence (IJCAI'1997), 1997, pp. 74–79.

[37] K.F. Wong, D. Song, P.D. Bruza, C.H. Cheng, Application of aboutness to functional benchmarking in information retrieval, ACM Transactions on Information Systems 19 (4) (2001) 337–370.

[38] Y. Yang, X. Liu, A Re-examination of Text Categorization Methods, Proceedings of ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR'99), 1999, pp. 42–49.

Dr. Dawei Song is a Senior Lecturer at the Knowledge Media Institute, the Open University, United Kingdom, since 2005. He obtained his Ph.D. in information systems from the Chinese University of Hong Kong in 2000. During 2000–2005, he worked in the Distributed Systems Technology Centre at the University of Queensland, Australia. His research interests include various theoretical and practical aspects of context-sensitive information retrieval, such as applied logic and language modelling for query expansion and relevance feedback. He has been publishing papers on well-respected journals and conferences, including ACM Transactions on Information Systems, Journal of American Society for Information Science and Technology, ACM SIGIR and ACM CIKM conferences.

![](/api/attachments/FBEF7CK9/fulltext/images/899ffd04454e7643cf18b2901dbb249cc53a6342dcbb179a1b041136f3978462.jpg)

Raymond Y.K. Lau, Ph.D. Dr Raymond Lau is currently the Program Leader of the Bachelor (Honors) degree in Electronic Commerce offered by the department of Information Systems at City University of Hong Kong. He was a lecturer at Queensland University of Technology in Australia before joining City University. He also worked as a research officer at the Australian Commonwealth Government's Scientific & Industrial Research Organisation (CSIRO) and

participated in nationwide software process improvement projects. He holds a Ph.D. in Information Technology, a M.Sc. in Business Systems Analysis and Design, and a MApp.Sc. in Information Studies. Dr Lau's research interests include Information Retrieval, Text Mining, Web Data Mining, and Agent-Mediated e-Commerce. He is the author of more than 50 refereed international journals and conference papers. His research work has been published in international journals such as International Journal of Cooperative Information Systems, Journal of Applied Non-Classical Logic, International Journal of Intelligent Systems, Web Intelligence and

Agent Systems, etc. He is the technical editor of the Journal of Asian Information Management and the guest editor of the International Journal of Knowledge and Learning.

Peter Bruza is a Professor of Information Systems at the Queensland University of Technology, Australia. Before this appointment he was a project leader in the Distributed Systems Technology Centre, based at UQ. During this time he was chief scientist behind www.guidebeam. com, a next generation Internet search technology which was successfully commercialized and deployed in numerous government departments in Australia and overseas. Peter Bruza is holder of a doctorate in computer science and mathematics from the University of Nijmegen, The Netherlands (1993). He has made major theoretical contributions to information retrieval and applied logic. In the last five years, Peter Bruza has been pioneering a line of research into subsymbolic reasoning using semantic space models. In recognition of this ground breaking work he was appointed to the editorial board of the Journal of Applied Logic (Elsevier) in the area of “human reasoning”. He has been Program committee chair of ACM SIGIR 2004.

Prof. Kam-Fai Wong is a Professor in the Department of Systems Engineering and Engineering Management, the Chinese University of Hong Kong. His research interest focuses on Chinese computing, database and information retrieval. He has published over 160 technical papers in these areas. He is the founding Editor-In-Chief of ACM Transactions on Asian Language Processing (TALIP), co-Editor-in-Chief of International Journal on Computer Processing of Oriental Languages. He has also chaired or served as Program Committee member of many international conferences, such as SIGMOD and CIKM.

Dr. Ding-Yi Chen is a postdoc research fellow at the School of Information Technology and Electrical Engineering, University of Queensland, Australia. His research interests are data mining, document classification, knowledge discovery and information retrieval.
