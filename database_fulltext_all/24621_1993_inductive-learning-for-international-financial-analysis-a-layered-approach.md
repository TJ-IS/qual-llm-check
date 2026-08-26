---
otero_id: 24621
otero_key: "YEDHHZ2E"
title: "Inductive Learning for International Financial Analysis: A Layered Approach"
authors: "Antoinette C. Tessmer; Michael J. Shaw; James A. Gentry"
year: "1993"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1993.11517976"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Inductive Learning for International Financial Analysis: A Layered Approach

Antoinette C. Tessmer, Michael J. Shaw & James A. Gentry

To cite this article: Antoinette C. Tessmer, Michael J. Shaw & James A. Gentry (1993) Inductive Learning for International Financial Analysis: A Layered Approach, Journal of Management Information Systems, 9:4, 17-36, DOI: 10.1080/07421222.1993.11517976

To link to this article: http://dx.doi.org/10.1080/07421222.1993.11517976

![](/api/attachments/YEDHHZ2E/fulltext/images/7e24114a7adb959557a3c18a8bc027cbb1c63796cb7c8a930c4b67b13eac0ab4.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/YEDHHZ2E/fulltext/images/abdf99306e4dbf41bc4ad3e4f7f00f62449e2713a31c2de8746d36892e2eb73f.jpg)

Submit your article to this journal ↗

![](/api/attachments/YEDHHZ2E/fulltext/images/74e13611842432f6e2f2205377c589c5eef9179be77dc466fcf77dc4ef5ac304.jpg)

View related articles ↗

![](/api/attachments/YEDHHZ2E/fulltext/images/a2a5d1aa4b60b39cc9d34441b5d670e2d634c51cfe2a8deb1a101ff7e3cd7887.jpg)

Citing articles: 1 View citing articles ↗

# Inductive Learning for International Financial Analysis: A Layered Approach

ANTOINETTE C. TESSMER, MICHAEL J. SHAW,

AND JAMES A. GENTRY

ANTOINETTE C. TESSMER is a Visiting Assistant Professor at the Department of Finance of the University of Illinois at Urbana-Champaign, and a postdoctoral researcher at the Beckman Institute for Advanced Science and Technology. Dr. Tessmer earned a graduat in computer science at IESN, Namur, Belgium, a licence in applied economic sciences at the Catholic University of Mons, Belgium, and a doctorate in finance/information science at the University of Namur, Belgium. Prior to visiting the Department of Finance, she was a Visiting Scholar at the Beckman Institute for Advanced Science and Technology for two years, under a doctoral fellowship from the Intercollegiate Center for Management Science, Brussels. Her research interests include knowledge acquisition, machine learning, and decision support systems for international decision processes.

MICHAEL J. SHAW is an Associate Professor of Information Systems at the Department of Business Administration. He also has been a research faculty member at the Beckman Institute for Advanced Science and Technology since it opened in January 1989. His research interests include machine learning, intelligent scheduling, distributed artificial intelligence, group decision support, and their applications to developing flexible manufacturing and information management methods. He is currently coordinating the research program studying decision support systems at the Beckman Institute, with intelligent manufacturing, financial management, and organization coordination technology for enterprise integration as the targeted applications. He is the Guest Editor of a special issue of IIE Transactions on Design and Manufacturing on system integration and of a special issue of Decision Support Systems on machine learning methods. He is also on the editorial board of Information Systems Research, Institute of Industrial Engineers Transactions, and Decision Support Systems.

JAMES A. GENTRY is Investors in Business (IBE) Professor of Finance at the University of Illinois College of Commerce and Business Administration, Urbana–Champaign. He earned a bachelor's degree from Indiana State University and a master's and doctorate in business administration from Indiana University. Prior to becoming a professor, Dr. Gentry was a navigator in the Strategic Air Command for four years and was a stockbroker with Dean Witter & Co. for five years. He joined the faculty at the University of Illinois in 1966. He is the author of several articles on working capital management as well as on predicting bankruptcy, bond ratings, and loan risks.

Acknowledgment: Research sponsored by an ICM Doctoral Fellowship, Brussels, Belgium, KPMG Peat Marwick Foundation, under the Research Opportunities in International Business Information, and a Collaborative Research Grant of the NATO International Scientific Exchange Programmes.

He is currently completing a major study on cash flow components. University of Illinois students voted Dr. Gentry to Outstanding Professor of Finance from 1981 through 1985, and again in 1990. In May 1985 he was one of three university faculty members to receive the Burlington Northern Foundation Faculty Achievement Award. He has been a visiting professor at Louvain, Belgium; Melbourne, Australia; Bangalore, India; the University of Stellenbosch, South Africa; and the University of Virginia.

ABSTRACT: This paper presents a layered approach to inductive learning that improves the stability and accuracy of the knowledge acquisition method. The methodology is applied to international financial analysis where the comparison of risk structures of different economic environments is critical. The results demonstrate the efficacy of the learning approach for financial decision support. The highly explicit decision structures are especially useful for comparing national differences. The method's utility for decision integration is also discussed.

KEY WORDS AND PHRASES: inductive learning, international financial analysis, layered learning, knowledge acquisition.

## 1. Introduction

THIS PAPER PRESENTS AN ENHANCED INDUCTIVE LEARNING TECHNIQUE supporting an international risk assessment process. The technique is used as a knowledge acquisition module of a decision support system (DSS) and is applied to a comparative risk evaluation of companies from different countries. Moreover, the technique allows the development of an integrated risk structure that incorporates the risk characteristics of firms in the international arena.

The assessment of a firm's financial health is recognized as an important decision task. An incorrect evaluation of financial risks can result in serious losses to creditors or investors. As world business activities become more internationalized, it is increasingly important to understand the financial characteristics of corporations in different countries in order to develop a global risk assessment process. Such an understanding would be particularly important for auditors, investors, and bankers in evaluating different risk characteristics of a firm, either foreign or domestic. Considering the increasing integration of the global economic and financial markets, an integrated DSS that takes into consideration multinational risk characteristics can be highly relevant. In this paper, the focus is on the knowledge acquisition process of an integrated DSS and on a comparative study covering American and Belgian companies.

The design of a DSS for such international financial risk evaluation requires knowledge bases that can differentiate the risk characteristics of firms from different economic environments and across national boundaries. Several methods have been used to model the classification problems that are commonly encountered in finance. Statistical classification models, such as MDA, logit, or probit, are efficient as far as prediction accuracy is concerned $[5]$ , but they do not provide an explicit description of the classification process. In the mid-1980s, the inductive learning approach was introduced as an alternate classification method $[3, 4, 11, 22, 23]$ , that provides comparable prediction accuracy with a far richer description of the decision structure. In this paper, an inductive learning method is developed to generate decision trees that capture the underlying risk assessment processes contained in the data.

The literature in predicting credit risk assessment, bankruptcy, and bond rating $[4, 11, 23, 24]$ has emphasized the qualities of a decision tree in the classification process. A decision tree is highly explicit in its knowledge representation and it expresses the decision process in an understandable and interpretable structure that is very close to the human reasoning process. However, experiments frequently show very unstable results, that is, slightly different subsets of the same data population may generate markedly different decision trees with changing structures and varying prediction accuracies. For example, data covering different years or different subsets from an initial financial data set may generate markedly different decision structures. The instability of the results, and especially the instability in the outlook of the decision trees, represents a major problem for comparing and integrating the risk assessment process between different economic environments. For that purpose, we need an explicit and stable model of the decision process. In this paper, the instability problem is tackled by developing a layered learning technique that generates stable and relevant decision structures on which comparison and/or integration may be performed. First the learning process is performed on data pertaining to Belgian companies and American companies individually in order to identify individual practices in the Belgian and the American economic environments. Next the learning process is applied to the combined data from both countries to identify an integrated risk structure that provides an international risk assessment process.

Section 2 proposes a layered approach to reduce the instability problem encountered with basic inductive learning algorithms. A Global Tree interpretation process (GTip) is proposed as part of a two-layered induction process that generates stable and relevant global decision structures. Section 3 applies the two-layered learning technique to international financial analysis. Finally, section 4 discusses the enhanced inductive learning approach and its relevance in evaluating financial risk in the international arena.

## 2. Global Tree Interpretation Process:

## A Two-layered Inductive Learning Approach

ALTHOUGH THE TREE-BASED INDUCTIVE LEARNING APPROACH has been emphasized as a relevant and efficient technique to model finance-related classification problems $[4, 11, 23, 24]$ , existing algorithms performing inductive learning appear to concentrate on an incomplete model of the learning process. Section 2.1 gives a general description of an inductive learning algorithm. The problem of unstable results is discussed in section 2.2, which also introduces a layered model for performing advanced inductive learning. GTip is introduced in section 2.3. and is illustrated and discussed in section 2.4.

## 2.1. General Description of an Inductive Learning Algorithm

In its general form, an inductive learning process is structured into three distinct elements as shown in figure 1 [19]: an instance space, an algorithm performing induction, and an output describing a target classification concept.

The instance space is a k-dimensional space where each example is described by a vector $(x)$ composed of k independent variables called attributes, and a discrete or continuous classification function $(u)$ . In the framework of bankruptcy prediction, the classification function is binary: 0 represents a negative example of the concept, such as a nonbankrupt company and 1 represents a positive example, such as a bankrupt company. The instance space is the set of bankrupt and nonbankrupt companies on which the induction is performed. For a given run of the algorithm, the instance space is defined in an input training sample. Each company is an example that is described by pieces of financial information, which are the attributes. The output concept gives a description of the classes, that is, a description of the assessment process that predicts if a company is bankrupt or nonbankrupt.

The purpose of induction is to discover the most precise and accurate approximation of the target concept. Such an induction is largely influenced by the configuration of the instance space that is approximated by the training sample. The training sample provides the positive (+) and negative (−) examples, as illustrated in figure 2. A given training sample may reflect a concentrated concept in the instance space, that is, the target concept is represented under one single peak, as shown in figure 2a. Another training sample may show a widespread concept in the instance space, where several narrow peaks are necessary to approximate the concept, as shown in figure 2b. From a given training sample, a best approximation of the target concept, also called hypothesis, is induced. Each best approximation forms an observation in a hypothesis space, in which each hypothesis represents a more or less credible approximation of the target concept. Figure 3 shows the best approximation H1 induced from figure 2a and the hypothesis H2 induced from figure 2b. H1 and H2 form two observations in the hypothesis space where they are ranked according to a credibility function, $\mu(Z_{1}, Z_{2}, \ldots, Z_{i})$ . $Z_{1}$ and $Z_{2}$ represent two dimensions characterizing the hypotheses, such as the size or the prediction accuracy of a decision tree.

The way to express the output concept may follow several formalisms $[19]$ , each explicitly defining the characteristics of examples that belong to the concept (bankrupt companies) or that do not belong to the concept (nonbankrupt companies) in varying detail. The decision tree representation, which has largely contributed to the success of the inductive learning method in several fields of applications, describes the concept using a set of conjunctions. Moreover, it creates an ordering among the attribute values characterizing positive and negative examples.

The standard method for inducing a decision tree from a training set of preclassified examples, each of them described by a fixed set of attributes, is summarized as follows [14, 15]:

\- If all training examples belong to a single class, the tree is a leaf labeled with that class.

![](/api/attachments/YEDHHZ2E/fulltext/images/9bb8381890580dd7afc48d5e33df5e7d0ef9cc61b089e9be73bf69c97281d7f3.jpg)  
Figure 1. General Description of a Learning Algorithm

![](/api/attachments/YEDHHZ2E/fulltext/images/a98a314505ab7a9abbb17d9019c376237a02d5b9b04ee8fe9115406f27760cec.jpg)  
Figure 2. Outlook of the Concept in the Instance Space

\- Otherwise,

—select a test, based on one attribute, with mutually exclusive outcomes;

—divide the training sample into subsets, each corresponding to one outcome; and

—repeat the same procedure with each subset.

This procedure partitions the training sample into smaller subsets, in step with the growth of the tree. The selection of the most relevant attribute on which to split the training sample efficiently has been a primary concern of designers [2]. Among several contingency table statistics and measures based on information theory, Mingers empirically shows that Quinlan's entropy criterion generates the smallest trees [12]. Originating in thermodynamics, the concept of entropy has been used in information sciences since Shannon's contribution on message transmission [21].

Quinlan's formulation of an attribute's entropy,

$$
H = - \Sigma_ {\mathrm{i}} p _ {\mathrm{i}} \log_ {2} p _ {\mathrm{i}},
$$

where $i = 1, \ldots, n; n =$ alternative events for this attribute; and $p_{i} =$ the probability of alternative i, gives the amount of information or the reduction in uncertainty provided by an attribute, for classifying the training examples. The entropy is equal to 0 if and only if all the $p_{i}$ 's but one are equal to 0, that is, the entropy vanishes when the outcome of an event is certain, and thus no valuable information is provided by the attribute. The entropy is maximum when all the $p_{i}$ 's are equal, that is, when all alternatives are equally likely, that is, the most uncertain situation exists. Any change toward an even distribution of $p_i$ 's increases the entropy but as soon as some alternatives become more probable than others the entropy decreases.

![](/api/attachments/YEDHHZ2E/fulltext/images/a9bc21b3cac169a5dc0c363bc7e9faab51942b6e490922ea4885916e67dbb333.jpg)  
Figure 3. Hypothesis Space

The tree-based inductive learning approach captures the knowledge contained in a decision process in a comprehensive and complete formalism. Furthermore, it offers a unique advantage over the results commonly provided by a statistical classification tool. An interpretation of the financial risk elements in the decision tree provides insights about the underlying structure of the data, which highlights the important criteria used in the classification procedure $[2]$ . However, the instability of classification results poses a major problem in the application of the inductive learning approach to real-world data. Our experience shows that the output decision tree can be extremely sensitive to noise in the data and the learning process can overfit the training examples. That is, our experiments in the domain of financial risk assessment showed highly disparate trees being induced from slightly different training samples. The trees differ not only in their selection of specific attributes, but also in the positions of the attributes appearing in the tree. Moreover, the accuracy on testing samples varies greatly from one tree to the other.

The instability phenomenon raises the problem of selecting a best tree that offers the greatest number of insights about the underlying predictive structure of a given set of data and from which a DSS's knowledge could be acquired. A selection based on accuracy does not assure that the chosen tree will reflect the global financial theory justifying the risk assessment process. On the other hand, when selecting from a set of induced trees, one can never be certain that the highest accuracy has been attained. It appears, therefore, that a global interpretation process would summarize and concentrate the positive information provided by a set of original trees, while at the same time reduce the detrimental effects caused by noise or overfitting.

## 2.2. The Layered Concept Learning Approach

In its most basic version, such as in ID3 [13] or PLS [17], an inductive learning algorithm searches for a target concept in an instance space that contains a limited number of preclassified examples, each of them described by a user-defined fixed set of attributes. The search for the best approximation of the target concept is greatly influenced by the shape of that instance space. Ideally it should show a smooth surface without abrupt deformations, as presented in figure 2a. In a “hilly” instance space (figure 2b), a basic hill-climbing algorithm can be stuck in local optima and therefore misses the correct target concept. As the shape of the instance space remains highly dependent on the training set of examples and its fixed set of attributes, it is not surprising that a slightly different training sample could generate a markedly different concept. Experiments prove that the decision trees differ in size, prediction accuracy, and internal structure, that is, they contain different attributes or their attributes appear in various positions.

The layered concept learning model $[18]$ views concept learning as an interaction among three distinct spaces: the instance space, the hypothesis space, and the bias space. The instance space contains the ground objects and remains highly dependent on the training sample, as illustrated in figure 2. The hypothesis space contains all candidate hypotheses that approximate the correct target concept and are built from the instance space. A measure of “credibility” may be assigned to each hypothesis, which will guide a learning process performed on the hypothesis space, as shown in figure 3. In other words, the hypothesis space may be defined as a set of “synthetic” versions of several instance spaces and it remains less dependent on the relative smoothness of a specific instance space. The bias space contains elements that constrain the search for the best approximation of the target concept. For example, a specific concept representation, such as a decision tree, or a specific learning technique in the algorithm itself, such as an entropy criterion to select the best splitting attributes, can help the search for the best target concept.

A learning technique combining several layers in a single system offers computational and conceptual advantages $[18]$ . When focusing on a single instance space, the learning process may be performed on a hilly space, as shown in figure 2b. The irregularities of the space make the search slower, less accurate, and less stable. Any narrow peak present in the instance space, whether relevant or due to noisy input data, may be searched as a candidate hypothesis. Moreover, hill-climbing algorithms operating in the original instance space may become stuck in some local optima. As a result, the learned concept lacks accuracy and generality. On the other hand, an induction performed on the hypothesis space operates in a much smoother environment in which candidate hypotheses are ranked by credibility. Therefore, the search for the most credible hypothesis is faster and focuses directly on an accurate and general description of the target concept. Changes in the bias space may also improve the configuration of instance and hypothesis spaces. The main purpose of the layered approach is to create a smooth and concentrated search space that allows fast and accurate learning. Figure 4 illustrates a general scheme for layered learning and shows how the layered methodology compares with an induction based solely on the instance space.

![](/api/attachments/YEDHHZ2E/fulltext/images/604dad178d7cb5883da73016193fae762c925e9b045f9ac8acd28dfab61b619e.jpg)  
Figure 4. A General Scheme for Layered Learning

Several algorithms are proposed in the literature to improve the basic induction. For example, DLS [20] performs a learning in two layers: the first layer generates a hypothesis space from the instance space, using PLS; the second layer is performed on the hypothesis space using a genetic algorithm approach. CRIS [10] utilizes the bias space by modifying the learning algorithm according to the type of attributes under consideration. LFC [16] creates new attributes and therefore modifies the instance space in order to smooth its shape and to avoid local optima. Moreover LFC includes a lookahead search procedure in the bias space which increases the computational efficiency. These improved versions of the basic inductive learning algorithm are substantiated by real-world data and offer a more relevant and accurate concept as well as a higher computational efficiency.

The two-layered induction process proposed in this paper follows a similar approach. In the first layer it performs basic induction on the instance space in order to create a set of trees that approximate the target concept. These approximations form a tree space comparable to the hypothesis space shown in figure 3. In the second layer, GTip is utilized in the training tree space to generate a global final decision tree. GTip is aimed at acquiring the relevant and accurate characteristics of each training tree while avoiding their irrelevant components due to noise and overfitting effects. As a result, a more general decision tree is learned that shows higher accuracy and relevance. The proposed improvement does not modify the instance space, nor the bias space.

## 2.3. GTip as Part of the Two-layered Induction Process

GTip is developed to improve the induction process focusing solely on the instance space [25]. The enhanced method first performs induction on several independent training samples, generated at random from an initial input data set, as shown in figure 5. The objective is to design a training tree space in which a second layer of learning is performed. As explained earlier, the decision trees or hypotheses learned in the first layer by a basic inductive learning algorithm are influenced by noisy data and they overfit the instance space. GTip, the second layer, reduces noise and overfitting effects by summarizing and concentrating on the most relevant information provided in the training tree space. By taking advantage of the decision tree representation, GTip retains general patterns shared by most of the training trees. Particular or isolated tree structures are disregarded. As a result, a final global tree is built that reflects the most general and accurate approximation of the target concept.

![](/api/attachments/YEDHHZ2E/fulltext/images/bbf7db1a2f7d9349195c09bc27208923b32edd9e381cf0bd8e64d2b5f2dd0cf6.jpg)  
Figure 5. The Two-Layered Induction Process

At first, GTip considers the number of times an attribute appears in the trees. The attributes appearing with a frequency higher than 50 percent are called primary; the attributes appearing with a frequency falling between 50 percent and 25 percent are called secondary; an attribute appearing with a frequency lower than 25 percent is considered a noisy effect. It is supposed that the more frequently an attribute appears on the trees, the more important it is in the decision process being modeled.

The second topology considers the position of an attribute's appearance on the tree. The basic induction process selects the best candidate attribute in order to reduce uncertainty. This optimization is based on an entropy criterion. It selects the attribute that provides the best split of the subset of examples under consideration. Naturally, the lower in the tree the splitting is repeated, the smaller the subset of examples. The higher an attribute appears on the tree, the higher its discriminant ability for classifying the initial training sample. The average level on which a given attribute appears on the tree is thus related to its relevance and importance in the decision process.

Finally, GTip classifies the attributes according to their presence on the main path or on an alternate path of the tree. The main path of the tree is the path followed by the largest proportion of training examples. Thus, GTip identifies these main paths because they are highly relevant in the decision process being modeled. The attributes appearing on the main path are called major, as they help to discriminate the largest proportion of examples. The attributes belonging to an alternate path are called minor attributes. The root node implicitly belongs to the main path. The algorithm followed by GTip is described as follows:

Given

—a set of examples described with a list of n attributes;

—a set of m trees generated by induction from a subset of training examples selected at random;

— $i=1,\ldots,n$ and $j=1,\ldots,m$ .

Step 1. For each attribute, observe:

a. the level on which it appears in each tree;

b. its presence on the main or an alternate path in tree $_{j}$ .

Step 2. Define the final status of attribute, as:

a. a primary (secondary) attribute if it appears in more than 50 percent (between 50 percent and 25 percent) of the trees;

b. a major (minor) attribute if it appears in more (less) than 50 percent of the main paths;

and calculate its discriminant ability, that is, the average level where it appears.

Step 3. The final global tree is built per level, starting from the root node of the tree, and according to the following rules:

—primary attributes prevail over secondary attributes;

—major attributes appear on the main path;

—minor attributes appear on alternate paths;

—an alternate path is started from a given node, as soon as several attributes are in conflict for the subsequent level.

The final global tree should not exceed the average length (number of successive nodes present on the longest path of the tree) and width (number of nodes only followed by final leaves) of the training trees.

## 2.4. Application and Evaluation of the

## Two-layered Induction Process

Let us consider a set of twenty training trees shown in Table 1. Each tree was learned from an independent training sample selected at random from the same original set of examples. Therefore, each training tree represents a more or less credible approximation of the target concept, or hypothesis. As a result, Table 1 represents a training tree space on which GTip is performed, as shown in figure 5. A set of fourteen attributes, that is, att1 to att14 are used to describe the input examples. The position of each attribute in each tree is given in the first twenty rows of Table 1. A value of 1 indicates that the attribute is the top node in the corresponding tree; a bold value corresponds to a main path position. Table 1 shows a highly unstable hypothesis space. The trees differ in their structure (columns 2 to 15): for example, att3 is the only attribute to always appear on the top of all the trees (column 6), whereas the second position is occupied alternatively by att1, att2, att5, or att11. The size of the trees is relatively unstable, as shown in column 16: although all of them show a width of one path (W = 1), their length (L) varies from 2 to 9. Finally, their prediction accuracy on testing sample (column 17) varies from 77 percent to 93 percent. GTip is aimed at searching the most credible target concept out of the hypothesis space of Table 1. In the process, noise and overfitting effects are reduced. For example, the two occurrences of att8 (column 9) on tree 10 and tree 20 are considered as an overfitting problem and att8 is not kept in the description of the final global tree.

Table 1 Example of a Global Tree Interpretation

<table><tr><td>TREE(1)</td><td>att1(2)</td><td>att2(3)</td><td>att3(4)</td><td>att4(5)</td><td>att5(6)</td><td>att6(7)</td><td>att7(8)</td><td>att8(9)</td><td>att9(10)</td><td>att10(11)</td><td>att11(12)</td><td>att12(13)</td><td>att13(14)</td><td>att14(15)</td><td>L/W(16)</td><td>error rate(%) (17)</td></tr><tr><td>1</td><td></td><td>2</td><td>1</td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>13</td></tr><tr><td>2</td><td></td><td>2</td><td>1</td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>10</td></tr><tr><td>3</td><td></td><td>2</td><td>1</td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>10</td></tr><tr><td>4</td><td></td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4/1</td><td>13</td></tr><tr><td>5</td><td></td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4/1</td><td>13</td></tr><tr><td>6</td><td></td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4/1</td><td>13</td></tr><tr><td>7</td><td>3</td><td>2</td><td>1</td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5/1</td><td>7</td></tr><tr><td>8</td><td></td><td>4</td><td>1</td><td></td><td>5</td><td></td><td></td><td></td><td>3</td><td></td><td>2</td><td></td><td></td><td></td><td>5/1</td><td>17</td></tr><tr><td>9</td><td>2</td><td>3</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>7</td></tr><tr><td>10</td><td>2</td><td>3</td><td>1</td><td></td><td></td><td>6</td><td></td><td>4</td><td></td><td></td><td>7</td><td></td><td>8</td><td></td><td>8/1</td><td>13</td></tr><tr><td>11</td><td>2</td><td>3</td><td>1</td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5/1</td><td>13</td></tr><tr><td>12</td><td>2</td><td>3</td><td>1</td><td></td><td>3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4/1</td><td>20</td></tr><tr><td>13</td><td>4</td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4/1</td><td>10</td></tr><tr><td>14</td><td>3</td><td>2</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>7</td></tr><tr><td>15</td><td>5</td><td>4</td><td>1</td><td></td><td></td><td>7</td><td></td><td></td><td></td><td></td><td>6</td><td></td><td>3</td><td></td><td>8/1</td><td>13</td></tr><tr><td>16</td><td>3</td><td>5</td><td>1</td><td></td><td>9</td><td></td><td></td><td></td><td>7</td><td></td><td>6</td><td></td><td>4</td><td></td><td>9/1</td><td>10</td></tr><tr><td>17</td><td></td><td></td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>2/1</td><td>23</td></tr><tr><td>18</td><td></td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>20</td></tr><tr><td>19</td><td></td><td>3</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>3/1</td><td>20</td></tr><tr><td>20</td><td>3</td><td>2</td><td>1</td><td></td><td>6</td><td>5</td><td></td><td>8</td><td>4</td><td></td><td></td><td></td><td></td><td></td><td>8/1</td><td>10</td></tr><tr><td>occurr.</td><td>10</td><td>19</td><td>20</td><td>0</td><td>16</td><td>3</td><td>0</td><td>2</td><td>3</td><td>0</td><td>4</td><td>0</td><td>3</td><td>0</td><td>4.55/1</td><td>13</td></tr><tr><td>main path</td><td>100</td><td>100</td><td>100</td><td>*</td><td>100</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td></td><td></td></tr><tr><td>aver.level</td><td>2.9</td><td>3.0</td><td>1.0</td><td>*</td><td>3.2</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td></td><td></td></tr><tr><td>status</td><td>MP</td><td>MP</td><td>MP</td><td>*</td><td>MP</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td>*</td><td></td><td></td></tr><tr><td>1</td><td colspan="6">level on the main path</td><td colspan="2">MP</td><td colspan="8">major primary attribute</td></tr><tr><td>1</td><td colspan="6">level on alternate path</td><td colspan="2">L</td><td colspan="8">length of the tree</td></tr><tr><td>*</td><td colspan="6">non-discriminant attribute</td><td colspan="2">W</td><td colspan="8">width of the tree</td></tr></table>

The row entitled occurrence, which gives the number of times an attribute appears in the original trees, enables the compilation of the attribute status as primary (P if occurrence > 10) or secondary (S if 4 < occurrence < 10). The attributes that appear four times or less are considered as noise and disregarded, as represented by an asterisk in Table 1. The next row, entitled main path, which gives the frequency of an attribute appearing on a main path, enables the definition of the attribute status as major (M if main path ≥ 50 percent) or minor (m if main path < 50 percent). Finally, the row entitled aver. level provides information about the attribute's average position on the trees.

The last row (status) is presented in order to build a final global tree, as shown in figure 6. Four major attributes are used to build the main path (att1, att2, att3, att5), with the primary attributes prevailing over the secondary attributes. The root position is occupied by attribute att3. Attribute att1 stands on the second level of the main path, followed by attribute att2 and attribute att5. Because all the attributes always appear on the main path, the final global tree does not contain any alternate paths and is quite linear [1]. The final global tree has a size comparable to the average of the original trees (length = 4.5 and width = 1), as shown in figure 6.

The final global tree given in figure 6 represents the most credible approximation of the target concept out of the tree space. It concerns the bankruptcy risk analysis of American companies. A brief explanation will help the reader to interpret the results shown in the final global tree. Dividends (att3) appear as the first characteristic that determines a firm's bankruptcy status, that is, bankrupt firms, coded as 1, usually do not pay dividends (att3 = 0). A company paying dividends (att3 > 0), but showing negative net operating flows (att1 < 0) is likely to go bankrupt. Positive net operating flows (att1 ≥ 0) with a positive variation in net investment flows (att2 > 0), that is, a strategy of disinvestment, is the next bankruptcy characteristic in the tree. Finally, a firm that passes the first three tests is likely to go bankrupt if more than 20 percent of the cash flows finance an increase in receivables (att5 > 0.2). This final global tree correctly predicts 87.5 percent of a hold-out testing sample and it offers a decision structure that is stable, informative, and accurate.

## 3. Application to International Financial Analysis

THIS SECTION FOCUSES ON THE LEARNING AND INTERPRETATION of an international risk structure that supports the financial analysis of companies from different economic environments. In view of the upcoming integration of the European market, a methodology capable of comparing and integrating American and European risk characteristics would be valuable to firms extending credits. For that purpose, a set of Belgian companies were selected as representative of the European economic environment. Such a decision structure must be explicit enough to differentiate clearly the risk characteristics of firms from different economic environments across national boundaries. In that framework, the tree-based inductive learning approach, enhanced by the layered learning scheme, offers unique features. While offering predictive validity comparable to common statistical classification tools, the inductive learning approach provides a set of structural information that describes particularly well the decision process to be modeled. The risk evaluation represented in a decision tree clearly shows a structured and fixed decision process: successive well-defined tests on specific attributes form a hierarchy that is easy to understand and to interpret. Therefore, the decision trees are very useful for comparing national differences in the financial risk structure as well as for integrating the risk structure of different economic environments.

![](/api/attachments/YEDHHZ2E/fulltext/images/08cdf02bd2c2ef37d624146e65a5cc650d921721f6dabe9faac425586702501e.jpg)  
Figure 6. Final Global Tree

The first objective of the experiments is the development of decision structures that enable a comparison of the risk characteristics of American and Belgian companies. The American and Belgian companies are modeled separately and two resulting decision trees represent the risk structure for predicting bankruptcy in the two economic environments. These two trees are compared in order to discover similarities and differences in the risk characteristics of companies from the two countries. The second objective of the experiments concerns an integrative financial analysis approach of the firms in the two countries. For that purpose, the American and Belgian samples are combined to generate a unique decision tree that integrates the risk characteristics of the two economic environments. The interpretation of the integrated decision tree provides a risk evaluation process covering both economic environments while considering the risk characteristics of each nation.

Two data sets contain approximately 200 American and 200 Belgian companies. Both sets are composed of 50 percent bankrupt firms and a matching sample of 50 percent nonbankrupt firms. All companies belong to similar industries—mainly manufacturing companies—and are of comparable size within their respective group, although the Belgian companies are generally smaller than the American companies.

Cash-flow analysis, which is one of the most effective tools for risk assessment [6, 7, 8, 9], uses fourteen attributes to characterize each company. These attributes, shown in Table 2, are based on the financial statements provided in the Compustat PC Plus database for the American companies, and the CD-Rom published by the National Bank of Belgium for the Belgian companies. For inducing the integrated decision tree, the same set of fourteen attributes is used and an attribute representing the nationality (COUN) is added. Each company is thus defined in terms of fifteen attributes.

The three global decision trees, that is, the Belgian tree, the American tree, and the integrated tree are generated by an inductive learning algorithm (C4.5) developed by J.R. Quinlan at the University of Sydney in Australia [13]. For each global tree, twenty hypotheses were first induced from twenty independent training samples. GTip then globalizes the relevant information contained in the twenty trees into one final global tree, as explained in section 2.3. The final global tree is evaluated on a hold-out sample representing 25 percent of the original data set.

## 3.1. American Risk Structure versus Belgian Risk Structure: A Comparative Study

This section performs a comparative study of the risk structure of Belgian and American companies, which are shown in figures 7 and 8. The two final global trees correctly predict 87.5 percent of the American hold-out sample and 84 percent of the Belgian hold-out sample. At each test of both trees, there is enough information to classify a subsample of companies as bankrupt or nonbankrupt. Such a linear tree structure [1] provides a clear and easily interpretable decision process. The Belgian tree (6 nodes), however, is 1.5 times longer than the American tree (4 nodes). The extremes (top and bottom) of the trees look similar: they start by considering the dividends (DIV\*) and the net operating flows (NOF\*) for the American structure and by considering the net operating flows (NOF\*) for the Belgian structure; they end with the change in accounts receivable (ARF\*) for both structures. Therefore, the two economic environments appear similar not only with respect to the most discriminant risk characteristics but also with respect to the least discriminant characteristic.

However, the cash outflow to dividends (DIV\*) does not appear on the Belgian tree. In evaluating the significance of this finding we observed that the Belgian companies selected for this research are not quoted on the Brussels Stock Exchange, but the American companies are quoted on the New York Stock Exchange. One possible interpretation is that the level of dividends for small Belgian companies (total assets < \$30 million and total sales < \$20 million) is therefore far less representative than the dividends that are publicly announced by an American company. Although the concept of value creation or excess market returns may be targeted by most of the large Belgian companies, the companies selected for this research project do not seem to reflect their financial, operational, or investment strategies in the level of their dividends. In other words, an absence of dividends is not directly related to higher bankruptcy risk in the Belgian economic environment, while it appears among the most discriminant characteristics in the American economic environment.

Between the extremes—DIV\* and NOF\* on the top, ARF\* on the bottom—only one more risk characteristic, NIF\*, appears on the American tree, whereas four supplementary attributes appear on the Belgian tree: OCAF\*, INVF\*, AD/FA, and FCE\*. The presence of the net investment flows (NIF\*), in the center of the American tree, nicely completes a compact and meaningful risk structure: the level of dividends (DIV\*) reflects the main objective of excess market returns targeted by American companies or the availability of surplus cash flow for paying dividends to investors; the primary operating and investment strategies are discriminating at subsequent levels, NOF\* and NIF\*; and finally, an element of operations and working capital management (ARF\*) is considered to complete the risk assessment process.

Table 2. Attributes Describing Belgian and American Companies [8]

<table><tr><td>NOF*</td><td>Net operating flow/total cash flow</td></tr><tr><td>NIF*</td><td>Net investment flow/total cash flow</td></tr><tr><td>DIV*</td><td>Dividends/total cash flow</td></tr><tr><td>FCE*</td><td>Fixed coverage expenditures/total cash flow</td></tr><tr><td>ARF*</td><td>Change in receivables/total cash flow</td></tr><tr><td>INVF*</td><td>Change in inventories/total cash flow</td></tr><tr><td>OCAF*</td><td>Change in other current assets/total cash flow</td></tr><tr><td>APF*</td><td>Change in payables/total cash flow</td></tr><tr><td>OCLF*</td><td>Change in other liabilities/total cash flow</td></tr><tr><td>NFF*</td><td>Change in net financial/total cash flow</td></tr><tr><td>NOA&amp;L*</td><td>Change in net other assets and liability/total cash flow</td></tr><tr><td>TCF/TA</td><td>total cash flow/total asst</td></tr><tr><td>AD/FA</td><td>Accumulated depreciation/fixed assets</td></tr><tr><td>SALT</td><td>Sales trend</td></tr></table>

\* Refers to a measure of cash flow relative to the total cash flow.

A longer risk structure is observed in the Belgian decision tree: two attributes refer to the working capital management, that is, the change in other current assets (OCAF\*) and the change in inventory (INVF\*); the financial strategy is characterized by payment of interest, which is represented in the fixed coverage expenses (FCE\*); finally a non-cash flow measure is introduced, that is, accumulated depreciation on fixed assets (AD/FA), which characterizes the maturity of a company. The node on attribute AD/FA tells the following story: a “mature” company, that is, a company that has depreciated its assets more than 60 percent (AD/FA > 0.60), is not likely to go bankrupt; a “young” company whose assets are depreciated less than 60 percent (AD/FA ≤ 0.60) represents a risk and more information is required before taking a final decision, namely the subsequent nodes on attributes FCE\* and ARF\*.

In summary, for the decision trees generated, net operating flows and change in accounts receivable (NOF\* and ARF\*) are similarly considered in both economic environments. Dividends (DIV\*), which appear highly relevant in the American environment, are not recognized as important in the Belgian economic context. This reflects a major difference between the two countries in capital management and managerial objectives. The size of the Belgian companies may justify that major discrepancy between the two countries. The American risk structure shows a compact decision process that considers major cash-flow components. However, in the Belgian case, the tree is markedly longer, reflecting a more intricate risk structure that also includes the only non-cash-flow attribute, that is, the maturity of the company (AD/TA).

## 3.2. Integrated Decision Tree

Figure 9 shows the integrated risk structure induced from a sample containing American and Belgian companies. The additional attribute characterizing the nationality (COUN) appears at the bottom of the tree. A linear tree [1] is obtained that is longer (ten nodes) than the two individual risk structures discussed in the previous section.

The presence of the nationality attribute (COUN) at the bottom of the tree in figure 9 shows how the inductive learning approach nicely integrates the risk characteristics of the two different countries, but still needs a last attribute to assess the financial risk of some remaining Belgian companies exclusively, that is, the last node on attribute TNF/TA, below attribute COUN.

Among the upper eight attributes, only the change in other current liabilities (OCLF\*) does not appear on the individual trees discussed in the previous section. As expected, the net operating flows (NOF\*) appears as the root node and therefore is the most discriminant attribute in the integrated structure. The second test concerning the level of dividends (DIV\*) helps to classify American companies paying dividends (if DIV\* < 0, then the company is likely not to go bankrupt) but does not directly penalize mainly the Belgian companies that do not pay dividends (if DIV\* = 0, then more information is required). The same attribute (change in accounts receivable—ARF\*) appears at the bottom of the integrated part of the tree, while the attributes appearing in the middle of the Belgian individual structure, OCAF\*, AD/FA, and FCE\*, are integrated as an extension of the American individual structure, that is, between net investment flows (NIF\*) and change in accounts receivable (ARF\*). As flows covering other current assets (OCAF\*) and other current liabilities (OCLF\*) are usually related, this may explain the addition of attribute OCLF\* below attribute OCAF\*.

At the ninth level, the nationality attribute (COUN) eventually interrupts the integrated risk assessment process to further concentrate on Belgian companies exclusively. The last attribute (total net flows on total assets—TNF/TA) characterizes a global appreciation of the company's efficiency to manage its assets and to generate an appropriate proportion of flows from each of the cash flow sources, that is, operations, financing, and investment. The resulting integrated tree efficiently globalizes the American and Belgian characteristics in a richer international risk assessment process, which is able to correctly predict 75 percent of the hold-out sample.

## 3.3. Discussion

Presenting a financial risk analysis in the form of a decision tree greatly helps to compare individual risk structures of Belgian and American companies. The two-layered induction process selects common attributes for the first and last nodes of the trees, that is, for the most and least discriminant risk characteristics. In the decision tree corresponding to the Belgian companies, the risk structure appears longer and more intricate than that of the American companies. When applied to companies of both countries, the induction reveals interesting insights into the differences and similarities of their risk evaluation processes. The presence of the nationality attribute at a low level in the tree highlights the ability of the learning approach to integrate national commonalities and differences. As a result, a richer risk evaluation process is learned that makes possible an integrated evaluation scheme independent of the nationality. Also it provides the ability to consider differences among the various economic environments.

![](/api/attachments/YEDHHZ2E/fulltext/images/ce3ec991281a97ab92920060faf648d09c1de0f672daeb8befd612ce58a97308.jpg)  
Figure 7. Belgian Risk Structure

![](/api/attachments/YEDHHZ2E/fulltext/images/f1e46c523cbf9049f776ae8ee8520eb883c838e4974dcd3efbbe551ee7d13912.jpg)  
Figure 9. Integrated Decision Tree

The integrated risk structure encapsulates the two individual structures. The encapsulation is performed in a reorganization of the attributes, as well as in a revision of the use of specific attributes in an integrated scheme. Figure 9 shows that the first part of the tree (above the Nationality attribute) integrates the individual structures presented in figures 7 and 8. The attributes specific to the Belgian risk structure (AD/FA, FCE\*, and OCAF\*) are reorganized during the learning process and encapsulated inside the American risk structure between NIF\* and ARF\*. Moreover, the use of the most discriminant attribute in the American context (DIV\*) is adapted in the integrated structure in order to comply with the Belgian context.

The enhanced inductive learning technique offers a unique tool that allows a clear interpretation of the integrated decision structure. To our knowledge, such explicit and interpretable results has not previously been provided by any common statistical classification tool.

## 4. Conclusion

THE TWO-LAYERED INDUCTION PROCESS IS SHOWN TO BE VERY HELPFUL for assessing financial risk, especially when the internationalization of the markets calls for enhanced DSSs that are able to learn from national differences and adapt their knowledge accordingly. Although results obtained by basic inductive learning generally shows a high degree of instability, the two-layered induction process, involving a Global Tree Interpretation Process, allows the selection of the most concise and relevant hypothesis while reducing noise and overfitting effects present in the instance space. The enhanced inductive learning approach provides a unique tool that meets our objective of developing an improved machine learning methodology for evaluating a company's financial risk.

The ability to reveal structural characteristics of decision processes is highlighted by applying the methodology to American and Belgian companies. This type of comparative study becomes especially significant considering the forthcoming integration of the European market and the new investment opportunities that may arise. The integration clearly shows how the resulting DSS framework can help enhance the support for international risk evaluation processes. Currently, we are applying the same methodology to the Japanese markets. The two-layered induction involving the global interpretation process offers a unique contribution to the design of DSSs for financial evaluation.

New learning algorithms are being developed to further implement the layered concept learning model. For instance, we are building a “new generation” of learning algorithms capable of constructing new attributes from implicit relationships among the original attributes of the data. Such improvements can reveal more accurate, relevant, and concise decision structures by constructing and searching a highly smooth instance space and highly stable hypothesis space. Further experiments are necessary in order to verify their impact on the final decision structure.

## REFERENCES

1. Arbab, A. Generating rules from examples. Proceedings of the 9th International Conference on Artificial Intelligence. Los Altos, CA: Morgan Kaufmann, 1985, 631–633.

2. Breiman, L.; Friedman, J.H.; Olshen, R.A.; and Stone, C.J. Classification and Regression Trees. Belmont: Wadsworth International Group, 1984.

3. Carter, C., and Catlett, J. Assessing credit card applications using machine learning. IEEE Expert (Fall 1987), 71–79.

4. Chandler, J.S.; Liang, T.; and Han, I. An empirical comparison of probit and ID3 methods for accounting classification research. Department of Accountancy, College of Commerce and Business Administration, University of Illinois, Urbana–Champaign, August 1989.

5. Frydman, H.; Altman, E.I.; and Kao, D.-L. Introducing recursive partitioning for financial classification: the case of financial distress. Journal of Finance, 40, 1 (March 1985).

6. Gentry, J.A.; Newbold, P.; and Whitford, D.T. Classifying bankrupt firms with funds

flow components. Journal of Accounting Research (Spring 1985), 146–160.

7. Gentry, J.A.; Newbold, P.; and Whitford, D.T. Predicting bankruptcy: if cash flow is not the bottom line, what is? Financial Analysts Journal (September/October 1985), 47–56.

8. Gentry, J.A.; Newbold, P.; and Whitford, D.T. Profiles of cash flow components. Financial Analysts Journal (July/August 1990), 41–48.

9. Heffert, E.A. Techniques of Financial Analysis, 5th ed. Homewood, IL: Richard D. Irwin, 1982.

10. Liang, T. A composite approach to inducing knowledge for expert systems design. Management Science, 38, 1 (January 1992).

11. Messier, W.F., and Hansen, J.V. Inducing rules for expert system development: an example using default and bankruptcy data. Management Science, 34, 12 (December 1988), 1403–1415.

12. Mingers, J. An empirical comparison of selection measures for decision-tree induction. Machine Learning, 3 (1989), 319–342.

13. Quinlan, J.R. Induction of decision trees. Machine Learning, 1 (1986), 81–106.

14. Quinlan, J.R. Unknown attribute values in induction. In A.M. Segre (ed.), Proceedings of the 6th International Workshop on Machine Learning. Los Altos, CA: Morgan Kaufmann, 1989, 164–168.

15. Quinlan, J.R. Decision trees and decision making. IEEE Transactions on Systems, Man, and Cybernetics, 20, 2 (March/April 1990), 339–346.

16. Ragavan, H.; Rendell, L.; Shaw, M.J.; and Tessmer, A.C. Decision tree induction through informed construction. Technical report, Beckman Institute, University of Illinois, Urbana-Champaign, October 1992.

17. Rendell, L. A general framework for induction and a study of selective induction. Machine Learning, 1 (1986), 177–226.

18. Rendell, L. Layered concept learning and its advantages. Technical Report UIUCDCS-R-87-1320, Department of Computer Science, University of Illinois, Urbana-Champaign, March 1987.

19. Rendell, L., and Cho, H. Empirical concept learning as a function of data sampling and concept character. Technical Report R–88–1410, Department of Computer Science, University of Illinois, Urbana–Champaign, May 1988.

20. Sikora, R., and Shaw, M.J. A double-layered learning approach to acquiring rules for financial classification. BEBR Faculty Working Paper No. 90–1693, College of Commerce and Business Administration, University of Illinois, Urbana–Champaign, September 1990.

21. Shannon, C.E., and Weaver, W. The Mathematical Theory of Communication. Urbana: University of Illinois Press, 1963.

22. Shaw, M.J. Applying inductive learning to enhance knowledge-based expert systems. Decision Support System, 3 (1987), 319–332.

23. Shaw, M.J., and Gentry, J.A. Using an expert system with inductive learning to evaluate business loans. Financial Management (Autumn 1988), 45–56.

24. Shaw, M.J., and Gentry, J.A. Inductive learning for risk classification. IEEE Expert (February 1990), 47–53.

25. Tessmer, A.C. Machine learning applied to the credit granting decision. The case of small Belgian businesses. Doctoral Dissertation, University of Namur, Belgium, January 1992.
