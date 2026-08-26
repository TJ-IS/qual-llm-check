---
otero_id: 8144
otero_key: "TSBSG3KK"
title: "TM-OKC: An Unsupervised Topic Model for Text in Online Knowledge Communities"
authors: "Dongcheng Zhang; Kunpeng Zhang; Yi Yang; David A. Schweidel"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17885"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# TM-OKC: AN UNSUPERVISED TOPIC MODEL FOR TEXT IN ONLINE KNOWLEDGE COMMUNITIES<sup>1</sup>

Dongcheng Zhang CUHK Business School, The Chinese University of Hong Kong, Shatin, Hong Kong SAR, CHINA {dongchengzhang@cuhk.edu.hk}

Kunpeng Zhang Department of Decision, Operations and Information Technologies, Robert H. Smith School of Business, University of Maryland, College Park, College Park, MD 20742, U.S.A. {kpzhang@umd.edu}

Yi Yang Department of Information Systems, Business Statistics and Operations Management, Hong Kong University of Science and Technology, Hong Kong SAR, CHINA {imyiyang@ust.hk}

David A. Schweidel Goizueta Business School, Emory University, Atlanta, GA 30322, U.S.A. {dschweidel@emory.edu}

Online knowledge communities (OKCs), such as question-and-answer sites, have become increasingly popular venues for knowledge sharing. Accordingly, it is necessary for researchers and practitioners to develop effective and efficient text analysis tools to understand the massive amount of user-generated content (UGC) on OKCs. Unsupervised topic modeling has been widely adopted to extract humaninterpretable latent topics embedded in texts. These identified topics can be further used in subsequent analysis and managerial practices. However, existing generic topic models that assume documents are independent are inappropriate for analyzing OKCs where structural relationships exist between questions and answers. Thus, a new method is needed to fill this research gap. In this study, we propose a new topic model specifically designed for the text in OKCs. We make three primary contributions to the research on topic modeling in this context. First, we build a general and flexible Bayesian framework to explicitly model structural and temporal dependencies among texts. Second, we statistically demonstrate the approximate model inference using mean-field and coordinate ascent algorithms. Third, we showcase the practical value and relative merit of our method via a specific downstream task (i.e., user profiling). The proposed model is illustrated using two real-world datasets from well-known OKCs (i.e., Stack Exchange and Quora), and extensive experiments demonstrate its superiority over several cutting-edge benchmarks.

Keywords: Unsupervised topic model, document dependency, variational inference, practical value, question-and-answer

## Introduction

User-generated content (UGC) continues to make a wealth of text data readily available. One manifestation of this trend is online question-and-answer (Q&A) communities and discussion forums, which are platforms for knowledge sharing and information seeking on which users can ask and answer questions in a threaded structure. For example, Stack Exchange is a network of such information exchange websites, each covering a specific theme (e.g., Stack Overflow is the Stack Exchange site for professional programmers and amateur programming enthusiasts) (Xu et al., 2019).

Organizations have also launched knowledge exchange forums to promote knowledge sharing among employees (McKinsey, 2013; Pu et al., 2022). The growth of these online knowledge communities (OKCs) has resulted in a massive amount of text data, and this accumulation of knowledge and information is a potentially rich source of insight for researchers and practitioners.

To identify latent topics embedded in such textual data, topic modeling has become the dominant technique used by information systems (IS) and business discipline researchers (Tirunillai & Tellis, 2014; Loughran & McDonald, 2016; Rivera et al., 2021). Among topic modeling methods, latent Dirichlet allocation (LDA) has been widely used in many studies (Blei et al., 2003). LDA can automatically uncover latent topics from a collection of documents and provide a probabilistic human-understandable interpretation of textual data. In addition, LDA and its variants have been widely integrated with qualitative and quantitative methodologies to generate theory (Huang et al., 2018a; Bellstam et al., 2021; Rai, 2016).

Researchers have used the latent topic vectors learned from topic models to either understand text or incorporate the learned vectors into subsequent analyses. For example, Bao and Datta (2014) used topic models to discover and quantify risk types based on corporate annual reports. Ghose et al. (2019) derived a semantic complexity measure based on review topic vectors to study the impact of review complexity on consumers’ search behavior. Topic features can also be used to measure the topic-sensitive influence of Twitter users (Weng et al., 2010) and the topic-specific expertise level of community members (Liu et al., 2020). In addition, topic models also exhibit many practical values on various applications, such as user profiling, reducing information overload, and trending topic detection (Wang et al., 2011; Geva et al., 2019; Zhong & Schweidel, 2020). In these scenarios, obtaining high-quality topic vectors (i.e., those with high representation capability and human interpretability) is critical, as imperfect topic modeling could lead to incomprehensible text mining results or measurement errors that can cause biased estimations (Yang et al., 2018).

Generic unsupervised topic models, including traditional statistical topic models (e.g., LDA) and new deep learningbased topic models (e.g., neural topic model [NTM]—Miao et al., 2017; Dieng et al., 2020) typically assume that documents are independent of each other. However, the most prominent structural feature in OKCs is that posts (i.e., questions and answers) are organized within Q&A or discussion threads, resulting in a strong dependency between the topics of the original question and subsequent answers. These dependencies could play an important role and ignoring them might result in suboptimal topic modeling that affects representation and interpretability and accordingly influences downstream tasks.<sup>2</sup>

To model the structural information in OKC texts, researchers have recently developed two streams of topic modeling methods. The first leverages the observed attributes of posts (e.g., author demographics and the post category) to model relations among posts. Specifically, these methods assume that posts with the same attributes exhibit similar topic distributions (Ma et al., 2015; Card et al., 2018; Roberts et al., 2019). However, posts are still assumed to be independent of each other during model inference, thereby neglecting the explicit structural impact of one post on another. This can be problematic because two posts may have completely different observed attributes, but their topics might be correlated because of the Q&A threaded structure (i.e., question-answer, prior answer-current answer). In addition, due to the privacy concerns and anonymity rules of many online communities, such attribute-level data may not be publicly available.

To explicitly capture the interdependencies among texts in topic modeling, especially when post-related attributes are not available, researchers developed the second stream of methods that focus on modeling Q&A relations and threaded structures among posts. Although several studies have pursued this direction of model development, their topic models capture the structural relations among posts in a partial way (Wang et al., 2011; Ji et al., 2012; Li et al., 2018). For example, LeadLDA was proposed to model the conversational structures of microblog posts with topic dependencies (Li et al., 2018; Magdy et al., 2020). However, this method assumes that the topic of the current post only depends on its parent post (i.e., the nearest ancestor post) rather than its more distant ancestors. Ignoring such long-range dependencies in a conversation thread may deteriorate the topic modeling performance. To simplify the model, this method also restricts each post to a single topic. The SITS (Speaker Identity for Topic Segmentation) model not only considers the threaded structure but also allows multiple topics for a single post (Rossiter, 2022); however, it still does not capture long-range dependencies. Furthermore, both LeadLDA and SITS do not distinguish the inherently different roles between questions (or initialized posts) and answers (or responses). The ability to draw such distinctions could be informative in topic modeling, especially in OKCs, where questions may initiate topics followed by answers and answers may introduce new topics.

To address this research gap, we propose a novel unsupervised Bayesian topic modeling framework for OKC texts (TM-OKC) that explicitly captures complex relationships among the posts. First, our method assumes that the topic distribution of a post follows a logistic-normal distribution. This allows for a mixture of topics within one post, and different posts can have different focal topics. Second, our method allows for the possibility that the topics of the current answer may be affected by the question and also potentially by prior answers. To make the dependency setting closer to the reality of OKCs, we introduce a binary latent variable in our model to denote whether an answer is novel (e.g., when the user does not pay attention to prior answers and writes a response that is independent of the previous answers) or whether it follows up on previous answers. To capture different probabilities of being a novel answer in different Q&A threads, the binary variable is drawn from a binomial distribution, whose parameter is generated from a beta distribution. Note that any answer should be somehow relevant to the question if participants decide to provide their opinions. Therefore, the topics of a novel answer are only dependent on the question, while the topics of a follow-up answer depend on both its question and prior answers. Both novel and follow-up answers may introduce additional topics due to the variances of random variables. In other words, users can bring information that may not be covered or may be less saliently mentioned in the question or prior answers based on their own understanding.

Take a real question in our data as an example: “How do you boil coffee in the morning?” Most answers provide relevant information, such as the optimal temperature and water amount. However, some topics that are not explicitly raised in the question or previous answers (e.g., recipes or the brand of coffee machines) can become salient in current answers.

Third, nontrivial technical challenges exist in our unified Bayesian framework. Exact inference becomes intractable when jointly modeling these interdependencies among topics and the novelty of answers. Thus, in this study, we adopted the variational inference paradigm and used the mean-field approach to approximate the posterior distribution of latent variables given just the observed text corpus.

To demonstrate the superior performance of our TM-OKC model, we conducted several computational experiments and lab studies using two datasets from well-known OKCs (i.e., Stack Exchange and Quora). First, we evaluated the statistical model fit on a holdout dataset and showed better performance in terms of perplexity and coherence compared to cutting-edge topic models. We also demonstrated the superior representation capability and interpretability of our TM-OKC using a document classification task and two lab studies. Second, we chose a specific downstream task (i.e., user profiling) to demonstrate the practical value and relative merit of our TM-OKC. We found that, in addition to the novel design of explicitly modeling structural relationships among texts, TM-OKC does not require large data to obtain reasonably good performance, offering an advantage compared to deep learning-based methods. Third, we demonstrated the flexibility and generalizability of our TM-OKC by analyzing some important parameters (e.g., differential impacts of questions and prior answers, and heterogeneous variances of answer topic distributions). This analysis allowed us to present interesting and meaningful observations that could not have been attained using extant topic models.

Recently, large language models (LLMs) have gained significant attention from the research community and industry professionals. Their remarkable success in natural language understanding and text generation is evident, particularly with the advent of models like ChatGPT (Devlin et al., 2019; Brown et al., 2020; Liu et al., 2023). The foundational architecture fueling these LLMs is the transformer framework, which harnesses the capabilities of neural networks and attention mechanisms to appropriately represent text (Vaswani et al., 2017). LLMs are usually trained with a massive number of diverse datasets including news articles, social media feeds, Q&A-forum discussions, and more, to obtain a broad spectrum of knowledge. This vast training allows LLMs to capture generalized knowledge spanning various domains. Such acquired implicit knowledge proves instrumental in tasks such as answering queries, summarizing content, making recommendations, coding, and offering text representations for downstream applications.

In contrast to the versatile nature of LLMs which can be seen as “generalists,” our topic modeling approach operates more like a “specialist.” It is trained on relatively small datasets, aiming to distill domain-specific or community-specific insights. It is also worth noting that the inherent complexity of LLMs, due to intricate neural networks, indicates that the encoded knowledge is often diffused, making the text representation generally difficult to interpret (AlKhamissi et al., 2022). In contrast, our method yields humaninterpretable results, being rooted in transparent and easily interpretable probabilistic graphical models. Interestingly, combining interpretable classic methods with these highly flexible LLMs presents a promising avenue for future research. This is underscored by the challenges LLMs face in crafting prompts with structured information (Liu et al., 2023). With statistical tools like our TM-OKC that explicitly accommodate textual structure, it becomes possible to design more interpretable prompts that can be used in conjunction with LLMs to produce enhanced and more comprehensible outputs.

This paper contributes to the IS literature in three major ways. First, we identified the structural and temporal dependencies among OKC texts (i.e., Q&A relations and threaded structures). Explicitly incorporating such dependencies into topic modeling can significantly enhance the discovery of latent semantics in texts. Motivated by this, we introduced a novel unsupervised Bayesian topic modeling framework that explicitly captures the complex interdependencies among OKC texts in a more generalizable and realistic way, addressing a gap in the literature and offering a new perspective on text analytics. Second, as exact inference is not practical, we resorted to approximate inference and statistically demonstrated its feasibility using the mean-field and coordinate ascent algorithm. Furthermore, TM-OKC is sufficiently flexible to allow for modified dependency structures, such as removing the dependency among answers by setting the impact weights of prior answers to zero. Third, we conducted experiments on two highly IS-relevant datasets from OKCs, thus allowing us to showcase the superiority and practical value of TM-OKC.

## Literature Review

Our work is built upon and methodologically contributes to the literature of topic modeling for OKC texts. In this section, we organize the relevant literature as follows. First, we summarize how topic modeling has been widely applied in existing OKC research. Next, we review methodological work aimed at developing topic models that can capture structural information in OKC texts. These topic modeling approaches can be mainly categorized into two streams (i.e., based on observed attributes or explicit structural relations). In this paper, we position our research in the second stream and focus on explicitly modeling the complex structural relations among OKC texts. We contrast our work with existing methods along this line, upon which we highlight our contributions.

## Applications of Topic Modeling in OKC Research

An OKC is a virtual space where information can be presented and shared in the form of natural language (Shah, 2010). OKCs typically take the form of a knowledge site, a social question-and-answer (Q&A) community, or a discussion forum. Most OKCs offer text-based, interactive, and asynchronous communication and rely on the voluntary participation of users to generate content (Hwang et al., 2015; Lee et al., 2019). As the popularity of OKCs has grown, researchers have become increasingly interested in investigating various questions raised in OKCs, such as UGC production or consumption (Singh et al., 2014; Pu et al.,

2022), quality assessment of peer-produced content (Velichety et al., 2019), answer usefulness (Kim & Oh, 2009; Liu et al., 2020), and impact of information dissemination (Yue et al., 2019; Hwang et al., 2019).

OKCs contain both a massive number of discussions and a high degree of variation in the topics discussed. To automatically uncover these topics from this large volume of OKC texts, topic modeling approaches have been widely applied by researchers in IS and other business disciplines (Blei, 2012). There are four main ways in which an analysis may benefit from the topic vectors learned by topic models: (1) Identified topic vectors can be used as independent variables. For example, Yue et al. (2019) applied LDA to extract the topics of threaded posts in online hacking forums and explored the impact of different topics on distributed denial of service attacks. (2) Identified topic vectors can be used as dependent variables. For example, Singh et al. (2014) used LDA to identify topics of blogs and comments in an enterprise forum, and they further investigated the effect of various factors (e.g., textual characteristics) on users’ dynamic blog-reading of different topics. (3) Identified topic vectors can be used as control variables. For example, Kumar et al. (2022) studied the impact of trademarking hashtags on consumer engagement in the brand communities on Twitter, where topics of threaded posts learned by LDA were included as control variables in the regression analysis for causal identification. (4) Identified topic vectors can be used to extract and/or derive new variables. For example, Kokkodis et al. (2020) applied LDA to uncover the latent topics of users Q&A posts in an online diabetes community and then categorized users into different contribution types for further user engagement investigation. In addition, Hwang et al. (2019) constructed users’ information networks based on the topics identified by LDA from the Q&A posts in a customer support crowdsourcing community; then, they further explored how the breadth and depth of the topic-based information network influenced the generation of novel ideas. Guo et al. (2017) applied LDA, hierarchical LDA (hLDA), and the dynamic topic model (DTM) to extract representative information from the articles and comments on a blogging platform. Kyriakou et al. (2022) applied a correlated topic model (CTM) on the descriptions and comments about product designs in an online innovation community and used derived topic vectors to calculate the similarity among product designs to further measure novelty. Apart from these illustrative studies, we also extensively reviewed recent OKC studies that apply topic models in IS and other business disciplines, which are summarized in Table A1 of Appendix A.

Based on the topic modeling applications in OKC research reviewed above, we can see that most of these studies applied existing generic topic models including LDA, hLDA, DTM, and CTM to extract topic vectors or identify topics for certain subsequent analyses. Apart from these topic modeling approaches, researchers have also recently proposed combining topic models with deep language models to develop more powerful topic models, such as NTM (Miao et al., 2017; Dieng et al., 2020; Churchill & Singh, 2022). However, these topic models without exception follow the fundamental assumption that documents are independent, ignoring the potential structural relationships among texts (e.g., question-and-answer, post-and-comment, or threaded discussions) and making them inappropriate for the generative process of textual data in OKCs. As a result, the produced topic vectors may be suboptimal and inaccurate and can thus introduce systematic biases into the subsequent analysis and threaten the validity of statistical inference (Yang et al., 2018). In order to incorporate the structural information of OKC texts into topic models, researchers have adopted two perspectives, which we review in the two subsequent subsections.

## Topic Modeling Methods Based on Observed Attributes of OKC Texts

The first stream of topic modeling methods models interdependencies among OKC texts based on their associated observed attributes. Studies in this stream often assume that the attributes of texts have an impact on the topics; that is, that texts having the same attributes (e.g., authors, post types, and rank of answers) may exhibit similar topic distributions. Among these attributes, authorship is one of the most commonly used in topic modeling. One straightforward way to incorporate authorship is to aggregate posts from the same author and apply a topic model (e.g., LDA) to those aggregated texts (Weng et al., 2010; Hong & Davison, 2010). Similar processes can be found in other models. For example, the author-topic model (ATM) allows one post to have multiple users and incorporates authorship into the model as a covariate to influence topics so that posts from similar users have similar topic distributions (Rosen-Zvi et al., 2010). Zhao et al. (2011) proposed Twitter-LDA with userspecific topic distributions, in which each tweet by a user has only one topic drawn from the user’s topic distribution. Sasaki et al. (2014) further combined the topic tracking model (TTM) into Twitter-LDA and proposed Twitter-TTM where the dynamic change of topics was considered. He et al. (2018) also aggregated all the microblog messages posted by the same user and proposed the interaction-aware topic model (IATM) to account for different users’ impact on topic distribution. The topic expertise model (TEM) (Yang et al., 2013) jointly models the topics of posts and the expertise of users in Q&A communities but does not distinguish post types (i.e., question or answer). The tri-role topic model (TRTM) (Ma et al., 2015; Costa & Ortale, 2020) considers the different roles of a user (i.e., asker, answerer, and voter) when modeling posts from the same user. Specifically, TRTM models the relationship among the questions asked by the user, questions answered by that user, and answers written by the same user. Apart from authorship, other attributes such as post type and answer ranking can also be included in topic models—for example, the Bayesian-based structural topic model (STM) (Roberts et al., 2019; Jo et al., 2022). To further improve the expressive power of topic models with attributes, researchers have recently proposed the sparse contextual hidden and observed language autoencoder (SCHOLAR), which leverages deep neural networks to model the impact of observed attributes on topics (Card et al., 2018; Zhao et al., 2021). Table 1 summarizes the differences across these methods in several major dimensions.

<table><tr><td colspan="5">Table 1. Topic Modeling Methods Based on Observed Attributes</td></tr><tr><td>Models</td><td>Explicit topic dependencies among posts</td><td>Author information</td><td>User roles (e.g., asker and answerer)</td><td>Other attributes (e.g., post types and answer ranks)</td></tr><tr><td>Simple aggregation (Weng et al., 2010; Hong &amp; Davison, 2010)</td><td rowspan="6">×</td><td rowspan="6">√</td><td rowspan="6">×</td><td rowspan="6">×</td></tr><tr><td>ATM (Rosen-Zvi et al., 2010)</td></tr><tr><td>Twitter-LDA (Zhao et al., 2011)</td></tr><tr><td>Twitter-TTM (Sasaki et al., 2014)</td></tr><tr><td>IATM (He et al., 2018)</td></tr><tr><td>TEM (Yang et al., 2013)</td></tr><tr><td>Tri-role topic model (Ma et al., 2015; Costa &amp; Ortale, 2020)</td><td>×</td><td>√</td><td>√</td><td>×</td></tr><tr><td>STM (Roberts et al., 2019; Jo et al., 2022)</td><td>×</td><td>√</td><td>√</td><td>√</td></tr><tr><td>SCHOLAR (Card et al., 2018; Zhao et al., 2021)</td><td>×</td><td>√</td><td>√</td><td>√</td></tr></table>

Note: √ indicates that an attribute/relationship is included or modeled in the study while × means it is not.

<table><tr><td colspan="7">Table 2. Topic Modeling Methods Based on Explicit Structural Relations</td></tr><tr><td>Models</td><td>Threaded structure</td><td>Allow for “leader” / novelty</td><td>Multiple topics in one post</td><td>Long-range dependency</td><td>Distinguish Q&amp;A</td><td>Learnable heterogeneity between Q&amp;A</td></tr><tr><td>strTM (Wang et al., 2011)</td><td>√</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>QATM (Ji et al., 2012)</td><td>×</td><td>×</td><td>√</td><td>×</td><td>√</td><td>×</td></tr><tr><td>Forum-LDA (Chen &amp; Ren, 2017)</td><td>×</td><td>×</td><td>√</td><td>×</td><td>√</td><td>×</td></tr><tr><td>LeadLDA (Li et al., 2018; Magdy et al., 2020)</td><td>√</td><td>√</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>SITS (Rossiter, 2022)</td><td>√</td><td>√</td><td>√</td><td>×</td><td>×</td><td>×</td></tr><tr><td>TM-OKC (our model)</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

Note: √ indicates that a component is included or modeled in the study while × means it is not.

However, these attribute-based models have two major limitations. First, such models neglect the explicit structural relations (i.e., Q&A relations and threaded structures) among posts. Although they consider the topic similarity among posts with similar observed attributes, the posts are still assumed to be independent of each other conditional on the attributes already given. In other words, these models ignore the explicit structural impact of one post on another. Furthermore, with the Q&A relations and threaded structures of OKC texts, posts can be related in terms of topics even if they have completely different observed attributes (e.g., authors, user roles, and post types). This could make these attribute-based topic models problematic for learning accurate latent topic distributions. Second, attributes associated with texts may not always be publicly available, or they may be inaccurately measured due to various reasons (e.g., privacy concerns, anonymity rules, and reporting biases). Thus, it is necessary to develop new methods that rely only on texts and model the explicit Q&A relations and threaded structures. This motivates the second stream of topic modeling on OKC texts, which is also the focus of the present study.

## Topic Modeling Methods Based on Explicit Structural Relations of OKC Texts

The second stream of topic modeling methods focuses on explicit structural relations (i.e., Q&A relations and threaded structures) in OKC texts without involving any attribute-level data. In contrast to attribute-based models, where posts are still independent conditioned on the observed attributes, existing methods in this line of work explicitly model the structural dependencies among texts. Ji et al. (2012) proposed the question-answer topic model (QATM) to explicitly model the question-answer relations in OKCs. Nonetheless, QATM does not consider the threaded structure, e.g., the impact of previous answers on the current answer. In addition, QATM assumes a question, and all its answers share exactly the same topic distribution, which rules out the possibility of any variations in future answers. Similarly, forum-LDA takes into account the link between an initialized post (analogous to a question) and its responses (analogous to answers) in a discussion forum, but it does not model the threaded structure of the conversations (Chen & Ren, 2017). To model the threaded structure of OKC texts, Wang et al. (2011) proposed the structural topic model (strTM) with first-order Markov transition among the posts in the same thread. Based on strTM, LeadLDA further differentiates “leaders” and “followers” in the posts when modeling the topic dependencies within a threaded conversation (Li et al., 2018; Magdy et al., 2020). However, when modeling the topic of a given post, both strTM and LeadLDA only consider the impact of its immediate parent post (i.e., nearest ancestor post) rather than its distant ancestors. Ignoring such long-range dependencies might deteriorate the model performance. Furthermore, these approaches do not model the heterogeneity between questions (or initialized posts) and answers (or responses), even if the two are intrinsically different in OKCs. Moreover, they only allow one post to have a single topic in order to simplify the Markov framework, which is not realistic in many contexts. The speaker identity for topic segmentation model (SITS) not only considers the threaded structure but also allows multiple topics in one post (Rossiter, 2022). However, the long-range dependencies and Q&A heterogeneity among OKC texts are still missing. To summarize, these studies have empirically demonstrated the value of modeling explicit structural relationships, but they only partially capture the Q&A and threaded structure of OKC texts.

Given the limitations of extant methods stated above, we aim to develop a general topic modeling approach that relies only on OKC texts and captures the explicit Q&A relations and threaded structures within the texts. Table 2 summarizes the differences between our method and existing ones across several dimensions, demonstrating its increased generalizability and flexibility. As made evident in Table 2, our TM-OKC has two major innovations. (1) Long-range dependency: In real-world OKCs, users engaged in a discussion thread can be influenced by all the historical posts, which is modeled in TM-OKC by allowing the topic distribution of an answer to depend on the question and all prior answers. (2) Learnable Q&A heterogeneity: Though QATM and Forum-LDA do not model the learnable Q&A heterogeneity, they account for the difference between questions and answers. Our TM-OKC goes a step further by allowing for differential impacts of questions and prior answers on the current answer, as well as different topic variances for different types of answers. These heterogeneous parameters can be learned from data to capture richer insights and contribute to better topic modeling performance.

## Our Approach: TM-OKC Topic Model

## Overall Framework Design

Before we elaborate our proposed topic model (TM-OKC), we first discuss the uniqueness of text data with Q&A relations or threaded structures and the importance of modeling structural and temporal dependencies among texts in the context of OKCs. OKC texts differ from traditional unstructured text data, especially when it is necessary to perform common text analysis, such as topic modeling. These differences are as follows. (1) There exists an impact of a question (or an initialized post) on its answers (or its responses) that generic topic models such as LDA ignore. Answers might completely follow their question and cover all topics raised by the question, might only focus on a portion of topics in the question, or could emphasize topics that are only slightly related to the question. (2) The current answer may or may not be affected by prior answers, depending on whether it is a follow-up answer or a novel answer, yet answers are treated as completely unrelated in traditional document analysis. (3) The impacts of the question and prior answers on the current answer are not equally weighted and can be learned with data. Therefore, incorporating these dependencies can potentially lead to a higher quality (i.e., stronger representation capability and human interpretability) of topic modeling and, accordingly, to the improvement of subsequent analyses.

In the following sections, we describe the details of our Bayesian-based approach, including the generative process that explicitly models the complex interdependencies among questions and answers in a generalizable and flexible way, as well as our model inference and parameter estimation.

## Our Proposed Topic Model (TM-OKC)

We begin by illustrating the intuition of our TM-OKC design. To capture the complex relations among texts in OKCs, TM-OKC explicitly models their topic interdependencies. For example, the topics of an answer are influenced by its question because users read the question before providing their answers. But different users may have their own understanding of the question and may focus on different aspects of it due to their unique background and knowledge. This suggests that the topics of answers are dependent on the question while varying among themselves. In addition, a user may also read prior answers before writing their own answer, which indicates that the topics of the current answer are likely to be affected by the topics discussed in prior answers. Meanwhile, prior answers may not have equal impacts on the topics of a later answer due to different ranks and perceived usefulness. Users may also completely ignore previous answers and provide “novel” answers. As discussed in previous sections, these structural and temporal dependencies in OKC texts are not well captured by existing topic modeling methods, giving rise to the need for a new framework.

Next, we describe the detailed generative process of the TM-OKC model. The plate graphical representation is shown in Figure 1, where each step is numbered corresponding to the elaboration below. Table 3 summarizes major notations used throughout the paper.

![](/api/attachments/TSBSG3KK/fulltext/images/c326c0e2585433516c5a2e8cac63899aa7f15565fd7159a418961f9dbc86cd30.jpg)  
Figure 1. Graphical Representation of Our Proposed TM-OKC Topic Model

<table><tr><td colspan="2">Table 3. Summary of Variables and Their Definitions</td></tr><tr><td>Variable</td><td>Definition</td></tr><tr><td> $\theta_q$ </td><td>The topic distribution (proportion) of question  $q$ </td></tr><tr><td> $\eta_q$ </td><td>Natural parameterization of the topic distribution  $\theta_q$ , where  $\theta_q = \frac{exp\{\eta_q\}}{\sum_{k=1}^{K} exp\{\eta_q^k\}}$ </td></tr><tr><td> $x_d$ </td><td>Proportions of follow-up and novel answers for the question-answer thread  $d$ </td></tr><tr><td> $y_{a_t}$ </td><td> $y_{a_t}$  equals 0 if  $a_t$  is a follow-up answer, 1 if  $a_t$  is a novel answer</td></tr><tr><td> $\theta_{a_t}$ </td><td>The topic distribution (proportion) of the  $t^{th}$  answer of question  $q$ </td></tr><tr><td> $\eta_{a_t}$ </td><td>Natural parameterization of the topic distribution  $\theta_{a_t}$ , where  $\theta_{a_t} = \frac{exp\{\eta_{a_t}\}}{\sum_{k=1}^{K} exp\{\eta_{a_t}^k\}}$ </td></tr><tr><td> $z_q$ </td><td>The topic assignment of words in question  $q$ </td></tr><tr><td> $z_{a_t}$ </td><td>The topic assignment of words in the  $t^{th}$  answer of question  $q$ </td></tr><tr><td> $\beta_q$ </td><td>The topic-word distribution of questions</td></tr><tr><td> $\beta_a$ </td><td>The topic-word distribution of answers</td></tr><tr><td> $w_q$ </td><td>The observed words in question  $q$ </td></tr><tr><td> $w_{a_t}$ </td><td>The observed words in the  $t^{th}$  answer of question  $q$ </td></tr></table>

(1) Draw the question topic-word distribution $\beta _ { q } ^ { k }$ from a Dirichlet distribution, for $k \in \{ 1 , 2 , \ldots , K \}$ , where K is the number of topics:

$$
\boldsymbol {\beta} _ {q} ^ {k} \sim \text { Dirichelet } (\boldsymbol {\alpha} _ {q}).
$$

(2) Draw the answer topic-word distribution $\beta _ { a } ^ { k }$ from a Dirichlet distribution<sup>3</sup>, for $k \in \{ 1 , 2 , \ldots , K \}$ }:

$$
\boldsymbol {\beta} _ {a} ^ {k} \sim D i r i c h e l e t (\boldsymbol {\alpha} _ {a}).
$$

(3) Draw the question-level topic distribution $\theta _ { q }$ from a logistic-normal distribution. The rationale behind this is that logistic-normal is relatively flexible in that it can model topics with correlations:

$$
\begin{array}{c} \boldsymbol {\eta} _ {q} \sim N (\boldsymbol {\mu}, \boldsymbol {\Sigma} _ {q}), \\ \boldsymbol {\theta} _ {q} = \frac {e x p \{\boldsymbol {\eta} _ {q} \}}{\sum_ {k = 1} ^ {K} e x p \{\eta_ {q} ^ {k} \}}. \end{array}
$$

(4) To model the dependencies regarding the questionanswer and the answer-answer, we perform the following steps.

(4-1) We first draw $x _ { d }$ at the document level (i.e., a whole question-answer thread) from a beta distribution:

$$
\boldsymbol {x} _ {d} \sim B e t a (\boldsymbol {\delta}),
$$

where $x _ { d }$ is a two-dimensional vector that denotes the probability of an answer being a follow-up or a novel answer. It can capture different proportions of novel answers in diverse question-answer threads.

(4-2) Suppose the question q has T answers for every answer $a _ { t } , \ t \in \{ 1 , 2 , \ldots , T \}$ . We draw $y _ { a _ { t } }$ at an answer level from a binomial distribution:

$$
y _ {a _ {t}} \sim \text { Binomial } (x _ {d}).
$$

$y _ { a _ { t } }$ equals 0 if $a _ { t }$ is a follow-up answer, 1 if $a _ { t }$ is a novel answer.

(4-3) Then, we draw the topic distribution $\pmb { \theta } _ { a _ { t } }$ for every answer as follows:

(4-3-1) If $y _ { a _ { t } } = 0 ,$ , indicating $a _ { t }$ is a follow-up answer, the topic distribution is dependent on the question and its previous answers. Note that previous answers may have different weights on the current answer. Specifically, we draw $\pmb { \theta } _ { a _ { t } }$ of a follow-up answer from a logistic-normal distribution:

$$
\begin{array}{r} \pmb {\eta} _ {a _ {t}} \sim N \left(\frac {\pmb {\eta} _ {q} + \gamma \overline {{\pmb {\eta}}} _ {a _ {t - 1}}}{1 + \gamma}, \pmb {\Sigma} _ {a _ {f}}\right), \\ \pmb {\theta} _ {a _ {t}} = \frac {e x p \{\pmb {\eta} _ {a _ {t}} \}}{\sum_ {k = 1} ^ {K} e x p \{\eta_ {a _ {t}} ^ {k} \}}, \end{array}
$$

where ?? is a non-negative parameter and $\overline { { \eta } } _ { a _ { t - 1 } }$ is the weighted sum of the impact of all previous answers on the current $t ^ { t h }$ one, characterized by the following:

$$
\begin{array}{c} \overline {{\boldsymbol {\eta}}} _ {a _ {0}} = \boldsymbol {\eta} _ {q}, \\ \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}} = \zeta_ {t - 1} ^ {t} \boldsymbol {\eta} _ {a _ {t - 1}} + \zeta_ {t - 2} ^ {t} \boldsymbol {\eta} _ {a _ {t - 2}} + \dots + \zeta_ {1} ^ {t} \boldsymbol {\eta} _ {a _ {1}}, i f t \\ \geq 2, w h e r e \sum_ {i = 1} ^ {t - 1} \zeta_ {i} ^ {t} = 1. \end{array}
$$

Note that the weight $\zeta _ { i } ^ { t }$ can have various formats $( \mathrm { e . g . }$ equally weighted, by time decay, or by the number of usefulness votes).

(4-3-2) $\mathrm { I f } y _ { a _ { t } } = 1$ , indicating $a _ { t }$ is a novel answer, the topic distribution is only dependent on the question. Specifically, we draw $\pmb { \theta } _ { a _ { t } }$ of a novel answer from a logistic-normal distribution:

$$
\begin{array}{r} \pmb {\eta} _ {a _ {t}} \sim N (\pmb {\eta} _ {q}, \pmb {\Sigma} _ {a _ {n}}), \\ \pmb {\theta} _ {a _ {t}} = \frac {e x p \{\pmb {\eta} _ {a _ {t}} \}}{\sum_ {k = 1} ^ {K} e x p \{\eta_ {a _ {t}} ^ {k} \}}. \end{array}
$$

Note that the variance-covariance matrix for novel answers (i.e., $\pmb { \Sigma } _ { { \pmb { a } } _ { n } } )$ is different from the matrix for follow-up answers $( \mathrm { i } . \mathrm { e } . , \pmb { \Sigma } _ { { \pmb { a } } _ { f } } )$ , which allows for different variations of these two types of answers.

(5) Assume the question q has $N _ { q }$ words, for every word $n _ { q } \in \{ 1 , 2 , \dots , N _ { q } \}$ :

(5-1) We first draw its topic assignment $z _ { q } ^ { n _ { q } }$ via a multinomial distribution:

$$
z _ {q} ^ {n _ {q}} \sim M u l t i n o m i a l (\pmb {\theta} _ {q})
$$

(5-2) Conditioned on the assigned topic k (suppose $z _ { q } ^ { n _ { q } } = k )$ , we draw a certain word $w _ { q } ^ { n _ { q } }$ from that topic k via:

$$
w _ {q} ^ {n _ {q}} \sim M u l t i n o m i a l (\pmb {\beta} _ {q} ^ {k})
$$

(6) For every answer $a _ { t }$ with $N _ { a _ { t } }$ words, $t \in \{ 1 , 2 , \dots , T \}$ and for every word $n _ { a _ { t } } \in \{ 1 , 2 , \dots , N _ { a _ { t } } \}$

(6-1) We first draw its topic assignment $z _ { a _ { t } } ^ { n _ { a _ { t } } }$ via a multinomial distribution:

$$
z _ {a _ {t}} ^ {n _ {a _ {t}}} \sim M u l t i n o m i a l (\pmb {\theta} _ {a _ {t}})
$$

(6-2) Conditioned on the assigned topic k (suppose $z _ { a _ { t } } ^ { n _ { a _ { t } } } = k )$ , we draw a certain word $w _ { a _ { t } } ^ { n _ { a _ { t } } }$ from that topic k via:

$$
w _ {a _ {t}} ^ {n _ {a _ {t}}} \sim M u l t i n o m i a l (\pmb {\beta} _ {a} ^ {k})
$$

The key design novelty of our approach lies in Steps 3 and 4. In Step 3, we capture the topic correlation at the question level by drawing topics from a logistic-normal distribution. In traditional topic models, topics of documents (regardless of questions or answers) are usually drawn from some predefined prior (e.g., Dirichlet), which fails to capture the inherent correlation in various topics in a given corpus. In Step 4, we explicitly model two typical document structural and temporal dependencies (i.e., question-answer and answeranswer) by creating the “relation chains” among the topic distributions of the documents. This setting not only allows us to uncover latent topics in the context of threaded discussions, but we can also model the learnable Q&A heterogeneity (e.g., differential impacts of questions and prior answers on the current answer and different topic variances between Q&A) and the explicit long-range dependencies among threaded posts. Moreover, we incorporated answer novelty into the model to make the model more realistic in the context of OKCs. As discussed in the Literature Review section, these advantages cannot be fully achieved by existing topic models aiming to model explicit Q&A relations and threaded structures (e.g., QATM, LeadLDA, and SITS). However, the explicit generative process described above adds complexity to the model inference process due to the high interdependencies among latent variables. To address this challenge, we used variational mean-field inference and coordinate ascent algorithm for model inference and parameter estimation, which we discuss next.

## Model Inference

Given a Q&A document d (represented as a bag of words from the question ${ \pmb q } ( { \pmb w } _ { { \pmb q } } )$ and its answers a $( w _ { a _ { 1 : T } } ) )$ , our objective is to infer the posterior distribution of the latent variables:

$$
\begin{array}{l} p \big (\eta_ {q}, \eta_ {a _ {1: T}}, x _ {d}, y _ {a _ {1: T}}, z _ {q}, z _ {a _ {1: T}}, \beta_ {q}, \beta_ {a} \mid w _ {q}, w _ {a _ {1: T}} \big) \\ = \frac {p \big (\eta_ {q} , \eta_ {a _ {1 : T}} , x _ {d} , y _ {a _ {1 : T}} , z _ {q} , z _ {a _ {1 : T}} , \beta_ {q} , \beta_ {a} , w _ {q} , w _ {a _ {1 : T}} \big)}{p \big (w _ {q} , w _ {a _ {1 : T}} \big)}. \end{array}\tag{1}
$$

The numerator of Equation (1) is the joint distribution and can be rewritten as follows:

$$
\begin{array}{l} p \big (\boldsymbol {\eta} _ {q}, \boldsymbol {\eta} _ {a _ {1: T}}, x _ {d}, \mathbf {y} _ {a _ {1: T}}, z _ {q}, z _ {a _ {1: T}}, \boldsymbol {\beta} _ {q}, \boldsymbol {\beta} _ {a}, w _ {q}, w _ {a _ {1: T}} \big) \\ = p \big (\boldsymbol {\eta} _ {q}; \boldsymbol {\mu}, \boldsymbol {\Sigma} _ {q} \big) \prod_ {n _ {q} = 1} ^ {N _ {q}} \big [ p \big (z _ {q} ^ {n _ {q}} | \boldsymbol {\eta} _ {q} \big) p \big (w _ {q} ^ {n _ {q}} | z _ {q} ^ {n _ {q}}, \boldsymbol {\beta} _ {q} ^ {1: K} \big) \big ] \prod_ {k = 1} ^ {K} p \big (\boldsymbol {\beta} _ {q} ^ {k}; \boldsymbol {\alpha} _ {q} \big) \\ p (x _ {d}; \delta) \prod_ {t = 1} ^ {T} \Big [ p \big (y _ {a _ {t}} | x _ {d} \big) p \left(\boldsymbol {\eta} _ {a _ {t}} \Big | \boldsymbol {\eta} _ {q}, \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}}, y _ {a _ {t}}; \boldsymbol {\Sigma} _ {a _ {f}}, \boldsymbol {\Sigma} _ {a _ {n}}, \gamma\right) \Big ] \\ \prod_ {t = 1} ^ {T} \prod_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} \Big [ p \Big (z _ {a _ {t}} ^ {n _ {a _ {t}}} \Big | \boldsymbol {\eta} _ {a _ {t}} \Big) p \Big (w _ {a _ {t}} ^ {n _ {a _ {t}}} \Big | z _ {a _ {t}} ^ {n _ {a _ {t}}}, \boldsymbol {\beta} _ {a} ^ {1: K} \Big) \Big ] \prod_ {k = 1} ^ {K} p \big (\boldsymbol {\beta} _ {a} ^ {k}; \boldsymbol {\alpha} _ {a} \big). \end{array}\tag{2}
$$

Due to the large space in the denominator, exact inference is intractable. Thus, following prior literature (Wainwright & Jordan, 2008; Blei et al., 2017), we approximated the posterior distribution using variational inference. Specifically, we derived the log-likelihood and its evidence lower bound (ELBO) using the mean-field variational inference as follows:

$$
\begin{array}{l} \log p \left(\boldsymbol {w} _ {q}, \boldsymbol {w} _ {\boldsymbol {a} _ {1: T}}; \boldsymbol {\mu}, \boldsymbol {\Sigma} _ {q}, \boldsymbol {\Sigma} _ {a _ {f}}, \boldsymbol {\Sigma} _ {a _ {n}}, \gamma , \delta , \boldsymbol {\alpha} _ {q}, \boldsymbol {\alpha} _ {a}\right) \\ \geq E _ {u} \big [ \log p (\boldsymbol {\eta} _ {q}; \boldsymbol {\mu}, \boldsymbol {\Sigma} _ {q}) \big ] + \sum_ {n _ {q} = 1} ^ {N _ {q}} E _ {u} \big [ \log p (z _ {q} ^ {n _ {q}} | \boldsymbol {\eta} _ {q}) \big ] \\ + \sum_ {n _ {q} = 1} ^ {N _ {q}} E _ {u} \big [ \log p (w _ {q} ^ {n _ {q}} | z _ {q} ^ {n _ {q}}, \boldsymbol {\beta} _ {q} ^ {\mathbf {1 : K}}) \big ] \\ + \sum_ {k = 1} ^ {K} E _ {u} \big [ \log p (\boldsymbol {\beta} _ {q} ^ {k}; \boldsymbol {\alpha} _ {q}) \big ] + E _ {u} [ \log p (\boldsymbol {x} _ {d}; \boldsymbol {\delta}) ] \\ + \sum_ {t = 1} ^ {T} E _ {u} \big [ \log p (y _ {a _ {t}} | x _ {d}) \big ] \\ + \sum_ {t = 1} ^ {T} E _ {u} \left[ \log p (\boldsymbol {\eta} _ {a _ {t}} | \boldsymbol {\eta} _ {q}, \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}}, y _ {a _ {t}}; \boldsymbol {\Sigma} _ {a _ {f}}, \boldsymbol {\Sigma} _ {a _ {n}}, \gamma) \right] \\ + \sum_ {t = 1} ^ {T} \sum_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} E _ {u} \left[ \log p (z _ {a _ {t}} ^ {n _ {a _ {t}}} | \boldsymbol {\eta} _ {a _ {t}}) \right] \\ + \sum_ {t = 1} ^ {T} \sum_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} E _ {u} \left[ \log p (w _ {a _ {t}} ^ {n _ {a _ {t}}} | z _ {a _ {t}} ^ {n _ {a _ {t}}}, \boldsymbol {\beta} _ {a} ^ {\mathbf {1 : K}}) \right] \\ + \sum_ {k = 1} ^ {K} E _ {u} \big [ \log p (\boldsymbol {\beta} _ {a} ^ {k}; \boldsymbol {\alpha} _ {a}) \big ] + H (u), \end{array}\tag{3}
$$

where the expectation is taken with respect to ??, which is the variational distribution of those latent variables, and $H ( u )$ is the entropy of ??. Specifically, ?? is characterized by:

$$
\begin{array}{r l} & u \big (\boldsymbol {\eta} _ {q}, \boldsymbol {\eta} _ {a _ {1: T}}, \boldsymbol {x} _ {d}, \boldsymbol {y} _ {a _ {1: T}}, \boldsymbol {z} _ {q}, \boldsymbol {z} _ {a _ {1: T}}, \boldsymbol {\beta} _ {q}, \boldsymbol {\beta} _ {a} \big) \\ & = \prod_ {k = 1} ^ {K} u \left(\eta_ {q} ^ {k}; \lambda_ {q} ^ {k}, \left(\sigma_ {q} ^ {k}\right) ^ {2}\right) \prod_ {t = 1} ^ {T} \prod_ {k = 1} ^ {K} u \left(\eta_ {a _ {t}} ^ {k}; \lambda_ {a _ {t}} ^ {k}, \left(\sigma_ {a _ {t}} ^ {k}\right) ^ {2}\right) \\ & u (\boldsymbol {x} _ {d}; \boldsymbol {\nu} _ {d}) \prod_ {t = 1} ^ {T} u \big (y _ {a _ {t}}; \boldsymbol {\psi} _ {a _ {t}} \big) \prod_ {n _ {q} = 1} ^ {N _ {q}} u \big (z _ {q} ^ {n _ {q}}; \boldsymbol {\phi} _ {q} ^ {n _ {q}} \big) \\ & \prod_ {t = 1} ^ {T} \prod_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} u \left(z _ {a _ {t}} ^ {n _ {a _ {t}}}; \boldsymbol {\phi} _ {a _ {t}} ^ {n _ {a _ {t}}}\right) \prod_ {k = 1} ^ {K} u \big (\boldsymbol {\beta} _ {q} ^ {k}; \boldsymbol {\tau} _ {q} ^ {k} \big) \prod_ {k = 1} ^ {K} u \big (\boldsymbol {\beta} _ {a} ^ {k}; \boldsymbol {\tau} _ {a} ^ {k} \big). \end{array}\tag{4}
$$

To optimize the ELBO specified in Equation (3), we adopted the coordinate ascent algorithm, iteratively maximizing the objective function with respect to every variational parameter. Please refer to the details provided in Appendix B.

## Parameter Estimation

Given a collection of online discussion documents (i.e., Q&A threads), we estimate the parameters by variational expectation-maximization (VEM) (Blei et al., 2003; Wainwright & Jordan, 2008; Roberts et al., 2016). The objective function of parameter estimation for VEM is the likelihood bound given by summing up the ELBO in Equation (3) over all the documents.<sup>4</sup> Thus, it becomes a likelihood function with respect to parameters ?? $\mathbf { \nabla } , \pmb { \Sigma } _ { q } , \pmb { \Sigma } _ { { \pmb { a } } _ { f } } , \pmb { \Sigma } _ { { \pmb { a } } _ { n } }$ and ??:

$$
\begin{array}{l} L \left(\boldsymbol {\mu}, \boldsymbol {\Sigma} _ {q}, \boldsymbol {\Sigma} _ {a _ {f}}, \boldsymbol {\Sigma} _ {a _ {n}}, \gamma ; \boldsymbol {w} _ {1: D, q}, \boldsymbol {w} _ {1: D, a _ {1: T}}\right) \geq \widehat {L} \\ = \sum_ {d = 1} ^ {D} \Bigl \{E _ {u _ {d}} \left[ \log p \binom{\boldsymbol {\eta} _ {d, q}, \boldsymbol {\eta} _ {d, a _ {1: T}}, \boldsymbol {x} _ {d}, \boldsymbol {y} _ {d, a _ {1: T}}}{\boldsymbol {z} _ {d, q}, \boldsymbol {z} _ {d, a _ {1: T}}, \boldsymbol {\beta} _ {q}, \boldsymbol {\beta} _ {a}, \boldsymbol {w} _ {d, q}, \boldsymbol {w} _ {d, a _ {1: T}}} \right] + H (u _ {d}) \Bigr \}. \end{array}\tag{5}
$$

Please refer to Appendix B for the details of this objective function. Based on the objective function, we took the firstorder condition to update these parameters as follows:

(1) Maximize $\widehat { L }$ with respect to ??:

$$
\frac {d \hat {L}}{d \boldsymbol {\mu}} = \sum_ {d = 1} ^ {D} \boldsymbol {\Sigma} _ {q} ^ {- 1} (\lambda_ {d, q} - \boldsymbol {\mu}) = 0 \implies \boldsymbol {\mu} = \frac {1}{D} \sum_ {d = 1} ^ {D} \lambda_ {d, q}
$$

(2) Maximize $\widehat { L }$ with respect to $\pmb { \Sigma } _ { q } ^ { - 1 }$ :

$$
\begin{array}{l} \frac {d \hat {L}}{d \boldsymbol {\Sigma} _ {q} ^ {- 1}} = \sum_ {d = 1} ^ {D} \left\{\frac {1}{2} \frac {1}{| \boldsymbol {\Sigma} _ {q} ^ {- 1} |} | \boldsymbol {\Sigma} _ {q} ^ {- 1} | \boldsymbol {\Sigma} _ {q} - \frac {1}{2} \left[ d i a g (\boldsymbol {\sigma} _ {q} ^ {d}) ^ {2} + (\lambda_ {d, q} - \boldsymbol {\mu}) (\lambda_ {d, q} - \boldsymbol {\mu}) ^ {T} \right] \right\} = 0 \\ \Rightarrow \boldsymbol {\Sigma} _ {q} = \frac {1}{D} \sum_ {d = 1} ^ {D} \left[ d i a g (\boldsymbol {\sigma} _ {d, q}) ^ {2} + (\lambda_ {d, q} - \boldsymbol {\mu}) (\lambda_ {d, q} - \boldsymbol {\mu}) ^ {T} \right] \end{array}
$$

(3) Maximize $\widehat { L }$ with respect to $\Sigma _ { a _ { f } } ^ { - 1 }$ :

$$
\begin{array} { r l } & { \frac { d \hat { L } } { d \pmb { \Sigma } _ { a f } ^ { - 1 } } = \sum _ { d = 1 } ^ { D } \left\{ \sum _ { t = 1 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } \left[ \frac { 1 } { 2 } \frac { 1 } { \left| \pmb { \Sigma } _ { a f } ^ { - 1 } \right| } \Big | \pmb { \Sigma } _ { a f } ^ { - 1 } \Big | \pmb { \Sigma } _ { a f } - \frac { 1 } { 2 } d i a g \big ( \pmb { \sigma } _ { d , a _ { t } } \big ) ^ { 2 } \right] \right. } \\ & { \qquad - \psi _ { d , a _ { 1 } } ^ { 1 } * \frac { 1 } { 2 } d i a g \big ( \pmb { \sigma } _ { d , q } \big ) ^ { 2 } - \psi _ { d , a _ { 1 } } ^ { 1 } } \\ & { \qquad * \frac { 1 } { 2 } \big ( \lambda _ { d , a _ { 1 } } - \lambda _ { d , q } \big ) \big ( \lambda _ { d , a _ { 1 } } - \lambda _ { d , q } \big ) ^ { T } } \\ & { \qquad - \sum _ { t = 2 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } * \frac { 1 } { 2 } \frac { 1 } { ( 1 + \gamma ) ^ { 2 } } d i a g \big ( \pmb { \sigma } _ { d , q } \big ) ^ { 2 } } \\ & { \qquad - \sum _ { t = 2 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } * \frac { 1 } { 2 } \sum _ { i = 1 } ^ { t - 1 } \Big ( \frac { \gamma \zeta _ { i } ^ { t } } { 1 + \gamma } \Big ) ^ { 2 } d i a g \big ( \pmb { \sigma } _ { d , a _ { i } } \big ) } \\ & { \qquad - \sum _ { t = 2 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } } \\ & { \qquad * \frac { 1 } { 2 } \Bigg ( \lambda _ { d , a _ { t } } - \frac { 1 } { 1 + \gamma } \lambda _ { d , q } } \\ & { \qquad - \sum _ { i = 1 } ^ { t - 1 } \frac { \gamma \zeta _ { i } ^ { t } } { 1 + \gamma } \lambda _ { d , a _ { i } } \Bigg ) ^ { T } \Bigg ( \lambda _ { d , a _ { t } } - \frac { 1 } { 1 + \gamma } \lambda _ { d , q } } \\ & { \qquad - \sum _ { i = 1 } ^ { t - 1 } \frac { \gamma \zeta _ { i } ^ { t } } { 1 + \gamma } \lambda _ { d , a _ { i } } ) \Bigg ) = 0 } \\ &  \Rightarrow   \pmb { \Sigma } _ { a f } = \frac { 1 } { \sum _ { d = 1 } ^ { D } \sum _ { t = 1 } ^ { T _ { d }} \psi _ { d , a _ { t } } ^ { 1 }} \sum _ { d = 1 } ^ { D } \left\{ \sum _ { t = 1 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } d i a g \big ( \pmb { \sigma } _ { d , a _ { t } } \big ) ^ { 2 } + \psi _ { d , a _ { 1 } } ^ { 1 } d i a g \big ( \pmb { \sigma } _ { d , q} \big ) ^ { 2 } + \psi _ { d , a _ { 1 } } ^ { 1 } ( \lambda _ { d , a _ { 1 } } - \lambda _ { d , q} ) ( \lambda _ { d , a _ { 1 } } - \lambda _ { d , q } ) ^ { T } + \sum _ { t = 2 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } ( \frac { 1 } { ( 1 + \gamma ) ^ { 2 } } d i a g ( \pmb { \sigma } _ { d , q} ) ^ { 2 } + \sum _ { t = 2 } ^ { T _ { d } } \psi _ { d , a _ { t } } ^ { 1 } ( i = 1 ) ( i + j ) ( i + k ) ( i + l ) ( i + m ) ( i + n ) ( i + o ) ( i + p ) ( i + q ) ( i + r ) ( i + s ) ( i + t ) ( i + u ) ( i + v ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i + w ) ( i + x ) ( i + y ) ( i + z ) ( i +w ) ( i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) ( i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i +w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i + w ) (i + x ) (i + y ) (i + z ) (i +w ) ( i - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1/ e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ -T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ {- T - 1} / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ {\prime} / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ - T - 1 / e ^ {- T - t} / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - T - t / e ^ - t / t | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
$$

(4) Maximize ??<sup>̂</sup> with respect to $\Sigma _ { a _ { n } } ^ { - 1 }$ :

$$
\begin{array}{r l} \frac {d \hat {L}}{d \boldsymbol {\Sigma} _ {a _ {n}} ^ {- 1}} = & \sum_ {d = 1} ^ {D} \left\{\sum_ {t = 1} ^ {T _ {d}} \psi_ {d, a _ {t}} ^ {2} \left[ \frac {1}{2} \frac {1}{| \boldsymbol {\Sigma} _ {a _ {n}} ^ {- 1} |} | \boldsymbol {\Sigma} _ {a _ {n}} ^ {- 1} | \boldsymbol {\Sigma} _ {a _ {n}} - \frac {1}{2} d i a g (\boldsymbol {\sigma} _ {d, a _ {t}}) ^ {2} \right. \right. \\ & \left. \left. - \frac {1}{2} d i a g (\boldsymbol {\sigma} _ {d, q}) ^ {2} \right. \right. \\ & \left. \left. - \frac {1}{2} (\lambda_ {d, a _ {t}} - \lambda_ {d, q}) (\lambda_ {d, a _ {t}} - \lambda_ {d, q}) ^ {T} \right] \right\} = 0 \end{array}
$$

$$
\begin{array}{r l} & {\Rightarrow \boldsymbol {\Sigma} _ {a _ {n}} = \frac {1}{\sum_ {d = 1} ^ {D} \sum_ {t = 1} ^ {T _ {d}} \psi_ {d , a _ {t}} ^ {2}} \sum_ {d = 1} ^ {D} \Bigg \{\sum_ {t = 1} ^ {T _ {d}} \psi_ {d, a _ {t}} ^ {2} \left[ d i a g (\pmb {\sigma} _ {d, a _ {t}}) ^ {2} \right.} \\ & {\qquad \left. + d i a g (\pmb {\sigma} _ {d, q}) ^ {2} \right.} \\ & {\qquad \left. + (\lambda_ {d, a _ {t}} - \lambda_ {d, q}) (\lambda_ {d, a _ {t}} - \lambda_ {d, q}) ^ {T} \right] \Bigg \}} \end{array}
$$

(5) Maximize ??<sup>̂</sup> with respect to ??:

$$
\begin{array}{r l} & {\frac {d \hat {L}}{d \gamma}} \\ & {\quad = \sum_ {d = 1} ^ {D} \sum_ {t = 2} ^ {T _ {d}} - \frac {1}{2} \psi_ {d, a _ {t}} ^ {1} \Bigg \{\frac {- 2}{(1 + \gamma) ^ {3}} T r \left[ d i a g (\pmb {\sigma} _ {d, q}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right]} \\ & {\quad + \sum_ {i = 1} ^ {t - 1} \frac {2 \gamma \zeta_ {i} ^ {t}}{1 + \gamma} \frac {\zeta_ {i} ^ {t}}{(1 + \gamma) ^ {2}} T r \left[ d i a g (\pmb {\sigma} _ {d, a _ {i}}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right]} \\ & {\quad + 2 \bigg (\lambda_ {d, a _ {t}} - \frac {1}{1 + \gamma} \lambda_ {d, q} - \sum_ {i = 1} ^ {t - 1} \frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma} \lambda_ {d, a _ {i}} \bigg) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \bigg (\frac {1}{(1 + \gamma) ^ {2}} \lambda_ {d, q}} \\ & {\quad - \sum_ {i = 1} ^ {t - 1} \frac {\zeta_ {i} ^ {t}}{(1 + \gamma) ^ {2}} \lambda_ {d, a _ {i}} \bigg) \Bigg \}} \\ & {\Rightarrow \gamma} \\ & {\quad = \frac {\sum_ {d = 1} ^ {D} \sum_ {t = 2} ^ {T _ {d}} \psi_ {d , a _ {t}} ^ {1} \left\{ \begin{array}{c} T r [ d i a g (\pmb {\sigma} _ {d , q}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} ] \\ + (\lambda_ {d , q} - \lambda_ {d , a _ {t}}) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} (\lambda_ {d , q} - \sum_ {i = 1} ^ {t - 1} \zeta_ {i} ^ {t} \lambda_ {d , a _ {i}}) \end{array} \right\}}{\sum_ {d = 1} ^ {D} \sum_ {t = 2} ^ {T _ {d}} \psi_ {d , a _ {t}} ^ {1} \left\{ \begin{array}{c} \sum_ {i = 1} ^ {t - 1} \zeta_ {i} ^ {t 2} T r [ d i a g (\pmb {\sigma} _ {d , a _ {i}}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} ] \\ + (\lambda_ {d, a _ {t}} - \sum_ {i = 1} ^ {t - 1} \zeta_ {i} ^ {t} \lambda_ {d, a _ {i}}) \pmb {\Sigma} _ {a _ {f}} ^ {- 1} (\lambda_ {d , q} - \sum_ {i = 1} ^ {t - 1} \zeta_ {i} ^ {t} \lambda_ {d , a _ {i}}) \end{array} \right\}}} \end{array}
$$

To sum up, based on the unique Q&A relations and threaded structures of texts in OKCs, we propose a novel Bayesianbased unsupervised topic modeling approach. To tackle the technical challenge posed by complex interdependencies, we adopted mean-field variational inference for model inference and VEM for parameter estimation.

## Online Knowledge Community Dataset

Before we evaluate and demonstrate the effectiveness of our proposed model, we first describe the datasets used in later computational experiments. We collected two datasets containing discussion threads from well-known online knowledge Q&A platforms (i.e., Stack Exchange and Quora). Like other text data, the online Q&A community has been extensively studied within the IS and business literature (Faraj et al., 2016; Goes et al., 2016; Chen et al., 2017). In Stack Exchange, discussion threads are grouped into six sites, with each having many different categories. In this study, we randomly chose one category per site to evaluate our TM-OKC model.

<table><tr><td colspan="5">Table 4. Descriptive Statistics of the Stack Exchange Dataset</td></tr><tr><td>Section (Category)</td><td># of questions</td><td># of answers</td><td># of answers per question</td><td># of words per question/answer</td></tr><tr><td>Technology (Data Science)</td><td>20740</td><td>31181</td><td>1.50</td><td>73.10</td></tr><tr><td>Culture/Recreation (English Language &amp; Usage)</td><td>109977</td><td>268356</td><td>2.44</td><td>47.45</td></tr><tr><td>Life/Arts (Cooking)</td><td>23387</td><td>58078</td><td>2.48</td><td>57.49</td></tr><tr><td>Science (Computer Science)</td><td>31156</td><td>45807</td><td>1.47</td><td>72.49</td></tr><tr><td>Professional (Writing)</td><td>10429</td><td>34116</td><td>3.27</td><td>77.61</td></tr><tr><td>Business (Project Management)</td><td>5782</td><td>17724</td><td>3.07</td><td>70.26</td></tr></table>

<table><tr><td colspan="5">Table 5. Descriptive Statistics of the Quora Dataset</td></tr><tr><td>Section (Category)</td><td># of questions</td><td># of answers</td><td># of answers per question</td><td># of words per question/answer</td></tr><tr><td>Science and Technology</td><td>1471</td><td>3144</td><td>2.14</td><td>28.82</td></tr><tr><td>Business and Marketing</td><td>1140</td><td>1981</td><td>1.74</td><td>23.50</td></tr><tr><td>Health and Life</td><td>2281</td><td>4144</td><td>1.82</td><td>20.18</td></tr></table>

These six sites (categories) are: Technology (Data Science), Culture/Recreation (English Language & Usage), Life/Arts (Cooking), Science (Computer Science), Professional (Writing), and Business (Project Management). In Quora, we chose three categories (selected from popular Quora “spaces”): Science and Technology, Business and Marketing, and Health and Life. Table 4 and Table 5 provide summary statistics of the two datasets.

To improve the data quality, we applied standard text preprocessing, such as removing punctuation, numbers, URLs, stop words, and rare words (e.g., word frequency is below 0.025% of the total number of words), as well as word stemming using NLTK.<sup>5</sup> We also filtered out questions that did not have any answers. Then, we randomly split the dataset into 70% as the training set, 10% as the validation set, and the remaining 20% as the holdout test set.

## Model Evaluation

## Statistical Model Fit

One common evaluation of a probabilistic topic model is the model fitness on a holdout test set (Blei et al., 2003). Following this, we examined whether our proposed TM-OKC model outperformed existing topic models in terms of model fitness. In this study, we evaluated the model fitness using two common metrics: perplexity and topic coherence. Perplexity is computed as a function of negative log-likelihood on a holdout test set, defined as:

$$
p e r p l e x i t y = \exp \left\{- \frac {\log p (\boldsymbol {w})}{\sum_ {d} ^ {| D _ {t e s t} |} \sum_ {v = 1} ^ {V} n u m _ {d} ^ {v}} \right\},
$$

where log ??(??) is the total log-likelihood of the holdout test set, $| D _ { t e s t } |$ is the number of documents in the test data, $n u m _ { d } ^ { v }$ is the frequency (number) of word ?? in document $d ,$ and ?? is the vocabulary size. A lower perplexity indicates higher likelihood, which suggests that the topic modeling has better generalizability. Topic coherence measures how well the topics are learned. Here we adopted the CV coherence measure (Syed & Spruit, 2017). It computes the average pairwise scores on words $w _ { 1 } , w _ { 2 } , \cdots , w _ { n }$ used to describe a topic, usually the top n words by frequency $( \boldsymbol { \mathrm { e } } . \boldsymbol { \mathrm { g } } . , \boldsymbol { \mathrm { n } } = 2 0 )$ . The CV coherence score is formally defined as:

$$
C V s c o r e = \frac {1}{\mathrm{n}} \sum_ {i = 1} ^ {n} s c o r e (w _ {i}),
$$

$$
s c o r e (w _ {i}) = c o s i n e \big (\vec {v} _ {w _ {i}}, \vec {u} \big),
$$

$$
\begin{array}{r l} & {\vec {v} _ {w _ {i}} = \{N P M I (w _ {i}, w _ {j}) ^ {\gamma} \} _ {j = 1, 2, \dots , n},} \\ & {\vec {u} = \left\{\sum_ {i = 1} ^ {n} N P M I (w _ {i}, w _ {j}) ^ {\gamma} \right\} _ {j = 1, 2, \dots , n},} \end{array}
$$

$$
N P M I (w _ {i}, w _ {j}) ^ {\gamma} = \left(\frac {l o g \frac {p (w _ {i} , w _ {j}) + \varepsilon}{p (w _ {i}) \cdot p (w _ {j})}}{- \log (p (w _ {i} , w _ {j}) + \varepsilon)}\right) ^ {\gamma},
$$

where $p ( w _ { i } )$ and $p \big ( w _ { i } , w _ { j } \big )$ are, respectively, the count of documents containing the word $w _ { i }$ and the count of documents containing both words $w _ { i }$ and ?? , divided by the total number of documents. ?? is used to account for the logarithm of zero and ?? is used to place more weight on higher NPMI (normalized pointwise mutual information) values. After calculating the ?????????????? of each topic, we used the arithmetic mean of these scores as the CV coherence measure of the model.

As TM-OKC is an unsupervised Bayesian approach that models complex interdependencies among OKC texts with Q&A relations and threaded structures, we specifically chose the following topic models as our benchmarks for evaluation.

LDA (Blei et al., 2003). LDA is one of the most widely used topic models in IS and business research. It treats every question/answer as an independent document, and thus it does not consider any dependencies among questions and answers.

NTM (Dieng et al., 2020; Churchill & Singh, 2022). NTM is a state-of-the-art topic model that combines the merits of deep language models and probabilistic topic models. It uses a variational inference framework for generative models of texts and leverages the power of deep neural networks to achieve good performance.

TRTM (Ma et al., 2015). TRTM considers different roles of a user (i.e., asker, answerer, or voter) to enhance topic modeling performance for Q&A posts in OKCs.

STM (Roberts et al., 2019; Jo et al., 2022). Apart from authorship information, STM incorporates other metadata (e.g., indicating whether a document is a question or an answer in our context, as well as the order of answers) to improve topic modeling.

SCHOLAR (Card et al., 2018; Zhao et al., 2021). SCHOLAR is a topic modeling method that combines deep language models to incorporate observed attributes.

QATM (Ji et al., 2012). QATM assumes that a question and its answers share exactly the same topic distribution when modeling the explicit relationships between questions and answers.

LeadLDA (Li et al., 2018; Magdy et al., 2020). LeadLDA explicitly models topic dependencies among posts with the first-order Markov transition, assuming each post to have one single topic. As it only allows a post to depend on one single parent post, while an answer may be correlated with both the question and previous answers, we adapted it to our context in two ways. (1) We used the question as the parent post of the current answer, denoted as LeadLDA1. (2) We used the most recent answer as the parent post of the current answer, denoted as LeadLDA2. Note that we did not compare TM-OKC with strTM because LeadLDA is the extended version of strTM.

SITS (Rossiter, 2022). Similar to LeadLDA, SITS also considers the first-order threaded structure and novelty of posts. In addition, SITS allows multiple topics in one post.

Among these methods, LDA and NTM are generic topic models, while others are designed specifically to model structural information of texts, with a particular focus on Q&A threads. As previously discussed, QATM, LeadLDA, and SITS are highly related to our method. All aim to model explicit Q&A relations and threaded structures based on pure textual data without any post-level or author-level attributes. To make our evaluation extensive, we even compared our TM-OKC model to state-of-the-art attribute-based methods (i.e., TRTM, STM, and SCHOLAR), even though they neglect the explicit structural relations among posts and attributes may not always be available due to privacy concerns and anonymity rules.

TM-OKC has three variants, reflecting the ways in which prior answers may impact the current answer.

TM-OKC (mean). All previous answers have equal weights. That is, $\begin{array} { r } { \zeta _ { i } ^ { t } = \frac { 1 } { t - 1 } , } \end{array}$ for $i = 1 , \cdots , t - 1$ . This is our main scenario. Unless specifically indicated otherwise, all results discussed hereafter are based on this TM-OKC (mean) model.

TM-OKC (decay). This assumes that the weight of earlier answers decreases as more answers are contributed. Here we used a weight decay with time. That is, $\zeta _ { i } ^ { t } =$ ${ \frac { \rho ^ { t - 1 - i } } { 1 + \rho + \cdots + \rho ^ { t - 2 } } } ,$ for $i = 1 , \cdots , t - 1$ , where ρ is a given hyper-parameter and $0 < \rho < 1 ( { \mathrm { e . g . , 0 . 8 } }$ is used in our experiments). Note that we can also specify a “shorter” range of dependency. For example, if we assume that only the most recent three answers can impact the current answer, the weights of the earlier answers can be set to zeros.

TM-OKC (weight). Each answer on Stack Exchange and Quora has a score (e.g., number of usefulness votes), which indicates the quality of an answer. Thus, we can use this score to weight previous answers. That is, $\zeta _ { i } ^ { t } =$ ${ \frac { x ^ { i } } { x ^ { 1 } + x ^ { 2 } + \cdots + x ^ { t - 1 } } } ,$ for $i = 1 , \cdots , t - 1$ , where $x ^ { i }$ is the number of usefulness votes for answer i.

Note that the perplexity scores are calculated on the holdout test set under the learned optimal models for each method. Specifically, we trained the model with the training set, chose the best model from a set of predefined numbers of topics (i.e., K=5, 10, 20, 40, and 80) based on the perplexities on a separate validation set (Griffiths & Steyvers, 2004; Bapna et al., 2019), and, finally, evaluated the model on the holdout test set. We ran the experiments 30 times and report the average performance. We report the hyper-parameter settings and computational resources in Appendix C.

Tables 6 and 7 summarize the perplexities of the test data for different categories within Stack Exchange and Quora, respectively. We make several observations. First, out of all models, TM-OKC has the lowest perplexity across categories, suggesting that TM-OKC has a stronger document modeling capability. Second, comparing NTM with LDA, we find that increasing the expressiveness of document representation (i.e., via deep neural networks in NTM) reduces model perplexity. Third, the baseline structural topic modeling approaches (i.e., TRTM, STM, SCHOLAR, QATM, LeadLDA, and SITS) generally achieve lower perplexity scores than LDA, which confirms that capturing structural information among texts indeed helps to improve topic modeling performance. Fourth, the perplexity difference among the three TM-OKC variants is insignificant, which indicates that the model is robust across different predefined weighting schemas.

To make a further comparison, we illustrate the perplexity scores of various models with varying numbers of topics. Figure 2 shows the comparison of different models in two example categories (i.e., Data Science within Stack Exchange and Business and Marketing within Quora), and the comparisons in other categories are presented in Appendix D. From Figure 2, we can see that the perplexity increases for all models after the number of topics exceeds 40 and our TM-OKC method has the lowest perplexity across settings. In addition, both QATM and LeadLDA favor fewer topics. This might be caused by their simplified model assumptions (e.g., a question and its answers sharing exactly the same topic distribution in QATM, and one single topic per post in LeadLDA).

Tables 8 and 9 summarize the topic coherence scores of different models across categories within Stack Exchange and Quora, respectively. We first observe that our TM-OKC model has the highest coherence scores in most cases compared to baseline models, suggesting that the topics learned by TM-OKC are more coherent and interpretable. Second, the coherence scores for “hard-skill” categories (e.g., Data Science and Computer Science) are relatively higher than those for “soft-skill” categories (e.g., Writing and Project Management). This is consistent with our expectation that the topics of posts in hard-skill subjects are easier to summarize using top words (e.g., probably technical words) than those in soft-skill subjects, where topics are more flexible and can be represented by different words. Third, similar to the perplexity results, coherence scores across the three variants of TM-OKC are close to each other. Finally, the coherence measure of LDA is relatively worse than it is in other structural topic modeling approaches (i.e., TRTM, STM, SCHOLAR, QATM, LeadLDA and SITS), likely arising from LDA not imposing any interdependencies between a question and its answers. It is also inferior to NTM due to the powerful representation from the deep neural networks in NTM.

The model fit in terms of both perplexity and coherence scores statistically validates the high-quality topic modeling of TM-OKC and its improvement over existing methods. However, our main value proposition is that TM-OKC can better model OKC text data to produce more accurate topic vectors for use in subsequent analyses, and we will demonstrate this value proposition in the next subsection (i.e., the Additional Evaluation section). In addition to modeling the complex interdependency of a question and its answers in the context of OKCs, TM-OKC is flexible in the settings of some important parameters (e.g., different impacts of the question and prior answers on the current answer, variance of question topic distribution, and variance of answer topic distribution). On this basis, our model yields many interesting and meaningful observations, as presented in Appendix E.

## Additional Evaluation

Based on the topic modeling applications in OKC research summarized in the Literature Review section, the practical value of topic models highly depends on two factors: (1) whether the topic vectors learned from the model can appropriately represent or summarize the semantics of texts and (2) whether the identified topics are easy to interpret. In other words, a high-quality topic model should generate human-interpretable topic vectors that represent the texts well. As the statistical measures in the Statistical Model Fit section are not direct metrics that show the representation capability and interpretability of topic models, in this section we present additional evaluation to demonstrate the superiority of our method over existing models in OKC contexts.

## Representation Capability

We demonstrate the representation capability of the topic vectors derived from our TM-OKC using a prediction task of document classification. This has been used in previous studies to evaluate the effectiveness of topic models (Zeng et al., 2019; Yang et al., 2023). The results highlight the fact that topic models can be used to represent the semantics of texts. Compared to existing topic modeling methods, our model has stronger representation capability on OKC texts. The details are presented in Appendix F.

<table><tr><td colspan="7">Table 6. Perplexity Comparison for the Stack Exchange Dataset</td></tr><tr><td>Model</td><td>Technology (Data Science)</td><td>Culture/ Recreation (English Language &amp; Usage)</td><td>Life/Arts (Cooking)</td><td>Science (Computer Science)</td><td>Professional (Writing)</td><td>Business (Project Management)</td></tr><tr><td>LDA</td><td>1152.11</td><td>2181.84</td><td>1520.59</td><td>1063.53</td><td>1726.48</td><td>1087.31</td></tr><tr><td>NTM</td><td>1021.39</td><td>2176.38</td><td>1407.79</td><td>1028.45</td><td>1639.31</td><td>1063.06</td></tr><tr><td>TRTM</td><td>1029.95</td><td>2030.30</td><td>1296.18</td><td>976.34</td><td>1727.38</td><td>998.90</td></tr><tr><td>STM</td><td>1054.08</td><td>2015.43</td><td>1271.62</td><td>975.40</td><td>1718.43</td><td>1010.79</td></tr><tr><td>SCHOLAR</td><td>951.94</td><td>1586.73</td><td>1251.94</td><td>934.26</td><td>1615.01</td><td>1037.08</td></tr><tr><td>QATM</td><td>931.21</td><td>1625.43</td><td>1297.68</td><td>958.23</td><td>1479.63</td><td>939.54</td></tr><tr><td>LeadLDA1</td><td>1256.93</td><td>1702.28</td><td>1376.98</td><td>1063.31</td><td>1512.57</td><td>956.25</td></tr><tr><td>LeadLDA2</td><td>1100.50</td><td>1707.15</td><td>1326.48</td><td>1075.64</td><td>1498.23</td><td>1064.47</td></tr><tr><td>SITS</td><td>1008.46</td><td>1635.08</td><td>1280.41</td><td>979.68</td><td>1482.28</td><td>934.51</td></tr><tr><td>TM-OKC (mean)</td><td>863.44***</td><td>1591.63</td><td>1220.97</td><td>891.59</td><td>1400.93</td><td>901.03</td></tr><tr><td>TM-OKC (decay)</td><td>863.93</td><td>1582.44</td><td>1221.01</td><td>891.30***</td><td>1394.29</td><td>899.39***</td></tr><tr><td>TM-OKC (weight)</td><td>867.69</td><td>1591.73</td><td>1218.70***</td><td>892.54</td><td>1390.96***</td><td>900.59</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline under a one-tailed t-test. \*\* $p < 0 . 0 1 _ { \cdot }$ , \*\*\* p < 0.001. The best perplexity is in bold while the second best is underlined.

<table><tr><td colspan="4">Table 7. Perplexity Comparison for the Quora Dataset</td></tr><tr><td>Model</td><td>Science and Technology</td><td>Business and Marketing</td><td>Health and Life</td></tr><tr><td>LDA</td><td>1579.54</td><td>1698.37</td><td>1357.71</td></tr><tr><td>NTM</td><td>1204.54</td><td>1368.05</td><td>1083.70</td></tr><tr><td>TRTM</td><td>1131.22</td><td>1310.21</td><td>1104.22</td></tr><tr><td>STM</td><td>1117.93</td><td>1301.27</td><td>1109.51</td></tr><tr><td>SCHOLAR</td><td>1192.71</td><td>1321.77</td><td>1087.89</td></tr><tr><td>QATM</td><td>1033.00</td><td>1243.23</td><td>1065.07</td></tr><tr><td>LeadLDA1</td><td>1399.21</td><td>1227.56</td><td>1088.73</td></tr><tr><td>LeadLDA2</td><td>1350.26</td><td>1242.85</td><td>1132.91</td></tr><tr><td>SITS</td><td>1313.06</td><td>1264.70</td><td>1058.69</td></tr><tr><td>TM-OKC (mean)</td><td>1014.30***</td><td>1202.66***</td><td>1042.97</td></tr><tr><td>TM-OKC (decay)</td><td>1015.86</td><td>1212.19</td><td>1040.38</td></tr><tr><td>TM-OKC (weight)</td><td>1018.13</td><td>1215.98</td><td>1032.61***</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline under a one-tailed t-test. \*\*\* $p < 0 . 0 0 1$ . The best perplexity is in bold while the second best is underlined.

![](/api/attachments/TSBSG3KK/fulltext/images/3b2db058253ffec8f928d96b3a308f6361b2fda686cfdebb9c7b398a0419a337.jpg)  
(a) Data Science in Stack Exchange

![](/api/attachments/TSBSG3KK/fulltext/images/c055d2677e0a4e354ace1b7704593782589af57bf7a711effab4c00f2f558dda.jpg)  
(b) Business and Marketing in Quora  
Figure 2. Perplexity Under Different Numbers of Topics for Two Example Categories

<table><tr><td colspan="7">Table 8. Coherence Comparison for the Stack Exchange Dataset</td></tr><tr><td>Model</td><td>Technology (Data Science)</td><td>Culture/ Recreation (English Language &amp; Usage)</td><td>Life/Arts (Cooking)</td><td>Science (Computer Science)</td><td>Professional (Writing)</td><td>Business (Project Management)</td></tr><tr><td>LDA</td><td>0.51</td><td>0.42</td><td>0.47</td><td>0.47</td><td>0.37</td><td>0.37</td></tr><tr><td>NTM</td><td>0.53</td><td>0.43</td><td>0.47</td><td>0.48</td><td>0.37</td><td>0.39</td></tr><tr><td>TRTM</td><td>0.51</td><td>0.42</td><td>0.46</td><td>0.48</td><td>0.37</td><td>0.36</td></tr><tr><td>STM</td><td>0.53</td><td>0.41</td><td>0.48</td><td>0.49</td><td>0.39</td><td>0.37</td></tr><tr><td>SCHOLAR</td><td>0.53</td><td>0.43</td><td>0.48</td><td>0.49</td><td>0.37</td><td>0.37</td></tr><tr><td>QATM</td><td>0.52</td><td>0.42</td><td>0.48</td><td>0.48</td><td>0.37</td><td>0.42</td></tr><tr><td>LeadLDA1</td><td>0.50</td><td>0.40</td><td>0.47</td><td>0.47</td><td>0.35</td><td>0.36</td></tr><tr><td>LeadLDA2</td><td>0.51</td><td>0.40</td><td>0.46</td><td>0.48</td><td>0.36</td><td>0.37</td></tr><tr><td>SITS</td><td>0.52</td><td>0.41</td><td>0.47</td><td>0.48</td><td>0.38</td><td>0.39</td></tr><tr><td>TM-OKC (mean)</td><td>0.53</td><td> $0.45^*$ </td><td> $0.50^*$ </td><td> $0.51^{**}$ </td><td>0.39</td><td>0.42</td></tr><tr><td>TM-OKC (decay)</td><td>0.53</td><td>0.43</td><td> $0.50^*$ </td><td> $0.51^{**}$ </td><td>0.38</td><td>0.41</td></tr><tr><td>TM-OKC (weight)</td><td> $0.56^{***}$ </td><td>0.44</td><td> $0.50^*$ </td><td> $0.51^{**}$ </td><td>0.38</td><td>0.41</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline under a one-tailed t-test. \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001. The best coherence is in bold.

<table><tr><td colspan="4">Table 9. Coherence Comparison for the Quora Dataset</td></tr><tr><td>Model</td><td>Science and Technology</td><td>Business and Marketing</td><td>Health and Life</td></tr><tr><td>LDA</td><td>0.40</td><td>0.39</td><td>0.41</td></tr><tr><td>NTM</td><td>0.46</td><td>0.41</td><td>0.42</td></tr><tr><td>TRTM</td><td>0.42</td><td>0.42</td><td>0.42</td></tr><tr><td>STM</td><td>0.43</td><td>0.43</td><td>0.43</td></tr><tr><td>SCHOLAR</td><td>0.45</td><td>0.40</td><td>0.42</td></tr><tr><td>QATM</td><td>0.43</td><td>0.44</td><td>0.42</td></tr><tr><td>LeadLDA1</td><td>0.46</td><td>0.38</td><td>0.44</td></tr><tr><td>LeadLDA2</td><td>0.41</td><td>0.39</td><td>0.42</td></tr><tr><td>SITS</td><td>0.43</td><td>0.41</td><td>0.43</td></tr><tr><td>TM-OKC (mean)</td><td> $\mathbf{0.48}^{**}$ </td><td>0.45</td><td> $\mathbf{0.47}^{***}$ </td></tr><tr><td>TM-OKC (decay)</td><td>0.47</td><td> $\mathbf{0.46}^{**}$ </td><td>0.46</td></tr><tr><td>TM-OKC (weight)</td><td> $\mathbf{0.48}^{**}$ </td><td>0.45</td><td>0.46</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline under a one-tailed t-test. \*\* p < 0.01, \*\*\* p < 0.001. The best coherence is in bold.

## Interpretability

To evaluate the interpretability of our TM-OKC, we first examine the face validity, where we show the top 10 words for several topics of our model and the best baseline model (please refer to Appendix G). Then we follow previous research to explore the interpretability in a more rigorous way by conducting word intrusion and topic intrusion through lab studies (Chang et al., 2009; Bao & Datta, 2014; Palese & Piccoli, 2020). The results show that our model achieves significantly better human evaluation performance than other topic models. The details are presented in Appendix F.

## Practical Value of TM-OKC

Our proposed TM-OKC model can provide an interpretable representation of UGC (i.e., posts with Q&A relations and threaded structures) on OKC platforms. It also shows better statistical model fit, representation capability and interpretability by evaluations in the Model Evaluation section. In addition, our proposed method can be incorporated into downstream tasks such as user profiling, friendship suggestion, and trending topic detection, as illustrated in Figure 3.

![](/api/attachments/TSBSG3KK/fulltext/images/a5dd80a5d870839f3ccd340e5b7751b90e18ce38554222c0a7c814be3119297e.jpg)  
Figure 3. Evaluation and Practical Values of TM-OKC

For this section, we chose the downstream task of user profiling to demonstrate the practical value and relative merit of our TM-OKC compared to existing methods. <sup>6</sup> User profiling, an important task on the UGC platform, allows a platform or firm to identify topics of interest for each user based on their previously generated content. Mathematically, we profiled users by projecting each user’s generated content (i.e., questions and answers they provided on the platform) into a vector representation. It is practically valuable in IS and marketing because platforms or firms can leverage user profiles (i.e., user-level representations) for various purposes, such as content personalization, user segmentation, and ad recommendation (Atahan & Sarkar, 2011; Lakiotaki et al., 2009; Timoshenko & Hauser, 2019; Trusov et al., 2016; Dhillon & Aral, 2021). All these applications are consistent with the objective of the OKC—better information dissemination and community formation.

Baselines: Existing methods to extract text representations for user profiling mainly fall into three categories: (1) traditional approaches used in information retrieval, such as the term frequency-inverse document frequency (TF-IDF) method (Manning et al., 2008); (2) Bayesian topic modeling methods (Tang et al., 2010; Lee et al., 2016; Liang, 2018; Geva et al., 2019); (3) deep learning-based methods, including pretrained deep language models, topic modeling combined with deep language models, and other state-of-the-art deep learning methods. Specifically, we chose the following methods in each category as benchmarks.

(1) Traditional approaches used in information retrieval. We employed TF-IDF with the top W (W = 100, 500, or 1,000) words in the corpus to represent each document.

(2) Bayesian topic modeling methods. We used all benchmark Bayesian topic models listed in the Model Evaluation section, including LDA (Blei et al., 2003), TRTM (Ma et al., 2015), STM (Roberts et al., 2019; Jo et al., 2022), QATM (Ji et al., 2012), LeadLDA (Li et al., 2018; Magdy et al., 2020), and SITS (Rossiter, 2022).

(3) Deep learning-based methods. We chose pretrained BERT (Devlin et al., 2019; Liu et al., 2023), NTM (Dieng et al., 2020; Churchill & Singh, 2022), SCHOLAR (Card et al., 2018; Zhao et al., 2021) and neural matrix factorization (NMF) (Dhillon & Aral, 2021).

Evaluation of user profiling: We evaluated the user profiling performance of our method and existing methods by assessing whether the constructed user profiles through different methods can help identify users’ interested content. Specifically, consistent with prior literature (Szpektor et al., 2013; Dhillon & Aral, 2021), we adopted the following process:

(1) Constructing the test set: For each user in the Q&A dataset,<sup>7</sup> we held out the last question answered by the user as the ground truth for that user’s interested content. We assumed that the user was likely to be interested in that question if they answered the question. Then we put these questions together to form the test set and the remaining Q&A posts served as the training set.

(2) Building user profiles: We first trained the model (e.g., our TM-OKC) and obtained the text representation (i.e., a vector) for each post in both training and test sets. Then we aggregated the text representation of a focal user’s posts in the training set as the profile of that user.

(3) Performing a similarity search: Following the strategy used in prior studies (Elkahky et al., 2015; He et al., 2017), for each user, we first randomly sampled 99 questions in the test set that were not answered by the user. We then combined these questions with the true holdout question that was answered by that user to form a 100-question pool.<sup>8</sup> Then we used cosine similarity to find the top K (K = 5, 10, or 20) similar questions in this 100-question pool to the user’s profile—i.e., the user’s representation vector obtained in (2). If one of the top K questions was truly answered by that user, we considered it a hit. We then aggregated hits across users to construct the hit rate to measure the performance of the user profiling task.<sup>9</sup>

Table 10 presents the user profiling performance comparison of different methods under a moderate data size (i.e., number of questions is 8,000), which demonstrates the superiority of our TM-OKC compared with the state-of-the-art baseline methods.<sup>10</sup> In general, we can see that when the data size is moderate, deep learningbased methods perform worse than Bayesian topic modeling methods. We also notice that LeadLDA performs much worse than other topic models, which may be due to its limitation of only allowing each post to have a single topic, making it of limited use for user profiling.

Furthermore, our model has one particular merit—it does not require large data to obtain reasonably good performance when compared to deep learning-based methods. To investigate this, we conducted experiments on the user profiling task under different data sizes (i.e., 1,000, 2,000, 4,000, 8,000, 16,000, 32,000, and 64,000 Q&A threads).

Table 10. User Profiling Performance Comparison of Different Methods Under a Moderate Data Size (Number of Q&A Threads is 8,000)

<table><tr><td rowspan="2" colspan="2"></td><td colspan="3">Hit rate for top K</td></tr><tr><td>K=5</td><td>K=10</td><td>K=20</td></tr><tr><td rowspan="3">Basic text feature extraction methods</td><td>TF-IDF features (top 100 words)</td><td>5.1%</td><td>11.7%</td><td>21.4%</td></tr><tr><td>TF-IDF features (top 500 words)</td><td>5.3%</td><td>11.5%</td><td>21.2%</td></tr><tr><td>TF-IDF features (top 1000 words)</td><td>5.5%</td><td>11.8%</td><td>21.6%</td></tr><tr><td rowspan="7">Bayesian topic modeling methods</td><td>LDA</td><td>20.9%</td><td>33.9%</td><td>49.7%</td></tr><tr><td>TRTM</td><td>26.6%</td><td>43.7%</td><td>59.3%</td></tr><tr><td>STM</td><td>26.5%</td><td>44.1%</td><td>59.4%</td></tr><tr><td>QATM</td><td>26.5%</td><td>45.2%</td><td>60.1%</td></tr><tr><td>LeadLDA1</td><td>6.2%</td><td>11.7%</td><td>22.1%</td></tr><tr><td>LeadLDA2</td><td>6.5%</td><td>12.8%</td><td>24.1%</td></tr><tr><td>SITS</td><td>26.0%</td><td>41.4%</td><td>58.3%</td></tr><tr><td>Pretrained deep language models</td><td>Pretrained BERT</td><td>8.6%</td><td>14.9%</td><td>26.6%</td></tr><tr><td rowspan="2">Topic modeling combined with deep language models</td><td>NTM</td><td>18.2%</td><td>32.1%</td><td>42.8%</td></tr><tr><td>SCHOLAR</td><td>19.4%</td><td>33.6%</td><td>50.6%</td></tr><tr><td>Neural matrix factorization</td><td>NMF</td><td>19.0%</td><td>32.1%</td><td>46.0%</td></tr><tr><td>Our method</td><td>TM-OKC</td><td>32.6%***</td><td>49.1%**</td><td>64.8%**</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline method under a one-tailed t-test. \*\* p < 0.05, \*\*\* p < 0.01.

<table><tr><td colspan="9">Table 11. User Profiling Performance Comparison of Different Methods Under Different Data Sizes for K=10 (i.e., Top 10 Hit Rate)</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="7">Data size N (number of Q&amp;A threads)</td></tr><tr><td>1,000</td><td>2,000</td><td>4,000</td><td>8,000</td><td>16,000</td><td>32,000</td><td>64,000</td></tr><tr><td rowspan="3">Basic text feature extraction methods</td><td>TF-IDF features (top 100 words)</td><td>10.5%</td><td>10.7%</td><td>11.1%</td><td>11.7%</td><td>11.1%</td><td>12.4%</td><td>12.2%</td></tr><tr><td>TF-IDF features (top 500 words)</td><td>10.3%</td><td>10.6%</td><td>11.5%</td><td>11.5%</td><td>11.8%</td><td>11.3%</td><td>11.5%</td></tr><tr><td>TF-IDF features (top 1000 words)</td><td>10.6%</td><td>10.4%</td><td>11.9%</td><td>11.8%</td><td>11.2%</td><td>11.2%</td><td>11.7%</td></tr><tr><td rowspan="7">Bayesian topic modeling methods</td><td>LDA</td><td>26.9%</td><td>29.6%</td><td>31.5%</td><td>33.9%</td><td>34.8%</td><td>35.9%</td><td>36.4%</td></tr><tr><td>TRTM</td><td>37.7%</td><td>39.8%</td><td>40.5%</td><td>43.7%</td><td>44.3%</td><td>45.1%</td><td>45.1%</td></tr><tr><td>STM</td><td>36.4%</td><td>40.9%</td><td>42.0%</td><td>44.1%</td><td>44.9%</td><td>45.2%</td><td>45.6%</td></tr><tr><td>QATM</td><td>30.0%</td><td>35.0%</td><td>40.0%</td><td>45.2%</td><td>45.7%</td><td>45.3%</td><td>46.0%</td></tr><tr><td>LeadLDA1</td><td>10.2%</td><td>10.1%</td><td>10.7%</td><td>11.7%</td><td>12.2%</td><td>14.8%</td><td>15.2%</td></tr><tr><td>LeadLDA2</td><td>10.5%</td><td>10.6%</td><td>10.6%</td><td>12.8%</td><td>12.1%</td><td>15.4%</td><td>15.9%</td></tr><tr><td>SITS</td><td>34.5%</td><td>40.1%</td><td>39.8%</td><td>41.4%</td><td>43.9%</td><td>44.7%</td><td>45.8%</td></tr><tr><td>Pretrained deep language models</td><td>Pretrained BERT</td><td>13.3%</td><td>14.1%</td><td>13.4%</td><td>14.9%</td><td>14.6%</td><td>13.6%</td><td>14.1%</td></tr><tr><td rowspan="2">Topic modeling combined with deep language models</td><td>NTM</td><td>15.5%</td><td>23.6%</td><td>27.0%</td><td>32.1%</td><td>41.7%</td><td>47.2%</td><td>50.6%</td></tr><tr><td>SCHOLAR</td><td>20.4%</td><td>22.5%</td><td>28.8%</td><td>33.6%</td><td>42.6%</td><td>47.8%</td><td>51.4%</td></tr><tr><td>Neural matrix factorization</td><td>NMF</td><td>20.8%</td><td>23.7%</td><td>27.8%</td><td>32.1%</td><td>40.8%</td><td>46.7%</td><td>49.8%</td></tr><tr><td>Our method</td><td>TM-OKC</td><td>46.8%***</td><td>47.7%***</td><td>48.0%***</td><td>49.1%**</td><td>49.7%**</td><td>50.1%*</td><td>51.3%</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline method under a one-tailed t-test. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.

Table 11 presents the user profiling performance comparison of different methods under different data sizes in terms of the top-10 hit rate. Our TM-OKC performs significantly better than other Bayesian topic modeling methods. One plausible reason is that we explicitly modeled the complex structural relationships among the texts in OKCs. Comparing our model to deep learning-based methods (i.e., NTM, SCHOLAR, and NMF), we found a significant discrepancy in performance when the data size is small. As data size increases, the performance difference between our method and deep learning methods shrinks. When the data becomes large (e.g., 64,000 Q&A threads), TM-OKC performs comparably to deep learning-based methods and the difference is not significant. Our method is less sensitive to the data size compared to deep learning-based methods because such methods usually involve lots of parameters that need to be learned and are known to have stability issues (Hoyle et al., 2022).<sup>11</sup>

## Discussion and Conclusion

To extract topics from OKC texts with Q&A relations and threaded structures, we developed an unsupervised topic model that explicitly models the structural and temporal dependencies. Specifically, we propose a unified Bayesian framework in which interdependencies among texts, and in particular the impact of the question and prior answers on the current answer, are modeled. Our model’s ability to identify topics from texts in OKCs could be useful in a myriad of information systems settings in which documents arriving sequentially could be considered to belong to a thread. Due to its superior statistical model fit, representation capability, and human interpretability, our model has significant implications for obtaining superior results when combined with subsequent analyses.

We also highlight that our proposed TM-OKC is a general Bayesian framework for modeling the structural and temporal dependencies among texts. The interdependencies among documents can vary in different contexts and are adjustable in the TM-OKC. We list three common scenarios below.

(1) The relationship among answers can be removed by manually setting ?? = 0. This can be applied in some contexts where the responses (i.e., “answers” in our framework) are provided independently and are only affected by the solicited post (i.e., “question” in our framework), such as in open-ended surveys with multiple independent responses to one question (Shriver et al., 2013).

(2) The current document can only depend on a particular set of previous documents, which means that some of the weights ??<sup>??</sup> (i.e., the impact of the i<sup>th</sup> document on the t<sup>th</sup> document) can be manually labeled as zero. For example, in a social network setting, it is possible that users’ responses may be influenced by their friends but not by strangers without any connections (i.e., responses may not be visible to non-friends). The weights may also be related to recency to capture the continuous time intervals among posts or related to user reputation to capture users’ differential impacts.

(3) The Q&A relations and threaded structures among texts may be more complex, e.g., answers to a given question can be split into several distinct threads and answers may receive specific comments. In these cases, our model can be extended to incorporate more than one answer thread (by adding more answer threads related to the question) or more hierarchies (by adding corresponding commentlevel variables related to an answer).

This study offers implications for several stakeholders. As we demonstrate in the previous section, OKC platforms can leverage our approach to user profiling (Weng et al., 2010; Geva et al., 2019), thus increasing the accuracy of personalized content, friendship suggestion, or ad recommendation (Liu et al., 2012; Yin et al., 2022). They can also adopt our approach to better summarize UGC to reduce information overload and decrease users’ information searching costs (Jones et al., 2004; Wang et al., 2011). Moreover, our method can be used for event tracking by detecting trending topics (Lin et al., 2010; Zhong & Schweidel, 2020; Hu, 2021), which can inform the platform on how to create more appropriate policies and strategies in response to certain events.

For researchers, given the popularity and prevalence of OKCs, examining the information value of questions and answers on OKCs is a growing trend in IS and other business disciplines.

For such inquiries, topic modeling is a useful tool to summarize texts into interpretable topics and representative topic vectors, which can be used as independent variables, as dependent variables, as control variables, or to derive new variables for subsequent analyses (Singh et al., 2014; Yue et al., 2019; Kokkodis et al., 2020; Kumar et al., 2022). Furthermore, topic models can also be useful in generating features for different machine learning and natural language processing (NLP) tasks (Churchill & Singh, 2022). Our proposed topic model, TM-OKC, which is specifically designed for OKC-like text data, explicitly models the document structures and better captures the underlying topics in UGC in such venues, enabling researchers to better test and generate theories or develop methods using variables of interest derived from the model.

Our proposed TM-OKC can also be generalized to other UGC formats that have similar Q&A relations and threaded structures to those in OKCs. For example, on social media platforms such as Facebook, firms post content and users comment on these posts at different times. The documents under one post (including the original post and its associated comments) are related in terms of their topics. Moreover, firms can reply to the user’s previous comments, indicating that temporal dependency also applies. Similarly, news outlets (e.g., The New York Times) also have a mechanism to allow users to provide feedback and opinions. A dialogue between two or more parties would also be expected to exhibit interdependencies. We believe the proposed topic model can be extended and applied to research questions that go beyond OKCs.

This study has some limitations that provide opportunities for future research. First, we assume that the question-level topic distribution is drawn from a logistic-normal distribution. Although this assumption provides good performance, as demonstrated by both quantitative and qualitative evaluations as well as the practical utilities shown by subsequent tasks, it may still diverge substantially from the underlying true distribution, which we do not know. To address this issue, researchers could employ distribution learning-based approaches, such as flow-based methods (Huang et al., 2018b), to first approximate the true underlying distribution. Second, TM-OKC is currently unsupervised. Developing supervised topic modeling frameworks by incorporating document labels could improve model performance with regard to topic identification, which has been demonstrated by some prior studies. For example, Blei and McAuliffe (2007) and Chong et al. (2009) proposed supervised LDA (sLDA) by incorporating into LDA a response variable associated with each document. Yang et al. (2023) developed a supervised Bayesian deep topic model by incorporating the review rating, which helps the model learn more sentimental, valanceoriented topics.

## Acknowledgments

The authors are grateful for the constructive comments and suggestions provided by the senior editor, the associate editor, and the reviewers during the entire review process. The authors also thank the seminar participants at the Ohio State University, University of Virginia, University of Florida, University of Rochester, Chinese University of Hong Kong, and Shanghai Jiao Tong University for their helpful feedback.

## References

Adhikari, A., Ram, A., Tang, R., & Lin, J. (2019). Rethinking complex neural network architectures for document classification. In Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (pp. 4046-4051). https://doi.org/10.18653/v1/N19- 1408

Atahan, P., & Sarkar, S. (2011). Accelerated learning of user profiles. Management Science, 57(2), 215-239. https://doi.org/10.1287/ mnsc.1100.1266

AlKhamissi, B., Li, M., Celikyilmaz, A., Diab, M., & Ghazvininejad, M. (2022). A review on language models as knowledge bases. arXiv. https://doi.org/10.48550/arXiv.2204.06031

Bachura, E., Valecha, R., Chen, R., & Rao, H. R. (2022). The OPM data breach: An investigation of shared emotional reactions on Twitter. MIS Quarterly, 46(2), 881-910. https://doi.org/ 10.25300/MISQ/2022/15596

Bao, Y., & Datta, A. (2014). Simultaneously discovering and quantifying risk types from textual risk disclosures. Management Science, 60(6), 1371-1391. https://doi.org/10.1287/mnsc.2014. 1930

Bapna, S., Benner, M., & Qiu, L. (2019). Nurturing online communities: An empirical investigation. MIS Quarterly, 43(2), 425-452. https://doi.org/10.25300/MISQ/2019/14530

Bellstam, G., Bhagat, S., & Cookson, J. A. (2021). A text-based analysis of corporate innovation. Management Science, 67(7), 4004-4031. https://doi.org/10.1287/mnsc.2020.3682

Blei, D. M. (2012). Probabilistic topic models. Communications of the ACM, 55(4), 77-84. https://doi.org/10.1145/2133806.2133826

Blei, D. M., Kucukelbir, A., & McAuliffe, J. D. (2017). Variational inference: A review for statisticians. Journal of the American Statistical Association, 112(518), 859-877. https://doi.org/10.1080/01621459.2017.1285773

Blei, D. M., & Lafferty, J. D. (2005). Correlated topic models. In Proceedings of the International Conference on Neural Information Processing Systems (pp. 147-154). https://dl.acm.org/doi/abs/10.5555/2976248.2976267

Blei, D. M., & Lafferty, J. D. (2007). A correlated topic models of science. Annals of Applied Statistics, 1, 17-35. https://doi.org/ 10.1214/07-AOAS114

Blei, D. M., & McAuliffe, J. D. (2007). Supervised topic models. In Proceedings of the International Conference on Neural Information Processing Systems. https://dl.acm.org/doi/10.5555/2981562. 2981578

Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993-1022. https://dl.acm.org/doi/10.5555/944919.944937

Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J. D., Dhariwal, P., ... Amodei, D. (2020). Language models are few-shot learners. In Proceedings of the 34th International Conference on Neural Information Processing Systems (pp. 1877-1901). https://dl.acm.org/doi/abs/10.5555/3495724.3495883

Byrd, R. H., Lu, P., Nocedal, J., & Zhu, C. (1995). A limited memory algorithm for bound constrained optimization. SIAM Journal on Scientific Computing, 16(5), 1190-1208. https://doi.org/10.1137/ 0916069

Card, D., Tan, C., & Smith, N. A. (2018). Neural models for documents with metadata. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (pp. 2031-2040). https://doi.org/10.18653/v1/P18-1189

Chang, J., Gerrish, S., Wang, C., Boyd-Graber, J., & Blei, D. M. (2009). Reading tea leaves: How humans interpret topic models. In Proceedings of the 22nd International Conference on Neural Information Processing Systems (pp. 288-296) https://dl.acm.org/ doi/10.5555/2984093.2984126

Chen, C., & Ren, J. (2017). Forum latent Dirichlet allocation for user interest discovery. Knowledge-Based Systems, 126, 1-7. https://doi.org/10.1016/j.knosys.2017.04.006

Chen, W., Wei, X., & Zhu, K. (2017). Engaging voluntary contributions in online communities: A hidden Markov model. MIS Quarterly, 42(1), 83-100. https://doi.org/10.25300/ MISQ/2018/14196

Chong, W., Blei, D. M., & Li, F.-F. (2009). Simultaneous image classification and annotation. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (pp. 1903-1910). https://doi.org/10.1109/CVPR.2009.5206800

Churchill, R., & Singh, L. (2022). The evolution of topic modeling. ACM Computing Surveys, 54(10s), 1-35. https://doi.org/10.1145/ 3507900

Costa, G., & Ortale, R. (2020). Integrating overlapping community discovery and role analysis: Bayesian probabilistic generative modeling and mean-field variational inference. Engineering Applications of Artificial Intelligence, 89, Article 103437. https://doi.org/10.1016/j.engappai.2019.103437

Devlin, J, Chang, M. W., Lee, K., & Toutanova K. (2019). BERT: Pretraining of deep bidirectional transformers for language understanding. In Proceedings of the Conference of the North American Chapter of the Association for Computational Linguistics: Human Language. https://doi.org/10.18653/v1/N19- 1423

Dhillon, P. S., & Aral, S. (2021). Modeling dynamic user interests: A neural matrix factorization approach. Marketing Science, 40(6), 1059-1080. https://doi.org/10.1287/mksc.2021.1293

Dieng, A. B., Ruiz, F.J., & Blei, D. M. (2020). Topic modeling in embedding spaces. Transactions of the Association for Computational Linguistics, 8, 439-453. https://doi.org/10.1162/ tacl\_a\_00325

Elkahky, A. M., Song, Y., & He, X. (2015). A multi-view deep learning approach for cross domain user modeling in recommendation systems. In Proceedings of the 24th International Conference on World Wide Web (pp. 278-288). https://doi.org/10.1145/2736277. 2741667

Faraj, S., von Krogh, G., Monteiro, E., & Lakhani, K. R. (2016). Special section introduction—Online community as space for knowledge flows. Information Systems Research, 27(4), 668-684. https://doi.org/10.1287/isre.2016.0682

Geva, H., Oestreicher-Singer, G., & Saar-Tsechansky, M. (2019). Using retweets when shaping our online persona: Topic modeling approach. MIS Quarterly, 43(2), 501-524. https://doi.org/ 10.25300/MISQ/2019/14346

Ghose, A., Ipeirotis, P. G., & Li, B. (2019). Modeling consumer footprints on search engines: An interplay with social media. Management Science, 65(3), 1363-1385. https://doi.org/10.1287/ mnsc.2017.2991

Goes, P. B., Guo, C., & Lin, M. (2016). Do incentive hierarchies induce user effort? Evidence from an online knowledge exchange. Information Systems Research, 27(3), 497-516. https://doi.org/ 10.1287/isre.2016.0635

Gour, A., Aggarwal, S., & Kumar, S. (2022). Lending ears to unheard voices: An empirical analysis of user‐generated content on social media. Production and Operations Management, 31(6), 2457- 2476. https://doi.org/10.1111/poms.13732

Griffiths, T. L., & Steyvers, M. (2004). Finding scientific topics. In Proceedings of the National Academy of Sciences, 101(suppl\_1), 5228-5235. https://doi.org/10.1073/pnas.0307752101

Guo, X., Wei, Q., Chen, G., Zhang, J., & Qiao, D. (2017). Extracting representative information on intra-organizational blogging platforms. MIS Quarterly, 41(4), 1105-1128. https://doi.org/ 10.25300/MISQ/2017/41.4.05

He, R., Zhang, X., Jin, D., Wang, L., Dang, J., & Li, X. (2018). Interaction-aware topic model for microblog conversations through network embedding and user attention. In Proceedings of the 27th International Conference on Computational Linguistics (pp. 1398-1409).

He, X., Liao, L., Zhang, H., Nie, L., Hu, X., & Chua, T. S. (2017). Neural collaborative filtering. In Proceedings of the 26th International Conference on World Wide Web (pp. 173-182). https://doi.org/10.1145/3038912.3052569

Hong, L., & Davison, B. D. (2010). Empirical study of topic modeling in Twitter. In Proceedings of the 1st Workshop on Social Media Analytics, pp. 80-88. https://doi.org/10.1145/1964858.1964870

Hoyle, A., Goel, P., Sarkar, R., & Resnik, P. (2022). Are neural topic models broken? Findings of the Association for Computational Linguistics: EMNLP (pp. 5321-5344). https://doi.org/10.18653/v1 2022.findings-emnlp.390

Hu, Y. (2021). Characterizing social TV activity around televised events: A joint topic model approach. INFORMS Journal on Computing, 33(4), 1320-1338. https://doi.org/10.1287/ijoc.2020.1038

Huang, A. H., Lehavy, R., Zang, A. Y., & Zheng, R. (2018a). Analyst information discovery and interpretation roles: A topic modeling approach. Management Science, 64(6), 2833-2855. https://doi.org/ 10.1287/mnsc.2017.2751

Huang, C. W., Krueger, D., Lacoste, A., & Courville, A. (2018b). Neural autoregressive flows. In Proceedings of the International Conference on Machine Learning (pp. 2078-2087).

Hwang, E. H., Singh, P. V., & Argote, L. (2015). Knowledge sharing in online communities: Learning to cross geographic and hierarchical boundaries. Organization Science, 26(6), 1593-1611. https://doi.org/10.1287/orsc.2015.1009

Hwang, E. H., Singh, P. V., & Argote, L. (2019). Jack of all, master of some: Information network and innovation in crowdsourcing communities. Information Systems Research, 30(2), 389-410. https://doi.org/10.1287/isre.2018.0804

Ji, Z., Xu, F., Wang, B., & He, B. (2012). Question-answer topic model for question retrieval in community question answering. In Proceedings of the 21st ACM International Conference on

Information and Knowledge Management (pp. 2471-2474). https://doi.org/10.1145/2396761.2398669

Jo, W., Kim, Y., Seo, M., Lee, N., & Park, J. (2022). Online information analysis on pancreatic cancer in Korea using structural topic model. Scientific Reports, 12(1), 10622. https://doi.org/ 10.1038/s41598-022-14506-1

Jones, Q., Ravid, G., & Rafaeli, S. (2004). Information overload and the message dynamics of online interaction spaces: A theoretical model and empirical exploration. Information Systems Research, 15(2), 194-210. https://doi.org/10.1287/isre.1040.0023

Jordan, M. I. (2003). An introduction to probabilistic graphical models.

Kim, S., & Oh, S. (2009). Users’ relevance criteria for evaluating answers in a social Q&A site. Journal of the American Society for Information Science and Technology, 60(4), 716-727. https://doi.org/10.1002/asi.21026

Kokkodis, M., Lappas, T., & Ransbotham, S. (2020). From lurkers to workers: Predicting voluntary contribution and community welfare. Information Systems Research, 31(2), 607-626. https://doi.org/10.1287/isre.2019.0905

Kumar, N., Qiu, L., & Kumar, S. (2022). A hashtag is worth a thousand words: An empirical investigation of social media strategies in trademarking hashtags. Information Systems Research, 33(4), 1403-1427. https://doi.org/10.1287/isre.2022.1107

Kyriakou, H., Nickerson, J. V., & Majchrzak, A. (2022). Novelty and the structure of design landscapes: A relational view of online innovation communities. MIS Quarterly, 46(3), 1691-1720. https://doi.org/10.25300/MISQ/2022/15059

Lakiotaki, K., Delias, P., Sakkalis, V., & Matsatsinis, N. F. (2009). User profiling based on multi-criteria analysis: The role of utility functions. Operational Research, 9(1), 3-16. https://doi.org 10.1007/s12351-008-0024-4

Lappas, T., Sabnis, G., & Valkanas, G. (2016). The impact of fake reviews on online visibility: A vulnerability assessment of the hotel industry. Information Systems Research, 27(4), 940-961. https://doi.org/10.1287/isre.2016.0674

Lee, G. M., Qiu, L., & Whinston, A. B. (2016). A friend like me: Modeling network formation in a location-based social network. Journal of Management Information Systems, 33(4), 1008-1033. https://doi.org/10.1080/07421222.2016.1267523

Lee, S.-Y., Rui, H., & Whinston, A. B. (2019). Is best answer really the best answer? The politeness bias. MIS Quarterly, 43(2), 579-600. https://doi.org/10.25300/MISQ/2019/14160

Li, J., Liao, M., Gao, W., He, Y., & Wong K. F. (2018). Topic extraction from microblog posts using conversation structures. Social Media Content Analysis: Natural Language Processing and Beyond, 419-437. https://doi.org/10.18653/v1/P16-1199

Li, W., Chen, H., & Nunamaker Jr, J. F. (2016). Identifying and profiling key sellers in cyber carding community: AZSecure text mining system. Journal of Management Information Systems, 33(4), 1059- 1086. https://doi.org/10.1080/07421222.2016.1267528

Liang, S. (2018). Dynamic user profiling for streams of short texts. In Proceedings of the 32nd AAAI Conference on Artificial Intelligence (pp. 5860-5867). https://doi.org/10.1609/aaai.v32i1.12051

Lin, C. X., Zhao, B., Mei, Q., & Han, J. (2010). PET: A statistical model for popular events tracking in social communities. Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 929-938). https://doi.org/10.1145/1835804.1835922

Liu, Q., Chen, T., Cai, J., & Yu, D. (2012). Enlister: Baidu’s recommender system for the biggest Chinese Q&A website. In

Proceedings of the 6th ACM Conference on Recommender Systems (pp. 285-288). https://doi.org/10.1145/2365952.2366016

Liu, X., Wang, G. A., Fan, W., & Zhang, Z. (2020). Finding useful solutions in online knowledge communities: A theory-driven design and multilevel analysis. Information Systems Research, 31(3), 731-752. https://doi.org/10.1287/isre.2019.0911

Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., & Neubig, G. (2023). Pre-train, prompt, and predict: A systematic survey of prompting methods in natural language processing. ACM Computing Surveys, 55(9), 1-35. https://doi.org/10.1145/3560815

Loughran, T., & McDonald, B. (2016). Textual analysis in accounting and finance: A survey. Journal of Accounting Research, 54(4), 1187-1230. https://doi.org/10.1111/1475-679X.12123

Ma, Z., Sun, A., Yuan, Q., & Cong, G. (2015). A tri-role topic model for domain-specific question answering. In Proceedings of the 29th AAAI Conference on Artificial Intelligence. https://doi.org/10.1609 aaai.v29i1.9182

Magdy, A., Abdelhafeez, L., Kang, Y., Ong, E., & Mokbel, M. F. (2020). Microblogs data management: A survey. The VLDB Journal, 29(1), 177-216. https://doi.org/10.1007/s00778-019-00569-6

Manning, C. D., Raghavan, P., & Schutze, H. S. (2008). Term weighting, and the vector space model. Introduction to Information Retrieval, 109-133. https://dl.acm.org/doi/abs/10.5555/1394399

McKinsey. (2013). Evolution of the networked enterprise. https://www.mckinsey.com/business-functions/mckinseydigital/our-insights/evolution-of-the-networked-enterprisemckinsey-global-survey-results

Miao, Y., Grefenstette, E., & Blunsom, P. (2017). Discovering discrete latent topics with neural variational inference. Proceedings of the International Conference on Machine Learning (pp. 2410-2419).

Mousavi, R., Raghu, T. S., & Frey, K. (2020). Harnessing artificial intelligence to improve the quality of answers in online questionanswering health forums. Journal of Management Information Systems, 37(4), 1073-1098. https://doi.org/10.1080/07421222. 2020.1831775

Narang, U., Yadav, M. S., & Rindfleisch, A. (2022). The “idea advantage”: How content sharing strategies impact engagement in online learning platforms. Journal of Marketing Research, 59(1), 61-78. https://doi.org/10.1177/00222437211017828

Oh, H., Goh, K. Y., & Phan, T. Q. (2023). Are you what you tweet? The impact of sentiment on digital news consumption and social media sharing. Information Systems Research, 34(1), 111-136. https://doi.org/10.1287/isre.2022.1112

Palese, B., & Piccoli, G. (2020). Evaluating topic modeling interpretability using topic labeled gold-standard sets. Communications of the Association for Information Systems, 47, 433-451. https://doi.org/10.17705/1CAIS.04720

Pu, J., Chen, Y., Qiu, L., & Cheng, H. K. (2020). Does identity disclosure help or hurt user content generation? Social presence, inhibition, and displacement effects. Information Systems Research, 31(2), 297-322. https://doi.org/10.1287/isre.2019.0885

Pu, J., Liu, Y., Chen, Y., Qiu, L., & Cheng, H. K. (2022). What questions are you inclined to answer? Effects of hierarchy in corporate Q&A communities. Information Systems Research, 33(1), 244-264. https://doi.org/10.1287/isre.2021.1052

Rai, Arun. (2016). Editor’s comments: Synergies between big data and theory. MIS Quarterly, 40(2), iii-ix. https://dl.acm.org/doi/ 10.5555/3177617.3177618

Rivera, M., Qiu, L., Kumar, S., & Petrucci, T. (2021). Are traditional performance reviews outdated? An empirical analysis on

continuous, real-time feedback in the workplace. Information Systems Research, 32(2), 517-540. https://doi.org/10.1287/isre. 2020.0979

Roberts, M. E., Stewart, B. M., & Airoldi, E. M. (2016). A model of text for experimentation in the social sciences. Journal of the American Statistical Association, 111(515), 988-1003. https://doi.org/10.1080/01621459.2016.1141684

Roberts, M. E., Stewart, B. M., & Tingley, D. (2019). stm: An R package for structural topic models. Journal of Statistical Software, 91(1), 1-40. https://doi.org/10.18637/jss.v091.i02

Rosen-Zvi, M., Chemudugunta, C., Griffiths, T., Smyth, P., & Steyvers, M. (2010). Learning author-topic models from text corpora. ACM Transactions on Information Systems, 28(1), 1-38. https://doi.org/10.1145/1658377.1658381

Rossiter, E. L. (2022). Measuring agenda setting in interactive political communication. American Journal of Political Science, 66(2), 337-351. https://doi.org/10.1111/ajps.12653

Samtani, S., Chinn, R., Chen, H., & Nunamaker Jr, J. F. (2017). Exploring emerging hacker assets and key hackers for proactive cyber threat intelligence. Journal of Management Information Systems, 34(4), 1023-1053. https://doi.org/10.1080/07421222. 2017.1394049

Sasaki, K., Yoshikawa, T., & Furuhashi, T. (2014). Online topic model for Twitter considering dynamics of user interests and topic trends. In Proceedings of the Conference on Empirical Methods in Natural Language Processing (pp. 1977-1985). https://doi.org/ 10.3115/v1/d14-1212

Shah, C. (2010). Collaborative information seeking: A literature review. Advances in Librarianship, 32, 3-33. https://doi.org/ 10.1108/S0065-2830(2010)0000032004

Shriver, S. K., Nair, H. S., & Hofstetter, R. (2013). Social ties and usergenerated content: Evidence from an online social network. Management Science, 59(6), 1425-1443. https://doi.org/10.1287/ mnsc.1110.1648

Singh, P. V., Sahoo, N., & Mukhopadhyay, T. (2014). How to attract and retain readers in enterprise blogging? Information Systems Research, 25(1), 35-52. https://doi.org/10.1287/isre.2013.0509

Syed, S., & Spruit, M. (2017). Full-text or abstract? Examining topic coherence scores using latent Dirichlet allocation. In Proceedings of the IEEE International Conference on Data Science and Advanced Analytics (pp. 165-174). https://doi.org/10.1109/DSAA. 2017.61

Szpektor, I., Maarek, Y., & Pelleg, D. (2013). When relevance is not enough: Promoting diversity and freshness in personalized question recommendation. In Proceedings of the 22nd International Conference on World Wide Web (pp. 1249-1260). https://doi.org/10.1145/2488388.2488497

Tang, J., Yao, L., Zhang, D., & Zhang, J. (2010). A combination approach to web user profiling. ACM Transactions on Knowledge Discovery from Data, 5(1), 1-44. https://doi.org/10.1145/1870096. 1870098

Timoshenko, A., & Hauser, J. R. (2019). Identifying customer needs from user-generated content. Marketing Science, 38(1), 1-20. https://doi.org/10.1287/mksc.2018.1123

Tirunillai, S., & Tellis, G. J. (2014). Mining marketing meaning from online chatter: Strategic brand analysis of big data using latent Dirichlet allocation. Journal of Marketing Research, 51(4), 463- 479. https://doi.org/10.1509/jmr.12.0106

Trusov, M., Ma, L., & Jamal, Z. (2016). Crumbs of the cookie: User profiling in customer-base analysis and behavioral targeting.

Marketing Science, 35(3), 405-426. https://doi.org/10.1287/mksc. 2015.0956

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... Polosukhin, I. (2017). Attention is all you need. In Proceedings of the International Conference on Neural Information Processing Systems. https://dl.acm.org/doi/10.5555/ 3295222.3295349

Velichety, S., Ram, S., & Bockstedt, J. (2019). Quality assessment of peer-produced content in knowledge repositories using development and coordination activities. Journal of Management Information Systems, 36, 478-512. https://doi.org/10.1080/07421 222.2019.1598692

Wainwright, M. J., & Jordan, M. I. (2008). Graphical models, exponential families, and variational inference. Foundations and Trends in Machine Learning, 1(1-2), 1-305. https://doi.org/ 10.1561/2200000001

Wang, C., & Blei, D. M. (2013). Variational inference in nonconjugate models. Journal of Machine Learning Research, 14(1), 1005- 1031. https://dl.acm.org/doi/10.5555/2567709.2502613

Wang, F., Zhang, J. L., Li, Y., Deng, K., & Liu, J. S. (2021). Bayesian text classification and summarization via a class-specified topic model. Journal of Machine Learning Research, 22(89), 1-48. https://dl.acm.org/doi/10.5555/3546258.3546347

Wang, H., Zhang, D., & Zhai, C. (2011). Structural topic model for latent topical structure analysis. In Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics: Human Language Technologies (pp. 1526-1535). https://dl.acm.org/doi/ 10.5555/2002472.2002657

Weng, J., Lim, E. P., Jiang, J., & He, Q. (2010). Twitterrank: Finding topic-sensitive influential Twitterers. In Proceedings of the 3rd ACM International Conference on Web Search and Data Mining (pp. 261-270). https://doi.org/10.1145/1718487.1718520

Xie, P., Chen, H., & Hu, Y. J. (2020). Signal or noise in social media discussions: The role of network cohesion in predicting the bitcoin market. Journal of Management Information Systems, 37(4), 933- 956. https://doi.org/10.1080/07421222.2020.1831762

Xu, L., Nian, T., & Cabral, L. (2019). What makes geeks tick? A study of stack overflow careers. Management Science, 66(2), 587-604. https://doi.org/10.1287/mnsc.2018.3264

Yang, L., Qiu, M., Gottipati, S., Zhu, F., Jiang, J., Sun, H., & Chen, Z. (2013). Cqarank: Jointly model topics and expertise in community question answering. In Proceedings of the 22nd ACM International Conference on Information & Knowledge Management, 99-108. https://doi.org/10.1145/2505515.2505720

Yang, M., Adomavicius, G., Burtch, G., & Ren, Y. (2018). Mind the gap: Accounting for measurement error and misclassification in variables generated via data mining. Information Systems Research, 29(1), 4-24. https://doi.org/10.1287/isre.2017.0727

Yang, Y., Zhang, K., & Fan, Y. (2023). sDTM: A supervised Bayesian deep topic model for text analytics. Information Systems Research, 34(1), 137-156. https://doi.org/10.1287/isre.2022.1124

Yin, K., Fang, X., Chen, B., & Liu Sheng, O. R. (2022). Diversity preference-aware link recommendation for online social networks. Information Systems Research, 34(4), 1398-1414. https://doi.org/ 10.1287/isre.2022.1174

Yue, W. T., Wang, Q., & Hui, K.-L. (2019). See no evil, hear no evil? Dissecting the impact of online hacker forums. MIS Quarterly, 43(1), 73-95. https://doi.org/10.25300/MISQ/2019/13042

Zeng, J., Li, J., He, Y., Gao, C., Lyu, M. R., & King, I. (2019). What you say and how you say it: Joint modeling of topics and discourse in microblog conversations. Transactions of the Association for Computational Linguistics, 7, 267-281. https://doi.org/10.1162/ tacl\_a\_00267

Zhao, W. X., Jiang, J., Weng, J., He, J., Lim, E. P., Yan, H., & Li, X. (2011). Comparing Twitter and traditional media using topic models. In Proceedings of the 33rd European Conference on IR Research (pp. 338-349). https://doi.org/10.1007/978-3-642- 20161-5\_34

Zhao, H., Phung, D., Huynh, V., Jin, Y., Du, L., & Buntine, W. (2021). Topic modelling meets deep neural networks: A survey. In Proceedings of the International Joint Conference on Artificial Intelligence (pp. 4713-4720). https://doi.org/10.24963/ijcai.2021/638

Zhong, N., & Schweidel, D. A. (2020). Capturing changes in social media content: A multiple latent changepoint topic model. Marketing Science, 39(4), 827-846. https://doi.org/10.1287/ mksc.2019.1212

## About the Authors

Dongcheng Zhang is an assistant professor at the CUHK Business School, the Chinese University of Hong Kong. His research primarily focuses on developing and applying machine learning algorithms, statistical methods, and analytical models to improve decision-making in digital marketing and management information systems.

Kunpeng Zhang is an associate professor of information systems in the Department of Decision, Operations & Information Technologies, Robert H. Smith School of Business, affiliated with MTI and AMSC at the University of Maryland, College Park. His research focuses on developing and applying scalable machine/deep learning algorithms to analyze unstructured data for better business decisions in online social media platforms. Specifically, he is interested in text/network/multimedia representation learning + causal inference.

Yi Yang is an associate professor in the Department of Information Systems, Business Statistics and Operations Management, School of Business and Management, at the Hong Kong University of Science and Technology. His research interests are natural language processing, machine learning, statistical inference, and their applications in finance and business.

David A. Schweidel is a professor of marketing at Emory University’s Goizueta Business School. He is an expert in the areas of customer relationship management and social media analytics. His research focuses on the development and application of statistical models to understand customer behavior and inform managerial decisions.

## Appendix A

## Summary of Topic Modeling Applications in OKC Research

Table A1 summarizes major studies on the topic modeling applications in OKC. To do so, we conducted an extensive literature search among premier journals in IS and other business disciplines and reviewed recent studies that apply topic models on texts with Q&A relations and threaded structures.

<table><tr><td colspan="5">Table A1. Summary of Topic Modeling Applications on OKC Texts</td></tr><tr><td>Ways to use topic vectors</td><td>Authors (Year)</td><td>Topic model applied</td><td>Textual data</td><td>Research topic</td></tr><tr><td rowspan="3">As independent variables</td><td>Yue et al. (2019)</td><td>LDA</td><td>Threaded posts in an online hacking forum</td><td>Extracting topics discussed in online hacking forum posts and exploring the impact of topics on distributed denial of service attacks</td></tr><tr><td>Narang et al. (2022)</td><td>LDA</td><td>Online learning discussions</td><td>Identifying the impact of content type (i.e., topic) on learner engagement</td></tr><tr><td>Gour et al. (2022)</td><td>LDA</td><td>Social media discussions</td><td>Deriving topics from social media discussions to help predict the disease outbreak</td></tr><tr><td rowspan="3">As dependent variables</td><td>Singh et al. (2014)</td><td>LDA</td><td>Enterprise blogs and comments</td><td>Impact of various factors (e.g., textual characteristics) on users' blog-reading of different topics</td></tr><tr><td>Li et al. (2016)</td><td>LDA</td><td>Threaded advertisements in a cyber carding community</td><td>Profiling key sellers using the derived topic vectors of advertisement threads</td></tr><tr><td>Geva et al. (2019)</td><td>LDA</td><td>Threaded tweets</td><td>Identifying users' interested topics from their blogs and studying the user behavior of shaping online persona via retweets</td></tr><tr><td rowspan="3">As control variables</td><td>Bapna et al. (2019)</td><td>LDA</td><td>Posts and comments in online brand communities</td><td>Impact of posts content dimensions on user engagement with topics as control variables</td></tr><tr><td>Xie et al. (2020)</td><td>LDA</td><td>Online Bitcoin-related discussion threads</td><td>Controlling the topics of discussion threads to identify the role of network cohesion in predicting Bitcoin returns</td></tr><tr><td>Kumar et al. (2022)</td><td>LDA</td><td>Posts and comments in online brand communities</td><td>Impact of trademarking hashtags on social media consumer engagement with topics as control variables</td></tr><tr><td rowspan="3">Deriving new variables</td><td>Lappas et al. (2016)</td><td>LDA</td><td>Customers' reviews and businesses' responses</td><td>Using the derived topics to further classify businesses' responses to customers' comments into different types</td></tr><tr><td>Guo et al. (2017)</td><td>LDA, hLDA, and DTM</td><td>Articles and comments on a blogging platform</td><td>Using the derived topics to extract representative information</td></tr><tr><td>Samtani et al. (2017)Hwang et al. (2019)</td><td>LDALDA</td><td>Posts and comments in an online hacker forumQ&amp;A posts in a customer support crowdsourcing community</td><td>Building topic-specific social networks based on the topics learned from textsConstructing each user's information network based on learned topics to further explore how topic-based information network influences the generation of novel ideas.</td></tr><tr><td rowspan="7"></td><td>Kokkodis et al. (2020)</td><td>LDA</td><td>Q&amp;A posts in an online diabetes community</td><td>Categorizing users into different contribution types by the topics of their posts</td></tr><tr><td>Mousavi et al. (2020)</td><td>HDP</td><td>Q&amp;A posts in a health-related community</td><td>Calculating the topic similarity between an answer and the question based on the derived topic vectors</td></tr><tr><td>Pu et al. (2020)</td><td>LDA</td><td>Q&amp;A posts on an enterprise platform</td><td>Impact of identity disclosure on users' effort measured by the topic similarity of Q&amp;A</td></tr><tr><td>Bachura et al. (2022)</td><td>LDA</td><td>Threaded tweets</td><td>Extracting breach-related concepts based on top salient terms from each topic</td></tr><tr><td>Kyriakou et al. (2022)</td><td>CTM</td><td>Descriptions and comments of product designs in an online innovation community</td><td>Using derived topic vectors to calculate the similarity among product designs to further measure novelty</td></tr><tr><td>Oh et al. (2023)</td><td>LDA</td><td>News articles</td><td>Combining learned topics with sentiment analysis to calculate topic valence</td></tr><tr><td>Pu et al. (2022)</td><td>LDA</td><td>Q&amp;A posts on an enterprise platform</td><td>Effects of hierarchy on question answering, controlling user's knowledge level measured by the topic similarity between the question and the user's existing answers</td></tr></table>

## Appendix B

## Details of Variational Inference

## The Objective Function: ELBO

The ELBO is given in Equation (3) of the Model Inference section. Before deriving optimization procedures in the coordinate ascent algorithm, we write each term of the ELBO in a specific functional form as follows.

(1) The first term (1):

$$
E _ {u} \big [ \log p (\pmb {\eta} _ {q}; \pmb {\mu}, \pmb {\Sigma} _ {q}) \big ] = \frac {1}{2} \log | \pmb {\Sigma} _ {q} ^ {- 1} | - \frac {K}{2} \log 2 \pi - \frac {1}{2} E _ {u} \left[ (\pmb {\eta} _ {q} - \pmb {\mu}) ^ {T} \pmb {\Sigma} _ {q} ^ {- 1} (\pmb {\eta} _ {q} - \pmb {\mu}) \right],
$$

where

$$
E _ {u} \big [ (\pmb {\eta} _ {q} - \pmb {\mu}) ^ {T} \pmb {\Sigma} _ {q} ^ {- 1} (\pmb {\eta} _ {q} - \pmb {\mu}) \big ] = T r \big [ d i a g (\pmb {\sigma} _ {q}) ^ {2} \pmb {\Sigma} _ {q} ^ {- 1} \big ] + \big (\lambda_ {q} - \pmb {\mu} \big) ^ {T} \pmb {\Sigma} _ {q} ^ {- 1} \big (\lambda_ {q} - \pmb {\mu} \big).
$$

(2) The second term $( N _ { q } ) \mathrm { : }$ :

$$
E _ {u} \big [ \log p \big (z _ {q} ^ {n _ {q}} | \pmb {\eta} _ {q} \big) \big ] = E _ {u} \big [ \pmb {\eta} _ {q} ^ {T} \pmb {\phi} _ {q} ^ {n _ {q}} \big ] - E _ {u} \left[ \log \left(\sum_ {k = 1} ^ {K} e ^ {\pmb {\eta} _ {q} ^ {k}}\right) \right] = \sum_ {k = 1} ^ {K} \lambda_ {q} ^ {k} \phi_ {q} ^ {n _ {q}, k} - E _ {u} \left[ \log \left(\sum_ {k = 1} ^ {K} e ^ {\pmb {\eta} _ {q} ^ {k}}\right) \right].
$$

As a logistic normal distribution is not conjugate to multinomial distribution, this term $\begin{array} { r } { E _ { u } \left[ \log \left( \sum _ { k = 1 } ^ { K } e ^ { \pmb { \eta } _ { q } ^ { k } } \right) \right] } \end{array}$ cannot be analytically computed. To preserve the lower bound on the log probability, we use a Taylor expansion here:

$$
E _ {u} \left[ \log \left(\sum_ {k = 1} ^ {K} e ^ {\eta_ {q} ^ {k}}\right) \right] \leq \xi_ {q} ^ {- 1} \left(\sum_ {k = 1} ^ {K} E _ {u} \left(e ^ {\eta_ {q} ^ {k}}\right)\right) + \log \xi_ {q} - 1.
$$

As $E _ { u } \left( e ^ { \eta _ { q } ^ { k } } \right) = e ^ { \lambda _ { q } ^ { k } + \frac { 1 } { 2 } \left( \sigma _ { q } ^ { k } \right) ^ { 2 } }$ , we know that:

$$
E _ {u} \bigl [ \log p (z _ {q} ^ {n _ {q}} | \pmb {\eta} _ {q}) \bigr ] \geq \sum_ {k = 1} ^ {K} \lambda_ {q} ^ {k} \phi_ {q} ^ {n _ {q}, k} - \xi_ {q} ^ {- 1} \left(\sum_ {k = 1} ^ {K} e ^ {\lambda_ {q} ^ {k} + \frac {1}{2} (\sigma_ {q} ^ {k}) ^ {2}}\right) - \log \xi_ {q} + 1.
$$

(3) The third term $( N _ { q } )$

$$
E _ {u} \big [ \log p \big (w _ {q} ^ {n _ {q}} | z _ {q} ^ {n _ {q}}, \pmb {\beta} _ {\pmb {q}} ^ {\mathbf {1 : K}} \big) \big ] = \sum_ {k = 1} ^ {K} \phi_ {q} ^ {n _ {q}, k} E _ {u} \left(\log \beta_ {q} ^ {\mathrm{k}, n _ {q}}\right) = \sum_ {k = 1} ^ {K} \phi_ {q} ^ {n _ {q}, k} \Bigg [ \psi (\tau_ {q} ^ {k, n _ {q}}) - \psi (\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}) \Bigg ].
$$

(4) The fourth term (K):

$$
E _ {u} \big [ \log p (\pmb {\beta} _ {q} ^ {k}; \pmb {\alpha} _ {q}) \big ] = - \log B (\pmb {\alpha} _ {q}) + \sum_ {v = 1} ^ {V} (\alpha_ {q} ^ {v} - 1) \big [ \psi (\tau_ {q} ^ {k, v}) - \psi (\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}) \big ],
$$

where V is the vocabulary size.

Zhang et al. / An Unsupervised Topic Model for Text in Online Knowledge Communities

(5) The fifth term (1):

$$
E _ {u} [ \log p (\pmb {x _ {d}}; \pmb {\delta}) ] = - \log B (\pmb {\delta}) + \sum_ {i = 1} ^ {2} (\delta_ {i} - 1) \left[ \psi \big (\nu_ {d} ^ {i} \big) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right].
$$

(6) The sixth term (T):

$$
E _ {u} \big [ \log p \big (y _ {a _ {t}} \big | \pmb {x} _ {d} \big) \big ] = \sum_ {i = 1} ^ {2} \psi_ {a _ {t}} ^ {i} E _ {u} \big [ \log \big (x _ {d} ^ {i} \big) \big ] = \sum_ {i = 1} ^ {2} \psi_ {a _ {t}} ^ {i} \left[ \psi \big (v _ {d} ^ {i} \big) - \psi \left(\sum_ {i = 1} ^ {2} v _ {d} ^ {i}\right) \right].
$$

(7) The seventh term (T):

$$
\begin{array}{l} E _ {u} \left[ \log p \left(\boldsymbol {\eta} _ {a _ {t}} \Big | \boldsymbol {\eta} _ {q}, \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}}, y _ {a _ {t}}; \boldsymbol {\Sigma} _ {a _ {f}}, \boldsymbol {\Sigma} _ {a _ {n}}, \gamma\right) \right] \\ = \psi_ {a _ {t}} ^ {1} \left\{\frac {1}{2} \log \left| \boldsymbol {\Sigma} _ {a _ {f}} ^ {- 1} \right| - \frac {K}{2} \log 2 \pi - \frac {1}{2} E _ {u} \left[ \left(\boldsymbol {\eta} _ {a _ {t}} - \frac {\boldsymbol {\eta} _ {q} + \gamma \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}}}{1 + \gamma}\right) ^ {T} \boldsymbol {\Sigma} _ {a _ {f}} ^ {- 1} \left(\boldsymbol {\eta} _ {a _ {t}} - \frac {\boldsymbol {\eta} _ {q} + \gamma \overline {{\boldsymbol {\eta}}} _ {a _ {t - 1}}}{1 + \gamma}\right) \right] \right\} \\ + \psi_ {a _ {t}} ^ {2} \left\{\frac {1}{2} \log \big | \boldsymbol {\Sigma} _ {a _ {n}} ^ {- 1} \big | - \frac {K}{2} \log 2 \pi - \frac {1}{2} E _ {u} \left[ (\boldsymbol {\eta} _ {a _ {t}} - \boldsymbol {\eta} _ {q}) ^ {T} \boldsymbol {\Sigma} _ {a _ {n}} ^ {- 1} (\boldsymbol {\eta} _ {a _ {t}} - \boldsymbol {\eta} _ {q}) \right] \right\}. \end{array}
$$

Let $\begin{array} { r } { \mathrm { A } = E _ { u } \left[ \left( \pmb { \eta } _ { a _ { t } } - \frac { \pmb { \eta } _ { q } + \gamma \overline { { \eta } } _ { a _ { t - 1 } } } { 1 + \gamma } \right) ^ { T } \pmb { \Sigma } _ { a _ { f } } ^ { - 1 } \left( \pmb { \eta } _ { a _ { t } } - \frac { \pmb { \eta } _ { q } + \gamma \overline { { \eta } } _ { a _ { t - 1 } } } { 1 + \gamma } \right) \right] , } \end{array}$ then:

$$
\text {   If   } t = 1,
$$

$$
A = T r \left[ d i a g (\pmb {\sigma} _ {a _ {t}}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right] + T r \left[ d i a g (\pmb {\sigma} _ {q}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right] + \bigl (\lambda_ {a _ {t}} - \lambda_ {q} \bigr) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \bigl (\lambda_ {a _ {t}} - \lambda_ {q} \bigr).
$$

$$
\mathrm{If} t \geq 2,
$$

$$
\begin{array}{r l} & A = T r \left[ d i a g (\pmb {\sigma} _ {a _ {t}}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right] + \frac {1}{(1 + \gamma) ^ {2}} T r \left[ d i a g (\pmb {\sigma} _ {q}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right] + \sum_ {i = 1} ^ {t - 1} \left(\frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma}\right) ^ {2} T r \left[ d i a g (\pmb {\sigma} _ {a _ {i}}) ^ {2} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right] \\ & \qquad + \left(\lambda_ {a _ {t}} - \frac {1}{1 + \gamma} \lambda_ {q} - \sum_ {i = 1} ^ {t - 1} \frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma} \lambda_ {a _ {i}}\right) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \left(\lambda_ {a _ {t}} - \frac {1}{1 + \gamma} \lambda_ {q} - \sum_ {i = 1} ^ {t - 1} \frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma} \lambda_ {a _ {i}}\right). \end{array}
$$

Let $\begin{array} { r } { \mathbf { B } = E _ { u } \left[ \left( \pmb { \eta } _ { \pmb { a } _ { t } } - \pmb { \eta } _ { \pmb { q } } \right) ^ { T } \pmb { \Sigma } _ { \pmb { a } _ { n } } ^ { - 1 } \left( \pmb { \eta } _ { \pmb { a } _ { t } } - \pmb { \eta } _ { \pmb { q } } \right) \right] . } \end{array}$ , then:

$$
B = T r \big [ d i a g (\pmb {\sigma} _ {a _ {t}}) ^ {2} \pmb {\Sigma} _ {a _ {n}} ^ {- 1} \big ] + T r \big [ d i a g (\pmb {\sigma} _ {q}) ^ {2} \pmb {\Sigma} _ {a _ {n}} ^ {- 1} \big ] + \big (\lambda_ {a _ {t}} - \lambda_ {q} \big) ^ {T} \pmb {\Sigma} _ {a _ {n}} ^ {- 1} \big (\lambda_ {a _ {t}} - \lambda_ {q} \big).
$$

(8) The eighth term $\textstyle ( \sum _ { t = 1 } ^ { T } N _ { a _ { t } }$ , similar to the second term):

$$
\begin{array}{r l} & E _ {u} \left[ \log p \left(z _ {a _ {t}} ^ {n _ {a _ {t}}} \middle | \pmb {\eta} _ {a _ {t}}\right) \right] = E _ {u} \big [ \pmb {\eta} _ {a _ {t}} ^ {T} \pmb {\phi} _ {a _ {t}} ^ {n _ {a _ {t}}} \big ] - E _ {u} \left[ \log \left(\sum_ {k = 1} ^ {K} e ^ {\eta_ {a _ {t}} ^ {k}}\right) \right] = \sum_ {k = 1} ^ {K} \lambda_ {a _ {t}} ^ {k} \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} - E _ {u} \left[ \log \left(\sum_ {k = 1} ^ {K} e ^ {\eta_ {a _ {t}} ^ {k}}\right) \right] \\ & \qquad \geq \sum_ {k = 1} ^ {K} \lambda_ {a _ {t}} ^ {k} \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} - \xi_ {a _ {t}} ^ {- 1} \left(\sum_ {k = 1} ^ {K} e ^ {\lambda_ {a _ {t}} ^ {k} + \frac 12 (\sigma_ {a _ {t}} ^ {k}) ^ {2}}\right) - \log \xi_ {a _ {t}} + 1. \end{array}
$$

(9) The ninth term $\textstyle ( \sum _ { t = 1 } ^ { T } N _ { a _ { t } }$ , similar to the third term):

$$
E _ {u} \left[ \log p \left(w _ {a _ {t}} ^ {n _ {a _ {t}}} \middle | z _ {a _ {t}} ^ {n _ {a _ {t}}}, \pmb {\beta} _ {\pmb {a}} ^ {\mathbf {1 : K}}\right) \right] = \sum_ {k = 1} ^ {K} \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} E _ {u} \left(\log \beta_ {a} ^ {\mathrm{k}, n _ {a _ {t}}}\right) = \sum_ {k = 1} ^ {K} \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} \left[ \psi \left(\tau_ {a} ^ {k, n _ {a _ {t}}}\right) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v}\right) \right].
$$

(10) The tenth term (??, similar to the fourth term):

$$
E _ {u} \big [ \log p \big (\pmb {\beta} _ {a} ^ {k}, \pmb {\alpha} _ {a} \big) \big ] = - \log B (\pmb {\alpha} _ {a}) + \sum_ {v = 1} ^ {V} (\alpha_ {a} ^ {v} - 1) \left[ \psi \big (\tau_ {a} ^ {k, v} \big) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v}\right) \right].
$$

(11) The eleventh term (1, the entropy term):

$$
\begin{array}{r l} & H (u) = \sum_ {k = 1} ^ {K} \frac {1}{2} \Big [ \log \big (\sigma_ {q} ^ {k} \big) ^ {2} + \log 2 \pi + 1 \Big ] + \sum_ {t = 1} ^ {T} \sum_ {k = 1} ^ {K} \frac {1}{2} \Big [ \log \big (\sigma_ {a _ {t}} ^ {k} \big) ^ {2} + \log 2 \pi + 1 \Big ] + \log B (\pmb {\nu_ {d}}) - \sum_ {i = 1} ^ {2} \big (\nu_ {d} ^ {i} - 1 \big) \Bigg [ \psi \big (\nu_ {d} ^ {i} \big) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \Bigg ] \\ & \qquad - \sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {2} \psi_ {a _ {t}} ^ {i} \log \psi_ {a _ {t}} ^ {i} - \sum_ {n _ {q} = 1} ^ {N _ {q}} \sum_ {k = 1} ^ {K} \phi_ {q} ^ {n _ {q}, k} \log \phi_ {q} ^ {n _ {q}, k} - \sum_ {t = 1} ^ {T} \sum_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} \sum_ {k = 1} ^ {K} \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} \log \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} + \sum_ {k = 1} ^ {K} \log B (\pmb {\tau_ {q} ^ {k}}) \\ & \qquad - \sum_ {k = 1} ^ {K} \sum_ {v = 1} ^ {V} (\tau_ {q} ^ {k, v} - 1) \Bigg [ \psi (\tau_ {q} ^ {k, v}) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \Bigg ] + \sum_ {k = 1} ^ {K} \log B (\pmb {\tau_ {a} ^ {k}}) - \sum_ {k = 1} ^ {K} \sum_ {v = 1} ^ {V} (\tau_ {a} ^ {k, v} - 1) \Bigg [ \psi (\tau_ {a} ^ {k, v}) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \Bigg ]. \end{array}
$$

To summarize, the ELBO is given by:

$$
\begin{array} { r l } E L B O = & { } \frac { 1 } { 2 } \log | \pmb { \Sigma } _ { q } ^ { - 1 } | - \frac { K } { 2 } \log 2 \pi - \frac { 1 } { 2 } T r \left[ d i a g ( \pmb { \sigma } _ { q } ) ^ { 2 } \pmb { \Sigma } _ { q } ^ { - 1 } \right] - \frac { 1 } { 2 } ( \lambda _ { q } - \pmb { \mu } ) ^ { T } \pmb { \Sigma } _ { q } ^ { - 1 } ( \lambda _ { q } - \pmb { \mu } ) \\ & + \sum _ { n _ { q } = 1 } ^ { N _ { q } } \left\{ \sum _ { k = 1 } ^ { K } \lambda _ { q } ^ { k } \phi _ { q } ^ { n _ { q } , k } - \xi _ { q } ^ { - 1 } \left( \sum _ { k = 1 } ^ { K } e ^ { \lambda _ { q } ^ { k } + \frac { 1 } { 2 } ( \sigma _ { q } ^ { k } ) ^ { 2 } } \right) - \log \xi _ { q } + 1 \right\} + \sum _ { n _ { q } = 1 } ^ { N _ { q } } \left\{ \sum _ { k = 1 } ^ { K } \phi _ { q } ^ { n _ { q } , k } \left[ \psi ( \tau _ { q } ^ { k , n _ { q } } ) - \psi ( \sum _ { v = 1 } ^ { V } \tau _ { q } ^ { k , v } ) \right] \right\} \\ & + \sum _ { k = 1 } ^ { K } \left\{ - \log B ( \pmb { \alpha } _ { q } ) + \sum _ { v = 1 } ^ { V } ( \alpha _ { q } ^ { v } - 1 ) [ \psi ( \tau _ { q } ^ { k , v } ) - \psi ( \sum _ { v = 1 } ^ { V } \tau _ { q } ^ { k , v } ) ] \right\} - \log B ( \pmb { \delta } ) + \sum _ { i = 1 } ^ { 2 } ( \delta _ { i } - 1 ) [ \psi ( \nu _ { d } ^ { i } ) - \psi ( \sum _ { i = 1 } ^ { 2 } \nu _ { d } ^ { i } ) ] \\ & + \sum _ { t = 1 } ^ { T } \sum _ { i = 1 } ^ { 2 } \psi _ { a _ { t }} ^ { i } [ \psi ( \nu _ { d } ^ { i } ) - \psi ( \sum _ { i = 1 } ^ { 2 } \nu _ { d } ^ { i } ) ] \\ & + \sum _ { t = 1 } ^ { T } \left\{ \psi _ { a _ { t }} ^ { 1 } \left\{ \frac { 1 } { 2 } \log | \pmb { \Sigma } _ { a _ { f }} ^ { - 1 } | - \frac { K } { 2 } \log 2 \pi - \frac { 1 } { 2 } E _ { u } [ (\pmb { \eta } _ { a _ { t }} - \frac  \pmb { \eta } _ { q } + \gamma \overline { { \pmb { \eta } } } _ { a _ { t - 1 } } ) ^ { T } \pmb {\Sigma} _ { a _ { f }} ^ {- 1} ( \pmb { \eta } _ { a _ { t }} - \frac { \pmb { \eta } _ { q } + \gamma \overline { { \pmb { \eta } } } _ { a _ { t - 1 } } ) ) ]} \right\} \\ & + \psi _ { a _ { t }} ^ { 2 } [ \frac { 1 } { 2 } \log | \pmb { \Sigma } _ { a _ { n }} ^ { - 1 } | - \frac { K } { 2 } \log 2 \pi - \frac { 1 } { 2 } E _ { u } [ ( \pmb { \eta } _ { a _ { t }} - \pmb { \eta } _ { q } ) ^ { T } \pmb {\Sigma} _ { a _ { n }} ^ {- 1} ( \pmb { \eta } _ { a _ { t }} - \pmb { \eta } _ { q} ) ] ] ] \\ & + \sum _ { t = 1 } ^ { T } \sum _ { n _ { a _ { t }} = 1 } ^ { N _ { a _ { t } } } [ \sum _ { k = 1 } ^ { K } \lambda _ { a _ { t }} ^ { k } \phi _ { a _ { t }} ^ { n _ { a _ { t }} , k } - \xi _ { a _ { t }} ^ { - 1 } ( \sum _ { k = 1 } ^ { K } e ^  \lambda _ { a _ { t }} ^ { k } + \frac { 1 } { 2 } ( \sigma _ { a _ { t }} ^ { k }) ^ { 2 } ) - \log \xi _ { a _ { t }} + 1 ] \\ & + \sum _ { t = 1 } ^ { T } \sum _ { n _ { a _ { t }} = 1 } ^ { N _ { a _ { t } } } [ \sum _ { k = 1 } ^ { K } \phi _ { a _ { t }} ^ { n _ { a _ { t }} , k } [ \psi ( \tau _ { a } ^ { k , n _ { a _ { t} }} ) - \psi ( \sum _ { v = 1 } ^ { V } \tau _ { a} ^ { k , v} ) ] ] \\ & + \sum _ { k = 1 } ^ { K } [ - l o g B ( \pmb {\alpha} _ {\pmb {\alpha}} ) + s u m b e r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f u r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f o r e f u r e f o r e f o r c e l i n g h i s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s w i d j i n g h i s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u s u . \\ & - \sum_ {{n _ {\boldsymbol {\alpha}}} = 1} ^ {{N} _ {\boldsymbol {\alpha}}} \sum_ {{k = 1}} ^ {{K}} {\phi_ {\boldsymbol {\alpha}} ^ {{n} _ {{q}}, k}} {\log {\phi_ {\boldsymbol {\alpha}} ^ {{n} _ {{q}}, k}}} - \sum_ {{t = 1}} ^ {{T}} \sum_ {{n} _ {{a} t}} \sum_ {{k = 1}} ^ {{N} _ {{a} t}} {\sum_ {{k = 1}} ^ {{K}} {\phi_ {\boldsymbol {\alpha} _ {{t}}}} ^ {{n} _ {{a} t}, k}} {\log {\phi_ {\boldsymbol {\alpha} _ {{t}}}} ^ {{n} _ {{a} t}, k}} + {\sum_ {{k = 1}} ^ {{K}} {\log B (\tau_ {\boldsymbol {\alpha}} ^ {{k}})}} \\ & - \sum_ {{k = 1}} ^ {{K}} \sum_ {{v = 1}} ^ {{V}} (\tau_ {\boldsymbol {\alpha}} ^ {{k}, v} - 1) [ \psi (\tau_ {\boldsymbol {\alpha}} ^ {{k}, v}) - {\psi (\sum_ {{v = 1}} ^ {{V}} {\tau_ {\boldsymbol {\alpha}} ^ {{k}}, v})} ] + {\sum_ {{k = 1}} ^ {{K}} {\log B (\tau_ {\boldsymbol {\alpha}} ^ {{k}})}} - \sum_ {{k = 1}} ^ {{K}} \sum_ {{v = 1}} ^ {{V}} (\tau_ {\boldsymbol {\alpha}} ^ {{k}, v} - 1) [ {\psi (\tau_ {\boldsymbol {\alpha}} ^ {{k}, v}) - {\psi (\sum_ {{v = 1}} ^ {{V}} {\tau_ {\boldsymbol {\alpha}} ^ {{k}}, v})} ]}. \\ & + C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C , \\ & + C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C, C , \\ & + D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D, D , \\ & + D (D) [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] [ A ] \\ & + E (E) [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] [ E ] {[ I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I I ,} \\ & + F (F) [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ] [ F ]. \\ & + G (G) [ G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ], G ]. \\ & + H (H), H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H : H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ; H ? , \\ & + J (J); J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J; J ; \\ & + K (K); K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K; K ; \\ & + L (L); L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L; L   . \\ & + M (M); M is the sum of all possible values. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & . \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + M (M) = M / N. \\ & + S (S) S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S S , \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & .\\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| P,Q,R,K,L,M,N,K,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,N,P,Q,R,K,L,M,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,m,n,\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{u},\mathbf{U}),\\ & + R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <  R (\mathbf{u}),\\ & + R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}),\\ & + R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}) <   R (\mathbf{u}),\\ & + R (\mathbf{u}) <   R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <    R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}) <     R (\mathbf{u}),\\ & + R (\mathbf{u}) <    R (\mathbf{u}) <    R (\mathbf{u}) <     R (\mathbf{u})< |content_end|>
$$

## Optimization Algorithm

For optimization in the variational inference, we use the coordinate ascent algorithm, iteratively maximizing the ELBO with respect to each variational parameter. Here we derive to update these parameters, including $\xi _ { q } , \phi _ { q } , { \lambda } _ { q } , \sigma _ { q } , \xi _ { a _ { t } } , \phi _ { a _ { t } } , { \lambda } _ { a _ { t } } , \sigma _ { a _ { t } } , \psi _ { a _ { t } } , \nu _ { d } , \tau _ { q } , \tau _ { a }$

(1) Maximize with respect to $\xi _ { q }$

$$
\frac {d E L B O}{d \xi_ {q}} = N _ {q} \left[ \xi_ {q} ^ {- 2} \left(\sum_ {k = 1} ^ {K} e ^ {\lambda_ {q} ^ {k} + \frac {1}{2} (\sigma_ {q} ^ {k}) ^ {2}}\right) - \xi_ {q} ^ {- 1} \right].
$$

$\begin{array} { r } { \mathrm { S e t } \frac { d E L B O } { d \xi _ { q } } = 0 , } \end{array}$ , we obtain: $\begin{array} { r } { \xi _ { q } ^ { * } = \sum _ { k = 1 } ^ { K } e ^ { \lambda _ { q } ^ { k } + \frac { 1 } { 2 } \left( \sigma _ { q } ^ { k } \right) ^ { 2 } } } \end{array}$ . Note that this is $E _ { q } \left( \sum _ { k = 1 } ^ { K } e ^ { \pmb { \eta } _ { q } ^ { k } } \right)$

(2) Maximize with respect to $\phi _ { q } ^ { n _ { q } }$

$$
\frac {d E L B O}{d \phi_ {q} ^ {n _ {q} , k}} = \lambda_ {q} ^ {k} + \left[ \psi (\tau_ {q} ^ {k, n _ {q}}) - \psi (\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}) \right] - \log \phi_ {q} ^ {n _ {q}, k} - 1.
$$

Since $\begin{array} { r } { \sum _ { k = 1 } ^ { K } \phi _ { q } ^ { n _ { q } , k } = 1 , \frac { d E L B O } { d \phi _ { q } ^ { n _ { q } , k } } = 0 } \end{array}$ implies $\phi _ { q } ^ { n _ { q } , k } \propto e ^ { \lambda _ { q } ^ { k } + \left[ \Psi \left( \tau _ { q } ^ { k , n _ { q } } \right) - \Psi \left( \sum _ { v = 1 } ^ { V } \tau _ { q } ^ { k , v } \right) \right] }$ , so then we can write the updating formula as follows:

$$
\phi_ {q} ^ {n _ {q}, k} = \frac {e ^ {\lambda_ {q} ^ {k} + [ \psi (\tau_ {q} ^ {k , n _ {q}}) - \psi (\Sigma_ {v = 1} ^ {V} \tau_ {q} ^ {k , v}) ]}}{\sum_ {k = 1} ^ {K} e ^ {\lambda_ {q} ^ {k} + [ \psi (\tau_ {q} ^ {k , n _ {q}}) - \psi (\Sigma_ {v = 1} ^ {V} \tau_ {q} ^ {k , v}) ]}}.
$$

(3) Maximize with respect to $\lambda _ { q }$

$$
\begin{array}{r l} & {\frac {d E L B O}{d \lambda_ {q}} = - \Sigma_ {q} ^ {- 1} (\lambda_ {q} - \mu) + \sum_ {n _ {q} = 1} ^ {N _ {q}} \phi_ {q} ^ {n _ {q}} - \frac {N _ {q}}{\xi_ {q}} \Big (e ^ {\lambda_ {q} + \frac {1}{2} (\sigma_ {q}) ^ {2}} \Big) + \psi_ {a _ {1}} ^ {1} \Sigma_ {a _ {f}} ^ {- 1} (\lambda_ {a _ {1}} - \lambda_ {q})} \\ & {\qquad + \frac {1}{1 + \gamma} \sum_ {t = 2} ^ {T} \psi_ {a _ {t}} ^ {1} \Sigma_ {a _ {f}} ^ {- 1} \Bigg (\lambda_ {a _ {t}} - \frac {1}{1 + \gamma} \lambda_ {q} - \sum_ {i = 1} ^ {t - 1} \frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma} \lambda_ {a _ {i}} \Bigg) + \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {2} \Sigma_ {a _ {n}} ^ {- 1} (\lambda_ {a _ {t}} - \lambda_ {q}).} \end{array}
$$

Se $\begin{array} { r } { \frac { d E L B O } { d \lambda _ { q } } = 0 . } \end{array}$ , and we find that this cannot be analytically solved. In previous studies, numerical methods have often been applied in variational inference for nonconjugate models (Blei & Lafferty, 2005; Blei & Lafferty, 2007; Wang & Blei, 2013; Roberts et al., 2016). Thus, we use the extended limited memory BFGS (Byrd et al., 1995; Wang et al., 2021) algorithm to update $\lambda _ { q }$ numerically. Moreover, note that as the Hessian matrix of ELBO on $\lambda _ { q }$ is negative-definite, this is a convex optimization problem, which guarantees that we can achieve the global optimum with the numerical method:

$$
H (E L B O) _ {\lambda_ {q}} = - \pmb {\Sigma} _ {q} ^ {- 1} - \frac {N _ {q}}{\xi_ {q}} \bigg (e ^ {\lambda_ {q} + \frac {1}{2} (\sigma_ {q}) ^ {2}} \bigg) - \psi_ {a _ {1}} ^ {1} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} - \frac {1}{(1 + \gamma) ^ {2}} \sum_ {t = 2} ^ {T} \psi_ {a _ {t}} ^ {1} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} - \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {2} \pmb {\Sigma} _ {a _ {n}} ^ {- 1}.
$$

(4) Maximize with respect to $\sigma _ { q }$

$$
\frac {d E L B O}{d \left(\sigma_ {q} ^ {k}\right) ^ {2}} = - \frac {1}{2} \pmb {\Sigma} _ {q} ^ {- 1 (k, k)} - \frac {N _ {q}}{2 \xi_ {q}} \bigg (e ^ {\lambda_ {q} ^ {k} + \frac {1}{2} \left(\sigma_ {q} ^ {k}\right) ^ {2}} \bigg) - \frac {1}{2} \psi_ {a _ {1}} ^ {1} \pmb {\Sigma} _ {a _ {f}} ^ {- 1 (k, k)} - \frac {1}{2} \sum_ {t = 2} ^ {T} \frac {\psi_ {a _ {t}} ^ {1}}{(1 + \gamma) ^ {2}} \pmb {\Sigma} _ {a _ {f}} ^ {- 1 (k, k)} - \frac {1}{2} \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {2} \pmb {\Sigma} _ {a _ {n}} ^ {- 1 (k, k)} + \frac {1}{2 \left(\sigma_ {q} ^ {k}\right) ^ {2}}.
$$

Similar to $\lambda _ { q } ,$ we use the extended limited memory BFGS to update ${ \pmb { \sigma } } _ { { \pmb { q } } } .$ This is also a convex optimization problem since the second derivative of ELBO on $\left( \sigma _ { q } ^ { k } \right) ^ { 2 }$ is negative:

$$
\frac {d ^ {2} E L B O}{[ d (\sigma_ {q} ^ {k}) ^ {2} ] ^ {2}} = - \frac {N _ {q}}{4 \xi_ {q}} \bigg (e ^ {\lambda_ {q} ^ {k} + \frac {1}{2} (\sigma_ {q} ^ {k}) ^ {2}} \bigg) - \frac {1}{2 [ (\sigma_ {q} ^ {k}) ^ {2} ] ^ {2}}.
$$

(5) Maximize with respect to $\xi _ { a _ { t } } , \tau = 1 { : } \mathrm { T }$

$$
\frac {d E L B O}{d \xi_ {a _ {t}}} = N _ {a} \left[ \xi_ {a _ {t}} ^ {- 2} \left(\sum_ {k = 1} ^ {K} e ^ {\lambda_ {a _ {t}} ^ {k} + \frac {1}{2} (\sigma_ {a _ {t}} ^ {k}) ^ {2}}\right) - \xi_ {a _ {t}} ^ {- 1} \right].
$$

$\begin{array} { r } { \mathrm { S e t } \frac { d E L B O } { d \xi _ { a _ { t } } } = 0 . } \end{array}$ , we obtain $\begin{array} { r } { \xi _ { a _ { t } } ^ { * } = \sum _ { k = 1 } ^ { K } e ^ { \lambda _ { a _ { t } } ^ { k } + \frac { 1 } { 2 } \left( \sigma _ { a _ { t } } ^ { k } \right) ^ { 2 } } } \end{array}$ . Note that this is $E _ { q } \left( \sum _ { k = 1 } ^ { K } e ^ { \pmb { \eta } _ { a _ { t } } ^ { k } } \right)$

Zhang et al. / An Unsupervised Topic Model for Text in Online Knowledge Communities

(6) Maximize with respect to $\phi _ { a _ { t } } ^ { n _ { a _ { t } } } , \mathrm { t } = 1 \colon \mathrm { T }$

$$
\frac {d E L B O}{d \phi_ {a _ {t}} ^ {n _ {a _ {t}} , k}} = \lambda_ {a _ {t}} ^ {k} + \left[ \psi (\tau_ {a} ^ {k, n _ {a _ {t}}}) - \psi (\sum_ {\nu = 1} ^ {V} \tau_ {a} ^ {k, \nu}) \right] - \log \phi_ {a _ {t}} ^ {n _ {a _ {t}}, k} - 1.
$$

Since $\begin{array} { r } { \sum _ { k = 1 } ^ { K } \phi _ { a _ { t } } ^ { n _ { a _ { t } } , k } = 1 , } \end{array}$

$$
\phi_ {a _ {t}} ^ {n _ {a _ {t}, k}} \propto e ^ {\lambda_ {a _ {t}} ^ {k} + \left[ \psi (\tau_ {a} ^ {k, n _ {a _ {t}}}) - \psi (\Sigma_ {v = 1} ^ {V} \tau_ {a} ^ {k, v}) \right]}, \mathrm{specifically} \phi_ {a _ {t}} ^ {n _ {a _ {t}, k}} = \frac {e ^ {\lambda_ {a _ {t}} ^ {k} + \left[ \psi (\tau_ {a} ^ {k , n _ {a _ {t}}}) - \psi (\Sigma_ {v = 1} ^ {V} \tau_ {a} ^ {k , v}) \right]}}{\sum_ {k = 1} ^ {K} e ^ {\lambda_ {a _ {t}} ^ {k} + \left[ \psi (\tau_ {a} ^ {k , n _ {a _ {t}}}) - \psi (\Sigma_ {v = 1} ^ {V} \tau_ {a} ^ {k , v}) \right]}}.
$$

(7) Maximize with respect to $\lambda _ { a _ { t } } , \mathrm { t } = 1 \colon \mathrm { T }$

When t = 1:

$$
\begin{array}{r} \frac {d E L B O}{d \pmb {\lambda} _ {a _ {t}}} = \psi_ {a _ {t}} ^ {1} \Bigg [ - \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \big (\pmb {\lambda} _ {a _ {t}} - \pmb {\lambda} _ {q} \big) + \sum_ {j = t + 1} ^ {T} \frac {\gamma \zeta_ {t} ^ {j}}{1 + \gamma} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \Bigg (\pmb {\lambda} _ {a _ {j}} - \frac {1}{1 + \gamma} \pmb {\lambda} _ {q} - \sum_ {i = 1} ^ {j - 1} \frac {\gamma \zeta_ {i} ^ {j}}{1 + \gamma} \pmb {\lambda} _ {a _ {i}} \Bigg) \Bigg ] + \psi_ {a _ {t}} ^ {2} \big [ - \pmb {\Sigma} _ {a _ {n}} ^ {- 1} \big (\pmb {\lambda} _ {a _ {t}} - \pmb {\lambda} _ {q} \big) \big ] + \sum_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} \pmb {\Phi} _ {a _ {t}} ^ {n _ {a _ {t}}} \\ - \frac {N _ {a _ {t}}}{\xi_ {a _ {t}}} \Big (e ^ {\lambda_ {a _ {t}} + \frac {1}{2} (\sigma_ {a _ {t}}) ^ {2}} \Big). \end{array}
$$

When $\mathrm { { t } } \geq 2 \mathrm { { : } }$

$$
\begin{array}{r l} & {\frac {d E L B O}{d \lambda_ {a _ {t}}} = \psi_ {a _ {t}} ^ {1} \Bigg [ - \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \bigg (\pmb {\lambda} _ {a _ {t}} - \frac {1}{1 + \gamma} \pmb {\lambda} _ {q} - \sum_ {i = 1} ^ {t - 1} \frac {\gamma \zeta_ {i} ^ {t}}{1 + \gamma} \pmb {\lambda} _ {a _ {i}} \bigg) + \sum_ {j = t + 1} ^ {T} \frac {\gamma \zeta_ {t} ^ {j}}{1 + \gamma} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \bigg (\pmb {\lambda} _ {a _ {j}} - \frac {1}{1 + \gamma} \pmb {\lambda} _ {q} - \sum_ {i = 1} ^ {j - 1} \frac {\gamma \zeta_ {i} ^ {j}}{1 + \gamma} \pmb {\lambda} _ {a _ {i}} \bigg) \Bigg ]} \\ & {\qquad + \psi_ {a _ {t}} ^ {2} \big [ - \pmb {\Sigma} _ {a _ {n}} ^ {- 1} \big (\pmb {\lambda} _ {a _ {t}} - \pmb {\lambda} _ {q} \big) \big ] + \sum_ {n _ {a _ {t}} = 1} ^ {N _ {a _ {t}}} \phi_ {a _ {t}} ^ {n _ {a _ {t}}} - \frac {N _ {a _ {t}}}{\xi_ {a _ {t}}} \Big (e ^ {\lambda_ {a _ {t}} + \frac {1}{2} (\sigma_ {a _ {t}}) ^ {2}} \Big).} \end{array}
$$

Similar to $\lambda _ { q } ,$ this is a convex optimization problem because the Hessian matrix of ELBO on $\lambda _ { a _ { t } }$ is negative-definite:

$$
H (E L B O) _ {\lambda_ {a _ {t}}} = - \psi_ {a _ {t}} ^ {1} \pmb {\Sigma} _ {\pmb {a} _ {f}} ^ {- 1} - \psi_ {a _ {t}} ^ {1} \sum_ {j = t + 1} ^ {T} \left(\frac {\gamma \zeta_ {t} ^ {j}}{1 + \gamma}\right) ^ {2} \pmb {\Sigma} _ {\pmb {a} _ {f}} ^ {- 1} - \psi_ {a _ {t}} ^ {2} \pmb {\Sigma} _ {\pmb {a} _ {n}} ^ {- 1} - \frac {N _ {a _ {t}}}{\xi_ {a _ {t}}} \Big (e ^ {\lambda_ {a _ {t}} + \frac {1}{2} (\sigma_ {a _ {t}}) ^ {2}} \Big).
$$

Therefore, we use the extended limited memory BFGS to update $\lambda _ { a _ { t } }$ . From this updating process, we can see that the topic distribution of a focal answer is impacted by not only the focal question and former answers, but also the latter answers. In other words, our Bayesian framework takes the bidirectional correlations of threaded answers into account, which enhances the capability of posterior model inference.

(8) Maximize with respect to $\pmb { \sigma _ { a _ { t } } , \mathrm { t } } = 1 : \mathrm { T }$

$$
\frac {d E L B O}{d \left(\sigma_ {a _ {t}} ^ {k}\right) ^ {2}} = \psi_ {a _ {t}} ^ {1} \left[ - \frac {1}{2} \boldsymbol {\Sigma} _ {\boldsymbol {a} _ {f}} ^ {- 1 (k, k)} - \frac {1}{2} \sum_ {j = t + 1} ^ {T} \left(\frac {\gamma \zeta_ {t} ^ {j}}{1 + \gamma}\right) ^ {2} \boldsymbol {\Sigma} _ {\boldsymbol {a} _ {f}} ^ {- 1 (k, k)} \right] + \psi_ {a _ {t}} ^ {2} \left[ - \frac {1}{2} \boldsymbol {\Sigma} _ {\boldsymbol {a} _ {n}} ^ {- 1 (k, k)} \right] - \frac {N _ {a _ {t}}}{2 \xi_ {a _ {t}}} \Bigl (e ^ {\lambda_ {a _ {t}} ^ {k} + \frac {1}{2} (\sigma_ {a _ {t}} ^ {k}) ^ {2}} \Bigr) + \frac {1}{2 (\sigma_ {a _ {t}} ^ {k}) ^ {2}}.
$$

Similar to ${ \pmb { \sigma } } _ { { \pmb { q } } } ,$ this is a convex optimization problem because the second derivative of ELBO on $\left( \sigma _ { a _ { t } } ^ { k } \right) ^ { 2 }$ is negative:

$$
\frac {d ^ {2} E L B O}{[ d (\sigma_ {a _ {t}} ^ {k}) ^ {2} ] ^ {2}} = - \frac {N _ {a _ {t}}}{4 \xi_ {a _ {t}}} \bigg (e ^ {\lambda_ {a _ {t}} ^ {k} + \frac {1}{2} (\sigma_ {a _ {t}} ^ {k}) ^ {2}} \bigg) - \frac {1}{2 [ (\sigma_ {a _ {t}} ^ {k}) ^ {2} ] ^ {2}},
$$

so we use the extended limited memory BFGS to update $\pmb { \sigma } _ { \pmb { a } _ { t } }$

(9) Maximize with respect to $\psi _ { a _ { t } } , \mathrm { t } = 1 : \mathrm { T }$

$$
\frac {d E L B O}{d \psi_ {a _ {t}} ^ {1}} = \left[ \psi (\nu_ {d} ^ {1}) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] + \frac {1}{2} \log \left| \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \right| - \frac {K}{2} \log 2 \pi - \frac {1}{2} E _ {u} \left[ \left(\pmb {\eta} _ {a _ {t}} - \frac {\pmb {\eta} _ {q} + \gamma \overline {{\pmb {\eta}}} _ {a _ {t - 1}}}{1 + \gamma}\right) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \left(\pmb {\eta} _ {a _ {t}} - \frac {\pmb {\eta} _ {q} + \gamma \overline {{\pmb {\eta}}} _ {a _ {t - 1}}}{1 + \gamma}\right) \right] - \log \psi_ {a _ {t}} ^ {1}
$$

$$
\frac {d E L B O}{d \psi_ {a _ {t}} ^ {2}} = \left[ \psi (\nu_ {d} ^ {2}) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] + \frac {1}{2} \log | \pmb {\Sigma} _ {a _ {n}} ^ {- 1} | - \frac {K}{2} \log 2 \pi - \frac {1}{2} E _ {u} [ (\pmb {\eta} _ {a _ {t}} - \pmb {\eta} _ {q}) ^ {T} \pmb {\Sigma} _ {a _ {n}} ^ {- 1} (\pmb {\eta} _ {a _ {t}} - \pmb {\eta} _ {q}) ] - \log \psi_ {a _ {t}} ^ {2} - 1.
$$

Since $\textstyle \sum _ { i = 1 } ^ { 2 } \psi _ { a _ { t } } ^ { i } = 1$ , it is easy to know $\begin{array} { r } { \psi _ { a _ { t } } ^ { 1 } = \frac { e ^ { C } } { e ^ { C } + e ^ { D } } , \psi _ { a _ { t } } ^ { 2 } = \frac { e ^ { D } } { e ^ { C } + e ^ { D } } , \mathrm { ~ w h e r e ~ } C = \left[ \Psi ( \nu _ { d } ^ { 1 } ) - \Psi \big ( \sum _ { i = 1 } ^ { 2 } \nu _ { d } ^ { i } \big ) \right] + \frac { 1 } { 2 } \log \left| \Sigma _ { a _ { f } } ^ { - 1 } \right| - \frac { 1 } { 2 } E _ { u } \left[ \left( \eta _ { a _ { t } } - \eta _ { a _ { t } } \right) ^ { 2 } \right] , } \end{array}$

$$
\left. \frac {\eta_ {q} + \gamma \overline {{\eta}} _ {a _ {t - 1}}}{1 + \gamma}\right) ^ {T} \pmb {\Sigma} _ {a _ {f}} ^ {- 1} \left(\pmb {\eta} _ {a _ {t}} - \frac {\eta_ {q} + \gamma \overline {{\eta}} _ {a _ {t - 1}}}{1 + \gamma}\right) \Bigg ], D = \left[ \psi (\nu_ {d} ^ {2}) - \psi (\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}) \right] + \frac {1}{2} \log | \pmb {\Sigma} _ {a _ {n}} ^ {- 1} | - \frac {1}{2} E _ {u} \left[ (\pmb {\eta} _ {a _ {t}} - \pmb {\eta} _ {q}) ^ {T} \pmb {\Sigma} _ {a _ {n}} ^ {- 1} (\pmb {\eta} _ {a _ {t}} - \pmb {\eta} _ {q}) \right].
$$

(10) Maximize with respect to $\nu _ { d }$

$$
\begin{array}{r l r} & & {\frac {d E L B O}{d \nu_ {d} ^ {i}} = (\delta_ {i} - 1) \left[ \psi_ {1} (\nu_ {d} ^ {i}) - \psi_ {1} \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] + \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {i} \left[ \psi_ {1} (\nu_ {d} ^ {i}) - \psi_ {1} \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] + \left[ \psi (\nu_ {d} ^ {i}) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] - \left[ \psi (\nu_ {d} ^ {i}) - \psi \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right]} \\ & & {- (\nu_ {d} ^ {i} - 1) \left[ \psi_ {1} (\nu_ {d} ^ {i}) - \psi_ {1} \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right] = (\delta_ {i} + \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {i} - \nu_ {d} ^ {i}) \left[ \psi_ {1} (\nu_ {d} ^ {i}) - \psi_ {1} \left(\sum_ {i = 1} ^ {2} \nu_ {d} ^ {i}\right) \right].} \end{array}
$$

$\begin{array} { r } { \mathrm { S e t } { \frac { d E L B O } { d \nu _ { d } ^ { i } } } = 0 , \mathrm { a s } \left[ \Psi _ { 1 } \left( \nu _ { d } ^ { i } \right) - \Psi _ { 1 } \left( \sum _ { i = 1 } ^ { 2 } \nu _ { d } ^ { i } \right) \right] > 0 \mathrm { ( N o t e } \Psi ^ { \prime } > 0 , \Psi ^ { \prime \prime } < 0 ) } \end{array}$ , we obtain:

$$
\nu_ {d} ^ {i} = \delta_ {i} + \sum_ {t = 1} ^ {T} \psi_ {a _ {t}} ^ {i}.
$$

(11) Maximize with respect to $\tau _ { q }$

$$
\begin{array}{l} \frac {d E L B O}{d \tau_ {q} ^ {k , v}} = (\phi_ {q} ^ {v, k} * n u m _ {q} ^ {v}) \left[ \psi_ {1} (\tau_ {q} ^ {k, v}) - \psi_ {1} \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right] + (\alpha_ {q} ^ {v} - 1) \left[ \psi_ {1} (\tau_ {q} ^ {k, v}) - \psi_ {1} \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right] \\ \qquad + \frac {1}{B (\boldsymbol {\tau} _ {q} ^ {k})} B (\boldsymbol {\tau} _ {q} ^ {k}) \left[ \psi (\tau_ {q} ^ {k, v}) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right] - \left[ \psi (\tau_ {q} ^ {k, v}) - \psi \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right] - (\tau_ {q} ^ {k, v} - 1) \left[ \psi_ {1} (\tau_ {q} ^ {k, v}) - \psi_ {1} \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right] \\ \qquad = (\phi_ {q} ^ {v, k} * n u m _ {q} ^ {v} + \alpha_ {q} ^ {v} - \tau_ {q} ^ {k, v}) \left[ \psi_ {1} (\tau_ {q} ^ {k, v}) - \psi_ {1} \left(\sum_ {v = 1} ^ {V} \tau_ {q} ^ {k, v}\right) \right], \end{array}
$$

where ??????<sub>??</sub><sup>??</sup> is the number of word ?? in document ??.

Set $\begin{array} { r } { \frac { d E L B O } { d \tau _ { q } ^ { k , v } } = 0 , \mathrm { a s } \left[ \Psi _ { 1 } \big ( \tau _ { q } ^ { k , v } \big ) - \Psi _ { 1 } \big ( \sum _ { v = 1 } ^ { V } \tau _ { q } ^ { k , v } \big ) \right] > 0 } \end{array}$ (Note $\Psi ^ { \prime } > 0 , \Psi ^ { \prime \prime } < 0 )$ , we obtain $\tau _ { q } ^ { k , v } = \phi _ { q } ^ { v , k } * n u m _ { q } ^ { v } + \alpha _ { q } ^ { v }$ . (Note that $\begin{array} { r l r } { \mathrm { } } & { { } } & { \frac { d ^ { 2 } E L B O } { d \tau _ { a } ^ { k , v ^ { 2 } } } = } \end{array}$ (??<sub>??</sub><sup>??,??</sup> ∗ ??????<sub>??</sub><sup>??</sup> + α<sub>??</sub><sup>??</sup> − ??<sub>??</sub><sup>??,??</sup>)[ψ<sub>2</sub>(??<sub>??</sub><sup>??,??</sup>) − ψ<sub>2</sub>(∑ ??<sub>??</sub><sup>??</sup> <sup>??,??</sup><sub>??=1</sub> )] − [ψ<sub>1</sub>(??<sub>??</sub><sup>??,??</sup>) − ψ<sub>1</sub>(∑ ??<sub>??</sub><sup>??</sup> <sup>??,??</sup><sub>??=1</sub> )] = −[ψ<sub>1</sub>(??<sub>??</sub><sup>??,??</sup>) − ψ<sub>1</sub>(∑ ??<sub>??</sub><sup>??</sup> <sup>??,??</sup><sub>??=1</sub> )] < 0.)

(12) Maximize with respect to $\pmb { \tau _ { a } }$

$$
\begin{array}{r l} & {\frac {d E L B O}{d \tau_ {a} ^ {k , v}} = \sum_ {t = 1} ^ {T} \big (\phi_ {a _ {t}} ^ {v, k} * n u m _ {a _ {t}} ^ {v} \big) \Bigg [ \psi_ {1} \big (\tau_ {a} ^ {k, v} \big) - \psi_ {1} \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ] + (\alpha_ {a} ^ {v} - 1) \Bigg [ \psi_ {1} \big (\tau_ {a} ^ {k, v} \big) - \psi_ {1} \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ]} \\ & {\qquad + \frac {1}{B (\pmb {\tau} _ {a} ^ {k})} B (\pmb {\tau} _ {a} ^ {k}) \Bigg [ \psi (\tau_ {a} ^ {k, v}) - \psi \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ] - \Bigg [ \psi (\tau_ {a} ^ {k, v}) - \psi \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ] - (\tau_ {a} ^ {k, v} - 1) \Bigg [ \psi_ {1} \big (\tau_ {a} ^ {k, v} \big) - \psi_ {1} \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ]} \\ & {\qquad = \Bigg (\sum_ {t = 1} ^ {T} \phi_ {a _ {t}} ^ {v, k} * n u m _ {a _ {t}} ^ {v} + \alpha_ {a} ^ {v} - \tau_ {a} ^ {k, v} \Bigg) \Bigg [ \psi_ {1} \big (\tau_ {a} ^ {k, v} \big) - \psi_ {1} \Bigg (\sum_ {v = 1} ^ {V} \tau_ {a} ^ {k, v} \Bigg) \Bigg ],} \end{array}
$$

where $n u m _ { a _ { t } } ^ { v }$ is the number of word ?? in document $a _ { t } .$

Set $\begin{array} { r } { \frac { d E L B O } { d \tau _ { a } ^ { k , v } } = 0 . } \end{array}$ , we obtain $\begin{array} { r } { \tau _ { a } ^ { k , v } = \sum _ { t = 1 } ^ { T } \phi _ { a _ { t } } ^ { v , k } * n u m _ { a _ { t } } ^ { v } + \alpha _ { a } ^ { v } . } \end{array}$

If there are multiple Q&A documents, the updating formulas of $\tau _ { q }$ and $\pmb { \tau _ { a } }$ are as follows:

$$
\tau_ {q} ^ {k, v} = \sum_ {d = 1} ^ {D} \phi_ {d, q} ^ {v, k} * n u m _ {d, q} ^ {v} + \alpha_ {q} ^ {v},
$$

$$
\tau_ {a} ^ {k, v} = \sum_ {d = 1} ^ {D} \sum_ {t = 1} ^ {T} \phi_ {d, a _ {t}} ^ {v, k} * n u m _ {d, a _ {t}} ^ {v} + \alpha_ {a} ^ {v}.
$$

## A Variant of TM-OKC (one ??)

As we illustrate in Figure 1 of the main paper, our topic modeling framework TM-OKC allows questions and answers to have different topic-word distributions $\pmb { \beta _ { q } }$ and $\pmb { \beta _ { a } }$ . This is because the same topic in questions and answers can be expressed by different words. For example, in online news and comments, news is written by reporters while comments are made by the general public. For the same topic, words used in news can be more formal than those in comments. Therefore, we use different $\pmb { \beta _ { q } }$ and $\pmb { \beta _ { a } }$ to make the main framework as generalizable as possible. This setting is also seen in prior research (Ji et al., 2012). Note that if the texts are not observed, $\beta _ { q }$ and $\pmb { \beta _ { a } }$ are independent from each other. However, during the model inference, conditioned on the observed texts (i.e., $w _ { q }$ and ${ \pmb w _ { a _ { t } } } ) , { \pmb \beta _ { q } }$ and $\pmb { \beta _ { a } }$ are dependent due to the “v-structures” among parameters: $\ " { z } _ { q } \right. \pmb { w } _ { q } \left. \pmb { \beta } _ { q } \mathnormal { , } \qquad $ and $\mathbf { } ^ { \mathrm { e } } \mathbf { } _ { { \pmb { Z } } _ { { \pmb { a } } _ { t } } }  \mathbf { w } _ { { \pmb { a } } _ { t } }  \beta _ { { \pmb { a } } } ^ { \mathrm { ~  ~ } }$ (Jordan, 2003). Thus, $\pmb { \beta _ { q } }$ and $\pmb { \beta _ { a } }$ need to be jointly optimized to ensure their comparability. All the derivation of variational inference presented previously in this Appendix B is based on this general framework. However, it should be noted that it makes more sense to adopt the same topic-word distribution for questions and answers in certain contexts (e.g., professional Q&A). Thus, we intentionally created a variant with only one ?? (i.e., $\beta _ { q } =$ $\pmb { \beta _ { a } } )$ . The graphical representation is shown in Figure B1.

![](/api/attachments/TSBSG3KK/fulltext/images/923d9f9bf5d8c9350c6b5f0fdbff19c162f85c65ed8ad6393ca5da0ebf1ff90b.jpg)  
Figure B1. Graphical Representation of the Variant with One ??

The model derivation can be obtained straightforwardly by revising the previous derivations as follows.

(1) Substitute all $\beta _ { q }$ and $\pmb { \beta _ { a } }$ in the derivations with the same $\pmb { \beta } .$ And substitute the prior parameter of $\beta _ { q }$ and $\pmb { \beta _ { a } }$ (i.e., $\alpha _ { q }$ and $\pmb { \alpha _ { a } } )$ with the same ??.

(2) Substitute all $\tau _ { q }$ and $\pmb { \tau _ { a } }$ with the same ??. Recall that ?? is the parameter of the variational distribution of $\pmb { \beta } .$

(3) Substitute the derivation of $\tau _ { q }$ and $\pmb { \tau _ { a } }$ in (11) and (12) in the Optimization Algorithm section with the same derivation for ?? as follows.

$$
\begin{array}{r l} & {\frac {d E L B O}{d \tau_ {q} ^ {k , v}} = \bigg (\phi_ {q} ^ {v, k} * n u m _ {q} ^ {v} + \sum_ {t = 1} ^ {T} \phi_ {a _ {t}} ^ {v, k} * n u m _ {a _ {t}} ^ {v} \bigg) \bigg [ \psi_ {1} (\tau^ {k, v}) - \psi_ {1} \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ] + (\alpha^ {v} - 1) \bigg [ \psi_ {1} (\tau^ {k, v}) - \psi_ {1} \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ]} \\ & {\qquad + \frac {1}{B (\pmb {\tau} _ {q} ^ {k})} B (\pmb {\tau} _ {q} ^ {k}) \bigg [ \psi (\tau^ {k, v}) - \psi \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ] - \bigg [ \psi (\tau^ {k, v}) - \psi \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ] - (\tau^ {k, v} - 1) \bigg [ \psi_ {1} (\tau^ {k, v}) - \psi_ {1} \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ]} \\ & {\qquad = \bigg (\phi_ {q} ^ {v, k} * n u m _ {q} ^ {v} + \sum_ {t = 1} ^ {T} \phi_ {a _ {t}} ^ {v, k} * n u m _ {a _ {t}} ^ {v} + \alpha^ {v} - \tau^ {k, v} \bigg) \bigg [ \psi_ {1} (\tau^ {k, v}) - \psi_ {1} \bigg (\sum_ {v = 1} ^ {V} \tau^ {k, v} \bigg) \bigg ].} \end{array}
$$

where ??????<sub>??</sub><sup>??</sup> is the number of word ?? in document $q ,$ and $n u m _ { a _ { t } } ^ { v }$ is the number of word ?? in document $a _ { t }$

Set $\begin{array} { r } { \frac { d E L B O } { d \tau ^ { k , v } } = 0 . } \end{array}$ , as $\begin{array} { r } { [ \Psi _ { 1 } ( \tau ^ { k , v } ) - \Psi _ { 1 } ( \sum _ { v = 1 } ^ { V } \tau ^ { k , v } ) ] > 0 } \end{array}$ (Note $\Psi ^ { \prime } > 0 , \Psi ^ { \prime \prime } < 0 )$ , we obtain the updating formula of ?? as follows:

$$
\tau^ {k, v} = \phi_ {q} ^ {v, k} * n u m _ {q} ^ {v} + \sum_ {t = 1} ^ {T} \phi_ {a _ {t}} ^ {v, k} * n u m _ {a _ {t}} ^ {v} + \alpha^ {v}.
$$

If there are multiple Q&A documents, the updating formula of ?? is as follows:

$$
\tau^ {k, v} = \sum_ {d = 1} ^ {D} \phi_ {d, q} ^ {v, k} * n u m _ {d, q} ^ {v} + \sum_ {d = 1} ^ {D} \sum_ {t = 1} ^ {T} \phi_ {d, a _ {t}} ^ {v, k} * n u m _ {d, a _ {t}} ^ {v} + \alpha^ {v}.
$$

## Explanation of “Dependency and Variation”

Our framework is flexible in modeling the explicit structural relations by capturing both the dependency and variation within the Q&A thread. “Dependency” means that the topics of the current answer depend on the question and perhaps also on prior answers, and “variation” means that users can focus on new topics that may not be saliently mentioned in the question or prior answers.

The mathematical details of the model structure are presented in Figure 1 and the related explanations in the main paper. Note that “dependent $\mathrm { o n } ^ { \dag }$ does not suggest “equal $\mathrm { t o } ^ { \prime \prime }$ in the model. For example, for a novel answer, we draw the topic distribution $\pmb { \theta } _ { a _ { t } }$ from a logistic-normal distribution as follows:

$$
\pmb {\eta} _ {a _ {t}} \sim N \big (\pmb {\eta} _ {q}, \pmb {\Sigma} _ {a _ {n}} \big),
$$

$$
\pmb {\theta} _ {a _ {t}} = \frac {e x p \{\pmb {\eta} _ {a _ {t}} \}}{\sum_ {k = 1} ^ {K} e x p \{\eta_ {a _ {t}} ^ {k} \}}.
$$

On the one hand, the mean parameter of this logistic-normal distribution is $\pmb { \eta _ { q } }$ (the natural parameterization of the question’s topic distribution $\pmb { \theta } _ { q } ) _ { \mpb { \imath } }$ , reflecting the dependency on the question. On the other hand, the variance-covariance matrix $\Sigma _ { a _ { r } }$ reflects the variation. This is why the answer depends on the question while there are differences between the topic distributions of the question and its answer. It can be analogous to the familiar linear regression, $\begin{array} { r } { \mathbf { y } = \mathbf { \nabla } \beta \cdot x + \varepsilon , \mathbf { \nabla } \varepsilon { \sim } N ( 0 , \sigma ) } \end{array}$ . This regression is equivalent to $y { \sim } N ( \beta \cdot x , \sigma )$ , where y depends on $\beta \cdot x$ but is not equal to $\beta \cdot x$ because there is the variation parameter ?? to capture the “fluctuation” around $\beta \cdot x .$

The rationale behind this “dependency and variation” structure is quite straightforward, because users usually read questions before providing their answers. Some answers may be highly correlated with the question, while others may be less or barely correlated with the question. Such a variation is captured by the $\Sigma _ { a _ { n } }$ . Intuitively, we can think that the topic distribution of a novel answer varies or fluctuates around the topic distribution of its question.

## Appendix C

# Hyper-Parameter Settings and Computational Resources

## Hyper-Parameter Settings

In the experiments of evaluating the statistical model fit, we set the common hyper-parameters to be the same for fair comparison. For other hyper-parameters that are specific to each method, we followed recommendations from the original papers, as well as performing a grid search to find relatively optimal settings. Specifically, the hyper-parameters of our TM-OKC and other topic models are set as follows.

Number of topics. For all topic models, we adopted a widely used approach to select the optimal number of topics from a set of predefined numbers (i.e., 5, 10, 20, 40, and 80). That is, we trained the model on the training set, chose the number of topics based on the log-likelihood on the validation set, and, finally, reported the performance on the holdout test set (Griffiths & Steyvers, 2004; Roberts et al., 2019; Bapna et al., 2019).

Stopping criteria. All these methods optimized the model by iteratively improving the log-likelihood. We used the same stopping criteria in training, e.g., the log-likelihood between two consecutive iterations is less than a predefined threshold (i.e., 1e-5).

Prior distribution. For the hyper-parameters of the prior Dirichlet and beta distributions (i.e., ?? and ?? in our model) in the topic models, we followed prior literature and set them to 0.1 (Griffiths & Steyvers, 2004). We also performed a grid search over the range of [0.01, 1] and the results are similar.

Other hyper-parameters specific to some methods. For the topic models combined with deep language models (i.e., NTM and SCHOLAR), we performed a grid search for the dimension of hidden embedding (the original papers of NTM and SCHOLAR both recommended 300) over the set of [50, 150, 300, 450, 600], for the learning rate during training (the original paper of NTM and SCHOLAR recommended 0.001 and 0.002, respectively) over the set of [0.01, 0.002, 0.001, 0.0005, 0.0001], and for the batch size during training (the original paper of NTM and SCHOLAR recommended 512 and 200, respectively) over the set of [32, 128, 200, 512, 1024]. For LeadLDA, since it uses Gibbs sampling for model inference, we performed a grid search over the set of [500, 1000, 2000] for the maximum number of iterations and the results are similar.

In the experiments of document classification in the additional evaluation presented in Appendix F, we needed to specify the hyper-parameters for the random forest algorithm where we feed the document-level topic vectors into a random forest model to predict the category of each document. Specifically, we performed a grid search over the set of [50, 100, 200, 300, 500] for the number of estimators, and over the set of [2, 4, 6, 8, 12, None] for the maximum depth of the decision trees. In addition, we followed the default settings of the scikit-learn package in Python for other hyper-parameters of the random forest algorithm.

## Computational Resources

All the experiments were conducted on a machine with an Intel 8-core i9 CPU with 64GB of RAM. In our Stack Exchange datasets, the largest one was the category of “English Language & Usage” with 109,977 questions and 268,356 answers, which took approximately 23 hours to finish training our TM-OKC; the smallest one was the category of “Project Management,” with 5,782 questions and 17,724 answers; it took approximately 0.7 hours to finish training our TM-OKC. Note that since we use EM algorithm, the most time-consuming part is the E-step, which can be parallelized with multiple processes to further reduce the run time.

## Appendix D

## Perplexity Scores for Other Categories

To show robustness of the model fit, we pictorially show the perplexity scores for each method (ours and the baselines) under different numbers of topics (i.e., 5, 10, 20, 40, and 80) on the holdout data.

![](/api/attachments/TSBSG3KK/fulltext/images/546225f63896913561e4f698c3dea9b2fe524dfb1fcb7999c673c5fc1d41a92f.jpg)

![](/api/attachments/TSBSG3KK/fulltext/images/925d7dae0616d0615717a67b2729ea2466398890d77199df1e47065436dfaac7.jpg)

(a) Category: English Language & Usage  
![](/api/attachments/TSBSG3KK/fulltext/images/1fc24347841792acd4c45e28c670e8f6011b4a67aa46761504cb0dae74e03668.jpg)  
(c) Category: Computer Science

b) Category: Cooking  
![](/api/attachments/TSBSG3KK/fulltext/images/b415c5eba9a6dc38bf6611c5b09eed58adede691c1195e5b35e147f6d0288349.jpg)  
(d) Category: Writing

![](/api/attachments/TSBSG3KK/fulltext/images/dacf7d501bfb9aa4a3ed28a09fd4e7bee42acc6f4919fd4553b382578aa30494.jpg)  
(e) Category: Project Management

## Appendix E

## Examination of Important Parameters in the TM-OKC

The TM-OKC models the interdependency of a question and its answers, as well as the temporal variation of threaded answers in its Bayesian framework, which is significantly different from prior studies. For example, the TM-OKC allows differential impacts of the question and of prior answers on the current answer by incorporating the parameter ??. The TM-OKC also captures the variances of topic distributions for questions and answers, denoted by $\Sigma _ { q } , \Sigma _ { a _ { f } }$ and $\Sigma _ { a _ { n } }$ , respectively. Larger ?? indicates that answers are more easily affected by prior answers. Larger $\pmb { \Sigma } _ { q }$ indicates more variation in the topics of questions, while larger $\Sigma _ { a _ { f } } \mathrm { o r } \Sigma _ { a _ { n } }$ means that the topic distribution of follow-up or novel answers is more likely to fluctuate. These unique parameters in our model can reflect important structural information of OKC texts, which can potentially be used in subsequent empirical studies to generate new insights.

Table E1 shows values of ?? learned from the Stack Exchange dataset, upon which we make the following observations. First, the values of ?? are larger for “soft-skill” categories (i.e., Project Management, Writing, English Language & Usage and Cooking) compared to the “hardskill” categories (i.e., Data Science, Computer Science), suggesting that answers in soft-skill categories are more likely to be affected by previous answers. This is expected because answers to questions in the soft-skill categories are more flexible. Second, the values of ?? for the categories of Data Science and Computer Science are less than 1 while the values for the other four categories are greater than 1, which indicates that topics of follow-up answers in these four categories might be dominated by the previous answers but not the original question. Table E2 shows values of ?? learned from the Quora dataset, which are much higher than the values learned from the Stack Exchange dataset in general. This might be because Stack Exchange is a professional Q&A site while Quora is more like a social media platform, so the user of Stack Exchange will focus more on answering the questions rather than on joining previous discussions.

<table><tr><td colspan="7">Table E1. The Learned γ Under Different Models Across Categories of Stack Exchange</td></tr><tr><td>Model</td><td>Technology (Data Science)</td><td>Culture/ Recreation (English Language &amp; Usage)</td><td>Life/Arts (Cooking)</td><td>Science (Computer Science)</td><td>Professional (Writing)</td><td>Business (Project Management)</td></tr><tr><td>TM-OKC (mean)</td><td>0.38</td><td>2.72</td><td>2.59</td><td>0.89</td><td>2.68</td><td>2.65</td></tr><tr><td>TM-OKC (decay)</td><td>0.36</td><td>2.45</td><td>2.58</td><td>0.87</td><td>9.76</td><td>2.51</td></tr><tr><td>TM-OKC (weight)</td><td>0.72</td><td>2.66</td><td>1.90</td><td>0.77</td><td>2.04</td><td>2.08</td></tr></table>

<table><tr><td colspan="4">Table E2. The Learned γ Under Different Models Across Categories of Quora</td></tr><tr><td>Model</td><td>Science and Technology</td><td>Business and Marketing</td><td>Health and Life</td></tr><tr><td>TM-OKC (mean)</td><td>2.50</td><td>3.59</td><td>3.84</td></tr><tr><td>TM-OKC (decay)</td><td>2.31</td><td>3.75</td><td>3.98</td></tr><tr><td>TM-OKC (weight)</td><td>2.20</td><td>3.81</td><td>3.73</td></tr></table>

Table E3 summarizes the variances reflected by $\Sigma _ { a _ { f } }$ and $\pmb { \Sigma _ { a _ { n } } } ^ { 1 2 }$ learned from the Stack Exchange dataset, upon which we can make several notable observations. First, in the categories of Data Science and Computer Science, ?? is smaller but $\pmb { \Sigma } _ { { \pmb { a } } _ { f } }$ and $\Sigma _ { a _ { n } }$ are larger. One possible explanation is that, in these two hard-skill categories, users need to raise distinct topics to address hardcore technical issues. Therefore, users are more likely to adjust the focus of the discussion, driven by their intention to provide professional answers rather than participating for fun. Second, in the two hard-skill categories, $\Sigma _ { a _ { f } }$ is larger than $\Sigma _ { a _ { n } }$ , indicating greater fluctuation in follow-up answers than novel answers. This might be because a novel answer tends to address the technical question directly and thus would not deviate much, while a follow-up answer may deviate from th previous discussions due to the user’s own interests. However, in the categories of English Language & Usage and Cooking, $\Sigma _ { a _ { f } }$ can be smaller than $\Sigma _ { a _ { n } }$ because the follow-up discussions in these categories are more like daily chat and thus do not fluctuate much. In addition, Table E4 summarizes the variance parameters learned from the Quora dataset. We can see that the heterogeneity among different Quora categories is not very significant compared to Stack Exchange, which shows the different styles of these two Q&A platforms.

Table E3. The Variances of Topic Distribution by Different Models Across Stack Exchange Categories

<table><tr><td></td><td>Model</td><td>Technology (Data Science)</td><td>Culture/ Recreation (English Language &amp; Usage)</td><td>Life/Arts (Cooking)</td><td>Science (Computer Science)</td><td>Professional (Writing)</td><td>Business (Project Management)</td></tr><tr><td rowspan="3"> $\Sigma_{af}$ </td><td>TM-OKC (mean)</td><td>5.96</td><td>0.46</td><td>0.48</td><td>4.12</td><td>1.72</td><td>0.49</td></tr><tr><td>TM-OKC (decay)</td><td>3.86</td><td>0.49</td><td>0.48</td><td>4.51</td><td>1.63</td><td>0.49</td></tr><tr><td>TM-OKC (weight)</td><td>3.52</td><td>0.52</td><td>0.53</td><td>7.33</td><td>0.50</td><td>0.51</td></tr><tr><td rowspan="3"> $\Sigma_{an}$ </td><td>TM-OKC (mean)</td><td>1.17</td><td>0.74</td><td>0.82</td><td>1.27</td><td>0.59</td><td>0.73</td></tr><tr><td>TM-OKC (decay)</td><td>2.32</td><td>0.78</td><td>0.81</td><td>1.27</td><td>0.60</td><td>0.74</td></tr><tr><td>TM-OKC (weight)</td><td>1.14</td><td>0.74</td><td>0.82</td><td>1.26</td><td>0.71</td><td>0.73</td></tr></table>

<table><tr><td colspan="5">Table E4. The Variances of Topic Distribution by Different Models Across Quora Categories</td></tr><tr><td></td><td>Model</td><td>Science and Technology</td><td>Business and Marketing</td><td>Health and Life</td></tr><tr><td rowspan="3"> $\Sigma_{a_f}$ </td><td>TM-OKC (mean)</td><td>0.60</td><td>0.61</td><td>0.57</td></tr><tr><td>TM-OKC (decay)</td><td>0.61</td><td>0.59</td><td>0.56</td></tr><tr><td>TM-OKC (weight)</td><td>0.63</td><td>0.57</td><td>0.59</td></tr><tr><td rowspan="3"> $\Sigma_{a_n}$ </td><td>TM-OKC (mean)</td><td>0.98</td><td>1.08</td><td>1.04</td></tr><tr><td>TM-OKC (decay)</td><td>1.01</td><td>1.06</td><td>1.01</td></tr><tr><td>TM-OKC (weight)</td><td>1.03</td><td>1.05</td><td>1.06</td></tr></table>

## Appendix F

## Additional Evaluation of the TM-OKC

In this Appendix, we present the details on the additional evaluation of our TM-OKC in terms of representation capability and interpretability.

## Representation Capability

We used a prediction task of document classification to demonstrate the representation capability among different methods; this has been used by previous studies to evaluate the effectiveness of topic models (Zeng et al., 2019; Yang et al., 2023). Specifically, the prediction task is formalized in three steps. (1) We sampled 2,000 questions and their answers from each of the six categories in our Stack Exchange dataset (or sample 1,000 questions and their answers from each of the three categories within our Quora dataset) and then combined them to form a dataset for document classification, where the category was the label in this supervised classification task. (2) We applied topic models on the combined dataset to obtain a topic vector for each document. (3) We fed the learned topic vector to a classifier (i.e., random forest) to predict the document category.

Baselines: To validate the effectiveness of our method, we chose three sets of baselines to obtain document representations (i.e., Step 2 as described above).

• Topic models: We used all benchmark topic models listed in the Model Evaluation section of the main paper (i.e., LDA, NTM, TRTM, STM, SCHOLAR, QATM, LeadLDA, and SITS).

• Basic textual feature extraction methods: We employed the commonly used term frequency-inverse document frequency (TF-IDF) method with the top W (W=100, 500, or 1,000) words in the corpus to represent each document.

• Representation learning methods: First, we chose the bidirectional long-short term memory (Bi-LSTM) method, given its success in many document classification tasks (Adhikari et al., 2019). Second, we chose the transformer-based BERT, an advanced large language model (Devlin et al., 2019). To make a comprehensive comparison, we used both pretrained and fine-tuned BERT.<sup>13</sup> Note that although they may have strong prediction power, the representation learning methods were not able to produce interpretable results (e.g., topics). While our study focused on unsupervised topic modeling that can extract interpretable topics from texts, we still included these cutting-edge representation learning methods for comparison to show the representative capability of TM-OKC.

Evaluation Metrics: Since this is a standard multiclass classification task and the datasets are balanced, we used the standard classification accuracy (i.e., the percentage of correctly classified instances) as the evaluation metric. We repeated the experiments 30 times and report the average performance.

The prediction results are presented in Table F1. For topic modeling methods, we varied the number of topics to show robustness. From the table, we make the following observations. First, our model achieved the best prediction performance among all topic modeling methods across different numbers of topics. Second, all topic modeling methods other than LDA showed better performance than the basic TF-IDF feature extraction method. Third, using the topic vectors derived from our topic model as the input to a simple machine learning classifier (i.e., random forest) can achieve even better performance than Bi-LSTM and comparable performance with the fine-tuned BERT. These results highlight that topic models can be used to represent the semantics of texts and that compared to existing topic modeling methods, our model has stronger representation capability on OKC texts.

<table><tr><td colspan="8">Table F1. Prediction Accuracy of Different Methods on Two Modified Datasets</td></tr><tr><td rowspan="2"></td><td></td><td colspan="3">Stack Exchange</td><td colspan="3">Quora</td></tr><tr><td>Number of topics</td><td>40</td><td>80</td><td>120</td><td>40</td><td>80</td><td>120</td></tr><tr><td rowspan="3">Basic text feature extraction methods</td><td>TF-IDF features (top 100 words)</td><td></td><td>0.517</td><td></td><td></td><td>0.600</td><td></td></tr><tr><td>TF-IDF features (top 500 words)</td><td></td><td>0.717</td><td></td><td></td><td>0.779</td><td></td></tr><tr><td>TF-IDF features (top 1000 words)</td><td></td><td>0.718</td><td></td><td></td><td>0.804</td><td></td></tr><tr><td rowspan="7">Bayesian topic modeling methods</td><td>LDA</td><td>0.727</td><td>0.710</td><td>0.699</td><td>0.728</td><td>0.726</td><td>0.712</td></tr><tr><td>TRTM</td><td>0.891</td><td>0.885</td><td>0.893</td><td>0.935</td><td>0.920</td><td>0.937</td></tr><tr><td>STM</td><td>0.886</td><td>0.847</td><td>0.888</td><td>0.935</td><td>0.935</td><td>0.930</td></tr><tr><td>QATM</td><td>0.898</td><td>0.853</td><td>0.860</td><td>0.960</td><td>0.962</td><td>0.937</td></tr><tr><td>LeadLDA1</td><td>0.867</td><td>0.832</td><td>0.751</td><td>0.762</td><td>0.749</td><td>0.747</td></tr><tr><td>LeadLDA2</td><td>0.865</td><td>0.865</td><td>0.749</td><td>0.796</td><td>0.762</td><td>0.737</td></tr><tr><td>SITS</td><td>0.903</td><td>0.891</td><td>0.868</td><td>0.881</td><td>0.893</td><td>0.876</td></tr><tr><td rowspan="2">Topic modeling combined with deep language models</td><td>NTM</td><td>0.905</td><td>0.900</td><td>0.859</td><td>0.813</td><td>0.827</td><td>0.848</td></tr><tr><td>SCHOLAR</td><td>0.901</td><td>0.903</td><td>0.885</td><td>0.826</td><td>0.855</td><td>0.818</td></tr><tr><td rowspan="3">Representation learning methods</td><td>Bi-LSTM</td><td></td><td>0.822</td><td></td><td></td><td>0.919</td><td></td></tr><tr><td>Pretrained BERT</td><td></td><td>0.696</td><td></td><td></td><td>0.722</td><td></td></tr><tr><td>Fine-tuned BERT</td><td></td><td>0.936</td><td></td><td></td><td>0.992</td><td></td></tr><tr><td>Our method</td><td>TM-OKC</td><td>0.911*</td><td>0.933***</td><td>0.918***</td><td>0.983**</td><td>0.990***</td><td>0.968***</td></tr></table>

Note: The statistical significance was calculated compared with the best topic modeling method under a one-tailed t-test. \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001.

## Interpretability

We now turn to investigating the interpretability of the generated topics. One intuitive way to do this is by evaluating face validity, where we showed the top 10 words for several topics of our model and the best baseline model (please refer to Appendix G). To further explore the interpretability in a more rigorous way, we followed previous research (Chang et al., 2009; Bao & Datta, 2014; Palese & Piccoli, 2020) and conducted word intrusion and topic intrusion through lab studies. The detailed procedures are described below.

The word intrusion task was used to quantitatively measure the semantic coherence of the identified topics. Specifically, the subject was presented with six randomly ordered words. The subject’s task is to find the one word (i.e., the intruder) that is out of place or not in line with the others. If the set of words excluding the intruder makes sense together, then the subject can easily identify the intruder. For example, in the set {elephant, tiger, horse, apple, pig, cow}, most people can identify “apple” as the intruder because the remaining words, {elephant, tiger, horse, pig, cow} are coherent—they are all animals. In contrast, for another set {car, teacher, lion, agile, blue, square} that lacks such semantic coherence, it is difficult to identify the intruder. In order to evaluate the semantic coherence of a topic, we first selected the five most probable words of a topic. Then, an intruder word was randomly selected from those words with low probabilities in the current topic (to reduce the possibility of the intruder coming from the same semantic group) but high probabilities in some other topics (to ensure that the intruder would not be rejected solely because of rarity). Finally, all six words were shuffled and presented to the subject, as in Figure F1a. The evaluation metric for such a word intrusion task is the model precision, which is defined as the fraction of subjects agreeing with the topic model. Specifically, the word intrusion precision of the k<sup>th</sup> topic learned by model m is defined as:

<table><tr><td colspan="8">1/20Not every model is able to learn sample-by-sample or incrementally. However, in scikit-learn, there&#x27;re some models which have partial_fit method: Incremental fit on a batch of samples ... You can just search for methods name in sklearn&#x27;s documentation ... Also, you can use Random Forest and set number of samples (or sample ratio) per tree is small to fit the memory. Or use Dask and Dask ML to fit your data in memory.</td></tr><tr><td>model</td><td>data</td><td>train</td><td>test</td><td>feature</td><td>valu</td><td>predict</td><td>class</td></tr><tr><td>memori</td><td>access</td><td>address</td><td>map</td><td>block</td><td>bit</td><td>store</td><td>devic</td></tr><tr><td>inform</td><td>method</td><td>news</td><td>govern</td><td>descript</td><td>like</td><td>medium</td><td>offici</td></tr><tr><td>problem</td><td>number</td><td>algorithm</td><td>time</td><td>sum</td><td>log</td><td>function</td><td>frac</td></tr></table>

$$
W I P _ {m} ^ {k} = \frac {1}{S} \sum_ {s = 1} ^ {S} {\bf 1} (i _ {k, s} ^ {m} = w _ {k} ^ {m}),
$$

where $w _ { k } ^ { m }$ is the true intruding word among the set of words generated from the $k ^ { \mathrm { { t h } } }$ topic learned by model m, $i _ { k , s } ^ { m }$ is the intruder selected by subject s from the set of words generated from the $k ^ { \mathrm { { t h } } }$ topic learned by model m, S is the number of subjects, and $\mathbf { 1 } ( \cdot )$ is the indicator function. Finally, the precision of model m $( \mathrm { i . e . , } W I P _ { m } )$ is obtained by taking the average of $W I P _ { m } ^ { k }$ over topics.

![](/api/attachments/TSBSG3KK/fulltext/images/6904e851368412abc9d5ea57bcb5696b842e2a07ae9532698365c6280cc04510.jpg)  
(a) Word intrusion  
(b) Topic intrusion  
Figure F1. Screenshots of the Lab Studies for Word Intrusion and Topic Intrusion

The topic intrusion task measures whether the model’s document decomposition, in which a document is broken down into a mixture of topics, is consistent with human judgment of the same document. In this task, human subjects are presented with a document along with four topics (with each topic represented by the eight words with the highest probabilities within that topic), as in Figure F1b. Three of those topics are those with the highest probabilities associated with that document. The remaining intruder topic is randomly chosen from other topics with low probabilities. The evaluation metric for topic intrusion task is topic log odds, a quantitative measure of the agreement between the model and human judgment. Specifically, the measure is defined as the log ratio of the probability assigned to the true intruder to the probability assigned to the intruder selected by the subject:

$$
T L O _ {m} ^ {d} = \frac {1}{S} \sum_ {s = 1} ^ {S} \Bigl (\log \hat {\theta} _ {d, t _ {d} ^ {m}} ^ {m} - \log \hat {\theta} _ {d, j _ {d, s} ^ {m}} ^ {m} \Bigr),
$$

where $t _ { d } ^ { m }$ is the true intruder topic among those with the highest probabilities of document d inferred by model m, $j _ { d , s } ^ { m }$ is the intruder topic selected by subject s from the topics with the highest probabilities of document d inferred by model m, $\hat { \theta } _ { d , k } ^ { m }$ is the probability assigned to topic k in document d inferred by model $m ,$ and S is the number of subjects. Finally, the overall measure for model m $( \mathrm { i . e . , } T L O _ { m } )$ is obtained by taking the average of $T L O _ { m } ^ { d }$ over documents. A larger value of $T L O _ { m }$ indicates a greater agreement between the judgment of the model and the subjects. We can see that the upper bound of $T L O _ { m }$ is 0, which can only be achieved when all subjects pick out the true intruder topics for all documents.

Using the same two modified datasets introduced in the previous Representation Capability section, we conducted the two tasks separately on our model and the baseline topic models (i.e., LDA, NTM, TRTM, STM, SCHOLAR, QATM, LeadLDA, and SITS). For the word intrusion task, we evaluated the top 10 topics generated by each topic model on two datasets across different numbers of topics (i.e., 40, 80, and 120). For the topic intrusion task, we randomly sampled 60 posts from the corpus and evaluated the performance for each topic model across different numbers of topics. To carry out these tasks with human subjects, we used the popular crowdsourcing platform Amazon Mechanical Turk and presented each subject with 10 word intrusion or 20 topic intrusion tasks. For the sake of robustness, we ensured that each task was performed by eight different workers (Chang et al., 2009). The results are shown in Table F2. The table shows that our model achieved significantly better human evaluation performance.

<table><tr><td colspan="7">Table F2. Human Evaluation Results of Word Intrusion and Topic Intrusion Tasks</td></tr><tr><td></td><td colspan="3"> $WIP_m$  in word intrusion</td><td colspan="3"> $TLO_m$  in topic intrusion</td></tr><tr><td>Number of topics</td><td>40</td><td>80</td><td>120</td><td>40</td><td>80</td><td>120</td></tr><tr><td>LDA</td><td>0.806</td><td>0.794</td><td>0.788</td><td>-1.61</td><td>-1.65</td><td>-1.85</td></tr><tr><td>NTM</td><td>0.825</td><td>0.813</td><td>0.819</td><td>-1.52</td><td>-1.47</td><td>-1.48</td></tr><tr><td>TRTM</td><td>0.813</td><td>0.838</td><td>0.806</td><td>-1.43</td><td>-1.35</td><td>-1.49</td></tr><tr><td>STM</td><td>0.819</td><td>0.825</td><td>0.819</td><td>-1.37</td><td>-1.25</td><td>-1.47</td></tr><tr><td>SCHOLAR</td><td>0.813</td><td>0.819</td><td>0.813</td><td>-1.36</td><td>-1.30</td><td>-1.51</td></tr><tr><td>QATM</td><td>0.825</td><td>0.831</td><td>0.813</td><td>-1.31</td><td>-1.22</td><td>-1.39</td></tr><tr><td>SITS</td><td>0.819</td><td>0.825</td><td>0.800</td><td>-1.32</td><td>-1.29</td><td>-1.38</td></tr><tr><td>LeadLDA1</td><td>0.813</td><td>0.806</td><td>0.800</td><td>-</td><td>-</td><td>-</td></tr><tr><td>LeadLDA2</td><td>0.819</td><td>0.813</td><td>0.794</td><td>-</td><td>-</td><td>-</td></tr><tr><td>TM-OKC</td><td> $0.856^{**}$ </td><td> $0.869^{**}$ </td><td> $0.838^*$ </td><td> $-1.12^{**}$ </td><td> $-0.96^{***}$ </td><td> $-1.23^{**}$ </td></tr></table>

Note: (1) The statistical significance was calculated compared with the best topic modeling method under a one-tailed t-test. \* $p < 0 . 0 5 , ^ { \star \star } p <$ $0 . 0 1 , ^ { \star \star \star } p < 0 . 0 0 1 ; ( 2 )$ As LeadLDA only assigns one single topic to each post, the $T L O _ { m }$ cannot be calculated and thus LeadLDA is excluded in the topic intrusion task.

## Appendix G

## Face Validity of Generated Topics

To provide the face validity of generated topics, we showed the top 10 words with the highest probabilities in the top 10 topics of our model and of the best baseline model. For the modified Stack Exchange dataset, we chose NTM as the baseline, and we report the results of our model and NTM with 40 topics in Table G1 and Table G2. We chose NTM because it achieved the best prediction performance among the topic model baselines in the document classification task presented in Appendix F, with 40 topics. As shown in Table G1 and G2, Topic 7 and Topic 8 learned by NTM are both about “model” and are not very distinguishable, while the topic on “model” is well captured in one single topic (i.e., Topic 4) of TM-OKC. For the Quora dataset, we report the results of our model and QATM with 80 topics in Table G3 and Table G4. We selected QATM because it achieved the best prediction performance among the topic model baselines in the document classification task presented in Appendix F, with 80 topics. It can be seen that the topic on “code and software” spreads across three topics (Topic 2, 5, and 10) in QATM, while this topic is well captured in one single topic (i.e., Topic 3) in TM-OKC. From these tables, we can see that in comparison to the best benchmark, the topics learned by our TM-OKC model are more coherent and distinguishable, providing a face validity of its effectiveness in modeling interdependencies among questions and answers in OKCs.

<table><tr><td colspan="2">Table G1. Top 10 Topics Learned by TM-OKC on the Stack Exchange Dataset</td></tr><tr><td>Topic</td><td>Most probable words</td></tr><tr><td>1</td><td>quot, charact, stori, write, reader, word, think, thing, way, peopl</td></tr><tr><td>2</td><td>cook, food, water, time, heat, temperatur, pan, oil, get, meat</td></tr><tr><td>3</td><td>team, product, work, sprint, scrum, stori, develop, agil, user, backlog</td></tr><tr><td>4</td><td>model, data, train, test, featur, valu, predict, class, learn, set</td></tr><tr><td>5</td><td>project, manag, need, work, risk, cost, time, peopl, develop, requir</td></tr><tr><td>6</td><td>recip, flour, bake, dough, egg, sugar, bread, milk, tast, flavor</td></tr><tr><td>7</td><td>problem, number, algorithm, time, sum, log, function, frac, comput, solv</td></tr><tr><td>8</td><td>languag, state, word, quot, type, machin, context, mean, accept, definit</td></tr><tr><td>9</td><td>tree, node, graph, element, edg, array, vertex, algorithm, path, number</td></tr><tr><td>10</td><td>task, time, work, day, project, hour, resourc, date, start, schedul</td></tr></table>

<table><tr><td colspan="2">Table G2. Top 10 Topics Learned by NTM on the Stack Exchange Dataset</td></tr><tr><td>Topic</td><td>Most probable words</td></tr><tr><td>1</td><td>team, project, work, scrum, sprint, time, task, need, product, process</td></tr><tr><td>2</td><td>cook, water, add, time, food, pan, oil, flour, good, need</td></tr><tr><td>3</td><td>character, reader, write, think, want, know, thing, way, need, good</td></tr><tr><td>4</td><td>quot, word, english, mean, phrase, verb, say, noun, think, know</td></tr><tr><td>5</td><td>problem, number, algorithm, time, set, sum, give, function, log, find</td></tr><tr><td>6</td><td>write, book, work, good, read, want, find, publish, page, author</td></tr><tr><td>7</td><td>model, time, algorithm, problem, need, good, way, number, case, set</td></tr><tr><td>8</td><td>model, train, test, class, quot, dataset, layer, input, set, loss</td></tr><tr><td>9</td><td>work, time, need, know, way, good, want, find, question, write</td></tr><tr><td>10</td><td>time, work, need, know, way, good, want, find, question, quot</td></tr></table>

<table><tr><td colspan="2">Table G3. Top 10 Topics Learned by TM-OKC on the Quora Dataset</td></tr><tr><td>Topic</td><td>Most probable words</td></tr><tr><td>1</td><td>time, life, peopl, get, think, good, know, thing, even, day</td></tr><tr><td>2</td><td>bitcoin, invest, market, cryptocurr, crypto, buy, coin, trade, money, ethereum</td></tr><tr><td>3</td><td>softwar, engin, work, code, develop, program, test, problem, need, job</td></tr><tr><td>4</td><td>peopl, thing, question, find, need, ask, want, know, answer, think</td></tr><tr><td>5</td><td>wear, look, woman, cloth, dress, shirt, style, girl, jean, fashion</td></tr><tr><td>6</td><td>cost, pay, countri, govern, increas, rate, inflat, high, economi, tax</td></tr><tr><td>7</td><td>god, human, differ, truth, philosophi, religion, world, analysi, exist, purpos</td></tr><tr><td>8</td><td>content, medium, websit, seo, blog, social, search, googl, page, post</td></tr><tr><td>9</td><td>busi, product, brand, custom, start, onlin, digit, servic, company, plan</td></tr><tr><td>10</td><td>weight, eat, lose, exercis, food, calori, diet, bodi, healthi, day</td></tr><tr><td colspan="2">Table G4. Top 10 Topics Learned by QATM on The Quora Dataset</td></tr><tr><td>Topic</td><td>Most probable words</td></tr><tr><td>1</td><td>bitcoin, invest, cryptocurr, crypto, ethereum, buy, market, blockchain, transact, time</td></tr><tr><td>2</td><td>time, work, softwar, know, need, way, code, someth, develop, think</td></tr><tr><td>3</td><td>wear, look, dress, tri, get, cloth, string, time, good, love</td></tr><tr><td>4</td><td>god, energi, human, object, exist, say, time, peopl, medit, self</td></tr><tr><td>5</td><td>engin, code, program, comput, softwar, problem, linguag, time, write, thing</td></tr><tr><td>6</td><td>develop, applic, busi, compani, get, work, start, need, peopl, idea</td></tr><tr><td>7</td><td>unit, peopl, implement, test, chang, mani, function, may, thing, engin</td></tr><tr><td>8</td><td>project, request, screen, video, get, creat, need, want, experi, manag</td></tr><tr><td>9</td><td>work, system, way, program, task, time, need, weight, get, lose</td></tr><tr><td>10</td><td>code, test, softwar, interview, engin, question, skill, manag, work, ask</td></tr></table>

## Appendix H

## Logic and Additional Evaluation of User Profiling

## Logic of the User Profiling Example

As illustrated in Figure 3 of the main paper, with better statistical model fit, representation capability, and interpretability, our TM-OKC can benefit many downstream tasks, which can be user-related (e.g., user profiling) or not user-related (e.g., trending topic detection). In our study, user profiling is selected as an example to demonstrate the practical utility and relative merit of TM-OKC. As elaborated in the Literature Review section of the main paper, our study aims to develop a general topic modeling framework that explicitly captures the complex structural relationships among OKC texts, thus we do not model the observed attributes of texts (e.g., authorship information) which is beyond our research focus. Note that although this user profiling example happens to be user related, that does not mean that we have to model authorship a priori because the key aim of topic models is to obtain good text representation (i.e., topic vectors), and this modeling process does not necessarily include authorship information. After deriving topic vectors from texts, different downstream tasks can use these topic vectors in their own ways. For example, here in this study, we used topic vectors to construct user profiles. This procedure actually incorporates authorship information a posteriori. Other topic models that capture authorship a priori follow the same procedure. However, this is just a downstream task, which does not impose restrictions on whether the topic model should include authorship information a priori. This is also reflected in prior research. For example, LDA, which does not model authorship information, has also been applied to construc Twitter users’ online profiles (Geva et al., 2019). In addition, although modeling authorship is beyond our research scope, we still compared our method with the state-of-the-art baseline methods that model authorship and achieved significantly better performance, through which we empirically demonstrated the importance of modeling explicit structural relationships among OKC texts and made our methodological contributions in this regard. It is worth noting that adding authorship into our framework might be able to further improve the model performance, which we leave for future research.

## Additional Evaluation

In the user profiling experiments in the Practical Value of TM-OKC section of the main paper, we followed the strategy used in prior studies to perform a similarity search in a 100-question pool randomly selected from the holdout test set (Elkahky et al., 2015; He et al., 2017). Here we also present the results using the whole holdout test set as the question pool to perform the similarity search in Tables H1 and H2. Not surprisingly, the results presented in Tables H1 and H2 are consistent with the results presented in Tables 10 and 11 in terms of the relative performance across different methods<sup>14</sup>

<table><tr><td colspan="5">Table H1: User Promising Performance Comparison of Different Methods Under a Moderate Data Size (Number of Q&amp;A Threads is 8,000)</td></tr><tr><td colspan="2" rowspan="2"></td><td colspan="3">Hit rate for top K</td></tr><tr><td>K=5</td><td>K=10</td><td>K=20</td></tr><tr><td rowspan="3">Basic text feature extraction methods</td><td>TF-IDF features (top 100 words)</td><td>0.17%</td><td>0.34%</td><td>0.63%</td></tr><tr><td>TF-IDF features (top 500 words)</td><td>0.15%</td><td>0.26%</td><td>0.52%</td></tr><tr><td>TF-IDF features (top 1000 words)</td><td>0.17%</td><td>0.27%</td><td>0.63%</td></tr><tr><td rowspan="7">Bayesian topic modeling methods</td><td>LDA</td><td>0.83%</td><td>1.92%</td><td>3.95%</td></tr><tr><td>TRTM</td><td>0.95%</td><td>2.11%</td><td>4.03%</td></tr><tr><td>STM</td><td>1.02%</td><td>2.30%</td><td>4.23%</td></tr><tr><td>QATM</td><td>1.07%</td><td>2.19%</td><td>4.11%</td></tr><tr><td>LeadLDA1</td><td>0.17%</td><td>0.31%</td><td>0.63%</td></tr><tr><td>LeadLDA2</td><td>0.19%</td><td>0.37%</td><td>0.78%</td></tr><tr><td>SITS</td><td>1.16%</td><td>2.29%</td><td>4.23%</td></tr><tr><td>Pretrained deep language models</td><td>Pretrained BERT</td><td>0.48%</td><td>0.84%</td><td>1.45%</td></tr><tr><td rowspan="2">Topic modeling combined with deep language models</td><td>NTM</td><td>0.79%</td><td>1.90%</td><td>3.39%</td></tr><tr><td>SCHOLAR</td><td>0.91%</td><td>1.98%</td><td>4.08%</td></tr><tr><td>Neural matrix factorization</td><td>NMF</td><td>0.88%</td><td>1.83%</td><td>3.90%</td></tr><tr><td>Our method</td><td>TM-OKC</td><td>1.28%**</td><td>2.55%**</td><td>4.58%**</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline method under a one-tailed t-test. \*\* $p < 0 . 0 5 , { } ^ { \star \star \star } p < 0 . 0 1 .$

Table H2. User Profiling Performance Comparison of Different Methods Under Different Data Sizes for K=10 (i.e., Top 10 Hit Rate)

<table><tr><td rowspan="2" colspan="2"></td><td colspan="7">Data size N (number of Q&amp;A threads)</td></tr><tr><td>1,000</td><td>2,000</td><td>4,000</td><td>8,000</td><td>16,000</td><td>32,000</td><td>64,000</td></tr><tr><td rowspan="3">Basic text feature extraction methods</td><td>TF-IDF features (top 100 words)</td><td>1.19%</td><td>0.73%</td><td>0.60%</td><td>0.34%</td><td>0.27%</td><td>0.17%</td><td>0.12%</td></tr><tr><td>TF-IDF features (top 500 words)</td><td>1.37%</td><td>0.80%</td><td>0.66%</td><td>0.26%</td><td>0.31%</td><td>0.20%</td><td>0.13%</td></tr><tr><td>TF-IDF features (top 1000 words)</td><td>1.37%</td><td>0.87%</td><td>0.61%</td><td>0.27%</td><td>0.24%</td><td>0.15%</td><td>0.13%</td></tr><tr><td rowspan="7">Bayesian topic modeling methods</td><td>LDA</td><td>5.13%</td><td>3.74%</td><td>2.40%</td><td>1.92%</td><td>1.37%</td><td>0.74%</td><td>0.65%</td></tr><tr><td>TRTM</td><td>5.96%</td><td>4.02%</td><td>2.54%</td><td>2.11%</td><td>1.41%</td><td>0.90%</td><td>0.72%</td></tr><tr><td>STM</td><td>6.45%</td><td>4.12%</td><td>2.53%</td><td>2.30%</td><td>1.55%</td><td>0.96%</td><td>0.79%</td></tr><tr><td>QATM</td><td>6.26%</td><td>4.30%</td><td>2.40%</td><td>2.19%</td><td>1.52%</td><td>1.05%</td><td>0.79%</td></tr><tr><td>LeadLDA1</td><td>1.31%</td><td>0.72%</td><td>0.44%</td><td>0.31%</td><td>0.19%</td><td>0.24%</td><td>0.19%</td></tr><tr><td>LeadLDA2</td><td>1.50%</td><td>0.75%</td><td>0.68%</td><td>0.37%</td><td>0.35%</td><td>0.25%</td><td>0.21%</td></tr><tr><td>SITS</td><td>5.41%</td><td>4.09%</td><td>2.69%</td><td>2.29%</td><td>1.61%</td><td>1.08%</td><td>0.79%</td></tr><tr><td>Pretrained deep language models</td><td>Pretrained BERT</td><td>2.44%</td><td>1.87%</td><td>1.06%</td><td>0.84%</td><td>0.71%</td><td>0.61%</td><td>0.59%</td></tr><tr><td rowspan="2">Topic modeling combined with deep language models</td><td>NTM</td><td>2.32%</td><td>2.22%</td><td>1.78%</td><td>1.90%</td><td>1.74%</td><td>1.28%</td><td>1.04%</td></tr><tr><td>SCHOLAR</td><td>4.82%</td><td>3.07%</td><td>2.10%</td><td>1.98%</td><td>1.77%</td><td>1.30%</td><td>1.10%</td></tr><tr><td>Neural matrix factorization</td><td>NMF</td><td>2.11%</td><td>1.97%</td><td>1.70%</td><td>1.83%</td><td>1.68%</td><td>1.23%</td><td>1.02%</td></tr><tr><td>Our method</td><td>TM-OKC</td><td>7.33%***</td><td>4.51%***</td><td>2.98%**</td><td>2.55%**</td><td>1.98%**</td><td>1.37%*</td><td>1.10%</td></tr></table>

Note: The statistical significance was calculated compared with the best baseline method under a one-tailed t-test. \* p < 0.1, \*\* p < 0.05, \*\*\* p < 0.01.
