---
otero_id: 20162
otero_key: "K9B9KVDG"
title: "A group decision support approach to evaluating journals"
authors: "Efraim Turban; Duanning Zhou; Jian Ma"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.12.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A group decision support approach to evaluating journals

Efraim Turban<sup>a</sup>, Duanning Zhou<sup>b</sup>, Jian Ma<sup>a,\*</sup>

<sup>a</sup>Information Systems Department, City University of Hong Kong, Kowloon Tong, Hong Kong, China <sup>b</sup>Accounting & Information Systems Department, Eastern Washington University, Spokane, USA

Received 1 November 2001; received in revised form 3 July 2003; accepted 21 December 2003

Available online 1 April 2004

## Abstract

One of the most important decisions made in academic institutions, research organizations, and government agencies is the grading or ranking of journals for their academic values. Current methods for evaluating journals use either a subjective (e.g., experts’ judgments on journals) or objective approach (e.g., impact factors of journals), or an informal mix of the two. This paper presents a formal procedure that integrates objective and subjective judgments to provide a comprehensive method. The procedure is based on a fuzzy set approach that deals with the imprecise and missing information inherent in the evaluation process. The system was tested in Hong Kong in an assessment of faculty research productivity. Similar assessments exist in the UK, Singapore, and other countries. The proposed model can also be used for similar decisions that involve subjective and objective information.

<sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Group decision making; Distributed (virtual) GDSS; DSS; Fuzzy set; Journal evaluation; Subjective evaluation; Objective evaluation

## 1. Introduction

In a university setting, evaluating the quality of academic journals is required for several personnel decisions, such as recruiting, promotion, tenure, and retention. Such evaluation is also performed for merit increases and for allocation of research funding. Many institutions use formal grading or point systems for such evaluations. In many cases, the grading decision is made by a group (a committee or panel) which complicates the decision process, since a consensus is attempted. For years, researchers in several disciplines have attempted to find appropriate approaches for such evaluations. Unfortunately, there is no consensus on how best to conduct the evaluation. The methodologies proposed here (see Table 1) can be classified as either subjective or objective, depending on how the decision information is obtained and used.

The objective approaches are usually based on some form of citation counts over a certain time period. For example, Holsapple et al. [11] employed a citation analysis methodology to rank information systems research journals. This is publicly available in a form of ‘‘total cites’’, ‘‘immediacy index’’, ‘‘total articles’’, ‘‘cited half-life’’ and ‘‘impact factor’’. Citation information is published periodically in sources such as the Journal Citation Reports, a CD-ROM database available in many libraries.

The subjective approach, also called perception analysis approach, solicits information from experts such as academic staff, deans, or department heads (see [23]). The collected information is compiled and the average is used to rank the journals. Thus, the final ranking of the journals reflects the opinions of the group members.

Table 1  
Summarization of studies on journal ranking

<table><tr><td>Year</td><td>Authors</td><td>Field</td><td>Methodology</td></tr><tr><td>1984 [16]</td><td>Liebowitz and Palmer</td><td>Economics</td><td>Citation analysis</td></tr><tr><td>1990 [6]</td><td>Extejt and Smith</td><td>Behavioral sciences and management</td><td>Citation analysis</td></tr><tr><td>1991 [9]</td><td>Gillenson and Stutz</td><td>MIS</td><td>Questionnaire survey (judgment)</td></tr><tr><td>1991 [1]</td><td>Beattie and Ryan</td><td>Accounting and finance</td><td>Citation analysis</td></tr><tr><td>1993 [10]</td><td>Holsapple, Johnson and Tanner</td><td>MIS</td><td>Citation analysis</td></tr><tr><td>1994 [11]</td><td>Holsapple, Johnson, Manakyan and Tanner</td><td>MIS</td><td>Citation analysis</td></tr><tr><td>1995 [22]</td><td>Walstrom, Hardgrave and Wilson</td><td>MIS</td><td>Questionnaire survey (judgment)</td></tr><tr><td>1996 [4]</td><td>Diaz, Black and Rabianski</td><td>Real estate</td><td>Questionnaire survey (judgment)</td></tr><tr><td>1997 [24]</td><td>Wing</td><td>Construction management</td><td>Questionnaire survey (judgment)</td></tr><tr><td>1999 [2]</td><td>Cheng, Kumar, Motwani, Reisman and Madam</td><td>Technology innovation management</td><td>Citation analysis</td></tr><tr><td>1999 [20]</td><td>Soteriou, Hadjinicola and Patsia</td><td>Management</td><td>Questionnaire survey (judgment)</td></tr><tr><td>2001 [8]</td><td>Forgionne and Kohli</td><td>MIS</td><td>Multivariable (objective) and judgment</td></tr><tr><td>2001 [23]</td><td>Walstrom and Hardgrave</td><td>MIS</td><td>Questionnaire survey (judgment)</td></tr></table>

However, evaluations and rankings of journals determined by subjective approaches can be influenced by biases [7] or by lack of sufficient knowledge or experience by some group members. Therefore, it is likely that neither the subjective, nor the objective approaches are the best method of evaluation. Thus, it makes sense to combine the two. However, despite considerable research conducted on evaluation, there is almost no research on how to integrate the two approaches. One exception is Forgionne and Kohli [8] who suggested measuring the quality of journals by 24 objective variables, giving subjective weights for each using the AHP software. Their methodology may not, however, be applicable to situations like ours due to the complexity of the model. In addition, there is very little work on two related issues: how to deal with incomplete subjective or objective information and how to transform the evaluations into a tangible journal grade.

Our paper attempts to fill this gap by proposing a group decision support system (GDSS) that deals with these research issues. The system is based on a methodology developed to fit the process of funding research in Hong Kong; however, it can be easily modi fied to cover other situations. The Hong Kong process involves a combination of subjective information solicited from experts who are organized in disciplinary panels and objective information in the form of an impact factor. A journal’s impact factor for a specific year is defined as ‘‘the number of citations to articles published in this journal in the previous 2-year period divided by the total number of articles published in this journal in the previous 2-year period’’ [26].

## 2. The proposed decision support process

Due to incomplete and uncertain objective information (e.g., citation information may not be available for some journals), as well as lack of sufficient knowledge, experts may find it difficult to express their preferences precisely. Fuzzy set theory [25], which is widely used in decision making (e.g., [14,15,17]), is used here as a tool for solving the problem of imprecise subjective judgments and incomplete objective information.

The proposed decision support process is composed of the following nine steps.

## 2.1. Step 1: computing the relationship between historical impact factors and grades

Since journal evaluation is a repetitive process, we can find the grade (or points) assigned to a journal in the previous evaluation, and the impact factor of the journal at that time. Using the concepts of membership degree and membership function in fuzzy set theory (see Appendix A), our methodology expresses these relationships for a set of journals in each discipline, such as information technology or marketing. A typical computed membership function for three grades, A–C is shown in Fig. 1. The mathematical basis for the computation is provided in Appendix A.

![](/api/attachments/K9B9KVDG/fulltext/images/e74997185b82b5097c7801cd715af19dc17f7c184c5092d2f5f0f1d769a618ef.jpg)  
Fig. 1. The relationship functions of grades A–C for information systems journals.

## 2.2. Step 2: determining the membership degrees of an individual journal

Once the membership functions are established, we can compute the membership degrees of each journal given that its current impact factor is known. For example, a grade of A is assured for a journal with an impact factor of 1.6 or more (see arrow #1 in Fig. 1). For an impact factor of 0.9, the membership degrees are 0.2 for point A and 0.8 for point B (see arrow #2). These results expressed as a vector h0.2, 0.8, 0i are the membership degrees for the specific journal. Note that these represent likelihood, but not, as the case with probabilities, with a sum of 1. The detailed mathematics is shown in Appendix A.

## 2.3. Step 3: expressing the experts’ subjective judgments

Instead of requiring each expert to assign a grade to a journal, we allow him/her to provide likelihood values (membership degreesin fuzzy set terminology). For example, if an expert believes that a journal’s value is ‘‘somewhat less than an A’’, she/he can express this belief in one of the two choices:

 Enter numerical values: Some experts may feel comfortable in using a quantitative vector such as h0.9, 0.3, 0, 0i to express the ‘‘somewhat less than $\mathbf { A } ^ { \prime \prime }$ . If an expert is certain that a journal belongs to a specific grade, e.g., B, then h0, 1, 0, 0i is used.

 Or enter a qualitative statement: For those experts who are not comfortable with the numerical opinion expression, we allow a choice from a list of predefined statements or judgment terms. Typical judgment terms can be: ‘‘somewhat less than an A’’, ‘‘better than B’’ etc.

## 2.4. Step 4: assigning weights

Weights must next be assigned to express the evaluators’ policy regarding the importance of the objective versus the subjective evaluation components. The procedure is:

 The weights can be assigned by the organization conducting the evaluation, by the group leader, and/ or jointly by the panel experts.

 A total weight of 1 is divided between the impact factor (objective information) and the judgmental information.

 The weight of the judgmental information can be assigned to each expert individually or to the panel as a whole (and then each part to the experts).

 Different weights may be assigned for each journal.

At this time, we have all the input information necessary for the analysis.

## 2.5. Step 5: consolidating the experts’ judgments

In order to consolidate the experts’ opinions, it is necessary first to convert the qualitative statements in step 3 into quantitative values. The conversion table is known to the experts, who can change it if they so wish. This approach is similar to the one used by Saaty [19] in Expert Choice, which is an implementation of the AHP methodology.

For a group of experts, we aggregate all these vectors into a matrix: the subjective evaluation matrix (see Appendix A).

In current approaches, once the subjective information is aggregated, it can be shown to all the experts and a consensus attempted. However, if more information can be provided, the consensus reaching step (step 8) can be accomplished quickly, resulting in a more accurate decision. A well known disfunction of a group process is the tendency to compromise for a less than the best possible solution. In our methodology, there is almost no elapsed time between steps 5 and 8, and there is no need for face-to-face contacts. The execution of steps 5–7 takes only a few minutes. Therefore, it may be advantageous to attempt a consensus only at step 8, after more information is available.

## 2.6. Step 6: combining the objective and subjective information

Here, we add the objective information to the subjective evaluation matrix. The result is the overall evaluation matrix.

Next, we consider the availability of information. For some journals, no impact factor is available. Also, one or more experts may abstain from providing information. In such cases, fuzzy set-based mathematical adjustments are used to solve the problems of incomplete preference information.

## 2.7. Step 7: adjusting the weights

The impact of the weights can now be added to the evaluation matrix by a composition matrix operation. The result is called an evaluation vector, see Appendix A.

## 2.8. Step 8: reaching consensus

The result of step 7 for each journal is a grade vector which may look like h0.68, 0.36, 0, 0i. From this, the experts may infer that the grade of the journal is most likely to be A. Here, deliberations can take place, either in a face-to-face mode or electronically. If strong disagreement arises, a sensitivity analysis and/or consensus reaching session can be invoked.

## 2.9. Step 9: sensitivity analysis and reaching a final decision

To help the consensus reaching process and conflict resolution, a sensitivity analysis m2odule is added. In this, experts can change their subjective evaluations and/or weights and then see the impact on the evaluation vector. If the values of the evaluation vector are not too sensitive to changes, it is likely that a vector such as h0.68, 0.36, 0, 0i will receive a quick ‘‘A’’ vote. However, if the analysis results in large variations of the evaluation values, the use of a method (such as the Delphi method) [3] or other consensus reaching approach is recommended.

## 3. The GDSS structure

Based on this assessment process, a GDSS was defined; it consists of the four major components shown in Fig. 2.

(a) The database: The database contains two types of objective data: historical and current. The historical data include the journal ranking that existed prior to the current evaluation. In Hong Kong, this will be 3 years old or less, while in other countries it may be 1–5 years old. In addition, the database includes the impact factors of the relevant journals at the time the most recent ranking was completed. The historical and current impact factors can be transferred to the database from a library’s CD ROM.

(b) The knowledge base: Several types of knowledge are entered into the knowledge base; e.g., academic journal surveys of the importance in certain areas, opinions of previous judges, rankings provided in other universities, or the opinions of current experts. In addition, the knowledge base includes information about converting qualitative terms to quantitative ones. Finally, assessing an organization’s priorities about the tradeoffs between subjective and objective information, expressed as ‘‘weights’’, are also retained.

![](/api/attachments/K9B9KVDG/fulltext/images/6a871aded4b287a4c16d99c5634399ca17b0478598f2b798fe9a84bbc4d569d3.jpg)  
Fig. 2. The components of the GDSS (the arrows indicate information flow).

(c) User interfaces: The user interface allows for communication among the users (panel members, panel leader, and researchers) and between the users, panel facilitator, and the GDSS. This must be a web-based interface with sufficient security mechanisms embedded so that parti cipants can be in different locations working asynchronously.

(d) The model base: The model base includes:

(A) Fuzzy logic-based relationship: The fuzzy logic-based relationship model expresses the relationship between historical impact factors and historical ranking provided by experts. This is computed only one time in each evaluation cycle for the set of journals in each discipline. The other models are used for computing the required decision support values for each journal.

(B) Impact factor converter: This converts the current impact factor of a journal to a fuzzy membership set, based on the fuzzy relationship function.

(C) Expert’s opinions converter and consolidator: This converts qualitative judgment terms, based on a conversion table stored in the knowledge base, into quantitative values. It is used each time an expert enters data or changes her/his opinion. The converted values of a group of experts are then consolidated by the model.

(D) Evaluation integrator: This integrates the output of models ‘‘B’’ (objective) and ‘‘C’’ (subjective).

(E) Weight adjustor: This adjusts the values generated by the evaluation integrator (‘‘D’’) to the weights provided in the knowledge base, resulting in a fuzzy evaluation matrix.

The model base will be expanded in future to include two other modules:

(F) Conflict resolution model: This may include new mechanisms, such as anonymous voting used to reach a consensus. Commercial software, such as GroupSystems V [12], may be used for this purpose.

(G) Sensitivity analysis: This would be added to provide an easy way for experts to change their votes and to see its impact on the results.

## 4. Application in Hong Kong

To enhance research activities in Hong Kong, the University Grant Committee (UGC), a central government funding agency, has conducted research assessment exercises (RAE) once every 3 years. Similar exercises are conducted in the UK (e.g., see [5]). For this exercise, local universities form cost centers according to disciplines suggested by the UGC. Academic staff members are then assigned to these centers. Each staff member submits up to five recently (i.e., in the past 3-year period) published or accepted journal articles for RAE assessment. The disciplinary panels review the journals and assign a grade to each: A for top tier; B for mid-tier; and C for lower-tier. When an academic staff member is assessed to have three ‘‘B’’ grades (or better) articles published in the assessment period, he/she is likely to become an active researcher (AR). In previous RAE exercises, an AR implied allocation of research funds to the cost center, without a need to submit any research proposals. The funding for an AR is equivalent at least to the researcher’s salary for the three forthcoming years. In Hong Kong, this can be about HK\$ 1,200,000 per person per year. Thus, universities in Hong Kong pay a great deal of attention to the RAE exercises. From the perspective of the universities, it is very important to estimate well in advance the likely grades of different journals. These estimations can be communicated to faculty so that they can identify journals in which to publish and which journals to include as the five ‘‘best’’ (if they have more than five). Our GDSS can be used by the universities to optimize the decision. The GDSS can also be used by the different panels to arrive at their decisions.

The proposed GDSS was tested in evaluating the grades of journals in the discipline of Science and Engineering. The detailed steps are:

## 4.1. Step 1: analysis of the relationship between the historical grades of journals and impact factors

A frequency analysis method was used to find the relationship between grades of journals and impact factors in the Science and Engineering discipline to which Information Systems belongs. A list of journals for 1996, including the impact factor and suggested grade, was used for this purpose. The set of grades of the journals was G ¼ ðA; B; C; 0Þ, and the impact factor set was found to be S ¼ ½0; 6:4	. Because the sample size (285) is not very large, we considered the interval ½x; x þ 0:2	 as the analysis unit. The results of frequency distribution for every element of G are shown in Fig. 3—the frequency of grade A on S, in Fig. 4—The frequency of grade B on S, and in Fig. 5—The frequency of grade C on S.

Based on the distribution of the grades, the percentages of the grades A–C were calculated and shown graphically in Fig. 6—The percentages of grades A–C on S.

Fig. 6 reflects the relationship between impact factors and grades A–C. Using fuzzy set theory, we explain the relationship as the possibilities (likelihood) of journals with impact factors belonging to the grade set. We approximated the curves in Fig. 6 by using straight lines to connect the main points (see Fig. 7) and received the membership functions representing grades A–C, which was shown earlier in Fig. 1.

![](/api/attachments/K9B9KVDG/fulltext/images/89261888595876b9f8bc85784a5ecdbf1135233f53201ba8fe3b496a299bf56f.jpg)  
Fig. 3. The frequency of grade A on S.

## 4.2. Step 2: determining membership degrees

From these membership functions and from the current factor of the specific journal under investigation, we can determine the membership degrees of each journal. For instance, if the impact factor of journal is 1.2. Then the membership degrees are approximately h0.6, 0.4, 0, 0i (see arrow #3 in Fig. 1).

## 4.3. Step 3: experts’ subjective judgments

The judgment terms in the knowledge base are fourtuples corresponding to the grade set G, which are shown in Table 2. The values in the right-hand side of the table are set by the authors and are stored in the knowledge base. These values can be changed by the members of each panel.

We now provide an example of how the experts opinions are expressed. Six experts were asked to rank a given MIS journal. The subjective opinions were as follow:

Judgment provided by expert 1: ‘‘much better than B’’ Judgment expert 2: ‘‘somewhat less than A’

Judgment expert 3: ‘‘absolutely belongs to B’’

Judgment expert 4: ‘‘absolutely belongs to A’’

Judgment expert 5: ‘‘abstain’’

Judgment expert $6 \colon ^ { 6 \div } \langle 0 . 9 , 0 . 3 , 0 , 0 \rangle \ ^ { \ast }$ (used numerical data)

![](/api/attachments/K9B9KVDG/fulltext/images/6d8dcfa0fd550896c65ef877c6a858439eef511a9fb8f08ad9057e1c43dc9885.jpg)  
Fig. 4. The frequency of grade B on S.

![](/api/attachments/K9B9KVDG/fulltext/images/51cc47dbed2e2f34a1cf97a5884923466772202c500458df4a75b7cc77ec26b5.jpg)  
Fig. 5. The frequency of grade C on S.

![](/api/attachments/K9B9KVDG/fulltext/images/82989195ee5c8e12d7dbc403db0a2b7ac5995337e7daa975a71ebb6f2334834e.jpg)  
Fig. 6. The percentages of grades A–C on S.

![](/api/attachments/K9B9KVDG/fulltext/images/d52389572da2feaa981ad08dd4fd88b54558fb88b7f35f0a001af40d69d7413c.jpg)  
Fig. 7. Straight lines on Fig. 6.

4.4. Step 4: assigning the weights for the impact factor and experts

Assume the assigned weight for the impact factor of the journal is 0.35. The weight of the subjective assessment is $1 - 0 . 3 5 = 0 . 6 5 .$ According to the method of calculating the weights, we get h0.35, 0.13, 0.13, 0.13, 0.13, 0, 0.13i.

Table 2  
The judgment terms (normalized)

<table><tr><td>Judgment term</td><td>Four-tuple</td></tr><tr><td>Absolutely belongs to A</td><td> $\langle 1, 0, 0, 0 \rangle$ </td></tr><tr><td>A somewhat less than A</td><td> $\langle 0.9, 0.1, 0, 0 \rangle$ </td></tr><tr><td>Less than A</td><td> $\langle 0.7, 0.3, 0, 0 \rangle$ </td></tr><tr><td>Much better than B</td><td> $\langle 0.5, 0.5, 0, 0 \rangle$ </td></tr><tr><td>Better than B</td><td> $\langle 0.2, 0.8, 0, 0 \rangle$ </td></tr><tr><td>Absolutely belongs to B</td><td> $\langle 0, 1, 0, 0 \rangle$ </td></tr><tr><td>A somewhat less than B</td><td> $\langle 0, 0.9, 0.1, 0 \rangle$ </td></tr><tr><td>Less than B</td><td> $\langle 0, 0.7, 0.3, 0 \rangle$ </td></tr><tr><td>Much better than C</td><td> $\langle 0, 0.5, 0.5, 0 \rangle$ </td></tr><tr><td>Better than C</td><td> $\langle 0, 0.2, 0.8, 0 \rangle$ </td></tr><tr><td>Absolutely belongs to C</td><td> $\langle 0, 0, 1, 0 \rangle$ </td></tr><tr><td>A somewhat less than C</td><td> $\langle 0, 0, 0.9, 0.1 \rangle$ </td></tr><tr><td>Less than C</td><td> $\langle 0, 0, 0.7, 0.3 \rangle$ </td></tr><tr><td>Much better than 0</td><td> $\langle 0, 0, 0.5, 0.5 \rangle$ </td></tr><tr><td>Better than 0</td><td> $\langle 0, 0, 0.2, 0.8 \rangle$ </td></tr><tr><td>Absolutely belongs to 0</td><td> $\langle 0, 0, 0, 1 \rangle$ </td></tr><tr><td>No information</td><td> $(\phi, \phi, \phi, \phi)$ </td></tr></table>

## 4.5. Step 5: consolidating the experts’ judgment

From conversion Table 1 and the expert judgment (step 3), results in the evaluation matrix of experts subjective judgments.

<table><tr><td>A</td><td>B</td><td>C</td><td>0</td><td></td><td></td></tr><tr><td>0.5</td><td>0.5</td><td>0</td><td>0</td><td>Expert</td><td>#1</td></tr><tr><td>0.9</td><td>0.1</td><td>0</td><td>0</td><td>&quot;</td><td>#2</td></tr><tr><td>0</td><td>1</td><td>0</td><td>0</td><td>&quot;</td><td>#3</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>&quot;</td><td>#4</td></tr><tr><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td> $\phi$ </td><td>&quot;</td><td>#5</td></tr><tr><td>0.9</td><td>0.3</td><td>0</td><td>0</td><td>&quot;</td><td>#6</td></tr></table>

## 4.6. Step 6: combining the objective and subjective information

Now, we add the impact factor membership degrees from step 2 as the first row elements into the above subjective evaluation matrix to obtain the evaluation matrix.

$$
\left( \begin{array}{c c c c} 0. 6 & 0. 4 & 0 & 0 \\ 0. 5 & 0. 5 & 0 & 0 \\ 0. 9 & 0. 1 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ \phi & \phi & \phi & \phi \\ 0. 9 & 0. 3 & 0 & 0 \end{array} \right)
$$

## 4.7. Step 7: adjusting for the weights

According to Eq. (2) in Appendix A, we adjust the matrix for the weights, and obtain the evaluation vector h0.639, 0.387, 0, 0i.

## 4.8. Steps 8 and 9: determination of the grade of the journal

From the evaluation vector, we can infer that the grade of the journal is most likely to be A. As stated earlier, if the group does not accept this result, a sensitivity analysis and/or consensus reaching method can be used to resolve the conflict.

## 5. Evaluation, limitation, generalization and conclusion

## 5.1. Evaluation

The proposed system was demonstrated to potential users in Hong Kong. The essentials of the system were also presented at two academic conferences. We used a simple questionnaire to test the participants perception to the proposed system. The results of a pilot study using 13 participants who had experienced the use of the old method in Hong Kong and 13 academics who participated in a conference and attended our presentation about the system, indicated the following:

On a Likert scale of 7 (1: undesirable, 7: very much desirable), people favor the proposed system with an average of 5.62. The idea of providing a qualitative option was regarded highly desirable (6.31), the idea of combining the objective and subjective information was favored at a level of 5.62, while the idea of using the Web to reach a consensus received a vote of 6. Using the web for collaboration received a vote of 5.92. Finally, anonymity was favored at a level of 5.31.

## 5.1.1. Implementation

Even if the method is validated in one place or several, there is likely to be resistance to its implementation. For example, it may be a challenge to tell academics to enter their subjective opinions into a computer. Like any implementation of innovations, one needs to deal with change management. The success of the implementation would depend upon:

(a) How good the existing process is? If there are many complaints, people will be more willing to try an alternative.

(b) While some people will resist entering opinions into a computer, others will be apprehensive about expressing opinions in a face-to-face meeting. Dozens of experiments indicate the value of anonymity, especially in controversial issues such as the value of a journal. If people are assured of anonymity they will express their true opinions (e.g., [13,18,21]).

(c) Funding agencies may mandate the use of the method once they find that it works better.

(d) The specific organizational culture and attitude, and the power of management, could be important determinants of successful implementation.

(e) With more and more academic institutions moving to merit-based salary increases, the need for a better evaluation process becomes critical. Publication is a major criterion in most universities and the valuation of journals is a difficult and controversial issue. Therefore, the chance of implementation of a method like that proposed is high, especially when its cost is minimal and it is user friendly.

## 5.2. Discussion of the proposed methodology, limitations, and generalization

Several issues related to the implementation of the GDSS and its potential expansions are:

(a) The proposed methodology is based on the assumption that historical grades of the journals are available in the organizational memory. Grades published in the literature may also be used for this purpose. One discipline where such ranking is available is MIS, for example, Holsapple et al., and Walstrom et al. [22].

(b) The role of the facilitator (or panel leader) is minimal and most of the tasks could be automated. The individual users can perform steps 1–8. If there is no consensus at step 8, the facilitator needs to act. However, the system can be expanded to include an automatic consensus building mechanism. For example, a Delphi-like procedure asking them to justify their vote, which is then shared among all panel members.

(c) The impact factor is selected as the objective criteria. Is this the best objective measure? To the best of our knowledge, there are no empirical studies that address this issue. Such a measure is also used by the government in the UK for similar purposes. In our literature review, we found a variety of citation-based methods.

(d) The proposed GDSS procedure is user friendly, since it is Web implemented. Trial runs at the City University of Hong Kong indicated that the system was well liked by the users but is it really superior to other approaches?

(e) In our systems, the experts can be in one room, using supportive GDSS software like Group-Systems V or eroom.com to improve the decision process. The experts can also be in different places. In Hong Kong, as in many other places, the experts used to meet face-to-face. Our methodology allows them to be dispersed. In an informal discussion here, most faculty said they liked it because it saved time, allowed for anonymity, and employed objective input infor mation.

(f) The quantification of judgmental terms approach was implemented before and is fairly acceptable in multiple criteria decision analysis modeling. Obviously, the conversion values of judgment terms vary. However, our model allows for adjustments by the users.

(g) The representation of the objective information can be accomplished either by using one value or several in a vector. This permits quick integration of the objective and subjective data—clearly an advantage of our GDSS. The fuzzy set approach also allows for missing information.

## 5.3. Conclusion

The GDSS proposed here can be very useful for making difficult and controversial decisions regarding the value of academic journals. Furthermore, an evaluation must be done periodically since journals quality may change over time. Journals strive to improve quality and new editors or new policies may significantly change the quality and the image of a journal.

The proposed subjective and objective assessment method and the developed GDSS can be extended to cover a wide range of applications, including the selection of R&D projects in government funding agencies. In the National Natural Science Foundation of China (NSFC), an Internet-Based Science Information System (ISIS, http://isis.nsfc.gov.cn) has been developed based on the research methods proposed in this paper. It has been used to support the decision tasks of online review of over 34,000 research projects in 2003. The results have shown that the subjective and objective integrated approach balanced the opinions of decision makers (external reviewers) and that web-based group decision support interfaces provide efficient tools for decision makers to express their opinions.

## Acknowledgements

This research was partly supported by the National Natural Science Foundation of China and Hong Kong Research Grant Council Joint Funding Scheme (Project No. 9050137), and the Competitive Earmarked Research Grant (CERG), Hong Kong SAR (Project Nos. 9040709 and 9040825) and Strategic Research Grant of City University of Hong Kong (Project Nos. 7100288 and 7001143). Many thanks to the anonymous reviewers for their contributions to improve this manuscript.

## Appendix A. The supportive mathematical operations

## A.1. General notations

Let X be a classical set of objects, called the universe. The generic elements in X is denoted as x, i.e., X ¼ fxg. A fuzzy set A in X is characterized by a membership function $\mu _ { A } ( x )$ that associate each element in X with a real number in the unit interval [0, 1].

A fuzzy set A is usually denoted by a set of pairs, $A = \{ ( x , \mu _ { A } ( x ) ) , x \in X , \mu _ { A } ( x ) \in [ 0 , 1 ] \} . \mu _ { A } ( x )$ is called membership degree [25]. For example, let $X = \{ \mathrm { B i l l } . $ Louis, Michael, Stephen}. Fuzzy set tall people can be represented as $A = \{ ( \mathrm { B i l l } , 0 . 8 ) , ( \mathrm { L o u i s } , 0 . 5 )$ , (Michael, 0.3), (Stephen, 1.0)}, which means that Stephen absolutely belongs to tall people, and Bill, Louis, Michael belong to tall people in 0.8, 0.5, and 0.3 degree respectively. When X is a definite set, i.e., $\{ x _ { 1 } , \ldots , x _ { n } \}$ , the fuzzy set A can be represented as $\textstyle A = \sum _ { i = 1 } ^ { n } x _ { i } / \mu _ { A } ( x _ { i } )$ . If there is a natural ordering of the elements in the universe U, one can simply use the vector $( \mu _ { A } ( x _ { 1 } ) , \ldots , \mu _ { A } ( x _ { n } ) )$ (or more clearly, $( x _ { 1 } / \mu _ { A } ( x _ { 1 } ) , \ldots , x _ { n } / \mu _ { A } ( x _ { n } ) ) )$ of the membership degrees to represent the fuzzy set A. When a universal set in infinite, which is usually the case for a set of real numbers, it is impossible to list all the elements together with their membership degrees. This kind of fuzzy set is often represented by an analytic form. For example, fuzzy set about 6 can be represented as

$$
A (x) = \left\{ \begin{array}{l l} x - 5, & \text { when } 5 \leq x \leq 6 \\ 7 - x, & \text { when } 6 \leq x \leq 7 \\ 0, & \text { otherwise } \end{array} \right.
$$

Let $G = \{ g _ { 1 } , g _ { 2 } , \ldots , g _ { d } \}$ be a set of grades of journals (without loss of generality, we assume $g _ { 1 }$ is the best grade and g<sub>d</sub> the worst grade). Let $P = \{ P _ { 1 } , P _ { 2 } , \ldots , P _ { t } \}$ be the set of experts and $J = \left\{ J _ { 1 } , J _ { 2 } , \ldots , J _ { n } \right\}$ be the set of journals. The grades $\{ g _ { 1 } , g _ { 2 } , \ldots , g _ { d } \}$ are fuzzy sets defined on journal set J, with membership values between 0 and 1, and they can be represented as:

$$
\begin{array}{l} g _ {i} = \left\{\frac {J _ {i}}{a _ {i 1}}, \frac {J _ {2}}{a _ {i 2}}, \dots , \frac {J _ {n}}{a _ {i n}} \right\} \quad (a _ {i j} \in [ 0, 1 ]; 1 \leq i \leq d \\ \text { and } \quad j = 1, 2, \dots , n) \end{array}
$$

## A.2. Step 1: analyzing the relationship between grades and impact factors of journals

Assume that there exist membership functions $\mu _ { g _ { 1 } } , \mu _ { g _ { 2 } } , \ldots , \mu _ { g _ { d } }$ which reflect the relationship between impact factors and grades of journals. If we denote the impact factor of journal $J _ { l }$ as $J _ { l } ^ { x } \left( 1 \leq l \leq n \right)$ , then we can determine fuzzy set $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ on the consideration of impact factors of journals, which have the following format:

$$
g _ {i} = \left\{\frac {J _ {1}}{\mu_ {g _ {i}} (J _ {1} ^ {x})}, \frac {J _ {2}}{\mu_ {g _ {i}} (J _ {2} ^ {x})}, \dots \frac {J _ {n}}{\mu_ {g _ {i}} (J _ {n} ^ {x})} \right\} (i = 1, \dots , d
$$

$$
\mu_ {g _ {i}} (J _ {1} ^ {x}), \dots , \mu_ {g _ {i}} (J _ {n} ^ {x}) \in [ 0, 1 ])
$$

Membership functions $\mu _ { g _ { 1 } } , \mu _ { g _ { 2 } } , \ldots , \mu _ { g _ { d } }$ can be obtained by analyzing historical data at one point of time $( \mathrm { e . g . }$ , the latest data) of impact factors and grades of journals. From the point view of journal $J _ { k } ,$ , vector $( \mu _ { g _ { 1 } } ( J _ { k } ^ { x } ) , \mu _ { g _ { 2 } } ( J _ { k } ^ { x } ) , \ldots , \mu _ { g _ { d } } ( J _ { k } ^ { x } ) )$ expresses the grade of journal $J _ { k } .$ . This means that journal $J _ { k }$ belongs to the grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ with membership degrees $\mu _ { g _ { 1 } } ( J _ { k } ^ { x } ) , \mu _ { g _ { 2 } } ( J _ { k } ^ { x } ) , \ldots , \mu _ { g _ { d } } ( J _ { k } ^ { x } )$ respectively. In other word, the vector $( \mu _ { g _ { 1 } } ( \ddot { J _ { k } } ) , \mu _ { g _ { 2 } } ( J _ { k } ^ { x } ) , \ldots , \mu _ { g _ { d } } ( J _ { k } ^ { x } ) )$ Þ represents fuzzy set ‘‘grade of journal $J _ { k } { } ^ { \binom { 6 } { 7 } }$ defined on the grade set $g _ { 1 } , g _ { 2 } , \ldots , g _ { d } .$

## A.3. Step 2: determining membership degrees

In general, with membership functions, we can define a fuzzy mapping as follows:

$$
f: x \to (\mu_ {g _ {1}} (x), \mu_ {g _ {2}} (x), \dots , \mu_ {g _ {d}} (x))
$$

where $x \in S .$ With the membership functions $\mu _ { g _ { 1 } } , \mu _ { g _ { 2 } } , \ldots , \mu _ { g _ { d } }$ , the fuzzy mapping f gives a journal $( \mathrm { e } . \mathrm { g } . , : J _ { k } )$ with an impact factor, x, the degree to which the specific journal belongs to the grades of journals $g _ { 1 } , g _ { 2 } , \ldots , g _ { d } .$ , respectively. We can explain that the degrees form a fuzzy set ‘‘grade of journal $J _ { k } ^ { \mathbf { \Phi } _ { k } \mathbf { \Phi } ^ { \left\{ \begin{array} { r l } \end{array} \right. } \left. \begin{array} { r l } \end{array} \right. }$ defined on the grades set $g _ { 1 } , g _ { 2 } , \ldots , g _ { d } .$ . For example, if the impact factor of a journal is known to be 0.9, a designation of $\mu _ { g _ { 1 } } ( 0 . 9 ) = 0 . 7 , \mu _ { g _ { 2 } } ( 0 . 9 ) = 0 . 5 , \ldots ,$ $\mu _ { g _ { d } } ( 0 . 9 ) = 0 . 2 $ ; means the journal belongs to a set of grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ with $0 . 7 , 0 . 5 , \ldots , 0 . 2$ degrees, respectively. For each journal $J _ { l } \in J ( 1 \le l \le n )$ , the degrees which the journal belongs to different grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ form a vector, denoted as impact factor vector $V ^ { l } ;$

$$
V ^ {l} = (v _ {1} ^ {l}, v _ {2} ^ {l}, \ldots , v _ {d} ^ {l}), l = 1, \ldots , n\tag{1}
$$

## A.4. Step 3: expressing the experts’ subjective judgments individually

Assume that a group of experts, $\begin{array} { r l } { P , } & { { } ( P = } \end{array}$ $\{ P _ { 1 } , P _ { 2 } , \ldots , P _ { t } \} )$ , participates in a panel. Usually, panel members express their opinions, first, independently of each other. Then, they try to reach a consensus. As mentioned above, the grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ are fuzzy sets defined on journal set, J, where member ship is between 0 and 1, where

$$
\begin{array}{l} g _ {i} = \left\{\frac {J _ {1}}{a _ {i 1}}, \frac {J _ {2}}{a _ {i 2}}, \dots \frac {J _ {n}}{a _ {i n}} \right\} \quad (a _ {i j} \in [ 0, 1 ]; 1 \leq i \leq d \\ j = 1, 2, \dots , n) \end{array}
$$

However, in practice, it may be impractical or not easy for experts to specify their subjective judgments using fuzzy sets $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ and associated degrees of memberships for a set of journals. Such information can be expressed in the following matrix:

Journals

$$
\begin{array}{c} \text {Grades} \\ \left[ \begin{array}{c c c c} & g _ {1} & g _ {2} \dots & g _ {d} \\ J _ {1} & & & \\ J _ {2} & \mu_ {1 1} & \mu_ {1 2} & \mu_ {1 d} \\ . & \mu_ {2 1} & \mu_ {2 2} & \mu_ {2 d} \\ . & & & \\ J _ {n} & \mu_ {n 1} & \mu_ {n 2} & \mu_ {n d} \end{array} \right] \end{array}
$$

Judgment terms can be used to simplify the above processes. A judgment term is an ordered d-tuple $\langle a _ { 1 } , a _ { 2 } , \ldots , a _ { d } \rangle$ , where $a _ { i } \in [ 0 , 1 ] , 1 \leq i \leq d .$ The values of the judgment term, i.e., d-tuple, of a journal represent the degrees that a specific journal belongs to the grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d } .$ , respectively.

## A.5. Step 4: assigning the weights

Let the weight of impact factor for journal $J _ { k }$ be $w _ { 0 } ^ { k } ,$ and the weight of the panel of experts for that $J _ { k }$ journal, be $w _ { e } ^ { k } ,$ , where $w _ { 0 } ^ { \bar { k } } + w _ { e } ^ { k } = 1 , \bar { w } _ { 0 } ^ { k } \geq 0 , w _ { e } ^ { k } \geq 0 .$ The reason that the sum of the weights is one, is that we allow this way a trade off between the subjective and objective assessments. Suppose we assign weights $w _ { e _ { 1 } } ^ { \bar { k } } , w _ { e _ { 2 } } ^ { k } , \dots , w _ { e _ { t } } ^ { k }$ , one each to experts $P _ { 1 } , P _ { 2 } , \ldots , P _ { t } ,$ respectively, where $\begin{array} { r } { \sum _ { j = 1 } ^ { t } w _ { e _ { i } } ^ { k } = 1 , \bar { w } _ { e _ { i } } ^ { k } \geq 0 , j = 1 , \dots , t . } \end{array}$ According to the impact factor of the journal and judgment information of the journals given by experts, we consider four cases regarding the assignment of weights to impact factors and to experts. These are:

Case 1. The impact factor of journal $J _ { k }$ is known and the judgment information about journal $J _ { k }$ is complete: The weight of the impact factor is known to be $w _ { o } ^ { k } ,$ , and the weight assigned to the expert $P _ { j }$ is given by:

$$
w _ {j} ^ {k} = w _ {j} ^ {k} w _ {e _ {j}} ^ {k} \quad j = 1, \ldots , t,
$$

where $\begin{array} { r } { \sum _ { j = 1 } ^ { t } w _ { j } ^ { k } = w _ { e } ^ { k } . } \end{array}$ . In this case, the weight set corresponding to journal $J _ { k }$ is $W ^ { k } = ( w _ { 0 } ^ { k } , w _ { 1 } ^ { k } , \cdot \cdot \cdot , w _ { t } ^ { k } )$

Case 2. The impact factor of journal $J _ { k }$ is known and the judgment information of journal $J _ { k }$ is incomplete: Suppose expert $P _ { l } \left( 1 \leq l \leq t \right)$ does not give judgment information of journal $J _ { k } .$ Therefore, we set the weight of expert $P _ { l }$ be $0 ,$ and correspondingly, the normalized weight of expert $P _ { j } \left( 1 \leq j \leq t , j \neq l \right)$ is given by:

$$
w _ {e _ {j}} ^ {k ^ {\prime}} = \frac {w _ {e _ {j}} ^ {k}}{\sum_ {i = 1 , i \neq l} ^ {t} w _ {e _ {j}} ^ {k}}, \quad j = 1, \ldots , t; j \neq l,
$$

where $\begin{array} { r } { \sum _ { j = 1 , j \neq l } ^ { t } w _ { e _ { j } } ^ { k ^ { \prime } } = 1 } \end{array}$ . Therefore, in order to obtain the weight set, the weight assigned to the expert $P _ { j }$ is given by:

$$
w _ {j} ^ {k} = w _ {e} ^ {k} w _ {e _ {j}} ^ {k ^ {\prime}}, \quad j = 1, \dots , t; j \neq l,
$$

where $\textstyle \sum _ { j = 1 , j \neq l } ^ { t } w _ { j } ^ { k } = w _ { e } ^ { k }$ . In this case, the weight set corresponding to journal $J _ { k }$ is $W ^ { k } = ( w _ { 0 } ^ { k } , \bar { w } _ { 1 } ^ { k } , \dots ,$ $0 , \ldots w _ { t } ^ { k } )$

Case 3. The impact factor of journal $J _ { k }$ is unknown but the judgment information of journal $J _ { k }$ is complete: Since there is no objective information we set the weight of the impact factor be 0. Therefore, we have $w _ { e } ^ { k } = 1$ , and the weight assigned to the expert $P _ { j }$ is given by:

$$
w _ {j} ^ {k} = w _ {e} ^ {k} w _ {e _ {j}} ^ {k}, \quad j = 1, \ldots , t,
$$

where $\textstyle \sum _ { j = 1 } ^ { t } w _ { j } ^ { k } = 1$ . In this case, the weight set corresponding to journal $J _ { k }$ is $W ^ { k } = ( 0 , w _ { 0 } ^ { k } , w _ { 1 } ^ { \bar { k } } , \dots , w _ { t } ^ { k } )$

Case 4. The impact factor of journal $J _ { k }$ is unknown and the judgment information of journal $J _ { k }$ is also incomplete: First, we set the weight of the impact factor be 0. Therefore, $w _ { e } ^ { k } = 1$ . Suppose expert $P _ { l }$ $( 1 \leq l \leq t )$ does not give judgment information of journal $J _ { k } .$ Then, we set the weight of expert $P _ { l }$ be

0, and correspondingly, the normalized weight of expert $P _ { j } \left( 1 \leq j \leq t , j \neq l \right)$ is given by:

$$
w _ {e _ {j}} ^ {k ^ {\prime}} = \frac {w _ {e _ {j}} ^ {k}}{\sum_ {i = 1 , i \neq l} ^ {l} w _ {e _ {i}} ^ {k}} \quad , j = 1, \dots , t; j \neq l,
$$

where $\begin{array} { r } { \sum _ { j = 1 , j \neq l } ^ { t } w _ { e _ { i } } ^ { k ^ { \prime } } = 1 } \end{array}$ . Therefore, in order to obtain the weight set, the weight assigned to the expert $P _ { j }$ is given by:

$$
w _ {j} ^ {k} = w _ {e} ^ {k} w _ {e _ {j}} ^ {k ^ {\prime}}, j = 1, \dots t, j \neq l,
$$

where $\textstyle \sum _ { j = 1 , j \neq l } ^ { t } w _ { j } ^ { k } = w _ { e } ^ { k }$ . In this case, the weight set corresponding to journal $J _ { k }$ is $W ^ { k } = ( 0 , \bar { w _ { 1 } ^ { k } } , \dots ;$ $0 , \ldots { } w _ { t } ^ { k } )$

## A.6. Step $5 ;$ converting and consolidating the experts’ opinions

For expert $P _ { i } ,$ the subjective judgment $( \mathrm { i . e . } ,$ , judgment term) on the journal $J _ { k }$ forms a vector, denoted as $V _ { i } ^ { k } = ( \nu _ { i 1 } ^ { k } , \nu _ { i 2 } ^ { k } , \cdot \cdot \cdot , \nu _ { i d } ^ { k } )$ , where each $\nu _ { i j } ^ { k } \in [ 0 , 1 ]$ $( 1 \leq i \leq t ; j = 1 , \ldots , d )$

For a panel of t experts involved in evaluating the journal $J _ { k } ,$ a subjective evaluation relation matrix, denoted as $E ^ { k ^ { \prime } } = [ \nu _ { i i } ^ { k } ] , \ i = 1 , \dots , t ; j = 1 , \dots , d .$ , is formed by integrating the individual experts’ judgment vectors $V _ { i } ^ { k } , i = 1 , \dots , t .$ . The relation $\mathbf { \bar { \boldsymbol { E } } ^ { \boldsymbol { k } ^ { \prime } } }$ consists of the experts’ subjective judgments information on journal $J _ { k } .$

## A.7. Step 6: integrating the subjective and objective information

To evaluate the journal $J _ { k }$ both subjectively and objectively, we add the impact factor vector $V ^ { k }$ in (1) as the first row elements of the matrix $E ^ { k ^ { \prime } }$ , then get the integrated evaluation matrix denoted as $E ^ { k } = [ \nu _ { i j } ^ { k } ]$ $i = 0 , 1 , \ldots , t ; j = 1 , \ldots , d .$

## A.8. Step 7: Adjusting for the weights

For a journal $J _ { k } ,$ we derived the fuzzy weight $\boldsymbol { W } ^ { k }$ and the fuzzy evaluation relation $E ^ { k }$ . Then, the process of determining the final grade of the journal $J _ { k }$ is equivalent to the process of determining a membership value for the journal $J _ { k }$ in each of the evaluation grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d }$ . This process can be implemented through the composition operation $W ^ { k } \circ E ^ { k }$ . The result is a fuzzy vector (evaluation vector), denoted as $Y ^ { k }$ containing the membership values for the journal $J _ { k }$ in each of evaluation grades $g _ { 1 } , g _ { 2 } , \ldots , g _ { d } \colon$

$$
\begin{array}{l} Y ^ {k} = W ^ {k} \circ E ^ {k} \\ = (w _ {0} ^ {k}, w _ {1} ^ {k}, \ldots , w _ {t} ^ {k}) \circ \left[ \begin{array}{c c c c} e _ {0 1} ^ {k} & e _ {0 2} ^ {k} & \dots & e _ {0 d} ^ {k} \\ e _ {1 1} ^ {k} & e _ {1 2} ^ {k} & \dots & e _ {1 d} ^ {k} \\ \vdots & \vdots & & \vdots \\ e _ {t 1} ^ {k} & e _ {t 2} ^ {k} & \dots & e _ {t d} ^ {k} \end{array} \right] \\ = (y _ {1} ^ {k}, y _ {2} ^ {k}, \ldots , y _ {d} ^ {k}), \end{array}\tag{2}
$$

where $y _ { j } ^ { k } = \left( w _ { 0 } ^ { k } \cdot e _ { 0 j } ^ { k } \right) \oplus \left( w _ { 1 } ^ { k } \cdot e _ { 1 j } ^ { k } \right) \oplus . . . \oplus \left( w _ { n } ^ { k } \cdot e _ { n j } ^ { k } \right)$ and $^ { \bullet \bullet } \cdot ^ { \ l , \bullet } \oplus ^ { \ l , \bullet }$ are defined as:

(a) algebraic product, $a \cdot b : c = a b$

(b) bounded sum, $a \oplus b : c = a \oplus b = m i n \left\{ 1 , a + b \right\}$

## A.9. Step 8: trying to reach a consensus

According to the principles of fuzzy classification, we have $y _ { i } ^ { \bar { k } } = \operatorname* { m a x } ( y _ { 1 } ^ { k } , y _ { 2 } ^ { k } , \ldots , y _ { d } ^ { k } )$ . Thus, the corresponding grade $g _ { i }$ is the final grade of the journal $J _ { k } .$ In practical evaluation process, we set a parameter d to check if $| y _ { i } ^ { k } - y _ { i + 1 } ^ { k } | < \bar { \delta } , i < d .$ , if it happens, then we can say this journal is between grades $g _ { i }$ and $g _ { i + 1 } .$ $\mathrm { I f } | y _ { i } ^ { k } - y _ { j } ^ { k } | { < } \delta .$ , and $i < j , j \neq i + 1 , i < d - 1$ , then the experts have strong contradicting opinions.

## A.10. Step 9: sensitivity analysis

A trial and error approach can be employed for this step. The decision makers enter modified subjective data and the model recalculates the value of $\bar { Y ^ { k } }$

## References

[1] V.A. Beattie, R.J. Ryan, The impact of non-serial publications on research in accounting and finance, ABACUS 27 (1), 1991, pp. 32–50.

[2] C.H. Cheng, A. Kumar, J.G. Motwani, A. Reisman, M.S. Madam, A citation analysis of the technology innovation management journals, IEEE Transactions on Engineering Management 46 (1), 1999, pp. 4–13.

[3] N.C. Dalkey, The Delphi Method: An Experimental Study of Group Opinion, The Rand Corporation, Santa Monica, 1969.

[4] J. Diaz, R.T. Black, J. Rabianski, A note on the ranking of real estate research journals, Real Estate Economics 24 (4), 1996, pp. 551–563.

[5] J.R. Doyle, Grade inflation in the UK’s 1996 research assessment exercise, Omega 26 (1), 1998, pp. 461–465.

[6] M.M. Extejt, J.E. Smith, The behavioral sciences and management: an evaluation of relevant journals, Journal of Management 16 (3), 1990, pp. 539–551.

[7] L.Y. Flores, S.C. Rooney, P.P. Heppner, L.D. Browne, Trend analyses of major contributions in the counseling psychologist cited from 1986 to 1996: impact and implications, Counseling Psychologist 27 (1), 1999, pp. 73–95.

[8] G.A. Forgionne, R. Kohli, A multiple criteria assessment of decision technology system journal quality, Information and Management 38, 2001, pp. 421–435.

[9] M.L. Gillenson, J.D. Stutz, Academic issues in MIS: journals and books, MIS Quarterly 15 (4), 1991, pp. 447–452.

[10] C.W. Holsapple, L.E. Johnson, H. Manakyan, J.T. Tanner, A citation analysis of business computing research journal, Information and Management 25, 1993, pp. 231–244.

[11] C.W. Holsapple, L. Johnson, H. Manakyan, J. Tanner, Business computer research journals: a normalized citation analysis, Journal of Management Information Systems 11 (1), 1994, pp. 131–140.

[12] L.M. Jessup, J. Valacich, Group Support Systems: New Perspectives, Macmillan, New York, 1993.

[13] R. Kwok, J. Ma, D. Vogel, Assessing GSS and content facilitation effects on knowledge acquisition, Journal of Management Information Systems 19 (3), 2002, pp. 185– 229.

[14] R. Kwok, J. Ma, D. Zhou, Improving group decision making: a fuzzy GSS approach, IEEE Transactions on Systems, Man, and Cybernetics, Part C 32 (1), 2002, pp. 54–63.

[15] R. Kwok, J. Ma, D. Vogel, D. Zhou, Collaborative assessment in education: an application of a fuzzy GSS, Information and Management 39, 2001, pp. 243–253.

[16] S.J. Liebowitz, J.P. Palmer, Assessing the relative impacts of economic journals, Journal of Economic Literature 22, 1984, pp. 77–88.

[17] J. Ma, D. Zhou, Fuzzy set approach to the assessment of student-centered learning, IEEE Transactions on Education 43 (2), 2000, pp. 237–241.

[18] J. Ma, Group decision support systems for assessment of problem-based learning, IEEE Transaction on Education 39 (3), 1996, pp. 388–393.

[19] T.L. Saaty, Decision Making for Leaders: The AHP for Decision in a Complex World, RWS Publication, Pittsburgh, 1995.

[20] A.C. Soteriou, G.C. Hadjinicola, K. Patsia, Assessing production and operations management related journals: the European perspective, Journal of Operations Management 17, 1999, pp. 225–238.

[21] D. Vogel, J. Nunamaker, B. Martz, R. Grohowski, C. McGoff, Electronic meeting system experience at IBM, Journal of Management Information Systems 6 (3), 1990, pp. 25–43.

[22] K.A. Walstrom, B.C. Hardgrave, R.I. Wilson, Forums for management information systems scholars, Communications of the ACM 38 (3), 1995, pp. 93–102.

[23] K.A. Walstrom, B.C. Hardgrave, Forums for information systems scholars: III, Information and Management 39, 2001, pp. 117–124.

[24] C.K. Wing, The ranking of construction management journals, Construction Management and Economics 15, 1997, pp. 387–398.

[25] L.A. Zadeh, Fuzzy sets, Information and Control 8, 1965, pp. 338–353.

[26] http://www.isinet.com/isi/search/glossary.

Efraim Turban (MBA, PhD, University of California at Berkeley) is Professor of Information Systems at City university of Hong Kong. Prior to that, he served on the faculty of several universities, including Lehigh University, Florida International University, and the University of Southern California. Prof. Turban is the author of over 100-refereed articles in journals such as Management Sciences, MIS Quarterly, Operations Research, Journal of MIS and IEEE Transaction on Engineering Management. He also coauthored 20 books including Decision Support and Intelligent Systems, Electronic Commerce: A managerial perspective, and Information Technology for Management. Prof. Turban areas of research are quantitative decision support and implementation of Electronic commerce.

Duanning Zhou is Assistant Professor at the Accounting & Information Systems Department, School of Business and Public Administration, Eastern Washington University, Washington. He received his PhD in Information Systems from City University of Hong Kong in 2000. His current research interests include group decision support systems (GDSS), fuzzy systems, system analysis & design, and electronic commerce. He has papers published in IEEE Transactions on Education, Information & Management, and Theoretical Computer Science.

Jian Ma is Associate Professor in the Department of Information Systems at the City University of Hong Kong. He received his Doctor of Engineering degree in Computer Science from the Asian Institute of Technology in 1991. He was a Lecturer in the School of Computer Science and Engineering at the University of New South Wales, Australia, before joining the City University in 1993. Dr. Ma’s current research areas include electronic business systems, web-based decision support systems, object-oriented and component-based methods for information systems development. His past research has published in IEEE Transactions on Education, IEEE Transactions on Systems, Man and Cybernetics, Decision Support Systems and European Journal of Operational Research.
