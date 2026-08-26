---
otero_id: 9698
otero_key: "6N5ED5FJ"
title: "Family profile mining in retailing"
authors: "Shaohua Lian; Yunjie Xu; Cheng Zhang"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.007"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Family profile mining in retailing

Shaohua Lian, Yunjie Xu<sup>⁎</sup>, Cheng Zhang

School of Management, Fudan University, 670 Guoshun Road, Shanghai, China

![](/api/attachments/6N5ED5FJ/fulltext/images/bbb2001d8d858a781e3aa7aa25cd1ee190779486f39f204149bb97d21de60477.jpg)

A R T I C L E I N F O

Keywords: Family profiles Database marketing Positive and unlabeled (PU) learning Feature selection Unlabeled learning

## A B S T R A C T

In the era of personalized marketing, the ability to leverage data analysis to recommend tailored products is a key competitive advantage for retailers. Family profiles are an essential aspect of customer information to boost the performance of knowledge-based recommendations. This study integrates positive and unlabeled learning and feature selection techniques to design a novel and flexible family profiling algorithm that tags target customers based on unlabeled transaction data. The empirical evaluation shows that our algorithm outperforms other algorithms in terms of the recall rate of families of the target tag. The knowledge of inferred family profiles also enhances the product recommendation performance. Our algorithm can help retailers eficiently target customers based on family profiles for better marketing performance.

## 1. Introduction

Customer-centric retailers must answer two fundamental questions: “Who are my customers, and which products to ofer?” The two questions are intertwined. The choice of products has an efect on the cus tomers they attract, and the existing customer base suggests what are the right products to ofer. Because these two aspects of a business coevolve over time, retailers need to constantly monitor their customer composition and adjust their product ofering.

Retailers' ongoing decisions are based on the collection, processing, and analysis of their customer information [1,2]. Customer information includes two categories: transaction data and customer profiles. Transaction data refers to customers' purchase records in databases. They provide a detailed record of customer purchase behavior and suggest their product interest. Customer profiles are the socioeconomic, geographic, demographic, psychographic, and behavioral characteristics of a customer [9]. A customer profile can be presented by a tag attached to a customer, such as “married”. Classification or clustering techniques are used to group customers of similar profiles into segments. Customers of the same segment have similar product interest [3]. The ultimate goal of retailers is to understand each customer and achieve personalized marketing [10].

Although increasingly sophisticated technology has been used to collect customer information, inferring useful customer profiles remains a significant challenge. On the one hand, customers often regard retailers' information collection activities as an invasion of privacy, and thus, refuse to disclose their personal information to avoid marketing messages. On the other hand, most existing customer-profile-based marketing approaches collect customer profiles through surveys or external data sources that could be erroneous or costly. Therefore, inferring customer profiles from transaction data becomes an attractive alternative. However, transaction data itself does not come with a label of customer profile tag. To the best of our knowledge, few studies have predicted customer profiles using unlabeled transaction data.

In the extant research, the family profiles of a customer have received even less attention [11,12]. Studies have mainly focused on mining profiles of individual customers. However, shopping is often conducted for an entire family. In this paper, we define family profiles as the tags describing the demographic characteristics of a family, such as size, the presence of children, income, and socioeconomic status. It is a subset of the customer profile.

This study focuses on the family profiles of supermarket customers. Assume that a membership card represents a family, the aim of this study is to propose an algorithmic framework that employs positive and unlabeled (PU) learning techniques to predict family profiles by using only the unlabeled transaction data of membership cards. The use of unlabeled transaction data for family profile prediction not only avoids the limitation of surveys and self-reports but also links profiles with corresponding product preference implied in transaction history, hence facilitates the product ofering decision for retailers.

The main contributions of this study are fourfold. First, we propose a novel algorithmic framework to predict family profiles from unlabeled transaction data. Second, we integrate feature selection and PU learning into a new framework. Third, we explore the balance between the efectiveness and eficiency of the proposed algorithm and compare the performance of diferent profile characteristics. Fourth, we demonstrate the application of family profiles for product recommendations as a type of product ofering decision. Overall, the proposed algorithm ofers satisfactory precision for family profile pre diction. Retail companies can use our proposed algorithm to build and expand their customer profile systems for product recommendations.

The remainder of this paper is organized as follows. Section 2 reviews the literature related to database marketing, PU learning, and feature selection. Section 3 states our research problem and explains the details of the proposed family profiling algorithm. Section 4 describes the procedures and results of the empirical evaluation. Sections 5 and 6 further demonstrate the efectiveness of our proposed algorithm through two experiments. Finally, we provide conclusions and directions for future study.

## 2. Literature review

## 2.1. Database marketing

Database marketing is techniques to use customer profiles for product recommendations. It comprises of activities related to the “gathering, saving and using the maximum amount of useful knowledge about your customers and prospects” [13]. Customer information is the foundation of database marketing. The precision and depth of a company's customer information determine the potential of database analysis to increase profitability [16]. As mentioned above, customer information includes transaction data and customer profiles. Transaction data in databases usually includes the transaction time, member id, product description, purchase quantity, and purchase amount. Customer profiles include geographic, demographic, psychographic, and behavioral information [9,17]. With such information, database marketing can target customers in a more personalized way [14] and build an efective relationship with each customer [15].

The family is a central concept in marketing and demands retailer's attention. Compared with individual decision-making, family behaviors are more complex [18], because the needs of all family members need to be satisfied. In this study, the family profiles of supermarket customers refer to tags describing family characteristics, such as whether it is a family with a baby. If that is the case, a marketer may recommend a wider range of baby and maternity products. The knowledge of family profiles thus enhances the individual profiles of the customer and ofers new marketing opportunities. Unfortunately, Retailers cannot easily obtain family profiles. In most cases, they can only obtain basic individual profiles, such as name, address, and contact information through membership registration. Other customer profiles such as sociodemographic, lifestyle, and credit information might be obtained from external sources [21]. The purchase of external data is not only costly but also subject to legal restrictions. Therefore, mining customer profiles from ubiquitous transaction data is an imperative task [22].

An important family profile is customers' family structure. Previous studies have noted the influence of family structure on family purchase decisions [19,20]. Recent studies have demonstrated that the knowl edge of the age of child helps recommender systems to improve recommendation accuracy [23,24]. Closely related to family structure, the life stage of a family is regarded as an important indicator of family behavior in marketing and sociology studies [25,26]. Unfortunately, few marketing tools and recommender systems have utilized these family characteristics.

This study chooses three profile tags that are representative of fa mily structure and life stage, including ‘infant’ (i.e., a family has an infant or not), ‘child’ (i.e., a family has a young child aged 4–17 or not), and ‘elder’ (i.e., a family has elders or not). This study also includes ‘car ownership’ (i.e., a family has a car or not) as an additional family tag. In a developing economy where not every family has a car, car ownership indicates not only the income level of a family but also the parking facility to provide and the geographic reach of a retailer. A few studies have demonstrated that these tags have an influence on consumer purchase behavior and recommender systems performance [18,19,23,24]. This set of family profiles are by no means comprehensive, but they are adequate to demonstrate the family profile mining process.

## 2.2. Learning from positive and unlabeled examples

From a technical perspective, customer profile mining from transaction data is essentially a classification problem. It has been defined as “the technology that allows building customer models each describing the specific habits, needs, and behavior of a group of customers” [12]. A customer model is a binary or multiclass classifier that assigns a specific tag or label to each customer. Training such a classifier with traditional classification algorithms requires a training set of labeled positive and negative examples. However, in many cases, only a few positive examples are labeled manually, and the remainder is unlabeled [27]. It is often expensive to manually label a large number of negative examples. A manual labeling process can also be subjective and erroneous for ambiguous cases [28,29]. In some cases, collecting negative examples is simply unfeasible.

Algorithms for learning from PU examples ofer a viable solution to address the lack of negative examples [28–30]. Learning from PU examples has also been called a partially supervised classification, positive-example-based learning, or PU learning (in this paper) [31]. Studies have found that by using only a few labeled positive examples and many unlabeled examples, PU learning algorithms can be almost as accurate as traditional supervised classification algorithms [32]. In this study, we first convert the family profiling problem into a PU learning problem.

Mainstream PU learning approaches can be classified into three categories. The first category completely ignores unlabeled examples and only learns from positive examples, for example, by regarding all unlabeled examples as negative examples or by using more advanced learning algorithms such as one-class support vector machines (SVMs) [31,33]. The second category includes two-step algorithms that attempt to identify a set of likely negative examples. Then, the known positive examples and likely negative examples are used to train a traditional classifier [28,29,34]. The third category consists of algorithms that directly use unlabeled examples to extract information about the un derlying probability distribution of the examples [35]. For example, positive Bayesian network classifiers (PBCs) learn Bayesian network models from PU data [36].

PU learning uses a diferent approach to evaluate the classification performance. Almost all performance measures of a classifier require a complete confusion matrix including the true positive, false positive, true negative, and false negative [37]. However, because negative examples are unlabeled in the PU setting, true negative and false positive rates cannot be calculated. To address this problem, some alternative PU performance measures have been proposed, such as pseudo-F [31] and positive and unlabeled learning performance (PULP) [38]. Pseudo-F uses the recovery of positive examples in PBCs to approximate the F1 score through the Bayes rule. PULP calculates the probability that random prediction can yield the same number of known positive samples as a classifier. A smaller probability indicates that the classifier is stronger in detecting more potential positive samples.

Although PU learning is a potentially powerful tool to identify target customers from a mixed dataset, most PU learning algorithms have been applied only to text mining [29] and computational biology [30]. Moreover, most of these algorithms have only focused on classification algorithms but omitted feature selection. For example, when PU learning algorithms classify documents with terms as features [29], they use all features to build classification models without feature se lection.

![](/api/attachments/6N5ED5FJ/fulltext/images/7ca6696fd8b944847579c63ce8a2eb8dc8130606993f4f376c013a532015d48c.jpg)  
Fig. 1. Family profiling algorithmic framework based on unlabeled transaction data.

## 2.3. Feature selection

In the context of supermarket customers, feature selection is necessary. Products that customers purchase form a very large feature set. A large set of features is likely to contain considerable redundant in formation and noise that could be a threat to both the eficiency and accuracy of learning algorithms [39]. Thus, it is necessary to perform feature selection to improve the prediction performance, accelerate the training process, and provide a more understandable model [40].

A feature selection process involves three decisions: feature subset search, feature subset evaluation, and criterion for halting the search [41]. In feature subset search, one must determine the starting point of a search and the direction of search. For example, the feature subset might start with nothing and add features individually or start with all features and remove them individually. These processes are known as forward selection and backward elimination [42]. In subset evaluation, one must evaluate the classification performance of a feature subset. Individual features can be evaluated using metrics of information theory (e.g., mutual information and information gain) or the model prediction performance when a feature is added. Finally, the criteria for halting the subset search might be defined as the moment when no feature candidate can further improve the prediction performance.

Studies have identified three types of feature selection: filter, wrapper, and embedded methods. The filter method first evaluates the relevance of an individual feature through correlation, mutual in formation, or information gain. Then, it constructs a “best” feature subset. A single model is established based on this subset [43]. The wrapper method uses the performance of a predetermined learning algorithm to evaluate the relevance of feature subsets. It can identify the optimal subset for a model. However, this method must build many models, making it computationally expensive [44]. The embedded method integrates feature selection into the model construction process. Thus, feature selection is automatically completed in the process of model construction. Examples of embedded methods include the least absolute shrinkage and selection operator (LASSO) and its variations [45].

Feature selection is an important issue in family profile prediction because customer transaction data involves thousands of products. Not all products (i.e., features) are relevant to the prediction of a specific profile. It is, therefore, necessary to find the most relevant feature for each profile.

## 3. Predicting family profiles: problem statement and proposed framework

Based on the assumption that a membership card represents a family in a supermarket, this study ofers a practical algorithmic framework to predict family profiles. With the collaboration of a Chinese supermarket chain, we obtained the following datasets: (1) a customer set $C = \{ u _ { 1 } , u _ { 2 } , u _ { 3 } , \dots , u _ { m } \}$ containing all members of the supermarket; (2) a product set $P = \{ p _ { 1 } , p _ { 2 } , p _ { 3 } , \ldots , p _ { n } \}$ containing all products; (3) a transaction set $R = \{ r _ { 1 } , r _ { 2 } , r _ { 3 } , \ldots , r _ { p } \}$ including the transaction flows of all members, where each record comprises the transaction time, member id, product description, purchase quantity, and purchase amount; and (4) product categories T as defined by the supermarket at an appropriate level of grouping. In this study, we define features according to the product categories. For instance, “stationery” is a feature that includes the total purchase amounts of all products (e.g., pen and paper) in this category.

Given C, P, R, and $T ,$ this study aims to identify customers whose families are most likely to have a certain tag. We choose ‘infant’, ‘child’, ‘elder’, and ‘car ownership’ as a representative set of family profiles. We propose a heuristic method to convert unlabeled data into partially labeled data. We assume that a retailer has only unlabeled transaction data, and our heuristic method first selects definite features, that are clear indicators for a certain family profile. Indefinite features are other features except for definite features. For examples, the definite features of the infant profile include diapers, baby food, and baby milk powder. Such heuristics can even be used to directly label customers. For example, an infant profile can be assigned to customers who have recently purchased definite features of infant profile. However, the simplistic tagging method based on definite features can miss customers who have a baby but do not purchase definite features from this store. Nevertheless, heuristics are useful to obtain partially labeled data. We aim to identify more infant families even if they have not purchased definite features of infant profile from this company.

As outlined in Fig. 1, our proposed framework consists of three stages: category feature construction, training set initialization, and PU learning with feature selection. Category feature construction is the data preparation stage that aggregates members' transactions by product categories, where each category is a product feature. We apply heuristics and classify features into definite and indefinite features for each family profile. We construct a positive sample based on definite features as well as an initial likely negative sample according to definite and indefinite features. Finally, the initial training set is fed to an iterative PU learning algorithm. Meanwhile, we embed a feature selection process into the algorithm to eliminate redundant information and boost the model training speed.

## 3.1. Category feature construction

The preference for diferent products manifests diferent customer profiles. In natural language processing and information retrieval, the frequency of each word in a document is employed as a feature to train classifiers. Similarly, we transform the purchase amount of each product category as a feature in the context of retailing because products in the same category have a very similar purpose. Eventually, we obtain 200 product categories (features) from the original SKUs, denoted as $P C = \{ c _ { 1 } , c _ { 2 } , c _ { 3 } , \ldots , c _ { k } \}$ . Each element of PC represents a category and each product belongs to only one category.

From customer set C, transaction set R, and product category set $P C ,$ we then create a customer-monetary matrix $M _ { m \times k }$ where m denotes the number of customers and k the number of product categories. Each element of the matrix $M _ { m \times k }$ is the purchase amount of a product category by a customer. Then, we normalize each column of $M _ { m \times k }$ to the interval of [0,1] by subtracting the minimum and dividing by the range. Normalization helps control for diferences in sales amounts across diferent categories. Normalization also makes the feature weights in the fitted model comparable.

To assess the importance of each product category to each customer, we follow the term frequency–inverse document frequency (TF-IDF) relevance measure used in information retrieval [46]. The importance of a product category to a customer increases in proportion to the number of times that the customer purchases products in this category; however, it is ofset by the number of customers who purchase product in the category. We create a customer-frequency matrix $Q _ { m \times k }$ from $C ,$ R, and PC. Each element of the matrix $Q _ { m \times k }$ is the purchase frequency of a customer in the corresponding product category. The importance weight of product category j to customer i can be calculated as<sup>1</sup>

$$
T I _ {i, j} = \frac {Q _ {i , j}}{\sum_ {j ^ {\prime} = 1} ^ {k} Q _ {i , j ^ {\prime}}} \times l o g \left[ \frac {m}{\sum_ {i ^ {\prime} = 1} ^ {m} I (Q _ {i ^ {\prime} , j} > 0)} \right].\tag{1}
$$

The first part of Eq. (1) measures how frequently customer i purchases product category j out of the sum of all purchase frequencies. In the second part of Eq. (1), I denotes an indicator function that is set to 1 if the condition is satisfied and 0 otherwise. The second part measures how unique the product category j is to identify customer i. Suppose very few customers have bought category j, the denominator is then small. Consequently, the second part is large. We then create a weight matrix $T I _ { m \times k } ,$ each element of which is the weight calculated by Eq. (1). Finally, we construct the category feature matrix $M _ { m \times k } ^ { }$ as the Hadamard product of $M _ { m \times k }$ and $T I _ { m \times k }$ , Columns of $M _ { m \times k }$ form the category feature set $F = \{ f _ { 1 } , f _ { 2 } , f _ { 3 } , \ldots , f _ { k } \}$

## 3.2. Training set initialization

A unique challenge of our unlabeled dataset is that we do not have labeled positive or negative examples. We must convert the problem to a PU learning one using heuristics. We manually select definite features for each profile based on discussions with supermarket professionals. For a given family profile, let $F _ { d e f }$ denotes the definite feature set; then, the indefinite feature set $F _ { i n d }$ is the diference between sets $F _ { d e f }$ and $F ,$ namely, $F _ { i n d } = F \setminus F _ { d e f } .$ We assign equal importance to all definite features of a given profile.

To identify positive examples, the frequency of purchasing definite features is used to indicate the probability that a customer belongs to the corresponding family profile. To alleviate the noise of an occasional purchase, we label those customers who have purchased definite features at least twice as reliable positive examples POS; these customers are further divided into a positive training set PT and a validation set PV. PT remains unchanged in the process of algorithm iteration. $P V ,$ as a hidden positive example, is used to test the recall of a model in the model building process. Except for PT, all other customers are called unlabeled customers UC.

To identify likely negative examples from UC, we rank customers in UC and regard those with a low rank as the negative set NEG. However, such customers have not bought any definite feature. Our solution is to rank them based on indefinite features. The weight of indefinite features is based on their relevance to definite features.

The association rule mining algorithm is used to find the relevance of indefinite features to definite features. An association rule captures the relationships between products based on their patterns of co-occurrence in diferent shopping baskets [47]. It is a rule that goes from the left-hand side (LHS) to the right-hand side (RHS) [48]. Finding association rules with the definite features as the LHS would help us to identify the most related indefinite features on the RHS.

The relevance of an indefinite feature to definite features is calcu lated as follows. To obtain the relevance weight of all indefinite features, we extract the transaction data of customers in PT and use the Apriori algorithm [49] without minimum support to generate all association rules with the LHS being a definite feature and the RHS being an indefinite feature. The time window of association rules is set to one week, which means that we define a shopping basket as a list of pro ducts that a customer buys within one week. To penalize the high-frequency RHS, we use lift to measure the usefulness of an association rule. For a given indefinite feature, its relevance is defined as the sum of the lift of all association rules with the RHS being the indefinite feature, and the LHS being one of the definite features.

The relevance weights of all indefinite features are normalized to the interval of [0,1]. Then, we can form a feature weight vector $W = \{ w _ { 1 } , w _ { 2 } , \dots , w _ { k } \}$ in which the value of an indefinite feature is its relevance weight and the value of a definite feature is 1. Based on $W ,$ the initial profile score of all customers can be calculated as

Score $\mathbf { \Psi } = M ^ { \prime } ( W ) ^ { T }$

(2)

We rank all customers in descending order of Score and label a bottom portion of UC with a low score as NEG. To avoid learning biases from an imbalanced training set, the size of NEG is the same as that of PT. Finally, PT and NEG together form the initial training set of our profiling algorithm.

## 3.3. A family profiling algorithm with feature selection

After initializing the training set, we integrate PU learning and feature selection techniques to design a novel family profiling algorithm. Our family profiling process is illustrated in Algorithm 1. This algorithm contains four main components: feature subset search, feature subset evaluation, negative example update, and criterion for halting the search.

## Algorithm 1. Family profiling with PU learning and feature selection.

Our main challenge is to classify customers who do not buy definite features with a classifier based on indefinite features. To build such a profile classification model, the first component of the algorithm (line 7, 8–26), the feature subset search is implemented as follows. Based on the assumption that the higher the relevance weight of an indefinite feature, the more relevant the feature is to a specific profile, we rank all indefinite features $F _ { i n d }$ in descending order of their relevance weight in W. The descending order of indefinite features remains constant throughout the iterations. Then, the feature subset starts with an empty set, and one ranked feature in $F _ { i n d }$ is added to the feature subset in each iteration.

![](/api/attachments/6N5ED5FJ/fulltext/images/43fbd78baef383655b68bcf4b6bff39001deac84eb17f544b085560cf9b1f1c3.jpg)  
Fig. 2. Example of halt conditions.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
1 Inputs: Customer set C; Reliable positive examples POS; Likely negative examples NEG; Indefinite feature vector  $F_{ind}$ ; Feature weight vector W; Demographic threshold D; Halt parameter  $\alpha$ 
2 Output: A vector recording the recall of validation set for each iteration Recall
3 Main Procedure:
4 initialize feature  $\leftarrow\emptyset$ , prob  $\leftarrow\emptyset$ , r  $\leftarrow0$ , l  $\leftarrow0$ 
5 split POS into positive training set PT and validation set PV
6 unlabeled customer set UC  $\leftarrow C\setminus PT$ 
7  $F_{ind} \leftarrow rank F_{ind}$  in descending order of W
8 for each feature  $f \in F_{ind}$  do
9 feature  $\leftarrow feature \cup \{f\}$ 
10 train a classifier  $\Phi$  by feature, PT and NEG
11 prob  $\leftarrow predict(UC,\Phi)$ 
12 label the top  $|D| - |PT|$  customers in prob in UC as positive and calculate recall R
13 if R &gt; r //if a new feature f increases recall
14 Recall  $\leftarrow Recall \cup \{R\}$  //save the new recall level
15 r  $\leftarrow R$  //update the latest high recall
16 l  $\leftarrow0$  //reset the counter for stagnant recall
17 else //if a new feature f does not increase recall
18 feature  $\leftarrow feature\setminus\{f\}$  //discard the indefinite feature
19 Recall  $\leftarrow Recall \cup \{r\}$  //save the latest high. The recalls in Fig. 2 is monotonic
20 l  $\leftarrow l+1$  //increase the counter for stagnant recall
21 end if
22 update NEG as the bottom |PT| customers in prob in UC
23 if l  $\geq\alpha$ 
24 break
25 end if
26 end for
</div>

Once the feature subset is established for each iteration (line 9), we first use PT and NEG to train a classifier. Logistic regression is used as the basic classifier because of its eficiency and good probabilistic in terpretations (line 10). Next, we use the classifier to predict the probability of UC being positive examples (line 11). Only a top portion of UC with high profile probability is marked as positive examples (line 12).

The portion is based on the demographic prior probability of each profile from other sources (see Section 4.1). For example, the car ownership rate is 30%, and we label this part of UC with high profile probability as positive examples. Finally, we calculate the proportion of PV correctly predicted as positive examples as the measure of model performance (line 12). This proportion is also called the recall of the validation set. The more positive examples a predictive model can recall from the validation set, the more likely it is to recall the unknown positive examples from unlabeled examples. Therefore, the recall of the validation set indicates the performance of the feature subset.

The third component of Algorithm 1 is to update NEG (line 22). Initial negative examples are likely to be inaccurate. To obtain a better sample of negative examples, we update negative examples every time when a new classifier is trained. After each iteration, a matching size of UC with the lowest profile probability is set as a new negative example for the next iteration.

Finally, the halt condition of our algorithm determines when to stop the iteration process (lines 23–25). In the iteration process of Algorithm 1, as the weights of indefinite features decrease, it becomes increasingly dificult to find predictive indefinite features for a specific profile. Thus, it is not necessary to iterate through all indefinite features. Omitting insignificant indefinite features serves three purposes: to implement feature selection, to avoid over fitting the data, and to save computation time.

The following example illustrates how the iteration progresses. In Fig. 2, the x-axis represents the number of iterations and the y-axis indicates the recall achieved at each iteration. To generate the data for Fig. 2, Algorithm 1 iterates through all indefinite features, and it saves the number of iteration, the recall of each iteration, and the consecutive iterations when the recall is stagnant (lines 13–21). In this example, the recall reaches its maximum at the 38th iteration and reaches at least 95% of the maximal recall at the 28th iteration. It is reasonable to stop the iteration process when the relative recall level reaches 95%. Before the 28th iteration, the maximal number of consecutive iterations when the recall remains stagnant is 6. We use parameter α as the halt parameter. It is set to the maximum number of consecutive iterations when the recall remains stagnant and the relative recall reaches 95% of the full recall. In this case, the value of the halt parameter α can be set to 7 (because when $\alpha = 6 ,$ the relative recall has not reached 95%).

While it is possible to obtain α for a profile by iterating through all estimates α with five times of five-fold cross-validation (i.e., 25 rounds of iterations in total).

Table 1  
Statistics of consumer purchase behavior.

<table><tr><td>Indicator</td><td>Mean</td><td>S.D.</td><td>Min</td><td>1st Qu.</td><td>Median</td><td>3rd Qu.</td><td>Max</td></tr><tr><td>Recency</td><td>171.2</td><td>207.1</td><td>1.0</td><td>12.0</td><td>60.0</td><td>321.0</td><td>730.0</td></tr><tr><td>Frequency</td><td>20.1</td><td>27.4</td><td>1</td><td>3</td><td>10</td><td>26</td><td>558</td></tr><tr><td>Monetary</td><td>2434.6</td><td>4615.1</td><td>0.62</td><td>382.8</td><td>1215.5</td><td>2997.5</td><td>252,119.6</td></tr><tr><td>Length</td><td>349.4</td><td>259.1</td><td>1.0</td><td>90.0</td><td>337.0</td><td>618.0</td><td>730.0</td></tr><tr><td># records</td><td>133.4</td><td>198.7</td><td>1.0</td><td>22.0</td><td>71.0</td><td>175.0</td><td>10,253.0</td></tr><tr><td># categories</td><td>34.1</td><td>24.0</td><td>1.0</td><td>14.0</td><td>31.0</td><td>51.0</td><td>172.0</td></tr></table>

The first component of Algorithm 2 (lines 3–22) scans recall vectors of all iterations (i.e., 25 in total) to create a dictionary to record relative recall levels for each value of l, where l is the number of consecutive iterations when the recall is stagnant. L is a vector to store the unique values of l. The relative recall levels of each l are recorded in the dictionary Dict with key l. After scanning all recall vectors, we sort Dict in the ascending order of its keys (i.e., values of l) (line 23). The second component of Algorithm 2 calculates the average recall for each level of l. When the average recall exceeds 95% for the first time, we set the associated key l as the final halt parameter α (lines 23–28). In other words, we pick the first l with an average relative recall level above 95% as the value of α.

## Algorithm 2. Estimating α.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inputs: recall vectors by five times of five-fold cross-validation Recalls
Output: optimal halt parameter  $\alpha$ 
Main Procedure:
initialize Dict ← empty dictionary
for each recall vector R ∈ Recalls do
    l ← 0, L ←  $\emptyset$ 
    for i = 2 to |R| do
    if  $R_i &gt; R_{i-1}$ 
    l ← 0
    Else
    l ← l + 1
    end if
    If l &gt; 0 and l ∉ L
    if l ∉ keys(Dict)
    Dict[l] ← { $R_i \div \max(R)$ }
    else
    Dict[l] ← Dict[l] ∪ { $R_i \div \max(R)$ }
    end if
    L ← L ∪ {l}
    end if
end for
end for
Dict ← sort Dict by the ascending order of its keys
for each key l in Dict do
    if mean(Dict[l]) ≥ 0.95
    $\alpha \leftarrow l$ 
    break
end for
</div>

indefinite features in a round, it is better to estimate α based on more rounds of iterations for statistical stability. Algorithm 1 generates a recall vector recall for each round of iterations. If we use the data subsets from the five-fold cross-validation process, we could generate five rounds of iterations. For more statistical stability, Algorithm 2

## 4. Empirical evaluation

## 4.1. Dataset

The supermarket that we cooperated with is a regional supermarket chain in eastern China. It ofered us the transaction data of all members in Shanghai from January 1, 2013, to December 31, 2014. The supermarket chain is one of the leading retail operators in Shanghai. Its mission is “to ofer a fresh and pleasurable shopping experience to all families”. As a local competitor of Walmart and Carrefour, the target market of the firm is the vast majority of people. Thus, we anticipate that our dataset is representative of the general populations in Shanghai.

Table 2  
Basic information of four family profiles.

<table><tr><td>Family profile</td><td>Demographic threshold</td><td># reliable positive examples</td><td>Definite features</td></tr><tr><td>Infant</td><td>5116</td><td>5750</td><td>Baby food, baby milk powder, baby food supplement, feeding accessories, infant wear, maternity bras, baby care, diaper</td></tr><tr><td>Child</td><td>11,313</td><td>5351</td><td>Kid&#x27;s health supplement, girl&#x27;s wear, boy&#x27;s wear, toys, kid&#x27;s bedding, kid&#x27;s furniture, school material, student bag, kid&#x27;s reading, kid&#x27;s electronic accessories, kid&#x27;s shoes</td></tr><tr><td>Elder</td><td>18,038</td><td>1557</td><td>Gen Seng/Aweto/Ganoderma, mend wine, basic functional supplement, diabetes patient food, drug</td></tr><tr><td>Car</td><td>15,879</td><td>1137</td><td>Engine oil, car fragrance, car accessories, car security, car cleaning</td></tr></table>

![](/api/attachments/6N5ED5FJ/fulltext/images/7dee4bf9df72949221f98b70055e67117e7a520342b45f8db10481a395b456e6.jpg)  
Fig. 3. Halt parameters and corresponding numbers of iterations.

We drew a random sample of 50,000 members and extracted their transaction records to predict their family profiles. Table 1 reports the descriptive statistics of consumer purchase behavior. Recency is the number of days between a customer's last purchase and December 31, 2014. If a customer's last purchase was on December 31, 2014, we set the customer's recency to 1. Frequency and monetary represent the number of purchases a customer has made and the amount of money (in Chinese Yuan) a customer has spent. Length is the number of days between the first purchase and the last purchase. If a customer only purchased once in the transaction data, we set the customer's length to 1. The last two indicators are the number of transaction records of a customer and the number of product categories (features) purchased by a customer.

Our profiling algorithm classifies customers above a certain threshold as positive. For each profile, this threshold is estimated based on the population demographic threshold, that is, the proportion of the population who are of this type.

(1) Infant: The sixth national census<sup>2</sup> shows that a family in Shanghai has 2.5 people on average. Therefore, 50,000 member cards cover approximately 125,000 people. We define an infant as a baby not yet 3. The total population of Shanghai in 2014 was 24.26 million and the number of babies born from 2010 to 2014 was 993,000.<sup>3</sup> Thus, we estimate that the demographic threshold of the infant profile is $1 2 5 0 0 0 \times ( 9 9 . 3 \div 2 4 2 6 ) \approx 5 1 1 6$

Table 3  
Indefinite feature selection and negative example update in each algorithm.

<table><tr><td>Algorithm</td><td>Indefinite feature selection</td><td>Negative example update</td></tr><tr><td>AFRN</td><td>All Features (no selection)</td><td>Random Negative examples (no update)</td></tr><tr><td>AFBN</td><td>All Features (no selection)</td><td>Bottom Negative examples</td></tr><tr><td>RFBN</td><td>Random order of Feature</td><td>Bottom Negative examples</td></tr><tr><td>DFBN</td><td>Descending order of Feature by relevance weight</td><td>Bottom Negative examples</td></tr></table>

(2) Child: Similar to the calculation of infant profile, we define a child as a person in the age range of 4–17. People who are younger than 18 made up 10.99% of the total population of Shanghai in 2014. Thus, we estimate that the demographic threshold of the child profile is 125000 $\times ( 1 4 \div 1 7 ) \times 1 0 . 9 9 \% \approx 1 1 3 1 3$

(3) Elders: People aged 60 years and above made up 28.86% of the total population of Shanghai in 2014. We assume that the average fa mily includes two elders. Therefore, we estimate that the demographic threshold of the elder profile is 125000 × 28.86 % ÷ 2 ≈ 18038.

(4) Car: In 2014. there were 8.25 million families in Shanghai, of which 2.62 million had cars. Therefore, we estimate that the demographic threshold of the car profile is $5 0 0 0 0 \times ( 2 . 6 2 \div 8 . 2 5 ) \approx 1 5 8 7 9 .$

Ideally, a profiling algorithm ranks customers by their profile probability. The top portion of customers above the demographic threshold is assigned the predicted tag. Table 2 presents the basic information of the four family profiles, including the demographic threshold, number of reliable positive examples, and definite features. Compared with the elder and car profiles, the infant and child profiles have more definite features. Consequently, these two profiles have a larger number of reliable positive examples. Notably, the number of reliable positive examples for the infant profile is higher than its demographic threshold, suggesting that the heuristic of treating those who buy definite features as infant families is already a high-recall tagging method. For other profiles, the profiling algorithm has to recover more “hidden” members.

Table 4  
Average recall of algorithms by family profile (% improvement).

<table><tr><td>Algorithm</td><td>Infant</td><td>Child</td><td>Elder</td><td>Car</td><td>All profiles</td></tr><tr><td>AFRN</td><td>26.00(1.54)</td><td>60.34(4.18)</td><td>61.41(13.91)</td><td>50.97(36.49)</td><td>57.57(17.18)</td></tr><tr><td>AFBN</td><td>19.51(35.32)</td><td>47.85(31.37)</td><td>69.90(0.07)</td><td>64.03(8.65)</td><td>60.59(11.34)</td></tr><tr><td>RFBN</td><td>22.44(17.65)</td><td>43.39(44.87)</td><td>62.52(11.88)</td><td>60.17(15.62)</td><td>55.36(21.86)</td></tr><tr><td>DFBN</td><td>26.40</td><td>62.86</td><td>69.95</td><td>69.57</td><td>67.46</td></tr></table>

The bold face indicates the best performance algorithm, DFBN in this case.

## 4.2. Halt parameter tuning

To strike a balance between the predictive power and computational eficiency, we follow the procedure in Algorithm 2 to estimate the optimal value of the halt parameter α. Furthermore, for each family profile, we calculate the average number of iterations of five-fold crossvalidation under the condition that the halt parameter is set at the optimal value. Fig. 3 shows the values of the halt parameter and the average number of iterations for diferent profiles. The halt parameters and the average number of iterations are relatively low for the infant and child profiles and higher for the elder and car profiles. A plausible reason is that the definite features of the elder and car profiles have a lower purchase frequency.<sup>4</sup> That is, the definite features of the two profiles are less likely to co-occur with their indefinite features in the same shopping basket. Therefore, it is more dificult to find predictive indefinite features based on definite features for the two profiles.

## 4.3. Model comparison

We defined four other family profiling algorithms as benchmarks for comparison. As illustrated in Table 3, the AFRN algorithm is the only non-iterative algorithm. It randomly selects unlabeled customers as negative examples and uses all indefinite features to train a classifier. The number of negative examples is set to the number of positive training examples. The AFBN algorithm uses the method described in Section 3.2 to sort customers in the descending order of a profile score and selects the bottom customers as likely negative examples. In each iteration, it uses all features to train a classifier and updates negative examples according to the profile probability predicted by the classifier. The RFBN algorithm employs the same negative example update method as AFBN. However, RFBN includes a feature selection process, but it adds indefinite features to the model in the random order of re levance weight. The DFBN algorithm is our proposed family profiling algorithm, as described in Section 3.

We use these four algorithms to predict diferent family profiles with the optimal halt parameter obtained as described in Section 4.2. We evaluate the performance of each algorithm using five times of fivefold cross-validation. Table 4 reports the average recall of diferent algorithms by family profiles. The values in parentheses are the relevant improvements of the proposed algorithm (DFBN) over the three comparison algorithms. On average, the DFBN algorithm outperforms the other three algorithms by 17.18%, 11.34%, and 21.86%.

The demographic threshold and the number of positive training examples both have an impact on the algorithm performance. A larger |D| and a smaller |PT| result in a larger recall. We define recall lift as the ratio of the recall of DFBN to the recall of random prediction. Assume that the unlabeled customers are evenly distributed in the validation set; then, the random recall is $( | D | - | P T | ) / ( | C | - | P T | )$ . We find that the recall lifts of the four profiles are 23.52, 4.13, 2.04, and 2.35, respectively. Although the absolute recall of the DFBN algorithm for infant and child profiles is relatively small, the recall lifts of these two profiles are higher than those of the elder and car profiles.

## 5. The sensitivity of the algorithm to partial definite features

The performance of our family profiling algorithm depends on the algorithm user's choice of the initial set of definite features because they afect both the assumed positive examples and the consequent choice of indefinite features. However, a user of the algorithm might not be able to identify all definite features because of lack of experience or the dificulty in identifying definite features for certain profiles. Thus, we design an experiment to examine how partial experience (i.e., incomplete definite features) influences the performance of the DFBN algorithm.

Without loss of generality, we take the infant and elder profiles as examples because they represent the two ends of the spectrum. The definite features of the infant profile are the most indicative, while the definite features of the elder profile are the least. In the experiment, we divide the definite features of each profile into two subsets. The first subset (labeled as S1) is used to train the profiling model. The second subset (labeled as S2) is used as hidden definite features to verify whether the model trained by S1 can retrieve customers who have purchased products of S2.

The testing procedure is as follows. For each partial experience, S1 varies in size (e.g., we could choose one to seven out of the eight definite features of the infant profile). Similarly. S2 as the complement of S1 also varies in size. For each size of S1, a DFBN model is trained for every combination of S1. For each combination, we label the customers who have purchased products of S1 at least twice as reliable positive examples. Then, we randomly divide these customers into a positive training set and a validation set in a ratio of 8:2. Meanwhile, we define customers who have purchased S2 at least twice as a test set. Finally, we calculate the recall lift of the validation and test sets.

To measure the performance of the algorithm with regard to the size of S1, we use the average recall lift of all combinations of S1 at a size. Fig. 4 shows the average recall lift of the validation set and the test set for diferent sizes of S1. For the infant profile, as the number of definite features increases, the average recall lift of the validation set gradually approaches the recall lift of the full set of definite features, the value of which is 23.52 (Section 4.3). Even when S1 has only one definite feature, the average recall of the validation set is still at least three times larger than that of random prediction. For the elder profile, as the number of definite features increases, the recall lift of the validation set has not improved as much as the infant profile. Despite this, the average recall of the validation set is about twice as large as that of random prediction when S1 has only one definite feature. This suggests that the DFBN algorithm still works with a partial experience, although its performance sufers. Moreover, the average recall lift of the test set is higher than that of the validation set for both profiles, suggesting that the DFBN algorithm can use S1 to identify customers of S2 and thus retrieve more hidden positive examples. Overall, the above result indicate that the DFBN algorithm is useful even with partial experience.

![](/api/attachments/6N5ED5FJ/fulltext/images/2667b2ff4a574d7be56520bf87fa809bcbd364f1e43adca802741478e2714141.jpg)  
Fig. 4. Average recall lift of the validation and test sets for diferent partial experiences.

Table 5  
Statistics of customer-feature rating matrix for each profile.

<table><tr><td rowspan="2">Profile</td><td rowspan="2"># profile-related features</td><td colspan="2"># customers with target profile</td><td colspan="2">Density on all features</td><td colspan="2">Density on profile-related features</td></tr><tr><td> $C_{old}$ </td><td> $C_{new}$ </td><td> $C_{old}$ </td><td> $C_{new}$ </td><td> $C_{old}$ </td><td> $C_{new}$ </td></tr><tr><td>Infant</td><td>21</td><td>5116</td><td>1023</td><td>28.11%</td><td>23.93%</td><td>21.10%</td><td>18.27%</td></tr><tr><td>Child</td><td>36</td><td>11,313</td><td>2262</td><td>26.51%</td><td>25.86%</td><td>16.78%</td><td>16.39%</td></tr><tr><td>Elder</td><td>22</td><td>18,038</td><td>3607</td><td>21.39%</td><td>24.14%</td><td>10.38%</td><td>12.00%</td></tr><tr><td>Car</td><td>22</td><td>15,879</td><td>3175</td><td>24.13%</td><td>23.55%</td><td>13.06%</td><td>14.49%</td></tr></table>

## 6. Application in profile-based product recommendation

One way to illustrate the value of the algorithm is to apply family profiles to profile-based product recommendations. Such recommendation also suggests how a retailer can make product ofering decisions based on family profiles. Given a family profile, we define the union of definite features and selected indefinite features as profile-related features. Our hypothesis is as follows: If a family profile reflects customers' needs, the profile tag should boost the prediction accuracy of customers' purchase amount of profile-related features.

The process of customer-based collaborative filtering is used for product recommendations. For each customer, we look for customers who have the same profile tag and have a similar preference for the profile-related features. For example, to predict customers' purchase amounts for an infant-related feature, we should select their neighbors from those customers with an infant profile. This filter mechanism reduces the interference of features unrelated to the infant profile. Based on this idea, we use the contextual pre-filtering approach [50] to compare the performance of two nearest neighbor selection strategies: global neighbor selection and local neighbor selection. For a given customer, global neighbor selection refers to the selection of a customer's nearest neighbors from all customers in the dataset, and local neighbor selection refers to the selection of nearest neighbors only from customers with the same target profile. Our experiment includes the following steps.

(1) Predict a new customer's family profiles: We use the transaction data of 50,000 customers (labeled as $C _ { o l d }$ in Section 4.1 to build a DFBN family profiling model (labeled as M). Model M gives the coefficients of selected indefinite features. Then, we use all profile-related features (i.e., definite features and selected indefinite features) and the profiles predicted by model M to train a new logistic model (labeled as L). Model L is the final model used to predict the profile of 10,000 new customers (labeled as $C _ { n e w } )$ selected randomly from among the remaining members. Those whose rank of profile score is above the de mographic threshold are assigned the corresponding profile tag.

(2) Construct a product purchase training set and a test set: The aim of the experiment is to use the transaction data of $C _ { o l d }$ to predict the purchase amount of the profile-related features for $C _ { n e w } .$ As a common practice, we convert the purchase amount of each feature of $C _ { o l d }$ to a 1–5 rating based on its quantiles and use the converted rating data as the training set. For each feature of $C _ { n e w }$ we also apply the quantiles of $C _ { o l d }$ as cutof points to convert their purchase amounts to a 1–5 rating. For each $C _ { n e w }$ we randomly select a rating of a profile-related feature to form the test set. Table 5 shows the statistics of the customer-feature rating matrix for each profile. In this table, density refers to the proportion of nonempty ratings in the rating matrix of customers.

(3) Predict ratings by collaborative filtering: We use the K nearest neighbors approach to select a group of customers in $C _ { o l d }$ as the nearest neighbors of a customer in $C _ { n e w } .$ Nearest neighbors' ratings for the target profile-related feature are aggregated to predict the new customer's feature rating with a customer-based mean-centering approach [51]:

$$
\widehat {r} _ {u i} = \overline {{r}} _ {u} + \frac {\sum_ {v \in N _ {u}} w _ {u v} (r _ {v i} - \overline {{r _ {v}}})}{\sum_ {v \in N _ {u}} | w _ {u v} |}\tag{3}
$$

where $\widehat { r } _ { u i }$ is the predicted rating of customer u for feature $i , \overline { { r } } _ { u }$ and $\overline { { r } } _ { \upsilon }$ are respectively the average ratings of customers u and $\mathfrak { v } , N _ { u }$ is the top K nearest neighbors of customer u, $w _ { u v }$ is the cosine similarity between customer u and customer $\mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } } \mathbf { \delta } _ { \mathbf { \delta } }$ and $r _ { b i }$ is the actual rating of customer υ for feature i. The first term $\overline { { r } } _ { u }$ represents one's average preference for a product. The second term measures how one's nearest neighbors prefer a product over other products, weighted by their similarity to the focal customer.

(4) Evaluate the prediction accuracy: We measure the prediction accuracy using three popular metrics: mean absolute error (MAE), root mean square error (RMSE), and coverage. Coverage refers to the percentage of feature ratings that can be predicted by collaborative filtering. Because an individual's rating of a feature depends on their neighbors' ratings of the feature, if none of the neighbors have bought the feature, the feature becomes unpredictable. MAE and RMSE are calculated based on the predicted rating $\widehat { r } _ { u i }$ and actual rating $r _ { u i }$ in the test set. MAE is defined as

![](/api/attachments/6N5ED5FJ/fulltext/images/a7c85e8bd4e645f8561fb44cefc4f37880118ee5298a32e5977b808b54414828.jpg)  
Fig. 5. The impact of local neighbor proportion on prediction performance.

![](/api/attachments/6N5ED5FJ/fulltext/images/2cc751316772d23f04aebec2e7452efde04f35d7ef3a5607faea74c69bcb8b02.jpg)  
Fig. 6. Prediction performance of the global and local neighbor selection.

Table 6  
The average improvement of local to global neighbor selection.

<table><tr><td>Profile</td><td>Metrics</td><td>Global</td><td>Local best</td><td>Local worst</td></tr><tr><td rowspan="3">Infant</td><td>MAE</td><td>1.283</td><td>1.191 (7.17%)</td><td>1.248 (2.73%)</td></tr><tr><td>RMSE</td><td>1.536</td><td>1.419 (7.62%)</td><td>1.491 (2.93%)</td></tr><tr><td>Coverage</td><td>94.76</td><td>98.84 (4.31%)</td><td>98.68 (4.14%)</td></tr><tr><td rowspan="3">Child</td><td>MAE</td><td>1.256</td><td>1.215 (3.26%)</td><td>1.235 (1.67%)</td></tr><tr><td>RMSE</td><td>1.498</td><td>1.439 (3.94%)</td><td>1.468 (2.00%)</td></tr><tr><td>Coverage</td><td>96.49</td><td>99.65 (3.27%)</td><td>99.38 (3.00%)</td></tr><tr><td rowspan="3">Elder</td><td>MAE</td><td>1.222</td><td>1.199 (1.88%)</td><td>1.217 (0.42%)</td></tr><tr><td>RMSE</td><td>1.480</td><td>1.436 (3.02%)</td><td>1.469 (0.76%)</td></tr><tr><td>Coverage</td><td>99.37</td><td>99.20 (2.94%)</td><td>98.49 (2.20%)</td></tr><tr><td rowspan="3">Car</td><td>MAE</td><td>1.179</td><td>1.167(1.03%)</td><td>1.176 (0.26%)</td></tr><tr><td>RMSE</td><td>1.433</td><td>1.405 (1.91%)</td><td>1.420 (0.85%)</td></tr><tr><td>Coverage</td><td>96.97</td><td>99.42 (2.52%)</td><td>98.44 (1.52%)</td></tr></table>

$$
\mathrm{MAE} = \frac {\sum_ {u , i \in \mathrm{T}} | r _ {u i} - \widehat {r} _ {u i} |}{| \mathrm{T} |}\tag{4}
$$

where ∣T∣ is the number of ratings in the test set, $r _ { u i }$ is the actual rating of customer u for feature i, and $\widehat { r } _ { u i }$ is the predicted rating of customer u for feature i. RMSE is defined as

$$
\mathrm{RMSE} = \sqrt {\frac {\sum_ {u , i \in \mathrm{T}} (r _ {u i} - \widehat {r} _ {u i}) ^ {2}}{| \mathrm{T} |}}\tag{5}
$$

In neighbor-based recommender systems, the size of neighbors has a significant impact on the recommendation quality. To examine the effect of neighbor size, we vary K from 20 to 200 in steps of 20 in all the following experiments.

In both global and local nearest neighbor selection, the distance between two customers is based on cosine similarity. In local neighbor selection, we also define the candidate set based on their profile probability scores. For example, we could select customers with top 10% profile probability as local neighbor candidates for a new cus tomer. This filtering is expected to generate a more accurate rating prediction. We vary the proportion of local neighbors from 10% to 100% in steps of 10%. For each proportion, we use the collaborative filtering algorithm to predict ratings in the test set at diferent K values and calculate the three performance measures.

Fig. 5 shows the impact of the local neighbor proportion on prediction performance. It indicates that the proportion of local neighbors does afect the prediction performance. For MAE and RMSE, a high proportion of local neighbors may include unnecessary noise owing to the presence of low-quality neighbors. For each profile, the optimal proportions for MAE and RMSE are 10%, 30%, 40%, and 40% respec tively. By contrast, the coverage decreases as the proportion of local neighbors increases, suggesting that customers with high profile probability tend to purchase more profile-related features; consequently, the target rating is more likely to be predictable. Among all local neighbor proportions, we identify two values, one representing the best performance (‘Local\_best’) and the other representing the worse performance (‘Local\_worst’).

After examining the impact of diferent local neighbor proportions, we continue to compare the prediction performance of global neighbor selection and local neighbor selection. For each performance measure of each profile, we show the predicted results at diferent K values for global neighbor selection and local neighbor selection. For local neighbor selection, the local best and local worst proportions are used. Fig. 6 shows the prediction performance as K is increased from 20 to 100. All curves level of after K = 100. The area between the local best and local worst is displayed in grey. The best results of the local neighbor selection show an apparent improvement compared with the results of the global neighbor selection. The worst results of the local neighbor selection show a smaller improvement of MAE and RMSE, especially for the elder and car profiles. Overall, as indicated in Table $^ { 6 , }$ the local neighbor selection consistently outperforms the global neighbor selection in the three performance measures.

## 7. Discussion and conclusion

Customer profiles are the foundation of understanding who the customers are. They are suggestive of which products can meet customers' individual and family needs. However, a critical gap in the use of customer profiles is the lack of an efective method to mine family profiles. Therefore, this study focuses on the mining of family profile [11,12].

In terms of algorithms, this study proposes a novel algorithmic framework to classify unlabeled data. Unlabeled data is often regarded as a domain for unsupervised learning. However, our algorithm can accommodate users' experience in the problem domain and convert unlabeled data into partially labeled data for PU learning. This type of method has not been explored thus far. It ofers a viable solution to the classification challenges when a labeled training set is impossible or very costly to obtain.

This study also advances traditional PU learning by integrating feature selection. The association-rule-based feature selection process of this algorithm enables an equivalent set of features to be obtained for the prediction of customer profiles if a definite feature set is unobservable. Previous feature selection algorithms aim to reduce the dimension, whereas this study proposes a new use of feature selection, namely, to find a nearly equivalent indefinite feature set for a definite feature set.

Our proposed algorithm can achieve a higher recall rate than benchmarks that use diferent indefinite feature selection methods and negative example construction strategies. Our experiments also further verify its efectiveness in the case of partial experience and showcase it application for product recommendations.

## 7.1. Managerial implications

This study ofers very practical managerial implications for retailing firms. It addresses the question of “who are customers” with family profile tags predicted by a novel family profile mining algorithm. It addresses the question of “which products to ofer” by relating the family profile to the definite and selected indefinite features of the profile.

Firms can use family profiles to cluster families. Consequently, we can summarize diferent family structures and classify families into groups. For example, a cluster with high scores in the child, elder, and car profiles can be labeled as middle-class families with three generations. Another cluster might have a high score only in the infant profile. We can label them as young couples with an infant. Our exploratory clustering results clearly reveal such patterns. With such derived family profile tags, more target-driven product oferings and marketing methods can be implemented.

Firms can use our algorithm to design product bundles for crossselling. Compared with general cross-selling methods such as association rules, our proposed algorithm can deduce features sets that are specific to a profile. Thus, we can design product bundles using the profile-related features to meet the specific needs of a segment.

Firms can use this algorithm for precision targeting. Consider the following two situations: (1) Under the condition of a fixed marketing budget, marketers can reach only a certain number of customers. In this case, our algorithm can target those top-ranked potential customers with the profile of interest. (2) Under the condition of fixed coverage in which marketers aim to cover a certain proportion of target customers, our algorithm can guide marketers to limit target customers to a smaller but more precise range, thereby reducing marketing costs while achieving the coverage goal. In both cases, with demographic thresholds or other business criteria, firms can use the proposed framework to target a certain number of customers with the highest probability of the target profile.

Firms can use this algorithm for product recommendations. While traditional recommender systems have employed transaction data to recommend products [2,4], they are not capable to generate a recommendation for new customers with no transaction history [6]. They also fail to utilize customer profiles such as personal disposition for product recommendation [5]. Product recommendation based on cus tomer profile is known as knowledge-based filtering [7,8]. Once the family profiles of a customer are predicted, knowledge-based product recommendations can be applied to complement transaction based recommendation.

Besides the implication for the retail industry, our framework might be applied to other business problems where a firm has only partial behavior records of a customer. For example, in the field of online advertising, demand-side platforms (DSPs) collect Internet users' visits to some websites. They want to deliver an ad to the audience of the right profile. Since a DSP has only a partial browsing history of a user, the DSP can use our framework to predict users' interest profiles, consequently achieving a higher conversion rate. Similarly, the algorithm can be used to tag customers' movie and music preference even when a digital content provides does not have customers' full consumption records. Another application is text classification. Assume that we can manually label only some positive examples and identify a few definite features (i.e. words) related to a specific topic, we can use the proposed framework to find more relevant features to complete a semi-supervised classification.

## 7.2. Limitations and future work

This study could be extended in several directions. First, although our algorithm can accommodate domain insights in the form of heuristics, its performance could be sensitive to the choice of initial definite features. In addition, the algorithm initially treats all definite features with equal importance. Future work can design more rigorous procedures to improve the quality of definite features. A more fine-grained weighting scheme should explore the quality of definite features. Second, in the process of inferring the weight of indefinite features, we set the time window of association rules as 1 week. That is, we assume that an indefinite feature has predictive power only if the indefinite feature and a definite feature have been purchased together within 1 week. Other time windows can be explored for diferent purchase habits and product attributes. Third, we adopt a forward feature se lection process based on the weight ranking of indefinite features. Because many feature selection methods have been proposed, future studies can employ other feature selection methods to yield improved results. Fourth, any classifier that can produce a probabilistic result can be embedded in our proposed framework. Future studies can investigate classification methods other than logistic regression. Finally, we only test four family profile tags in this study. Future studies can explore more family profile tags and their applications.

## Declarations of interest

None.

## Acknowledgment

This work was supported by the National Natural Science Foundation of China under Grant #71531006, #71490721 and #71871065, and the Program for Professor of Special Appointment (Eastern Scholar) at Shanghai Institutions of Higher Learning.

## References

[1] V. Kumar, D. Shah, Building and sustaining profitable customer loyalty for the 21st century. J Betail. 80 (2004) 317–330

[2] C. Park, Y. Kim, A framework of dynamic CRM: linking marketing with information

strategy, Bus. Process. Manag. J. 9 (2003) 652–671.

[3] G. Adomavicius, A. Tuzhilin, Using data mining methods to build customer profiles, Computer 34 (2001) 74–81.

[4] G. Adomavicius, R. Sankaranarayanan, S. Sen, A. Tuzhilin, Incorporating contextual information in recommender systems using a multidimensional approach, ACM Trans. Inf. Syst. 23 (2005) 103–145.

[5] V. Salonen, H. Karjaluoto, Web personalization: the state of the art and future avenues for research and practice, Telematics Inform. 33 (2016) 1088–1104.

[6] R. Burke, Hybrid recommender systems : survey and experiments, User Model User-Adap. Inter. 12 (2002) 331–370.

[7] J. Bobadilla, F. Ortega, A. Hernando, A. Gutiérrez, Recommender systems survey, Knowl.-Based Syst. 46 (2013) 109–132

[8] R. Burke, A case-based reasoning approach to collaborative filtering, Adv. Case Based Reason, (2000) 370–379

[9] T.P. Beane, D.M. Ennis, Market segmentation: a review, Eur. J. Mark. 21 (1987) 20–42.

[10] G. Long, M.K. Hogg, M. Hartley, S.J. Angold, Relationship marketing and privacy: exploring the thresholds, J. Mark. Pract. Appl. Mark. Sci. 5 (1999) 4–20.

[11] J. Vesanen, M. Raulas, Building bridges for personalization: a process model fo marketing, J. Interact. Mark. 20 (2006) 5–20.

[12] L.B. Romdhane, N. Fadhel, B. Ayeb, An eficient approach for building customer profiles from business data, Expert Syst. Appl. 37 (2010) 1573–1585.

[14] L.A. Petrison, R.C. Blattberg, P. Wang, Database marketing, J. Interact. Mark. 11 (1997) 109–125.

[15] F.V. Cespedes, H.J. Smith, Database marketing: new rules for policy and practice, Sloan Manag. Rev. 34 (1993) 7.

[16] E.K. Clemons, B.W. Weber, Segmentation, diferentiation, and flexible pricing: experiences with information technology and segment-tailored strategies, J. Manag. Inf. Syst. 11 (1994) 9–36.

[17] R. Kahan, Using database marketing techniques to enhance your one-to-one marketing initiatives, J. Consum. Mark. 15 (1998) 491–493.

[18] S. Commuri, J.W. Gentry, Opportunities for family research in marketing, Acad. Mark. Sci. Rev. 2000 (2000) 1.

[19] P. Kaur, R. Singh, Children in family purchase decision making in India and the West: a review, Acad. Mark. Sci. Rev. 2006 (2006) 1.

[20] S. Wang, B.B. Holloway, S.E. Beatty, W.W. Hill, Adolescent influence in family purchase decisions: an update and cross-national extension, J. Bus. Res. 60 (2007 1117-1124.

[21] P.C. Verhoef, P.N. Spring, J.C. Hoekstra, P.S.H. Leeflang, The commercial use of segmentation and predictive modeling techniques for database marketing in the Netherlands, Decis. Support. Syst. 34 (2002) 471–481.

[22] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decis. Support. Syst. 31 (2001) 127–137.

[23] W. Hong, L. Li, T. Li, Product recommendation with temporal dynamics, Expert Syst. Appl. 39 (2012) 12398–12406.

[24] P. Jiang, Y. Zhu, Y. Zhang, Q. Yuan, Life-stage prediction for product recommendation in e-commerce, SIGKDD 2015, Proceedings of the 21st ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2015, pp. 1879-1888.

[25] M. Bauer. K.J. Auer-Srnka, The life cycle concept in marketing research. J. Hist. Res Mark, 4 (2012) 68–96

[26] P.E. Murphy. W.A. Staples, A modernized family life cycle. J. Consum. Res. 6 (1979 12–22.

[27] Y.H. Lee, P.J.H. Hu, T.H. Cheng, Y.F. Hsieh, A cost-sensitive technique for positiveexample learning supporting content-based product recommendations in B-to-C ecommerce, Decis. Support. Syst. 53 (2012) 245–256.

[28] H. Yu, J. Man, K.C.C. Chang, PEBL: web page classification without negative examples, IEEE Trans. Knowl. Data Eng, 16 (2004) 70–81

[29] B. Liu, W.S. Lee, S. Yu. X. Li, Partially supervised classification of text documents ICML 2002, Proceedings of the Nineteenth International Conference on Machine Learning. 2002, pp. 387–394

[30] R.T.-H. Tsai, H.-C. Hung, H.-J. Dai, Y.-W. Lin. W.-L. Hsu, Exploiting likelv-positive and unlabeled data to improve the identification of protein-protein interaction ar ticles, BMC Bioinforma. 9 (Suppl. 1) (2008) S3.

[31] B. Calvo, I. Inza, P. Larrañaga, J.A. Lozano, Wrapper positive Bavesian network classifiers, Knowl. Inf. Syst. 33 (2012) 631–654.

[32] X. Wang, Z. Xu, C. Sha, M. Ester, A. Zhou, Semi-supervised learning from only positive and unlabeled data using entropy, Web-Age Information Management, 2010, pp. 668–679.

[33] L.M. Manevitz, M. Yousef, N. Cristianini, J. Shawe-Taylor, B. Williamson, One-class SVMs for document classification, J. Mach, Learn, Res, 2 (2001) 139–154

[34] B. Liu, Y. Dai, X. Li, W.S. Lee, P.S. Yu, Building text classifiers using positive and unlabeled examples, Third IEEE International Conference on Data Mining, 179 2003.

[35] F. Denis, PAC learning from positive statistical queries, Algorithmic Learn. Theory (1998).112-126.

[36] B. Calvo. P. Larrañaga, LA. Lozano. Learning Bavesian classifiers from positive and unlabeled examples, Pattern Recogn. Lett, 28 (2007) 2375–2384.

[37] P. Baldi, S. Brunak, Y. Chauvin, C.A.F. Andersen, H. Nielsen, Assessing the accuracy of prediction algorithms for classification: an overview, Bioinformatics 16 (2000) 412-424.

[38] S. Hajizadeh, Z. Li, R.P.B.J. Dollevoet, D.M.J. Tax, Evaluating classification performance with only positive and unlabeled samples, Joint IAPR International Workshops on Statistical Techniques in Pattern Recognition (SPR) and Structura

and Syntactic Pattern Recognition (SSPR), 2014, pp. 233–242.

[39] P. Ristoski, H. Paulheim, Feature Selection in Hierarchical Feature Spaces, Springer International Publishing, 2014.

[40] I. Guyon, A. Elisseef, An introduction to variable and feature selection, J. Mach. Learn, Res, 3 (2003) 1157–1182

[41] A.L. Blum, P. Langley, Selection of relevant features and examples in machine learning, Artif. Intell. 97 (1997) 245–271.

[42] S. Derksen, H.J. Keselman, Backward, forward and stepwise automated subset selection algorithms: frequency of obtaining authentic and noise variables, Br. J. Math. Stat. Psychol. 45 (1992) 265–282

[43] O. Reyes, C. Morell, S. Ventura, Scalable extensions of the ReliefF algorithm for weighting and selecting features on the multi-label learning context, Neurocomputing 161 (2015).168–182

[44] R. Kohavi, G.H. John, Wrappers for feature subset selection, Artif. Intell. 97 (1997) 273–324.

[45] R. Tibshirani, Regression shrinkage and selection via the lasso, J. R. Stat. Soc. Ser. B (Methodol.) (1996) 267–288.

[46] J. Ramos, Using TF-IDF to determine word relevance in document queries, Proceedings of the First Instructional Conference on Machine Learning. 2003.

[47] B. Mobasher, H. Dai, T. Luo, M. Nakagawa, Efective personalization based on association rule discovery from web usage data, Proceedings of the 3rd Internationa Workshop on Web Information and Data Management, 2001, pp. 9–15.

[48] Z. Zheng, R. Kohavi, L. Mason, Real world performance of association rule algorithms. Proceedings of the Seventh ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2001, pp. 401–406.

[49] R. Agrawal, R. Srikant, Fast algorithms for mining association rules, Proceedings of the 20th International Conference on Very Large Data Bases, 1215 1994, pp. 487–499.

[50] U. Panniello, M. Gorgoglione, Incorporating context into recommender systems: an empirical comparison of context-based approaches, Electron. Commer. Res. 12

(2012) 1–30.

[51] F. Ricci, L. Rokach, B. Shapira, Introduction to recommender systems handbook, Recommender Systems Handbook, Springer, 2011, pp. 1–35.

Shaohua Lian is a Ph.D. candidate at the department of Information Management and Information Systems, School of Management, Fudan University, Shanghai, China. His research interests include precise targeting, recommender systems, and predictive analytics.

Yunjie Xu is a professor at the School of Management. Fudan University. Shanghai China. He got his Ph.D. in Management Information Systems from Syracuse University, New York. His research interests cover electronic commerce, knowledge management, and online social network analysis. His publications appeared in Information Systems Research, Journal of Management Information Systems, Journal of Association for Information Systems, Journal of the American Society for Information Science and Technology, IEEE Transactions on Professional Communication, Communication of the ACM, International Journal of Electronic Commerce, Journal of Retailing, Decision Support Systems, and more.

Cheng Zhang received the Ph.D. degree in Information Systems from the National University of Singapore, Singapore. He is a Professor in the School of Management, Fudan University, Shanghai, China. His publications have appeared in MIS Quarterly, Marketing Science, Journal of Marketing, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, European Journal of Information Systems, Decision Support Systems, Journal of Electronic Commerce Research. Journal of International Marketing. and Journal of Global Information Management. His research interests include electronic commerce. the diffusion of in formation technologies, and online social network analysis.
