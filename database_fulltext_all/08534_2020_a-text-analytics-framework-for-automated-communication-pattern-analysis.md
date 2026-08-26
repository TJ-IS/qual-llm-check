---
otero_id: 8534
otero_key: "DWQDGXRB"
title: "A text analytics framework for automated communication pattern analysis"
authors: "Shaokun Fan; Noyan Ilk"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103219"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Journal Pre-proof

A Text Analytics Framework for Automated Communication Pattern Analysis

Shaokun Fan, Noyan Ilk

![](/api/attachments/DWQDGXRB/fulltext/images/4d2f0d3db5805cdcbee65f09b23d7560e386fe325fad1359f19696bba948b897.jpg)

PII: S0378-7206(19)30129-6

DOI: https://doi.org/10.1016/j.im.2019.103219

Reference: INFMAN 103219

To appear in: Information & Management

Received Date: 6 February 2019

Revised Date: 14 October 2019

Accepted Date: 25 October 2019

Please cite this article as: Fan S, Ilk N, A Text Analytics Framework for Automated Communication Pattern Analysis, Information and amp; Management (2019), doi: https://doi.org/10.1016/j.im.2019.103219

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2019 Published by Elsevier.

# A Text Analytics Framework for Automated Communication Pattern Analysis

Shaokun Fan<sup>\*</sup> Shaokun.fan@oregonstate.edu, Noyan Ilk nilk@business.fsu.edu

College of Business, Oregon State University, USA;,Address: 302 Austin Hall, College of

Business, Oregon State University, Corvallis, USA, 97331.

Noyan Ilk

College of Business, Florida State University, USA;

Corresponding author

Highlights:

We propose a text analytics framework for conversation analysis in large text data.

The framework combines text mining, process mining, sequential pattern mining, and econometric modeling methods.

We demonstrate the value of the framework using a real-world data set.

The framework can be used for communication monitoring, training, and improvement.

Abstract: Human-coding reliant conversation analysis methods are ineffective when analyzing large volumes of data. In this paper, we propose a text analytics framework for automated conversation pattern analysis. This framework first extracts speech acts (i.e., activities) from conversation logs, and then analyzes their flow through frequent pattern mining algorithms to reveal insightful communication patterns. Using a realworld data set collected from a customer service center, we demonstrate the usefulness of the framework for identifying patterns that are associated with service quality outcomes. Our work has implications for the design of communication policies and systems for customer service management.

Keywords: text analytics; pattern mining; communication pattern; speech act; service center

## 1. Introduction

Conversation analysis [1,2] is one of the prominent research methods used to study social interaction in real-world conversations. It is widely employed in social and information sciences (e.g., sociology, linguistics, and psychology) to investigate how participants of a conversation understand and respond to each other [3,4]. Traditional conversation analysis approaches rely heavily on manual effort – i.e., they require human coding and analysis of utterances in conversation logs to find recurring patterns of communication. However, the amount of “by hand” effort and time required in human coding of text-based transcripts severely restricts the number of cases that can be analyzed, thereby reducing the effectiveness of existing methods in identifying insightful communication patterns [5]. In addition, it is well-known that human cognitive capability is limited in terms of recognizing obscure patterns in large data structures [6,7]. Unfortunately, these two issues hinder the applicability of conversation analysis for practical communication management purposes in dynamic real-world settings such as service centers.

To address this research gap, we propose a text analytics framework for automated conversation analysis. Grounded in the speech act theory [8] and pattern mining techniques [9,10], this framework first models conversations as a process of speech acts (i.e., activities), and then analyzes these processes through mining algorithms to reveal insightful communication patterns. Automated text analysis techniques have been commonly utilized for various natural language processing tasks, such as market intelligence [11] and document clustering [12]. However, their use in analyzing text corpora generated from conversation transcripts has been limited. To conversation transcripts collected from the online service center of an S&P 500 firm. The findings of this case study demonstrate that the proposed framework is useful for identifying patterns that are associated with service quality outcomes, such as problem

Our work is motivated by both practical relevance and theoretical significance. In recent years, there has been a resurgence of interest in analyzing conversations for decision-making purposes in various business contexts, such as service centers and ately, organizations have difficulty in understanding people’s semantic dimension of texts such as keywords, sentiment, and topics [15]. On the other hand, the earlier work in the conversation analysis domain have considered conversations to be a sequence of speech acts, and focused on decoding the structure of these sequences from a turn-taking perspective [1]. As mentioned earlier, labor intensive analysis methods that are commonly applied in this line of research have limited the practicality of earlier efforts.

A contribution of our framework is to incorporate a pattern mining perspective on analyzing social conversations. To achieve this, the framework operates in three stages: 1) automated classification of messages in a conversation into speech acts, 2) the identification of communication patterns within conversations via process mining algorithms, and 3) explanatory analysis to establish a connection between the patterns and communication outcomes such as problem resolution or customer satisfaction. The classification stage is based on state-of-the-art text-based machine learning techniques, whereas the communication pattern mining stage is based on frequent pattern mining methods. The third and the last stage, that is, explanatory analysis, relies on the econometric formulation of communication quality-based variables. Our framework is novel in three aspects. First, while most existing text analytics approaches focus on the semantic dimension of text, we approach the analysis of text from a process perspective (i.e., flow of activities). Second, the proposed framework allows for automation in Third, it enables us to have a quantitative assessment of how such patterns affect managerial level performance measures, such as service quality.

To validate its implementation and value, we deploy the framework in a proofconversations that have occurred in the contact center of an S&P 500 firm. The contact center provides technical assistance through its human service agents, who communicate with firm customers through an online chat channel. The benefit of utilizing the online chat channel is the text-based nature of conversation transcripts, which negates the need for voice-to-text preprocessing of data. We access two data sources within this contact center: 1) conversation transcripts and 2) post-service surveys. Conversation transcripts include all the messages exchanged between customers and service agents as well as the timestamps of these messages and are stored as raw text files. Post-service surveys include customers’ responses to questions regarding their recent service experience. The implementation of the proposed methodology based on these data reveals that there exist communication patterns that can be used as signals of customers’ perceived satisfaction and problem resolution. It is possible for service agents to utilize this information to improve the quality of communication in the contact center. Our study makes several unique contributions to research and practice. From a theoretical perspective, we address the problem of communication pattern identification approaches used to study social interactions in various face-to-face and online mediums such as social media. Yet, the laborious nature of human coding and pattern matching efforts in traditional conversation analysis techniques severely restricts the applicability developing an automated approach for identifying insightful communication patterns in large text-based conversation corpora. A particular benefit of the approach is to minimize the need for “by hand” human intervention in terms of speech act coding and pattern analysis. Next, from a methodological perspective, our pattern mining approach relaxes the need for extracting a single unified model for the entire conversation process. The algorithms proposed in this paper can be potentially applied to ad hoc processes, which may not conform to a unified model, such as those in healthcare, knowledge sharing, and so on. Finally, for practical purposes, we provide a proof-ofconcept implementation of the proposed approach using a real-world case study.

Demonstrating the value of conversation analysis in actual business settings has been quite rare in the existing literature. In particular, the empirical findings from the case study and the propositions developed based on these findings can help managers improve communication strategies employed in service centers.

## 2. Literature Review

This paper is related to three areas in the literature: (1) pattern mining, (2) conversation analysis, and (3) customer service management. To place our contributions in perspective, we first review the relevant work in these three areas.

## 2.1 Pattern Mining

The communication between different participants can be viewed as a sequence of messages, and the goal of this paper is to identify and analyze insightful patterns in communication processes. To reach this goal, our work is built on sequential pattern analysis methods. Sequential pattern mining aims to discover frequent subsequences as patterns from a set of data with sequential records. There are three main types of [10]. The apriori-based algorithms are based on the rule that “all nonempty subsets of a frequent itemset must also be frequent” [16]. One drawback of this type of algorithms is that they require multiple scans of the database. Pattern growth algorithms typically use tree structures to represent sequential patterns, but the trees can grow to be very large and consume a lot of memory [17] . Finally, as their names imply, early-pruning algorithms can prune candidate sequences at the initial state of the mining process and help narrow the search space [18].

Sequential pattern mining has been applied to many problem domains. For example, researchers have modeled web page usage as sequential patterns and developed algorithms to mine such usage patterns from web access logs [19]. An analysis of web usage log can provide significant and useful information about user navigation behavior that can be used for website design and web server optimization. Sequential pattern mining can also be used to analyze customer purchase behavior [20], disease prediction [21], and so on.

As the communication process pattern is not always a strict sequential process, business process mining is another related domain that aims to discover business manual efforts, and use methods such as “walk-throughs,” interviews, and workshops [22]. Process mining techniques enable the automatic discovery of processes by extracting knowledge from event logs readily available in today’s information systems. The starting point for process mining is usually an event log and each event in such a log refers to an activity. Well-known process mining algorithms include the alpha algorithm, heuristic mining algorithm, multiphase mining algorithm, and fuzzy mining algorithm [23]. The communication pattern mining problem tackled in this paper is structures from sequential event logs. However, the majority of existing algorithms assume that there is one underlying unified process model that can capture the process logic of all event logs [24]. This assumption may not hold in conversations that tend to be ad hoc and dynamic.

## 2.2 Conversation Analysis

In conversation analysis, a speech act is defined as the most basic unit of utterance that serves a function in communication [8,13]. Also known as a dialogue act, a speech act carries phonological, syntactic, and semantic properties for the purpose of making a statement, whether it is a request, a question, a promise, etc. In his seminal work, Searle [8] defines five types of speech acts: assertive, directive, commissive, expressive, and declarative. Vosoughi and Roy [25] adapt Searle’s speech act taxonomy to computer-mediated communication by establishing six speech act categories as follows: assertion, recommendation, expression, question, request, and miscellaneous. Oraby et al. [26] further refine this classification into more refined categories within the context of the Twitter-based customer service as: greeting, statement, request, question, answer, and social act. In our study, we build on these taxonomies to model conversations in the online contact center context.

In conversation analysis, a “turn-taking” structure reflects the process by which communicating parties allocate the right or obligation to participate in social interactions [1]. It concerns the relative ordering of conversation parties [27]. The communication pattern between customer and agent is essentially a “turn-taking” process, which captures the ordering of interactions. Existing studies on turn-taking performance find that more interactive and equally distributed turn-taking lead to better team performance [28]. We argue that even with the same turn-taking structure, the impact of conversations may be different if the speech acts in those conversations are different because both turns and actions are essential components of conversations.

Conversation analysis theories claim that communicative behavior is multichanneled, multi-functional, and reflects a complex array of levels of organization [27]. Both turns and actions are essential components of conversations [29]. The conversation patterns mined from live-chat messages allow us to capture both turn-taking structures and speech acts.

## 2.3 Customer Service Management

Depending on the goal of customer service management, service quality can be measured by many different key performance indicators [30,31]. In the context of customer services, customer satisfaction and problem resolution are the two widely used measures of service quality [30]. Existing studies on service quality have extensively investigated the relationship between service processes and service quality [32]. The literature on customer satisfaction has mainly focused on how characteristics of service agents affect service quality. For example, Hurley [33] found that agents with higher extroversion and agreeableness, tend to perform better in customer services. Lin et al. [34] also found that personality traits have an impact on customers’ perceptions of service quality. Froehle [35] proposed six customer service representative characteristics often measured in industry surveys: courtesy, professionalism, attentiveness, knowledgeableness, preparedness, and thoroughness. They also found that some of these characteristics might have different impact depending on the communication media. Regarding the problem resolution dimension of service quality, the most salient factors tend to be task knowledge related [32] . While customer satisfaction can be related to relationship-building communications, problem resolution is more relevant to the knowledge, skills, and abilit es of service agents. In this paper, outcome quality to assess the impact of communication patterns.

## 3. A Framework for Communication Pattern Analysis

In this section, we describe the communication pattern analysis framework that is developed following insights from the speech act theory [8] and process mining techniques [9]. Figure 1 outlines the main stages of the framework. The first stage is the classification process, in which the main goal is to build supervised machine learning models that can automatically detect the speech act categories of individual messages in conversations. We propose to use three sets of features extracted from messages: lexical, contextual, and sentiment to improve the prediction performance of the classifier. Next, we propose a communication pattern mining method to identify frequent process structures in conversations. Finally, we propose to employ econometric modeling to investigate the precise relationship between the identified communication patterns and process outcomes.

![](/api/attachments/DWQDGXRB/fulltext/images/d2be1d2ab3686367b7f583b2bb75d3c2dcb48b7d0f1020ba7fc72f70a0a089bf.jpg)  
Figure 1. A Text Analytics Framework for Communication Pattern Analysis

To facilitate a more in-depth explanation of the proposed framework, we introduce three illustrative examples of conversations between a customer and a service agent in the service center context. In all of these three hypothetical cases, customers have issues about purchasing and activating a software package. Accordingly, they contact the service center of the hypothetical firm to seek assistance for their issues. To simplify the demonstration, we only present a snippet from each conversation while noting that there can be more messages before and after these snippets.

![](/api/attachments/DWQDGXRB/fulltext/images/dbd5d85538ea5d4f938389d75e284db8ed7739dfb1d32f0b88ac80656d21ff4e.jpg)

```txt
Case 3:
...
Customer: Do you have a free version of the software?
Agent: Yes you can download the free version from our website at www.freefreefree.com
Customer: Yes, I have done that. But it still asks for activation code. Can you tell me what is the activation code?
Agent: The activation code for free version is J72TAMWB2.
Customer: Awesome, thanks!
...
```  
Next, we discuss each of the framework stages in more detail while referring back to these exemplary cases for illustrative purposes.

## 3.1 Speech Act Classification

Speech act classification refers to the categorization of statements in conversations (i.e., individual messages in a dialog) into speech act labels. As discussed in the Literature Review section, we adapt the taxonomy originally developed by Searle [8] to the online communication context and establish six labels for the messages to be classified into: Question, Answer, Informative Statement, In-progress Statement, Request, and Social Act. From a technical standpoint, the task at hand is known as a multi-class classification problem, in which the goal is to classify a message’s speech act category using features extracted from the content and the metacharacteristics of the message. Specifically, we propose to use three sets of features: lexical, contextual, and sentiment for this purpose. Below, we discuss each of these feature sets in more detail.

Lexical Features: Lexical features are those that constitute the structured textual representation of the message. They can be generated by breaking down the message into tokens (i.e., unique words, phrases, and other entities) and then assigning weights to these tokens. This type of text representation is also known as Vector Space Modeling [36]. Figure 2 illustrates the Vector Space Modeling process for the entire message corpus. During this procedure, the messages are first broken into tokens and then passed through preprocessing operations involving stop word removal, normalization (e.g., lowercase transformation and removal of symbols), stemming, and term weighting. The final outcome is a matrix that represents all messages in a uniform space, where each feature is an individual lexical token. Unsurprisingly, the default Vector Space Model approach generates a large number of lexical features (with each feature representing a unique term), which might lead to the curse of dimensionality problem. To reduce the state space of the lexical features, feature selection approaches that sort the lexical features according to a goodness criterion (e.g., χ2 measure), and remove those that do not pass a predetermined threshold can be used [37].

![](/api/attachments/DWQDGXRB/fulltext/images/42010030de8b7c22996e4aca66cf4a0854bf475fc0b73e91e178457907883168.jpg)  
Figure 2. Vector Space Modeling

Contextual Features: Contextual features are those that define the characteristics of the message outside its semantics. In other terms, they are the “meta” attributes that provide descriptive information about the message [37]. Examples of these features include the author of the message, the number of words and characters, the position of the message within the conversation, indicators for certain punctuation marks (e.g., the question mark), and indicators for certain key words such as “yes” and “no”. These key words and punctuation marks can be tailored based on the context of the problem, and the features can be extracted from the text using straightforward parsing techniques.

Sentiment Features: Sentiment features help represent the emotions, attitudes, and degree of polarity embedded in messages. Following Oraby et al. [26], we incorporate these features in the methodology with the expectation that the direction (positive or negative), and the strength of sentiment in a message could be indicative of the message’s speech act category. For instance, social acts are more likely to be positive in terms of sentiment whereas questions are more likely to be neutral. There are two main types of sentiment identification approaches commonly used in literature: 1) lexicon-based and 2) machine-learning based [38]. The former approach is based on using a predefined semantic dictionary and matching words from the message to this dictionary; whereas the latter approach is based on machine-learning modeling with textual input features.

To illustrate these features, consider the message: “Great! Thank you very much.” by the customer in Case 2. Here, the lexical features are the words: great, thank, you, very, and much (before stop word removal). Contextual features are customer (author of the message) and “3” (the position of the message within the conversation). Finally, the sentiment feature is the positive sentiment label (or the numerical score corresponding to the positive label). These features (and corresponding observation values) are then fed into a machine learning-based classification model to predict the label of the message – i.e., the social act. Using this classification model (details of which are provided in Section 4.1), the framework should, ideally, label all the other messages within the three illustrative cases as C1: (1Q, 2A, 1Q, 2A), C2: (1Q, 2A, 1S), and C3: (1Q, 2A, 1Q, 2A, 1S). Here the prefixes “1” and “2” before the labels are used to represent roles of message authors – i.e., “1” represents customers and “2” represents agents.

## 3.2 Communication Pattern Mining

Using the speech act labels extracted from each message, we can then transform a conversation into a communication process, which can be described as a directed graph showing communication content and process flow between participants. Such communication processes are usually complicated, ad hoc, and dynamic. In reality, it is hard (if not impossible) to find two identical communication processes even if the conversations are used to solve similar problems. Therefore, we focus on the common segments of a process for the analysis, which we refer to as “communication pattern” in this paper. These patterns can be very useful when trying to explain how individuals or organizations accommodate to different situations [39]. We first provide formal definitions of concepts related to communication processes, and their patterns based on process modeling concepts

Definition 1. Communication Activity. A communication activity is an act that is derived from a speech of a particular role (customer, agent, etc.). An activity is formally represented as a tuple $a _ { i } = ( r _ { i } , ~ c _ { i } )$ , where ri is the role of an actor, and $c _ { i }$ is the type of an act.

Definition 2: Communication Process Instance. A communication process instance, I, is a sequence of communication activities, which can be represented as an ordered list, $I = < a _ { I } , . . . , a _ { n } >$

Definition 3: Process Segment. A process segment S of a given process instance, $I = < a _ { I } , . . . , a _ { n } >$ is a subsequence $< a _ { m } ,$ am+ $I , \mathrel { \ldots } \mathrel { \ldots } , a _ { m + k } >$ , where $\mathbf { m } \geq 1$ and $\mathrm { m } + \mathrm { k }$ $\leq \mathtt { n } .$

Definition 4: Process Segment Graph. The Graph G for a process segment (S) is a directed graph $G = ( A ; E )$ , where

$A = \left\{ a _ { i } \right\}$ is a set of communication activities in S. Each $a _ { i } = ( r _ { i } , c _ { i } )$

$E = \{ ( \ a _ { i } , \ a _ { j } ) \ \}$ contains the edges between adjacent and different vertexes, i.e., ai, $a _ { i } \in A , a _ { i } \neq a _ { j }$ , and aj directly follows ai in S.

Following the literature of business process modeling, we define the most basic unit of a communication process as a communication activity [40]. In Definition 1, the actor role and the speech act are two basic aspects of an activity. For instance, in the

##

customer service context, some of the typical activities are customer and agent questions/answers, requests, statements, etc. The role of a participant in a process reflects the goal and responsibility. The speech act represents the content of activity that a participant uses to achieve the goal. Definition 2 formalizes process instances, which are corresponding to a sequence of activities in solving a problem. A company usually has many process instances, each of which often contains a sequence of activities from different roles. Definition 3 formalizes process segments, which represent a portion of a process instance. In practice, process instances are seldom identical. The shared process segments across process instances reflect routines that actors use to solve similar problems across different cases. Definition 4 formalizes how a process segment can be converted to a graph structure, which is called a process segment graph. Process segment graphs show how each activity needs to be conducted before r after) some other activities. While process segments only capture sequential relationships among activities, process segment graphs directly reflect inherent dependencies behind . In this research, we only focus on process segment graphs that occur frequently in communication processes. Next, we formally define the communication pattern and its related concepts.

Definition 5: Support. The support of a process segment graph is the proportion of communication process instances that contain process segments that can be mapped to the process segment graph.

Definition 6: Frequent Process Graph. A process graph G is considered frequent when its support is greater than or equal to a predefined threshold value ts.

Frequent occurrence is a common requirement in data mining studies [24,41,42]. For example, association rule mining aims at identifying frequent itemsets that occur more than a predefined threshold value [43]. In this paper, we follow the standard frequent pattern mining methods in the literature. We first formally define support and frequent process graph in definitions 5 and 6, respectively. Note that one process segment graph can correspond to many different process segments that have similar speech acts and dependency relationships.

The accuracy and quality of discovered patterns should always be well balanced by setting an appropriate level of threshold values. In the process mining literature, accuracy and quality can be measured by fidelity and fitness. Fidelity measures the degree to which the model explains a case and specific measures the degree to which a model is specific to a given case [44]. Instead of mining one unified process model for all process cases, we try to mine multiple patterns from process logs in communication pattern mining. Therefore, we need to balance the number of patterns identified, and how many cases can be covered by those identified patterns.

Definition 7: Graph Coverage. A process segment graph G is covered by another graph G’ in a process instance I if all process segments in I that can be

Definition 8: Unique Support. Given a set of frequent segment graphs GS, the unique support of a graph G GS is the proportion of communication process instances that satisfy two conditions:

The process instance contains process segments that can be converted to G;

G is not covered by any other graphs in GS in the process instance.

According to the definition of process graphs, more complicated graphs always contain many simple graphs. For example, a process graph A→B→C contains A→B and B→C. Therefore, when A→B→C is considered as a frequent process graph, all its subgraphs are considered as frequent process graphs. However, those simple graphs that are embedded in other graphs are usually not meaningful for communication process analysis because their effects are covered by the supergraph. To avoid such subgraphs and reduce complexity for pattern analysis, we further define graph coverage and unique support in definitions 7 and 8, respectively.

Definition 9: Communication Pattern. A frequent process graph can be considered a communication pattern if its unique support is greater than the predefined threshold value tus.

Action patterns should have two features: frequent and independent [39]. The frequent occurrence requirement means that a pattern should be universal across many process instances. If a process segment graph can only be found in a limited number of process segments, the graph may be found because of some ad hoc reasons, and cannot be generalized as patterns. The independency requirement means that one pattern should not rely on the appearance of other patterns. If one pattern is always covered by other patterns, it is not necessary to specifically extract and investigate that pattern. This independency requirement also addresses the concern that smaller patterns will always have an advantage over complicated patterns. This solution is consistent with previous data mining literature on finding the maximal common subunits in a set of data instances [16].

roles. This process instance actually starts with a question from the customer and follows by answers from the agent. It is a circular process with questions and answers between two parties. When we set the support value as 2/3, we have five graphs that occur at least at two process instances. However, some of the frequent graphs cannot be considered as a pattern because their occurrences are depending on other supergraphs. For example, the graph (1Q→2A) occurs in all three processes, but it is covered by its supergraphs (1Q↔2A or 1Q→2A→1S). Therefore, we only have two frequent graphs that can be considered as patterns in these three examples.

![](/api/attachments/DWQDGXRB/fulltext/images/a99dba5a888bb262dc906956dc3d83215efc3aca7e87cbf49a9d9858ee93e627.jpg)  
Figure 3. Illustrative Examples of Communication Patterns

To mine communication patterns from process logs, we need to count the occurrences of all possible process segment graphs. Furthermore, we need to check whether the occurrences of the frequent process segment graphs are independent from the occurrences of other process segment graphs. We propose a three-step procedure to mine the patterns from conversation logs. Next, we explain each step of the procedure

Step 1 (Frequent Graph Extraction): In this step, our goal is to extract a set of frequent graphs that can represent common routines in a data set of process logs. For each process instance, we first extract process segments of various sizes from the process instance by scanning from the beginning to the end of the instance. For every extracted process segment, we convert them into a process graph based on the formalization of the process graph in definition 4. We then count the occurrences of all process graphs, and only keep frequent process graphs for further processing. Algorithm 1 shows the logic of frequent graph extraction.

raction Input: A set of process instances (PI), support threshold value (ts) Output: A set of frequent segment graphs 1. frequent\_graph\_set = {} 2. for each process instance in PI do 3. identify all process segments of the process instance 4. convert the process segments into graphs 5. for each graph g identified in i do 6. if g is in frequent\_graph\_set then 7. g.count ++ 8. else 9. g.count = 1 and add g to frequent\_graph\_set 10. end if 11. end for 12. end for 13. for each graph g in frequent\_graph\_set do 14. if g.support < t<sub>s</sub> then 15. remove g from frequent\_graph\_set 16. end if 17. end for 18. return frequent\_graph\_set

Step 2 (Frequent Graph Grouping): We divide frequent graphs into groups according to their subgraph relationships. Given a set of frequent graphs identified in Step 1, the unique support of a frequent graph depends on other frequent graphs. It is computationally intensive to enumerate all possible combinations of graphs in the set and count their unique support. To address this concern, we divide all frequent graphs into subgroups according to their subgraph relationships. Graphs that have no supergraphs in the frequent graph set will be considered as the first group of graphs. We then remove the first group of graphs from the frequent graph set. We use the same supergraph logic to iteratively divide the rest of graphs into groups. Note that the output of this step is a list of graph sets because the order between graph sets is important for the next step. Algorithm 2 presents the detailed procedure of frequent graph grouping.

## Algorithm 2: Frequent Graph Grouping

```txt
Input: A set of frequent graphs frequent_graph_set = {g1, g2, ..., gn}
Output: A list of graph groups
1.    graph_group_list = []
2.    while frequent_graph_set is not empty do
3.    next_graph_group = {}
4.    for each graph gi in frequent_graph_set do
5.    if graph gi has no supergraph in frequent_graph_set then
6.    add gi to next_graph_group
7.    end if
8.    end for
9.    remove all graphs in next_graph_group from frequent_graph_set
10.    add next_graph_group to graph_group_list
11. end while
12. return graph_group_list
```

Step 3 (Frequent Graph Pruning): In this step, we iteratively prune the frequent graphs that are covered by other graphs in process instances. When a frequent graph has no supergraph in the pattern set, its unique support equals its support value. Thus, we can iteratively inspect the frequent graphs, starting from candidates that have no supergraphs, and determine whether they meet the minimum unique support requirement. If a graph meets the unique support requirement, it remains in the candidate set and eventually becomes a communication pattern. Otherwise, it receives no further consideration. Then, uninspected candidates that have no supergraphs in the uninspected candidates are added and processed iteratively. Algorithm 3 describes the procedure of frequent graph pruning.

## Algorithm 3: Frequent Graph Pruning

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Input: A set of process instances (PI), a list of frequent graph groups (L), unique support threshold value $(t_{us})$,
Output: A set of process patterns
1. pattern_set = {}
2. for each group of graphs in L do
3. add this group of graphs to pattern_set
4. initialize the count for all graphs in this group as 0
5. for each process instance in PI do
</div>

6. identify all process segments (PS) of the process instance 7. for each process segment PS<sub>i</sub> in PS do 8. convert PS<sub>i</sub> to graph g 9. if g is in pattern\_set then 10. remove all process segments that are covered by PS<sub>i</sub> from PS 11. end if 12. end for 13. convert all remaining process segments in PS to graphs 14. increase the count of these graphs by 1 15. end for 16. remove graphs with unique support $< t _ { u s }$ from pattern\_set 17. end for 18. return pattern\_set

With the three algorithms introduced in this section, we can mine a set of patterns that reflects common process structures in communication logs. These patterns occur frequently in the processes and their occurrences do not depend on the occurrence of other patterns. These patterns tend to be adopted by users because of many possible specific features, and so on.

## 3.3 Process Outcome Analysis

From a business standpoint, one of the potential benefits of conversation analysis is to improve communication monitoring and management in firms. To achieve this benefit, it is important to understand the precise relationship between the communication patterns and the process outcomes. Within the context of communication patterns, the measurement concern is of particular importance. More precisely, the exact issue is how to identify and count the patterns accurately when the only visible component of a conversation is a sequence of activities, but not the pattern. To address this issue, we modify the Algorithm 3 and identify occurrences of patterns in each communication process instance. We count how many activities in a process belong to a particular pattern, and record the count of these activities as the measurement of the pattern in the process. The number of activities belonging to a pattern captures not only the existence of the pattern in a process, but also how important the pattern is in the process. Thus, pattern measurement based on the number of activities allows us to better measure how patterns affect process outcomes.

In the context of customer services, such as service centers, typical measurements of process outcomes are customer satisfaction and problem resolution. Problem resolution is a dichotomous item with possible values being “Yes” and “No”. Customer satisfaction is usually measured by ordinal scale values with a predefined range. For example, customer satisfaction can be from 1 to 5 with 1 as unsatisfied and 5 as extremely satisfied.

Econometric modeling techniques are commonly used for constructing models to investigate the impact of factors on outcome variables [45]. During this process, the main objective is to isolate and infer the true effect of a variable (e.g., communication pattern) on the process outcome (e.g., customer satisfaction) while ruling out alternative concerns, such as omitted variables, simultaneity, and measurement errors need e carefully addressed to obtain reliable results [45]. To address possible econometric concerns regarding confounding factors, we need to include a number of control variables in both models. Several types of control variables need to be considered in this context. First, the experience of an agent satisfaction and problem resolution. Third, different types of problems that are addressed in the conversations may also affect both communication patterns and process outcomes. Fourth, politeness and agents’ promptness in the conversation may also affect the process outcome significantly. A typical regression model to estimate the effect of main independent variables (i.e., patterns) on the service outcome variable while controlling for alternative explanations can be modeled using the following formulation:

$$
O u t c o m e _ {i} = \alpha^ {E S T} + \mathrm{B} ^ {E S T} X _ {i} + \Gamma^ {O E S T} C o n t r o l s _ {i}\tag{1}
$$

where the $X _ { i }$ vector contains the independent variables of interest – i.e., pattern occurrence counts. The indicator EST refers to the appropriate estimator depending on the characteristic of the outcome variable (e.g., dichotomous, ordinal, or continuous) and the specification of the relationship. Finally, $C o n t r o l s _ { i }$ refer to the set of control variables.

## 4. Proof-of-concept Case Study

real-world data set collected from the online contact center of a financial software company. The main consumer-facing product provided by the company is an income tax preparation and filing software. Customer support for this product is provided through an online live-chat service center, in which service agents provide real-time assistance to customers reaching out to the company. We access two data sources within the contact center. The first one is a repository that stores chat conversation transcripts between service agents and customers in raw text format. Chat transcripts include all the messages exchanged between agents and customers as well as the time stamp of these messages. Figure 4 illustrates a sample live-chat conversation. We randomly select and extract $2 { , } 5 0 0$ unique conversation files from this data source. We develop automated text-processing programs to extract over 50,000 messages from these conversations.

![](/api/attachments/DWQDGXRB/fulltext/images/ce61c243d4853ad197a1aad6c8f6194836b596f85c620fbb78df6abc8b22370c.jpg)  
Figure 4. An Illustrative Live-chat Conversation

The second data source is customers’ post-service survey responses. Each customer completing a chat service receives an e-mail survey (sent one day after the chat session) from the company with questions about their chat experience, satisfaction, and problem resolution. We ensure that each one of the 2,500 conversations randomly selected from the conversation data source has a survey response associated with it. Next, we discuss the implementation of the framework on this data set in more detail.

## 4.1. Speech Act Classification

As discussed earlier, speech act classification is a multi-class supervised machine learning problem, in which the goal is to train a classifier that can identify a message’s speech act category using features extracted from the content and the metacharacteristics of the message. Next, we summarize the three steps to achieve this goal.

## 4.1.1. Manual Labeling

A prerequisite of standard supervised machine-learning techniques is to have labeled data for training [38]. As this information is not readily available within the raw conversation transcripts, we use a manual labeling approach to generate the “ground truth” for messages that will be used for training purposes. First, we randomly select 200 conversations from the transcript data and extract the 2,578 individual messages from these conversations. These messages are analyzed and manually labeled by one of the co-authors with one of the six speech act categories: (1) question, (2) answer, (3) social act, (4) in-progress, (5) request, and (6) informative.

Note that it is possible for individual messages to include two or more sentences; hence, a non-trivial number of messages in conversations consist of multiple two or more speech acts. For instance, a message such as “I will be happy to assist you with this question. Please hold on for a few moments while I double check this issue” consists of three elementary speech acts: a “social act” followed by “in-progress” statements. Given that our pattern mining algorithms operate based on a single speech act per message, we need to consolidate composite speech acts into a single one. On the basis of manual coding results, we find that informative and social act messages are commonly combined with other speech acts <sup>1</sup> . For instance, in multiple occasions, customers make an informative statement and then ask a question. On other similar of your social security number?”). According to the speech act theory, it is common for secondary speech acts in a compound message to serve the purpose of reinforcing the main speech act [46]. For instance, in the customer service context, the goal of a social act could be to ensure that other speech acts (e.g., request, etc.) will be thoroughly executed. Therefore, if a message has two speech acts and one of them is informative or social acts, we choose to use the other act as the primary act. Table 1 illustrates some examples of actual messages that appeared in the data set and their respective manually identified labels. Figure 5 provides the frequency distribution of speech acts in the labeled data set.

Table 1. Examples of Messages and Associated Speech Acts

<table><tr><td>Message</td><td>Speech Act</td></tr><tr><td>“How can I help you?”</td><td>Question</td></tr><tr><td>“Yes, that is right.”</td><td>Answer</td></tr><tr><td>“Please refresh your web page and recheck now.”</td><td>Request</td></tr><tr><td>“You should be able to login now.”</td><td>Informative statement</td></tr><tr><td>“Please give me a moment. I am still researching.”</td><td>In-progress</td></tr><tr><td>“Have a great evening!”</td><td>Social act</td></tr></table>

![](/api/attachments/DWQDGXRB/fulltext/images/59b4281e31ab277e2561656197c47fa7410508ced9566a94450cd08dcebcbd09.jpg)  
Figure 5. Frequency Distribution of Speech Act Categories

## 4.1.2. Feature Engineering

In the second step of speech act classification, we create a structured form of the data from the raw text messages by extracting the lexical, contextual, and sentiment features described in Section 3.1. To illustrate, consider the message: “what is the Error code that you are getting after clicking the button”? Vector space modeling of this message following the stop word removal, normalization, stemming, and tokenization steps generates the following terms: {what, error, get, click, button}. The values of these terms for any particular observation can then be calculated using TF-IDF scoring. For instance, if 2% of the messages in the corpus included the term “error”, then the TF-IDF of the feature “error” for the observation that consists of 5 terms (including 1 occurrence of “error”) can be calculated as: $1 / 5 \times \log ( 1 0 0 / 2 ) = 0 . 3 4$ . After calculating the TF-IDF scores of all terms, we perform feature selection, and choose the top two hundred terms that have the largest predictive power according to the $\mathbb { \chi } 2$ criterion. These terms constitute the finalized lexical feature set.

Next, we consider the meta characteristics of the messages (i.e., descriptive information) to use as contextual features. As two of our speech act categories are “question” and “answer”, we create two binary features: one to indicate whether the message ended with a question mark or not (“endsWithQ”) and the other to indicate whether the last earlier message by the previous party ended with a question mark or not (“lastOtherPartyEndsWithQ”) with the assumption that these features can be helpful in predicting the “question” and “answer” categories. In addition, we also create another binary feature (“isYesNoIncluded”) of meta attributes, we record the author of the message (customer or the service agent) – i.e., “author”, as well as the position of the message in the conversation (“positionGroup”). For position identification, we divide each conversation into three parts: the beginning (the first two messages), the end (the last two messages), and the middle (the rest). Finally, we calculate the number of words and characters in the message (“wordLength” and “characterLength”, respectively) as additional structural information to be included in the contextual feature set.

We include sentiment-based features in the transformed data with the assumption that the polarity of a message might be associated with the speech act category (e.g., social act type messages tend to be more positive). To extract the sentiment features, we use a predefined semantic dictionary [47] that annotates words with their corresponding sentiment scores, and compute the overall positive (“pos”), negative (“neg”), and neutral (“neu”) orientation by aggregating the scores of each term in the message. This process is also known as lexicon-based sentiment analysis [38].

## 4.1.3. Algorithm Implementation and Fine-Tuning

After constructing the features discussed in the earlier section, we follow a supervised machine learning process to train the classification model that will be used for speech act labeling. For this purpose, we implement a variety of machine learning algorithms, including support vector machines (SVM), random forest (RF), neural networks (NN), logistic regression (Logit), adaptive boosting (AdaBoost), Naïve Bayes (NB), and deep learning (DL) and compare their predictive performances. It is important to note that a majority of machine learning algorithms make use of pre-run parameters (i.e., hyperparameters) for execution purposes. Considering that these hyperparameters can have a significant impact on the prediction performance [48], we conduct an extensive computational search to identify the optimal hyperparameters for each algorithm before finalizing the models. For hyperparameter tuning, we follow the grid-search method [48] , in which various different combinations of parameter values are evaluated using 5-fold cross-validation and the parameter combination that provides the best overall prediction accuracy is included in the final model configuration for each algorithm. A list of parameter values tested and the final parameters used for each algorithm are provided in Appendix A<sup>2</sup>.

Prior literature has also shown that ensemble learning methods that combine several machine learning algorithms into a single model can be useful in further improving the predictive performance in a classification problem [49]. Accordingly, we utilize three ensemble learning approaches: hard voting (i.e., plurality voting), soft voting (i.e., probabilistic voting), and stacking. In hard voting, each prediction made by an individual algorithm is given equal weight and the class label that receives the highest number of predictions in total is selected as the final label [50]. Soft voting operates in a similar way to hard voting with the main difference being instead of counting the labels per algorithm, it calculates the average of the class probabilities predicted by individual algorithms for each class [51]. Finally, the stacking ensemble learning method operates by fitting a meta-classifier on the outputs of individual algorithms to determine a new set of predictions [52,53]. Stacking is considered a general ensemble “framework” and hence, different classification algorithms can be utilized for model training purposes at both first and second training levels of the stacking process. In our stacking implementation, we utilize the same individual algorithms mentioned earlier at the first level and apply the eXtreme Gradient Boosting (XGBoost) technique as the meta-classifier at the second level. We choose XGBoost as the meta-classifier following Chen and Guestrin [54].

The implementation of the supervised learning process including algorithm/ensemble learning execution, hyperparameter tuning, and cross-validation is performed using the Python programming framework with the assistance of Scikitlearn, mlxtend, keras, and xgboost machine learning libraries. For model evaluation purposes, we use a 5-fold cross validation procedure and compute the performance scores of individual algorithms as well as the ensemble learning methods. Table 2 presents these scores after 5-fold cross validation as each feature set is gradually introduced to the models. We report the average accuracy results as well as the average precision, recall, and F1 scores with simple averaging (macro) and weighted averaging (weighted). Figure 6 provides a visual illustration of the overall accuracy comparison between the classifiers with different combinations of features.

Table 2. Prediction Performance Results

<table><tr><td>Features</td><td>Algorithm</td><td>Accuracy</td><td>Precision(weighted)</td><td>Precision(macro)</td><td>Recall(weighted)</td><td>Recall(macro)</td><td>F1(weighted)</td><td>F1(macro)</td></tr><tr><td rowspan="10">Lexical</td><td>SVM</td><td>0.617</td><td>0.647</td><td>0.718</td><td>0.617</td><td>0.636</td><td>0.619</td><td>0.662</td></tr><tr><td>RF</td><td>0.609</td><td>0.605</td><td>0.666</td><td>0.611</td><td>0.652</td><td>0.609</td><td>0.657</td></tr><tr><td>NN</td><td>0.590</td><td>0.622</td><td>0.678</td><td>0.603</td><td>0.627</td><td>0.606</td><td>0.633</td></tr><tr><td>Logit</td><td>0.600</td><td>0.605</td><td>0.666</td><td>0.600</td><td>0.643</td><td>0.601</td><td>0.653</td></tr><tr><td>AdaBoost</td><td>0.574</td><td>0.586</td><td>0.623</td><td>0.576</td><td>0.628</td><td>0.576</td><td>0.623</td></tr><tr><td>NB</td><td>0.569</td><td>0.591</td><td>0.661</td><td>0.569</td><td>0.582</td><td>0.563</td><td>0.598</td></tr><tr><td>DL</td><td>0.592</td><td>0.599</td><td>0.642</td><td>0.588</td><td>0.633</td><td>0.593</td><td>0.643</td></tr><tr><td>Hard Voting</td><td>0.620</td><td>0.628</td><td>0.697</td><td>0.621</td><td>0.654</td><td>0.619</td><td>0.669</td></tr><tr><td>Soft Voting</td><td>0.616</td><td>0.641</td><td>0.697</td><td>0.618</td><td>0.654</td><td>0.617</td><td>0.662</td></tr><tr><td>Stacking</td><td>0.595</td><td>0.651</td><td>0.700</td><td>0.595</td><td>0.626</td><td>0.593</td><td>0.638</td></tr><tr><td rowspan="10">Lexical + Sent.</td><td>SVM</td><td>0.617</td><td>0.630</td><td>0.698</td><td>0.617</td><td>0.644</td><td>0.620</td><td>0.665</td></tr><tr><td>DT</td><td>0.610</td><td>0.628</td><td>0.680</td><td>0.632</td><td>0.649</td><td>0.623</td><td>0.665</td></tr><tr><td>RF</td><td>0.554</td><td>0.628</td><td>0.679</td><td>0.418</td><td>0.591</td><td>0.462</td><td>0.585</td></tr><tr><td>Logit</td><td>0.608</td><td>0.634</td><td>0.711</td><td>0.608</td><td>0.622</td><td>0.608</td><td>0.648</td></tr><tr><td>AdaBoost</td><td>0.586</td><td>0.591</td><td>0.619</td><td>0.586</td><td>0.629</td><td>0.588</td><td>0.633</td></tr><tr><td>NB</td><td>0.583</td><td>0.612</td><td>0.687</td><td>0.583</td><td>0.589</td><td>0.580</td><td>0.611</td></tr><tr><td>DL</td><td>0.596</td><td>0.602</td><td>0.657</td><td>0.591</td><td>0.638</td><td>0.601</td><td>0.643</td></tr><tr><td>Hard Voting</td><td>0.629</td><td>0.640</td><td>0.714</td><td>0.622</td><td>0.657</td><td>0.623</td><td>0.671</td></tr><tr><td>Soft Voting</td><td>0.631</td><td>0.634</td><td>0.703</td><td>0.630</td><td>0.667</td><td>0.628</td><td>0.672</td></tr><tr><td>Stacking</td><td>0.629</td><td>0.642</td><td>0.696</td><td>0.621</td><td>0.655</td><td>0.627</td><td>0.668</td></tr><tr><td rowspan="10">Lexical + Sent. + Context.</td><td>SVM</td><td>0.742</td><td>0.753</td><td>0.770</td><td>0.742</td><td>0.729</td><td>0.744</td><td>0.744</td></tr><tr><td>DT</td><td>0.751</td><td>0.770</td><td>0.797</td><td>0.765</td><td>0.735</td><td>0.757</td><td>0.752</td></tr><tr><td>RF</td><td>0.738</td><td>0.749</td><td>0.793</td><td>0.740</td><td>0.696</td><td>0.732</td><td>0.741</td></tr><tr><td>Logit</td><td>0.759</td><td>0.779</td><td>0.796</td><td>0.759</td><td>0.751</td><td>0.763</td><td>0.765</td></tr><tr><td>AdaBoost</td><td>0.723</td><td>0.747</td><td>0.750</td><td>0.723</td><td>0.700</td><td>0.731</td><td>0.725</td></tr><tr><td>NB</td><td>0.665</td><td>0.683</td><td>0.714</td><td>0.665</td><td>0.648</td><td>0.666</td><td>0.663</td></tr><tr><td>DL</td><td>0.747</td><td>0.741</td><td>0.790</td><td>0.748</td><td>0.721</td><td>0.756</td><td>0.740</td></tr><tr><td>Hard Voting</td><td>0.766</td><td>0.797</td><td>0.820</td><td>0.767</td><td>0.750</td><td>0.771</td><td>0.768</td></tr><tr><td>Soft Voting</td><td>0.765</td><td>0.776</td><td>0.795</td><td>0.762</td><td>0.747</td><td>0.761</td><td>0.770</td></tr><tr><td>Stacking</td><td>0.761</td><td>0.777</td><td>0.796</td><td>0.758</td><td>0.752</td><td>0.762</td><td>0.762</td></tr></table>

![](/api/attachments/DWQDGXRB/fulltext/images/7883d9a9d02e3bc72d38621891ce8ec6acd9b8b952762ba872cb98090bc1f823.jpg)  
Figure 6. Classification Accuracy Results

From these results, we can see that the best ensemble model achieves an overall prediction accuracy of 77% when all features are used together. A possible concern during model evaluation is the generalizability of model performance to the prediction data set (i.e., the larger conversation data with unknown speech act labels). We alleviate this concern from two points. First, both the small labeled data set that is used for model data source that only covers three months of system operations. Considering that both of these data sets are randomly sampled from the same data source and the model evaluation has been conducted using cross-validation, there should not be any systematic reason that would lead to significant prediction performance differences between the two sample data sets. To further investigate if there might be differences because of randomness embedded in the sampling process, we calculate the average number of messages in a conversation (18 for unlabeled data vs. 19 for labeled data) and the average number of words in each message (12.5 for unlabeled data vs. 12.7 for labeled data) in both data sets. The results reinforce our belief that both data sets are similar in structure. Accordingly, we use the ensemble approach to build the final model from the entire labeled data set (2,578 observations). Once this model is built, we apply it on the larger conversation data set to generate the speech act labels for over 50,000 messages in 2,500 unique conversations. This final step completes our speech act classification stage in the methodology.

## 4.2. Communication Pattern Mining

After speech act classification, we move on to the $2 ^ { \mathrm { n d } }$ stage in the methodology – i.e., the communication pattern mining. Following the three-step procedure discussed in Section 3.2, we apply our pattern mining algorithms to the conversation data set with speech act labels. Similar to other data mining tasks, the threshold value for frequent patterns should be determined based on the data characteristics and analysis requirements. The choice of threshold value should be based on the level of noise and frequency of patterns [55]. In this paper, we choose 10% as the threshold value to calculate the support and the unique support. Our choice of 10% as the threshold value in our main analysis is because of two reasons: (1) this threshold gives us the appropriate number of interesting patterns to analyze; and (2) patterns occurring in more words, the 10% threshold value allows us to discover a set of patterns with a good balance of quality and accuracy [44]. Whether a message is from a customer or an agent is also recorded in the data set provided by the focal company. Therefore, we can combine the role information of messages with the predicted acts and create labels to represent messages.

To further reduce the search space, we only consider sequences with at least three activity actions. This also helps us identify more interesting patterns that might have a feedback mechanism (i.e., with three actions, it is possible for the message originator to send a follow-up/response message). After these operations, we are able to extract 52 frequent process segment graphs from the data set. We further divide the 52 graphs into four groups. By removing the graphs that are covered by other frequent graphs, we finally achieve a set of 37 patterns, which are shown in Figure 7. About 1/3 of these patterns have loops and the other 2/3 have sequential structures. Each pattern contains up to 4 unique activities. Most patterns contain activities from both roles, i.e., the customer and the service agent. We note that each one of the six speech acts is represented in at least one of the identified patterns.

![](/api/attachments/DWQDGXRB/fulltext/images/ee693d3e62eb6f274d5b3e98da6320668a200a73824caff8d52804ea5b499c6e.jpg)  
Figure 7. All Communication Process Patterns Mined from the Data Set

## 4.3. Process Outcome Analysis

To investigate whether communication patterns indeed have a relationship with the outcome of conversations, we conduct empirical analyses based on the econometric models proposed in Section 3.3. In the next two subsections, we first describe the variables used in our model estimations and then discuss the results.

## 4.3.1. Variables Definition and Measurement

Dependent Variables: In our analyses, the two dependent variables of interest are customer problem resolution (Resolution) and perceived customer satisfaction (Satisfaction). Resolution is measured using a survey question that asks whether a customer’s problem was resolved at the end of the conversation or not. It is a dichotomous item with possible values being “Yes” and “No”. Satisfaction is measured using a survey item that asks if the expectations of the customer were fulfilled at the end of the chat conversation. This question is measured using a 5-point scale with the values ranging from “1 - fell way short of my expectations” to “5 - greatly exceeded my expectations”.

Pattern Variables: Patterns are our main independent variables of interest and we include the 37 patterns discussed earlier in the model to estimate their impact on Resolution and Satisfaction outcome variables. Patterns in our econometric specifications are represented with the variable name P#, where the numeric suffix corresponds to the index of the pattern in conjunction with Figure 7. We operationalize pattern variables using activity counts – .e., for each pattern, we count how many activities belong to the pattern within the conversation.

Control Variables: To address possible endogeneity concerns such as timespecific trends and chat session/agent heterogeneity, we include a number of controls in our estimations. For instance, waiting time in service is widely known to be a major determinant of customer satisfaction [56] and it can also be correlated with the formation of patterns; therefore, we include the variable QueueWait that indicates how much a customer waited for service after arriving to the system. Similar to QueueWait, the service duration can also affect both the customer’s satisfaction from the service [57] and can be correlated with longer patterns. Accordingly, we use the ServiceTime variable to control for this possible form of endogeneity. Both of these time-related variables are measures in seconds. Given the skewed nature of the time distributions, we use the logged versions of these variables in estimations. For the satisfaction model, we include the orthogonalized resolution (Resolution<sup>T</sup>) – projected as the residuals of the resolution model, to control for the direct marginal effect of resolution on satisfaction [58].

Next, we include the experience of the agent, AgentExp, in both models (satisfaction and resolution) considering that experienced agents might both be more skilled and faster (with shorter patterns) to solve customers’ problems. We operationalize AgentExp using a running tally of the number of conversations that the agent handled before each conversation during the data period. An agent’s messaging style and attitude can also affect the outcome. Specifically, two variables that can be correlated with both the outcome variables and patterns are the number of questions that an agent asked (AQCnt) and his/her politeness level (APoliteness) during the conversation. To calculate the former variable, we identify and count the messages that end with a question mark (“?”). For the latter variable (i.e., politeness), we borrow from Danescu-Niculescu-Mizil et al. [59] and Hu et al. [60], both of whom develop a number of strategies to categorize and define core politeness markers that can be automatically extracted from the text. Following these strategies, we search for lexical indicators markers to measure an agent’s politeness level in a conversation. The total number of lexical indicators belonging to these markers is then added to our models as another control variable.

In addition, the type of the problem a customer is facing as well as the type of the software product that they are using might both affect the service quality outcome and dictate the pattern of communication [61]. To account for possible customer heterogeneity that manifests itself through problem and product types, we include ProblemType and ProductType fixed effects into our models. Finally, to account for possible temporal variations [62] across the conversations, we include contact date and contact hour fixed effects, represented as ContactDate and ContactHour, respectively in our models.

Table 3 Summary Statistics and Correlation Scores

<table><tr><td></td><td>Variable</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td><td>(a)</td><td>(b)</td><td>(c)</td><td>(d)</td><td>(e)</td></tr><tr><td>(a)</td><td>QueueWait</td><td>2,575</td><td>349.37</td><td>540.42</td><td>0</td><td>2644</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>(b)</td><td>AgentExp</td><td>2,575</td><td>70.67</td><td>136.02</td><td>0</td><td>1016</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>(c)</td><td>ServiceTime</td><td>2,575</td><td>974.93</td><td>588.53</td><td>44</td><td>6627</td><td>0.07</td><td>-0.03</td><td>1.00</td><td></td><td></td></tr><tr><td>(d)</td><td>AQCnt</td><td>2,575</td><td>3.08</td><td>2.46</td><td>0</td><td>24</td><td>-0.06</td><td>0.01</td><td>0.40</td><td>1.00</td><td></td></tr><tr><td>(e)</td><td>APoliteness</td><td>2,575</td><td>16.71</td><td>9.46</td><td>1</td><td>82</td><td>-0.06</td><td>0.17</td><td>0.33</td><td>0.53</td><td>1.00</td></tr></table>

Table 3 reports the summary statistics and correlation scores for the continuous variables. For conciseness, we do not report the 37 individual pattern variables in this table. The min and max values for the pattern variables (across all the patterns) are: 0 and 19. 0 means the pattern does not occur in a particular case, where 19 means the correlation values across all of the

## 4.3.2. Estimation Results and Findings

Table 4 reports the estimation results under various specifications. Models (1) - (3) use customer satisfaction as the dependent variable and Models (4) - (6) use problem resolution as the dependent variable. Models (1) and (4) are the baseline models that include only identified patterns as independent variables. Models (2), (3), (5), and (6) introduce additional control variables to check the stability of coefficients. For conciseness, we only include the selective patterns that obtain a statistically significant coefficient in full models (e.g., Models (3) and (6)) in the results table. The complete results are provided in Appendix B.

From these results, we can see that Patterns 24 and 33 have a significant positive impact on both customer satisfaction and problem resolution. Pattern 32 has a positive impact on customer satisfaction but no significant impact on problem resolution after including the control variables. Patterns 6 and 11 tend to have negative impacts on process outcomes. Some of these patterns’ impacts are sensitive to the control variables. For example, Pattern 32 has a positive impact on the resolution in Model (4). However, the significance of this impact disappears after including the control variables in Models (5) and (6). In the rest of this paper, we use the full models that include all of the control variables – i.e., Models (3) and (6), when interpreting the effects of the patterns.

Table 4. The Impact of Communication Patterns on Service Quality Measures

<table><tr><td rowspan="2">Variables</td><td colspan="3">Satisfaction</td><td colspan="3">Resolution</td></tr><tr><td>Ordinal Logit (1)</td><td>Ordinal Logit (2)</td><td>Ordinal Logit (3)</td><td>Logit (4)</td><td>Logit (5)</td><td>Logit (6)</td></tr><tr><td>P6</td><td>-0.066(-0.039)</td><td>-0.052(-0.042)</td><td>-0.090*(-0.044)</td><td>-0.089(-0.047)</td><td>-0.07(-0.051)</td><td>-0.117*(-0.054)</td></tr><tr><td>P11</td><td>-0.101*(-0.042)</td><td>-0.102*(-0.043)</td><td>-0.110*(-0.044)</td><td>-0.106*(-0.049)</td><td>-0.105*(-0.05)</td><td>-0.105(-0.058)</td></tr><tr><td>P23</td><td>-0.035-(0.019)</td><td>-0.069***(-0.02)</td><td>-0.078***(-0.021)</td><td>-0.032(-0.023)</td><td>-0.047*(-0.024)</td><td>-0.048(-0.025)</td></tr><tr><td>P24</td><td>0.099**(-0.037)</td><td>0.118**(-0.038)</td><td>0.110**(-0.039)</td><td>0.153**(-0.047)</td><td>0.142**(-0.048)</td><td>0.124*(-0.051)</td></tr><tr><td>P26</td><td>-0.003(-0.017)</td><td>0.017(-0.018)</td><td>-0.029(-0.019)</td><td>-0.011(-0.019)</td><td>0.001(-0.021)</td><td>-0.049*(-0.023)</td></tr><tr><td>P32</td><td>0.094***(-0.027)</td><td>0.077**(-0.029)</td><td>0.063*(-0.03)</td><td>0.081*(-0.036)</td><td>0.065(-0.037)</td><td>0.047(-0.04)</td></tr><tr><td>P33</td><td>0.227***(-0.035)</td><td>0.238***(-0.037)</td><td>0.189***(-0.038)</td><td>0.345***(-0.05)</td><td>0.300***(-0.051)</td><td>0.252***(-0.054)</td></tr><tr><td>log(QueueWait)</td><td></td><td>-0.033*(-0.015)</td><td>-0.029(-0.023)</td><td></td><td>-0.028(-0.017)</td><td>-0.002(-0.029)</td></tr><tr><td>log(AgentExp)</td><td></td><td>0.025(-0.023)</td><td>0.034(-0.034)</td><td></td><td>0.096***(-0.028)</td><td>0.058(-0.041)</td></tr><tr><td>log(ServiceTime)</td><td></td><td>-0.421***(-0.077)</td><td>-0.717***(-0.083)</td><td></td><td>-0.479***(-0.091)</td><td>-0.778***(-0.102)</td></tr><tr><td>AQCnt</td><td></td><td>-0.060*(-0.028)</td><td>0.086**(-0.031)</td><td></td><td>-0.056(-0.034)</td><td>0.092*(-0.039)</td></tr><tr><td>APoliteness</td><td></td><td>0.076***(-0.006)</td><td>0.115***(-0.007)</td><td></td><td>0.068***(-0.007)</td><td>0.100***(-0.009)</td></tr><tr><td>ResolutionT</td><td></td><td>1.380***(-0.048)</td><td>1.479***(-0.05)</td><td></td><td></td><td></td></tr><tr><td>ProblemType FE</td><td></td><td></td><td>Included</td><td></td><td></td><td>Included</td></tr><tr><td>ProductType FE</td><td></td><td></td><td>Included</td><td></td><td></td><td>Included</td></tr><tr><td>ContactDate FE</td><td></td><td></td><td>Included</td><td></td><td></td><td>Included</td></tr><tr><td>ContactHour FE</td><td></td><td></td><td>Included</td><td></td><td></td><td>Included</td></tr><tr><td>Other Patterns</td><td></td><td></td><td>See Appendix B</td><td></td><td></td><td></td></tr><tr><td>Observations</td><td>2,568</td><td>2,561</td><td>2,561</td><td>2,575</td><td>2,575</td><td>2,568</td></tr></table>

Standard errors in parentheses

\*\*\* p<0.001, \*\* p<0.01, \* p<0.05

Besides identifying the direction and strength of individual patterns on process outcome variables, a follow-up objective of our analysis is to deduce higher level and generalizable insights from these findings. Combining these results with the theoretical arguments made in conversation analysis and customer satisfaction domains, we propose the following three propositions that are drawn from empirical findings from the data set. For each proposition, we also propose a set of hypotheses that can be formally tested in future studies in similar settings.

Proposition 1: The same pattern may have different impacts on different process outcome measures.

This proposition is derived from our empirical findings based on the data set collected from a live-chat center. In Table 5, we summarize patterns that have different impacts on problem resolution and customer satisfaction. For example, Pattern 11 has no significant impact on resolution, but has a negative impact on satisfaction. This may be because of the clarity of the agent’s informative statement that leads to the customer’s questions. It has a negative impact on customer satisfaction because preparedness, and thoroughness [35]. But if the issues can be clarified by questions, it should not affect problem resolution. Patterns 23 and 32 also have different impacts on resolution and satisfaction according to the regression result. These two patterns imply that informative statements are only associated with customer satisfaction, but not problem resolution. On the basis of the discussion, we can further propose two hypotheses that can be formally tested in future studies:

H1: When a customer makes an informative statement, the response from the service agent with one or multiple informative statements have a negative impact on customer satisfaction.

H2: Multiple rounds of agent’s informative statements and customer’s social acts have a positive impact on customer satisfaction.

Table 5. Patterns with Different Impacts on Different Service Quality Measures

<table><tr><td>Graph Structure</td><td>Explanation</td><td>Impact on Satisfaction</td><td>Impact on Resolution</td></tr><tr><td>1I→2IP11→1Q</td><td>Customer provides an informative statement, followed by an information statement by the agent. Then customer asks a question.</td><td>Negative</td><td>None</td></tr><tr><td><img src="/api/attachments/DWQDGXRB/fulltext/images/087464fb49199c4b6584be1ec26ae7f7110cc868f96e1b9603a3fbc06136c164.jpg"/></td><td>After customer&#x27;s informative statement, agent gives multiple informative statements. Multiple rounds of such a sequence occur.</td><td>Negative</td><td>None</td></tr><tr><td><img src="/api/attachments/DWQDGXRB/fulltext/images/cbd011249d22179f50ee24ea66a4aeb39f160242b5589c5f544bb18f17eca56c.jpg"/></td><td>Multiple rounds of the agent&#x27;s informative statement and customer&#x27;s social act occur.</td><td>Positive</td><td>None</td></tr></table>

Proposition 2: Different patterns with the same “turn-taking” structure may have different impacts on process outcomes.

With the same turn-taking structures, patterns with more clarified questions and answers or other task-related speck acts may show the preparedness and professionalism of agents. Table 6 summarizes the empirical results that are related to this proposition. their messages. In Pattern 6, the agent uses a question to respond to the question raised by the customer, while in Pattern 24, the agent answers the customer’s questions directly. Direct answers to customers’ questions are usually considered to be the most 24 on service quality. Cases 2 and 3 in the illustrative examples in Section 3 contain Pattern 24 and we can see that such a Q→A→S sequence indeed indicates a successful and efficient way of handling problems from customers. The customer’s social act confirms the customer is happy about the agent’s answer. A similar comparison can be made between the patterns 33 and 34. We further propose three hypotheses based on the above.

H3: When a customer asks a question, the response from the service agent with a question has a negative impact on customer satisfaction and problem resolution. H4: When a customer asks a question, the response from the service agent with an answer has a positive impact on customer satisfaction and problem resolution. H5: When a service agent asks a question and the customer answers, the request message from the agent has a positive impact on customer satisfaction and problem resolution.

Table 6. Comparison of Patterns with the Same Turn-Taking Structure

<table><tr><td>Graph Structure</td><td>Explanation</td><td>Impact on Satisfaction</td><td>Impact on Res.</td><td>Comparison</td></tr><tr><td>1Q→2QP6→1A</td><td>Customer asks a question. Agent Responds with another question. Customer answers the question.</td><td>Negative</td><td>Negative</td><td rowspan="2">Both patterns have a (customer, agent, customer)Turn-Taking structure. Pattern 6 ends with a question but Pattern 24 ends with a social act.</td></tr><tr><td>1Q→2AP24→1S</td><td>Customer asks a question. Agent answers the question. Customer uses a social act.</td><td>Positive</td><td>Positive</td></tr><tr><td>2Q→1AP33→2R</td><td>Agent asks a question and customer answers. Agent follows up with a request message.</td><td>Positive</td><td>Positive</td><td rowspan="2">Both patterns have a (agent, customer, agent)Turn-Taking structure. Pattern 33 ends with a request but Pattern 34 ends with in-progress.</td></tr><tr><td>2Q→1AP34→2P</td><td>Agent asks a question and customer answers. Agent follows up with an in-progress (e.g., “working”) message.</td><td>None</td><td>None</td></tr></table>

Proposition 3: Different patterns with the same set of speech acts may have different impacts on process outcomes.

Both turns and actions are essential components of conversations. Therefore, for patterns with speech acts that are in different order, their impact on service quality may differ. Assuming the same set of speech acts, more interactive communication behavior will lead to better communication performance [29].

In Table 7, both Pattern 1 and Pattern 23 have the same set of speech acts (e.g., 1I and 2I), but their communication patterns are different. Pattern 1 has no significant impact on either resolution or satisfaction, while Pattern 23 has a negative impact on customer satisfaction. Pattern 1 is more interactive than Pattern 23 and the agent provides more informative statements in the latter pattern. Similarly, the main difference between Pattern 17 and Pattern 32 is that Pattern 32 is more interactive. Therefore, we observe more positive impact from Pattern 32. We further propose H6 based on the discussion above. We do not propose individual hypotheses for P23 and P32 as they have already been considered in H1 and H2.

H6: Multiple consecutive informative statements from the service agent have a negative impact on customer satisfaction.

Table 7. Comparison of Patterns with the Same Set of Speech Acts

<table><tr><td>Graph Structure</td><td>Explanation</td><td>Impact on Satisfaction</td><td>Impact on Resolution</td><td>Comparison</td></tr><tr><td>1I 2I P1</td><td>Multiple rounds of customer&#x27;s informative statement and agent&#x27;s informative statement occur.</td><td>None</td><td>None</td><td>Both patterns have the same set of speech acts: 1I and 2I.</td></tr><tr><td>1I 2I P23</td><td>After customer&#x27;s informative statement, agent gives multiple informative statements. Multiple rounds of such a sequence occur.</td><td>Negative</td><td>None</td><td>But 2I occurs more frequently in P23.</td></tr><tr><td>2I 1S P17</td><td>Agent gives multiple informative statements, followed by a social act from the customer.</td><td>None</td><td>None</td><td>Both patterns have the same set of speech acts: 1S and 2I.</td></tr><tr><td>1S 2I P32</td><td>Multiple rounds of agent&#x27;s informative statement and customer&#x27;s social act occur.</td><td>Positive</td><td>None</td><td>The timing of social act is different.</td></tr></table>

## 4.4 Robustness Check

To further validate the robustness of the proposed approach and empirical findings, we re-run our analyses with different threshold values for pattern mining.

Threshold values are commonly used in frequent pattern mining algorithms. Similar to hyperparameters in unsupervised machine learning tasks, it is often hard to determine the best threshold values because there is no standardized criteria to evaluate threshold values [63]. Besides, the 10% threshold used in our main analysis, we also utilize two different threshold values (e.g., 8% and 12%) and observe the results for robustness purposes. These threshold values lead to the discovery of 28 and 44 patterns, respectively. As expected, higher threshold values lead to fewer identified patterns. We find that the majority of the patterns that are statistically associated with the outcome variables in our main results, as presented in Table 4, also appear in 8% and 12% robustness models and are correctly captured by our proposed approach. Furthermore, as illustrated in Table 8 below. In brief, we find that the impact of these common patterns on outcome variables is all consistent across different thresholds.

Table 8. Robustness Check Result

<table><tr><td>Variables</td><td>(7)8%Satisfaction</td><td>(8)8%Resolution</td><td>(9)12%Satisfaction</td><td>(10)12%Resolution</td></tr><tr><td>P6</td><td>-0.0899*(0.0443)</td><td>-0.120*(0.0538)</td><td></td><td></td></tr><tr><td>P11</td><td>-0.115*(0.0453)</td><td>-0.102(0.0535)</td><td></td><td></td></tr><tr><td>P23</td><td>-0.0626**(0.0210)</td><td>-0.0359(0.0249)</td><td>-0.0512*(0.0203)</td><td>-0.0379(0.0249)</td></tr><tr><td>P24</td><td>0.124**(0.0401)</td><td>0.151**(0.0509)</td><td>0.0700(0.0385)</td><td>0.119*(0.0501)</td></tr><tr><td>P26</td><td>-0.0350(0.0191)</td><td>-0.0500*(0.0228)</td><td>-0.0245(0.0188)</td><td>-0.0433(0.0235)</td></tr><tr><td>P32</td><td>0.0620*(0.0295)</td><td>0.0470(0.0398)</td><td>0.0582*(0.0279)</td><td>0.0440(0.0388)</td></tr><tr><td>P33</td><td>0.229***(0.0383)</td><td>0.280***(0.0532)</td><td>0.105**(0.0362)</td><td>0.187***(0.0534)</td></tr></table>

Standard errors in parentheses \*\*\* p<0.001, \*\* p<0.01, \* p<0.05  
Similar to M(3) and M(6), Models (7) – (10) include all mined patterns and controls. For conciseness, we only report the patterns in Table 4.

## 5. Discussion and Conclusion

In this paper, we propose a framework for conducting conversation analysis in large text-based conversation data. The volume of such unstructured data, as commonly observed in dynamic business environments such as service centers, render it impractical to apply traditional labor-intensive conversation analysis techniques for practical purposes. To address this challenge, we develop an automated approach that utilizes process- and text-mining techniques. To our knowledge, this is one of the first data sets.

## 5.1 Theoretical Contributions

This work contributes to the existing literature in three aspects. First, we pattern analysis [9,10]. We aim to mine communication patterns that are frequent subgraphs of the complete conversation process. Instead of considering a single unified model for all event logs in a data set, we only assume that some conversations share a common portion (i.e., segment) of the process as the pattern [39]. The algorithms proposed in this paper can be potentially applied to ad hoc processes, which may not conform to a unified model, such as those in healthcare, knowledge sharing, and so on. Second, building on a well-known linguistics theory known as the speech act theory, we propose an automated classification method for transforming conversation logs into activity logs. The speech act classifier allows us to leverage process mining techniques to analyze text-based interactions. Given the recent popularity social media platforms [64], this approach should be of particular interest to firms that attract large amounts of postings on their social media pages. Third, we provide a proof-of-concept implementation of the approach using a real-world case study. Demonstrating the value of conversation analysis in actual business settings has been quite rare in the existing literature. The findings from the case study demonstrate the usefulness of the framework for improving process monitoring and management.

## 5.2 Practical Implications

The framework proposed in this paper can be used for communication process monitoring, training, and improvement. A communication support system can be developed based on the algorithms proposed in this paper. Companies can utilize such a tool to monitor conversations between their customers and agents. From the perspective of process quality improvement, the algorithms can automatically detect communication patterns with positive or negative impact in real-time. The early indicators of a process outcome can also be used for communication systems (e.g., live-chat) to prioritize cases when agents are assigned to multiple cases at the same time [65,66]. For employee training purposes, individual agents who commonly invoke communication patterns with unfavorable process outcomes can also be identified and trained for improvement.

Empirical findings from the online service center case study also have practical implications for the design of communication policies. The three propositions we propose based on theoretical bases in conversation analysis and customer satisfaction provide insights for managers of customer services. In Proposition 1, we find that the impact of patterns on process quality may differ depending on the selected process outcome measures (e.g., satisfaction vs. resolution). Thus, companies need to prioritize their goals of service management because we see that patterns may have different impacts on different measures of service quality. Managers need to consider their strategic goals and service outcome trade-offs when making decisions regarding service management. In propositions 2 and 3, we find that communicative behavior between customers and agents is multi-faceted and complex. Both actions and orders of interactions have a significant impact on process outcomes. Managers need to pay attention to both facets of communications between customers and agents. For example, by comparing Patterns 6 and 24, we know that direct answers to customers’ questions lead to a positive impact on problem resolution and customer satisfaction. For another example, by comparing Patterns 17 and 32 (and also Patterns 1 and 23), we know that more interactive informative statements are preferred in the customer service context. These findings can be coined into agent training modules and service quality monitoring processes.

## 5.3 Limitations and Future Work

The current work can be extended in a number of directions in the future. First, our proposed approach uses a classification model trained from a manually labeled data sample to identify the speech act categories in the large conversation data set. Future research can investigate if the prediction performance of this model can be improved by employing different supervised machine-learning approaches. Expanding the size of the labeled data sample can also help with concerns regarding the generalizability of the model in larger unlabeled data sets. Second, we note that the politeness control variable used in this study is calculated following a dictionary-based approach. A machine learning based approach as shown in Hu et al. [60] has the potential to improve the detection of politeness further, and hence, is a good avenue to investigate in future work. Third, it should also be noted that we utilize data from a single source and one should be cautious when generalizing the empirical findings from a single case study to other conversation contexts. Future studies can apply the proposed framework in other contexts and observe possible differences. Finally, future studies can also use lab or field experiments to study the antecedents and consequences of specific communication patterns as well as their interaction with the problem resolution variable when customer satisfaction is concerned.

## References

[1] H. Sacks, E. Schegloff, G. Jefferson, A Simplest Systematics for the Organization of Turn-Taking for Conversation, Language (Baltim). 50 (1974) 696–735. doi:10.2307/412243.

[2] A. Peräkylä, S. Vehviläinen, Conversation analysis and the professional stocks of interactional knowledge, Discourse Soc. 14 (2003) 727–750. doi:10.1177/09579265030146003.

[3] I. Hutchby, R. Wooffitt, Conversation analysis, 2008.

[4] R. Nordquist, Conversation Analysis Glossary of Grammatical and Rhetorical Accessed on October 22, 2018., (2017).

[5] G. King, W. Lowe, An Automated Information Extraction Tool for International Conflict Data with Performance as Good as Human Coders: A Rare Events Evaluation Design, Int. Organ. 57 (2003) 617–642. doi:10.1017/S0020818303573064.

[6] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From Data Mining to Knowledge Discovery in Databases, AI Mag. 17 (1996) 37–54. doi:10.1609/aimag.v17i3.1230.

[7] R. Chellappa, S. Sirohey, C.L. Wilson, Human and Machine Recognition of Faces: A Survey, Proc. IEEE. 83 (1995) 705–741. doi:10.1109/5.381842.

[8] J.R. Searle, SPEECH ACTS AND RECENT LINGUISTICS, Ann. N. Y. Acad. Sci. 263 (1975) 27–38. doi:10.1111/j.1749-6632.1975.tb41567.x.

[9] W.M.P. van der Aalst, Process Mining: Overview and Opportunities, ACM Trans. Manag. Inf. Syst. 3 (2012) 1–17. doi:10.1007/978-3-642-19345-3.

[10] N.R. Mabroukeh, C.I. Ezeife, A taxonomy of sequential pattern mining algorithms, ACM Comput. Surv. 43 (2010) 3.

[11] W. He, H. Wu, G. Yan, V. Akula, J. Shen, A novel social media competitive analytics framework with sentiment benchmarks, Inf. Manag. 52 (2015) 801– 812. doi:10.1016/j.im.2015.04.006.

[12] S. Jun, S.S. Park, D.S. Jang, Document clustering method using dimension reduction and support vector clustering to overcome sparseness, Expert Syst. Appl. 41 (2014) 3204–3212. doi:10.1016/j.eswa.2013.11.018.

[13] A. Abbasi, Y. Zhou, S. Deng, P. Zhang, Text Analytics to Support Sense-Making in Social Media: A Language-Action Perspective, MIS Q. 42 (2018) 427–464. doi:10.25300/MISQ/2018/13239.

[14] J. Mann, Hype Cycle for Business Use of Social Technologies, Gart. Res. (2011).

[15] B. Liu, L. Zhang, A survey of opinion mining and sentiment analysis, in: C. Aggarwal, C. Zhai (Eds.), Min. Text Data, Springer, Boston, MA, 2012: pp. 415– 463. doi:10.1007/978-1-4614-3223-4\_13.

[16] R. Agrawal, R. Srikant, Mining sequential patterns, in: Proc. 11th Int. Conf. Data

Eng., Taipei, Taiwan, 1995: pp. 3–14. doi:10.1016/j.jbi.2007.05.004.

[17] J. Han, J. Pei, B. Mortazavi-Asl, Q. Chen, U. Dayal, M.C. Hsu, FreeSpan: frequent pattern-projected sequential pattern mining, in: Proc. Sixth ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., 2000: pp. 355–359.

[18] Z. Yang, M. Kitsuregawa, LAPIN-SPAM: An improved algorithm for mining sequential pattern, in: 21st Int. Conf. Data Eng. Work., IEEE, 2005: p. 1222.

[19] J. Chen, T. Cook, Mining contiguous sequential patterns from web logs, in: Proc. 16th Int. Conf. World Wide Web, ACM, 2007: pp. 1177–1178.

[20] C.-H. Yun, M.-S. Chen, Mining mobile sequential patterns in a mobile commerce environment, IEEE Trans. Syst. Man, Cybern. Part C (Applications Rev. 37 (2007) 278–295.

[21] K.R. Lakshmi, S.P. Kumar, Utilization of data mining techniques for prediction of diabetes disease survivability, Int. J. Sci. Eng. Res. 4 (2013) 933–940.

[22] G.A. Wang, J.H. Wang, J. Li, A. Abrahams, W. Fan, An Analytical Framework for Understanding Knowledge-Sharing Processes in Online Q & A Communities, ACM Trans. Manag. Inf. Syst. 5 (2015) 1–31. doi:10.1145/2629445.

[23] W.M.P. van der Aalst, A.J.M.M. Weijters, Process mining: a research agenda, Comput. Ind. 53 (2004) 231–244. doi:10.1016/j.compind.2003.10.001.

[24] S. Fan, X. Li, J.L. Zhao, Collaboration process pattern approach to improving teamwork performance: A data mining-based methodology, INFORMS J. Comput. 29 (2017) 438–456. doi:10.1287/ijoc.2016.0739.

[25] S. Vosoughi, D. Roy, Tweet Acts: A Speech Act Classifier for Twitter, in: Proc. Tenth Int. AAAI Conf. Web Soc. Media (ICWSM 2016), 2016.

[26] S. Oraby, P. Gundecha, J. Mahmud, M. Bhuiyan, R. Akkiraju, “How May I Help You?”: Modeling Twitter Customer ServiceConversations Using Fine-Grained Dialogue Acts, in: Proc. 22nd Int. Conf. Intell. User Interfaces, Limassol, Cyprus, 2017: pp. 343–355.

[27] E.A. Schegloff, Sequence organization in interaction: A primer in conversation analysis I, 2007. doi:10.1017/CBO9780511791208.

[28] A.W. Woolley, C.F. Chabris, A. Pentland, N. Hashmi, T.W. Malone, Evidence for a collective intelligence factor in the performance of human groups, Science (80-. ). 330 (2010) 686–688. doi:10.1126/science.1193147.

[29] L. Turkstra, A. Ciccia, C. Seaton, Interactive Behaviors in Adolescent Conversation Dyads, Lang. Speech. Hear. Serv. Sch. 34 (2006) 117–127. doi:10.1044/0161-1461(2003/010).

[30] B. Marr, S. Parry, Performance management in call centers: Lessons, pitfalls and achievements in Fujitsu Services, Meas. Bus. Excell. 8 (2004) 55–63. doi:10.1108/13683040410569415.

[31] W.L. Tate, W. van der Valk, Managing the performance of outsourced customer contact centers, J. Purch. Supply Manag. 14 (2008) 160–169. doi:10.1016/j.pursup.2008.04.002.

[32] D.X. Ding, P.J.H. Hu, R. Verma, D.G. Wardell, The impact of service system design and flow experience on customer satisfaction in online financial services,

J. Serv. Res. 13 (2010) 96–110. doi:10.1177/1094670509350674.

[33] R.F. Hurley, Customer service behavior in retail settings: A study of the effect of service provider personality, J. Acad. Mark. Sci. 26 (1998) 115–127. doi:10.1177/0092070398262003.

[34] N.P. Lin, H.C. Chiu, Y.C. Hsieh, Investigating the relationship between service providers’ personality and customers’ perceptions of service quality across gender, Total Qual. Manag. 12 (2001) 57–67. doi:10.1080/09544120020010093.

[35] C.M. Froehle, Service personnel, technology, and their interaction in influencing customer satisfaction, Decis. Sci. 37 (2006) 5–39. doi:10.1111/j.1540- 5414.2006.00108.x.

[36] G. Salton, A. Wong, C.S. Yang, A vector space model for automatic indexing, Commun. ACM. 18 (1975) 613–620. doi:10.1145/361219.361220.

[37] Abbasi, Chen, CyberGate: A Design Framework and System for Text Analysis of Computer-Mediated Communication, MIS Q. 32 (2008) 811–837. doi:10.2307/25148873.

[38] B. Liu, Sentiment Analysis and Opinion Mining, Synth. Lect. Hum. Lang. Technol. 5 (2012) 1–167. doi:10.2200/S00416ED1V01Y201204HLT016.

[39] M. Hansson, B. Pentland, T. Haerem, Identifying Mid-Range Patterns of Action: Tools for the Analysis of Organizational Routines, in: Acad. Manag. Proc., 2017.

[40] W.M.P. van der Aalst, A.H.M. Hofstede, M. Weske, Business Process Management: A Survey, Bus. Process Manag. 2678 (2003) 1–12. doi:10.1007/3- 540-44895-0.

[41] J. Han, J. Pei, Y. Yin, R. Mao, Mining frequent patterns without candidate generation: A frequent-pattern tree approach, Data Min. Knowl. Discov. 8 (2004) 53–87. doi:10.1023/B:DAMI.0000005258.31418.83.

[42] D. Bera, R. Pratap, Frequent-Itemset Mining Using Locality-Sensitive Hashing, in: T.N. Dinh, M.T. Thai (Eds.), Comput. Comb. 22nd Int. Conf. COCOON 2016, Ho Chi Minh City, Vietnam, August 2-4, 2016, Proc., Springer International Publishing, Cham, 2016: pp. 143–155. doi:10.1007/978-3-319- 42634-1\_12.

[43] J. Hipp, U. Güntzer, G. Nakhaeizadeh, Algorithms for association rule mining --- a general survey and comparison, ACM SIGKDD Explor. Newsl. 2 (2000) 58– 64. doi:10.1145/360402.360421.

[44] Z. Huang, A. Kumar, A study of quality and accuracy trade-offs in process mining, INFORMS J. Comput. 24 (2012) 311–327. doi:10.1287/ijoc.1100.0444.

[45] D.N. Gujarati, Basic Econometrics, 5th ed., McGraw-Hill Education, 2008.doi:10.1126/science.1186874.

[46] T. van Dijk, Macrostructures: An interdisciplinary study of global structures in discourse, interaction, and cognition, Routledge, 2019.

[47] C.J.C.J. Hutto, E. Gilbert, VADER: A parsimonious rule-based model for sentiment analysis of social media text, Proc. 8th Int. AAAI Conf. Weblogs Soc. Media. (2014) 216–225. doi:10.1093/aobpla/plv053.

[48] B. James, B. Yoshua, Random Search for HyperParameter Optimization, J.

Mach. Learn. Res. 13 (2012) 281–305. doi:10.1162/153244303322533223.

[49] Kim Iljoo, Pant Gautam, Predicting web site audience demographics using content and design cues, Inf. Manag. (2018). doi:10.1016/j.im.2018.11.005.

[50] X. Lin, S. Yacoub, J. Burns, S. Simske, Performance analysis of pattern classifier combination by plurality voting, Pattern Recognit. Lett. 24 (2003) 1959–1969.

[51] T.G. Dietterich, Ensemble methods in machine learning, in: Lect. Notes Comput. Sci. (Including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics), 2000: pp. 1–15.

[52] Y. Li, J. Gao, Q. Li, W. Fan, Ensemble learning, in: Data Classif. Algorithms Appl., 2014: pp. 483–503. doi:10.1201/b17320.

[53] G. Wang, J. Hao, J. Ma, H. Jiang, A comparative assessment of ensemble learning for credit scoring, Expert Syst. Appl. 38 (2011) 223–230. doi:10.1016/j.eswa.2010.06.048.

[54] T. Chen, C. Guestrin, XGBoost: A scalable tree boosting system, in: Proc. ACM SIGKDD Int. Conf. Knowl. Discov. Data Min., San Francisco, California, USA, 2016: pp. 785–794. doi:10.1145/2939672.2939785.

[55] A.J.M.M. Weijters, W. van der Aalst, Process mining with the heuristics mineralgorithm, 2006.

[56] G. Tom, S. Lucey, Waiting time delays and customer satisfaction in supermarkets, J. Serv. Mark. 9 (1995) 20–29. doi:10.1108/08876049510100281.

[57] M.M. Davis, T.E. Voilmann, A framework for relating waiting time and customer satisfaction in a service operation, J. Serv. Mark. 4 (1990) 61–69. doi:10.1108/EUM0000000002506.

[58] J. Chen, H. Hong, W. Jiang, J.D. Kubik, Outsourcing mutual fund management: Firm boundaries, incentives, and performance, J. Finance. 68 (2013) 523–558.

[59] C. Danescu-Niculescu-Mizil, M. Sudhof, D. Jurafsky, J. Leskovec, C. Potts, A computational approach to politeness with application to social factors, ArXiv Prepr. ArXiv1306.6078. (2013).

[60] Y. Hu, A. Tafti, D. Gal, Read This, Please? The Role of Politeness in Customer Service Engagement on Social Media, in: Proc. 52nd Hawaii Int. Conf. Syst. Sci., 2019.

[61] P.J. Danaher, Customer heterogeneity in service management, J. Serv. Res. 1 (1998) 129–139. doi:10.1177/109467059800100203.

V. Mittal, J.M. Katrichis, P. Kumar, Attribute performance and customer 343–356. doi:10.1108/EUM0000000005655.

[63] S.H. Kwon, Threshold selection based on cluster analysis, Pattern Recognit. Lett. 25 (2004) 1045–1050. doi:10.1016/j.patrec.2004.03.001.

[64] J. Li, X. Li, B. Zhu, User opinion classification in social media: A global consistency maximization approach, Inf. Manag. 53 (2016) 987–996. doi:10.1016/j.im.2016.06.004.

[65] P. Goes, N. Ilk, W. Yue, Jl. Zhao, Live-chat agent assignments to heterogeneous e-customers under imperfect classification, ACM Trans. Manag. Inf. Syst. 2

[66] P. Goes, N. Ilk, M. Lin, L. Zhao, When More Is Less: Field Evidence on Unintended Consequences of Multitasking, Manage. Sci. 64 (2017) 3033–3054. doi:10.1287/mnsc.2017.2763.

(2011) 1–15. doi:10.1145/2070710.2070715.

Shaokun Fan is an Assistant Professor in Business Information Systems, College of Business, Oregon State University. He received his Ph.D. degree from the University of Arizona, M.S. degree and B.S. degree from Nanjing University, China. His research interests involve business analytics, business process management, and Fintech. He has published research articles in journals, such as Decision Support Systems, Informs Journal on Computing, Information & Management, Data & Knowledge Engineering, and Information Systems Frontiers.

Noyan Ilk is an assistant professor of Management Information Systems (MIS) in the College of Business at the Florida State University. His research addresses analytical problems that are at the intersection of service operations and information system domains. Specifically, he seeks to develop novel methods and policies to effectively manage service systems in electronic mediums. Noyan has taught courses in business analytics, business intelligence, and operations management topics at both undergraduate and graduate levels. He has published research articles in journals, such as Decision Support Systems, Management Science, ACM Transactions on Management Information Systems, and Information Systems Frontiers.
