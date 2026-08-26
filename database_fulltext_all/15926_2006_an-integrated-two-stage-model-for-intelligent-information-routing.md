---
otero_id: 15926
otero_key: "DBWF2B2Y"
title: "An integrated two-stage model for intelligent information routing"
authors: "Weiguo Fan; Michael D. Gordon; Praveen Pathak"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.01.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An integrated two-stage model for intelligent information routing

Weiguo Fan <sup>a</sup>, Michael D. Gordon <sup>b</sup>, Praveen Pathak

<sup>a</sup> Virginia Polytechnic Institute and State University, United States h University of Michigan, United States

Available online 5 March 2005

## Abstract

A recent surge of subscriptions to online news services exemplifies the fact that people and organizations constantly need up-to-date information to stay competitive and make better informed decisions. However, many of these news services often require users to either manually input their profiles or subscribe to existing news channels. This results in lack of intelligence and personalization, and thus make these services less attractive to users. In this paper, an integrated model that combines query expansion with ranking function adaptation for online information routing is proposed and tested using two different large scale corpora. The experimental results show that this new model can deliver much better quality information than existing models. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Information routing; Information retrieval; Personalization; Genetic programming; Text mining

## 1. Introduction

In the current fast-changing world, information is treasure, money, and the source of knowledge. Delivering the right information to the right people at the right time not only can help people make better decisions, but also can dramatically reduce the associated opportunity cost due to wrong or missed information. Many online information routing services, such as MyYahoo<sup>1</sup> and Google<sup>2</sup> strive to provide such information monitoring and delivery service to millions of end users to help keep them aware of current events and stay competitive. Many organizations utilize corporate portals to manage increasingly available structured and unstructured information. Targeted information routing<sup>3</sup>, or information push, is frequently an integrated part of such a portal system [1,20]. We will see more and more such routing applications deployed by organizations in the future to deliver timely information to their customers or employees.

However, these services often are less attractive and useful to users due to the lack of personalization and intelligence [2,10]. Here, personalization is defined as a process used by a computer system to proactively profile and learn a user’s interest and deliver useful information to a particular user based on its findings. Intelligence is defined as automatic adaptation of a service based on implicit behavior observation and learning, instead of explicit solicitation from users. As Peter Dushkin, an analyst with Jupiter Communications L.L.P., put it, <sup>b</sup>Push often delivers way too much information. In the future, we will see more personalization and search engines partnered with push<sup>Q</sup> [21].

What does this message convey for information professionals? What is wrong with the current information push/routing services? A closer examination of the current practices of existing information routing services reveals shortcomings in two major areas a) Capture and Representation of User Need and b) Matching Process. We will discuss in detail these shortcomings in the next section. In the area of capturing and representing the user information need, the current methods require users’ direct input to represent their information need which may place too much of a burden on users. In the area of matching processes past research [30,33] shows that a single ranking function is inadequate.

Hence there is no reason to believe that current routing services have adopted optimal solutions for the matching process.

## 1.1. Research goal

In this paper we present architecture for routing/ pushing information using an integrated two-stage process model for routing services. Instead of requiring a user to specify what she wants, the new twostage model can implicitly construct a user’s persistent query (stage 1) and discover its corresponding ranking function (stage 2) in a systematic and automatic way. A user’s profile consists of these two key elements—a user’s persistent query and its corresponding ranking function. Such a user profile provides the foundation for later information routing. The two-stage model is empirically validated by comparing our model with existing systems using two different large text collections. To our knowledge such an integrated approach to information routing has not been addressed in literature.

Our paper is organized as follows: in Section 2, we first discuss in detail some of the shortcomings in the existing information routing services. Then we outline some of the required background on query construction and ranking function used in the matching process. In Section 3, we present the routing architecture and our proposed two-stage routing model; Section 4 shows the results of two experiments to test this model and Section 5 concludes the paper and points out future research directions.

## 2. Background

In this section we first discuss in detail the shortcomings in the current practices in information routing services. Then we proceed to review related work in personalized query and personalized ranking function. Before we proceed, we would define Persistent Query (PQ) to be a query that represents a user’s long-term standing information need. This PQ will be used later on in the paper when we describe our integrated model for information routing.

2.1. Shortcomings in existing information routing services

As mentioned earlier, a closer examination of the current practices in information routing services reveals shortcomings in two major areas a) Capture and Representation of User Need and b) Matching Process. We now discuss these shortcomings.

## 2.1.1. Capture and representation of user need

There are two typical ways for routing services to solicit and capture a user’s information need:

(a) Method 1: Explicit Bag-of-Words approach.

In this method [3,4], when a user first registers for a routing service, she has to explicitly specify her interest using a set of keywords. Thus it is often called the Bag-of-Words approach. For example, when a user wants to keep track of information related to the recent investment in Japan by any US company, she can register the following keywords with a routing service: <sup>b</sup>United States Investment in Japan<sup>Q</sup>. The routing system will match any future information against this set of words and deliver the information to the user if the information matches the profile. Some routing systems allow more advanced features, such as Boolean expressions—AND, OR, NOT—to be used in the PQ specification.

(b) Method 2: Explicit Subject/Category/Channel approach.

Another method [15,23] would be to ask a user to choose topics from a set of pre-defined categories, subjects, or channels. These categories can be very broad, such as <sup>b</sup>Sports<sup>Q</sup>, <sup>b</sup>News<sup>Q</sup>, <sup>b</sup>Weather<sup>Q</sup> <sup>b</sup>Finance<sup>Q</sup>, etc. Within each category, there may be some fine-tuned sub-categories. For example, in the main category of <sup>b</sup>Finance<sup>Q</sup>, its sub-categories may include: <sup>b</sup>Personal Finance<sup>Q</sup>, <sup>b</sup>Insurance<sup>Q</sup>, <sup>b</sup>Employment<sup>Q</sup>, etc. The hierarchy of the categories/subjects can be quite large. Once a user finds a category in a specific level that meets his/her requirement, the user can request the routing system to store the selected category as his/her interest.

Although either of these methods may work well for certain users with advanced domain knowledge or for certain popular topics, these methods may pose problems for other scenarios:

<sup>!</sup> For Method 1, most users do not know how to formulate a good PQ that can represent their long term interests or needs. For instance, in the Method 1 example, the PQ representation—<sup>b</sup>United States Investment in Japan<sup>Q</sup>—might find a lot of matches but very little information useful to a user. Why? Because the query is not formulated properly. For example, documents about US investing policy in Japan can match the query but are certainly not what the user is looking for because these documents are about investing policy, not about investment examples. Ultimately, through trial and error, it will take a user much longer than expected to find a good query. By the time the user finds such a query, she may already have been frustrated enough to give up this kind of service. The same scenario happens all the time in traditional ad hoc information retrieval contexts when users fail to formulate a good query to get the information they want [29].

In fact, this problem is a classic problem in human computer interaction—the so-called <sup>b</sup>Vocabulary Problem<sup>Q</sup> [9]—in which case users have a hard time selecting the right words to communicate with a computer system. In order to make a routing system work, a PQ cannot be too broad; otherwise, a routing system will deliver too much non-relevant information to a user. Nor can a PQ be too specific because a user will miss a lot of valuable information with a very specific query. Finding a good query of reasonable specificity is never a trivial task in human computer interaction.

<sup>!</sup> For Method 2, there are at least three major issues: a) Lack of precision in the subject taxonomy design. Designing good subject taxonomy is not an easy task. Often, the subject or category a user selects may not be precise enough, suffering from the same vocabulary problem as a broad query formulation in Method 1.

b) Longer learning curve for end users.

Users often do not know the scope of a particular category. For example, in order to know what the category <sup>b</sup>Finance<sup>Q</sup> means, a user has to click many times to know the topics covered under <sup>b</sup>Finance<sup>Q</sup>. Getting users to familiarize themselves with the subject taxonomy often demands domain expertise and may take longer time than a simple keyword search as in Method 1. So the learning curve for users to use such a system is very high. There might be cases where users will not be able to find any suitable category to represent their information need, which means the routing system will become totally useless in these cases.

c) Mis-classification of information (the ontology problem).

Even though the subject hierarchy is precise enough, the information that a user looks for may fall in a different subject category due to the discrepancy between the system designer and the end user.

In summary, either of the above mentioned methods require users’ direct input to represent their information need. This may place too much burden on users, especially for users who often fail to know how to formulate a good PQ to express their interests, as in the <sup>b</sup>US investment in Japan<sup>Q</sup> example. A more intelligent way of capturing and representing a user’s interest is needed.

## 2.1.2. Matching process

In order for a routing system to work, it needs not only a proper representation of a user’s long-term interest, but also a mechanism that helps decide whether new information matches a user’s interest.

For proprietary reasons, details are not known about how commercial systems handle the matching process. In routing research literature, however, most routing systems use a single fixed ranking function to decide the relevance of new information against a user’s PQ. The same fixed ranking function is used for all user queries—so-called <sup>b</sup>consensus ranking<sup>Q</sup>—in which the computed relevancy for the entire population is presumed relevant for each user [22].

One of benefits of <sup>b</sup>consensus ranking<sup>Q</sup> is that all users get the same results, which fosters result-sharing [22]. However, there are many other cases where users prefer search results to be tailored to their own personal preference | the so-called personalized search or ranking [22]. This is especially valuable in the routing context where personalized information delivery is highly desired.

In fact, past research work on ranking function studies demonstrates that a single ranking function does not work well for all user queries [30,33]. The performance of a ranking function often depends on the application context<sup>4</sup>. With all this evidence, there is really no reason to believe that current routing services have adopted optimal solutions for the matching process.

## 2.2. Related work in personalized query and personalized ranking function

We mentioned earlier that two key components exist in the proposed routing system:

a) a persistent query (PQ) that represents a user’s long-term standing information needs. These needs are assumed to be relatively stable and valid within a certain period of time.

b) a personalized ranking function that estimates the relevance of incoming new in-formation.

Note that our model differs from traditional routing systems in that not only is a user’s persistent query stored in a user profile, but also the corresponding ranking function for the PQ is stored as a part of user profile. We will now review related work in both areas.

## 2.2.1. Persistent query construction and representation

Two kinds of PQs are commonly used: explicit and implicit [8,19]. Explicit PQs are provided by users themselves, while implicit PQs are constructed by systems automatically, based on users’ relevance feedback, using a training set of documents or by observing a user’s actions on the information pushed by these services [19]. In this paper, explicit PQs and implicit PQs are also called user-provided PQs and system-constructed PQs, respectively.

Most commercial routing systems, such as Yahoo, PointCast, BackWeb, Google etc., utilize only userprovided PQs in their services. As discussed earlier user-provided PQs are at least partially responsible for the unsatisfactory performance of these services due to the so-called vocabulary problem [9]. Systemconstructed PQs, on the other hand, do not suffer from this problem. In fact, system-constructed PQs have been found to be able to capture more accurately and effectively users’ long term information needs than user-provided PQs [8,19]. We will focus our discussion in this section on various system-constructed PQ approaches. User-provided PQs will be used as a benchmark for later experimental comparison.

To create a system-constructed PQ for a user, most PQ construction algorithms learn a set of features (words) that may potentially help distinguish relevant documents from the non-relevant documents [24]. Based on the occurrences of these features in a new document, this new document can either be considered potentially useful and be routed to the user or can be considered non-relevant and be discarded. Most algorithms also assign weights to these features for relevance estimation. To learn the features and their weights, these algorithms use the probability of occurrences (or some variations of it) of a feature in both the documents marked relevant and those marked non-relevant by a user in a training corpus [24]. The idea is that if a feature occurs with a high probability in the relevant documents but with a low probability in the non-relevant documents, then this feature is a good indicator of relevance and should be assigned a high weight in a user PQ. On the other hand, if such a feature occurs with a low probability in relevant documents but with a high probability in non-relevant documents, then this feature is not a good indicator of relevance and should be assigned a low weight in the PQ or should not even be included in the PQ at all.

There are two types of methods commonly used in PQ construction. One type of method is the wellknown relevance feedback method, which originated in traditional ad hoc IR. These include the classic Rocchio’s relevance feedback formula based on the vector space model [27], Robertson’s selection value (RSV) formula based on probabilistic theory [25], and the document relevance correlation (DRC) based on the vector space model [8]. The other type of method is the feature selection method from machine learning literature. The machine learning methods include information gain (IG) based on information theory [17], Chi-square test and its square root version, the correlation coefficient (CC) [18]. Other feature selection methods are discussed in [12,16].

Although most of these methods differ from each other in mathematical form due to their different origin, they are all based on probabilistic properties of words. Moreover, the PQ construction process can be done independently of the later ranking process. The implication of this property is that we can decouple the effects of ranking function on PQ construction and thus make the two-stage model (PQ construction and ranking function discovery) possible.

## 2.2.2. Ranking function

The objective of a ranking function is to match new incoming documents or information to a user’s PQ and place them in descending order of their predicted relevance to a user’s information requirement. To facilitate this relevance estimation process, both the incoming documents and a user’s PQ need to be transformed into a form that can be effectively processed by computers. One of the most successful models is the so-called Vector Space Model (VSM) [28,29].

The VSM is chosen to be the underlying model for this study due to its ease of interpretation [29] and great success in various performance evaluations [11,30]. Moreover, most existing search engines and information retrieval systems are based on this model.

More specifically, both documents and PQs are represented as vectors in the VSM. Suppose there are total t index terms in an entire collection, a given document D and query Q can be represented as follows:

$$
D = \left(w _ {d 1}, w _ {d 2}, w _ {d 3}, \dots , w _ {d t}\right)
$$

$$
Q = \left(w _ {q 1}, w _ {q 2}, w _ {q 3}, \dots , w _ {d t}\right)
$$

where $w _ { d i } , w _ { q i } ( i { = } 1 \mathrm { ~ t o ~ } t )$ are term weights assigned to different terms for the document D and query Q respectively. The similarity between a query and a document can be calculated by the widely used cosine measure [30]:

$$
\text { Similarity } (Q, D) = \frac {\sum_ {i = 1} ^ {t} w _ {q i} \times w _ {d i}}{\sqrt {\sum_ {i = 1} ^ {t} \left(w _ {q i}\right) ^ {2} \times \sum_ {i = 1} ^ {t} \left(w _ {d i}\right) ^ {2}}}\tag{1}
$$

Documents are then ordered by decreasing values of this measure and presented tothe user.

There are various features available in the VSM to compute the term weights— $\ – w _ { d i } , w _ { q i } ( i { = } 1 \ \mathrm { t o } \ t )$ . One of the most widely used features for term weighting is Term Frequency (TF), which measures the number of times a term appears in a document or query. Another commonly used feature, measuring the rarity of a term in a collection, is the Inverse Document Frequency (IDF) which can be calculated by log(N / DF), where N is the total number of documents in a text collection, and DF measures the number of documents in which the term has appeared at least once. More features used in term weighting can be found in [29,30]. These features can also be combined to generate a wide range of new composite term weighting strategies, e.g., TF \* IDF, etc.

## 3. Routing architecture and a two-stage information dissemination model

Following the discussion above it is clear that both the PQ representation and the ranking function used for matching are very important for the performance of a routing system for each individual interest. In order to deliver high quality information to an end user, both the PQ and the ranking function need to be carefully designed and constructed. Obviously, the current routing mechanisms require a lot of user input and intervention and do not provide an optimal routing solution to satisfy the information needs of end users. A better scheme for information routing is needed.

In this section we first present the overall architecture for information routing and see where our two-stage model for user profile generation fits in. Later we discuss the two-stage model in details.

## 3.1. Information routing architecture

Information routing architecture is presented in Fig. 1 (part a) along with our two-stage model for creating user profile (part b). The aim of information routing is to prioritize incoming (unseen) documents and present the documents according to the decreasing order of priority. The documents are prioritized based on the calculated score for each document. The score for each document is calculated using some query and some matching function to match the query with the incoming document. From this paper’s perspective the user query is the PQ and the matching function is the personalized ranking function (RF) for the user. The PQ and RF together form the user profile and documents are routed based on the score produced by such a personalized user profile. As can be seen from the figure, the PQ and RF are the products of a process for creating user profile (part b). We will next discuss the two-stage model we developed for creating such a user profile.

## 3.2. The two-stage model for user profile creation

We propose a new two-stage model for creating user profile as shown in part b of Fig. 1. We now discuss each of these stages.

## 3.2.1. Stage 1: representing a user’s real information need: construct the persistent query

A major problem of existing routing services is that they require direct solicitation of a user’s interest. This, as argued in Section 1, often results in poor service quality and poor user satisfaction due to a user’s inability to create good PQs. Instead of asking a user to explicitly specify her need, an indirect method using some sample information with user feedback could be used. Therefore, in Stage 1, an implicit method for query construction—the query by selected samples approach [24]—is recommended to capture a user’s real information need. In this approach, a set of training documents with known relevance information are provided by an end user to assist the process of user need capture and representation. Alternatively, the set of training documents can be obtained by monitoring a user’s click-stream behavior.

![](/api/attachments/DBWF2B2Y/fulltext/images/66ac41ce6109caec23532c0ee431454a35be07733ef8c2b4aecc68a93007bbe7.jpg)  
b) Creatin g User Profile (PQ, RF)  
Fig. 1. Information routing architecture and user profiles.

To build a user’s PQ (system constructed PQ in Table 1) using the training doc-uments provided, we need to decide which terms to put in the PQ. We decided to use Robertson’s Selection Value (RSV) [24] formula as the PQ construction method due to its superior performance and its less dependence on matching process [8]. The steps of building a PQ are as follows:

1) Extract all terms from relevant documents;

2) Apply the RSV formula to each term and obtain a score of v<sub>j</sub>;

3) Rank all terms j, based on v<sub>j</sub>;

4) Select the top k (user parameter) ranked terms as the PQ. Use the term fre-quency of the terms to weigh these terms.

## 3.2.2. Stage 2: learning a user’s ranking preference towards information: adaptively discover the personalized ranking function using genetic programming

Successful construction of the PQ is only the first step towards the success of information routing. After we construct the PQ we need to decide how to effectively match the PQ with new incoming documents by taking account of each user’s personal ranking preference. For example, some information relevant to John may not be relevant to Mary even though they both might look for information on the same topic [32]. We need to take this into consideration when we design the ranking function.

So the purpose of the second stage is to adaptively discover the <sup>b</sup>optimal<sup>Q</sup> ranking function to approximate a user’s relevance judgment criteria. An inductive learning technique—Genetic Programming (GP)—is used for the ranking function discovery [7].

Input and output information for different stages of the two-stage model

<table><tr><td>Stage</td><td>Input</td><td>Output</td></tr><tr><td>Stage 1</td><td>Feedback data</td><td>System-constructed PQ</td></tr><tr><td>Stage 2</td><td>Feedback data+system-constructed PQ</td><td>Personalized RF</td></tr></table>

The detailed specification of the two-stage model regarding the input and output of each stage is shown in Table 1.

Note that Stage 1 is done independently of Stage 2 since the PQ construction requires only term distribution information in the training documents. The feedback training data (the sample documents with relevance information) combined with the output from Stage 1—System-Constructed PQ—is used as the input for Stage 2 to discover the personalized ranking function (RF).

Since the existence of the best/optimal ranking function is never known a priori, we use the ranking function discovery framework [7] to discover the personalized ranking function. The idea of the discovery framework is to encode each candidate ranking function as a <sup>b</sup>ranking tree<sup>Q</sup> and to use genetic programming to adaptively evolve these <sup>b</sup>ranking trees<sup>Q</sup> to discover an optimal ranking function according to certain performance measures.

The detailed description of the personalized ranking function discovery framework based on Genetic Programming is summarized in Fig. 2.

As shown in Fig. 2, the entire discovery framework is an iterative process. Starting with a set of training documents with known relevance judgment, GP first operates on a large population of random ranking functions. These ranking functions are then evaluated based on the relevance information of training documents. If the stopping criteria is not met, it will go through the genetic transformation steps to create and evaluate the next generation population iteratively. The validation data set is used to help select ranking functions that generalize well for unseen documents and thus avoid the effect of over-training.

The detailed implementation of the above framework is described as follows:

3.2.2.1. Terminals. In GP, terminals are leaf nodes of a tree data structure. Essentially they are statistical lexical features used in term weighting to capture word semantics information. In this work, terminals were chosen and modified after examining various term weighting and ranking formulas as in [29,31,33]. These terminals are listed in Table 2.

Table 2  
![](/api/attachments/DBWF2B2Y/fulltext/images/8f8a16c3b7295029262abf3f9eca1df22613ae48777541abe969fbe795a6ff7a.jpg)  
Fig. 2. The personalized ranking function discovery framework.

3.2.2.2. Functions. Functions are the operations applied to combine terminals and/or sub-trees to produce longer expressions. The following functions were used in our implementation: + , - , / , log.

These functions were chosen as these are the most often observed operators inthe information retrieval literature that combine the various terminals mentioned above.

The terminals used in our GP system

<table><tr><td>Terminals</td><td>Statistical meaning</td></tr><tr><td>tf</td><td>Same as TF: number of times the term appeared in a document</td></tr><tr><td>tf_max</td><td>Maximum tf for a document</td></tr><tr><td>tf_avg</td><td>Average tf for a document</td></tr><tr><td>tf_doc_max</td><td>Maximum tf in the entire document collection</td></tr><tr><td>df</td><td>Same as df: number of unique documents the term appeared</td></tr><tr><td>df_max</td><td>Maximum df for a given query</td></tr><tr><td>N</td><td>Total number of documents in the entire text collection</td></tr><tr><td>length</td><td>Length of a document</td></tr><tr><td>length_avg</td><td>Average length of documents in the entire collection</td></tr><tr><td>R</td><td>Real constant number randomly generated by the GP system</td></tr><tr><td>n</td><td>Number of unique terms in a document</td></tr></table>

3.2.2.3. Fitness function. A fitness function measures how effective a weighting strategy represented by an individual tree is for ranking. In our implementation, Average Precision (P<sup>\_</sup>avg defined in Table 3) is used as the fitness function. To calculate it, the average of precision score is calculated every time a relevant document is found, normalized by total number of relevant documents in the entire collection. Mathematically it can be expressed as: $\begin{array} { r } { P . a \nu g = \sum _ { i = 1 } ^ { T R e l } P _ { i } / } \end{array}$ TRel; where P =i / Rank .

Here TRel is the total number of relevant documents for a given query, and $R a n k _ { i }$ is the ranking position for the ith relevant document. Precision is defined as the proportion of documents examined by a user that are relevant to her information need. Recall is defined as the ratio of the number of relevant documents examined by the user to the total number of relevant documents in the entire collection. It is easy to see that P\_avg incorporates both precision and recall in a single measure. We chose this measure as the fitness function as this is the most used performance measure in information retrieval studies.

<table><tr><td colspan="2">Performance measures and their definitions</td></tr><tr><td>Measure</td><td>Definition</td></tr><tr><td>P_avg</td><td>The average of precision every time a new relevant is found, normalized by the total number of relevant documents in a data set</td></tr><tr><td>P10</td><td>The precision of the top 10 documents</td></tr></table>

3.2.2.4. Genetic operators. We use three operators in our implementation: selection, reproduction and crossover. We employed a generational replacement scheme with elitism whereby in reproduction the best individual is directly copied to the next generation without crossover. We used tournament selection (of size 6 with replacement) to select the best two parents for crossover. In crossover the two parents exchanged their internal genes-sub-trees.

Detailed theoretical properties of the GP based discovery framework have been discussed elsewhere [5–7].

## 4. Experiments

## 4.1. Data

To test how our model performs compared to other well known routing systems we use two different data sets in the experiments. The first data set is the threeyear news corpus from the Associated Press (AP). The AP news-wire data covers a broad variety of domains and the documents average roughly 450 words in length. Using news-wire data is a very popular method to test new retrieval and routing techniques since most of the routing applications today are concerned with the routing of current news to end users. The second data set is the 10 GB web data used in TREC (see http://trec.nist.gov for more details), consisting of more than a million web documents. Web data contains rich sources of information. Testing the model on the web data will give us more insights about the efficacy of the integrated model as it applies to web based information.

There are 35 testing topics (queries) in natural language on a variety of domains for the AP data set. There are 89 topics available for the web data set. We extract query terms from these topics and call them user-provided PQs (explicit queries as mentioned before) in this paper. The terms are weighted by their term frequency within the topic. These user-provided

PQs will be compared with the system-constructed PQs (implicit queries) which are built using query expansion techniques based on relevance feedback as described in stage 1 of the model. As described earlier we have used RSV formula to construct the systemconstructed PQs. We chose to use RSV for such construction as this was found in literature [8] to be the best among various methods of profile generation. Top 30 terms (parameter k in stage 1 described previously) after applying RSV were chosen to be part of the system-constructed PQs.

## 4.2. Performance measures

There are various performance measures used in retrieval and routing evaluations. Two prominent measures are listed in Table 3.

Each measure defined in Table 3 studies different properties of retrieval effectiveness.

As mentioned earlier, among the measures defined in Table 3, P\_avg is the dominant one used in retrieval evaluations. It incorporates both precision and recall in a single measure. We chose this measure as this is the most used performance measure in information retrieval studies.

The P10 measure looks at the precision of the top 10 retrieved documents. This measure is important in situations where the user is willing to see only a few of the retrieved documents, a typical scenario in web search. For both the measures in Table 3 higher value means better performance.

## 4.3. Baselines

We compare our model against the models used by two well known systems. The first is the Okapi system using the well-known Okapi BM25 ranking function [26]. The Okapi system is one of the best systems in several TREC routing evaluations. The other is a classifier system using Support Vector Machine (SVM). SVM is a high-performing learning-based system that performs very well in information routing experiments [14]. It was implemented using SVM light package. Detailed implementation of the SVM method is found in [14]. Each of these two systems will be supplied with two different types of PQs and the results will be compared with those obtained by our integrated model.

Table 4 Summary of the performance comparison results on the AP news data set

<table><tr><td>PQ</td><td>Matching</td><td>PAVG</td><td>P10</td></tr><tr><td>User-provided</td><td>Okapi</td><td>0.3103</td><td>0.41</td></tr><tr><td>User-provided</td><td>GP</td><td>0.3619</td><td>0.53</td></tr><tr><td>System-constructed</td><td>Okapi</td><td>0.3861</td><td>0.54</td></tr><tr><td>System-constructed</td><td>SVM</td><td>0.4024</td><td>0.57</td></tr><tr><td>System-constructed</td><td>GP</td><td>0.4270</td><td>0.61</td></tr></table>

## 4.4. Results

In order to facilitate the learning of GP and SVM and provide a fair comparison with the Okapi system, we randomly split each of the two data sets into training (49%), validation (21%) and test (30%) data parts. The training and validation parts were used to build system-constructed PQs and learn query-specific ranking functions (based on GP) and classifiers (based on SVM). Such a three data-set design or residual collection method for evaluation purposes is very common in information retrieval studies. K-fold cross validation is not considered for two reasons. First, the data-sets used are big (e.g. the 10 GB web database) and hence the size of database is not a limitation. Secondly, the feasibility of application of GP using Kfold cross-validation is limited due to the computational complexity involved. The performance results reported in this section are all based on the test data set.

Tables 4 and 5 summarize the experimental results on AP news data and web data, respectively<sup>5</sup>. The numbers mentioned are the averages of the performance measures across all queries. In these tables, row 1 stands for no query personalization and a fixed ranking function (i.e. without adaptation). Row 2 stands for no query personalization but using GP based ranking function adaptation. Rows 3 and 4 stand for system constructed PQ and Okapi and SVM as ranking systems, respectively. The last row stands for system constructed PQ along with a GP based ranking function adaptation (the last row represents our two-stage model). We compare the results obtained in each of the first four rows with those obtained by our two-stage model.

As can be seen from these two tables, our proposed integrated model-combining query expansion with ranking function (depicted in the last row of the tables) achieves the best performance on both data sets. On the other hand, one of the baseline models—using the userprovided queries on a fixed ranking system (Okapi)(row 1)—performs the worst in both cases. This confirms our initial concerns about the poor quality of the existing routing services which use a fixed matching function and queries provided by users. Instead of direct user input/solicitation, by changing the profile representation to include richer information about a user’s information need through query expansion, and user preference modeling through ranking discovery, we can improve the baseline performance (measured in PAVG) by more than 37% on AP corpus and 74% on the web corpus. We conducted t-tests which were statistically significant at p=0.01.

The advantage of using a GP based adaptive matching function over a fixed ranking system (Okapi) even for the user provided queries can be seen by observing the first two rows in the two tables. Here the PAVG performance improves by 17% and 15% for the AP corpus and the web data respectively.

There is also a significant difference between system-constructed queries through query expansion and user-provided queries even on the same ranking function. This can be seen from looking at the first and the third rows of Tables 4 and 5. The difference in terms of PAVG is quite remarkable: 22% on the AP corpus and 52% on the web corpus (with statistically significant t-tests at p=0.01). Similar observations can be made by comparing the second row and the last row in either of the tables. Here the matching function is the same (GP) but the queries are either userprovided or are system-constructed through query expansion. The performance improvement in terms of PAVG is 18% and 52% for the AP corpus and the web corpus respectively with the improvements being statistically significant at $\scriptstyle : p = 0 . 0 1$ . The implication from this result is that the capture of a user’s real information is a daunting issue in information routing. Direct user input to represent queries may be a good starting point, but the user information need representation should be implicitly, adaptively changed based on a user’s feedback to further improve the routing performance.

Summary of the performance comparison results on 10GB web data set

<table><tr><td>PQ</td><td>Matching</td><td>PAVG</td><td>P10</td></tr><tr><td>User-provided</td><td>Okapi</td><td>0.2591</td><td>0.28</td></tr><tr><td>User-provided</td><td>GP</td><td>0.2971</td><td>0.31</td></tr><tr><td>System-constructed</td><td>Okapi</td><td>0.3933</td><td>0.42</td></tr><tr><td>System-constructed</td><td>SVM</td><td>0.4216</td><td>0.44</td></tr><tr><td>System-constructed</td><td>GP</td><td>0.4510</td><td>0.46</td></tr></table>

The introduction of stage two in our two-stage model i.e. the addition of ranking function adaptation/ discovery using GP for user preference modeling to query expansion is clearly beneficial. It provides additional performance improvement (in PAVG) of 15% on the AP data and 22% on the web data (with statistically significant t-tests at $\scriptstyle { p = 0 . 0 1 }$ . A comparison of Row 3 and Row 5 in both tables helps illustrate this point.

Similar performance gain of our integrated model over the first baseline (user-provided queries on Okapi) can also be found on the performance measure of P10. The first baseline has been improved by almost 50% on the AP data and more than 64% on the web data, both in terms of P10.

A comparison between GP and SVM (our second baseline) on system-constructed queries shows comparable results, with GP having an edge over SVM. Both GP and SVM are learning-based algorithms. The results of SVM are harder to interpret by human beings as they are represented as support vectors (vectors of feature weights). On the other hand, the results of GP learning are ranking functions, which can be easily visualized for human interpretation and fine-tuning. The query-specific or personalized ranking function can be encoded in a user profile and be used for later information routing by the routing services.

## 5. Conclusions and future research

In this paper, we considered a novel approach to the problem of effective routing of personalized information, also known as the selective dissemination of information (SDI). A new integrated two-stage model, combining effective PQ construction through query expansion and ranking function adaptation using GP, is proposed and tested on two different large scale text corpora. The results are quite promising and encouraging compared to other competitive baseline systems.

Our technique has practical applications in situations where selective dissemination of information is important. A knowledge worker does not have time to sift through vast amounts of incoming information. Our technique can tailor the information retrieval for such a worker.

One limitation of this study is that the training data is explicitly collected from users. In practice, this may impose a constraint on the adoption of the new model. What if a user is unwilling to explicitly provide the feedback data? In such a case, we have to resort to the non-intrusive ways of collecting training data by monitoring and collecting data from a user’s behavior (click-stream) as done in [13]. We are currently in the process of exploring this issue.

Another research direction is to test the integrated model more extensively using a large pool of real users. The results reported in this paper are based on two benchmark data collections from TREC. More testing on real users, especially users of different expertise in various search domains, will shed more insights on the efficacy of our approach.

In this paper we assume a user’s profile will remain static over a sufficiently long period of time (which is a reasonable assumption). However as information environment changes over a longer time frame so can the user’s profile. Hence over a longer time frame it may be necessary to adapt the user’s profile to the changing routing environment. More research needs to be done in the area of adapting the user profile over long periods of time.

## References

[1] L. Ardissono, A. Goy, G. Petrone, M. Segnan, Personalization in business to consumer interaction, Communications of the ACM 45 (5) (2002 (May)) 52–53.

[2] J. Balderston, Push aims to get smarter, InfoWorld 19 (21) (1997) 1 – 2.

[3] J. Budzik, K. Hammond, L. Birnbaum, Information access in context, Knowledge Based Systems 14 (2001) 37– 53.

[4] L. Chen, K. Sycara, WebMate: a personal agent for browsing and searching, in: K.P. Sycara, M. Wooldridge (Eds.), Proceedings of the 2nd International Conference on Autonomous Agents (Agents’98), ACM Press, New York, 1998, pp. 132– 139.

[5] W. Fan, E. Fox, P. Pathak, H. Wu, The effects of fitness functions on genetic programming-based ranking discovery for web search, Journal of the American Society for Information Science and Technology 55 (2004) 628– 636.

[6] W. Fan, M. Gordon, P. Pathak, A generic ranking function discovery frame-work by genetic programming for information retrieval, Information Processing & Management 40 (2004) 587–602.

[7] W. Fan, M.D. Gordon, P. Pathak, Discovery of contextspecific ranking functions for effective information retrieval using genetic programming, IEEE Transactions on Knowledge and Data Engineering 16 (4) (2004) 523– 527.

[8] W. Fan, M.D. Gordon, P. Pathak, Effective profiling of consumer information retrieval needs: a unified framework and empirical comparison, Decision support systems, Forthcoming.

[9] G.W. Furnas, T.K. Landauer, L.M. Gomez, S.T. Dumais, The vocabulary problem in human-system communication, Communications of the ACM 30 (11) (1987) 947–971.

[10] P. Gibson, Push versus pull news gathering, Information Today 14 (5) (1997) 57.

[11] D.K. Harman, Overview of the fourth text retrieval conference (TREC-4), in: D.K. Harman (Ed.), Proceedings of the Fourth Text Retrieval Conference, NIST Special Publication 500-236, 1996, pp. 1 –24.

[12] R. Kohavi, G. John, Wrappers for feature subset selection, Artificial Intelligence 97 (1997) 273 – 324.

[13] G. Leroy, A.M. Lally, H. Chen, The use of dynamic contexts to improve casual internet searching, ACM Transactions on Information Systems 21 (3) (2003 July) 229– 253.

[14] D.D. Lewis, Applying support vector machines to the TREC-2001 batch filtering and routing tasks, Proceedings of Tenth Text Retrieval Conference, 2001.

[15] F. Liu, C. Yu, W. Meng, Personalized web search by mapping user queries to categories, Proceedings of the 11th IEEE International Conference on Information and Knowledge Management, ACM Press, 2002, pp. 558 – 565.

[16] H. Liu, H. Motoda, Feature Selection for Knowledge Discovery and Data Mining, Kluwer, 1998.

[17] T.M. Mitchell, Machine Learning, McGraw Hill, 1997.

[18] H. Ng, W. Goh, K.L. Low, Feature selection, perceptron learning, and a usability case study for text categorization, Proceedings of the 20th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ACM press, New York, NY, 1997.

[19] D.W. Oard, G. Marchionini, A Conceptual Framework for Text Filtering, CS-TR-3643, University of Maryland, College Park, 1996.

[20] D. Peppers, M. Rogers, Enterprise One to One: Tools for Competing in the Internet Age, Currency Doubleday, New York, 1997.

[21] L. Picarille, Push comes to shove on web, Computer Reseller News 749 (1997 Aug. 11) 113–114.

[22] J. Pitkow, H. Schutze, T. Cass, R. Cooley, D. Turnbull, A. Edmonds, et al., Personalized search, Communications of the ACM 45 (9) (2002 September) 50– 55.

[23] A. Pretschner, S. Gauch, Ontology based personalized search, Proceedings of 11th IEEE International Conference on Tools with Artificial Intelligence, IEEE Computer Society, 1999, pp. 391– 398.

[24] S. Robertson, On relevance weight estimation and query expansion, Journal of Documentation 42 (1986) 182 – 188.

[25] S. Robertson, On term selection for query expansion, Journal of Documentation 46 (1990) 359– 364.

[26] S.E. Robertson, S. Walker, S. Jones, M.M. Hancock-Beaulieu, M. Gatford, Okapi at TREC-4, in: D.K. Harman (Ed.), Proceedings of the Fourth Text Retrieval Conference, NIST Special Publication 500-236, 1996, pp. 73–97.

[27] J.J. Rocchio, Relevance feedback in information retrieval, in: G. Salton (Ed.), The SMART Retrieval System-experiments in Automatic Document Processing, Prentice Hall, Englewood Cliffs, NJ, 1971.

[28] G. Salton, The SMART Retrieval System: Experiments in Automatic Document Processing, Prentice Hall, New Jersey, 1971.

[29] G. Salton, Automatic Text Processing, Addison-Wesley Pub. Co., Reading, MA, 1989.

[30] G. Salton, C. Buckley, Term weighting approaches in automatic text retrieval, Information Processing & Management 24 (5) (1988) 513–523.

[31] A. Singhal, G. Salton, M. Mitra, C. Buckley, Document length normalization, Information Processing & Management 32 (5) (1996) 619– 633.

[32] E.M. Voorhees, Variations in relevance judgments and the measurement of retrieval effectiveness, Information Processing & Management 36 (5) (2000) 697– 716.

[33] J. Zobel, A. Moffat, Exploring the similarity space, SIGIR Forum 32 (1) (1998) 18– 34.

Weiguo Fan is an Assistant Professor of Information Systems and Computer Science at the Virginia Polytechnic Institute and State University. He received his PhD in Information Systems from the Ross School of Business, University of Michigan, Ann Arbor, in 2002. His research interests include personalization, data mining, text/web mining, web computing, business intelligence, digital library, and knowledge sharing and individual learning in online communities. His research has appeared in many prestigious information technology journals such as Information Processing and Management (IP&M), IEE Transactions on knowledge and Data Engineering (TKDE), Information Systems (IS), Decision Support Systems (DSS), Journal of Management Information Systems (JMIS), ACM Transactions on Internet Technology (TOIT), Journal of the American Society for Information Science and Technology (JASIST), Journal of Classification, International Journal of Electronic Business, and in leading information technology conference such as ICIS, HICSS, AMCIS, WWW, CIKM, DS, ICOTA, etc.

Michael Gordon is Professor of Business Information Technology and Associate Dean for information technology at the Ross School of Business, University of Michigan, Ann Arbor. His research interests include information retrieval, especially adaptive methods and methods that support knowledge sharing among groups; information and communication technology in the service of social enterprise (promoting economic development, providing health care delivery, and improving educational opportunities for the poor); and using information technology along with social methods to support business education. He publishes extensively in leading IT journals such as Information Processing and Management (IP&M), IEEE Transactions on the Knowledge and Data Engineering (TKDE), Decision Support Systems (DSS), ACM Transactions on Internet Technology (TOIT), Journal of the American Society for Information Science and Technology (JASIST), Information Systems Research, Communication of ACM.

Dr. Praveen Pathak is an Assistant Professor of Decision and Information Sciences at the Warrington College of Business at the University of Florida. He received his PhD in Information Systems from the Ross School of Business, University of Michigan, Ann

Arbor, in 2000. He also holds a MBA (PGDM) from Indian Institute of Management, Calcutta, and a Engineering degree, B. Tech. (Hons.), from the Indian Institute of Technology, Kharagpur. His research interests include information retrieval, text mining, business intelligence, and knowledge management. His research has appeared in many prestigious journals such as Decision Support Systems (DSS), IEEE Transactions on Knowledge and Data Engineering (TKDE), Journal of Management Information Systems (JMIS), Information Processing and Management (IP&M), Journal of the American Society for Information Science and Technology (JASIST), and in leading information technology conferences such as ICIS, HICSS, WITS, etc.
