---
otero_id: 7724
otero_key: "R6RK6TS7"
title: "Designing utilization-based spatial healthcare accessibility decision support systems: A case of a regional health plan"
authors: "Yan Li; Au Vo; Manjit Randhawa; Genia Fick"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.011"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Designing utilization-based spatial healthcare accessibility decision support systems: A case of a regional health plan

ELSEVIER Decision Support Systems

Yan Li, Au Vo, Manjit Randhawa, Genia Fick

![](/api/attachments/R6RK6TS7/fulltext/images/d0173df65ba220b1dd9fd6cec7821b00d39084276f56eea873a8edf2ed47e7cf.jpg)

PII: S0167-9236(17)30089-1

DOI: doi: 10.1016/j.dss.2017.05.011

Reference: DECSUP 12846

To appear in: Decision Support Systems

Received date: 5 October 2016

Revised date: 25 April 2017

Accepted date: 4 May 2017

Please cite this article as: Yan Li, Au Vo, Manjit Randhawa, Genia Fick , Designing utilization-based spatial healthcare accessibility decision support systems: A case of a regional health plan, Decision Support Systems (2017), doi: 10.1016/j.dss.2017.05.011

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Designing Utilization-based Spatial Healthcare Accessibility Decision Support Systems: A Case of a Regional Health Plan

\* Yan Li Claremont Graduate University Center for Information Systems and Technology 130 E. 9th Street - ABC 217, Claremont, CA 91711 USA Email: Yan.Li@cgu.edu Phone: +1.909.607.3673

Au Vo Center for Information Systems and Technology 130 E. 9th Street - ABC 217, Claremont, CA 91711 USA Email: Au.Vo@cgu.edu

Manjit Randhawa Inland Empire Health Plan 10801 6th St, Rancho Cucamonga, CA 91730 Email: Randhawa-M@iehp.org

Genia Fick

Inland Empire Health Plan

10801 6th St, Rancho Cucamonga, CA 91730

Email: Fick-G@iehp.org

\* Corresponding author

# Designing Utilization-based Spatial Healthcare Accessibility Decision Support Systems: The Case of a Regional Health Plan

## Abstract:

In the U.S., myriad healthcare reforms have begun to show some positive effects on enabling “potential access”. One facet of healthcare access, “having access”, which is the availability and accessibility of health services for the surrounding populations, has not been adequately addressed. Research regarding “having access” is presently championed by a family of methods called Floating Catchment Area (FCA). However, existing scholarship is limited in integrating non-spatial factors within the FCA methods. In this research, we propose a novel utilization-based framework as the first attempt to adopt the Behavioral Model of Health Services Use as a theoretical lens to integrate non-spatial factors in spatial healthcare accessibility research. The framework employs a unique approach to derive categorical and factor weights for different population subgroup’s healthcare needs using predictive analytics. The proposed framework is evaluated using a case study of a regional health plan. A Spatial Decision Support System (SDSS) instantiates the framework and enables decision makers to S validates the practicality of the proposed utilization-based framework and subsequently allows other FCA methods to be implemented in real-world applications.

## Keywords:

Two-step floating catchment area; healthcare access; spatial analytics; spatial decision support; the Behavioral Model of Health Services Use.

## 1. Introduction

Access to healthcare is a complex and multidimensional phenomenon. It refers to the ability of individuals to obtain needed healthcare services. To increase health insurance quality, affordability, and coverage, the U.S. government has enacted the Patient Protection and Affordable Care Act [36]. In terms of improving healthcare access, the Affordable Care Act has started to address the issue of enabling “potential access” [17]. Another dimension of access, “equitable access”, indicates that healthcare utilization should be determined by population healthcare needs instead of their socioeconomic characteristics. The federal government has also facilitated this dimension. For example, Medicare and Medicaid programs are designed to provide equal access to the U.S. healthcare system for various disadvant ed groups. One dimension of access that the U.S. government has not adequately addressed t hrough policies and legislations is “having access”. Having access, which is the notion of health services availability and accessibility for surrounding populations, has been delegated to healthcare organizations [17]. As a result, understanding healthcare access in terms of service availability, especially in lieu of primary care providers (PCPs), is integral to improving access.

Factors that influence “having access” can be categorized into two dimensions: spatial and non-spatial. Spatial factors emphasize geographic distances between population and health service providers, while non-spatial factors consist of variables such as demographics and socioeconomic status. To assess these he U.S. Health Resources and Services Administration (HRSA) has defined, red, and continuously monitored locations that are designated as Health Professional Shortage Areas (HPSAs) and Medically Underserved Areas/Populations (MUP/As) [45]. HPSAs contain three types of medical provider designations: Primary Care, Dental, and Mental Health. These designations help policy makers, researchers, and healthcare professionals address the current population needs and related resource allocation. Of these designations, primacy care resources remain inadequate yet the most demanded. Therefore, providing access to primary care resources presents major challenges.

Researchers attempted to improve upon the HPSA designation method and derived a family of methods to measure healthcare spatial accessibility called Floating Catchment Area (FCA) [26]. FCA methods focus on designing spatial accessibility algorithms to accommodate the

# ACCEPTED MANUSCRIPT

interplay between population demand and healthcare supply. However, they have not been incorporated into existing practices of designating HPSAs by the HRSA. In fact, the spatial accessibility index (SPAI) derived from the FCA methods family, when compared with existing HPSAs published by the HRSA, showed little overlapping regions [25]. One plausible explanation is that healthcare needs of populations impact significantly on healthcare service availability. While the HPSA designation method takes into account some non-spatial factors, a majority of FCA methods do not consider them. A few applied FCA research cognized this deficit and begun to incorporate non-spatial factors [24, 32, 52]. Ho ost of them investigated the non-spatial and non-spatial aspects separately. While it is possible to directly incorporate the population’s healthcare needs into the SPAI by assigning weights to different population subgroups, the determination of such weights requires empirical evidence, such as the real healthcare utilization data. To date, the weight determination for non-spatial access factors remains as a theoretical conjecture and has t been tested empirically. Thus, the first objective of this research is to investigate how demand weights of various population subgroups may be determined based on real utilization data.

From a theoretical viewpoint, the Behavioral Model of Health Services Use (BM) [1, 3] is one of the most widely used models for understanding how population characteristics determine healthcare access. The BM has been used in numerous research studies, including several systematic reviews on different aspects of healthcare utilization [11, 20, 30]. However, theoretical constructs from the BM have not been employed in spatial accessibility research despite past research suggestions. Integrating spatial and non-spatial factors successfully is a critical step in the design of an effective method to assess healthcare access [52]. We posit that the BM can guide the inclusion of empirically grounded non-spatial factors within the existing healthcare spatial access measurements. To bridge this theoretical gap, the second objective of this research is to design a framework to measure healthcare spatial access by integrating nonspatial factors prescribed by the BM.

# ACCEPTED MANUSCRIPT

The increasing usage of Geographical Information Systems (GIS) in health organizations,

together with the proliferation of spatially disaggregated data, has led to a plethora of

applications that analyze spatial accessibility of health services [19]. The ability to identify and

measure spatial variations in healthcare need and access is vital to health service planning and

resource allocation [19]. However, the decision process is increasingly more complex when

attempting to integrate both spatial and non-spatial factors. Thus, a Spatial Decision Support

System (SDSS) is essential to integrate database management systems, analytical models,

geographical displays, and tabular reporting capabilities with the expert knowledge of decision

makers (DMs) [13]. Similar to previous SDSS research [22, 39], our third research objective

aims to design a SDSS that supports both spatial and non-spatial inputs, complex spatial

relations, spatial data analysis, and map representations of outputs.

Our research thus targets to answer two important research questions. Research Question 1:

How can non-spatial factors prescribed by the BM be integrated within the FCA method family’s

spatial accessibility algorithm using real healthcare utilization data? And, Research Question 2:

How can healthcare spatial accessibility indices that include non-spatial factors be presented to

decision makers (DMs) to explore the effect of non-spatial factors in healthcare shortage areas.

By answering these research questions, this research makes three important contributions.

First, by adopting the BM in evaluating accessibility among different population subgroups, our

study bridges the theoretical gap between healthcare spatial accessibility research and survey-

based healthcare access studies. This research is the first attempt to use the BM as the

theoretical foundation to evaluate non-spatial factors in healthcare spatial accessibility research.

Furthermore, the BM has been employed frequently in survey-based research, which is

deductive in nature (i.e., testing BM-based hypotheses using sample data). In contrast, our

proposed framework demonstrates how data mining and predictive analytics can be used to

inductively discover new knowledge about healthcare access. Scientific advance may be seen

as an iterative cycle of induction and deduction, where hypothetic-deductive reasoning links

# ACCEPTED MANUSCRIPT

background knowledge to observations, and inductive reasoning turns observations into new knowledge [21]. Thus, our utilization-based knowledge discovery approach complements traditional hypothesis-led BM studies in providing a holistic view of healthcare access. Second, this study improves upon current FCA research by proposing a utilization-based framework that measures healthcare spatial access with non-spatial factors integration. The framework takes into consideration various healthcare needs for different population subgroups d employs a data-driven approach to assign relative weights to these groups. The novelty framework is the capitalization of actual utilization data to derive weights for popula haracteristics as opposed to statistical assumptions that are prevalent in previous spatial accessibility studies. Finally, the SDSS we developed embodies the utilization-based framework in a real-world organization. DMs can reply on the SDSS to envisage differ arios based on different population characteristics and make appropriate adjust ents healthcare resource location and allocation. In a boarder generalizability and app context, our SDSS highlights the limitless potential of FCA methods to help improve the assessment of healthcare access.

The rest of the paper is organized as follows. Section 2 presents a background on BM, the theoretical framework we used for measuring healthcare access, followed by a review of the FCA method family in section 3. Section 4 illustrates the research methodology and the case study background. The proposed utilization-based healthcare accessibility framework for measuring healthcare spatial access is designed and evaluated using a real-world case study in section 5, followed by the design of our SDSS in section 6. In section 7, we present future research directions and our research conclusion.

## 2. Theoretical Framework for Measuring Healthcare Access

In this research, we utilized the BM [1, 3] as the theoretical framework for measuring healthcare access. The BM posits that access is a multi-dimensional concept that can be measured as potential access (presence of potential resources) or revealed access (actual use of healthcare services). The most commonly used explication of the BM (Figure 1) by Andersen and Davidson [4] includes two determinants of healthcare access: contextual and individual.

![](/api/attachments/R6RK6TS7/fulltext/images/710c33d1eb4fd53beb2dd2b51a6184391d1d7956bcbd2f2660668af66e62202b.jpg)  
Figure 1: The Behavioral Model of health services use [4]

Contextual characteristics refer to circumstances and environments of healthcare access such as healthcare-provider-related factors and community characteristics. They are e.g., provider organizations, health plans, or local communities. Indiv aracteristics ibe the population at risk (i.e. healthcare consumer). They are rela he contextual ristics through membership (e.g., a member of a health plan) or res a community). Furthermore, each determinant of healthcare access is divided three components: predisposing, enabling, and need. The predisposing factors, such as age and social support, exist prior to healthcare access and describe the propensity of individuals to use or not to use health services. The enabling factors, such as income and rural-urban characterization, describe the means individuals possess. The need factors refer to the immediate cause of health service use, such as the level of illness that is being perceived by an individual. These determinants are integral in measuring health behaviors and health outcomes (i.e., perceived health, evaluated health, and consumer satisfaction) as shown in Figure 1. Table 1 summarizes these key determinants and characteristics of healthcare access behavior.

Table 1: Determinants and components of healthcare access (summarized based on [4])

<table><tr><td colspan="3">Determinant</td></tr><tr><td>Component</td><td>Contextual</td><td>Individual</td></tr><tr><td>Predisposing</td><td>Demographic (e.g., age, gender, ethnicity of a community)Social (e.g., educational level, ethnic composition, employment rate)Belief (community perspective on how health services should be organized, financed, and made accessible to the population)</td><td>Demographic (e.g., age, gender, ethnicity)Social (e.g. individual&#x27;s education, occupation, and ethnicity, social network and social interactions)Health belief (e.g. attitudes, values and knowledge about the health and health services).</td></tr><tr><td>Enabling</td><td>Health Policy (government or private sectors)Financing (resources potentially available to pay for health services, such as per capita community income, relative price of medical care)Organization of health services (such as ratios of physicians and hospital to population)</td><td>Financing (e.g., income, wealth, having insurance)Organization (e.g. an individual has a regular source of care, means of transportation and travel time for care)</td></tr><tr><td>Need</td><td>Environmental need (e.g., air and water quality, death rates from homicides, etc.)Population health indices (general indicators of community health such as mortality rates, disability, etc.)</td><td>Perceived (i.e. how people view their general health and functional state).Evaluated need (i.e. professional judgement and objective measurement about the physical status and need for medical care)</td></tr></table>

The BM has been frequently applied in healthcare utilization studies, mainly in fields of public health and public policy. Babitsch et. al. [6] reviewed 16 studies that explicitly employed the BM as the theoretical foundation to study access to healthcare. A majority of studies utilized survey-based data such as National Health Interview Survey [5] or state-based telephone survey [14] to investigate a wide variety of predisposing, enabling, and need factors. The BM, therefore, enables not only the theoretical assessment, but also pragmatic decisions on selecting variables in our proposed framework.

In addition, our research diverges from the deductive logic presented in previous research. Prior studies have mostly attempted to test healthcare access behavior hypotheses put forth by the BM through a quantitative assessment of survey-based data. In contrast, our research embodies inductive logic through the use of data mining techniques to discover healthcare access patterns by examining real healthcare utilization data. Potentially, our proposed comprehensive view of healthcare access.

## 3. Floating Catchment Area Method Family

The current HPSA designation method primarily measures healthcare spatial availability as a ratio between population (demand) and provider (supply) within a region [50]. Although it is straightforward to implement, it does not account the interac regional boundaries and spatial variability within a region. The FCA method fa overcome these limitations by considering the intricate relations between supp and demand [51, 52]. In essence, a FCA method generates demand polygons around regions’ centroids and supply polygons around healthcare providers’ locations based on an assumed travel threshold. The catchment area encompasses both emand and supply polygons. Because the purpose of this research is to design a process that integrates non-spatial factors within spatial accessibility measures based on utilization data, our accessibility algorithm uses the FCA method family as the basis, but with non-spatial extensions. Because each FCA method has its strengths and limitations, we posit that the selection of a specific FCA method should be evaluated against business objectives and problems at hand. In the next section, we provide a brief comparison on FCA method main variations. Interested readers can refer to Wang [51] and Vo et. al. [46] for more comprehensive reviews.

# ACCEPTED MANUSCRIPT

## 3.1 Variations of FCA Methods

A substantial method improvement of the simple FCA was developed by Radke and Mu [38] by repeating the floating catchment twice. First, it creates supply catchments on physician locations. Next, it creates demand catchments for each population location. The SPAI is then calculated as the sum of the provider-to-population ratio at these locations. This method is Enhanced 2SFCA (E2SFCA) [25] is considered the benchmark for the FCA method improvement. The E2SFCA dissects the catchment into smaller travel time s and utilizes Gaussian weights to account for distance decay in each zone, addressing the dichotomous measure of access problem in the 2SFCA. Since then, research in improving the E2FCA has proliferated. These improvements can be characterized as three types. The first type concerns with catchment modification and catchment sizes. For instance, Luo and Whippo [27] introduced steps to calculate variable catchment sizes before applying the E2FCA. Alternatively, McGrail and Humphrey [33] chose variable catchment sizes based on five levels of geographical remoteness in Australia.

The second type aims to improve upon different travel time or distance measurement procedures. For example, Mao and Nekorchuk [28] applied weights to different transportation modes (e.g., bus versus car) to determine travel time; Wan et al. [49] created an additional step to the E2SFCA by assigning a selection weight between population and service locations to minimize overestimation; and Delamater [12] hypothesized the healthcare supply-demand interaction using pairwise comparison. In another effort, Wan et al. [48] proposed spatial access ratio as the accessibility measure to alleviate the uncertainty in SPAI associated with different impedance coefficient [26].

The third type investigates distance decay modeling approaches, i.e., stepwise, continuous, and hybrid (combination of stepwise and continuous) [50]. While research has utilized the stepwise approach extensively [28, 42, 49], continuous and hybrid approaches have also gained

# ACCEPTED MANUSCRIPT

sufficient attention. For example, Schuurman et al. [40] proposed a segmented inverse-power distance decay function; Gao et al. [16] defined the distance decay using a three-zone hybrid approach; and a variable distance decay function [7] was developed using a downward sigmoid function following a logistic distribution. These functions can be conceptualized using the Generalized 2SFCA (G2SFCA) [50], where a distance decay function is written as either a discrete (e.g. binary), continuous (e.g. power), or hybrid (e.g. kernel) function. However, currently, there is no empirical research on how to model distance decay atically [31]. Besides these improvements, there are also efforts to incorporate non-spatial data when measuring spatial accessibility, which is discussed below.

## 3.2 Incorporating Non-Spatial Factors to Measure Spatial Accessibility

As discussed in section 2, healthcare access is closely related to many non-spatial factors, such as individual demographic and socioeconomic characteristics. While most FCA-related research focus on the spatial factor (i.e., the spatial separation of population and providers) [50], a few studies have begun to incorporate no -spatial factors to measure spatial accessibility. Among those, a majority did not integrate non-spatial factors within the SPAI calculation. For to ntegrate spatial and non-spatial factors into one framework for identifying physician shortage areas. However, they first calculated the SPAI using 2SFCA, followed by a principle component analysis (PCA) to consolidate 11 non-spatial variables into three non-spatial factors. These two separate results were subsequently combined to define PCP shortage areas based on heuristic rules. Similarly, Wan et al. [47] estimated spatial and non-spatial access separately to examine the association between colorectal cancer survival and healthcare access. Their analysis focused on how non-spatial factors influenced cancer survival rather than how those factors would influence healthcare access. Likewise, Wang [50] investigated spatial and non-spatial factors’ influences in the variation of late-stage cancer rate using ordinary least squares regression. Mobley et al. [34] used multilevel regression to estimate effects of socio-ecological factors from the BM that could impact cancer screening, and then spatially translated the results into bivariate maps to reveal geographic disparity patterns.

Recently, Wang and Tormala [53] presented a framework to integrate spatial and nonspatial factors to evaluate the rural population’s access to PCP. They first measured the SPAI using the E2SFCA, and then calculated a non-spatial accessibility score using standardized zscore of aboriginal population percentage in Canada. scores were combined to highlight low spatial accessibility areas where there w hig centrations of a predetermined population with non-spatial disadvantages. However, the framework still separated the non-spatial factors from the SPAI calculation.

To the best of our knowledge, only one study [32] alluded to the true integration of nonspatial factors within the FCA method. In their study, McGrail and Humphreys [32] first created a single health need indicator for population locations and a single mobility indicator for provider locations. Both indicators were then integrated within an improved 2SFCA method to calculate the SPAI. However, their study is different from ours for two reasons. First, they used a single health need indicator in the SPAI algorithm as opposed to multiple non-spatial characteristics in our research. As acknowledged by other researchers [52], it is possible to assign larger weights to population subgroups with higher healthcare needs and directly incorporate them into the SPAI. However, existing research is constrained by data availability to define such weights. Our utilization-based approach is not limited by such constraints. Instead, the availability of real utilization data could enable us to derive these weights. Second, in calculating a single health need indicator, they derived weights for non-spatial factors from aggregated government population survey data (e.g., % males unemployed within a spatial unit). In comparison, our utilization-based approach provided the flexibility to choose different granularity of analysis based on different business objectives.

# ACCEPTED MANUSCRIPT

To summarize, almost all existing studies used aggregated census or government population data as the demand estimation, and all of the reviewed literature employed traditional statistics analysis techniques such as multilevel regression or PCA. Additionally, a vast majority of FCA studies that included non-spatial factors did not integrate them within the SPAI algorithm of the FCA method family. Rather, non-spatial accessibility and SPAI were examined separately. By provisioning real utilization data, this research pre uctively discover non-spatial accessibility patterns at the individual level. More import proach is the first attempt to integrate different non-spatial factors within the SPAI algorithm by determining demand weights among different population subgroups.

## 3.3. Related Work

Two related, but distinctive studies, have been published by members of this research team. First, Vo et al. [46] provided a literature review and delineated steps on how to compare different FCA methods. It did not involve designing artifacts, nor did it investigate non-spatial factors. Second, Plachkinova et al. [37] descri conceptual framework for a general FCA method, indicating the potential areas where improvements could be beneficial to the FCA method family develo pment. It also include non-spatial population characteristics. Both studies differed significantly from this research in terms of research objectives and research outputs. Past research, including the two studies summarized in this section, looks at healthcare accessibility at the macro level. However, US healthcare is of a network sort: each health insurance plan has its own provider network (in-network) that includes a set of doctors, hospitals and other healthcare providers. The overall in-network cost of care for a healthcare plan subscriber is significantly lower than an out-of-network one. Subscribers of a healthcare plan have an unparalleled incentive to stay within the plan’s provider network for their healthcare needs. Therefore, an investigation of actual access within a medical network, is crucial for the understanding of the applicability of the FCA method family as a whole.

## 4. Research Methodology and Case Study Background

This research is guided by the Design Science Research (DSR) framework and seven practical guidelines proposed by Hevner et. al. [18]. The framework emphasizes achieving Information Systems (IS) research relevance by framing research activities to address business needs and IS research rigor by meticulously applying existing foundations and methodologies from the knowledge base. Specifically, following the design as a search process guideline [18], our research activities were carried out through an iterative build-and-evaluate process. The research rigor guideline [18] was maintained throughout the design process by integrating theories, concepts, and best practices from interdisciplinary knowledge base, including the BM from public health, knowledge discovery and data mining process (KDDM) from IS, and spatial accessibility measures from GIS.

According to Hevner et al. [18], an environment is the problem space where the phenomena of interests reside, and is composed of organization, its people, and technologies. Our research achieves research relevance guideline by solving pressing business problems in a real-world healthcare organization. The organization is Southern California Regional (SCR), a pseudonamed for a regional healthcare plan provider. SCR offers both Medicare and Medicaid health plans to the public. To date, SCR has more than 1.3 million active members and 31,000 medical providers. As one of the top-rated Medicaid plans in the region, SCR strives to provide access to healthcare with minimal barriers. SCR actively monitors its members’ healthcare access rates through a variety of means, including active data collection. At the time of the study, the SCR had several transactional databases storing approximately 3TB data, and had just rolled out a centralized data warehouse that hosted approximately 500GB data.

At SCR, the business need for systematically measuring healthcare access was motivated by a recent finding regarding the lack of PCPs in San Bernardino and Riverside Counties in California, USA. As a part of its corrective action plan, SCR sought to spatially measure its

## ACCEPTED MANUSCRIPT

members’ healthcare accessibility and identify PCP shortage areas based on different member characteristics. The healthcare spatial measure could help SCR strategically target its outreach efforts to recruit more PCPs in shortage areas. Hence, two researchers with established background in spatial analytics were invited by two senior directors of SCR to design a utilization-based SDSS to analyze healthcare access. The researchers joined the team in beginning of 2016 and were actively involved for 12 months.

This research produced two GIS-based design artifacts (guideline 1 [18]). Our first artifact was the utilization-based framework, a conceptual structure intended to serve as a guide for measuring healthcare accessibility based on actual utilization data. The uniqueness of this artifact lies in the true integration of non-spatial factors with the spatial accessibility measures through inductive discovery of the varying healthcare needs among different population subgroups. The second artifact was a SDSS that insta iated th utilization-based framework using GIS tools. The SDSS provides capabilities of iewing and modifying accessibility indices of the regions of interest. It enables health service planners and policy makers to assess healthcare accessibility of a selected based on different population features.

The research also includes a methodological design evaluation (guideline 3 [18]) to design artifacts. The utilization-based framework was first evaluated by comparing the utilization-based SPAI with other comparable methods. Secondly, similar to Chiang & Che [10], the framework was evaluated by SCR from both understandingand action-oriented perspectives. Furthermore, the feasibility of the framework (i.e. its implementation into a working system) was indirectly evaluated using the SDSS instantiation. The outputs of the SDSS was assessed towards the business objectives of the case study. This evaluation also enabled us to determine whether the proposed framework achieved its intended purpose.

## 5. A Utilization-based Framework for Measuring Spatial Healthcare Access

## 5.1 Framework Overview

We developed the utilization-based framework by delineating four steps to derive the SPAI, as illustrated in Figure 2. The framework design is based on the existing knowledge discovery and data mining (KDDM) process models (e.g., CRISP-DM [41], KDD Process model [15], and KDDA process model [23]). These KDDM process models share some common iterative phases: Business Understanding (BU), Data Understanding (DU), Data Preparation (DP), Data Mining (Modeling), Evaluation, and Deployment. They aim to help practitioners organize analytic projects and communicate solutions to business users within a common framework [29]. Similarly, our proposed framework strives to guide the process of integrating BM characteristics within the spatial accessibility calculation. It assumes the availability of revealed access (i.e. actual utilization) data for inductively learning of utilization patterns.

![](/api/attachments/R6RK6TS7/fulltext/images/e4c27eeecc91e1ff8ab68d16d82826e959424c2b97b8c173fc67be11cb70f1cf.jpg)  
Figure 2: Flow diagram of the utilization-based framework for spatial healthcare access

The steps within the utilization-based frameworks were inspired by its similarities with the various KDDM phases (i.e., both support data-driven decision making, and employ inductive learning). The first step in the utilization-based framework is the evaluation of population and contextual characteristics derived from the BM. It is similar to the BU phase of the KDDM process that focuses on the business requirement elicitation and the translation of high-level business objectives into specific analytic goals. The outputs of this step include a set of BMrelated variables and business rules for variable transformation. The second step is data

# ACCEPTED MANUSCRIPT

preparation, where data from different sources are extracted, transformed, cleaned, and aggregated to the desired granularity level (e.g., community level) for predictive modeling. This is similar to the DU and DP phases in the KDDM process. The third step uses predictive modeling to determine weights for the BM characteristics, which is similar to the Modeling and Evaluation phase of KDDM. These weights are then used to calculate the SPAI in the fourth modeling phase is applied to the organizational decision-making process. Similar to the KDDM process, the proposed steps are iterative, and moving back and forth between steps are desirable and encouraged. In the following section, we detail each step of the proposed utilization-based framework.

## 5.2 Utilization-based Framework Description

## Step 1: Population and contextual Characteristics Evaluation

As discussed previously, the BM provides a theoretical foundation for evaluating different individual and contextual factors that can be used to explain healthcare access. For example, at the individual level, many studies have found age to have a significant association with healthcare utilizati [6], where olde peopl are more likely to visit PCPs but less likely to ntextual level, a community that is populated primarily by older persons might need a different composition of health services and facilities from one where the majority of residents are younger parents and children.

While the BM provides a set of variables that can be used to measure spatial accessibility, their inclusion should be based on whether they are pertinent to the business objectives, as well as the availability of data sources. For example, individual social determinants, such as an individual’s education, occupation, and social interactions, are important predisposing determinants of utilization. However, those data might not be available in the organization. Thus, it is important to involve both DMs and data experts when creating a representative set of

# ACCEPTED MANUSCRIPT

variables. Furthermore, business domain knowledge could help formulate business rules for data transformation and aggregation. Because BM characteristics are categorical and the goal of utilization-based method is to differentiate the population subgroups that have different health needs, the utilization-based method requires all continuous inputs that characterize these subgroups to be discretized. The discretization can be based on business domain knowledge (e.g., how to group people of different ages) or statistics distributions (e.g., optimal binning method). The output of this step includes an initial report on required project such as where the data would be sourced, who would be the key personnel (e.g., perts, data experts, analytical experts), and what would be the required hardware and software resources (e.g., computing environment and analytical tools). The report should also include a set of business rules for data preparation needs.

## Step 2: Data Preparation

The first task in this step is to gain access to all relevant data sources identified in step 1. In an organizational environment, the data sources may reside in different locations. Data would then need to be extracted, transformed, cleaned, and integrated. Furthermore, individual utilization data need to be aggregated to the contextual unit level desired for predictive modeling based on the business requirements from step 1. For example, if the business objective is to analyze the accessibility for different communities, the granularity of the final dataset should be at the community level. Hence, a data preparation plan is needed to describe the process of extracting, transforming, cleaning, and aggregating data into a format suitable for predictive modeling and SPAI calculation. This plan should include locations of data elements, data understanding tasks required before and after data integration, data transformation steps, data quality requirements, and modeling requirements [23]. In addition, the plan should include how to create actual spatial access measures.

The second task is to prepare data based on the data preparation plan. This process is iterative, and going back to the previous step to re-evaluate variable selection and discretization rules may be necessary. For example, if an input variable is found to have a minority class (e.g., less than 1% of the total population), the discretization rule for this variable should be changed or some other variables should be selected. The output of this step is the final dataset for predictive modeling. It should include the revealed access as the target variable and aggregated individual and contextual characteristics as input variables.

## Step 3: Predictive Modeling for Weights Determination

The main purpose of this step is to determine weights for the different healthcare utilization needs of various population subgroups, the outputs of which will be used in Ste to calculate the SPAI. In the traditional FCA method, both population (demand) and health service providers (supply) are assumed to be homogeneous. The main challeng is how to empirically determine the different healthcare needs based on non-spatial population characteristics. For example, various study reported women were more likely to visit a physician than men [2, 9]. However, no integrative approach has been proposed to determin e relative weights for utilization propensity between male and female. Therefore, we propose the use of predictive modeling to discover real healthcare utilization patterns and then determine demand weights among different population subgroups (e.g., the female subgroup usually has a higher healthcare need than the male subgroup). Selecting an appropriate modeling technique is essential for meaningful results. Because the main purpose of predictive modeling is to determine variable weights, explanatory modeling techniques is desired. The relative weights among different classes of an input variable can be inferred using odds ratio [43], which can be obtained through association rules [44] or logistics regression. For example, in logistic regression, odds ratio can present the odds of occurrence of the target outcome given a particular case of input variable.

On the other hand, different population characteristics or factors could have a different impact on overall population needs. For example, age might have a larger impact on the overall healthcare demand than ethnicity. In such cases, the relative weight for each non-spatial factor can be obtained through a variable importance evaluation function using analytical techniques such as decision trees or clustering analysis. For example, in the decision tree growth phase, variable selection occurs in the recursive node splitting process based on maximum impurity reduction. The decision on selecting a specific variable to split indicates the relative importance of that variable [8]. The outputs from this step include a set of weights for each factor of categorical input variables (categorical weights) and relative weights among population or provider characteristics (factor weights).

## Step 4: Calculate Spatial Healthcare Accessibility

In this step, a utilization-based algorithm is used to measure the spatial healthcare accessibility. The algorithm integrates weighted population characteristics with those in the FCA method family. The unit of analysis for the catchment area should be based on the desired contextual unit level, which can be the census block group (BG), census tract, zip code, or even the community level. Below, we modify the G2SFCA model [50] to create the utilization-based healthcare accessibility algorithm. First, for each provider location $j ,$ search all population locations k that are within threshold travel tim (d<sub>0</sub>) from the location $j ,$ and compute the utilization-based provider to population ratio $R _ { j }$ within the catchment area using a distance decay function f (d):

$$
R _ {j} = \frac {S _ {j}}{\sum_ {k = 1} ^ {m} W _ {f l} W _ {l g} P _ {k l g} f (d _ {k j})}\tag{1}
$$

where $S _ { j }$ is the number of providers at location $j ,$ m is the total number of population locations; $P _ { k I g }$ is the population of subgroup g for the factor l (e.g., female subgroup for the gender factor) of the location k whose centroid falls within the catchment threshold; $W _ { I g }$ is the categorical weight of each subgroup g within the factor $I _ { \ l }$ and $W _ { f I }$ is factor weight of the factor l; $d _ { k j }$ is the actual travel time between k and $j ;$

Next, for each population location i, search all physician locations j that are within the threshold of travel time (d<sub>0</sub>) from location (i.e., catchment area i), and sum up the provider to population ratio $R j$ at these locations using the distance decay function f (d):

$$
A _ {i} = \sum_ {j = 1} ^ {n} R _ {j} f (d _ {i j}) = \sum_ {j = 1} ^ {n} \frac {S _ {j} f (d _ {i j})}{\sum_ {k = 1} ^ {m} W _ {f l} W _ {l g} P _ {k l g} f (d _ {k j})}\tag{2}
$$

where $A _ { i }$ represents the accessibility index at location i based on the utilization-based SPAI algorithm; n is the total number of locations of the physician; $R _ { j }$ is the physician-to-population ratio at the physician location j whose centroid falls within the catchment centered at i; and $d _ { i j }$ is the actual travel time between i and j. A larger value of $A _ { i }$ indicates a better accessibility at a location.

## 5.3 Case Study

As mentioned in the case study background (section 4), the business objective of the SCR was to strategically place more PCPs in shortage areas. The organization was also interested in understanding how different member utilization. Such an understanding would allow the effective expansion of SCR’s provider network to serve more members. Business knowledge of the case study furnished by two senior directors who were domain experts and a senior data analyst who was the data expert. The domain experts were interested in the process showed in the framework, as commented by a senior director: “I virtual machine with tools such as the SQL Server (to access the data warehouse), ArcGIS Suite, Python, SAS, and R to perform steps in this section. SCR members’ utilization data were at the individual level, though all identifiable personal information was removed in compliance with privacy and regulatory requirements.

## 5.3.1 Population and Contextual Characteristics Evaluation

Based on the stated business objective, existing data sources were first reviewed to identify member and PCP characteristics. The data warehouse included member characteristics data, such as gender, age, ethnicity, language spoken, address, plan type, and payment type. Members were connected to their PCPs through the enrollment fact table. The data warehouse also contained PCP characteristics, for instance, demographics (e.g., ethnicity, gender, age), primary specialty, location, and office hours. Because the domain experts expressed the interest to assess the spatial accessibility at the lowest possible granularity level, we decided to measure contextual characteristics at the BG level. Guided by the BM, we consulted the domain experts to identify potential data sources that were currently not available in the data warehouse for individual and contextual determinants such as income, employment, and educational levels. However, due to the privacy restrictions and organizational constraints, these were not available at the time of the analysis. Though the domain experts preferred to u existing data for analysis, they were aware that these additional factors could improve the population and contextual characteristics assessment in future iterations.

The next task is to determine healthcare access measures. PCP utilization can be measured using medical claims or encounters, which can be either PCP office visits or the number of diagnoses from a PCP. Office visit is n important measure in preventive care, because without the office visit, members do not receive counseling on diet, exercises, smoking, and other risky health behaviors. After reviewing potential PCP utilization measures, the domain experts expressed the ir interests in understanding one of the key access measures at SCR: the percentage of mem had a preventive care visit per year. This meant that a “having r would have made at least one PCP visit during the plan year. Hence, the target variable, Access, was transformed to “Yes” or “No”, where “Yes” meant a member had at least One PCP visit in a year.

Since the case study started in early 2016, we selected 2015 utilization data for analysis, giving us a whole year of member utilization. Furthermore, based on suggestions by the domain experts, we limited members to adults (i.e., 18 years or older) who were active in 2015. In total, our data included approximately 730,000 members. Before deciding final variables and transformation rules for predictive modeling, we proceeded to the data preparation step to create an initial member PCP utilization dataset.

# ACCEPTED MANUSCRIPT

After the initial data investigation, we included the following population and contextual characteristics of members: gender, age, ethnicity, and primary language spoken. PCP characteristics were dropped due to insignificant correlations with the target variable, Access. The variable Payment Types was also excluded because it contained a minority class that was less than five percent of the overall observations. Among these selected variables, a transformation rule for Age was created based on th experts’ 0 inputs. It included four age groups: Group One (between 18 and 29), Group etween 30 and 44), Group Three (between 45 and 64), and Group Four (65 above). Language Spoken variable had a total of 30 classes, which were grouped into three categories: English, Spanish, and Other Non-English. Moreover, the Ethnicity dimensions were reduced from 18 to five categories: White, Black, Hispanic, Asian, and Other.

## 5.3.2 Data Preparation

Due to page limit constraints, we do not present all tasks and iterations performed related data transformation, cleaning, and aggregation. Instead, we elaborate on main activities in this stage. The first activity was creating a unique set of PCP and member pairs (approximately 1.9 million pairs) using the enrollment data, and then performing a left join with the claim table to obtain the number of PCP visits. If a member and PCP pair did not appear in the claim table, it meant that the member did not visit the PCP in 2015. All member-related characteristics were transformed based on the transformation rules described in the previous step. We utilized the Origin-Destination (OD) Matrix [54] to calculate pairwise travel time between members and PCPs using the member’s BG centroids and PCP locations as origins and destinations, respectively. Any travel time more than 60 minutes was considered as out of area assignments and removed. This resulted in a total of 734,504 observations at the BG level. To assign each member’s locations into their respective BGs, a spatial join was performed. Subsequently, the BG-PCP OD Matrix results were integrated with member data as the actual travel time between the PCP and member pair. This step was necessary to anonymize members’ locations and also provided actual travel time to be used later. The actual travel time was discretized into two categories using the optimal binning method: low (between 0 and 15 minutes) and high (15 minutes and above), as the data dictated.

Figure 3 depicts SCR’s member characteristics. The Ethnicity variable distribution was similar to that of the general population characteristics of the region. This may be attributed to the fact that all SCR’s members are eligible for Medicare, a US federal gov rnment program that provides healthcare coverage for seniors and people with disability, and Medicaid, a U.S. federal government program that offers healthcare for low income population subgroups. As a result, people who are enrolled in Medicare and Medicaid could also be identified as socially disadvantaged groups for healthcare access. Because Ethnicity had a sizable “missing” data, tree imputation method was used to replace these missing values. This replacement technique is usually more accurate than other imputation meth ods such as variable distribution, because the replacement value of tree imputation is based on other input variables.

![](/api/attachments/R6RK6TS7/fulltext/images/bcd4d7baa640ce5a917e85634ac5da588254a28d11796e0b5fd25a737298e0d2.jpg)  
Figure 3: Summary statistics of input variables

The cleaned and transformed dataset was further aggregated to the BG level using their Federal Information Processing Standard (FIP) codes. The aggregated dataset included total 93,725 observations and 2,228 unique BGs. The utilization at the BG level was measured as Average Visit, which was the total number of visits by individuals divided by the total population of the BG. The target variable, Access, could be transformed in several ways. The final transformation rule for the target variable was based on the statistical analysis of Average Visit distribution and the domain experts’ feedback. The rule was: if Average Visit is greater or equal

0.5, Access equals to “Yes”, otherwise, Access equals to “No”. The rule generated the target event, “Yes”, which was about 28% of the total observations in the final dataset.

## 5.3.3 Predictive Modeling

As described earlier, the objective of the predictive modeling is to determine weights for healthcare needs of different population subgroups. To do so, we first used logistic regression to determine the relative weights within each population subgroup. The model passed linearity test of logit (no significant interactions between input variables) and multicollinearity (all Variance Inflation Factors were close to 1). All inputs variables, except for the E nicity Group “Black” and the transformed Travel Time, were statistically significant. The logistic regression provided the odds ratio estimates (Figure 4) for the main effect in the model, which could be interpreted as the relative weights for each subgro or example, for subgroup, the odds of seeing a PCP is 1.69 times larger n the male subgr e group 4 (65 or older) has more than four times the possibility to see a PC group 1 (between 18 and 30). Overall, the odds ratio estimates were consistent with literature findings.

![](/api/attachments/R6RK6TS7/fulltext/images/5cf1468f67830cc924a7833ae78ad0b40ac567806accd99270980cd4372c26f8.jpg)  
Figure 4: Odds Ratio estimates for main effect

Our next step was to find the factor weights among input variables. We ran decision trees using 70% training and 30% validation with a leaf size of 285 to avoid overfitting. Travel time was not included in the final decision tree modeling, because the tree did not select the Travel Time to split, meaning Travel Time had no predictive power for Access. The decision tree result confirmed the logistic regression results, where the association between Travel Time and Access was not significant. This finding was unexpected, as it was in contradiction to the assumption that spatial separation between the population and healthcare provider is a key factor towards accessibility [51]. With only four input variables, the best decision tree model achieved an accuracy of 73.4%. This would be considered high, because many other known factors associated with the utilization were not captured in the modeling dataset. In addition, the lift value was 2.63, signifying that the model predicted 2.63 times better than a random guess 0 0.2916, 0.2492, and 0.2086 for Age Group, Gender, Language, and Ethnicity, respectively.

![](/api/attachments/R6RK6TS7/fulltext/images/f296e582a2fe80be8a6b8a0c55ea2e7f3d70889e883e8e89d7c84c380c6502c9.jpg)  
Figure 5: Variable Importance

## 5.3.4 Calculating Spatial Accessibility

In this step, we integrated the weights of different population characteristics to calculate the SPAI for each BG. First, each odds ratio in Figure 4 was normalized. Because one of the future plans was to integrate factors such as education and income levels from the census data into existing population characteristics, total population for each of these factors (i.e., sum of female and male population for gender factor) should be the same as the total population for each BG. Thus, given the total population $\mathsf { P } _ { k }$ for each contextual unit k, and for a factor l with g categories (subgroups),

$$
P _ {k} = P _ {k l} = \sum_ {i = 1} ^ {g} p _ {l i}\tag{3}
$$

where $P _ { k I }$ is the total population of the l factor, and $\mathsf { P } _ { I I }$ is each subgroup population for l. This means each category is given an equal weight of 1. Thus, the normalized score for each factor equals n. For example, based on the odds ratios in Figure 4, the categorical weights for Age Group were normalized to 0.301, 0.624, 1.845, and 1.230, respectively. Secondly, the combined factor variable normalized score equals one. Based on the variable importance score in Figure 5, the normalized weights for Age Group, Gender, Language, and Ethnicity were transformed to 0.553, 0.169, 0.163, and 0.115, respectively.

In order to calculate the SPAI, we first need to determine the distance decay function f (d) in Eq. (1) and (2). Because Travel Time was not a significant predictor for Access, continuous or hybrid distance decay functions were not relevant. Hence, we implemented the utilization-based algorithm using the distance decay function as a dichotomous measure of accessible or inaccessible by a cutoff distance $\mathsf { d } _ { O } ,$ which is essentially the 2SFCA method. Thus, the spatial accessibility index $A _ { i }$ for each BG was calculated based on Eq. (4),

$$
A _ {i} = \sum_ {j \in (d _ {i j} \leq d _ {0})} R _ {j} = \sum_ {j \in (d _ {i j} \leq d _ {0})} (\frac {S _ {j}}{\sum_ {k \epsilon (d _ {k j} \leq d _ {0})} W _ {f l} W _ {l g} P _ {k l g}})\tag{4}
$$

where $R _ { j }$ is the physician-to-population ratio at the physician location j whose centroid falls within the catchment centered at i; $d _ { i j }$ is the travel time between i and j. Finally, the result of the utilization-based method was instantiated using ESRI’s ArcGIS Suite. A visual comparative evaluation of $A _ { i }$ output using the utilization-based method and the traditional 2SFCA method is demonstrated in the next section.

## 5.4 Evaluation of the Utilization-based Spatial Accessibility Index Algorithm

For this comparative evaluation, we first created two maps: one using our utilization-based healthcare accessibility algorithm and one using the traditional 2SFCA algorithm. Both maps used the data from our case study. Additionally, we generated a map using the traditional 2SFCA algorithm but with the census tract population data and provider utilization data provided by the Center for Medicare and Medicaid Services. All three maps use 30 minutes as the travel time thresholds for evaluation purpose.

The utilization-based healthcare accessibility map (Figure 6) showed that areas with higher SPAI (better spatial access) were concentrated in urban areas (e.g., Rancho Cucamonga, Riverside, Sun City, Palm Springs), whereas lower accessibility areas were mostly rural areas.

![](/api/attachments/R6RK6TS7/fulltext/images/98a87485e156c0b0a9e5e7930d3a16d10a0db09a095268b1991e8d25ff2a2dfa.jpg)  
Figure 6: Utilization-based healthcare accessibility map

Furthermore, lower population density areas, such as Palm Springs, Yucca Valley, and Big Bear Lake, had higher accessibility scores than higher population density areas such as Moreno Valley and Redlands. This may be attributed to the strong presence of SCR provider networks in these low population density areas with less competition from other healthcare plan providers.

In contrast, the map created using the traditional 2SFCA method (Figure 7) exhibited some notable differences. However, many low accessibility areas remained the same. For example, Lenwood, Barstow, and Hinkley area were scored with poor spatial accessibility using our utilization-based accessibility algorithm. SCR confirmed that these areas had a lower ratio of PCPs and its members. However, the 2SFCA method showed these areas as having medium accessibility. A closer look at these areas revealed that they had a high percentage of older population (a ge 45 years or older). Generally, these age groups have relatively higher 1 healthcare needs. However, this observation revealed the inability of the traditional 2SFCA method in considering distinctive healthcare needs among different population subgroups. Hence, although using the same population-to-provider data, the utilization-based method uncovered these PCP shortage areas while the traditional 2SFCA method was unable to point out the deficiencies.

![](/api/attachments/R6RK6TS7/fulltext/images/7a71760719a7204e90e86a0bc92b8ad3cbc9577610963510ad9142a649960d50.jpg)  
Figure 7: 2SFCA healthcare accessibility map for SCR

The second analysis focused on comparing healthcare accessibility measures between SCR members (Figure 6) and the overall population (Figure 8). As discussed previously, SCR population characteristics were quite different from that of the general population because SCR members were mostly recipients of Medicare and Medicaid benefits. Hence, we use relative rank in sextiles) to compare the result. Among several interesting findings, the areas that were northeast of Sedco Hills and the surroundings of Canyon Lake required the most attention. These areas were identified as PCP shortage areas using our utilization-based method while the traditional 2SFCA method indicated that these areas had medium accessibility. One possible explanation is that, although PCP resources for the overall population in these areas were acceptable, SCR did not have sufficient PCP providers within their network to meet the demand. Thus, the result provided valuable feedback to SCR’s resource planning team to proactively recruit PCPs in these areas who would accept their monthly reimbursement, or capitated rates. Another interesting finding was that, one BG in an identified shortage area belonged to a census block where all other BGs had moderate SPAI. This finding highlights the importance of selecting the right unit of analysis in measuring spatial accessibility

## ACCEPTED MANUSCRIPT

![](/api/attachments/R6RK6TS7/fulltext/images/da2e8c99c39ea929095515b85f34672614877817d9a282635d2104a26a62d11b.jpg)  
Figure 8: 2SFCA healthcare accessibility map using census data

We further conducted a correlation analysis and a t-test to compare our utilization-based algorithm with the traditional 2SFCA method, similar to tudies [7, 35, 49]. Using the same utilization data, we calculated one utilization one 2SFCA-based SPAI for each BG. The Pearson’s correlation coefficient showed a strong correlation between the utilization-based SPAI and the 2SFCA-based SPAI (r=0.54, p-value <0.001). However, the t-test confirmed that they were statistically ifferent (statistic=36.92, p-value <0.001). The scatterplot (Figure 9) indicated that there were overestimation and underestimation issues at certain BGs. The lack of the benchmark for estimation errors is an ongoing methodological concern in the FCA method family. One possible approach is to create a revealed accessibility index from utilization data as a benchmark. While this is out of scope of this research, additional field studies could be carried out to test and confirm a rigorous revealed access benchmark measure. To that end, we urge future research to heed this call to enrich the knowledge base of the FCA method family.

![](/api/attachments/R6RK6TS7/fulltext/images/f04db4531ec2e9c1d38f426aa2a8c130c728d71054b9b47d936f8a3c188db029.jpg)  
Figure 9: Scatter Plot of Utilization-based SPAI vs 2SFCA-based SPAI

## 6. A SDSS for Utilization-based Healthcare Accessibility Assessment

In this section, we present the implementation of our utilization-based framework in a SDSS. Model Builder in ArcGIS for backend geoprocessing, and JavaScript plus HTML5 for f nd web application development. Model Builder is a visual programming tool for building, automating, and documenting geoprocessing SDSS was quite complex and contained voluminous model elements. Fo r simplicity of presentation, we present a parsimonious view of the geoprocessing workflow of our system, as depicted in Figure 10.

![](/api/attachments/R6RK6TS7/fulltext/images/bc2feb743929b06f509474fb010870343414ac4e25bf1c272587e5646a796ea8.jpg)  
Figure 10: Geoprocessing workflow of the SDSS

## ACCEPTED MANUSCRIPT

The workflow starts with inputs of weighted population data based on the contextual characteristics. The input data also include BG centroids that are calculated using the Featureto-Point tool in ArcGIS. Following the input data, the geoprocessing tool, Recalculate Field, is used to modify the underlying input data (e.g., subgroup population distribution, categorical weights, or factor weights) based on specific use cases. The SDSS then automatically recalculates the weighted population and population centroids, are then aggregated via a spatial join with providers’ travel time polygons. Spatial utputs are then joined with the provider locations (with difference capabilities for each location). Consequently, the supply index is created where each provider has a utilization-based provider to population ratio. This corresponds to the first step of the utilization-based healthcare accessibility index algorithm, as shown in Eq. (1). To model the second step of the algorithm, provider locations with the supply index (i.e., utilization-based provider population ratio) is spatially joined with the population BG travel time polygons. The spatial join cumulates supplier indices for each BG and creates the utilization-based SPAI. Finally, the output data is transferred into the BG polygons and the accessibility indices are visually displayed in a map.

Ideally, DMs should be able to explore the identified shortage areas in the map and interactively change input variables (such as contextual characteristics, categorical weights, or factor weights) to gauge their effects on the outputs. This would give DMs insights on how to allocate resources based on location, supply, and demand. However, the categorical and factor weights for our utilization-based SPAI are modeled based on real healthcare utilization patterns and therefore, they should not be changed by DMs. Hence, in our SDSS implementation, we opted to allow only contextual characteristics to be modifiable. Figure 11 presents a screenshot of the SDSS web interface, where the right-side panel displays the spatial accessibility map, and the left-side panel allows DMs to select different decision scenarios. Although the SDSS was designed for the regional health plan as a test case, the tool may be adapted to different

# ACCEPTED MANUSCRIPT

regions and different health organizations (private or public), with additional contextual characteristics.

![](/api/attachments/R6RK6TS7/fulltext/images/450b482efe720c41db232b40453cb1683c5d5bb6227e7d4e6c826519856a03b9.jpg)  
Figure 11: Web Interface of GDSS (Utilization-based accessibility map using only Gender factor)

We now demonstrate the utility and practicality of the SDSS using the following scenario: given the identified PCP shortage areas, DMs want to see if Gender is a potential influence factor. DMs can select Gender, after which the Model Builder will automatically assign 0s to all other factor weights and display an accessibility map based on Gender only (Figure 11). If PCP shortage areas do not change, it would mean that Gender does not have a significant impact on these hortage areas. th er hand, if the SPAI changes significantly, the underlying Gender may be important factor for the demand in these areas. In the case of SCR, previously identified PCP shortage areas, such as Lenwood, Barstow, and Hinkley, were considered to have moderate accessibility when considering Gender as the only factor.

# ACCEPTED MANUSCRIPT

## 7. Research Implications and Limitations

This research has implications for both theory and practices. From a theoretical perspective, it bridges the theoretical gap between quantitative spatial accessibility research and surveybased healthcare access studies. Our proposed framework not only demonstrates how the BM can inform the selection and evaluation of non-spatial factors for spatial access, but also contributes to the general deductive survey-based BM research by introducing inductive pattern discovery of healthcare access behaviors. In addition, the framework design ided by the theoretical foundations from KDDM, and yet integrated within the F family. By appropriately applying existing theories, methodologies, and methods from interdisciplinary knowledge bases, our research contributes to the theoretical knowledge upon which DSR artifacts are developed and built. More importantly, our stud how DSR benefits from the rich body of literature, and how it reciprocates by con ibuting to the scientific knowledge [23].

In addition to solving real-world business problems, this research has other practical implications. First, our utilization-based framework is designed as a common structure to communicate the spatial analytic solutions to business users. It not only enables DMs to understand the analytical process carried out by the researchers, but also is usable by policy interested in exploring relationships between population characteristics and healthcare access. Second, we present a novel approach of deriving categorical and factor weights through predictive modeling. This approach may be adopted by other analytics practitioners who attempt to create multiple-attribute weights inductively. Third, the SDSS tool is designed with embedded geoprocessing workflow for SPAI calculation, which can be adopted by various public or private health organizations.

This study is not without limitations. First, since the boundary is not defined by a geographical extent, it is possible that edge effect might be observed and may skew the results. However, the edge effect in our case study can be minimal. This claim is justifiable by the nature of SCR’s business practice: an overwhelming majority of SCR members reside in two counties: San Bernardino and Riverside. As a result, the edge effect is deemed to be mimic that of the regional geographical extent since SCR’s business practice does not concern other geographic areas. Thus, although there may be some unavoidable amount of edge effects in the study, they would not substantially influence the results to the extent that it may be uninterpretable.

Additionally, we realize that the case study is only an initial attempt toward a comprehensive spatial accessibility measurement. Due to the da SCR, socioeconomic data were not included. Nevertheless, our framework pr vides conceptual structure where additional factors and categorical weights associated with socioeconomic characteristics can be added to calculate the SPAI. Similarly, we did not explore the characteristics related to healthcare ser h will integrate provider characteristics, such as service quality, within the FCA method family. Furthermore, our focus in this research pertained only to PCPs. Future researc expand to other healthcare services entities such as hospitals, specialists, and home care.

Another limitation is related to the inclusion of distance decay functions and multi-modal transportation when calculating the SPAI index [25, 28, 33]. Researchers should also be wary of multi-dimensional data integration, as it could be computational costly and less intuitive to interpret [51]. Moreover, an optimal distance decay function may require additional data to be defined and may be regional specific [53]. For example, our case study concluded a binary function for distance decay because the travel time was tested with no significant effect on healthcare access. This is an interesting finding that merits further investigation. If travel time had no significant effect on realized access, we should re-examine travel time assumptions of the FCA methods. In this study, OD Matrix was employed to measure the actual travel time pairwise between BGs and PCPs. Our initial data exploration postulated that the median actual travel time varies from 12 to 14 minutes, depending on population characteristics. As a result, further inquiries regarding the interplay between travel times and healthcare utilization will be beneficial to healthcare spatial accessibility research.

## 8. Conclusion

Improving healthcare accessibility could aid in reducing health expenditures, increasing healthcare equality, and improving health outcomes. Through our research, we designed a novel utilization-based framework for measuring health pra l SDSS instantiation that is rooted in theoretical concepts of M and existing ds. We presented a unique approach to derive weights of opulation charac employing predictive analytics using real utilization data. The evaluation espoused the need for integrating non-spatial factors within existing algorithms in deriving the SPAI. The findings should encourage future research to further explore how populati haracteristics may shape the demand for healthcare. Our research achieves rigor by applying DSR methodology and utilizing knowledge foundations of healthcare accessibility literature, BM, KDDM, and GIS, while it maintains relevance by addressing real organizational needs.

## References:

[1] L.A. Aday, R. Andersen, A framework for the study of access to medical care, Health services research, 9 (1974) 208-220.

[2] J. Afilalo, A. Marinovich, M. Afilalo, A. Colacone, R. Leger, B. Unger, C. Giguere, Nonurgent emergency department patient characteristics and barriers to primary care, Academic Emergency Medicine, 11 (2004) 1302-1310.

[3] R.M. Andersen, Revisiting the behavioral model and access to medical care: does it matter?, Journal of health and social behavior, 36 (1995) 1-10.

[4] R.M. Andersen, P.L. Davidson, S. Baumeister, Improving access to care in America, 3rd ed., Jossey-Bass, San Francisco, 2007.

[5] R.M. Andersen, H. Yu, R. Wyn, P.L. Davidson, E.R. Brown, S. Teleki, Access to medical care for low-income persons: how do communities make a difference?, Medical care research and review, 59 (2002) 384-411.

[6] B. Babitsch, D. Gohl, T. von Lengerke, Re-revisiting Andersen’s Behavioral Model of Health Services Use: a systematic review of studies from 1998–2011, GMS Psycho-Social-Medicine, 9 (2012).

[7] J. Bauer, D.A. Groneberg, Measuring spatial accessibility of health care providers–introduction of a variable distance decay function within the floating catchment area (FCA) method, PloS one, 11 (2016) e0159148.

[8] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and regression trees. , Wadsworth & Brooks, Monterey, CA, 1984.

[9] R.W. Broyles, W.J. McAuley, D. Baird-Holmes, The medically vulnerable: their health risks, health status, and use of physician care, Journal of health care for the poor and underserved, 10 (1999) 186-200.

## ACCEPTED MANUSCRIPT

[10] T.-A. Chiang, Z. Che, A decision-making methodology for low-carbon electronic product design, Decision Support Systems, 71 (2015) 1-13.

[11] A.G. de Boer, W. Wijker, H.C. de Haes, Predictors of health care utilization in the chronically ill: a review of the literature, Health Policy, 42 (1997) 101-115.

[12] P.L. Delamater, Spatial accessibility in suboptimally configured health care systems: A modified two-step floating catchment area (M2SFCA) metric, Health & Place, 24 (2013) 30-43.

[13] P.J. Densham, Spatial decision support systems, in: D.J. Maguire, M.F. Goodchild, D.W. Rhind (Eds.) Geographical information systems: Principles and applications, John Wiley & Sons, Inc., New York, 1991, pp. 403-412.

[14] S.S. Dhingra, M. Zack, T. Strine, W.S. Pearson, L. Balluz, Determining prevalence and correlates of psychiatric treatment with Andersen's behavioral model of health services use, Psychiatric Services, 61 (2010) 524-528.

[15] U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, The KDD process for extracting useful knowledge from volumes of data, Communications of the ACM, 39 (1996) 27-34.

[16] F. Gao, W. Kihal, N. Le Meur, M. Souris, S. Deguen, Assessment of the spatial accessibility to health professionals at French census block level, International Journal for Equity in Health, 15 (2016) 125.

[17] M. Gulliford, J. Figueroa-Munoz, M. Morgan, D. Hughes, B. Gibson, R. Beech, M. Hudson, What does' access to health care'mean?, Journal of health services research & policy, 7 (2002) 186-188.

[18] A.R. Hevner, S.T. March, J. Park, Design science in information systems research, MIS Quarterly, 28 (2004) 75-105.

[19] G. Higgs, The role of GIS for health utilization studies: literature review, Health Services and Outcomes Research Methodology, 9 (2009) 84-99.

[20] G. Kadushin, Home health care utilization: a review of the research for social work, Health & social work, 29 (2004) 219-244.

[21] D.B. Kell, S.G. Oliver, Here is the evidence, now what is the hypothesis? The complementary roles of inductive and hypothesis‐driven science in the post‐genomic era, Bioessays, 26 (2004) 99-105.

estimation and temporal price prediction: The hotel brokers' context, Decision Support Systems, 54 (2013) 1119-1133.

[23] Y. Li, M.A. Thomas, K.-M. Osei-Bryson, A snail shell process model for knowledge discovery via data analytics, Decision Support Systems, 91 (2016) 1-12.

[24] J. Luo, Integrating the Huff Model and Floating Catchment Area Methods to Analyze Spatial Access to Healthcare Services, Transactions in GIS, 18 (2014) 436-448.

[25] W. Luo, Y. Qi, An enhanced two-step floating catchment area (E2SFCA) method for measuring spatial accessibility to primary care physicians, Health & Place, 15 (2009) 1100-1107.

[26] W. Luo, F. Wang, Measures of spatial accessibility to health care in a GIS environment: synthesis and a case study in the Chicago region, Environment and Planning B: Planning and Design, 30 (2003) 865-884.

[27] W. Luo, T. Whippo, Variable catchment sizes for the two-step floating catchment area (2SFCA) method, Health & Place, 18 (2012) 789-795.

[28] L. Mao, D. Nekorchuk, Measuring spatial accessibility to healthcare for populations with multiple transportation modes, Health & place, 24 (2013) 115-122.

[29] Ó. Marbán, G. Mariscal, E. Menasalvas, J. Segovia, An engineering approach to data mining projects, in: H. Yin, P. Tino, E. Corchado, W. Byrne, X. Yao (Eds.) Intelligent Data Engineering and Automated Learning - IDEAL 2007, Springer Berlin, Heidelberg, 2007, pp. 578-588.

[30] J. McCusker, I. Karp, S. Cardin, P. Durand, J. Morin, Determinants of emergency department visits by older adults: a systematic review, Academic Emergency Medicine, 10 (2003) 1362-1370.

[31] M.R. McGrail, Spatial accessibility of primary health care utilising the two step floating catchment area method: an assessment of recent improvements, International Journal of Health Geographics, 11 (2012) 50.

[32] M.R. McGrail, J.S. Humphreys, The index of rural access: an innovative integrated approach for measuring primary care access, BMC Health Services Research, 9 (2009) 124.

[33] M.R. McGrail, J.S. Humphreys, Measuring spatial accessibility to primary health care services: Utilising dynamic catchment sizes, Applied Geography, 54 (2014) 182-188.

[34] L.R. Mobley, T.-M. Kuo, M. Urato, S. Subramanian, L. Watson, L. Anselin, Spatial Heterogeneity in Cancer Control Planning and Cancer Screening Behavior, Annals of the Association of American Geographers. Association of American Geographers, 102 (2012) 1113-1124.

[35] A.N. Ngui, P. Apparicio, Optimizing the two-step floating catchment area method for measuring spatial accessibility to medical clinics in Montreal, BMC Health Services Research, 11 (2011) 166.

[36] B. Obama, United states health care reform: Progress to date and next steps, JAMA, 316 (2016) 525- 532.

[37] M. Plachkinova, A. Vo, R. Bhaskar, B. Hilton, A conceptual framework for quality healthcare accessibility: a scalable approach for big data technologies, Information Systems Frontiers, DOI 10.1007/s10796-016-9726-y(2016) 1-14.

[38] J. Radke, L. Mu, Spatial decompositions, modeling and mapping service regions to predict access to social programs, Geographic Information Sciences, 6 (2000) 105-112.

[39] J.J. Ray, A web-based spatial decision support system optimizes routes for oversize/overweight vehicles in Delaware, Decision Support Systems, 43 (2007) 1171-1185.

[40] N. Schuurman, M. Berube, V.A. Crooks, Measuring potential spatial access to primary health care physicians using a modified gravity model, The Canadian Geographer/Le Geographe Canadien, 54 (2010) 29-45.

[41] C. Shearer, The CRISP-DM model: the new blueprint for data mining, Journal of Data Warehousing, 5 (2000) 13-22.

[42] M. Siegel, D. Koller, V. Vogt, L. Sundmacher, Developing a composite index of spatial accessibility across different health care sectors: A German example, Health Policy, 120 (2016) 205-212.

[43] M. Szumilas, Explaining Odds Ratios, Journal of the Canadian Academy of Child and Adolescent Psychiatry, 19 (2010) 227-229.

[44] P.-N. Tan, V. Kumar, J. Srivastava, Selecting the right interestingness measure for association patterns, Proceedings of the eighth ACM SIGKDD international conference on Knowledge discovery and data mining, ACM, Edmonton, Alberta, Canada, 2002, pp. 32-41.

[45] The Health Resources and Services Administration, Type of Shortage Designations, Retrieved March 13, 2017, from https://bhw.hrsa.gov/shortage-designation/types

[46] A. Vo, M. Plachkinova, R. Bhaskar, Assessing healthcare accessibility algorithms: A comprehensive investigation of two-step floating catchment methodologies family, Twenty-first Americas Conference on Information Systems, Puerto Rico, 2015.

[47] N. Wan, F.B. Zhan, Y. Lu, J.P. Tiefenbacher, Access to healthcare and disparities in colorectal cancer survival in Texas, Health & place, 18 (2012) 321-329.

[48] N. Wan, F.B. Zhan, B. Zou, E. Chow, A relative spatial access assessment approach for analyzing potential spatial access to colorectal cancer services in Texas, Applied Geography, 32 (2012) 291-299.

[49] N. Wan, B. Zou, T. Sternberg, A three-step floating catchment area method for analyzing spatial access to health services, International Journal of Geographical Information Science, 26 (2012) 1073- 1089.

[50] F. Wang, Measurement, optimization, and impact of health care accessibility: a methodological review, Annals of the Association of American Geographers, 102 (2012) 1104-1112.

[51] F. Wang, GIS-based measures of spatial accessibility and application in examining health care access,

in: F. Wang (Ed.) Quantitative Methods and Socio-Economic Applications in GIS, CRC Press, Boca Raton, FL, 2014, pp. 93-113.

[52] F. Wang, W. Luo, Assessing spatial and nonspatial factors for healthcare access: towards an integrated approach to defining health professional shortage areas, Health & Place, 11 (2005) 131-146.

[53] L. Wang, T. Tormala, Integrating spatial and aspatial factors in measuring accessibility to primary health care physicians: a case study of Aboriginal population in Sudbury, Canada, J Community Med Health Educ, 4 (2014) 2161-0711.1000284.

[54] H. Yang, Heuristic algorithms for the bilevel origin-destination matrix estimation problem, Transportation Research Part B: Methodological, 29 (1995) 231-242.

# ACCEPTED MANUSCRIPT

Yan Li is an Assistant professor at Center for Information Systems and Technology, Claremont Graduate University. Driven by her intellectual curiosity for data and emergent information technologies, and her passion for designing and building things, she has oriented her career in the direction that integrates research, teaching, and practice in the realm of information science. Her research focuses on data and knowledge management areas such as data mining, data warehousing, and semantic technologies with an emphasis on exploring the synergies between information systems and data analytics. Her other research stream focuses on developing Information and Communication Technology (ICT) solutions for under-served population in low-resource areas and improving social inclusion in health care. She continuously investigates and learn new and advanced methods, techniques and tools for big data analytics, text mining, ETL, business intelligence and visual analytics, and multiple criteria decision analysis. Prior to joining CISAT, she was a data scientist in industry with hands-on experience in advanced analytics, machine learning, and big data platforms.

Au Vo is a Claremont National Scholar. He is a PhD Candidate at the Center for Information Systems and Technology at the Claremont Graduate University. His current research areas are healthcare, management information systems, spatial analysis, and big data analytics. He is also an Associate Director for the Center for Information Technology and Business Analytics at California State University, Fullerton, assisting the Center with maintaining and expanding industry relationship. He also holds a faculty position at the University of LaVerne.

Manjit “Mike” Randhawa, MD, MPH is the Clinical Research & Analytics Manager at Inland Empire Health Plan (IEHP), a not-for-profit health plan in Southern California. Dr. Randhawa is leading the transformation of IEHP’s population health strategy and data-driven decision support system. Dr. Randhawa and his team are responsible for developing and implementing guidelines and processes to improve the analytic framework to support IEHP’s strategic priorities. Before joining IEHP, Dr. Randhawa was an Assistant Professor at Loma Linda University School of Public Health and School of Medicine for over 10 years. While at Loma Linda University, he also served as the Division Chief for Applied and Translation Research, as well as the Program Director of Population Medicine Masters of Public Health Program at the Loma Linda University School of Public Health. He continues to hold the dual faculty appointments and teaches part time with Loma Linda University School of Public Health and School of Medicine. Dr. Randhawa received his bachelor’s degree in Molecular Biology from University of California, San Diego, his medical degree from University of Szeged in Hungary and his Masters in Public Health from Loma Linda University School of Public Health with a focus in Population Medicine.

With more than 14 years of experience in healthcare analytics, Genia Fick is currently a Senior Director of the Quality Systems Department at Inland Empire Health Plan. She is a champion of various innovative quality and health care analytics projects such as the deployment of an organization-wide data warehouse, health plan quality reporting, risk adjustment programs and population health reporting. She is also responsible for supporting informatics and analytics needs within functional areas such as Medical Services, Quality Management, Provider Services and Network Development. She received her Master Arts in Health Psychology from Northern Arizona University.

## Designing Utilization-based Spatial Healthcare Accessibility Decision Support Systems:

## A Case of a Regional Health Plan

## Highlights:

 The healthcare spatial accessibility algorithm is improved via predictive analytics.

 First attempt to use the Andersen’s Behavioral Model to evaluate non-spatial factors.

 The utilization-based method integrates both spatial and non-spatial factors.

 The method is evaluated using a real world case of a regional health plan.

 The research designs a Spatial Decision Support Systems for healthcare resources planning
