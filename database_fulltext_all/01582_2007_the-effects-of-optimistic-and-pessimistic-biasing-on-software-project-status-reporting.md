---
otero_id: 1582
otero_key: "2MSDBGNC"
title: "The effects of optimistic and pessimistic biasing on software project status reporting"
authors: "Andrew P. Snow; Mark Keil; Linda Wallace"
year: "2007"
journal: "Information & Management"
doi: "10.1016/j.im.2006.10.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The effects of optimistic and pessimistic biasing on software project status reporting

Andrew P. Snow <sup>a</sup>, Mark Keil <sup>b</sup>, Linda Wallace <sup>c,\*</sup>

<sup>a</sup> McClure School of Information and Telecommunication Systems, Ohio University, United States <sup>b</sup> Department of Computer Information Systems, J. Mack Robinson College of Business, Georgia State University, United States <sup>c</sup> Department of Accounting and Information Systems, Virginia Polytechnic Institute and State University, United States Received 11 April 2005; received in revised form 3 October 2005; accepted 26 October 2006 Available online 3 January 2007

## Abstract

Anecdotal evidence suggests that project managers (PMs) sometime provide biased status reports to management. In our research project we surveyed PMs to explore possible motivations for bias, the frequency with which bias occurs, and the strength of the bias typically applied. We found that status reports were biased 60% of the time and that the bias was twice as likely to be optimistic as pessimistic. By applying these results to an information-theoretic model, we estimated that only about 10–15% of biased project status reports were, in fact, accurate and these occurred only when pessimistic bias offset project management status errors. There appeared to be no significant difference in the type or frequency of bias applied to high-risk versus low-risk projects Our work should provide a better understanding of software project status reporting. © 2006 E1sevier R V A11 rigbt

Keywords: Project management and scheduling; Reporting bias; Software project management; Traffic light reporting; Information theor

## 1. Introduction

Accurately discerning the status of a software project is difficult. Project managers (PMs) often make mistakes when estimating their project’s status (e.g., [1,2,11]). We refer to such mistakes here as reporting errors, which may be attributed to many factors; e.g., it has been shown that PMs tend to anchor on their initial project estimates and are not likely to make changes to their estimates when reporting the status at a later time [16]. Furthermore, software is intangible, extremely complex, and difficult to observe, all of which increases the likelihood that status reports will be erroneous [21,24].

In addition to reporting error, some PMs may intentionally skew project status when reporting to senior management. We refer to this as reporting bias, which is postulated here to be either optimistic or pessimistic. Optimistic bias occurs when the PM reports a project to be in a better situation than s/he truly believes. It can ultimately lead to situations where senior management is suddenly faced with the grim reality that a project is either in serious trouble or even unrecoverable. While there is anecdotal evidence of optimistic bias (e.g., [15]), there has been no reported effort to determine why a PM might intentionally apply optimistic bias.

The other type, pessimistic bias, occurs when a project is reported to be in worse shape than the PM considers it to be. One motivation for this bias might be to acquire additional organizational resources; another might be a desire to be cautious, because the PM recognizes the difficulty of accurately ascertaining a project’s status. Alternatively, the PM may wish to be considered a hero when the project is finished successfully. Such bias might be damaging if it diverts skills and resources from more critical projects. The frequency or magnitude with which either type of bias occurs is unknown and we thought it should be investigated.

The extent to which PMs apply bias to their status perceptions before reporting to executive management may also vary with project risk levels. High-risk projects are more likely to experience problems or failures [22,31]. The failure of a high-risk project may come as a shock to companies if the PM has optimistically biased its status report (e.g., [8]). The differences in reporting bias among high- and low-risk projects have apparently not been studied previously and were worthy of investigation.

The purpose of our research was thus four-fold to: (1) identify reasons why PMs chose to apply either optimistic or pessimistic bias to their status reports; (2) investigate how frequently optimistic and pessimistic bias occurred in project status reporting for both high- and low-risk projects; (3) investigate the magnitude with which optimistic and pessimistic bias was applied in high- and low-risk projects; and (4) determine how both optimistic and pessimistic reporting biases combined with reporting error to affect project status reports.

## 2. Background

Large numbers of software projects are completed over budget and behind schedule [33]. Controlling software projects is a difficult task that becomes more challenging in the absence of accurate information about project status. The reporting errors made by PMs can be significant [3,9,34], but reporting bias may be even more important in contributing to reporting status inaccuracies [27]. We note that our investigation of bias was limited to intentional biasing of project status reports on the part of the PM; others have examined how unintentional cognitive biases have impacted decision makers in software development projects (e.g., [4,17]).

Literature on a phenomenon called the mum effect offers one explanation for why a PM might apply optimistic bias; the human tendency to avoid transmitting bad news [20]. Smith, et al. [25] suggested that this may contribute to the large numbers of software projects that fail though senior management was not aware that they were in danger. Alternatively, Sabherwal, et al. [23] found that top level managers might continue to commit resources to a failing project if they felt that their future in the company depended on its success or they feared some type of punishment if it was unsuccessfully terminated. The same rationale might apply to PMs at a lower level.

Of course, software PMs sometimes apply pessimistic bias to status reports. They may be distracting senior management’s attention and resources away from projects that are truly in trouble.

The lack of literature regarding the factors that drive software PMs to apply bias led us to our first question: 1. Why do PMs choose to apply either optimistic or pessimistic bias to their status reports?

However, this does not show how often these biases are applied by software PMs. To address this question, we asked software PMs to estimate how frequently they believe their fellow PMs apply bias. If the biasing of status reports were wide-spread then it would be important that executives were made aware of it and introduced controls to deal with the problem.

Furthermore, by gathering data on both low- and high-risk projects, we could determine whether the estimates of bias frequency depended on the level of project risk. Previous research has shown that there were significant differences between high- and low-risk projects (e.g., [32]); therefore, we might expect that the extent to which a PM made errors in assessing project status and the bias that the PM applied before reporting to executive management would vary with project risk. High-risk projects may be more likely to have biased status reports. If so, top level executives should more heavily scrutinize the status reports of high-risk projects. We tried to determine if this was the case in our second question:

2. What are software PMs’ estimates of the frequency of each type of bias occurring for low- and high-risk projects?

However, the answer to this will not provide insight into the degree of bias that PMs apply. We have found no research articles on the level of either optimistic or pessimistic bias in project status reporting and, though there is anecdotal evidence of optimistic biasing, there is apparently nothing published on pessimistic biasing. In order to get a more accurate sense of the extent to which PMs apply bias, we obtained estimates of the frequency, magnitude, and type of bias applied by software PMs. Additionally, from a senior management perspective, it is useful to know whether the expected level of bias is the same or different for low-risk versus high-risk software projects. Hence, we asked the question:

3. What is the expected level of bias, and is it the same for low- and high-risk software projects?

We also wanted to understand the extent to which reporting bias distorted the accuracy of the status report. Status errors and reporting bias combine to affect the accuracy of a project status report. There are three distinct possibilities of how error and bias combine: (1) the project is said to be better than it really is, (2) the project is said to be worse than it actually is, or (3) the bias and error off-set each other, resulting in an essentially accurate status report. A better understanding of the combined effects on status reports can help executive management determine how to interpret the reports. This leads to the final question:

4. How does the full range of optimistic and pessimistic bias combine with reporting error to affect reporting status on high-risk projects?

In our exploratory research, the effects of reporting bias and reporting error were investigated using a twostage probabilistic model that predicted the accuracy of software project management status reports, given varying levels of reporting error and bias [26]. This information theory model (see Fig. 1) contained three variables: true status (T), perceived status (P), and reported status (R). Perceived status and true status are different if the PM makes an error (E) in assessing current status and reported status is different from perceived status if the PM biases (B) his or her perception before reporting the status.

The model shows true status information passing through an error channel, and perceived status information through a bias channel. The combined effect is report distortion, resulting in reported status being different from true status. Previous work [28] showed a potential for large differences between true and reported status when varying levels of optimistic bias were applied.

Earlier research was limited, because it relied on simulated reported status results generated over a range of contrived optimistic bias levels. No empirical data were gathered to determine the extent to which PMs actually applied optimistic or pessimistic bias. In order to get a better sense of the extent to which bias affected project status reporting, it was important to obtain estimates from actual software PMs.

![](/api/attachments/2MSDBGNC/fulltext/images/8664286ff7f47c86e37ec53f6f64c207dc31533776a23fa273f233cfcfd203d8.jpg)  
Fig. 1. Two-stage status model.

## 3. Data collection

Measures of bias frequency, bias strength, reporting error, and true status estimates were required in order to answer the research questions. Subjects were asked to estimate how often PMs apply optimistic bias, no bias, or pessimistic bias before reporting perceived status. Subjects were asked to estimate the level, or strength, of any applied bias and furnish their bias estimates under the assumption that a project had just finished the design phase, and the development stage was just beginning. This point of the project was chosen because it is an important point in the lifecycle where a decision will be made to approve or disapprove the next phase. Accurate status reports are particularly important at this time. The information was elicited for both low-risk and high-risk projects using the survey questions shown in Appendix A.

The subjects were also told that the three major goals of the project were (1) budget, (2) schedule, and (3) functionality/quality. They were asked to consider only three project status levels—Green, Yellow, and Red (traffic light reporting) [5,7,12]. Then they were asked to code a questionnaire using Green for a project in which the three goals were being substantially met, Yellow for a project where two of the goals were being met, and Red for a project where one or no goals were being achieved.

Data previously elicited from a panel of five software project risk experts using the traffic light reporting scheme were used for the reporting error estimates and the true status estimates. The qualification level of the experts and the protocol used for collecting estimates were described by Snow and Keil [28].

To gain insight into why software PMs apply bias, we included two open-ended questions asking respondents to give three reasons why PMs apply optimistic bias and three reasons why they apply pessimistic bias (Questions 4 and 5). The survey also included demographic and other questions about the respondent’s project management experience. The survey instrument was pre-tested with a small number of PMs and slight modifications were made, based on their feedback, before the survey was administered.

PMs were not asked to report their own personal behavior regarding bias, because previous researchers have noted limitations when PMs reported on their own behavior [18]. We were concerned that the subjects might have inhibitions in reporting actions that could be perceived as poor or bad behavior on their part [19]. Social desirability bias has been shown to distort data gained from self-reporting in socially or ethically sensitive surveys [6,30]. Indirect questioning (asking respondents what other people think about sensitive issues) is frequently used to overcome such effects [10,14].

A convenience sample of experienced software PMs was constructed from two sources: the first set consisted of Project Management Institute (PMI) members who belonged to the Information Systems Special Interest Group (ISSIG) and had expressed interest in participating in research on software project management. The second set consisted of software PMs working in a southeastern U.S. metropolitan area who had also agreed to participate in the study. Other researchers interested in software project management issues have gathered survey data from similar subject groups (e.g., [13]).

Survey forms were emailed and 65 practicing software PMs responded. 9 surveys were removed from the sample due to the respondent’s lack of any significant software project management experience. 56 responses were therefore used in subsequent analysis. Roughly equal parts of the usable responses were obtained from each of the sources. After comparing the responses obtained from the two sub-groups for any significant differences, a decision was made to pool the samples for subsequent analysis. Table 1 provides a characterization of the overall subject pool. Subjects indicated that they had served as a PM for an average of more than 17 software projects.

subjected to content analysis, using an open-coding approach (i.e., the researchers did not use predetermined codes but allowed the data to suggest categories [29]). This produced ten unique codes that captured a majority of the reasons that the subjects gave for applying optimistic bias.

Using the same open coding procedure, nine unique codes were created to capture the majority of the reasons that subjects gave for applying pessimistic bias. Then all of the qualitative responses were coded. There were some responses that truly were unique and did not fit neatly into any of the established codes: they were coded as ‘‘other’’ and not subjected to further analysis. The remaining coded responses were further analyzed to determine which reasons were given most frequently for optimistic and pessimistic biasing. Tables 2 and 3 show the most frequently mentioned reasons (expressed as a percent of total coded responses).

Interestingly, the most frequently cited reason for applying optimistic bias was reluctance to transmit bad news, the mum effect. The other top reasons given for optimistic biasing involved impressing management and overoptimism on the part of the PM.

The most frequently cited reason for applying pessimistic bias was that the PM wanted to create slack for contingencies that could arise later. Other frequently cited reasons had to do with the PM’s wish to look like a hero, lack of confidence in the project team or his or her own abilities, and the need to manage expectations. The goal of obtaining additional resources for the project was mentioned repeatedly as a reason for engaging in pessimistic biasing. The ability to shift blame was also mentioned.

## 4. Results

## 4.1. Reasons for bias

In all of the 56 usable surveys, subjects gave one or more reasons why bias was applied. The responses were

Table 1  
Characterization of subject pool

<table><tr><td>Variable</td><td>Mean (X̄)</td><td>S.D.</td></tr><tr><td>Years of experience in software development projects</td><td>3.21 (where 3 = 11–15 years and 4 = 16–20 years)</td><td>1.64</td></tr><tr><td>Number of software development projects participated in</td><td>4.38 (where 4 = 16–20 projects and 5 = 21–25 projects)</td><td>2.24</td></tr></table>

Table 2  
Reasons for optimistic biasing

<table><tr><td>Reasons for optimistic biasing</td><td>Percent</td></tr><tr><td>Project manager believes that senior management “shoots the messenger”—fear of giving bad news</td><td>22</td></tr><tr><td>Project manager wants to make him or herself look good</td><td>22</td></tr><tr><td>Project manager thinks s/he can fix whatever is wrong or that it will all work out in the end</td><td>17</td></tr><tr><td>Project manager does not want to look bad</td><td>9</td></tr><tr><td>Project manager does not want to let the client down</td><td>8</td></tr><tr><td>Project manager succumbs to management pressure</td><td>8</td></tr><tr><td>Project manager does not want to “face the music”</td><td>4</td></tr><tr><td>Project manager’s desire for continued funding</td><td>4</td></tr><tr><td>Project manager wants to keep up the project team’s morale</td><td>4</td></tr><tr><td>Project manager believes that things will work out</td><td>3</td></tr></table>

Table 4  
Table 3  
Reasons for pessimistic biasing

<table><tr><td>Reasons for pessimistic biasing</td><td>Percent</td></tr><tr><td>Project manager wants to create slack for contingencies that may arise later</td><td>17</td></tr><tr><td>Project manager hopes to become a hero later (who turned around a project)</td><td>15</td></tr><tr><td>Project manager has low confidence in project team and/or his/her own ability</td><td>14</td></tr><tr><td>Project manager wants to set management&#x27;s expectations low</td><td>13</td></tr><tr><td>Project manager hopes to obtain additional resources for the project (or hold on to existing resources)</td><td>13</td></tr><tr><td>Project manager wants the ability to shift blame when things go wrong</td><td>9</td></tr><tr><td>Project managers are pessimistic by nature</td><td>9</td></tr><tr><td>Project manager prefers to err on the side of caution if the project is believed to be risky</td><td>8</td></tr><tr><td>Project manager wants to escalate issues and to send a wake-up call to senior management</td><td>4</td></tr></table>

## 4.2. Bias probabilities for low- and high-risk software projects

Estimates by software PMs of the probability of applying bias versus not in high- and low-risk projects are shown in Table 4. The results suggested that PMs were likely to apply bias approximately 60% of the time. A powerful distribution free test, the Kolmogorov–Smirnov (K–S) test statistic, was used to find whether the differences observed were significant. Regardless of the risk level of the project, the results showed that PMs were more likely to apply bias to a project than not. Their estimates of the probability of applying bias do not significantly change for low-risk versus high-risk projects.

The next step was to identify which type of bias was more often applied: optimistic or pessimistic. Table 5 shows the estimates of software PMs for high- and lowrisk projects; apparently, regardless of the risk level of the project, when PMs apply bias they are more likely to apply optimistic than pessimistic bias. Specifically, the data suggested that PMs were more than twice as likely to apply optimistic than pessimistic bias. Also, their estimates of the probability of applying each type of bias do not significantly change from low- to high-risk projects.

Although these results were insightful, they presented only part of the picture. The next step was to look at the strength of the bias that was applied when PMs chose to bias their report. Some status reports may be very biased, while others may only be slightly biased.

## 4.3. Expected level of bias for low- and high-risk software projects

In order to estimate the level of expected bias, we created a probability-weighted metric using the probability of each type of bias and the bias level estimated for each type of bias. This measure was created for each subject reporting, defining optimistic bias as positive and pessimistic bias as negative, as follows:

$$
\begin{array}{r l} B _ {i} & = B _ {\mathrm{op} _ {i}} \left[ \frac {p (B _ {\mathrm{op} _ {i}})}{p (B _ {\mathrm{op} _ {i}}) + p (B _ {\mathrm{ps} _ {i}})} \right] \\ & - B _ {\mathrm{ps} _ {i}} \left[ \frac {p (B _ {\mathrm{ps} _ {i}})}{p (B _ {\mathrm{op} _ {i}}) + p (B _ {\mathrm{ps} _ {i}})} \right] \end{array}\tag{1}
$$

where $B _ { i }$ has an optimistic component (optimistic bias level times probability of applying optimistic bias) and a pessimistic component (pessimistic bias level times probability of applying pessimistic bias). Each subject reported the optimistic and pessimistic bias levels using a Likert type scale.

Probability estimates of bias application by risk level

<table><tr><td></td><td>Probability of no bias</td><td>Probability of bias</td><td> $\mathbf{H}_{\mathrm{o}}$ : no difference between probability of no bias and bias</td></tr><tr><td>High-risk project</td><td>0.39</td><td>0.61</td><td>Reject  $\mathbf{H}_{\mathrm{o}}$  ( $p = .004$ ); implying that most PMs apply bias on high-risk projects</td></tr><tr><td>Low-risk project</td><td>0.44</td><td>0.56</td><td>Reject  $\mathbf{H}_{\mathrm{o}}$  ( $p = .080$ ); implying that most PMs apply bias on low-risk projects</td></tr></table>

Table 5  
Probability estimates of bias type by risk level

<table><tr><td></td><td>Probability of optimistic bias</td><td>Probability of pessimistic bias</td><td> $\mathbf{H}_{\mathrm{o}}$ : no difference between probability of optimistic and pessimistic bias</td></tr><tr><td>High-risk project</td><td>0.42</td><td>0.19</td><td>Reject  $\mathbf{H}_{\mathrm{o}}$  ( $p = .0000$ ); implying that when PMs apply bias on high-risk projects, it is most often optimistic</td></tr><tr><td>Low-risk project</td><td>0.41</td><td>0.15</td><td>Reject  $\mathbf{H}_{\mathrm{o}}$  ( $p = .0000$ ); implying that when PMs apply bias on low-risk projects, it is most often optimistic</td></tr></table>

Table 6 Bias expectation

<table><tr><td>Project risk type</td><td>Mean (X̄)</td><td>S.D.</td><td>Median</td></tr><tr><td>High-risk</td><td>0.96</td><td>1.84</td><td>1.33</td></tr><tr><td>Low-risk</td><td>1.21</td><td>1.56</td><td>1.00</td></tr></table>

The sample mean and variance of the bias expectation measure is shown in Table 6. The means and medians showed that when bias was applied, the bias expectation was optimistic, but the standard deviation indicated that some PMs applied pessimistic bias. The standard deviation on high-risk projects was greater, indicating that there was more variance in terms of the expected bias for high-risk rather than low-risk projects. In terms of central tendency, the median level of bias for high-risk projects was higher than for lowrisk projects, as expected. However, the mean bias expectation on low-risk projects appeared higher than on high-risk projects. The K–S test showed that we could not reject the null hypothesis of no difference $( p = 0 . 8 9 )$ . Therefore, we inferred that PMs applied approximately the same level of bias on both high-risk and low-risk projects, and that the bias in expectation was optimistic.

## 4.4. The impact of reporting bias and reporting error on reporting status

The purpose here was two-fold, to: (1) explain how the previously posited information theory model was extended to include both pessimistic and optimistic bias, and (2) show how the quantitative pessimistic and optimistic bias data collected by the survey instrument was used to address Research Question 4.

In order to determine how reporting bias combined with reporting error to affect status reports, we used the two-stage information theoretic status model as our basis of investigation. Three elements were needed to derive reported status using this model: true status, status error, and reporting bias. From information theory, the model can be expressed in matrix form as:

$$
\mathbf {R} = \mathbf {T} \times \mathbf {E} \times \mathbf {B}\tag{2}
$$

where R represents the probabilities that a project is reported as one of the three possible reporting outcomes (Green, Yellow, or Red); T represents the probabilities that the project is truly in the Green, Yellow, or Red states; E represents the probabilities of error; and B represents the probabilities of applied bias. As the alphabet of this system has three ‘‘letters’’ (G, Y, and R) the T and R vectors are 3-by-1 while the E and B matrices are 3-by-3.

## 4.4.1. True status

The true status matrix was formulated by a panel of software risk experts and was previously described in the literature. For a high-risk project, the true status was estimated to be:

$$
\mathbf {T} _ {\mathrm{H}} = \left| \begin{array}{c c c} 0. 2 2 & 0. 3 4 & 0. 4 4 \end{array} \right|\tag{3}
$$

This shows the probabilities, left to right, of a high-risk project being truly in the Green, Yellow, and Red state, just after the design phase and at the start of the development phase.

## 4.4.2. Status error

Status error was also estimated by the same panel of experts. For the high-risk project the estimated status errors are:

$$
\mathbf {E} _ {\mathrm{H}} = \left| \begin{array}{c c c} 0. 6 1 & 0. 2 2 & 0. 1 7 \\ 0. 2 7 & 0. 5 4 & 0. 1 9 \\ 0. 1 4 & 0. 3 8 & 0. 4 8 \end{array} \right|\tag{4}
$$

In this error matrix, the first row, left to right, shows the probability of the PM perceiving Green, Yellow, or Red if the project is truly Green. The second row shows the same probabilities if the project is truly Yellow, and the third row shows the probabilities if the project is truly Red. The elements of the matrix are thus conditional probabilities, as the chance of error is dependent upon the true status value (Green, Yellow, or Red). The diagonal in this matrix shows the probabilities that Green, Yellow, and Red projects are perceived without error.

## 4.4.3. Applied bias

Bias levels range from completely pessimistic bias to completely optimistic bias. The full set of matrices used for each level of bias in the survey instrument is shown in Appendix B. The assignment of minus (-) values for pessimistic bias and positive (+) values for optimistic bias is arbitrary, and used to create the bias range: [-5, -4, $\cdot . . , 0 , . . . , + 4 , + 5 ]$ . The 11 bias matrices representing each bias value provided a continuum ranging from completely pessimistic to completely optimistic behavior.

The rationale for the different matrices is straightforward: probability gradations in the range [0, 1] are required to represent the different linearly increasing levels of bias in the survey instrument (1, slight; 2, modest; 3, moderate; 4, heavy; 5, complete). This naturally leads to use of corresponding probability values (0.2, 0.4, 0.6, 0.8, 1.0) for the same element in the different bias matrices. Note that the following rules were used to develop the matrices:

1. The probability values in rows add up to unity, thereby covering all possibilities.

2. Optimistic bias never reports a status worse than perceived, and pessimistic bias never reports a status better than perceived, explaining the 0’s in the G, Y, and R reported columns.

3. Complete optimistic bias always reports Red, no bias always reports as perceived, and complete pessimistic bias always reports Green. This explains the 1’s in the reported columns.

4. Moving from matrix to matrix there are distinct gradations, in 0.2 increments, for the ‘‘Perceived Green Reported Green’’, ‘‘Perceived Yellow Reported Yellow’’ and ‘‘Perceived Red Reported Red’’ matrix elements.

These rules account for all but 16 of the 99 matrix elements in the 11 different bias matrices. While other values could be used for the remaining 16 elements, because of these interval and reporting constraint rules, any other possible sets of values cannot be far from the values shown in Appendix B. Therefore plausible probabilities for these remaining matrix elements were selected and, when these 16 elements were perturbated, there was little change in the results, indicating robustness in the model.

## 4.4.4. Information theory model results overlaid by expected bias distribution

The algebraic representation of the model (Eq. (2)) was executed for each integer bias level. For example, for a high-risk project where the bias matrix for slight optimistic bias (1 on the Likert scale) is used as shown in Appendix B, the reported status probabilities at that level of bias is:

![](/api/attachments/2MSDBGNC/fulltext/images/9862d99bf03100ddb388d6a9ea97351ca7c3c29cf65295deb43ff00837df6ee6.jpg)  
Fig. 2. Probabilistic perceived and reported status for the high-risk project.

(which has been subjected to both error and bias) is on the right. Note that the true probability of Green is 0.22 while the reported probability is 0.38, etc.

The probabilistic model was executed in order to determine the probability of reported statuses at each integer level of bias in the range [-5, +5], for both highrisk and low-risk projects. We focused here on high-risk projects as such projects typically involve the greatest financial risk, are of longer duration, and are the subject of most software project catastrophes.

The results for high-risk projects are shown graphically (Fig. 2). The horizontal lines represent true status probabilities for Red, Yellow, and Green, respectively. The curved lines with symbols represent the probabilistic reported status. At bias level 0, the symbols represent perceived status probabilities with no bias applied (i.e., reported status is subject only to error) while the symbols at non-zero bias levels represent reported status probabilities at various levels of either optimistic or pessimistic bias. At completely optimistic bias (+5) projects are always reported Green, while completely pessimistic bias (-5) projects are always reported Red.

In order to gauge the range of bias that one might expect to find in a high-risk project and the implications

$$
\begin{array}{r l} \mathbf {R} _ {\mathrm{1OPT}} & = \mathbf {T} \times \mathbf {E} \times \mathbf {B} _ {\mathrm{1OPT}} \\ & = | 0. 2 2 \quad 0. 3 4 \quad 0. 4 4 | \times \left| \begin{array}{l l l} 0. 6 1 & 0. 2 2 & 0. 1 7 \\ 0. 2 7 & 0. 5 4 & 0. 1 9 \\ 0. 1 4 & 0. 3 8 & 0. 4 8 \end{array} \right| \times \left| \begin{array}{l l l} 1. 0 & 0. 0 & 0. 0 \\ 0. 2 & 0. 8 & 0. 0 \\ 0. 0 5 & 0. 1 5 & 0. 8 \end{array} \right| = | 0. 3 8 \quad 0. 3 7 \quad 0. 2 5 | \end{array}\tag{5}
$$

The true and error matrices are for a high-risk project, estimated by software risk experts. The reading of this result in Eq. (5) is: the true status of the project (Green, Yellow, Red) is on the left, while the reported status for project status reporting, we combined the results of this probabilistic model with the previously computed bias expectation statistic. A box plot of bias expectation was overlaid on the information theory results at the bottom of Fig. 2. In this, the centerline is the median, and the divisions are quartiles; however, the box plot comparison does not include the 39% for which no bias is applied.

Table 7  
Reporting discrepancies at various bias levels for the high-risk project

<table><tr><td>Bias level</td><td>Bias type</td><td>Observation</td></tr><tr><td>-3</td><td>Pessimistic</td><td>About 67% of projects are reported Red when 44% truly are</td></tr><tr><td>-2</td><td>Pessimistic</td><td>PMs report fairly accurately at this bias level—bias offsets error to some extent; however, Red is somewhat over reported and Green is somewhat under reported</td></tr><tr><td>-1</td><td>Pessimistic</td><td>PMs report fairly accurately at this bias level—bias almost exactly offsets error</td></tr><tr><td>0</td><td>None</td><td>PMs are most likely to report projects as Yellow, when they are really most likely Red</td></tr><tr><td>1</td><td>Optimistic</td><td>PMs are about as likely to report projects Green or Yellow, but least likely to report projects Red. The true incidence of Red projects is almost two times greater than the reported frequency</td></tr><tr><td>2</td><td>Optimistic</td><td>PMs are more than twice as likely to report projects Green as they are Red, when the opposite is true</td></tr><tr><td>3</td><td>Optimistic</td><td>PMs are about five times as likely to report projects Green, as they are Red</td></tr></table>

We summarized our observations in Table 7. It shows what happens as we move from moderate pessimistic to moderate optimistic bias (-3 to +3). For optimistic bias, the combination of error and bias resulted in very inaccurate reporting, even with small amounts of bias. A contrary result is seen for pessimistic bias; the reporting discrepancy is relatively benign, as the combination of error and bias tend to offset one another.

We also observed that for the bias range [-2, +2], Yellow reports can be believed. And in the bias range [-1, -2], all reports can be believed, while in the range [+1, +5] Red and Green reports should not be believed. Comparing the box plot to the probabilistic model, we can infer the following, for high-risk project status reports:

1. About 25% of applied bias is optimistic and greater than 2, where the most prevalent report is decidedly Green, even though the true state probabilities indicate that projects are most likely to be in a Red or Yellow state.

2. About 25% of applied bias is optimistic between 1 and 2, where Green and Red reports become the opposite of reality. Green reporting is most prevalent here, even though projects are more often in the Red state. Here, the reported incidence of Yellow projects is close to the true state probability.

3. About 20% of applied bias is optimistic between 0 and 1, where Red starts to become the least frequently reported status. Since the bias here is neutral to slightly positive, reporting error is the principal driver of project status distortion.

4. About 10–15% of applied bias is pessimistic in the range [-1, -2], unwittingly providing fairly accurate reports, because PM status errors offset their bias.

Therefore, only about 10–15% of biased PM reports appear to be accurate and reliable. These results address Research Question 4.

## 5. Summary, limitations, and implications

## 5.1. Summary

While previous research has suggested that PMs may intentionally bias their status reports, we attempted to ascertain the reasons why they might behave in this manner. Two other key contributions that distinguish our work in this area are: (1) the consideration of both pessimistic and optimistic bias and (2) the computation of an expected level of bias based on empirical data obtained from PMs.

Our data suggested that PMs are likely to apply bias in both low- and high-risk projects and when PMs do bias, they are twice as likely to bias optimistically. While the expected level of bias is slight and tends to be more optimistic than pessimistic, it is important to recognize that the expected level of bias represents the central tendency, and that the actual distribution of bias observed was broad, meaning that individual PMs may have applied bias that was much more optimistic or pessimistic than the overall expected level of bias we calculated. Thus, it is critical for the senior executive to consider the personality and behavior of individual PMs before coming to any conclusion about the accuracy of their status reports.

Our results show that even at low levels of optimistic bias, it combines with status errors to make reports decidedly overoptimistic. Even in cases where no bias is applied, status error results in skewed status reports. Optimistic bias leads to status reports that are very different from reality, while pessimistically biased status reports tend to be accurate because bias offsets error. When PMs apply bias, only 10–15% of high-risk software project management status reports seem to be accurate, produced only when pessimistic PM bias offsets PM status error.

## 5.2. Limitations

Since we asked PMs to estimate the percent of PMs that apply pessimistic, optimistic, and no bias, one limitation deals with the extent to which PMs can be accurate in making such estimates. PMs are, however, able to assess the behavior of other PMs by virtue of having worked with them on past projects and having observed their behavior. Thus, while the bias estimates may be imperfect, we believe that they are more accurate than we would have obtained by asking PMs to report on their own application of bias. The effects of indirect questioning have been shown to be less severe than those of self reporting, but they may still exist.

Although the bias matrices used in the model construction appear reasonable and produce internally consistent results, no model will exactly represent behavior. This limitation is recognized in any model building research. Additionally, the reported status probabilities combined two independent empirical studies. However, even with this limitation, the results showed that an information theory method holds promise for deriving important insights into status reporting.

Our results may also only be valid at one point in the project lifecycle (the end of the design phase), as the experts and PMs were given this point in the lifecycle for which to answer questions about the probabilities.

This research utilized a convenience sample for its subject source. The subjects were all experienced PMs, but they were not randomly selected. As a result, the findings may not be representative of the entire population of software PMs.

## 5.3. Implications

The most frequently cited reason for optimistic biasing was reluctance to transmit bad news. Perhaps methods could be developed by upper management to reward accurate reporting rather than penalize bearers of bad news. Although the reluctance to transmit bad news has been examined in previous research, methods to overcome this and to deal with the problem of biased reports have not.

Our research has demonstrated that the amount of inaccuracy in a status report is sensitive to the amount of optimistic bias of the PM. Unfortunately, it appears that if a PM applies bias, it is twice as likely to be optimistic as pessimistic. Furthermore, the applied bias is typically strongly optimistic, resulting in status reports that can be quite distorted and misleading.

## 6. Conclusions

We have shown that while both optimistic and pessimistic biasing occurs, optimistic tends to outweigh pessimistic biasing. The impact of optimistic biasing appears to be very deleterious to reporting accuracy and senior management should take all reasonable steps to counteract it. Attacking the primary reasons for biasing requires an introspective examination to determine if the organizational culture or the behaviors of specific executives is contributing to the problem. Our data suggest that PMs employ optimistic biasing because of fear and a wish to impress management. Executives need to establish environments where bad news is accepted as a norm. In some organizations, employees are explicitly asked not to spread ‘‘fear, uncertainty, and doubt’’ on a project. When the organizational culture is ‘‘good news only’’ in nature, the PM has an incentive to optimize the project’s status report in the hope that the situation may improve.

Deciding when and how to intervene in response to bad news is critical. By consistently overreacting to Yellow or Red reports with micromanagement, the executive may create or reinforce an environment for optimistic bias. The executive must continually stress the need for realistic reports and the importance of not being surprised after it is too late to intervene effectively.

PMs should be made aware of the impact that even a slight optimistic bias may have on the accuracy of their reporting status and to err on the side of caution or pessimism when producing a status report. Ironically, our research also suggested that the PM who is pessimistic gives the most accurate reports, but by accident. In discussing our early findings, one CIO at a Fortune 100 company interpreted our results as validation for his recruiting strategy: he tried to eliminate overly optimistic PMs, preferring to hire those who would furnish accurate reports.

## Appendix A. Question format used to assess bias

1. We would like you to estimate below what percent of PM's apply optimistic bias, no bias, or pessimistic bias before reporting perceived status to the organizational executive. By optimistic bias, we mean the PM tends to report the status to be better than what s/he perceives; by no bias, we mean that the PM tends to report the status exactly as s/he perceives; by pessimistic bias, we mean the PM tends to report the status to be worse than s/he perceives (Fill in the blanks for each project risk type for your answer, and note that the answers must add up to 100%)

## LOW-RISK PROJECTS:

% OF THE TIME PMs APPLY OPTIMISTIC BIAS TO LOW-RISK PROJECTS

% OF THE TIME PMs APPLY NO BIAS TO LOW-RISK PROJECTS

% OF THE TIME PMs APPLY PESSIMISTIC BIAS TO LOW-RISK PROJECTS

100 % OF LOW-RISK PROJECTS

## HIGH-RISK PROJECTS

% OF THE TIME PMs APPLY OPTIMISTIC BIAS TO HIGH-RISK PROJECTS

% OF THE TIME PMs APPLY NO BIAS TO HIGH-RISK PROJECTS

% OE THE TIME PMs APPLY PESSIMISTIC BIAS TO HIGH-RISK PROJECTS

100 % OF HIGH-RISK PROJECTS

2. For those PM's applying optimistic bias (tend to report status better than perceived), assess the average level of bias applied by PMs on the scale below. (Circle number to answer for each project risk type).

AMOUNT OF OPTIMISTIC BIAS APPLIED BY PMs ON

<table><tr><td rowspan="2">LOW-RISK PROJECTS</td><td colspan="5">1----2----3----4----5</td></tr><tr><td>SLIGHT</td><td>MODEST</td><td>MODERATE</td><td>HEAVY</td><td>COMPLETE</td></tr><tr><td rowspan="2">HIGH-RISK PROJECTS</td><td colspan="5">1----2----3----4----5</td></tr><tr><td>SLIGHT</td><td>MODEST</td><td>MODERATE</td><td>HEAVY</td><td>COMPLETE</td></tr></table>

NOTE: IN THIS CONTEXT, “COMPLETE" MEANS PROJECTS ARE ALWAYS REPQRTED GREEN REGARDLESS OF PERCEIVED STATUS

3. For those PM's applying pessimistic bias (tend to report status worse than perceived), assess the average level of bias applied by PMs on the scale below. (Circle number to answer for each project risk type)

AMOUNT OE PESSIMISTIC BIAS APPLJED BY PMs ON

<table><tr><td rowspan="2">LOW-RISK PROJECTS</td><td colspan="5">1----2----3----4----5</td></tr><tr><td>SLIGHT</td><td>MODEST</td><td>MODERATE</td><td>HEAVY</td><td>COMPLETE</td></tr><tr><td rowspan="2">HIGH-RISK PROJECTS</td><td colspan="5">1----2----3----4----5</td></tr><tr><td>SLIGHT</td><td>MODEST</td><td>MODERATE</td><td>HEAVY</td><td>COMPLETE</td></tr></table>

NOTE: IN THIS CONTEXT. “COMPLETE" MEANS PROJECTS ARE ALWAYS REPORTED RED REGARDLESS OF PERCEIVED STATUS

4. If you believe PMs apply optimistic bias in status reporting, list, in order of importance, up to three reasons.

3.

5. If you believe PMs apply pessimistic bias in status reporting, list, in order of importance, up to three reasons.

2.

3.

Appendix B. Pessimistic and optimistic bias channels

<table><tr><td rowspan="2"></td><td colspan="3">Bias channel (reported)</td><td rowspan="2">Bias type</td><td rowspan="2">Bias level</td></tr><tr><td>G</td><td>Y</td><td>R</td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Completely pessimistic</td><td>-5</td></tr><tr><td>G</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Heavily pessimistic</td><td>-4</td></tr><tr><td>G</td><td>0.20</td><td>0.05</td><td>0.75</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>0.20</td><td>0.80</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Moderately pessimistic</td><td>-3</td></tr><tr><td>G</td><td>0.40</td><td>0.20</td><td>0.40</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>0.40</td><td>0.60</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Modestly pessimistic</td><td>-2</td></tr><tr><td>G</td><td>0.60</td><td>0.20</td><td>0.20</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>0.60</td><td>0.40</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Slightly pessimistic</td><td>-1</td></tr><tr><td>G</td><td>0.80</td><td>0.15</td><td>0.05</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>0.80</td><td>0.20</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>No bias</td><td>0</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td><td></td><td></td></tr><tr><td>Y</td><td>0.00</td><td>1.00</td><td>0.00</td><td></td><td></td></tr><tr><td>R</td><td>0.00</td><td>0.00</td><td>1.00</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Slightly optimistic</td><td>1</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td><td></td><td></td></tr><tr><td>Y</td><td>0.20</td><td>0.80</td><td>0.00</td><td></td><td></td></tr><tr><td>R</td><td>0.05</td><td>0.15</td><td>0.80</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Modestly optimistic</td><td>2</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td><td></td><td></td></tr><tr><td>Y</td><td>0.40</td><td>0.60</td><td>0.00</td><td></td><td></td></tr><tr><td>R</td><td>0.20</td><td>0.20</td><td>0.60</td><td></td><td></td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td>Moderately optimistic</td><td>3</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td><td></td><td></td></tr><tr><td>Y</td><td>0.60</td><td>0.40</td><td>0.00</td><td></td><td></td></tr><tr><td>R</td><td>0.40</td><td>0.20</td><td>0.40</td><td></td><td></td></tr></table>

Appendix B. (Continued )

<table><tr><td rowspan="2"></td><td colspan="3">Bias channel (reported)</td><td rowspan="2">Bias type</td><td rowspan="2">Bias level</td></tr><tr><td>G</td><td>Y</td><td>R</td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td rowspan="4">Heavily optimistic</td><td rowspan="4">4</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Y</td><td>0.80</td><td>0.20</td><td>0.00</td></tr><tr><td>R</td><td>0.75</td><td>0.05</td><td>0.20</td></tr><tr><td>Perceived</td><td></td><td></td><td></td><td rowspan="4">Completely optimistic</td><td rowspan="4">5</td></tr><tr><td>G</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Y</td><td>1.00</td><td>0.00</td><td>0.00</td></tr><tr><td>R</td><td>1.00</td><td>0.00</td><td>0.00</td></tr></table>

## References

[1] T.K. Abdel-Hamid, Understanding the ‘90% Syndrome’ in software project management: a simulation-based case study, The Journal of Systems and Software 8 (4), 1988, pp. 319–330.

[2] F.P. Brooks, No silver bullet: essence and accidents of software engineering, Computer 20 (4), 1987, pp. 10–19.

[3] F.P. Brooks, The Mythical Man-Month: Essays on Software Engineering, Anniversary Edition, Addison-Wesley, Reading, Massachusetts, 1995.

[4] R. Buehler, D. Griffin, Planning, personality, and prediction: the role of future focus in optimistic time predictions, Organizational Behavior and Human Decision Processes 92, 2003, pp. 80–90.

[5] R. Burris, Get the green light, The Wight Line 7 (2), 1994, pp. 6–9.

[6] J. Chung, G.S. Monroe, Exploring social desirability bias, Journal of Business Ethics 44 (4), 2003, pp. 291–302.

[7] C. Coulter, Multiproject management and control, Cost Engineering 32 (10), 1990, pp. 19–24.

[8] R.X. Cringely, When disaster strikes IS, Forbes ASAP 1994, pp. 60–64.

[9] T. DeMarco, Controlling Software Projects, Yourdon Press, New York, 1982

[10] R.J. Fisher, Social desirability bias and the validity of indirect questioning, Journal of Consumer Research 20, 1993, pp. 303– 315.

[11] W.W. Gibbs, Software’s chronic crisis, Scientific American 271 (3), 1994, pp. 86–95.

[12] B. Hughes, M. Cotterall, Software Project Management, McGraw Hill International, London, 1999.

[13] J.J. Jiang, G. Klein, Risks to different aspects of system success, Information and Management 36, 1999, pp. 264–272.

[14] M.-S. Jo, Controlling social-desirability bias via method factors of direct and indirect questioning in structural equation models, Psychology & Marketing 17 (2), 2000, pp. 137–148.

[15] M. Jorgensen, D.I.K. Sjoberg, Impact of effort estimates on software project work, Information and Software Technology 43, 2001, pp. 939–948.

[16] M. Jorgensen, D.I.K. Sjoberg, The impact of customer expectation on software development effort estimates, International Journal of Project Management 22, 2004, pp. 317–325.

[17] P.J. Kirs, K. Pflughoeft, G. Kroeck, A process model cognitive biasing effects in information systems development and usage, Information & Management 38 (3), 2001, pp. 153–165.

[18] T. Moynihan, Coping with client-based ‘People-Problems’: the theories-of-action of experienced is/software project managers, Information & Management 39, 2002, pp. 377–390.

[19] J.C. Nunnally, Psychometric Theory, McGraw-Hill, New York, 1978.

[20] E.C. O’Neal, D.W. Levine, J.F. Frank, Reluctance to transmit bad news when the recipient is unknown: experiments in five nations, Social Behavior and Personality 7 (1), 1979, pp. 39–47.

[21] J.S. Reel, Critical success factors in software projects, IEEE Software 16 (3), 1999, pp. 18–23.

[22] J. Ropponen, K. Lyytinen, Components of software development risk: how to address them? A project manager survey IEEE Transactions on Software Engineering 26 (2), 2000, pp. 98–112.

[23] R. Sabherwal, M.K. Sein, G.M. Marakas, Escalating commitment to information systems projects: findings from two simulated experiments, Information & Management 40 (8), 2003, pp. 781–798.

[24] K. Sengupta, T.K. Abdel-Hamid, The impact of unreliable information on the management of software projects: a dynamic decision perspective, IEEE Transactions on Systems, Man and Cybernetics 26 (2), 1996, pp. 177–189.

[25] H.J. Smith, M. Keil, G. DePledge, Keeping mum as the project goes under: toward an explanatory model, Journal of Management Information Systems 18 (2), 2001, pp. 189–227.

[26] A. Snow, M. Keil, A framework for assessing the reliability of software project management reports, Engineering Management Journal 14 (2), 2002, pp. 20–26.

[27] A.P. Snow, M. Keil, The challenge of accurate project status reporting: a two stage model incorporating status errors and reporting bias, in: Proceedings of the 34th Annual Hawaii International Conference on System Sciences (HICSS-34), Kihei, Hawaii, January 3–6, 2001, pp. 1–10.

[28] A.P. Snow, M. Keil, The challenge of accurate software project status reporting: a two-stage model incorporating status errors and reporting bias, IEEE Transactions on Engineering Management 49 (4), 2002, pp. 491–504.

[29] A. Strauss, J. Corbin, Basics of Qualitative Research: Grounded Theory Procedures and Techniques, Sage Publications, Newbury Park, CA, 1990.

[30] S. Sudman, N.M. Bradburn, Respose Effects in Surveys: A Review and Synthesis, Aldine, Chicago, 1974.

[31] L. Wallace, M. Keil, A. Rai, How software project risk affects project outcomes: an investigation of the dimensions of risk and an exploratory model, Decision Sciences 35 (2), 2004, pp. 289–321.

[32] L. Wallace, M. Keil, A. Rai, Understanding software project risk: a cluster analysis, Information & Management 42 (1), 2004, pp. 115–125.

[33] B. Whittaker, What went wrong? Unsuccessful information technology projects Information Management & Computer Security 7 (1), 1999, pp. 23–29.

[34] R.W. Zmud, Management of large software development efforts, MIS Quarterly 4 (2), 1980, pp. 45–55.

![](/api/attachments/2MSDBGNC/fulltext/images/a4b2753d98aea50d6e29d32b7cfc593f4be6a05bae068fe18bfc7173c7188976.jpg)

Andrew P. Snow is an associate professor and director of the McClure School of Information and Telecommunication Systems at Ohio University. He received his bachelor’s and master’s degrees in electrical engineering from Old Dominion University, and his PhD in information science from the University of Pittsburgh. His research interests include telecommunication network resiliency and IT project man-

agement. His publications appear in journals such as IEEE Transactions on Reliability, IEEE Transactions on Engineering Management, Journal of Networks and Systems Management, Telecommunications Policy, Journal on Mobile Networks and Applications, IEEE Computer, and the International Journal of Industrial Engineering. Prior to returning to university for an academic career, he held positions as electronics engineer, member of the technical staff, manager, director, vice president, general manager, and chairman in telecommunications carrier, systems integration and consulting firms.

![](/api/attachments/2MSDBGNC/fulltext/images/0e511e5693fe8d1dc16f4773b5bfdbf65e72ea195ce35d237d1100d5addbec8e.jpg)

Mark Keil is the department chair and board of advisors professor in computer information systems at Georgia State University. His research focuses on software project management, with particular emphasis on understanding and preventing software project escalation. His research is also aimed at providing better tools for assessing software project risk and removing barriers to software use. His research

has been published in MIS Quarterly, Sloan Management Review, Communications of the ACM, Journal of Management Information Systems, Information & Management, IEEE Transactions on Engineering Management, Decision Support Systems, and other journals. He has served as an associate editor for the MIS Quarterly and as coeditor of The DATA BASE for Advances in Information Systems. He currently serves on the editorial board of the Journal of Management Information Systems, Decision Sciences, and IEEE Transactions on Engineering Management.

![](/api/attachments/2MSDBGNC/fulltext/images/2b2560be2b5f5c38faabe774d53568d4652194c7a1484974bd622a1e2c772bbc.jpg)

Linda Wallace is an associate professor in the Department of Accounting and Information Systems at Virginia Polytechnic Institute and State University. She obtained her PhD in computer information systems from Georgia State University in 1999. Her research interests include software project risk, information security, knowledge communities, and agile software development. Her research has been accepted for pub-

lication in Decision Sciences, Communications of the ACM, Information & Management, IEEE Security & Privacy, Decision Support Systems, and Journal of Systems and Software.
