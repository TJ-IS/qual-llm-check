---
otero_id: 6512
otero_key: "SH46ERUR"
title: "Drug prescription behavior and decision support systems"
authors: "M. Tolga Akçura; Zafer D. Ozdemir"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.045"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
M. Tolga Akçura <sup>b</sup>, Zafer D. Ozdemir <sup>a,</sup>⁎

<sup>a</sup> Farmer School of Business, Miami University, United States

<sup>b</sup> School of Economics and Administrative Sciences, Ozyegin University, Turkey

## a r t i c l e i n f o

Available online 5 November 2012

Keywords: Decision support systems Computerized physician order entry Adverse drug event Prescription error Drug selection Drug administration Dosage

## a b s t r a c t

Adverse drug events plague the outcomes of health care services. In this research, we propose a clinical learning model that incorporates the use of a decision support system (DSS) in drug prescriptions to improve physicians' decisions about the initial drug selection and administration. The model allows for both the analytical investigation of the effects of different DSS features on clinical learning and the estimation of the physician learning behavior given a panel data set. The analytical results suggest that using a DSS to improve physicians' prescription decisions would positively in<sup>fl</sup>uence their clinical learning. Conversely, without improvements in successful drug selection, the use of a DSS would negatively affect clinical learning. The empirical results provide further evidence on the factors that drive physicians' responses to information sources and the extent to which they rely on clinical experience in prescribing drugs.

© 2012 Published by Elsevier B.V.

## 1. Introduction

Researchers estimate that adverse drug events (ADEs) cause between 700,000 and 1.5 million injuries annually [16,47,48,73]. A prominent study suggests that 28 percent of the ADEs, most of which are due to prescription errors [41,46,49], are preventable [6]. Mirco et al. [57] <sup>fi</sup>nd that the most common prescription errors are de<sup>fi</sup>ciencies related to choosing the right drug, dosage, frequency, route of administration (i.e., pills, gels, and liquids), drug interactions, and length of therapy.

The sheer number of prescription errors has its roots in the challenges that physicians face in keeping abreast of developments in pharmacology. As powerful new drugs and clinical information become available, the need for accurate prescription decisions grows proportionately. Thus, de<sup>fi</sup>ciencies in keeping up with new developments in pharmacology unavoidably lead to suboptimal prescription decisions, even though the choice and administration of drugs make up some of the most important clinical decisions in medical practice [69].

Continuous physician learning is arguably the most effective solution to reducing prescription errors. Physician learning involves effectively integrating the clinical experiences with the most recently acquired information and then modifying the prescription behavior accordingly. Physicians regularly update their beliefs and thus learn about the ef<sup>fi</sup>cacy of drugs from their own clinical experiences [23]. Improving prescription decisions through continuous learning would not only minimize preventable ADEs and provide better treatments for the patients, but also improve patient satisfaction [24,28], reduce insurance risks, and lead to superior quality and audit ratings for the physicians [51].

When integrated with clinical, practice guidelines and work<sup>fl</sup>ows, decision support systems (DSSs) and computerized physician order entry (CPOE) can help physicians with their clinical learning and thus enhance their prescription decisions. CPOE refers to computerized systems that automate the medication ordering process. Basic CPOE features include veri<sup>fi</sup>cation of typed orders in a standard and complete format, and CPOE systems typically have or interface with DSSs of varying sophistication, although some DSSs are implemented without a CPOE [41]. In general, CPOE and DSSs support two types of decisions: drug selection and drug administration. Drug selection refers to the initial decision of matching a patient with an appropriate drug from a set of alternatives. Computerized decision support on drug selection is provided through drug recommendations, drug–allergy checks, drug– laboratory value checks, and drug–drug interaction checks. Drug administration refers to how the selected drug should be administered in terms of dosage, frequency, route, and length of therapy, and such decisions are supported with appropriate recommendations by the software. The drug selection feature of CPOE has been shown to reduce the rate of non-intercepted, serious prescription errors by more than half [7,8]. The use of DSSs has also been shown to reduce the errors associated with drug administration (i.e., decisions regarding medication dosage, frequency, and route). Table 1 summarizes the literature on the effect of DSS use on prescription decisions and outcomes.

Because DSSs do not replace physician judgment,<sup>1</sup>the sustainable positive results can be achieved only through improved physician learning supported with DSSs. Bochicchio et al. [10] also argue that the main bene<sup>fi</sup>t of computerized decision support is simply improved pharmacological knowledge. Physicians assume full responsibility of their prescribing decisions with or without using a DSS, and therefore the most successful DSSs are those that best facilitate physician learning.

Table 1  
Studies on the impact of CPOE and DSS usage on prescription errors

<table><tr><td>Study</td><td>Type of decision support</td><td>Result</td></tr><tr><td>Bochicchio et al. [10]</td><td>Drug</td><td>21% improvement in antibiotic decision accuracy (P=0.005).</td></tr><tr><td>Hunt et al. [37]</td><td>Dosing</td><td>9 of 15 studies showed improvement in drug dosing.</td></tr><tr><td>Kirk et al. [45]</td><td>Dosing</td><td>Significantly fewer dosing errors for computer-assisted prescriptions than their traditional counterparts (P&lt;0.001)</td></tr><tr><td>Bates et al. [7]</td><td>Drug and dosing</td><td>55% reduction in non-intercepted serious medical errors (P=0.37) and 17% reduction in preventable ADEs (P=0.37)</td></tr><tr><td>Bates et al. [8]</td><td>Drug, dosing, and frequency</td><td>81% reduction in prescription errors (P=0.01) and 86% reduction in non-intercepted serious prescription errors (P=0.01)</td></tr><tr><td>Ammenwerth et al. [3]</td><td>Drug, dosing, and frequency</td><td>4 of 6 studies showed a significant relative risk reduction in ADEs.23 of 25 studies showed a significant relative risk reduction in prescription errors.</td></tr><tr><td>Teich et al. [70]</td><td>Drug, dosing, and frequency</td><td>Statistically significant improvements in five types of drug selection and administration decisions</td></tr><tr><td>Evans et al. [30]</td><td>Drug, dosing, frequency, and route</td><td>70% reduction in ADEs caused by anti-infectives (P=0.02)</td></tr><tr><td>Burke and Pestotnik [15]</td><td>Drug, dosing, frequency, and route</td><td>ADE rate dropped from 1.22% to 0.04%.</td></tr></table>

Our objective in this paper is to understand the interaction between physician learning and the use of a DSS and the corresponding impact on prescription decisions. We also aim to understand which type of decision support is more critical for physician learning. To this end, we develop a model of physician prescription behavior supported by two types of DSS features. One category of DSS features supports the decisions regarding when to prescribe a focal drug (drug selection), and the other category supports the drug administration decisions for the focal drug. Using the DSS features can potentially reduce the variances and uncertainties behind drug selection and administration decisions and in<sup>fl</sup>uence physicians' learning, with the objective that prescription behaviors are in line with the clinical guidelines established for the focal drug. The proposed framework provides both an analytical model to investigate the effects of these two DSS capabilities and an empirical model to estimate the physician prescription behavior given a panel data set (for other similar empirical models, see [1,23,46]). The model accounts for the following two factors: (1) physicians may be subject to different patient pro<sup>fi</sup>les and experiences, and (2) they may arrive at different clinical conclusions, even after observing the same evidence, because of their prior clinical experiences [46].

Using the proposed model, we ask the following research questions: How are the two types of DSS features related to physicians' clinical learning about a focal drug? What are the salient physician characteristics that affect clinical learning? What are some of the important physician-level factors that facilitate the adoption of

DSSs? We use a hierarchical Bayesian estimation technique that captures the individual, physician-level uncertainties and learning behavior. Thus, the proposed model can be used to analyze, compare, and contrast different physician responses to the use of computerized decision support in the prescription process. Previous research in information systems has shown the importance of combining individual-level learning behavior and user environment [38]. A contribution of this study is that it combines physician learning and the use of information technology in modeling physician behavior. The analytic modeling approach combined with the empirical analysis of clinical learning behavior provides a powerful framework for capturing the impact of DSS on physician learning.

The analytical results emphasize the importance of computerized support for drug selection decisions and highlight both the bene<sup>fi</sup>ts and the risks associated with designing and implementing DSSs. When DSSs lead to superior drug selection decisions, patient-level observations are better integrated into the prescription behavior, which improves physician learning. An implication of this result is that proper design and use of DSS may help in enforcing compliance with treatment protocols and reducing prescription errors. Thus, the model provides an explanation on when and how the use of a DSS would allow us to observe physician decisions similar to those of an expert panel [67]. We also <sup>fi</sup>nd that, without improvements in the accuracy of drug selection decisions, the use of a DSS negatively in<sup>fl</sup>uences the physicians' clinical learning because they attribute less importance to the information they gather from patients than to their established expectations of the drug. Consequently, improper design and implementation may lead to negative outcomes [22,49].

The empirical results provide further evidence on the role of the information acquired through clinical experience. We <sup>fi</sup>nd that physicians differ substantially with regard to their responses toward the information sources and clinical experiences. Physician specialty and location have signi<sup>fi</sup>cant effects on the overall physician responses to new information about a focal drug. General practice physicians (i.e., generalists) and physicians located in high-income areas rely more on their clinical experiences than specialists and physicians located in low-income areas, respectively. Accordingly, our analysis suggests that computerized decision support for drug selection bene<sup>fi</sup>ts specialists and physicians located in low-income areas relatively more. These results provide further evidence on the importance of specialty and location on the success of DSS use.

We organize the rest of the paper as follows: We <sup>fi</sup>rst present an analytical model that captures the physician prescription and learning behavior in Section 2. Then, we describe our data and empirical methods in Section 3. The empirical results on salient physician characteristics and how they are related to DSS usage are then presented in Section 4. The paper concludes with a summary and discussion in Section 5.

## 2. Model

We begin with a basic model that formulates physicians' prescription of a focal drug in the absence of DSS and clinical learning. We extend the model <sup>fi</sup>rst with two DSS features and then with a mechanism for clinical learning about the focal drug. Finally, we present the analytical results on how the two DSS features facilitate physician learning.

## 2.1. Basic model

Consider, for example, patients who suffer from existing conditions that require ongoing treatments. Bipolar disorders or cardiovascular diseases are examples of such conditions. Physicians consider prescribing a focal drug in treating their patients given the existing condition. Physicians also prescribe the focal drug according to their preferences, past habits, and external information sources about the drug [69]. Physicians differ depending on the pro<sup>fi</sup>le of their patients, their prescription habits, and their responses to the external information they receive about the drugs. Physician uncertainties may arise in prescribing the focal drug to the right set of patients with the correct dosage, frequency, route, and length of therapy.

Physicians face uncertainty in deciding whether the focal drug is the most appropriate one for a speci<sup>fi</sup>c patient. In making this decision, each physician considers the characteristics of the drug, including its side effects in view of a patient's general health and lifestyle. For example, certain drugs that reduce cholesterol levels should not be prescribed to patients with pre-existing health conditions. A similar concern exists for patients who suffer from bipolar disorders because they often have a multitude of medical problems and therefore need to take additional drugs that may interact with the drugs used to treat bipolar disorder. For example, children with bipolar disorders have a high risk of developing attention de<sup>fi</sup>cit hyperactivity disorder (ADHD), and the stimulants used to treat ADHD can complicate the bipolar treatment. (http://www.healthcentral.com/bipolar/therapy-000066\_6-145.html). Moreover, some patients may be allergic to certain drugs, some others may experience side effects due to their lifestyles, or the focal drug may not perform as expected, leading to unforeseen reactions. Chan and Hamilton [17] show that even the least effective drug may still have a signi<sup>fi</sup>cant market share because of the heterogeneity in the effectiveness of drugs and their side effects on patients. Thus, physicians consider selecting the focal drug with varying degrees of con<sup>fi</sup>dence. Let the random term $\omega _ { i t }$ represent the overall drug selection uncertainty for physician i at time t. We view this uncertainty as physician speci<sup>fi</sup>c according to physician activity learning theory [29]. This theory posits that the most appropriate unit of analysis is the subject (in our case, a physician) who learns how to carry out a meaningful activity (i.e., prescribing the focal drug given the existing condition) in a system of activities (i.e., through many interactions with the patients) [39]. The idiosyncrasies in physicians' patient pro<sup>fi</sup>les contribute to the differences in physician-speci<sup>fi</sup>c characteristics, which in turn generate physician-speci<sup>fi</sup>c uncertainties when selecting the drug.

Let $Q _ { i t }$ represent physician i's preference for the focal drug given the existing condition among the patients, where higher values of $Q _ { i t }$ represent a more positive preference for the focal drug. The number of prescriptions written in period t is a function of physician i's preference for the focal drug $Q _ { i t }$ and the overall drug selection uncertainty $\omega _ { i t } .$ Assume that during period t, physician i handles $n _ { i t }$ new patients. Let $Y _ { i t }$ denote the total number of new prescriptions in period t and follow a Poisson distribution.<sup>2</sup>The probability of observing y prescriptions equals the following:

$$
\mathrm{p} (Y _ {i t} = y _ {i t}) = \frac {\mu^ {y _ {i t}} e ^ {- y _ {i t}}}{y _ {i t} !},\tag{1}
$$

where the mean of the distribution $\mu _ { i t }$ is proportional $\mathrm { t o } ^ { 3 }$

$$
n _ {i t} \exp (Q _ {i t} + \omega_ {i t}).\tag{2}
$$

External information sources help physicians establish a preference for the focal drug [69,71]. We consider three external information sources available to physicians [59]. First, face-to-face discussions and training materials on the focal drug are a signi<sup>fi</sup>cant source of information for physicians. Using the industry terminology, we call these activities detailing. Second, drug samples provide a trial opportunity for physicians and act as an additional information source that may in<sup>fl</sup>uence a doctor's preference. We call the clinical use of drug samples sampling. Finally, conferences, publications, advertisements, and other announcements represent the third external information source. Because this information source usually pertains to alternative drugs and treatments other than the focal drug, we refer to this as competitive activities. Given the existing medical conditions of the patients, physician i's preference for the focal drug $Q _ { i t }$ is modeled as the following:

$$
Q _ {i t} = G _ {i} Q _ {i, t - 1} + \beta_ {1 i} d _ {i t} + \beta_ {2 i} s _ {i t} + \beta_ {3 i} c _ {i t} + \nu_ {i t},\tag{3}
$$

where $d _ { i t } , s _ { i t } ,$ and $c _ { i t }$ are the detailing, sampling, and competitive activities that physician i experiences about the focal drug during period t and $\beta _ { 1 i } , \beta _ { 2 i } ,$ and $\beta _ { 3 i }$ are the corresponding response coef<sup>fi</sup>cients associated with these activities. According to Eq. (3), positive response coef<sup>fi</sup>cients for sampling, detailing, and competitive activities reinforce a physician's preference for the focal drug.

The physician preference $( Q _ { i t } )$ is a function of past preference $( Q _ { i , t - 1 } )$ carried over to the next period subject to a coef<sup>fi</sup>cient $G _ { i } ,$ which is a physician-speci<sup>fi</sup>c decay coef<sup>fi</sup>cient that captures the impact of a physician's habits (past beliefs and preferences) on the current preference for the focal drug. According to prior research, physician behavior is driven to a large extent by past beliefs [22,25,28,31]. Fiscella et al. [31] argue that risk-averse physicians are more likely to discount their prior beliefs and seek additional information. Davis et al. [25] suggest that experienced physicians are more likely to believe that they already operate at or near optimum levels (which they term “ceiling effects”). That is, what physicians already know plays a major role in shaping their future behavior. Because physicians also exhibit differences in their cognitive <sup>fl</sup>exibility to assimilate new information, they differ in terms of how long they preserve their old habits in light of new information. In our model, a physician with a high carryover coef<sup>fi</sup>cient G (closer to one) tends to repeat previous prescription choices frequently. In general, physicians with a high $G _ { i } / \beta _ { . i }$ ratio are more likely to exhibit “ceiling effects.” A high $G _ { i }$ suggests that physician i relies heavily on past habits, and a low β represents a low response to new information.

The term $\nu _ { i t }$ in Eq. (3) represents the drug administration uncertainty, which is physician i's uncertainty about how to administer the focal drug after deciding to prescribe it to the patients in period t. The effectiveness of the focal drug is closely related to its correct use, which requires identifying the correct dosage, frequency, route, and length of therapy. For example, statin drugs are frequently used to treat cardiovascular problems. They come in various dosages from as low as 5 milligrams to 80 milligrams with various usage frequencies. Wrong dosage and frequency decisions present signi<sup>fi</sup>cant health risks. For example, a wrong drug dosage when treating bipolar disorders leads to signi<sup>fi</sup>- cant complications and side effects, such as thyroid problems, stomach pain, drowsiness, and memory and concentration dif<sup>fi</sup>culties that may even lead to suicide and loss of life.<sup>4</sup>Similar to the drug selection uncertainty $\omega _ { i t } ,$ the drug administration uncertainty $\nu _ { i t }$ is also physician speci<sup>fi</sup>c.

## 2.2. Impact of DSS

As discussed previously, the use of DSSs can improve drug selection and administration decisions. Recall that physicians face various degrees of uncertainties when selecting $( \omega _ { i t } )$ and administering $( \nu _ { i t } )$ the focal drug. The effectiveness of decision support for drug selection and administration varies depending on the sophistication of the DSS features.

The effectiveness of the DSS in reducing the drug selection uncertainty is captured by $\gamma ,$ where $0 { < } \gamma { < } 1$ . Let the drug selection uncertainty $\omega _ { i t }$ follow a normal distribution with mean zero and variance $\gamma W _ { i } ,$ where $W _ { i } { > } 0$ . Physicians rely on their own professional knowledge in the absence of a DSS. This is the case in which γ equals one and the uncertainty is captured by the physician-speci<sup>fi</sup>c variance $W _ { i \cdot }$ Conversely, a low γ value indicates that the DSS is effective in identifying the most appropriate drug and recognizing important and relevant side effects given the patient pro<sup>fi</sup>le. This is equivalent to using an advanced DSS that makes appropriate drug recommendations as well as executes all the necessary checks, such as drug allergies and drug–drug interactions.

The effectiveness of the DSS in reducing the drug administration uncertainty is captured by δ. Similar to the preceding discussion, we let the uncertainty $\nu _ { i t }$ follow a normal distribution with $N ( 0 , \delta V _ { i } )$ where, $\ 0 { < } \delta { < } 1$ and $V _ { i } > 0 .$ . As δ decreases toward zero, the DSS gets better at identifying and minimizing errors related with the administration of the focal drug. An intermediate δ value can be viewed as using a DSS that is effective in recommending the appropriate drug dosage and frequency, but perhaps not so effective in suggesting the route and length of therapy when treating the existing condition with the focal drug. A DSS with a low δ value would make appropriate recommendations in all aspects of drug administration.

Note that consistent with Dreiseitl and Binder's [27] evidence, a physician with a high degree of uncertainty $( V _ { h } , W _ { h } )$ in our setting bene<sup>fi</sup>ts more from the use of a DSS than a physician with a low degree of uncertainty $( V _ { l } , W _ { l } )$ , given $( 1 - \delta ) ( V _ { h } - V _ { l } ) > 0$ and $( 1 - \gamma ) ( W _ { h } - W _ { l } ) > 0$ . Drug selection and drug administration uncertainties vary at the physician level to allow each physician to bene<sup>fi</sup>t differently from computerized decision support on drug selection and drug administration [62].

## 2.3. Clinical learning about the focal drug

So far, the process has captured prescription behavior independent of the clinical learning about the focal drug that occurs through the observation of the clinical outcomes. In the basic model presented in Eq. (2), the physicians use the external information sources but not the information obtained through the clinical experience. In reality, each physician likely develops an intrinsic preference about a drug based on the clinical experience with the patients. Physicians observe their patients while searching for the right drugs and dosages to improve treatment outcomes and eliminate potential problems [67]. For example, if a physician discovers that the focal drug being used for the treatment of the existing condition is leading to certain adverse side effects among the patients, the physician will likely revise his or her preference for the drug for future reference. Alternatively, a repeated positive experience with a focal drug may lead a physician to prescribe the drug even more frequently. In what follows, we propose a mechanism that captures the role of a DSS as well as other salient factors on physician-level learning. In the model, physicians vary in terms of the bene<sup>fi</sup>t they derive from computerized decision support, data analysis, and interpretation [5,27].

Physicians incorporate their clinical experiences into their prescription preferences using a Bayesian updating rule. The use of Bayesian updating has been advocated in modeling physician learning [52]. We present the preference updating process and our model in Fig. 1. Physicians start each period with a prior preference for the focal drug. Using the clinical experience in a given period, each physician updates the prior preference to form a posterior preference, a process that is repeated every period. Let physician i's prior preference at time t be denoted by $Q _ { i , t \mid t - 1 }$ . The index t|t–1 indicates that the updating process involves the clinical information gathered until the end of period t–1 but excludes the clinical information obtained in period t. Here, $Q _ { i , t \mid t - 1 }$ is a function of physician i's posterior preferences at the end of period $t - 1 ( Q _ { i , t - 1 | t - 1 } ) .$

Consider the end of period t–1 when the physicians incorporate all the information and establish the posterior preference $Q _ { i , t - 1 | t - 1 } \left( { \sec { \mathrm { F i g } } } . 1 \right)$ Let $Q _ { i , t - 1 | t - 1 }$ follow a normal distribution with $N ( M _ { i , t - 1 | t - 1 } { R } _ { i , t - 1 | t - 1 } ) .$ Then, the mean and variance of physician i's prior preference at the start of period t, $Q _ { i , t | t - 1 } ,$ , are given by the following:

$$
M _ {i, t | t - 1} = G _ {i} M _ {i, t - 1 | t - 1} + \beta_ {1 i} d _ {i t} + \beta_ {2 i} s _ {i t} + \beta_ {3 i} c _ {i t},\tag{4}
$$

![](/api/attachments/SH46ERUR/fulltext/images/b5240df7799ff263fd418378406bb7ea0a0557caad29bfc8b7152b22716ef7a5.jpg)  
Fig. 1. Preference updating process (subscript i denotes physician).

$$
R _ {i, t | t - 1} = G _ {i} ^ {2} R _ {i, t - 1 | t - 1} + \delta V _ {\mathrm{i}}.\tag{5}
$$

According to Eq. (4), the mean of the prior preference $M _ { i , t \mid t - 1 }$ depends on the mean of the posterior preference $M _ { i , t - 1 | t - 1 }$ , as well as information signals from the most recent information $( d _ { i t } , s _ { i t } , c _ { i t } )$ The uncertainty associated with the prior preference is re<sup>fl</sup>ected in the expression for $R _ { i , t \mid t }$ <sub>−1</sub> in Eq. (5). Eqs. (4) and (5) together capture all the information a physician receives, with the exception of the impact of the most recent clinical experience and learning.

The term $Q _ { i , t \mid t }$ denotes the posterior preference updated after the observation of the clinical experience by the physician during period t. Let ϕ represent the observed outcome at the end of this period. Then, the distribution of the posterior is given by $Q _ { i , t | t } { \sim } N ( M _ { i , t | t } , R _ { i , t | t } )$ where

$$
M _ {i, t | t} = M _ {i, t | t - 1} + K _ {i t} \Big (\phi_ {i t} - M _ {i, t | t - 1}),\tag{6}
$$

$$
R _ {i, t | t} = R _ {i, t | t - 1} - K _ {i t} R _ {i, t | t - 1},\tag{7}
$$

and $K _ { i t }$ is the clinical learning coef<sup>fi</sup>cient for physician i during period t. The term $K _ { i t }$ captures the extent to which clinical observations are integrated with physician i's preference for the focal drug in period t, and we de<sup>fi</sup>ne $K _ { i t }$ as follows:

$$
K _ {i t} = \frac {R _ {i , t | t - 1}}{R _ {i , t | t - 1 + \gamma W _ {i}}}.\tag{8}
$$

We obtain Eqs. (6)–(8) using the Kalman <sup>fi</sup>ltering technique, which requires marginalizing a joint normal distribution. Kalman <sup>fi</sup>ltering is commonly employed in the individual (patient) learning literature [1,23]. We provide the details of the derivation and a brief introduction to Kalman <sup>fi</sup>ltering in Appendix A.

## 2.4. An analysis of the physician clinical learning

Eqs. (6)–(8) jointly represent the clinical learning mechanism. First, we discuss how these equations represent the clinical learning behavior of physicians. Second, we investigate how the two types of DSS features interact with the clinical learning behavior.

The term $\left( \phi _ { i t } - M _ { i , t | t - 1 } \right)$ in Eq. (6) represents the information discrepancy between the observed outcome $\phi _ { i t }$ at the end of period t and the mean value of prior preference (see Eq. (4)) $M _ { i , t \mid t - 1 }$ at the start of period t. The change in posterior mean $M _ { i , t \mid t }$ in Eq. (6) depends on the sign of this discrepancy. For example, many failed therapies across the patient pro<sup>fi</sup>le using the focal drug are equivalent to a negative $\left( \phi _ { i t } - M _ { i , t | t - 1 } \right)$ , which gets incorporated into the future preference for the focal drug as part of the learning process. Such a clinical observation reduces the posterior mean $M _ { i , t \mid t }$ according to Eq. (6).

Eq. (7) shows that the posterior variance drops as new information is acquired. Over time, physicians gain clinical experience and reduce their uncertainties on the drug's performance and its <sup>fi</sup>t to their patients. Note that the posterior uncertainty $( R _ { i , t | t } )$ decreases in proportion to the prior uncertainty $( R _ { i , t | t - 1 } ) .$ . Because of the dynamic nature of the process, the information obtained early on (under a relatively high level of uncertainty) affects physician con<sup>fi</sup>- dence more than the information obtained later (when the degree of uncertainty is relatively lower).

We also observe in Eqs. (6) and (7) that the extent to which a physician relies on new clinical experience in updating the preference is determined by the value of the learning coef<sup>fi</sup>cient $K _ { i t } .$ The learning coef<sup>fi</sup>cient represents the weight attached by physician i to the information signals received through clinical experience when integrating the new information. The term $K _ { i t }$ ranges from zero to one depending on the uncertainty levels $( R _ { i , t | t - 1 }$ and $\gamma W _ { i } )$ , as speci<sup>fi</sup>ed by Eq. (8).

Note that $K _ { i t }$ drops as physicians reduce their uncertainty with clinical experience (see Eq. (8)), limiting the role of new information in the updating process. The impact of the DSS features on clinical learning varies for each physician [5,27] through the physician-speci<sup>fi</sup>c $K _ { i t } .$

Fig. 2a illustrates the benchmark case for a given physician with no impact of clinical experience. The horizontal axis represents the period, and the vertical axis represents the focal drug prescriptions. The solid line represents the prescription level based on clinical guidelines, which incorporate the relevant compliances and agreed-on treatment protocols by the experts. Note that in Fig. 2a the physician prescribes the focal drug at a strictly lower rate than what an expert panel would, as the dotted curve titled Physician Prescription Preference indicates. Because the physician does not learn from clinical observations, the physician prescriptions represented by the dotted curve continue to remain well below the prescriptions based on the clinical guidelines. The difference between the two is represented by the long dashed curve, which should trend lower if the physician were to bene<sup>fi</sup>t from the information gained through clinical experience.

In Fig. 2b, we provide a similar graph that shows the trend of the prescriptions across time, but in this case with an active learning mechanism. Contrary to the case with no clinical learning, the difference between the actual preference and the prescription level based on clinical guidelines eventually disappears over time, and the long dashed curve approaches zero.

If a physician effectively uses new information for learning, the difference in Fig. 2b is quickly minimized, and thereafter the physician prescriptions closely follow the prescriptions based on clinical guidelines. This is the case in which the $K _ { i t }$ coef<sup>fi</sup>cient in Eq. (8) is high, suggesting a signi<sup>fi</sup>cant level of Bayesian updating through Eq. (6) and, thus, the quick approach of the long dashed curve to zero in Fig. 2b. Below we state our <sup>fi</sup>rst proposition. The proof is in Appendix A.

![](/api/attachments/SH46ERUR/fulltext/images/e4802141207f6b33a1c01428ae22fe4f8e8d2980c899c4f4a9b355007015b2c3.jpg)  
Fig. 2. An Illustration of Prescription Behavior Model. Fig. 2a: Prescribing the focal drug: No impact of clinical experience. Fig. 2b: Prescribing the focal drug: With clinical learning.

Proposition 1. Using a DSS does not positively contribute to physician learning, even if it reduces the drug administration uncertainty, unless it also reduces the drug selection uncertainty.

Proposition 1 provides new insights with implications on how and when to use DSSs for prescription purposes. Consider a physician who compares the initial preference for a focal drug with the observed prescription outcome associated with the use of the drug and identi<sup>fi</sup>es the discrepancy between the two. Such a mental exercise would enable the physician to decide how to modify future prescriptions depending on the weight he or she assigns to the clinical observation. When a physician experiences a high level of drug selection uncertainty, and the patient–drug match is in doubt (i.e., high $\gamma ) ,$ the clinical experience that takes place in period t has a limited effect on the preference updating process. Note that $K _ { i t }$ decreases with γ (see the proof of Proposition 1). Drug interactions and different patient lifestyles may prevent physicians from observing all the relevant information and, in turn, limit their ability to update their preferences for the focal drug (low $K _ { i t } )$ . When the drug selection uncertainty is high, a physician will not be able to accurately infer the success of his or her administration of the focal drug. Consequently, clinical learning and the level of change in future prescription behavior will be limited.

An implication of Proposition 1 is that seasoned physicians who prefer to operate according to their past habits do not constitute an appropriate target population in terms of DSS adoption. Experienced physicians may prefer to follow the suggestions of a DSS only after selecting the drug or may not pay any attention to the DSS at all [27,62]. In such cases, given the DSS's limited impact on the drug selection decision (i.e., γ is close to one), the overall impact of the DSS on physician learning will also be limited. The physicians may even view the DSS as a nuisance and hassle. Even if the DSS makes relevant recommendations on drug administration, the physicians are not likely to obtain any long-term bene<sup>fi</sup>t because of the limited learning.

A few other studies have also reported that the use of DSS may not improve prescription outcomes and may even be perceived as counter-productive by physicians. In the context of health care, Lindgaard et al. [52, p. 526] examine the importance of the diagnosticity of information, which they and Wells and Lindsay [72, p. 778] de<sup>fi</sup>ne as “how much impact a datum should have in revising one's opinion on an issue without regard to what the prior odds are.” They show that when the diagnosticity of the new information provided by the DSS is low, physicians do not internalize the information and make biased decisions. In our context, low diagnosticity (and, thus, limited learning) occurs when the DSS fails to provide reliable information that boosts physicians' con<sup>fi</sup>dence in the appropriateness of the focal drug for the patients. Lerch and Harter [50] observe through experiments that it may be dif<sup>fi</sup>cult to improve learning with a DSS under dynamic, real-time environments. Furthermore, they <sup>fi</sup>nd that certain types of cognitive support can degrade decision makers' performance in the presence of time pressure. In a similar vein, Williams et al. [74] examine the effect of DSS use on decision makers' error patterns and decision quality. They <sup>fi</sup>nd that the accidental effects (e.g., mechanical errors) introduced by a DSS may lead to lower-quality decisions and thus defeat the purpose of using the system. Coiera et al. [21] <sup>fi</sup>nd that some physicians may commit new types of error biases (e.g., automation) because of using a DSS, in which decision makers miss important information because the system does not prompt them. They may also commit errors of commission, in which they do what the decision aid tells them to do even when this contradicts their training and other available data [20]. Thus, the evidence suggests that in some cases, DSS use may increase the number of decision errors or introduce new types of errors. According to Proposition 1, the best approach to prevent such negative, unintended outcomes is to ensure that the use of the DSS is associated with reduced drug selection uncertainty.

So far, we have considered the impact of DSS use on drug selection and administration decisions separately; we now analyze the impact of a simultaneous improvement in the two types of decisions due to the DSS. Consider an advanced DSS that reduces both drug selection and drug administration uncertainties, and let the capabilities of the DSS be represented by the parameters $\gamma _ { 1 }$ and $\delta _ { 1 } .$ . Let the capabilities of a less advanced DSS be represented with $\gamma$ and $\delta ,$ where $\gamma _ { 1 } < \gamma$ and $\delta _ { 1 } { < } \delta . \mathsf { W e }$ present our next result below. The proof is in Appendix A.

Proposition 2. Consider a DSS (represented with parameters γ and $\delta _ { 1 } )$ that reduces drug selection and drug administration uncertainties more than another (less advanced) DSS (represented with parameters γ and δ), where $\gamma _ { 1 }$ bγ and $\delta _ { 1 } < \delta _ { * }$ The more advanced DSS facilitates the clinical learn ing more than the less advanced DSS $i f$ and only if the change in the physician's drug selection uncertainty is elastic with respect to the change in drug administration uncertainty such that $\left( \frac { \gamma - \gamma _ { 1 } } { \gamma } \right) / \left( \frac { \delta - \delta _ { 1 } } { \delta } \right) > 1$

Proposition 2 provides the condition which ensures that the improvements in decision support contribute to long-term improvements in physician behavior. In other words, this condition suggests that the reduction in the drug selection uncertainty due to the improvements in decision support should be more than the reduction in the drug administration uncertainty. Proposition 2 further emphasizes the notion that not all DSS improvements bene<sup>fi</sup>t physicians. DSS capabilities should ensure that physician con<sup>fi</sup>dence in the drug choice is reinforced (e.g., by improving the decision support on drug–drug interactions and other side effects). Without such an improvement, physician learning will not be facilitated even with more advanced DSS capabilities.

In line with Lindgaard et al.'s [52] terminology, an implication of Propositions 2 is that improvements in DSS capabilities should aim to increase the diagnosticity of new information for the physicians. Better diagnosticity through improved DSS features requires reducing the drug selection uncertainty more than the drug administration uncertainty. Another implication is that the identi<sup>fi</sup>cation of the right set of physicians and use occasions (which exhibit a high degree of initial drug selection uncertainty) is critical from an adoption perspective. For example, Mikulich et al. [56] report that physicians who specialize in pediatric fever and low back pain do not prefer to use a DSS, whereas physicians who specialize in occupational exposure to blood or body <sup>fl</sup>uid always use a DSS. This suggests that physicians bene<sup>fi</sup>t from computerized decision support relatively more when dealing with complex issues that involve a high degree of uncertainty on the initial treatment selection.

Fig. 3 illustrates the discrepancy between the physicians' prescriptions of the focal drug and the prescriptions based on clinical guidelines under various DSS scenarios. Recall that the DSS has no impact on physicians' prescribing behavior when δ=1 and $\gamma = 1$ . The long dashed curve in the <sup>fi</sup>gure represents the base case with no DSS. The dotted curve represents the case in which the DSS effectively supports the drug administration decisions only (δb1 and $\gamma = 1 )$ . Although the dotted curve trends toward zero, the trend is slower than that in the baseline case with no DSS (see the dotted curve versus the long dashed curve in Fig. 3). Thus, the discrepancy between physician prescriptions and the prescriptions based on clinical guidelines is higher than it is in the base case. In other words, improving only drug administration decision support is not effective, because in this case, physicians discount their clinical observations relatively more.

Reducing the selection uncertainty $( \gamma < 1 )$ through computerized decision support enables physicians to better extract valuable information from their clinical observations and integrate it ef<sup>fi</sup>ciently with their overall treatment preferences. In turn, this results in the relatively quick elimination of the discrepancy between actual physician behavior and best practices. The discrepancy is minimized when the DSS effectively reduces both types of uncertainties (see the solid line in Fig. 3).

Table 2 Descriptive statistics.

![](/api/attachments/SH46ERUR/fulltext/images/d7b454854ccdce9257781085cbb1e0159cd789d5d33e949698fe0c107ae410b0.jpg)  
Fig. 3. Difference between preference and clinical guidelines for different DSS features.

## 3. Data

A large pharmaceutical company (hereinafter referred to as the “focal <sup>fi</sup>rm”) in the United States provided the data set, which includes individual physician prescription records in a therapeutic category. The focal <sup>fi</sup>rm produces and markets one (focal) drug in the category; there are no generic alternatives. The annual combined sales of all the drugs in the category are \$4.1 billion. The patients who require treatment in this category suffer from chronic diseases.

The data include the number of new prescriptions written by each physician in the sample during each month between 2001 and 2003. The data also include the number of details (visits by sales representatives) and the number of drug samples received by each physician per month. Furthermore, the data contain information on each physician's specialty and location by zip code. General practice physicians, whom we also refer to as generalists, are distinguished from specialists who possess expertise in the therapeutic area. Our sample includes a nationwide representative sample of 1000 physicians. The physicians in the sample wrote prescriptions each month and were detailed at least three times during the observation period. We augmented the data made available by the pharmaceutical <sup>fi</sup>rm with secondary data on per-capita income and urbanicity index of each zip code in which the physicians in our sample are located. Table 2 presents a summary of the descriptive statistics.

The focal drug was launched in 1997. The chemical formulation behind the drug was <sup>fi</sup>rst approved for the prevention of a condition and was later extended to the treatment of the same condition two years after its introduction to the market. The focal drug is the fourth-most popular drug in the market with a 14 percent market share. The <sup>fi</sup>rst-, second-, and third-most popular drugs had average market shares of 32 percent, 18 percent, and 15 percent, respectively, during the observation period. The combined sales volume of all the drugs in the category and the market shares were fairly stable during this period. Altogether, there were nine different drugs in the category. Although these drugs treat the same condition, each drug requires a different treatment plan with different side effects, speed of onset, and length of therapy.

## 3.1. Model specification

We operationalize the variables for the external information sources in Eq. (2) as follows: Detailing is represented by the variable $d _ { i t } ,$ which denotes the monthly detailing effort directed at physician i by the focal <sup>fi</sup>rm during period t. We use the natural logarithm of detailing to adjust for diminishing marginal returns [11]. The second variable s denotes the focal <sup>fi</sup>rm's sampling activity directed at physician i during period t. Often, the drug representatives hand out samples to physicians during their sales visits. However, we also observe a few cases in our data in which sampling takes place in the absence of detailing activities. It is likely that some samples may have been delivered by mail or dropped off in the of<sup>fi</sup>ces. Note that the correlation coef<sup>fi</sup>cient between detailing and sampling is 0.30. Because heavy sampling usually accompanies detailing, we normalize the number of samples by the details received by physician i in the same period. A natural logarithm transformation accounts for the diminishing marginal returns for the sampling effort. We expect the signs of both the detailing coef<sup>fi</sup>cient, $\beta _ { 1 i }$ and the sampling coef<sup>fi</sup>cient, $\beta _ { 2 i } ,$ , to be positive [33]. The <sup>fi</sup>nal variable in Eq. (2) is the competitive marketing activities that represent other treatments and drugs. Information obtained on competing treatments is likely to play a role in in<sup>fl</sup>uencing physicians' preferences for the focal drug. In line with the work of Mizik and Jacobson [59], we use the number of prescriptions for closely competing treatments as a proxy for their competitive detailing and sampling activities. To remove the effects of drug-speci<sup>fi</sup>c <sup>fi</sup>xed factors that account for the baseline demand, following Boulding and Staelin [12], we take the <sup>fi</sup>rst difference of the prescriptions of the main competing drugs and divide it by the total category prescription volume to construct the third variable $c _ { i t } .$ We expect the sign of the estimate for the corresponding coef<sup>fi</sup>cient to be negative.

<table><tr><td>Variable</td><td>Mean</td><td>Std dev</td><td>Min</td><td>Max</td></tr><tr><td>Total number of overall category Rx per physician (monthly)</td><td>16.75</td><td>5.12</td><td>5.83</td><td>33.00</td></tr><tr><td>Total number of focal drug Rx per physician (monthly)</td><td>2.34</td><td>0.84</td><td>0.48</td><td>6.65</td></tr><tr><td>Average number of details per month</td><td>2.33</td><td>1.30</td><td>0.09</td><td>8.74</td></tr><tr><td>Average number of samples per month</td><td>2.51</td><td>2.38</td><td>0</td><td>10.47</td></tr><tr><td> $Specialty^a$  (0 or 1)</td><td>0.22</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td> $Urbanicity^b$  (0 or 1)</td><td>0.75</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td> $Income^c$  (0 or 1)</td><td>0.44</td><td>0.48</td><td>0</td><td>1</td></tr></table>

<sup>a</sup> Equals one for specialists and zero otherwise  
b Equals one for urban locations and zero otherwise. We obtained the urbanicity measure from the WWAMI Rural Health Research Center Web site. We assigned a value of 1 to an area if it was designated as an “urban core” area (i.e., 1.0 and 1.1 as de-<sup>fi</sup>ned in RUCA) and a value of 0 if otherwise. For details, please refer to http:// www.fammed.washington.edu/wwamirhrc.  
<sup>c</sup> Equals one for high income areas and zero otherwise. We classi<sup>fi</sup>ed each area represented by a zip code as being “low” or “high” in terms of the income of the residents in that area. We designated an area as low income if the average income of residents was less than \$36,360, and vice versa.

We use the observable physician characteristics to explain the unobserved heterogeneity in $\beta _ { i }$ and $G _ { i }$ in Eq. (2). This is similar to Rossi et al. [66]. Speci<sup>fi</sup>cally, we have the following:

$$
\beta_ {i} = \Theta^ {'} Z _ {1 i} + \tau_ {i},\tag{9}
$$

$$
G _ {i} = \Delta^ {'} Z _ {2 i} + \lambda_ {i},\tag{10}
$$

where τ and λ follow i.i.d. normal distributions with N(0, T) and N(0, Λ). We use an intercept and three demographic variables to construct both $Z _ { 1 i }$ and $Z _ { 2 i }$ variable vectors: the physician's specialty, per capita income, and urbanicity of the area in which a physician is located. We meancenter all the aforementioned demographic variables.

## 3.2. Model estimation

We estimate the model using a hierarchical Bayesian technique that involves a Markov chain Monte Carlo (MCMC) simulation. The MCMC techniques are powerful in capturing unobserved heterogeneity at the individual level [19,65]. The essential approach is to iteratively sample from the marginalized posterior distributions, given all the other parameters, until the estimates of the model parameters reach a steady state across successive samples. The samples obtained in this steady state provide a sample from the joint distribution of the parameters. We use the Metropolis algorithm to draw from the posterior densities when distributions do not represent conjugate pairs. We use the Gibbs sampler to obtain the draws for the rest of the parameters [18]. To demonstrate that the estimation procedure can indeed recover the true values of parameters, we estimate the model using simulated data. Overall, the simulation results reveal that the estimation procedure can successfully recover the true parameter values. The estimation procedure follows the established steps in the previous literature (see, e.g., the appendix in [2]). We provide the exact details in Appendix B.

## 4. Empirical results

Table 3 presents the estimates. The rows in Table 3 represent the mean estimates obtained over all physicians associated with the response parameters β , β , β and the $G _ { i }$ coef<sup>fi</sup>cient, see Eq. (3). Recall that our model incorporates a hierarchy on the individual-level response parameters. Speci<sup>fi</sup>cally, the physician-level parameters $\beta _ { 1 i }$ $\beta _ { 2 i } , \beta _ { 3 i }$ and $G _ { i }$ are estimated using Eqs. (9) and (10) as functions of an intercept term, and specialty, urbanicity and local income. The columns in Table 3 represent these values.<sup>5</sup>We observe that the mean response for the detailing parameter $( \beta _ { 1 } )$ is positive and statistically signi<sup>fi</sup>cant and that all physicians in our sample have a positive response coef<sup>fi</sup>- cient. This indicates that the physicians use the detailing by the pharmaceutical company as a signi<sup>fi</sup>cant source of information regarding the drug's efficacy. As Table 3 shows, detailing efforts tend to have a stronger effect on specialists than on general practice physicians. This may be because specialists are more actively engaged in learning about new research <sup>fi</sup>ndings than general practice physicians. The mean estimate for the sampling variable coef<sup>fi</sup>cient $( \beta _ { 2 } )$ is positive and statistically signi<sup>fi</sup>cant. This reveals that sampling plays a signi<sup>fi</sup>cant role in helping physicians match patients with drugs (and thus helps them update their preferences). We also observe in Table 3 that the mean estimate for the competitive activities $( \beta _ { 3 } )$ is negative and statistically signi<sup>fi</sup>- cant. As expected, this suggests that such competitive activities have a negative impact on physicians' preferences for the focal drug. The mean estimate of the carrvover coefficient $G _ { i } \mathrm { i } s 0 . 6 4 .$ Overall, individual physicians show a relatively dispersed pattern of persistence in their preferences, with 15 percent of them having carryover coef<sup>fi</sup>cient estimates less than 0.5. This suggests that while a majority of the physicians have fairly stable preferences toward the drug, some physicians adjust their preferences relatively more over time. An examination of the profiles of physicians with low estimates of $G _ { i }$ reveals that specialists tend to have a signi<sup>fi</sup>cantly lower degree of carryover coef<sup>fi</sup>cients in their preferences than general practice physicians. This indicates that specialists are more active than general practice physicians in seeking information from various external sources, including drug representatives, in updating their preferences about the drug. Finally, we observe in Table 3 that physicians who practice in high-income areas have a significantly higher degree of carryover coef<sup>fi</sup>cient.

## 4.1. Clinical learning

We now turn to the estimates of the clinical learning parameter $K _ { i t } .$ Recall that this parameter represents the extent to which physician i relies on new clinical experience to update the focal drug's preference in period t (see Eqs. (6–8)). For each physician, we calculate the average value of the learning coef<sup>fi</sup>cient over all the periods (denoted by K). Across our sample of physicians, K ranges from 0.47 to 0.74 with a mean value of 0.60. There exists considerable heterogeneity among physicians in the clinical experience-based learning rates, with some physicians relying more on new clinical experience in updating their drug ef<sup>fi</sup>cacy preferences than others. This suggests that clinical experience provides varying learning opportunities to physicians, possibly because of the differences in their patient pro<sup>fi</sup>les and the level of access to other information sources. The empirical results in Table 3 suggest that specialty and local income have significant effects on physicians' information gathering and learning behavior. In speci<sup>fi</sup>c, we observe that general practice physicians rely more on clinical experience in updating their preferences about the focal drug than specialists. A possible reason driving this result is that the specialists may have accumulated more clinical experience than general practice physicians. We also observe that physicians located in high-income areas bene<sup>fi</sup>t more from clinical experience than others. This may be related to a more intense competition in such areas. For example, a large number of competing physicians and treatment alternatives may raise the importance of satisfying individual customer preferences. In addition, customers may be more educated and knowledgeable in high-income areas, and such a customer pro<sup>fi</sup>le may require physicians to focus relatively more on the clinical feedback and patient response.

Table 3 Empirical estimates<sup>a</sup>.

<table><tr><td>Coefficient</td><td>Mean value</td><td>Specialty</td><td>Urbanicity</td><td>Local income</td></tr><tr><td>detailing ( $\beta_1$ )</td><td>1.45*(0.05)</td><td>0.52*(0.11)</td><td>0.09(0.08)</td><td>-0.12(0.07)</td></tr><tr><td>sampling ( $\beta_2$ )</td><td>0.11*(0.02)</td><td>-0.05(0.05)</td><td>-0.07(0.05)</td><td>-0.003(0.05)</td></tr><tr><td>comp ( $\beta_3$ )</td><td>-0.39*(0.02)</td><td>0.01(0.06)</td><td>0.04(0.05)</td><td>0.05(0.05)</td></tr><tr><td>Carryover (G)</td><td>0.64*(0.01)</td><td>-0.13*(0.03)</td><td>-0.01(0.02)</td><td>0.06*(0.02)</td></tr></table>

\* Signi<sup>fi</sup>cant at 0.05 level.  
<sup>a</sup> Values in parentheses represent the standard deviations across physicians.

## 4.2. Clinical learning with DSS

We now investigate the effect of DSS use on the physician learning behavior. Recall that the parameters γ and δ are related to the DSS features that support drug selection and drug administration decisions, respectively. In Fig. 4a, we <sup>fi</sup>x the value of γ at one and vary δ to illustrate how the average learning coef<sup>fi</sup>cient (K) varies between specialists and generalists and between physicians in high- and low-income areas. Our clinical learning model suggests that the role of clinical learning is limited when physicians have an established preference on the focal drug. Thus, improving decision support for the administration of the focal drug (lower δ) strengthens physician preferences and, in turn, limits the contribution of clinical learning on the prescription behavior. As discussed previously and as Fig. 4a shows, generalists and physicians in high-income areas tend to rely more on their clinical experience (K values are higher). In Table 4a, we provide the percent changes on average learning coef<sup>fi</sup>cients for low and high values of δ. The table shows that the negative effect on clinical learning behavior is less pronounced for generalists and physicians in high-income areas. Thus, this observation also implies that generalists and physicians in high-income areas may bene<sup>fi</sup>t more from DSS drug administration features.

Next, in Fig. 4b, we <sup>fi</sup>x the value of δ parameter at one, vary γ, and plot the changes in the average clinical learning coef<sup>fi</sup>cients for generalists and physicians in high-income areas and for specialists and physicians in low-income areas. Table 4b provides a comparison of the changes in K values. Note that the specialists and physicians in low-income areas are more sensitive to changes in both δ and γ. This suggests that a DSS with drug selection features is likely to support the learning of specialists and physicians in low-income areas relatively more.

a) Effectiveness in Drug Administration  
![](/api/attachments/SH46ERUR/fulltext/images/52e6b55842d65ca0d0c35503648260a1425bc755f50818b86ccaa5bcf80f2406.jpg)

b) Effectiveness in Drug Selection  
![](/api/attachments/SH46ERUR/fulltext/images/2b4f3d072ddc0b1737ed6508071999ec359757c88e589e7f8b4b5fffcca611b5.jpg)  
Fig. 4. Changes in learning coef<sup>fi</sup>cient values as a function of different DSS effectiveness in reducing uncertainty. Fig. 4a: Effectiveness in drug administration δ\*. Fig. 4b: Effectiveness in drug selection $\gamma ^ { * } , \ ^ { * } \mathsf { A }$ low value represents a high level of effectiveness of DSS in reducing physicians' uncertainty.

## 5. Discussion and conclusion

Previous information systems research in health care has examined the business value of information technology [26] and its adoption within the sector [9,13,14,35,36,44,55,58,64]. We contribute to this literature by investigating when and how DSSs can improve physicians' clinical learning and thus improve their prescription decisions in terms of choosing and administering the right drug.

The results have implications on how to increase the perceived usefulness of the technology and facilitate adoption [20,60]. Bates et al. [8] indicate that physicians tend to be more pragmatic in their acceptance of the technology. The literature suggests that physicians value the usefulness of information technologies much more than their ease of use. Keil et al. [43, p. 89] note that “no amount of ease of use will compensate for low usefulness.” Usefulness is typically operationalized as increasing physicians' productivity, improving the quality of care, and enhancing their effectiveness. Because facilitating clinical learning is perhaps the most critical bene<sup>fi</sup>t of DSSs for physicians, we can argue that drug selection features are of paramount importance in the adoption of DSSs that are used in the prescription process.

Usefulness of DSSs is also critical from an educational perspective. Teich et al. [70] question whether DSSs really help the medical education of physicians-in-training. They acknowledge that DSSs improve care in the hospital, but they also suggest that it is not known how physicians perform in other settings without computerized decision support after having been trained with it. One possibility is that physicians learn some facts less well because of their growing dependence on the computer to supply important pieces of information. Another possibility is that clinical learning is enhanced because guidelines and recommendations are frequently re-presented and reinforced at crucial moments. By focusing on the bene<sup>fi</sup>ts of DSSs on clinical learning in this study, we tend to support the latter argument in that physicians should be able to carry over their improved skills to settings that lack a DSS.

Our learning model provides analytical justi<sup>fi</sup>cation for the existing empirical results in the literature that associate DSS adoption with reduced ADE rates. Differences in clinical use of DSSs have been documented empirically. For example, Grant et al. [34] <sup>fi</sup>nd that primary care physicians are associated with greater use of DSSs. The results of this study provide implications on which types of decision support offer more potential for which categories of physicians and, correspondingly, on which DSS implementations are more likely to fail. Despite the documented bene<sup>fi</sup>ts and the mandates, the widespread clinical acceptance of DSSs has been lacking, and this has been a concern for researchers and medical informaticians [4,40,42]. A recent study estimates that under current conditions, computerized order entry adoption in urban hospitals will not reach 80 percent penetration until 2029 [32]. There is a clear need to help facilitate the adoption, and our results can help policy makers design better incentives and mechanisms so that they can identify and target physicians who stand to bene<sup>fi</sup>t the most from computerized decision support.

Sensitivity analysis of estimated learning coef<sup>fi</sup>cients on γ and δ.

<table><tr><td colspan="4">Table 4a: Varying the effectiveness in drug administration δ (γ=1)</td><td colspan="4">Table 4b: Varying the effectiveness in drug selection γ (δ=1)</td></tr><tr><td>δ</td><td>Generalist</td><td>High income</td><td>Overall avg. K</td><td>γ</td><td>Generalist</td><td>High income</td><td>Overall avg. K</td></tr><tr><td>1</td><td>0.62</td><td>0.61</td><td>0.60</td><td>1</td><td>0.62</td><td>0.61</td><td>0.60</td></tr><tr><td>0.5</td><td>0.42</td><td>0.41</td><td>0.39</td><td>0.5</td><td>0.82</td><td>0.81</td><td>0.80</td></tr><tr><td>% Change</td><td>-32.22%</td><td>-32.60%</td><td>-33.75%</td><td>% Change</td><td>32.97%</td><td>32.66%</td><td>33.63%</td></tr><tr><td>δ</td><td>Specialist</td><td>Low income</td><td>Overall avg. K</td><td>γ</td><td>Specialist</td><td>Low income</td><td>Overall avg. K</td></tr><tr><td>1</td><td>0.57</td><td>0.58</td><td>0.60</td><td>1</td><td>0.57</td><td>0.58</td><td>0.60</td></tr><tr><td>0.5</td><td>0.37</td><td>0.38</td><td>0.39</td><td>0.5</td><td>0.77</td><td>0.78</td><td>0.80</td></tr><tr><td>% Change</td><td>-34.78%</td><td>-34.43%</td><td>-33.75%</td><td>% Change</td><td>35.79%</td><td>34.93%</td><td>33.63%</td></tr></table>

Our empirical estimations highlight the importance of physicianlevel differences and salient physician characteristics that affect clinical behavior and DSS use. Coscelli [22] argue that clinical DSSs should be viewed as socio-technical systems in which an individual physician's social background and demographics also play a role in the success of the adoption of the system. In a somewhat related vein, our results show that physician specialty and location have signi<sup>fi</sup>cant effects on the overall physician response to information sources and that the specialists and physicians in low-income areas are likely to bene<sup>fi</sup>t more from decision support on drug selection than general practice physicians and physicians located in high-income areas.

Ray et al. [63] report that more than one-quarter of of<sup>fi</sup>ce-based Tennessee physicians mis-prescribed an antibiotic (i.e., tetracycline), which is associated with permanent discoloration of developing teeth, to young children. The authors show that rural family and general practitioners faced a high risk of prescribing these and other agents (e.g., chloramphenicol) in a potentially unsafe manner. Such <sup>fi</sup>ndings illustrate that general practitioners may have more “room” for learning about pharmacology than specialists, in which case they may bene<sup>fi</sup>t more from computerized decision support over time, in line with our results. However, because DSS use lengthens the duration of a physician– patient encounter ([68] has shown that it takes 245 and 113 seconds to make a decision with and without the DSS, respectively), such bene<sup>fi</sup>ts may be dif<sup>fi</sup>cult to realize in low-income areas that typically exhibit relatively high demand for physician services. Thus, DSS developers should incorporate their products into physician work<sup>fl</sup>ows well, especially when targeting physicians who work in low-income areas.

This study offers several future research directions. An immediate application of the learning model presented herein is the individual identi<sup>fi</sup>cation of the physicians who would bene<sup>fi</sup>t the most from decision support and those who may be distracted by it. Such a targeted approach may facilitate the diffusion of DSS adoption and may provide new avenues to overcome the adoption dif<sup>fi</sup>culties [61]. Researchers can also apply our learning model to speci<sup>fi</sup>c types of DSSs to understand the role of more detailed aspects of these systems on physician learning. For example, researchers can examine, both analytically and by observing actual physician behavior, which types of DSSs (e.g., optimization systems, expert systems, and data mining tools) and which form of recommendation systems (e.g., those that employ collaborative-<sup>fi</sup>ltering versus content search through machine learning) are most promising from a learning perspective. Additionally, a similar methodology can be used to investigate the role of DSSs used for physician training. The dynamic nature of our model makes it a suitable framework for capturing the relative importance of external information sources (over time) in supporting physicians' prescribing decisions. A similar methodology can also be used to explore the optimal recency, frequency, and amount of training needed for each physician. Finally, with suitable modi<sup>fi</sup>cations, the methodology developed here can be applied to understand and improve the professional learning of other knowledge workers.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2012.10.045.

## References

[1] M.T. Akçura, F. Gönül, E. Petrova, Consumer learning and brand valuation: an application on over-the-counter drugs, Marketing Science 23 (1) (2004) 156–169.

[2] G.M. Allenby, P.J. Lenk, Modeling household purchase behavior with logistic normal regression, Journal of the American Statistical Association 89 (428) (1994) 1218–1231.

[3] E. Ammenwerth, P. Schnell-Inderst, C. Machan, U. Siebert, The effect of electronic prescribing on medication errors and adverse drug events: a systematic review Journal of the American Medical Informatics Association 15 (5) (2008) 585–600.

[4] In: J.G. Anderson, S.J. Jay (Eds.), Use and Impact of Computers in Clinical Medicine, Springer, New York, 1987.

[5] B.E. Barnes, Creating the practice-learning environment: using information technology to support a new model of continuing medical education, Academic Medicine 73 (3) (1998) 278–281.

[6] D.W. Bates, D.J. Cullen, N. Laird, et al., Incidence of adverse drug events and potential adverse drug events: implications for prevention, Journal of the American Medical Association 274 (1) (1995) 29–34.

[7] D.W. Bates, L.L. Leape, D.J. Cullen, et al., Effect of computerized physician order entry and a team intervention on prevention of serious medication errors, Journal of the American Medical Association 280 (15) (1998) 1311–1316

[8] D.W. Bates, J.M. Teich, J. Lee, et al., The impact of computerized physician order entry on medication error prevention, Journal of the American Medical Informatic Association 6 (1999) 313–321.

[9] A. Bhattacherjee, N. Hikmet, Physicians' resistance toward healthcare information technology: a theoretical model and empirical test, European Journal of Information Systems 16 (2007) 725–737.

[10] G.V. Bochicchio, P.A. Smit, R. Moore, et al., Pilot study of a web-based antibiotic decision management guide, Journal of the American College of Surgeons 202 (3) (2006) 459–467.

[11] E.W. Boehm, E.G. Brown, K. Molvar, Pharma's detailing overhaul, in: Forrester Report, February, 2001.

[12] W. Boulding, R. Staelin, Environment, market share, and market power, Management Science 36 (10) (1990) 1160–1177.

[13] J. Braa, E. Monteiro, S. Sahay, Networks of action: sustainable health information systems across developing countries, Management Information Systems Quarterly 28 (3) (2004) 337–362.

[14] J. Braa, O. Hanseth, A. Haywood, W. Mohammed, V. Shaw, Developing health information systems in developing countries, Management Information Systems Quarterly 21 (2) (2007) 381–402.

[15] J.P. Burke, S.L. Pestotnik, Antibiotic use and microbial resistance in intensive care units: impact of computer-assisted decision support, Journal of Chemotherapy 11 (6) (1999) 530–535.

[16] B.L. Carter, D.K. Helling, Ambulatory care pharmacy services: the incomplete agenda, The Annals of Pharmacotherapy (1992) 701–708.

[17] T.Y. Chan, B.H. Hamilton, Learning, private information, and the economic evaluation of randomized experiments, Journal of Political Economy 114 (6) (1996) 997–1040.

[18] G.M. Chertow, J. Lee, G.J. Kuperman, et al., Guided medication dosing for inpatients with renal insuf<sup>fi</sup>ciency, Journal of the American Medical Association 286 (2001) 2839-2844

[19] S. Chib, E. Greenberg, Markov chain Monte Carlo simulation methods in econometrics, Econometric Theory 12 (3) (1996) 409–431.

[20] W.G. Chismar, S.W. Patton, Does the extended technology acceptance model apply to physicians? in: Proceedings of the 36th Hawaii International Conference on System Sciences, 2003, (Waikoloa, HI).

[21] E. Coiera, J.I. Westbrook, J.C. Wyatt, The safety and quality of decision support systems, in: IMIA Yearbook of Medical Informatics, 2006, pp. 20–25

[22] A. Coscelli, The importance of doctors' and patients' preferences in the prescription decision, The Journal of Industrial Economics 48 (3) (2000) 349–369.

[23] A. Coscelli, M. Shum, An empirical model of learning and patient spillovers in new drug entry, Journal of Econometrics 122 (2004) 213–246.

[24] G.S. Crawford, M. Shum, Uncertainty and learning in pharmaceutical demand, Econometrica 73 (4)(2005)1137–1173.

[25] D.A. Davis, M.A. Thomson, A.D. Oxman, R.B. Haynes, Changing physician performance: a systematic review of the effect of continuing medical education strategies, Journal of the American Medical Association 274 (9) (1995) 700–705

[26] S. Devaraj, R. Kohli, Information technology payoff in the health-care industry: a longitudinal study, Journal of Management Information Systems 16 (4) (2000) 41–67.

[27] S. Dreiseitl, M. Binder, Do physicians value decision support? A look at the effect of decision support systems on physician opinion, Arti<sup>fi</sup>cial Intelligence in Medicine 33 (2005) 25–30.

[28] P. Duberstein, S. Meldrum, K. Fiscella, C.G. Shields, R.M. Epstein, Short communication in<sup>fl</sup>uences on patients' ratings of physicians: physicians demographics and personality, Patient Education and Counseling 65 (2007) 270–274.

[29] Y. Engeström, Expansive learning at work: toward an activity theoretical reconceptualization, Journal of Education and Work 14 (1) (2001) 133–156

[30] R.S. Evans, S.L. Pestotnik, D.C. Classen, T.P. Clemmer, L.K. Weaver, J.F. Orme, J.F. Lloyd, J.P. Burke, A computer-assisted management and other antiinfective agents, The New England Journal of Medicine (1998) 232–238.

[31] K. Fiscella, P. Franks, J. Zwanziger, C. Mooney, M. Sorbero, G.C. Williams, Risk aversion and costs: a comparison of family physicians and general internists, Journal of Family Practice 49 (1) (2000) 12–17.

[32] E.W. Ford, A.S. McAlearney, M.T. Phillips, N. Menachemi, B. Rudolph, Predicting computerized physician order entry system adoption in US hospitals: can the federal mandate be met? International Journal of Medical Informatics 77 (8) (2008) 539–545.

[33] F. Gönül, F. Carter, E. Petrova, K. Srinivasan, Promotion of prescription drugs and its impact on physicians' choice behavior, Journal of Marketing 65 (3) (2001) 79–90.

[34] R.W. Grant, E.G. Campbell, R.L. Gruen, T.G. Ferris, D. Blumenthal, Prevalence of basic information technology use by US physicians, Journal of General Internal Medicine 21 (11) (2006) 1150–1155

[35] N. Hikmet, A. Bhattacherjee, N. Menachemi, V. Kayhan, R.G. Brooks, The role of organizational factors in the adoption of healthcare information technologies in Florida hospitals, Health Care Management Science 11 (1) (2008) 1–9.

[36] P.J. Hu, P.Y.K. Chau, O.R.L. Sheng, K.Y. Tam, Examining the technology acceptance model using physician acceptance of telemedicine technology, Journal of Management Information Systems 16 (2) (1999) 91–112.

[37] D.L. Hunt, R.B. Haynes, S.E. Hanna, K. Smith, Effects of computer-based clinical decision support systems on physician performance and patient outcomes: a systematic review, Journal of the American Medical Association 280 (15) (1998) 1339–1346.

[38] B. Ives, S. Hamilton, G.B. Davis, A framework for research in computer-based management information systems, Management Science 26 (9) (1980) 910–934.

[39] D. Jonassen, L.R. Murphy, Activity theory as a framework for designing constructivist learning environment, Educational Technology Research and Development 47 (1) (1999) 61–79.

[40] B. Kaplan, Evaluating informatics applications—Clinical decision support systems literature review, International Journal of Medical Informatics 64 (2001) 15–37.

[41] R. Kaushal, D.W. Bates, Computerized physician order entry (CPOE) with clinical decision support systems (CDSSs), in: Managing Care Safer: A Critical Analysis of Patient Safety Practices, Evidence Report/Technology Assessment, No. 43, Agency for Healthcare Research and Quality, Rockville, MD, July 2001.

[42] R. Kaushal, K.G. Shojania, D.W. Bates, Effects of computerized physician order entry and clinical decision support systems on medication safety, Archives of Internal Medicine 163 (12) (2003) 1409–1416.

[43] M. Keil, P.M. Beranek, B.R. Konsynski, Usefulness and ease of use: <sup>fi</sup>led study evidence regarding task considerations, Decision Support Systems 13 (1) (1995) 75–91.

[44] K. Khoumbati, M. Themistocleous, Z. Irani, Evaluating the adoption of enterprise application integration in health-care organizations, Journal of Management Information Systems 22 (4) (2006) 69–108.

[45] R.C. Kirk, D.L.M. Goh, J. Packia, et al., Computer calculated dose in paediatric prescribing, Drug Safety 28 (9) (2005) 817–824.

[46] In: T. Kohn, J. Corrigan, M.S. Donaldson (Eds.), To Err Is Human: Building a Safer Health System, National Academy Press, Washington, DC, 2000.

[47] L. Landro, Incentives Push More Doctors to E-Prescribe, Wall Street Journal (January 21 2009) B7–B8.

[48] R.H. Leach, C. Feetam, D. Butler, An evaluation of a ward pharmacy service, Journal of Clinical and Hospital Pharmacy 6 (1981) 173–182.

[49] L. Leape, D. Bates, D. Cullen, et al., System analysis of adverse drug events, Journal of the American Medical Association 274 (1995) 35–43.

[50] J.F. Lerch, D.E. Harter, Cognitive support for real-time dynamic decision making, Information Systems Research 12 (1) (2001) 63–82.

[51] C. Lin, C.M. Lin, B. Lin, M. Yang, A decision support system for improving doctors' prescribing behavior, Expert Systems with Applications 36 (2009) 7975–7984.

[52] G. Lindgaard, C. Pyper, M. Frize, R. Walker, Does Bayes have it? Decision support systems in diagnostic medicine, International Journal of Industrial Ergonomics 39 (3) (2009) 524–532.

[53] P. Manchanda, Pradeep K. Chintagunta, Responsiveness of physician prescription behavior to salesforce effort: an ındividual level analysis, Marketing Letters 15 (2/3) (2004) 129–145.

[54] P. McCullagh, J.A. Nelder, Generalized Linear Models, Chapman and Hall, London, 1989.

[55] N. Menachemi, N. Hikmet, A. Bhattacherjee, A. Chukmaitov, R.G. Brooks, The effect of payer mix on the adoption of information technologies by hospitals Health Care Management Review 32 (2) (2007) 102–110.

[56] V.J. Mikulich, Y.A. Liu, J. Steinfeldt, D.L. Schriger, Implementation of clinical guidelines through an electronic medical record: physician usage, satisfaction and assessment, International Journal of Medical Informatics 63 (3) (2001) 169–178.

[57] A. Mirco, L. Campos, F. Falcao, et al., Medication errors in an internal medicine department: evaluation of a computerized prescription system, Pharmacy World & Science 27 (4) (2005) 351–352.

[58] G. Miscione, Telemedicine in the Upper Amazon: interplay with local health care practices, Management Information Systems Quarterly 31 (2) (2007) 403.

[59] N. Mizik, R. Jacobson, Are physicians ‘easy marks’? Quantifying the effects of detailing and sampling on new prescriptions, Management Science 50 (12) (2004) 1704–1715.

[60] C.S. Ong, Y.S. Wang, Factors affecting engineers' acceptance of asynchronous e-learning systems in high-tech companies, Information Management 41 (2004) 795–804.

[61] E.S. Patterson, A.D. Nguyen, J.P. Halloran, S. Asch, Human factors barriers to the effective use of ten HIV clinical reminders, Journal of the American Medical Association 11 (2004) 50–59.

[62] S.A. Pearson, A. Moxey, J. Robertson, I. Hains, Do computerised clinical decision support systems for prescribing change practice? A systematic review of the literature (1990–2007), Journal of BMC Health Services Research 9 (154) (2009) 1–14.

[63] W.A. Ray, C.F. Federspiel, W. Schaffner, Prescribing of tetracyclines to children less than 8 years of age in ambulatory practice-2-year epidemiologic-study among Tennessee Medicaid recipients, American Journal of Epidemiology 104 (3) (1976) 339–340.

[64] J.L. Reardon, E. Davidson, An organizational learning perspective on the assimilation of electronic medical records among small physician practices, European Journal of Information Systems 16 (2007) 681–694.

[65] P.E. Rossi, G.M. Allenby, Bayesian statistics and marketing, Marketing Science 22 (3) (2003) 304–328.

[66] P.E. Rossi, R.E. McCulloch, G.M. Allenby, The value of purchase history data in target marketing, Marketing Science 15 (4) (1996) 321–340.

[67] S.M. Shortell, C.L. Bennett, G.R. Byck, Assessing the impact of continuous quality improvement on clinical practice: what it will take to accelerate progress, The Milbank Quarterly 76 (4) (1998) 593–624.

[68] V. Sintchenko, V. Coiera, J.R. Iredell, G.L. Gilbert, Comparative impact of guidelines, clinical data, and decision support on prescribing decisions: an interactive Web experiment with simulated cases, Journal of the American Medical Informatics Association 11 (1) (2004) 71–77.

[69] S.B. Soumerai, T.J. McLaughlin, J. Avorn, Improving drug prescribing in primary care: a critical analysis of the experimental, The Milbank Quarterly 67 (2) (1989) 268–317.

[70] J. Teich, R. Pankaj, Merchia, J.L. Schmiz, G.J. Kuperman, C.D. Spurr, D.W. Bates, Effects of computerized physician order entry on prescribing practices, Archives of Internal Medicine 160 (2000) 2741–2747.

[71] C. van den Bulte, G.L. Lilien, Medical innovation revisited: social contagion versus marketing effort, The American Journal of Sociology 106 (5) (2001) 1409–1435

[72] G.L. Wells, R.C.L. Lindsay, On estimating the diagnosticity of eyewitness nonidenti<sup>fi</sup>cation, Psychological Bulletin 88 (3) (1980) 776–784.

[73] M.S. Willett, K.E. Bertch, D.S. Rich, L. Ereshefsky, Prospectus. The economic value of clinical pharmacy services: a position statement of the American College of Clinical Pharmacy, Journal of Pharmacotherapy 9 (1989) 45–56.

[74] M.L. Williams, A.R. Dennis, A. Stam, J.E. Aronson, The impact of DSS use and information load on errors and decision quality, European Journal of Operational Research 176 (1) (2007) 468–481.

M. Tolga Akçura is an Associate Professor of Marketing at Ozyegin University. Previously, he taught at Purdue University and Carnegie Mellon University. His research interests include information-intensive environments, database marketing, learning and structural choice models and competitive retailing strategies. He holds a B.Sc. and an M.A. from Bogaziçi University and a Ph.D. from Carnegie Mellon University. His research has been published in Management Science, Marketing Science, and Decision Support Systems among others.

Zafer D. Ozdemir is an Associate Professor at the Farmer School of Business, Miami University. He received his doctorate from Krannert Graduate School of Management, Purdue University. His research has been published in Information Systems Research, Journal of Management Information Systems, International Journal of Electronic Commerce, Decision Support Systems, Information & Management, Communications of the ACM, and Communications of the AIS, among others.
