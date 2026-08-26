---
otero_id: 7698
otero_key: "3QZZ2BAN"
title: "An experimental comparison of real and artificial deception using a deception generation model"
authors: "Yanjuan Yang; Michael V. Mannino"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.04.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An experimental comparison of real and arti<sup>fi</sup>cial deception using a deception generation model

Yanjuan Yang <sup>a</sup>, Michael V. Mannino <sup>b,</sup>⁎

<sup>a</sup> Automapath Inc., Santa Clara, CA 95050, United States

<sup>b</sup> The Business School, University of Colorado Denver, United States

## a r t i c l e i n f o

Article history: Received 6 April 2011 Received in revised form 23 March 2012 Accepted 29 April 2012 Available online 5 May 2012

Keywords: Deception Deception detection Noise model Data generation model

## a b s t r a c t

To develop a data mining approach for a deception application, data collection costs can be prohibitive because both deceptive data and truthful data are necessary to be collected. To reduce data collection costs, arti<sup>fi</sup>cially generated deception data can be used, but the impact of using arti<sup>fi</sup>cially generated deception data is not well understood. To study the relationship between arti<sup>fi</sup>cial and real deception, this paper presents an experimental comparison using a novel deception generation model. The deception and truth data were collected from <sup>fi</sup>nancial aid applications, a document centric area with limited resources for veri<sup>fi</sup>cation. The data collection provided a unique data set containing truth, natural deception, and boosted deception. To simulate deception, the Application Deception Model was developed to generate arti<sup>fi</sup>cial deception in different deception scenarios. To study differences between arti<sup>fi</sup>cial and real deception, an experiment was performed using deception level and data generation method as factors and directed distance and outlier score as outcome variables. Our results provided evidence of a reasonable similarity between arti<sup>fi</sup>cial and real deception, suggesting the possibility of using arti<sup>fi</sup>cially generated deception to reduce the costs associated with obtaining training data.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Deception involving intentionally provided false information can lead to adverse outcomes in many areas including law enforcement, national security, employment, government bene<sup>fi</sup>ts, taxation, and university admissions. Because of the impact of deception on decision making, there has been an increasing interest in learning about deception and its detection for many years. Research has mainly focused on detecting deception in richly mediated communication channels with more recent emphasis on deception in text and documents.

This research involves document deception, an emerging area of concern in industry and government. In document deception, an individual falsi<sup>fi</sup>es an application for an obligation such as a tax liability or a bene<sup>fi</sup>t such as a position, <sup>fi</sup>nancial aid, loan, government bene<sup>fi</sup>t, or admission to a university. The most prominent area of document deception, tax fraud by individuals and corporations, has been a long standing concern of government. The U.S. I.R.S. estimates the net tax gap of \$385B in 2006 [17], an increase of \$85B from the estimate of the 2001 tax gap. With the ease of submitting electronic applications, fraud in other areas such as health care reimbursements, mortgage applications, and welfare applications have grown in importance in recent years. According to CoreLogic Inc., loan origination fraud was estimated at \$12B in 2010 and \$7.4B in 2011 [10]. The decline in loan origination fraud is due to reduced loan origin amounts and tighter lending standards in the mortgage industry enacted as a result of growing mortgage application fraud in the mid-2000s.

With the increasing cost of higher education, <sup>fi</sup>nancial aid deception has become a prominent form of document deception. Federal, state and private <sup>fi</sup>nancial aid programs target assistance toward students with the least ability to pay for college. This targeting of aid is based on self-reports of <sup>fi</sup>nancial condition by students and parents. Honest reporting of <sup>fi</sup>nancial condition in student <sup>fi</sup>nancial aid applications ensures equitable allocation of scarce <sup>fi</sup>nancial aid resources. Colleges and universities routinely verify the accuracy of a subset of aid applications. According to the report prepared by Rhodes and Tuccillo [26], 30% of dependent student records and 20% of independent student records had false data <sup>fi</sup>elds when schools veri<sup>fi</sup>ed the information as part of the random sample process. The results of discrepancies in the original <sup>fi</sup>nancial aid applications were estimated to cause improper payment of approximately \$270 million (15.9%) of U.S. Pell dollars in 2006–2007.

This research is primarily motivated by the unavailability of data and cost of data collection for developing data mining methods to detect document deception. According to [24], unavailability of data sets is a major deterrent to developing data mining approaches for fraud detection. In most deception studies, deceptive data paired with truth data are collected manually [6,35]. In a university setting, internal review boards may restrict data collection in studies involving deception increasing the cost and dif<sup>fi</sup>culty to obtain a suitable data set. In the student <sup>fi</sup>nancial aid area, <sup>fi</sup>nancial aid of<sup>fi</sup>ces perform tedious audits of applications to determine discrepancies between truth and non-compliant data. To lower the cost of data collection, arti<sup>fi</sup>cially generated deception data can be used to train a data mining program, but the impact of using arti<sup>fi</sup>cially generated deception data is not well understood. For new systems in development, the availability and reliability of test data with deception may be severely limited. Generating arti<sup>fi</sup>cial data may be the only available way to test a new system on deceptive cases.

There is limited understanding about the relationship between arti<sup>fi</sup>cially generated deception and real deception. A number of studies [1,19,22,23,38] have used arti<sup>fi</sup>cially generated noise to study the sensitivity of classi<sup>fi</sup>cation algorithm performance to noise with little understanding of the relationship between real and arti<sup>fi</sup>cial noise. In the intrusion detection domain, large amounts of arti<sup>fi</sup>cial test data were generated for the 1998 and 1999 US DARPA competition [14] although no evaluation of the generated data was reported. For fraud detection in video on demand usage, Barse et al. [2] developed a data generation methodology and performed evaluation. However, their results were limited by the authentic data collection, deception model, and informal comparison between authentic and synthetic data. Thus, previous research does not provide a reasonable understanding about the relationship between real deception and arti<sup>fi</sup>cially generated deception in document-centric deception.

The goals of this study are to develop a deception generation model and to investigate the <sup>fi</sup>t between real deception data and arti<sup>fi</sup>cial deception data created with the deception generation model. To simulate deception, the Application Deception Model (ADM) was developed to generate arti<sup>fi</sup>cial deception in different deception scenarios. The ADM substantially extends previous data generation approaches through goal directed changes for groups of related attributes in observations with incentive to deceive. Deception data and the ground truth data were collected from <sup>fi</sup>nancial aid applications, a document-centric area with limited resources for veri<sup>fi</sup>cation. The data collection provided naturally occurring deception in which subjects had some incentive to falsify applications and boosted deception in which subjects were instructed to falsify their applications. Using the collected data and the ADM, an experiment was conducted with deception level and data generation method as factors and directed distance and outlier score as outcome variables. The experimental results indicated a reasonable <sup>fi</sup>t between arti<sup>fi</sup>cially generated deception and real deception, suggesting the possibility of using arti<sup>fi</sup>cially generated deception to train data mining algorithms.

This paper makes three contributions to research and practice. First, this paper emphasizes the difference between noise and deception through development of a deception generation model and empirical comparison between arti<sup>fi</sup>cially generated noise and deception. Most previous research has failed to make this distinction. Second, this paper brings rigor to the study of arti<sup>fi</sup>cially generated deception through a careful empirical comparison of the data characteristics. Previous research has not performed careful empirical comparisons of arti<sup>fi</sup>cially generated deception. Third, the results of this study suggest the value of arti<sup>fi</sup>cially generated deception in practice. More research is needed to con<sup>fi</sup>rm the value and understand limitations in speci<sup>fi</sup>c applications. If the value of arti<sup>fi</sup>cially generated deception is con<sup>fi</sup>rmed, lower data collection costs may allow improved deception detection policies and methods to be developed.

The rest of the paper is organized as follows. In the next section, we brie<sup>fl</sup>y review deception and noise background and provide details about past efforts to generate arti<sup>fi</sup>cial deception. Section 3 presents the data collection process for the real deceptive data set used in the study. Section 4 describes the data generation models used in the study particularly the Application Deception Model (ADM), a novel method of arti<sup>fi</sup>cial deception generation developed for this study. Section 5 presents the experiment design to investigate the relationship between real deception and arti<sup>fi</sup>cial deception generated by data generation models. The experimental results and <sup>fi</sup>ndings are presented in Section 6. Section 7 concludes the study.

## 2. Related work

The theoretical foundation for this research is drawn from a combination of theories of deception and noise. To provide a context for this study, some literature about deception and its detection are brie<sup>fl</sup>y reviewed. The directly relevant efforts on the usage of arti<sup>fi</sup>cially generated noise and deception are presented after the deception background.

Deception detection has a long history especially in adversarial areas such as law enforcement and intelligence gathering. Numerous studies have noted that the accuracy with which people typically identify deception is only slightly better than chance (approximately 54%) [4]. This issue is more intense when the deception is conveyed in documents because of the lack of nonverbal cues.

Practice in detection of document deception is dominated by scoring models to target audit resources. Because these models are not public, red <sup>fl</sup>ags and guidelines have emerged to guide individuals seeking to avoid audit. For example, FraudGuides.com provides a list of likely triggers for an IRS audit. A relatively small number of classi<sup>fi</sup>cation methods have been proposed in the literature for detection of document deception. Bonchi et al. [3] proposed a classi<sup>fi</sup>cation-based methodology for constructing pro<sup>fi</sup>les of fraudulent taxpayers in tax fraud detection. More recent work by Thang et al. [30] has used fuzzy inference and neural network for tax fraud detection in small businesses. There has also been an initial attempt at applying decision trees in fraud detection for border customs processing [27]. Extensive research has also been conducted on methods of health care fraud detection [21].

Although deception and noise both involve deviations from the true state of an attribute, the underlying data generation processes are different. This research effort focuses on deception as intentional misrepresentations and noise as random, unintentional deviations. Although some research exists about unintentional deception [29], document-based deception involves effort to complete a form with speci<sup>fi</sup>c <sup>fi</sup>eld values. Prominent studies about noise in a data mining context focus on unbiased random noise [13,22,38]. To provide contrast, we compared a standard noise model used in data mining studies to the deception generation model developed for this research.

In the literature, some research has treated deception as noise. Jiang et al. [18] conducted a study to handle explicitly noisy input data on the web. Although the authors refer to noise, the study actually deals with deception on the web. To cope with deception, they proposed two methods: knowledge base modi<sup>fi</sup>cation (KM) and input modi<sup>fi</sup>cation (IM). The KM method modi<sup>fi</sup>es the knowledge base (a decision tree) to account for distortion in the inputs provided by the user. The IM method modi<sup>fi</sup>es an observed input to the most likely true value of the input given the observations made by the system. They used a distortion rate parameter to generate arti<sup>fi</sup>cial training and testing data. The distortion rate parameter does not support goal directed state changes for deception. In addition, the work assumes that inputs are distorted independently rather than allowing scenarios in which groups of inputs are jointly modi<sup>fi</sup>ed.

The most closely related research [2] involves synthetic data generation and evaluation for fraud detection in video on demand usage. Underlying the data generation method is a <sup>fi</sup>nite state model of user behavior. Authentic data was provided by employees demonstrating friendly user behavior and known fraud cases. The authors found a reasonable <sup>fi</sup>t between authentic and synthetic data resulting in fraud detection with somewhat higher speci<sup>fi</sup>city for synthetic data and somewhat higher sensitivity for authentic data. Our work overcomes the limitations of authentic data (small and non-random sample) in their study and provides an important extension (identifying observations with incentive to deceive) for deception generation. Our data collection effort provided a reasonable sample size from a larger population of potential subjects along with collection of two kinds of deceptive behavior (natural and boosted). The Application Deception Model (ADM) developed in this study provides a component to select observations with incentive to deceive. We have also developed a more careful comparison between real and arti<sup>fi</sup>cial deception enabling a more precise characterization of the differences.

![](/api/attachments/3QZZ2BAN/fulltext/images/cf527c3071b2a606324e59969ed57ec40261172688bb0c9fdffe95c7e4703f4d.jpg)  
Fig. 1. Directed distance from truth to natural and boosted deception.

## 3. Real deception data collection

Because a data set containing truthful data paired with deception was not available, we collected a data set for this study. Our experimental data were collected from subjects completing a hypothetical <sup>fi</sup>nancial aid application. Participants in the data collection were students enrolled in undergraduate level courses, eligible to apply for <sup>fi</sup>nancial aid. Subjects were told the purpose of the research and provided instructions about their participation in the study. Before participating in the data collection, subjects completed a consent form indicating their voluntary participation and understanding of the data collection procedures.

Subject participation was limited to completing the same <sup>fi</sup>nancial aid application three times. In the <sup>fi</sup>rst completion (natural deception), subjects were told to provide their natural responses in completing a <sup>fi</sup>nancial aid application in which they perceive little chance for consequences of providing false data. In the second completion (truth), subjects were told to correct all dishonest responses in their original application. In the third completion (boosted deception), subjects were instructed to deliberately respond unethically to make themselves appear to be as competitive as possible.

![](/api/attachments/3QZZ2BAN/fulltext/images/7a54c28a90239344ba23eb000da4d3035e14f3aa11405b07386aa752e8bcaec4.jpg)  
Fig. 2. Application Deception Model.

Table 2  
Table 1  
Deception scenarios in <sup>fi</sup>nancial aid application.

<table><tr><td>Scenarios</td><td>Conditions</td><td>Actions</td></tr><tr><td>Scenario 1Deception on status</td><td>DependentHigh parents&#x27; financial variable</td><td>Change status to independent or reduce parents&#x27; financial variable</td></tr><tr><td>Scenario 2Deception on merit-based features</td><td>Low merit-based feature value</td><td>Increase merit-based feature value</td></tr></table>

## 3.1. Natural deception data collection

For natural deception, our data collection methods adhered to requirements of the internal review board. The University of Colorado internal review board required that student subjects be told that <sup>fi</sup>nancial aid applications were hypothetical. Thus, it was not possible to collect <sup>fi</sup>nancial aid applications under false pretenses with student subjects concerned about consequences of submitting false applications. Student subjects were well informed about <sup>fi</sup>nancial aid applications so we felt that they could provide responses that closely resembled responses under a natural scenario with little perceived risk of detection. Our <sup>fi</sup>nancial aid application design was similar to the internal college application that lacks the intimidating warnings of the of<sup>fi</sup>cial government <sup>fi</sup>nancial aid document

As evidence of the reasonableness of our data collection approach, the deception rate in our natural deception data set (23%) was similar to the rates reported by Rhodes and Tuccillo [26]. They reported 20% of independent students and 30% of dependent students had provided false information before veri<sup>fi</sup>cation. In private conversations, <sup>fi</sup>nancial aid administrators indicated that students had no repercussions from providing false data initially as they could correct the data without recourse if asked for veri<sup>fi</sup>cation. Thus, our instructions to complete a <sup>fi</sup>nancial aid application with a perception of little chance for consequences of deception were consistent with veri<sup>fi</sup>cation practices by <sup>fi</sup>nancial aid of<sup>fi</sup>ces.

Our data collection was also consistent with other recent studies on deception. A number of other studies [7,12,31,34,36] have performed deception detection studies using data collected from subjects instructed to provide deception. Although some studies collected deception through a game environment, the impact of the game environment on the reasonableness of the deceptive patterns was not clear in the studies. For example in George et al. [12], data collection involved subjects competing in an interview process pitting interviewee against interviewer. Zhou et al. [37] used data sets from four studies to evaluate a statistical language modeling approach for deception detection in computer mediated communication.

Features included in each group of variables

<table><tr><td>Variables</td><td>Attributes</td></tr><tr><td rowspan="2">Status</td><td>Age</td></tr><tr><td>Marital status</td></tr><tr><td rowspan="7">Financial</td><td>Student&#x27;s earned income</td></tr><tr><td>Student&#x27;s total bank balance</td></tr><tr><td>Student&#x27;s net worth of real estate</td></tr><tr><td>Parents&#x27; earned income</td></tr><tr><td>Parents&#x27; investment income</td></tr><tr><td>Parents&#x27; total bank balance</td></tr><tr><td>Parents&#x27; net worth of real estate</td></tr><tr><td rowspan="8">Merit-based</td><td>Cumulative GPA</td></tr><tr><td>GPA from the most recent semester</td></tr><tr><td>GPA from the semester prior to the most recent semester</td></tr><tr><td>Previous award</td></tr><tr><td>Number of employment positions</td></tr><tr><td>Number of management positions</td></tr><tr><td>Number of activities</td></tr><tr><td>Number of leadership experiences</td></tr></table>

## 3.2. Boosted deception data collection

Our usage of boosted deception was similar to the data collection procedure used by George et al. [12]. In this study, the authors instructed student subjects to deliberately pad resumes to fool subjects serving as interviewers.

Our usage of boosted deception provided a higher level of deception so that we could compare real and arti<sup>fi</sup>cial data on higher levels of deception and noise. Fig. 1 shows a graph demonstrating the different levels of deception in the natural deception and boosted deception data sets. The horizontal axis corresponds to the observation number (1 to 150) and the vertical axis represents the directed distance (see Section 5.3) from the observation to the truth. The diamonds show the distances of the natural deception observations, while the squares indicate the distances of the boosted deception observations. The graph indicates that every case in the boosted deception dataset involves deception, which is reasonable because the subjects were instructed to lie in the application to maximize the chances for the <sup>fi</sup>nancial aid. On the other hand, 23% (35 out of 150) of the natural deception observations contain deception.

Note that the entire boosted data set is not used in the experiments described later. We mixed observations from the boosted deception and truth data sets to control the level of deception.

## 4. Data generation models for noise and deception

Since some past studies of deception have not clearly distinguished noise and deception, data generation models for both noise and deception were used in this study. This section brie<sup>fl</sup>y reviews a prominent noise model used in this study and provides a detailed description of the Application Deception Model, a new deception generation model developed for this study.

## 4.1. Variable Noise Model

Noise occurs when the true input state is perturbed by a measurement process. A noise model provides a method to perturb or change data from its true state to an incorrect state. The Variable Noise Model [13] has been used in studies of noise handling as well as deception in the data mining literature.

In the Variable Noise Model, each attribute is randomly perturbed with its own perturbation probability. Each attribute is randomly assigned a noise level from a uniform distribution between the speci<sup>fi</sup>ed ranges. If a random number is less than or equal to the attribute's noise probability, the value is changed. If the attribute's scale is nominal, the value is randomly changed to any other value. If the attribute's scale is ordinal, the attribute is changed to an adjacent value. If the attribute is numeric (ratio or absolute scale), the value is changed using an equal

Table 3  
Data selection for deception scenarios in <sup>fi</sup>nancial aid application.

<table><tr><td>Subset 1TruthStatus + financial features</td><td>Ideal candidateDistance</td><td>Subset 2TruthMerit features</td><td>Ideal candidate</td></tr><tr><td colspan="2">ideal candidate: independent and lowest parent financial variables</td><td colspan="2">ideal candidate: highest merit variables</td></tr></table>

Table 6

height histogram with at most 10 ranges. A smaller number of ranges were used for highly skewed numeric attributes. After randomly selecting an adjacent cell of the equal height histogram, a value was randomly selected between the end points of the cell.

## 4.2. Application Deception Model

The Application Deception Model (ADM) involves scenario analysis, feature grouping, and data perturbation as depicted in Fig. 2. The starting point of the model is the analysis of deception scenarios. Each scenario is de<sup>fi</sup>ned by conditions and corresponding actions. It is possible that some scenarios have identical conditions, but different actions. In this case, they are combined into one scenario for ease of data generation.

After speci<sup>fi</sup>cation of scenarios, the next step involves classi<sup>fi</sup>cation of features based on the scenarios. These features are changed together during the perturbation process. Unlike typical noise models, the ADM supports dependencies by grouping attributes.

Independence is a strong assumption that has been shown to be false even in processes in which individuals work independently. For example, Knight and Levenson [20] demonstrated that independence does not hold for testing reliability of N version software development as programmers tend to make the same mistakes even when working independently. The lessons from independent software development cast doubt even on the usage of independence in random noise models. For deception generation models, independence is not reasonable as individuals tend to change related items to move closer to a deception goal. For example, <sup>fi</sup>nancial aid applicants can avoid detection by changing a number of components of adjusted gross income in smaller amounts as opposed to changing just one component in a larger amount. In mortgage applications, applicants can avoid detection by changing both assets and income [11] to make them appear consistent.

The data selection step chooses observations with potential for deceptive action. In this study, we used a simple distance threshold because deception rewards increase with improvements in an applicant's level of need. Observations are selected for possible perturbation if the distances from the ideal candidate are more than the speci<sup>fi</sup>ed distance determined by the distance threshold. The distance threshold is speci<sup>fi</sup>ed as a percentile ranking of distances to the ideal candidate.

The data selection step can be customized, providing support for other areas with different rewards for deceptive behavior. For areas with equal reward for all successful applicants, a radius parameter around a marginal candidate may be more appropriate. For example, the U.S. Medicaid program has a uniform minimum bene<sup>fi</sup>t structure consistent with a data selection function using a radius parameter centered near a marginal candidate. Other data selection functions can be used for different reward structures such as non-linear rewards. For additional customization, the deception rate can be set for each scenario. Customization provides more <sup>fl</sup>exibility in generating deceptive patterns but involves more effort to model deceptive patterns.

In the perturbation procedure, the actual values of each attribute in a deception scenario are randomly perturbed between the threshold and extreme value. The threshold and extreme values (either maximum or minimum) must be speci<sup>fi</sup>ed for each attribute in a deception scenario.

Table 4  
Data perturbation for deception scenarios in <sup>fi</sup>nancial aid application.

<table><tr><td>Subset 1</td><td>Subset 2</td></tr><tr><td>Conditions: dependent and high parents financial variable</td><td>Conditions: low merit-based variables</td></tr><tr><td>Perturb: status to independent or reduce parent financial variables</td><td>Perturb: increase merit-based variables</td></tr></table>

Table 5  
Threshold and ideal values for parents' <sup>fi</sup>nancial variables.

<table><tr><td>Parents&#x27; financial variables</td><td>Threshold value</td><td>Ideal value</td></tr><tr><td>Parents&#x27; earned income</td><td>$100,000</td><td>$0</td></tr><tr><td>Parents&#x27; investment income</td><td>$100,000</td><td>$0</td></tr><tr><td>Parents&#x27; total balance</td><td>$100,000</td><td>$0</td></tr><tr><td>Parents&#x27; net worth of real estate</td><td>$100,000</td><td>$0</td></tr></table>

A formal description of the procedure for generating arti<sup>fi</sup>cial deception in the application-based context follows with the list of variables and data generation algorithm.

• TV: set of threshold values, one threshold value for each attribute,

• EV: set of extreme values, one extreme value for each attribute

• FG: set of feature groups (each feature group is a set of attributes manipulated together).

```txt
Input
O(x, n): original dataset where x denotes the number of observations and n denotes the number of attributes
p: percentile threshold for determining candidate deceptive set
c: deception rate
Output
DS: deceptive set of instances whose feature values have been changed
Procedure
1. Let DS = O // Initialization
2. For each feature set f ∈ FG
3.    For each case i ∈ DSf do // DSf is the part of DS that only contains feature set f
4.    Compute distance di from the ideal candidate using feature set f
5.    End For
6. Sort(di, d2, ..., dc) // Sort in descending order
7. For each case t ∈ Top p of DSf by di do // Perturb top p percent of cases
8.    Let r be a random number in [0, 1]
9.    If r ≤ c then
10.    For all features do
11.    // Use EV and TV sets for current feature
12.    randomly choose a value v between extreme and threshold values
13.    Set feature value to v
14.    End For
15.    End If
16.    End For
17. End For
```

For additional <sup>fl</sup>exibility, the deception rate (d) and deceptive candidate threshold (p) could be speci<sup>fi</sup>ed for each feature group. Specifying different values by feature group requires more background about the domain, however.

## 4.3. Application to the financial aid application

To clarify the ADM, it is applied to the <sup>fi</sup>nancial aid application. The <sup>fi</sup>rst step of the ADM involves scenario analysis. Based on discussions with decision makers in the University of Colorado <sup>fi</sup>nancial aid of<sup>fi</sup>ce, three scenarios cover most deceptive behaviors. Students falsify their applications to appear eligible for <sup>fi</sup>nancial aid. In Scenario 1, students change their status from dependent to independent to qualify for <sup>fi</sup>nancial aid if their parents' <sup>fi</sup>nancial condition is strong. In scenario 2, students reduce their parents' <sup>fi</sup>nancial variables to qualify rather than change their status. Scenarios 1 and 2 have the same conditions, but different actions. Therefore, they are combined into one scenario. Scenario 3 involves in<sup>fl</sup>ating merit-based features to make a candidate appear more quali<sup>fi</sup>ed. Scenario 3 is similar to resume padding performed by job applicants. After the combination of the original Scenario 1 and 2, two <sup>fi</sup>nal scenarios that are applied in this study are summarized in Table 1.

Threshold and ideal values for merit-based variables.

<table><tr><td>Merit variables</td><td>Threshold value</td><td>Ideal value</td></tr><tr><td>Cumulative GPA</td><td>3.0</td><td>4.0</td></tr><tr><td>GPA from the most recent semester</td><td>3.0</td><td>4.0</td></tr><tr><td>GPA from the semester prior to the most recent semester</td><td>3.0</td><td>4.0</td></tr><tr><td>Previous award (counts)</td><td>0</td><td>2</td></tr><tr><td>Employment (counts)</td><td>1</td><td>2</td></tr><tr><td>Management experience (counts)</td><td>1</td><td>2</td></tr><tr><td>Activity (counts)</td><td>1</td><td>2</td></tr><tr><td>Leadership experience (counts)</td><td>1</td><td>2</td></tr></table>

Table 8  
![](/api/attachments/3QZZ2BAN/fulltext/images/a17196fd127c8339d90f655aeb4005891d1c07724f3b1dc41e81bd0bd9f55190.jpg)  
Fig. 3. Percent of critical <sup>fi</sup>elds experiencing change.

Based on the speci<sup>fi</sup>ed scenarios as described in the table above, the features are classi<sup>fi</sup>ed into three groups: status variables, <sup>fi</sup>nancial variables, and merit-based variables. Table 2 lists the features included in each group.

Status variables indicate the condition of either an independent student or a dependent student. Determining the status as dependent or independent from their parents is one common factor involved in all federal and state <sup>fi</sup>nancial aid applications. The status is determined on the basis of the information provided on the application. Students are considered to be independent if they are at least 24 years old or married. Otherwise, they are considered dependent on their parents.

## 4.3.1. Data selection

Based on two scenarios, the subsets of data that are eligible for perturbation are selected using the method depicted in Table 3. To select data for each subset, the distances from each observation in the truth dataset to the ideal candidate are computed using the features corresponding to the variables in each group. Based on the percentile threshold, the observations are selected to form the subset.

## 4.3.2. Data perturbation

Once the feature subsets are selected, the perturbation process can occur. The method of data perturbation for each scenario is described in Table 4.

4.3.2.1 . Scenario 1. This scenario considers the deceptive actions on status or <sup>fi</sup>nancial variables that applicants may take to strengthen their need of <sup>fi</sup>nancial aid when they have dependent status and their parents' <sup>fi</sup>nancial status is good. Under these conditions, <sup>fi</sup>nancial variables and status variables are manipulated. For each individual selected in the subset, a random number between 0 and 1 is drawn for each group of variables. If the number is less than or equal to the deception rate assigned for the group of status variables, the status is changed to independent. If the number is less than or equal to the deception probability assigned for the group of <sup>fi</sup>nancial variables, the original state for each variable in this group is changed by randomly picking a value between the threshold and ideal value. The thresholds are determined according to the guidelines from the federal form. Table 5 shows the threshold and ideal values for parents' <sup>fi</sup>nancial variables.

Table 7  
Experimental comparisons between real and arti<sup>fi</sup>cial deception

<table><tr><td rowspan="2">Experiment</td><td colspan="2">Deception type</td></tr><tr><td>Real</td><td>Artificial</td></tr><tr><td>Experiment 1a (150)</td><td>Natural</td><td>VariableLow</td></tr><tr><td>Experiment 1b (150)</td><td>Natural</td><td>ADMLow</td></tr><tr><td>Experiment 2a (150)</td><td>Boosted</td><td>VariableHigh</td></tr><tr><td>Experiment 2b (150)</td><td>Boosted</td><td>ADMHigh</td></tr></table>

4.3.2.2 . Scenario 2. This scenario focuses on the merit-based variables. For each individual selected in the subset, a random number between 0 and 1 is drawn for the group of merit-based variables. If the number is less than or equal to the deception rate, the original value for each variable in this group is randomly perturbed to the level between the threshold and ideal value for each attribute. The threshold and ideal values for the merit-based variables are listed in Table 6. As shown in the table, some features are interpreted using counts from their original text-based values for data analysis.

## 4.3.3. Data selection

For additional insight about the data perturbation process, Fig. 3 compares the changes among critical <sup>fi</sup>elds in each data set. Each <sup>fi</sup>eld shows a reasonable correspondence between the percentages of changed <sup>fi</sup>elds for the natural and ADM (low deception rate) data sets and the boosted (a random mix of 20% boosted and 80% truth) and $\mathsf { A D M } _ { \mathrm { H } }$ (high deception rate) data sets. The changes for all <sup>fi</sup>elds re<sup>fl</sup>ect the same direction, closer to the goal.

## 5. Research design and methodology

## 5.1. Research model and hypotheses

The research model involves the proposed relationships between real deception and data generation models for noise and deception presented in the previous section. The real deceptive data were collected for a student <sup>fi</sup>nancial aid application with two levels of treatments: natural and boosted deception. The arti<sup>fi</sup>cial data were generated using a data generation model (noise or deception) to change feature values according to speci<sup>fi</sup>ed change parameters. The parameters for the data generation models were consistent with deception levels in the real deceptive data set. To be consistent with the different amounts of deception involved in the natural and boosted deception data sets, the arti<sup>fi</sup>cial data sets were generated using two perturbation levels: low and high. The low perturbation rate is compared with natural deception, while high rate is compared with boosted deception.

The sign for directed distance

<table><tr><td>Value comparison</td><td>Ideal goal of deception</td><td>Sign (s)</td></tr><tr><td> $Value_{deception}>Value_{truth}$ </td><td>Maximize the value</td><td>s=1</td></tr><tr><td> $Value_{deception}>Value_{truth}$ </td><td>Minimize the value</td><td>s=-1</td></tr><tr><td>\( Value_{deception}Maximize the values=-1</td><td>Maximize the value</td><td>s=-1</td></tr><tr><td>\( Value_{deception}Minimize the values=1</td><td>Minimize the value</td><td>s=1</td></tr></table>

Table 9  
Hypotheses based on directed distance measure and outlier score measure.

<table><tr><td>Model hypothesis</td><td>Null hypothesis</td><td>Alternative hypothesis</td></tr><tr><td>H1a</td><td> $\mu_{distance(natural)} = \mu_{distance(VariableLow)}$ </td><td> $\mu_{distance(natural)} \neq \mu_{distance(VariableLow)}$ </td></tr><tr><td>H1b</td><td> $\mu_{distance(natural)} = \mu_{distance(ADMLow)}$ </td><td> $\mu_{distance(natural)} \neq \mu_{distance(ApplicationLow)}$ </td></tr><tr><td>H2a</td><td> $\mu_{distance(boosted)} = \mu_{distance(VariableHigh)}$ </td><td> $\mu_{distance(boosted)} \neq \mu_{distance(VariableHigh)}$ </td></tr><tr><td>H2b</td><td> $\mu_{distance(boosted)} = \mu_{distance(ADMHigh)}$ </td><td> $\mu_{distance(boosted)} \neq \mu_{distance(ADMHigh)}$ </td></tr><tr><td>H1a</td><td> $\mu_{outlier(natural)} = \mu_{outlier(VariableLow)}$ </td><td> $\mu_{outlier(natural)} \neq \mu_{outlier(VariableLow)}$ </td></tr><tr><td>H1b</td><td> $\mu_{outlier(natural)} = \mu_{outlier(ADMLow)}$ </td><td> $\mu_{outlier(natural)} \neq \mu_{outlier(ADMLow)}$ </td></tr><tr><td>H2a</td><td> $\mu_{outlier(boosted)} = \mu_{outlier(VariableHigh)}$ </td><td> $\mu_{outlier(boosted)} \neq \mu_{outlier(VariableHigh)}$ </td></tr><tr><td>H2b</td><td> $\mu_{outlier(boosted)} = \mu_{outlier(ADMHigh)}$ </td><td> $\mu_{outlier(boosted)} \neq \mu_{outlier(ADMHigh)}$ </td></tr></table>

Table 11

We expected the two data generation models to have different relationships to real deception. To simulate deception, data should be perturbed purposefully. The ADM proposed in this study simulates deceptive actions by manipulating groups of features based on scenarios of deceptive behavior. In this data generation model, perturbations will be on one side: to make an applicant appear stronger. Thus, it is predicted that the pattern of real deception matches the deception pattern in the arti<sup>fi</sup>cial data set modeled by deception.

In contrast, noise models generate non-systematic errors by corrupting the original feature values randomly without considering simulating actions. The Variable Noise Model [13] adopted here applies the noise rate to each feature randomly and independently. Variable noise should not make an observation move to a deception goal because perturbations from the truth are symmetric with a mean level of perturbation near zero. Therefore, the data generation pattern modeled by variable noise should not <sup>fi</sup>t the real deception pattern since deception involves systematic perturbations to a goal.

Based on the analysis, four hypotheses were identi<sup>fi</sup>ed, the <sup>fi</sup>rst two dealing with the relationship between natural and arti<sup>fi</sup>cial data generated using a low perturbation level, and the other two focusing on comparing boosted and arti<sup>fi</sup>cial data generated using a high perturbation level. The hypotheses are based on the differences between deception and noise. Noise is symmetric change from the truth without a goal direction. Deception (real or arti<sup>fi</sup>cial) is change

Summary of statistical test results based on distance measure.

(The numbers in parentheses are the p-values and effect sizes.)

<table><tr><td>Comparison</td><td>Significance and effect</td></tr><tr><td>Natural vs. VariableLow</td><td>Significant (0.000*, 0.30)</td></tr><tr><td>Natural vs. ADMLow</td><td>Not significant (0.282)</td></tr><tr><td>Boosted vs. VariableHigh</td><td>Significant (0.000*, 0.74)</td></tr><tr><td>Boosted vs. ADMHigh</td><td>Not significant (0.127)</td></tr></table>

水 Signi<sup>fi</sup>cant at the 0.05 level.

from the truth directed toward a goal. Thus, it is expected that variable noise will be different than real deception but arti<sup>fi</sup>cial deception will be similar to real deception. Effectively, the noise model serves as a control group to demonstrate that differences between the ADM and deception data sets are substantially more than unbiased noise.

## 5.1.1 . Natural deception versus data generation models

H1a. There will be a detectable difference between natural deception and arti<sup>fi</sup>cial deception generated by the Variable Noise Model at low rates.

H1b. There will be no detectable difference between natural deception and arti<sup>fi</sup>cial deception generated by the ADM at low rates.

## 5.1.2 . Boosted deception versus data generation models

H2a. There will be a detectable difference between boosted deception and arti<sup>fi</sup>cial deception generated by the Variable Noise Model at high rates.

H2b. There will be no detectable difference between boosted deception and arti<sup>fi</sup>cial deception generated by the ADM at high rates.

## 5.2. Experimental methodology

The relationships between real deception and data generation models for noise and deception were analyzed in two experiments. The <sup>fi</sup>rst experiment involved the relationships between data generation models and natural deception, while the second experiment involved the relationships between data generation models and boosted deception. Each experiment involved two comparisons between the real deceptive data and the data perturbed by a data generation model (noise or deception) with corresponding parameters as shown in Table 7. Because of the nature of boosted deception, each case in the original boosted deception data set contains false information. Based on the reported percentage of deception in <sup>fi</sup>nancial aid [26], the boosted deception data set applied in the experiments was generated by mixing 20% of cases with boosted deception and 80% of cases with truth. Perturbation rates consistent with the deception levels in the real deception data sets were used: 0.05 for the low perturbation rate and 0.20 for the high perturbation rate. The high perturbation rate is the same as the percentage of boosted deception in the real boosted deception data set.

Table 10  
Hypothesis testing results for the directed distance measure.

<table><tr><td></td><td>VariableLow-Natural</td><td>ADMLow-Natural</td><td>VariableHigh-Boosted</td><td>ADMHigh-Boosted</td></tr><tr><td>Mean</td><td>0.307</td><td>0.127</td><td>0.447</td><td>0.045</td></tr><tr><td>Std. deviation</td><td>.958</td><td>1.616</td><td>1.981</td><td>1.385</td></tr><tr><td>95% confidence interval</td><td>(0.152, 0.462)</td><td>(-0.133, 0.388)</td><td>(0.129, 0.768)</td><td>(-0.178, 0.268)</td></tr><tr><td>Z</td><td>-3.724</td><td>-1.076</td><td>-9.052</td><td>-1.528</td></tr><tr><td>Asymp. sig. (2-tailed)</td><td>0.000</td><td>0.282</td><td>0.000</td><td>0.127</td></tr></table>

Table 12  
Summary of statistical test results for the D<sub>n</sub><sup>k</sup> outlier score measure.

<table><tr><td rowspan="2">Comparison</td><td colspan="6">Outlier score ( $D_n^k$ )</td></tr><tr><td>Mean</td><td>Std</td><td>95% conf. int.</td><td>t-value</td><td>Sig.</td><td>Effect size</td></tr><tr><td>Natural vs. VariableLow</td><td>-.034</td><td>.223</td><td>(-0.069, 0.002)</td><td>-1.870</td><td>.064</td><td>N/A</td></tr><tr><td>Natural vs. ADMLow</td><td>.010</td><td>.191</td><td>(-0.020, 0.041)</td><td>.692</td><td>.490</td><td>N/A</td></tr><tr><td>Boosted vs. VariableHigh</td><td>-.084</td><td>.211</td><td>(-0.117, -0.049)</td><td>-4.860</td><td> $.000^*$ </td><td>0.80</td></tr><tr><td>Boosted vs. ADMHigh</td><td>.016</td><td>.214</td><td>(-0.018, 0.051)</td><td>.946</td><td>.346</td><td>N/A</td></tr></table>

\* Signi<sup>fi</sup>cant at the 0.05 level.

To determine the sample size before the data was collected, the traditional values for type I error $( \propto = 0 . 0 5 )$ and power (0.80) were used. A sample size of 150 (as noted in Table 7) is suf<sup>fi</sup>cient to detect an effect size of 0.2. According to Cohen [9], an effect size of 0.2 is between a small effect size (0.1) and medium effect size (0.3).

## 5.3. Measures

## 5.3.1. Directed distance measure

To measure the <sup>fi</sup>t between real and arti<sup>fi</sup>cial deception, we compared the distances from the truth to both data generation models. Standard distance measures only involve the amount of change because they are symmetric. Symmetric distance does not differentiate between changes toward a goal (deception) and changes not directed toward a goal (noise). Because both the direction and magnitude of change are important, directed distance should be measured. As a similarity measure, directed distance has been used for object matching in images [28] and graph partitioning problems [8].

The directed distance measure contains a sign indicating a positive or negative change. In this study, the sign of the directed distance was determined based on the distance from the ideal candidate as shown in Table 8. Each attribute has an extreme value indicating the ideal candidate. If the deceptive value is closer to the ideal candidate than the truth, the directed distance is positive. If the deceptive value is farther from the ideal candidate than the truth, the directed distance is negative.

To handle applications with both numeric and non-numeric attributes, a heterogeneous distance function that uses different attribute distance functions was used. This study used the overlap metric for nominal attributes and normalized distance for linear attributes [32]. The heterogeneous distance function de<sup>fi</sup>nes the distance between two values x and y of a given attribute as:

$$
d _ {a} (x, y) = \left\{ \begin{array}{l} 1, \text {   if   } x \text {   or   } y \text {   is   unknown,   else } \\ \text { overlap } (x, y), \text {   if   } a \text {   is   nominal,   else. } \\ r n \_ d i f f _ {a} (x, y) \end{array} \right.\tag{1}
$$

The function overlap and the range-normalized difference rn\_diff are de<sup>fi</sup>ned as:

$$
\operatorname{overlap} (x, y) = \left\{ \begin{array}{l} 0, \text { if } x = y \\ 1, \text { otherwise } \end{array} \right.\tag{2}
$$

$$
r n _ {d i f f a} (x, y) = \frac {| x - y |}{\text { range } _ {a}}.\tag{3}
$$

The value range is used to normalize the attributes, and is de<sup>fi</sup>ned as the difference between maximum and minimum values. The overall directed distance between two input vectors x and y is given in Eq. (4) by the Heterogeneous Directed Distance function in which s is de<sup>fi</sup>ned in Table 8.

$$
\mathrm{HDD} (x, y) = \sum_ {a = 1} ^ {\mathrm{m}} \mathrm{d} _ {a} (x _ {a}, y _ {a}) s\tag{4}
$$

## 5.3.2. Outlier score measures

In addition to comparing the data sets on mean directed distances, dispersion of observations was a secondary comparison in the experiments. Noise should have more dispersion than deception because noise is symmetric and deception is directed. Deception should tend to increase the density of the observations toward the goal.

Since there is no accepted dispersion measure for data sets with variables of mixed scales, outlier scores were used. Traditionally, an outlier score is a measure of unusualness. An outlier score can also be considered as a multivariate measure of dispersion of an observation relative to other observations as suggested by Hellerstein [16]. In the experiments, the relationship between real and generated deception was measured by comparing the average outlier scores.

We used two non-parametric outlier detection algorithms, both based on the distance from the kth nearest neighbor. In the $D _ { n } ^ { k }$ algorithm [25], outliers are the top n instances with the largest distance to their kth nearest neighbor. These outliers are referred as the $D _ { n } ^ { k }$ outliers of a dataset. The density-based algorithm [5] uses the Local Outlier Factor (LOF) that measures the degree of an object as an outlier with respect to the density of its local neighborhood. The outlier score in the LOF approach is an adjusted k nearest neighbor score. The choice of k should be made relative to the size of the data set.

## 6. Analysis of results

## 6.1. Evaluation of model

The relationships between real deception and arti<sup>fi</sup>cial deception were evaluated by paired tests of group means, with α of 0.05 and N of 150. If the result is not statistically signi<sup>fi</sup>cant at the chosen α, the null hypothesis of no difference in means between two groups cannot be rejected. If the difference is statistically signi<sup>fi</sup>cant, an effect size should be examined to see if the difference is also practically signi<sup>fi</sup>cant. A statistically signi<sup>fi</sup>cant outcome only indicates that it is likely that there is a difference between group means. It does not mean that the difference is large or important. In this study, the effect sizes are computed using the Hedge's g measure [15]. Cohen [9] provides the following guidelines of effect size (r): small effect size, r = 0.1; medium, r = 0.3; large, r = 0.5.

Table 13  
Summary of statistical test results for the LOF outlier score measure.

<table><tr><td rowspan="2">Comparison</td><td colspan="6">Outlier score (LOF)</td></tr><tr><td>Mean</td><td>Std</td><td>95% conf. int.</td><td>t-value</td><td>Sig.</td><td>Effect size</td></tr><tr><td>Natural vs. VariableLow</td><td>.024</td><td>.099</td><td>(0.008, 0.040)</td><td>2.926</td><td>.004*</td><td>0.48</td></tr><tr><td>Natural vs. ADMLow</td><td>-.002</td><td>.088</td><td>(-0.016, 0.012)</td><td>-.282</td><td>.778</td><td>N/A</td></tr><tr><td>Boosted vs. VariableHigh</td><td>.026</td><td>.099</td><td>(0.010, 0.043)</td><td>3.240</td><td>.001*</td><td>0.53</td></tr><tr><td>Boosted vs. ADMHigh</td><td>-.000</td><td>.074</td><td>(-0.012, 0.011)</td><td>-.066</td><td>.948</td><td>N/A</td></tr></table>

Signi<sup>fi</sup>cant at the 0.05 level.

Summary of explanatory power of regression models.

<table><tr><td>Model</td><td>R</td><td>R square</td><td>Adjusted R square</td><td>Std. error of estimate</td></tr><tr><td>ADM</td><td>0.995</td><td>0.990</td><td>0.990</td><td>0.013</td></tr><tr><td>Boosted</td><td>0.994</td><td>0.989</td><td>0.989</td><td>0.013</td></tr><tr><td>Variable</td><td>0.645</td><td>0.416</td><td>0.401</td><td>0.006</td></tr></table>

For easy interpretation, the hypotheses proposed in Section 5 are restated with the null hypothesis and alternative hypothesis based on the directed distance measure and the outlier score measure as shown in Table 9. The mean of directed distances from the true data to the deception data is denoted by: μ<sub>distance(deception type)</sub> and the mean of the outlier score in the deception data set is denoted by: μ<sub>outlier(deception type)</sub>, where deception type indicates real (natural or boosted) or arti<sup>fi</sup>cial (VariableLow, VariableHigh, ADMLow or ADMHigh) deception.

For the hypotheses involving ADM-generated deception (H1b and H2b), the statistical testing framework involves additional analysis if the null hypothesis is not rejected. The model hypotheses indicate that no detectable difference will be found. Because inability to reject a null hypothesis is not evidence of a non-effect, additional analysis with con<sup>fi</sup>dence intervals was used to demonstrate the magnitude of the differences.

Table 10 shows the SPSS output for testing the mean distance differences between the real and arti<sup>fi</sup>cial deception data. Table 11 summarizes the results and lists the p-values and the effect sizes for the signi<sup>fi</sup>cant results. The results provide strong evidence that variable noise differs from deception, both natural and boosted. Furthermore, the effect sizes of 0.30 (moderate) and 0.74 (large) suggest that both statistically signi<sup>fi</sup>cant results are practically signi<sup>fi</sup>cant. The results, as expected, do not allow rejection of the null hypotheses for comparisons of ADM and real deception (H1b and H2b). The con<sup>fi</sup>dence intervals pass through 0 although they are somewhat larger on the positive side. Using both the mean values and con<sup>fi</sup>dence intervals from Table 10, the differences between ADM and real deception appear much smaller than differences between variable noise and real deception.

Tables 12 and 13 show the results of the average mean of the outlier score based on two outlier detection algorithms. The results provide strong evidence about the differences between variable noise and real deception on outlier scores as outcome variables. Three of the four null hypotheses were rejected with small p values. In addition, the large effect sizes (0.48, 0.53, and 0.80) suggest that all statistically signi<sup>fi</sup>cant results are practically signi<sup>fi</sup>cant. The variable-low hypothesis (H1a) involving the $\smash { \mathsf { D } _ { \mathrm { n } } ^ { \mathrm { k } } }$ outlier score was not rejected although its p value is close to the traditional 0.05 rejection limit. The results did not allow rejection of the null hypotheses (H1b and H2b) for the ADM generated deception. The con<sup>fi</sup>dence intervals for the non-rejected null hypotheses suggest that the differences between ADM and real deception are small. The con<sup>fi</sup>dence intervals are reasonably symmetric with small ranges compared to the con<sup>fi</sup>dence intervals for variable noise.

Additional evidence about data generation patterns was obtained by <sup>fi</sup>tting linear models with perturbation rate (deception or noise rate) as the predictor variable and average directed distance as the outcome variable. The models were derived from simulations of 100 observations in which the perturbation rate was randomly selected in the range of 0.10 to 0.40. Each observation is the average directed distance over all data set observations between the data generation method (ADM or variable noise) using the noise/deception rate and the truth data set. For boosted deception, the deception rate is the rate of deceptive cases randomly selected from the boosted deception data set.

The results in Tables 14 and 15 provide strong evidence of a linear relationship for all three models (ADM, Variable, and Boosted). However, the Variable model explains a relatively small amount of variance (Adjusted $R ^ { 2 }$ of 0.401) so its explanatory power seems weak especially for a simulation result. In contrast, the explanatory power of the ADM and Boosted models are strong with very large Adjusted $R ^ { 2 }$ values (0.990 and 0.980, respectively). The model coef<sup>fi</sup>cients in Table 15 indicate similar slopes and intercepts for the ADM and Boosted models (1.45 and 1.326 respectively for the slopes and −0.012 and 0.021 respectively for the intercepts) but a much smaller slope and much larger intercept for the Variable model (0.061 for the slope and 0.699 for the intercept). The graphs in Fig. 4 corroborate the regression results showing a close correspondence between ADM and boosted deception and a sharp divergence between variable noise and the other models. The scale in Fig. 4 somewhat obscures the scatter among the variable noise observations.

## 6.2. Discussion

The hypothesis testing results for two measures are summarized in Table 16. These results provide preliminary evidence that arti<sup>fi</sup>cially generated deception could augment real deception. However, the deception generation model must be selected carefully. Data generation models that perturb the original state without considering deceptive behavior are not appropriate. The proposed Application Deception Model contains three elements for simulating deception: deception scenarios supporting conditions and dependencies among attributes, a parameter to characterize potential to deceive, and a deception rate parameter. The experimental results con<sup>fi</sup>rm the importance of these elements to simulate deception in the <sup>fi</sup>nancial aid area.

This study is just a <sup>fi</sup>rst step to understand the relationship between arti<sup>fi</sup>cial and real deception. This study focused on the data generation model and a comparison of the difference between arti<sup>fi</sup>cial and real deception. A second investigation by the authors [33] studies the impact of arti<sup>fi</sup>cial deception on the screening policies for <sup>fi</sup>nancial aid applications. The results of the second study provide additional evidence that arti<sup>fi</sup>cial deception can be used to augment real deception.

Summary of coef<sup>fi</sup>cients of regression models.

<table><tr><td>Model</td><td>Component</td><td>Coefficient (B)</td><td>Coefficient (std. error)</td><td>t</td><td>Sig.</td></tr><tr><td rowspan="2">ADM</td><td>Constant</td><td>-0.012</td><td>0.006</td><td>-2.053</td><td>0.046</td></tr><tr><td>Deception</td><td>1.450</td><td>0.022</td><td>64.965</td><td>0.000</td></tr><tr><td rowspan="2">Boosted</td><td>Constant</td><td>0.021</td><td>0.006</td><td>3.743</td><td>0.001</td></tr><tr><td>Deception</td><td>1.326</td><td>0.022</td><td>61.328</td><td>0.000</td></tr><tr><td rowspan="2">Variable</td><td>Constant</td><td>0.699</td><td>0.003</td><td>227.526</td><td>0.000</td></tr><tr><td>Noise</td><td>0.061</td><td>0.011</td><td>5.335</td><td>0.000</td></tr></table>

![](/api/attachments/3QZZ2BAN/fulltext/images/3a1ce0d6d3d1698b7ca779f98899c217a1052ff18247ec9f88c78e1804f6a00c.jpg)

Summary of <sup>fi</sup>ndings.

<table><tr><td>Hypothesis</td><td>Findings</td></tr><tr><td>H1a: Significant difference between natural deception and low variable noise</td><td>Support: Statistically significant differences in directed distances and LOF outlier scores with moderate effect size.Exception: Marginal significance indicates some evidence but not conclusive evidence of a difference in  $D_{n}^{k}$  outlier scores.</td></tr><tr><td>H1b: No difference detected between natural deception and low ADM deception</td><td>Support: No difference detected by hypothesis tests for directed distance and outlier scores. Small and reasonably symmetric confidence intervals.</td></tr><tr><td>H2a: Significant difference between boosted deception high variable noise</td><td>Support: Statistically significant differences in directed distances and outlier scores with large effect size. Simulation with varying perturbation rates shows dissimilar patterns of directed distances for variable noise and boosted deception.</td></tr><tr><td>H2b: No difference detected between boosted deception and high ADM deception</td><td>Support: No difference detected by hypothesis tests for directed distance and outlier scores. Small and reasonably symmetric confidence intervals; Simulation with varying deception rates shows similar patterns of directed distances for ADM and boosted deception.</td></tr></table>

Even with the second study, more work remains for practical application of arti<sup>fi</sup>cial deception generation in the <sup>fi</sup>nancial aid area. Both studies were limited by the data collection procedure partially imposed by the internal review board. Answers on the second and third forms (truth and boosted deception) could be subtly impacted by subjects <sup>fi</sup>rst providing natural deception. To overcome this limitation, the ADM should be applied to data from a <sup>fi</sup>nancial aid of<sup>fi</sup>ce for a more detailed evaluation. This evaluation must consider both errors and deception so the ADM will require extensions to deal with errors and deception. The goal of practical application should be more modest than replacing current practices at student <sup>fi</sup>nancial aid of<sup>fi</sup>ces. Arti<sup>fi</sup>cial data generation may be used to reduce the frequency of compliance checking so that a larger number of screening policies can be evaluated.

## 7. Conclusion

The relationships between real deception and arti<sup>fi</sup>cial deception generated by data generation models were systematically analyzed. Speci<sup>fi</sup>cally, the study investigated the quality of <sup>fi</sup>t between collected deception data and arti<sup>fi</sup>cially generated deception. The data collection procedure provided a unique data set of student <sup>fi</sup>nancial aid applications containing truth, natural deception, and boosted deception. The Application Deception Model, a new data generation model, was developed to generate arti<sup>fi</sup>cial deception. The proposed model considers the generation of the arti<sup>fi</sup>cial deception in different application-based deception contexts. We designed an innovative experimental study to investigate the feasibility of using a data generation model to simulate real deception. The experiment involved comparisons of real and arti<sup>fi</sup>cial deception with directed distance and outlier score as outcome variables. Our results provided preliminary evidence that the arti<sup>fi</sup>cially generated deception could augment real deceptive data to reduce the costs associated with obtaining data for the data mining applications.

This study with an emphasis on internal validity has limitations on conclusions in a wide variety of domains. Further studies concerning different types of document-centric deception would provide additional external validity to complement this study. Another extension of this study is to simulate real data using a model that can generate correct data, noise, and deception. Complete data generation eliminates the need to correct a base data set. To con<sup>fi</sup>rm the evidence in this study, a future study should use data from a <sup>fi</sup>nancial aid of<sup>fi</sup>ce with falsi<sup>fi</sup>ed data noted from actual audits.

## References

[1] D. Angluin, P. Laird, Learning from noisy examples, Machine Learning 2 (4) (1988) 343–370.

[2] E. Barse, H. Kvarnstrom, E. Jonsson, Synthesizing test data for fraud detection systems, Proceedings of the 19th Annual Computer Security Applications Conference, 2003, pp. 384–395

[3] F. Bonchi, F. Giannotti, G. Mainetto, D. Pedreschi, A classi<sup>fi</sup>cation-based methodology for planning auditing strategies in fraud detection, Proceedings of SIGKDD99, San Diego, 1999, pp. 175–184.

[4] C. Bond, B. DePaulo, Accuracy of deception judgments, Personality and Social Psychology Review 10 (2006) 214–234.

[5] M.M. Breunig, H.P. Kriegel, R.T. Ng, LOF: identifying density-based local outliers, Proceedings of ACM Conference, 2000, pp. 93–104.

[6] J. Burgoon, J. Blair, T. Qin, J. Nunamaker, Detecting deception through linguistic analysis, Proceedings of the First NSF/NIJ Symposium on Intelligence and Security Informatics, Springer Verlag, 2003, pp. 91–101, Tucson, AZ.

[7] J.K. Burgoon, J.P. Blair, R. Strom, Heuristics and modalities in determining truth versus deception, Proceedings of Thirty-Eighth Hawaii International Conference on System Sciences, IEEE, 2005, Big Island, HI.

[8] M. Charikar, K. Makarychev, Y. Makarychev, Directed metrics and directed graph partitioning problems, Proceedings of the 17th Annual ACM-SIAM Symposium on Discrete Algorithms, 2006, pp. 51–60.

[9] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, 2nd ed. Academic Press, New York, 1988.

[10] CoreLogic, Inc., 2011 Mortgage Fraud Trends Report, http://www.corelogic.com/ about-us/researchtrends/asset\_upload\_<sup>fi</sup>le371\_12432.pdf2011.

[11] Fannie Mae, Mortgage Fraud Overview, https://www.efanniemae.com/utility legal/pdf/mtgfraudoverview.pdf2007.

[12] J. George, K. Marett, P. Tilley, Deception detection under varying electronic media and warning conditions, Proceedings of Thirty-Seventh Hawaii International Conference on System Sciences, IEEE, 2004, Hawaii.

[13] S. Goldman, R. Stone, Can PAC algorithms tolerate random attribute noise? Algorithimica 14 (1995) 70–84.

[14] J. Haines, J. Lippmann, R. Fried, M. Zissman, E. Tran, S. Boswell, 1999 DARPA Intrusion Detection Evaluation: Design and Procedures, MIT Lincoln Laboratory, Lexington, MA, 2001.

[15] L. Hedges, Distribution theory for Glass's estimator of effect size and related estimators Journal of Educational Statistics 6 (2) (1981) 107–192

[16] J. Hellerstein, “Quantitative Data Cleaning for Large Databases,” White Paper, United Nations Economic Commission for Europe, http://db.cs.berkeley.edu/jmh papers/cleaning-unece.pdf2008.

[17] irs.gov, “IRS Releases 2006 Tax Gap Estimates,” FS-2012-6, January 2012, http:// www.irs.gov/newsroom/article/0,id=252094,00.html2012.

[18] Z. Jiang, V. Mookerjee, S. Sarkar, Lying on the web: implications for expert systems redesign, Information Systems Research 16 (2) (2005) 131–148.

[19] M. Kearns, M. Li, Learning in the presence of malicious errors, SIAM Journal on Computing 22 (4) (1993) 807–837.

[20] J. Knight, N. Levenson, An experimental evaluation of the assumption of independence of multi-version programming, IEEE Transactions on Software Engineering SE-12 (1) (January 1986) 96–109.

[21] J. Li, K. Huang, J. Jin, J. Sh, A survey on statistical methods for health care fraud detection, Health Care Management Science 11 (2007) 392–403

[22] M. Mannino, Y. Yang, Y. Ryu, Classi<sup>fi</sup>cation algorithm sensitivity to training data with non-representative attribute noise, Decision Support Systems 46 (2009) 743–751.

[23] M. Mannino, V. Mookerjee, R. Gilson, Improving the performance stability of inductive expert systems under input noise, Information Systems Research 6 (4) (December 1995) 328–356.

[24] C. Phua, V. Lee, K. Smith, R. Gayler, A Comprehensive Survey of Data Mining Based Fraud Detection, http://arxiv.org/ftp/arxiv/papers/1009/1009.6119.pdf2005.

[25] S. Ramaswamy, R. Rastogi, K. Shim, Ef<sup>fi</sup>cient algorithms for mining outliers from large data sets, Proceedings ACM Int. Conf. on Management of Data (SIGMOD'00), 2000, pp. 427–438.

[26] D. Rhodes, A. Tuccillo, Analysis of Quality Assurance Program Sample Data: 2006– 07 Retrieved from the website:, http://ifap.ed.gov/qadocs/ToolsforSchools/ 0607DataAnalysisReport.pdf2008.

[27] H. Shao, H. Zhao, G. Chang, Applying data mining to detect fraud behavior in customs declaration, Proceedings of 1st International Conference on Machine Learning and Cybernetics, November 2002, Beijing, 2002, pp. 1241–1244.

[28] D. Sim, O. Kwon, R. Park, Pyramidal robust hausdorff distance for object matching, Proceedings of IEEE International Conference on Image Processing (ICIP'99), 1999, pp. 88–92.

[29] D. Smith, Why We Lie: The Evolutionary Roots of Deception and the Unconscious Mind, St Martin's Press, 2004.

[30] C. Thang, P. Toan, E. Cooper, K. Kamei, Application of soft computing to tax fraud detection in small businesses, Proceedings of the First International Conference on Communications and Electronics (ICCE'06), 2006, pp. 402–407.

[31] D. Twitchell, K. Wiers, M. Adkins, J. Burgoon, J. Nunamaker, StrikeCOM: a multiplayer online strategy game for researching and teaching group dynamics, Proceedings of Thirty-Eighth Hawaii International Conference on System Sciences, 2005.

[32] R. Wilson, T. Martinez, Improved heterogeneous distance functions, Journal of Arti<sup>fi</sup>cial Intelligence Research 6 (1) (1997) 1–34.

[33] Yang, Y. and Mannino, M. (in press), “An Experimental Comparison of a Document Deception Detection Policy using Real and Arti<sup>fi</sup>cial Deception”, Journal of Data and Information Quality (TDIQ), ACM Digital Library, 2012.

[34] L. Zhou, D. Zhang, An exploratory study into deception detection in textbased computer-mediated communication, IEEE Transactions on Professional Communication 48 (2005) 291–400.

[35] L. Zhou, D. Twitchell, T. Qin, J. Burgoon, J. Nunamaker, An exploratory study into deception detection in text-based computer-mediated communication, Proceedings of Thirty-Sixth Hawaii International Conference on System Sciences, 2003.

[36] L. Zhou, J. Burgoon, D. Twitchell, T. Qin, J. Nunamaker, A comparison of classi<sup>fi</sup>cation methods for predicting deception in computer-mediated communication, Journal of Management Information Systems 20 (4) (2004) 139–165

[37] L. Zhou, Y. Shi, D. Zhang, A statistical language modeling approach to online deception detection, IEEE Transactions on Knowledge and Data Engineering 20 (8) (2008) 1077–1081.

[38] X. Zhu, X. Wu, Class noise vs. attribute noise: a quantitative study of their impacts, Arti<sup>fi</sup>cial Intelligence Review 22 (3) (2004) 177–210.

Yanjuan Yang received a Ph.D. from the Business School in the Computer Science and Information Systems program at the University of Colorado, Denver in 2009. She received her M.S. in Computer Science from the University of Bristol, and her B.S. in Management from North China University of Technology. Her current research interests include data mining, deception detection, and database systems.

Michael V. Mannino is an associate professor in the Business School of the University of Colorado Denver. Previously he was on the faculty at the University of Florida, University of Texas at Austin and University of Washington. He has been active in research about database management, knowledge representation, and organizational impacts of technology. He has published articles in major journals of the IEEE (Transactions on Knowledge and Data Engineering and Transactions on Software Engineering), ACM (Communications and Computing Surveys), and INFORMS (Informs Journal on Computing and Information Systems Research). His research includes several popular survey and tutorial articles as well as many papers describing original research. He is the author of the textbook, Database Design, Application Development, and Administration in its <sup>fi</sup>fth edition.
