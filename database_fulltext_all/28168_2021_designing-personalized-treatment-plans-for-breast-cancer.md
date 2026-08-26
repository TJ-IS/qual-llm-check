---
otero_id: 28168
otero_key: "UTFSYS2Y"
title: "Designing Personalized Treatment Plans for Breast Cancer"
authors: "Wei Chen; Yixin Lu; Liangfei Qiu; Subodha Kumar"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing Personalized Treatment Plans for Breast Cancer

Wei Chen,<sup>a</sup> Yixin Lu,<sup>a</sup> Liangfei Qiu,<sup>b</sup> Subodha Kumar<sup>c</sup>

<sup>a</sup> School of Business, George Washington University, Washington, District of Columbia 20052; <sup>b</sup> Warrington College of Business, University of Florida, Gainesville, Florida 32611; <sup>c</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122 Contact: wei\_chen@gwu.edu (WC); yixinlu@gwu.edu, https://orcid.org/0000-0001-6515-1940 (YL); liangfei.qiu@warrington.u<sup>fl</sup>.edu, https://orcid.org/0000-0002-8771-9389 (LQ); subodha@temple.edu, https://orcid.org/0000-0002-4401-7950 (SK)

Received: August 28, 2019<sub>Revised:</sub> Accepted: Published Online in Articles in Advance: August 9, 2021

https://doi.org/10.1287/isre.2021.1002

Copyright:

Abstract. Breast cancer remains the leading cause of cancer deaths among women around the world. Contemporary treatment for breast cancer is complex and involves highly specialized medical professionals collaborating in a series of information-intensive processes. This poses signi<sup>fi</sup>cant challenges to personalization and customization of treatment plans for individual patients. In this research, we follow the information systems design science paradigm and propose a novel framework for decision support of treatment planning for early stage breast cancer patients undergoing radiotherapy. The core of our framework consists of a predictive model that predicts patient outcome of a treatment plan based on clinical and patient characteristics, and an optimization model that optimizes the treatment plan based on predicted outcomes of different plans. Using a series of simulation experiments, we show that the treatment plans generated from our framework consistently outperform those from the existing practices in balancing the risk of local tumor recurrence and radiation-induced adverse effects, thereby reducing the treatment cost associated with these adverse effects. Our research contributes to the growing literature that examines the potential of healthcare information technologies in delivering cost-effective care. Further, we also contribute to healthcare practices by providing models and tools that have pragmatic value as part of the clinical care delivery system.

History: Yong Tan, Senior Editor; Lucy (Lu) Yan, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.1002.

Keywords: clinical decision support <sub>•</sub> design science <sub>•</sub> healthcare information technologies <sub>•</sub> personalized medicine <sub>•</sub> treatment planning

## 1. Introduction

Breast cancer is the most frequently diagnosed cancer among women worldwide. In the United States alone, more than 3.5 million women had been diagnosed with breast cancer by 2020.<sup>1</sup> The immense burden is not just from the large number of lives it touches, but also from its signi<sup>fi</sup>cant economic impact. According to a recent article published in Forbes, the cost of treating breast cancer was expected to reach \$16.5 billion by 2020 (Seegert 2020).

Currently, most of the early stage breast cancer patients<sup>2</sup> are treated with radiotherapy (Smith et al. 2018, Cardoso et al. 2019) after surgery to reduce the risk of local tumor recurrence. Although the general goal of radiotherapy is straightforward (i.e., targeting tumor cells, while sparing the surrounding normal cells and organs at risk), the complex interplay of various clinical and nonclinical factors in the treatment trajectory (Valdes et al. 2017) imposes signi<sup>fi</sup>cant challenges in optimizing treatment plans for individual patients. Physicians<sup>3</sup> are relying on their domain knowledge and experience in making treatment-planning decisions. This raises the question of whether and to what extent these knowledge-driven or experience-based treatment plans are effective for individual patients. In particular, recent studies have reported that patients who receive a conventional radiotherapy are at higher risks of developing lung cancer and heart diseases (Darby et al. 2013, Grantzau et al. 2014).

In this research, we are interested in the following research question in the context of radiotherapy planning: How can we incorporate patient-speci<sup>fi</sup>c information to predict treatment outcomes and adapt treatment plans for individual patients? To address this question, we follow the information systems design science paradigm (Hevner et al. 2004) and propose a novel framework for decision support of radiotherapy planning for individual patients. Our framework consists of a predictive model and an optimization model. The predictive model integrates patient and clinical information revealed in the treatment trajectory and predicts patient outcome of a given treatment plan. The optimization model optimizes a treatment plan based on clinical targets and predicted outcomes of different plans. By accounting for patient-speci<sup>fi</sup>c responses to different plans, our framework enables personalization and customization of treatment plans for individual patients.

We evaluate our framework with synthetic patients that are created based on real-world clinical data sets. Based on a series of simulation experiments with varying clinical targets, we show that our framework consistently outperforms the existing planning methods in balancing the risk of local tumor recurrence and radiation-induced adverse effects. In particular, we <sup>fi</sup>nd that personalized treatment plans generated from our framework can reduce the average radiation dose to a patient’s lung and heart by more than 90%, and thereby lower the risk of developing lung cancer and heart diseases substantially. Given the annual estimated new cases of breast cancer,<sup>4</sup> the personalized treatment-planning framework can reduce the annual treatment cost associated with radiation-induced lung cancer and heart diseases by more than \$200 million.

Our study makes several contributions to research and practice. To start with, we contribute new insights to the design and meaningful use of healthcare information technologies (HIT). Despite the increasing consensus about their promises in improving care quality and ef<sup>fi</sup>ciency, while reducing cost, the design and deployment of HIT are still in their infancy (Agarwal et al. 2010, Fichman et al. 2011). Speci<sup>fi</sup>cally, prior studies have primarily focused on the design of novel models and methods in clinical diagnostics (see Bardhan et al. 2015 and Lin et al. 2017, for example); few have examined the potential of HIT in facilitating treatment decisions. Our research <sup>fi</sup>lls this gap in the literature by designing a novel framework for decision support of personalized radiotherapy planning. Our treatment-planning framework incorporates clinical expertise from radiologists, pathologists, and radiation oncologists. From the design science perspective, our study provides implications about how to integrate domain knowledge into the design of clinical decision-support systems.

We also contribute to the literature that measures the payoff and impact of HIT. As Agarwal et al. (2010, p. 802) point out, “an estimation of the overall impact of HIT across various care settings is still much needed, but it has become apparent that we need more granular and microlevel studies to generate useful insights.” We respond to this call by examining the impact of a novel treatment-planning framework on patient outcome and treatment cost. To ensure the relevance to the clinical setting of radiotherapy planning, we draw upon the existing work<sup>fl</sup>ow and incorporate both patient characteristics and clinical information along the treatment trajectory. By doing so, we are able to derive useful insights about the potential bene-<sup>fi</sup>ts of the proposed framework in clinical practice.

Finally, although clinical trials remain the gold standard for treatment decisions, they have many limitations when used to compare the performance of status quo plans and alternative plans on individual patients (Goldberger and Buxton 2013). For example, in the context of radiotherapy planning, due to prohibitive cost and long follow-up time, clinical trials have been limited to comparison of a few conventional radiotherapy plans. In the current research, we use simulations to evaluate our proposed treatment-planning framework. Our simulations allow for direct comparisons of different treatment options; they also suggest promising treatment plans that have not been used or tested in prior trials.

The rest of this paper is organized as follows. Section 2 reviews the related literature and provides background information about the clinical context of our research. Section 3 describes our proposed framework. Section 4 provides detailed evaluations of the framework. Finally, Section 5 discusses the contributions and implications of our research and outlines the directions for future work.

## 2. Research Background

In this section, we <sup>fi</sup>rst review two streams of literature that are closely related to our current work. Figure 1 provides an overview of the theoretical background of our research. We then describe the clinical problem along with the current solutions and discuss how our proposed framework differs from these solutions.

## 2.1. Healthcare Predictive Analytics

Predictive analytics comprises models, tools, and systems that can leverage data from different sources to make predictions for future events or outcomes (Shmueli and Koppius 2011). Over the past two decades, predictive analytics has shown promising results in various healthcare settings. Some of the wellknown applications include identifying high-risk patients for complications or adverse events (Tabak et al. 2014), emergency department triage (Sagha<sup>fi</sup>an et al. 2014), clinical trial design (Bertsimas et al. 2016), and epidemic surveillance (Ginsberg et al. 2009).

Early works around healthcare predictive analytics are primarily concerned with population-level outcomes, such as clinically relevant strati<sup>fi</sup>cation of patients and ef<sup>fi</sup>cient allocation of scarce care resources (Bates et al. 2014). However, with the increasing availability and accessibility of patient data at a more granular level, there has been a growing interest in designing and evaluating patient-level analytics (Bardhan et al. 2015). For example, using a large clinical data set, where each patient is characterized by almost 4,000 features, ranging from laboratory tests to detailed doctor notes, Caruana et al. (2015) applied machine learning techniques to predict which patients were likely to be readmitted to the hospital within 30 days after being discharged. In a similar vein,

Figure 1. Overview of the Theoretical Background  
![](/api/attachments/UTFSYS2Y/fulltext/images/5e0f3709a862dd5b0e7a9eb133f7d9fa78396170a7412814e7d7c08e3f39c420.jpg)

Bardhan et al. (2015) developed a predictive analytics model to predict the propensity, frequency, and timing of readmissions of patients diagnosed with congestive heart failure. To address comorbidities among patients with chronic diseases, Lin et al. (2017) proposed a Bayesian multitask learning framework that allows for risk pro<sup>fi</sup>ling of multiple events simultaneously.

From the methodological perspective, existing literature that examines the potential of predictive analytics in healthcare can be broadly cast into two categories. The <sup>fi</sup>rst category of works relies on a priori parametric assumptions, such as a speci<sup>fi</sup>cation of the relationship between variables for the underlying prediction model (i.e., model-based), whereas the second category of work is primarily data-driven and requires fewer assumptions (i.e., model-free). Because of their <sup>fl</sup>exibility in capturing intrinsic data characteristics, model-free techniques, especially deep learning methods, have recently seen wide applications in medical image analysis (De Fauw et al. 2018), computational genomics (Chang et al. 2018), and disease prediction (Lee et al. 2018).

However, the <sup>fl</sup>exibility in capturing complex relationships in the data without making restricting assumptions comes at a cost of interpretability and transparency (Shmueli and Koppius 2011), which may result in skepticism about the predicted outcome or aversion to the recommendations generated from the predictive models. Further, the model-free approach generally requires a large amount of data to build the predictive model. Unfortunately, in many clinical contexts, patient data are limited in volume, and the lack of relevant data can undermine the ef<sup>fi</sup>cacy of the model-free tools. Given these considerations, in this research, we chose to take the model-based approach and draw upon relevant biomedical and clinical knowledge bases in developing our predictive model.

It is worth noting that most of the current research on patient-level analytics has focused on improving diagnostic decisions or predicting adverse events so that timely intervention can be taken (Bardhan et al. 2015, Helm et al. 2015, Lin et al. 2017, Kazemian et al. 2019, Son et al. 2020). Our paper differs from these studies in that we aim to develop predictive analytics models to facilitate physicians’ treatment decisions. To be useful, these models should take into account the trajectory of a patient’s disease and make accurate predictions of patients’ treatment responses. The most closely related paper to ours is Meyer et al. (2014), where the authors developed a novel approach based on machine learning and control theory to guide treatment decisions in diabetes management. The main difference is that Meyer et al. (2014) adopted an existing patient model to predict treatment failures and improve treatment strategies over time, whereas, in our case, we focus on the optimization of individual patients’ treatment (i.e., radiotherapy) plans by incorporating patient and clinical information revealed in the treatment trajectory.

## 2.2. Personalized Medicine

Our research is also closely related to the growing literature on personalized medicine—that is, health planning, treatment strategies, and drugs customized to the individual patient, rather than broader population cohorts (Hamburg and Collins 2010). Incorporating the concept of personalized medicine helps guide treatment-planning decisions by stratifying patients into unique subgroups that could receive targeted therapies to which they are more likely to respond, and thereby improving the survival rates and reducing the side effects. It also has the potential to lower the overall cost of healthcare dramatically (Aspinall and Hamermesh 2007). Although physicians have long recognized the heterogeneity in patients’ responses to treatment and sought to make treatment decisions that are as relevant to individual patients as possible, because of the lack of understanding about treatment effects, physicians often have little guidance about which patients are most likely to bene<sup>fi</sup>t from a given treatment.

The advances in genomic technologies have enabled clinical researchers to identify genetic variability in patients’ responses to different treatments and tailor treatment plans to patients’ individual needs (Burke and Psaty 2007). However, currently, genetics-driven personalization is limited to a few diseases. To move forward in personalized medicine, it requires both well-designed infrastructure—for example, healthcare information exchanges (HIEs)—and analytics tools to aggregate and integrate clinical data, identify patient similarities and connections, and provide personalized disease risk pro<sup>fi</sup>les for each individual patient (Fichman et al. 2011). On the infrastructure side, Yaraghi et al. (2014) found that network externalities are crucial in realizing the potential of HIE platforms in integrating patient information from different sources and facilitating decision making. Demirezen et al. (2016) took one step further and examined speci<sup>fi</sup>c strategies to increase the participation and sustainability of HIE.

On the analytics side, researchers have made extensive progress in developing new models that allow individual-speci<sup>fi</sup>c estimates from clinical trial data (Xu et al. 2016). Estimating individual-level effects allows physicians to customize the treatment to the individual patient. Unfortunately, in most real-world cases, it is not possible to run clinical trials on all possible treatment regimens, given their prohibitive cost. In those cases, physicians tend to extrapolate from the existing clinical trial results without solid evidence.

An alternative is to use computational simulations to estimate the outcome from any speci<sup>fi</sup>c treatment option (Meyer et al. 2014). When used effectively, simulations allow for a comparison of many different treatment options without the commitment of real patients. For example, Rosenberg et al. (2007) conducted a series of simulations to examine the relative bene<sup>fi</sup>ts of alternative treatment strategies for HIV infection. More recently, Negoescu et al. (2018) used simulation to determine optimal adaptive treatment policy for multiple sclerosis patients. Our current research shares the same spirit of these studies, in that we employ simulation to quantify the expected bene<sup>fi</sup>ts and risks associated with alternative treatment options. However, unlike Rosenberg et al. (2007) and Negoescu et al. (2018), where the simulations are based on existing disease models, we derive a realistic model to approximate the disease progression taking place in patients before using simulations to evaluate different treatment plans.

## 2.3. Radiotherapy Planning for Breast Cancer

Radiotherapy uses high-energy X-rays, protons, or other particles to destroy tumor cells. It has been widely used to treat breast cancer patients<sup>5</sup> at almost every stage after lumpectomy or mastectomy (Smith et al. 2018, Cardoso et al. 2019). Despite its effectiveness in reducing the risk of local recurrence (Bartelink et al. 2007) and improving the long-term survival (Early Breast Cancer Trialists’ Collaborative Group 2005), radiotherapy often involves incidental irradiation of the adjacent organs (e.g., heart and lungs), which increases the risk of cardiac mortality and mortality from lung cancer (Darby et al. 2013, Grantzau et al. 2014). As such, it is critical to balance the risk of local tumor recurrence and the risk of radiationinduced damage on normal cells of adjacent organs.

Optimizing radiotherapy plans for individual patients is highly challenging. For one thing, the microscopic tumor cells (hereafter, MTCs) around the primary tumor, which are the major cause of local tumor recurrence, cannot be detected directly by even the most advanced imaging technologies (Njeh and Dong 2013); they can only be identi<sup>fi</sup>ed in the histologic examination performed by pathologists. For another, it takes a long time and requires a large patient pool to compare alternative treatment plans through randomized controlled trials. Currently, most early stage breast cancer patients are treated with a standard radiotherapy plan, where a total dose of 50 grays (Gy)<sup>6</sup> is delivered throughout 25 sessions (i.e., a dose of 2 Gy delivered per session) over a <sup>fi</sup>ve-week period (Smith et al. 2018, Cardoso et al. 2019). Because such a standard plan does not account for the heterogeneity of tumor cells or patients’ risk pro<sup>fi</sup>les, it may lead to suboptimal patient outcomes in balancing the local tumor control and treatment-related morbidity.<sup>7</sup>

The recent development of intensity-modulated radiation therapy (IMRT) has led to a burgeoning interest in re<sup>fi</sup>ning radiotherapy plans. For example, Bortfeld et al. (2008) developed a robust framework that accounts for uncertainties resulting from breathing motions in IMRT. More recently, Ungun et al. (2019) proposed a suite of ef<sup>fi</sup>cient methods to facilitate the choice of optimal set of beams used in the treatment to maximize tumor coverage, while minimizing collateral damage on normal cells. Despite these progresses, the current literature on radiotherapy planning has, to the best of our knowledge, restricted attention to the optimization of delivery of prescribed doses. There is limited understanding about how to determine the optimal radiation dose for an individual patient in the <sup>fi</sup>rst place. Our work <sup>fi</sup>lls this gap by leveraging predictive analytics to prescribe optimal radiation doses that account for patient and disease heterogeneity. Table 1 summarizes the major studies on the optimization of radiation therapy that have been published in INFORMS journals and describes the differences between these studies and our current research.

At the outset, our personalized treatment-planning framework shares the same spirit of the dose-painting concept (Jaffray 2012), which aims to achieve a better trade-off in reducing the risk of local tumor recurrence and radiation-induced side effects by adapting the doses to patient heterogeneity—that is, the doses applied to different areas around the primary tumor are optimized based on the radiobiological features of the tumor cells and the clinical features of the patient. The dose-painting concept has already been implemented in the treatment of other types of cancer (e.g., lung cancer and prostate cancer), thanks to the continuous improvement in imaging technologies. However, in the case of breast cancer, as mentioned above, the residual MTCs around the primary tumor cannot be detected directly by the existing imaging tools. Our proposed framework overcomes this obstacle by characterizing the MTC distribution based on patient and clinical information revealed in the treatment trajectory.

## 3. The Proposed Framework

As mentioned earlier, the goal of radiotherapy planning is to eradicate the residual tumor cells while reducing the risk of radiation-induced damage to normal tissues. However, given the complex biological and physical processes involved in the radiotherapy, physicians cannot fully account for individual patients’ clinical pro<sup>fi</sup>les while making the treatmentplanning decisions. There is a strong need for decision support in balancing the risk of local tumor recurrence and normal tissue toxicity in radiotherapy planning.

Our research draws upon the information systems design science paradigm (Hevner et al. 2004, Gregor and Hevner 2013). The design science paradigm provides concrete prescriptions for understanding and addressing problems in information systems design and implementation (Hevner et al. 2004). In the healthcare domain, the design science paradigm has guided the development of innovative IT artifacts, including frameworks, models, methods, and instantiations, to facilitate clinical decision making (Hevner et al. 2004, Gregor and Hevner 2013). For example, Meyer et al. (2014) developed a machine learning based iterative approach that improves treatment decisions in diabetes management. Lin et al. (2017) proposed a Bayesian multitask learning approach that can facilitate the identi<sup>fi</sup>cation of patient risks of different adverse events and timely interventions. More recently, Son et al. (2020) developed an analytics framework that detects abnormal inhaler usage patterns using data from a smart asthma management system. Our work shares the same spirit of these studies. We aim to improve decision making in radiotherapy planning through the design of a novel IT artifact.

Table 1. Summary of Prior Research on Optimization of Radiation Therapy

<table><tr><td>Paper</td><td>Main focus</td><td>Differences from our paper</td></tr><tr><td>Romeijn et al. (2006)</td><td>Optimal orientation of beams during treatment delivery</td><td>Romeijn et al. (2006) imposed an upper bound (maximum dose) and a lower bound (minimum dose) and formulated the optimal beam setting problem in the dose delivery procedure as a linear programming problem; no radiobiological process is incorporated in the model.</td></tr><tr><td>Bortfeld et al. (2008)</td><td>Optimization of delivery while accounting for motion uncertainties</td><td>Bortfeld et al. (2008) proposed a model to account for motion uncertainty using probability density functions that describe breathing motion during treatment delivery; the prescribed doses are used as input in the formulation of the robust optimization problem; no radiobiological process is incorporated in the model.</td></tr><tr><td>Bortfeld et al. (2015)</td><td>Optimal schedule of treatment delivery</td><td>Bortfeld et al. (2015) formulated the optimal scheduling of treatment delivery as a dynamic programming problem using a TCP model; the key parameters that characterize the tumor growth and radiation effects (tumor kill), as well as the total dose, are set to constant based on prior literature in the simulation experiments.</td></tr><tr><td>Ungun et al. (2019)</td><td>Optimal selection of radiation beams in the treatment delivery</td><td>Ungun et al. (2019) proposed a suite of cluster and bound methods to optimize the sets of beams used in delivering the prescribed dose; no radiobiological process is incorporated in the model.</td></tr></table>

When there are insuf<sup>fi</sup>cient guidelines for the creation of new IT artifacts, the design science paradigm suggests that kernel theories can facilitate the development process (Gregor and Hevner 2013, Abbasi et al. 2019). In our case, given the lack of guidelines for the design of effective decision support systems for personalized radiotherapy planning, we <sup>fi</sup>rst draw upon the clinical oncology literature to model the intrinsic relationship between radiation dose and tumor progression while accounting for patient-speci<sup>fi</sup>c characteristics. The characterization of the complex interplay of different factors allows us to predict patient outcome of any potential treatment plan. We then take a decision-theoretic approach to optimize the radiation doses for individual patients.

Figure 2 provides the overview of our personalized treatment-planning framework. The entire planning process takes three steps and requires close collaboration of a team of medical specialists: (1) incorporate patient-speci<sup>fi</sup>c information—that is, presurgical MTC volume, removed MTC volume, and MTC density— into an MTC model to determine the postsurgical MTC quantity; (2) characterize the interplay between treatment dose and tumor characteristics—postsurgical MTC quantity, clonogenic cell fraction,<sup>8</sup> and radiosensitivity of tumor cells $( \mathrm { i . e . , }$ the relative susceptibility of tumor cells to radiation)—and predict tumor progression using a tumor control probability (hereafter, TCP) model; and (3) derive optimal doses based on clinical targets speci<sup>fi</sup>ed by radiation oncologists and recommend treatment plans accordingly.

## 3.1. The Predictive Model

The most commonly used measure of radiotherapy outcome is TCP (Zaider and Hanin 2011). It is de<sup>fi</sup>ned as the probability that no clonogenic cells (i.e., the MTCs that contribute to the risk of local recurrence of tumor) are left alive at the end of the treatment (Webb and Nahum 1993). There has been extensive effort in building models to estimate TCP based on the survival of clonogenic cells. The general idea underlying these models is as follows. For a given radiation dose D, the number of surviving clonogenic cells $N _ { s }$ from the starting number $N _ { 0 }$ after the radiotherapy is given by:

$$
N _ {s} = N _ {0} \cdot \exp (- \alpha D),\tag{1}
$$

where α denotes the radiosensitivity of tumor cells. Tumor cells with high radiosensitivity can be completely destroyed by radiotherapy, whereas those with low radiosensitivity might survive. Following the de<sup>fi</sup>nition that no clonogenic cells survive after the treatment, TCP can be formulated as

$$
T C P (D, N _ {0}) = \exp (- N _ {0} \cdot \exp (- \alpha D)).\tag{2}
$$

Mathematically, the TCP formulation in Equation (2) is straightforward: (i) For a given number of clonogenic cells, a higher radiation would yield better tumor control; and (ii) a large number of clonogenic cells requires a high dose to achieve good tumor control. Depending on the underlying assumptions about the MTC distribution and dose distribution, clinical researchers have developed different TCP models (O’Rourke et al. 2009). In the current research, we follow prior works by Chen et al. (2014) and Shusharina et al. (2018) and model the residual MTCs’ volume, density, and radiosensitivity as random variables to account for both intrapatient and interpatient heterogeneity. The resulting model is speci-<sup>fi</sup>ed as follows:

$$
\begin{array}{c} T C P (V, \rho , c, \alpha , D) = \int_ {V} \int_ {\rho} \int_ {\alpha} f _ {V} f _ {\rho} f _ {\alpha} \exp [ - c \cdot V \cdot \rho \\ \cdot \exp (- \alpha D) ] d V d \rho d \alpha , \end{array}\tag{3}
$$

where $V , \rho , \alpha , c ,$ and D denote the residual MTCs’ volume, density, radiosensitivity, the clonogenic cell fraction, and the prescribed radiation dose, respectively. $f _ { V } , f _ { \rho } ,$ and $f _ { \alpha }$ are the corresponding probability density functions. For any given patient, the predictive model described in Equation (3) takes the patient-speci<sup>fi</sup>c MTC information and the prescribed treatment dose as inputs and generates the expected TCP.

Figure 2. Personalized Treatment-Planning Framework  
![](/api/attachments/UTFSYS2Y/fulltext/images/5ec498ce43f8a541847c92221b0d035979fc694e5fea7a5f631bc3278b7ce747.jpg)

The main challenge in applying the above TCP model lies in the characterization of the patientspeci<sup>fi</sup>c MTCs. Because MTCs cannot be detected directly, we use patient and clinical information revealed in the treatment trajectory (please refer to Online Appendix EC.1. for details about the information <sup>fl</sup>ow during the patient journey) to model their distribution. Drawing upon <sup>fi</sup>ndings from prior clinical oncology research, we model the presurgery (initial) MTC volume with a zero-in<sup>fl</sup>ated Poisson distribution and the MTC density with a Gaussian distribution. Because a small margin of normal breast tissue around the primary tumor is removed during the surgery, we also need to account for the potential deformation of the breast tissue when modeling the remaining MTCs after surgery. The details of MTC modeling can be found in Online Appendix EC.2.

Before moving to the estimation and validation of our predictive model, we would like to brie<sup>fl</sup>y discuss our key modeling choices and their implications on the performance of our predictive model. To start with, we note that there has been a burgeoning interest in adopting machine learning and data mining techniques to identify factors contributing to TCP. Despite the potential improvement in prediction power, such a data-driven approach typically requires a large sample of high-quality training data, which is rarely encountered in radiotherapy planning. In the current research, we have chosen to adopt a model-based approach and draw upon the radiobiological processes that characterize the dynamics of tumor cells. Although our model speci<sup>fi</sup>ed in Equation (3) is inevitably a simpli<sup>fi</sup>cation of the complex interplay of different factors related to tumor control, the predictions from the model are suf<sup>fi</sup>ciently interpretable, which is important in clinical settings. Further, we assume that all the patient-speci<sup>fi</sup>c biological and clinical information is well-integrated and readily accessible for treatmentplanning purposes. In reality, this assumption may not hold. Nevertheless, we believe that the increasing adoption and use of electronic health records, as well as clinical technologies, such as digital pathology, would eventually lead to a seamless integration of patient data along the treatment trajectory.

3.1.1. Model Estimation. In order to estimate the key parameters in our predictive model, we use a pathology dataset from a breast cancer treatment center and two clinical trial datasets—the European Organization for Research and Treatment of Cancer (EORTC) trial

22881-10882 (Vrieling et al. 2017) and the 2011 Report of Early Breast Cancer Trialists’ Collaborative Group (EBCTCG) (Darby et al. 2011). The pathology dataset consists of more than 1,000 microscopic slides that were thoroughly reviewed by breast pathologists. It is used to estimate the parameters in the MTC model. The EORTC dataset consists of 1,616 patients who were randomly assigned to radiotherapy with a total dose of either 50 Gy (801 patients) or 66 Gy (815 patients), and the EBCTCG dataset consists of 10,801 patients from 17 trials where patients were randomly assigned to receive a radiotherapy with a total dose of 50 Gy or no radiotherapy (0 Gy). Although both clinical trial datasets have recorded patient outcomes (TCP), only the EORTC dataset includes patients’ clinical information, such as tumor size, tumor grade, and surgical margins.

In order to estimate the clonogenic cell fraction (c) and radiosensitivity (α) in the TCP model in Equation (3), we use Bayesian inference via Markov chain Monte Carlo simulation (Rasmussen and Ghahramani 2003). Speci<sup>fi</sup>cally, we assume a normal prior distribution for c—that is,

$$
c \sim \mathcal {N} (\mu_ {0} ^ {c}, \sigma_ {0} ^ {c}).\tag{4}
$$

As mentioned earlier, we try to account for the heterogeneity of radiosensitivity across patients. Therefore, we assume that for each patient i, the radiosensitivity $\alpha _ { i }$ follows a normal distribution with parameters θ and $\zeta ,$

$$
\alpha_ {i} \sim \mathcal {N} (\theta , \zeta),\tag{5}
$$

where both θ and $\zeta$ are assumed to have normal prior distributions:

$$
\theta \sim \mathcal {N} (\mu_ {0} ^ {\theta}, \sigma_ {0} ^ {\theta}),\tag{6}
$$

$$
\zeta \sim \mathcal {N} (\mu_ {0} ^ {\zeta}, \sigma_ {0} ^ {\zeta}).\tag{7}
$$

We simulate 10,000 synthetic patients, whose age, tumor size, tumor grade, and surgical margins are drawn independently and randomly from the empirical distributions of patients in the EORTC dataset. For each patient, the postsurgery MTC quantity and distribution is generated from our MTC model, and the treatment dose is randomly chosen from the three observed plans in the two clinical trial datasets (i.e., 0 Gy, 50 Gy, and 66 Gy). Using the simulated patient data, we estimate the clonogenic cell fraction and radiosensitivity parameters<sup>9</sup> with the following loglikelihood function:

$$
L (c, \alpha_ {i}) = - \frac {1}{2} N \mathrm{log} (2 \pi \sigma_ {D _ {i}} ^ {2}) - \sum_ {i = 1} ^ {N} \frac {[ T C P (c , \alpha_ {i} , D _ {i}) - \mu_ {D _ {i}} ] ^ {2}}{2 \sigma_ {D _ {i}} ^ {2}}.\tag{8}
$$

In Equation (8), N denotes the size of the synthetic patient pool $( \mathrm { i . e . , ~ } N = 1 0 , 0 0 0 ) ; D _ { i }$ denotes the treatment dose assigned to patient $i ,$ and $\mu _ { D _ { i } }$ and $\sigma _ { D _ { i } }$ denote the mean and standard deviation, respectively, of the TCP given the treatment dose $D _ { i } .$ Note that $\mu _ { D _ { i } }$ and $\sigma _ { D _ { i } }$ can be directly estimated from the clinical trial data. To mitigate the potential bias associated with the choice of priors, we repeat the simulation 100 times (i.e., we obtain 100 cohorts of synthetic patients). Each time, we use Heidelberger and Welch’s (1983) convergence diagnostic test to examine the convergence of the sequence of the estimated values. All of our estimated values passed the test.

3.1.2. Model Validation. We employ two different methods to evaluate the performance of our predictive model. To start with, we perform a cross-validation using the clinical trial data. Cross-validation is a popular technique to evaluate predictive models by partitioning the original sample of data into a training set and a test set (Bishop 2006). In our case, we pool the patients from the two clinical trials and randomly split the pooled sample by half as the training set, which is used to estimate the key parameters in the TCP model, and the test set, which is used to evaluate the prediction accuracy.<sup>10</sup> We repeat the process 100 times. The root mean square error of TCP on the test set is 1.3%, suggesting a good prediction accuracy.

Next, we create a synthetic dataset by drawing upon a more recent trial (Polgar et al.´ 2013), where patients were treated with partial-breast irradiation instead of whole-breast irradiation, as in the data sets. For patients undergoing partial-breast irradiation, radiation is only delivered to the breast tissue immediately adjacent to the primary tumor, and thereby it reduces the potential damage to the adjacent organs. Given the patients’ age distribution, tumor size distribution, tumor grade distribution, and surgical margin distribution documented in Polgar et al. (´ 2013), we simulate 10,000 synthetic patients, whose residual MTC quantity and distribution can be estimated from the MTC model. We then plug the estimates of the clonogenic cell fraction parameter and the radiosensitivity parameters as well as the dose information into the TCP model to predict the TCP of the synthetic patients. Again, we repeat the simulation 100 times and obtain a 95% con<sup>fi</sup>dence interval of 93:7%, 94:4% , which is very close to the TCP (94.1%) reported in Polgar et al. (´ 2013).

Finally, we conduct a sensitivity analysis to examine the potential extrapolation issue of our model. Speci<sup>fi</sup>cally, we train two additional models on subsamples of the clinical trial data—one consists of patients who received treatment doses of 0 Gy and 50 Gy, and the other of patients who received treatment doses of 0 Gy and 66 Gy—and compare the predictions from these two models and the original model trained on the full sample. Figure 3 shows the predicted TCP for different treatment doses under the three models. We can see that the predictions from the two models trained on subsamples and the model trained on the full sample are quite consistent. Such observation indicates that our predictive model captures the data-generation process well, and thereby alleviates our concern about extrapolation.

## 3.2. The Optimization Model

By incorporating individual patients’ clinical pro<sup>fi</sup>les into the prediction of treatment outcomes, our predictive model offers a promising way to tailor treatment plans to individual patients based on what will work best for them. Below, we will discuss how to leverage our predictive model to optimize treatment plans under different clinical constraints.

Figure 3. Sensitivity Analysis of the Predictive Model  
![](/api/attachments/UTFSYS2Y/fulltext/images/6f689f76e7d4b4c845d073b11179509ee7572d4ce79906ec8f0be2309767f2ee.jpg)

To start with, prior clinical trials have shown that a boost radiation dose $( \mathrm { e . g . }$ , an additional 16 Gy on top of the standard dose of 50 Gy) could lead to improved local tumor control (Bartelink et al. 2007). However, it remains unclear whether a further increase of the radiation dose could improve the overall patient outcome. In light of this, we consider two scenarios in optimizing patients’ treatment plans: (1) no constraint on the radiation doses delivered in the radiotherapy; and (2) the total prescribed dose is capped by a maximum of 66 Gy, which is the maximum dose used in prior clinical trials.

We also note that recent advances in diagnostics technologies enable physicians to perform effective risk strati<sup>fi</sup>cation when determining treatment options for individual patients (Tolmachev et al. 2010). Although such strati<sup>fi</sup>cation cannot fully capture patient heterogeneity, if patients in the same group share some of the most important clinical features (e.g., tumor size, tumor stage), the average outcome predicted by our TCP model would still be relevant and useful in guiding the treatment decisions for individual patients within the group. Based on this consideration, we <sup>fi</sup>rst discuss how to optimize treatment plans for patient groups. This can be considered as an intermediate step between the current clinical practice (i.e., all patients receive the same standard uniform radiation dose) and our ultimate goal of personalizing treatment plans.

3.2.1. Optimizing Treatment Plans for Patient Groups. Consider a patient group of size N. For computational tractability, we assume that the MTCs are distributed symmetrically around the primary tumor. This allows us to simplify the three-dimensional TCP model to a one-dimensional model—that is, for any patient i,

$$
T C P ^ {(i)} := \Pi_ {d} T C P _ {d} ^ {(i)},\tag{9}
$$

where $d$ denotes the distance of a tumor tissue voxel to the mass center of the primary tumor (i.e., 1 mm, 2 mm, … , 50 mm). The average TCP of the patient group is given by

$$
T C P _ {N} := \Sigma_ {i} (\Pi_ {d} T C P _ {d} ^ {(i)}) / N.\tag{10}
$$

Recall that the goal of radiotherapy planning is to maximize the TCP while minimizing the radiation-induced adverse effects—that is, the damage to normal cells. A key indicator for these effects is the average dose delivered to the breast,<sup>11</sup> which is given by

$$
A v g D o s e := \Sigma_ {d} (V _ {d} ^ {b r e a s t} \cdot D (d)) / \Sigma_ {d} V _ {d} ^ {b r e a s t}.\tag{11}
$$

Here, $V _ { d } ^ { b r e a s t }$ denotes the volume of the breast tissue at distance $d ,$ and $D ( d )$ the planned radiation dose at distance d. For the no-constraint scenario, the optimization problem can be formulated as

$$
\begin{array}{c} \underset {D (d)} {\min} A v g D o s e \\ \text { subject   to } T C P _ {N} = T C P _ {t a r g e t}, \end{array}\tag{12}
$$

where $T C P _ { t a r g e t }$ denotes the prede<sup>fi</sup>ned TCP target. Similarly, for the constraint scenario $( \mathrm { i . e . , }$ the maximum dose is capped by 66 Gy), the optimization problem can be formulated as:

$$
\begin{array}{c} \underset {D (d)} {\min} A v g D o s e \\ \text { subject   to } T C P _ {N} = T C P _ {t a r g e t} \\ \forall d, D (d) \leq 6 6. \end{array}\tag{13}
$$

To solve the optimization problems de<sup>fi</sup>ned in Equation (12) and Equation (13), we apply the Lagrange multiplier method. Speci<sup>fi</sup>cally, for the no-constraint scenario, after plugging Equation (9) and Equation (11) into Equation (12), we obtain the following Lagrange function:

$$
\begin{array}{l} \mathcal {L} ^ {(N)} (D) := \sum_ {d = 1} ^ {5 0} (V _ {d} ^ {\text { breast }} \cdot D (d)) / \sum_ {d = 1} ^ {5 0} V _ {d} ^ {\text { breast }} \\ \qquad + \lambda \cdot (T C P _ {\text { target }} - \prod_ {d = 1} ^ {5 0} \exp (- c \cdot \rho \cdot V _ {d} \\ \qquad \cdot \exp (- D (d) \cdot \alpha))), \end{array}\tag{14}
$$

where λ is the Lagrange multiplier, and $V _ { d }$ denotes the MTC volume at distance d.

For the constraint scenario, we impose a high penalty when the radiation dose exceeds 66 Gy (Luenberger and Ye 2016), and the resulting Lagrange function is given by:

$$
\begin{array}{l} \mathcal {L} ^ {(M)} (D) := \sum_ {d = 1} ^ {5 0} (V _ {d} ^ {b r e a s t} \cdot D (d)) / \sum_ {d = 1} ^ {5 0} V _ {d} ^ {b r e a s t} \\ \qquad + \lambda \cdot (T C P _ {t a r g e t} - \prod_ {d = 1} ^ {5 0} \exp (- c \cdot \rho \cdot V _ {d} \\ \qquad \cdot \exp (- D (d) \cdot \alpha))) + p \cdot H ^ {6 6} (D). \end{array}\tag{15}
$$

In Equation (15), p denotes the penalty, and $H ^ { 6 6 } ( D )$ is the Heaviside step function (or unit step function), which takes the value of zero for $D \leq 6 6$ and one for $D > 6 6$

Given the strong nonlinearity of the TCP function (see Equation (3)) and the stochastic nature of our optimization problems, we use the adaptive moment estimation method (Adam) proposed by Kingma and Ba (2014) to <sup>fi</sup>nd the optimal dose distribution. Adam is an ef<sup>fi</sup>cient algorithm for stochastic optimization. It only requires the calculation of <sup>fi</sup>rst-order gradients and has little memory requirement.<sup>12</sup> It works particularly well in nonstationary settings with noisy and/or sparse gradients, which are exactly the challenges we encounter when solving the optimization problems in Equations (12) and (13). We provide the detailed derivation of gradients of Equation (14) and Equation (15) in Online Appendix EC.3.

Algorithm 1 describes how to apply Adam to optimize treatment plans for patient groups.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1 (Dose Optimization)
Input: Patient Data A; Subsample Size b = 5000; Learning Rate  $\kappa_{0} = 0.001$ ; Exponential Decay Rates  $\kappa_{1} = 0.9$ ,  $\kappa_{2} = 0.999$ ; Precision Rate  $\kappa_{3} = 10^{-8}$ 

Output: Dose Distribution D

1 Initialize parameters for D using standard Normal distribution N(0,1)

2  $\iota_{0} \leftarrow 0$  (Initialize  $1^{st}$  moment vector)

3  $v_{0} \leftarrow 0$  (Initialize  $2^{st}$  moment vector)

4 t  $\leftarrow 0$  (Initialize timestep)

5 tag  $\leftarrow$  False (Initialize convergence tag)

6 while tag == False do

7 Randomly select a subsample B of size b from A

8 for each subsample B ⊂ A do

9 t  $\leftarrow t + 1$  (Update timestep)

10 g  $\leftarrow \nabla_{D} L(D; B)$  (Compute gradient vector on the subset B)

11  $\iota_{t} \leftarrow \kappa_{1} \cdot \iota_{t-1} + (1 - \kappa_{1}) \cdot g$  (Update biased first moment estimate)

12  $v_{t} \leftarrow \kappa_{2} \cdot v_{t-1} + (1 - \kappa_{2}) \cdot g^{2}$  (Update biased second moment estimate)

13  $\hat{\iota}_{t} \leftarrow \iota_{t-1}/(1 - \kappa_{1}^{t})$  (Compute bias-corrected first moment estimate)

14  $\hat{v}_{t} \leftarrow v_{t-1}/(1 - \kappa_{2}^{t})$  (Compute bias-corrected second moment estimate)

15  $D_{t} \leftarrow D_{t-1} - \kappa_{0} \cdot \hat{\iota}_{t}/(\sqrt{\hat{v}_{t}} + \kappa_{3})$  (Update parameters)

16 end for

17 if  $\mathcal{L}(D_{t}) - \mathcal{L}(D_{t-1}) &lt; \kappa_{3}$  then

18 tag  $\leftarrow True$ 

19 end if

20 end while
</div>

The algorithm requires six inputs: patient data $\scriptstyle A ,$ consisting of 10,000 synthetic patients; subsample size $b ;$ learning rate $\kappa _ { 0 } ;$ two exponential decay rates for the moment estimates denoted by $\kappa _ { 1 }$ and $\kappa _ { 2 } ,$ respectively; and precision rate $\kappa _ { 3 } .$ For learning rate, exponential decay rates, and precision rate, we choose to use the values recommended in Kingma and Ba (2014). For each synthetic patient, the key parameters in the TCP model are randomly drawn from the estimated distributions following the simulation procedure described in Section 3.1.1. For the constrained scenario, following the guidelines from Luenberger and Ye (2016), we set the penalty coef<sup>fi</sup>cient to 1,000,000 when the radiation dose exceeds 66 Gy. Given these inputs, Algorithm 1 minimizes the Lagrange functions described earlier by updating the dose distribution D.

3.2.2. Optimizing Treatment Plans for Individual Patients. There is a clear trade-off between an individualized plan and a group-based plan. Speci<sup>fi</sup>cally, an individualized plan is costly (Geruso et al. 2018) and time-consuming, given the current clinical tools: It requires a <sup>fi</sup>ne-grained histologic examination that can yield the clinical features. As such, only a few treatment centers (typically colocated with cancer-research institutions) have the capacity to perform such examinations. A group-based plan, on the other hand, is much more ef<sup>fi</sup>cient and bears much lower cost, as it leverages the current clinical practice. Despite the trade-off, it is our premise that the problem of customizing treatment plans for individual patients is far too important to remain unanswered because of the technological or cost constraints; we believe that the continuous development of biomedical tools $( \mathrm { e . g . } ,$ advanced digital pathology tools) will make personalized treatment planning not only feasible, but also affordable in the near future.

When individual patients’ medical history and clinical features throughout the entire treatment trajectory are available, we can customize the treatment plans by replacing the average TCP by the individual TCP in Equation (12) and Equation (13). As the optimized individual treatment plans share the same spirit of the dose-painting concept proposed in Jaffray (2012), hereafter, we refer to these plans as dose-painting plans to differentiate them from the group-based optimal plans described in Section 3.2.1.

## 4. Evaluation of the Framework

To demonstrate the ef<sup>fi</sup>cacy of our proposed framework, we follow the guidelines from Hevner et al. (2004) and perform a series of evaluations using different benchmarks.

## 4.1. Baseline Evaluation

As the baseline evaluation, we <sup>fi</sup>rst compare the standard uniform plans and the optimal plans generated from our framework with respect to two TCP targets, 90% and 80%. For optimal plans, we need to account for two types of errors that are common in the treatment delivery process (van Herk et al. 2000): systematic errors and random errors. The systematic error (denoted by $e _ { s } )$ refers to the systematic deviation in the same direction of similar magnitude during each session of the treatment. Such error may arise from incorrect calibration of the radiation machine or incorrect input of patient data. On the contrary, the random error (denoted by e ) is a deviation that varies, both in sign and magnitude, across different treatment sessions. Random errors may occur due to patient movement (e.g., breathing) during the treatment. Given these two types of errors, the treatment volume and the prescribed doses need to be adjusted to ensure the coverage of the MTCs during the treatment session. We include the detailed discussion of the adjustments in Online Appendix EC.3.

Table 2. Overview of Treatment Plans

<table><tr><td rowspan="2">Plan</td><td rowspan="2">TCP target (%)</td><td colspan="3">Treatment scenarios</td></tr><tr><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td></tr><tr><td>Standard</td><td>90</td><td>U90</td><td>U90</td><td>U90</td></tr><tr><td>uniform plan</td><td>80</td><td>U80</td><td>U80</td><td>U80</td></tr><tr><td>No-constraint</td><td>90</td><td>N90-S0R0</td><td>N90-S1R1</td><td>N90-S5R5</td></tr><tr><td>optimal plan</td><td>80</td><td>N80-S0R0</td><td>N80-S1R1</td><td>N80-S5R5</td></tr><tr><td>Constraint</td><td>90</td><td>M90-S0R0</td><td>M90-S1R1</td><td>M90-S5R5</td></tr><tr><td>optimal plan</td><td>80</td><td>M80-S0R0</td><td>M80-S1R1</td><td>M80-S5R5</td></tr></table>

Note. $e _ { r } ,$ random error; $e _ { s } ,$ systematic error; M, constraint optimal plan (maximum dose capped by 66 Gy); N, no-constraint optimal plan; U, standard uniform plan.

We consider three combinations of setup errors: (i) no setup errors, that is, $e _ { s } , e _ { r } = 0$ mm; (ii) small setup errors, that is, $, e _ { s } , e _ { r } = 1$ mm; and (iii) large setup errors, that is, $e _ { s } , e _ { r } = 5$ mm. Table 2 provides an overview of different types of treatment plans to be evaluated in the baseline evaluation. Note that standard uniform plans prescribe the same dose for the whole breast, so the setup errors will not affect the determination of the prescribed dose for a given TCP target.

4.1.1. Comparison of Treatment Outcomes on Patient Groups. For a group of 10,000 synthetic patients, Figure 4 shows the dose distributions under the standard uniform plans and group-based optimal plans for different TCP targets and setup errors. Here, the solid lines represent the dose distributions for the TCP target of 90% under no-constraint scenarios; the dotted lines represent the dose distributions for the TCP target of 90% TCP under the constraint scenarios;

Figure 4. Dose Distribution Under Different Treatment Plans for a Patient Group  
(a)  
![](/api/attachments/UTFSYS2Y/fulltext/images/51c061f41335862cbcd063f58c44a3eacecf9d6cb5af3ca404c3f03b24856914.jpg)

(b)  
![](/api/attachments/UTFSYS2Y/fulltext/images/afc81c11d0acdb71dda74a942d4f9c18a9fd0e7c5d080dfb5931020cd0709953.jpg)

(c)  
![](/api/attachments/UTFSYS2Y/fulltext/images/f6c6e8ae4a368829ebafa8357ba833ce36f1a582818cb4775105b4cfdb7c6080.jpg)

$$
(e _ {s}, e _ {r} = 5 \mathrm{mm})
$$

(d)  
![](/api/attachments/UTFSYS2Y/fulltext/images/218dcac2f8a949a5113ccd21beae0e5791feef15a6aeb4c0d68caf52b49028e1.jpg)  
Notes. (a) Optimal plans under S0R0 $( e _ { s } , e _ { r } = 0 \mathrm { m m } )$ . (b) Optimal plans under S1R1 $( e _ { s } , e _ { r } = 1$ mm). (c) Optimal plans under S5R5 $( e _ { s } , e _ { r } = 5 \mathrm { m m } ) .$ (d) Standard uniform plan.

Table 3. Comparison of Average Doses (Group Plans)

<table><tr><td rowspan="2">Plan</td><td rowspan="2">TCP target (%)</td><td colspan="3">Average dose (Gy)</td></tr><tr><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td></tr><tr><td rowspan="2">Standard uniform plan</td><td>90</td><td>54</td><td>54</td><td>54</td></tr><tr><td>80</td><td>34</td><td>34</td><td>34</td></tr><tr><td rowspan="2">No-constraint optimal plan</td><td>90</td><td>2.86</td><td>2.97</td><td>3.35</td></tr><tr><td>80</td><td>0.96</td><td>0.99</td><td>1.26</td></tr><tr><td rowspan="2">Constraint optimal plan (max dose: 66 Gy)</td><td>90</td><td>4.67</td><td>4.70</td><td>5.15</td></tr><tr><td>80</td><td>0.96</td><td>0.99</td><td>1.26</td></tr></table>

and the dashed lines correspond to the dose distributions for the TCP target of 80%, in which case the optimal plans derived from our algorithm did not reach the maximum dose cap $( \mathrm { i . e . , 6 6 G y } )$ , and, thereby, the two optimization scenarios are not differentiated.

According to Figure 4, under the no-constraint scenario with 0-mm setup error, the maximum doses required to achieve the TCP targets of 90% and 80% are approximately 80 and 45 Gy, respectively. When the setup errors increase to 5 mm, the maximum doses required to achieve the same TCP target increase to approximately 95 Gy for the TCP target of 90% and 50 Gy for the TCP target of 80%. Under the constraint scenario, the optimal dose plans have wider spread, and the optimal doses close to the primary tumor (within 10 mm) are capped by the maximum dose of 66 Gy for the TCP target of 90%. Overall, we can see that the dose distributions are shifted eccentrically toward the right side with increased setup errors.

Next, we compare the average doses under different treatment plans. The results are summarized in Table 3. To start with, we can see that the required average dose is signi<sup>fi</sup>cantly higher with higher TCP target and larger setup errors. Nevertheless, the average doses under both no-constraint and constraint optimal plans are signi<sup>fi</sup>cantly lower than those under the standard uniform plans. Speci<sup>fi</sup>cally, compared with the standard uniform plan, the average dose required to achieve the TCP target of 90% under the no-constraint (constraint) optimal plan decreases by approximately 94.7% (91.4%) when there is no setup error. Even in the presence of large setup errors (e.g., 5 mm), the average doses required for the TCP target of 90% under the constraint and no-constraint optimal plans are still 93.8% and 90.5% lower than the required average dose under the standard uniform plan, respectively.

Interestingly, we also <sup>fi</sup>nd that the average dose required to achieve a higher TCP target (e.g., 90%) is higher in the constraint scenario as compared with the no-constraint scenario. Combined with the observation from Figure 4 that optimal dose distributions under the constraint scenario have wider spread than those under the no-constraint scenario, such a <sup>fi</sup>nding indicates that insuf<sup>fi</sup>cient dose for the breast tissues with large quantity of MTCs (e.g., the tissues within a distance of less than 10 mm to the primary tumor) would require much higher doses in the rest part of the breast for the given TCP target, and thereby result in higher risk of normal tissue toxicity. Overall, the results from Table 3 reinforce the importance of dose adaptation and customization in treatment planning.

4.1.2. Comparison of Treatment Outcomes on Individual Patients. In light of the observed difference in tumor control (see Table 3) between the constraint and no-constraint scenarios, we chose to focus on the noconstraint scenario with the TCP target of 90% for the individual optimal plans. Figure 5 depicts the aggregated optimal dose distributions under the dosepainting plan. Note that each data point on the <sup>fi</sup>gure represents the average taken across the 10,000 synthetic patients. The solid curve corresponds to the aggregated optimal distribution when the systematic and random errors are set to 5 mm; the dotted curve and the dashed curve represent the distributions when the errors are set to 1 and 0 mm, respectively. Again, we can see that large setup errors would require higher doses, and the resulting optimal distributions also have wider spread.

We also compare the average doses required to achieve the TCP target of 90% under different plans. Table 4 summarizes the results. Overall, we can see that the dose-painting plans can substantially reduce the average dose used in the treatment. In particular, the average dose required to achieve a TCP target of 90% under the dose-painting plan is approximately 94.4% lower than the average dose required under the standard uniform plan when the setup errors are set to 5 mm. By lowering the exposure of normal tissues to radiation, the dose-painting plan can substantially reduce the side effects.

Figure 5. Optimal Dose Distributions (Averaged Across 10,000 Synthetic Patients)  
![](/api/attachments/UTFSYS2Y/fulltext/images/bf4a4f7a2f9537ef3a31497b3d20618bfd7feefeb3e18cec4f5f5ed568776140.jpg)

Table 4. Comparison of Average Doses with TCP Target 90% (Individual Plans)

<table><tr><td rowspan="2">Plan</td><td colspan="3">Average dose (Gy)</td></tr><tr><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td></tr><tr><td>Standard uniform plan</td><td>54</td><td>54</td><td>54</td></tr><tr><td>Dose-painting plan</td><td>1.2</td><td>1.5</td><td>3.0</td></tr></table>

Taken together, the results from Table 3 and Table 4 indicate that by incorporating patient-speci<sup>fi</sup>c information and characterizing the MTC distribution, we can achieve the same TCP target with signi<sup>fi</sup>cantly lower doses than standard uniform plans. Speci<sup>fi</sup>cally, if there are only a small amount of MTCs around the primary tumor, the excessive dose delivered under the standard uniform plan would increase the toxicity on normal cells without improving the local tumor control. In fact, if no MTCs are left after the surgery, there is no need for radiotherapy.

## 4.2. Additional Evaluation

To demonstrate the utility and quality (especially computational ef<sup>fi</sup>ciency) of our framework, we conduct additional simulation experiments to compare the performance of the optimization method used in our framework (i.e., Adam) with three widely used stochastic optimization methods, namely, Limited-memory Broyden–Fletcher–Goldfarb–Shanno algorithm with boundaries (hereafter, L-BFGS-B) (Nash 2014), Simulated Annealing (hereafter, SA) (van Laarhoven and Aarts 1987), and Genetic Algorithm (hereafter, GA) (Vose 1999). For each method, we generate 10,000 synthetic patients and follow the same procedures described in Sections 3.2.1 and 3.2.2 to calculate the optimal plans. All the simulations are run on a Windows 10 machine with Intel i7-8700 CPU (3.20 GHz processor) and 16 GB RAM.

For the TCP target of 90%, Table 5 and Table 6 summarize the experiment results for group-based plans and individual plans, respectively. Apart from the required dose, we also include the calculation time as a performance indicator for each optimization method.

We can see that Adam consistently outperforms the three benchmark methods, both in terms of patient outcome, which is measured by the average dose, and computational ef<sup>fi</sup>ciency. Speci<sup>fi</sup>cally, both SA and GA take signi<sup>fi</sup>cantly more time to converge and are more likely to get trapped in a local optimum. L-BFGS-B yields comparable patient outcome as Adam, but the latter is more ef<sup>fi</sup>cient.

## 4.3. Economic Benefits

As society is struggling to manage the rising cost of cancer care, care providers, especially oncologists, are under increasing pressure to deliver better outcomes in a cost-effective manner. In light of this, we further estimate the potential cost saving associated with the lower average dose under our personalized treatment plans.

Prior clinical research has demonstrated that patients who received a high dose in radiotherapy are at higher risks of lung cancer and heart diseases. Speci<sup>fi</sup>- cally, Grantzau et al. (2014) found that the risk of developing lung cancer increased linearly at a rate of 8.5% per Gy among patients who received the standard uniform treatment plan (with average dose of 50 Gy to the breast and 8.7 Gy to the lung). Similarly, Darby et al. (2013) reported that major coronary events increased linearly at a rate of 7.4% per Gy under the standard uniform treatment plan (with average dose of 50 Gy to the breast and 4.9 Gy to the whole heart). The estimated morbidity rates of lung cancer and heart diseases for these patients are 0.64% (Grantzau et al. 2014) and 3% (Højris et al. 1999), respectively.

To estimate the cost saving, we consider a TCP target of 90% and set both the systematic error and random error to 5 mm to be consistent with clinical practices. According to Table 4, the average radiation dose is reduced from 54 Gy to 3 Gy under the personalized plans. Thus, the average dose to a patient’s lung and heart can be reduced by 8.22 Gy $( = \bar { 8 } . 7 G y \times ( 5 4 \bar { G } y - 3 G y ) / 5 4 G y )$ and 4.63 Gy $( = 4 . 9 G y \times ( 5 4 G y - 3 G y ) / 5 4 G y ) ,$ , respectively. Following prior <sup>fi</sup>ndings from Grantzau et al. (2014) and Darby et al. (2013), this would lower the risk of developing lung cancer and heart diseases by 69.8% and 34.2%; that is, the morbidity rate of lung cancer and heart diseases can be reduced to $\begin{array} { r l } { 0 . 1 9 \% } & { { } \hat { ( = 0 . 6 4 \% \times ( 1 0 0 \% - 6 9 . 8 \% ) ) } } \end{array}$ and $2 . 0 \% ( = 3 \% \times ( 1 0 0 \% - 3 4 . 2 \% ) )$ , respectively.

Table 5. Comparison of Alternative Optimization Methods for Group Plans

<table><tr><td rowspan="2">Performance</td><td colspan="3">No-constraint</td><td colspan="3">Constraint</td></tr><tr><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td></tr><tr><td>Adam</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>2.86</td><td>2.97</td><td>3.35</td><td>4.67</td><td>4.70</td><td>5.15</td></tr><tr><td>Time (min)</td><td>1.81</td><td>3.36</td><td>3.55</td><td>1.47</td><td>2.84</td><td>3.26</td></tr><tr><td>L-BFGS-B</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>2.87</td><td>3.41</td><td>4.48</td><td>4.70</td><td>4.87</td><td>6.68</td></tr><tr><td>Time (min)</td><td>3.98</td><td>4.08</td><td>5.92</td><td>2.77</td><td>3.34</td><td>3.71</td></tr><tr><td>SA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>4.48</td><td>5.06</td><td>6.85</td><td>5.81</td><td>6.25</td><td>8.47</td></tr><tr><td>Time (min)</td><td>5.52</td><td>7.42</td><td>7.27</td><td>5.78</td><td>7.27</td><td>7.53</td></tr><tr><td>GA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>4.41</td><td>4.79</td><td>6.73</td><td>4.94</td><td>5.13</td><td>7.36</td></tr><tr><td>Time (min)</td><td>12.21</td><td>15.28</td><td>15.08</td><td>12.45</td><td>15.20</td><td>15.54</td></tr></table>

Table 6. Comparison of Alternative Optimization Methods for Dose-Painting Plans

<table><tr><td rowspan="2">Performance</td><td colspan="3">No-constraint</td><td colspan="3">Constraint</td></tr><tr><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td><td> $e_s,e_r=0$ </td><td> $e_s,e_r=1$ </td><td> $e_s,e_r=5$ </td></tr><tr><td>Adam</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>1.20</td><td>1.54</td><td>3.01</td><td>1.27</td><td>1.64</td><td>4.87</td></tr><tr><td>Time (min)</td><td>2.94</td><td>3.97</td><td>4.45</td><td>2.21</td><td>2.88</td><td>2.89</td></tr><tr><td>L-BFGS-B</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>2.80</td><td>3.08</td><td>3.42</td><td>3.57</td><td>3.93</td><td>4.92</td></tr><tr><td>Time (min)</td><td>6.04</td><td>6.85</td><td>8.73</td><td>22.12</td><td>21.42</td><td>23.28</td></tr><tr><td>SA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>10.79</td><td>11.21</td><td>13.26</td><td>10.82</td><td>10.96</td><td>13.57</td></tr><tr><td>Time (min)</td><td>34.72</td><td>36.17</td><td>36.46</td><td>32.72</td><td>36.65</td><td>42.30</td></tr><tr><td>GA</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Avg. dose (Gy)</td><td>8.43</td><td>8.76</td><td>10.69</td><td>8.87</td><td>9.00</td><td>10.25</td></tr><tr><td>Time (min)</td><td>71.84</td><td>76.94</td><td>85.29</td><td>72.22</td><td>61.23</td><td>98.88</td></tr></table>

According to Kakushadze et al. (2017) and Yu et al. (2013), the estimated average treatment costs for lung cancer and heart diseases are approximately \$88,139 and \$45,532 per patient in 2018, respectively. Both estimates have been adjusted for in<sup>fl</sup>ation over the years. Therefore, the cost savings associated with the treatment of lung-cancer treatment and heart diseases are \$396.63 $( = \bar { 9 } 8 8 , 1 3 9 \times ( 0 . 6 4 \% - 0 . 1 9 \% ) )$ and \$455.32 $( = \ S 4 5 , 5 3 2 \times ( 3 . 0 \% - 2 . 0 \% ) )$ per patient. Given the estimated 276,480 new cases of invasive breast cancer in 2020 (Breastcancer.org 2019), the proposed personalized treatment-planning framework can reduce the expected treatment cost associated with radiationinduced lung cancer and heart diseases by \$235.5 million. Because we have not accounted for the reduced risk of other adverse effects (such as depression and anxiety) under the personalized treatment plans, such estimate is conservative, and the actual cost savings could be higher.

## 5. Discussion

In this research, we propose a novel framework to guide the prescription of personalized radiotherapy plans for early stage breast cancer patients. Our research brings two important advances to decision support in radiotherapy planning. First, we incorporate the patient-speci<sup>fi</sup>c information along the treatment trajectory into a radiobiological model to predict patients’ responses to different treatment plans. This is distinct from the pure data-driven approach that is commonly employed in the existing literature. Second, we adapt a state-of-the-art algorithm $( \mathrm { i . e . , A d a m } )$ to solve the constraint optimization problem in the personalization and customization of treatment plans. Although much progress has been made in optimizing the delivery of radiotherapy plans for breast cancer, this is, to the best of our knowledge, the <sup>fi</sup>rst paper that studies the optimal design of radiotherapy plans for individual patients.

## 5.1. Contribution to Research

Our work responds directly to the call for more information systems (IS) research on “the design, implementation, and meaningful use of HIT” (Agarwal et al. 2010, p. 799). Speci<sup>fi</sup>cally, our proposed framework uni<sup>fi</sup>es and expounds upon the insights from both statistical modeling and computational simulations to offer new capabilities in optimizing treatment planning for individual patients. To ensure the <sup>fi</sup>delity of our simulations and the relevance of the results, we have also accounted for various complications and constraints from real-world clinical environments.

Our work also showcases the potential of predictive modeling and optimization strategies for personalized medicine, a prominent area for healthcare IS research (Fichman et al. 2011). Because of the limited availability of high-quality clinical and patient data, current IS research around personalized medicine has primarily focused on individuals’ self-management of health conditions via social media (Yan and Tan 2014) and wearable devices (Son et al. 2020); little attention has been paid to measure or quantify the value of analytics-based treatment strategies. Our research attempts to <sup>fi</sup>ll this gap by examining the potential of a personalized treatment-planning framework. To this point, it is worth mentioning that although the current study is speci<sup>fi</sup>cally geared toward radiotherapy planning for breast cancer, the design principles of our framework can be applied to the personalization of treatment plans for patients with other chronic diseases that typically involve complications and comorbidities.

Finally, despite the recent wave of promises and breakthroughs around the application of arti<sup>fi</sup>cial intelligence techniques in clinical diagnostics, the idiosyncratic nature of the healthcare sector poses many challenges to the design and deployment of predictive models. To start with, it requires signi<sup>fi</sup>cant knowledge of the existing clinical work<sup>fl</sup>ow to ensure that models are trained on relevant patient cohorts and are applied at a relevant point during the clinical work-<sup>fl</sup>ow. Besides, healthcare predictive models are also expected to have a (high) degree of interpretability in order to facilitate the communication between patients and physicians. In the current research, we try to balance the trade-off between the <sup>fl</sup>exibility and interpretability of our predictive model by drawing upon the extant literature on clinical oncology to characterize patients’ response to a speci<sup>fi</sup>c treatment. Our work sheds new light on how to combine domain knowledge and patient data in developing effective decision support tools for clinical use.

## 5.2. Implication to Practice

Recent advances in gene sequencing, imaging technologies, and digital pathology have greatly increased our understanding of disease mechanisms and provided unprecedented opportunities to identify novel treatment plans that may yield better patient outcomes. However, in many clinical settings, care providers’ ability to optimize treatment is limited by the complexities resulting from the patient heterogeneity and lack of high-precision biomarkers. Speci<sup>fi</sup>cally, in the context of radiotherapy, given the con<sup>fl</sup>icting objectives (i.e., maximizing tumor control while minimizing the normal tissue toxicity and complication) and lack of information about the exact locations and amount of MTCs, designing a good treatment plan is particularly challenging. Our novel treatmentplanning framework addresses these challenges by incorporating individual patients’ clinical features into the inferences of patients’ disease progression to tailor the treatment plans.

Our <sup>fi</sup>ndings reinforce the necessity and importance of effective and ef<sup>fi</sup>cient information sharing in multidisciplinary care settings. In our case, the personalization of treatment plans (and, thus, the realization of the potential economic bene<sup>fi</sup>ts) is only possible if we can integrate patients’ medical records and clinical information seamlessly throughout the diagnostic and treatment trajectory. Despite the increasing adoption and use of electronic medical records, in many realworld clinical settings, patients’ medical records and clinical information are still not readily accessible or are poorly synchronized among care providers from different institutions or even across different departments (e.g., the digitized microscopy slides from the pathology department are not shared with the radiation oncologists in the radiotherapy department). Such information friction remains a major obstacle for effective management of care. To this end, we believe that successful partnership between IS researchers and clinical practitioners could offer rich opportunities for continuous improvement in clinical information sharing and integration.

It is worth noting that although clinical researchers have a rich history of adopting data mining and machine learning techniques for prediction of treatment outcomes (especially patient survival rates), most of the existing studies rely on models that are built around given treatment regimens and trained on individual patient records. Such models do not enable predictions of outcomes for patients treated with previously unseen therapy, thus limiting their ability to provide useful insights for designing novel treatment plans. In contrast, our predictive model is informed by the clinical domain knowledge (i.e., the TCP model that captures the complex radiobiological process) and allows for evaluation of novel treatment plans. Therefore, our research complements prior works of predictive analytics in clinical practices.

Finally, as clinical trials are very costly and typically take a long time, it is important to select high-quality treatment plans for clinical trials. Our framework can be used to screen and select prospective treatment plans to be tested in future clinical trials. It is particularly useful when we consider nonconventional treatment plans that have not received much attention in clinical research.

## 5.3. Limitations and Future Work

Our current study bears several limitations that, nevertheless, provide possible directions for future research. First, our model-based approach necessitates the use of simplifying assumptions about the complex radiobiological processes. However, one advantage of this approach is that it provides us with a platform upon which we can perform counterfactuals using computational experiments to address some of the most pressing questions in personalizing treatment plans as best as we can. Second, we have assumed a classical setup of breast-conserving therapy (i.e., surgery plus radiotherapy) when modeling patients’ treatment processes. In some real-world cases, adjuvant therapy (such as chemotherapy and hormone therapy) may be used along with radiotherapy, which would lead to the increase of radiosensitivity of tumor cells or other biological effects and, thus, would bias our estimation and prediction. Further, recent research has shown that the timing of radiotherapy could also impact the treatment outcome (Jobsen et al. 2013). Because the clinical trial data used in our modeling process did not include the timing information, we cannot take it into account in the optimization process. Once such data are available, we can develop a dynamic treatment-planning framework by closely monitoring patient response and disease progression (Helm et al. 2015, Kazemian et al. 2019). Third, we use average dose as the key indicator to measure the side effects caused by radiation to adjacent organs such as heart and lung. Such a measure does not fully account for patients’ clinical pro<sup>fi</sup>les. Future research may explore other <sup>fi</sup>ne-grained indicators to better re<sup>fl</sup>ect patients individual needs. Finally, the personalized treatment plans presented in the current paper are evaluated solely through simulation experiments and, thus, merit further evaluation in clinical trials before they can be adopted in practice.

## Acknowledgments

The authors thank senior editor Yong Tan, associate editor Lucy Yan, and the three anonymous reviewers for their extremely helpful comments and suggestions. The paper also received valuable feedback from participants at the research seminar of Survival, Longitudinal And Multivariate Data Working Group of the Johns Hopkins Bloomberg School of Public Health, and the Conference on Health IT and Analytics. Any remaining errors are the authors’ own. Wei Chen and Yixin Lu contributed equally to this research; their names are listed in alphabetic order.

## Endnotes

<sup>1</sup> https://www.breastcancer.org/symptoms/understand\_bc/ statistics (last accessed: January 30, 2021).

<sup>2</sup> Early stage patients represent more than 80% of the diagnosed cases; see details at https://www.cancer.org/content/dam/cancerorg/research/cancer-facts-and-statistics/breast-cancer-facts-andfigures/breast-cancer-facts-and-figures-2019-2020.pdf (last accessed: January 30, 2021).

<sup>3</sup> In the current clinical practice, radiation oncologists are taking the major responsibility in making radiotherapy plans; see details at https://www.nationalbreastcancer.org/breast-cancer-radiationtherapy (last accessed: January 30, 2021).

<sup>4</sup> The estimated new cases are 276,480 in 2020; see details at https:// seer.cancer.gov/statfacts/html/breast.html (last accessed: January 30, 2021).

<sup>5</sup> Radiotherapy for breast cancer may be delivered in two ways: external beam radiation and internal radiation (brachytherapy). In this research, we focus on the external beam radiation, as it is the most common type of radiation treatment used for breast cancer.

<sup>6</sup> Gray is the unit that measures the intensity of the energy deposited in any small tissue of a patient in radiotherapy.

<sup>7</sup> Prior clinical trials (Bartelink et al. 2007) suggest that a boosted homogeneous plan (i.e., 66 Gy) can improve local tumor control; however, it would also lead to considerable tissue damage (fibrosis).

<sup>8</sup> There are two types of MTCs: indolent cells and clonogenic cells. Only clonogenic cells contribute to the risk of local recurrence of tumor.

<sup>9</sup> The clonogenic cell fraction and the MTC radiosensitivity are independent: The former is related to certain gene types (Slamon et al. 2001, Chen and Parmigiani 2007), and it captures the aggressiveness of the tumor and determines the progression of the tumor cells; the latter is a measure of how easy it is to kill individual tumor cells through DNA damage by using radiation. It can be affected by nuclear protein (Jiao et al. 2007) or chemotherapy medication (Rao et al. 2000).

<sup>10</sup> We chose to split the clinical-trial data by half to ensure that we have a sufficient number of patients under different treatment plans in both the training and test sets.

<sup>11</sup> When it comes to the radiation-induced side effects, given the high uncertainty involved in individual patients’ disease progression, it is very difficult to quantify the general impact in terms of disutility or life years lost without relevant data. On the other hand, there is solid clinical evidence that shows patients who received a high dose of radiotherapy are at higher risks of lung cancer (Grantzau et al. 2014) and heart diseases (Darby et al. 2013). Based on these considerations, we believe that the average dose serves as a good metric to measure the adverse effects of radiation treatment.

<sup>12</sup> Over the past few years, Adam has been incorporated into many deep-learning models for clinical event prediction (Deasy et al. 2020), image recognition (Xu et al. 2015), and natural language processing (Vaswani et al. 2017). To the best of our knowledge, this is the first study that applies Adam to treatment planning.

## References

Abbasi A, Li J, Adjeroh D, Abate M, Zheng W (2019) Don’t mention it? Analyzing user-generated content signals for early adverse drug event warnings. Inform. Systesm Res. 30(3):1007–1028.

Agarwal R, Gao G, DesRoches C, Jha A (2010) Research commentary—the digital transformation of healthcare: Current status and the road ahead. Inform. Systems Res. 21(4):796–809.

Aspinall MG, Hamermesh RG (2007) Realizing the promise of personalized medicine. Harvard Bus. Rev. 85(10):108–117.

Bardhan I, Oh J, Zheng Z, Kirksey K (2015) Predictive analytics for readmission of patients with congestive heart failure. Inform. Systems Res. 26(1):19–39.

Bartelink H, Horiot JC, Poortmans PM, Struikmans H, Van den Bogaert W, Fourquet A, Jager JJ, et al (2007) Impact of a higher radiation dose on local control and survival in breast-conserving therapy of early breast cancer: 10-year results of the randomized boost vs. no boost EORTC 22881-10882 trial. J. Clin. Oncol. 25(22):3259–3265.

Bates DW, Saria S, Ohno-Machado L, Shah A, Escobar G (2014) Big data in healthcare: Using analytics to identify and manage high-risk and high-cost patients. Health Affairs 33(7):1123–1131.

Bertsimas D, O’Hair A, Relyea S, Silberholz J (2016) An analytics approach to designing combination chemotherapy regimens for cancer. Management Sci. 62(5):1511–1531.

Bishop CM (2006) Pattern Recognition and Machine Learning (Springer, New York).

Bortfeld T, Chan TC, Tro<sup>fi</sup>mov A, Tsitsiklis JN (2008) Robust management of motion uncertainty in intensity-modulated radiation therapy. Oper. Res. 56(6):1461–1473.

Bortfeld T, Ramakrishnan J, Tsitsiklis JN, Unkelbach J (2015) Optimization of radiation therapy fractionation schedules in the presence of tumor repopulation. INFORMS J. Comput. 27(4): 788–803.

Breastcancer.org (2019) U.S. breast cancer statistics. Accessed January 30, 2021, https://www.breastcancer.org/symptoms/ understand bc/statistics.

Burke W, Psaty BM (2007) Personalized medicine in the era of genomics. JAMA 298(14):1682–1684.

Cardoso F, Kyriakides S, Ohno S, Penault-Llorca F, Poortmans P, Rubio I, Zackrisson S, Senkus E (2019) Early breast cancer: ESMO clinical practice guidelines for diagnosis, treatment and follow-up. Ann. Oncol. 30(8):1194–1220.

Caruana R, Lou Y, Gehrke J, Koch P, Sturm M, Elhadad N (2015) Intelligible models for healthcare: Predicting pneumonia risk and hospital 30-day readmission. Proc. 21st ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (Association for Comput ing Machinery, New York), 1721–1730.

Chang Y, Park H, Yang HJ, Lee S, Lee KY, Kim TS, Jung J, Shin JM (2018) Cancer drug response pro<sup>fi</sup>le scan: A deep learning model that predicts drug effectiveness from cancer genomic signature. Sci. Rep. 8(1):1–11.

Chen S, Parmigiani G (2007) Meta-analysis of BRCA1 and BRCA2 penetrance. J. Clin. Oncol. 25(11):1329–1333.

Chen W, Gilhuijs K, Stroom J, Bartelink H, Sonke JJ (2014) A simulation framework for modeling tumor control probability in breast conserving therapy. Radiotherapy Oncol. 111(2):289–295.

Darby S, Ewertz M, McGale P, Bennet AM, Blom-Goldman U, Bronnum D, Correa C, et al (2013) Risk of ischemic heart disease in women after radiotherapy for breast cancer. N. Engl. J. Med. 368(11):987–998.

Darby S, McGale P, Correa C, Taylor C, Arriagada R, Clarke M, Cutter D, et al (2011) Effect of radiotherapy after breastconserving surgery on 10-year recurrence and 15-year breast cancer death: Meta-analysis of individual patient data for 10,801 women in 17 randomised trials. Lancet 378(9804):1707–1716.

De Fauw J, Ledsam JR, Romera-Paredes B, Nikolov S, Tomasev N, Blackwell S, Askham H, et al (2018) Clinically applicable deep learning for diagnosis and referral in retinal disease. Nature Med. 24(9):1342–1350.

Deasy J, Ercole A, Lio P (2020) Adaptive prediction timing for elec-\` tronic health records. Preprint, submitted March 5, https:// arxiv.org/abs/2003.02554.

Demirezen E, Kumar S, Sen A (2016) Sustainability of healthcare information exchanges: A game-theoretic approach. Inform. Systems Res. 27(2):240–258.

Early Breast Cancer Trialists’ Collaborative Group (2005) Effects of radiotherapy and of differences in the extent of surgery for early breast cancer on local recurrence and 15-year survival: an overview of the randomised trials. Lancet 366(9503):2087–2106.

Fichman R, Kohli R, Krishnan R, Kane G (2011) The role of information systems in healthcare: Current research and future trends. Inform. Systems Res. 22(4):419–428.

Geruso M, Jena AB, Layton T (2018) Will personalized medicine mean higher costs for consumers? Harvard Bus. Rev. (March 1), https://hbr.org/2018/03/will-personalized-medicine-mean -higher-costs-for-consumers.

Ginsberg J, Mohebbi MH, Patel RS, Brammer L, Smolinski MS, Brilliant L (2009) Detecting in<sup>fl</sup>uenza epidemics using search engine query data. Nature 457(7232):1012–1014.

Goldberger JJ, Buxton AE (2013) Personalized medicine vs guideline-based medicine. JAMA 309(24):2559–2560.

Grantzau T, Thomsen M, Væth M, Overgaard J (2014) Risk of second primary lung cancer in women after radiotherapy for breast cancer. Radiotherapy Oncol. 111(3):366–373.

Gregor S, Hevner A (2013) Positioning and presenting design science research for maximum impact. MIS Quart. 37(2):337–355.

Hamburg MA, Collins FS (2010) The path to personalized medicine. N. Engl. J. Med. 363(4):301–304.

Heidelberger P, Welch PD (1983) Simulation run length control in the presence of an initial transient. Oper. Res. 31(6):1109–1144.

Helm JE, Lavieri MS, Van Oyen MP, Stein JD, Musch DC (2015) Dynamic forecasting and control algorithms of glaucoma progression for clinician decision support. Oper. Res. 63(5):979–999.

Hevner A, March ST, Park J, Ram S (2004) Design science in information systems research. MIS Quart. 28(1):75–105.

Højris I, Overgaard M, Christensen J, Overgaard J (1999) Morbidity and mortality of ischaemic heart disease in high-risk breast-cancer patients after adjuvant postmastectomy systemic treatment with or without radiotherapy: Analysis of DBCG 82b and 82c randomised trials. Lancet 354(9188):1425–1430.

Jaffray D (2012) Image-guided radiotherapy: From current concept to future perspectives. Nat. Rev. Clin. Oncol. 9(12):688–699.

Jiao Y, Wang H-c, Fan S-j (2007) Growth suppression and radiosensitivity increase by HMGB1 in breast cancer. Acta Pharmacol. Sin. 28(12):1957–1967.

Jobsen J, Van der Palen J, Baum M, Brinkhuis M, Struikmans H (2013) Timing of radiotherapy in breast-conserving therapy: A large prospective cohort study of node-negative breast cancer patients without adjuvant systemic therapy. Brit. J. Cancer. 108(4):820–825.

Kakushadze Z, Raghubanshi R, Yu W (2017) Estimating cost savings from early cancer diagnosis. Data (Basel) 2(3):30.

Kazemian P, Helm JE, Lavieri MS, Stein JD, Van Oyen MP (2019) Dynamic monitoring and control of irreversible chronic diseases with application to glaucoma. Production Oper. Management 28(5):1082–1107.

Kingma DP, Ba J (2014) Adam: A method for stochastic optimization. Preprint, submitted December 22, https://arxiv.org/abs/ 1412.6980.

Lee CK, Hofer I, Gabel E, Baldi P, Cannesson M (2018) Development and validation of a deep neural network model for prediction of postoperative in-hospital mortality. Anesthesiology 129(4):649–662.

Lin Y, Chen H, Brown R, Li S, Yang H (2017) Healthcare predictive analytics for risk pro<sup>fi</sup>ling in chronic care: A Bayesian multitask learning approach. MIS Quart. 41(2):473–495.

Luenberger DG, Ye Y (2016) Linear and Nonlinear Programming, 4th ed., International Series in Operations Research & Management Science, vol. 228 (Springer Science & Business Media, Cham, Switzerland).

Meyer G, Adomavicius G, Johnson PE, Elidrisi M, Rush WA, Sperl-Hillen JM, O’Connor PJ (2014) A machine learning approach to improving dynamic decision making. Inform. Systems Res. 25(2):239–263.

Nash JC (2014) On best practice optimization methods in R. J. Statist. Software 60(2):1–14.

Negoescu DM, Bimpikis K, Brandeau ML, Iancu DA (2018) Dynamic learning of patient response types: An application to treating chronic diseases. Management Sci. 64(8):3469–3488.

Njeh CF, Dong L (2013) IGRT has limited clinical value due to lack of accurate tumor delineation. Med. Phys. 40(4):040601.1–040601.4.

O’Rourke S, McAneney H, Hillen T (2009) Linear quadratic and tumour control probability modelling in external beam radiotherapy. J. Math. Biol. 58(4-5):799–817.

Polgar C, Fodor J, Major T, Sulyok Z, K´ asler M (2013) Breast-´ conserving therapy with partial or whole breast irradiation: Ten-year results of the Budapest randomized trial. Radiotherapy Oncol. 108(2):197–202.

Rao GS, Murray S, Ethier SP (2000) Radiosensitization of human breast cancer cells by a novel ErbB family receptor tyrosine kinase inhibitor. Internat. J. Radiation Oncol. Biol. Phys. 48(5):1519–1528.

Rasmussen CE, Ghahramani Z (2003) Bayesian Monte Carlo. Adv. Neural Inform. Processing Systems 15:489–496.

Romeijn HE, Ahuja RK, Dempsey JF, Kumar A (2006) A new linear programming approach to radiation therapy treatment planning problems. Oper. Res. 54(2):201–216.

Rosenberg ES, Davidian M, Banks HT (2007) Using mathematical modeling and control to develop structured treatment interruption strategies for HIV infection. Drug Alcohol Dependence 88(Suppl. 2):S41–S51.

Sagha<sup>fi</sup>an S, Hopp WJ, Van Oyen MP, Desmond JS, Kronick SL (2014) Complexity-augmented triage: A tool for improving

patient safety and operational ef<sup>fi</sup>ciency. Manufacturing Service Oper. Management 16(3):329–345.

Seegert L (2020) The <sup>fi</sup>nancial burden of breast cancer. Forbes (January 21), https://www.forbes.com/sites/nextavenue/2020/01/ 21/the-<sup>fi</sup>nancial-burden-of-breast-cancer/#cae666a4d217.

Shmueli G, Koppius OR (2011) Predictive analytics in information systems research. MIS Quart. 35(3):553–572.

Shusharina N, Craft D, Chen YL, Shih H, Bortfeld T (2018) The clinical target distribution: A probabilistic alternative to the clinical target volume. Phys. Med. Biol. 63(15):155001.

Slamon DJ, Leyland-Jones B, Shak S, Fuchs H, Paton V, Bajamonde A, Fleming T, et al (2001) Use of chemotherapy plus a monoclonal antibody against HER2 for metastatic breast cancer that overexpresses HER2. N. Engl. J. Med. 344(11):783–792.

Smith B, Bellon J, Blitzblau R, Freedman G, Haffty B, Hahn C, Halberg F, et al (2018) Radiation therapy for the whole breast: Executive summary of an American Society for Radiation Oncology (ASTRO) evidence-based guideline. Practical Radiation Oncol. 8(3):145–152.

Son J, Brennan P, Zhou S (2020) A data analytics framework for smart asthma management based on remote health information systems with Bluetooth-enabled personal inhalers. MIS Quart. 43(4):285–303.

Tabak YP, Sun X, Nunez CM, Johannes RS (2014) Using electronic health record data to develop inpatient mortality predictive model: Acute laboratory risk of mortality score (ALaRMS). J. Amer. Med. Inform. Assoc. 21(3):455–463.

Tolmachev V, Stone-Elander S, Orlova A (2010) Radiolabelled receptor-tyrosine-kinase targeting drugs for patient strati<sup>fi</sup>cation and monitoring of therapy response: prospects and pitfalls. Lancet Oncol. 11(10):992–1000.

Ungun B, Xing L, Boyd S (2019) Real-time radiation treatment planning with optimality guarantees via cluster and bound methods. INFORMS J. Comput. 31(3):544–558.

Valdes G, Simone CB II, Chen J, Lin A, Yom SS, Pattison AJ, Carpenter CM, Solberg TD (2017) Clinical decision support of radiotherapy treatment planning: A data-driven machine learning strategy for patient-speci<sup>fi</sup>c dosimetric decision making. Radiotherapy Oncol. 125(3):392–397.

van Herk M, Remeijer P, Rasch C, Lebesque J (2000) The probability of correct target dosage: Dose-population histograms for

deriving treatment margins in radiotherapy. Internat. J. Radiation Oncol. Biol. Phys. 47(4):1121–1135.

van Laarhoven PJ, Aarts EH (1987) Simulated annealing. Simulated Annealing: Theory and Applications (Springer, Dordrecht, Netherlands), 7–15.

Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez AN, Kaiser Ł, Polosukhin I (2017) Attention is all you need. Adv. Neural Inform. Processing Systems 30:6000–6010.

Vose MD (1999) The Simple Genetic Algorithm: Foundations and Theory (MIT Press, Cambridge, MA).

Vrieling C, van Werkhoven E, Maingon P, Poortmans P, Weltens C, Fourquet A, Schinagl D, et al (2017) Prognostic factors for local control in breast cancer after long-term follow-up in the EORTC boost vs no boost trial: A randomized clinical trial. JAMA Oncol. 3(1):42–48.

Webb S, Nahum A (1993) A model for calculating tumour control probability in radiotherapy including the effects of inhomogeneous distributions of dose and clonogenic cell density. Phys. Med. Biol. 38(6):653–666.

Xu Y, Xu Y, Saria S (2016) A Bayesian nonparametric approach for estimating individualized treatment-response curves. Workshop and Conf. Proc. J. Machine Learn. Res. 56:282–300.

Xu K, Ba J, Kiros R, Cho K, Courville A, Salakhudinov R, Zemel R, Bengio Y (2015) Show, attend and tell: Neural image caption generation with visual attention. Proc. 32nd Internat. Conf. Machine Learn. 37:2048–2057.

Yan L, Tan Y (2014) Feeling blue? Go online: An empirical study of social support among patients. Inform. Systems Res. 25(4): 690–709.

Yaraghi N, Du A, Sharman R, Gopal R, Ramesh R (2014) Health information exchange as a multisided platform: Adoption, usage, and practice involvement in service co-production. Inform. Systems Res. 26(1):1–18.

Yu J, Shah B, Ip E, Chan J (2013) A Markov model of the costeffectiveness of pharmacist care for diabetes in prevention of cardiovascular diseases: Evidence from Kaiser Permanente Northern California. J. Managed Care Pharmacy 19(2):102–114.

Zaider M, Hanin L (2011) Tumor control probability in radiation treatment. Med. Phys. 38(2):574–583.

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
