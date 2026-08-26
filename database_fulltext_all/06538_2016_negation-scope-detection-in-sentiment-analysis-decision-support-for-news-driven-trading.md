---
otero_id: 6538
otero_key: "YAFVKS29"
title: "Negation scope detection in sentiment analysis: Decision support for news-driven trading"
authors: "Nicolas Pröllochs; Stefan Feuerriegel; Dirk Neumann"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.05.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Negation scope detection in sentiment analysis: Decision support for news-driven trading

Nicolas Pröllochs\*, Stefan Feuerriegel, Dirk Neumann

Chair for Information Systems Research, University of Freiburg, Platz der Alten Synagoge, 79098 Freiburg, Germany

A R T I C L E I N F O

Article history: Received 13 November 2015 Received in revised form 28 May 2016 Accepted 28 May 2016 Available online xxxx

Keywords: Decision support Machine learning Sentiment analysis Negation scope detection Financial news

## A B S T R A C T

Decision support for financial news using natural language processing requires robust methods that process all sentences correctly, including those that are negated. To predict the corresponding negation scope, related literature commonly utilizes rule-based algorithms and generative probabilistic models. In contrast, we propose the use of a tailored reinforcement learning method, since it can conquer learning task of arbitrary length. We then perform a thorough comparison with a two-pronged evaluation. First, we compare the predictive performance using a manually-labeled dataset. Here, reinforcement learning outperforms common approaches from the related literature, leading to a balanced classification accuracy of up to 70.17%. Second, we examine how detecting negation scopes can improve the accuracy of sentiment analysis for financial news, leading to an improvement of up to 10.63% in the correlation between news sentiment and stock market returns. This reveals negation scope detection as a crucial leverage in decision support from sentiment.

© 2016 Elsevier B.V. All rights reserved

## 1. Introduction

Sentiment analysis is a frequently utilized approach for sensing the tone in written content. Although this method is popular in various domains, it has gained traction especially in the financial domain. Here, it can relate positive and negative wording in financial disclosures to subsequent stock market movements [1–4]. While this idea seems intriguing, previous research identifies obstacles: “positive tone is dificult to accurately measure, since positive words are easily negated in ways dificult to programmatically identify” [5]. In fact, negations are a fundamental stylistic device for inverting the meaning of both words and sentences. For instance, financial news in the form of German ad hoc announcements contains negations in as many as 4.74% of all sentences.

As such, identifying and predicting negated parts are crucial for providing accurate decision support, since otherwise sentences are likely to be classified erroneously. According to Ref. [5], “the results for positive words are mixed because many times, negative phrases are wrapped in positive words”. To alleviate such a possible cause of disturbance, this paper proposes and evaluates algorithms with the aim of predicting negated parts of sentences. This demonstrates how the narrative content of disclosures [6–10] can be harnessed to provide decision support for investors.

Negations can appear in various forms; inverting not only the meaning of single words but also of whole phrases. Accordingly, one refers to the part whose meaning is changed as the so-called negation scope. Furthermore, negations can also flip the meaning of sentences implicitly; e.g. “the company has invented a new product; it was the first and last time”. Unfortunately, many machine learning algorithms struggle with this type of problem as it is virtually impossible to encode with a fixed-length vector while preserving its order and context. To justify this formally, we immediately observe that both negation scopes and sentences can be of changing length m that can theoretically range from one to infinity. Each word $w _ { i } , i \in \{ 1 , . . . , \infty \}$ thus represents an individual classification task

$$
f: (w _ {i}, [ w _ {1}, w _ {2}, \dots ]) \mapsto \{\text { Negated }, \neg \text { Negated } \},\tag{1}
$$

where $\left[ w _ { 1 } , w _ { 2 } , \ldots \right]$ is an ordered list of arbitrary length providing context information. This learning task f lies in contrast to many algorithms from classical machine learning, such as supervised learning, which always require an input vector of a fixed, pre-defined length m. As a remedy, this calls for special methods in order to deal with natural text and negation scope detection in particular.

Previous approaches for negation scope detection can be primarily grouped into two categories (e.g. [11]). On the one hand, rule-based approaches are straightforward to implement. However, they can barely identify implicit negations, not to mention linguistic peculiarities, such as sarcasm or irony. On the other hand, generative probabilistic models are computationally more expensive and require ex ante transition probabilities but can adapt to domainspecific features/language. Examples of the latter include Hidden Markov models or conditional random fields.

As an alternative, we propose the use of a third group, namely, reinforcement learning. The reason is that this method can work well with learning tasks of arbitrary length [12]. Interestingly, reinforcement learning has been greatly neglected in the domain of natural language processing (see Section 2), even though it aims at replicating actual human negation detection. More precisely, it learns based on past experience using only limited feedback in the form of a reward signal that indicates how well the learner is behaving while not explicitly detailing how to improve its behavior. In addition, the episode-based and flexible structure of this method can handle highly complex sentences and thus appears to be well suited for negation scope detection.

As a main contribution, this paper explores the impact of negation scope detection on the sentiment analysis of financial news. This allows us to investigate and compare predicted negation scopes in practice. In contrast to previous research, we not only implement a single method but also provide a holistic comparison of different options: rule-based approaches and Hidden Markov models, as well as conditional random fields, with both supervised and unsupervised learning. In addition, we propose the use of reinforcement learning in order to predict negation scopes. Moreover, we also investigate the sensitivity to the underlying sets of negation words. Finally, all approaches are compared in terms of their predictive performance and computational time using two dimensions: (1) we examine the accuracy of a manually-labeled dataset consisting of negated sentences from financial news. (2) Since the chosen labels are biased by subjective interpretation, the stock market reaction of investors serves as an objective measure. Here, we compute sentiment values for financial news and then compare the correlation of these sentiment values with the corresponding stock market returns. Altogether, this two-pronged evaluation reveals a compelling way of measuring and improving the accuracy of sentiment analysis.

The rest of this paper is structured as follows. Section 2 provides an overview of related works on negation scope detection, while Section 3 explains how we improve the state of the art with reinforcement learning. We then benchmark these approaches with financial news in Section 4. Finally, Section 5 discusses our results and identifies the implications of our research.

## 2. Related work

This section recapitulates related research in a structured fashion and points out how sentiment analysis can be improved by accurate negation detection. The detection of negation scopes essentially affects any context [13–17] in which sentiment analysis occurs but is particularly true when it comes to financial news [1, 5, 18]. Managers can easily negate words in ways that are dificult to identify computationally [1, 5]. Investigations about 10-K reports indicate that companies often frame negative news using positive words and rarely relay positive news in terms of negative words [18]. A thorough survey on the role of negation in sentiment analysis, as well as how to embed negation scopes, is found in Ref. [14].

Negation scope detection based on heuristic rules results in significant improvements when working with user-generated blog entries [19]. A similar approach inverts the meaning only within windows of a fixed size [20], which is evaluated using IMDb movie reviews. Investigations of political news during an election campaign incorporate part-of-speech tags to capture entity interactions by modeling subjects and objects [16]. Efforts in opinion mining systems on several manually-labeled corpora lead to robust crossdomain performance of rule-based approaches [21]. Research using similar approaches on the same data demonstrates problems with implicit negations and recommends the application of machine learning approaches [22].

In the domain of machine learning, authors propose the use of conditional random fields [13] to predict negation scopes for the sentiment analysis of product reviews. These are, in fact, a common [17, 23, 24, 25] methodological choice. Even though Ref. [25] compares two approaches, namely, conditional random fields and an approach based on regular expressions, the author does not explicitly consider financial news nor sets of negation words. In Ref. [26], the authors hand-checked a small set of negation scopes, arguing that the denial component is irrelevant when studying filings from initial public offerings (IPO). Finally, we note that negation scope detection is also a frequent research topic (e.g. [11]) for information retrieval aimed at medical reports.

Hence, this paper addresses the following research goal: we propose and compare algorithms to predict negation scopes by utilizing both linguistic rules and machine learning from previous work. In addition, we also evaluate the suitability of reinforcement learning for predicting negation scopes. Although this method is particularly popular in the domain of robotics and game theory (e.g. [27]), it is only rarely applied to the domain of computational linguistics. In fact, we are not aware of any publication that utilizes reinforcement learning to predict negation scopes. Moreover, to our best knowledge, this is the first study that predicts negation scopes designed to enhance the sentiment analysis of financial news.

## 3. Methods and materials

This section introduces our research methodology, as well as our datasets. Fig. 1 depicts how, in a first step, each announcement is subject to preprocessing steps which transform the running text into machine-readable tokens. Among others, this includes standard techniques, such as tokenization, part-of-speech tagging and stemming [28]. Afterwards, we extend previous works [29] and evaluate the suitability of the reinforcement learning approach for negation scope detection with common methods from the related literature. This includes generative probabilistic models, such as Hidden Markov models and conditional random fields, as well as rule-based algorithms.

We follow a two-sided approach. First, we evaluate the predictive performance on a manually-labeled dataset. Second, we examine the benefits of predicted negation scopes in an application from natural language processing; more precisely, how the sentiment analysis of financial news can be improved. In order to calculate the polarity of news announcements, we utilize the frequently employed approach of the so-called Net-Optimism sentiment [3]. This approach assumes that a news announcement with a positive message correlates with more positive words and vice versa. Thus, the Net-Optimism measure rates the content according to the frequencies of words classified in pre-defined dictionaries as either positive or negative. Although many other approaches can be found in the literature [30, 31], Net-Optimism provides not only robust results [32], but its simplicity makes later comparisons straightforward. We combine this measure with negation scope detection by inverting the polarity of words that are negated. For example, in the sentence “company sales have not significantly increased”, the negation scope is given by the sentence fragment inside the angled brackets. Here, the meaning of significantly increased is negated by the negation word not and the connotation according to the pre-defined dictionaries should be reversed. In the following sections, we present the underlying methods in order to determine negation scopes.

N. Pröllochs, et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/YAFVKS29/fulltext/images/daf416c29bd10eb332b05d5ab6df616840094d9535187fea143f66532c640251.jpg)  
Fig. 1. Research model combining sentiment analysis with negation scope detection by reinforcement learning, rules and generative probabilistic models, i.e. Hidden Markov models (HMM) and conditional random fields (CRF) in a two-edged evaluation.

## 3.1. Negation scope detection with reinforcement learning

Negation scope detection in related research predominantly relies on rule-based algorithms or machine learning in the form of generative probabilistic models [11]. However, both of these strategies involve certain limitations. For example, rule-based algorithms cannot adapt to domain-specific features or particularities of the chosen prose, whereas generative probabilistic models rely on ex ante transition probabilities that are dificult to define.

As a remedy, reinforcement learning allows for the learning of a suitable policy for negation classification directly through trial-anderror experience. In contrast to explicit teaching using supervised learning methods, the fundamental idea of the reinforcement learning approach is to learn a so-called agent from the outcome of its actions on the basis of past experience. This method tries to replicate human-like learning and thus appears well suited for natural language processing. For this purpose, reinforcement learning entails numerical rewards which encode the success of the interactions and, then, reinforcement learning aims to maximize these visible rewards. In this framework, the decision maker, i.e. the agent, interacts with an environment over a sequence of iterations and seeks a reward to be maximized over time. Formally, the model consists of a finite set of environment states $S ,$ a finite set of agent actions A, and a set of scalar reinforcement signals, i.e. rewards, R. At each iteration i, the agent observes some representation of the environment’s state $s _ { i } ~ \in ~ S .$ On that basis, the agent selects an action $a _ { i } ~ \in ~ A ( s _ { i } )$ where $A ( s _ { i } ) \subseteq A$ denotes the set of actions available in state s . After each iteration, the agent receives a numerical reward $r _ { i + 1 } \in R ,$ and observes a new state $s _ { i + 1 } .$ . This agent–environment relationship is visualized in Fig. 2.

In order to store current knowledge, the reinforcement learning method introduces a so-called state-action function $Q ( s _ { i } , a _ { i } )$ that defines the expected value of each possible action $a _ { i }$ in each state $s _ { i } .$ If $Q ( s _ { i } , a _ { i } )$ is known, then the optimal policy $\pi ^ { * } ( s _ { i } , a _ { i } )$ is given by the action a that maximizes $Q ( s _ { i } , a _ { i } )$ given the state $s _ { i } .$ . Consequently, the learning problem of the agent is to maximize the expected reward by learning an optimal policy function $\pi ^ { * } ( s _ { i } , a _ { i } )$

Among the several reinforcement learning algorithms that are available, we choose the so-called Q-learning method to learn the optimal behavior of the agent. The strength of the Q-learning method is finding the optimal policy without the requirement of an explicit model (i.e. a pre-defined Markov decision process) of the environment [12]. In fact, the Q-learning method is called model-free reinforcement learning because it can directly learn an optimal policy without knowing either the reward function or the state transition function [33]. Here, the agent iteratively updates its knowledge on the action-value $Q ( s _ { i } , a _ { i } )$ . This behavior with learning rate a and discount factor c can be formalized by an update rule

![](/api/attachments/YAFVKS29/fulltext/images/9c2493410c1bff4c65a3dd52b69a8f7da2d76c6e03b3c0e3eedf162233840ce6.jpg)  
Fig. 2. The agent–environment interaction in reinforcement learning [12].

$$
Q (s _ {i}, a _ {i}) \leftarrow Q (s _ {i}, a _ {i}) + \alpha \left[ r _ {i + 1} + \gamma \max _ {a _ {i + 1}} [ Q (s _ {i + 1}, a _ {i + 1}) - Q (s _ {i}, a _ {i}) ] \right],\tag{2}
$$

where $r _ { i + 1 }$ is the reward observed after performing an action $a _ { i + 1 } ,$ resulting in state $s _ { i + 1 }$ . Thus, Q-learning learns an optimal policy while following another policy for action selection. This feature is called off-policy learning. In order to perform Q-learning, we initialize the action-value function that stores the current knowledge to zero for all states and actions. Subsequently, the agent successively observes a sequence, i.e. one labeled sentence from the manually labeled dataset.

We now describe how we adapt Q-learning for our problem from natural language processing. At each iteration, the agent observes its current state in the form of its position in a labeled sentence. This information consists of an n-gram of the corresponding part-ofspeech tags or word stems. By definition, n-grams are a contiguous sequence of n items from a given sequence of text. This method is used extensively in text mining and natural language processing tasks to expand the feature space of machine learning methods and enrich these with contextual information [34]. For our purposes, we create unigrams, bigrams, trigrams and 4-grams using the part-ofspeech patterns and word stems in our news corpus. Then, one state can be given by an n-gram of part-of-speech tags, e.g. in the form of the trigram (verb, noun, article). Here, verb denotes the word class of the current word, whereas article and noun denote the word classes of the two preceding words. This set of features does not impose any restriction or preference, i.e. the part-of-speech patterns can include any possible word class, just as the word stems can include any existing word from the corpus. In addition, the state is expanded with the previous action $a _ { i - 1 }$ in order to introduce a context dependency, which allows to pass negations through to subsequent states. This results into a state specification

$$
s _ {i} = [ w _ {i - n + 1}, \ldots , w _ {i}, a _ {i - 1} ] ^ {T},
$$

for words $w _ { i }$ (and similarly for part-of-speech tags). This recurrent formulation is similar to belief states in partially-observable Markov decision processes (POMDP).

In this environment, the agent chooses at each iteration an action $a _ { i }$ out of two possible actions: either it can set the current state to

Please cite this article as: N. Pröllochs, et al., Negation scope detection in sentiment analysis: Decision support for news-driven trading, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.009

![](/api/attachments/YAFVKS29/fulltext/images/3de83d3f8ca9d728b8774a1c1265ecdcc5ea7da782ff7bdb7fbe0ccb0c81b1a4.jpg)  
Fig. 3. Example of reinforcement learning framework for negation scope detection based on unigrams of word stems. Here, the boxes with dark gray background denote words that should be negated according to the labeled dataset

negated or it can set the current state to not negated. Hence, the set of possible actions is given by $A \ = \ \{ \mathrm { N e g a t e d } , \neg \mathrm { N e g a t e d } \}$ . By definition, we set $a _ { 0 } = \mathrm { d e f } { \mathrm { - N e g a t e d } }$ . Subsequent to each action, the agent receives a numerical reward $r _ { i }$ from the environment. Here, we choose a binary reward structure based on related studies that also aim at implementing reinforcement learning for binary classification tasks [35]. If the agent classifies the word correctly as positive or negative, such that when $a _ { i } = a _ { i , \mathrm { L a b e l } }$ with the labeled value $a _ { i , \mathrm { L a b e l } } ,$ it earns a reward of zero. In the case of incorrect classifications, it receives a reward $\mathsf { o f } - 1 . ^ { 1 }$ Formally, the rewards $r _ { i } ~ = ~ R ( s _ { i } , a _ { i } )$ are given by

$$
r _ {i} = R (s _ {i}, a _ {i}) = \left\{ \begin{array}{l l} 0, & \text { if } a _ {i} = a _ {i, \text { Label }}, \\ - 1, & \text { otherwise }. \end{array} \right.\tag{3}
$$

An example is given in Fig. 3, which illustrates the setup with unigrams of stemmed words for an exemplary fragment “have not increas”. The first word $w _ { 1 } = h a v e$ is marked as not negated on the labeled dataset, whereas the second and third words, $\mathbf { i . e . } w _ { 2 } = n o t$ and $w _ { 3 } = i n c r e a s ,$ , are marked as negated. When observing the first state $s _ { 1 } = ( \mathrm { h a v e } , \mathrm { - N e g a t e d } )$ , the agent might then, at random, decide to explore the environment by negating $s _ { 1 } ,$ i.e. taking $a _ { 1 } = \mathsf { N e g a t e d }$ Since $a _ { 1 } \neq a _ { 1 , \mathrm { L a b e l } }$ the agent receives a negative reward $r _ { 1 } \mathrm { o f } - 1$ . Subsequently, it observes the second state $s _ { 2 } = ( \mathrm { n o t }$ , Negated), where it might decide to select $a _ { 2 } = \tt { \mathrm { - N e g a t e d } }$ . Since this word is marked as negated on the labeled dataset, the agent receives a reward $r _ { 2 } = 0 .$ It then continues with $w _ { 3 } = i n c r e a s$ . Also here, the agent receives a reward $r _ { i + 2 }$ of $0 ,$ if it decides to take $a _ { 3 } = \mathrm { - N e g a t e d } ,$ , and, otherwise, a reward $\mathbf { 0 } \mathbf { f } - 1$ . Since the agent iteratively updates its current knowledge, it will, sooner or later, find a policy that applies the best possible action in each state. In this example, the negation action will be applied for the states not and increas, but discarded for the state have.

In the following, we specify how the agent explores new actions in order to broaden its knowledge of the environment. At each word in the sequence, the agent takes an action based on e-greedy action selection. In this strategy, the agent explores the environment by selecting an action at random with probability e and, alternatively with probability $1 \ - \varepsilon ,$ exploits its current knowledge by choosing the optimal action, i.e. the action with the highest estimated reward according to its policy. In Section $^ { 4 , }$ we compare all variants of Q-learning models – including their sensitivity to exploration, discounting and learning parameters – in terms of their predictive performance for negation scope detection.

![](/api/attachments/YAFVKS29/fulltext/images/965358ac66cde6c77da9dc957e17260c89d2f315c401a5d96c8e9a3ec096e86e.jpg)  
Fig. 4. Schematic visualization of a Hidden Markov model where word classes serve as the emission alphabet.

## 3.2. Negation scope detection with Hidden Markov models

Next, we adapt the concept of Hidden Markov models (HMM) to our problem. This method belongs to the group of generative probabilistic models and has gained a lot of traction in recent studies that aim to predict negation scopes in textual materials (e.g. [23–25]). Hidden Markov models allow one to draw inferences when the true states of a model are not directly observable, but only its possible effects, as it is the case for negated sentence fragments.

According to the definition from Ref. [36], we proceed as follows in order to apply Hidden Markov models to the prediction of negation scopes. The unobservable, i.e. hidden, states are given by $\tilde { S } = \{ \mathrm { N e g a t e d } ,$ ¬Negated}. Each of these states emits at word i a value v˜ from an emission alphabet V<sup>˜</sup> . Here, we compare the predictive performance for negation scope detection across three variants of the emission alphabet: first, we set the emission alphabet to a list of partof-speech tags. This setup is illustrated in $\mathrm { F i g . }$ 4. Second, we choose the word stems as emission symbols — yielding a considerably larger set but allowing for higher accuracy.

Finally, we determine both the transition probabilities and emission probabilities. This is achieved by employing either the Viterbi algorithm for supervised learning (using a manually-annotated dataset) or the Baum–Welch algorithm for unsupervised learning.<sup>2</sup> All variants of Hidden Markov models are compared in terms of their predictive performance for negation scope detection in Section 4.

## 3.3. Negation scope detection with conditional random fields

Generative probabilistic models like HMMs assume each observation to be independent of its context, i.e. each state depends only on a previous state and each observation depends only on the current state. Given a sentence of length m, discriminative probabilistic models, such as conditional random fields (CRF), make conditional independence assumptions among a sequence of states Q<sup>˜</sup> and assumptions regarding how Q<sup>˜</sup> depends on a sequence of observations ${ \tilde { \cal { O } } } ( m ) ,$ but do not make conditional independence assumptions among Õ(m). In fact, the main conceptual difference between HMMs and CRFs is that HMMs maximize the joint probability $P \left[ \tilde { q } ^ { ( i ) } , \tilde { 0 } ( m ) \right]$ of observation $\tilde { \boldsymbol { q } } ^ { ( i ) }$ and label sequence $\tilde { \mathrm { O } } ( m )$ , while CRFs maximize a conditional probability $P \left\lceil \tilde { Q } \mid \tilde { 0 ( m ) } \right\rceil$ of labels Q<sup>˜</sup> given a sequence of observations $\widetilde { \mathrm { O } } ( m ) . { \ r A }$ principal advantage of discriminative models is that they allow for the inclusion of overlapping features of the input sequence, since each feature function can depend on observations from any iteration and more than one can be active.

Table 1  
Words in related literature which are marked as negations.

<table><tr><td>Reference</td><td>Signals</td><td>Negating pronouns</td><td>Negating adverbs</td><td>Inherent</td><td>Others</td><td>Count</td></tr><tr><td>Councill et al. [13],Lapponi [24]</td><td>Not, *n&#x27;t,</td><td>Neither, nothing, nobody, none</td><td>No, hardly, never, nowhere,never, hardly</td><td>Lack</td><td>Nor</td><td>14</td></tr><tr><td>Dadvar et al. [22]</td><td>Not, *n&#x27;t</td><td></td><td>No, rather, hardly</td><td></td><td></td><td>5</td></tr><tr><td>Ferris et al. [26]</td><td>Not, *n&#x27;t</td><td>Nothing, nobody, none</td><td></td><td></td><td>Nor, nay</td><td>7</td></tr><tr><td>Jia et al. [19], Hogen-boom et al. [20]</td><td>Not, *n&#x27;t</td><td></td><td>No, hardly, less, rarely, barely,never</td><td></td><td>without</td><td>9</td></tr><tr><td>Pröllochs et al. [43]</td><td>Not, *n&#x27;t</td><td></td><td>No, rather, hardly, never</td><td>Deny</td><td>Without</td><td>8</td></tr><tr><td>Taboada et al. [21]</td><td>Not</td><td>Nobody, nothing, none</td><td>never</td><td>Lack</td><td>Without</td><td>7</td></tr></table>

For the purpose of negation scope detection, we specify a socalled linear-chain conditional random field with a current observation identity [37]. This special case can be thought of as the undirected graphical model version of HMMs. Similar to our implementation of Hidden Markov models, we use two possible state labels <sup>˜</sup>S = {Negated, ¬Negated}, although, in this case, we only incorporate part-of-speech tags as the emission alphabet V. We use two labels and 11 possible part-of-speech tags as our emission alphabet, which gives four label–label features and 22 label–observation features. We learn the model using the L-BFGS algorithm with a manually-annotated dataset.

## 3.4. Rule-based detection of negation scopes

In order to accurately predict the scope of negations, a common approach relies upon rules which try to imitate the grammatical structure of a sentence. More precisely, these negation rules search for the occurrence of negation words and invert the meaning of certain surrounding parts. A simple example is given by “sales could not be increased”. In this sentence, the originally positive word “increased” is inverted by the preceding negation word “not”; one must now regard “increased” in a negative context. However, the effect of negation words can vary substantially. For instance, the first word following a negation phrase might be negated, whereas the meaning of all succeeding words remains the same, such as in “the production has not grown, but we are hopeful for the future”.

What the above examples all have in common is the fact that readers apply linguistic rules to resolve negation scopes in order to understand the meaning. Consequently, we utilize algorithmic negation rules as a benchmark to predict negation scopes. Individual negation rules, originating from related work, are as follows:

• Rule 1: No Inverting (Benchmark). Negation words have no impact on the negation scope.

• Rule 2: Negation of Sentence Fragments. Invert all subsequent words in a sentence after the occurrence of a negation word [20].

• Rule 3: Negation of Sentence Fragments. Negation of the whole sentence, if one or more negation words occur [20].

• Rule 4: Negation of Fixed Window Sizes. Invert a given window of words following a negation word; the window is set to varying sizes of 1–5 words [20, 22].

## 3.5. Dataset

Our news corpus originates from German, regulated ad hoc announcements<sup>3</sup> , between January 2004 and June 2011. As a requirement, each announcement must contain at least 50 words and be written in English. Our final corpus consists of 14,463 ad hoc announcements. In research, ad hoc announcements are a frequent choice [38–40] when it comes to evaluating and comparing methods for sentiment analysis. Additionally, this type of news corpus presents several advantages: ad hoc announcements must be authorized by company executives, the content is quality-checked by the Federal Financial Supervisory Authority<sup>4</sup> and several publications analyze their relevance to stock market reactions — finding a direct relationship (e.g. [41]).

To study the stock market reaction, we use daily stock market returns from the corresponding company, originating from Thomson Reuters Datastream. For those firms whose stock market returns we were not able to retrieve, we use the corresponding ad hoc announcements only in the manually-labeled dataset. In order to measure the sentiment of these announcements, we utilize the Loughran and McDonald Financial Sentiment Dictionary [18, 42]. This dictionary contains 354 entries with a positive polarity and 2350 entries marked as negative.

For the evaluation of negation scope detection, we use a dataset that was labeled manually by an external person. This dataset originates from ad hoc announcements without stock market returns and is therefore disjunct from the actual news corpus; we can use it as training data to estimate parameters for the machine learning implementations. This dataset consists of 3100 sentences from ad hoc announcements, with each sentence containing at least one negation phrase. It is noteworthy that the related literature proposes various selections of negation phrases (see Table 1). In this paper, we use the negation words from Ref. [43] as a benchmark, while we also evaluate all other negation groups in our online appendix. In the gold standard (i.e. the benchmark), a total of 29,338 words (33.3% of all words) are labeled as negated.

## 4. Results

We proceed by comparing the previous strategies for the prediction of negation scopes, namely, reinforcement learning, generative probabilistic models in the form of Hidden Markov models and conditional random fields, and rule-based algorithms. The contribution of our evaluation is twofold. On the one hand, Section 4.1 compares the predictive performance on a manually-labeled dataset to yield a direct and comparative measure. On the other hand, negation scope detection is likely to be combined with various tasks in natural language processing (NLP), most probably in combination with sentiment analysis. When it comes to applications like sentiment analysis, it is not always the case that the model that performs best on a dataset labeled by humans also provides the best results in an application scenario. The reason for this is that classifications by investors can deviate from the overall market reaction since, for example, high-frequency traders might overlook negations due to time pressure. Consequently, Section 4.2 further evaluates algorithms for negation scope detection within sentiment analysis.

Table 2  
Negation scope detection by rule-based and machine learning approaches compared across a labeled dataset, using the negation list from Ref. [43]. Cells are colored according to value (the darker the color, the higher and better the result).

<table><tr><td rowspan="2">Method</td><td colspan="5">Results: Labeled Dataset</td></tr><tr><td>Recall</td><td>Precision</td><td> $F_1$  Score</td><td>Accuracy</td><td>Balanced Accuracy</td></tr><tr><td colspan="6">Reinforcement Learning</td></tr><tr><td>Reinforcement Learning using word stem1-grams</td><td>0.5213</td><td>0.6888</td><td>0.5934</td><td>0.7617</td><td>0.7017</td></tr><tr><td>Reinforcement Learning using word stem 2-grams</td><td>0.2806</td><td>0.7590</td><td>0.4098</td><td>0.7302</td><td>0.6180</td></tr><tr><td>Reinforcement Learning using word stem 3-grams</td><td>0.1784</td><td>0.7297</td><td>0.2867</td><td>0.7038</td><td>0.5727</td></tr><tr><td>Reinforcement Learning using word stem 4-grams</td><td>0.1561</td><td>0.7307</td><td>0.2572</td><td>0.6992</td><td>0.5636</td></tr><tr><td>Reinforcement Learning using POS 1-grams</td><td>0.6022</td><td>0.5509</td><td>0.5754</td><td>0.7035</td><td>0.6782</td></tr><tr><td>Reinforcement Learning using POS 2-grams</td><td>0.4184</td><td>0.7357</td><td>0.5334</td><td>0.7558</td><td>0.6716</td></tr><tr><td>Reinforcement Learning using POS 3-grams</td><td>0.5792</td><td>0.5677</td><td>0.5734</td><td>0.7124</td><td>0.6792</td></tr><tr><td>Reinforcement Learning using POS 4-grams</td><td>0.5073</td><td>0.6230</td><td>0.5592</td><td>0.7332</td><td>0.6768</td></tr><tr><td colspan="6">Detection using Hidden Markov Models</td></tr><tr><td>HMM using POS for supervised learning</td><td>0.5160</td><td>0.5891</td><td>0.5501</td><td>0.7184</td><td>0.6679</td></tr><tr><td>HMM using word stems for supervised learning</td><td>0.4446</td><td>0.6583</td><td>0.5308</td><td>0.7377</td><td>0.6645</td></tr><tr><td>HMM using POS for unsupervised learning</td><td>0.7221</td><td>0.3174</td><td>0.4410</td><td>0.3891</td><td>0.4723</td></tr><tr><td>HMM using word stems for unsupervised learning</td><td>0.3803</td><td>0.3620</td><td>0.3709</td><td>0.5696</td><td>0.5223</td></tr><tr><td colspan="6">Detection using Conditional Random Fields</td></tr><tr><td>CR Fusing POS for supervised learning</td><td>0.2568</td><td>0.5263</td><td>0.3451</td><td>0.6749</td><td>0.5705</td></tr><tr><td colspan="6">Rule Benchmark: No Inverting</td></tr><tr><td>1 No negation recognition</td><td>0.0000</td><td>1.0000</td><td>0.0000</td><td>0.6663</td><td>0.5000</td></tr><tr><td colspan="6">Rule Negation of Sentence Fragments</td></tr><tr><td>2 Negation of all following words</td><td>0.5980</td><td>0.3529</td><td>0.4439</td><td>0.5000</td><td>0.5245</td></tr><tr><td>3 Negation of the whole sentence</td><td>1.0000</td><td>0.3337</td><td>0.5004</td><td>0.3337</td><td>0.5000</td></tr><tr><td colspan="6">Rule Negation of Fixed Window Sizes</td></tr><tr><td>4a Negation of fixed window of 1 word</td><td>0.1142</td><td>0.9498</td><td>0.2038</td><td>0.7024</td><td>0.5556</td></tr><tr><td>4b Negation of fixed window of 2 words</td><td>0.2085</td><td>0.8795</td><td>0.3370</td><td>0.7264</td><td>0.5971</td></tr><tr><td>4c Negation of fixed window of 3 words</td><td>0.2842</td><td>0.8158</td><td>0.4215</td><td>0.7397</td><td>0.6260</td></tr><tr><td>4d Negation of fixed window of 4 words</td><td>0.3444</td><td>0.7588</td><td>0.4738</td><td>0.7447</td><td>0.6448</td></tr><tr><td>4e Negation of fixed window of 5 words</td><td>0.3930</td><td>0.7103</td><td>0.5060</td><td>0.7440</td><td>0.6564</td></tr></table>

## 4.1. Comparison using the manually labeled dataset

We start our evaluation with a manually-labeled dataset consisting of 3100 extracted sentences. For this purpose, we compare the forecast performance in negation scope prediction of reinforcement learning to the performance of generative probabilistic models and linguistic rules from the related literature. In this context, we use 10- fold cross-validation [44] to calculate accuracy, precision, recall and $F _ { 1 }$ score of the prediction. In addition, we also calculate the so-called balanced accuracy, also known as eficiency, which is defined as the arithmetic mean of sensitivity and specificity. Since this performance metric corrects for inflated estimates on imbalanced datasets, it is well suited for our task [45]. The results for the different approaches are listed in Table 2.

![](/api/attachments/YAFVKS29/fulltext/images/a1aeded2d648d94cde0cff20fba60ab8692f489ee60729046a6a98281ed50263.jpg)

First, we assess the suitability of reinforcement learning for negation scope detection on the labeled dataset. In order to choose the most appropriate parameter setup, we generate models using various combinations of the model parameters a, c and e. These parameters are varied between zero and one using a step size of 0.1, resulting in a total number of 1331 trained models for reinforcement learning. Out of all considered models, we find the highest balanced accuracy of 70.17% using word stem unigrams with the parameter combination of $\alpha = 0 . 1$ $\gamma = 0 . 1$ 1 and $\varepsilon = 0 . 1$ . The sensitivity for the different parameter settings using word stem unigrams is also visualized in Fig. 5. The left plot shows the variation of the balanced accuracy for different parameters, whereas the right plot shows the variation of the reward that is cumulated across all sequences. Evidently, the model is most sensitive to changing the parameter e, whereas the parameters a and c have a smaller effect.

In contrast to reinforcement learning, the above generative probabilistic models lead to overall inferior results for negation scope detection. In the case of supervised learning, Hidden Markov models outperform the conditional random field implementation and show thehighestbalancedaccuracywhenusingpart-of-speechtagsastraining data. The unsupervised learning method using the Baum–Welch algorithm obtains, generally speaking, inferior performance results, possibly because of the complex grammar used in financial news.

When it comes to linguistic rules, negations only affect the meaning of small sentence fragments; the meaning of words at the beginning of a sentence is unlikely to be inverted. Thus, data labels are unevenly distributed and the accuracy of the gold standard (by always guessing ¬Negated) goes well beyond 50%. Consequently, our benchmark model given by rule 1 (which does not recognize negations at all) has an accuracy of 66.63%, equivalent to the share of non-negated words in the dataset. Rules that negate complete sentence fragments (rules 2 and 3) achieve a high recall but produce low accuracy. In contrast, rules that negate only fixed window sizes after the occurrence of a negation word lead to superior outcomes. In fact, the highest balanced accuracy of 65.64% for rule-based algorithms is achieved using a fixed negation window of 5 words. Altogether, we find that negation scope detection using reinforcement learning in combination with part-of-speech patterns dominates linguistic rules, as well as generative probabilistic models, in terms of predictive accuracy on a manually-labeled dataset.

## 4.2. Comparison using sentiment analysis as a NLP application

We now evaluate how negations in financial news affect sentiment analysis. In a first step, we calculate a sentiment value for each announcement with varying negation detection algorithms. In a second step, we analyze the correlation between the sentiment values and the corresponding daily stock market returns as measure for

![](/api/attachments/YAFVKS29/fulltext/images/a58a2fac785f2637d6b5bfe848c40f85e25cd6583b5d7971793128daf582caf2.jpg)  
Fig. 5. Sensitivity analysis for the most relevant parameters in reinforcement learning using word stem unigrams. Left: variation of balanced accuracy for different parameter settings. Right: variation of the reward that is cumulated by the agent across all sequences.

Please cite this article as: N. Pröllochs, et al., Negation scope detection in sentiment analysis: Decision support for news-driven trading, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.05.009

Table 3  
Negation scope detection using rule-based and machine learning approaches compared according to sentiment analysis, using the negation list from Ref. [43]. Cells are colored according to value (the darker the color, the higher and better the result).

<table><tr><td rowspan="2">Method</td><td colspan="3">Results: Sentiment Analysis</td></tr><tr><td>Correlation</td><td>Δ Correlation (in %)</td><td>Computation Time (in μs)</td></tr><tr><td colspan="4">ReinforcementLearning</td></tr><tr><td>Reinforcement Learning using word stem 1-grams</td><td>0.0866</td><td>8.51</td><td>4.56</td></tr><tr><td>Reinforcement Learning using word stem 2-grams</td><td>0.0814</td><td>1.99</td><td>4.78</td></tr><tr><td>Reinforcement Learning using word stem 3-grams</td><td>0.0801</td><td>0.37</td><td>4.76</td></tr><tr><td>Reinforcement Learning using word stem 4-grams</td><td>0.0798</td><td>0.00</td><td>4.91</td></tr><tr><td>Reinforcement Learning using POS 1-grams</td><td>0.0877</td><td>9.94</td><td>25.94</td></tr><tr><td>Reinforcement Learning using POS 2-grams</td><td>0.0873</td><td>9.35</td><td>25.57</td></tr><tr><td>Reinforcement Learning using POS 3-grams</td><td>0.0883</td><td>10.63</td><td>25.67</td></tr><tr><td>Reinforcement Learning using POS 4-grams</td><td>0.0865</td><td>8.46</td><td>26.45</td></tr><tr><td colspan="4">Detection using Hidden Markov Models</td></tr><tr><td>HMM using POS for supervised learning</td><td>0.0827</td><td>3.59</td><td>32.82</td></tr><tr><td>HMM using word stems for supervised learning</td><td>0.0830</td><td>4.02</td><td>469.71</td></tr><tr><td>HMM using POS for unsupervised learning</td><td>0.0776</td><td>-2.69</td><td>33.75</td></tr><tr><td>HMM using word stems for unsupervised learning</td><td>0.0820</td><td>2.72</td><td>460.72</td></tr><tr><td colspan="4">Detection using Conditional Random Fields</td></tr><tr><td>CRF using POS for supervised learning</td><td>0.0833</td><td>4.42</td><td>28.55</td></tr><tr><td colspan="4">Rule Benchmark: No Inverting</td></tr><tr><td>1 No negation recognition</td><td>0.0798</td><td>-</td><td>-</td></tr><tr><td colspan="4">Rule Negation of Sentence Fragments</td></tr><tr><td>2 Negation of all following words</td><td>0.0845</td><td>5.90</td><td>3.98</td></tr><tr><td>3 Negation of the whole sentence</td><td>0.0781</td><td>-2.08</td><td>4.03</td></tr><tr><td colspan="4">Rule Negation of Fixed Window Sizes</td></tr><tr><td>4a Negation of fixed window of 1 word</td><td>0.0842</td><td>5.54</td><td>3.99</td></tr><tr><td>4b Negation of fixed window of 2 words</td><td>0.0858</td><td>7.59</td><td>3.99</td></tr><tr><td>4c Negation of fixed window of 3 words</td><td>0.0871</td><td>9.20</td><td>4.00</td></tr><tr><td>4d Negation of fixed window of 4 words</td><td>0.0870</td><td>9.04</td><td>3.96</td></tr><tr><td>4e Negation of fixed window of 5 words</td><td>0.0875</td><td>9.61</td><td>3.98</td></tr></table>

predictive power. The results of the correlation values are listed in Table 3.

A benchmark model, in which negations are left untreated, gives a correlation of 0.0798 between the sentiment value and stock market return. Out of all the considered reinforcement learning implementations, choosing part-of-speech 3-grams results in the highest predictive performance, improving the correlation with the corresponding stock market returns by 10.63% in comparison to the benchmark.

Negation scope detection using generative probabilistic models leads to inferior results. Here, we achieve the highest correlation when training a conditional random field using part-of-speech tags— improving the correlation by 4.07% in comparison to the benchmark model. Similar to Ref. [22], we achieve the highest correlation among all rules when using a negation window with a fixed size of 5 words (rule 4e). This rule improves the correlation by 9.61% in comparison to the benchmark. In contrast, rules 2 and 3 that negate complete parts of sentences lead to an inferior performance.

Overall, we find that methods that show a high accuracy on the labeled dataset also tend to achieve a superior performance in sentiment analysis. Our reinforcement learning strategy outperforms all other approaches.

We now hypothesize why reinforcement learning works best with stems on the labeled dataset and with part-of-speech tags in the sentiment application. In fact, the large number of possible states can raise issues of overfitting, which makes implementations with fewer states beneficial within sentiment analysis. The use of n-grams yields only marginal changes as our definition of states implies a recursive fashion where one word can pass on a negation scope. Altogether, reinforcement learning performs best, since labeled sequences can be biased due to subjective interpretation and do not adequately reflect the perception of investors of the stock market. Lastly, rules achieve a fair performance as financial news consist of relatively long and intricate sentences (as in ad hoc announcements) where simple rules are less likely to be affected by the complex grammar.

Finally, we note that the impact of negations in sentiment analysis seems to be more significant than for the predictive performance of the manually-labeled dataset. This is an effect which can be explained as follows: when measuring sentiment in textual materials, only those words that also appear in the dictionary are taken into account. These dictionary entries apparently occur more often after a negation word and, thus, are more dependent on correct negation classification. Overall, 4.74% of all sentences contain at least one negation word according to the negation list from Ref. [43] in Table 1. Each of these sentences contains an average of 0.906 dictionary entries, whereas this number drops to 0.596 for sentences without negations. When examining the position of dictionary entries in negated sentences more closely, 39.56% precede a negation, while 60.46% follow a negation.

## 4.3. Comparison of computation times

Next, we consider the average computation times for the identification of negation scopes.<sup>5</sup> The mean computation times for the different rules in microseconds per sentence are listed in the last column of Table 3. In this comparison, we exclude the time needed for training the models.

Rules that negate either fixed window sizes or sentence fragments require a computation time of approximately 3.98 ls. When it comes to machine learning approaches, they are likely to exceed the runtimes of rule-based algorithms. For example, the Viterbi algorithm (used for decoding the state sequences in our Hidden Markov model and conditional random field implementations) requires significantly more computational operations: a Hidden Markov model and the conditional random field require 32.82 ls and 28.55 ls, respectively, when using part-of-speech tags as emission symbols. A HMM using word stems requires 469.71 ls, which is 118.02 times longer than the time needed for rules with a fixed window size. In contrast, the reinforcement learning approach entails a shorter runtime per sentence; for example, when using word stems as training data, these algorithms require 4.75 ls on average.

When using part-of-speech patterns, we have to calculate the corresponding POS tags for each word in a sentence. To compute these tags, these algorithms require, on average, a computation time of around 25.91 ls, which is 6.51 times longer than the average computation time for the rule-based algorithms. Notably, machine learning methods also require a large additional computation time to build and train the models beforehand.

Table 4  
Comparison of best performing methods across different sets of negation words.

<table><tr><td>Source negations</td><td>Best performing method</td><td>Correlation</td><td>ΔCorrelation (in %)</td></tr><tr><td>Councill et al. [13], Lapponi [24]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0880</td><td>10.28</td></tr><tr><td>Dadvar et al. [22]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0875</td><td>9.63</td></tr><tr><td>Ferris et al. [26]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0875</td><td>9.60</td></tr><tr><td>Jia et al. [19], Hogenboom et al. [20]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0876</td><td>9.77</td></tr><tr><td>Pröllochs et al. [43]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0883</td><td>10.63</td></tr><tr><td>Taboada et al. [21]</td><td>Reinforcement learning using POS 3-grams</td><td>0.0878</td><td>10.02</td></tr></table>

## 4.4. Comparison across different negation word sets

Ultimately, we evaluate how different negation word lists translate into improvements for sentiment analysis. Hence, Table 4 provides a comparison of the best performing methods across all negation word sets. Surprisingly, we first see that, irrespective of which negation word set we choose, reinforcement learning performs best. Second, the largest improvement in terms of correlation results from using the word list proposed in Ref. [43]. A possible explanation might be that this list is a tradeoff between being too short and causing overfitting. Third, we notice that a fixed negation window of 5 words appears to be a suitable choice among the rule-based variants.

## 4.5. Robustness checks using IMDb movie review dataset

As a final step, we validate the benefits of negation scope detection for other text sources. For this purpose, we utilize a second dataset that consists of 5006 movie reviews originating from the Internet Movie Database archive (IMDb). Here, we use the scaled dataset<sup>6</sup> from Ref.[46].Thedocumentsaremanuallylabeledbyexternalsubjectsand are a frequent choice in the literature when it comes to evaluating and comparing methods for sentiment analysis [47].

In the following, we briefly introduce the main results, while more detailed results for the individual methods are presented in our online appendix. To determine the negation scopes for the IMDb movie review dataset, we use the already trained models from the preceding sections. We find a correlation of 0.1804 between the sentiment values and the IMDb review ratings using the benchmark model, in which occurring negations are left untreated. When incorporating negations, reinforcement learning outperforms the generative probabilistic models and increases the correlation with the IMDb review ratings by up to 2.74%. Altogether, the results strongly afirm that negation scope detection can enhance the accuracy of sentiment analysis for text sources from an arbitrary domain.

## 5. Discussion

This paper provides a proof of concept that reinforcement learning can enhance the detection of negation scopes. This is interesting since this method tries to imitate human-like learning. Based on our results, we note that negations significantly impact the perception of investors of the stock market. This opens a path as to how further research can benefit from enhancements in negation scope detection when studying how investors react to negated sentence fragments. Accordingly, our three main implications are as follows.

Implication 1. Reinforcement learning for negation scope detection can exceed the balanced accuracy of rule-based approaches from the related literature by up to 4.53 percentage points on a labeled dataset (e.g. [20, 43]). In addition, reinforcement learning also provides the highest gains across all of the above methods when it comes to sentiment analysis.

Implication 2. Dictionary-based sentiment analysis can be misleading when ignoring the correct classification of negation scopes. In fact, incorporating negations into sentiment analysis leads to an improvement in correlation with stock market returns of up to 10.63%. This is even more striking when keeping in mind that only around 4.74% of all sentences in German ad hoc announcements contain negations.

Implication 3. The interpretation of written text depends on negations. Thus, practitioners from investor relations and media departments should be cautious when framing negative statements using negations and positive terms because of the fact that these negations are identified by investors when judging an investment.

Altogether, our findings indicate that handling negations plays a decisive role in measuring the tone of financial news. This also coincides with corresponding hypotheses from related literature (e.g. [1, 5, 18]). Accordingly, practitioners, investors or automated traders should consider negations when forming their trading decisions.

## 6. Conclusion

As its main contribution, this paper proposes and compares methods for predicting negation scopes across different sets of negation words. We follow a two-sided approach. We evaluate the predictive performance not only on a manually-labeled dataset, but examine the benefits of predicted negation scopes in an application from natural language processing — more precisely, how the sentiment analysis of financial news can be improved. In terms of classification accuracy on a labeled dataset, reinforcement learning outperforms rule-based algorithms, as well as common machine learning approaches from the literature, leading to a balanced classification accuracy of up to 70.17%.

In terms of sentiment analysis, reinforcement learning is also superior. In this instance, we achieve an improvement in correlation between sentiment value and stock market return of up to 10.63% in comparison to a benchmark model with no handling of negations. However, the considerable overall improvement reinforces negation scope detection as a crucial component of sentiment analysis.

## Acknowledgments

The valuable contributions of Laura Cuthbertson, Amiran Gelantia and Ryan Grabowski are gratefully acknowledged.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2016.05.009.

## References

[1] P.C. Tetlock, Giving content to investor sentiment: the role of media in the stock market, Journal of Finance 62 (2007) 1139–1168.

[2] E. Henry, Are investors influenced by how earnings press releases are written? Journal of Business Communication 45 (2008) 363–407.

[3] E.A. Demers, C. Vega, Soft information in earnings announcements: news or noise? SSRN Electronic Journal (2010)

[4] S. Feuerriegel, G. Wolff, D. Neumann, News sentiment and overshooting of exchange rates, Applied Economics (2016) in press.

[5] T. Loughran, B. McDonald, IPO first-day returns, offer price revisions, volatility, and form S-1 language, Journal of Financial Economics 109 (2013) 307–326.

[6] R. Balakrishnan, X.Y. Qiu, P. Srinivasan, On the predictive ability of narrative disclosures in annual reports, European Journal of Operational Research 202 (2010) 789–801.

[7] S.W. Chan, J. Franklin, A text-based decision support system for financial sequence prediction, Decision Support Systems 52 (2011) 189–198.

[8] E. Fersini, E. Messina, F.A. Pozzi, Sentiment analysis: Bayesian ensemble learning, Decision Support Systems 68 (2014) 26–38.

[9] Y.-M. Li, T.-Y. Li, Deriving market intelligence from microblogs, Decision Support Systems 55 (2013) 206–217.

[10] G. Wang, J. Sun, J. Ma, K. Xu, J. Gu, Sentiment classification: the contribution of ensemble learning, Decision Support Systems 57 (2014) 77–93.

[11] L. Rokach, R. Romano, O. Maimon, Negation recognition in medical narrative reports, Information Retrieval 11 (2008) 499–538.

[12] R.S. Sutton, A.G. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, MA, 1998.

[13] I.G Councill, R. McDonald, L. Velikovich, What’s great and what’s not: learning to classify the scope of negation for improved sentiment analysis, Proceedings of the Workshop on Negation and Speculation in Natural Language Processing, AssociationforComputationalLinguistics,Stroudsburg,PA,USA,2010, pp.51–59.

[14] M. Wiegand, A. Balahur, B. Roth, D. Klakow, A. Montoyo, A survey on the role of negation in sentiment analysis, Proceedings of the Workshop on Negation and Speculation in Natural Language Processing, Association for Computational Linguistics, Stroudsburg, PA, USA, 2010, pp. 60–68.

[15] A.Athar,Sentimentanalysisof citationsusingsentencestructure-basedfeatures, Proceedings of the ACL, 2011. pp. 81–87.

[16] S. Padmaja, S. Fatima, S. Bandu, Evaluating sentiment analysis methods and identifyingscopeofnegationinnewspaperarticles,InternationalJournalofAdvanced Research in Artificial Intelligence 3 (2014) 1–6.

[17] J. Reitan, J. Faret, B. Gambäck, L. Bungum, Negation scope detection for Twitter sentiment analysis, Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis, 2015. pp. 99–108.

[18] T. Loughran, B. McDonald, When is a liability not a liability? Textual Analysis, Dictionaries, and 10-Ks, Journal of Finance 66 (2011) 35–65.

[19] L. Jia, C. Yu, W. Meng, The effect of negation on sentiment analysis and retrieval effectiveness,in:D.Cheung(Ed.), Proceedingofthe18thACMConferenceonInformation and Knowledge Management (CIKM ’09), ACM, New York, NY, 2009, pp. 1827–1830.

[20] A. Hogenboom, P. van Iterson, B. Heerschop, F. Frasincar, U.Kaymak, Determining negationscopeandstrengthinsentimentanalysis,IEEEInternationalConference on Systems, Man, and Cybernetics, 2011. pp. 2589–2594.

[21] M. Taboada, J. Brooke, M. Tofiloski, K. Voll, M. Stede, Lexicon-based methods for sentiment analysis, Computational Linguistics 37 (2011) 267–307.

[22] M. Dadvar, C. Hauff, F de Jong, Scope of negation detection in sentiment analysis, ProceedingsoftheDutch-BelgianInformationRetrievalWorkshop, Universityof Amsterdam, Amsterdam, Netherlands, 2011, pp. 16–20.

[23] A. Abu-Jbara, D. Radev, UMichigan: A conditional random field model for resolving the scope of negation, Proceedings of the First Joint Conference on Lexical and Computational Semantics (SemEval ’12), 2012. pp. 328–334.

[24] E.Lapponi,WhyNot!SequenceLabelingtheScopeofNegationUsingDependency Features, University of Oslo, Oslo, Norway, 2012. Master’s Thesis

[25] R. Remus, Modeling and representing negation in data-driven machine learning-based sentiment analysis, Proceedings of the 1st International Workshop on EmotionandSentimentinSocialandExpressiveMedia(ESSEM),2013.pp.22–33.

[26] S.P. Ferris, Q. Hao, M.-Y. Liao, The effect of issuer conservatism on IPO pricing and performance, Review of Finance 17 (2013) 993–1027.

[27] I. Erev, A.E. Roth, Predicting how people play games: reinforcement learning in experimental games with unique mixed strategyequilibria American Economic Review(1998)848-881.

[28] C.D.Manning,H.Schütze,FoundationsofStatisticalNaturalLanguageProcessing, MITPress Cambridge MA 1999

[29] N. Pröllochs, S. Feuerriegel, D. Neumann, Detecting negation scopes for financial news sentiment using reinforcement learning, 49th Hawaii International Conference on System Sciences(HICSS) 2016, pp. 1164-1173.

[30] B.Pang,L.Lee,Opinionminingandsentimentanalysis,FoundationsandTrendsin Information Retrieval 2 (2008) 1–135.

[31] R.P.Schumaker,H.Chen,Aquantitativestockpredictionsystembasedonfinancial news, Information Processing & Management 45 (2009) 571–583.

[32] S. Feuerriegel, D. Neumann, News or noise? How news drives commodity prices, Proceedings of the International Conference on Information Systems (ICIS 2013) Association for Information Systems. 2012,

[33] J.Hu,M.P.Wellman,NashQ-learningforgeneral-sumstochasticgames,Journalof Machine Learning Research 4 (2003) 1039–1069.

[34] P.F. Brown, P.V. Desouza, R.L. Mercer, V.J.D. Della Pietra, J.C. Lai, Class-based N-gram models of natural language, Computational Linguistics 18 (1992) 467–479.

[35] P. Lichodzijewski, M. Heywood, Binary versus real-valued reward functions under coevolutionary reinforcement learning, Proceedings of the International Conference on Artificial Evolution, 2009.

[36] L.R. Rabiner, A tutorial on Hidden Markov models and selected applications in speech recognition, Proceedings of the IEEE 77 (1989) 257–286.

[37] C. Sutton, A. McCallum, An introduction to conditional random fields for relational learning, Foundations and Trends in Information Retrieval 4 (2011) 267–373.

[38] S. Feuerriegel, A. Ratku, D. Neumann, Analysis of how underlying topics in financial news affect stock prices using latent dirichlet allocation, 49th Hawaii International Conference on System Sciences (HICSS), 2016. pp. 1072–1081.

[39] S.S. Groth, J. Muntermann, An intraday market risk management approach based on textual analysis, Decision Support Systems 50 (2011) 680–691.

[40] M. Hagenau, M. Liebmann, D. Neumann, Automated news reading: stock price prediction based on financial news using context-capturing features, Decision Support Systems 55 (2013) 685–697.

[41] J. Muntermann, A. Guettler, Intraday stock price effects of ad hoc disclosures: the Germancase,J.JournalofInternationalFinancialMarkets,InstitutionsandMoney 17 (2007) 1–24.

[42] B.McDonald,LoughranandMcDonaldFinancialSentimentDictionary,2012,URL http://www3.nd.edu/mcdonald/Word\_Lists.html.

[43] N. Pröllochs, S. Feuerriegel, D. Neumann, Enhancing sentiment analysis of financial news by detecting negation scopes, 48th Hawaii International Conference on System Sciences (HICSS), 2015. pp. 959–968.

[44] C.M.Bishop,Patternrecognitionandmachinelearning, 8ed., Springer,NewYork, NY, 2009.

[45] V. Garcia, R.A. Mollineda, J.S. Sánchez, Index of balanced accuracy: a performance measure for skewed class distributions, Pattern Recognition and Image Analysis Springer. 2009, pp. 441–448.

[46] B. Pang, L. Lee, Seeing stars: exploiting class relationships for sentiment categorization with respect to rating scales, Proceedings of the 43rd Annual Meeting on Association for Computational Linguistics (ACL ’05), 2005. pp. 115–124.

[47] G. Li, F. Liu, Application of a clustering method on sentiment analysis, Journal of Information Science 38 (2012) 127–139.

![](/api/attachments/YAFVKS29/fulltext/images/b1827267fa2d0be2756a6310a94830de9b8438dc66ceeb2b6ce5160062f9b0f9.jpg)  
Nicolas Pröllochs is a PhD student at the Chair of Information Systems of the University of Freiburg with a focus on text mining and sentiment analysis of financial news. He holds a Master of Science in Economics and Information Systems from the University of Freiburg. He has co-authored research publications for the Hawaii International Conference on System Sciences, the European Conference on Information Systems and the Conference on Information Systems and Technology.

![](/api/attachments/YAFVKS29/fulltext/images/66d11f43e8441b53d04ef5f4b6d8f9820c4de45ed954909d32f30a6cf2555d74.jpg)

Stefan Feuerriegel is a postdoctoral researcher at the Chair of Information Systems of the University of Freiburg with a focus on text mining and sentiment analysis of financial news. He holds a Master of Science in Simulation Sciences from the RWTH Aachen University, He has co-authored research publications in the European Journal of Operational Research, International Journal of Applied Mathematics and Computer Science, Optimization Engineering and the Journal of Decision Systems.

![](/api/attachments/YAFVKS29/fulltext/images/7bd316e06b3595bbf02122d617b595c5bc63ba852eb055b7d135b6f332d62b09.jpg)

Dirk Neumann is a full professor with the Chair of Infor mation Systems of the University of Freiburg, Germany. His research topics include Business Analytics, Text Min ing and Cloud Computing. He studied information systems in Giessen (Dinloma). Economics in Milwaukee WI USA (Master) and received a PhD from Karlsruhe Institute of Technology (KIT) in 2004. He has (co-)authored many research publications at European Journal of Operationa Research, ACM Transactions on Internet Technology, Journal of Management of Management Information Systems or Decision Support Systems.
