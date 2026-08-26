---
otero_id: 22284
otero_key: "4CH4EY5N"
title: "Inductive machine learning for instrument development"
authors: "Gholamreza Torkzadeh; Krzysztof J. Cios; Kurt A. Pflughoeft"
year: "1996"
journal: "Information & Management"
doi: "10.1016/s0378-7206(96)01061-0"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Research

# Inductive machine learning for instrument development

Gholamreza Torkzadeh $^{a,*}$ , Krzysztof J. Cios $^{b}$ , Kurt A. Pflughoeft $^{a}$

$^{a}$ Department of Information and Decision Sciences, The University of Texas at El Paso, 500 W. University Avenue,

El Paso, TX 79968-0544, U.S.A

$^{b}$ Department of Electrical Engineering, The University of Toledo, Toledo OH, USA

## Abstract

An inductive machine learning (ML) algorithm is used to discriminate between respondents and examine the dimensionality of an end-user computing satisfaction instrument. In all 616 responses were partitioned for training and testing purposes. Each respondent was required to assess his or her overall satisfaction level; this was used for classification of responses in two groups: satisfied and dissatisfied. Using 12 other survey items, the Cover Learning using Integer Linear Programming (CLILP2) algorithm correctly categorized 76% of the respondents. Recognition and discrepancy rates were used for instrument validation and in developing a shorter instrument.

Keywords: Instrument development; Machine learning; User satisfaction measurement

## 1. Introduction

MIS researchers have relied heavily on survey-based research in their quest to achieve theory formation. For this type of empirical research, instrument validation is an important component, as it can increase the power of the study, expedite future studies, and provide a basis for comparing results across studies. There is a need for reliable multiple-item instruments that can be administered with ease and confidence by both researchers and practitioners.

Three important features of an instrument are: internal consistency, dimensionality, and stability. These features are often measured by statistical methods. For example, internal consistency is measured by coefficient alpha [6, 9], dimensionality is determined by factor analysis and correlations between total scores and item scores [16], and stability is examined through test/retest procedures [12, 33]. The benefits of these and other statistics are clear but there are costs associated with their use.

Statistical techniques often have assumptions that relate to scale, sample distribution, and power of the test. Recent MIS studies have expressed caution about the use of statistical methods that do not address the above concerns $[31, 32, 34]$ . Furthermore, a survey of MIS articles employing inference testing suggests that their statistical power is substantially below accepted norms $[4]$ . Given the importance of these issues, exploring alternative, non-statistical means for accessing instruments is useful.

A machine learning (ML) method is proposed to help in determining the validity of an end-user satisfaction instrument. This method addresses the instrument's dimensionality as well as determining what items are useful for measuring a specific construct. The results of this method are compared with a previous end-user satisfaction study and they provide encouragement for the further development and application of this method.

## 2. The machine learning method

The machine learning algorithm, CLILP2, used in this study is fully described in $[7, 8]$ . This algorithm combines decision tree-based learning with rule-based learning $[13, 19, 20, 21, 22]$ . A decision rule, or a “cover”, is a statement specifying common features of some examples.

The method partitions the data by selecting a combination of features. The partition is analyzed to see how many positive examples are included and negative examples excluded $[1]$ . When a selected rule excludes all the negative examples, the positive examples that match the rule are separated in a subset. Next, a search is performed for a new rule to partition the remaining positive examples. The learning process ends when all positive examples are grouped into subsets.

There are many ways, however, to partition the set of positive examples into subsets, and this means that more than one rule can be used to create the same partition.

An important aspect of any learning algorithm is the effectiveness of the generated decision rules; this is checked by applying them to test cases $[24, 28]$ . In general, the more positive examples that are covered by a decision rule, the stronger the confidence in that decision rule $[17, 23]$ . Thus, generation of a small number of strong decision rules covering all positive examples is a desired property of an ML algorithm $[5, 35]$ . In order to find a partition with strong decision rules and to avoid exponential growth of the solution (number of rules), a heuristic-based linear programming method is used. This is briefly described.

Since several competing rules may exist for a single partition [11], the CLILP2 algorithm, as used here, employs several heuristics to detect the “best” rule. The most general rule uses the fewest features to distinguish between positive and negative examples, while a specific rule includes every common feature in the group of examples. A “perfect” general rule should recognize all positive examples and exclude all negative examples. The following measures are used to find the “best” rule. Each rule is ranked based on the summation of measures [7, 8].

$$
\text { sensitivity } = \frac {\text { number   of   recognized   positive   examples }}{\text { number   of   total   positive   examples   tested }}
$$

$$
\text { specificity } = \frac {\text { number   of   recognized   negative   examples }}{\text { number   of   total   negative   examples   tested }}
$$

predictive accuracy

$$
= \frac {\text {(number of recognized positive examples} + \text {number of recognized negative examples)}}{\text {(number of total positive examples} + \text {number of total negative examples)}}
$$

The rules are generated via an integer linear programming model; a description of this method, using an example, is provided in Appendix A. The algorithm can also incorporate prior information to generate rules; e.g., the user knows some features are more important than others.

## 3. An application

The CLILP2 algorithm was applied to a data set that was gathered for the development of an end-user (EU) computing satisfaction instrument. The rapid growth of EU computing has made instrument development an important and useful research activity [29]. Perceived user satisfaction is chosen, as it is frequently studied in assessing information systems performance [2, 3, 15, 30].

The instrument measured the user's perception of five satisfaction factors: Content, Accuracy, Format, Ease of Use, and Timeliness for micro-, mini-, and mainframe applications. Eighteen questions were originally used for factor measurement but six items were later deleted. Table 1 lists the proposed 12-item instrument, which incorporated a 5-point Lickert scale where $1 =$ almost never; $2 =$ some of the time;... and $5 =$ almost always. A separate criterion question was used to measure the user's overall level of satisfaction directly; it was worded as follows: "Overall, how would you rate your satisfaction with this application?" A 5-point Lickert scale was also applied, where $1 =$ non-existent; $2 =$ poor; $3 =$ fair;

Table 1
Measures of end-user computing satisfaction

<table><tr><td>C1.</td><td>Does the system provide the precise information you need?</td></tr><tr><td>C2.</td><td>Does the information content meet your needs?</td></tr><tr><td>C3.</td><td>Does the system provide reports that seem to be just about exactly what you need?</td></tr><tr><td>C4.</td><td>Does the system provide sufficient information?</td></tr><tr><td>A1.</td><td>Is the system accurate?</td></tr><tr><td>A2.</td><td>Are you satisfied with the accuracy of the system?</td></tr><tr><td>F1.</td><td>Do you think the output is presented in a useful format?</td></tr><tr><td>F2.</td><td>Is the information clear?</td></tr><tr><td>E1.</td><td>Is the system user friendly?</td></tr><tr><td>E2.</td><td>Is the system easy to use?</td></tr><tr><td>T1.</td><td>Do you get the information you need in time?</td></tr><tr><td>T2.</td><td>Does the system provide up-to-date information?</td></tr></table>

4= good; and 5= excellent. For additional information concerning the instrument and the factor structure, see Doll and Torkzadeh [10].

The original study collected 618 cases, of which $25\%$ related to microcomputer applications and $75\%$ to mini/mainframe applications. The researchers reported that the 12 item instrument's reliability, as measured by Cronbach's alpha, was 0.92 and that each item had a corrected-item total correlation (a measure of internal consistency) above 0.63. All factors had a correlation of 0.55 or higher with the criterion question. The authors concluded that this instrument represented substantial progress in measuring EU satisfaction but they recommended that future research efforts should be made to validate the instrument.

The CLILP2 algorithm is applied to the same data set as an alternative, non-statistical method for instrument validation. This algorithm requires that the responses to the criterion question are compressed to a binary scale. Users who responded with a 2 (poor) or 3 (fair) were categorized as “dissatisfied” while those who marked 4 (good) or 5 (excellent) are considered “satisfied.” Two respondents rated their satisfaction as non-existent (1) and were omitted, leaving 616 cases. One third of the responses represented dissatisfied users.

For machine learning purposes, 70% of the cases were used for training while the remaining cases were used for testing. This breakdown is frequently used for evaluating machine learning algorithms [18, 26]. The rules that are learned can be applied to the five factors to predict satisfied versus dissatisfied users.

Additionally, these rules can be used to identify overlapping cases which are useful in determining the instrument's dimensionality (number of factors) and proposing shorter instruments.

Overlapping occurs when responses to the factor questions are inconsistent with the criterion question. For example, an individual answers some factor questions in a negative (dissatisfied) fashion but still records a positive (satisfied) response to the criterion question. This pattern of responses may indicate that a particular factor is not useful for measuring satisfaction. Thus, the number of overlapping cases has an inverse relationship with the instrument's dimensionality.

Overlapping cases can also be used as a basis for proposing shorter instruments. Although more questions provide more information, some questions might be eliminated without substantially increasing the number of overlapping cases or, possibly, reducing the accuracy of prediction. Examining all subsets from the original 18 questions is impractical due to the sheer number of combinations. However, complete enumeration may be needed only in situations where the user has no idea what questions or factors are relevant. Using the five factors proposed by Doll and Torkzadeh, an instrument is proposed that contains one question per factor. A total of 480 combinations was examined, as the original survey contained the following number of questions for each factor: Content (5), Accuracy (4), Format (4), Ease of Use (3) and Timeliness (2).

## 4. Results

Rules learned by the CLILP2 algorithm correctly recognized 89% of the respondents in the satisfied class and 62% in the dissatisfied class. The unweighted, average recognition rate was 75.5% for the 12 item instrument. The unweighted average is a conservative figure, as there are more satisfied respondents. Only one overlapping case was noted, suggesting that each factor is useful in determining the user's overall satisfaction.

The data were further divided to see if the rules performed differently for applications that reside on microcomputers versus mainframes. Using rules based on microcomputer applications, the system recognized 70% of satisfied users. The sample size for the negative class was too small to generate reliable results. Using rules based on the mainframe applications, the system recognized 89% of the positive and 76% of the negative classes, yielding an average recognition rate of 82.5%.

The two sets of rules generated from data for the microcomputer and mainframe applications were applied to the entire test data set. Using microcomputer application rules, the system recognized 84% of the positive class. Again, the sample size for the negative class was too small to generate reliable results. Using mainframe application rules, the system recognized 88% of the positive and 71% of the negative classes, yielding an average recognition rate of 79.5%. There is little evidence to suggest that the instrument is dependent on the platform upon which the application resides.

## 4.1. An alternative instrument

To identify the best combination of items (one per factor) that provide the highest recognition rates and the lowest overlap, the researchers conducted experiments for all possible five-item combinations from the pool of 18 questions. Rules generated from each combination were used to measure the number of overlapping cases and recognition rates for each instrument.

The 5 item instrument that contained the fewest overlapping cases with the highest recognition rate is presented in Table 2. There were 15 overlapping cases and the average recognition rate was 86.5%. The questions included four items from Table 1 (C3, A2, E1, T2) and one item (F4) from the original 18-item list. This last item is a format item, “Is the output easy to understand?”

## 5. Summary and discussion

The results of CLILP2 algorithm do not appear to contradict the results reported in the original instrument development study. Only one overlapping case in the test data set and a high recognition rate was detected, indicating that all factors are useful in determining satisfaction.

Table 2  
An alternative measure of end-user computing satisfaction

<table><tr><td>Instruction:</td><td>Please circle the response below which best describes your satisfaction with this application.</td></tr><tr><td>Scale:</td><td>(1) Almost never(2) Some of the time(3) About half of the time(4) Most of the time(5) Almost always</td></tr><tr><td>Measures:</td><td>1. Does the system provide reports that seem to be just about exactly what you need?2. Are you satisfied with the accuracy of the system?3. Is the system user friendly?4. Does the system provide up-to-date information?5. Is the output easy to understand?</td></tr></table>

Additional data analysis also suggested that there is no appreciable difference in satisfaction measures for microcomputers and mainframes. The consistency of results across platforms suggests that pooling the mainframe and microcomputer data is appropriate. The results may also show that users are applying the same standards in evaluating applications, irrespective of the environment.

The CLILP2 algorithm was also useful for proposing shorter instruments. Out of the original 18 questions, the algorithm created a 5 item instrument with a higher average recognition (86.5%) than using the 12 item survey (75.5%). The shorter instrument had more overlapping cases, but 15 overlapping cases in several hundred are still considered quite small.

The shorter instrument contained all but one question listed in the 12 item survey. Additional analysis is needed to determine whether this question should be used instead of the two format questions suggested in the original study. It is possible that in some situations the one question addressing the ease of understanding the output would also encompass the output's usefulness and clarity.

Although the CLILP2 algorithm is an alternative method for instrument validations, it is not without limitations. This algorithm requires a criterion question whose results are recorded on a binary scale. Users may feel that they cannot adequately express their level of satisfaction using such a scale. Would users who feel that their overall level of satisfaction is fair, record dissatisfied on a binary scale? This is difficult to determine and the survey assumed that all such users would do so. Also, if the criterion question does not capture all possible dimensions of a construct, it will be difficult to use it as a criterion for determining overlapping cases.

The CLILP2 algorithm requires a large sample for training and testing purposes. Each of the partitioned data sets should also contain a sufficient number of responses including adequate levels of positive and negative responses. These requirements may make our method impractical for some studies, especially those that are pilot in nature.

Several subjective decisions must be made by the researcher to recommend a specific set of rules and analyze results. First, there are no accepted levels that allow a decision to be made on overlapping cases being considered relevant to a concept. Second, it is not obvious whether models that produce higher recognition rates are always preferable, if they produce overlapping cases.

The set of learned decision rules may be suboptimal, as only positive examples are examined and an heuristic method is used for evaluation. Algorithms that examine negative and positive examples may help in discovering better rules. Even if the CLILP2 algorithm has found the optimal set of rules, the heuristics may not rank the rules accordingly.

## 6. Conclusion

Researchers and practitioners need reliable and easy-to-use instruments. These require careful design and rigorous validation. We used a non-statistical method, based on an inductive machine learning algorithm, to test an instrument and develop a short multiple item user satisfaction scale. This captures multiple dimensions of the satisfaction phenomenon. While the algorithm demands a larger sample size than traditional statistical tests, it offers flexibility by generating single-item constructs.

## Acknowledgements

The authors would like to thank William J. Doll of The University of Toledo for his valuable comments and cooperation.

## Appendix A

The learning examples are usually represented as vectors [14], where each component of a vector corresponds to a certain feature. Thus, a set of learning examples can be stored in two matrices, one representing positive (POS) examples and the other negative (NEG) examples.

Examples stored in matrices POS and NEG are row vectors with their components/features being either binary or multiple-valued. Two types of multiple values are distinguished. Type one: values that a feature takes on are specific numbers, say 5 and 12. Type two: values that a feature are restricted from taking, specific numbers, say 3, 5 and 6. Typical format of a decision rule using both types follows:

$$
\begin{array}{r l} \text { RULE } (X) & = [ V (1) = 5 ] \text { and } [ V (3) <   > 3, 5, 5 ] \\ & \text { and } [ V (6) = 1 2 ] \end{array}
$$

Let us consider a problem in which four positive and five negative learning examples are given. For simplicity, all features are assumed to be binary.

$$
\mathrm{POS} = \begin{array}{c c c c c c c c c c} | & \mathrm{V1} & = | & 1 & 0 & 1 & 1 & 0 & 1 & 1 \\ | & \mathrm{V2} & = | & 0 & 1 & 0 & 0 & 0 & 1 & 1 \\ | & \mathrm{V3} & = | & 0 & 0 & 1 & 0 & 1 & 0 & 1 \\ | & \mathrm{V4} & = | & 1 & 0 & 0 & 1 & 0 & 0 & 1 \end{array} \quad | \quad \mathrm{N} ^ {*} \mathrm{D}
$$

$$
\mathrm{NEG} = \begin{array}{c c c c c c c c c c} | & \mathrm{U1} | & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\ | & \mathrm{U2} | & 0 & 1 & 1 & 0 & 1 & 1 & 1 \\ | & \mathrm{U3} | = & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\ | & \mathrm{U4} | & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\ | & \mathrm{U5} | & 0 & 0 & 1 & 1 & 1 & 0 & 0 \end{array} \mid \mathbf {M} ^ {*} \mathbf {D}
$$

A description of the CL/ILP algorithm follows:

1. Part I: Partition matrix POS into subsets.

First, select a positive example as a prototype of a cover and compare it with all negative examples. Common features between positive and negative examples are eliminated. The cover of a subset is generated by selecting noncommon features so that a group of positive examples sharing those features can be distinguished from all negative examples. The result of comparing a positive example with all negative examples is stored in a matrix called TEMPLATE.

For the above example, the TEMPLATE matrix C(V1), corresponding to the first positive example, is generated as:

$$
\mathrm{C} (\mathrm{V} 1) = \begin{array}{c c c c c c c c c} & X & X & 1 & 1 & X & 1 & 1 \\ & 1 & 0 & X & 1 & 0 & X & X \\ & X & X & 1 & 1 & 0 & 1 & 1 \\ & 1 & X & X & X & 0 & X & X \\ & 1 & X & X & X & 0 & 1 & 1 \end{array} \quad \mathrm{M} ^ {*} \mathrm{D}
$$

Second, choose another positive example in order to update the TEMPLATE matrix. Now, instead of comparing with all negative examples, the newly selected positive example is compared with the TEMPLATE matrix. When comparing with each row, the eliminated features and the noncommon features are ignored, but the common features are further processed. For the second positive example the matrix is updated to:

$$
\mathrm{C} (\mathrm{V} 2) = \left| \begin{array}{c c c c c c c} X & X & X & X & X & 1 & 1 \\ X & X & X & X & 0 & X & X \\ X & X & X & X & 0 & 1 & 1 \\ X & X & X & X & 0 & X & X \\ X & X & X & X & 0 & 1 & 1 \end{array} \right| \mathbf {M} ^ {*} \mathbf {D}
$$

All positive examples will be used in updating the TEMPLATE matrix. The positive examples that have been actually used to update the TEMPLATE matrix constitute a subset, and are deleted from matrix POS. From the TEMPLATE matrix, the rule specifying "significant" features for the subset is generated by a cover learning algorithm which, basically, is a 0-1 integer linear programming based algorithm, and will be described later.

Third, select the next positive example from matrix POS to build a new TEMPLATE matrix, i.e. repeat the above procedure until all positive examples are classified in subsets. The final generated covers are $R1 = (X, X, X, X, 0, X, 1)$ and $R2 = (X, X, X, X, X, 0, 1)$ , where $X$ stands for "don't care" features. These covers can be written in a simpler form: $R1 = (\text{feature } 5 = 0 \text{ and feature } 7 = 1)$ , and $R2 = (\text{feature } 6 = 0 \text{ and feature } 7 = 1)$ .

In Part 1, the partition of the matrix POS is formed by generating one subset after another. The algorithm includes as many positive learning examples in a subset as possible. After all positive examples are classified in subsets, the next step is to find the minimum number of subsets which constitute a partition.

## 2. Part 2: Minimize the number of subsets.

All examples that can be recognized by the cover of the most recent subset are reclassified as belonging to that subset. The cover of the next-to-most-recent subset will then include as many positive examples as possible, and so forth. If any subset becomes empty, it is redundant and, therefore, is deleted. For the above example the resulting partition is sub-optimal.

## 3. Part 3: Cover learning

From the final template matrix, decision rules are formed to cover all examples in the corresponding subset. The decision rules are formed in such a way that none of the features used in the rule are satisfied at the same time by negative examples. The simplest way to form a rule is to add all not eliminated features in the TEMPLATE matrix. However, some redundant features may make the rule too specific. The most general rule is formed only by the significant features.

To continue with our example, let us take a look at the resultant template matrix:

$$
\left| \begin{array}{c c c c c c c} 0 & X & 1 & X & 1 & X & 1 \\ X & 0 & X & X & X & 0 & X \\ 0 & X & 1 & X & X & X & 1 \\ X & X & X & X & X & 0 & X \\ X & X & X & 0 & X & X & 1 \end{array} \right| \mathbf {M} ^ {*} \mathbf {D}
$$

If a decision rule is chosen by taking every feature (one value from each column), for instance, R = (0010101), then such a decision rule is too specific to cover any example other than V = (0010101). If the rule is formed by selecting, for example, R = (<), then all negative examples (see the beginning) are excluded, because none has features six and seven equal to 0 and 1, respectively. If the decision rule is formed by selecting R = (<), the fifth negative example is not excluded. In the above template matrix, there is no single feature which could be used to discriminate between all negative examples so the rule with two features is the most general one.

In order to find the most general decision rule from a template matrix, we use an integer linear programming (ILP) model $[25, 27]$ . To do so, the template matrix is first transformed into another matrix, called a coefficient matrix. From the coefficient matrix, the minimum number of features is obtained to form a decision rule. The dimension of the coefficient matrix is the same as the dimension of the template matrix. An example of transforming the above template matrix in a coefficient matrix is shown below. If an element in a template matrix has the symbol 'X' the element in the corresponding position of the coefficient matrix takes a value of 0, otherwise it takes a value of 1.

$$
\left| \begin{array}{c c c c c c c} 0 & X & 1 & X & 1 & X & 1 \\ X & 0 & X & X & X & 0 & X \\ X & X & X & X & X & 0 & X \\ X & X & X & 0 & X & X & 1 \end{array} \right| \mathbf {M} ^ {*} \mathbf {D}
$$

$$
\rightarrow \left|\begin{array}{c c c c c c c}1&0&1&0&1&0&1\\0&1&0&0&0&1&0\\0&0&0&0&0&1&0\\0&0&0&1&0&0&1\end{array}\right| \mathbf {M} ^ {*} \mathbf {D}
$$

Denoting the generic element of the coefficient matrix as $a_{ij}, i = 1, \ldots, M, j = 1, \ldots, D$ , the task of finding the most general rule is stated as:

$$
\text { Minimize } \sum_ {j = 1} ^ {D} X _ {j}
$$

subject to the constraints:

$$
\sum_ {j = i} ^ {D} a _ {i j} X _ {j} \geq 1 (i = 1, \dots , M)   a _ {i j} = 0, 1, \text { where } X _ {j} = 0, 1
$$

For the above template matrix, this ILP model is defined as:

$$
\text { Min } Z = X _ {1} + X _ {2} + X _ {3} + X _ {4} + X _ {5} + X _ {6} + X _ {7}
$$

subject to:

$$
\begin{array}{c c c c c c c c} X _ {1} & & + X _ {3} & & + X _ {5} & & + X _ {7} & \geq 1 \\ & X _ {2} & & & & + X _ {6} & & \geq 1 \\ X _ {1} & & + X _ {3} & & & & + X _ {7} & \geq 1 \\ & & & & + X _ {6} & & & \geq 1 \\ & & & X _ {4} & & & + X _ {7} & \geq 1 \end{array}
$$

$$
\mathrm{X} _ {\mathrm{j}} = 0, 1 (j = 1, 2, \dots , 7)
$$

Due to the specific character of the transformed ILP problem, every parameter in the equations is either 1 or 0 and all constraints are in ‘greater or equal’ form. The solution for the example is $X_{6}=1$ and $X_{7}=1$ , indicating that features six and seven are selected to form the rule. Thus the general rule is R = (XXXXX01).

## References

[1] Angluin, D., Learning regular sets from queries and counterexamples. Technical Report, YALEU/DCS/TR-464, Yale University, 1986.

[2] Bailey, J.E. and Pearson, S.W., “Development of a tool for measuring and analyzing computer user satisfaction”, Management Science, 29(5), 1983, 530–545.

[3] Baroudi, J.J., Olson, M.H. and Ives, B., "An empirical study of the impact of user involvement on system usage and information satisfaction", Communications of the ACM, 29(3), 1986, 232–238.

[4] Baroudi, J.J. and Orlikowski, W.J., “The problem of statistical power in MIS research”, MIS Quarterly, 13(1), 1989, 87–106.

[5] Botta, M., “Constructive learning conjunctive concept characterization”, Proceedings of the Third International Symposium on Methodologies for Intelligent Systems, Turin, Italy, 1988.

[6] Carmines, E.G. and Zeller, R.A., Reliability and Validity Assessment, Sage University Paper 17, Sage Publications, Beverly Hills, 1979.

[7] Cios, K.J. and Liu, N., "An algorithm which learns multiple covers via interger linear programming, Part I – The CLILP2 Algorithm", KYBERNETES, MCB University Press, U.K., 1995, Vol. 24, No. 2, pp. 29–50.

[8] Cios, K.J. and Liu, N., "An algorithm which learn multiple covers via integer linear programming, Part II - Experimental Results and Conclusions", KYBERNETES, MCB University Press, U.K., 1995, Vol. 24, No. 3, pp. 28-40.

[9] Cronbach, L.J., “Coefficient alpha and the internal structure of tests”, Psychometrika, 16, 1951, 297–334.

[10] Doll, W.J. and Torkzadeh, G., "The measurement of end-user computing satisfaction", MIS Quarterly, 12(2), 1988, 258–274.

[11] Duda, R.O. and Hart, P.E., Pattern classification and scene analysis, Wiley, 1973.

[12] Galletta, D.F. and Lederer, A.L., “Some cautions on the measurement of user information satisfaction”, Decision Sciences, 20(3), 1989, 419–438.

[13] Horowitz, E. and Sahni, S., Fundamentals of Data Structures in PASCAL, Computer Science Press, 1984.

[14] Hoff, B., Michalski, R.S. and Step, R.E., INDUCE.2: A program for learning structural descriptions from examples, Report ISG 83-4 UIUCDCS-F-83-904, Dept. of Computer Science, University of Illinois, Urbana, 1983.

[15] Ives, B., Olson, M.H. and Baroudi, J.J., “The measurement of user information satisfaction”, Communications of the ACM, 26(10), 1983, 785–793.

[16] Kerlinger, F.N., Foundations of Behavioral Research, McGraw-Hill, New York, 1978.

[17] Kodratoff, K., Introduction to Machine Learning, Morgan Kaufmann, 1988.

[18] Lewis, P.M., “The characteristic selection problem in recognition systems”, IRE Transactions on Information Theory IT-8(2) 1987, pp. 171–178.

[19] Mehler, G., Bentrup, J. and Riedesel, J., INDUCE.4: A Program for Incrementally Learning Structural Description from Examples, Working paper, Department of Computer Science, University of Illinois, Urbana, 1986.

[20] Michalski, R.S., Mozetic, I., Hong, I. and Lavrac, N., “The multi-purpose incremental learning system AQ15 and its testing application to three medical domains”, Proceedings of the Fifth National Conference on Artificial Intelligence, AAAI-86, 1986.

[21] Michalski, R.S., Mozetic, I., Hong, I. and Lavrac, N., The AQ15 inductive learning system: An overview and experiments, Technical Report No. ISG-86-20, Department of Computer Science, University of Illinois at Urbana-Champaign, Urbana, 1986.

[22] Michalski, R.S., “A Theory and Methodology of Inductive Learning”, Artificial Intelligence, 20, 1983, 111–161.

[23] Mitchell, T., “Generalization as search”, Artificial Intelligence, 18(2), 1982, 203–226.

[24] Mooney, R.J. and Bennett, S., “A domain independent explanation-based generalizer, I”, Proceedings of the Fifth National Conference on Artificial Intelligence, Morgan Kaufmann, 1987.

[25] Ning, L. and Cios, K.J., “Knowledge-based intelligent tutoring systems”, Proceedings of the Second International Conference on Computer Assisted Learning, ICCAL'89, Springer-Verlag, 1989.

[26] Quinlan, J.R., “Learning effective classification procedures and their application to chess ending games”, in Michalski, Carbonell, Mitchell (eds.), Machine Learning: An Artificial Intelligence Approach, Morgan Kaufmann, 1986.

[27] Ravindran, A., Phillips, D.T. and Solberg, J.J., Operations Research Principles and Practice, Wiley, 1987.

[28] Rajamoney, S. and DeJong, G., “The classification, detection and handling of imperfect theory problems”, Proceedings of the International Joint Conference on Artificial Intelligence, IJCAI-87, Milano, Italy, 1987.

[29] Rivard, S. and Huff, S.L., “Factors of success for end user computing”, Communications of the ACM, 31(5), 1988, 552–561.

[30] Rushinek, A. and Rushinek, S.F., “What makes users happy?”, Communications of the ACM, 29(7), 1986, 594–598.

[31] Straub, D.W., "Validating instruments in MIS research", MIS Quarterly, 13(2), 1989, 147-165.

[32] Subramanian, A. and Nilakanta, S., "Measurement: A blueprint for theory-building in MIS", Information and Management, 26, 1994, 13–20.

[33] Torkzadeh, G. and Doll, W.J., “Test-retest reliability of the end-user computing satisfaction instrument”, Decision Sciences, 22(1), 1991, 26–37.

[34] Treacy, M.E., “An empirical examination of a causal model of user information satisfaction”, Center for Information Systems Research, Sloan School of Management, IT, April, 1985.

[35] Weiss, S.M., Galen, R.R. and Tadepalli, P.V., “Optimizing the predictive value of diagnostic decision rules”, in Proceedings of the Sixth National Conference on Artificial Intelligence, AAAI-87, 1987, Vol. 2.

![](/api/attachments/4CH4EY5N/fulltext/images/58dcdf1eacf545ecf92d29231a6c24122dbb77666aead3eb1f5adaafa3fdb0ea.jpg)

G. Torkzadeh is Professor and Chair of Information and Decision Sciences Department at The University of Texas in El Paso. He holds a Ph.D. in Operations Research from Lancaster University, England and is a member of The Institute

of Operations Research and Management Sciences, Association for Computing Machinery, Association for Information Systems, Decision Sciences Institute, and Society for Information Management. He has been involved in research programs pertaining to management of the information systems function, distribution, resource allocation, and mathematical modeling and has published in Management Science, Communications of the ACM, MIS Quarterly, Decision Sciences, Omega, Information and Management, Journal of Operational Research, Journal of Knowledge Engineering, Long Range Planning, Journal of MIS, and others.

![](/api/attachments/4CH4EY5N/fulltext/images/ad0592b9d54787646edf27903a7d63bd60ba5eed6ad9a7b8c74066415bdc30dd.jpg)

K.J. Cios is an associate professor of Electrical Engineering and Computer Science at The University of Toledo, Toledo, Ohio, U.S.A. His research interests are in the area of neuro-fuzzy systems, machine learning, and pattern recognition. His research was funded, among others, by the National Science Foundation, NASA, and the

American Heart Association. He has published extensively in journals and in conference proceedings. Dr. Cios consults for several U.S. companies. He is a senior member of the IEEE and a member of Sigma Xi. He is on editorial boards of NEUROCOMPUTING and the Handbook of Neural Computation.

![](/api/attachments/4CH4EY5N/fulltext/images/40a301701a2c2c526b941c6b366dfe2e50160b052022fd78c8095ca8813d8c99.jpg)

K. Pflughoeft is an assistant professor in the Information and Decision Sciences Department at the University of Texas in El Paso. He has a Ph.D. in Management Science from the University of Wisconsin - Milwaukee. His research programs pertain to knowledge-based systems, simulation,

information theory, user training, and manufacturing scheduling. He has published in the Journal of Manufacturing Systems, International Journal of Production Research, and Statistics and Probability Letters. He is a member of the Decision Sciences Institute.
