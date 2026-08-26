---
otero_id: 5368
otero_key: "HTNG7CNN"
title: "Can Recommender Systems Reduce Healthcare Costs? The Role of Time Pressure and Cost Transparency in Prescription Choice"
authors: "Lina Bouayad; Balaji Padmanabhan; Kaushal Chari"
year: "2020"
journal: "MIS Quarterly"
doi: "10.25300/misq/2020/14435"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# CAN RECOMMENDER SYSTEMS REDUCE HEALTHCARE COSTS? THE ROLE OF TIME PRESSURE AND COST TRANSPARENCY IN PRESCRIPTION CHOICE<sup>1</sup>

Lina Bouayad College of Business, Florida International University, 1200 SW 8<sup>th</sup> Street, Miami, FL 33174 U.S.A. {lbouayad@fiu.edu}

Balaji Padmanabhan Muma College of Business, University of South Florida, 4202 E. Fowler Avenue, Tampa, FL 33620 U.S.A. {bp@usf.edu}

Kaushal Chari Lubar School of Business, University of Wisconsin–Milwaukee, 3202 N. Maryland Avenue, Milwaukee, WI 53202 U.S.A. {kchari@uwm.edu}

This paper presents and synthesizes results from three studies (two controlled experiments and one interview) on using recommender systems to reduce healthcare costs at prescription time, while taking time pressure into account. All of our subjects were real practicing physicians, nurse practitioners, or physician assistants. Across these studies, a total of 160 medical practitioners used a system that provides recommendations for medications along with associated cost information. The main finding was a general tendency among practi tioners to reduce healthcare costs by prescribing lower cost medications when cost information is provided by a recommender system. The time pressure faced daily by prescribers, however, appears to impact the use of recommendations by nurse practitioners and physician assistants more than it does physicians. These results have significant implications for cost reduction in healthcare and for the design of effective real-time healthcare recommender systems.

Keywords: Cost transparency, time pressure, clinical recommender systems, design science

## Introduction

Healthcare costs have reached astronomical figures in the United States. In 2015, U.S. healthcare spending reached nearly \$3.2 trillion with prescription drugs accounting for \$324.6 billion (Martin et al. 2016). A common approach for reducing medication costs without compromising on outcomes is through the use of generic drugs (Shrank et al. 2011). Generic drugs approved by the Food and Drug Administration (FDA), which contain the same active ingredients, dosage, and concentrations, and are administered the same way as corresponding branded drugs (Kesselheim et al. 2016). In a 1997–2000 survey, cost savings from prescriptions of equivalent generic drugs were estimated to be approximately \$6 billion for adults below 65 years and \$3 billion for adults 65 years or older (Haas et al. 2005). Insurance providers also offer three-tier plans, where in addition to generic and brand medications, medications on a shortlist of preferred brands (of similar outcomes) have a lower share of costs for patients (Joyce et al. 2002). Under the three-tier plans, similaroutcome brand medications vary significantly in terms of costs, depending on each patient’s insurance plan. Substituting drugs within the same drug class can be effective in reducing costs while maintaining outcomes. However, healthcare practitioners who make prescription decisions are typically unaware of the exact medication costs (Reichert et al. 2000).

Traditionally, cost information has not been included in the electronic medical record (EMR) systems used by medical practitioners. Recent studies indicate that several hurdles need to be crossed before price displays can be integrated into EMR systems (Hoffer 2015; Riggs and DeCamp 2014). Early research indicates promising outcomes for this initiative. For example, experimental results indicate a reduction, albeit at modest levels, in rates of ordering laboratory tests when realtime cost information is displayed in electronic health records (Horn et al. 2013). Building on these ideas, this paper investigates the potential of EMR systems in reducing medication prescription costs, an issue of immense significance particularly in the United States.

Specifically, our focus is on investigating the role that recommender systems can play in influencing choices by presenting lower cost alternatives with similar outcomes at the time the prescription is written. There have been some initial efforts in this direction to integrate recommender systems with existing EMRs, with the purpose of optimizing health care plans (Duan et al. 2011) and predicting disease risk (Davis et al. 2008). Using the patient’s medical history, the system can help healthcare practitioners predict diagnosis and act early to improve health outcomes (Davis et al. 2008). While prior research suggests the potential for such systems in this domain, to our knowledge, no prior study has evaluated the use of recommender systems for the purpose of reducing healthcare costs. Specifically, in this paper we consider the context where a physician, a physician assistant, or a nurse practitioner makes a diagnosis and chooses a treatment plan before seeing any recommendations or cost information. The recommender system then provides alternatives, along with the detailed cost information. The medical practitioner can choose an alternate option or keep his/her original treatment plan.

An aspect that differentiates our work from prior work and the practice of using generics as a low cost option is the consideration of a mixed cost system design. While different brand medications within the same drug class have similar health outcomes and side effects, they may vary in terms of dosage and administration mode (Appendix E, Physician Report 1). In a mixed cost system design, cost information is displayed for all medication options with efficacies equivalent to the original treatment chosen. Some of these options may be cheaper, while others may be more expensive than the original treatment chosen (in a low cost system design, only low-cost recommendations are presented). Presenting all options as recommendations may generate a list of alternatives with higher and lower costs than the initial plan chosen. In addition to being more realistic, this may resonate more with physicians who also consider patients’ convenience and health outcomes while prescribing medications.

Theoretically we know that the framing, or how costs are presented as recommendations, could impact the use of the system through the reference price effect anchored in adaptation level theory (Rajendran and Tellis 1994). According to the adaptation level theory, consumers respond to prices in a two-step process. Practitioners, like consumers, are assumed to first form an internal reference price (adaptation level) based on the average of prices of similar products (Helson 1964; Rajendran and Tellis 1994). The reference price then serves as a price scale or anchor for judging other prices (Emery 1970; Monroe 1973).

While prior research has linked price framing to consumers’ willingness to buy in the context of marketing (Grewal, Monroe, and Krishnan 1998), it is important to examine how cost framing (low versus mixed costs) of alternatives could impact a clinician’s selection of recommendations because there are important differences here. Decision making by providers in healthcare is different from the typical consumer behavior decision making context, as practitioners (1) do not make decisions for themselves, and (2) have limited knowledge of a patient’s share of costs, as costs often vary from one patient to the other based on insurance plans.

To the best of our knowledge, this is the first study to examine the impact of the design of health recommender systems on the adoption of cost-effective medication options presented by the system. The implications are significant to both research and practice. If the mixed cost design prevents practitioners from switching to a lower cost option, then such recommenders may not reduce costs significantly. This may suggest going with only low-cost recommenders if cost reduction is a major goal. On the other hand, if the mixed cost design works to lower costs, then we might have a new option that has not been considered yet. This paper presents important insights in this context.

Time plays a critical role as well here. Practitioners will need to spend additional time to review cost information and recommendations provided in the system. Since time is clearly a precious resource in a clinical setting, any recommendation system will need to be designed to support decision making at the point when practitioners write the prescriptions, and designed in a manner that considers the impact of additional time. Indeed, because of the time prescribers need to evaluate different alternatives, computerized systems have been either selectively used or completely removed in some cases (Drescher et al. 2011). Grounding our work in the extensive literature on the effects of time pressure on decision making, we use a two-step experimental design to also investigate how time pressure impacts practitioners’ use of costaware recommender systems.

A unique aspect of our study is that we examine differences in the effectiveness of these recommender systems across medical practitioner types. In addition to physicians, in many states nurse practitioners and physician assistants can prescribe as well. Compared to physicians, nurse practitioners and physician assistants undergo different types of training and work under different financial arrangements. These differences can impact their responses to (1) cost framing and (2) time pressure.

Our broader objectives are driven by a desire to provide insights in three related areas. First, we investigate how different types of cost-aware recommender systems impact prescription-choice behavior. Second, we examine how the use of such cost-aware systems is affected by time pressure on practitioners. Third, we explore the moderating effect of practitioner expertise on the evaluation and adoption of costaware recommendations in clinical settings.

Collectively, the results from this paper provide several contributions to the literature and to practice. While our interview results shed light on the relevance of cost information and time pressure on the prescription-choice behavior of practitioners, experimental results provide new insights on the use of medical recommender systems for addressing the issue of rising healthcare costs. Building on some of the recent contributions in this area (Adomavicius et al. 2013), we show through three different studies that cost-framing and time pressure can play a significant role in the adoption of medical recommender systems. These results also offer opportunities for theory building (presented in more detail in the “Discussion” section) related to the impact of time pressure and cost framing as well as for recommender system design in a clinical environment. To our knowledge, this is the first study to have examined recommender systems for clinical settings that provide cost-transparency under time pressure with a large number of subjects (160 in total), who are practicing physicians, nurse practitioners, or physician assistants.

## Background and Theoretical Foundations

Not surprisingly most physicians do recognize the importance of cost while prescribing (Hoffman et al. 1995; Reichert et al. 2000). In a survey of 134 physicians, 71% of respondents were open to even trading some degree of efficacy to prescribe more affordable medicines (Reichert et al. 2000). In a different survey of 95 physicians (Shrank et al. 2005), 91% of responding physicians agreed, mildly or strongly, with the following statement: When choosing between equally effective and safe medications, it is important to prescribe the drug that minimizes patients’ out-of-pocket costs.

Hence, physicians seem to be willing to consider low-cost prescription options for the same level of efficacy (Ahluwalia et al. 1996). When presented with cost information, physicians have been shown to significantly reduce prescribing more expensive medications in favor of cost-effective equivalent ones (Guterman et al. 2002). In addition to the overall healthcare cost savings, prescription of cost-effective medications could also improve the compliance of patients who are unable to afford expensive medications (Glickman et al. 1994). However, the lack of adequate knowledge of drug costs could prevent physicians from prescribing cost-effective options, which is where cost transparency facilitated by recommender systems could help.

Some early attempts to generate cost benefits by providing cost information to physicians via computerized systems have been unsuccessful. A study aiming to assess the changes in drug expenses after the introduction of a price comparison module in a computerized system found no significant changes in the prescription costs after the introduction of the module (Vedsted et al. 1997). Another study investigating the impact of cost information in a computer-based patient record system on the prescribing behavior of physicians found no evidence of an impact of providing real-time drug cost information on the overall drug costs to patients, although some differences in certain medication classes could be seen (Ornstein et al. 1999). However, changes over the past two decades, such as the rise of technology as a driver in healthcare and the broader focus on both outcomes and costs, might affect this. These earlier studies also mostly focused on brand versus generic medications. Extending the literature, we investigate the effects of substitution of brand medications within the same drug class. This approach would be more appropriate given the increasing adoption of three-tier insurance plans.

Further, prior studies on pharmacy cost reduction through cost transparency have primarily targeted medical doctors. In our studies, we include all clinicians with prescription privileges, namely physicians, nurse practitioners, and physician assistants. Nurse practitioners have been shown to be comparable to doctors in terms of care (Kuo et al. 2015) and patient satisfaction (Roblin et al. 2004). Hence, this group can play a significant role in reducing prescription costs.

## The Cost Framing Effect

In examining the relationship between cost framing and adoption of cost-effective recommendations, we draw on the rich literature anchored in adaptation level theory (Helson 1947). In general, adaptation level theory explains how individuals respond to stimuli relative to an adaptation level. The adaptation level represents a combination of all stimuli to which an organism has been attuned. This has been quantified using a weighted logarithmic mean of all stimuli. As per the theory, any stimuli near the adaptation level will fail to trigger any response. Stimuli above the adaptation level will trigger positive gradients with responses of one kind, and stimuli below the adaptation will trigger responses of the opposite kind. The adaptation level is assumed to change over time with varying types of stimulation (Helson 1947).

In marketing, adaptation level theory has been used to explain how consumers respond to prices. In a two-step process, consumers are assumed to first form an internal reference price (adaptation level) based on the average of prices of similar products. The reference price then serves as a price scale or anchor for judging other prices (Emery 1970; Monroe 1973).

In the healthcare context, this theory suggests that practitioners’ perception of patients’ share of costs depends on the alternative prices displayed by the recommender system, which in turn can affect their adoption of cost-effective recommendations. Based on the theory, we anticipate that practitioners will (1) form an internal reference price based on the cost information presented by the system and (2) evaluate the relative cost of their selected prescription medication based on their internal reference prices. Because of physicians’ lack of accurate knowledge of costs, we expect that their reference prices in our setting will be affected primarily by the cost information presented by the system, rather than by the price information accumulated over time. There is ample evidence in the literature to suggest our premise: that users (physicians) in general have inadequate knowledge of the costs of various treatment options (Allan et al. 2007; McGuire et al. 2009; Reichert et al. 2000), and little or no knowledge of the out-of-pocket costs to patients for prescription drugs (Shrank et al. 2005). Furthermore, the out-ofpocket cost of a medication might vary from one patient to another based on insurance plans (Joyce et al. 2002). Practitioners will base their perceptions of medication expensiveness on the cost of the medication that they typically select for the case (focal stimulus), and the costs of system recommendations (contextual stimuli).

In the case of a simple design, the system would identify the cost of the medication selected by the provider at the time of prescription, identify similar outcome medications, and present cost-effective alternatives for each specific patient. We refer to this as the low-cost design. Upon viewing the cheaper alternatives, practitioners are expected to form a reference price that is below the cost of their initial prescription. According to adaptation level theory, this will trigger a change of prescription to a lower cost medication. The adoption of cost-sensitive recommendations in this design may also be affected by the appeal to social norms. Appeal to social norms has been shown to play a significant role in influencing human behavior in several settings, for example in environment conservation (Goldstein et al. 2008). Based on that effect, systems have been designed to carefully select settings such as defaults (Johnson and Goldstein 2004), and recommendation characteristics (Thaler et al. 2013). A display of a cheaper alternative treatment, for instance, might signal practitioners that they are diverging from the low-cost prescription norm and thereby trigger adoption of cost-effective recommendations. The appeal to the social norm effect could be moderated by factors such as laws (Posner 1997) or individual self-interest (Olson 1965; Ostrom 2014). However, under our main assumption that all recommended treatments result in similar or better clinical outcomes, prescribing the lower-cost alternative treatment would not cause any liability issues. In fact, given the U.S. government’s recent emphasis on reducing prescription drug costs (Obama 2016), altering prescriptions to the low-cost treatment options would likely be more aligned with a practitioner’s self-interest to reduce costs, thereby making the adoption of cost-aware recommender systems more likely.

A system design that limits recommendations to low-cost alternatives would not be applicable in clinical settings involving certain patient populations such as children or seniors. While different brand medications within the same drug class have similar health outcomes and side effect, they often vary by administration mode (Appendix E, Physician Report 1). If a higher cost medication has a more convenient administration mode, it may be preferred by patients and practitioners. How easy a medication is to take, or to remember to take, may affect whether the patient follows the prescriber’s orders. Administration mode, for instance, can be correlated with medication adherence. For example, medications that are taken once a day are easier to comply with than alternatives taken three times daily. For patients, the additional convenience from an easier administration mode may offset the higher share of cost. Patients and providers might also prefer particular medication brands if they have been shown to be effective in prior personal use. In these settings, it is important that the recommender system displays treatment options that have a more convenient administration mode even if they may be more expensive than the medication usually prescribed by the practitioner. This would result in a system that lists high and low cost alternatives, referred to here as the “mixed-cost design.”

Note that in other consumer contexts, users might also perceive high costs to be indicative of higher quality (Grewal, Krishnan et al. 1998; Monroe and Chapman 1987). Clinicians with prescription privileges have the necessary knowledge to recognize the similarity of alternatives in terms of efficacy and side effects (see experts’ reports in Appendix E). Practitioners are less likely to adopt higher cost alternatives simply by using price as a signal.

Even when high-cost recommendations are not adopted, they can serve as anchors at the time of evaluating alternative prices and may impact the adoption of cost-effective recommendations. Prior research indicates that recommendation ratings affect consumers’ preferences (Adomavicius et al. 2013; Cosley et al. 2003). That is, when a system presents favorable ratings, a consumer’s expressed preference for that option is high (and vice versa). Similarly, we might expect prices presented by recommender systems to influence adoption of recommendations. Based on the adaptation level theory, when faced with a mix of high and low cost recommendations, practitioners are expected to form a reference price in the middle of the displayed prices. In this scenario, practitioners are expected to keep their initial prescription if the price is close to this reference price. The display of highcost recommendations could reduce the likelihood of adopting cost-effective alternatives that are suggested by the recommender.

One of the important distinctions in our work is the consideration of nurse practitioners and physician assistants in this domain. In practice, nurse practitioners are more likely to care for Medicaid recepients and other vulnerable populations (Buerhaus et al. 2015), and have longer consultations with patients (Horrocks et al. 2002; Laurant et al. 2005). As a result, compared to physicians, they provide more information to patients (Kinnersley et al. 2000) and are likely to take more time to view alternatives and related cost information. This would suggest that they are more likely to form reference prices. Moreover, the earnings of nurse practitioners or physician assistants are estimated to be 20% to 35% lower than the earnings of physicians (Naylor and Kurtzman 2010). This suggests that nurse practitioners and physician assistants are more price sensitive compared to physicians, and are likely to form lower reference prices (Bell and Lattin 2000). Therefore, compared to physicians, there would be a higher likelihood that nurse practitioners and physician assistants would judge the initial prescription price as too high. This in turn also could lead to a higher adoption of cost-effective treatment alternatives compared to physicians.

## The Time Pressure Effect

Patient–practitioner encounter time has always been a scarce resource, especially in managed care settings (Dugdale et al. 1999; Linzer et al. 2000). Practitioners often encounter time pressure and, in some cases, physicians were reported to spend less than two minutes answering patients’ clinical questions (Ely et al. 1999; Ramos et al. 2003). On the other hand, nurse practitioners often spend more time with patients (Venning et al. 2000). Time pressure is still relevant, yet less acutely so for the nurse practitioners and physician assistants.

The literature has suggested some ways to remedy this lack of time, such as by using computer-based prescribing software (Allan et al. 2007) and “reminder systems” for just-in-time intervention at the time of prescription (Alexander et al. 2005). To date, however, no controlled study has actually investigated the role of time pressure in impacting the actual use of such systems in healthcare in general, and reducing costs in particular. In this context, it is also important to note that practitioners are more likely to make prescription medication changes at the time of the prescription rather than make adjustments later (Awdishu et al. 2016). Understanding the time pressure during patient–prescriber interactions is critical in the effective design of clinical recommender systems.

Prior literature indicates that the extra cognitive demands of time pressure could drive practitioners to use simplifying rules (Landry 2015) and select easier decisions or “defaults” (Bobadilla-Suarez and Love 2018). For cost-aware recommender systems, this suggests that, under high time pressure, clinicians might elect to simply prescribe the treatment they are accustomed to in similar cases and ignore system recommendations.

In general, individuals under high time pressure are likely to filter out (Hahn et al. 1992) and process less information (Wright 1974). At the time of prescription, clinicians under high time pressure might filter out information they deem less important, such as cost. In outpatient settings such as primary care (the focus of our studies), taking extra time to view and update prescriptions is less likely to put any patient at risk, but this is also a context in which providers are pushed to see more patients, creating more pressure on their scarce time.

The decision to view system recommendations could also depend on the perceived importance of cost information. Practitioners who view cost as a secondary criterion for medication selection might dismiss system recommendations. On the other hand, clinicians who consider cost a barrier to medication adherence may be more likely to consider costsensitive recommendations even under high time pressure.

The training a prescriber receives in dealing with time pressure could also be relevant. During residency, medical doctors are taught to work under time pressure. On the other hand, nurse practitioners are trained to spend more time with patients, as well as trained to consider aspects of care such as disease-prevention counseling, health education, and health promotion (Mundinger 1994). In most states, nurse practitioners and physician assistants work under the mandated supervision of physicians. When working in a medical practice, nurse practitioners and physician assistants typically work for managed-care organizations that employ a prepaid rather than fee-for service care model (Hooker 2006). Thus they have a lower incentive to consult more patients. Physicians’ income, on the other hand, is correlated with the number of patient consultations. Therefore, they might be inclined to consult more patients and are likely to feel time pressure more than nurse practitioners and physician assistants. Because of the lack of time pressure experience and training, however, nurse practitioners and physician assistants could be more affected by time pressure than physicians.

## Decision Making on Behalf of Others

Even with health insurance, patients are responsible for a share of medication costs. Since costs are not borne by the prescriber, one argument may be that physicians are not sensitive to prescription prices (Gönül et al. 2001), suggesting minimal impact of adaptation level and reference price effects on physicians.

However, the literature on decision making on behalf of others suggests otherwise. Users making decisions on behalf of others are likely to seek more information. When choosing for others, decision makers tend to view more alternatives (Polman 2012) and review more attributes (Liu et al. 2018). Practitioners are expected to consider various alternatives presented by the system. This in turn is likely to increase the impact of adaptation level.

Practitioners are also more likely to process information about alternatives after selecting a prescription (post-decisional distortion). Research literature has shown that when choosing for others, decision makers tend to be less biased. Compared to making decisions for self, individuals are likely to exhibit less omission bias (Zikmund Fisher et al. 2006), intertemporal discounting bias (Ziegler and Tunney 2012), and less postdecisional distortion bias (Polman 2010). In our setting, practitioners are less likely to bypass the process of evaluating the various priced alternatives (omission bias, intertemporal bias). Many patients do not take their medications as prescribed because they cannot afford the cost of the medication (Gibson et al. 2005; Glickman et al. 1994). Given these considerations, we posit that practitioners are more likely to consider alternatives presented by the system.

There are many theoretical reasons to believe that cost framing and time pressure can impact the use of recommender systems for cost reduction in healthcare. However, to date, there have been no controlled experiments to provide answers to whether these matter in practice and how significant their impacts might be. Driven by three studies (two controlled experiments and one qualitative interview) involving a total of 160 practicing doctors, nurse practitioners, and physician assistants, this paper presents results that can both inform theory and impact practice in a meaningful manner.

## Study One: Physician Study— Controlled Experiment

At the core of all our studies is the design of cost-sensitive recommender systems that present options for medications with similar efficacies along with accurate cost information. This underscores our focus not only on costs but also on outcomes.

These studies employ two different recommender settings. In the first setting, referred to as the “low-cost setting,” practitioners are presented with a list of low-cost alternatives with similar efficacies. In the other recommender setting, referred to as the “mixed-cost setting,” the list of recommendations includes a mix of high and low-cost alternatives with similar efficacies. We posit that practitioners are likely to view recommendations and adjust their treatment prescription based on the costs of various recommendations presented. As per the discussion earlier, the adoption of system recommendations is likely to be higher when all recommendations presented are of low costs. In the mixed-cost settings, high cost options are anticipated to impact a practitioner’s internal reference cost, thereby possibly lowering the adoption of lowcost recommendations.

## Experimental Design

In collaboration with two medical practitioners we created a set of six medical cases for use in our experiments. Each medical case included a patient’s information and associated medication lists as indicated by the medical protocol. The patient’s information included general information, insurance information, demographics, active problem list, medication list (within and outside the current practice), any clinical alerts, chief complaint(s), history of present illness, past medical history, family medical history, social history, and a detailed visit description in the method of healthcare documentation called the “subjective, objective, assessment, and plan” (SOAP) format. The treatment plan section was intentionally left out since the participating practitioner’s task was to determine the treatment plan. Appendix B includes the list of medical cases created for the experiment.

Even though the cases were different in nature, they were assessed by these experts as being of similar complexity and risk levels. Using fictional patient profiles (age, family history, clinical alerts, vital signs, and physical exam), we were able to create cases of similar degrees of severity. While creating the cases, we also intentionally focused on internal medicine conditions in order to ensure familiarity of all experimental subjects with the clinical cases and treatment options across designation and specialty. The treatment options presented were identified using the most up-to-date medical protocols for each specific condition. Importantly, using the same drug class and active ingredients, we were able to present alternatives with similar side effects as well. Hence, the recommendations provided primarily varied based on the cost information associated with them and did not have different side effect profiles or differences in outcome propensities. Also, the information displayed was realistic and in great detail and mimicked the traditional EMR systems that were used in this context.

For this experiment, we used a 2×2 experiment design where treatments were cost and time pressure. A between-subject design was used to investigate the effects of cost on the adoption of recommendations. Participants were randomly placed into two different groups (Table 1). Depending on their respective group, participants were presented with varying recommendation costs. Half of the participants (Group 1) were presented a list of all low-cost recommendations, while the other half (Group 2) received recommendations of mixed costs. Because of the anticipated low number of participants, we used a within-subjects design to evaluate the impact of time pressure on a practitioner’s use of system recommendations. In three out of the six cases, the participants were under high time pressure (see Table 1). A counterbalanced design was used to control for the order effect. Using random assignment, half of the participants received the time pressure treatment first, while the remaining half received the time pressure treatment last.

Operationalization of the treatments used in the experiment was rooted in the literature and practice. The time pressure treatment was represented by the presence/absence of a message in three out of the six cases, indicating increased workload for the remaining time (THE SYSTEM HAS JUST ADDED SEVERAL CASES TO YOUR QUEUE! Please try to complete all cases within the allocated time) along with a timer counting the number of seconds spent on each page.

The recommendation costs treatment was represented through the manipulation of cost information. After designing the experiment, a group of one physician and two pharmacists was asked to estimate the average patient’s share of the cost for each medication. Costs of various drugs were then dynamically manipulated during the experiment. Differences in costs between different brands ranged from \$50 to \$100. After each participant had selected an initial treatment option, the recommender system provided alternatives. For the lowcosts groups, the recommendations presented by the systems were cheaper than the treatment originally selected by the participants. For the mixed-costs groups, the initial treatment option selected by a participant was dynamically set to a cost X. Two recommendations were then presented with costs Y and Z, where Y < X < Z. The practitioner then had the option to alter his/her initial selection. The experiments were conducted online using Qualtrics, which allowed for the dynamic allocation of medications and costs.

## Experimental Procedure

For the experiment, we used a convenience sample of 32 participants from the state of Florida.<sup>2</sup> In order to prevent learning effects, participants were also required to certify completing the experiment once only.

The experiment flow was as follows. First, participants were presented with an informed consent agreement page describing the purpose of the study, the study procedures, alternatives to participation, compensation, and contact information. All participant identities remained anonymous. Next, each participant was presented with six fictional patient cases. For each case, a participant was prompted to prescribe a treatment. The participant was then provided with the treatment cost information and given the option to view other recommended medications. The list of recommendations included two medications presented in random order. After reviewing the system recommendations, the participants were given the option to adjust their treatment prescription for each patient.

Participants were randomly placed into different groups. Depending on their group assignment, participants were presented with either (1) a list of recommendations all cheaper then their original prescription or (2) a mix of high and low cost recommendations. In three out of the six cases, participants experienced low time pressure, while in the remaining three cases, they experienced high time pressure. Follow-up survey questions were also presented to capture all participants’ specialty and their years of experience (a walkthrough of a sample scenario is available in Appendix A).

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Treatment 1: Time Pressure</td></tr><tr><td>Low TP</td><td>High TP</td></tr><tr><td rowspan="2">Treatment 2: Recommendation Costs</td><td>Low Cost Recommendations</td><td>Group 1 (3 cases)</td><td>Group 1 (3 cases)</td></tr><tr><td>Mixed Cost Recommendations</td><td>Group 2 (3 cases)</td><td>Group 2 (3 cases)</td></tr></table>

Notes: Participants were randomly placed in each of the treatment groups.  
Each subject within the groups was presented with the same patient cases 1 through 6.

## Subjects and Data Description

A total of 32 physicians participated in the experiments. By virtue of the generic nature of the cases used (related to primary care practice), practitioners of all specialties were able to complete them. Our pool of participants was composed of physicians in Florida, most of whom had a considerable number of years of experience (see Figure 1).

We were able to collect a balanced set of responses in terms of both subjects and cases. Eight complete responses were recorded in each of the four groups. With each of the 32 participants completing 6 cases, we had a set of 192 case level observations. Clinical cases used in this study included conditions commonly treated by practitioners across all specialties of medicine.

Two different dependent variables were measured, namely “view,” which represents the number of occurrences where the participants viewed the system recommendations, and “adjust,” which refers to the number of times the participants changed their initial treatment plan to the one recommended by the system.

Overall, we observed that participants viewed system recommendations for 147 out of the 192 cases and adjusted their treatment plans in 95 out of the 147 cases for which participants viewed recommendations. These large numbers indicate that the physicians had a general tendency to reduce patient treatment costs when given the option to do so. This is a key overall finding from this experiment, indicating the potential for healthcare cost reduction from carefully designed recommender systems.

## Experiment Results

## Descriptive Statistics

Our sample included real physicians many with substantial experience. The sample size was therefore a limitation with only eight physicians in each group. However, 192 observations were collected at the case level, allowing for statistical analysis. Dichotomous predictors were created to investigate the impact of recommendation costs, time pressure level, and time pressure order on the viewing of system recommendations and the adjustment of prescriptions (Table 2). Other variables were used to control for the effects of specialty and years of experience on viewing and adjustment of recommendations.

## Manipulation Checks

To ensure that participants were successfully manipulated by the cost framing and time pressure treatments, we used several criteria. To check for the cost framing manipulation, through a post-experiment questionnaire, participants were asked whether they had noticed cost information. Observations for participants that reported not noticing cost information (a total of 3 participant observations impacting 18 patient cases cases) were replaced. To check for the effectiveness of time pressure treatment manipulation, we recruited an additional eight physicians for a control group. Since we used a withinsubject experimental design for the time pressure treatment, all participants received the time pressure treatment at some point during the experiment (either the first three or last three cases). In the control group, physicians received no time pressure for all six cases. Average and standard deviations of the completion time were calculated for the control group (34.9 minutes, 12.06 minutes). Observations (a total of 3 participant observations impacting 18 patient cases) that lasted more than 56 minutes (34.9 + 2 \*12.06) were replaced, since those participants were likely ignoring the time pressure treatment or completed the experiment in more than one sitting. All invalid observations were then dropped and replaced by recruiting new participants.

![](/api/attachments/HTNG7CNN/fulltext/images/e5f68751c05e67374707e97f9023754d69c6f1f7a3e5d37e2e85d516a1dc06ae.jpg)  
(a) Years of Experience

![](/api/attachments/HTNG7CNN/fulltext/images/753e8d645009c6b9b8f214ddf337bd7eccff9ab7d69f0e7f68cc21d8b42a106b.jpg)  
(b) Physician Specialty

Figure 1. Participant Profiles

<table><tr><td colspan="5">Table 2. Descriptive Statistics</td></tr><tr><td>Variable</td><td>Levels</td><td>N</td><td>View Mean (Std. Var.)</td><td>Adjust Mean (Std. Var.)</td></tr><tr><td colspan="5">Independent Variables</td></tr><tr><td rowspan="2">Recommendations Costs</td><td>1: Mixed Costs</td><td>96</td><td>0.687 (0.466)</td><td>0.406 (0.494)</td></tr><tr><td>0: Low Costs</td><td>96</td><td>0.844 (0.365)</td><td>0.583 (0.496)</td></tr><tr><td rowspan="2">Time Pressure</td><td>1: High TP</td><td>96</td><td>0.75 (0.435)</td><td>0.490 (0.503)</td></tr><tr><td>0: Low TP</td><td>96</td><td>0.781 (0.416)</td><td>0.500 (0.503)</td></tr><tr><td colspan="5">Control Variables</td></tr><tr><td rowspan="2">Specialty</td><td>1: Internal Medicine</td><td>78</td><td>0.884 (0.322)</td><td>0.512 (0.503)</td></tr><tr><td>0: Other</td><td>114</td><td>0.684 (0.467)</td><td>0.482 (0.502)</td></tr><tr><td rowspan="5">Years of Experience</td><td>5: 15+ years</td><td>114</td><td>0.772 (0.421)</td><td>0.474 (0.502)</td></tr><tr><td>4: 10–15 years</td><td>12</td><td>0.917 (0.289)</td><td>0.500 (0.522)</td></tr><tr><td>3: 6–9 years</td><td>24</td><td>0.958 (0.204)</td><td>0.750 (0.442)</td></tr><tr><td>2: 3–6 years</td><td>30</td><td>0.533 (0.507)</td><td>0.367 (0.490)</td></tr><tr><td>1: 0–3 years</td><td>12</td><td>0.750 (0.500)</td><td>0.500 (0.522)</td></tr></table>

## Statistical Findings

Since each participant responded to six different cases (repeated measures as per our experiment’s within-subject design), we used generalized estimating equations (GEE) (Liang and Zeger 1986), an approach that has been used extensively in health research (O’Campo et al. 1995; Schneeweiss and Avorn 2005; Wechsler et al. 2002) to test the main effects, while taking into account the correlation of responses within subjects (Ballinger 2004; Morris and Venkatesh 2010). Using the method, we created two different models for each of the dependent variables. We first created base models using control variables only, and then we created models that included control and predictor variables. The models were used to investigate the impact of time pressure on recommendation viewing and the impact of cost framing on treatment adjustment.

Estimation results from the GEE models (Table 3) indicated no significant effect of time pressure on recommendation viewing, but showed a significant effect of cost framing on treatment adjustment. These results suggest that for physicians, time pressure did not impact their interest or ability to process the additional recommendations provided along with detailed cost information. However, given the significance of cost framing, this group of participants tended to be influenced by the presence of expensive options in the recommendation list. More of them changed to lower cost options when all costs were lower, unlike the mixed-costs case (distributed around the cost of their originally chosen treatment). Given the experiment design, the participants who chose to

QIC: Quasi-likelihood under the Independence model Criterion; QICu: Approximation of QIC used in GEE with correlated data. Heckman model stage 1: Selection model with controls and the exclusion restriction time pressure variable. Stage 2: Main adjustmen model given View = 1.

<table><tr><td rowspan="2"></td><td colspan="2">Viewership Models</td><td colspan="2">Adjustment Models</td><td colspan="2">Heckman Model</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td><td>Stage 1</td><td>Stage 2</td></tr><tr><td colspan="7">Control Variable</td></tr><tr><td>Specialty (0)</td><td>-2.71**(0.0068)</td><td>-2.74**(0.0062)</td><td>-0.46(0.6424)</td><td>0.11(0.9122)</td><td>3.84***(0.0001)</td><td>-1.22(0.2231)</td></tr><tr><td>Years of Experience (1)</td><td>-0.10(0.9164)</td><td>-0.03(0.9790)</td><td>0.09(0.9271)</td><td>0.71(0.4805)</td><td>-0.54(0.5868)</td><td>0.94(0.3482)</td></tr><tr><td>Years of Experience (2)</td><td>-1.91(0.0556)</td><td>-1.91(0.0565)</td><td>-0.63(0.5279)</td><td>-0.90(0.3687)</td><td>-2.40*(0.0166)</td><td>0.66(0.5062)</td></tr><tr><td>Years of Experience (3)</td><td>2.29*(0.0217)</td><td>2.41*(0.0159)</td><td>1.97*(0.0490)</td><td>2.40*(0.0166)</td><td>2.44*(0.0145)</td><td>0.03(0.9769)</td></tr><tr><td>Years of Experience (4)</td><td>1.90(0.0574)</td><td>1.83(0.0677)</td><td>0.21)(0.8337)</td><td>-0.42(0.6769)</td><td>1.81(0.0702)</td><td>-1.31(0.1912)</td></tr><tr><td colspan="7">Predictor Variable</td></tr><tr><td>Time Pressure Level (1)</td><td></td><td>-0.40(0.6917)</td><td></td><td></td><td>-0.44(0.6608)</td><td></td></tr><tr><td>Recommendations Costs (1)</td><td></td><td></td><td></td><td>-2.03*(0.0420)</td><td></td><td>-2.22*(0.0263)</td></tr><tr><td>Lambda</td><td></td><td></td><td></td><td></td><td></td><td>-0.63(0.5279)</td></tr><tr><td colspan="7">Performance Measure</td></tr><tr><td>QIC</td><td>202.0314</td><td>204.9506</td><td>287.5275</td><td>278.2490</td><td></td><td></td></tr><tr><td>QICu</td><td>188.5961</td><td>190.3420</td><td>268.7993</td><td>259.6330</td><td></td><td></td></tr><tr><td>Log Likelihood</td><td></td><td></td><td></td><td></td><td>-88.200</td><td></td></tr><tr><td>AIC</td><td></td><td></td><td></td><td></td><td>190.399</td><td>-212.893</td></tr><tr><td>Regression  $R^2$ </td><td></td><td></td><td></td><td></td><td></td><td>0.078</td></tr><tr><td>Adjusted  $R^2$ </td><td></td><td></td><td></td><td></td><td></td><td>0.032</td></tr></table>

Notes: \*p < .05; \*\*p < .01; \*\*\*p < .001. Standard errors are in parentheses.  
Model 1: GEE base model with control variables only; Model 2: GEE model with control variables and main effects.

adjust their prescriptions had to view alternative treatment options before adjusting their prescriptions. To account for these potential endogenous choices, we also used a two-stage regression model commonly used for this purpose (Heckman 1979; Shaver 1998). First, we estimated a probit model to assess the effects of time pressure on the viewing of recommendations. We then created the second-stage model to evaluate the effects of cost framing on the adoption of recommendations, given that the user had viewed system recommendations (View = 1). Since participants were unaware of the alternative costs prior to viewing, the recommendation cost predictor variable could only impact prescription adjustment. To strengthen the Heckman model, we also included an exclusion restriction variable (Briggs 2004). We used an independent variable that was included in the selection equation but not included in the main equation. As discussed in earlier in the section on the use of filtering and simplifying rules under time pressure, time pressure impacted viewing of recommendations but did not directly affect the adjustment of prescriptions. Therefore, time pressure was included in the section equation (stage 1, viewership), but not included in the main equation (stage 2, adjustment). Since specialty and years of experience could impact both viewing and adjustment of prescriptions, these were included in both stages 1 and 2 of the model. Physicians with relatively less experience are expected to view the recommender system as a tool to view what other physicians prescribed in similar cases. With less prescription experience, novice physicians are also less likely to have loyalty to specific brands of medications. They are expected to adjust treatment options more than experienced doctors. Compared to physicians in other specialties, internists commonly treated patients in a more holistic manner. Given their holistic view, internists are expected to view system recommendations and adjust treatments more than physicians of other specialties. In addition, some specialties had greater cost pressure, which could impact the rate at which prescription adjustments were made. As a case in point, given the recent wild inflation of patients’ cost of insulin, physicians treating diabetes cases may be expected to adjust more.

The two-stage analysis results (Table 3) also confirmed the results from the GEE models. The results indicated no significant impact of time pressure, but showed a significant impact of the recommendation cost on the adjustment of prescription behavior, thereby suggesting that the display of all low-cost alternatives had a high impact on prescriptionchanging behavior.

Overall the physician experiment results indicated that framing of cost alternatives in the recommender system did impact their decision to prescribe cost-effective medications, thereby suggesting that even experts (physicians) were impacted by the reference price effect. It is interesting to note that the reference price effect also applied in healthcare in cases when costs were not accrued directly by the user (i.e., these costs were not faced by the clinician prescribing the treatment).

Results of the tests for the impact of time pressure on the use of recommendations contradicted what we expected based on how time pressure in general affects users of systems. Even under time pressure, physicians did not change their use patterns in terms of choosing to view recommendations. There could be different explanations for this. It is possible that physicians, whose primary goal is patient outcome, might choose to use a recommender system only when access to the knowledge of alternatives might affect the outcome, regardless of the extra time they spend using the system. It is also possible that for these experts, in addition to their training during residency programs that prepares them for this, time pressure is so prevalent in their lives, that it no longer affects their decision making. Our experiments were not designed to tease out the reasons for this, but future research can explore some of these possible explanations in detail.

## Robustness Checks

Because of the challenges in recruiting physicians to participate in an experiment, the physician experiment was designed to include six patient cases. While the multiple cases enabled us to test statistical significance at the case level, the design also introduced the possibility of learning effects influencing the results. To check for the robustness of cost framing effect on treatment adjustment, we dropped the first case (out of eight cases) completed by each participant and recreated the statistical models. Another effect that could have impacted our results is the tiring effect. Because each participant was prompted to review six patient cases, he/she could have refrained from adjusting treatment because of the tiring effect. To control for this effect, we dropped the last case (out of eight cases) completed by each participant and recreated the statistical models. Estimates from the updated statistical models (Table 4) showed no qualitative difference in the results.

## Study Two: Physician Study— Post-Experiment Interviews

To gain a better understanding of the impact of our findings in practice and validate some of our study’s underlying assumptions, we conducted detailed post-experiment interviews with a different group of physicians. We used the protocol guide approach to get insights in a few areas. This method was chosen over the closed-fixed response interviews, as it enabled us to gather richer insights. This guided approach also enabled us to gather data related to specific questions and issues of interest as follows: (1) whether physicians have access to accurate cost information today (if they all do, then our findings might be seen as less relevant, lagging practice), (2) how physicians view cost information and time pressure, and (3) how physicians could use an intelligent recommender system.

## Subjects and Methods

A questionnaire was developed for this study targeting physicians outside the pool of participants in the initial experiment. The open-ended questionnaire was developed based on key underlying study assumptions. For content validity, a pilot questionnaire was used and refined after each interview of four different physicians, and then frozen after the pilot test. The questionnaire used for the survey is available in Appendix C.

Over a two-month period we interviewed a total of ten physicians after piloting the questionnaire with four physicians (Table 5). Interviews were typically 30 to 50 minutes long. They were conducted over the telephone (usually in the evenings when physicians had more time to talk), recorded, and transcribed for further analysis.

## Data Analysis

We then analyzed the data as follows. Key indicators mentioned by respondents were identified and iteratively refined. The initial round of indicator extraction was performed by the three authors. Each indicator was then mapped to key contextual factors: cost and time pressure.

<table><tr><td colspan="4">Table 5. Qualification Summary of Experts Interviewed</td></tr><tr><td>Participant</td><td>Specialty</td><td>Years of Experience</td><td>Practice Type</td></tr><tr><td>Physician 1</td><td>Nephrology</td><td>17</td><td>Solo practice</td></tr><tr><td>Physician 2</td><td>Nephrology</td><td>11</td><td>Solo practice</td></tr><tr><td>Physician 3</td><td>Internal Medicine</td><td>23</td><td>Hospital</td></tr><tr><td>Physician 4</td><td>Emergency Medicine</td><td>6</td><td>Group practice</td></tr><tr><td>Physician 5</td><td>Emergency Medicine</td><td>45</td><td>Group practice</td></tr><tr><td>Physician 6</td><td>Geriatrics and Palliative Care</td><td>4</td><td>Federal government</td></tr><tr><td>Physician 7</td><td>Obstetrics and Gynecology</td><td>17</td><td>Group practice</td></tr><tr><td>Physician 8</td><td>Neonatology</td><td>16</td><td>Hospital/Clinic</td></tr><tr><td>Physician 9</td><td>General Pediatrics</td><td>26</td><td>Solo practice</td></tr><tr><td>Physician 10</td><td>Cardiologist</td><td>15</td><td>Group practice</td></tr></table>

## Qualitative Results

The rich responses of experts in the field revealed important insights into the relevance of cost and the effects of time pressure in the practice of medicine. Interview questions prompted the interviewees to talk about access to cost information. While interviewees confirmed the overall lack of access to accurate cost information, interesting indicators that came up related to the type of cost information currently available and the laborious retrieval process. Similarly, when prompted to talk about time pressure in practice, interviewees mentioned several factors leading to the time pressure, providing great opportunities for future research.

## Medication Cost Consideration

Several years after the initial studies on the importance of treatment costs (Hoffman et al. 1995; Reichert et al. 2000), our study affirms that the majority of physicians still view cost as a significant factor in treatment selection. Consistent with prior findings (Reichert et al. 2000), physicians in our cohort significantly valued the importance of reducing patient out-ofpocket cost. They also brought up an important potential link between the prescription of affordable medications and patient compliance to medications, as one physician noted:

Absolutely, as a provider, my responsibility to you as a patient is not only to write a prescription. It’s also important to give the best medication that the patients can afford.

Most interviewees indicated the obscurity of cost information. This indicates that cheaper treatment alternatives may be as effective as expensive ones:

In this day and age of evidence-based medicine. I think everyone looks at the evidence with the exclusion of the cost. If it’s been proven that a treatment works and the research backs that up then, that’s what most providers base their treatment decisions on.

However, one cardiologist stressed that when a patient’s clinical outcome is at stake, cost information is rendered less significant.

Cost has always been an issue. It’s something in the back of your mind but when I am dealing with, in my specific situation, someone’s heart condition, my opinion is somewhat skewed. Cost is probably the last thing that I think about when I care for the patient.

Results therefore confirm that physicians do recognize the importance of treatment costs. Considering cheaper treatment options that are recommended, however, is only likely when health outcomes are equally likely.

## Cost Information Access

Despite the perceived importance of cost information, physicians in our cohort reported no access or limited access to accurate medication cost information at the time of prescription. Interviewees did report a relative improvement in cost information access led by recent initiatives:

I would say more so than in the past there has been even a lot of effort as of late to help providers understand the cost of the medication that they are prescribing.

However, several factors that limited the consideration of cost information at prescription time emerged during the interviews. First, cost information presented by existing systems tended to be very broad, indicating the cost tier level for medications. Second, when detailed cost information was made available, data retrieval required extensive effort and time. Also, because patients under different insurance plans might pay very different amounts for the same medication, prescribers face a major barrier to accessing knowledge of those costs:

I would not know the exact cost of that drug … for a month’s supply because that differs from one insurance to another. Sometimes the patients don’t even know themselves.

Even with recent efforts in providing cost information to physicians, only broad or incomplete cost information is now available. These results further stress the need for systems that automatically provide accurate cost information at the time of prescription.

## Time Pressure Relevance

These interviews also suggested that most physicians did not have control over the number of patients they saw, and hence little control over their time in a given day, as suggested by the quote below:

I don’t have so much control over my time. In the sense that when I’m in the office, we see whoever wants to be seen. In that way, I have a pretty tight day schedule in the office.

Physicians across different specialties mentioned experiencing time pressure due to various factors such as (1) the multitude of conditions that needed to be discussed during patient consultation, (2) the number of patients per day, (3) the criticality of patient cases, (4) the need to expedite care in accordance with organization rules, (5) seasonality, and (6) the number of tasks during consultation.

## System Use under High Time Pressure

Interestingly, results from the physician interviews suggested that physicians were likely to use their current information systems more, not less, under high time pressure. Different from emergency room contexts considered in prior literature, where clinicians either selectively used or completely removed computerized systems (Drescher et al. 2011), physicians in the outpatient context seemed to value system recommendations more under high time pressure. When faced with time pressure, physicians reported their tendency to change the way they interacted with the electronic medical record (EMR). In order to save time, physicians mentioned using prompts and templates, skimming through the medical records, or completing patient chart information at a later time such as at the end of a workday.

Because of its hypothetical nature, the intended use of costsensitive recommender systems was difficult to assess through the interviews. Most respondents seemed reluctant to provide definite answers about its use without actually trying the system. However, participants provided very interesting feedback regarding the specific features that they would like to see in an effective cost-sensitive recommender system:

1. Comparison of efficacy and safety across alternative treatment options (recommendations):

Yes, if it is the same efficacy and that’s cheaper, I’m fine with that. Not just efficacy: we are talking about safety; we are talking about probability. So, when we are talking about giving a patient a medication it’s not just how effective it’s going to be, it’s also how safe it is and how vulnerable the patient is going to be. So, if those criteria are met of course.

2. Scientific evidence supporting the efficacy of treatment options (recommendations):

[Alternatives] that are acceptable by the medical standards for that condition.

If the system is perfect and recommendations are evidence-based, I would use it.

3. Time-saving practitioner experience:

I mean if it is very time consuming, then obviously people are not going to be keen on using it, but if it is easy to use and user friendly and doesn’t take a lot of time then I am sure that we could use it.

Overall, these post-experiment interviews were useful in assessing the relevance of cost-sensitive recommenders in the field. Insights gained from the interviews suggested that physicians would be inclined to consider cost information if available. While time pressure seemed prevalent, the interviews did suggest that it may not impact a physician’s use of costaware recommender systems, when the recommender was easy to use and useful. This is in line with what we found in the physician experiments reported earlier. From a practical perspective, the interviews suggested that the physicians may indeed be ready to embrace a recommender that provided accurate cost information at the time of prescription.

Integrating the results from the interviews and the controlled experiment, we find that physicians do realize the importance of cost reduction and are likely to adopt cost-sensitive recommenders, even under time pressure, but that cost-framing can play a role. Overall, these results bode well for cost reduction efforts in healthcare, particularly if recommenders such as the one discussed in this study (similar outcomes/low cost) were available in practice.

We next present a study of nurse practitioners and physician assistants, who also have prescription privileges in most states in the United States, and therefore could also play a significant role in cost reduction.

## Study Three: Nurse Practitioners and Physician Assistants

Finally, to investigate the differences in decision-making between practitioners of various levels of expertise in a clinical setting, we also studied nurse practitioners and physician assistants. The details and insights emerging from this are presented below.

## Experimental Design

To recruit real nurse practitioners and physician assistants through Qualtrics, we had to abbreviate the time required to complete the task; the new experiment included only three of the six previously designed patient cases. The three selected cases were based on a review by associate chief of nursing research Jill Paul Massengale, James A. Haley Veterans Hospital, Tampa, Florida, for ensuring fit with this population.

For the first two cases, the participants were asked to summarize the patient cases. Participants were then asked to prescribe a treatment for the third patient case. Using a similar recommender system design as in the physician experiment, participants were prompted to view and adopt cost-effective treatment alternatives.

The new experiment included only three patient cases that required less time to complete than the physician experiment. We therefore made the time pressure treatment stronger. To operationalize the time pressure treatment, we used a pilot phase that kept track of the top three best completion times.

For participants in the high time pressure groups, we added a competitive element by tracking their performance (completion time) percentile. The time pressure treatment was represented by the presence/absence of the percentile information message as follows:

Through this experiment, you are given the opportunity to benchmark your performance:

The current best times for completion were between 5 minutes 43 seconds and 7 minutes 54 seconds. If you complete the experiment in this range (or better) you will be considered an “A+ Grade Level Star Performer.” If you complete close enough to this range you will be considered an “A Grade Level Performer.” If you take much more time to finish, you will be considered to be a “B Grade Level Performer.” Your performance level will be displayed at the end of the experiment.

The method was adapted from the incentive approach used in prior time pressure experiment research (Kocher and Sutter 2006). The relative cost treatments were duplicated from the physician experiment. Depending on their group, participants viewed either all low cost or mixed cost treatment alternatives.

For this experiment, we used a 2×2 experiment design. Unlike the physician’s experiment where we had a limited number of participants (real physicians), for this study we recruited a larger sample of nurse practitioners and physician assistants through Qualtrics. For a total amount of approximately \$5,000 we were able to recruit 120 practicing nurses and physician assistants (verified by Qualtrics) but for a limited time to complete the experiment (the cost would have been substantially larger if we had required this group to do what our sample of physicians did, for instance, which was reviewing six cases each). Therefore, we opted for a between subject design for both the cost and time pressure treatments (Table 6). In each of the four treatment groups, participants were presented with three patient cases. A counterbalanced design was used to control for the order effect. The order in which the patient cases were presented varied in sequence.

## Experiment Procedure

These participants were first presented with an informed consent agreement page describing the purpose of the study, the study procedures, alternatives to participation, compensation, and contact information. Participant identities remained anonymous. Next, each participant was presented with two fictional patient cases, where they were asked to summarize the cases. The participants were then presented with a third case and were prompted to provide a summary and also prescribe a treatment. They were then prompted to view the system recommendation and were given the opportunity to adjust their treatment plan.

Table 6. Recommendations Costs and Time Pressure Treatments

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Treatment 1: Time Pressure</td></tr><tr><td>High TP</td><td>Low TP</td></tr><tr><td rowspan="2">Treatment 2: Recommendation Costs</td><td>Mixed Costs</td><td>Group 1</td><td>Group 2</td></tr><tr><td>Low Costs</td><td>Group 3</td><td>Group 4</td></tr></table>

Notes: Participants were randomly placed in each of the treatment groups.  
Each subject within the groups was presented with the same cases 1 through 3.

Participants were randomly placed into different groups. Depending on their group assignment, participants were presented with either (1) mixed-cost alternatives or (2) low-cost alternatives, and experienced either (1) high time pressure or (2) low time pressure. Follow-up survey questions were presented to capture a participant’s designation and years of experience.

## Subjects

A total of 120 nurse practitioners and physician assistants who had prescription privileges were recruited for this experiment. As indicated by the profiles (Figure 2), this cohort of participants included mostly nurse practitioners (88%), most with over 10 years of experience (68%).

## Experiment Results

## Descriptive Statistics

A total of 120 observations were collected for analyzing the two dependent variables: recommendation viewing and treatment adjustment. Two predictor variables were measured: recommendation cost and time pressure level. Participant designation and years of experience were used as control variables.

Overall, 114 out of 120 physician assistants and nurse practitioners in this cohort viewed system recommendations, and 79 of the 114 who viewed recommendations adjusted their treatment options. This indicated an even higher rate of adoption of system recommendations compared to that of physicians.

## Manipulation Checks

To check for the cost framing manipulation, participants were asked through a post-experiment questionnaire whether they had noticed cost information. Observations (a total of 15) corresponding to participants who reported not noticing cost information were replaced. To check for the time pressure treatment manipulation, we conducted a pilot phase with ten participants (five in the low time pressure group, and five in the high time pressure group). We then calculated the average and standard deviation of the completion time: (14.75 minutes, 7.45 minutes) for the high time pressure group and (19.63 minutes, 9.49 minutes) for the low time pressure group. These values provided a range for adequate completion times. In this experiment, we used the mean + or – one standard deviation (versus two standard deviations for physicians). This is because of variance in the overall length of the experiment. The physician’s experiment included six patient cases, whereas the nurse practitioner and physician assistant experiments included only three patient cases, for which only prescription selection was needed. Based on these results, observations in the high time pressure groups that lasted more than 22 minutes (14.68 + 7.45) were replaced (a total of four observations), while observations in the low time pressure groups that lasted less than 10 minutes (19.63 – 9.49) were replaced (a total of seven observations).

We note here that additional participants were also recruited through Qualtrics. Even though the experiment was anonymous, Qualtrics kept an internal identifier to ensure that no participant completed the experiment more than once.

We also went through a systematic procedure reviewing responses for quality. This was necessary, in part because we recruited this sample from Qualtrics, a third-party (unlike in our prior physician experiments where we directly recruited the experts). For the first two cases, we had asked participants to summarize the patient cases. These summaries were used to assess the validity of the responses and the expertise of participants. Observations (a total of 14) that provided incomplete or inadequate summaries of the cases were replaced. In addition, the total time spent to complete the experiment was used as another quality indicator. Observations that were completed in less than 5 minutes (a total of two observations) were replaced. Also, observations that had more than 45 minutes (a total of five observations) were assumed to have been completed in more than one sitting, and were therefore replaced as well.

![](/api/attachments/HTNG7CNN/fulltext/images/443267be46753579eee2f5f9d7869e064fe452c0a4995b1ec438b4ab1ce3aa87.jpg)  
Figure 2. Participant Profiles

![](/api/attachments/HTNG7CNN/fulltext/images/d29964d553bf9e7d2e6c1b2caede8496a67e839d3c19b278b59cee84db14b0b8.jpg)

<table><tr><td colspan="5">Table 7. Descriptive Statistics</td></tr><tr><td>Variable</td><td>Levels</td><td>N</td><td>View Mean (Std. Var.)</td><td>Adjust Mean (Std. Var.)</td></tr><tr><td colspan="5">Independent Variables</td></tr><tr><td rowspan="2">Recommendations Costs</td><td>1: Mixed Costs</td><td>60</td><td>0.933 (0.251)</td><td>0.600 (0.494)</td></tr><tr><td>0: Low Costs</td><td>60</td><td>0.966 (0.181)</td><td>0.717 (0.454)</td></tr><tr><td rowspan="2">Time Pressure Level</td><td>1: High TP</td><td>60</td><td>0.9000 (0.303)</td><td>0.617 (0.490)</td></tr><tr><td>0: Low TP</td><td>60</td><td>1.000 (0.000)</td><td>0.700 (0.462)</td></tr><tr><td colspan="5">Control Variables</td></tr><tr><td rowspan="2">Designation</td><td>1: Nurse Practitioner</td><td>106</td><td>0.953 (0.213)</td><td>0.660 (0.476)</td></tr><tr><td>0: Physician Assistant</td><td>14</td><td>0.929 (0.267)</td><td>0.643 (0.497)</td></tr><tr><td rowspan="5">Years of Experience</td><td>5: 15+ years</td><td>62</td><td>0.952 (0.216)</td><td>0.645 (0.482)</td></tr><tr><td>4: 10–5 years</td><td>20</td><td>1.000 (0.000)</td><td>0.700 (0.470)</td></tr><tr><td>3: 6–9 years</td><td>13</td><td>0.923 (0.277)</td><td>0.615 (0.506)</td></tr><tr><td>2: 3–6 years</td><td>13</td><td>0.923 (0.277)</td><td>0.615 (0.506)</td></tr><tr><td>1: 0–3 years</td><td>12</td><td>0.917 (0.289)</td><td>0.750 (0.452)</td></tr></table>

## Statistical Findings

To investigate the impacts of time pressure on viewing of recommendations and cost framing on treatment adjustments for this cohort, we created two models for each independent variable. The first model included control variables only, while the second model included control as well as predictor variables. Similar to physician experiment data analysis, we also created a two-stage model to account for endogeneity between the viewing and adjustment dependent variables.

Results showed no significant effects of mixed-cost framing on the treatment adjustment behavior, but nurse practitioners and physician assistants were more likely to be cost-sensitive than physicians (see Table 8). Essentially, they appeared to change more often as long as cheaper options were available, and the framing (mixed costs versus all-low cost) did not appear to matter.

Unlike the physicians, participants in this cohort showed a high impact of time pressure on the use of the recommender system, suggesting that the extra cognitive load imposed by the cost information affected the participants’ decisions to consider system alternatives. This suggests that these clinicians may not be able to process additional information as well as physicians do under time pressure. There are important implications for system design suggesting a need for possibly adapting clinical systems to suit user types.

## Discussion

Our results indicate that medical recommender systems in healthcare can play a significant role in lowering pharmacy costs if designed appropriately. Displaying treatment options that are of higher or equivalent efficacy than the treatments prescribed, along with providing accurate cost information can work in most cases. For context on potential value, a recent study on excess prescription costs (Van Nuys et al. 2018), estimated the average overpayment on medications to be about \$4.98 in Medicare Part D 2013. With a total of 40,634,384 pharmacy claims that year, adoption of comparable-outcome cost-effective options, similar to the ones presented in this study, could have generated savings totaling \$202,359,232.32 in Medicare alone.

<table><tr><td rowspan="2"></td><td colspan="2">Viewership Models</td><td colspan="2">Adjustment Models</td><td colspan="2">Heckman Model</td></tr><tr><td>Model 1</td><td>Model 2</td><td>Model 1</td><td>Model 2</td><td>Stage 1</td><td>Stage 2</td></tr><tr><td colspan="7">Control Variable</td></tr><tr><td>Designation (1)</td><td>0.38(0.7030)</td><td>0.51(0.6098)</td><td>0.15(0.8808)</td><td>0.23(0.8213)</td><td>0.38(0.7018)</td><td>0.08(0.9374)</td></tr><tr><td>Years of Experience (1)</td><td>-0.47(0.6350)</td><td>-0.51(0.6098)</td><td>0.71(0.4753)</td><td>0.53(0.5963)</td><td>0.54(0.5882)</td><td>-0.51(0.6116)</td></tr><tr><td>Years of Experience (2)</td><td>-0.47(0.6350)</td><td>-0.03(0.9754)</td><td>-0.20(0.8441)</td><td>-0.21(0.8366)</td><td></td><td></td></tr><tr><td>Years of Experience (3)</td><td>-0.41(0.6816)</td><td>-0.73(0.4653)</td><td>0.21(0.8345)</td><td>-0.27(0.7887)</td><td></td><td></td></tr><tr><td>Years of Experience (4)</td><td>-0.43(0.6641)</td><td></td><td>0.45(0.6526)</td><td>0.45(0.6497)</td><td></td><td></td></tr><tr><td>Predictor Variable</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Time Pressure Level (1)</td><td></td><td>-22.03***(&lt;0.0001)</td><td></td><td></td><td>-19.78***(&lt;0.0001)</td><td></td></tr><tr><td>Recommendations Costs (1)</td><td></td><td></td><td></td><td>-1.29(0.1983)</td><td></td><td>-1.07(0.2858)</td></tr><tr><td>Lambda</td><td></td><td></td><td></td><td></td><td></td><td>-0.36(07164)</td></tr><tr><td colspan="7">Performance Measure</td></tr><tr><td>Log Likelihood</td><td>-22.435</td><td>-18.287</td><td>-76.602</td><td>-75.770</td><td>-19.286</td><td></td></tr><tr><td>AIC</td><td>56.87</td><td>50.57</td><td>165.20</td><td>165.54</td><td>46.572</td><td>-168.071</td></tr></table>

Notes: \*p < .05; \*\*p < .01; \*\*\*p < .001; Standard errors are in parentheses.  
Model 1: Base model with control variables only; Model 2: Model with control variables and main effects.  
Heckman Model Stage 1: Selection model with controls and the exclusion restriction time pressure variable. Heckman Model Stage 2: Main adjustment model given View = 1.

Our interviews of medical practitioners confirmed the lack of knowledge of drug costs and also indicated the lack of focus on reducing costs in general. Hence in addition to implementing cost-aware recommender systems, more effort needs to be put in place to sensitize doctors on the broader cost issue. Importantly, the adoption of cost-sensitive recommendations can significantly impact overall healthcare spending, given how strong our experimental results were in creating change, when providers are cost-aware. However, time pressure can be important to consider for nurse practitioners and physician assistants, a population that appears to be more likely to favor lower cost options in general, when prescribing. In that sense, ensuring that they continue to have adequate time during patient interactions can be both desirable from an overall patient perspective and also from a cost-savings perspective.

Our study also offers important theoretical contributions related to the effects of cost framing and time pressure on the use of recommender systems. Experimental results suggested that most medical practitioners who have prescription privileges do switch to lower cost options when they appear to have the same (or better) efficacy. Yet, results on the effects of cost framing showed interesting differences in recommendation adoption between the types of practitioners. While nurse practitioners and physician assistants switched to lower cost options regardless of cost framing, physicians did seem more affected by mixed-cost framing, changing more often if all options were cheaper then their original prescription. The physician experiment results confirmed the propositions made based on the adaptation level and reference price effects. As expected, the mixed cost framing seemed to increase the physician’s reference price, thereby triggering less adoption of cost-effective recommendations. Extending prior marketing literature on price framing, our results indicated the presence of such effects in the context of healtthcare, where practitioners made decisions on behalf of their patients.

We conjecture that the variance in the effect of cost framing on recommendation adoption could be explained by one of several reasons. It could be the case that physicians have limited to no knowledge of drug costs compared to nurse practitioners and physician assistants. Alternatively, it is also possible that nurse practitioners and physician assistants who already favor lower cost options are affected more by costframing, perhaps suggesting that the reference price effect may be affected by prior disposition. The potential moderating effect of user attributes, prior disposition and experience has not been well explored in this work and could be an important direction for future research to extend the literature on adaptation level theory and recommender system design.

Experimental results also indicated that time pressure appears to play a role for nurses and physician assistants but not for physicians, who are likely used to this in their professional lives. The extra cognitive demands exerted by cost information did drive physician assistants and nurse practitioners to dismiss cost-aware recommendations. Somewhat unexpected based on the general theory in the time pressure context, these same information overloads (cost information) did not have an effect on physicians. Physicians did not seem to filter information or switch to defaults. This may be due to the difference in training, where physicians are taught to work under time pressure. While we did not explicitly investigate the moderating effect of user attributes and experience under time pressure, these could be fruitful directions for research as well.

These results also provide valuable insights for recommender system design. In prior health systems literature, researchers have focused on the effectiveness of recommender systems on improving health outcomes by providing diagnoses, treatments, and nursing plans (Duan et al. 2011). To our knowledge no study has looked at cost-aware health recommender systems for providers. Initial attempts to evaluate the cost transparency effect included costs in the computer provider order entry (CPOE) systems. Yet studies using CPOEs focus only on lower cost alternatives, generics (Kuperman et al. 2007), and do not take into account variance in costs caused by patient insurance plans. The prototype used in our experiments shows the feasibility of designing cost-aware health recommender systems using same drug-class alternatives, which can potentially reduce costs while maintaining health outcomes.

We find that the design of cost-aware recommender systems might need to be adapted to fit user attributes and experience. While showing treatment options along with cost information is likely an effective way to both help patients and lower costs, adoption and effectiveness of this approach to lower costs appears to depend somewhat on the type of user (physician versus nurse practitioner or physician assistant). There is not much work in the recommender systems area on how much information to show in the recommendations themselves, but we do see that it matters, and quite significantly in the healthcare setting. Our results also confirm the importance of context in recommendation adoption (Adomavicius and Tuzhilin 2011, 2015). Since time pressure seems to affect recommendation adoption among certain practitioners, an important policy issue to address in the future is therefore the time allocated for consultation, which should incorporate the time needed to process the additional cost information provided by the system.

We acknowledge several limitations of this study. The sample sizes in the experiments were relatively small due to the nature of the domain. Medical practitioners are extremely busy and not easy to recruit for experiments. We note that prior information systems research involving real health practitioners has also limited the number of participants to less than 100 (Dennis and Garfield 2003; Davidson and Chismar 2007; Kohli and Kettinger 2004; Lapointe and Rivard 2005; Paul and McDaniel 2004). In psychology, several high impact experimental studies have also limited the number of participants to less than 50 subjects per experiment (Ben Zur and Breznitz 1981; Payne 1976; Payne et al. 1988; Strack and Mussweiler 1997). Our sample distribution did follow a similar distribution as the overall population of physicians with the majority of the participants specializing in internal medicine. Our cohort of subjects, however, consisted mostly of highly experienced practitioners, which might have biased our results. Medical residents and less experienced physicians might react differently to the recommendations provided by the system.

The medical cases used in the experiments pertained to primary care, thereby limiting generalizability. Future research is needed to assess the influence of such cost-sensitive recommendations on practitioners of different specialties, where cost variance among similar-outcome alternatives may be more relevant, and where time pressure might be more significant. As is the case for all experiments, there is also the limitation that these findings may not be generalizable to a real practice. Future research involving a field study can help provide more accurate estimates of the time pressure and cost framing in real settings.

Potential biases might have been introduced by the experiment design. Unlike traditional recommender systems, our prototype did not provide information about the behavior of fellow practitioners. Such information might have impacted the adoption of a recommendation, with more probability of adopting the most popular alternatives, regardless of costs. Also, although our experiments allowed us to examine the effects of cost framing on cost-effective recommendation adoption, we note that the experiments did not explicitly cap ture reference prices, as it would have imposed additional time to complete the experiments by participants. Further, measuring the reference price would have also made the system’s design in the experimental setting different than the one in the real setting. Because of the difficulty in recruiting physicians to complete our experiments, we also used a repeated-measures design. The design enabled us to collect 192 observations with only 32 participants. In order to isolate the effects of the practitioners’ perceived medication value on the recommendation adoption, we did not brief participants about recommendation costs before the experiment. However, the repeated measures design could have introduced a learning bias, where participants learned the type of recommendations (low costs versus mixed costs) presented by the system. We were able to alleviate this repeated measure issue in the nurse practitioner and physician assistant experiment, where we reduced the number of patient cases to one and increased the number of participants. However, the difference in experiment design might have introduced a variance in response to the time pressure treatment. Furthermore, the adoption of a system recommendation may have been impacted by external factors. The U.S. government’s emphasis on reducing prescription drug costs (Obama 2016) at the time of experiments could also have explained the high inclination of viewing and adoption of cost-sensitive recommendations. As with most research in new areas, many of these limitations can be addressed by additional studies that replicate or extend our work.

## Conclusion

This paper provides an understanding of a medical practitioner’s use of cost information presented through recommender systems. Driven by three separate studies involving a total of 160 medical practitioners of various types, we provide important insights regarding the roles of time pressure and cost transparency in using recommender systems to lower healthcare costs. Broadly, we show the overall tendency to lower costs when cost comparisons are provided. This is significant, given that use of such information is fairly uncommon in practice today. When designed well, recommender systems that incorporate treatment costs can result in significant cost savings, while providing similar or better health outcomes. Scenarios where practitioners do not feel time pressure and have access to accurate cost information are most conducive for adopting recommendations and creating change. We also present some directions for theory-building that can incorporate user experience, attributes and prior disposition to better understand the roles of framing in recommender systems.

Our research makes broad contributions to both information systems and healthcare. When viewing recommender systems as artifacts designed to bring about change, we show how the effectiveness of this change depends on both the information presented by the system and the overall context in which the system operates. Hence, trying to optimize one (i.e., display cost information) without accounting for the context (i.e., considering time pressure) is likely to be less effective for reasons discussed in this paper.

Recently, there have been several initiatives to reduce healthcare costs in the United States, suggesting the importance and urgency of the issue. Our findings suggest that presenting similar-outcome low-cost alternatives to practitioners at the time of prescription, would be well adopted by clinicians in practice, leading to an overall reduction in healthcare costs.

## References

Adomavicius, G., Bockstedt, J. C., Curley, S. P., and Zhang, Z. 2013. “Do Recommender Systems Manipulate Consumer Preferences? A Study of Anchoring Effects,” Information Systems Research 24 (4), pp. 956-975.

Adomavicius, G., and Tuzhilin, A. 2011. “Context-Aware Recommender Systems,” in Recommender Systems Handbook, F. Ricci, L. Rokach, B. Shapira, and P. B. Kantor (eds.), Boston: Springer, pp. 217-253.

Adomavicius, G., and Tuzhilin, A. 2015. “Context-Aware Recommender Systems,” in Recommender Systems Handbook, F. Ricci, L. Rokach, and B. Shapira (eds.), Boston: Springer, pp. 191-226.

Ahluwalia, J. S., Montie, S., Weisenberger, L., Bernard, A. M., McNagny, S. E. 1996. “Changing Physician Prescribing Behavior: A Low-Cost Administrative Policy That Reduced the Use of Brand Name Nonsteroidal Anti-Inflammatory Drugs,” Preventive Medicine (25:6), pp. 668-672.

Alexander, G. C., Casalino, L. P., and Meltzer, D. O. 2005. “Physician Strategies to Reduce Patients’ Out-of-Pocket Prescription Costs,” Archives of Internal Medicine (165:6), pp. 633-636.

Allan, G. M., Lexchin, J., and Wiebe, N. 2007. “Physician Awareness of Drug Cost: A Systematic Review,” PLOS Medicine 4 (9), p. e283 (https://doi.org/10.1371/journal.pmed.0040283).

Awdishu, L., Coates, C. R., Lyddane, A., Tran, K. Daniels, C. E., Lee, J., and Kareh, R. E. 2016. “The Impact of Real-Time Alerting on Appropriate Prescribing in Kidney Disease: A

Cluster Randomized Controlled Trial,” Journal of the American Medical Informatics Association (23:3), pp. 609-616.

Ballinger, G. A. 2004. “Using Generalized Estimating Equations for Longitudinal Data Analysis,” Organizational Research Methods (7:2), pp. 127-150.

Bell, D. R., and Lattin, J. M. 2000. “Looking for Loss Aversion in Scanner Panel Data: The Confounding Effect of Price Response Heterogeneity,” Marketing Science (19:2), pp. 185-200.

Ben Zur, H., and Breznitz, S. J. 1981. “The Effect of Time Pressure on Risky Choice Behavior,” Acta Psychologica (42:), pp. 89-104.

Bobadilla-Suarez, S., and Love, B. C. 2018. “Fast or Frugal, but Not Both: Decision Heuristics under Time Pressure,” Journal of Experimental Psychology. Learning, Memory, and Cognition (44:1), pp. 24-33.

Briggs, D. C. 2004. “Causal Inference and the Heckman Model,” Journal of Educational and Behavioral Statistics (29:4), pp. 397-420.

Buerhaus, P. I., DesRoches, C. M., Dittus, R., and Donelan, K. 2015. “Practice Characteristics of Primary Care Nurse Practitioners and Physicians,” Nursing Outlook (63:2), pp. 144-153.

Cosley, D., Lam, S. K., Albert, I., Konstan, J. A., and Riedl, J. 2003. “Is Seeing Believing? How Recommender System Interfaces Affect Users’ Opinions,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York: ACM, pp. 585-592.

Davidson, E. J., and Chismar, W. G. 2007. “The Interaction of Institutionally Triggered and Technology-Triggered Social Structure Change: An Investigation of Computerized Physician Order Entry,” MIS Quarterly (31:4), pp. 739-758.

Davis, D. A., Chawla, N. V., Blumm, M., Christakis, N., and Barabasi, A-L. 2008. “Predicting Individual Disease Risk Based on Medical History,” in Proceedings of the 17<sup>th</sup> ACM Conference on Information and Knowledge Management, New York: ACM, pp. 769-778.

Dennis, A. R., and Garfield, M. J. 2003. “The Adoption and Use of GSS in Project Teams: Toward More Participative Processes and Outcomes,” MIS Quarterly (27:2), pp. 289-323.

Drescher, F. S., Chandrika, S., Weir, I. D., Weintraub, J. T., Berman, L., Lee, R., Van Buskirk, P. D., Wang, Y., Adewunmi, A., and Fine, J. M. 2011. “Effectiveness and Acceptability of a Computerized Decision Support System Using Modified Wells Criteria for Evaluation of Suspected Pulmonary Embolism,” Annals of Emergency Medicine (57:6), pp. 613-621.

Duan, L., Street, W. N., and Xu, E. 2011. “Healthcare Information Systems: Data Mining Methods in the Creation of a Clinical Recommender System,” Enterprise Information Systems (5:2), pp. 169-181.

Dugdale, D. C., Epstein, R., and Pantilat, S. Z. 1999. “Time and the Patient–Physician Relationship,” Journal of General Internal Medicine (14:S1), pp. 34-40.

Ely, J. W., Osheroff, J. A., Ebell, M. H., Bergus, G. R., Levy, B. T., Chambliss, M. L., and Evans, E. R. 1999. “Analysis of Questions Asked by Family Doctors Regarding Patient Care,” BMJ (319:7206), pp. 358-361.

Emery, F. 1970. “Some Psychological Aspects of Price,” in Pricing Strategy, B. Taylor and G. Wills (eds.), Princeton, NJ: Brandon/Systems Press, pp. 98-111.

Gibson, T. B., Ozminkowski, R. J., and Goetzel, R. Z. 2005. “The Effects of Prescription Drug Cost Sharing: A Review of the Evidence,” The American Journal of Managed Care (11:11), pp. 730-740.

Glickman, L., Bruce, E. A., Caro, F. G., and Avorn, J. 1994. “Physicians’ Knowledge of Drug Costs for the Elderly,” Journal of the American Geriatrics Society (42:9), pp. 992-996.

Goldstein, N. J., Cialdini, R. B., and Griskevicius, V. 2008. “A Room with a Viewpoint: Using Social Norms to Motivate Environmental Conservation in Hotels,” Journal of Consumer Research (35:3), pp. 472-482.

Gönül, F. F., Carter, F., Petrova, E., and Srinivasan, K. 2001. “Promotion of Prescription Drugs and its Impact on Physicians Choice Behavior,” Journal of Marketing (65:3), pp. 79-90.

Grewal, D., Krishnan, R., Baker, J., and Borin, N. 1998. “The Effect of Store Name, Brand Name and Price Discounts on Consumers’ Evaluations and Purchase Intentions,” Journal of Retailing, Research Perspective on Retail Pricing (74:3), pp. 331-352.

Grewal, D., Monroe, K. B., and Krishnan, R. 1998. “The Effects of Price-Comparison Advertising on Buyers’ Perceptions of Acquisition Value, Transaction Value, and Behavioral Intentions,” Journal of Marketing (62:2), pp. 46-59.

Guterman, J. J., Chernof, B. A., Mares, B., Gross-Schulman, S. G., Gan, P. G., and Thomas, D. 2002. “Modifying Provider Behavior,” Journal of General Internal Medicine (17:10), pp. 792-796.

Haas, J. S., Phillips, K. A., Gerstenberger, E. P., and Seger, A. C. 2005. “Potential Savings from Substituting Generic Drugs for Brand-Name Drugs: Medical Expenditure Panel Survey, 1997- 2000,” Annals of Internal Medicine (142:11), pp. 891-897.

Hahn, M., Lawson, R., and Lee, Y. G. 1992. “The Effects of Time Pressure and Information Load on Decision Quality,” Psychology and Marketing (9:5), pp. 365-378.

Heckman, J. J. 1979. “Sample Selection Bias as a Specification Error,” Econometrica (47:1), pp. 153-161.

Helson, H. 1947. “Adaptation-Level as Frame of Reference for Prediction of Psychophysical Data,” The American Journal of Psychology (60:1), pp. 1-29.

Helson, H. 1964. Adaptation-Level Theory: An Experimental and Systematic Approach to Behavior, New York: Harper.

Hoffer, E. K. 2015. “Goals of Displaying Health Care Prices to Physicians,” JAMA (313:7), pp. 728-728.

Hoffman, J., Barefield, F. A., and Ramamurthy, S. 1995. “A Survey of Physician Knowledge of Drug Costs,” Journal of Pain and Symptom Management (10:6), pp. 432-435.

Hooker, R. S. 2006. “Physician Assistants and Nurse Practitioners: The United States Experience,” The Medical Journal of Australia (185:1), pp. 4-7.

Horn, D. M., Koplan, K. E., Senese, M. D., Orav, E. J., and Sequist, T. D. 2013. “The Impact of Cost Displays on Primary Care Physician Laboratory Test Ordering,” Journal of General Internal Medicine (29:5), pp. 708-714.

Horrocks, S., Anderson, E., and Salisbury, C. 2002. “Systematic Review of Whether Nurse Practitioners Working in Primary Care Can Provide Equivalent Care to Doctors,” BMJ (324:7341), pp. 819-823.

Johnson, E. J., and Goldstein, D. G. 2004. “Defaults and Donation Decisions,” Transplantation (78:12), pp. 1713-1716.

Joyce, G. F., Escarce, J. J., Solomon, M. D., and Goldman, D. P. 2002. “Employer Drug Benefit Plans and Spending on Prescription Drugs,” JAMA (288:14), pp. 1733-1739.

Kesselheim, A. S., Eddings, W., Raj, T., Campbell, E. G., Franklin, J. M., Ross, K. M., Fulchino, L. A., Avorn, J., and Gagne, J. J. 2016. “Physicians’ Trust in the FDA’s Use of Product-Specific Pathways for Generic Drug Approval,” PLOS ONE (11:10), p. e0163339 ( https://doi.org/10.1371/journal.pone.0163339).

Kinnersley, P., Anderson, E., Parry, K., Clement, J., Archard, L., Turton, P., Stainthorpe, A., Fraser, A., Butler, C. C., and Rogers, C. 2000. “Randomised Controlled Trial of Nurse Practitioner Versus General Practitioner Care for Patients Requesting ‘Same Day’ Consultations in Primary Care,” BMJ (320:7241), pp. 1043-1048.

Kocher, M. G., and Sutter, M. 2006. “Time Is Money—Time Pressure, Incentives, and the Quality of Decision-Making,” Journal of Economic Behavior & Organization (61:3), pp. 375-392.

Kohli, R., and Kettinger, W. J. 2004. “Informating the Clan: Controlling Physicians’ Costs and Outcomes,” MIS Quarterly (28:3), pp. 363-394.

Kuo, Y-F., Chen, N-W., Baillargeon, J., Raji, M. A., and Goodwin, J. S. 2015. “Potentially Preventable Hospitalizations in Medicare Patients with Diabetes: A Comparison of Primary Care Provided by Nurse Practitioners Versus Physicians,” Medical Care (53:9), pp. 776-783.

Kuperman, G. J., Bobb, A., Payne, T. H., Avery, A. J., Gandhi, T. K., Burns, G., Classen, D. C., and Bates, D. W. 2007. “Medication-Related Clinical Decision Support in Computerized Provider Order Entry Systems: A Review,” Journal of the American Medical Informatics Association (14:1), pp. 29-40.

Landry, C. F. 2015. “The Impacts of Time Pressure and Emotion on the Information Behavior of High Stakes Decision Makers: The Home Buying Experience,” Unpublished Ph.D. Thesis, University of Washington (https://digital.lib.washington.edu: 443/researchworks/handle/1773/27509).

Lapointe, L., and Rivard, S. 2005. “A Multilevel Model of Resistance to Information Technology Implementation,” MIS Quarterly (29:3), pp. 461-491.

Laurant, M., Reeves, D., Hermens, R., Braspenning, J., Grol, R., and Sibbald, B. 2005. “Substitution of Doctors by Nurses in Primary Care,” Cochrane Database of Systematic Reviews (2) (https://doi.org/10.1002/14651858.CD001271.pub2).

Liang, K-Y., and Zeger, S. L. 1986. “Longitudinal Data Analysis Using Generalized Linear Models,” Biometrika (73:1), pp. 13-22.

Linzer, M., Konrad, T. R., Douglas, J., McMurray, J. E., Pathman, D. E., Williams, E. S., Schwartz, M. D., Gerrity, M., Scheckler, W., Bigby, J. A., and Rhodes, E. 2000. “Managed Care, Time Pressure, and Physician Job Satisfaction: Results from the Physician Worklife Study,” Journal of General Internal Medicine (15:7), pp. 441-450.

Liu, Y., Polman, E., Liu, Y., and Jiao, J. 2018. “Choosing for Others and its Relation to Information Search,” Organizational

Behavior and Human Decision Processes (147:July), pp. 65-75.

Martin, A. B., Hartman, M., Washington, B., Catlin, A., and the National Health Expenditure Accounts Team. 2016. “National Health Spending: Faster Growth in 2015 as Coverage Expands and Utilization Increases,” Health Affairs (36:1) (https:// www.healthaffairs.org/doi/full/10.1377/hlthaff.2016.1330).

McGuire, C., King, S., Roche-Nagle, G., and Barry, M. C. 2009. “Doctors’ Attitudes about Prescribing and Knowledge of the Costs of Common Medications,” Irish Journal of Medical Science (178:3), Article 277.

Monroe, K. B. 1973. “Buyers’ Subjective Perceptions of Price,” Journal of Marketing Research (10:1), pp. 70-80.

Monroe, K. B., and Chapman, J. D. 1987. “Framing Effects on Buyers’ Subjective Product Evaluations,” Advances in Consumer Research (14), pp. 193-197.

Morris, M. G., and Venkatesh, V. 2010. “Job Characteristics and Job Satisfaction: Understanding the Role of Enterprise Resource Planning System Implementation,” MIS Quarterly (34:1), pp. 143-161.

Mundinger, M. O. 1994. “Advanced-Practice Nursing—Good Medicine for Physicians?,” The New England Journal of Medicine (330), pp. 211-214.

Naylor, M. D., and Kurtzman, E. T. 2010. “The Role Of Nurse Practitioners In Reinventing Primary Care,” Health Affair (29:5), pp. 893-899.

Obama, B. 2016. “United States Health Care Reform: Progress to Date and Next Steps,” JAMA (316:5), pp. 525-532.

O’Campo, P., Gielen, A. C., Faden, R. R., Xue, X., Kass, N., and Wang, M. C. 1995. “Violence by Male Partners against Women During the Childbearing Year: A Contextual Analy sis,” American Journal of Public Health (85), pp. 1092-1097.

Olson, M. 1965. The Logic of Collective Action: Public Goods and the Theory of Groups, Cambridge, MA: Harvard University Press.

Ornstein, S. M., MacFarlane, L. L., Jenkins, R. G., Pan, Q., and Wager, K. A. 1999. “Medication Cost Information in a Computer-Based Patient Record System: Impact on Prescribing in a Family Medicine Clinical Practice,” Archives of Family Medicine (8:2), pp. 118-121.

Ostrom, E. 2014. “Collective Action and the Evolution of Social Norms,” Journal of Natural Resources Policy Research (6:4), pp. 235-252.

Paul, D. L., and McDaniel, R. D. 2004. “A Field Study of the Effect of Interpersonal Trust on Virtual Collaborative Relationship Performance,” MIS Quarterly (28:2), pp. 183-227.

Payne, J. W. 1976. “Task Complexity and Contingent Processing in Decision Making: An Information Search and Protocol Analysis,” Organizational Behavior and Human Performance (16:2), pp. 366-387.

Payne, J. W., Bettman, J. R., and Johnson, E. J. 1988. “Adaptive Strategy Selection in Decision Making,” Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), pp. 534-552.

Polman, E. 2010. “Information Distortion in Self-Other Decision Making,” Journal of Experimental Social Psychology (46:2), pp. 432-435.

Polman, E. 2012. “Effects of Self-Other Decision Making on Regulatory Focus and Choice Overload,” Journal of Personality and Social Psychology (102:5), pp. 980-993.

Posner, R. A. 1997. “Social Norms and the Law: An Economic Approach,” The American Economic Review (97:2), pp. 365-369.

Rajendran, K. N., and Tellis, G. J. 1994. “Contextual and Temporal Components of Reference Price,” Journal of Marketing (58:1), pp. 22-34.

Ramos, K., Linscheid, R., and Schafer, S. 2003. “Real-Time Information-Seeking Behavior of Residency Physicians,” Family Medicine (35:4), pp. 257-260.

Reichert, S., Simon, T., and Halm, E. A. 2000. “Physicians’ Attitudes About Prescribing and Knowledge of the Costs of Common Medications,” Archives of Internal Medicine (160:18), pp. 2799-2803.

Riggs, K. R., and DeCamp M. 2014. “Providing Price Displays for Physicians: Which Price Is Right?,” JAMA (312:16), pp. 1631-1632.

Roblin, D. W., Becker, E. R., Adams, E. K., Howard, D. H., and Roberts, M. H. 2004. “Patient Satisfaction with Primary Care: Does Type of Practitioner Matter?,” Medical Care (42:6), pp. 579-590.

Schneeweiss, S., and Avorn, J. 2005. “A Review of Uses of Health Care Utilization Databases for Epidemiologic Research on Therapeutics,” Journal of Clinical Epidemiology (58:4), pp. 323-337.

Shaver, J. M. 1998. “Accounting for Endogeneity When Assessing Strategy Performance: Does Entry Mode Choice Affect FDI Survival?,” Management Science (44:4), pp. 571-585.

Shrank, W. H., Liberman, J. N., Fischer, M. A., Girdish, C., Brennan, T. A., and Choudhry, N. T. 2011. “Physician Perceptions About Generic Drugs,” Annals of Pharmacotherapy (45:1), pp. 31-38.

Shrank, W. H., Young, H. N., Ettner, S. L., Glassman, P., Asch, S. M., and Kravitz, R. L. 2005. “Do the Incentives in 3-Tier Pharmaceutical Benefit Plans Operate as Intended? Results From a Physician Leadership Survey,” American Journal of Managed Care (111:1) (http://www.ajmc.com/journals/ issue/2005/2005-01-vol11-n1/jan05-1975p016-022).

Strack, F., and Mussweiler, T. 1997. “Explaining the Enigmatic Anchoring Effect: Mechanisms of Selective Accessibility,” Journal of Personality and Social Psychology (73:3), pp. 437-446.

Thaler, R. H., Sunstein, C. R., and Balz, J. P. 2013. “Choice Architecture,” Chapter 25 in The Behavioral Foundations of Public Policy, E. Shafir (ed.), Princeton, NJ: Princeton University Press, pp. 428-439.

Van Nuys, K., Joyce, G., Ribero, R., and Goldman, D. 2018. “Overpaying for Prescription Drugs: The Copay Clawback Phenomenon,” University of Southern California, Leonard D. Schaeffer Center for Healty Policy & Economics (https:// healthpolicy.usc.edu/research/overpaying-for-prescriptiondrugs/).

Vedsted, P., Nielsen, J. N., and Olesen, F. 1997. “Does a Computerized Price Comparison Module Reduce Prescribing Costs in General Practice?,” Family Practice (14:3), pp. 199-203.

Venning, P., A. Durie, M. Roland, C. Roberts, and B. Leese. 2000. “Randomised Controlled Trial Comparing Cost Effectiveness of General Practitioners and Nurse Practitioners in Primary Care,” BMJ (320:7241), pp. 1048-1053.

Wechsler, H., Lee, J. E., Kuo, M., Seibring, M., Nelson, T. F., and Lee, H. 2002. “Trends in College Binge Drinking During a Period of Increased Prevention Efforts. Findings from 4 Harvard School of Public Health College Alcohol Study Surveys: 1993–2001,” Journal of American College Health (50:5), pp. 203-217.

Wright, P. 1974. “The Harassed Decision Maker: Time Pressures, Distractions, and the Use of Evidence,” Journal of Applied Psychology (59:5), pp. 555-561.

Ziegler, F. V., and Tunney, R. J. 2012. “Decisions for Others Become Less Impulsive the Further Away They Are on the Family Tree,” PLOS ONE (7:11), p. e49479 (https://doi.org/ 10.1371/journal.pone.0049479).

Zikmund Fisher, B., J., Sarr, B., Fagerlin, A., and Ubel, P. A. 2006. “A Matter of Perspective: Choosing for Others Differs from Choosing for Yourself in Making Treatment Decisions,” Journal of General Internal Medicine (21:6), pp. 618-622.

## About the Authors

Lina Bouayad is an associate professor in the Information Systems and Business Analytics Department at Florida International University and a Health Science Specialist at the Rehabilitation Outcomes Research Service at James A. Haley Veterans Hospital. Her research includes the design and application of algorithms to improve business outcomes. Lina has been involved in several HSR&D and NIH studies that aim at leveraging healthcare data to increase provider effectiveness and improve veterans’ care quality and experience.

Balaji Padmanabhan is the director of the Center for Analytics and Creativity at the University of South Florida’s Muma College of Business, the Anderson Professor of Global Management, and a professor in the Information Systems & Decision Sciences Department. Balaji’s specific interests and expertise include analytics and business intelligence, designing analytics algorithms for business applications, building and evaluating predictive models, patterns discovery in data, enabling citizen data science and applications of analytics in churn, healthcare, recommender systems, fraud detection, and elections.

Kaushal Chari serves as the Dean of the Sheldon B. Lubar School of Business at the University of Wisconsin–Milwaukee. Previously he served as the Associate Dean of research and professional programs for the University of South Florida’s Muma College of Business and chair of the Information Systems & Decision Sciences Department from 2006–2013. Kaushal’s research program covers three broad areas: software engineering, business intelligence, and distributed systems. He is interested in applying quantitative as well as intelligent techniques to address problems related to IT systems, software development and business process management.

## Appendix A

## Experiment Screenshots

![](/api/attachments/HTNG7CNN/fulltext/images/fe764790a2a4864bd65bc00d788d223bd17893d1bc86aef5567b2c7c11b855d3.jpg)

Visit Date: 02/11/2016 Visit Type: Problem Visit Visit Provider: YOU Primary Plan: BCBS

Problem List Status

Duodenal Ulcer Active

Medication List Dose

Prescribed within Practice

Ranitidine Maalox

150mg/12h 200-200-20mg/5mL

Prescribed outside Practice

Clinical Alerts

New Endoscopic Exam Needed

Vital Signs

Date BP HR RR T(F) Wt Ht 02 12/20/2014 124/788217 98.5146|bs 5'6"99% 3oz 04/07/2010 125/78 84 15 98.8145|bs 99% 5'6" 6oz

Chief Complaint • Epigastric Pain • Weight Loss

Figure A1. Sample Case (Part 1)

## History of Present Illness

James Smith is a 42 year old Caucasian male who presents today for recurrent epigastric pain treated in the last year with ranitidine. Patient experience loss of weight. He lost 5 pounds within the last month. Exacerbation of pain after meals. Patient has had endoscopic exam with biopsy that revealed the presence of 1 cm bulbar ulcer in the posterior part of the duodenum.

Past Medical History

Duodenal ulcer for 10 years

Family Medical History

Significant for DM Type I; Hypertensior

Social History

Significant for Caffeine (Current); College graduate, 2 year; Divorced; Exercises regularly

SOAP Note

VS Height: Weight: BMI: Blood Pressure Temp Pulse Resp Rate 64.0 in 140.3lb 22.6 130/78 mmHg 98.6 F 70 pbm 12 rpm

CC Epigastric pain, weight loss

S Here for follow up of epigastric pain. Experiencing nausea. Taking rantidine and antiacids.

General: Normotensive. Chest: Lungs show no rales, no wheezes, no rhonchi. Heart: no O mumrmurs. Abdomen: Soft, no tenderness, no masses, BS normal. Extremities: no deformities, no edema, no erythema. Neuro: Conscious, Monofilament Screen normal. Labs: all at target.

A Duodenal Ulcer

P TO BE DETERMINED

Figure A2. Sample Case (Part 2)

![](/api/attachments/HTNG7CNN/fulltext/images/e41294f15f8baa05ae56761421389568899e6985ee4028f633706f6ecb09077a.jpg)

## PLAN

Next. you will see a list of drugs to be prescribed for this patient. Please Select the medication list you view as most appropriate for this specific patient.

Note that this list might not be comprehensive.

## AminoPenicillin

## Macrolide

Nitroimidazole Antimicrobial

PPI

Prostaglandin E1 Analog

## Figure A3. Sample Treatment Plan Screen—Without Cost Information

## YOUR CURRENT PLAN STATISTICS

Medication, Expected Cost to the Patient(\$)

Amoxicot, \$200

Biaxin, \$250

Flagyl, \$300

Nexium, \$180

Cytotec, Cytotec, \$250

Would you like to see systems recommendations?

O YES

O NO

![](/api/attachments/HTNG7CNN/fulltext/images/bdb7318269f5365488462d24d2da162a1b67abb74bd4e52bb2247c5947637159.jpg)

![](/api/attachments/HTNG7CNN/fulltext/images/daaa0bd5fddf086be9ffb907aa4829249386af1d4d8b72e0b976839c1a588bc2.jpg)

## YOUR CURRENT PLAN STATISTICS

Medication, Expected Cost to the Patient(\$)

Amoxicot, \$200

Biaxin, \$250

Flagyl, \$300

□Nexium, \$180

Cytotec, Cytotec, \$250

## SYSTEM RECOMMENDED PLAN & STATISTICS

Please note that all the alternative procedures listed below have been previously prescribed for similar cases

## AminoPenicillin

Amoxicillin

DisperMox \$100

Moxatag \$110

Moxilin \$90

## Nitroimidazole Antimicrobial

PPI

Prostaglandin E1 Analog

Would like to adjust your plan?

OYes

O No

## Your New/Adjusted Plan:

Moxilin \$90 Biaxin XL-Pak \$35 Vandazole \$70 Protonix \$30 Arthrotec \$45

Would you like to proceed with the change of plan?

O Yes

O No

Figure A6. Sample Adoption Screen

<table><tr><td colspan="5">General Information</td></tr><tr><td>Patient Name</td><td>Date of Birth</td><td>Age</td><td>Sex</td><td>Primary Plan</td></tr><tr><td>James Smith</td><td>02/25/1972</td><td>42</td><td>Male</td><td>BCBS</td></tr><tr><td>Problem List</td><td colspan="2">Medication – Administration Mode Dose</td><td>Allergy List</td><td>Clinical Alerts</td></tr><tr><td rowspan="3">Duodena Ulcer</td><td colspan="2">Prescribed within Practice</td><td>- Latex Exam Gloves</td><td>New Endoscopic</td></tr><tr><td colspan="2">Ranitidine - 150mg/12h</td><td>- Sulfur (rash)</td><td>Exam Needed</td></tr><tr><td colspan="2">Maalox - 200 20mg/5mL</td><td></td><td></td></tr></table>

## Appendix B

## Experiment Cases

Case 1

<table><tr><td colspan="8">Vital Signs</td></tr><tr><td>Date</td><td>BP</td><td>HR</td><td>RR</td><td>T(F)</td><td>Wt</td><td>Ht</td><td>O2</td></tr><tr><td>12/20/2014</td><td>124/78</td><td>82</td><td>17</td><td>98.5</td><td>146lbs 3oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr><tr><td>04/07/2010</td><td>125/78</td><td>84</td><td>15</td><td>98.8</td><td>145lbs 6oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr></table>

<table><tr><td>Chief Complaint</td><td>Past Medical History</td><td>Family Medical History</td><td>Social History</td></tr><tr><td>Epigastric Pain</td><td rowspan="2">Duodenal ulcer for 10 years</td><td rowspan="2">Significant for Hypertension</td><td rowspan="2">Significant for Caffeine (Current); College graduate, 2 year; Divorced</td></tr><tr><td>Weight Loss</td></tr></table>

## History of Present Illness

James Smith is a 42 year old Caucasian male who presents today for recurrent epigastric pain treated in the last year with ranitidine. Patient experience loss of weight. He lost 5 pounds within th last month. Exacerbation of pain after meals. Patient has had endoscopic exam with biopsy that revealed the presence of 1 cm bulbar ulcer in the posterior part of the duodenum.

## SOAP Note

<table><tr><td></td><td>Height</td><td>Weight</td><td>BMI</td><td>Blood Pressure</td><td>Temp</td><td>Pulse</td><td>Resp Rate</td></tr><tr><td>VS</td><td>64.0 in</td><td>140.3 lb</td><td>34.7</td><td>130/78 mmHg</td><td>98.6 F</td><td>70 pbm</td><td>12 rpm</td></tr><tr><td>CC</td><td colspan="7">Epigastric Pain, weight loss</td></tr><tr><td>S</td><td colspan="7">Here for follow up of epigastric pain. Experiencing nausea. Taking rantidine and anti-acids.</td></tr><tr><td>O</td><td colspan="7">Genera; Normotensive. Chext: Lungs show no rales, no wheezes, no rhonchi. Heart: no murmurs. Abdomen: Soft, no tenderness, no masses, BS normal. Extremities: no deformities, no erythema. Neuro: Conscious, Monofilament Screen normal. Labs: All at target.</td></tr><tr><td>A</td><td colspan="7">Duodenel Ulcer</td></tr><tr><td>P</td><td colspan="7">TO BE DETERMINED</td></tr></table>

<table><tr><td>Drug Class</td><td>Active Ingredient(s)</td><td>Drug Name(s)</td></tr><tr><td>AminoPenicillin</td><td>Amoxicillin</td><td>Amoxicot, Apo-Amoxi, Amoxil. DisperMox. Moxatag, Moxilin, Trimox, Wymox</td></tr><tr><td>Macrolide</td><td>Clarithromycin</td><td>Biaxin, Biaxin XL, Biaxin XL-Pak</td></tr><tr><td>Nitroimidazol</td><td>Metronidazole</td><td>Flagyl, MetroCream, Metrogel, Noritate</td></tr><tr><td>Antimicrobial</td><td></td><td>Rosidan, Vandazole, Vitazol</td></tr><tr><td rowspan="3">PPI</td><td>Omeprazole</td><td>Prilosec, Omesec, Losec</td></tr><tr><td>Dexlansoprazole</td><td>Dexilant</td></tr><tr><td>Esomeprazole</td><td>Nexium</td></tr><tr><td>Prostaglandin E1</td><td>Lansoprazole</td><td>Prevacid</td></tr><tr><td rowspan="4">Analog</td><td>Omeprazole + Sodium Bicarbonate</td><td>Zegerid</td></tr><tr><td>Pantoprazole</td><td>Protonix</td></tr><tr><td>Rabeprazole</td><td>Aciphex, Kadipex</td></tr><tr><td>Misoprostol</td><td>Arthrotec, Cyprostol, Cytotec, Mibetec, Oxaprost</td></tr></table>

Case 2

<table><tr><td colspan="8">General Information</td></tr><tr><td>Patient Name</td><td colspan="2">Date of Birth</td><td>Age</td><td colspan="2">Sex</td><td colspan="2">Primary Plan</td></tr><tr><td>Shawn Jones</td><td>02/25/1960</td><td>55</td><td></td><td colspan="2">Male</td><td colspan="2">BCBS</td></tr><tr><td>Problem List</td><td colspan="3">Medication – Administration Mode Dose</td><td colspan="2">Allergy List</td><td colspan="2">Clinical Alerts</td></tr><tr><td>Diabetes</td><td colspan="3">Prescribed within Practice</td><td colspan="2">None</td><td colspan="2">Diabetics: Eye</td></tr><tr><td>Mellitus, Type II</td><td colspan="3">Metformin – 2 500 mg</td><td colspan="2"></td><td colspan="2">Exam Needed</td></tr><tr><td>Hypertension</td><td colspan="3">Captopril – 2 25 mg</td><td colspan="2"></td><td colspan="2">Diabetic: Foot Exam</td></tr><tr><td colspan="8">Vital Signs</td></tr><tr><td>Date</td><td>BP</td><td>HR</td><td>RR</td><td>T(F)</td><td>Wt</td><td>Ht</td><td>O2</td></tr><tr><td>06/20/2014</td><td>135/80</td><td>82</td><td>17</td><td>98.5</td><td>246lbs 3oz</td><td>5&#x27;8&quot;</td><td>99%</td></tr><tr><td>12/07/2013</td><td>130/79</td><td>85</td><td>15</td><td>98.8</td><td>240lbs 6oz</td><td>5&#x27;8&quot;</td><td></td></tr><tr><td colspan="8">Illness Details</td></tr><tr><td>Chief Complaint</td><td colspan="2">Past Medical History</td><td colspan="2">Family Medical History</td><td colspan="3">Social History</td></tr><tr><td>Diabetes follow-up</td><td colspan="2">Diabetes Type II Hypertension</td><td colspan="2">None</td><td colspan="3">Significant for Alcohol (Current); College graduate, 4 year; Married</td></tr></table>

## History of Present Illness

Shawn Jones is a 55 year old Caucasian male who comes in for a follow-up visit. In the previous encounter, patient’s dose of metformin was increased to 500mg, 3 times a day. Patient presented today with an A1C level of 9% and glucose test of 220. Patient not following recommended diet and physical activity.

## SOAP Note

O General: Normotensive, in no acute distress. Chest: Lungs show no rales, no wheezes, no ronchi. Heart: no murmurs, no rubs, no gallops. Abdomen: Soft, globular, no tenderness, no masses, BS normal. Extremities: No deformities, no edema, no erythema. Neuro: physiological, no peripheripathy. Monofilament Scrn normal. Labs: Glucos 220, A1C 9^.

A Hypertension, Diabetes I

P TO BE DETERMINED

<table><tr><td>Drug Class</td><td>Active Ingredient(s)</td><td>Drug Name(s)</td></tr><tr><td>Biguanides</td><td>Metformin</td><td>Fortamet, Glucophage, Glucophage XR, Glumetza, Riomet</td></tr><tr><td rowspan="3">Sulfonylureas</td><td>Glyburide</td><td>DiaBeta, Glycron, Glynase, Micronase</td></tr><tr><td>Glipizide</td><td>Glipizide XL, Glucotrol, Glucotrol XL</td></tr><tr><td>Glimepiride</td><td>Amayrl</td></tr><tr><td rowspan="3">Meglitinides</td><td>Mitiglinide</td><td>Glufast</td></tr><tr><td>Nateglinide</td><td>Starlix</td></tr><tr><td>Repaglinide</td><td>Prandin</td></tr><tr><td rowspan="3">Thiazolidinediones</td><td>Piglitazone</td><td>Actos</td></tr><tr><td>Rosiglitazone</td><td>Avandia</td></tr><tr><td>Troglitazone</td><td>Rezulin</td></tr><tr><td rowspan="3">DPP-4 inhibitors</td><td>Linagliptin</td><td>Tradjenta</td></tr><tr><td>Saxagliptin</td><td>Onglyxa</td></tr><tr><td>Sitagliptin</td><td>Januvia</td></tr><tr><td rowspan="4">GLP-1 receptor agonists</td><td>Albiglutide</td><td>Tanzeum</td></tr><tr><td>Exenatide</td><td>Byetta</td></tr><tr><td>Liraglutide</td><td>Victoza</td></tr><tr><td>Lixisenatide</td><td>Lyxumia</td></tr><tr><td rowspan="3">SGLT2 inhibitors</td><td>Canagliflozin</td><td>Invokana</td></tr><tr><td>Dapagliflozin</td><td>Farxiga</td></tr><tr><td>Ipragliflozin</td><td>Suglat</td></tr><tr><td rowspan="3">Alpha-Glucosidase Inhibitors</td><td>Acarbose</td><td>Precose</td></tr><tr><td>Miglitol</td><td>Glyset</td></tr><tr><td>Voglibose</td><td>Voglib</td></tr><tr><td rowspan="4">Bile Acid Sequestrants</td><td>Cholestyramine</td><td>Questran</td></tr><tr><td>Colesevelam</td><td>Welchol</td></tr><tr><td>Colestipol</td><td>Colestid</td></tr><tr><td></td><td>Colestipid</td></tr><tr><td rowspan="4">Combination Pills</td><td>Glipizide &amp; Metformin</td><td>Metaglip</td></tr><tr><td>Glyburide &amp; Metformin</td><td>Glucovance</td></tr><tr><td>Pioglitazone &amp; Glimepiri</td><td>Duetact</td></tr><tr><td>Pioglitazone &amp; Metformin</td><td>Actoplus Met</td></tr></table>

Repaglinide & Metformin

Saxagliptin & Metformin

Prandimet

Kombiglyze

Sitagliptin & Metformin

Insulin therapy

Janumet

Insulin Aspart

Insulin Detemir

Novolog

Levemir

Insulin Glargine

Lantus

Insulin Glulisine

Apidra

Insulin Isophane

Insulin Lispro

Humulin N, Novolin N

Humalog

## Case 3

<table><tr><td colspan="5">General Information</td></tr><tr><td>Patient Name</td><td>Date of Birth</td><td>Age</td><td>Sex</td><td>Primary Plan</td></tr><tr><td>Claudia Santiago</td><td>05/25/1995</td><td>19</td><td>Female</td><td>Aetna</td></tr><tr><td>Problem List</td><td colspan="2">Medication – Administration Mode Dose</td><td>Allergy List</td><td rowspan="2">Clinical Alerts</td></tr><tr><td>Asthma</td><td colspan="2">Prescribed within PracticeLoratidine – 1 10 mgFluticasone – 2 50 mcgPrescribed outside PracticeAlbuterol – As needed</td><td>AspirinNon-steroid anti-inflammatory drugs</td></tr></table>

<table><tr><td colspan="8">Vital Signs</td></tr><tr><td>Date</td><td>BP</td><td>HR</td><td>RR</td><td>T(F)</td><td>Wt</td><td>Ht</td><td>O2</td></tr><tr><td>11/04/2014</td><td>124/84</td><td>78</td><td>15</td><td>98.8</td><td>158lbs 3oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr><tr><td>07/07/2013</td><td>124/79</td><td>83</td><td>15</td><td>98.8</td><td>147lbs 7oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr></table>

<table><tr><td>Chief Complaint</td><td>Past Medical History</td><td>Family Medical History</td><td>Social History</td></tr><tr><td>- Dyspnea</td><td>Chronic sinusitis;</td><td>Non</td><td>Non-smoker; High-school graduate;</td></tr><tr><td>- Wheezing</td><td>Allergic Rhinitis;</td><td></td><td>Exercises regularly</td></tr><tr><td></td><td>Unusual Childhood disease</td><td></td><td></td></tr></table>

## History of Present Illness

19 year old female comes in for worsening of asthma symptoms. She refers to difficulty breathing with effort. Constant dry cough. The condition is worse at night. Wheezing.

## SOAP Note

<table><tr><td></td><td>Height</td><td>Weight</td><td>BMI</td><td>Blood Pressure</td><td>Temp</td><td>Pulse</td><td>Resp Rate</td></tr><tr><td>VS</td><td>66.0 in</td><td>150.0 lb</td><td>28.7</td><td>121/78 mmHg</td><td>98.6 F</td><td>80 pbm</td><td>28 4pm</td></tr><tr><td>CC</td><td colspan="7">Asthma</td></tr><tr><td>S</td><td colspan="7">Here for worsening of asthma symptoms. Shortness of breath. Wheezing. Taking medications without difficulty.</td></tr><tr><td>O</td><td colspan="7">General: Normotenstive, tachypneic. No fever. Chest: Lungs show wheezes, ronchi. Heart: no murmurs, no rubs, no gallops. Abdomen: Soft, no tenderness, no masses, BS normal. Extremities: no deformities, no edema, no erythema. Neuro: physiological, no peripheropathy. Monofilament Screen normal. Labs: all at target.</td></tr><tr><td>A</td><td colspan="7">Asthma</td></tr><tr><td>P</td><td colspan="7">TO BE DETERMINED</td></tr></table>

Alternatives

Drug Class

Adrenergic Bronchodialators

Active Ingredient(s)

Albutrol

Drug Name(s) AccuNeb, Airet, Proventil, Proventil HFA, Ventolin, Ventolin HFA, Volmax, Vospire ER

<table><tr><td rowspan="5"></td><td>Epinephrine</td><td>Adrenalin, Adrenalin Chloride, Asthmahaler, Auvi-Q, EpiPen, Primatene Mist, Twinject</td></tr><tr><td>Isoproterenol</td><td>Isuprel, Isuprel Mistometer, Medihaler-Iso</td></tr><tr><td>Levalbuterol</td><td>Xopenex, Xopenex Concentrate, Xopenex HFA</td></tr><tr><td>Metaproterenol</td><td>Alupent, Orciprenaline, Metaprel</td></tr><tr><td>Terbutaline</td><td>Brethine, Bricanyl, Brethine</td></tr><tr><td rowspan="3">Anticholinergics Bronchodilators</td><td>Aclidinium</td><td>Tudorza Pressair</td></tr><tr><td>Ipratropium</td><td>Atrovent, Atrovent HFA</td></tr><tr><td>Tiotropium</td><td>Spiriva, Spiriva Respimat</td></tr><tr><td rowspan="2">Methylxanthines</td><td>Dyphylline</td><td>Dilor, Dylix, Lufyllin</td></tr><tr><td>Theophylline</td><td>Theo-24, Theo-Dur, Uniphyl</td></tr><tr><td rowspan="3">Leukotriene Modifiers</td><td>Montelukast</td><td>Singulair</td></tr><tr><td>Zafirlukast</td><td>Accolate</td></tr><tr><td>Zileuton</td><td>Zyflo</td></tr><tr><td rowspan="5">Inhaled Corti Costeroids</td><td>Flunisolide</td><td>Aerospan</td></tr><tr><td>Beclomethasone</td><td>Qvar</td></tr><tr><td>Budesonide</td><td>Pulmicort</td></tr><tr><td>Mometasone</td><td>Asmanex</td></tr><tr><td>Fluticasone</td><td>Flovent</td></tr><tr><td rowspan="4">Bronchodilator Combinations</td><td>Albuterol/Ipratropoum</td><td>Combivent</td></tr><tr><td>Budesonide/Formoterol</td><td>Symbiacort</td></tr><tr><td>Fluticasone/Salmeterol</td><td>Advar Diskus, Advar HFA</td></tr><tr><td>Umeclidinium/Vilanterol</td><td>Anoro Ellipta</td></tr><tr><td rowspan="3">Oral Corti Corteroids</td><td>Dexamethasone</td><td>Baycadron</td></tr><tr><td>Hydrocortisone</td><td>Cortef</td></tr><tr><td>Prednisolone</td><td>Oraped</td></tr></table>

<table><tr><td colspan="5">General Information</td></tr><tr><td>Patient Name</td><td>Date of Birth</td><td>Age</td><td>Sex</td><td>Primary Plan</td></tr><tr><td>Jessica Korman</td><td>11/28/1949</td><td>65</td><td>Female</td><td>United Health</td></tr><tr><td>Problem List</td><td colspan="2">Medication – Administration Mode Dose</td><td>Allergy List</td><td>Clinical Alerts</td></tr><tr><td>Chronic Ischemic Heart Disease</td><td colspan="2">Prescribed within Practice Prescribed outside Practice Aspirin – 1 50 mg Nitroglycerin – 3 1 mg</td><td></td><td></td></tr></table>

## Case 4

<table><tr><td>Date</td><td>BP</td><td>HR</td><td>RR</td><td>T(F)</td><td>Wt</td><td>Ht</td><td>O2</td></tr><tr><td>04/20/2013</td><td>130/78</td><td>82</td><td>17</td><td>98.5</td><td>190lbs 3oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr><tr><td>07/07/2012</td><td>135/79</td><td>83</td><td>15</td><td>98.8</td><td>186lbs 7oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr></table>

<table><tr><td>Chief Complaint</td><td>Past Medical History</td><td>Family Medical History</td><td>Social History</td></tr><tr><td>- Nocturnal Cough</td><td>Chronic Ischemic</td><td rowspan="2">Mother died with stroke at the age of 60</td><td rowspan="2">College graduate, 4 year; Married</td></tr><tr><td>- Fatigue</td><td>Heart Disease</td></tr></table>

## History of Present Illness

65 year old African-American female, diagnosed with chronic ischemic heart disease in 2013, refers dyspnea during her ordinar activities and asthenia. Symptoms began 3 months ago, and worsened in the past 2 weeks.

## SOAP Note

<table><tr><td></td><td>Height</td><td>Weight</td><td>BMI</td><td>Blood Pressure</td><td>Temp</td><td>Pulse</td><td>Resp Rate</td></tr><tr><td>VS</td><td>64.0 in</td><td>202.0 lb</td><td>32.6</td><td>130/78 mmHg</td><td>98.6 F</td><td>70 pbm</td><td>12 rpm</td></tr><tr><td>CC</td><td colspan="7">Dyspnea, nocturnal cough, fatigue</td></tr><tr><td>S</td><td colspan="7">Here for worsening cardiac failure symptoms. Pt suffers from dyspnea, asthenia.</td></tr><tr><td>O</td><td colspan="7">General: Pt normotensive, tachypneic. Lung auscultation show respiratory rales, wheezes. Cardiac Auscultation: gallop, no murmurs. Abdomen: normal, no hepatomegaly. Lower Extremities: slight maleolar edema. Labs: all at target.</td></tr><tr><td>A</td><td colspan="7">Chronic Ischemic Heart Disease</td></tr><tr><td>P</td><td colspan="7">TO BE DETERMINED</td></tr></table>

## Alternatives

<table><tr><td>Drug Class</td><td>Active Ingredient(s)</td><td>Drug Name(s)</td></tr><tr><td rowspan="5">Calcium Channel Blocking Agents</td><td>Amlodipine</td><td>Norvasc</td></tr><tr><td>Diltiazem</td><td>Cardizem, Diltzac, Tiazac</td></tr><tr><td>Nicardipine</td><td>Cardene IV</td></tr><tr><td>Nifedipine</td><td>Adalat CC, Nifediac CC, Procardia</td></tr><tr><td>Verapmil</td><td>Calan, Isoptin, Verelan</td></tr><tr><td>Cardio-selective Beta Blockers</td><td>Betaxolol</td><td>Kerlone</td></tr></table>

<table><tr><td rowspan="2"></td><td>Metoprolol</td><td>Lopressor, Metoprolol Succinate ER, Toprol-XL</td></tr><tr><td>Nebivolol</td><td>Bystolic</td></tr><tr><td>Loop Diuretics</td><td>Gurosemide</td><td>Lasix, Diaqua-2, Lo-Aqua</td></tr><tr><td rowspan="4">Potassium-Sparing Diuretics</td><td>Amiloride</td><td>Midamor</td></tr><tr><td>Spironolactone</td><td>Aldactone</td></tr><tr><td>Triamterene</td><td>Dyrenium, Cardiac Glycoside</td></tr><tr><td>Digoxin</td><td>Cardoxin, Lanoxicaps, Lanoxin</td></tr><tr><td>Vasodilators</td><td>Nitroglycerin</td><td>Nitro-Bid, Nitrostat, Rectiv</td></tr><tr><td>Angiotensin Converting</td><td>Captopril</td><td>Capoten</td></tr><tr><td rowspan="2">Enzyme Inhibitors</td><td>Fosinopril</td><td>Monopril</td></tr><tr><td>Perindopril</td><td>Aceon, Enalapril</td></tr><tr><td rowspan="3">Peripheral Vasodilators</td><td>Cyclandelate</td><td>Cyclospasmol</td></tr><tr><td>Isoxuprine</td><td>Voxsuprine</td></tr><tr><td>Papaverine</td><td>Pavoco, Papacon, Pavagen</td></tr><tr><td rowspan="5">Angiotensin Receptor Blockers</td><td>Azilsartan Medoxomil</td><td>Edarbi</td></tr><tr><td>Eprosartan</td><td>Teveten</td></tr><tr><td>Losartan</td><td>Candesartan, Cozaar</td></tr><tr><td>Olmesartan</td><td>Benicar</td></tr><tr><td>Telmisartan</td><td>Micardis</td></tr><tr><td rowspan="7">Statins</td><td>Atorvostatin</td><td>Lipitor</td></tr><tr><td>Fluvastatin</td><td>Lescol</td></tr><tr><td>Lovastatin</td><td>Mevacor</td></tr><tr><td>Pitavastatin</td><td>Livalo</td></tr><tr><td>Pravastatin</td><td>Pravachol</td></tr><tr><td>Rosuvastatin Calcium</td><td>Crestor</td></tr><tr><td>Simvastatin</td><td>Zocor</td></tr><tr><td rowspan="2">Platelet Aggregation Inhibitors</td><td>Aspirin</td><td>Ecotrin, Fasprin, Miniprin</td></tr><tr><td>Clopidrogrel</td><td>Clavix, Clopirad, Plavix</td></tr></table>

Case 5

<table><tr><td colspan="5">General Information</td></tr><tr><td>Patient Name</td><td>Date of Birth</td><td>Age</td><td>Sex</td><td>Primary Plan</td></tr><tr><td>Natasha Wood</td><td>07/25/1991</td><td>23</td><td>Female</td><td>United Health</td></tr><tr><td>Problem List</td><td colspan="2">Medication – Administration Mode Dose</td><td>Allergy List</td><td>Clinical Alerts</td></tr><tr><td rowspan="5">Hyperthyroid</td><td colspan="2">Prescribed within Practice</td><td>Macrodantin - emesis</td><td>EKG</td></tr><tr><td colspan="2">Synthroid – 25 mcg daily</td><td>NSAIDS/ ASA – GI Bleed</td><td>Echocardiography</td></tr><tr><td colspan="2">Fioricet – 325 mg one tablet every 6 hours as needed for headache</td><td>Food allergies: oranges – hives,</td><td></td></tr><tr><td colspan="2">Prescribed outside Practice</td><td>Chocolate – anaphylasis</td><td></td></tr><tr><td colspan="2">Claritin – 10 mg daily as needed</td><td></td><td></td></tr><tr><td colspan="5">Health Status</td></tr><tr><td>Chief Complaint</td><td>Past Medical History</td><td colspan="2">Family Medical History</td><td>Social History</td></tr><tr><td>Fatigue</td><td>Hypothyroid x 2 yrs.</td><td colspan="2">Mother: HTN (alive)Father: Stroke at age of 40Maternal Grandmother: Ischemic heart disease (deceased)Maternal grandfather: HTN (deceased)Paternal grandmother: DM type II (deceased)Paternal grandfather: CAD, MI at age 52 (deceased)</td><td>Patient denies ever having used tobacco or alcohol. She lives alone and has never been married. She has no children.She drinks 3 cups of coffee every morning.</td></tr></table>

## History of Present Illness

Pt. presents to the office for a routine checkup. She denies feelings of chest pain or pressure. She denies any edema or numbness in her extremities. She states she has felt chronic fatigue over the past three months.

## SOAP Note

<table><tr><td></td><td>Height</td><td>Weight</td><td>BMI</td><td>Blood Pressure</td><td>Temp</td><td>Pulse</td><td>Resp Rate</td></tr><tr><td>VS</td><td>62.0 in</td><td>111.0 lbs</td><td>20.34</td><td>110/80 mmHg</td><td>98.5 F</td><td>70 pbm</td><td>18 rpm</td></tr><tr><td>CC</td><td colspan="7">Fatigue</td></tr><tr><td>S</td><td colspan="7">23 y.o. with familiar antecedents of familial hypercholesterolemia and stroke at early age (like 40 in father), presents in routine exam high levels of cholesterol and triglycerides.</td></tr></table>

General: African American female who appears her age, in no acute distress. Appears to have a flat affect. Skin: Light brown, warm and dry. No lesions, rashes or ulcers. Skin turgor good

Hair: texture is course, shoulder length black hair. Equal distribution with no areas of hair loss

Chest: Symmetric expansoins, no rales/ rhonchi/ wheezes noted. Respirations equal and clear throughout all lung fields

Heart: RRR, S1 and S2 audible, No gallops or rubs, PMI @ 5<sup>th</sup> ICS @ midclavicular line, no edema noted, peripheral pulses present

Abdomen: Soft, non-tender, non-distended. Liver and spleen non palpable.

Ears: TM pearly gray, bony landmarks visible, no bulging or drainage noted bilaterally .

Eyes: PERRLA, no erythema or visible discharge noted bilaterally

Nose: No erythema or edema noted. No nasal discharge. Septum intact.

Throat: No visible exudates, no petechiae. Mucus membranes moist and pink. Teeth intact

Neck: No lymphadenopathy noted. Thyroid non-palpable

Neuro: CN II – XII intact, sensory intact, strength equal bilaterally, no tremors or nystagmus noted.

Labs: TC – 310 TG – 200 HDL – 240 ALT/ AST – 130

A Hyperlipidemia

P TO BE DETERMINED

## Alternatives

<table><tr><td>Drug Class</td><td>Active Ingredient(s)</td><td>Drug Name(s)</td></tr><tr><td rowspan="7">Statins</td><td>Atorvastatin</td><td>Lipitor</td></tr><tr><td>Fluvastatin</td><td>Lescol</td></tr><tr><td>Lovastatin</td><td>Mevacor</td></tr><tr><td>Pitavastatin</td><td>Livalo</td></tr><tr><td>Pravastatin</td><td>Pravachol</td></tr><tr><td>Rosuvastatin Calcium</td><td>Crestor</td></tr><tr><td>Simvastatin</td><td>Zocor</td></tr><tr><td rowspan="6">Combination Statins</td><td>Atorvastatin with Amlodipine</td><td>Caduet</td></tr><tr><td>Lovastatin with Niacin</td><td>Advicor</td></tr><tr><td>Simvastatin with Ezetimibe</td><td>Vytorin, Bile Acide-Binding Resins</td></tr><tr><td>Cholestyramine</td><td>Prevalite</td></tr><tr><td>Colesevelam Hcl</td><td>WIChol</td></tr><tr><td>Colstipol</td><td>Colstid</td></tr><tr><td rowspan="3">Fibrats</td><td>Clofibrat</td><td>Abitrat</td></tr><tr><td>Fenobirate</td><td>Antara, Tricor, Triglide</td></tr><tr><td>Gemfibrozil</td><td>Lopid</td></tr><tr><td>Nicotinic Acid</td><td>Niacin</td><td>Niacor, Niaspan, Slo-Niacin</td></tr></table>

Case 6

<table><tr><td colspan="8">General Information</td></tr><tr><td>Patient Name</td><td colspan="2">Date of Birth</td><td colspan="2">Age</td><td>Sex</td><td colspan="2">Primary Plan</td></tr><tr><td>Aliya White</td><td>9/25/1967</td><td>47</td><td></td><td></td><td>Female</td><td colspan="2">Unitd Halth</td></tr><tr><td>Problem List</td><td colspan="4">Medication – Administration Mode Dose</td><td>Allergy List</td><td colspan="2">Clinical Alerts</td></tr><tr><td rowspan="3">Hypertension</td><td colspan="4">Prescribed within Practice</td><td></td><td></td><td></td></tr><tr><td colspan="4">Motrin PRN headaches – 600 mg 3-4x weekly</td><td></td><td></td><td></td></tr><tr><td colspan="4">Exforge – 10/320 mg tablet once daily</td><td></td><td></td><td></td></tr><tr><td colspan="8">Vital Signs</td></tr><tr><td>Date</td><td>BP</td><td>HR</td><td>RR</td><td>T(F)</td><td>Wt</td><td>Ht</td><td>O2</td></tr><tr><td>02/05/2015</td><td>185/104</td><td>69</td><td>18</td><td>98.5</td><td>170lbs 3oz</td><td>5&#x27;6&quot;</td><td>99%</td></tr><tr><td colspan="8">Health Status</td></tr><tr><td>Chief Complaint</td><td colspan="2">Past Medical History</td><td colspan="2">Family Medical History</td><td colspan="3">Social History</td></tr><tr><td>– Follow-up of physical exam – HTN– Headaches</td><td colspan="2">Hypertension x 20 yrs.</td><td colspan="2">Father had HTN, is on dialysis for renal failure.Mother has DM Type II.</td><td colspan="3">Accountant, works 50-60 hrs/week,lives alone, poor diet: lots of fast food. Caffeine 2-3 /day, occasional EtOH, smokes 2 pack/day (27 pack-year hx). Would like to exercise more, but is often too tired.</td></tr></table>

## History of Present Illness

47 y.o. A.A. F presents to clinic for f/u of physical exam findings. Found to be hypertensive during physical exam 1 week ago. PCP ordered blood work

## SOAP Note

<table><tr><td></td><td>Height</td><td>Weight</td><td>BMI</td><td>Blood Pressure</td><td>Temp</td><td>Pulse</td><td>Resp Rate</td></tr><tr><td>VS</td><td>65.- in</td><td>168.0 lb</td><td>28.0</td><td>180/104 mmHg</td><td>98.6 F</td><td>62 pbm</td><td>12 4pm</td></tr><tr><td>CC</td><td colspan="7">F/u of physical exam</td></tr><tr><td>S</td><td colspan="7">47 y.o. A.A. F presents to clinic for f/u of physical exam findings. Found to be hypertensive during physical exam 1 week ago. PCP ordered blood work.</td></tr><tr><td>O</td><td colspan="7">BUN 35, SC4 1.8, 25-hr urine: &gt;2 g/day proteinuria, glucose: 99mg/dL. Lipid panel: TC: 240mg/dL, TG: 1 70 mg/dL, HDL: 34mg/dL LDL: 144 mg/dL</td></tr><tr><td>A</td><td colspan="7">- Pt has uncontrolled HTN- Smoking, caffeine, stress and poor diet exercise BP and risk of CV disease. Lifestyle modifications and smoking cessation will help to reduce BP.</td></tr><tr><td>P</td><td colspan="7">TO BE DETERMINED</td></tr></table>

<table><tr><td>Drug Class</td><td>Active Ingredient(s)</td><td>Drug Name(s)</td></tr><tr><td rowspan="5">Calcium Channel Blocking Agents</td><td>Amlodipine</td><td>Norvasc</td></tr><tr><td>Diltiazem</td><td>Cardizem, Diltzac, Tiazac</td></tr><tr><td>Nicardipine</td><td>Cardene IV</td></tr><tr><td>Nifedipine</td><td>Adalat CC, Nifediac CC, Procardia</td></tr><tr><td>Verapamil</td><td>Calan, Isoptin, Verelan</td></tr><tr><td rowspan="2">Cardiac Glycoside</td><td>Digoxin</td><td>Cardoxin, Lanoxicaps, Lanoxin, Vasodilators</td></tr><tr><td>Nitroglycerin</td><td>Nitro-Bid, Nitrostat, Rectiv</td></tr><tr><td rowspan="3">Angiotensin Converting Enzyme Inhibitors</td><td>Captopril</td><td>Captonen</td></tr><tr><td>Fosinopril</td><td>Monopril</td></tr><tr><td>Perindopril</td><td>Aceon, Enalapril</td></tr><tr><td rowspan="3">Peripheral Vasodilators</td><td>Cyclandelate</td><td>Cyclospasmol</td></tr><tr><td>Isoxsuprine</td><td>Voxsuprine</td></tr><tr><td>Papaverine</td><td>Pavacp. {a[acpm. {avagem}}</td></tr><tr><td rowspan="5">Angiotensin Receptor Blockers</td><td>Azilsartan Medoxomil</td><td>Edarbi</td></tr><tr><td>Eprosartan</td><td>Teveten</td></tr><tr><td>Losartan</td><td>Candesartan, Cozaar</td></tr><tr><td>Olmesartan</td><td>Benicar</td></tr><tr><td>Telmisartan</td><td>Micardis</td></tr><tr><td rowspan="7">Statins</td><td>Atorvastatin</td><td>Lipitor</td></tr><tr><td>Fluvastatin</td><td>Lescol</td></tr><tr><td>Lovastatin</td><td>Mevacor</td></tr><tr><td>Pitavastatin</td><td>Livalo</td></tr><tr><td>Pravastatin</td><td>Pravachol</td></tr><tr><td>Rouvastatin Calcium</td><td>Crestor</td></tr><tr><td>Simvastatin</td><td>Zocor</td></tr><tr><td rowspan="2">Platelet Aggregation Inhibitors</td><td>Aspirin</td><td>Ecotrin, Fasprin, Miniprin</td></tr><tr><td>Clopidogrel</td><td>Clafix, Clopirad, Plavix</td></tr></table>

## Appendix C

## Interview Questionnaire

## Demographic Questions:

1. What is your specialty?

2. Do you have your own practice or work for someone else’s practice?

3. How many years of experience do you have as a medical doctor?

4. Do you have access to a system which provides intelligent recommendations (meaning alternative treatment plans that are of similar or higher efficacy) at the time of prescription?

5. If so, do you find it useful? Why or why not?

## Cost Questions:

6. Does cost of treatment vary for the same medical diagnosis? If so, can you provide an example?

7. If so, do you think the variance [in cost] is an issue in healthcare? Why or why not?

8. Do you have access to accurate cost information of treatment alternatives at the time of prescription?

9. If yes, do you find it useful? Why or why not?

10. In your opinion, do medical providers in general today take into consideration the cost of a treatment in addition to efficacy when prescribing treatments to patients? Does this vary if we are talking about procedures versus drugs/pills?

11. When considering costs of treatment options, which cost will drive your decision (cost to patient or the insurance provider)?

12. Do you think some medical practitioners, consider more expensive treatment options as being more effective or put in another way

cheaper options as less effective? If so, do those represent the majority or minority of medical practitioners?

13. After the recent healthcare reforms, do you feel more accountable for excessive healthcare costs?

## Time Pressure Questions:

14. In general, what is your typical schedule like? How much control do you have over your time?

15. Do you experience time pressure during your work day? If so, how often and what are usually the reasons for the time pressure?

16. When you are under high time pressure, does it change the manner in which you interact with the EMR?

## System Use Questions:

17. If you had access to a system which provides intelligent recommendations (meaning alternative treatment plans that are of similar or higher efficacy) with accurate cost information at the time of prescription, would you use it?

18. Would you change the way you use it under high time pressure?

19. Would you change the way you use it when treating high risk patients?

## Appendix D

## Interview Results

<table><tr><td colspan="4">Table D1. Summary of Cost Information Relevance Factors</td></tr><tr><td>Main Concept</td><td>Extracted Factor</td><td>Type, Consensus</td><td>Sample Quote</td></tr><tr><td rowspan="3">Medication cost consideration</td><td>Patient compliance</td><td>E, S</td><td>“Absolutely, as a provider, my responsibility to you as a patient is not only to write a prescription. It&#x27;s also important for us to give the best medication that the patients can afford.”“Clearly cost to the patient because that is directly correlated with the compliance.”</td></tr><tr><td>Perceived cost-efficacy correlation</td><td>E, S</td><td>“In this day and age of evidence-based medicine. I think every-one looks at the evidence with the exclusion of the cost. If it&#x27;s been proven that a treatment works and the research backs that up then, that&#x27;s what most providers base their treatment decisions on.”</td></tr><tr><td>Patient risk</td><td>L, S</td><td>“Cost has always been an issue. It&#x27;s something in the back of your mind but when I am dealing with, in my specific situation, someone&#x27;s heart condition, my opinion is somewhat skewed. Cost is probably the last thing that I think about when I care for the patient.”</td></tr><tr><td rowspan="4">Cost information access</td><td>Cost transparency initiatives</td><td>E, M</td><td>“I would say more so than in the past there has been even a lot of effort as of late to help providers understand the cost of the medication that they are prescribing.”</td></tr><tr><td>Incomplete information</td><td>L, M</td><td>“The only information I have access to, is whether the prescription I prescribe is first tier, second tier, or third tier. I would not know exactly how much that would cost. All I know that the first-tier drug would be cheaper than the second tier or third tier.”</td></tr><tr><td>Non-automated information access</td><td>L, M</td><td>“It&#x27;s not something that&#x27;s automatic. We have access to databases of information on a particular condition that will state that accepted treatments ‘x’ are for a condition ‘abc.’ It&#x27;s something you have to go and look up and essentially ask the right question. It&#x27;s only going to go based on the question you ask.”</td></tr><tr><td>Cost variance</td><td>L, S</td><td>“I would not know the exact cost of that drug would be for a month&#x27;s supply because that differs from one insurance to another. Sometimes the patients don&#x27;t even know themselves.”“they are not aware of the actual pricing because of the variety of insurance copayments and limitations.”</td></tr></table>

S: strong support (>7 respondents); M: medium support (5 to 7 respondents); L: low support (1 to 4 respondents); L: limiting factor; E: enabling factor

<table><tr><td colspan="4">Table D2. Summary of Time Pressure Relevance Factors</td></tr><tr><td>Main Concept</td><td>Extracted Factor</td><td>Type, Consensus</td><td>Sample Quote</td></tr><tr><td>Time pressure relevance</td><td>Number of patients per day</td><td>E, S</td><td>“I don’t have so much control over my time. In the sense that when I’m in the office, we see whoever wants to be seen. In that way, I have a pretty tight day schedule in the office.”</td></tr><tr><td rowspan="3">Intended cost-sensitive system use under high time pressure</td><td>Efficacy and safety equivalence</td><td>E, M</td><td>“Yes if it is the same efficacy and that’s cheaper I’m fine with that. Not just efficacy we are talking about safety we are talking about probability. So when we are talking about giving a patient a medication it’s not just how its effective it’s going to be, it’s also how safe it is and how vulnerable the patient is going to be. So if those criteria are met of course.”</td></tr><tr><td>Recommendation reliability</td><td>L, M</td><td>“If the system is perfect and recommendations are evidence-based, I would use it.”</td></tr><tr><td>Time sensitivity</td><td>L, M</td><td>“I mean if it is very time consuming, then obviously people are not going to be keen on using it, but if it is easy to use and user friendly and doesn’t take a lot of time then I am sure that we could use it.”</td></tr></table>

S: strong support (>7 respondents); M: medium support (5 to 7 respondents); L: low support (1 to 4 respondents); L: limiting factor; E: enabling factor

## Appendix E

## Experiment Cases Comparisons

## MD Report 1

## Comparison Across Patient Cases

Cases’ degree of severity: All patients are clinically more or less stable. Patients in these cases don’t have apparent complications. They just present with uncontrolled symptoms within their diagnosis. Given their age, family history, clinical alerts, vital signs and physical exam, none of them require urgent care.

Familiarity with clinical case and adequate treatment across designation and specialty: All of the cases presented are considered potentia patients for any health care provider, as their diagnoses only require basic medical knowledge. They can be managed by providers of any designation and specialty

Familiarity with treatment options: Treatment options were listed by their class and subclass names. These drug classes and subclasses are taught in core pharmacology courses as part of any medical curriculum.

## Comparisons Within Each Patient Case

Comparative efficacy: The alternatives presented belonged to the same drug subclass. They all have the same indication and are therefore prescribed for the same purpose. Thus, they all have the same efficacy towards the concerning symptoms. The main potential difference between drugs of the same class would be the dosage and administration modes

## Side effects and adverse events:

• Drugs with the same active molecule have the exact side effects and adverse events.

Drugs within the same subclass and different active molecule have similar side effects. For example, side effects of two PPI drugs: Losec and Protonix both have side effects within the GI tract.

In addition, the medical protocols only include the subclasses’ names and active ingredients. Doctors have the freedom to choose the drug they feel most comfortable prescribing.

## MD Report 2

## Comparison Across Patient Cases

Cases’ degree of severity: All of these cases pertain to chronic diseases where the patients are in stable condition. The treatment plan is to therefore follow up on prior consultations and change the prescribed drugs as necessary.

The patients are considered stable based on the chief complaint, history of present illness, and current medication list.

Familiarity with clinical case across specialty: All the cases described in the experiment are addressed during the first years of residency (internal medicine). Therefore, medical providers of all specialties have the necessary knowledge to understand and treat these cases.

Familiarity with treatment options across specialty: All medical providers should be familiar with the treatment options presented. Doctors might not know specific drug names especially new drugs. However, they should all able to recognize the drug class names.

## Comparisons Within Each Patient Case

## Comparative Drug Efficacy

Drugs with the same active ingredients have the same efficacy. Different drugs within the same class have the same mechanism of action. We select one drug over the other based on the intake frequency.

Drug Side effects and adverse events: Drugs with the same active ingredients usually have the same side effects and adverse events. Drugs within the same subclass share certain side effects in common but could also have some different side effects.
