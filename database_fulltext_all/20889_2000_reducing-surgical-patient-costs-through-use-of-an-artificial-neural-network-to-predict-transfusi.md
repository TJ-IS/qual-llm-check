---
otero_id: 20889
otero_key: "4UHJ4AC3"
title: "Reducing surgical patient costs through use of an artificial neural network to predict transfusion requirements"
authors: "Steven Walczak; John E Scharf"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00093-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Reducing surgical patient costs through use of an artificial neural network to predict transfusion requirements

Steven Walczak <sup>a,)</sup>, John E. Scharf <sup>b</sup>

<sup>a</sup> College of Business and Administration, UniÕersity of Colorado at DenÕer, Campus Box 165, PO Box 173364 DenÕer, CO 80217-3364 USA

<sup>b</sup> Anesthesiology Department, College of Medicine, UniÕersity of South Florida, MDC 59, 12901 Bruce B. Downs BlÕd., Tampa, FL 33612, USA

## Abstract

Transfusion and blood bank services have long been identified as a source of potential cost savings. The implementation and use of maximum surgical blood ordering schedules MSBOS and type and screen practices have already succeeded inŽ . reducing overall waste and costs associated with transfusion services, but further reductions in waste and cost are still realizable. An artificial neural network ANN is trained to predict the quantity of transfusion units that are required byŽ . surgical patients for a specific operation. The ANNs produce a significant reduction in the quantity of blood ordered and a subsequent reduction in costs to the hospital and patients. ANNs offer a means to reduce patient costs while maintaining a high level of patient care. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Neural networks; Radial basis function; Transfusion; Cost reduction

## 1. Introduction

The medical field is experiencing ever increasing pressure to reduce costs 6,17,19,36 . Typically how-<sup>w</sup> <sup>x</sup> ever, there exists a tradeoff between cost and the quality of care 6 . For surgical patients, blood trans-<sup>w</sup> <sup>x</sup> fusions increase the cost of patient care 13,15 and <sup>w</sup> <sup>x</sup> savings from transfusions can be transferred to patients 9 . Annually, well over 12 million units of <sup>w</sup> <sup>x</sup> blood are transfused to patients 19,21,41 and the <sup>w</sup> <sup>x</sup> majority of transfusions are given to surgical patients <sup>w</sup> <sup>x</sup> 32 .

Various studies have shown blood unit acquisition costs for hospitals ranging from US\$48 19 to<sup>w</sup> <sup>x</sup> US\$110 22 with a national average of US\$76 per<sup>w</sup> <sup>x</sup> unit and corresponding costs charged to patients ranging from US\$60 19 to US\$219 17 . Over-<sup>w x</sup> <sup>w x</sup> ordering of blood for operations is the primary cause of blood waste and corresponding increases in transfusion service costs 25,45 . Although blood can be <sup>w</sup> <sup>x</sup> returned to the blood bank, a non-used unit of ordered blood removes that unit from the general supply for 48 h 35 . Furthermore, ordered, but non- <sup>w</sup> <sup>x</sup> transfused blood increases the costs of a hospital even if the blood can be returned to the blood bank. All ordered blood must be tested and routed, which costs an average of US\$33 per unit for US hospitals and furthermore, consumes 15 min<sup>r</sup>unit of a laboratory technician’s time. Blood ordering efficiency is typically evaluated using the ratio of the quantity of units crossmatched tested for patient compatibilityŽ and presence of diseases to the quantity of units . transfused Ž . C<sup>r</sup>T <sup>w</sup> <sup>x</sup> 1,25 , with a C<sup>r</sup>T ratio of 2.5 <sup>w</sup> <sup>x</sup> <sup>w x</sup> 25,32 or less 36 considered to be the maximum acceptable level. A C<sup>r</sup>T ratio of 2.5 indicates that for every unit, which is actually transfused to a patient, 2.5 units of blood are crossmatched and prepared for transfusion.

The maximum surgical blood ordering schedule Ž . MSBOS , which uses a simple statistical mean of blood unit usage in previous surgical procedures to estimate the transfusion requirements for future surgical procedures 32,35 , is an attempt to limit the<sup>w</sup> <sup>x</sup> widespread over-ordering of blood. Hospitals implementing MSBOS, typically order the same quantity of blood for every patient undergoing a specific procedure. MSBOS has been shown to reduce the C<sup>r</sup>T ratios for hospitals in the US 32 and world-<sup>w</sup> <sup>x</sup> wide 1,24,35,49 . One study on the implementation<sup>w</sup> <sup>x</sup> of MSBOS claimed an annual savings of US\$110,000 at a 561-bed hospital 32 and another claimed a<sup>w</sup> <sup>x</sup> savings of 70% 49 , but for operations with an <sup>w</sup> <sup>x</sup> MSBOS of 1 or greater at least 1 unit of blood isŽ ordered for the specific operation , several studies. still report C<sup>r</sup>T ratios values well in excess of 2.5 <sup>w</sup> <sup>x</sup> 1,35 .

A system capable of more accurately classifying the transfusion needs of individual patients insteadŽ of treating all patients as identical would result in . even greater savings over the MSBOS system. However, the prediction of the precise quantity of blood required by a patient is an extremely difficult problem 7 and no pre-operative lab test or hemostatic <sup>w</sup> <sup>x</sup> function currently exists that can accurately predict this value 13 . It takes a minimum of 30 min to <sup>w</sup> <sup>x</sup> perform a full crossmatch on 1 unit of blood to ensure the safety of the patient 45 , but partial<sup>w</sup> <sup>x</sup> crossmatches may be performed in 5 min 32,45 .<sup>w</sup> <sup>x</sup>

A radial basis function RBF artificial neuralŽ . network ANN method is trained to predict the Ž . quantity of red blood cell RBC units that a patient Ž . will require during surgery or within a 48-h period immediately following surgery for the abdominal aortic aneurysm AAA repair operation. The AAA Ž . repair operation is chosen because, AAA rupture is a leading cause of death in older men 29 and AAA <sup>w</sup> <sup>x</sup> repair operations typically require the use of RBC transfusions. Results from the ANN indicate that additional significant savings in the quantity of blood units ordered and a corresponding reduction in the $C / T$ ratios are achievable.

## 2. Background

The margin between supply and demand for blood has been diminishing since the late 1980s 41 . Rea-<sup>w</sup> <sup>x</sup> sons for the reduction in blood supply are an aging population and ever more rigorous screening procedures 44 . Current methods for reducing blood uti-<sup>w</sup> <sup>x</sup> lization are the MSBOS, that limits the number of units ordered for specific procedures 32,35 , and<sup>w</sup> <sup>x</sup> techniques for evaluating the appropriateness of a transfusion 11,18,19,22,36 . The need for blood units<sup>w</sup> <sup>x</sup> in surgery is ever present. Various surgical procedures continue to require blood transfusions 7,20,43 <sup>w</sup> <sup>x</sup> for the recovery and health of the patient.

## 2.1. Medical risk

In addition to the economic impact of over-ordering blood and its reduction of the blood supply, patient health may also be affected by the immediate availability of too many blood units in the operating room. Research has shown that physicians use blood more freely when it is readily available 27 without<sup>w</sup> <sup>x</sup> any corresponding difference in actual surgical blood loss. Inappropriate transfusions negatively impact the health of patients 11,19,20 .<sup>w</sup> <sup>x</sup>

Conversely, patient health risk is reduced if blood is available when it is required 13 . The ideal situa-<sup>w</sup> <sup>x</sup> tion is to reduce the common problem of over-ordering blood units 25,45 to benefit the patient econom-<sup>w</sup> <sup>x</sup> ically, without under-ordering blood which may cause negative health risks to the patient.

## 2.2. Neural networks in medicine

ANNs have been widely used in business, engineering, and medicine 33,46 . Regression and step-<sup>w</sup> <sup>x</sup> wise regression are the commonly used techniques for modeling problems in medical domains <sup>w</sup> <sup>x</sup> 7,13,20,21,39,43 . Researchers have reported that ANN techniques outperform standard statistical techniques 5,14 . Specifically, in medical domains,<sup>w</sup> <sup>x</sup> ANNs have outperformed discriminant analysis 42 ,<sup>w</sup> <sup>x</sup> Cox regression 28 , and logistic regression 30 .<sup>w x</sup> <sup>w x</sup>

Applications of ANNs in medical domains include: identifying myocardial infarct 4,5 , detect<sup>w</sup> <sup>x</sup> coronary artery disease 12,28 , detect pulmonary <sup>w</sup> <sup>x</sup> embolism 16 , read electro-diagnostic signals 23 ,<sup>w x</sup> <sup>w x</sup> detect correct placement of tracheal intubation 31 ,<sup>w</sup> <sup>x</sup> and tomography 40 . The majority of ANN applica-<sup>w</sup> <sup>x</sup> tions in medical domains are either image classifiers <sup>w</sup> <sup>x</sup> 12,16,23,33,40 or perform laboratory test analysis <sup>w</sup> <sup>x</sup> 14,23,33 . The medical literature indicates that ANNs have not been previously used for predicting transfusion requirements of surgical patients.

Why are ANN applications in medicine primarily limited to image classification or lab analysis? Several researchers 4,5,23 have indicated that physi- <sup>w</sup> <sup>x</sup> cians’ acceptance of neural networks is severely limited, especially when ANNs attempt to perform diagnosis. The ANN application discussed later in this article does not attempt to perform diagnosis, but instead approaches the problem of improving patient health care and reducing health care costs from an administrative perspective. Similar to the MSBOS technique, the ANN transfusion requirement prediction algorithm limits the quantity of blood units that are ordered and affords a direct economic benefit to the hospital and subsequently to the patient.

## 3. Radial basis function ANNs

Backpropagation is the most common form of implemented ANNs 8 however, the characteristics<sup>w</sup> <sup>x</sup> of the domain data for predicting transfusion requirements lend themselves to a different supervised learning ANN paradigm: the RBF neural network <sup>w</sup> <sup>x</sup> 34 . Several comparisons of backpropagation and RBF networks have been performed in biomedical domains 12,47 . In these comparative studies, RBF<sup>w</sup> <sup>x</sup> networks have similar performance to backpropagation ANNs or outperform them depending on the characteristics of the domain data. RBF networks perform better than the traditional backpropagation networks when extrapolation is required vs. interpo-Ž lation and when only small training sets are avail- . able for building the ANN model, which consequently are properties of the surgical transfusion domain.

An RBF network is composed of input and output layers similar to the backpropagation ANNs. The first hidden layer of an RBF network, or prototype layer, performs a self-organizing unsupervised clus-Ž . tering of the data based upon the training data or aŽ portion thereof 26 . Once the center values for each . <sup>w</sup> <sup>x</sup> cluster node are determined using an adaptive Ž . Kmeans algorithm, each data cluster’s output value is produced by a Gaussian function,

$$
y _ {k} = \exp \left(\left(I _ {k} - R ^ {2}\right) / \left(\sigma_ {k} ^ {2}\right)\right),
$$

where $I _ { k }$ is the root-mean-square difference between a new set of data values, $X _ { i = I \ldots N } $ , and the established cluster center at node k. The clusters divide the training data population into distinct segments Ž . one per node in the prototype layer and new data is associated with clusters depending on its distance from the cluster’s center value. The output value is a linear combination, using a supervised learning algorithm such as least means squared, of the non-linear output from the Gaussian clustering functions. Additional functional complexity may be achieved by adding an optional supervised learning hidden layer Žsimilar to those found in traditional backpropagation ANNs between the prototype and output layers.. Readers who are interested in learning more details on RBF networks are directed to Refs. 26,34 .<sup>w</sup> <sup>x</sup>

Patients undergoing an operation that normally requires transfusions will fall into one of several distinct clusters: 1 no transfusion required, 2Ž . Ž . transfused less than or equal to the MSBOS quantity of units, and 3 transfused greater than the MSBOSŽ . quantity of units. This natural domain segmentation lends itself to an RBF network solution. RBF networks perform better at extrapolation than backpropagation ANNs 3,47 and since the data population <sup>w</sup> <sup>x</sup> will not be completely represented in the training data set as all patients are unique , extrapolationŽ . from the learned data clusters is a requirement. Other factors that promote the AfitB between an RBF network solution and the transfusion prediction research problem are that RBF neural networks perform better than backpropagation ANNs when: the set of training in-sample data is small 3 , training instances Ž . <sup>w</sup> <sup>x</sup> are not balanced 12 , and training data is multimodal<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 47 .

## 4. Neural network models to predict transfusion quantity

RBF neural networks are implemented to solve the medical domain problem of accurately predicting the quantity of RBC units to be transfused to a specific patient during an AAA repair operation or within 48 h thereafter to reduce the quantity of blood units ordered that are never transfused. All training Ž . Ž . in-sample and test out-of-sample data is taken from a local version of the V.A. Surgical Risk Assessment VA-SRA Database 10 at the James Ž . <sup>w</sup> <sup>x</sup> A. Haley V.A. Hospital, which contains quantitative information regarding all operations performed at the V.A. hospital, excluding heart operations e.g., coro- Ž nary artery bypass graft CABG , which are kept in Ž .. a separate database. Evaluation data additional out-Ž of-sample data sets are taken from the Haley V.A. . Hospital and the Lexington V.A. Hospital. The selection of a supervised learning ANN method, such as RBF or backpropagation, is indicated by the presence of a large historical database with known outcomes.

## 4.1. Data and input Õariable selection

In addition to being a leading cause of death in older men 29 , the AAA operation is selected as the<sup>w</sup> <sup>x</sup> data set for performing the research because it is the non-coronary operation with the greatest quantity of operations requiring transfusions. Training data for the research RBF neural network is taken from the VA-SRA database records for all operations performed between January 1992 and December 1995 Žexcluding November and December 1992 and January and February 1995, due to retrieval errors in the database . Test data is taken from the VA-SRA. database records for all operations performed between January 1996 and July 1996 and a secondary validation data set is taken from the VA-SRA database and Lexington V.A. cases for operations performed between August 1996 and May 1997. For the combination of the training and test periods, 6236 operations are performed at the particular V.A. hospital of which 325 operations required at least 1 RBC unit transfusion. The AAA operation has 109 cases with 87 requiring RBC transfusions.

The separation of the out-of-sample data sets into two groups reflects the time difference between the start of the reported research and the publication of the results. The test data may be viewed as a validation set for the feasibility analysis part of the research to verify if any improvement is achieved through the use of ANNs, while the AvalidationB set may be viewed as the prospective application of the designed ANNs to the domain problem of predicting blood usage for AAA operations performed at V.A. hospitals.

The training set 1992–1995 contains 94 opera-Ž . tions, 75 of which required at least one transfusion Ž . 80% and the test data contains 15 operations, 12 of which required at least one transfusion 80% andŽ . the validation data set contains 43 operations, 27 of which required transfusion at least on transfusion Ž . 63% . The average number of units transfused for the training and test data sets is 2.76 and 2.79 units, respectively, or 3.45 and 3.55 units, respectively, if only those operations requiring a transfusion are considered. An MSBOS value of 4 RBC units for the AAA repair operation is established at James A. Haley V.A. hospital and the average number of RBC units transfused to AAA patients for the research data period supports this value, while the Lexington V.A. institution did not utilize an MSBOS system, but typically 4–6 units are ordered pre-operatively. However, a significant inter-operative variation in the number of units transfused is observed during each of the three data sets with the range of RBC units transfused being: 0–44 during the training data period, 0–10 during the test data period, and 0–7 during the validation data period.

Once the availability of data is determined, the independent<sup>r</sup>input variables must be selected. Bansal et al. 2 claim that the data cost for ANN applica-<sup>w</sup> <sup>x</sup> tions is a critical factor and that ANN design should attempt to reduce the number of input values without sacrificing ANN performance. The local VA-SRA database made 23 variables available to the transfusion prediction ANN research. All values that are not available prior to the start of surgery are eliminated, including intra-operation bleeding volume and the elapsed time of the operation.

In addition to consultation with anesthesiologists and surgeons practicing at the James A. Haley V.A. Hospital, a literature review of transfusion technique and protocol is used to establish a set of possible independent variables. Factors that are cited in the literature as affecting the decision to transfuse a patient, establishing the volume to be transfused, or determining the appropriateness of a transfusion are:

1. hematocrit 13,15,18,21,22,36,43,44 ,<sup>w</sup> <sup>x</sup>

2. age 15,27,43,44 , <sup>w</sup> <sup>x</sup>

3–4. prothrombin time PT and partial thrombo-Ž . plastin time PTT 11,13,15,21 , Ž . <sup>w</sup> <sup>x</sup>

5. gender 20,43 , <sup>w</sup> <sup>x</sup>

6. platelet count 13,21 ,<sup>w</sup> <sup>x</sup>

7. American Society of Anesthesiologists ASAŽ . class 20 ,<sup>w</sup> <sup>x</sup>

8–9. pulmonary and cardiac diseases 44 .<sup>w</sup> <sup>x</sup>

Gender is not included because there is no variation in the data only one example of a femaleŽ patient is available from the 109 cases of training and test data, remember that the AAA is primarily an operation performed on males . Platelet count, PT,. and PTT are all related to coagulation. Because of Smith’s 38 recommendation that correlated values<sup>w</sup> <sup>x</sup> should be removed from ANN input vectors, as they hinder the performance of an ANN due to theŽ modeling of noise by the ANN , only one of these. values, platelet count, is used. The decision of which of these correlated variables to use is due in part to missing values for many of the PT and PTT fields in the VA-SRA database. The effect of including the PT and PTT variables, to account for relatedness vs. correlation, on the prediction performance of the RBF transfusion prediction ANN is discussed in Section 5.2.

Using the literature and the above design heuristics and limitations, an input vector of the following six variables is designed: age mean 71.25, rangeŽ 43–87 , pulmonary disease, cardiac disease, ASA . class mean 2.98, range 2–5 , hematocrit mean 40.22 Ž . Ž range 21.2–52.5 , and platelet count mean 234.59, . Ž range 101–566 . Finally, the VA-SRA database val- . ues for the number of RBC units transfused intra-operatively is the desired output value to be used in training.

## 4.2. ANN architecture

One significant problem in the use of ANNs for solving problems in any domain is over-fitting of the training data 3 . Over-fitting occurs when the ANN<sup>w</sup> <sup>x</sup> is too large has too many hidden nodes and simply Ž . memorizes the output values associated with each set of input values. Various RBF architectures are implemented to control for over-fitting of data. As the quantity of hidden nodes rises, the output performance of the ANN should also rise until over-fitting occurs which is marked by a drop in performance.

Another factor to be considered in the design of the RBF ANN architecture is the presence of an optional hidden layer. A second layer will improve the closeness of fit to the data, but may cause a decrease in the extrapolation capabilities of the ANN <sup>w</sup> <sup>x</sup> 3 . RBF networks with only a single cluster prototype layer and with both a prototype and hidden layer are implemented to determine any potential trade-offs between closeness of fit and extrapolation capability for the RBF neural networks predicting the quantity of RBC units required by a specific AAA patient.

All of the RBF network results reported in Section 3 are for RBF neural networks with six input variables, as listed above, and one output variable, the quantity of RBC units that the current patient will require intra-operatively. Single prototype layer RBF networks are implemented with 6, 9, 12, and 18 nodes. Two-layer RBF networks are implemented with a prototype layer of 6, 9, and 12 nodes and a second hidden layer with three, six, and nine nodes Žexcept the six-prototype node model which uses only three or six second hidden layer nodes . Six-. prototype layer nodes is chosen as the minimum quantity to match the size of the input vector and enable a sufficient quantity of prediction clusters. The second conventional hidden layer if presentŽ . varies from three to the size of the prototype layer to enable a rapid approximation of the best performing ANN architecture, while controlling for over-fitting.

The cluster center values are initialized to be random values. Each of the implemented RBF networks is trained for 10,000 presentations of randomly selected data sets from the pool of training data. The first 1800 presentations establish the cluster centers using the adaptive K-means algorithm and the remaining training presentations use supervised learning to establish the connection weights between the prototype layer and hidden layer to theŽ . output node. Following training, all data from the test out-of-sample set is presented a single time toŽ . each trained RBF network and the results are recorded. After the best performing networks are identified an additional prediction trial is carried out using the validation data set data from August 1996Ž through May 1997, that is collected after the RBF research is already started and the feasibility of the ANN approach is inferred to simulate the prospec-. tive use of the RBF neural network systems.

## 5. Results

Before analyzing the RBF neural network results on the medical domain problem of predicting the transfusion requirements of AAA surgical patients, a multiple linear regression model as in Refs.Ž <sup>w</sup> <sup>x</sup> 13,20,21 is constructed to model the identical . problem. As stated previously, regression is the current predominant modeling method in medical research 7,13,20,21,39,43 . The regression model is<sup>w</sup> <sup>x</sup> constructed using the same six variables in the RBF neural network prediction models. Only the presence of pulmonary disease is significant at a level of 0.10 Ž . p value , while the next most significant predictor variable is the ASA class with a p value of 0.12. In a prior research study to use multiple regression for predicting transfusion requirements across several operative groups, hematocrit was the only significant variable this time atŽ $p < 0 . 0 5 )$ , and the coefficient for the hematocrit variable found in the current research’s regression model is nearly identical to the coefficient for hematocrit previously found.

## 5.1. Feasibility test study results( )

Results of the test runs for each of the implemented RBF neural networks is displayed in Table 1 along with the actual number of RBC units transfused, the MSBOS ordered quantity of units, and the regression prediction. The research ANNs and regression model produce real-valued output. The values displayed in Table 1 are rounded to the nearest integer value.

Values in bold font in the table represent perfect predictions number of units predictedŽ <sup>s</sup>number of units actually used and values in italic font represent. under predictions an insufficient quantity for thoseŽ .

Out-of-sample prediction results January–July 1996 Ž .

<table><tr><td rowspan="2">RBF architecture (proto, hidden)</td><td colspan="14">CASE</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Transfused (actual)</td><td>0</td><td>2</td><td>6</td><td>0</td><td>1</td><td>10</td><td>1</td><td>1</td><td>7</td><td>2</td><td>0</td><td>6</td><td>2</td><td>1</td></tr><tr><td>MSBOS</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>Regression</td><td>7</td><td>3</td><td>2</td><td>5</td><td>4</td><td>4</td><td>1</td><td>2</td><td>6</td><td>3</td><td>2</td><td>3</td><td>1</td><td>2</td></tr><tr><td>RBF (6,0)</td><td>6</td><td>3</td><td>3</td><td>5</td><td>3</td><td>3</td><td>3</td><td>3</td><td>6</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>RBF (9,0)</td><td>3</td><td>2</td><td>1</td><td>3</td><td>1</td><td>1</td><td>2</td><td>1</td><td>4</td><td>1</td><td>1</td><td>1</td><td>2</td><td>2</td></tr><tr><td>RBF (12,0)</td><td>5</td><td>2</td><td>2</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>RBF (18,0)</td><td>5</td><td>2</td><td>0</td><td>5</td><td>2</td><td>3</td><td>0</td><td>1</td><td>5</td><td>2</td><td>1</td><td>1</td><td>0</td><td>2</td></tr><tr><td>RBF (6,3)</td><td>3</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>RBF (6,6)</td><td>3</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>RBF (9,3)</td><td>6</td><td>4</td><td>3</td><td>6</td><td>4</td><td>4</td><td>4</td><td>3</td><td>6</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>RBF (9,6)</td><td>4</td><td>2</td><td>1</td><td>4</td><td>2</td><td>2</td><td>1</td><td>2</td><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>RBF (9,9)</td><td>7</td><td>4</td><td>4</td><td>7</td><td>4</td><td>4</td><td>3</td><td>4</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td>RBF (12,3)</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>RBF (12,6)</td><td>4</td><td>2</td><td>2</td><td>4</td><td>2</td><td>2</td><td>3</td><td>2</td><td>3</td><td>2</td><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>RBF (12,9)</td><td>8</td><td>3</td><td>2</td><td>7</td><td>3</td><td>3</td><td>2</td><td>2</td><td>6</td><td>3</td><td>2</td><td>3</td><td>3</td><td>3</td></tr></table>

operations that used the MSBOS quantity of RBC units or less. The problem of under-predicting and consequently under-ordering the number of RBC units requires further examination.

Table 1 illustrates a performance problem with both the ANN and regression models in predicting transfusion requirements. For those operations that transfuse an amount greater than the MSBOS designated amount, neither regression nor ANN models perform well. In fact, only case 9, the AAA operation that transfused 7 RBC units, is regularly predicted to require the MSBOS level or greater. MSBOS also under-orders blood for these four operations. A surgeon or anesthesiologist has much greater knowledge of the probable blood requirements for a specific patient after the operation has started and may order additional units to be prepared as soon as a possible need is detected. For this reason, as long as the RBF neural networks predicted that at least 1 unit of blood would be required, the surgical cases that actually required greater than the MSBOS amount of blood are not used in the calculation of $C / T$ ratios. Neither MSBOS nor the ANNs are able to predict these over-usage cases accurately and these cases do not afford any economic benefit to the hospital or patient.

The number of RBC units below the MSBOS recommended amount for all of the RBF neural networks and the regression analysis are listed in Table 2 along with the number of perfect predictions and the number of under-predictions. Under-predictions for the cases that do not exceed the MSBOS recommended amount of blood should be minimized. Therefore, if an RBF neural network model underpredicts the actual blood transfusion requirements of one of the 10 patients requiring MSBOS amounts or less, then the ANN is penalized by simulating that it required the same quantity as the MSBOS schedule Žto eliminate any perceived benefit gained from under-predicting cases . As noted above, the RBF. ANNs does not perform well in predicting surgical cases that will exceed the MSBOS values, so a reasonable heuristic to implement for the purpose of reducing the quantity of ordered blood is to not permit a value greater than MSBOS to be predicted by the ANNs. The third column in Table 2 indicates the RBC unit order reductions is the ANNs are limited to a maximum prediction value of 4 RBC units. The $C / T$ ratio for MSBOS and each of the RBF neural networks and the regression analysis, assuming a maximum of 4 units may be ordered, is also displayed in Table 2 with those $C / T$ ratios below 2.5 appearing in bold font. Four of the various RBF networks achieved a $C / T$ ratio below 2.5, with only one of these RBF networks making a single under-prediction.

From Table 2, it can be seen that using an RBF neural network can significantly reduce the hospital’s $C / T$ ratio, and correspondingly its blood ordering efficiency. Using the RBC cost values given in Section 1, for the 7 months of the test data, a net savings to the hospital of US\$594 to US\$627 de-Ž pending on which RBF network is used for the . single type of operation of AAA repair can be realized.

As a final test of the RBF neural networks applicability in predicting the transfusion requirements for individual AAA patients, a second holdout sample is gathered following the implementation, training, and testing of the RBF neural networks listed in Tables 1 and 2. The validation data set is for AAA operations performed from August 1996 through March 1997 and consists of 43 cases with transfusions ranging from 0 to 7 units, with a mean of 2.15 units transfused per patient and three operations exceeding the MSBOS designated number of transfusion units. Only the top three RBF ANNs from the feasibility portion of the research are validated: the single-layer, nineprototype node network and both of the two-layer RBF ANNs with six nodes in the prototype layer. Additional training is not performed on the ANNs prior to the validation tests. Results for the three RBF neural networks and the MSBOS schedule are displayed in Table 3.

Table 2  
RBC unit savings from ANN and regression prediction models

<table><tr><td>RBF network or MSBOS</td><td>Units saved for transfused ≤ MSBOS</td><td>Units saved for transfused ≤ MSBOS if MAX = 4</td><td>C/T ratio MAX = 4</td><td>Perfect predictions</td><td>Under-predictions</td></tr><tr><td>MSBOS</td><td>N/A</td><td>N/A</td><td>4.0</td><td>0</td><td>N/A</td></tr><tr><td>(6,0)</td><td>5</td><td>8</td><td>3.2</td><td>0</td><td>0</td></tr><tr><td>(9,0)</td><td>19</td><td>19</td><td>2.1</td><td>4</td><td>1</td></tr><tr><td>(12,0)</td><td>15</td><td>16</td><td>2.4</td><td>3</td><td>0</td></tr><tr><td>(18,0)</td><td>12</td><td>14</td><td>2.6</td><td>3</td><td>3</td></tr><tr><td>(6,3)</td><td>18</td><td>18</td><td>2.2</td><td>3</td><td>0</td></tr><tr><td>(6,6)</td><td>18</td><td>18</td><td>2.2</td><td>3</td><td>0</td></tr><tr><td>(9,3)</td><td>-3</td><td>1</td><td>3.9</td><td>0</td><td>0</td></tr><tr><td>(9,6)</td><td>15</td><td>15</td><td>2.5</td><td>3</td><td>2</td></tr><tr><td>(9,9)</td><td>-5</td><td>1</td><td>3.9</td><td>0</td><td>0</td></tr><tr><td>(12,3)</td><td>9</td><td>9</td><td>3.1</td><td>0</td><td>0</td></tr><tr><td>(12,6)</td><td>12</td><td>12</td><td>2.8</td><td>2</td><td>0</td></tr><tr><td>(12,9)</td><td>4</td><td>11</td><td>2.9</td><td>0</td><td>0</td></tr><tr><td>Regression</td><td>7</td><td>11</td><td>2.9</td><td>1</td><td>1</td></tr></table>

Table 3  
RBF performance on validation data set August 1996–March Ž 1997.

<table><tr><td>RBF network</td><td>Units saved</td><td>C/T ratio</td><td>Perfect predictions</td><td>Under-predictions</td></tr><tr><td>MSBOS</td><td>N/A</td><td>3.90</td><td>2</td><td>N/A</td></tr><tr><td>RBF (9,0)</td><td>77</td><td>2.02</td><td>7</td><td>3</td></tr><tr><td>RBF (6,3)</td><td>83</td><td>1.90</td><td>3</td><td>1</td></tr><tr><td>RBF (6,6)</td><td>85</td><td>1.85</td><td>6</td><td>0</td></tr></table>

Values displayed in Table 3 use the heuristic rule that limits the RBF neural network predicted value to a maximum equal to the MSBOS value. Although the MSBOS schedule has a slightly better C<sup>r</sup>T ratio during the 8 validation months, the three RBF networks that are tested on the validation data all significantly outperform the MSBOS. The best performing network, the two-layer RBF with six nodes in each layer, achieves a 53% reduction in the quantity of unneeded RBC units that are ordered, which corresponds to an additional US\$2772 savings for the AAA operation at the studied hospitals, or US\$3399 for the combined test and evaluation periods.

Unfortunately, the larger evaluation data set introduces cases that are under-predicted for both the single-layer RBF network and the two hidden layer network with three nodes in the second layer. Reducing the under-predictions of these two RBF neural networks is discussed in Section 5.3. One of the under-predictions for both networks occurs in a data sample from the Haley V.A. database, while the other two under-predictions for the single prototype layer network occur when predicting on the 27 cases from the Lexington V.A. hospital. While the patient populations at the two hospitals are demographically similar, differences in transfusion protocols or other operative procedures could produce minor variations in the data model that would explain the marginally reduced performance of this one ANN. The other two ANN architectures appear to be more robust in that they are unaffected by the potential noise introduced from the second data source.

Several RBF network architectures are implemented to avoid out-of-sample prediction problems associated with over-fitting of the data. Because every possible RBF neural network architecture has not been implemented, the results presented in this section should be viewed as a lower limit on the possible results achievable with RBF neural networks for the problem of predicting the transfusion requirements for individual patients about to undergo AAA operations.

## 5.2. ImproÕing the ANN prediction performance

Other than the hidden layer architecture, two additional factors may have a significant effect on the performance of an ANN system: data quantity and data quality. Data quantity refers to the problem of not specifying enough of the domain relevant variables to enable the ANN system to learn an accurate categorization or prediction algorithm. Data quality is concerned with the signal to noise ratio in the training data. Each factor is considered separately in this section. An identical research design is used for all modifications to the RBF neural networks: after training, first establish the feasibility of the approach on the smaller test data set 14 cases , then if war-Ž . ranted test the new ANNs on the larger evaluation data set 43 cases .Ž .

In Section 4, two of the available input variables are not used, PT and PTT, because they are measures of coagulation and a possible correlation exists with the variable platelet count. However, PT and PTT are measures of a different stage of coagulation than platelet count and their inclusion in the input vector may increase the transfusion requirement prediction performance of the ANNs. Despotis et al. 11 claim<sup>w</sup> <sup>x</sup> that the inclusion of PT and PTT in a transfusion protocol algorithm was able to reduce the average number of intra-operative transfusions per patient from 9.9 to 4.9. Therefore, an eight-variable input vector is constructed containing the original six-input variables: age, pulmonary and coronary disease, ASA class, hematocrit, and platelet count, with the addition of PT and PTT values.

Various ANN hidden node architectures are designed to account for the larger quantity of input variables and enable a robust and fair comparison against the six-variable model. Several of the original training cases are eliminated because of missing PT or PTT values. Test cases are identical for the six- and eight-input-variable ANN models. The pattern of predictions for all of the eight-input-variable ANNs is similar to that of the six-input-variable ANNs, with case 9 requiring 7 RBC units forŽ transfusion being the only case exceeding the MS-. BOS values to have the MSBOS or greater RBC units predicted and cases 1 and 4 also being predicted above the MSBOS value by most of the eight-variable ANNs. Results, with an upper limit of the MSBOS amount, for the 10 cases that transfused the MSBOS amount or less are displayed in Table 4.

Table 4 shows that the best C<sup>r</sup>T ratios for the eight-variable model with values for PT and PTT do not match the $C / T$ ratios for the six-variable model. Inclusion of the PT and PTT data does not improve the RBF neural network’s prediction performance. An interesting outcome does occur when the PT and PTT variables are utilized by the RBF neural network. The quantity of operations for which the ANN predicts the exact number of RBC units to be transfused, 5, exceeds the best six-variable models. Unfortunately, the ANNs that produce the greatest quantity of AperfectB predictions also under-predict 2 other operations and under-prediction is a quality to be avoided in the ANN models, as it may negatively impact the health of the patient.

Although increasing the data variable quantity does not improve the RBF neural network performance, altering the training data quality to better reflect the Areal worldB may improve the ANN’s performance. Sharda and Wilson 37,48 have shown<sup>w</sup> <sup>x</sup> that ANNs perform better if the training data set mix more closely resembles the out-of-sample data mix. For the medical domain problem of predicting the transfusion requirements for patients, the normal data mix is expected to be approximately 90% of the cases at or below MSBOS levels of transfusions 1 .<sup>w</sup> <sup>x</sup>

Table 4  
Results for ANNs with PT and PTT added as input variables

<table><tr><td>RBF network (proto, hidden)</td><td>Units saved</td><td>C/T ratio</td><td>Perfect predictions</td><td>Under-predictions</td></tr><tr><td>MSBOS</td><td>N/A</td><td>4.0</td><td>0</td><td>N/A</td></tr><tr><td>RBF (6,0)</td><td>16</td><td>2.4</td><td>3</td><td>0</td></tr><tr><td>RBF (8,0)</td><td>9</td><td>3.1</td><td>1</td><td>0</td></tr><tr><td>RBF (10,0)</td><td>4</td><td>3.6</td><td>0</td><td>0</td></tr><tr><td>RBF (6,3)</td><td>17</td><td>2.3</td><td>3</td><td>2</td></tr><tr><td>RBF (6,6)</td><td>17</td><td>2.3</td><td>5</td><td>2</td></tr><tr><td>RBF (6,8)</td><td>15</td><td>2.5</td><td>2</td><td>0</td></tr><tr><td>RBF (8,6)</td><td>11</td><td>2.9</td><td>1</td><td>0</td></tr><tr><td>RBF (8,8)</td><td>17</td><td>2.3</td><td>4</td><td>1</td></tr><tr><td>RBF (8,10)</td><td>17</td><td>2.3</td><td>5</td><td>2</td></tr><tr><td>RBF (9,3)</td><td>14</td><td>2.6</td><td>3</td><td>0</td></tr><tr><td>RBF (9,6)</td><td>2</td><td>3.8</td><td>0</td><td>0</td></tr><tr><td>RBF (9,9)</td><td>12</td><td>2.8</td><td>2</td><td>3</td></tr><tr><td>RBF (12,6)</td><td>11</td><td>2.9</td><td>1</td><td>0</td></tr><tr><td>RBF (12,9)</td><td>7</td><td>3.3</td><td>0</td><td>0</td></tr><tr><td>RBF (12,12)</td><td>9</td><td>3.1</td><td>1</td><td>0</td></tr></table>

Other medical research studies 21,28 have re-<sup>w</sup> <sup>x</sup> moved outliers from their data sets to obtain more reliable data models. Outliers are typically caused by highly unusual and unpredictable medical scenarios. The training data for the RBF neural network research presented in this article has a mean of 2.76 units, a standard deviation, , of 4.81 units and a large positive skewedness value. One outlier exists that is 9 standard deviations away from the mean. If this value, a transfusion of 44 units, is eliminated from the data, the new mean is 2.31 units and has a of 2.21 and a very slight positive skewedness. The new mean, , and skewedness values are comparable to similar values for the test and validation data sets. Since blood is ordered in whole units, the mean value for the modified training data population is rounded up to 3 units, indicating that 95% 2Ž . of all operations should require at most 8 units of blood.

Two reduced training sets are constructed to test for the bias effect of an extreme outlier. The first reduced training set A removes only the single caseŽ . that transfused 44 RBC units and the second reduced training set B also removes the 44-unit case inŽ . addition the next highest transfusion case, 12 units Ž . <sup>)</sup>2 standard deviations , and two randomly selected 0 unit transfusion cases. The 0 transfusion unit cases are removed from the B reduced training set to maintain the general shape of the distribution of the training set while removing extreme positive outliers. The three top performing RBF neural network architectures from Section 5 are used to build six new ANNs that are trained with each of the two new reduced training sets. The 14 test cases are identical to the original test cases. Results for the RBF neural networks trained with the reduced training sets A and B is displayed in Table 5, along with the actual transfusions and the MSBOS amounts.

The C<sup>r</sup>T ratios of operations less than or equal to the MSBOS amount for the three RBF neural networks trained on training set A are: 2.1 9,0 , 2.0Ž . Ž . Ž . 6,3 , and 2.1 6,6 , while the C<sup>r</sup>T ratios for the three RBF neural networks trained on training set B are: 2.2, 2.1, and 2.0, respectively. For this particular test set of data, the two-layer RBF neural networks trained on the reduced size training sets outperformed their full training set equivalents. However, for the training set A RBF two-layer neural networks, several under-predictions also occur. Underpredictions are not present for the two-layer RBF neural networks trained on training set B. Pruning of the training data set can improve the RBF neural network’s performance, but there is a risk that the pruning of only cases with a very large number of transfusion units may introduce under-prediction errors.

Table 5  
RBF predictions using reduced training sets

<table><tr><td rowspan="2">RBF Architecture (proto, hidden)</td><td colspan="14">Case</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>Transfused (Actual)</td><td>0</td><td>2</td><td>6</td><td>0</td><td>1</td><td>10</td><td>1</td><td>1</td><td>7</td><td>2</td><td>0</td><td>6</td><td>2</td><td>1</td></tr><tr><td>MSBOS</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td colspan="15">Set A (1 training case removed: 44 unit transfusion case)</td></tr><tr><td>RBF (9,0)</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>RBF (6,3)</td><td>2</td><td>1</td><td>1</td><td>1</td><td>3</td><td>2</td><td>1</td><td>1</td><td>6</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>RBF (6,6)</td><td>2</td><td>1</td><td>0</td><td>2</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td colspan="15">Set B (4 cases removed: 44,12,0,0 transfusion units)</td></tr><tr><td>RBF (9,0)</td><td>3</td><td>2</td><td>1</td><td>1</td><td>2</td><td>5</td><td>0</td><td>1</td><td>7</td><td>2</td><td>1</td><td>1</td><td>1</td><td>2</td></tr><tr><td>RBF (6,3)</td><td>3</td><td>2</td><td>2</td><td>2</td><td>2</td><td>3</td><td>2</td><td>2</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr><tr><td>RBF (6,6)</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td><td>4</td><td>2</td><td>2</td><td>2</td><td>2</td><td>2</td></tr></table>

A different effect is also observed from the data presented in Table 5. While the general performance of the RBF neural networks on cases that require transfusions greater than the MSBOS amount remains poor, all of the evaluated networks performed better on case 9, the case that required 7 RBC units to be transfused. The single-layer RBF neural network trained on reduced training set B is the only ANN that predicts the correct quantity of units for case 9 and additionally predicts a greater than MS-BOS amount for one of the remaining three cases that exceed the MSBOS transfusion amount. Further research is needed to investigate if elimination of specific types of outliers and possible maintenance of training set distribution will enable RBF neural networks to predict all operations both above andŽ below the MSBOS amount that lie within 2. of the mean number of transfusions for that operation.

The reduced training set B is used to predict the blood requirements for the validation data set. Table 6 indicates the $C / T$ ratio and other pertinent data for predictions of the evaluation data sets 43 casesŽ . transfusion requirements. Comparing Table 6 with Table 3, a significant improvement in the C<sup>r</sup>T ratio is observed. A single under-prediction is observed for each of the three RBF architectures trained on the reduced training set removal of the 44-, 12-, andŽ two 0-transfusion cases . This under-prediction is. identical for all three ANNs, occurring on a data sample from the Lexington V.A. and for a case that transfused the full MSBOS amount of blood. Each of the RBF neural networks predicted a transfusion level of 3 units of blood, which just misses the actual value required for this one operation.

## 5.3. Reducing under-predictions with retraining

As noted in Section 5.1, two of the RBF neural networks suffer from an under-prediction, with one of these ANNs suffering two additional under-predictions. The under-prediction case that is common to both network architectures occurs late in 1996 Ž . December . To account for minor variations in surgical practice and transfusion protocols, the RBF networks are incrementally retrained 1996 data values. The test data set, January 1996 through July 1996, is used to add additional training to the ANN model. Usage of more recent data to incrementally train ANNs enables an ANN to AlearnB evolving trends in the data model.

The resulting prediction performance for the RBF neural networks on the evaluation data set, August

Table 6  
RBF performance with training set B for evaluation data August Ž 1996–March 1997.

<table><tr><td>RBF network</td><td>Units saved</td><td>C/T ratio</td><td>Perfect predictions</td><td>Under-predictions</td></tr><tr><td>RBF (9,0)</td><td>93</td><td>1.63</td><td>10</td><td>1</td></tr><tr><td>RBF (6,3)</td><td>114</td><td>1.12</td><td>12</td><td>1</td></tr><tr><td>RBF (6,6)</td><td>103</td><td>1.39</td><td>9</td><td>1</td></tr></table>

1996 through March 1997, produces nearly identical performance, with the exception that the under-prediction from December disappears. While the number of perfect predictions is incremented by one, there is no change in the $C / T$ ratio values or units of blood saved.

## 5.4. Statistical eÕaluation of results

The direct comparison of $C / T$ ratios is comparable to a standard comparison of the differences in the prediction performance of the RBF neural network models to the existing MSBOS methodology. The results of the research indicate that ANN models that predict transfusion requirements offer a significant improvement over the traditional MSBOS.

A further analysis of the significance of the improvement offered by ANNs is obtained by conducting a paired t-test. The paired t-test is appropriate since both methodologies are attempting to predict the same discrete value, the number of blood units to be transfused to a patient. A null hypothesis $H _ { 0 }$ that the MSBOS and RBF neural network are the same with regard to prediction capabilities is tested. The six RBF neural networks, the three modeled networks for both the full training set and the reduced training set B, are individually compared against MSBOS using the null hypothesis in separate paired t-tests. All six RBF network t-tests reject the null hypothesis with a significance level well below 0.001 Ž . p value .

Additionally, MSBOS produces a Root Mean Square Error RMSE of 3.15 units, while the bestŽ . RBF neural network, the two-layer architecture with six nodes in the second layer using the reduced training set B, produces an RMSE of 1.67332. The RMSE results, along with the mean values calculated for the paired t-test, indicate that the RBF neural networks will save an average of 1–2 units of blood per AAA operation performed.

## 6. Conclusions

The research presented in this article addresses the question: can ANN technology be used to reduce overall health care expenditures. Specifically, RBF ANNs are implemented to predict the number of

RBC units that an individual patient will require for transfusion during AAA operations. Results are presented to show that RBF neural networks are capable of reducing the overall quantity of blood units ordered for operations. The number of blood units crossmatched ordered over the number of unitsŽ . transfused $( C / T )$ ratio is a standard measure of transfusion efficiency 1,25,32,36 . Using the MS-<sup>w</sup> <sup>x</sup> BOS, if only those operations that do not exceed the MSBOS quantity of blood units transfused are considered, $\mathrm { ~ a ~ } C / T$ ratio of 3.92 results. The RBF neural networks achieve a $C / T$ ratio of 1.98. Further modification of the training set to evenly remove high and low data samples outliers , improves the RBF pre-Ž . dicted $C / T$ ratio to 1.29. A corresponding savings of US\$3399 is realized for the 50 cases of this single operation.

Furthermore, a reduction in the quantity of blood ordered, without under-ordering needed blood, may limit inappropriate transfusions 27 . Inappropriate <sup>w</sup> <sup>x</sup> transfusions have a negative impact on the health of patients 11,19 . Over-ordering of multiple blood <sup>w</sup> <sup>x</sup> units facilitates and may be a cause of inappropri- Ž . ate transfusions. The RBF neural networks enable a more precise quantity of blood to be ordered for individual patients.

Is the RBF neural network technique generalizable to other operations? A preliminary evaluation of the robustness of the RBF neural network technique for predicting the transfusion requirements of individual surgical patients is performed for the open prostatectomy operation. A training set of 91 cases with transfusions ranging from 0 to 4 units from 1992 through 1995 and a test set of 19 cases with transfusions ranging from 0 to 2 units from January 1996 to July 1996 is obtained from the VA-SRA database. The open prostatectomy operation has an MSBOS value of 2 units at the hospital were theŽ research is performed and produced a. $C / T$ ratio of 4.75. Only the three top performing ANNs from the AAA operation research are implemented. The single hidden layer nine nodes ANN achieved a Ž . $C / T$ ratio of 2.875 saving 15 units from the MSBOS prescribed amount. Both of the two-layer ANNS sixŽ nodes in the first prototype layer and either three or six nodes in the second hidden layer save 16 units . below MSBOS and achieve a $C / T$ ratio of 2.75. While the prostatectomy transfusion prediction ANNs did not succeed in lowering the $C / T$ ratio below 2.5, they did lower the average usage of blood units by 2.0 units per operation, similar to the best results obtained for the AAA transfusion prediction ANNs.

Use of ANN methods to solve the problem of ordering blood units for operations can result in significant cost savings and has the potential to improve patient health if inappropriate transfusions Ž are correspondingly reduced . The two-layer six. Ž nodes in each layer ANN produced a potential . savings of US\$891 US\$957 if pruned training dataŽ sets are used that would correspond to an annual. savings of over US\$1000 for the transfusion costs of the single class AAA of operations. Ordered andŽ . unused blood costs hundreds of thousands of dollars per year per hospital 32 . A significant savings is <sup>w</sup> <sup>x</sup> realizable in the nation’s health car expenditure through the use of ANNs.

## Acknowledgements

This research was supported in part by the University of South Florida, Research and Creative Scholarship Grant, a1407938RO.

## References

<sup>w</sup> <sup>x</sup> 1 H.I. Atrah, G. Galea, S.J. Urbanial, The sustained impact of a group and screen and maximum surgical blood ordering schedule policy on the transfusion practice in gynaecology and obstetrics, Clinical and Laboratory Haemotology 17 2Ž . Ž . 1995 177–181.

<sup>w</sup> <sup>x</sup> 2 A. Bansal, R.J. Kauffman, R.R. Weitz, Comparing the modeling performance of regression and neural networks as data quality varies: a business value approach, Journal of Management Information Systems 10 1 1993 11–32. Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 E. Barnard, L. Wessels, Extrapolation and interpolation in neural network classifiers, IEEE Control Systems 12 5Ž . Ž .1992 50–53.

4 W.G. Baxt, Application of artificial neural networks to clinical medicine, The Lancet 346 1995 1135–1138 OctoberŽ . Ž 28 ..

<sup>w</sup> <sup>x</sup> 5 W.G. Baxt, J. Skora, Prospective validation of artificial neural network trained to identify acute myocardial infarction, The Lancet 347 1996 12–15 January 6 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 R.H. Brook, C.J. Kamberg, E.A. McGlynn, Health system reform and quality, JAMA 276 6 1996 476–480 AugustŽ . Ž . Ž 14 ..

<sup>w</sup> <sup>x</sup>7 P.G. Budny, P.J. Regan, A.H. Roberts, The estimation of

blood loss during burns surgery, Burns 19 2 1993 , Ž . Ž . 134–137.

<sup>w</sup> <sup>x</sup> 8 V. Cherkassky, H. Lari-Najafi, Data representation for diagnostic neural networks, IEEE Expert 7 5 1992 43–53.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 J.A. Clark, M.M. Ayoub, Blood and component wastage report: a quality assurance function of the hospital transfusion committee, Transfusion 29 2 1989 139–142.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 Department of Veterans Affairs Veterans Health ServicesŽ and Research Administration , National VA Surgical Risk. Study, Technical Report SDR a91-007 October 1991 .Ž .

<sup>w</sup> <sup>x</sup> 11 G.J. Despotis, J.E. Grishaber, L.T. Goodnough, The effect of an intraoperative treatment algorithm on physicians’ transfusion practice in cardiac surgery, Transfusion 34 4 1994Ž . Ž . 290–296.

<sup>w</sup> <sup>x</sup> 12 G. Dorffner, G. Porenta, On using feedforward neural networks for clinical diagnostic tasks, Artificial Intelligence in Medicine 6 5 1994 417–435.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 B.H. Dorman, F.G. Spinale, M.K. Bailey, J.M. Kratz, R.C. Roy, Identification of patients at risk for excessive blood loss during coronary artery bypass surgery: thromboelastograph vs. coagulation screen, Anesthesia & Analgesia 76 4 1993Ž . Ž . 694–700.

<sup>w</sup> <sup>x</sup>14 R. Dybowski, V. Gant, Artificial neural networks in pathology and medical laboratories, The Lancet 346 1995 1203–Ž . 1207 November 4 .Ž .

<sup>w</sup> <sup>x</sup>15 V.A. Ferraris, V. Gildengorin, Predictors of excessive blood use after coronary artery bypass grafting, Journal of Thoracic and Cardiovascular Surgery 98 4 1989 492–497. Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 R.E. Fisher, J.A. Scott, E.L. Palmer, Neural networks in ventilation–perfusion imaging, Radiology 198 1996 699– Ž . 706 March . Ž .

<sup>w</sup> <sup>x</sup> 17 J.M. Forbes, M.D. Anderson, G.F. Anderson, G.C. Bleecker, E.C. Rossi, G.S. Moss, Blood transfusion costs: a multicenter study, Transfusion 31 4 1991 318–323.Ž . Ž .

<sup>w</sup> <sup>x</sup> 18 W.A. Ghali, A. Palepu, W.G. Paterson, Evaluation of red blood cell transfusion practices with the use of preset criteria, Canadian Medical Association Journal 150 9 1994 1449–Ž . Ž . 1454.

<sup>w</sup> <sup>x</sup> 19 L.T. Goodnough, R.W. Soegiarso, J.D. Birkmeyer, H.G. Welch, Economic impact of inappropriate blood transfusions in coronary artery bypass graft surgery, The American Journal of Medicine 94 5 1993 509–514.Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 J.M. Grosflam, E.A. Wright, P.D. Cleary, J.N. Katz, Predictors of blood loss during total hip replacement surgery, Arthritis Care and Research 8 3 1995 167–173.Ž . Ž .

<sup>w</sup> <sup>x</sup>21 P.B. Hasley, J.R. Lave, B.H. Hanusa, V.C. Arena, G. Ramsey, W.N. Kapoor, M.J. Fine, Variation in the use of red blood cell transfusions, Medical Care 33 11 1995 1145–Ž . Ž . 1160.

<sup>w</sup> <sup>x</sup> 22 P.B. Hasley, J.R. Lave, W.N. Kapoor, The necessary and the unnecessary transfusion: a critical review of reported appropriateness rates and criteria for red cell transfusions, Transfusion 34 2 1994 110–115.Ž . Ž .

<sup>w</sup> <sup>x</sup> 23 M.H. Hassoun, C. Wang, A.R. Spitzer, NNERVE: neural network extractions of repetitive vectors for electromyography — Part II: Performance analysis, IEEE Transactions on Biomedical Engineering 41 11 1994 1053–1061. Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 T. Iwasaki, T. Nishiyama, M. Otsuka, Y. Ohara, O. Kobayashi, K. Seto, Evaluation of preoperative blood preparation and blood consumption for implementation of type and screen and maximum surgical blood order schedule, Masuix 41 6 1995 880–884.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 B. Jaffray, P.M. King, J. Gillon, Efficiency of blood use and prospects for autologous transfusion in general surgery, Annals of the Royal College of Surgeons of England 73 4Ž . Ž . 1991 235–238.

<sup>w</sup> <sup>x</sup> 26 A.K. Jain, J. Mao, K.M. Mohiuddin, Artificial neural networks: a tutorial, Computer 29 3 1996 31–44.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 C.J. Julius, K.S. Purchase, B.E. Isham, P.L. Howard, Patterns of autologous blood use in elective orthopedic surgery: does the availability of autologous blood change transfusion behavior? Vox Sanguinis 66 3 1994 171–175.Ž . Ž .

<sup>w</sup> <sup>x</sup>28 P. Lapuerta, S.P. Azen, L. LaBree, Use of neural networks in predicting the risk of coronary artery disease, Computers in Biomedical Research 28 1 1995 38–52.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 F.A. Lederle, S.E. Wilson, G.R. Johnson, F.N. Littooy, C. Acher, L.M. Mesina, D.B. Reinke, D.J. Ballard, Design of the abdominal aortic aneurysm detection and management study, Journal of Vascular Surgery 20 2 1994 296–303. Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 M.A. Leon, Binary response forecasting: comparison be- ´ tween neural networks and logistic regression analysis, World Congress on Neural Networks — San Diego, vol. 2, 1994Ž . 244–247, June 5–9 , San Diego, CA. Ž .

<sup>w</sup> <sup>x</sup> 31 M.A. Leon, J. Rasanen, D. Mangar, Neural network-based´ ¨ ¨ detection of esophageal intubation, Anesthesia & Analgesia 78 1994 548–553.Ž .

<sup>w</sup> <sup>x</sup> 32 T.A. Lowery, J.A. Clark, Successful implementation of maximum surgical blood order schedule, Journal of the Medical Association of Georgia 78 3 1989 155–158.Ž . Ž .

<sup>w</sup> <sup>x</sup> 33 G. Montague, J. Morris, Neural-network contributions in biotechnology, Trends in Biotechnology 12 8 1994 312–Ž . Ž . 324.

<sup>w</sup> <sup>x</sup> 34 J. Moody, C.J. Darken, Fast learning in networks of locallytuned processing elements, Neural Computation 1 2 1989Ž . Ž . 281–294.

35 W.G. Murphy, P. Phillips, A. Gray, L. Heatley, J. Palmer, D. Hopkins, R.J. Crawford, Blood use for surgical patients: a study of Scottish hospital transfusion practices, Journal of the Royal College of Surgeons of Edinburgh 40 1 1995Ž . Ž . 10–13.

<sup>w</sup> <sup>x</sup> 36 R.H. Palmer, J.G. Kane, W.H. Churchill, L. Goldman, A.L. Komaroff, Cost and quality in the use of blood bank services for normal deliveries, cesarean sections, and hysterectomies, JAMA 256 2 1986 219–223 July 11 .Ž . Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 R. Sharda, R.L. Wilson, Neural network experiments in business-failure forecasting: predictive performance measurement issues, International Journal of Computational Intelligence and Organizations 1 2 1996 107–117.Ž . Ž .

<sup>w</sup> <sup>x</sup> 38 M. Smith, Neural networks for statistical modeling, Van Nostrand–Reinhold, New York, 1993.

<sup>w</sup> <sup>x</sup> 39 D.D. Tran, E. Van Onselen, A. Wensink, M.A. Cuesta, Factors related to multiple organ system failure and mortality in a surgical intensive care unit, Nephrology Dialysis Transplantation 9 Suppl. 4 1994 172–178.Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 G.D. Tourassi, C.E. Floyd, Lesion size quantification in SPECT using an artificial neural network classification approach, Computers in Biomedical Research 28 3 1995Ž . Ž . 257–270.

<sup>w</sup> <sup>x</sup> 41 E.L. Wallace, D.M. Surgenor, H.S. Hao, J. An, R.H. Chapman, W.H. Churchill, Collection and transfusion of blood and blood components in the United States, 1989, Transfusion 33 2 1993 139–144.Ž . Ž .

42 R.C. Watt, A comparison of artificial neural networks and classical statistical analysis, Anesthesiology 75 Suppl. 3AŽ . Ž . 1991 A451.

<sup>w</sup> <sup>x</sup> 43 R.S. Weber, A model for predicting transfusion requirements in head and neck surgery, Laryngoscope 105 8 1995Ž . Ž . 1–17.

<sup>w</sup> <sup>x</sup> 44 H.G. Welch, K.R. Meehan, L.T. Goodnough, Prudent strategies for elective red blood cell transfusion, Annals of Internal Medicine 116 5 1992 393–402.Ž . Ž .

<sup>w</sup> <sup>x</sup> 45 H.C. West, G. Jurkovich, C. Donnell, A. Luterman, Immediate prediction of blood requirements in trauma victims, Southern Medical Journal 82 2 1989 186–189.Ž . Ž .

<sup>w</sup> <sup>x</sup>46 B. Widrow, D.E. Rumelhart, M.A. Lehr, Neural networks: applications in industry, Business and Science Communications of the ACM 37 3 1994 93–105.Ž . Ž .

<sup>w</sup> <sup>x</sup> 47 M.F. Wilkins, C.W. Morris, L. Boddy, A comparison of Radial Basis Function and backpropagation neural networks for identification of marine phytoplankton from multivariate flow cytometry data, Computer Applications in the Biosciences 10 3 1994 285–294.Ž . Ž .

<sup>w</sup> <sup>x</sup> 48 R.L. Wilson, R. Sharda, Bankruptcy prediction using neural networks, Decision Support Systems 11 5 1994 545–557.Ž . Ž .

<sup>w</sup> <sup>x</sup> 49 Y. Yasuda, Y. Sugiura, M. Yanagimoto, H. Kawakami, Y. Goto, An analysis of the status of surgical transfusion and a trial of Maximum Surgical Blood Order Schedule MSBOSŽ . in Fukui Medical School Hospital, Masui 42 8 1993Ž . Ž . 1237–1240.

## Glossary

Glossary medical definitions are obtained from( Stedman’s Medical Dictionary, 25th edn)

AAA: Abdominal Aortic Aneurysm, an aneurysm in the aorta, above the Iliac arteries.

Aneurysm: circumscribed dilation of an artery.

ASA class: a rating scale that measures the degree of a patient’s systemic illness prior to an operation, ranging from 1 through 4 with 4 being the most ill.

Crossmatch: a test for incompatibility between donor and recipient blood, carried out prior to transfusion to avoid potentially lethal hemolytic reac-

tions, performed by mixing a sample of red blood cells of the donor with plasma of the recipient.

Hematocrit: percentage of the volume of blood occupied by red blood cells.

Partial-thromboplastin time: a measure of blood coagulation factor activity, intrinsic pathway, measured in seconds.

Platelet: an irregularly shaped cytoplasmic fragment of a megakaryocyte found in the peripheral blood where it functions in clotting.

Platelet count: a measure of the quantity of platelets occurring in the blood, indicating the strength of a blood clot.

Prostatectomy: removal of a part of or all of the prostate.

Prothrombin: a glycoprotein, in the presence of thromboplastin and calcium ion converts to thrombin which in turn converts fibrinogen to fibrin, resulting in coagulation of the blood.

Prothrombin time: a measure of blood coagulation factor activity, extrinsic pathway, in seconds.

Radial basis function: a transfer function that responds selectively to input over a small portion of the input space, $f ( x )$ is largest for x <sup>s</sup> cluster\_center and $f ( x )$ decreases to zero as the absolute difference between x and the cluster\_center increases.

RBC unit: Red Blood Cell, usually packed red blood cells for transfusion.

![](/api/attachments/4UHJ4AC3/fulltext/images/a174c6aa96ccfc0378e45116130c409fb52b17bcac055e2544cd53c63aaf88f8.jpg)

Steven Walczak is an Assistant Professor in the College of Business and Administration at the University of Colorado at Denver.

He received his PhD in artificial intelli-Ž gence from the University of Florida in. 1990. Dr. Walczak’s current research interests are in applied artificial intelligence methods including neural networks, expert systems, and intelligent agents. Applications in the domains of finance and medicine are currently un-

der research. He has been published in numerous academic journals including the Journal of Management Information Systems, Expert Systems with Applications, and IEEE’s Transactions on Systems, Man, and Cybernetics.
