---
otero_id: 20891
otero_key: "BA7A3S2P"
title: "Estimating drug/plasma concentration levels by applying neural networks to pharmacokinetic data sets"
authors: "Kristin M. Tolle; Hsinchun Chen; Hsiao-Hui Chow"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00094-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Estimating drug<sup>r</sup>plasma concentration levels by applying neural networks to pharmacokinetic data sets

Kristin M. Tolle <sup>a,)</sup>, Hsinchun Chen <sup>a,1</sup>, Hsiao-Hui Chow <sup>b,2</sup>

<sup>a</sup> MIS Department, Karl Eller Graduate School of Management, UniÕersity of Arizona, Tucson, AZ 85721, USA b College of Pharmacy, UniÕersity of Arizona, Tucson, AZ 85721, USA

## Abstract

Predicting blood concentration levels of pharmaceutical agents in human subjects can be made difficult by missing data and variability within and between human subjects. Biometricians use a variety of software tools to analyze pharmacokinetic information in order to conduct research about a pharmaceutical agent. This paper is the comparison between using a feedforward backpropagation neural network to predict blood serum concentration levels of the drug tobramycin in pediatric cystic fibrosis and hemotologic–oncologic disorder patients with the most commonly used software for analysis of pharmacokinetics, NONMEM<sup>w</sup>. Mean squared standard error is used to establish the comparability of the two estimation methods. The motivation for this research is the desire to provide clinicians and pharmaceutical researchers a cost effective, user friendly, and timely analysis tool for effectively predicting blood concentration ranges in human subjects. q 2000 Published by Elsevier Science B.V.

Keywords: Artificial neural networks; Medical applications; Medical user interfaces; Pharmaceutical estimation applications; Pharmacokinetic prediction

## 1. Introduction

Artificial neural networks, which have strong statistical prediction capabilities, continue to gain acceptance as data analysis tools. Testing in this and other research has shown that neural networks can be trained to estimate plasma concentration values of pharmaceutical agents without relying on complex computation models and<sup>r</sup>or cumbersome statistical prediction applications. If the need for complex modeling were eliminated, testing results could be generated more quickly and easily than it is accomplished using currently available technology.

Brier et al. 3 examined the use of neural net-<sup>w</sup> <sup>x</sup> works for population pharmacokinetic analysis, concluding that NONMEM and the neural networks provided comparable predictions of plasma drug concentrations. Our research question was to determine whether a neural network application specifically designed for the prediction of blood serum concentration levels of pharmaceutical drugs could be an effective replacement for current statistical analysis methodologies. Our goal was to create an intelligent tool that could assist clinicians in optimally administering drugs and provide pharmaceutical scientists with valuable data gathered in clinical settings, more promptly and efficiently.

In this paper, we first present a brief background description of pharmacokinetic analysis, statistical prediction methods, and neural networks. Next, we discuss an experiment in which we compared the predicative capability of a neural network application with NONMEM, the industry standard application currently used for pharmacokinetic data analysis. The paper then describes usability issues associated with a proposed neural network application, the user interface, the types of analysis for which it could be used to assist medical researchers and clinicians in their work, and the social implications of adopting the neural network application in place of NON-MEM and similar data analysis tools.

## 1.1. Background

## 1.1.1. Pharmacokinetic analysis

Pharmacokinetics is the study of how various biological processes influence the effectiveness of drugs — the quantifying of determinates of drug concentration.

Information about the proper administration of pharmaceutical drugs in clinical settings is obtained from varied sources. Some data are collected following a very formal set of procedures. Much of the information, however, must be obtained by observing the actual clinical administering of the drugs. However, the non-stringent nature by which clinical treatments are administered results in many of the data gathered in clinical settings being in a format which is not easily applicable to standardized statistical and data analysis.

Although clinical information gathering does not use rigorous methodology, data collected from clinical studies of pharmaceutic agents are still very useful to assist clinical physicians in modulating treatment dosages to patients in their care 13 . Such <sup>w</sup> <sup>x</sup> data record the administration of a drug to individuals and the subsequent observation of drug levels Ž . most often in blood plasma . The study of this type of information is referred to as Pharmacokinetics 2 .<sup>w</sup> <sup>x</sup>

In rigorous methods of gathering population data on a particular drug’s effects, an individual the Ž subject contributes one instance of information. In. clinical settings, a patient may contribute multiple instances of information, potentially occurring over an extended period of time, thereby creating the need for an analysis model, which takes into consideration a time series of responses — known as repeated measures. Related to this is the problem known as imbalance, in which one patient may contribute a series of data, while another patient may only produce one datum. A third issue, confounding, occurs when a patient is given specific dosages of a particular drug based on that patient’s prior reactions, in contrast to more stringent methods that require dosages to be given randomly 13 . These issues<sup>w</sup> <sup>x</sup> make it difficult to devise statistical analysis tools to predict pharmacokinetic parameters such as blood serum concentration levels, volume of distribution, and clearance how quickly a pharmaceutical agent Ž leaves the blood stream ..

Other data analysis problems stem from population within patient demographics such as age, Ž . weight, seriousness of the illness, gender, etc. Some demographic data may change during the period when treatment is administered, further complicating determination of the proper administration of drug dosages.

## 1.1.2. Statistical prediction methodologies

The current standard for the analysis of population pharmacokinetic data is the application NON-MEM, developed by the University of California at San Francisco. NONMEM is a data analysis technique for fitting nonlinear mixed effects statisticalŽ regression-type models that is mainly applied in the. estimation of pharmacokinetic and pharmacodynamic data 2 . NONMEM users must have high<sup>w</sup> <sup>x</sup> levels of understanding of statistics and pharmacokinetics 5 in order to use the application successfully.<sup>w</sup> <sup>x</sup> Furthermore, a user must initially determine the appropriate statistical model for the NONMEM program to use for data analysis before any interaction with an application is undertaken and this can take many hours or days to complete.

The UNIX version of NONMEM requires the use of FORTRAN-like commands Fig. 1 to convey Ž . modeling and data information to the application, which further complicates NONMEM usage. Only a small number of researchers in the field of biometrics have the skills needed to be proficient at pharmacokinetic data analysis using NONMEM, making them a scarce and expensive resource.

```txt
NONMEM code:
$PROBLEM MODEL FOR TOBRAMYCIN: CLEARANCE, LOG(WEIGHT) & AGE, VOLUME,
LOG(WEIGHT)
$INPUT ID AGE LNAG GEND DIS WT LNWT TIME UNDV DV AMT RATE SS II EVID
$DATA tobrt
$SUBROUTINE ADVAN1 TRANS2 DOUBLE
$PK
TVCL=THETA(1)*LNWT+THETA(3)*AGE
CL=TVCL*EXP(ETA(1))
TVVD=THETA(2)*LNWT
V=TVVD*EXP(ETA(2))
K=CL/V
S1=V
$ERROR
Y=LOG(F)+EPS(1)
$THETA (0,1.)(0,3.)(0,0.5)
$OMEGA 0.1, 0.1
$SIGMA 0.1
$ESTIMATION PRINT=5 POSTHOC
$COVR
$SCAT PRED VS DV UNIT
$SCAT RES VS DV
$SCAT ETA(2) VS AGE
$SCAT ETA(1) VS DIS
$SCAT ETA(2) VS DIS
$SCAT ETA(1) VS GEND
$SCAT ETA(2) VS GEND
```  
Fig. 1. An example of a NONMEM session.

Several other computerized methods of doing pharmacokinetic analysis exhibit varying degrees of usability and predictive capabilities, but Roe et al. 9<sup>w</sup> <sup>x</sup> found NONMEM to be more flexible, have fewer limitations in modeling of data, and be consistently more successful at predicting pharmacokinetic parameters than other similar applications. Since these are important issues to pharmaceutical researchers, NONMEM remains the accepted standard for conducting pharmaceutical studies.

## 1.1.3. Estimation using neural networks

Different models of neural networks exist. General details about artificial neural networks can be found in Ref. 11 . A taxonomy of the types of<sup>w</sup> <sup>x</sup> artificial neural networks can be found in Ref. 7 .<sup>w</sup> <sup>x</sup>

Our design employs a connectionist, feedforward<sup>r</sup> backpropagation neural network.

Since the predictive capability of neural networks is typically nonlinear, it is appropriate to explain that feedforward neural networks perform a kind of nonlinear regression in which a multilayer network is trying to find a low-order representation in the weights between the network layers. That representation itself is, in general, a nonlinear function of the physical input variables that allows for the interactions of relationships among many input variables at one time 10 . Thus, the inputs become dependent on<sup>w</sup> <sup>x</sup> one another through network interaction and ultimately, generate nonlinear estimations as output variables.

Backpropagation, selected for our design, is a neural networking algorithm in which activation is passed forward through the network and the output unit activations are compared with a teaching vector.

These represent the input<sup>r</sup>output pairs. The comparison of input<sup>r</sup>output pairs results in error scores, which are used to propagate changes back down through the layers of weights. Weights represent the numerical strength of the connections or links between a node and its neighbors in a neural network <sup>w</sup> <sup>x</sup> 1 and can have either positive or negative values <sup>w</sup> <sup>x</sup> 11 . These weights represent the AintelligenceB of the network — the essence of its predictive capability.

The role of an activation function is to combine the input being broadcast to a node from other nodes in a network. A typical activation function compresses the network activation impinging on a node between predetermined limits 1 — usually a value<sup>w</sup> <sup>x</sup> between zero and one. We chose a sigmoidal, or s-shaped, activation function on the basis of its excellent predictive capabilities demonstrated in a previous experiment involving the estimation of toxin concentration in soil samples 4 .<sup>w</sup> <sup>x</sup>

During the learning process, the sigmoidal unit is roughly linear for small weights a net input nearŽ zero and gets increasingly nonlinear in its response. as it approaches its points of maximum curvature on either side of the midpoint. Thus, at the beginning of learning, when weights are small, the system is mainly linear and seeking a linear solution. As the weights grow, the network becomes increasingly nonlinear and begins to move toward a nonlinear solution to the problem. This linearity property makes the units more robust and allows the network to reliably attain the same solution in repeated experimentation 10 . Thus, two different training sessions,<sup>w</sup> <sup>x</sup> using the same input data and randomly initialized weights, should consistently predict the same results.

## 1.1.4. Neural network parameters

The ability to train multilayer networks is an important step toward building intelligent applications. Neural networks must learn their own representations because it is not possible to program them by hand 8,10 . The optimization of neural network <sup>w</sup> <sup>x</sup> parameters is critical in order to achieve the best possible predictive ability.

Five different parameters can be adjusted in the creation of a backpropagation neural network: hidden units, number of layers, learning rate, momentum and number of epochs. The number of hidden units refers to the number of nodes plus a threshold node which are to be placed between the input and output vectors. Layers represent the number of layers of hidden units between the input and output vectors. Learning rate is the numeric value by which the weights between the input, hidden, and output layers are adjusted. Momentum is a parameter, which can increase the pace of learning, potentially reducing the amount of time that it takes to train the network. The number of epochs refers to the number of times a data set is applied to the neural network for training, tuning, and testing.

## 1.1.5. Current<sup>r</sup>possible scenario

For researchers, the greatest problem with the current system is that they must develop their own statistical prediction models in order to study a drug. This is a time-consuming process often days andŽ . takes a high level of skill.

Work conducted in research facilities commer-Ž cial, private, and academic conduct analysis on. pharmaceutical agents currently is reported to researchers either as information accompanying a drug or through journal articles and other publications. Clinicians must rely on the accuracy of such research although in practise, they develop a AfeelB for the effectiveness of a drug at a certain blood level concentrations for specific patients. They therefore dose drugs based both on past experience and recommended dosages generated by pharmaceutical companies and researchers without having any opportunity for discussion of findings. Also, the physician’s data and knowledge may or may not be shared with colleagues within their facility and<sup>r</sup>or field.

No application exists today which would allow medical practitioners to quickly and easily adjust dosage to patients who have differing pharmacokinetic parameters, which means they must rely on documentation and experience to correctly dose a patient to maintain a plasma concentration level in an effective range.

Providing clinicians with NONMEM would not necessarily generate more research; the software requires an ability to do extensive statistical modeling beyond the skills of many clinicians. In contrast, a neural network works empirically. Once a patient’s pharmacokinetic parameters are entered, the best possible dosing regimen for a particular individual can be found simply by using slider bars to adjust dose and the interval time between dosages. This application would not only be an effective clinical tool, but could also facilitate information sharing, resulting in better care for patients.

Pharmaceutical researchers would also benefit. Studies could be conducted more quickly than if they had to develop a prediction model for every study. Because the neural network would train itself to maximum prediction efficiency when given a certain set of parameters, the researcher could generate several studies in the amount of time it previously took to do one.

## 2. Experimental test bed for population analysis

The data set for our experiment contained information regarding tobramycin, a drug used for repressing infectious diseases of the blood. Patients eligible for the study had been diagnosed with either cystic fibrosis or a hemotologic–oncologic disorder, were less than 18 years of age, had been receiving tobramycin more than 24 h, and had had peak and trough concentration blood samples taken at approximately 2 and 6 h post-initiation of a 30-min drug infusion of tobramycin.

The data set, collected from 1983 to 1992, constituted a total of 311 instances of patient information gathered from 101 patients. Originally, this information was collected for a study to determine whether illness had a significant effect on the effectiveness of the tobramycin. The parameters of the data set are shown in Fig. 2.

There were two possibilities for data set representation: if peak and trough concentration levels were ignored, the data set would contain 622 data points. If peak and trough concentrations were predicted separately, the data set would contain 311 data points. Consistent with most data sets collected in clinical settings, several patients had contributed a small number of inputs while others had many inputs over an extended period of time.

## 3. The experiment

## 3.1. NONMEM analysis

The NONMEM analysis used 622 data points and predicted blood concentration values for each patient in the NONMEM study without consideration of peak and trough values. The pharmacokinetic model used for estimating blood serum concentration can be represented in Eq. 1 .Ž .

$$
C _ {i j} = \frac {k _ {i o} \left(1 - \mathrm{e} ^ {- (\mathrm{Cl} _ {i} / V) T _ {i}}\right)}{\mathrm{Cl} _ {i} \left(1 - e ^ {- (\mathrm{Cl} _ {i} / V) \tau_ {i}}\right)} \mathrm{e} - \left(\mathrm{Cl} _ {i} / V\right) _ {t _ {i j}}.\tag{1}
$$

Supporting equations for clearance and volume of distribution are found in Eqs. 2 and 3 .Ž . Ž .

$$
\mathrm{Cl} _ {i} = \left\lfloor \theta_ {1} \times \ln (\text { weight } _ {i}) + \theta_ {3} \times \text { age } _ {i} \right\rfloor \mathrm{e} ^ {\eta 1}\tag{2}
$$

$$
V _ {i} = \left\lfloor \theta_ {2} \times \ln (\text { weight } _ {i}) \right\rfloor e ^ {\eta 1}\tag{3}
$$

where for child $i , C _ { i j }$ is the observed concentration at measurement j. $k _ { i o }$ is the infusion rate. $T _ { i }$ is the infusion time. $\tau _ { i }$ is the dosing interval. $T _ { i j }$ is the elapsed time at measurement j after the end of infusion. $\mathrm { C l } _ { i }$ is the clearance. $V _ { i }$ is the volume of distribution and ln is the natural log.

```txt
There were eight demographic and dosage input parameters:
Age
Sex
Illness
Weight
Dose
Interval between dosages
Initial time of blood sample (peak)
Second time of blood sample (trough)

There were two concentration level output parameters:
Concentration level at initial blood sample (peak)
Concentration level at second blood sample (trough)
```  
Fig. 2. Data set parameters.

Table 1  
Normalization of input parameters

<table><tr><td>Input parameter</td><td>Test I</td><td>Test II</td></tr><tr><td>Age</td><td>age/max. age</td><td>age/max. age</td></tr><tr><td>Sex</td><td>n/a</td><td>n/a</td></tr><tr><td>Illness</td><td>n/a</td><td>n/a</td></tr><tr><td>Weight</td><td>weight/max. wt.</td><td>weight/max. wt.</td></tr><tr><td>Dose</td><td>dose/max. dose</td><td>dose/max. dose</td></tr><tr><td>Interval between dosages</td><td>interval/max. interval</td><td>interval/max. interval</td></tr><tr><td>Time of blood drawn (generic — Test I only)</td><td>time/max. time</td><td></td></tr><tr><td>Time of blood drawn (peak — Test II only)</td><td></td><td>time/max. time</td></tr><tr><td>Time of blood drawn (trough — Test II only)</td><td></td><td>time/max. time</td></tr></table>

## 3.2. Neural network testing phases

In our initial test, which directly matched the NONMEM analysis, the original data set was divided into the six demographic and dosage inputs plus the time of the blood drawing resulting in a total of 622 data points. A single output was generated — the plasma concentration of tobramycin given at the time of blood drawn. The network topology was a seven-input<sup>r</sup>one-output neural network with 30 hidden units.

In the second test, the original 311 data points were presented to the neural network. Peak and trough concentrations were predicted as separate values. The resulting network topology was eight inputs and two outputs with 23 hidden units.

In both data sets, two-thirds of the data points were used for the training phase of the neural network. The remaining data points were used for the tuning phase. The input units were normalized as shown in Table 1 for both tests. This resulted in the best predictive capability from the neural network.

The output vector of the neural network, a value between 0 and 1, needed to be modified in order to make comparisons between the network’s output vector and the actual data. This value was normalized to the same range of values. This was done using the formula found in Eq. 4 .Ž .

ln actual concentrationŽ . Ž .<sup>y</sup>ln minimum concentration value ln maximum concentration value Ž . Ž .<sup>y</sup>ln minimum concentration value .

Ž . 4

## 3.3. Neural network parameters

The goal of selecting the settings for the different parameters for a neural network is to minimize the mean standard squared error MSSE . While otherŽ . parameters are held constant, each parameter is tested using the data set. The ranges of parameters tested are shown in Table 2 and the optimal parameters, which were selected are shown in Table 3. Although momentum was tested, it was not used in the final selection of parameters due to increased MSSE in the results.

Table 2  
Testing parameter ranges

<table><tr><td>Parameter</td><td>Range</td><td>Increment</td></tr><tr><td>Epochs</td><td>0–10 000</td><td>1</td></tr><tr><td>Hidden units</td><td>3–60</td><td>1</td></tr><tr><td>Learning rate</td><td>0.05–0.60</td><td>0.05</td></tr><tr><td>Momentum</td><td>0.05–0.90</td><td>0.05</td></tr></table>

Table 3  
Optimal parameters selected

<table><tr><td></td><td>Test I</td><td>Test II</td></tr><tr><td>Epochs</td><td>5400</td><td>800</td></tr><tr><td>Hidden units</td><td>30</td><td>23</td></tr><tr><td>Learning rate</td><td>0.35</td><td>0.4</td></tr><tr><td>Momentum</td><td>0.0</td><td>0.0</td></tr></table>

![](/api/attachments/BA7A3S2P/fulltext/images/d94f3cd7cfe307271bab459876e444d212d8782e79b07696382d78f55e0ed634.jpg)  
Fig. 3. Results of Test I — one-way analysis of variance and paired two sample t-test.

## 3.4. Results of testing

The most direct comparison between the neural network results and the NONMEM analysis was Test

![](/api/attachments/BA7A3S2P/fulltext/images/60a92a7447534200250b8395b492f39092a5bb5b720fc251778e16207fe09b22.jpg)  
Fig. 4. Results of Test II — one-way analysis of variance and paired two sample t-test.

I — no separation of peak and trough concentrations, 622 data points. The result of these tests showed that the neural network could predict blood concentration levels more successfully than NON-MEM, however, not at a statistically significant level. The best result was obtained when peak and trough concentrations were predicted separately in Test II.

In Figs. 3 and 4, created using MiniTab<sup>w</sup>, the one-way analysis of variance shows that the neural network predicted blood serum concentration levels better than NONMEM. The mean squared error Ž . MSE associated with the prediction was lower in each of those cases. The p-value for Test I, the most direct comparison, was approximately 10%. The pvalue for Test II, which represents the lowest bestŽ . p-value, was approximately 9%.

## 4. A medical decision support application for clinicians and researchers

## 4.1. Usability issues

In order for a software application to be widely accepted, regardless of its type, it must be easy to use. The growing emphasis on usability is one of the most dominant of the current trends in computing <sup>w</sup> <sup>x</sup> <sub>6</sub> <sub>.</sub>

NONMEM has two difficulties: the application can be complex to use and the development of prediction models is required. A biometrician described the process of model development as taking a AvariableB length of time, sometimes as long as a day or several days. Since the cost of a typical biometrician’s time is expensive, there would be a cost benefit if he spent less time modeling and more time conducting research about gathered data. The biometrician also found the application difficult to use both because of the FORTRAN-like commands and the operating system in which it was used Ž . UNIX .

Timeliness of information: in clinical settings, it is necessary to have relevant drug information readily available 12 . Since a neural network should be able<sup>w</sup> <sup>x</sup> to generate predictions in a few minutes or seconds, clinicians could get information instantly, not read about them later after a biometrician has performed a study.

Ultimately, the criterion for acceptance is based on the performance of the application — how accurately it works. Proof that the neural network will consistently predict blood concentration values equal to or better than currently accepted statistical techniques must be provided to researchers in order to convince them to change from their proven methodologies.

## 4.2. The data analysis tool

The goal is to create an application that clinicians and researchers can reliably use to generate concentration levels and potentially other parameters asŽ well and perform trend analyses. Clinicians would. then have necessary information at their fingertips and pharmaceutical researchers would have a tool to make the analysis of data easier.

The proposed interface would address two possible types of analysis: prediction and data analysis. At invocation of the application, users could choose which of these tools they would prefer to use. The interface will be developed for use on a wide variety of platforms, using Java as the interface development tool.

Our proposed data analysis tool was developed in ANSI C the neural network component , with aŽ . Delphi interface component on Windows NT. Delphi and NT provide a convenient environment for quick prototyping. Several medical and pharmacy school researchers have participated in the design of this analysis tool Fig. 5 .Ž .

## 4.2.1. Whatif analysis

The Whatif analysis interface would be able to determine the potential blood concentration level in a patient’s blood stream. Two key types of data would be provided to the neural network’s input vector: patient data and drug application data. Patient data are parameters such as age, weight, illness, etc. Drug application data are the clinician’s dosing regimen such as dosage, dosing interval, time of blood drawn, etc.

As previously noted, patient data vary over time. Patients get older, may gain or lose weight, and perhaps grow increasingly ill or show signs of recovery. Whatif analysis will be a helpful tool to assist clinicians in predicting what the plasma concentration level will be, based on changes.

![](/api/attachments/BA7A3S2P/fulltext/images/b20597240546ca665139cac1a18cb71f29cf611fbb62f7557ac7e1a17d94fe37.jpg)  
Fig. 5. Main screen of pharmacokinetic predictor.

A likely scenario follows: a patient with cystic fibrosis was admitted to the hospital at the age of 3.25 years. The patient was treated for an infection with tobramycin. Two years later, the patient reenters the hospital for treatment of another infection. The patient’s previous data are helpful, but certain demographics have altered, so reaction to the drug is likely to be different. The patient is now age five. Between the ages of 3 and 5, children grow very rapidly, usually experiencing a considerable weight gain. The infection is less advanced than it was during the previous visit. At the minimum, three parameters have changed. The Whatif analysis can accept information changes and quickly predict a blood concentration level for a particular dosing regimen.

Drug applications can also be dynamic. Perhaps, a clinician would prefer to see a particular concentration level in a patient, for instance, the recommended optimal level. By using the Whatif analysis, the clinician could alter the dosage or dosing interval to reach the desired blood serum concentration level in the patient. This strategy would be particularly useful if previous dosing information about the patient were unavailable Fig. 5 .Ž .

A likely scenario here might be one in which the patient had never been previously treated, but is now entering the hospital with an infectious disorder. The clinician could enter patient data and within a few seconds determine, based on that information, what that patient’s blood concentration level will be after administration of a particular dosage and<sup>r</sup>or dosing interval. Information could be reentered until the clinician determines the regimen that best fits the desired concentration level without having to test the patient’s reaction to the drug by dosing him or her and then drawing blood and checking peak and trough concentrations Fig. 6 . Ž .

Graphing ability would be incorporated into the interface, allowing the clinician to choose a particular drug application parameter such as dosage, holding all other parameters constant. The Whatif analysis would display a chart showing the blood concentrations for different dosages Fig. 7 .Ž .

![](/api/attachments/BA7A3S2P/fulltext/images/51adb93259af08a0e10337603412b545bd74343f2b8e3c4c323ae23ad3523b14.jpg)  
Fig. 6. Data parameter selection screen of pharmacokinetic predictor.

Since the data set and the weights associated with it would already exist, predicting the blood concentration level of the patient would be a quick and easy process, requiring only a few seconds of CPU processing time. At present, no application of this kind is available to assist clinicians in finding an effective dose range for an individual patient.

## 4.2.2. The training session

Targeted toward meeting the requirements of pharmaceutical researchers, the Training Session interface would be used to present new data sets to the neural network for analysis or to take an existing data set and alter the fields included to analyze how highly each input is correlated with predicting the output. Additionally, the interface would be useful to a researcher who might wish to predict peak and trough concentrations or a single concentration level — either peak, trough or a generic value. The Training Session would give researchers the flexibility to set their own input and output vectors, allowing them to conduct a broad range of research relating to a particular drug in a short period of time.

![](/api/attachments/BA7A3S2P/fulltext/images/9ba15583a7d5e6b06a4ee790fc6e77cd209b0f80fb5b890afdb22a5b56da198c.jpg)  
Fig. 7. Graph of weight vs. concentration based on selected parameters.

A possible scenario might involve a pharmaceutical company that would like to determine whether the type of illness a patient has is highly correlated with the blood concentration level of a drug. The data set is loaded into the Training Session and input and output vectors are established. The neural network is trained the first time, including the illness parameter and then a second training session is run with the parameter removed. The Training Session can present the researcher with error information. If the error is significantly higher during the second session, it can be concluded that the illness is likely to be a highly correlated parameter and that perhaps, the drug is better for use in treating some illnesses than others.

An important usability feature of the Training Session will be the ability to automatically scale and normalize the data set, select optimal network parameters, and train the network to predict values, without the user’s having to understand the complexity of neural networking. No extensive training for the researcher would be required.

## 5. Conclusions and future work

The results of the study comparing NONMEM and neural network show that the neural network has predictive capability equal to or better than NON-MEM. Although statistical significance was not established, we were able to prove that a neural network can accurately predict blood concentration level in human subjects making the two methods interchangeable tools for effectively estimating concentration levels.

In addition to accuracy, the neural network application has the advantage of producing results empirically, without the need for developing statistical prediction models. This puts the power of generating results in the hands of clinicians who may not be well trained in this type of analysis methods. Further, it enables biometricians to have more time to conduct analyses. As a cost effective, accurate pharmacokinetic estimation application, it should be an ex cellent tool for both researchers and practitioners.

The future directions of this project are to complete the proposed modules in the prototype. Once these are completed, we plan to conduct a usability study and cost benefit analysis with both clinicians and researchers to investigate adoption issues and functionality.

## Acknowledgements

This project was supported in part by the following grants: Special Information Services, National Library of Medicine NLM , National Institutes ofŽ . Health NIH , Ž . ASemantic Retrieval for Toxicology and Hazardous Substance DatabasesB, 1996–1997; National Cancer Institute NCI , National Institutes Ž . of Health NIH ,Ž . AInformation Analysis and Visualization for Cancer LiteratureB, 1996–1997; and AT &T Foundation Special Purpose Grants in Science and Engineering, 1994–1996.

## References

<sup>w</sup> <sup>x</sup> 1 C. Beardon, Artificial Intelligence Terminology: A Reference Guide, Halstead Press, New York, 1989.

<sup>w</sup> <sup>x</sup> 2 A.J. Boeckmann, L.B. Sheiner, S.L. Beal, NONMEM Users Guide — Part V. Introductory Guide, University of California San Francisco, San Francisco, 1994, pp. 1–7, Chap. 1.

<sup>w</sup> <sup>x</sup> 3 M.E. Brier, J.M. Zurada, G.R. Aronoff, Neural network predicted peak and trough gentamicin concentrations, Pharmaceutical Research 12 3 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 H. Chow, H. Chen, T. Ng, Myrdal, S.H. Yalkowski, Using backpropagation networks for the estimation of aqueous activity coefficients of aromatic organic compounds, Journal of Chemical Information Computer Science 35 4 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 L. Kilmartin, E. Ambikairajah, S.M. Lavelle, A neural network diagnostic tool for liver disorders. Paper presented at Neural Computing Research and Applications: Part Two, 1992.

<sup>w</sup> <sup>x</sup> 6 R. Kling, Organizational analysis in computer science, The Information Society 9 2 1993 71–87.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 R.P. Lippmann, An introduction to computing with neural nets, IEEE ASSP 4 2 1987 4–22.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 E. Rich, K. Knight, Artificial Intelligence, McGraw-Hill, New York, 1991, pp. 487–509.

<sup>w</sup> <sup>x</sup> 9 D.J. Roe, M. Cheng, V.A. Elberry, P.E. Nolan, Estimating parameters in non-linear mixed effects models: a comparison using clinical data in children, Proceedings of the Biopharmaceutical Section, American Statistical Association 1994Ž . 318.

<sup>w</sup> <sup>x</sup> 10 D. Rummelhart, R. Durbin, R. Golden, Y. Chauvin, Backpropagation: the basic theory, Backpropagation Theory, Architectures, and Applications 1995 1–34.Ž .

<sup>w</sup> <sup>x</sup> 11 D. Rummelhart, B. Widrow, M. Lehr, The basic ideas in neural networks, Communications of the ACM 37 3 1994Ž . Ž . 87–92.

<sup>w</sup> <sup>x</sup>12 R. Schaff, G. Wasserman, R. Englebrecht, W. Scholz, Medical treatment assistance with an interactive drug information system, Medical Expert Systems Using Personal Computers Ž .1987 45–51.

<sup>w</sup> <sup>x</sup> 13 L.B. Sheiner, T.M. Ludden, Population pharmacokinetics<sup>r</sup> dynamics, Annual Review of Pharmacological and Toxicology 32 1992 185–209.Ž .

![](/api/attachments/BA7A3S2P/fulltext/images/bdbf14b3c0b0bffdd2ab448cf58c83e3a1d7cc0aa790b6bad82ba4d39a1acfd8.jpg)

Kristin M. Tolle is a PhD candidate of Management Information Systems at the University of Arizona where she received her MS in MIS 1997 . She isŽ . also a senior member and research associate of the UA<sup>r</sup>MIS Artificial Intelligence Lab. She received her BS in Computer Information Systems from Boise State University 1988 . Tolle is aŽ . recipient of a research fellowship from the National Library of Medicine and the Oak Ridge Institute for Science and

Education. She has published several journal and conference articles on topics ranging from medical information retrieval, natural language processing, intelligent agents and neural network medical decision support systems.

![](/api/attachments/BA7A3S2P/fulltext/images/08cdb6911d32a9f752951530376a9e59b7572b9d4dd9847190f9f5fd15b170ee.jpg)

Dr. Hsinchun Chen is a McClelland Professor of Management Information Systems at the University of Arizona and head of the UA<sup>r</sup>MIS Artificial Intelligence Lab. He received the PhD degree in Information Systems from New York University in 1989. He is the author of more than 70 journal articles covering semantic retrieval, search algorithms, knowledge discovery and collaborative computing in leading information technology publications such as Decision

Support Systems, Journal of the American Society for Information Science, and Communications of the ACM. He serves on the editorial board of the Journal of the American Society for Information Science and Decision Support Systems. He is an expert in digital library and knowledge management research, whose work has been featured in various scientific and information technologies publications including Science, Business Week, NCSA Access Magazine, WEBster and HPCWire.

![](/api/attachments/BA7A3S2P/fulltext/images/d3960ce6679adfff70420406954f69432c3808146458ff00e732eacef00aee7e.jpg)

Dr. Hsiao-Hui Chow is an Assistant Professor of Pharmacy at the University of Arizona and an affiliate member of the Arizona Cancer Center. Dr. Chow received her bachelors of Science degree from Taipei Medical College 1983Ž . and her PhD from State University of New York at Buffalo 1989 . She con-Ž . ducts research on the characterization of the disposition of drugs in the body, identification and understanding factors which may influence the disposition ki-

netics and responses of xenobiotics, and development of pharmacokinetic and pharmacodynamic models in quantitating and predicting the kinetic processes of drug absorption, distribution, elimination and response. She has published several articles in the areas of pharmacokinetics and biopharmaceutics.
