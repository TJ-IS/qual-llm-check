---
otero_id: 7646
otero_key: "2QHQCARH"
title: "A multi-attribute, multi-weight clustering approach to managing “e-mail overload”"
authors: "David Schuff; Ozgur Turetken; John D'Arcy"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.11.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 42 (2006) 1350–1365

www.elsevier.com/locate/dss

# A multi-attribute, multi-weight clustering approach to managing <sup>b</sup>e-mail overload<sup>Q</sup>

David Schuff <sup>a,\*</sup>, Ozgur Turetken <sup>a,1</sup>, John D’Arcy <sup>b,2</sup>

<sup>a</sup> Fox School of Business and Management, Temple University, 1810 N. 13th Street, Philadelphia, PA 19122, USA <sup>b</sup> Department of Computer and Information Sciences, Towson University, 8000 York Road, Towson, MD 21252, USA

Received 4 April 2005; received in revised form 2 November 2005; accepted 7 November 2005 Available online 20 December 2005

## Abstract

The increasing volume of electronic mail communication threatens to cause a state of <sup>b</sup>e-mail overload<sup>Q</sup> where the volume of messages exceeds individuals’ capacity to process them. To address this problem, this study extends the application of hierarchical clustering to the domain of e-mail. We report on the design and development of a system that applies a multi-weight, multi-attribute clustering approach to a collection of messages. We found strong evidence that clustering messages improves users’ ability to locate messages compared to an ordered list, and promising (though weaker) evidence of even greater improvement when given the ability to adjust attribute weights.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Electronic mail; Information overload; Clustering; Empirical study

## 1. Introduction and motivation

Electronic mail (e-mail) has become one of the most powerful communication tools in the workplace. The sheer volume, however, of electronic messages can be a burden; experienced e-mail users receive between 100 and 200 messages per day [14]. This number is expected to increase—a recent study by IDC Market Research predicts the number of worldwide e-mail messages to nearly double from 31 billion to 60 billion by 2006 [22]. Considering the massive number of messages a typical e-mail user receives, many messages are left in the mailbox to be processed later [25,49]. The increasing volume of these messages can become particularly overwhelming since messages are often not sequential and span multiple topics. While the number of e-mail messages continues to grow, the limits of individuals’ processing capacity remain the same [29]. Hence, the growth of e-mail communication threatens to cause <sup>b</sup>information overload<sup>Q</sup>—a state in which the amount of information that merits attention exceeds an individual’s ability to process it [24,40].

It has long been recognized that individuals tend to filter and omit information as the primary ways of coping with high rates of information overload [29]. Although omission may reduce mental workload, the process of filtering, in requiring the user to at least partially understand the content of a message, can increase mental workload. Moreover, people tend to omit important information when they are overloaded, thereby jeopardizing decision-making performance [40]. Omitting evaluation of the information effectively removes it from the decision-maker’s information set, leading to both a reduced ability to make fine distinctions and to unambiguously worse decisions [6]. Therefore, both coping strategies of filtering and omission negatively impact performance [21].

A recent survey [4] highlights a growing awareness of the <sup>b</sup>e-mail overload<sup>Q</sup> problem, indicating that practitioners are actively searching for strategies to reduce e-mail overload (earlier identified by Cranor and LaMacchia [10] in the context of eliminating unwanted <sup>b</sup>spam<sup>Q</sup> messages). We believe that a system that automatically classifies e-mail into groups is a potential solution for e-mail overload. Such a system can be designed in a way to limit the cognitive load on users even as the volume of e-mail messages (and the information contained within them) continues to increase. This requires the e-mail management system to present messages in a form that is consistent with the way people process and store information. Semantic network theory [9] contends that people encode information into a structured network of nodes. Organizing information into logical groups of related entities should thus assist users in comprehending and retrieving the information contained within those groups [35].

In the case of e-mail, the current methods of creating such a group structure involves assigning messages into manually created folders based on the content of the incoming message and the content of the other folders [26,49,30]. However, the user must still absorb the initial cognitive burden of creating the folder structure. We propose a system that automatically creates the folder structure based solely on the content of the messages in a user’s inbox. Although this folder structure is a static snapshot of a user’s collection of e-mails at a particular point in time, the technique can be extended to regenerate groups <sup>b</sup>on-demand<sup>Q</sup> as the collection changes.

The techniques for clustering text are well-developed [39]. In our adoption of these techniques to a collection of e-mails, we observe that several distinct elements of information comprise an e-mail message. In addition to the content of the message body itself, attributes such as date, sender, and recipient may be relevant when forming message groups. Therefore, accounting for multiple attributes when clustering messages should result in clusters that are more useful than those created based on a single attribute. Furthermore, this approach can be made more flexible by allowing users to vary the level of emphasis on each attribute.

In this work, we test the effectiveness of this idea by applying a multi-weight, multi-attribute clustering approach to a collection of e-mail messages. To that end, we developed a Java-based tool to serve as a prototype of this system, which we call the Automatic Clustering E-Mail Management System (ACEMS). Through a controlled laboratory experiment, we tested two versions of the clustering tool—one with and one without adjustable attribute weights.

The rest of the paper is organized as follows. In Section 2, we present the theoretical foundation for our approach through a discussion of semantic network theory. We then review prior research on e-mail management and document clustering. Section 3 presents the details of our multi-weight, multi-attribute clustering method, including an overview of the system (ACEMS) that employs this approach. In Section 4 we present our research hypotheses and in Section 5 we describe the experimental design we used to test these hypotheses. Section 6 presents the analysis of the data and discussion of our findings. Section 7 presents implications and potential limitations of our study. The paper concludes with a discussion of the potential contributions of this work and suggested directions for future research.

## 2. Background

## 2.1. Theoretical foundations from cognitive psychology

Well-established theory in cognitive psychology [29] contends that humans organize items into logical groups (or <sup>b</sup>chunks<sup>Q</sup>) as a way of dealing with large amounts of information. Miller found that more information than the generally accepted <sup>b</sup>seven plus or minus two<sup>Q</sup> limitation of human memory can be retrieved when the information is supplemented with additional attributes such as a relationship to a larger group. Mandler [27] first showed the link between these chunks and human performance on cognitive tasks. Later, Ashcraft [2] found that subjects group lists of meaningful words into categories and retrieve the items by those categories rather than in their original random order, presumably because the words have more semantic meaning due to their association with a chunk.

The relationship between chunks also serves as an aid to memory and comprehension. The central tenet of semantic network theory [9] argues that information is stored in human memory as a network of linked nodes. Presenting information consistent with such a network pattern can convey meaning regarding the information itself [27]. These networks can be arranged in a hierarchical structure to more clearly convey relationships between concepts [34]. Semantic networks have been applied successfully in the recent MIS literature as representation techniques for model management systems [1], business process reengineering models [48], and visualizations of large-scale electronic conversations [38].

## 2.2. Techniques for managing e-mail overload

The usual methods of reducing the amount of e-mail messages presented to a user are filtering and screening, whether manual or automatic. Automatic screening techniques (<sup>b</sup>spam filters<sup>Q</sup> or <sup>b</sup>junk filters<sup>Q</sup>) prevent some e-mails from ever reaching the user, diverting them into folders based on a pre-defined rule set. This may lead to the omission of potentially relevant information. Mackenzie [25,26] suggests that automating the screening and filtering of messages may have limited utility because the assessment of relevant information is best handled by the user. However, even manual screening or filtering of incoming messages [12,14], where users are encouraged to selectively attend to a subset of received e-mails (and presumably delete or ignore the rest), risks the omission of valuable information through erroneous assignment to an incorrect category [23]. In addition, manually prioritizing and screening incoming messages does little to reduce the cognitive load of individuals who must read through large volumes of e-mail messages. This is especially true if the task of reading the e-mail for classification approaches the complexity of reading the e-mail for content.

So far, the systems proposed to manage e-mail overload through a semantic network rather than a simplistic filtering approach [3,30,49] are limited to automatically classifying incoming e-mail messages into user-defined folders that may or may not be semantically related to one another. Mock [30] designed a system that places messages into categories based on the contents of existing folders and locates e-mails similar in content to a selected message. Balter and Sidner [3] created a prototype e-mail management system that contains a rule set that can be used to place incoming messages into predefined categories.

While potentially useful, these systems are limited in that users must still manually create categories or folders for incoming messages. Therefore, while these systems may aid in message retrieval, the problem of cognitive load when creating and maintaining the categories remains since the burden of maintaining the email classification scheme still falls on the user [49]. Kushmerick and Lau [24] recognized this issue, and proposed an interface that automatically identifies messages belonging to the same structured activity (an electronic commerce transaction). Their system is designed to support well-defined e-commerce transactions, and therefore is limited in scope. However, we believe that automatic clustering of any collection of email messages into a hierarchical semantic network would be an effective strategy for managing e-mail. Such automatically generated groups can be used in conjunction with other approaches (such as those mentioned above) for e-mail management.

## 2.3. Clustering

Automatic document clustering is a common and effective method of constructing semantic networks, despite claims that it is limited because users’ classification structures are too diverse to be captured by an automated process [17]. According to the cluster hypothesis [46], mutually similar documents will tend to be relevant to similar information needs. Therefore, document clustering has been commonly used for summarizing and presenting textual information, and has been applied to organizing web search results [36,37,45,47], static content on the web [8], and electronic group meeting output [7,31,35] by constructing semantic networks.

Clustering algorithms compute the similarity between textual documents for building clusters and assigning documents to them [37]. These algorithms are based on the principle that the more words and phrases the documents have in common, the more similar they are. Documents that do not share any common words or phrases would be considered the least similar and placed in different clusters. This technique has been shown to generate clusters that strongly resemble those produced by human experts. For example, Chen et al. [7] compared expert-generated clusters to automatically generated clusters on the output content of an electronic meeting, and found that the two sets of clusters were comparable. Moreover, participants in that study were more satisfied with the lower amount of time and the lower cognitive demands required while using an automated clustering tool.

Although these results suggest that textual clustering is a promising alternative to manual clustering, they do not provide evidence for the usefulness of clustering in general. To that end, Roussinov and Chen [36] implemented a method that takes advantage of particular mathematical representations of documents to achieve faster clustering. Due to this increased speed, this system could be highly interactive and allow its users to refine their searches multiple times. Through a controlled user study, the authors showed that this approach (<sup>b</sup>Adaptive Search<sup>Q</sup>) leads to speed improvements over the traditional output of a web search engine, and is preferred by its users.

Similar results in favor of clustering’s ability to improve content presentation while improving user satisfaction have been demonstrated in other studies (e.g., [20,32,41,45]). These studies provide evidence that managing large document collections (such as web pages) by using clustering would be successful. To our knowledge, automatic clustering has not, however, been specifically applied to an e-mail message collection.

## 3. Development of the Automatic Clustering E-Mail Management System (ACEMS)

The proof of concept implementation of our e-mail clustering strategy is based on applying an automatic text-clustering algorithm to a collection of e-mail messages. This approach exploits the structure of the message content (and the patterns relating content across messages) to categorize these messages into meaningful groups. The resulting hierarchically clustered structure would provide users a high-level characterization of the collection, and enhance the ability to locate individual messages. Presumably, the information in these messages is highly relevant for setting up the clusters into which they are organized; a system which takes advantage of this information should outperform one which does not. For example, given that the subject line of an e-mail message may be an important piece of information, grouping messages by their subject lines should then be useful [12]. Furthermore, an e-mail may contain potentially relevant information in multiple attributes (for example, subject and sender), therefore using a single attribute for clustering may not be sufficient.

To address this issue, we propose a multi-weight, multi-attribute clustering system that allows users to create clusters based on a combination of subject, sender, receiver, and text body. Users decide on the combination of these attributes by assigning different weights to different attributes. For this purpose, we created a proof of concept system. The Automatic Clustering E-Mail Management System (ACEMS) performs four key steps in the processing and presentation of a collection of e-mail messages. Details of those steps are described below and summarized in Fig. 1.

Step 1: Retrieve e-mail messages—A Java Server Page (JSP) application retrieves all e-mail messages from a user’s inbox using the JavaMail API. Each message is saved as a separate text file on the server’s disk drive in a directory with a unique session identifier.

Step 2: Generate <sup>b</sup>weighted<sup>Q</sup> e-mail messages—The Java application reads the messages from the directory and applies the user-defined weights to the attributes of each e-mail message. Weights are applied separately to the title, text body, sender, and receiver of the message. The weight attached to each attribute can vary depending on the preferences of the user (Fig. 2).

This weighted structure is operationalized by reading the plain text file that contains the e-mail message, applying the weights to each line in the message, and then writing the new file back to the hard disk. The weight $w _ { i }$ for each attribute is implemented by repeating the text for that attribute $w _ { i }$ times. For example, if the attribute <sup>b</sup>From<sup>Q</sup> had a weight of $w = 5$ , the text associated with the <sup>b</sup>From<sup>Q</sup> attribute of the message would be repeated five times. This approach was chosen because as is typical in text-clustering algorithms, the algorithm we use interprets this repetition as emphasis. Like many others, our clustering mechanism represents documents as a combination of their words and phrases. Words and phrases that occur more frequently will be weighted more heavily; therefore, a <sup>b</sup>weighted<sup>Q</sup> e-mail can be generated by repeating the text from different attributes of the e-mail. During this process, field titles such as <sup>b</sup>From<sup>Q</sup> are omitted so that the clustering tool would not consider them as part of the content of the message. A similar approach is used by certain commercial web sites to improve the ranking of their page in a typical web search since many search engines rank the result sets based on the similarity to a search query. In that approach, web pages are represented as a vector similar to the way e-mail messages are represented in our system.

![](/api/attachments/2QHQCARH/fulltext/images/d0756da4d439e8d7729b3313ca6e542df6e920ab78aa3ede400eda61069f025d.jpg)  
Fig. 1. ACEMS summary.

![](/api/attachments/2QHQCARH/fulltext/images/322afb11a953a0a845dd6badb2e843bfaa325607e6b9b63bec88f65da557fa0e.jpg)  
Fig. 2. Weight adjustment screen in ACEMS.

Step 3: Cluster <sup>b</sup>weighted<sup>Q</sup> messages—The processed messages are clustered by an <sup>b</sup>off the shelf<sup>Q</sup> tool. For the initial prototype, we used the hierarchical clustering component of IBM’s Intelligent Miner for Text. This clustering tool organizes the document collection into a hierarchy of clusters by first eliminating common noise words and then extracting key phrases from the weighted message collection and representing each message using those key phrases. This process creates a vector (one-dimensional array) for each message. The entry in the jth position of the vector contains the frequency $f _ { j }$ of the $j \mathrm { t h }$ key phrase in the corresponding message. Once these vectors are obtained, statistical procedures (such as Ward’s algorithm [15]) are used to cluster them.

The clustering process progresses by combining the two most similar elements found in each iteration. At the first iteration, all individual e-mails are considered. In consecutive iterations, e-mails that have not already been clustered and the previously constructed clusters are put through the clustering process. This process continues until every e-mail message belongs to a cluster. In each iteration, the similarity between elements is calculated as the scalar distance between the vectors representing those elements. The vector representing a cluster is calculated by averaging the vectors representing each element in the cluster. After the clustering process is complete, the cluster structure, the names of the clusters themselves, and messages contained in each cluster are stored in an output file.

Step 4: Present hierarchical clusters—The output of the clustering tool is read by the JSP application where it is parsed by a Java applet. The applet presents the hierarchy of clusters as a graphical tree. The clusters are represented as folders, and the e-mail messages are represented as documents within those folders. The program maps the documents within each cluster back to the original plain text file so that the message appears to the user in its original <sup>b</sup>unweighted<sup>Q</sup> form. The user can then navigate the tree by expanding and collapsing its branches in order to find and read specific messages. An example of the tree is provided in Fig. 3.

![](/api/attachments/2QHQCARH/fulltext/images/58e6b4b456c22d772d1045d0d46f7a9d1827571c60149f1da4c6bf680701696d.jpg)  
Fig. 3. Navigable tree generated from the ACEMS interface.

## 4. Research hypotheses for testing the usability of ACEMS

A primary benefit of decision support tools is that they enable their users to <sup>b</sup>save on cognitive resources<sup>Q</sup> ([27], p. 5) by pre-processing information. These savings can take the form of improved task performance, reduced effort, or both. We study the ability of our proposed system to reduce information overload by examining user task performance, effort expended, and intention to use-recognized aspects of success in user studies [13]. In this study, we interpret task performance as users’ ability to correctly locate e-mail messages containing desired information, effort expended as their perceived effort required to accomplish this level of effectiveness, and intention to use as the user’s selfreported intention to use the system in the future.

## 4.1. Measure of task performance: ability to locate e-mail messages

Speier and Morris [42] showed, in a study involving the use of a visual query tool, that a graphical decision aid can increase overall task performance. Essentially, the ACEMS tool creates a semantic network of message clusters, generating chunks of information linked through the hierarchical relationships inherent in the folder structure. The folder titles indicate the general content of the clusters, with related messages and clusters residing in the same folder. In accordance with semantic network theory, the folder structure will convey meaning regarding the information contained within the network of nodes [28]. Because the folders represent chunks of related information, the clustered format should enable navigation of message collections more effectively. This enables the user to <sup>b</sup>rule out<sup>Q</sup> groups of messages by avoiding irrelevant chunks, making the location of relevant messages easier with clustering. Varying the attribute weights allows the user to <sup>b</sup>tune<sup>Q</sup> the folder structure by experimenting with several different arrangements of the semantic network, each of which may have a different set of message clusters and folder names. Quillian’s [34] theory of semantic internalization predicts that a better-formed hierarchical folder structure should be more easily internalized, further enhancing the overall effectiveness of the tool. These theoretical foundations lead to the following hypotheses:

H1a. Compared to a non-cluster method, the clusteringbased e-mail management system with fixed or variable weights will increase a user’s ability to successfully locate an e-mail message.

H1b. Compared to a fixed, equal-weight system, a system that allows for varying the weights will increase a user’s ability to successfully locate an e-mail message.

## 4.2. Measure of effort expended: perceived effort required to locate messages

System success is not necessarily seen only in terms of increased task performance—a reduction in user effort or an increase in user’s intention to use the system in the future also serves as an important measure of success [36], particularly if performance is not compromised. Benbasat and Todd [5] posited that people equate effort with <sup>b</sup>cognitive cost<sup>Q</sup> and that they use decision aids to reduce that cost. Some studies have shown empirical evidence of a tradeoff between effort levels and performance: Todd and Benbasat [44] found that decision makers with access to better decision support tools emphasized completion speed over higher task success. In the Speier and Morris [42] study, however, the use of a visual query tool led to both a reduction in users’ mental effort and a simultaneous increase in task performance, implying that even further increases in performance would be possible if effort were maintained at the previous levels.

ACEMS is intended to increase the productivity of message search. Although it may impose a cognitive burden on the user initially by requiring them to decide on satisfactory attribute weights (especially if the user chooses to adjust the weights multiple times), the benefit is that the messages are placed within an intuitive structure. This eliminates the need to search either exhaustively or randomly to find the correct message. Saving this search cost should enable a user to achieve a similar level of message-location performance using less effort than they would without the aid of the clustering tool. As with our hypotheses regarding task performance, the flexibility to vary the attribute weights before determining the message clusters should result in a more intuitive folder structure. Consistent with Speier and Morris’ [42] study, it is possible for this to lead to less effort required to complete the task while still achieving a higher level of performance. Further, we believe that if subjects are (a) informed that sufficient time is available to complete the task and (b) given incentives attaching importance to the quality of their outcome, they can be encouraged to achieve this <sup>b</sup>simultaneous improvement<sup>Q</sup> outcome. From these arguments, we form the following two hypotheses:

H2a. Compared to a non-cluster method, the clustering-based e-mail management system with fixed or variable weights will reduce the perceived mental effort expended in the search and retrieval of e-mail messages.

H2b. Compared to a fixed, equal-weight system, a system that allows for varying the weights will reduce the perceived mental effort expended in the search and retrieval of e-mail messages.

## 4.3. Intention to use the e-mail management system

Ease of use and usefulness have been shown to positively influence intention to use a system (e.g., [11,33,43]), and can be used as a surrogate for satisfaction with that system. We assume that users prefer expending less mental effort and achieving higher performance. As some combination of reduction in mental effort and increase in search efficiency is achieved, we expect that users would find the automated-clustering system easier to use and more useful than a system that does not employ clustering. As a result, they will have a greater intention to use the system. From this, we form the following two hypotheses:

H3a. Compared to a non-cluster method, users will have a higher intention to use the clustering-based email management system with equal or variable weights.

H3b. Compared to a fixed, equal-weight system, users will have a higher intention to use the system that allows for varying the weights.

Support found for hypotheses H1a, H2a, or H3a will address the merit of the e-mail clustering concept in general, while support for hypotheses H1b, H2b, or H3b will show the incremental value of variable-weight clustering versus fixed, equal-weight clustering.

## 5. Experimental procedure and data collection

We conducted a controlled laboratory experiment to test the above hypotheses. The experimental subjects were 65 undergraduate students from an introductory computer literacy class at a large northeastern university. Since our study seeks to address the typical user of e-mail and students use e-mail for daily communications, the student population is an appropriate choice for the subject pool (arguments in the business literature against the use of student subjects for data collection are based on the premise that students are not representative of business managers [16]). The average age of the sample was 22.98, and 63% of our sample was female. Two incentives were offered to encourage participation. First, all participants were given extra credit. Second, the top two performers in each experimental condition were awarded a \$30 gift certificate.

Subjects were randomly assigned to one of three experimental conditions: no clustering, fixed (equal)- weighted clustering, and variable-weighted clustering. The subjects in the no-clustering condition were given a familiar, web-based e-mail client available to all users on the campus. Subjects assigned to the two clustering conditions were given different versions of ACEMS as described in Section 3—one version allowed the user to adjust the attribute weights, the other did not. Through a short questionnaire, we collected information about subjects’ e-mail experience and frequency of e-mail use, as well as whether English was their primary language. We used this data as control variables. After the questionnaire, the subjects received a short tutorial on the e-mail tool (based on their assignment), with opportunities to ask for clarification. The tutorial was most important for the two groups that were assigned versions of ACEMS, since most subjects were already familiar with the web-based client used for the no-clustering condition.

The subjects performed a message search-and-retrieval task that required working with the same, artificially generated electronic e-mail inbox. The messages used to generate the sample inbox were taken from the general campus news announcements sent to faculty, staff, and students in the university. The inbox consisted of 615 messages sent between the years 2000 and 2003. Accordingly, the experimental tasks involved answering a series of questions on various developments on campus that occurred during that time. The questions were selected such that an average student would not know the answer based on their prior knowledge (the list of questions is provided as Appendix A). Subjects were also told that the answers should come from the email collection and that an answer would not be considered correct if the source message could not be found in the collection.

The subjects were given 20 min for the completion of the experimental task. Two exit questionnaires measured the subjects’ perceived level of effort required to complete the tasks and their intention to use the tool (that they used in the experiment) in the future.

## 6. Analysis of experimental data

To measure perceived effort, we used the NASA-TLX instrument [19], which was used in previous IS studies to measure mental workload [18,42]. This instrument asks respondents to pairwise rank six dimensions of effort as they relate to a task, and then rank the overall level of each dimension on an absolute scale from 1 to 7. The number of times each dimension <sup>b</sup>won<sup>Q</sup> a pairwise comparison is multiplied by its overall level in order to arrive at a weighted measure of perceived overall effort. Our adaptation of the NASA/TLX instrument is included as Appendix B.

The <sup>b</sup>intention to use<sup>Q</sup> questionnaire was adapted from Taylor and Todd [43] and Plouffe et al. [33] and is included as Appendix C. A factor analysis verified that all the items on this questionnaire measure a single construct (i.e., intention to use) (the factor loadings were 0.92, 0.93, 0.79, and 0.94 for items 1 through 4 respectively). Therefore, the individual item scores were averaged to create a single intention score for each experimental subject.

After the experiments, two graduate students (who were aware neither of the purpose of the study nor the experimental conditions to which subjects were assigned) were given an answer key and asked to evaluate the subjects’ answers to the questions in the experiment to create a performance rating (the effectiveness measure). For each subject, each answer was marked right or wrong according to the rater’s judgment. Subjects received a final, scaled score from 0 to 100 based on the percentage of questions they correctly answered. Inter-rater reliability measured by Pearson correlations was sufficiently high (0.950, p <sup>b</sup> 0.01); therefore we averaged the raters’ evaluations to arrive at the subject’s overall score.

The data were analyzed using both multivariate and univariate analysis of variance (MANOVA/ANOVA) models because, as seen in Table 1, the dependent variables score and intention to use (the system in the future) were significantly correlated $( \rho = 0 . 3 0 2 , ~ p = 0 . 0 1 7 )$ However, perceived effort was not significantly correlated with either score (q = 0.071, p = 0.584) or intention to use $( \rho = - 0 . 6 0 , p = 0 . 5 8 4 )$ . Therefore, we constructed a bivariate MANOVA model using subject performance score and intention to use as the dependent variables, the e-mail tool condition as the independent variable (as reported in the hypotheses development section), and control variables of length of e-mail use, frequency of e-mail use, and whether English was the subject’s native language. A separate, but similar, ANOVA model was constructed with perceived effort as the dependent variable.

Table 1  
Dependent variable correlations

<table><tr><td colspan="2"></td><td>Score</td><td>Intention to use</td><td>Perceived effort</td></tr><tr><td rowspan="2">Score</td><td>Pearson ρ</td><td>1</td><td>.302(*)</td><td>.071</td></tr><tr><td>Significance (2-tailed)</td><td>-</td><td>.017</td><td>.584</td></tr><tr><td rowspan="2">Intention to use</td><td>Pearson ρ</td><td>.302(*)</td><td>1</td><td>-.060</td></tr><tr><td>Significance (2-tailed)</td><td>.017</td><td>-</td><td>.642</td></tr><tr><td rowspan="2">Effort</td><td>Pearson ρ</td><td>.071</td><td>-.060</td><td>1</td></tr><tr><td>Significance (2-tailed)</td><td>.584</td><td>.642</td><td>-</td></tr></table>

\*Correlation is significant at the 0.05 level (2-tailed).

To verify the appropriateness of (M)ANOVA, we verified that the assumptions of normality and homogeneity of error variance across groups were upheld. The results of these tests are found in Appendix D. Normality was verified by examining normal plots of the dependent variables (see Fig. D-1 through D-3). Levene’s test was used to test the error variance across groups (see Table D-1), and Box’s M statistic was used to verify the assumption of equality of covariance matrices required by MANOVA (see Table D-2). For score and intention to use, the error variances across groups as well as the covariance matrices are equal, indicating the MANOVA is appropriate for our analysis. However, there are unequal error variances across groups for perceived effort, implying that the F-statistic associated with the ANOVA model will be overly sensitive in detecting a difference between groups (i.e., a difference might be detected where one does not exist). Therefore, the findings regarding perceived effort should be interpreted with caution.

The results of the overall MANOVA model (the effects of the independent variables on both score and intention to use) are shown in Table 2. We have included two common test statistics, Pillai’s Trace and Wilks Lambda, in the table to show the robustness of the results. The only statistically significant variable using either test statistic was the e-mail tool ( p = 0.018, 0.014<sup>b</sup>0.05).

To test the individual hypotheses we separately examined the between-subjects effects of the independent variables on score and intention to use. We used three paired contrasts to test for differences among the three levels of the independent variable <sup>b</sup>e-mail tool.<sup>Q</sup> Tables 3 and 4 summarize the results of the tests for hypotheses H1a and H1b. As seen in Table 3, the overall effect of the e-mail tool on task score is highly significant $( p = 0 . 0 0 9 < 0 . 0 1 )$ . We then examined the results of two paired contrasts by looking at the contrast estimate (see Table 4), which reflects the estimated difference in the effect of varying levels of the independent variable (the tool) on the dependent variable (i.e., task score) after we account for the effects of the other independent variables. First, we compared the effect of the two clustering-based systems (separately and pooled) to those with no clustering. The effect of the variable-weight clustering tool was then compared to that of the equal-weight clustering tool. As seen in Table 4, the difference in effect between the pooled clustering and list-based tools is 21.928 points (in favor of the clusteringbased tools), and this difference is highly significant

Table 2  
Results of multivariate analysis of variance

<table><tr><td>Variable</td><td></td><td> $df_{h}$ </td><td> $df_{e}$ </td><td>F</td><td>p</td></tr><tr><td rowspan="2">(E-mail) Tool</td><td>Pillai&#x27;s Trace</td><td>4</td><td>88</td><td>3.136</td><td>0.018</td></tr><tr><td>Wilks&#x27; Lambda</td><td>4</td><td>88</td><td>3.313</td><td>0.014</td></tr><tr><td rowspan="2">Frequency (of e-mail use)</td><td>Pillai&#x27;s Trace</td><td>6</td><td>90</td><td>0.475</td><td>0.825</td></tr><tr><td>Wilks&#x27; Lambda</td><td>6</td><td>88</td><td>0.467</td><td>0.831</td></tr><tr><td rowspan="2">English (as first language)</td><td>Pillai&#x27;s Trace</td><td>2</td><td>44</td><td>1.213</td><td>0.307</td></tr><tr><td>Wilks&#x27; Lambda</td><td>2</td><td>44</td><td>1.213</td><td>0.307</td></tr><tr><td rowspan="2">Length (of e-mail use)</td><td>Pillai&#x27;s Trace</td><td>2</td><td>44</td><td>2.013</td><td>0.146</td></tr><tr><td>Wilks&#x27; Lambda</td><td>2</td><td>44</td><td>2.013</td><td>0.146</td></tr><tr><td rowspan="2">Tool * Frequency</td><td>Pillai&#x27;s Trace</td><td>8</td><td>90</td><td>1.789</td><td>0.090</td></tr><tr><td>Wilks&#x27; Lambda</td><td>8</td><td>88</td><td>1.782</td><td>0.091</td></tr><tr><td rowspan="2">Tool * English</td><td>Pillai&#x27;s Trace</td><td>4</td><td>90</td><td>0.992</td><td>0.416</td></tr><tr><td>Wilks&#x27; Lambda</td><td>4</td><td>88</td><td>0.989</td><td>0.418</td></tr><tr><td rowspan="2">English * Frequency</td><td>Pillai&#x27;s Trace</td><td>4</td><td>90</td><td>0.129</td><td>0.972</td></tr><tr><td>Wilks&#x27; Lambda</td><td>4</td><td>88</td><td>0.126</td><td>0.973</td></tr></table>

df<sub>h</sub>—hypothesis df.  
df<sub>e</sub>—error df.

Table 3  
Effects of independent variables on performance

<table><tr><td>Variable</td><td>df</td><td>F</td><td>p</td></tr><tr><td>(E-mail) Tool</td><td>2</td><td>5.195</td><td>0.009#</td></tr><tr><td>Frequency (of e-mail use)</td><td>3</td><td>0.552</td><td>0.649</td></tr><tr><td>English (as first language)</td><td>1</td><td>2.443</td><td>0.125</td></tr><tr><td>Length (of e-mail use)</td><td>1</td><td>4.084</td><td>0.049**</td></tr><tr><td>Tool * Frequency</td><td>4</td><td>2.367</td><td>0.067**</td></tr><tr><td>Tool * English</td><td>2</td><td>1.672</td><td>0.199</td></tr><tr><td>English * Frequency</td><td>2</td><td>0.123</td><td>0.884</td></tr></table>

R<sup>2</sup> =0.409.  
\*: statistically significant at the 10% level; \*\*: statistically significant at the 5% level.  
#: statistically significant at the 1% level.

Table 4  
Test of Hypothesis 1—effect of e-mail tool on performance

<table><tr><td>Fixed-weight clustering tool vs. list-based tool</td><td>Contrast estimate p-value (1-sided)</td><td>16.409 0.05**</td></tr><tr><td>Variable-weight clustering tool vs. list-based tool</td><td>Contrast estimate p-value (1-sided)</td><td>27.446 0.001#</td></tr><tr><td>Clustering-based tools vs. list-based tool (samples pooled to increase test power)</td><td>Contrast estimate p-value (1-sided)</td><td>21.928 0.006#</td></tr><tr><td>Variable-weight clustering vs. fixed-weight clustering</td><td>Contrast estimate p-value (1-sided)</td><td>11.037 0.071*</td></tr></table>

\*: statistically significant at the 10% level; \*\*: statistically significant at the 5% level.  
#: statistically significant at the 1% level

R<sup>2</sup> =0.177.

$\scriptstyle ( p = 0 . 0 0 6 )$ The difference in effect between just the fixed-weight clustering and list-based tools is 16.409 points (in favor of the fixed-weight clustering tool), which is significant at the 5% level using a 1- tailed t-test $( p = 0 . 0 5 )$ , in keeping with our strongly directional hypothesis H1a. The difference in the effect of the variable-weight clustering tool and that of the no-clustering tool is 27.45 (in favor of the variable-weight clustering); this difference is significant at the 1% level using a 1-tailed t-test $\left( { { p = 0 . 0 0 1 } } \right)$ . The difference in the effect of the variable-weight clustering tool and that of the fixed-weight clustering tool is 11.037 points (in favor of the variable-weight clustering); this difference is marginally significant at the 10% level but not at the 5% level given our limited sample size $( p = 0 . 0 7 1 )$ . These results thus support H1a, but provide only marginal support for H1b.

Table 5 shows the results of the tests for the third group of hypotheses (H3a and H3b), also tested as part of the MANOVA model. As seen in the table, the effect of the e-mail tool on intention to use is clearly not significant $\left( p = 0 . 7 3 \right)$ . Therefore, we found no statistical evidence to support hypotheses H3a and H3b.

Because the correlation between perceived effort and the other two independent variables was not statistically significant, we ran an analysis of the effect of the independent variables on perceived effort as a separate ANOVA model (see Table 6) to test hypotheses H2a and H2b. As with intention to use, the effect of the e-mail tool on perceived mental effort is not significant $( p = 0 . 8 0 5 )$ . Because there is a risk that the F-test will be overly sensitive when ANOVA’s homoskedacity assumption is violated, these p-values will be understated—that is, there is a chance that an effect may be detected when none exists. Because none of the effects was statistically significant in this model, this bias reinforces our conclusions that hypotheses H2a and H2b were not supported.

Table 5  
Effects of independent variables on intention to use

<table><tr><td>Variable</td><td>df</td><td>F</td><td>p</td></tr><tr><td>(E-mail) Tool</td><td>2</td><td>0.317</td><td>0.730</td></tr><tr><td>Frequency (of e-mail use)</td><td>3</td><td>0.263</td><td>0.852</td></tr><tr><td>English (as first language)</td><td>1</td><td>0.132</td><td>0.718</td></tr><tr><td>Length (of e-mail use)</td><td>1</td><td>0.767</td><td>0.386</td></tr><tr><td>Tool* Frequency</td><td>4</td><td>0.955</td><td>0.441</td></tr><tr><td>Tool* English</td><td>2</td><td>0.082</td><td>0.921</td></tr><tr><td>English* Frequency</td><td>2</td><td>0.184</td><td>0.832</td></tr></table>

Table 6  
Effects of independent variables on perceived effort

<table><tr><td>Variable</td><td>df</td><td>F</td><td>p</td></tr><tr><td>(E-mail) Tool</td><td>2</td><td>0.218</td><td>0.805</td></tr><tr><td>Frequency (of e-mail use)</td><td>3</td><td>1.626</td><td>0.196</td></tr><tr><td>English (as first language)</td><td>1</td><td>1.907</td><td>0.174</td></tr><tr><td>Length (of e-mail use)</td><td>1</td><td>3.458</td><td>0.069</td></tr><tr><td>Tool* Frequency</td><td>4</td><td>0.633</td><td>0.641</td></tr><tr><td>Tool* English</td><td>2</td><td>0.618</td><td>0.543</td></tr><tr><td>English* Frequency</td><td>2</td><td>0.133</td><td>0.876</td></tr></table>

$$
R ^ {2} = 0. 2 8 1.
$$

The poor ability of these apparently relevant independent variables to explain the variance of the amount of effort expended on the task suggests that the amount of effort chosen by the subjects in the three groups was quite similar. Our finding that comparable amounts of effort were invested over the 20-min span of the experiment while, at the same time, performance increased is interesting from a theoretical standpoint. It contradicts the predictions from Todd and Benbasat [44] and Benbasat and Todd [5] that effort should noticeably decrease when a superior tool is introduced.

Also, there appears to be no difference in intention to use among an ordered list, the clustering system with fixed and equal attribute weights, and the clustering system with adjustable weights. All of the system’s advantage seems to be concentrated in performance improvement in our setting (which offered rewards for the highest levels of performance). While we did not find evidence to support our initial hypotheses that the two versions of ACEMS (with fixed equal-weight clustering and adjustable-weight clustering) would improve intention to use, we believe our findings are encouraging for applications in settings where performance matters, because our approach clearly improves message-retrieval performance without additional effort or reduction in intention to use. We discuss the implications and conclusions of these results in the following sections.

## 7. Limitations and implications for future research

Three main limitations to our study present opportunities for future research. First, while the mailbox used in our study was intended to be large enough to reveal differences between the three groups, we did not find differences in perceived effort or intention to use. This may be because the mailbox was simply too small, or that the cognitive effort saved in locating the messages was offset by the effort required to parse the automatically generated set of folders. It would be useful to explore the scalability of this tool using a much larger mailbox (thousands of messages). Future experiments could also integrate more descriptive techniques regarding subjects’ message navigation patterns, such as protocol analysis, in order to determine the specific nature of the tradeoff between the effort required to interpret the folder structure and the reduced <sup>b</sup>search cost<sup>Q</sup> in locating a message once that structure was understood. This would provide additional insight into our hypothesized (but unsupported) reduction in perceived effort as a result of using our tool.

A second limitation of our study involves the use of general campus announcements as the source of our messages. This collection had the advantage of having generic, subject-independent content (i.e., the messages were easily understandable by everyone) and enabled us to have every subject work on identical tasks (thus providing greater experimental control). This approach increased internal validity and clearly demonstrated the value of our system. However, our message collection does not comprise the entirety of a user’s <sup>b</sup>typical<sup>Q</sup> inbox. Applying the ACEMS tool to a collection of messages from a user’s actual inbox would be an important step in verifying the usefulness of our clustering system while also providing higher external validity.

Third, because the foci of our experiment were message retrieval and extraction of pertinent information, our claims regarding the ACEMS tool must be interpreted with caution outside of the experimental task. Future studies should involve tasks that test other aspects of creating appropriate clusters for message collections, such as understanding high-level relationships among messages that may appear unrelated. We believe that the advantage of being able to vary the attributes’ weights will show up more clearly in these more complex tasks.

One such task could involve applying this clustering approach across the e-mail inboxes of multiple users. This way, knowledge distributed across the organization can be classified at a central location and used to interpret multiple users’ message collections. This information aggregation can lead to insights about the extraction of knowledge at the organization level from collections of electronic mail messages that are not easily attainable by traditional knowledge management techniques. The application of this centralized knowledge about the organization’s e-mail message base as a whole can lead to improved clustering (and associated retrieval performance) for all users for a single investment in clustering technology.

Finally, while we found that ACEMS improved task performance, it did so over that of a very basic information technology: an ordered list in a webbased email interface. The control group’s tool was chosen specifically for its <sup>b</sup>no clustering<sup>Q</sup> property and its standard and familiar interface for the test subjects. Other than subjects’ familiarity with the web-based interface, the only difference between the tools was the clustering support. The automated clustering tool could also be compared against a more sophisticated email tool (such as Microsoft Outlook), which also allows for a manually generated folder structure. We believe that ACEMS would lead to performance improvements over a manually generated folder structure not by replacing manual folders, but by supplementing them with another view of the email collection. Such a combined approach is worth exploring because it has the potential to use existing, familiar technologies to increase the effectiveness of an ever-growing population of e-mail users.

## 8. Conclusions

This paper expands prior research on document clustering to the domain of e-mail management. We hypothesized that applying a multi-weight, multi-attribute clustering approach to a collection of e-mail messages would increase retrieval effectiveness, reduce perceived effort, and increase intention to use. Our prototype system (ACEMS) showed that the use of clustering improves user effectiveness at finding information in an electronic mailbox by 41% to 69% over a simple ordered list of electronic mail messages, the default structure for most currently available e-mail clients.

The results of this research are potentially important for both academics and practitioners. For academics, this study integrates the concepts of semantic network theory and research on human memory chunking from cognitive psychology with prior information-science studies on textual document clustering. We extended this research to include clustering on key attributes of a textual document (in this case, attributes of an e-mail message). The ACEMS experiment has two implications for theory. First, while the application of a semantic network to an e-mail collection resulted in a nearly 41% improvement in task effectiveness, the additional increase from customizing the structure of the network was only marginally significant. This combination of results implies that most of the performance increase offered by a semantic network is in simply implementing the clustering structure in the first place—the specific choice of labels and the arrangement of nodes increase performance relatively less. While the impact of the ability to adjust attribute weights on performance remains an important issue, a more complex task is required to further explore the potential benefits of the effectiveness of adjustable weights.

Second, we believe that our ACEMS implementation offers a general contribution in extending the application of semantic network theory to the domain of textual knowledge management. Such an extension should offer insight into the specific relationships between the way a semantic network of textual information is created and the experiences of an enduser by whom that network is used. In this specific implementation, we observed that the benefits from a hierarchical cluster structure manifested themselves in the form of performance increases. This offers an additional finding in the stream of research regarding the tradeoff between task performance and effort when evaluating an information system. We found that subjects using ACEMS did not appear to expend any additional effort, but still achieved a significantly greater level of task performance.

These results are in contrast to Todd and Benbasat [44] and Benbasat and Todd’s [5] claim that users will reduce their effort when possible, resulting in comparable task performance even when using different and better tools. One possible explanation of this discrepancy is that the effort-minimization argument explains decision-makers’ natural behavior when they are given better tools without any incentive to perform better. Incentives for improved performance (as in our study) result in performance increases rather than a reduction in effort. In our experiments, we gave an explicit incentive (a gift certificate) to student subjects. For this reason, they may have maximized their effort, performing as effectively as they possibly could in either technology condition. Subjects treated with the improved technology achieved substantial performance increases with the same level of effort. We believe that this finding lends additional insight into end users’ tradeoff between performance and effort and the optimal implementation of labor-saving IT tools in general. It also points to the need for research to extend the theories on the impact of a system on user performance and behavior in a way to provide a holistic view of the relationship between these outcomes.

For practitioners, this study details a practical, simple implementation of a method of automatically organizing electronic mail messages into a hierarchy that can be easily navigated. ACEMS could be implemented as an add-in to an existing e-mail management system (e.g., Microsoft Outlook or Google’s Gmail) to increase its usability for the individual user and its value as a knowledge management tool for the organization as a whole. The intention is that this add-in would be implemented as an alternate mechanism for locating and viewing messages, supplementing the application’s default view of its <sup>b</sup>live<sup>Q</sup> inbox. This clustered view could be refreshed periodically as new messages are received.

For organizations suffering from reduced productivity due to e-mail overload, ACEMS offers several opportunities. On an individual level, this tool could be used as an aid for managing a single e-mail inbox. On an enterprise level, by grouping related email messages in a central location, the system could be part of a larger knowledge-management effort, which offers benefits to each participating user. Given that the ability to draw meaningful interpretations from massive amounts of information without being overwhelmed is a key challenge for the successful management of knowledge, the ability of information systems to effectively cluster and present that knowledge is important to address that challenge.

## Acknowledgements

The authors would like to thank David Croson for his helpful comments with regard to framing the motivation for this paper. The authors would also like to thank Xiaobin Li for his work coding the prototype system.

## Appendix A. Task questions

1. Name two locations on the University’s main campus where the American Red Cross Blood Drive has been held.

2. Who was named acting dean of the University School of Medicine in 2002?

3. What steps must the University take to conserve electricity in the event that a University-wide energy alert is issued during a summer heat wave?

4. What is the name of the United Nations security expert on crime who spoke at the University?

5. What date did United States senator Arlen Specter visit the University and where was his presentation held?

## Appendix B. Mental effort questionnaire

The following are dimensions of demand which could describe the task you have just completed:

<table><tr><td></td><td>Item</td><td>Description</td></tr><tr><td>MD</td><td>Mental Demand</td><td>How much mental and perceptual activity was required? Was the task easy or demanding, simple or complex?</td></tr><tr><td>PD</td><td>Physical Demand</td><td>How much physical activity was required? Was the task easy or demanding, slack or strenuous?</td></tr><tr><td>TD</td><td>Temporal Demand</td><td>How much time pressure did you feel due to the pace at which the tasks or task elements occurred? Was the pace slow or rapid?</td></tr><tr><td>OP</td><td>Overall Performance</td><td>How successful were you in performing the task? How satisfied were you with your performance?</td></tr><tr><td>FR</td><td>Frustration Level</td><td>How irritated, stressed, and annoyed versus content, relaxed, and complacent did you feel during the task?</td></tr><tr><td>EF</td><td>Effort</td><td>How hard did you have to work (mentally and physically) to accomplish your level of performance?</td></tr></table>

1) From each of the 15 pairs below, select the item that was the larger factor for you while performing the task you just completed (for example, for the first pair, was there more physical demand or mental demand while completing the task?).

<table><tr><td>PD</td><td>MD</td></tr><tr><td>TD</td><td>MD</td></tr><tr><td>OP</td><td>MD</td></tr><tr><td>FR</td><td>MD</td></tr><tr><td>EF</td><td>MD</td></tr></table>

<table><tr><td>□ TD</td><td>□ PD</td></tr><tr><td>□ OP</td><td>□ PD</td></tr><tr><td>□ FR</td><td>□ PD</td></tr><tr><td>□ EF</td><td>□ PD</td></tr><tr><td>□ TD</td><td>□ OP</td></tr></table>

<table><tr><td>□ TD</td><td>□ FR</td></tr><tr><td>□ TD</td><td>□ EF</td></tr><tr><td>□ OP</td><td>□ FR</td></tr><tr><td>□ OP</td><td>□ EF</td></tr><tr><td>□ EF</td><td>□ FR</td></tr></table>

2) For each type of demand below, rate its overall level for the task you just completed (for example, what was the level of mental demand for this task?).

<table><tr><td rowspan="2">Demands</td><td colspan="7">Ratings for task</td></tr><tr><td colspan="6">Low</td><td>High</td></tr><tr><td rowspan="2">MD</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">PD</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">TD</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">OP</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">FR</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">EF</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr></table>

## Appendix C. Intention to use questionnaire

Please answer each of the questions below as they pertain to your experience using the e-mail tool to perform the tasks you have just completed:

<table><tr><td></td><td>Strongly disagree</td><td>Disagree</td><td>Somewhat disagree</td><td>Neither agree nor disagree</td><td>Somewhat agree</td><td>Agree</td><td>Strongly agree</td></tr><tr><td rowspan="2">1. I would use this e-mail interface.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">2. I would use this e-mail interface regularly as part of a regular e-mail client.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">3. I see little need to use this e-mail interface.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td rowspan="2">4. I would encourage others to use this e-mail interface.</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr></table>

## Appendix D. MANOVA and ANOVA Diagnostics

Table D-1: Levene’s test of equality of error variances

<table><tr><td>Dependent variable</td><td>df1</td><td>df2</td><td>p</td></tr><tr><td>Score</td><td>15</td><td>46</td><td>0.116</td></tr><tr><td>Intention to use</td><td>15</td><td>46</td><td>0.072</td></tr><tr><td>Perceived effort</td><td>46</td><td>16</td><td>0.001</td></tr></table>

Tests $\operatorname { H } _ { 0 } { \mathrm { : } }$ Error variance equal across groups.

## References

[1] L.M. Applegate, G. Klein, B.R. Konsynski, J.F. Nunamaker, Model management systems: proposed model representations and future designs, Proceedings From the 6th International Conference on Information Systems, Association for Information Systems, Atlanta, Georgia, 1985.

[2] M.H. Ashcraft, Human Memory And Cognition, Scott, Foresman and Co., Glenview, IL, 1989.

[3] O. Balter, C.L. Sidner, Bifrost Inbox Organizer: giving users control over the inbox. Proceedings of the Second Nordic Conference on Human–Computer Interaction, ACM Press, New York, New York, 2002, pp. 111– 118.

[4] E. Barnfield, 2003: Year of internal communication? Strategic Communication Management 7 (1) (2002) 3 – 4.

[5] I. Benbasat, P. Todd, The effects of decision support and task contingencies on model formulation: a cognitive perspective, Decision Support Systems 17 (4) (1996) 241– 252.

[6] D. Blackwell, Comparison of experiments, Proceedings of the Second Berkeley Symposium on Mathematical Statistics and Probability, University of California Press, Berkeley, Los Angeles, CA, 1951, pp. 93– 102.

Table D-2: Box’s M test of equality of covariance matrices (MANOVA)

<table><tr><td>Box&#x27;s M statistic</td><td>F</td><td>df1</td><td>df2</td><td>p</td></tr><tr><td>29.685</td><td>1.084</td><td>21</td><td>993.776</td><td>0.359</td></tr></table>

[7] H. Chen, J. Nunamaker, R. Orwig, O. Titkova, Information visualization for collaborative computing, IEEE Computer 31 (8) (1998) 75– 82.

[8] H. Chen, C. Schuffels, R. Orwig, Internet categorization and search: a self-organizing approach, Journal of Visual Communication and Image Representation 7 (1) (1996) 88– 102.

[9] A.M. Collins, M.R. Quillian, Retrieval time from semantic memory, Journal of Learning and Verbal Behavior 8 (1969) 240– 247.

[10] L. Cranor, B. LaMacchia, Spam! Communications of the ACM 41 (8) (1998) 74– 83.

[11] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, Management Information Systems Quarterly 13 (3) (1989) 319– 340.

[12] R. Davidhizar, R. Shearer, A dilemma of modern technology: managing e-mail overload, Hospital Material Management Quarterly 21 (3) (2000) 42– 47.

[13] W.H. DeLone, E.R. McLean, Information system success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60– 95.

[14] P. Denning, The profession of IT, Communications of the ACM 45 (3) (2002) 15– 18.

Normal P-P Plot of Score

Fig. D-1, D-2, and D-3: Normal P–P plots of score, perceived effort, and intention to use.

![](/api/attachments/2QHQCARH/fulltext/images/d5b48f351ea26ca5351747bff195dfebc5e706808d5fae58b5bccb5fbb944279.jpg)

![](/api/attachments/2QHQCARH/fulltext/images/0d77c26108508d496edb135e17213bb43168ce2ec4a07bedc2133dafa4d82a61.jpg)

Normal P-P Plot of Intention to Use  
![](/api/attachments/2QHQCARH/fulltext/images/dd87b607fc718e74706c1e2d62eaf95482fe7ef8c4fb82796c0c6654d37e16bb.jpg)

[15] B. Everitt, Cluster Analysis, Heineman Educational Books, London, 1974.

[16] M. Gordon, L. Slade, N. Schmitt, The <sup>d</sup>Science of the Sophomore<sup>T</sup> revisited: from conjecture to empiricism, Academy of Management Review 11 (1) (1986) 191– 207.

[17] L. Gottlieb, J. Dilevko, Investigating how individuals conceptually and physically structure file folders for electronic bookmarks: the example of the financial services industry, Journal of the American Society for Information Science and Technology 54 (2) (2003) 124– 139.

[18] M. Grise´, R.B. Gallupe, Information overload: addressing the productivity paradox in face-to-face electronic meetings, Journal of Management Information Systems 16 (3) (2000) 157–185.

[19] S. Hart, L. Staveland, Development of NASA-TLX: results of empirical and theoretical research, in: P. Hancock, N. Meshkati (Eds.), Advances in Psychology, North Holland, Amsterdam, 1988, pp. 139– 184.

[20] M. Hearst, P. Pedersen, Reexamining the cluster hypothesis: scatter/gather on retrieval results, Proceedings of the 1996 Con

ference on Research and Development in Information Retrieval, Zurich, Switzerland, 1996.

[21] S.R. Hiltz, M. Turoff, Structuring computer-mediated communication systems to avoid information overload, Communications of the ACM 28 (7) (1985) 680–689.

[22] G. Johnston, We’ve got mail: 60 billion daily, PCWorld.com (Accessed March 30, 2005) Available at http://www.pcworld. com/resource/printable/article/0,aid,105525,00.asp.

[23] R. Kraut, S. Sunder, J. Morris, M. Cronin, D. Filer, Markets for attention: Will postage for email help? ACM Conference Proceedings on Computer Supported Cooperative Work, ACM Press, New York, NY, 2002, pp. 206– 215.

[24] N. Kushmerick, T. Lau, Automated email activity management: an unsupervised learning approach, Proceedings of the 10th international conference on intelligent user interfaces, ACM Press, New York, NY, 2005, pp. 67– 74.

[25] M. Mackenzie, The personal organization of electronic mail messages in a business environment: an exploratory study, Library and Information Science Research 22 (4) (2000) 405–426.

[26] M. Mackenzie, Storage and retrieval of e-mail in a business environment: an exploratory study, Library and Information Science Research 24 (3) (2002) 357–372.

[27] G. Mandler, Organization in memory, in: K.W. Spence, J.T. Spence (Eds.), The Psychology of Learning and Motivation, Academic Press, New York, NY, 1967, pp. 327–372.

[28] G. Marakas, Decision Support Systems in the 21st Century, Prentice Hall, Upper Saddle River, New Jersey, 2003.

[29] G.A. Miller, Information input overload, in: M.C. Yovits, G.T. Jacobi, G.D. Goldstein (Eds.), Proceedings of the Conference on Self-Organizing Systems, Spartan Books, Washington, 1962.

[30] K. Mock, An experimental framework for email categorization and management, Proceedings of the 24th Annual ACM International Conference on Research and Development in Information Retrieval, ACM Press, New York, NY, 2001, pp. 392– 393.

[31] R.E. Orwig, H. Chen, J. Nunamaker, A graphical, self-organizing approach to classifying electronic meeting output, Journal of the American Society for Information Science 48 (2) (1997) 157– 170.

[32] P. Pirolli, P. Schank, M. Hearst, C. Diehl, Scatter/gather browsing communicates the topic structure of a very large text collection, Proceedings of the Conference on Human Factors in Computing Systems, ACM Press, New York, NY, 1996.

[33] C. Plouffe, J. Hulland, M. Vandenbosch, Research report: richness versus parsimony in modeling technology adoption decisions—understanding merchant adoption of a smart card-based payment system, Information Systems Research 12 (2) (2001) 208– 222.

[34] M.R. Quillian, Semantic memory, in: M. Minsky (Ed.), Semantic Information Processing, The MIT Press, Cambridge, MA, 1968, pp. 227 – 270.

[35] D.G. Roussinov, H. Chen, Document clustering for electronic meetings: an experimental comparison of two techniques, Decision Support Systems 27 (1–2) (1999) 67–79.

[36] D.G. Roussinov, H. Chen, Information navigation on the web by clustering and summarizing query results, Information Processing and Management 37 (6) (2001) 789– 817.

[37] D.G. Roussinov, J.L. Zhao, Automatic discovery of similarity relationships through web mining, Decision Support Systems 35 (1) (2003) 149– 166.

[38] W. Sack, Conversation map: an interface for very large-scale conversations, Journal of Management Information Systems 17 (3) (2000) 73– 92.

[39] G. Salton, Automatic Text Processing: The Transformation, Analysis, and Retrieval of Information by Computer, Addison-Wesley, Reading, MA, 1989.

[40] U. Schultze, B. Vandenbosch, Information overload in a groupware environment: now you see it, now you don’t, Journal of Organizational Computing and Electronic Commerce 8 (2) (1998) 127–148.

[41] S. Spangler, J.T. Kreulen, J. Lessler, Generating and browsing multiple taxonomies over a document collection, Journal of Management Information Systems 19 (4) (2003) 191– 212.

[42] C. Speier, M.G. Morris, The influence of query interface design on decision-making performance, Management Information Systems Quarterly 27 (3) (2003) 397– 423.

[43] S. Taylor, P. Todd, Understanding information technology usage: a test of competing models, Information Systems Research 6 (2) (1995) 144–176.

[44] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer based decision aids, Management Information Systems Quarterly 16 (3) (1992) 373– 393.

[45] O. Turetken, R. Sharda, Development of a fisheye-based information search processing aid (FISPA) for managing information overload in the web environment, Decision Support Systems 37 (3) (2004) 415– 434.

[46] C. van Rijsbergen, Information Retrieval, 2nd Edition, Butterworths, London, 1979.

[47] Vivisimo Corporation, Clustering Engine—Introduction, (Accessed March 30, 2005). Available at http://vivisimo.com products/Clustering<sup>\_</sup>Engine/Introduction.html.

[48] S. Wang, A synthesis of natural language, semantic networks, and objects for business process modeling, Canadian Journal of Administrative Sciences 14 (1) (1997) 79 – 92.

[49] S. Whittaker, C. Sidner, Email overload: exploring personal information management of email, Proceedings of the ACM SIGCHI conference on Human factors in computing systems, ACM Press, New York, NY, 1996, pp. 276–283.

David Schuff is Assistant Professor of Management Information Systems in the Fox School of Business and Management at Temple University. He holds a BA in Economics from the University of Pittsburgh, an MBA from Villanova University, an MS in Information Management from Arizona State University, and a PhD in Business Administration from Arizona State University. His research interests include the strategic use of information systems, the assessment of total cost of ownership in large networked organizations, and data warehousing. His work has been published in journals such as Communications of the ACM, Information Systems Journal, and the European Journal of Operational Research.

Ozgur Turetken is Assistant Professor of Management Information Systems in the Fox School of Business and Management at Temple University. He received a BS in Electrical Engineering and an MBA from Middle East Technical University in Ankara, Turkey, and a PhD from Oklahoma State University. Dr. Turetken’s research interests are information visualization, decision support systems, and distributed work arrangements. His research has been published in Communications of the ACM, Decision Support Systems, Information Systems Frontiers, and in refereed proceedings of international conferences such as the International Conference on Information Systems (ICIS).

John D’Arcy is Assistant Professor of Computer and Information Sciences at Towson University. He holds a BS in Finance and Business Logistics from The Pennsylvania State University, an MBA in Management Information Systems from LaSalle University, and a PhD in Management Information Systems from Temple University. His research interests include information systems security, virtual teams, and human–computer interaction. His work has been published in journals such as Computers and Security, Risk Management and Insurance Review, and Human Resource Management.
