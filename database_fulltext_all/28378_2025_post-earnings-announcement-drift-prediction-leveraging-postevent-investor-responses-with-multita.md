---
otero_id: 28378
otero_key: "BNP8AKSM"
title: "Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning"
authors: "Yu Zhu; Xiao Liu; Olivia R. Liu Sheng"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0358"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Post-Earnings-Announcement Drift Prediction: Leveraging Postevent Investor Responses with Multitask Learning

Yu Zhu,<sup>a,</sup>\* Xiao Liu,<sup>b</sup> Olivia R. Liu Sheng<sup>b</sup>

<sup>a</sup> Department of Accounting and Management Information Systems, Lerner College of Business and Economics, University of Delaware, Newark, Delaware 19173; <sup>b</sup> Department of Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, Arizona 85281

\*Corresponding author

Contact: yuzhu@udel.edu, https://orcid.org/0000-0001-8278-9989 (YZ); xiao.liu.10@asu.edu, https://orcid.org/0000-0001-8277-4701 (XL); olivia.liu.sheng@asu.edu, https://orcid.org/0000-0002-5263-2726 (ORLS)

Received: June 27, 2022 Revised: August 13, 2023; June 2, 2024 Accepted: February 26, 2025 Published Online in Articles in Advance: April 4, 2025

https://doi.org/10.1287/isre.2022.0358

Copyright: © 2025 INFORMS

Abstract. Post-earnings-announcement drift (PEAD) refers to the phenomenon in which a company’s stock price tends to drift persistently in response to the information released during the earnings announcement event. Predicting PEAD is of great interest to both investors and researchers because the magnitude of PEAD is economically significant. Whereas decades of studies have explored various approaches to forecasting PEAD, prior research has largely overlooked postevent investor responses—a critical intermediary in the PEAD mechanism—because of the limitations of single-task learning (STL). This study addresses this gap by introducing a multitask learning (MTL) framework that explicitly incorporates investor responses as auxiliary tasks while mitigating look-ahead bias. To fur ther enhance model performance, we propose GradPerp, an adaptive task weighting method that assigns greater weight to auxiliary tasks that contribute diverse and informative training signals. Our model employs a multilevel, multiquery transformer architecture to facilitate cross-task learning, effectively integrating structured financial features with lengthy earnings call transcripts. Evaluation of the model from 2010 to 2022 demonstrates that the proposed design innovations not only outperform benchmark models in terms of prediction accuracy but also generate a daily risk-adjusted return (alpha) two to three times larger than the traditional earnings surprise–based models. This study contributes to the stream of information systems (IS) literature at the intersection of artificial intelligence (AI), finance, and design science research. Our work provides valuable decision support modules and managerial implications for investment and other financial decision makers.

History: Eric Zheng, Senior Editor; Huimin Zhao, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0358.

Keywords: post-earnings-announcement drift (PEAD) • earnings call transcripts • multitask learning (MTL) • adaptive weighting method • predictive analytics • investment decision support

## 1. Introduction

The quarterly earnings announcement is one of the most important information disclosure events for public companies (Fink 2021). Extensive research has established that stock prices may respond significantly to earnings news, leading to stock price drifts potentially ranging from days to even months (Abarbanell and Bernard 1992, Meursault et al. 2021). This phenomenon is known as post-earnings-announcement drift (PEAD).

Predicting PEAD is of great interest to both investors and researchers because the magnitude of PEAD is economically significant. Lee and Zhu (2022) found that “AMF (actively managed funds) trade 170% more on earnings announcement (EA) days than on non-EA days.” Ali et al. (2020) documented that “mutual funds on average trade on the PEAD anomaly.” The “earnings surprise,” defined as the discrepancy between the actual earnings and the expected earnings, is the most widely used predictor of PEAD (Livnat and Mendenhall 2006). Trading strategies based on earnings surprises are reported to generate significant abnormal returns (ARs) (Bernard and Thomas 1989). However, because of its accessibility and extensive exploitation, recent literature suggests that the predictive power of earnings surprises on PEAD is diminishing (Chordia et al. 2009, Hung et al. 2015, Fink 2021, Martineau 2021).

A recent trend in PEAD prediction involves utilizing the unstructured content generated during earnings conference calls, commonly referred to as earnings calls, in addition to earnings surprises. A firm’s earnings call is typically conducted the same day or the day after the written earnings press release. During the one-hour call, company executives—typically the CEO and CFO— first review the past quarter’s performance in the management discussion (MD) session and then take questions from professional stock analysts in the questions & answers (QA) session. Frankel et al. (1999) argue that these earnings calls contain significantly more new information than other regularly scheduled events, like the annual 10-K statements. Multiple features extracted from the earnings calls, such as speaker sentiment and the management team’s question circumvention, have been documented as having the potential to explain PEAD (Hollander et al. 2010, Chebonenko et al. 2018). In contrast to the literature indicating a declining PEAD (Chordia et al. 2009, Hung et al. 2015, Fink 2021, Martineau 2021), Meursault et al. (2021) observed that the magnitude of PEAD is “far from disappearing” when predicted using earnings call transcripts and more advanced machine learning methods.

Although various prediction features and models have been proposed, previous studies on PEAD prediction have mostly relied on single-task learning (STL) designs (Hollander et al. 2010, Fink 2021, Meursault et al. 2021). STL models predict a single outcome variable, namely, PEAD. The performance gain is achieved through either enhanced model inputs or a refined learning algorithm. However, STL may not be the most effective learning framework for PEAD prediction because it cannot leverage an important intermediary of the PEAD mechanism: the postevent investor responses. After the release of earnings news, investors respond by updating their beliefs and trading accordingly (Livnat and Mendenhall 2006), which pushes prices to new levels. Whereas today’s investors respond to earnings news very quickly, because of the heterogeneity of their responses, the resulting impact on the stock price may take time to fully reveal itself. Therefore, postevent investor responses serve as an intermediary step connecting the earnings event and the eventual stock price drift, making postevent investor responses potentially valuable data for an effective PEAD prediction framework. Unfortunately, gathering postevent investor responses entails a time lag ranging from days to months, whereas a PEAD model must provide predictions immediately after an earnings event in order to avoid missing crucial trading opportunities. As a result, it is infeasible for STL models to leverage postevent investor responses as model inputs, significantly limiting their power.

In contrast, multitask learning (MTL) offers a promising alternative research paradigm for PEAD prediction, as it circumvents the above-mentioned issues of STL through its unique mechanism of auxiliary tasks. In MTL, the primary task (PEAD in this study) is jointly predicted with postevent investor responses, which serve as additional model outputs known as “auxiliary tasks.” Compared with STL, MTL offers three advantages for PEAD prediction. First and foremost, when used as auxiliary tasks, the postevent investor responses provide new training signals (inductive biases) for the model (Caruana 1997), thereby enhancing the model’s generalizability even when using the same inputs as an STL model. As with humans, jointly learning a set of related tasks can be preferable to learning them independently, as the representations learned from one task can benefit other tasks. Second, MTL allows for timely predictions, as it no longer needs to wait for the collection of postevent investor responses because these responses are not used as model inputs. Third, postevent responses can serve as shortcuts to the challenging PEAD prediction task. We find that postevent responses are related to PEAD but are relatively easier to predict. As a result, the learning of these easier tasks can benefit the learning of the more challenging PEAD task, a phenomenon known as the eavesdropping effect (Caruana 1997).

This study explores design and method innovations to leverage MTL and earnings call transcripts for PEAD prediction. Specifically, we address three key questions related to MTL design strategies. The first question asks how to select appropriate auxiliary tasks. Auxiliary tasks are critical to the effectiveness of an MTL model because they provide the model with domain-specific training signals as inductive bias (Caruana 1997). However, except for the common recognition that auxiliary tasks should be related to the primary task, no clear guidance exists regarding the selection of auxiliary tasks. In this study, we identified three types of market participants (stock analysts, institutional investors, and retail investors) whose postevent responses serve as effective auxiliary tasks because of their pivotal role as intermediaries in the PEAD mechanism. We name this set of auxiliary tasks FinAux.

The second question asks how to assign proper weights (hereafter “task weights”) to the task losses in the MTL objective function. The MTL objective function is often a linea combination of losses from the primary and auxiliary tasks. Because the training signals provided by each task may not be equally helpful, carefully choosing the task weights is as essential to an MTL model as the selection of auxiliary tasks. Recent work has proposed vari ous adaptive task weighting methods, which treat task weights as learnable parameters, avoiding the expensive computational cost of a grid search (Chen et al. 2018, Du et al. 2018, Lin et al. 2019, Jha et al. 2020).<sup>1</sup> However, extant adaptive weighting methods prioritize convergence speed over learning generalizability (Lin et al. 2019), resulting in potentially suboptimal results. Our study proposes a new, gradient-based adaptive weighting method, GradPerp. The key idea behind GradPerp is that in order to enhance generalizability, it is more beneficial to learn from diverse training signals than from similar ones. In cases where two auxiliary tasks offer comparable training signals, GradPerp assigns a relatively smaller weight to one of them.

The third question asks how to design a neural network architecture to effectively learn representations from th lengthy earnings call transcripts and combine them with other structured features. Our proposed innovations in MTL, namely, FinAux and GradPerp, work on the objective function and can be paired with many underlying neural network architectures. In this paper, we choose the multiquery transformer (MQT) (Xu et al. 2023b) architecture. The MQT generates one query matrix for each task as a proxy for task-related context, facilitating the learning of task-specific features through the cross-task attention module. We integrate the proposed auxiliary tasks (FinAux) and adaptive weighting method (GradPerp) into the MQT architecture. Because prior literature indicates that the MD and QA sessions of an earnings call are notably distinct in nature (Hollander et al. 2010), our architecture generates separate embedding representations from the calls’ MD and QA sessions. Furthermore, the proposed architecture includes a module, structured feature enhancer (SFE), to improve the learning of structured features.

We evaluate the proposed method for PEAD prediction from 2010 to 2022 with 61,223 quarterly earnings calls from Russell 3000 stocks. Our evaluation includes both prediction performance evaluation and economic significance evaluation. Our findings demonstrate that a well-chosen set of auxiliary tasks and a proper task weighting method not only improve the prediction performance of PEAD but also lead to greater economic return.

Our work contributes to the interdisciplinary research of artificial intelligence (AI) and finance. Differing from prior MTL studies in information systems (IS) literature—which have primarily focused on developing models for cross-task knowledge sharing (Lin et al. 2017, Yu et al. 2022)—this study emphasizes auxiliary task selection and proper task weighting in the MTL objective function. Notably, we underscore the significance of domain knowledge in the search for diverse, relevant training signals, and we also highlight the importance of an innovative adaptive task weighting method to more effectively leverage these training signals. Our work expands the existing literature on finance and MTL within IS research and beyond, offering insights into innovative MTL design strategies in an effort to unlock the potential of AI in finance.

## 2. Literature Review

Our study is closely related to two research streams: (1) PEAD prediction, and (2) MTL. In the following subsections, we review representative studies from each stream and discuss the research gap this study fills.

## 2.1. PEAD Prediction

2.1.1. Measuring PEAD. PEAD is commonly measured as cumulative abnormal return (CAR) (Livnat and Mendenhall 2006, Francis et al. 2007, Kim et al. 2019,

Meursault et al. 2021) or buy-and-hold abnormal return (BHAR) (Martineau 2021); both are calculated by subtracting an “expected return” from the raw return.<sup>2</sup> Given a stock’s risk characteristics such as its size or book-to-market ratio, the expected return estimates the stock’s return if the earnings event had not occurred (MacKinlay 1997). The difference between the raw return and the expected return is defined as abnormal return, representing the impact on the stock price solely attributed to the earnings event. Because expected returns have captured the risk characteristics of the stock, the resulting abnormal returns are considered risk adjusted and are hence comparable across different stocks and market conditions. This comparability is crucial to investment practices because it ensures that investment decisions have fully taken account of the varying risk levels of stocks and market conditions (Feibel 2003). CAR and BHAR measure the aggregated abnormal return over a certain period following the earnings event, with the aggregation horizon varying from days to months, depending on the research context. CAR and BHAR differ in how they aggregate the abnormal returns. CAR first computes the daily AR and then aggregates over the desired horizon, whereas BHAR first calculates the raw return and expected return over the entire horizon and then takes their dif ference. Following the extensive adoption of CAR in finance literature (Francis et al. 2007, Tetlock et al. 2008, Doran et al. 2010, Lee 2016), we measure PEAD with CAR in this study.

2.1.2. Earnings Surprises and PEAD. Traditionally, PEAD has been predicted using a regression-based method with structured accounting figures. The earnings surprise is the most widely known predictor of PEAD (Livnat and Mendenhall 2006). Initially documented by Ball and Brown (1968), the association between earnings surprises and subsequent stock price drift has been one of the most robust and persistent anomalies challenging the efficient market paradigm, and trading strategies based on earnings surprises are reported to yield economically significant returns (Bernard and Thomas 1989). However, in recent years, a stream of studies have suggested that PEAD is disappearing (Chordia et al. 2009, Fink 2021, Martineau 2021). These disappearing PEAD studies differ from ours in three critical aspects. First, these disappearing PEAD studies are mostly explanatory in nature and solely use earnings surprises as an explanatory variable of PEAD under a linear regression setting. Because of the heavy media coverage of and easy access to data on earnings surprises, these studies found that the earnings surprise is no longer statistically significant in explaining PEAD, hence their claim that PEAD has vanished. In contrast, our work is predictive in nature, with the goal of improving PEAD prediction performance instead of examining the causal relationship between PEAD and a particular variable of interest. Second, in addition to earnings surprises, our study also utilizes earnings call transcripts and other financial ratios as predictors. Third, we no longer use linear regression; instead, we use a transformer-based, multitask learning neural network to process the textual and structural features in order to better predict PEAD. Because of these differences, we found that PEAD remains a profitable strategy.

2.1.3. Leveraging Earnings Call Transcripts. Recognizing the limitations of relying solely on structured accounting figures, researchers have diverted their attention to unstructured earnings call transcripts. Many financial studies have proposed a variety of manually crafted features based on earnings call transcripts, with sentiment (Doran et al. 2010) and management spontaneity (e.g., managers with bad news are less spontaneous in responding to analysts’ questions) (Hollander et al. 2010, Lee 2016) among the most popular. With the advancement of machine learning, particularly deep learning, novel approaches to predicting PEAD have emerged. These studies found that PEAD continues to exist and be economically meaningful (Ma et al. 2020, Meursault et al. 2021). For instance, Meursault et al. (2021) introduced PEAD.txt, a PEAD prediction model based on earnings call transcripts, and evaluated it over the 2010–2019 period. They observed that the riskadjusted return of a PEAD.txt strategy is 50% larger than that of the traditional earnings surprise–based strategy, asserting “PEAD is far from disappearing.”

## 2.1.4. Evaluating the Economic Significance of PEAD.

In addition to prediction performance, prior studies have employed two representative approaches when examining the economic significance of a PEAD prediction model: visualizing the realized PEAD (Martineau 2021, Meursault et al. 2021) and computing the excess return (alpha) (Chordia et al. 2009, Meursault et al. 2021). To visualize the realized PEAD, prior work sorts stocks according to the predicted PEAD, typically into quintiles. Then, the average realized PEAD of each quintile group is plotted as a curve of CAR(0, T), where T represents the number of trading days since the earnings event. An economically significant prediction model is indicated by a clear separation in the realized PEAD curves, with the top quintile significantly drifting above zero and the bottom quintile significantly drifting below zero. Some studies also plot the difference curve between the top and bottom PEAD quintile as the real ized PEAD in order to mimic a long-short strategy (Meursault et al. 2021). To compute alpha, most studies construct a portfolio by selecting stocks based on the predicted PEAD. The portfolio’s returns are then regressed on a set of risk factors, where each coefficient represents the portfolio’s exposure to a specific type of risk. An intercept term (alpha) significantly different from zero indicates that the portfolio’s return cannot be fully explained by the risks it has taken, implying out- or underperformance. In finance, a positive, statistically significant alpha is considered to be good, as it indicates that the portfolio is able to generate a return in excess of its risk-adjusted expectation (Carhart 1997).

## 2.2. Multitask Learning

In this section, we review three important aspects of a deep learning MTL model: (1) how to select auxiliary tasks, (2) how to judiciously determine the weights across tasks in the objective function, and (3) how to select the proper neural network architecture to enable cross-task parameter sharing.

2.2.1. MTL Auxiliary Task Selection. The auxiliary tasks must exhibit a degree of correlation with the primary task while avoiding excess similarity, ensuring that they provide helpful training signals. Table 1 below surveys the MTL literature and categorizes effective auxiliary tasks into four types. Notably, we observed that the boundaries between these categories can often be blurred in practice. Consequently, Table 1 should be viewed more as a guideline for identifying auxiliary tasks from various perspectives, rather than as a mutually exclusive taxonomy.

2.2.2. Homogeneous Tasks. Homogeneous auxiliary tasks are different measurements of the primary task. For example, in psychology, leadership can be evaluated by self-administered questionnaires, peer questionnaires, or external observations. Beyan et al. (2017) proposed a leadership identification model that jointly predicts the three leadership measurements. Similarly, Yang et al. (2020) simultaneously predict 3-, 5-, 7-, 15-, and 30-day stock price volatilities.

Table 1. Types of Auxiliary Tasks

<table><tr><td>Type of auxiliary tasks</td><td>Explanation</td><td>Example studies</td></tr><tr><td>Homogeneous tasks</td><td>Different measurements of the primary task</td><td>Beyan et al. (2017), Yang et al. (2020)</td></tr><tr><td>Future information</td><td>Information that comes after the ground truth of the primary task is available</td><td>Caruana et al. (1996)</td></tr><tr><td>Intermediary steps</td><td>Intermediary steps whose data come after the model inputs but before the ground truth of the primary task is available</td><td>Wang et al. (2018), Kuang et al. (2019)</td></tr><tr><td>Related properties</td><td>Different yet related properties of the entity associated with the primary task</td><td>Lin et al. (2017), Yu et al. (2022)</td></tr></table>

2.2.3. Future Information. One unique advantage of MTL is that it can leverage “future information.” In many prediction tasks, useful predictors are inaccessible because they are generated after the prediction target. For example, doctors often need to determine whether a patient needs hospitalization before laboratory test results are available. Caruana et al. (1996) developed an MTL model to predict a patient’s hospital admission using the patient’s pending laboratory test results as auxiliary tasks.

2.2.4. Intermediary Steps. Some MTL studies utilize the intermediary steps leading to the target variable as auxiliary tasks. In a taxi pick-up demand prediction problem, Kuang et al. (2019) used the drop-off demand as the auxiliary task to predict taxi pick-up demand because drop-offs lead to potential pick-ups. Wang et al. (2018) investigated how to better compress long product titles to fit into the limited space on a mobile device. Given the original product title, their model not only outputs a shorter title but also predicts the original user query that leads to the product. Wang et al. (2018) found that using user query as the auxiliary task helps the model learn what keywords most attract customers.

2.2.5. Related Properties. An entity associated with the primary task may have multiple properties. Each of these properties captures unique information about the entity and thus can be used as an auxiliary task. Based on the observation that a patient with chronic disease is likely to experience other adverse health events, Lin et al. (2017) added acute renal failure as an auxiliary task to a stroke prediction model for patients with chronic diseases. Similarly, Yu et al. (2022) jointly predicted different aspects of a patient’s chronic conditions to achieve better generalizability. In computer vision, the class and depth of an image are often jointly predicted (Kendall et al. 2018). In natural language processing (NLP), Isonuma et al. (2017) found that predicting the type of a news article (e.g., sports, finance, or politics) as an auxiliary task can improve the performance of text summarization.

The auxiliary task selection in extant MTL literature has two limitations. First, although all of the auxiliary task types in Table 1 could complement one another, researchers often use only one type of these auxiliary task types in their MTL design. Second, auxiliary task selection in prior studies is largely heuristic and empirical, lacking a comprehensive investigation of related domain knowledge. We posit that the selection of auxil iary tasks should rely on domain knowledge, as it provides valuable insights into the relationships between the auxiliary tasks and the primary task.

2.2.6. MTL Adaptive Task Weighting. After selecting the auxiliary tasks, the next question is how to properly join them into a single objective function. The conventional approach is to derive a total loss function that linearly combines the losses of all tasks (Caruana 1998, Zhang and Yang 2021). The weight of a task represents the extent to which a learning method prioritizes this task. Many studies treat task weights as fixed hyperparameters (Yang et al. 2020, Yu et al. 2022), with some manually tuning them using grid search. Such an approach, however, becomes infeasible because the search space increases exponentially with the number of tasks. To overcome this limitation, researchers propose adaptive task weighting methods, which treat task weights as learnable parameters of the model. Table 2 summarizes two major categories of adaptive weighting methods.

2.2.7. Adaptive Weighting Methods with No Task Preference. These are the scenarios where all the tasks are equally important to the end user. Hence, there are no distinctions between the primary and auxiliary tasks. In this case, an adaptive weighting method attempts to balance task weights: if one task dominates (or is dominated) during the training, then its weight is reduced (or increased). Different measures of task dominance lead to variations in methods, with common criteria including the magnitude of task losses (Liu et al. 2019), the gradient of task losses (Chen et al. 2018, Jha et al. 2020), and uncertainty (Kendall et al. 2018). This study, however, does not balance between tasks, as we are only interested in the performance of the primary task (PEAD).

Table 2. Adaptive Task Weighting Methods

<table><tr><td>Category</td><td>Method</td><td>Description</td><td>Example studies</td></tr><tr><td rowspan="3">No task preference</td><td>Loss based</td><td>The descending speed of the task loss determines its weight</td><td>DWA (Liu et al. 2019)</td></tr><tr><td>Gradient based (magnitude)</td><td>The magnitude of the task-specific gradient determines its task weight</td><td>GradNorm (Chen et al. 2018) AdaMT (Jha et al. 2020)</td></tr><tr><td>Uncertainty based</td><td>The uncertainty (prediction difficulty) of the task determines its weight</td><td>Uncertainty (Kendall et al. 2018)</td></tr><tr><td rowspan="2">Primary task preference</td><td>Gradient based (similarity)</td><td>Auxiliary tasks whose gradient is similar to that of the primary task are assigned a large weight</td><td>GradCos (Du et al. 2018) OlAux (Lin et al. 2019)</td></tr><tr><td>Gradient based (diverse training signals)</td><td>Auxiliary tasks that provide diverse training signals have a large weight</td><td>GradPerp (this study)</td></tr></table>

2.2.8. Adaptive Weighting Methods That Prefer the Primary Tasks. These are the scenarios where the purpose of the auxiliary tasks is to facilitate the learning of the primary task. Our study falls into this category. To effectively utilize the training signals contained in the auxiliary tasks, the adaptive weighting method must quantify the contribution of each auxiliary task to the primary task. A commonly used approach is based on gradient. Because most neural networks are trained using gradient descent, each task (either primary or auxiliary) will generate a task-specific gradient during training, which is the derivative of the task loss with respect to model parameters.<sup>3</sup> As a result, task gradients represent the training signals inherent in each task. Most extant literature measures the contribution of an auxiliary task by computing the similarity between its task gradient and that of the primary task (Du et al. 2018, Lin et al. 2019), where a stronger similarity leads to a larger weight. The rationale behind this approach is that when an auxiliary task produces a gradient akin to that of the primary task, it reinforces and accelerates the convergence of the primary task.

However, a fast convergence of the primary task does not necessarily lead to better generalizability (LeCun 1989). Many machine learning algorithms, such as SVM and LASSO, add regularizers or constraints that may slow a model’s convergence yet result in better generalizability. We posit that a model’s generalizability is enhanced when it can learn from a diverse set of auxiliary tasks whose gradients (training signals) are dissimilar to each other. To this end, we introduce a novel adaptive weighting method named GradPerp. Grad-Perp performs QR matrix decomposition (Trefethen and Bau 1997) on the task gradients, breaking down each task gradient into the portion that can be linearly explained by other task gradients and the residual portion that cannot. GradPerp places large weights on auxiliary tasks whose gradients are unique and not well explained by other tasks.

2.2.9. MTL Learning Architecture. Selecting the auxiliary tasks and determining the task weights, as previously discussed, works on the MTL objective function. The MTL learning architecture reviewed in this subsection focuses on the underlying deep neural networks that can be paired with the MTL objective function. A good MTL learning architecture typically enables parameter sharing, where model parameters from one task aid in learning parameters for another task (Zhang and Yang 2021). For non-deep-learning MTL models, parameter-sharing methods include low rank (Yang and Hospedales 2016), task clustering (Jacob et al. 2008), task relation learning (Bonilla et al. 2007), and parameter matrix decomposition (Jalali et al. 2010).

In deep learning–based MTL models, parameter shar ing often involves a shared encoder that first learns features from the inputs. Then, multiple task-specific decoders utilize the learned features to make a predic tion for each task. To enable cross-task learning, some studies design the parameters of different task-specific decoders to interact with one another during training (Vandenhende et al. 2020, Bru¨ ggemann et al. 2021, Bhattacharjee et al. 2022). However, this approach can be memory consuming and computationally expensive because the number of task-specific decoders grows lin early with the number of tasks. This problem has become more pronounced as recent MTL studies in NLP and computer vision have adopted large transformers as the encoders and decoders (Xu et al. 2022). To reduce memory and computation requirements while retaining the benefits of the transformer architecture, query-based MTL transformers are introduced (Carion et al. 2020; Xu et al. 2023a, b). Instead of requiring a separate decoder for each task, a query-based transformer employs a single shared decoder while generating mul tiple task-specific queries to capture task-related contexts. These task-specific queries interact with each other via the attention mechanism, enhancing generaliz ability without significantly increasing the model size (Xu et al. 2023b). In this study, we employ the multiquery transformer (Xu et al. 2023b) as the underlying neu ral network architecture.

Many deep learning–based studies adopt a multilevel approach to learn features from lengthy earnings call transcripts. The neural network first learns sentence-level representations, which are subsequently aggregated into a document-level representation for the final PEAD prediction (Yang et al. 2020, 2023). Additionally, an MTL model often has both structured (e.g., financial ratios) and unstructured (e.g., earnings call transcripts) inputs, with the latter transformed into a numeric representation (embedding) by the neural network. The conventional approach to combining the learned embeddings with the unstructured features is through concatenation (Cheng et al. 2016). However, this approach may mask the learning from structured features because the structured features are often significantly outnumbered by the learned embeddings. In this study, we propose a structured feature enhancer to address this issue.

## 3. MTL Architecture for PEAD Prediction 3.1. Problem Definition

Let $s _ { i , q }$ denote an earnings call transcript from firm i at quarter q. Later, we will drop the quarter index q to avoid cluttering because the inputs and outputs for one training sample are all associated with the same quarter. We differentiate an earnings call’s MD and QA sessions, denoting them as $s _ { i , q } ^ { M D }$ and $s _ { i , q } ^ { Q A }$ . Thus, the unstructured inputs of the model are $X _ { i , q } ^ { U n s t r } = ( s _ { i , q } ^ { M D } , s _ { i , q } ^ { Q A } )$ The model inputs also include F structured features $X _ { i , q } ^ { S t r } = ( x _ { i , q , 1 } ^ { S t r } , \cdot \cdot \cdot , x _ { i , q , F } ^ { S t r } )$ . These F structured features contain useful financial ratios and other manual textual features documented in the literature. The primary prediction target is PEAD. Our goal is to find a model $f _ { \theta } ( X _ { i , q } ^ { U n s t r } , X _ { i , q } ^ { \Breve { S } t r } )$ that jointly predicts PEAD and K auxiliary tasks, which we denote as $( A u x _ { 1 } , \ldots , A u x _ { K } )$ . θ represents learnable parameters of f . At training step τ, the objective function in Equation (1) minimizes the weighted sum of the primary task loss and the auxiliary task losses:

$$
\begin{array}{l} \min _ {\theta} \mathcal {L} _ {t o t a l} (\theta , \tau) = \lambda_ {p r i} (\theta , \tau) \cdot \mathcal {L} _ {p r i} (\theta , \tau) \\ \qquad + \sum_ {k = 1} ^ {K} \lambda_ {a u x, k} (\theta , \tau) \cdot \mathcal {L} _ {a u x, k} (\theta , \tau), \end{array}\tag{1}
$$

where $\lambda _ { p r i }$ and $\lambda _ { a u x , k }$ are weights for the losses of the primary task and the k-th auxiliary task. We normalize task weights to ensure $\begin{array} { r } { \lambda _ { p r i } + \sum _ { k } \overset { \cdot } { \lambda _ { a u x , k } } = 1 } \end{array}$ at each training step. The task weights $\lambda _ { p r i }$ and $\lambda _ { a u x , k }$ are learnable parameters of the model. Although we optimize for the weighted sum of the primary task loss and the auxiliary task loss, the evaluation is only conducted on the primary task.

## 3.2. The Multilevel, Multiquery Transformer-Based MTL Architecture

Figure 1 illustrates the components of the proposed MTL architecture for PEAD prediction. A sentence transformer (Reimers and Gurevych 2019) and an MQT are employed to learn sentence- and document-level representations from the MD and QA texts. Additionally, an SFE is introduced to enhance the learning of structured features before their fusion with the representations derived from the earnings call transcripts. The objective function is a linear combination of the losses from the primary task and the proposed auxiliary tasks, whose task weights are determined by GradPerp, the proposed adaptive weighting method. The complete model is denoted as FinAux + GradPerp + MQT. We use index i to denote a stock, and we drop the quarter index q to avoid notation cluttering.

3.2.1. Input Level. At the input level, the unstructured input $X _ { i } ^ { U n s t r }$ , which is the transcript text, is split into the MD and QA sessions, $X _ { i } ^ { U n s t r } = ( s _ { i } ^ { M D } , ~ s _ { i } ^ { Q A } )$ . We process MD and QA separately because of their differential patterns and predictive power (Price et al. 2012). We further split $\pmb { s } _ { i } ^ { M D }$ and $s _ { i } ^ { Q A }$ into two sets of sentences, $\pmb { s } _ { i } ^ { t y p e } = \big ( s _ { i , 1 } ^ { t y p e } , \ldots , s _ { i , N _ { i } } ^ { t y p e } \big )$ , where $N _ { i }$ represents the number of sentences in the type session of earnings call $i ,$ $t y p e \in \{ M D , Q A \}$ }. The structured inputs $X _ { i } ^ { S t r }$ will be processed by another module at a later stage.

3.2.2. Sentence Level. A shared sentence encoder generates a vector representation for each sentence. We adopted $\mathrm { M P N e t } , ^ { 4 }$ a variant of sentence transformer (Reimers and Gurevych 2019), as the sentence encoder based on empirical tests of various candidates (Online Appendix A details candidate sentence encoders and their impact on prediction performance). For computational efficiency, each sentence is encoded independently. As a result, the sentence encoder will not use information from sentence a when it encodes sentence b. The intersentence information will be learned at the next level. Let $e _ { i } ^ { { \cal M } { \cal D } }$ and $e _ { i } ^ { Q A }$ be the collection of resulting sentence embeddings for the MD and QA sessions for stock i (the dimension of each sentence embedding is 768, which is determined by the sentence encoder):

$$
\begin{array}{c} \boldsymbol {e} _ {i} ^ {\text {type}} = (e _ {i, 1} ^ {\text {type}}, \ldots , e _ {i, N _ {i}} ^ {\text {type}}) = S e n t E n c o d e r (s _ {i, 1} ^ {\text {type}}, \ldots , s _ {i, N _ {i}} ^ {\text {type}}), \\ \forall \text {type} \in \{M D, Q A \}. \end{array}\tag{2}
$$

3.2.3. Document Level. At the document level, two document encoders, one for each of the MD and QA ses sions, encode the sentences from the corresponding session into a document-level embedding for each task. Each document encoder is an MQT, which is reported to achieve state-of-the-art performance without significantly increasing model size (Xu et al. 2023b). For each of the primary and auxiliary tasks, a single query (a onedimensional embedding) is initialized to capture taskspecific context. These task queries interact through the attention mechanism, enabling the MQT to generate distinct representations tailored to each task. The length of each query vector is set to 256. Further details about the MQT architecture are provided in Online Appendix B. The outputs of each of the two MQT encoders are $K + 1$ document-level embeddings denoted as $d _ { i , j } ^ { t y p e }$ , where type $\in \{ M D , Q A \}$ and $j \in \{ p r i , a u x _ { 1 } , \ldots , a u x _ { K } \}$ The dimension of a document-level embedding is 768, the same as that of a sentence-level embedding. Equation (3) details the process:

$$
\begin{array}{r l} \boldsymbol {d} _ {i, j} ^ {\text {type}} & = D o c E n c o d e r ^ {\text {type}} \big (e _ {i, 1} ^ {\text {type}}, \ldots , e _ {i, N _ {i}} ^ {\text {type}} \big), \\ & \forall \text {type} \in \{M D, Q A \}, j \in \{p r i, a u x _ {1}, \ldots , a u x _ {K} \}. \end{array}\tag{3}
$$

3.2.4. Combining with Structured Features. We combine $d _ { i , j } ^ { { M D } }$ and $d _ { i , j } ^ { \bigcirc \overline { { A } } }$ with structured features $X _ { i } ^ { S t r }$ . Whereas a simple concatenation of feature vectors is popular in the literature (Cheng et al. 2016), it may hurt performance because of the mismatch of the features’ importance and dimensionality. With only 16 structured features collected from the literature compared with the 1,536 (768 × 2) features learned from the transcripts, a simple concatenation may mask contributions from the structured features because they are significantly outnumbered by the text embedding. To facilitate effective learning from the structured features, we introduce a structured feature enhancer. The SFE first projects the 16 structured features into 256 dimensions, followed by a ReLU activation. The upscaled structured features are then concatenated with the text embeddings. We empirically tested different dimension sizes and found that 256 dimensions resulted in the best performance. We denote the enhanced structured features of firm i as $X _ { i } ^ { S t r \_ e n h a n c e d }$

Figure 1. (Color online) The Multilevel MTL Architecture for PEAD Prediction  
![](/api/attachments/BNP8AKSM/fulltext/images/5df3d8630618e4ae827c801488523e57a75bef28594f5956028606a2bec83077.jpg)

$$
\mathbf {X} _ {i} ^ {\text { Str\_enhanced }} = \text { StructuredFeatureEnhancer } \left(\mathbf {X} _ {i} ^ {\text { Str }}\right).\tag{4}
$$

The final features used by the next level are a concatenation of the document-level text embeddings and enhanced structured features, with a dimension of 768 × 2 + 256 � 1,792:

$$
\boldsymbol {X} _ {i, j} = \left(\boldsymbol {d} _ {i, j} ^ {M D}, \boldsymbol {d} _ {i, j} ^ {Q A}, \boldsymbol {X} _ {i} ^ {\text { Str\_enhanced }}\right) \forall j \in \{p r i, a u x _ {1}, \dots , a u x _ {K} \}.\tag{5}
$$

3.2.5. Prediction Level. The final level is a collection of K + 1 independent linear projection layers, one for each of the primary and auxiliary tasks.

## 3.3. Measuring PEAD

Based on prior PEAD literature (Livnat and Mendenhall 2006, Francis et al. 2007, Kim et al. 2019, Meursault et al. 2021), we select CAR as the measure of PEAD to ensure a proper risk adjustment of stock returns. CAR is calculated by subtracting the stock’s expected return (Ret<sup>e</sup>) from its daily raw return (Ret), followed by aggregation over a specified interval, as shown in Equation (6):

$$
C A R (0, 2 1) = \sum_ {t = 0} ^ {2 1} (R e t _ {t} - R e t _ {t} ^ {e}) = \sum_ {t = 0} ^ {2 1} A R _ {t},\tag{6}
$$

where t denotes a trading day, with day 0 being the earnings call day. Conceptually, the expected return Ret<sup>e</sup> is the hypothetical return that the stock would have yielded if the earnings event had not occurred (MacKinlay 1997). By subtracting $R e t ^ { e }$ from Ret, the resulting $A R _ { t }$ is supposed to only capture the part of the stock return that is solely attributed to the earnings call event. Directly predicting CAR also encourages the model to laser focus on the event-specific information from the earnings call. We use the “five characteristics” (C5) model to estimate $R e t _ { t } ^ { e }$ because it is documented to better capture the expected return in various corporate events (Bessembinder et al. 2019). The five risk characteristics include firm size, book-to-market ratio, profitability, firm investment, and price momentum. In Online Appendix C, we provide a detailed introduction to the C5 model and high light its advantages over other alternative models such as the Fama-French three-factor model. Additionally, we measure PEAD using BHAR as an alternative, which is also presented in Online Appendix C. We use 21 trading days (approximately one calendar month) as the CAR horizon, striking a balance between ensuring an adequate horizon length to capture the full effect of PEAD— as the literature suggests that PEAD could persist for months (Livnat and Mendenhall 2006)—and avoiding an excessive horizon length, which can degrade prediction performance. We considered different horizon lengths, including 42 (two months) and 63 (three months) trading days, but we found that the model trained for CAR over 21 trading days performs the best. Online Appendix D provides a detailed discussion.

## 3.4. Selecting Auxiliary Tasks

To address the literature gap in auxiliary task selection, we employ two synergistic principles: (1) a thorough examination of the drivers behind the PEAD mechanism is valuable in suggesting auxiliary tasks, and (2) diverse auxiliary tasks can further help a predictive model learn complementary training signals. Table 3 summarizes the selected auxiliary tasks. We name them FinAux.

3.4.1. Market Responses. This group of auxiliary tasks, previously unexplored in PEAD literature, is derived through a thorough examination of the PEAD mechanism. Figure 2 illustrates this process. As shown in Figure 2, at day t, an earnings call takes place, and a surprise is formed when the released information deviates from expectations. As investors gradually recognize and respond to this surprise, the stock price is pushed to a new value at t + ∆t. An STL model (Figure 2(a)) takes all data available at day t as inputs in order to predict prices at t + ∆t. However, investors’ post-earningsevent responses, which serve as a crucial intermediary step connecting the earnings event and the following price movement, cannot be leveraged by an STL model. This is because investors require the model to make timely decisions at day t to avoid missing trading opportunities, whereas postevent responses take days or months to collect. In contrast, an MTL model (Figure 2(b)) is able to utilize postevent investor responses by treating them as auxiliary model outputs rather than inputs. This enhances the model’s generalizability because postevent responses offer additional training signals to the model.

In this study, we leverage postevent responses from three representative types of market participants. The first type consists of stock analysts who react to the earnings event by revising their forecasts. Because stock analysts’ career success relies on whether they can make timely and accurate forecasts, they are highly motivated to make timely revisions. These forecast revisions are widely used as indicators of market opinion change and often influence stock prices (Abarbanell and Bernard 1992). To capture this aspect, we propose the use of analyst forecast revision (Revision) as our first auxiliary task. Let $\Delta f o r e c a s t _ { i , j , q }$ denote the change in analyst $\dot { j } ^ { \prime } \mathrm { s }$ year-end earnings forecast for stock i over the following month after the earnings call on quarter $q .$ The forecast revision of stock i in quarter q is defined as the median of revisions made by all ana lysts, normalized by the stock price on the day prior to the earnings call $P _ { i , q } ,$

$$
R e v i s i o n _ {i, q} = \frac {m e d i a n (\Delta f o r e c a s t _ {i , j , q})}{P _ {i , q}}.\tag{7}
$$

Institutional investors are the second type of market participant. They hold approximately 70%–80% of the U.S. stock market value, making them crucial players with a significant impact on stock prices (Keswani and Stolin 2008). We use two data sources to capture the behavior of institutional investors. The first source is the Thomson/Refinitiv 13F database, which records the transactions and holdings of institutions with an asset under management of over \$100 million, as mandated by the SEC. We use net money inflow (InstInflow) to proxy institutional investors’ responses.

$$
I n s t I n f l o w _ {i, q} = \sum_ {j} \Delta p o s i t i o n _ {i, j, q},\tag{8}
$$

where ∆position $\cdot _ { i , j , q }$ denotes institution $j ^ { \prime } \mathbf { s }$ dollar-value change in its position of stock i made in the following three months after quarter $q ^ { \prime } \mathbf { s }$ earnings call.<sup>5</sup> A positive (negative) InstInflow indicates that the institutions are net buyers (sellers) of the stock, likely pushing the stock price upward (downward).

Given concerns about potential data quality issues with the Thomson/Refinitiv 13F database,<sup>6</sup> we also incorporate data from the CRSP Mutual Fund

Table 3. Auxiliary Tasks (FinAux)

<table><tr><td>Auxiliary tasks</td><td>Description</td><td>Type</td></tr><tr><td>Revision</td><td>Stock analyst forecast revision</td><td>Postevent investor responses</td></tr><tr><td>FundInflow</td><td>Mutual fund net money inflow</td><td></td></tr><tr><td>InstInflow</td><td>Institutional investors&#x27; net money inflow</td><td></td></tr><tr><td>RetailInflow</td><td>Retail investors&#x27; net money inflow</td><td></td></tr><tr><td>CAR(0,0)</td><td>Cumulative abnormal returns</td><td>CAR of different horizons</td></tr><tr><td>CAR(0,3)</td><td></td><td></td></tr></table>

Figure 2. From Earnings News to Price Movement  
![](/api/attachments/BNP8AKSM/fulltext/images/778ff1daf8b86906d9a9d9af3b9cd07ba58aa3d0873e315fbfd7e32b3019a8e8.jpg)  
At day t, the earnings news is released. As investors recognize and respond to this surprise, the stock price is pushed to a new value at t + Δt.

Panel A (STL): An STL model takes all data available at day t as inputs to predict price at $t + \Delta t$ . However, investors'post-earnings event responses, which are a critical intermediary of PEAD, cannot be leveraged by an STL model. This is because investors need to make timely decisions at day t to avoid missing trading opportunities, whereas post-event responses take days or months to collect

Panel B (MTL): In contrast, an MTL model is able to utilize post-event investor responses by treating them as auxiliary mode outputs rather than inputs. This enhances the model's generalizability because post-event responses offer additional training signals to the model.

Database,<sup>7</sup> which is known for its high quality, even though it primarily focuses on mutual funds. As of 2021, mutual funds have a combined 21.3 trillion USD in total net assets,<sup>8</sup> making them one of the most important types of institutional investors. Similar to InstInflow, we use FundInflow to denote the net money inflow from mutual funds, defined as

$$
F u n d I n f l o w _ {i, q} = \sum_ {j} \Delta p o s i t i o n _ {i, j, q},\tag{9}
$$

where ∆position denotes the dollar-value change in $\cdot _ { i , j , q }$ the position of stock i made by mutual fund j in the following three months after quarter q’s earnings call.

The third group of market participants consists of retail investors, whose ownership in the stock market is smaller than that of institutional investors but nevertheless influences stock prices, especially in terms of contributing to price volatility (Foucault et al. 2011). Retail investors’ net money inflow (RetailInflow) is denoted as

$$
\begin{array}{c} R e t a i l I n f l o w _ {i, q} = \\ - \text {retail\_buy\_order} _ {i, q} \\ - \text {retail\_sell\_order} _ {i, q}, \end{array}\tag{10}
$$

where \$ retail\_buy\_ $\_ o r d e r _ { i , q }$ (\$ retail\_sell $. o r d e r _ { i , q } )$ is the dollar value of all the retail buy (sell) orders for stock i in the three days following quarter $q ^ { \prime } \mathbf { s }$ earnings call. The retail orders are estimated following Boehmer et al. (2021). Unlike Revision, InstInflow, and FundInflow, which adopt a one- or three-month horizon, RetailInflow only has a three-day horizon. We observe that expanding the time window would render RetailInflow completely uncorrelated to the primary task, possibly because (1) retail orders are less persistent and easy to reverse (Lee et al. 2004), and (2) unlike InstInflow or

FundInflow, which are based on mandated financial statements, RetailInflow is completely estimated, as there is no perfect way to determine whether an order is initialized by a retail investor or not. Consequently, increasing the window likely accumulates more estimation errors.

3.4.2. CAR of Different Horizons. Whereas our primary task is CAR(0, 21), CAR of smaller horizons may also provide useful information (Yang et al. 2020). In this study, we include CAR(0, 0) and CAR(0, 3). We chose them because PEAD accumulates drastically from day 0 to day 3.

## 3.5. Adaptive Task Weighting Method: GradPerp (Gradient Perpendicular)

To determine the task weights, we introduce a novel adaptive task weighting method, GradPerp. The key idea behind GradPerp is that in order to enhance generalizability, it is more beneficial to learn from diverse training sig nals than from similar ones. In cases where two auxiliary tasks offer comparable training signals, GradPerp assigns a relatively smaller weight to one of them. GradPerp operates on task gradients, as they represent the inherent training signals of each auxiliary task. GradPerp employs QR decomposition (Trefethen and Bau 1997), a widely used matrix decomposition technique, to assess the relationship between task gradients. Let the task gradients at the τ-th training step be denoted as

$$
\begin{array}{c} \boldsymbol {\nabla} (\boldsymbol {\tau}) = \left[ \frac {\partial \mathcal {L} _ {p r i}}{\partial \theta}, \frac {\partial \mathcal {L} _ {a u x , 1}}{\partial \theta}, \frac {\partial \mathcal {L} _ {a u x , 2}}{\partial \theta}, \ldots , \frac {\partial \mathcal {L} _ {a u x , K}}{\partial \theta} \right] \\ = \left[ \boldsymbol {\nabla} _ {p r i} (\boldsymbol {\tau}), \boldsymbol {\nabla} _ {a u x, 1} (\boldsymbol {\tau}), \boldsymbol {\nabla} _ {a u x, 2} (\boldsymbol {\tau}), \ldots , \boldsymbol {\nabla} _ {a u x, K} (\boldsymbol {\tau}) \right], \end{array}\tag{11}
$$

where $\nabla _ { p r i }$ is the gradient of the primary task, and $\nabla _ { a u x , k }$ is the gradient of the k-th auxiliary task. They are computed by taking derivatives of task-specific losses with respect to model parameter θ. We flatten $\nabla _ { p r i }$ and $\nabla _ { a u x , k }$ into column vectors.<sup>9</sup> We perform a QR decomposition of $\nabla ( \pmb { \tau } )$ as shown in Equation (12); $q _ { 0 } , q _ { 1 } , q _ { 2 } , \ldots , q _ { K }$ are $K + 1$ unit-length, orthogonal column vectors, and r<sub>lk</sub> are elements of an upper-triangular matrix R. Note that the row and column indices of the Q and R matrices start from zero, which corresponds to the primary task. The remaining indices 1 to $\dot { K }$ indicate the K auxiliary tasks.

$$
\nabla (\pmb {\tau}) = Q \cdot R = [ q _ {0}, q _ {1}, q _ {2}, \ldots , q _ {K} ] \left[ \begin{array}{c c c c} r _ {0 0} & r _ {0 1} & \dots & r _ {0 K} \\ & r _ {1 1} & \dots & r _ {1 K} \\ & & \ddots & \vdots \\ & & & r _ {K K} \end{array} \right].\tag{12}
$$

In $\nabla ( \tau )$ , the k-th task gradient is a linear combination of the first k columns of Q with coefficients given by the k-th column of R. Geometrically, each element in the diagonal of the R matrix can be viewed as the portion of gradient that cannot be linearly explained by previous tasks. Figure 3 illustrates the geometric meaning of Equation (12). Given the k-th auxiliary task gradient $\nabla _ { a u x , k }$ (the blue solid line), the QR decomposition projects it onto a hyperplane spanned by the primary task gradient $\nabla _ { p r i }$ and the previous $k - 1$ auxiliary task gradients $\nabla _ { a u x , 1 } , \ldots , \nabla _ { a u x , k - 1 }$ (limited by the two-dimensional space, we use one axis to represent all the $k - 1$ auxiliary task gradients). The perpendicular part $r _ { k k } \cdot q _ { k }$ (red line) represents the incremental (as it cannot be explained by other task gradients) training signals contributed by the k-th auxiliary task, whose magnitude is $| r _ { k k } |$

The weight of the primary task $\lambda _ { p r i }$ and the weights of auxiliary tasks $\lambda _ { a u x , k }$ are determined as

$$
\lambda_ {a u x, k} = | r _ {k k} | \quad \forall k \in \{1, 2, \ldots , K \}\tag{13}
$$

$$
\lambda_ {p r i} = M \cdot | r _ {0 0} |,\tag{14}
$$

where $r _ { k k }$ and $r _ { 0 0 }$ are the diagonal of the R matrix, and M is a hyperparameter controlling the relative weights between the primary and all the remaining auxiliary tasks. To avoid the randomness resulting from stochastic gradient descending, we smooth the update of task weights λ using the exponential moving average.<sup>10</sup>

GradPerp is closely related to prior studies that use gradient similarity to determine task weights (Du et al. 2018, Lin et al. 2019). In these studies, the weight of an auxiliary task is positively correlated with its similarity to the primary task (e.g., measured by cosine similarity), which is conceptually equivalent to the projected component (the dashed blue line) in Figure 3. In contrast, GradPerp utilizes the perpendicular component (the red line in Figure 3) to determine task weight.

In GradPerp, a larger M indicates a stronger emphasis on the primary task. In the MTL objective function, auxiliary tasks improve generalizability by providing new training signals, effectively acting as regularizers in the objective function. Thus, M conceptually functions as a penalty coefficient, governing the extent of the regularization applied. Compared with grid searches of task weights, tuning M is very efficient: regardless of the number of auxiliary tasks, there remains only one M to be tuned. Empirically, we find that setting M � 1 produces desirable results. In Online Appendix E, we demonstrate that GradPerp is not very sensitive to M, with a wide range of M yielding reasonably good results.

Figure 3. (Color online) Geometric Meaning of QR Decomposition  
![](/api/attachments/BNP8AKSM/fulltext/images/51aa7f66a96ab5eda31e1470447f8c1826c0591b4db3bd8f4dc12a0383e5fa37.jpg)

Online Appendix E also provides the rationale behind designing M as a hyperparameter rather than a learnable parameter. Online Appendix F summarizes the entire GradPerp process.

In this paper, the auxiliary tasks in the total loss function are ordered based on their correlation with the primary task, with more highly correlated tasks appearing first. We find that this ordering approach yields slightly better performance. Detailed results using alternative ordering methods are provided in Online Appendix G.

## 4. Data and Evaluation Method 4.1. Data

Earnings call transcripts from 2008 to 2022 are collected from the S&P Capital IQ Transcript database. We only include stocks that (1) have been in the Russell 3000 index for more than 12 months since 2008, (2) have more than four earnings call records in the database, and (3) whose price and financial statement data are complete in the CRSP, I/B/E/S, Compustat, and Thomson/Refinitiv databases (detailed later). The Russell 3000 index encompasses 97% of the total market capitalization of U.S. equities. We present results for the entire sample (Russell 3000) as well as two subsamples: the S&P 500 and Russell 2000 stocks, representing large-cap and small-cap stocks, respectively. The S&P 500 includes the largest stocks in the U.S. market, covering 80% of the market capitalization. In contrast, the Russell 2000 comprises the smallest Russell 2000 stocks within the Russell 3000, representing approximately 10% of the total market capitalization of Russell 3000.

To ensure timely prediction and to avoid missing trading opportunities, we only keep earnings calls held on the same day or the day after the written earnings press release, as stock prices exhibit significant reactions to earnings news in the first few days (Price et al. 2012). Additionally, we exclude operators’ instructions from the earnings call transcripts, only retaining words from the management teams and analysts. Because of technical issues, some earnings calls are only partially recorded. Thus, calls with combined MD and QA sessions that total less than 1,000 words are also removed. The final data set consists of 2,728 unique stocks with 61,223 quarterly earnings calls. On average, an earnings call consists of 7,209 words (368 sentences), with 2,895 words (130 sentences) from the MD and 4,327 words (238 sentences) from the QA. Accurately determining the date and time of an earnings call is crucial for measuring PEAD. However, we observe discrepancies in the timestamps provided by the S&P transcript database when compared with the companies’ official websites. As a result, we further leverage the RavenPack database, which provides millisecond-level timestamps of various business events, to enhance the precision of the earnings call timestamps.<sup>11</sup> Online Appendix H describes this process in detail. We obtained stock pricerelated data from CRSP,<sup>12</sup> financial statements from Compustat,<sup>13</sup> analyst forecasts from I/B/E/S,<sup>14</sup> and institutional ownership data from CRSP and Thomson/ Refinitiv.<sup>15</sup> Table 4 presents summary statistics of the earnings call transcripts, primary tasks, and auxiliary tasks. Table 5 presents the correlation coefficients bet ween the different tasks.

In addition to the unstructured earnings call transcripts, we incorporate two sets of structured features as model inputs: the manual textual features and the financial ratios. The manual textual features, including sentiment and management spontaneity (Price et al. 2012, Lee 2016), are derived from earnings call transcripts. The financial ratios, including the earnings surprise, consist of 14 variables demonstrated to bear predictive power on PEAD in finance literature (Tetlock et al. 2008, Doran et al. 2010, Lee 2016). To facilitate model learning, we standardize all structured features to have zero mean and unit variance. Online Appendix I presents the definitions and summary statistics of the structured features before standardization.

Table 4. Summary Statistics of the Transcripts and the Primary and Auxiliary Tasks (Before Standardization)

<table><tr><td>Variables</td><td>Min</td><td>First quarter</td><td>Mean</td><td>Third quarter</td><td>Max</td></tr><tr><td colspan="6">Primary task</td></tr><tr><td>CAR(0,21) (%)</td><td>-154.21</td><td>-6.08</td><td>0.54</td><td>6.83</td><td>265.05</td></tr><tr><td colspan="6">Auxiliary tasks</td></tr><tr><td>CAR(0,0) (%)</td><td>-67.47</td><td>-3.57</td><td>0.17</td><td>3.92</td><td>271.87</td></tr><tr><td>CAR(0,3) (%)</td><td>-98.29</td><td>-4.40</td><td>0.22</td><td>4.83</td><td>236.86</td></tr><tr><td>InstInflow (millions of USD)</td><td>-572,934.72</td><td>-108.18</td><td>173.69</td><td>255.33</td><td>234,857.41</td></tr><tr><td>FundInflow (millions of USD)</td><td>-147,160.49</td><td>-42.98</td><td>96.47</td><td>120.21</td><td>130,380.08</td></tr><tr><td>Revision (%)</td><td>-151.07</td><td>0.00</td><td>0.01</td><td>0.00</td><td>233.92</td></tr><tr><td>RetailInflow (millions of USD)</td><td>-597.26</td><td>-0.38</td><td>0.04</td><td>0.23</td><td>753.16</td></tr><tr><td colspan="6">Transcripts</td></tr><tr><td>Number of words (sentences) in MD session</td><td>3 (1)</td><td>2,129 (96)</td><td>2,895 (130)</td><td>3,543 (158)</td><td>32,353 (1,732)</td></tr><tr><td>Number of words (sentences) in QA session</td><td>4 (2)</td><td>2,888 (160)</td><td>4,327 (238)</td><td>5,605 (308)</td><td>18,772 (1,027)</td></tr></table>

Note. Revision can be smaller than �100% when an analyst revises the forecast from a positive value to a negative value.

Table 5. Correlation Coefficients Between the Primary Task and the Auxiliary Tasks

<table><tr><td></td><td>CAR(0,21)</td><td>CAR(0,0)</td><td>CAR(0,3)</td><td>Revision</td><td>InstInflow</td><td>FundInflow</td><td>RetailInflow</td></tr><tr><td>CAR(0,21)</td><td>1</td><td>0.66</td><td>0.73</td><td>0.26</td><td>0.21</td><td>0.20</td><td>-0.01</td></tr><tr><td>CAR(0,0)</td><td></td><td>1</td><td>0.86</td><td>0.30</td><td>0.16</td><td>0.14</td><td>-0.02</td></tr><tr><td>CAR(0,3)</td><td></td><td></td><td>1</td><td>0.30</td><td>0.17</td><td>0.16</td><td>-0.02</td></tr><tr><td>Revision</td><td></td><td></td><td></td><td>1</td><td>0.08</td><td>0.07</td><td>-0.01</td></tr><tr><td>InstInflow</td><td></td><td></td><td></td><td></td><td>1</td><td>0.87</td><td>-0.03</td></tr><tr><td>FundInflow</td><td></td><td></td><td></td><td></td><td></td><td>1</td><td>-0.02</td></tr><tr><td>RetailInflow</td><td></td><td></td><td></td><td></td><td></td><td></td><td>1</td></tr></table>

## 4.2. Training and Evaluation Setting

To ensure that the results are not biased by unusual market conditions in a single year, we employ a rolling window approach (Brown et al. 2020, Meursault et al. 2021). Specifically, we create a rolling window with two years’ data for training and the subsequent quarter for testing.<sup>16</sup> The window is then rolled forward by one quarter to create the next pair of training and test sets. For instance, the first window utilizes data from 2008 Q1 to 2009 Q4 for training and evaluates the resulting model on 2010 Q1, whereas the second window collects training data from 2008 Q2 to 2010 Q1 and evaluates on 2010 Q2. The process is repeated, resulting in a total of 52 windows, with the last test quarter being 2022 Q4. On average, each training set and test set contains 7,616 and 950 earnings calls, respectively. We randomly select 20% of the samples from the training set as the validation set and use the rest for training. By employing the rolling window approach, we can evaluate the model’s performance over the past decade (2010 to 2022) quarter by quarter. The final reported prediction performance is averaged across all 52 test sets, and a one-sided t-test is conducted to determine if our proposed model outperforms the benchmarks.

We define the loss of the primary and auxiliary tasks, $\mathcal { L } _ { p r i }$ and $\mathcal { L } _ { a u x , k }$ in Equation (1) as the negative explained variance (EV), which the model is trained to minimize. Similarly, we report the prediction performance of CAR(0, 21) on the test set in terms of EV. EV is a scalefree metric defined as

$$
\begin{array}{l} E V = 1 - \frac {V a r (\hat {y} - y)}{V a r (y)} \\ = 1 - \frac {\sum_ {i} \left[ (\hat {y} _ {i} - y _ {i}) - \frac {1}{N} \sum_ {i} (\hat {y} _ {i} - y _ {i}) \right] ^ {2}}{\sum_ {i} (y _ {i} - \overline {{y}}) ^ {2}} \in (- \infty , 1 ], \end{array}\tag{15}
$$

where y ˆ is the predicted value, y is the ground truth, y is the sample average of $y ,$ and i is the sample index. EV represents the percentage of ground truth variance that can be explained by the model, with a larger EV indicating better performance.

Whereas mean squared error (MSE) is a more commonly used loss metric, we found that models trained using EV as the loss yield greater economic returns compared with those trained with MSE (see Online Appendix J). Furthermore, EV is positively associated with economic returns—models ranked higher by EV consistently deliver better economic outcomes. In contrast, models favored by MSE do not always exhibit this property. This difference stems from the nature of investment strategies, which often focus on identifying stocks with significant price movements (i.e., top and bottom performers) because these offer the greatest profit potential. Accurately ranking stocks, particularly identifying the top- and bottom-performing ones, is crucial for many trading strategies. Compared with MSE, which focuses on minimizing the absolute distance between predictions and ground truth, EV better rewards models that excel at ranking predictions correctly. To understand this, consider a model always making predictions $\hat { y } = y + c ,$ where c is a nonzero constant. From an MSE perspective, this model’s performance would be bad if c is large. However, in terms of EV, this model would achieve perfect performance because the ranking of the predictions aligns exactly with the ground truth. In PEAD prediction, preserving the order of the ground truth is critical because the predicted values are ultimately used to select the top- or bottom-performing stocks. In Online Appendix J, we provide a detailed discussion of the relationship between EV, MSE, and economic returns.

We used the AdamW optimizer (Loshchilov and Hutter 2019) with a learning rate of 1e-4, determined to be the best after testing {1e-5, 3e-5, 1e-4, 3e-4, 1e-3}. The proposed model contains 59.9 million learnable parameters. The batch size is 32. The training was conducted on a Nvidia RTX 6000 Ada GPU with 48GB VRAM. For each rolling window, we experimented with different values of M from {1, 2, 4, 6, 8} and selected the bestperforming one. We terminated the training early if the EV on the validation set showed no improvement for three consecutive epochs. We recorded the number of epochs at which the highest EV is achieved and retrained the model on the combined training and validation set using this number of epochs. The resulting model is used for the evaluation on the test set. The model converges within 11 epochs in most of the scenarios.

## 5. Prediction Performance and Economic Significance Evaluation

Our evaluation process consists of two stages. In the first stage (Section 5.1), we assess the proposed model’s prediction performance on PEAD against carefully selected benchmark models from prior literature, with an emphasis on examining the effectiveness of the proposed auxiliary tasks (FinAux) and the adaptive weighting method (GradPerp). In the second stage (Section 5.2), we evaluate the model’s economic significance by constructing investment portfolios utilizing the predicted PEAD.

## 5.1. PEAD Prediction Performance

5.1.1. Comparison with Benchmark Models on PEAD Prediction. We selected PEAD prediction benchmarks from related literature in finance, IS, and computer science. Table 6 summarizes the benchmark models. We considered three representative benchmarks from the finance literature: standard unexpected earnings (SUE), ordinary least squares (OLS), and PEAD.txt. SUE is defined as the difference between the actual earnings and the analyst forecast, normalized by stock price (Livnat and Mendenhall 2006). The SUE benchmark is a univariate regression model utilizing SUE to predict PEAD (Martineau 2021). OLS is a multivariate regression model that leverages the same set of structured features as our proposed model, including SUE (Tetlock et al. 2008, Doran et al. 2010). PEAD.txt (Meursault et al. 2021) is a machine learning model based on a bag-ofword representation of earnings call transcripts.<sup>17</sup> Furthermore, we selected two representative neural network–based models: bidirectional long short-term memory (bi-LSTM) (Ma et al. 2020, Yang et al. 2023) and transformer (Yang et al. 2020).<sup>18</sup> These two architectures are included because LSTM and transformer represent today’s most widely used architectures in NLP. Our proposed model is denoted as FinAux + GradPerp +

MQT, highlighting the two innovations: a set of auxiliary tasks grounded in the financial literature (FinAux) and an adaptive weighting method that encourages the learning of diverse auxiliary tasks (GradPerp). Because FinAux and GradPerp can be paired with any underlying neural network architecture, we also pair them with a vanilla transformer, denoted as FinAux + GradPerp + transformer.

Table 7 presents the prediction performance as measured by EV, which is averaged across 52 windows with the standard deviation given in parentheses. In Online Appendix J, we include MSE as the alternative metric and compare it to EV. To further validate our findings, we conducted a one-sided t-test with the null hypothesis that the benchmark models outperform our proposed model (FinAux + GradPerp + MQT). The results indicate that FinAux and GradPerp significantly enhance performance, as all multitask learning models outperform their single-task learning counterparts. Additionally, the combination of FinAux and GradPerp performs best when paired with MQT, as evidenced by the highest EV of 9.06% for FinAux + GradPerp + MQT, compared with 8.72% for FinAux + GradPerp + transformer and all other benchmarks. Finally, we observe that models achieve better prediction accuracy for small-cap stocks (Russell 2000) than large-cap stocks (S&P 500), consistent with findings in the literature that suggest large-cap stocks are harder to predict because of closer monitoring by analysts and investors (Hameed et al. 2015).

Table 8 shows the contribution of each design component. We find that a naïve STL model performs much worse than an MTL model using FinAux and GradPerp (the EV on Russell 3000 stocks drops by 18.56% from 9.06 to 7.38). If we keep the proposed auxiliary tasks (FinAux) but replace GradPerp with a fixed equal weighting method, the EV on Russell 3000 drops by 11.4% from 9.06 to 8.02. Lastly, the SFE, while being a minor design innovation, also improves performance.

Table 6. Description of the Benchmark and Proposed Models

<table><tr><td>Model</td><td>Description</td></tr><tr><td>SUE</td><td>SUE is the difference between actual earnings and the median of analyst forecasts, normalized by the stock price. This approach solely uses SUE to predict PEAD (Livnat and Mendenhall 2006).</td></tr><tr><td>OLS</td><td>A multivariate regression utilizing SUE and other financial ratios (Tetlock et al. 2008, Doran et al. 2010).</td></tr><tr><td>PEAD.txt</td><td>A machine learning model that predicts PEAD based on a bag-of-word representation of earnings call transcripts (Meursault et al. 2021).</td></tr><tr><td>LSTM</td><td>Features are learned from earnings call transcripts using a hierarchical LSTM (Yang et al. 2023).</td></tr><tr><td>Transformer</td><td>Features are learned from earnings call transcripts using a hierarchical transformer (Yang et al. 2020).</td></tr><tr><td>FinAux + GradPerp + MQT</td><td>FinAux is the proposed set of auxiliary tasks; GradPerp is the proposed adaptive weighting method that encourages learning from diverse auxiliary tasks. We pair FinAux and GradPerp with MQT (Xu et al. 2023b).</td></tr><tr><td>FinAux + GradPerp + Transformer</td><td>We pair FinAux and GradPerp with a transformer.</td></tr></table>

Table 7. Prediction Performance on Russell 3000 Stocks

<table><tr><td rowspan="2">MTL?</td><td rowspan="2">Method</td><td colspan="3">EV (%)</td></tr><tr><td>Russell 3000</td><td>Russell 2000</td><td>S&amp;P 500</td></tr><tr><td rowspan="2">Yes</td><td>FinAux + GradPerp + MQT</td><td>9.06 (4.41)</td><td>10.23 (4.60)</td><td>6.30 (6.89)</td></tr><tr><td>FinAux + GradPerp + Transformer</td><td>8.72 (4.11)</td><td>10.02 (4.23)</td><td>5.28 (6.75)</td></tr><tr><td rowspan="5">No</td><td>Transformer</td><td>7.38 (4.02)</td><td>8.51 (4.40)</td><td>5.27 (5.61)</td></tr><tr><td>LSTM</td><td>5.31 (3.55)</td><td>6.37 (4.22)</td><td>3.21 (4.29)</td></tr><tr><td>OLS</td><td>3.70 (5.02)</td><td>4.34 (6.02)</td><td>2.75 (4.85)</td></tr><tr><td>PEAD.txt</td><td>2.99 (3.05)</td><td>3.79 (3.03)</td><td>1.21 (5.43)</td></tr><tr><td>SUE</td><td>0.86 (4.83)</td><td>0.85 (6.23)</td><td>0.99 (1.67)</td></tr></table>

Notes. The EV is averaged across 52 windows, with the standard deviation provided in parentheses. A one-sided t-test shows that the EV of FinAux + GradPerp + MQT is statistically larger than any of the non-MTL models at a significance level of 0.001.

The same pattern is also observed in the S&P 500 and Russell 2000 subsamples.

5.1.2. Visualizing the Realized PEAD. In this section, we visualize the prediction performance by plotting the stocks’ realized PEAD as a curve of CAR(1, T) for increasing values of T (Meursault et al. 2021). Event time, denoted here as T, represents the number of trading days since an earnings call. Using event time allows for the alignment of earnings calls on different calendar days to the same time scale. To compute the realized PEAD, we first sort stocks into quintiles based on their predicted PEAD,<sup>19</sup> generating separate realized PEAD curves for each quintile. Subsequently, we plot the difference curve between the top and bottom PEAD quintiles as the final realized PEAD. This approach enables us to assess the model’s capability to predict both high and low PEAD stocks. It is also important to note that whereas the plotted PEAD provides a useful visual indication of the economic returns a model may generate, it does not serve as a statistical test of trading outcomes. In Section 5.2, we introduce a statistically testable economic return metric.

Figure 4 illustrates that the stocks picked by our model (FinAux + GradPerp + MQT) generate the largest PEAD, resulting in realized PEAD values of 1.99%, 4.19%, and 6.14% at the one-month, one-quarter, and one-year marks, respectively. Figure 4 also illustrates the diminishing power of the traditional earnings surprise–based strategy (SUE), as its realized PEAD curve shows almost no drift. This is consistent with existing literature that suggests the earnings surprise is no longer statistically significant in explaining PEAD (Chordia et al. 2009, Hung et al. 2015, Fink 2021, Martineau 2021).

Notably, although stocks are selected based on the predicted one-month PEAD, the stock prices continue to drift beyond the one-month period. This finding aligns with existing literature that suggests a persistent PEAD, possibly because of the tendency of companies that perform well in one quarter to continue performing well in subsequent quarters (Meursault et al. 2021).

5.1.3. Effectiveness of the Auxiliary Tasks. In this section, we explore possible mechanisms through which auxiliary tasks contribute to the overall performance improvement. Caruana (1997) posits that auxiliary tasks are beneficial because they are easier to learn than the primary task, thus providing shortcuts for the model. To assess a task’s prediction difficulty, we separately predict the primary task CAR(0,21) and each auxiliary task employing the same model and inputs as our proposed architecture, albeit excluding the multitask component. The prediction difficulty for an auxiliary task can be inferred by comparing its EV with that of the pri mary task.

Table 9 presents the results. We observe that, except for RetailInflow and InstInflow, the EV of the rest of the auxiliary tasks is larger than that of the primary task in most of the cases, confirming that these auxiliary tasks are indeed easier to predict.

Table 8. Ablation Analysis of the Proposed Framework

<table><tr><td rowspan="2">Method</td><td colspan="3">EV (%)</td></tr><tr><td>S&amp;P 500</td><td>Russell 2000</td><td>Russell 3000</td></tr><tr><td>FinAux + GradPerp + MQT</td><td>6.30 (6.89)</td><td>10.23 (4.60)</td><td>9.06 (4.41)</td></tr><tr><td>Exclude SFE</td><td>4.19 (6.45)</td><td>7.24 (4.06)</td><td>6.47 (3.83)</td></tr><tr><td>Exclude GradPerp (replacing GradPerp with equal, fixed-task weights)</td><td>5.33 (6.16)</td><td>9.18 (4.32)</td><td>8.02 (4.18)</td></tr><tr><td>Exclude FinAux and GradPerp (equivalent to an STL model)</td><td>5.27 (5.61)</td><td>8.51 (4.40)</td><td>7.38 (4.02)</td></tr></table>

Note. The EV is averaged across 52 windows, with the standard deviation provided in parentheses.

Figure 4. (Color online) PEAD up to Post–250 Trading Days (One Year)  
![](/api/attachments/BNP8AKSM/fulltext/images/fea589be8aeb0c1b4d04444c5fe70bd9d1f53979c30938612ee95865ae459a62.jpg)

We also examine the relative contribution of different types of FinAux. Table 10 presents the results of an ablation analysis where we exclude one type of auxiliary task at a time. Our findings indicate that all proposed auxiliary tasks are beneficial, with CAR(0, 0) and CAR(0, 3) having the most substantial influence, followed by Revision.

5.1.4. Effectiveness of GradPerp. In this section, we demonstrate the effectiveness of GradPerp by replacing it with six other adaptive weighting methods (summarized in Table 2). Additionally, we include a nonadaptive weighting method named FixedEqualWeights, which assigns a weight of one to all tasks and keeps the weight fixed throughout the training. The results are presented in Table 11. Our findings indicate that GradPerp outperforms other weighting methods. As expected, adaptive weighting methods that prefer the primary task generally outperform those that do not. It is also noteworthy that FixedEqualWeights remains a strong benchmark, as only two alternative adaptive weighting methods, GradCos and Uncert, outperform it. Table 11 also presents the training time per epoch for each weighting method, where the time of FixedEqual-Weights is normalized to one. Table 11 demonstrates that GradPerp does not significantly increase the computation time when compared with other gradientbased methods such as OlAux and GradCos.

## 5.2. Economic Significance of Improved PEAD Prediction

In this section, we evaluate the models’ economic significance by constructing investment portfolios utilizing the predicted PEAD. We investigate two representative investment strategies in finance literature: the “long”

and “long-short” strategies (Chordia et al. 2009, Fink 2021, Martineau 2021). The long strategy involves purchasing stocks on the day following the earnings call if the predicted PEAD falls within the top quintile.<sup>20</sup> Whereas this strategy can only profit from positive PEAD, it does not involve short selling, which is not available to many investment vehicles such as mutual funds.<sup>21</sup> On the other hand, the long-short strategy not only involves buying stocks—as in the long strategy— but also includes short-selling stocks if their predicted PEAD falls within the bottom quintile. This strategy can profit from both positive and negative PEADs, and it is more popular in hedge funds (Jiao et al. 2016). Online Appendix K presents the implementation details of the strategy. All stocks are only held for one month (21 trading days), which matches the prediction target of CAR(0,21). Using a fixed holding period reduces the impact of market timing and has been widely adopted in empirical finance research (Fama and French 1993, Chan et al. 1996, Rouwenhorst 1998). For robustness, we also experimented with other holding periods of three months (63 trading days) and six months (126 trading days), and we reported the results in Online Appendix L.

Table 9. Prediction Difficulty of the Primary and Auxiliary Tasks

<table><tr><td rowspan="2">Prediction target</td><td colspan="3">EV (%)</td></tr><tr><td>Russell 3000</td><td>Russell 2000</td><td>S&amp;P 500</td></tr><tr><td>CAR(0,21)</td><td>7.38 (4.02)</td><td>8.51 (4.40)</td><td>5.27 (5.61)</td></tr><tr><td>RetailInflow</td><td>1.78 (3.52)</td><td>-1.05 (3.22)</td><td>1.94 (3.59)</td></tr><tr><td>InstInflow</td><td>4.83 (13.93)</td><td>-12.21 (29.91)</td><td>5.69 (7.74)</td></tr><tr><td>FundInflow</td><td>6.87 (13.91)</td><td>-5.89 (21.65)</td><td>7.00 (7.79)</td></tr><tr><td>CAR(0,3)</td><td>12.65 (4.22)</td><td>13.80 (4.56)</td><td>8.87 (6.85)</td></tr><tr><td>CAR(0,0)</td><td>14.75 (4.59)</td><td>15.74 (4.82)</td><td>11.85 (6.44)</td></tr><tr><td>Revision</td><td>25.87 (6.44)</td><td>27.38 (6.77)</td><td>16.52 (12.92)</td></tr></table>

Note. The EV is averaged across 52 windows, with the standard deviation provided in parentheses.

Table 10. Ablation Analysis of Auxiliary Tasks

<table><tr><td rowspan="2">Auxiliary tasks</td><td colspan="3">EV (%)</td></tr><tr><td>Russell 3000</td><td>Russell 2000</td><td>S&amp;P 500</td></tr><tr><td>FinAux</td><td>9.06 (4.41)</td><td>10.23 (4.60)</td><td>6.30 (6.89)</td></tr><tr><td>Exclude RetailInflow</td><td>8.25 (4.10)</td><td>9.34 (4.27)</td><td>5.82 (5.83)</td></tr><tr><td>Exclude InstInflow and FundInflow</td><td>8.09 (4.00)</td><td>9.33 (4.35)</td><td>4.95 (6.20)</td></tr><tr><td>Exclude Revision</td><td>8.16 (4.31)</td><td>9.09 (4.47)</td><td>6.20 (6.00)</td></tr><tr><td>Exclude CAR(0,0) and CAR(0,3)</td><td>7.82 (4.03)</td><td>8.86 (3.94)</td><td>5.63 (6.27)</td></tr></table>

Note. The EV is averaged across 52 windows, with the standard deviation provided in parentheses.

Our evaluation spans from 2010 Q1 to 2022 Q4, resulting in two portfolios (long and long-short) with approximately 3,000 daily return records.<sup>22</sup> To assess if one model can statistically generate positive risk-adjusted return during the evaluation period, we employ the “alpha” measure, a well-established performance metric for portfolios in finance literature (Carhart 1997, Fama and French 2015, Meursault et al. 2021). Alpha is defined as the intercept term of Equation (16):

$$
\begin{array}{r} R e t _ {t} = a l p h a + \beta_ {1} M k t _ {t} + \beta_ {2} S M B _ {t} + \beta_ {3} H M L _ {t} + \beta_ {4} R M W _ {t} \\ + \beta_ {5} C M A _ {t} + \beta_ {6} U M D _ {t} + \varepsilon_ {t}, \end{array}\tag{16}
$$

where $R e t _ { t }$ is the portfolio raw return on day t, defined as the equally weighted return of all stocks in the portfolio. Mkt, SMB, HML, RMW, CMA, and UMD are risk factors related to the market, firm size, book-to-market ratio, firm profitability, firm investment, and stock price momentum (Carhart 1997, Fama and French 2015). The idea behind this regression is that the return of any portfolio should be explained by the risks it has taken; if not, then it indicates that the portfolio generates more (or less) return than its risks warrant, implying out- or underperformance. Specifically, the regression coefficients (βs) measure the portfolio’s exposure to a set of risk factors, and the nonintercept part $( \beta _ { 1 } M k t _ { t } +$ $\beta _ { 2 } S M B _ { t } + \beta _ { 3 } H M L _ { t } + \beta _ { 4 } R M W _ { t } + \beta _ { 5 } C M \bar { A _ { t } } + \bar { \beta } _ { 6 } U M \bar { D _ { t } } )$ measures the portfolio’s expected return given its risk level.

The intercept (alpha) measures the portfolio’s ability to generate a return in excess of its expectation. In finance, a positive, statistically significant alpha is deemed good. In Online Appendix M, we provide a more detailed discussion on the interpretation and usage of alpha.

Table 12 presents the economic return (alphas) of our model against alternative models. We report the alphas on S&P 500, Russell 2000, and Russell 3000 stocks. S&P 500 and Russell 2000 represent the performance on large-cap and small-cap stocks, respectively. We found that our proposed methods (those having FinAux + GradPerp in the names) outperform the benchmarks in most cases. Specifically, FinAux + GradPerp + MQT achieves a daily alpha of 0.064% (long only) on the Russell 3000 stocks, meaning its daily return surpassed the risk-adjusted benchmark by 0.064 percentage points. We also observe that whereas the MQT performs the best in terms of prediction accuracy, it does not always generate the largest alphas. Using a vanilla transformer as the underlying neural network architecture sometimes generates a slightly larger alpha than MQT. In Online Appendix L, we extend the holding period from one month to three and six months. The results show that the proposed model continues to generate larger alphas than the benchmarks in most of the cases.

Another notable observation from Table 12 is that the performance improvement from MTL is most pronounced for small-cap stocks. Most MTL models (those with FinAux in their names) outperform their non-MTL counterparts for Russell 3000 and Russell 2000 stocks. However, the advantage of MTL diminishes for the large-cap S&P 500 stocks. One possible explanation is that earnings call disclosures tend to be shorter for small-cap firms. For example, the average earnings call transcript is approximately 2,000 words for Russell 2000 stocks, compared with approximately 5,000 words for S&P 500 stocks. As a result, auxiliary tasks may provide more meaningful additional information for small-cap stocks, where available data from earnings calls are relatively limited.

Table 11. Comparison of GradPerp with Other Adaptive Weighting Methods

<table><tr><td rowspan="2">Weighting type</td><td rowspan="2">Weighting method</td><td colspan="3">EV (%)</td><td rowspan="2">Training time per epoch</td></tr><tr><td>Russell 3000</td><td>Russell 2000</td><td>S&amp;P 500</td></tr><tr><td rowspan="3">Adaptive: Primary task preference</td><td>GradPerp (Ours)</td><td>9.06 (4.41)</td><td>10.23 (4.60)</td><td>6.30 (6.89)</td><td>1.5</td></tr><tr><td>OlAux</td><td>6.64 (4.43)</td><td>7.69 (4.18)</td><td>4.81 (7.10)</td><td>1.3</td></tr><tr><td>GradCos</td><td>8.07 (3.86)</td><td>9.28 (3.92)</td><td>5.07 (6.36)</td><td>1.4</td></tr><tr><td rowspan="4">Adaptive: No task preference</td><td>Uncert</td><td>8.22 (4.15)</td><td>9.30 (4.35)</td><td>5.59 (5.94)</td><td>1.1</td></tr><tr><td>AdaMT</td><td>7.97 (4.19)</td><td>8.92 (3.89)</td><td>5.73 (5.74)</td><td>1.0</td></tr><tr><td>DWA</td><td>7.99 (4.19)</td><td>9.11 (4.46)</td><td>4.92 (6.36)</td><td>1.0</td></tr><tr><td>GradNorm</td><td>7.77 (4.35)</td><td>8.95 (4.53)</td><td>4.95 (6.18)</td><td>1.1</td></tr><tr><td>Nonadaptive</td><td>FixedEqualWeights</td><td>8.02 (4.18)</td><td>9.18 (4.32)</td><td>5.33 (6.16)</td><td>1.0</td></tr></table>

Table 12. Economic Return (Alpha) of Simulated Strategies (Holding Period of One Month)

<table><tr><td rowspan="3">Model</td><td colspan="6">Alpha %</td></tr><tr><td colspan="2">Russell 3000</td><td colspan="2">Russell 2000</td><td colspan="2">S&amp;P 500</td></tr><tr><td>Long only</td><td>Long-short</td><td>Long only</td><td>Long-short</td><td>Long only</td><td>Long-short</td></tr><tr><td>SUE</td><td>0.022**</td><td>0.013</td><td>0.021**</td><td>0.025</td><td>0.019</td><td>0.022</td></tr><tr><td>PEAD.txt</td><td>0.029**</td><td>0.033*</td><td>0.027</td><td>0.027</td><td>0.020</td><td>0.017</td></tr><tr><td>OLS</td><td>0.029*</td><td>0.032**</td><td>0.041**</td><td>0.061***</td><td>0.041**</td><td>0.046*</td></tr><tr><td>LSTM</td><td>0.047***</td><td>0.056***</td><td>0.049***</td><td>0.069***</td><td>0.050**</td><td>0.060***</td></tr><tr><td>Transformer</td><td>0.056***</td><td>0.076***</td><td>0.050***</td><td>0.098***</td><td>0.058***</td><td>0.072***</td></tr><tr><td>FinAux + Uncert + MQT</td><td>0.048***</td><td>0.066***</td><td>0.055***</td><td>0.092***</td><td>0.036**</td><td>0.062***</td></tr><tr><td>FinAux + GradCos + MQT</td><td>0.057***</td><td>0.076***</td><td>0.056***</td><td>0.087***</td><td>0.040*</td><td>0.045**</td></tr><tr><td>FinAux + GradPerp + Transformer</td><td>0.056***</td><td>0.069***</td><td>0.061***</td><td>0.103***</td><td>0.052***</td><td>0.046***</td></tr><tr><td>FinAux + GradPerp + MQT</td><td>0.064***</td><td>0.090***</td><td>0.069***</td><td>0.125***</td><td>0.057***</td><td>0.064***</td></tr></table>

Notes. Alpha is the intercept term in Equation (16), representing the average excess return a portfolio can generate after risk adjustment. Th number of asterisks represents the significance of alpha under the null hypothesis that alpha is zero. \*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Finally, to show how our proposed model performs during different market conditions, we calculate and plot the time-variant alpha from 2010 to 2022. Specifically, we calculate the alpha using the same method as in Equation (16) using a 100-trading-day window and then moving forward by one day until the end of the sample period. We also present the CRSP total market index (normalized to one at the beginning of the sample) for comparison. Figure 5 presents the result. We can see that most of the time, the alpha stays above zero. There is a significant drop in alpha around 2020 and early 2022, where the market is notably volatile because of trade wars, COVID-19, inflation, and supply chain disruptions. This implies that our strategy may be impacted by a volatile market.

Figure 5. Time-Variant Alpha  
![](/api/attachments/BNP8AKSM/fulltext/images/e9cae833536f66132103d2664170bc8746a430ebcaf854921c75c311e252a5f6.jpg)

## 6. Discussion and Conclusion 6.1. Research Implications

IS scholars suggest that novel IT artifacts should contribute prescriptive knowledge to the IS knowledge base (Nunamaker et al. 1990). Our research context, research method, and paradigm are closely related to and built on the following streams of research: Fintech IS (Hendershott et al. 2021), multitask learning, and computational design science (Shmueli and Koppius 2011, Gregor and Hevner 2013, Hevner 2017, Padmanabhan et al. 2022). Our contributions to the IS literature are threefold.

6.1.1. Fintech Research in IS. This study presents the first comprehensive investigation into the employment of MTL for PEAD prediction, bridging the realms of finance and IS literature. Whereas PEAD has been extensively studied by finance researchers and practi tioners for decades, there has been a lack of research into the utilization of postevent investor responses, a critical intermediary in the PEAD mechanism. Our proposed MTL framework leverages postevent investor responses as auxiliary model outputs, with a specific focus on three key investor groups: stock analysts, institutional investors, and retail investors. This study provides significant implications for grounding MTL design and implementation innovations in domain knowledge.

Moreover, this study identifies a potential type of Fintech problem that can benefit from MTL. The efficacy of our proposed auxiliary tasks lies in the inherent time lag between the input (earnings call) and the prediction tar get (stock price movement), with investor responses serving as a critical link between the two. Many financerelated predictions exhibit similar characteristics, such as the prediction of price after mergers and acquisitions, credit rating downgrades, analyst recommendation downgrades, initial and secondary public equity offerings, and share repurchases and splits (Abarbanell and Bernard 1992, Golubov et al. 2013). In all these events, investor responses function as a link between the initial events and the subsequent price movement.

6.1.2. MTL Research in IS. Our study is unique in MTL adaptive weighting studies, as it introduces a mathematical approach to determining task weights based on the number of diverse training signals each task provides. Unlike previous adaptive weighting methods that emphasize the fast convergence of the primary task, our proposed GradPerp approach focuses on enhancing generalizability. Empirical results support the efficacy of our approach. Furthermore, MTL studies in IS literature often focus on cross-task parameter sharing while neglecting to improve the task weights within the objective function based on the intrinsic characteristics of the focal prediction problem (Yu et al. 2022). The proposed GradPerp adaptive weighting method can be seamlessly integrated into any existing MTL architecture, provided that the objective function is a linear combination of task losses.

6.1.3. Design Science Research. This study also relates to computational design science research (Rai 2017, Padmanabhan et al. 2022). This paradigm emphasizes an “interdisciplinary approach in developing novel data representations, computational algorithms, business intelligence, and analytics methods.” Our study is motivated by the significance of the focal business problem and the contextual insights into how to effectively address the problem. We demonstrate that by adapting the MTL framework and incorporating the PEAD mechanism in the auxiliary task selection, we can achieve both a performance that surpasses prior work and a meaningful economic gain. Our study provides a foundation for research on how a prediction problem can leverage the MTL framework and how to judiciously select auxiliary tasks and adaptive weighting methods.

## 6.2. Practical Implications

Our research provides immediate implications for investors. First, our findings demonstrate that PEAD remains economically meaningful when predicted with an advanced deep learning model and when leveraging unstructured features such as earnings call transcripts. This contrasts with prior literature that suggests a disappearing PEAD. The discrepancy may arise because of the fact that prior studies relied solely on public and readily accessible accounting figures as inputs, requiring less sophisticated analysis. In contrast, utilizing earnings call transcripts involves more complex analysis and heavily relies on the advancement of the model. To investors, this observation underscores the importance of new technology, particularly deep learning, in the finance domain.

PEAD strategy belongs to the category of eventdriven strategies, which profit from price movement because of various corporate events. Investors like event-driven funds may be interested in our proposed method. In addition, the PEAD strategy does not require the investor to hold stock throughout the year, as earnings news is only released in particular windows. Therefore, the PEAD strategy is a valuable building block in investors’ hands, as investors can combine it with other strategies.

Furthermore, our findings open up new opportunities to improve the performance of finance-related predictions. Whereas the prior STL framework primarily focused on improving performance through feature selection and learning algorithms, the proposed Grad Perp and MTL architecture offers an additional avenue for performance improvement by incorporating relevant auxiliary tasks. This study provides a foundation for financial analysts and decision makers to leverage their expertise and explore additional auxiliary tasks for a variety of finance prediction problems.

## 6.3. Limitations and Future Directions

Our study is not without limitations. The performance of FinAux, the proposed PEAD framework, and Grad-Perp, the proposed task weighting method, could vary across different industry sectors. Furthermore, whereas our auxiliary tasks have the potential to extend to other stock price–related prediction tasks, we have not tested them. Similarly, we have not tested how GradPerp— despite outperforming other adaptive weighting tasks in the PEAD prediction context—performs in other domains. We suggest these topics for future work.

Additionally, our choice of EV as the training loss and primary metric is context specific and may not generalize to all regression tasks. We selected EV because it aligns with finance literature and the priorities of investment decision making, where economic outcomes are paramount. As the trade-offs between EV and MSE remain underexplored in the literature, we aim to spark awareness and encourage further exploration of this topic in future studies.

Furthermore, whereas large language models (LLMs) have shown promise in financial applications, we found that fine-tuning them for PEAD prediction presents unique challenges. In Online Appendix N, we document our attempt to fine-tune Mistral and Llama 3.1 for PEAD prediction. Understanding the impact of LLM fine-tuning on financial predictive models remains a promising direction for future research.

Lastly, we use a fixed holding period for portfolio construction. Whereas a dynamic holding period could potentially enhance profits, determining its optimal length involves complexities beyond this study’s scope.

As our focus is on improving prediction performance, we leave the exploration of dynamic holding periods to future research.

## Acknowledgments

The authors sincerely thank Senior Editor Dr. Eric Zheng, Associate Editor Dr. Huimin Zhao, and the anonymous reviewers for their valuable feedback and insightful suggestions, which have greatly enhanced this work. The authors are also grateful to Dr. Yiming Xu for his thoughtful feed back on the model design. Additionally, the authors acknowledge the participants of the Data Science Workshop at INFORMS for their valuable discussions and feedback.

## Endnotes

<sup>1</sup> If there are K tasks in the model and one wants to evaluate N different weights for each task, then a grid search approach requires us to evaluate $N ^ { K }$ combinations.

<sup>2</sup> The raw return from day t<sub>1</sub> to t<sub>2</sub> is calculated as $\begin{array} { r } { \frac { P _ { t _ { 2 } } } { P _ { t _ { 1 } } } - 1 } \end{array}$ , where $P _ { t }$ is the stock price on day t.

<sup>3</sup> When the objective function (total loss) is a linear combination of all the task losses, the total gradient will also be a linear combination of these task-specific gradients. The total gradient is then used to update the model parameters.

<sup>4</sup> See https://huggingface.co/sentence-transformers/all-mpnet-basev2. To reduce memory cost, we freeze the parameter of the sentence encoder during training. Using a pretrained model significantly reduces overfitting compared to training an end-to-end model from scratch. Our model has a total of 168 million parameters, but only 59 million are trainable.

<sup>5</sup> Mutual funds and many institutional investors are only obligated to report their holdings quarterly or semiannually. Consequently, if auxiliary tasks have a relatively short horizon, such as one month, what is captured might be last quarter’s holdings rather than the current quarter’s.

<sup>6</sup> Wharton Research Data Services (WRDS) and some researchers have identified several issues regarding potential missing and corrupted data in the Thomson/Refinitiv database. For further details, please refer to https://wrds-www.wharton.upenn.edu/pages/sup port/manuals-and-overviews/thomson-reuters/mutual-fund-andinvestment-company.

<sup>7</sup> See https://wrds-www.wharton.upenn.edu/documents/1414/ WRDS\_Ownership\_Data.pdf.

<sup>8</sup> See https://www.researchandmarkets.com/reports/5394162/usmutual-funds-industry-growth-trends-covid.

<sup>9</sup> As an implementation detail, we calculate the gradient of each task loss with respect to the final decoder block of the MQT module, rather than with respect to all model parameters. This significantly reduces the dimension of ∇(τ) while preserving the power of Grad-Perp. However, for the update of model parameters, we continue to take derivatives with respect to all model parameters.

<sup>10</sup> The task weight λ is updated with the formula $\lambda _ { t } \gets$ $\left( 1 - \beta \right) \cdot \lambda _ { t } + \beta \cdot \lambda _ { t - 1 }$ . In our implementation, β is set to 0.98. We also tested $\begin{array} { r } { { \vec { \beta } } = [ 0 . 6 , } \end{array}$ , 0:7; 0:8, 0:9, 0:99].

<sup>11</sup> See https://wrds-www.wharton.upenn.edu/pages/get-data/rave npack-news-analytics-40/.

<sup>12</sup> See https://wrds-www.wharton.upenn.edu/pages/get-data/centerresearch-security-prices-crsp/.

<sup>13</sup> See https://wrds-www.wharton.upenn.edu/pages/get-data/comp ustat-capital-iq-standard-poors/.

<sup>14</sup> See https://wrds-www.wharton.upenn.edu/pages/get-data/ibesthomson-reuters/.

<sup>15</sup> See https://wrds-www.wharton.upenn.edu/pages/get-data/thom son-reuters/.

<sup>16</sup> We adopt a rolling window approach with a training period of two years and a test period of one quarter. We made this choice in order to enhance the robustness of our evaluations and ensure comparability with prior work, specifically Meursault et al. (2021). In practice, increasing the window size can potentially improve performance.

<sup>17</sup> In the original paper, the prediction target of PEAD.txt is defined as CAR(0, 0), and the authors approach it as a binary classification problem (predicting whether CAR(0, 0) is positive or negative). In contrast, we redefine this task as a numerical prediction of CAR(0, 21) to ensure comparability of PEAD.txt with other models presented in this table. However, when evaluating the economic significance of PEAD.txt, we continue using CAR(0, 0) as the prediction target to preserve the original methodological design of the authors.

<sup>18</sup> The bi-LSTM model has two stacked bidirectional LSTM layers, producing the document-level embedding through the concatenation of the last token’s embeddings from both directions in the final layer. This transformer model has three encoder layers with a hidden dimension size of 3,072 (4 × 768).

<sup>19</sup> To avoid data leak, the quintile cutoffs are calculated using the training data.

<sup>20</sup> To make the strategy more realistic, we open a position on the next trading day rather than on the earnings call day (i.e., on day 1 instead of day 0). Following the earnings disclosure, stock prices often react within milliseconds, with a surge of buy and sell order flooding into the exchange. It is challenging for most investors to react so promptly. Investing on the next day, despite potentially risking the loss of some profit, is more applicable.

<sup>21</sup> See https://www.sec.gov/investment/laws-and-rules.

<sup>22</sup> During nonearnings seasons, a portfolio’s holding may be empty, resulting in zero daily return. We excluded these observations.

## References

Abarbanell JS, Bernard VL (1992) Tests of analysts’ overreaction/ underreaction to earnings information as an explanation for anomalous stock price behavior. J. Finance 47(3):1181–1207.

Ali A, Chen X, Yao T, Yu T (2020) Can mutual funds profit from post earnings announcement drift? The role of competition. J. Banking Finance 114:105774.

Ball R, Brown P (1968) An empirical evaluation of accounting income numbers. J. Accounting Res. 6(2):159–178.

Bernard VL, Thomas JK (1989) Post-earnings-announcement drift: Delayed price response or risk premium? J. Accounting Res. 27:1–36.

Bessembinder H, Cooper MJ, Zhang F (2019) Characteristic-based benchmark returns and corporate events. Rev. Financial Stud. 32(1):75–125.

Beyan C, Capozzi F, Becchio C, Murino V (2017) Multi-task learning of social psychology assessments and nonverbal features for automatic leadership identification. ICMI ‘17 Proc. 19th ACM Internat. Conf. Multimodal Interaction (Association for Computing Machinery, New York), 451–455.

Bhattacharjee D, Zhang T, Su¨ sstrunk S, Salzmann M (2022) MuIT: An end-to-end multitask learning transformer. Proc. IEEE/CVF Conf. Comput. Vision Pattern Recognition (IEEE, Piscataway, NJ) 12031–12041.

Boehmer E, Jones CM, Zhang X, Zhang X (2021) Tracking retail investor activity. J. Finance 76(5):2249–2305.

Bonilla EV, Chai K, Williams C (2007) Multi-task Gaussian process prediction. Adv. Neural Inform. Processing Systems, vol. 20 (Curran Associates, Inc., Red Hook, NY).

Brown NC, Crowley RM, Elliott WB (2020) What are you saying? Using topic to detect financial misreporting. J. Accounting Res. 58(1):237–291.

Bru¨ggemann D, Kanakis M, Obukhov A, Georgoulis S, Van Gool L (2021) Exploring relational context for multi-task dense predic tion. Proc. 2021 IEEE/CVF Internat. Conf. Comput. Vision (IEEE, Piscataway, NJ), 15869–15878.

Carhart MM (1997) On persistence in mutual fund performance. J. Finance 52(1):57–82.

Carion N, Massa F, Synnaeve G, Usunier N, Kirillov A, Zagoruyko S (2020) End-to-end object detection with transformers. Vedaldi A, Bischof H, Brox T, Frahm JM, eds. Comput. Vision – ECCV 2020, Lecture Notes in Computer Science, vol. 12346 (Springer, Cham, Switzerland), 213–229.

Caruana R (1997) Multitask learning. Machine Learn. 28(1):41–75.

Caruana R (1998) Multitask learning. Autonomous Agents Multi Agent Systems 27(1):95–133.

Caruana R, Baluja S, Mitchell T (1996) Using the future to “sort out” the present: Rankprop and multitask learning for medical risk evaluation. NIPS’95 Proc. 9th Internat. Conf. Neural Inform. Pro cessing Systems (MIT Press, Cambridge, MA), 959–965.

Chan LKC, Jegadeesh N, Lakonishok J (1996) Momentum strategies. J. Finance 51(5):1681–1713.

Chebonenko T, Gu O, Muravyev D (2018) Text sentiment’s ability to capture information: Evidence from earnings calls. Preprint, submitted November 12, 2013, http://dx.doi.org/10.2139/ssrn. 2352524.

Chen Z, Badrinarayanan V, Lee CY, Rabinovich A (2018) Gradnorm: Gradient normalization for adaptive loss balancing in deep multitask networks. Dy JG, Krause A, eds. Proc. 35th Internat. Conf. Machine Learn., vol. 80 (PMLR, New York), 794–803.

Cheng HT, Koc L, Harmsen J, Shaked T, Chandra T, Aradhye H, Anderson G, Corrado G, Chai W, Ispir M (2016) Wide & deep learning for recommender systems. DLRS 2016 Proc. 1st Workshop Deep Learn. Recommender Systems (Association for Comput ing Machinery, New York), 7–10.

Chordia T, Goyal A, Sadka G, Sadka R, Shivakumar L (2009) Liquidity and the post-earnings-announcement drift. Financial Anal. J. 65(4):18–32.

Doran JS, Peterson DR, Price SM (2010) Earnings conference cal content and stock price: The case of REITs. J. Real Estate Finan cial Econom. 45(2):402–434.

Du Y, Czarnecki WM, Jayakumar SM, Farajtabar M, Pascanu R, Lakshminarayanan B (2018) Adapting auxiliary losses using gradient similarity. Preprint, submitted December 5, https:// arxiv.org/abs/1812.02224.

Fama EF, French KR (1993) Common risk factors in the returns on stocks and bonds. J. Financial Econom. 33(1):3–56.

Fama EF, French KR (2015) A five-factor asset pricing model. J. Financial Econom. 116(1):1–22.

Feibel BJ (2003) Investment Performance Measurement (John Wiley & Sons, Hoboken, NJ).

Fink J (2021) A review of the post-earnings-announcement drift. J. Behav. Experiment. Finance 29:100446.

Foucault T, Sraer D, Thesmar DJ (2011) Individual investors and volatility. J. Finance 66(4):1369–1406.

Francis J, Lafond R, Olsson P, Schipper K (2007) Information uncer tainty and post-earnings-announcement-drift. J. Bus. Finance Accounting 34(3–4):403–433.

Frankel R, Johnson M, Skinner DJ (1999) An empirical examination of conference calls as a voluntary disclosure medium. J. Accounting Res. 37(1):133–150.

Golubov A, Petmezas D, Travlos NG (2013) Empirical mergers and acquisitions research: A review of methods, evidence and

managerial implications. Bell AR, Brooks C, Prokopczuk M, eds. Handbook of Research Methods and Applications in Empirical Finance (Edward Elgar Publishing Limited, Northampton, MA), 287–313.

Gregor S, Hevner AR (2013) Positioning and presenting design science research for maximum impact. MIS Quart. 37(2):337–355.

Hameed A, Morck R, Shen J, Yeung B (2015) Information, analysts, and stock return comovement. Rev. Financial Stud. 28(11): 3153–3187.

Hendershott T, Zhang X, Zhao JL, Zheng Z (2021) FinTech as a game changer: Overview of research frontiers. Inform. System Res. 32(1):1–17.

Hevner A (2017) Intellectual control of complexity in design science research. Editor’s Comments Divers. Des. Sci. Res. (pp. iii–vi), MIS Quart. 41(1):iii–xviii.

Hollander S, Pronk M, Roelofsen E (2010) Does silence speak? An empirical analysis of disclosure choices during conference calls. J. Accounting Res. 48(3):531–563.

Hung M, Li X, Wang S (2015) Post-earnings-announcement drift in global markets: Evidence from an information shock. Rev Financial Stud. 28(4):1242–1283.

Isonuma M, Fujino T, Mori J, Matsuo Y, Sakata I (2017) Extractiv summarization using multi-task learning with document classi fication. Palmer M, Hwa R, Riedel S, eds. Proc. 2017 Conf. Empirical Methods Natural Language Processing (Association for Computational Linguistics, Stroudsburg, PA), 2101–2110.

Jacob L, Philippe VJ, Bach F (2008) Clustered multi-task learning: A convex formulation. NIPS’08 Proc. 22nd Internat. Conf. Neural Inform. Pro cessing Systems (Curran Associates, Inc., Red Hook, NY), 745–752.

Jalali A, Sanghavi S, Ruan C, Ravikumar P (2010) A dirty model for multi-task learning. Adv. Neural Inform. Processing Systems, vol. 23 (Curran Associates, Inc., Red Hook, NY).

Jha A, Kumar A, Banerjee B, Chaudhuri S (2020) AdaMT-Net: An adaptive weight learning based multi-task learning model for scene understanding. 2020 IEEE/CVF Conf. Comput. Vision Pat tern Recognition Workshops (IEEE, Piscataway, NJ), 706–707.

Jiao Y, Massa M, Zhang H (2016) Short selling meets hedge fund 13F: An anatomy of informed demand. J. Financial Econom. 122(3):544–567.

Kendall A, Gal Y, Cipolla R (2018) Multi-task learning using uncertainty to weigh losses for scene geometry and semantics. 2018 IEEE/CVF Conf. Comput. Vision Pattern Recognition (IEEE, Piscataway, NJ), 7482–7491.

Keswani A, Stolin D (2008) Which money is smart? Mutual fund buys and sells of individual and institutional investors. J. Finance 63(1):85–118.

Kim JB, Li L, Yu Z, Zhang H (2019) Local versus non-local effects of Chinese media and post-earnings announcement drift. J. Banking Finance 106:82–92.

Kuang L, Yan X, Tan X, Li S, Yang X (2019) Predicting taxi demand based on 3D convolutional neural network and multi-task learning. Remote Sensing 11(11):1265.

LeCun Y (1989) Generalization and network design strategies. Pfeifer R, Schreter Z, Fogelman F, Steels L, eds. Connectionism in Perspective, vol. 19 (Elsevier/North-Holland Publishers, Amsterdam), 143–155.

Lee J (2016) Can investors detect managers’ lack of spontaneity? Adherence to predetermined scripts during earnings conference calls. Accounting Rev. 91(1):229–250.

Lee CM, Zhu C (2022) Active funds and bundled news. Accounting Rev. 97(1):315–339.

Lee YT, Liu YJ, Roll R, Subrahmanyam A (2004) Order imbalances and market efficiency: Evidence from the Taiwan stock exchange. J. Financial Quant. Anal. 39(2):327–341.

Lin X, Baweja HS, Kantor G, Held D (2019) Adaptive auxiliary task weighting for reinforcement learning. Lee DD, Sugiyama M, von Luxburg U, Guyon I, Garnett R, eds. Internat. Conf. Neural

Inform. Processing Systems, vol. 32 (Curran Associates, Inc., Red Hook, NY), 4773–4784.

Lin YK, Chen H, Brown RA, Li SH, Yang HJ (2017) Healthcare pre dictive analytics for risk profiling in chronic care: A Bayesian multitask learning approach. MIS Quart. 41(2):473–495.

Liu S, Johns E, Davison AJ (2019) End-to-end multi-task learning with attention. 2019 IEEE/CVF Conf. Comput. Vision Pattern Rec ognition (IEEE, Piscataway, NJ), 1871–1880.

Livnat J, Mendenhall RR (2006) Comparing the post–earnings announcement drift for surprises calculated from analyst and time series forecasts. J. Accounting Res. 44(1):177–205.

Loshchilov I, Hutter F (2019) Decoupled weight decay regularization. 7th Internat. Conf. Learn. Representations (International Soci ety of the Learning Sciences, Ann Arbor, MI).

Ma Z, Bang G, Wang C, Liu X (2020) Towards earnings call and stock price movement. Preprint, submitted August 23, https:// arxiv.org/abs/2009.01317.

MacKinlay AC (1997) Event studies in economics and finance. J. Econom. Literature 35(1):13–39.

Martineau C (2021) Rest in peace post-earnings announcement drift. Critical Finance Rev. 11(3–4):613–646.

Meursault V, Liang PJ, Routledge BR, Scanlon MM (2021) PEAD.txt: Post-earnings-announcement drift using text. J. Financial Quant. Anal. 58(6):2299–2326.

Nunamaker JF Jr, Chen M, Purdin TD (1990) Systems development in information systems research. J. Management Inform. Systems 7(3):89–106.

Padmanabhan B, Sahoo N, Burton-Jones A (2022) Machine learning in information systems research. MIS Quart. 46(1):iii–xix.

Price SM, Doran JS, Peterson DR, Bliss BA (2012) Earnings conference calls and stock returns: The incremental informativeness of textual tone. J. Banking Finance 36(4):992–1011.

Rai A (2017) Editor’s comments: Diversity of design science research. MIS Quart. 41(1):iii–xviii.

Reimers N, Gurevych I (2019) Sentence-BERT: Sentence embeddings using Siamese BERT-Networks. Proc. 2019 Conf. Empirical Methods Natural Language Processing 9th Internat. Joint Conf. Natural Language Processing (Association for Computational Linguistics, Kerrville, TX), 3982–3992.

Rouwenhorst KG (1998) International momentum strategies. J. Finance 53(1):267–284.

Shmueli G, Koppius OR (2011) Predictive analytics in information systems research. MIS Quart. 35(3):553–572.

Tetlock PC, Saar-Tsechansky M, Macskassy S (2008) More than words: Quantifying language to measure firms’ fundamentals J. Finance 63(3):1437–1467.

Trefethen LN, Bau D III (1997) Numerical Linear Algebra (Society for Industrial and Applied Mathematics, Philadelphia).

Vandenhende S, Georgoulis S, Van Gool L (2020) MTI-Net: Multiscale task interaction networks for multi-task learning. Vedaldi A, Bischof H, Brox T, Frahm JM, eds. Comput. Vision – ECCV 2020, Lecture Notes in Computer Science, vol. 12349 (Springer, Cham, Switzerland), 527–543.

Wang J, Tian J, Qiu L, Li S, Lang J, Si L, Lan M (2018) A multi-task learning approach for improving product title compression with user search log data. Proc. AAAI Conf. Artificial Intelligence (Association for the Advancement of Artificial Intelligence, Washington, DC), 451–458.

Xu Y, Yang Y, Zhang L (2023a) DeMT: Deformable mixer transformer for multi-task learning of dense prediction. Proc. AAAI Conf. Artificial Intelligence (Association for the Advancement of Artificial Intelligence, Washington, DC), 3072–3080.

Xu Y, Li X, Yuan H, Yang Y, Zhang L (2023b) Multi-task learning with multi-query transformer for dense prediction. IEEE Trans. Circuits Systems Video Tech. 34(2):1228–1240.

Xu X, Zhao H, Vineet V, Lim SN, Torralba A (2022) MTFormer: Multi-task learning via transformer and cross-task reasoning Avidan S, Brostow G, Cisse ´ M, Farinella GM, Hassner T, eds Comput. Vision – ECCV 2022, Lecture Notes in Computer Science, vol. 13687 (Springer Nature, Cham, Switzerland), 304–321.

Yang Y, Hospedales TM (2016) Deep multi-task representation learning: A tensor factorisation approach. Internat. Conf. Learn. Representation (ICLR, Appleton, MI).

Yang L, Ng TLJ, Smyth B, Dong R (2020) HTML: Hierarchical transformer-based multi-task learning for volatility prediction. WWW’20 Proc. Web Conf. 2020 (Association for Computing Machinery, New York), 441–451.

Yang Y, Qin Y, Fan Y, Zhang Z (2023) Unlocking the power of voice for financial risk prediction: A theory-driven deep learning design approach. MIS Quart. 47(1):63–96.

Yu S, Chai Y, Chen H, Sherman SJ, Brown RA (2022) Wearable sensor-based chronic condition severity assessment: An adversarial attention-based deep multisource multitask learning approach. MIS Quart. 46(3):1355–1394.

Zhang Y, Yang Q (2021) A survey on multi-task learning. IEEE Trans. Knowledge Data Engrg. 34(12):5586–5609.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
