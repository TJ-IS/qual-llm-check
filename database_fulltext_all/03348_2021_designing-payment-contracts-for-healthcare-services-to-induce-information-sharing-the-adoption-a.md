---
otero_id: 3348
otero_key: "G23RDAG8"
title: "Designing Payment Contracts for Healthcare Services to Induce Information Sharing: The Adoption and the Value of Health Information Exchanges (HIEs)"
authors: "Mehmet U. S. Ayvaci; Huseyin Cavusoglu; Yeongin Kim; Srinivasan Raghunathan"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/14809"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DESIGNING PAYMENT CONTRACTS FOR HEALTHCARE SERVICES TO INDUCE INFORMATION SHARING: THE ADOPTION AND THE VALUE OF HEALTH INFORMATION EXCHANGES (HIES)<sup>1</sup>

Mehmet U. S. Ayvaci and Huseyin Cavusoglu Naveen Jindal School of Management, The University of Texas at Dallas, Richardson, TX, U.S.A. {mehmet.ayvaci@utdallas.edu} {huseyin@utdallas.edu}

Yeongin Kim School of Business, Virginia Commonwealth University Richmond, VA, U.S.A. {ykim3@vcu.edu}

Srinivasan Raghunathan Naveen Jindal School of Management, The University of Texas at Dallas, Richardson, TX, U.S.A. {sraghu@utdallas.edu}

Recent initiatives to improve healthcare quality and reduce costs have centered around payment mechanisms and IT-enabled health information exchanges (HIEs). Such initiatives profoundly influence both providers’ choices in terms of healthcare effort levels and HIE adoption and patients’ choice of providers. Using a gametheoretical model of a healthcare setup, we examine the role of payment models in aligning providers’ and patients’ incentives for realizing socially optimal (i.e., first-best) choices. We show that the traditional fee-forservice (FFS) payment model does not necessarily induce the first-best solution. The pay-for-performance (P4P) model may induce the first-best solution under some conditions if provider switching by patients during a health episode is socially suboptimal, making provider coordination less of an issue. We identify an episode-based payment (EBP) model that can always induce the first-best solution. The proposed EBP model reduces to the P4P model if the P4P model induces the first-best solution. In other cases, the first-best inducing EBP model is multilateral in the sense that the payment to a provider depends not only on the provider’s own efforts and outcomes but also on those of other providers. Furthermore, the payment in this EBP model is sequence dependent in the sense that payment to a provider is contingent upon whether the patient visits a given provider first or second. We show that the proposed EBP model achieves the lowest healthcare cost, not necessarily at the expense of care quality or provider payment, relative to FFS and P4P. Although our proposed contract is complex, it sets an optimality baseline when evaluating simpler contracts and also characterizes aspects of payment that need to be captured for socially desirable actions. We further show that the value of HIEs depends critically on the payment model as well as on the social desirability of patient switching. Under all three payment models, the HIE value is higher when switching by at least some patients is desirable than when switching by any patient is undesirable. Moreover, the HIE value is highest under the FFS model and lowest under the P4P model. Hence, assessing the value of HIEs in isolation from the underlying payment mechanism and patientswitching behavior may result in under- or overestimation of the HIE value. Therefore, as payment models evolve over time, there is a real need to reevaluate the HIE value and the government subsidies that induce providers to adopt HIEs.

Keywords: Health-information exchange, incentive alignment, payment models, health IT

As we shift from paying for volume (fee-for-service) to paying for value (some kind of performance-based payment), providers will have a stronger incentive to produce high-quality efficiently and this requires coordination, elimination of duplication, and outcome tracking among other things. This, in turn, is facilitated by health information exchange.

– Richard G. Frank, Keynote Speech at the 7th Annual Workshop on Health IT and Economics, Washington D.C., October 2016).

## Introduction

The American healthcare system has long been characterized as highly inefficient even though it is capable of providing superior care (Garber and Skinner 2008). In a global study of healthcare-spending efficiency across developed nations, the U.S. ranked near the bottom (Shah 2015). Although many reasons for this have been cited, such as the emphasis on sick care rather than health care, inefficiency in delivery is largely attributed to misaligned economic incentives and the lack of care coordination among providers (Barr 2016). Recognizing these drivers of inefficiency, the U.S. Department of Health and Human Services (HHS) recently set forth the goal of achieving increased coordination, harnessing the power of information, and providing highervalue care (Burwell 2015). In particular, the HHS identified (1) setting the right incentives for providers through new payment models and (2) aligning IT practices—namely, coordinating care through IT-enabled health-information exchanges (HIEs)—as keys to success in realizing these goals. The role of payment models in influencing the provision of care and the role of HIEs in achieving better care coordination are apparent and have been well recognized (Furukawa et al. 2013). However, payment models and HIEs have subtle interactions in incentivizing providers and patients to choose socially desirable actions, and these interactions have not been clearly articulated in the academic literature or in the discussion of the recent initiatives by the HHS.

While payment models and HIEs are seemingly independent, each seeking to accomplish a different objective, they affect one another in a crucial way. The payment model directly affects the intensity and the type of services (or effort) exerted by providers (Ellis and McGuire 1996). Similar to other contracting contexts, two types of effort exist in healthcare services: observable and unobservable. Observable effort is related to services that can be well documented and reported, such as tests, procedures, and physician notes. The unobservable part of the effort is those services that are difficult to document and report, such as diligence in interpreting test results and the detailed communication between the physician and patient. The health economics literature treats observable effort as contractible physician actions and unobservable effort as noncontractible physician actions (McGuire 2000). While payment to a provider can be contingent on the level of observable (and thus verifiable) effort, it cannot be contingent on the level of unobservable (and unverifiable) effort. Consequently, payment models are likely to influence the type and amount of effort exerted by providers. Furthermore, observable effort is the type of effort that can be shared with other providers. In fact, the analysis of HIE access logs suggests that physicians most frequently access laboratory and radiology reports—observable actions taken by other providers (Campion et al. 2013). Hence, there is a clear connection between what is “observable” and what is “sharable.” Furthermore, it is known that providers participating in an HIE are able to use information available from other providers as part of electronic health records (EHR), such as the diagnostic test results, to provide care (Bailey et al. 2013). Given the natural link between observable effort and sharing it through HIEs, and the connection between payment model and the type and level of provider effort, the value and adoption of HIEs depends critically on the payment model in place.

An important consequence of HIE adoption is that it can alter “competition” among providers. For instance, providers adopting HIEs have access to the history of observable efforts undertaken by other providers on behalf of their patients, whereas providers not adopting HIEs only have access to the history of their own efforts. Consequently, patients are likely less deterred from switching providers during a health episode when providers adopt HIEs versus when they do not. In other words, HIEs can intensify provider competition for patients, while simultaneously enabling cooperation among providers through sharing observable efforts regarding patients (Adjerid et al. 2018; Grossman et al. 2006).

Because of the intricate interactions among payment model, provider efforts, the HIE, and patient behavior, it is unclear whether prevailing and newer payment models encourage care providers and patients to choose actions that lead to the most desirable social outcomes (O’Malley 2011). In a recent keynote speech at the 2016 Workshop on Health IT and Economics, Richard G. Frank—a renowned health economist and former assistant secretary for planning and evaluation at the HHS—confirmed this observation and argued that the current shift toward outcome-based payment models would not necessarily lead to successful HIE adoption if proper quality measures related to payment arrangements are not selected. In particular, one criticism of new payment models is the use of unilateral quality measures that do not adequately capture the value of information exchange between providers. The lack of interdependency between payments and incentives for HIE adoption will inevitably diminish the effectiveness of coordination efforts (Frank 2016). Consistent with this argument, in this paper, we aim to develop a coherent understanding of the interrelationships among new/existing payment models, providers’ incentives to work with, coordinate through, or invest in HIEs, patients’ choice of providers, and the value of HIEs. Specifically, we seek to answer the question of how payment structures should be designed to maximize the social welfare that accounts for all the interrelationships among these stakeholders.

## Health Information Exchanges

In an attempt to improve the quality of care and reduce costs, the Centers for Medicare and Medicaid Services introduced the Meaningful Use incentive program (Blumenthal and Tavenner 2010). This program provides nearly \$27 billion over the course of ten years in incentive payments to hospitals and physicians for adopting EHRs. An important criterion for receiving incentive payments is the ability to demonstrate the capability to share information among disparate providers. Such capability is effectively enabled through HIE platforms that electronically move clinical data among participating healthcare providers. Shared information may include lab results, radiology reports, discharge summaries, vital health information, etc. (Furukawa et al. 2013).

Although HIEs promise substantial value in improving quality of care and generating significant cost savings through efficiency gains (Hillestad et al. 2005), recent studies suggest that the exchange of information outside the boundaries of healthcare organizations is limited (ONC 2014). In particular, it has been shown that the prevalent payment structure in the U.S. could present a substantial barrier to widespread health information sharing (Furukawa et al. 2013). The lack of exchange of electronic health information is a concerning issue not only for policy makers but also for industry leaders and consumer advocates (Shapiro et al. 2016). Furthermore, the alternative payment models introduced as part of recent legislative efforts assume widespread exchange of health information among providers (Bitton et al. 2012). However, it is unclear how much value is offered by HIEs and whether providers would adopt HIEs under various payment models.

## Payment Models

Despite several proposals and pilots for alternative payment models, fee-for-service (FFS) is currently the dominant payment model for compensating providers for the services they render to patients. Electronically capturing healthcare data through EHR is attractive in an FFS environment because it facilitates compliance and revenue generation through better coding of provider services. However, there is widespread consensus that the FFS model promotes volume and intensity rather than value (Rosenthal 2008). Ever-increasing healthcare costs and unsatisfactory quality have prompted the introduction of the pay-for-performance (P4P) model over the last decade.

The P4P model aims to realign incentives to reduce costs, improve the quality of care, and mitigate the moral-hazard problem associated with the FFS model (Ellis and McGuire 1996). Although the specifics may vary across different implementations of the P4P model, these payment schemas generally reimburse providers based on outcome measures such as quality, efficiency, and patient satisfaction, thereby focusing on value over volume (Rosenthal and Dudley 2007). Recognizing the need for outcome-based payments to improve the quality of care, the value-based payment (VBP) modifier was created for providers participating in Medicare (Jha 2013). The VBP modifier adjusts a provider’s compensation upward or downward based on the provider’s performance relative to that of peers. It is expected that the corresponding gain or loss caused by the adjustment will realign providers’ incentives with the payer’s goals. The evidence on whether the P4P model achieves the intended objective is mixed (Goitein 2014).

The mixed evidence on the success of the P4P model and the continuing interest in “value” have paved the way for broader payment reforms (Rosenthal 2008) and led the HHS to consider bundling payments on the basis of a clinically defined episode of care, namely episode-based payments (EBP) (Burwell 2015) rather than payments based on individual services rendered by providers. Under EBP, the payer reimburses independent providers participating in the healthcare episode based on the outcome of treatment efforts related to that episode. For example, consider a patient who undergoes a bypass surgery at a hospital and later gets readmitted to the same or another hospital (readmission is an indicator of lowquality care). The payer then makes payments to hospitals participating in the episode using a predetermined rate, which is a function of (1) the typical cost of a bypass surgery, and (2) the extent to which the hospital in the initial admission is accountable for the readmission (e.g., see de Brantes et al. 2009 for an example of the distribution of EBP payments in such a scenario). However, it is unclear whether EBP or P4P models are active in HIEs, prompting policy makers to call for an investigation of payment models (Frank 2016).

## Model Setup and Summary of Main Findings

We examine the role of payment models in providers’ choice of effort levels and HIE adoption decisions and patients’ choice of providers in the context of a stylized health care setting with two providers. The providers exert observable (and hence sharable) effort as well as unobservable (and hence unsharable) effort in treating a patient. The patient needing care during a healthcare episode first visits the preferred provider. If the patient is not cured by the preferred provider in the first visit, the patient may return to the same provider or switch to the other provider for the second visit. The new provider has access to the sharable or observable services provided by the first provider if and only if both providers participate in the HIE. There are costs incurred by providers when they adopt an HIE, and, irrespective of HIE adoption, providers have access to their own first-visit services if the patient returns to them for a second visit. If the patient is not cured at the end of the episode, the patient incurs a disutility, which varies across patients and depends on whether the patient visited a single provider or both providers during the episode.

Our key findings and their main implications are as follows. First, from the social welfare perspective, a desirable HIE adoption status and patient switching behavior are interdependent. HIE adoption is socially desirable only when the cost of adopting the HIE does not exceed a threshold, which depends on whether or not provider switching by patients is desirable. Analogously, switching is desirable only when the benefit from switching exceeds a threshold, which depends on whether or not the HIE is desirable. Consequently, when the patients’ benefit from switching is high (low), the socially desirable patient behavior is switching (not switching), regardless of whether the HIE adoption is socially desirable. However, when the benefit of switching is only moderate, the socially desirable scenario is the one in which patients switch providers when HIE adoption is socially desirable and return to their preferred providers when HIE adoption is not socially desirable. Therefore, any potential value of an HIE arises solely from its impact on providers when the patients’ benefit of switching is either high or low. When the benefit is moderate, the value of the HIE arises from its impacts on providers as well as patients.

Second, regardless of patient switching behavior, FFS neither induces HIE adoption nor does it lead to socially optimal provider efforts. Moreover, it may not induce the desirable patient switching behavior. On the other hand, the P4P model can induce the first-best solution under some conditions when switching is not socially desirable. However, when switching is desirable, the P4P model may fail to induce (1) HIE adoption when it is socially desirable, (2) the socially desirable patient switching behavior, and (3) socially optimal effort levels. The P4P model achieves a higher quality of care and a higher overall social welfare compared to the FFS model, supporting the view that it is an improvement over FFS. However, there exists an EBP model that always induces socially optimal HIE adoption, patient switching behavior, and provider efforts, implying that the EBP model is superior to both FFS and P4P models from the social welfare maximization perspective.

Third, the social welfare-maximizing EBP model has three distinct characteristics when patient switching is desirable: first, it is multilateral in the sense that the payment to a provider depends not only on the provider’s own efforts and outcome but also those of the other provider. Second, the payment in the EBP model is sequence dependent in the sense that payment to a provider is contingent upon whether the patient visits the provider first or second. Finally, adjusting payments for both good and bad outcomes is an essential feature of the proposed EBP model when switching by at least some patients is socially desirable. These characteristics are individually reflected in different payment models that are being evaluated as part of ongoing healthcare payment reforms. Although our proposed contract is complex (in comparison to existing payment models), it sets an optimality baseline when evaluating simpler contracts and also characterizes aspects of payment that need to be captured for socially desirable actions.

Fourth, the social welfare-maximizing EBP model delivers not only the lowest health care costs but also the highest quality of care in most cases. Furthermore, the EBP model does not necessarily minimize the earnings of providers. This finding suggests that the switch to the first-best inducing EBP model from the prevailing FFS model may not reduce the payment to providers but the extra payment, if any, will likely be accompanied by quality improvements. The P4P model indeed delivers a higher quality of care while simultaneously reducing healthcare costs compared to the FFS model, but the P4P model does not necessarily reduce the payment to providers compared to the FFS model. The FFS model results in the highest healthcare costs and the lowest quality of care among the three payment models, supporting the claim that the FFS is an inefficient mechanism with poor quality outcomes. At the same time, the FFS model results in the lowest payment to providers among the three models, suggesting that the providers’ fear of reduced compensation under newer payment models (e.g., see Goitein 2014) may be unwarranted.

Finally, we show that the value of HIEs—defined as the social payoff under an HIE minus the social payoff under no HIE—depends critically on the payment model used by the payer as well as the patient switching behavior induced by it. The value of HIEs is higher when patients switch than when they do not, regardless of the payment model. Moreover, the value of HIEs is highest under the FFS model and lowest under the P4P model, while its value under the EBP model is lower than the value under the FFS model and higher than or equal to the value under the P4P model. Hence, assessing the value of an HIE independent of the underlying payment mechanism and patient switching behaviors results in over- or underestimating the true benefit of the adoption. This finding also suggests that even when an HIE does not offer a positive payoff under the centralized setup (i.e., from a social planner’s perspective), the HIE may be beneficial under the FFS model, and that even when an HIE offers a positive payoff under the centralized setup, the HIE may not be beneficial under the P4P model. Therefore, as new payment models evolve, the value of HIEs and government intervention policies like subsidies that promote HIE adoption must be carefully reevaluated, taking into account the factors that influence patients’ as well as providers’ choices.

## Literature Review

Our study relates broadly to the literature on the value of IT and, specifically, to the adoption and value of health IT. The question of the value of IT, and therefore the firms incentive to invest in IT, has been extensively studied in the IS literature (Melville et al. 2004). The main focus of this stream of work is to understand whether IT adoption improves a firm’s performance or competitive position (Bharadwaj 2000). Researchers have examined various forms of IT adoption decisions, including electronic data interchange (Premkumar et al. 1997), customer relationship management (Zablah et al. 2012), e-business (Zhu et al. 2003), and information security technology (Cavusoglu et al. 2009; Cavusoglu et al. 2005). While some empirical studies indicate that firms are more likely to invest in IT to improve their strategic position (Iacovou et al. 1995), others suggest that firms are less inclined to invest in IT because the value of IT can be competed away and, ultimately, customers and partners appropriate the returns from these investments in the form of higher quality or lower prices (Brynjolfsson and Hitt 1996). In terms of the impact on firm profits, the evidence is also mixed, ranging from none or negative (Hitt and Brynjolfsson 1996) to positive (Mithas et al. 2012). Our study contributes to the ongoing discussion about the value of IT-based technology adoptions. However, unlike prior studies—where the level of competition between firms shapes adoption decisions because firms invest in IT to gain a competitive edge or to improve productivity/profitability—we focus on how a social planner can design an incentive structure (i.e., payment model) to induce providers to cooperate through HIEs, even though such cooperation could facilitate patients switching from one provider to another.

There has been substantial research on the value and adoption of health IT, specifically that of electronic medical records (EMR) and HIEs. Chiasson and Davidson (2004) and Romanow et al. (2012) provide a comprehensive review of health IT research over the last two decades. Fichman et al. (2011) identify salient dimensions of the healthcare domain and recommend further research on the role of information systems. Much of the work on health IT has focused on EMR. For instance, the impact of EMR on physician productivity (Lee et al. 2013; Bhargava and Mishra 2014), workflow (Zheng et al. 2010), quality of care (McCullough et al. 2013; Aron et al. 2011), and care efficiency (Menon and Lee. 2000; Angst et al. 2011; Dranove et al. 2014) has been examined in the past. Prior work has also examined vulnerabilities caused by EMR and how to address them (Ahsen et al. 2019; Kim et al. 2020). Research on the adoption and value of HIEs is recent. Using longitudinal data on adoption decisions, Yaraghi et al. (2013) demonstrate network effects in HIE’s diffusion among various types of healthcare providers. Miller and Tucker (2014) show that hospital size is an important determinant of EMR and HIE adoption and that larger hospitals are more likely to adopt EMR but less likely to adopt HIE. Grounding their research in social network theory, service operations theory, and institutional isomorphism theory, Yaraghi et al. (2015) identify HIE adoption and use behaviors from a longitudinal database of medical practices. Desai (2013) examines the impact of competition on provider’s HIE-adoption decisions. Two recent empirical studies examine the value of HIEs. Ayer et al. (2019) use a large sample to study the impact of HIEs on length of stay in the emergency setting while Adjerid et al. (2018) study the moderating role of capitation-based payments in HIE’s impact on reduced costs. Although these empirical studies expand our understanding of HIEs, there is a lack of generalizable evidence regarding the cost and quality benefits of HIEs (Rahurkar et al. 2015) especially in the context of emerging payment models.

There exist a few theoretical models examining various drivers of HIE adoption and value. Ozdemir et al. (2011) show that when a patient controls the sharing of health information, an independent platform providing personal health record (PHR) services can align the incentives for information exchange under competition. They present the online PHR services Google Health and Microsoft HealthVault as evidence to support their findings. However, Google’s decision to discontinue the initiative and the uncertainty in Microsoft’s business model suggest that empowering consumers may not necessarily drive information sharing (Morris et al. 2012). The view that HIE adoption can be driven by incentivizing providers and by eliminating the need for patients to carry their health records across providers is consistent with the realities of the healthcare industry and expert opinion (Mahajan 2016; Frank 2016). Demirezen et al. (2016) show that subscription fees affect the sustainability of providers’ participation in HIEs. However, unlike our study, these studies investigate the value and thus adoption of HIEs without any reference to the underlying payment model.

There is voluminous literature in the healthcare domain about the role of payment models in the delivery of healthcare services. The health-economics literature consists of two broad streams: (1) the use of coordination mechanisms such as cost sharing on the demand side (i.e., patients) to maximize social welfare (Zeckhauser 1970), and (2) the impact of payment characteristics on the efficient delivery of care on the supply side (i.e., providers) (Ellis and McGuire 1986). Our study falls under the second stream and we refer readers to Newhouse (1996) and Cutler and Zeckhauser (2000) for a comprehensive review of the literature on payment models. Recent research has studied payment models in the healthcare domain to assess their impacts on patient selection (Ata et al. 2013), quality outcomes (Fuloria and Zenios 2001), patient waiting times (Jiang et al. 2012), providers’ workload and compensation (Powell et al. 2012), provider’s process compliance (Lee and Zenios 2012), hospital readmission (Carey 2015), the payer’s problem of choosing providers’ proposals to bundle payments (Gupta and Mehrotra 2015), and the impact of physician integration on the bundling of payments (Vlachy et al. 2020). However, to the best of our knowledge, there is no prior research on the role of payment models for incentivizing HIE adoption or on the value of HIEs under different payment models.

Because the type and the extent of healthcare services provided depend on the payment terms agreed upon between the payer and the provider, our research is also related to the vast literature on contracting. Since the early 1990s, the theory of incentives has been extensively studied within vast application areas (Gibbons 2005). For instance, in the IS literature, issues related to contract design have been studied in the context of IT outsourcing services, such as software development (Dey et al. 2010; Wu et al. 2012; Chen and Bharadwaj 2009), and information security management (Lee et al. 2013; Cezar et al. 2013; Rowe 2007). The contracting problem we study has distinctive characteristics in that it deals with multiple agents (i.e., providers) with sequential efforts exerted in stages where the outcome in each stage is determined by two types of efforts (observable and unobservable), and agents control not only the levels of efforts they exert but also the sharing of observable efforts with subsequent agents via HIEs.

## Model Description

Our model setup includes Provider A, Provider B, a single payer, and a heterogeneous population of patients with a mass normalized to one. The payer behaves as a social planner in the sense that it seeks to maximize the social payoff. The U.S. Centers for Medicare and Medicaid Services (CMS) is an example of such a payer. We label a particular disease or health condition requiring a provider’s attention as an episode.<sup>2</sup> When an episode strikes a patient, the patient visits one of the two providers. Patients have heterogeneous preferences for the provider they want to visit first. The patient’s provider choice for the first visit could arise from factors such as the distance of the provider from the patient or the provider’s reputation. We assume without loss of generality that ?? fraction of the patient population prefers Provider A and ??<sup>̃</sup>: = 1 − ?? fraction of the patient population prefers Provider B, where $1 / 2 \leq$ $\theta < 1 . ^ { 3 }$ For a patient, if the treatment succeeds (referred to as cured) at the end of the first visit, the episode ends. If the treatment in the first visit fails (referred to as not cured), the patient can choose to visit the other provider or return to the same provider in a second visit to seek care for the same condition.<sup>4</sup> The episode ends after two visits whether or not the patient is cured after the second visit.

In any of the visits related to a healthcare episode, we call the services rendered by the provider for diagnosing and treating the health condition effort. The provider effort consists of both observable and unobservable aspects. We denote the level of observable and unobservable efforts exerted by provider ?? during a visit, given that the patient (possibly) visited provider ?? in a previous visit corresponding to the same episode, using $e _ { i j }$ and $\begin{array} { r } { \hat { e } _ { i j } , } \end{array}$ respectively. Clearly, $i \in \{ \mathrm { A } , \mathrm { B } \}$ , but ?? can take one of three values: ?? = 0 when it is the patient’s first visit, ?? = ?? when the patient returns to ?? for a second visit, and $j \neq i ,$ which we denote as $j = ( - i )$ , when the patient switches to provider ?? for a second visit after visiting the other provider first.

We assume that there is a single HIE platform that providers can adopt. We consider the HIE adoption as indicating both contributing to and retrieving from a common information pool, which is consistent with “directed exchanges,” in which a provider both sends and receives information.<sup>5</sup> We treat only the observable effort as sharable information with the other provider. The two providers can exchange observable efforts via the HIE only if they both adopt it. We let $S _ { i } \in \{ \mathrm { H } , \mathrm { N } \}$ represent the HIE status of provider ?? with H denoting the adoption and N denoting the nonadoption of HIE. This, in turn, generates four possible adoption-status pairs based on the providers’ HIE adoption decisions: $\mathsf { \bar { ( } { S _ { A } } , { S _ { B } } ) } \in \{ { ( \mathrm { H } , \mathrm { H } ) } , { ( \mathrm { \bar { \mathrm { H } } } , \mathrm { N } ) } , { ( \mathrm { N } , \mathrm { H } ) } , { ( \mathrm { N } , \mathrm { N } ) } \}$

The probability that a patient is cured in any visit depends on several factors, including the provider efforts in the current visit, available provider efforts from the previous visit relating to the episode, and providers’ HIE adoption decisions. Specifically, we make the following observations regarding the probability of cure in any visit.

1. The observable and unobservable efforts exerted by the provider during the current visit affect the treatment outcome.

2. If the current visit is the patient’s second visit to the same provider during an episode, then the observable and unobservable efforts exerted by the provider during the first visit also affect the outcome because the provider will have access to the details of the previous visit.

3. The HIE adoption status affects the cure probability because the HIE facilitates coordination through the communication of clinical records. The HIE has an impact only when both providers adopt it. Thus, we define the following indicator function for the providers’ HIE statuses:

$$
\mathbf {p} _ {(S _ {\mathrm{A}}, S _ {\mathrm{B}})} = \left\{ \begin{array}{l l} 1, & \text {if (S_{A} , S_{B}) = (H,H),} \\ 0, & \text {otherwise.} \end{array} \right.
$$

When both providers adopt HIE, i.e., $\mathbf { p } _ { ( S _ { A } , S _ { B } ) } = 1$ , the following effects occur: (1) the HIE allows both providers to have access to the entire patient history, specifically the observable efforts in prior episodes. The clinical history benefits the providers and improves the cure probability regardless of whether it is the first or the second visit for the patient. We denote this effect using parameter ??. (2) More importantly, when a patient visits a different provider for a second visit in the current episode, the HIE allows the second provider to have access to the first provider’s observable effort related to the current episode.<sup>6</sup>

![](/api/attachments/G23RDAG8/fulltext/images/154f928c96d4120467a3912f872a96ffc12697d89dc54bd592e9a53e6f422b0c.jpg)  
Figure 1. Patient Pathways for $\bigotimes \bigotimes _ { i = 0 } ^ { \infty } \bigotimes \bigotimes$

We assume that the primary impact of an HIE on the cure probability is related to the sharing of observable effort in the same episode rather than the sharing of observable effort from prior episodes, i.e., ?? is not too high relative to $e _ { i ( - i ) }$

We assume that the probability of cure in a visit is a nondecreasing concave function in all available provider efforts. For easier exposition and simplicity, we assume a linear probability function.<sup>7</sup> A linear function for the probability of success or benefit is common in the literature for model tractability reasons (Koh et al. 2017; Varian 2004; Hao et al. 2017). Let $\beta _ { i j } ^ { \mathbf { p } }$ be the probability of cure when the patient visits provider ??, given that the patient has possibly visited ?? previously and the HIE status is $\mathbf { p } _ { ( S _ { \mathbf { A } } , S _ { \mathbf { B } } ) }$ . Then we have the following:

$$
\beta_ {i j} ^ {\mathbf {p}} = \left\{ \begin{array}{l l} e _ {i 0} + \hat {e} _ {i 0}, & \text {if j = 0 and \mathbf {p} = 0 ,} \\ \alpha + e _ {i 0} + \hat {e} _ {i 0}, & \text {if j = 0 and \mathbf {p} = 1 ,} \\ e _ {i 0} + \hat {e} _ {i 0} + e _ {i i} + \hat {e} _ {i i}, & \text {if j = i and \mathbf {p} = 0 ,} \\ \alpha + e _ {i 0} + \hat {e} _ {i 0} + e _ {i i} + \hat {e} _ {i i}, & \text {if j = i and \mathbf {p} = 1 ,} \\ e _ {i (- i)} + \hat {e} _ {i (- i)}, & \text {if j = -i and \mathbf {p} = 0 ,} \\ \alpha + e _ {i (- i)} + \hat {e} _ {i (- i)} + e _ {(- i) 0}, & \text {if j = -i and \mathbf {p} = 1 .} \end{array} \right.
$$

Figure 1 provides the schematic of the possible paths the patient can take in getting care for the episode, possible outcomes, and their probabilities.<sup>8</sup>

Provider efforts are costly. We assume a quadratic cost function for both effort types. Thus, we let the cost of $e _ { i j }$ be $\delta e _ { i j } ^ { 2 }$ and, analogously, the cost of $\hat { e } _ { i j }$ be $\delta \hat { e } _ { i j } ^ { 2 }$ , where $\delta >$ 0. If the patient is still not cured at the end of the episode, the patient incurs a positive treatment failure cost. The treatment failure cost, which represents the cost of diminished quality of life, varies across patients (Nease et al. 1995; Sassi 2006). Such patient heterogeneity in the cost of non-cure is standard in health care economics models (Chandra et al. 2011). We assume two types of patients: high and low. The high-type patients incur a cost of $u _ { H }$ for treatment failure and the low-type patients incur a cost of $u _ { L }$ for treatment failure, $0 < u _ { L } < u _ { H }$ . We assume that ?? fraction of patients belong to the high type and denote this as $1 - \epsilon = \tilde { \epsilon } .$ . We let ?? denote the mean treatment failure cost $( \mathrm { i . e . , ~ } U = \epsilon u _ { H } + \tilde { \epsilon } u _ { L } )$ . The treatment failure cost information is private to the patient; however, its distribution is common knowledge.

The patient’s disutility at the end of the episode, if not cured, also depends on whether the patient visited a single provider or both providers during the episode. Clearly, the benefit of visiting a single provider, relative to visiting two different providers, is that, in the former case, the single provider has access to all provider efforts in that episode whereas, in the latter case, the second provider in the episode does not have access to all efforts from the first visit. However, in reality, some patients do switch providers during the episode suggesting that patients do realize a benefit from switching. Specifically, when patients are not satisfied with the quality of care from a provider, they may switch to another provider (Jung et al. 2011) for various reasons, e.g., to obtain an alternative perspective on a health condition (Harris 2003; Olsen et al. 1976). We model the benefit of provider switching for a patient as a reduction in the disutility of non-cure at the end of the episode. Thus, we let $\mu$ denote the reduction in a patient’s disutility of non-cure if the patient visits both providers during the episode, and refer to $\mu$ as the benefit of switching.<sup>9</sup>

Engaging in information sharing through HIEs is a serious and costly undertaking (Vest and Gamm 2010) and providers need to pay the HIE platform operator for using it. Consistent with the subscription fee model in which the fee is based on the base volume of patients and/or episodes (e.g., see Demirezen et al. 2016), we let $C _ { \mathrm { H I E } }$ be each provider’s per-patient-per-episode cost of adopting and using the HIE, and therefore Provider $\mathrm { A } \mathbf { \bar { s } }$ HIE adoption cost is $\theta C _ { \mathrm { H I E } }$ and Provider B’s HIE adoption cost is (1 − $\theta ) C _ { \mathrm { H I E } } .$ 10

Following the per-patient-per-episode level of analysis, we let $\omega _ { i } \geq 0$ be the reservation payoff of provider ?? for providing care to the patient during an episode. We assume that the cost of efforts is sufficiently high and that other model parameters are such that the treatment in each visit has a nonzero and less-than-one probability of failure, so as to allow second visits for some patients, and to ensure that the HIE adoption decision is nontrivial and that the objective functions for every player are well behaved so as to yield interior solutions for their maximization problems.

## Benchmark: First-Best Solution

We first examine a benchmark scenario in which a centralized social planner makes socially optimal choices regarding effort levels and HIE adoption and induces socially optimal patient behavior. Clearly, the social payoff is the highest under the benchmark. While designing a payment model, the social planner would desire to induce providers and patients to make the same decisions as those under the benchmark. We refer to the optimal decisions in the benchmark scenario as the first-best solution.

We use backward induction to derive the first-best solution. We begin with a patient’s decision when the patient is not cured after the first visit to the preferred provider. Consider a patient who is not cured after the first visit to provider ??. For patient type $y \in \{ H , L \}$ , where ?? and ?? denote high type and low type, respectively, if the patient goes to provider $i , i \neq j$ , for the second visit, the patient’s expected future payoff conditional on the HIE status ??, denoted as $V _ { i j y } ^ { \mathbf { p } } .$ , is given by

$$
{V _ {i j y} ^ {\mathbf {p}}} {:= - (1 - \beta_ {i j} ^ {\mathbf {p}}) d _ {i j y} =}
$$

$$
\left\{ \begin{array}{l l} - (1 - e _ {i (- i)} - \hat {e} _ {i (- i)}) d _ {i j y}, & \text {if \mathbf {p} = 0 and i\neq j ,} \\ - (1 - \alpha - e _ {i (- i)} - \hat {e} _ {i (- i)} - e _ {(- i) 0}) d _ {i j y}, & \text {if \mathbf {p} = 1 and i\neq j ,} \\ - (1 - e _ {j 0} - \hat {e} _ {j 0} - e _ {j j} - \hat {e} _ {j j}) d _ {i j y}, & \text {if \mathbf {p} = 0 and i = j ,} \\ - (1 - \alpha - e _ {j 0} - \hat {e} _ {j 0} - e _ {j j} - \hat {e} _ {j j}) d _ {i j y}, & \text {if \mathbf {p} = 1 and i = j .} \end{array} \right.
$$

Where $d _ { i j y }$ is defined as

$$
d _ {i j y} := \left\{ \begin{array}{l l} u _ {y} - \mu , & \text {if i\neq j for \forall y\in\{H,L\}}, \\ u _ {y}, & \text {if i = j for \forall y\in\{H,L\}}. \end{array} \right.
$$

If $V _ { i j y } ^ { \mathbf { p } } > V _ { j j y } ^ { \mathbf { p } }$ , the patient switches to provider ?? for the second visit after visiting provider ??; otherwise, the patient stays with the same provider ?? for the second visit.

The social planner will choose the optimal HIE adoption status and provider efforts that will induce the desired patient switching behavior to maximize the social payoff. We use $k _ { y }$ to denote the provider in the second visit for a patient with type ?? preferring Provider A and $l _ { y }$ to denote the provider in the second visit for a patient with type ?? preferring Provider B. Then, given the patient switching behavior indicated by quadruple $( k _ { H } , l _ { H } , k _ { L } , l _ { L } )$ and HIE adoption status $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , we formulate the social planner’s problem, as provided in Appendix A, which yields the following observation.

Lemma 1: Regardless of HIE adoption status, if a hightype patient switches the provider for the second visit, then a low-type patient also switches the provider for the second visit. However, the reverse does not hold, i.e., if a low-type patient switches the provider for the second visit, then it is not necessary that a high-type patient also switches the provider for the second visit.

Lemma 1 reveals that three patient switching scenarios for the second visit are possible in equilibrium: (1) both lowand high-type patients switch providers, (2) neither lowtype nor high-type patients switch providers, and (3) hightype patients do not switch providers but low-type patients do. The switching scenario in the equilibrium depends on the values of model parameters and the HIE adoption status. Furthermore, the patient switching behavior can differ across payment models as well as in the first-best solution, resulting in a large number of possible patient switching scenarios if the entire parameter space is considered. For tractability and expositional clarity, we highlight the results when $u _ { H }$ is sufficiently large such that high-type patients never switch providers, regardless of HIE adoption. When $u _ { H }$ is sufficiently large, low-type patients may or may not switch depending on parameter values, resulting in either Scenario (2) or (3) in equilibrium under the first-best and all payment models. We note that the results presented in the main paper hold qualitatively for the scenario where both high-type and low-type patients switch providers regardless of HIE adoption.

Observe that $( k _ { H } , l _ { H } ) = ( \mathtt { A } , \mathtt { B } )$ regardless of the HIE adoption scenario when ?? is sufficiently large. We characterize the possible patient behaviors in the equilibrium, assuming a second visit occurs, using visit pairs $( k , l ) \colon = ( k _ { L } , l _ { L } ) = \{ ( \mathrm { A } , \mathrm { A } ) , ( \mathrm { B } , \mathrm { B } ) , ( \mathrm { A } , \mathrm { B } ) , ( \mathrm { B } , \mathrm { A } ) \}$ Then, given the possible patient switching behavior in the equilibrium indicated by pair (??, ??) and HIE adoption status $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , the social planner’s optimal efforts for patient-switching Scenario (3), i.e., high-type patients do not switch but low-type patients do, are given by the solution to Model (1) below:

$$
\begin{array} { l }\overbrace {\begin{array} { c }\operatorname * { m a x } _ { \substack { e _ { i 0 } , \hat { e } _ { i 0 } , e _ { i i } , \hat { e } _ { i i ^ { \prime } }\\e _ { k A } , \hat { e } _ { k A ^ { \prime } }\\e _ { l B } , \hat { e } _ { l B ^ { \prime } }\\\forall l \neq B } } \Pi ^ { k l } ( S _ { A } , S _ { B } )\\\end{array}} ^ { \text {Expected per patient social payoff when initial visit occurs at A and patient type is high} }\\= \overbrace { \theta \epsilon \left[ \overbrace { - \delta e _ { A 0 } ^ { 2 } - \delta \hat { e } _ { A 0 } ^ { 2 } } ^ { C o s t   o f   i n i t i a l   v i s i t   t o   A } + \overbrace { ( 1 - \beta _ { A 0 } ^ { p } ) } ^ { S e c o n d   v i s i t   p r o b a b i l i t y } \overbrace { ( - \delta e _ { A A } ^ { 2 } - \delta \hat { e } _ { A A } ^ { 2 } - d _ { A A H } ( 1 - \beta _ { A A } ^ { p } ) ) } ^ { C o s t   o f   s e c o n d   v i s i t   t o   k } \right] } ^ { \text {Expected per patient social payoff when initial visit occurs at A and patient type is low} }\\+ \overbrace { \theta \bar { \epsilon } \left[ - \delta e _ { A 0 } ^ { 2 } - \delta \hat { e } _ { A 0 } ^ { 2 } + ( 1 - \beta _ { A 0 } ^ { p } ) ( - \delta e _ { k A } ^ { 2 } - \delta \hat { e } _ { k A } ^ { 2 } - d _ { k A L } ( 1 - \beta _ { k A } ^ { p } ) ) ) \right] } ^ { \text {Expected per patient social payoff when initial visit occurs at B and patient type is high} }\\+ \overbrace { ( 1 - \theta ) \epsilon \left[ - \delta e _ { B 0 } ^ { 2 } - \delta \hat { e } _ { B 0 } ^ { 2 } + ( 1 - \beta _ { B 0 } ^ { p } ) ( - \delta e _ { B B } ^ { 2 } - \delta \hat { e } _ { B B } ^ { 2 } - d _ { B B H } ( 1 - \beta _ { B B } ^ { p } ) ) ) \right] } ^ { \text {Expected per patient social payoff when initial visit occurs at B and patient type is low} }\\+ \overbrace { ( 1 - \theta ) \tilde { \epsilon } \left[ \right. - \delta e _ { B 0 } ^ { 2 } - \delta \hat { e } _ { B 0 } ^ { 2 } + ( 1 - \beta _ { B 0 } ^ { p } ) ( - \delta e _ { l B } ^ { 2 } - \delta \hat { e } _ { l B } ^ { 2 } - d _ { l B L } ( 1 - \beta _ { l B } ^ { p } ) ) ) ] } ^ { \text {Expected per patient social payoff when initial visit occurs at B and patient type is low} }\\- \overbrace { \theta ( \mathbf { 1 } _ { S _ {\mathrm{A}}} C _ {\mathrm{HIE}} ) - ( 1 - \theta ) ( \mathbf { 1 } _ { S _ {\mathrm{B}}} C _ {\mathrm{HIE}} ) } ^ { E x p e c t e d   p a r   p a t i e n t   c o s t   o f   H I E }\\s . t .\\V _ { k A L } ^ { P } \geq V _ {\bar { K} A L } ^ { P }, f o r k \in \{A , B \} ,\\V _ { l B L } ^ { P } \geq V _ {\bar { I} B L } ^ { P }, f o r l \in \{A , B \} ,\\\end{array}\tag{1}
$$

where $\Pi ^ { k l } ( S _ { \mathrm { \tiny A } } , S _ { \mathrm { \tiny B } } )$ is the expected social payoff under HIE adoption status $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ and patient switching behavior $( k , l ) , \mathbf { 1 } _ { s _ { i } }$ is an indicator function for provider ??’s HIE adoption status; one if $S _ { i } = H$ , zero otherwise, and ${ \bar { k } } = A \operatorname { i f } k = B$ and B otherwise and ${ \bar { l } } = A { \mathrm { ~ i f ~ } } l = B$ and B otherwise.

The social payoff function consists of five main parts as described by the text above the brackets in each part. We note that the two constraints in the model above denote the incentive compatibility constraints related to the patient’s switching behavior. The social planner’s models for the scenario where low-type patients do not switch providers can be shown in an analogous manner.

Let the optimal social payoff for the HIE adoption status $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ and patient switching behavior (??, ??) be $\Pi ^ { * k l } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } ) . ^ { 1 1 }$ Clearly, the social planner will choose the $( k , l )$ and $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ that will result in the maximum $\Pi ^ { * k l } ( S _ { \mathrm { \AA } } , S _ { \mathrm { \AA } } )$ . For any patient switching behavior (??, ??), the social planner will choose HIE adoption only when $\Pi ^ { * k l } ( \mathrm { H } , \mathrm { H } )$ is greater than $\Pi ^ { * k l } ( \mathsf { N } , \mathsf { N } )$ . The asymmetric HIE adoption scenarios in which only one provider adopts an HIE cannot be an optimum solution under any patient switching behavior because health information sharing can bring value only when both providers participate in the exchange. This implies that asymmetric adoption scenarios cannot be better than nonadoption by either provider, i.e., $\Pi ^ { * k l } ( \mathbb { N } , \mathrm { H } ) < \Pi ^ { * k l } ( \mathbb { N } , \mathbb { N } )$ and $\Pi ^ { * \dot { k } \dot { l } } ( \mathrm { H } , \mathrm { N } ) \dot { < } \Pi ^ { * k l } ( \mathrm { N } , \mathrm { N } )$ for any (??, ??).

Before we present the first-best solution, let $\overline { { C } } _ { \mathrm { H I E } } ( \mu )$ (or simply $\overline { { C } } _ { \mathrm { H I E } } )$ denote the threshold on $C _ { \mathrm { H I E } }$ for a given ?? while $\mu _ { H H }$ and $\mu _ { N N }$ , respectively, denote thresholds on ?? for HIE adoption scenarios (H, H) and (N, N). We then have the following lemma. The expressions for $\overline { { C } } _ { \mathrm { H I E } } ( \mu )$ and $\mu _ { S _ { \tt A } S _ { \tt B } }$ and the proofs for our main results are provided in Appendix A.

## Lemma 2: The first-best solution is specified as follows.

a. For any given ??, the social planner adopts the HIE if $C _ { H I E } < \overline { { C } } _ { H I E } ( \mu )$ and does not adopt the HIE otherwise.

b. Under HIE adoption scenario $( S _ { A } , S _ { B } ) \in$ $\{ ( H , H ) , ( N , N ) \}$ , the low-type patients switch providers for their second visit if and only $\mathrm { \it { i f } } \mu > \mu _ { S _ { A } S _ { B } } .$

## c. The optimal effort levels are as shown in Table 1.

Lemma 2a is intuitive; it shows that, under any patient switching scenario, the social planner will not prefer HIE adoption if the cost of the HIE is greater than the benefit offered by it in that scenario. Lemma 4b reveals that the patient’s optimal provider choice for the second visit depends on both the benefit of switching and HIE adoption status. If the benefit of switching is low (i.e., $\mu \leq \mu _ { H H } )$ then the social planner will prefer the equilibrium in which the low-type patient returns to the same provider, even when HIE adoption is socially optimal. This is because the benefit from the availability of both observable and unobservable efforts from the first visit when the patient returns to the same provider exceeds any benefit from switching to a different provider even when the providers adopt HIE.

On the other hand, if the benefit of switching is high (i.e., $\mu > \mu _ { N N } ) .$ then the social planner prefers the low-type patient going to a different provider even when HIE adoption is not socially optimal. That is, returning to the same provider is not welfare maximizing despite the lack of sharing of the observable effort from the initial visit with the other provider. Hence, in both of these cases (i.e., low and high benefit of switching), HIE plays no role in the social planner’s preference for the patient’s provider switching behavior. When the benefit of switching is moderate (i.e., $\mu _ { H H } < \mu \leq \mu _ { N N } )$ , the social planner prefers that the low-type patient returns to the same provider if HIE is not adopted and switches to the other provider if the HIE is adopted. In a way, the benefit arising from the HIEenabled availability of prior observable effort makes switching to the other provider preferable from the social planner perspective.

Corollary 1: When high-type patients do not switch, under the first-best solution, the HIE adoption alters low-type patients’ provider choice for the second visit only if the benefit of switching is moderate (i.e., $\mu _ { H H } < \mu \leq \mu _ { N N } ) .$

The corollary reveals that in the first-best case with a moderate benefit of switching, the coordination through HIE adoption by both providers intensifies the competition between the providers by inducing low-type patients to switch providers for their second visit. The concern of providers that HIE participation may erode their competitive advantage has been widely documented in the popular press and academic research (e.g., see Yaraghi 2015, Adler-Milstein and Jha 2012). The above result clearly reflects such an observation, but only when the benefit from switching providers is neither high nor low.

<table><tr><td colspan="3">Table 1. The First-Best Effort Levels</td></tr><tr><td></td><td> $C_{\text{HIE}} \geq \overline{C}_{\text{HIE}}(\mu)$ </td><td>Otherwise</td></tr><tr><td> $\mu \leq \mu_{HH}$ </td><td> $e_{i0}^{*} = \frac{U(4\delta - U)}{4\delta(\delta + 2U)}$  $\hat{e}_{i0}^{*} = \frac{U(4\delta - U)}{4\delta(\delta + 2U)}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{U}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} := NA$ </td><td> $e_{i0}^{*} = \frac{U(4\delta(1 - \alpha) - U)}{4\delta(\delta + 2U)}$  $\hat{e}_{i0}^{*} = \frac{U(4\delta(1 - \alpha) - U)}{4\delta(\delta + 2U)}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{U}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} := NA$ </td></tr><tr><td> $\mu_{HH} < \mu \leq \mu_{NN}$ </td><td> $e_{i0}^{*} = \frac{U(4\delta - U)}{4\delta(\delta + 2U)}$  $\hat{e}_{i0}^{*} = \frac{U(4\delta - U)}{4\delta(\delta + 2U)}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{U}{\frac{2\delta}{2\delta}}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} := NA$ </td><td> $e_{i0}^{*} = \tilde{e}_{io}^{1}(\text{HH})$  $\hat{e}_{i0}^{*} = \tilde{e}_{io}^{2}(\text{HH})$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{u_{H}}{\frac{2\delta}{2\delta}}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = \frac{u_{L} - \mu}{\frac{2\delta}{2\delta}}$ </td></tr><tr><td> $\mu_{NN} < \mu$ </td><td> $e_{i0}^{*} = \tilde{e}_{io}(\text{NN})$  $\hat{e}_{i0}^{*} = \tilde{e}_{io}(\text{NN})$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{u_{H}}{\frac{2\delta}{2\delta}}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = \frac{u_{L} - \mu}{\frac{2\delta}{2\delta}}$ </td><td> $e_{i0}^{*} = \tilde{e}_{io}^{1}(\text{HH})$  $\hat{e}_{i0}^{*} = \tilde{e}_{io}^{2}(\text{HH})$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{u_{H}}{\frac{2\delta}{2\delta}} \\e_{i(-i)}, \hat{e}_{i(-i)}^{*} = \frac{u_{L} - \mu}{\frac{2\delta}{2\delta}}$ </td></tr><tr><td colspan="2">Note: We use “NA” to denote the case when the variable for the corresponding condition is not applicable. We define  $\tilde{e}_{io}(\text{NN}) := \frac{-\mu\tilde{\epsilon}(2\delta + \mu) - u_{H}^{2}\epsilon + 4\delta u_{H}\epsilon}{4\delta(\delta + 2u_{H}\epsilon)} - \frac{u_{L}^{2}\tilde{\epsilon}}{4\delta(\delta + 2u_{H}\epsilon)} + \frac{u_{L}\tilde{\epsilon}(\delta + \mu)}{2\delta(\delta + 2u_{H}\epsilon)}.$  $\tilde{e}_{io}^{1}(\text{HH}) := \frac{-8\delta^{2}\mu\tilde{\epsilon} + u_{H}^{2}u_{L}\tilde{\epsilon}\epsilon + 8\delta^{2}u_{H}\epsilon + u_{L}^{3}(\tilde{\epsilon})^{2} - 4\delta u_{L}^{2}\tilde{\epsilon} + 2\delta u_{L}^{2}\tilde{\epsilon}\epsilon + 8\delta^{2}u_{L}\tilde{\epsilon} + 8\delta\mu u_{L}\tilde{\epsilon}}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\tilde{\epsilon})^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\tilde{\epsilon})^{2})}+ \frac{-4\delta\mu^{2}\tilde{\epsilon} + 2\delta\mu^{2}\tilde{\epsilon}\epsilon + u_{H}^{2}\epsilon(-\mu\tilde{\epsilon} - 2\delta) - 3\mu u_{L}^{2}(\tilde{\epsilon})^{2} - 4\delta\mu u_{L}\tilde{\epsilon}\epsilon + 3\mu^{2}u_{L}(\tilde{\epsilon})^{2} - \mu^{3}(\tilde{\epsilon})^{2}}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\tilde{\epsilon})^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\tilde{\epsilon})^{2})}+ \frac{\alpha(8\delta^{2}\mu\tilde{\epsilon} + 2\delta\mu^{2}\tilde{\epsilon} - 2\delta\mu^{2}\tilde{\epsilon}\epsilon - 8\delta^{2}u_{H}\epsilon + 2\delta u_{L}^{2}(\tilde{\epsilon})^{2} - 8\delta^{2}u_{L}\tilde{\epsilon} - 4\delta\mu u_{L}(\tilde{\epsilon})^{2})}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\tilde{\epsilon})^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\tilde{\epsilon})^{2})}.$  $\tilde{e}_{io}^{2}(\text{HH}) := \frac{4\delta^{2}\mu(\epsilon - 1) - u_{H}^{2}u_{L}(\tilde{\epsilon})\epsilon + 8\delta^{2}u_{H}\epsilon + u_{L}^{3}(-(\tilde{\epsilon})^{2}) + 4\delta^{2}u_{L}\tilde{\epsilon} + 4\delta\mu u_{L}\tilde{\epsilon}}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\tilde{\epsilon})^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\til de)^{2})}+ \frac{-2\delta\mu^{2}\tilde{\epsilon} + u_{H}^{2}\epsilon(-2\delta + \mu - \mu\epsilon) - u_{L}^{2}\tilde{\epsilon}(2\delta + 3\mu(\epsilon - 1)) - 3\mu^{2}u_{L}(\tilde{\epsilon})^{2} + \mu^{3}(\til de)^{2}}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\epsilon - 1)^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\epsilon - 1)^{2})}+ \frac{\alpha(4\delta^{2}\mu\tilde{\epsilon} - 8\delta^{2}u_{H}\epsilon - 4\delta^{2}u_{L}\tilde{\epsilon})}{2\delta(4\delta^{2} - 4\delta\mu\tilde{\epsilon} + 8\delta u_{H}\epsilon - u_{L}^{2}(\epsilon - 1)^{2} - 2u_{L}\tilde{\epsilon}(-\mu\tilde{\epsilon} - 2\delta) - \mu^{2}(\epsilon - 1)^{2})}$ </td><td></td></tr></table>

## Contracting Problem under Prevailing Payment Models

The benchmark analysis and results hold when the social planner decides on effort levels and HIE adoption status. However, in practice, the payer contracts with providers to compensate for the services they render and providers make decisions to maximize their own payoffs by considering the contract terms. Therefore payer and provider incentives may not be aligned. In this section, we consider two of the prevailing payment models: FFS and P4P. Our primary goal is to examine whether either of these payment models can induce the first-best solution in a non-cooperative setting.

We assume the following sequence of events, regardless of the payment contract type offered (for FFS and P4P in the current section and EBP considered in the next section).

Stage 1: The payer offers a payment contract and each provider either accepts or rejects the contract.

Stage 2: If a provider accepts the contract, the provider chooses to either adopt or not adopt the HIE.

Stage 3: When a patient visits the preferred provider in the first visit, the provider exerts efforts and incurs the effort costs.

Stage 4: If the treatment is successful, the episode moves to Stage 6; otherwise, the patient chooses the provider for the second visit.

Stage 5: The provider in the second visit exerts efforts and incurs the effort costs.

Stage 6: The payer reimburses the provider (or both providers) based on the contract payment terms, all parties realize their respective payoffs, and the episode ends.

We assume that the payer is the social planner seeking to maximize the expected social welfare. In Stages 3 and 5, the provider exerts efforts to maximize the expected (future) payoff from serving a patient. In Stage 2, the providers make HIE adoption decisions based on the expected future payoff from serving the whole patient population. The timeline is consistent with the notion that a provider’s efforts are shortterm decisions focusing on the specific patient, but the provider’s adoption of an HIE is a long-term decision that accounts for the possible impacts of the decision on the expected payoff for the entire episode and for the whole patient population. In Stage 1, the social planner offers a contract that is acceptable to both providers to avoid the deadweight loss to the society, i.e., the loss to a patient if the preferred provider does not participate. We use backward induction to solve the contracting problem and derive the subgame perfect Nash equilibrium. When the payer is indifferent between two values for any payment contract term, the provider will choose the smaller value in all payment models.

We assume that the payer is the social planner seeking to maximize the expected social welfare. In Stages 3 and 5, the provider exerts efforts to maximize the expected (future) payoff from serving a patient. In Stage 2, the providers make HIE adoption decisions based on the expected future payoff from serving the whole patient population. The timeline is consistent with the notion that a provider’s efforts are shortterm decisions focusing on the specific patient, but the provider’s adoption of the HIE is a long-term decision that accounts for the possible impacts of the decision on the expected payoff for the entire episode and for the whole patient population. In Stage 1, the social planner offers a contract that is acceptable to both providers to avoid the deadweight loss to the society, i.e., the loss to a patient if the preferred provider does not participate. We use backward induction to solve the contracting problem and derive the subgame perfect Nash equilibrium. When the payer is indifferent between two values for any payment contract term, the provider will choose the smaller value in all payment models.

In our notation for the payment models, we use superscripts F for FFS and P for P4P. In Stage 3 and Stage 5 of the contracting game, we use $\pi _ { i j } ^ { \mathrm { M } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ to denote provider ??’s payoff in the patient’s current visit to ?? after visiting provider ?? in the previous visit under payment model M and HIE adoption scenario $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ Provider ?? maximizes $\pi _ { i j } ^ { \mathrm { M } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ for $j \in \{ i , - i \}$ by exerting optimal efforts for the second visit in Stage 5. In Stage 3, anticipating the optimal $\pi _ { i j } ^ { \mathrm { M } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ in Stage 5, the provider maximizes $\pi _ { i 0 } ^ { \mathrm { { M } } } ( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } )$ by exerting optimal efforts for the first visit.<sup>12</sup> In Stage 2, provider ?? maximizes $\overline { { \pi } } _ { i } ^ { \mathrm { M } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , which denotes the provider’s expected future payoff for the entire episode and for the whole patient population under payment model M and HIE adoption scenario $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ . The payoff function is given by the following:

$$
\begin{array}{l} \overline {{\pi}} _ {i} ^ {\mathrm{M}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = \\ \left\{ \begin{array}{l l} D _ {i} \pi_ {i 0} ^ {*} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) + D _ {(- i)} \tilde {\epsilon} (1 - \beta_ {(- i) 0} ^ {\mathbf {p}}) \\ \pi_ {i (- i)} ^ {*} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) - D _ {i} C _ {\text {HIE}}   \mathbf {p} _ {(S _ {\mathrm{A}}, S _ {\mathrm{B}})}, & \text {if low type swiches,} \\ \theta \pi_ {i 0} ^ {*} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) - D _ {i} C _ {\text {HIE}}   \mathbf {p} _ {(S _ {\mathrm{A}}, S _ {\mathrm{B}})}, & \text {otherwise}, \end{array} \right. \end{array}\tag{2}
$$

where $D _ { i } = \theta$ if $i = \mathsf { A }$ and $D _ { i } = \tilde { \theta }$ otherwise, and $\pi _ { i 0 } ^ { \mathrm { M } * } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ and $\pi _ { i j } ^ { \mathrm { M } * } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ for $j \in \{ i , - i \}$ are provider $i \ ' \mathbf { s }$ maximal expected payoffs from a patient’s first and second visit, respectively.

## Contracting under the Fee-for-Service Payment Model

Under the FFS payment model, a medical payment claim consists of two main components: (1) the medical condition for which the patient has sought attention, which is indicated by a code called the International Classification of Diseases in its 10th version (ICD-10), and (2) tests, procedures, devices, and treatments provided, which are captured by current procedural terminology (CPT) codes (e.g., see Berenson et al. 2012). To capture the former component, we let $\tau ^ { \mathrm { F } }$ denote the fixed payment to a provider if the patient visits the provider during the episode. The fixed payment to a provider is assumed to be paid when the patient visits that provider for the first time during the episode. To capture the variable component, we let $\gamma _ { 1 } ^ { \mathrm { F } }$ denote the payment per unit of observable effort for the patient’s first visit to a provider. Analogously, we let $\gamma _ { 2 } ^ { \mathrm { F } }$ denote the payment per unit of observable effort for a return visit to the same provider.

If the patient visits provider ?? in Stage 5 of the game, the provider chooses efforts $e _ { i j }$ and $\hat { e } _ { i j }$ to maximize the payoff in that stage given by the following:

$$
\begin{array}{r l} \pi_ {i j} ^ {\mathrm{F}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = & \left\{ \begin{array}{l l} \gamma_ {1} ^ {\mathrm{F}} e _ {i j} + \tau^ {\mathrm{F}} - \delta e _ {i j} ^ {2} - \delta \hat {e} _ {i j} ^ {2}, & \mathrm{if} j \neq i, \\ \gamma_ {2} ^ {\mathrm{F}} e _ {i j} - \delta e _ {i j} ^ {2} - \delta \hat {e} _ {i j} ^ {2}, & \mathrm{if} j = i. \end{array} \right. \end{array}\tag{3}
$$

In Stage 4, the patient chooses the second-visit provider using the decision rule discussed in the benchmark case, i.e., the patient chooses the provider that offers a higher patient payoff in the second visit. In Stage 3 of the game, if the patient visits provider ??, then the provider chooses efforts $e _ { i 0 }$ and $\hat { e } _ { i 0 }$ to maximize the provider’s future payoff given by the following:

$$
\begin{array}{l} \pi_ {i 0} ^ {\mathrm{F}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = \\ \left\{ \begin{array}{l l} \tilde {\epsilon} (\gamma_ {1} ^ {\mathrm{F}} e _ {i 0} + \tau^ {\mathrm{F}} - \delta e _ {i 0} ^ {2} - \delta \hat {e} _ {i 0} ^ {2}) + \epsilon (\gamma_ {1} ^ {\mathrm{F}} e _ {i 0} + \tau^ {\mathrm{F}} \\ - \delta e _ {i 0} ^ {2} - \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) \pi_ {i i} ^ {\mathrm{F*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}})), & \text {if low type switch,} \\ \gamma_ {1} ^ {\mathrm{F}} e _ {i 0} + \tau^ {\mathrm{F}} - \delta e _ {i 0} ^ {2} - \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) \pi_ {i i} ^ {\mathrm{F*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}), & \text {otherwise.} \end{array} \right. \end{array} \tag {4}
$$

Substituting the optimal Stage 3 and Stage 5 efforts into the payoff functions of Providers A and B, we solve the HIE adoption subgame in Stage 2. Finally, anticipating the providers’ decisions regarding HIE adoption and effort levels, the payer chooses the contract terms, $\gamma _ { 1 } ^ { \mathrm { F } } , \gamma _ { 2 } ^ { \mathrm { F } }$ , and $\tau ^ { \mathrm { F } }$ in Stage 1 that maximize the social payoff subject to the providers’ participation constraints. Let $\bar { \mu ^ { F } } ( S _ { \mathrm { \AA } } , S _ { \mathrm { \AA } } )$ provided in Appendix A, be the threshold for the patient’s benefit from switching under the FFS model and HIE adoption scenario $( S _ { \mathrm { A } } , \bar { S } _ { \mathrm { B } } )$

Lemma 3: The equilibrium under FFS has the following properties:

a. Neither provider adopts HIE.

b. The low-type patients return to their preferred provider after an unsuccessful treatment in the first visit $i f \mu \leq$ $\mu ^ { F } ( N , N )$ and switches to the other provider, otherwise.

c. The optimal effort levels and optimal contract parameters are as shown in Table 2.

Two observations from Lemma 3 are worth noting. (1) Neither provider adopts an HIE in the equilibrium under the FFS model. The primary reason for this finding is that HIE adoption neither increases the marginal benefit nor reduces the marginal cost of efforts to providers under this payment model. Therefore, for any given stage, providers’ optimal efforts, and hence payments as well as effort costs, are identical under $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( \mathrm { { H } , \mathrm { { H } ) } }$ and $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( \mathrm { { N } , \mathrm { { N } ) } }$ scenarios. However, the cost associated with adoption causes providers to not adopt HIE.<sup>13</sup> (2) Regardless of patient switching behavior, neither provider exerts a positive unobservable effort, i.e., $\hat { e } _ { i ( - i ) } ^ { * } = \hat { e } _ { i i } ^ { * } = \hat { e } _ { i 0 } ^ { * } = 0$ The reason for this finding is that there is no payment contingent on the unobservable effort, but this effort is costly for providers. The lack of observable effort reflects the moral hazard problem that exists in the FFS model and is well recognized in the healthcare literature (Ellis and McGuire 1996).

<table><tr><td colspan="3">Design of the F-NN Contract</td></tr><tr><td> $^{\dagger } \mu \leq \mu^{F}(S_{\mathrm {A}}^{*}, S_{\mathrm {B}}^{*})$ </td><td> $e_{i0}^{*} = \frac{4\gamma_{1}^{\mathrm {F}*}\delta - (\gamma_{2}^{\mathrm {F}*})^{2}}{8\delta^{2}}$  $e_{ii}^{*} = \frac{\gamma_{2}^{\mathrm {F}*}}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = NA$  $\hat{e}_{i0}^{*}, \hat{e}_{ii}^{*} = 0$ </td><td> $\gamma_{1}^{\mathrm {F}*} = \frac{U^{3} + 8\delta^{2}U}{4\delta^{2} + 4\delta U}$  $\tau^{\mathrm {F}*} = \dot{\tau}^{\mathrm {F}}$  $\gamma_{2}^{\mathrm {F}*} = U$ </td></tr><tr><td> $^{\ddagger } \mu > \mu^{F}(S_{\mathrm {A}}^{*}, S_{\mathrm {B}}^{*})$ </td><td> $e_{i0}^{*} = \frac{4\gamma_{1}^{\mathrm {F}*}\delta - \epsilon(\gamma_{2}^{\mathrm {F}*})^{2}}{8\delta^{2}}$  $e_{ii}^{*} = \frac{\gamma_{2}^{\mathrm {F}*}}{2\delta}$  $e_{i(-i)}^{*} = \frac{\gamma_{1}^{\mathrm {F}*}}{2\delta}$  $\hat{e}_{i0}^{*}, \hat{e}_{ii}^{*}, \hat{e}_{i(-i)}^{*} = 0$ </td><td> $\gamma_{1}^{\mathrm {F}*} = \ddot{\gamma}_{1}^{\mathrm {F}}$  $\tau^{\mathrm {F}*} = \ddot{\tau}^{\mathrm {F}}$  $\gamma_{2}^{\mathrm {F}*} = \ddot{\gamma}_{2}^{\mathrm {F}}$ </td></tr></table>

Note: We provide the expressions for $\overline { { \dot { \tau } ^ { \mathrm { F } } , \ddot { \tau } ^ { \mathrm { F } } , \ddot { \gamma } _ { 1 } ^ { \mathrm { F } } } } ,$ and ??̈<sup>F</sup> in Appendix A. We use “NA” to denote the case when the variable for the corresponding condition is not applicable. <sup>†</sup>: Low type returns to the same provider for the second visit. <sup>‡</sup>: Low type visits the other provider for the second visit.

Proposition 1: The social planner cannot induce the firstbest solution under the FFS payment model.

Lemma 3 and Proposition 1 suggest that, from the social planner’s perspective, the FFS model suffers from three limitations: (1) it does not induce HIE adoption even when the social planner prefers HIE adoption by both providers (i.e., when $C _ { \mathrm { H I E } } < \overline { { C } } _ { \mathrm { H I E } } )$ . (2) It does not necessarily induce the socially optimal patient switching behavior. For instance, when $\mu ^ { F } ( \mathbf { N } , \mathbf { \bar { N } } ) < \mu \leq \mu _ { N N }$ , while the social planner desires the low-type patients to return to the same provider under no HIE, the FFS induces low-type patients to switch to the other provider. (3) It does not induce the desired observable effort and is unable to induce any unobservable effort. Clearly, unobservable provider effort gives rise to a moral hazard issue under FFS, which partly explains the failure to achieve the first-best solution. A standard approach to mitigating moral hazard is to make payments contingent on observable outcomes. A P4P payment model that we examine next follows this approach.

## Contracting Under the Pay-for-Performance Model

Under a P4P model, a provider is paid a fixed amount for a patient visit (analogous to the fixed payment in the FFS payment model), but the pay for performance is implemented using one of two approaches—using a penalty or using a reward. The penalty-based approach penalizes a provider for an unsuccessful visit outcome, while the reward-based approach rewards a provider for a successful visit outcome. Both approaches are equivalent in our context, as any penalty-based P4P model can be converted into an equivalent reward-based P4P model that yields identical outcomes and vice versa. Consequently, we present only a penalty-based P4P model, hereafter referred to simply as the P4P model. Under the P4P model, we let $\tau ^ { \mathrm { P } }$ denote the fixed payment to a provider if the patient visits during the episode. The fixed payment to a provider is assumed to be paid when the patient visits that provider for the first time during the episode. We let $p _ { 1 }$ denote the penalty for a poor quality outcome if it is the patient’s first visit to the provider, and $p _ { 2 }$ denote the penalty for a poor quality outcome if it is the return visit to the same provider. No penalty is imposed if the patient is cured.

If the patient visits provider ?? in Stage 5 of the game, the provider’s payoff in that stage is given by the following:

$$
\pi_ {i j} ^ {\mathbf {p}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = \left\{ \begin{array}{l l} \tau^ {\mathbf {p}} - \delta e _ {i j} ^ {2} - \delta \hat {e} _ {i j} ^ {2} - p _ {1} (1 - \beta_ {i j} ^ {\mathbf {p}}), & \text {if} j \neq i, \\ - \delta e _ {i j} ^ {2} - \delta \hat {e} _ {i j} ^ {2} - p _ {2} (1 - \beta_ {i j} ^ {\mathbf {p}}), & \text {if} j = i. \end{array} \right.\tag{5}
$$

In Stage 3 of the game, if the patient visits provider ??, then the provider’s expected future payoff is given by the following:

$$
\begin{array}{l} \pi_ {i 0} ^ {\mathrm{P}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = \\ \left\{ \begin{array}{l l} \tilde {\epsilon} (\tau^ {\mathrm{P}} - \delta e _ {i 0} ^ {2} - \delta \hat {e} _ {i 0} ^ {2} - p _ {1} (1 - \beta_ {i 0} ^ {\mathbf {p}})) + \epsilon (\tau^ {\mathrm{P}} - \delta e _ {i 0} ^ {2} & \text {   if   low   type   } \\ - \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) (- p _ {1} + \pi_ {i i} ^ {\mathrm{P*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}))), & \text {   switch,   } \\ \tau^ {\mathrm{P}} - \delta e _ {i 0} ^ {2} - \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) (- p _ {1} + \pi_ {i i} ^ {\mathrm{P*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}})), & \text {   otherwise.   (6)   } \end{array} \right. \end{array}
$$

Following the backward induction procedure, we solve for the equilibrium under the P4P model. Unlike the equilibrium under the FFS model, there are two possible HIE adoption scenarios in the equilibrium under the P4P model: an equilibrium in which both providers adopt HIEs corresponding to the adoption status $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( H , H )$ and an equilibrium in which neither provider adopts an HIE corresponding to the adoption status $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( N , N )$ The former (latter) equilibrium occurs when $C _ { \mathrm { H I E } }$ is less than (greater than or equal to) a threshold value. Let $\overline { { C } } _ { \mathrm { H I E } } ^ { \mathrm { P } }$ be the threshold for the cost of HIE as given in Appendix A. Also, let $\mu ^ { \mathrm { P } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , provided in Appendix A, be the threshold for the benefit from switching under the P4P model and HIE adoption scenario $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$

Lemma 4: The equilibrium under P4P has the following properties:

a. Neither provider adopts an HIE $i f C _ { H I E } \geq \overline { { C } } _ { H I E } ^ { P } ,$ , but both adopt HIEs $i f C _ { H I E } < \overline { { C } } _ { H I E } ^ { P }$

b. Under an HIE adoption scenario $( S _ { A } , S _ { B } ) \in$ $\{ ( H , H ) , ( N , N ) \}$ , the low-type patients return to their preferred provider after an unsuccessful treatment in the first visit $i f \mu \leq \mu ^ { P } ( S _ { A } , S _ { B } )$ and switch to the other provider, otherwise.

c. The optimal effort levels and optimal contract parameters are as shown in Table 3.

Comparing Lemma 3 and Lemma 4, we observe that the P4P model can induce a nonzero unobservable effort, unlike the FFS model. Clearly, a penalty for a bad outcome increases the marginal benefit of both observable and unobservable efforts, leading to a nonzero unobservable effort that is nondecreasing in the penalty ??. However, it is also clear from Lemma 4 that the equilibrium under the P4P model can differ from that in the benchmark.

Proposition 2: (a) If $\mu \leq m i n [ \mu ^ { P } ( N , N ) , \mu _ { N N } ]$ and $C _ { H I E } > m a x [ \overline { { C } } _ { H I E } , \overline { { C } } _ { H I E } ^ { P } ] ,$ , then the social planner can induce the first-best solution under the P4P model. (b) If $\mu \leq m i n [ \mu ^ { P } ( H , H ) , \mu _ { H H } ]$ and $C _ { H I E } \leq m i n [ \overline { { C } } _ { H I E } , \overline { { C } } _ { H I E } ^ { P } ] ,$ then the social planner can induce the first-best solution under the P4P model. (c) In other cases, the social planner cannot induce the first-best solution under the P4P model.

A comparison of Proposition 1 and Proposition 2 reveals that the P4P model is superior to the FFS model in the following ways: (1) the P4P model can induce the first-best solution under some conditions whereas the FFS model can not induce the first-best solution under any condition, (2) the P4P model can induce positive unobservable efforts and thus partly mitigate the moral-hazard problem present under the FFS model. Basically, under the P4P model, the penalty parameter ?? motivates the provider to exert unobservable effort to reduce the expected penalty while there is no such motivation under the FFS model. (3) The P4P model possibly induces HIE adoption when it is socially desirable while the FFS model can not induce HIE adoption at all. (4) Lastly, the P4P model can induce a patient switching behavior that is socially desirable by penalizing the providers for poor quality of care and by internalizing the costs and benefits of HIE adoption. Despite the superiority of the P4P model over the FFS model along the above dimensions, the P4P model falls short relative to the first-best solution in the sense that the P4P model does not always induce socially optimal HIE adoption decisions, patient switching behavior, nor socially optimal effort levels.

In summary, the analysis of this section shows that currently popular FFS or P4P payment models do not always induce the first-best solution. Therefore, a critical question faced by a social planner is whether a new payment model can be designed that is guaranteed to induce the first-best solution, namely socially optimal HIE adoption decisions, effort levels, and patient behavior. We answer this question affirmatively in the next section by proposing and analyzing an EBP model.

## Contracting under the Episode-Based Payment Model

The proposed EBP model makes payments to provide is contingent on the episode outcome, denoted by ??. In particular, the following outcomes are possible in an episode: (1) the patient is cured after the first visit (??), (2) the patient is cured after a second visit to the same provider (????), (3) the patient is not cured after a second visit to the same provider (????), (4) the patient is cured after the patient switches to a different provider for the second visit (????), and (5) the patient is not cured after the patient switches to a different provider for the second visit (????).

<table><tr><td colspan="5">Table 3. Optimal Effort Levels and Equilibrium Contract under the P4P Payment Model</td></tr><tr><td></td><td colspan="2">If  $C_{HIE} \geq \overline{C}_{HIE}^{P}$ ,design the P-NN contract</td><td colspan="2">Otherwise,design the P-HH contract</td></tr><tr><td> $^{\dagger}\mu \leq \mu^{P}(S_{A}^{*}, S_{B}^{*})$ </td><td> $e_{i0}^{*}, \hat{e}_{i0}^{*}$  $= \frac{2\delta p_{1}^{*} + 4\delta p_{2}^{*} - (p_{2}^{*})^{2}}{4\delta(\delta + 2p_{2}^{*})}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{p_{2}^{*}}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = NA$ </td><td> $p_{1}^{*} = 0$  $\tau^{P*} = \dot{\tau}^{P}(N, N)$  $p_{2}^{*} = U$ </td><td colspan="2"> $e_{i0}^{*}, \hat{e}_{i0}^{*}$  $= \frac{2\delta p_{1}^{*} + 4\delta(1 - \alpha)p_{2}^{*} - (p_{2}^{*})^{2}}{4\delta(\delta + 2p_{2}^{*})}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{p_{2}^{*}}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = NA$ </td></tr><tr><td> $^{\ddagger}\mu > \mu^{P}(S_{A}^{*}, S_{B}^{*})$ </td><td> $e_{i0}^{*}, \hat{e}_{i0}^{*}$  $= \frac{2\delta p_{1}^{*} + 4\delta\epsilon p_{2}^{*} - \epsilon(p_{2}^{*})^{2}}{4\delta(\delta + 2\epsilon p_{2}^{*})}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{p_{2}^{*}}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*} = \frac{p_{1}^{*}}{2\delta}$ </td><td> $p_{1}^{*} = \ddot{p}_{2}(N, N)$  $\tau^{P*} = \ddot{\tau}^{P}(N, N)$  $p_{2}^{*} = \ddot{p}_{2}(N, N)$ </td><td> $e_{i0}^{*}, \hat{e}_{i0}^{*}$  $= \frac{2\delta p_{1}^{*} + 4\delta(1 - \alpha)\epsilon p_{2}^{*} - \epsilon(p_{2}^{*})^{2}}{4\delta(\delta + 2\epsilon p_{2}^{*})}$  $e_{ii}^{*}, \hat{e}_{ii}^{*} = \frac{p_{2}^{*}}{2\delta}$  $e_{i(-i)}^{*}, \hat{e}_{i(-i)}^{*}= \frac{p_{1}^{*}}{2\delta}$ </td><td> $p_{1}^{*} = \ddot{p}_{2}(H, H)$  $\tau^{P*} = \ddot{\tau}^{P}(H, H)$  $p_{2}^{*} = \ddot{p}_{2}(H, H)$ </td></tr></table>

Note: We provide the expressions for $\dot { \tau } ^ { \mathrm { P } } ( \mathrm { H } , \mathrm { H } ) , \ddot { \tau } ^ { \mathrm { P } } ( \mathrm { H } , \mathrm { H } ) , \ddot { p } _ { 1 } ( \mathrm { H } , \mathrm { H } )$ , and ??̈ (H, H) in Appendix A. We use $\mathrm { \Delta ^ { 6 6 } N A } ^ { 5 }$ to denote the case when the variable for the corresponding condition is not applicable. <sup>†</sup>: Low type returns to the same provider for the second visit. <sup>‡</sup>: Low type visits the other provider for the second visit.

Under the EBP model, we let $\tau _ { n } ^ { \mathrm { E } }$ denote the fixed payment to the provider in the patient’s $n ^ { t h } , n \in \{ 1 , 2 \}$ visit in the episode. The fixed payment to a provider is assumed to be paid when the patient visits that provider for the first time during the episode. We define the outcome-dependent payment to the provider in the $n ^ { t h }$ visit under outcome $o \in \{ C , C S , N S , C D , N D \}$ in EBP as $P _ { n o }$ . The game sequence for the EBP model remains identical to that for FFS and P4P models. Let ?? be the provider in the patient’s second visit and ?? be the provider in the patient’s first visit. Then, provider ?? maximizes the following payoff in Stage 5.

$$
\begin{array}{r l} & {\pi_ {i j} ^ {\mathrm{E}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) =} \\ & {\left\{ \begin{array}{l l} \tau_ {2} ^ {\mathrm{E}} + \beta_ {i j} ^ {\mathbf {p}} P _ {2 C D} + (1 - \beta_ {i j} ^ {\mathbf {p}}) P _ {2 N D} - \delta (e _ {i j} ^ {2} + \hat {e} _ {i j} ^ {2}), & \mathrm{if} j \neq i, \\ \beta_ {i j} ^ {\mathbf {p}} P _ {2 C S} + (1 - \beta_ {i j} ^ {\mathbf {p}}) P _ {2 N S} - \delta (e _ {i j} ^ {2} + \hat {e} _ {i j} ^ {2}), & \mathrm{if} j = i. \end{array} \right.} \end{array}
$$

In Stage 3 of the game, provider ?? in the patient’s first visit maximizes the following payoff.

$$
\begin{array}{c} \pi_ {j _ {0}} ^ {\mathrm{E}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) = \\ \left\{ \begin{array}{l l} \tilde {\epsilon} (\tau_ {1} ^ {\mathrm{E}} - \delta (e _ {j _ {0}} ^ {2} + \hat {e} _ {j _ {0}} ^ {2}) + \beta_ {j _ {0}} ^ {\mathbf {p}} P _ {1 C} & \\ + (1 - \beta_ {j _ {0}} ^ {\mathbf {p}}) (\beta_ {i j} ^ {\mathbf {p}} P _ {1 C D} + (1 - \beta_ {i j} ^ {\mathbf {p}}) P _ {1 N D})) & , \text {if low type} \\ + \epsilon (\tau_ {1} ^ {\mathrm{E}} - \delta (e _ {j _ {0}} ^ {2} + \hat {e} _ {j _ {0}} ^ {2}) + \beta_ {j _ {0}} ^ {\mathbf {p}} P _ {1 C} & \text {switches}, \\ + (1 - \beta_ {j _ {0}} ^ {\mathbf {p}}) \pi_ {j j} ^ {\mathrm{P*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}})) & \\ \tau_ {1} ^ {\mathrm{E}} - \delta (e _ {j _ {0}} ^ {2} + \hat {e} _ {j _ {0}} ^ {2}) + \beta_ {j _ {0}} ^ {\mathbf {p}} P _ {1 C} & \\ + (1 - \beta_ {j _ {0}} ^ {\mathbf {p}}) \pi_ {j j} ^ {\mathrm{P*}} (S _ {\mathrm{A}}, S _ {\mathrm{B}}) & , \text {otherwise}. \end{array} \right. \end{array}\tag{8}
$$

(??)

Following the backward induction procedure, we derive the equilibrium under EBP which is characterized in the following proposition.

Proposition 3: The social planner induces the first-best solution via the contracts specified in Table 4.

An important feature of the first-best inducing EBP model is that fixed wages are paid upfront and subsequent payment adjustments are made at the end of the episode rather than at the end of each visit, as in FFS and P4P models. Specifically, we highlight the following distinctive characteristics of the first-best-inducing EBP contract.

<table><tr><td colspan="3">Table 4. First-Best Inducing EBP Contracts</td></tr><tr><td></td><td>If  $C_{HIE} \geq \overline{C}_{HIE}$ ,Design the E-NN Contract</td><td>Otherwise,Design the E-HH Contract</td></tr><tr><td> $\mu \leq \mu_{HH}$ </td><td rowspan="3"> $\tau_{1}^{E*} = \dot{\tau}_{1}^{E}(N,N)$  $P_{2NS}^{*} = -U$ </td><td> $\tau_{1}^{E*} = \dot{\tau}_{1}^{E}(H,H)$  $P_{2NS}^{*} = -U$ </td></tr><tr><td> $\mu_{HH} < \mu \leq \mu_{NN}$ </td><td rowspan="2"> $\tau_{1}^{E*} = \dot{\tau}_{1}^{E}(H,H)$  $P_{1C}^{*} = \ddot{P}_{1C}(H,H)$  $P_{1CD}^{*} = \frac{2\delta(e_{i0}^{*} - \hat{e}_{i0}^{*})}{\tilde{\epsilon}(1 - \alpha - e_{i0}^{*} - \hat{e}_{i0}^{*})} + P_{1ND}^{*}$  $P_{1ND}^{*} = \ddot{P}_{1ND}(H,H)$  $P_{2CD}^{*} = \ddot{P}_{2CD}(H,H)$  $P_{2CS}^{*} = \ddot{P}_{2CS}(H,H)$  $P_{2ND}^{*} = -(u_{L} - \mu) + P_{2CS}^{*}$  $P_{2NS}^{*} = -(u_{L} - \mu) + P_{2CS}^{*}$ </td></tr><tr><td> $\mu > \mu_{NN}$ </td></tr></table>

Note: $e _ { i 0 } ^ { * }$ and $\hat { e } _ { i 0 } ^ { * }$ denote the first-best effort levels we derived from Lemma 4. We provide the expressions for $\dot { P } _ { n o } , \ddot { P } _ { n o } , \dot { \tau } ^ { \mathrm { E } } ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , and $\because \ d \div \mathrm { \tt { F } } _ { i } ( S _ { \mathrm { \tt A } } , S _ { \mathrm { \tt B } } )$ $\forall ( S _ { \mathrm { A } } , S _ { \mathrm { B } } ) \in \{ ( { \ddot { H } } , H ) , ( N , N ) \}$ in Appendix A. Furthermore, all parameter not indicated in the table are set to zero.

First, when patient switching is not socially desirable, regardless of HIE adoption, i.e., $\mu \leq \mu _ { H H } ,$ a simple contract in which the provider is paid a fixed payment at the beginning of the episode and imposed a penalty for not curing the patient after a second visit is sufficient to induce the first-best outcomeNote that $P _ { 2 N S } ^ { * }$ is negative when $\mu \leq$ $\mu _ { H H }$ . Because patients do not switch, the episode effectively involves a single provider. Hence, the contract is unilateral in the sense that the payment to the provider depends only on the provider’s performance. Second, when switching by low-type patients is socially desirable but HIE adoption is not, i.e., $\mu \leq \mu _ { H H }$ and $C _ { \mathrm { H I E } } \geq \overline { { C } } _ { \mathrm { H I E } }$ the contract is unilateral. However, unlike no switching, the contract includes payment adjustments for both cure and no-cure scenarios when the patient visits the same provider.

Specifically, in the case of no cure at the end of the episode, a penalty of $P _ { 2 N S } ^ { * } < 0$ is imposed on the provider, and in the case of a cure at the end of episode, the payment to the provider is adjusted by $P _ { 2 C S } ^ { * }$ , where $P _ { 2 C S } ^ { * } > P _ { 2 N S } ^ { * }$ holds. Third, when switching by low-type patients and HIE adoption are both socially desirable, i.e., $\mu > \mu _ { N N }$ and $C _ { \mathrm { H I E } } < \overline { { C } } _ { \mathrm { H I E } }$ , the EBP contract is multilateral in the sense that the payment to a provider is contingent not only on the provider’s performance but also on the performance of the other provider. For instance, consider the case in which a patient is not cured in the first visit and switches to a different provider for the second visit. The payment to the provider in the first visit differs depending on whether the patient is cured or not in the second visit, i.e., $P _ { 1 N D } ^ { * } \neq P _ { 1 C D } ^ { * }$

Fourth, when desirable switching behavior is affected by HIE adoption status, i.e., $\mu _ { H H } < \mu \leq \mu _ { N N }$ , the first-best inducing EBP contract is unilateral if HIE adoption is not socially desirable and multilateral if HIE adoption is socially desirable. Fifth, regardless of desirable patient switching behavior and HIE adoption, the fixed payment to a provider is contingent on whether the patient visits the provider first or second. Furthermore, the outcome-dependent payment adjustment can also differ for the first and the second providers if switching is desirable. For instance, note that $P _ { 1 N D } ^ { * } \neq P _ { 2 N D } ^ { * }$ . This observation suggests that the sequence of visits during the episode affects provider payments.

The main reason underlying the above five findings is the nature of externality created by HIE. When a provider adopts HIE, the observable effort (and only the observable effort exerted) affects the outcome of the other provider. We refer to this as the effort-related externality. Moreover, the shared observable effort enabled by the HIE benefits only the second provider. We refer to this as the sequencerelated externality. A multilateral and sequence-dependent payment model fully accounts for the two externality dimensions, and thus it can induce the first-best solution.

When patient switching is not desirable, neither provider should be able to influence nor be influenced by the other provider’s effort, and therefore, a unilateral, but still sequence-dependent, EBP contract is sufficient to induce the first-best solution.

## Practicality of the Proposed EBP Model

The EBP model we propose is clearly superior to the currently dominant FFS and P4P models, and no other payment model can be strictly superior to it from a social welfare perspective. We present the main features of the three types of contracts we considered to highlight similarities and differences among them in Table 5.

An important question that naturally arises is whether our EBP model is implementable in practice. At a high level, the EBP model we propose reflects some features of existing payment models, especially those that have been recently introduced as part of healthcare reforms. The three noteworthy programs relating to the EBP contract we propose are bundled payments, VBP programs, and accountable care organizations (ACO). The EBP model shares some of the features of all three payment programs while also differing from them in other aspects. These programs’ details are complex. However, we briefly compare these programs to the EBP model we propose.

Bundled payment programs aggregate FFS payments around an episode of care and build bundles (Cutler and Ghosh 2012). Currently, alternative bundled payment strategies are being tested and, as of October 2015, there were 1,551 healthcare organizations participating in the CMS’s bundled payment initiatives. Under these initiatives, the CMS was able to successfully define episodes of care with a clear beginning and an end for a number of conditions (Press et al. 2016). There have also been successful attempts at episodic payments in the private payer setting (e.g., see de Brantes et al. 2009, for an example of payments for an episode of bypass surgery). The payments under the EBP model are based on the whole episode, as in the bundled payment program. However, our EBP model provides a specific payment to each provider that participates in the episode, whereas the bundled payment program makes only a lump-sum payment for the episode without specifying how to allocate the overall payment among providers.

VBP programs implement a modifier to adjust payments to individual hospitals based on their comparative performance (Rau 2013). As the largest payer in the U.S., the CMS provides a high-level description of how payment modifiers are calculated. Specifically, hospitals are given so-called achievement points that are awarded by comparing an individual hospital’s performance with that of other hospitals (CMS 2013). In some sense, VBP payments resemble the multilateral nature of EBP. However, our EBP model assesses provider performance at the individual episode level, whereas the VBP program assesses performance at an aggregate level for a period such as a year. Furthermore, a specific VBP program called the Hospital Readmission Reduction Program (HRRP), implements sequence-dependent payments. Under the HRRP, the CMS penalizes hospitals that have comparatively higher readmission rates, where readmission is defined as the all-cause 30-day excess readmission ratio following initial hospital visits. In essence, a hospital that sees the patient first realizes a payment reduction if the patient is later readmitted (e.g., to another hospital), (Kocher and Adashi 2011). Such payment adjustment is consistent with sequencedependent payments of the EBP model we propose.

Providers voluntarily come together under an ACO and coordinate care for patients with the objective of reducing costs while preserving quality. If the participating providers demonstrate cost savings while meeting some quality standards, the payer rewards the providers based on the cost savings. Setting the right incentives for participating providers is important for the success of an ACO (American Academy of Actuaries 2012). Sequencebased payments of our EBP program reflect the spirit of one of the Medicare-driven ACO programs called the “Shared Savings Program” in which two or more disparate providers as part of a single ACO decide how to appropriate the yearly savings or rewards received from the payer. The providers can determine the distribution of savings to each participant in multiple ways. One such distribution scheme is based on each provider’s contribution to reduced need for utilization of services and the quality at different points during the episode, hence making both the sequence and outcome important factors in the allocation of payment adjustments (Bailit and Hughes 2011).

The above comparisons suggest that the most notable aspects of the proposed EBP model are already being experimented with by payer organizations and regulatory agencies as part of various initiatives. Therefore, the proposed EBP model does not pose unique implementation challenges that are difficult to overcome.

<table><tr><td colspan="4">Table 5. Comparison of Features of Payment Models</td></tr><tr><td>Contract Features</td><td>FFS</td><td>P4P</td><td>EBP</td></tr><tr><td>Fixed payment</td><td>YES</td><td>YES</td><td>YES</td></tr><tr><td>Variable payment for observable effort</td><td>YES</td><td>NO</td><td>NO</td></tr><tr><td>Payment adjustment for visit outcome</td><td>NO</td><td>YES</td><td>NO</td></tr><tr><td>Payment adjustment for episode outcome</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>Multilaterality</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>Sequence dependency across provider payments</td><td>NO</td><td>NO</td><td>YES</td></tr></table>

However, the key insight we derive is that achieving socially desirable coordination and efforts from providers requires that key elements of the programs under experimentation such as bundled payments, VBP, and ACO, be integrated into a single program such as the EBP model we propose.

Although the EBP contract is promising from a social welfare perspective (as it achieves the first-best solution) and also because different aspects of it are already being experimented with in reality, the complexity of the EBP model may pose a challenge for implementation. For example, if more than two providers are involved in an episode, it will be more difficult to define and implement the already complex EBP contract. Future research could develop algorithmic approaches and devise near-optimal and possibly less complex contracts while taking our EBP contract as the baseline for optimality.

## Comparison of Payment Models

In this section, we examine the three payment models more closely. Specifically, we compare the payment models along three outcome metrics: healthcare cost, quality of care, and payment to providers. These metrics respectively help us assess outcomes from the social planner’s, patients’, and providers’ perspectives. After contrasting the payment models along the three important dimensions, we also examine the value of HIEs under each payment model, as HIEs promise to eliminate duplicate testing, thus providing savings, and coordinate care between providers.

We present analytical results for parameter space where patient switching behavior is the same across the payment models, and an HIE is not adopted. Technically, we assume the following: $C _ { \mathrm { H I E } } \geq m a x [ \overline { { C } } _ { \mathrm { H I E } } , \overline { { C } } _ { \mathrm { H I E } } ^ { \mathrm { P } } ]$ and $\mu \leq$ ?????? $[ \mu _ { \mathrm { N , N } } , \mu ^ { \mathrm { F } } ( \mathrm { N } , \mathrm { N } ) , \mu ^ { \mathrm { P } } ( \mathrm { N } , \mathrm { N } ) ]$ . The primary reasons for the above restrictions are threefold: (1) There are six possible equilibrium regions in the first-best (as well as the EBP model), two different equilibrium regions under FFS model, and four different equilibrium regions under the P4P model. Consequently, an exhaustive comparison of the payment models will require examining a large number of combinations of these regions. (2) The FFS model does not induce HIE adoption, and (3) a closedform solution for the equilibrium contract does not exist when low-type patients switch under the FFS and P4P models, eliminating the possibility of analytical comparison of the payment models for some parameter region. We conducted extensive numerical analysis to complement our theoretical results. We present a representative set of numerical results in Appendix B.

## Healthcare Cost, Quality of Care, and Payment

Conditional on an episode taking place, we denote the healthcare cost as the negative of the expected social payoff defined earlier which accounts for both the patients’ cost when they are not cured and the providers cost in treating the patients. We denote the quality of care and the payment for provider efforts for adoption scenario $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ using $\Sigma ( S _ { \mathrm { A } } , \bar { S } _ { \mathrm { B } } )$ and $\Gamma ( S _ { \mathrm { \scriptscriptstyle A } } , S _ { \mathrm { \scriptscriptstyle B } } )$ , respectively (we assume the reservation wage to be zero to focus on service-related payments). We compute these quantities in expectation over an episode as:

$$
\Sigma (S _ {\mathrm{A}}, S _ {\mathrm{B}}) :=
$$

$$
\left\{ \begin{array}{l l} 1 - \tilde {\epsilon} (1 - \beta_ {i 0} ^ {\mathbf {p}}) (1 - \beta_ {(- i) i} ^ {\mathbf {p}}) - \epsilon (1 - \beta_ {i 0} ^ {\mathbf {p}}) (1 - \beta_ {i i} ^ {\mathbf {p}}) & , \text { if   low   type   switch }, \\ 1 - (1 - \beta_ {i 0} ^ {\mathbf {p}}) (1 - \beta_ {i i} ^ {\mathbf {p}}) & , \text { otherwise }. \end{array} \right. \tag {9}
$$

$$
\Gamma (S _ {\mathrm{A}}, S _ {\mathrm{B}}) :=
$$

$$
\left\{ \begin{array}{l l} \tilde {\epsilon} (\delta e _ {i 0} ^ {2} + \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {(- i) 0} ^ {\mathbf {p}}) (\delta e _ {i (- i)} ^ {2} + \delta \hat {e} _ {i (- i)} ^ {2})) \\ + \epsilon (e _ {i 0} ^ {2} + \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) (\delta e _ {i i} ^ {2} + \delta \hat {e} _ {i i} ^ {2})) & , \text {   if   low   type   switch, } \\ \delta e _ {i 0} ^ {2} + \delta \hat {e} _ {i 0} ^ {2} + (1 - \beta_ {i 0} ^ {\mathbf {p}}) (\delta e _ {i i} ^ {2} + \delta \hat {e} _ {i i} ^ {2}) & , \text {   otherwise. } \end{array} \right. \tag {10}
$$

In the above definitions, $\Sigma ( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ is calculated as one minus the probability of non-cure at the end of the episode and $\Gamma ( S _ { \mathrm { \scriptscriptstyle A } } , S _ { \mathrm { \scriptscriptstyle B } } )$ is calculated as the cost of effort at the preferred provider plus the expected cost of effort in a possible second visit (based on non-cure in the first visit).

Proposition 4: Suppose $C _ { H I E } \geq m a x [ \overline { { C } } _ { H I E } , \overline { { C } } _ { H I E } ^ { P } ]$ and $\mu \leq m a x [ \mu _ { N N } , \mu ^ { F } ( N , N ) , \mu ^ { P } ( N , N ) ]$ . In total expectation, the healthcare cost and the quality of care under different payment models are ordered as follows:

a. Healthcare Cost (FFS) > Healthcare Cost $\left( P 4 P \right) =$ Healthcare Cost (EBP).

b. Quality of Care (EBP) = Quality of Care $( P 4 P ) >$ Quality of Care (FFS).

Under the conditions stated in Proposition 4, the P4P model achieves the first-best as does the EBP model. Therefore, both payment models are equivalent, and superior to FFS, in cost and quality dimensions. Because we are unable to analytically compare payment to providers under different payment models and wish to examine how comparisons of the cost and the quality dimensions change when we relax the assumptions in Proposition 4, we subsequently performed an extensive numerical analysis. The numerical computations show the following.

1. Healthcare Cost (FFS) ≥ Healthcare Cost $\mathrm { ( P 4 P ) } \geq$ Healthcare Cost (EBP).

2. Quality of Care (EBP) > Quality of Care (FFS), Quality of Care (P4P) > Quality of Care (FFS).

3. Provider Payment (EBP) > Provider Payment (FFS), Provider Payment (P4P) > Provider Payment (FFS).

It is clear that EBP delivers the lowest healthcare cost. It is also clear that both EBP and P4P are superior to FFS in terms of quality of care and provider payment. On the one hand, the finding that the EBP model always achieves the lowest healthcare cost is intuitive because the EBP model induces the first-best solution and no payment model can achieve a lower cost than the first-best solution. On the other hand, it is interesting to observe that both the EBP and the P4P models give rise to lower healthcare costs than the FFS model, not by reducing service-related payment to providers but rather by achieving a higher quality of care.

These findings also suggest that providers need not fear a loss of compensation if they move away from the FFS model. That is, the fear that a switch from FFS to other payment models will decrease their service-related compensation may be unwarranted (e.g., see Goitein 2014 and Lee 2014 for a series of discussions). Thus, instead of resisting them, providers should actually welcome new payment models. Critically, an increase in payment is likely to be accompanied by a quality improvement, which can further support provider buy-in. Overall, lower healthcare costs, higher provider payments, and higher quality of care under the EBP and P4P models imply that the current shift from volume-based care (FFS) to valuebased care (P4P and EBP) benefits all three parties involved in the care system (i.e., social planners, providers, and patients). In summary, the FFS model results in the highest total healthcare cost, lowest quality of care, and lowest total provider payment among the three payment models, thereby supporting the claim that the FFS model is inefficient.

## Value of HIEs

As stated earlier in this paper, the U.S. government is using subsidies to induce HIE adoption in facilitating patientinformation sharing among providers. The premise of subsidies is based largely on the conventional wisdom that information sharing is valuable and subsidizing HIE adoption is, therefore, a good investment. The existing research on the value of HIEs provides limited guidance to policymakers. The question of whether the U.S. government should intervene to encourage HIE adoption— and, if so, how much—is therefore not clear, especially in the face of emerging payment models. For each payment model, we define the value of HIEs as the social payoff that would be realized under the optimal effort choices of providers when providers adopt HIEs minus the social payoff under the optimal effort choices of providers when providers do not adopt HIEs.

![](/api/attachments/G23RDAG8/fulltext/images/3cbc27598e9caf2eae40e08b6905ed71ca4b162c438be898d8f6921eda5ce473.jpg)  
(a) Low-type patients do not switch regardless of HIE adoption under EBP $( \mu = 1 0 )$

![](/api/attachments/G23RDAG8/fulltext/images/3c7bd5de0d74b43dcdb8c10341ff89a81f4a08c2547e0853fb8f247ea4dfcf13.jpg)  
(b) Low-type patients switch regardless of HIE adoption under EBP $( \mu = 6 0 )$

![](/api/attachments/G23RDAG8/fulltext/images/9e96f0169d00a1339619a27ebeb76c5644fb86b74012d820a98202059e1973ef.jpg)  
(c) Low-type patients switch only when HIE is adoptedunder EBP (?? = 25)

$$
\text { Note:   We   set } \delta = 5 0 0 0, \theta = 0. 7, \alpha = 0. 0 1, u _ {H} = 1 0 0 0, u _ {L} = 3 5 0, \epsilon = 0. 1 5.
$$

As in the case of Proposition 4, we present the comparison of payment models regarding the value of HIEs for a parameter space in which patients do not switch providers under any of the three payment models and supplement the analytical result with numerical findings . <sup>14</sup>

## Proposition 5:

Suppose $\mu \leq m i n [ \mu _ { H H } , \mu ^ { F } ( N , N ) , \mu ^ { P } ( N , N ) , \mu ^ { P } ( H , H ) ] .$ In total expectation, the Value of HIE under different payment models is ordered as Value of HIE (FFS) > Value of HIE (EBP) = Value of HIE (P4P)

As stated previously, under the condition stated in Proposition 5, the P4P model achieves the first-best solution as does the EBP model. When we relax the conditions stated in Proposition 5, the numerical computations show Value of HIE (FFS) > Value of HIE (EBP) ≥ Value of HIE (P4P). Figure 2 provides a representative set of numerical results for each possible patient behavior in reference to HIE adoption status. Figure 2 reveals the following significant insights regarding the value of HIEs. First, the value of HIEs is critically dependent on the payment model. Regardless of the value of ??, i.e., regardless of patient switching behavior, the value of an HIE is the highest under FFS and (weakly) lowest under P4P. The FFS model yields the highest HIE value because, as shown in Lemma 3, providers exert solely the observable effort under FFS in order to benefit from the payment that is tied to the observable effort. HIEs enable sharing of the observable effort with the second provider and improving the cure rate in the second visit. Therefore, HIEs offer the highest value under the FFS model.

Second, the HIE value critically depends on patients’ switching behavior under all payment models. Clearly, when low-type patients switch providers, regardless of HIE adoption, the HIE value is highest (see Figure 1) because the HIE enables the sharing of observable effort across providers. The HIE value is the lowest (see Figure 1) when low-type patients do not switch providers because under the no-switching condition, the value only arises from the availability of patient information from prior episodes and not the sharing of effort across providers in the current episode. The HIE value is in the middle (see Figure 1) when the low-type patient’s switching behavior depends on HIE adoption status. Third, an HIE may offer a positive value under one payment model but a negative value under another payment model. For instance, when $C _ { \mathrm { H I E } } = 1 5$ and low-type patients switch only under HIE adoption, as in

Figure (1), the HIE is beneficial under the FFS model but is not beneficial under the P4P and EBP models.

The findings clearly suggest that the value of HIEs can be ?????????????????????????? or ???????????????????????????? if the payment model and their effects on provider and patient behavior are not explicitly accounted for. Furthermore, this finding implies that, depending on the HIE adoption cost, there exist situations in which a centralized social planner making all decisions does not find it beneficial to use an HIE, but the HIE is valuable under the FFS model. Also, there exist other situations where the social planner finds it beneficial to use an HIE, but the HIE is not valuable under the P4P model. Thus, the HIE value cannot be assessed without considering the underlying payment mechanism. Therefore, as new payment models evolve, the value of HIEs must be reevaluated and, consequently, government intervention policies (like subsidies and their amount) encouraging providers to adopt HIEs should be revised. Furthermore, patient switching behavior is an important factor to consider when a social planner develops HIE policies. In markets where patients are less likely to switch providers, the cost of adopting an HIE may outweigh the benefits potentially associated with the HIE.

## Policy Implications and Conclusion

This study fills a crucial gap in our understanding of the interdependency between two major parts of the federal strategy set by the U.S. government to improve the delivery of healthcare services: (1) promoting alternative, valuedriven rather than volume-driven, payment models, and (2) leveraging IT efforts to coordinate care, in particular facilitating information sharing through HIEs (Burwell 2015). Thus, a significant contribution of this study lies in the strong insights it provides to policymakers. We highlight these implications in the following paragraphs.

First, we identify a specific episode-based payment model that offers the right set of incentives to providers to maximize social welfare. The payment to a provider under this proposed model depends not only on the outcome at the end of the episode but also on the sequence of patient visits. Furthermore, the payment adjustment to each provider for good or bad outcomes at the end of an episode is an essential component of this model. We find that the performance-based model, which considers only the individual provider performance (and not the joint performance), while superior to the fee-for-service model, does not offer the right set of incentives. This finding is consistent with the qualitative observation that the unilateral quality measures used in the performance-based model may not promote the adoption of HIEs even when the exchange of information is socially desirable (Frank 2016). Therefore, while the variants of the P4P model are a good start for reforming existing payment systems, the CMS and other policymakers should consider shifting toward multilateral and sequence-dependent EBP mechanisms to achieve their objective of a higher quality of care and lower cost of care.

Second, although not identical, the EBP model that we propose is reminiscent of the alternative payment models currently being evaluated by the CMS (e.g., bundled payments or ACO) and is expected to be widespread in the near future (Press et al. 2016). For example, in a bundledpayment setup, providers receive a lump-sum payment for an episode, and a convener facilitates splitting the payment among the providers caring for the patient. One rationale for the bundled-payment model is that it will induce providers to behave like a single entity, analogous to a social planner. However, our analysis suggests that the bundled-payment model does not guarantee the right set of incentives to providers if sharing of the payment among providers is not addressed. Similarly, it has been reported that, in the context of determining payments to the participating members in an ACO, a common approach used in practice is that providers agree ex ante to share the payment equally (The Advisory Board Company 2013). That is, the sharing rule is contingent on neither the collective outcome nor the sequence. Such a sharing arrangement may not lead to the actions desired by the social planner, as it may not provide the right set of incentives to the providers participating in the ACO. Our analysis indicates that the CMS should manage payments at the individual-provider level for an episode, not only at the aggregate level, as in the current bundled-payment schemes or ACO models being considered.

Third, introducing new payment models is just one part of ongoing healthcare reforms that seek to encourage desirable provider behavior related to reducing costs and improving quality of care. Concurrent with these payment reforms, the U.S. government is also pursuing other strategies, such as promoting HIEs through subsidies. Even though federal incentive money may have prompted an expansion of HIE efforts, a slowdown, and perhaps even active blocking of these efforts, seems to be looming on the horizon (Adler-Milstein et al. 2013; ONC 2015). The primary implication of our results is that the U.S. government should carefully coordinate a two-pronged strategy of reforming payment models and promoting HIE adoption. In fact, if the CMS is successful in increasing the percentage of P4P-based payments and reducing pure FFSbased payments (ONC 2014), then our results suggest that it should also reduce the subsidy level because the HIE value is lower under the P4P model than under the FFS model. On the other hand, if the CMS is successful in changing the prevailing payment model to the EBP model that we have identified, then it should increase the level of subsidy from what it would offer under the P4P model. Furthermore, a uniform strategy of encouraging HIE adoption in all markets regardless of patient incentives to switch providers may not be appropriate.

Finally, our study has implications for further research on the value of HIEs. Because early studies on the assessment of HIEs predated widespread HIE adoption, there has been a lack of solid evidence on the value propositon of HIEs. The widespread adoption of HIEs has created more opportunities for evaluating their value. However, as our review of studies on HIEs suggests, the vast majority of existing studies are constrained to specific settings with disparate outcome measures and, hence, there is a need for new generalizable studies (Rahurkar et al. 2015). We offer two insights for future HIE research and the interpretation of the prior studies: (1) it is critical that future empirical research on the value of HIEs use the payment model as a mediating variable due to the payment model’s impact on HIE value, and (2) past studies on the value of HIEs conducted in an FFS environment should be interpreted with caution because they may have overestimated the actual value for the current environment in which P4P and other outcome-based payment models are becoming increasingly popular.

The insights presented in this paper were derived from a stylized yet rich model of a typical healthcare setting. Particularly, we focus on the interactions between providers in coordinating care (via an HIE) for a patient and the patient’s choice of providers under different payment mechanisms. We analyzed several variants of the model we present in the paper, such as those that incorporate interactions between costs of observable and nonobservable efforts and the correlation between outcomes in first and second visits. We found that the primary result—namely, that the EBP model induces the first-best solution whereas the FFS and P4P models do not—holds under these variations.

Despite these robustness checks, our stylized model has limitations, and extending the model in different directions could provide a richer set of insights. For example, our model could be extended to accommodate more than two providers. Another valuable extension would be to model and examine different variations of bundled payments under consideration by the CMS. Also, the modeling of patients could be enriched. For instance, relaxing the binary health outcome (cured vs. non-cured) to allow for multiple states of cure, allowing more than two visits in an episode, and the timing of patient switching behavior could be analyzed in future research. Finally, we considered a single payer that acts as a social planner. Future research could treat the social planner and insurance companies (payers) as separate entities. The lack of such modeling is not an issue in our setup because, in the U.S. market, a significant portion of healthcare payments are made by the CMS (roughly 60%). Because it is the largest payer, the CMS can unilaterally make decisions on how to pay for care. A valuable extension of this research would be to separately model insurance providers as profit-maximizing entities and examine a social planner’s policies for maximizing social welfare, anticipating insurance company responses. We hope that our study, which is unique in untangling the relationship between payment mechanisms and the value of HIE adoption, will pave the way for further research on these topics.

## References

Adjerid, I., Adler-Milstein, J., and Angst, C. 2018). “Reducing Medicare Spending Through Electronic Health Information Exchange: The Role of Incentives and Exchange Maturity,” Information Systems Research (29:2), pp. 341-361.

Adler-Milstein, J., and Jha, A. K. 2012. “Sharing Clinical Data Electronically: Critical Challenge for Fixing the Health Care System,” JAMA (307:16), 1695-1696.

Adler-Milstein, J., Bates, D. W., and Jha, A. K. 2013. “Operational Health Information Exchanges Show Substantial Growth, But Long-Term Funding Remains a Concern,” Health Affairs (32:8), pp. 1486-1492.

The Advisory Board Company. 2013. “How to Approach Physician Compensation: Three Lessons from Early ACOs” (https://www.advisory.com/research/medical-groupstrategy-council/practice-notes/2013/august/learning-fromearly-acos)

Ahsen, M. E., Ayvaci, M. U., and Raghunathan, S. 2019. “When Algorithmic Predictions Use Human-Generated Data: A Bias-Aware Classification Algorithm for Breast Cancer Diagnosis,” Information Systems Research (30:1), pp. 97- 116.

American Academy of Actuaries. 2012. “An Actuarial Perspective on Accountable Care Organizations”

(http://www.actuary.org/files/ACO\_IB\_UPDATE\_Final\_12 1912.pdf)

Angst, C., Devaraj, S., Queenan, C., and Greenwood, B. 2011. “Performance Effects Related to the Sequence of Integration of Healthcare Technologies,” Production and Operations Management (20:3), pp. 319-333.

Aron, R., Dutta, S., Janakiraman, R., and Pathak, P. 2011. “The Impact of Automation of Systems on Medical Errors: Evidence from Field Research,” Information Systems Research (22:3), pp. 429-446.

Ata, B., Killaly, B. L., Olsen, T. L., and Parker, R. P. 2013. “On Hospice Operations Under Medicare Reimbursement Policies,” Management Science (59:5), pp. 1027-1044.

Ayer, T., Ayvaci, M. U., Karaca, Z., and Vlachy, J. 2019. “The Impact of Health Information Exchanges on Emergency Department Length of Stay,” Production and Operations Management (28:3), pp. 740-758.

Bailey, J. E., Wan, J. Y., Mabry, L. M., Landy, S. H., Pope, R. A., Waters, T. M., and Frisse, M. E. 2013. “Health Information Exchange Reduces Repeated Diagnostic Imaging for Back Pain,” Annals of Emergency Medicine (62:1), pp. 16-24.

Bailit, M., and Hughes, C. 2011. “Key Design Elements of Shared-Savings Payment Arrangements,” Commonwealth Fund, (https://www.commonwealthfund.org/sites/default/ files/documents/\_\_\_media\_files\_publications\_issue\_brief\_2 011\_aug\_1539\_bailit\_key\_design\_elements\_sharedsavings \_ib\_v2.pdf).

Barr, D. A. 2016. Introduction to US Health Policy: The Organization, Financing, and Delivery of Health Care in America, Baltimore: Johns Hopkins University Press.

Berenson, R. A., Paulus, R. A., and Kalman, N. S. 2012. “Medicare’s Readmissions-Reduction Program: A Positive Alternative,” New England Journal of Medicine, (366), pp. 1364-1366.

Bharadwaj, A. S. 2000. “A Resource-Based Perspective on Information Technology Capability and Firm Performance: An Empirical Investigation,” MIS Quarterly (24:1), pp. 169- 196.

Bhargava, H. K., and Mishra, A. N. 2014. “Electronic Medical Records and Physician Productivity: Evidence from Panel Data Analysis,” Management Science (60:10), pp. 2543- 2562.

Bitton, A., Flier, L. A., and Jha, A. K. 2012. “Health Information Technology in the Era of Care Delivery Reform: To What End?,” JAMA (307:24), pp. 2593-2594.

Blumenthal, D., and Tavenner, M. 2010. “The ‘Meaningful Use’ Regulation for Electronic Health Records,” New England Journal of Medicine (363), pp. 501-504.

Brynjolfsson, E., and Hitt, L. 1996. “Paradox Lost? Firm-Level Evidence on the Returns to Information Systems Spending,” Management Science (42:4), pp. 541-558.

Burwell, S. M. 2015. “Setting Value-Based Payment Goals: HHS Efforts to Improve US Health Care,” New England Journal of Medicine (372), pp. 897-899.

Campion, T. R., Edwards, A. M., Johnson, S. B., and Kaushal, R. 2013. “Health Information Exchange System Usage Patterns in Three Communities: Practice Sites, Users,

Patients, and Data,” International Journal of Medical Informatics (82:9), pp. 810-820.

Carey, K. 2015. “Measuring the Hospital Length of Stay/Readmission Cost Trade-Off Under a Bundled Payment Mechanism,” Health Economics (24:7), pp. 790-802.

Cavusoglu, H., Mishra, B., and Raghunathan, S. 2005. “The Value of Intrusion Detection Systems in Information Technology Security Architecture,” Information Systems Research (16:1), pp. 28-46.

Cavusoglu, H., Raghunathan, S., and Cavusoglu, H. 2009. “Configuration of and Interaction Between Information Security Technologies: The Case of Firewalls and Intrusion Detection Systems,” Information Systems Research (20:2), pp. 198-217.

Cezar, A., Cavusoglu, H., and Raghunathan, S. 2013. “Outsourcing Information Security: Contracting Issues and Security Implications,” Management Science (60:3), pp. 638-657.

Chandra, A., Cutler, D., and Song, Z. 2011. “Who Ordered That? The Economics of Treatment Choices in Medical Care,” in Handbook of Health Economics, M. V. Pauly, T. G. Mcguire, and P. P. Barros, Amsterdam: Science Direct, vol. 2, pp. 397-432.

Chen, Y., and Bharadwaj, A. 2009. “An Empirical Analysis of Contract Structures In IT Outsourcing,” Information Systems Research (20:4), pp. 484-506.

Chiasson, M. W., and Davidson, E. 2004. “Pushing the Contextual Envelope: Developing and Diffusing IS Theory for Health Information Systems Research,” Information and Organization (14:3), 155-188.

CMS. 2013. “National Provider Call: Hospital Value-Based Purchasing” (https://www.cms.gov/Medicare/Quality-Initiatives-Patient-Assessment-Instruments/hospital-value-basedpurchasing/Downloads/HVBP-NPC-Transcript-022812.pdf

Cutler, D. M., and Ghosh, K. 2012. “The Potential for Cost Savings Through Bundled Episode Payments,” New England Journal of Medicine (366), pp. 1075-1077.

Cutler, D. M., and Zeckhauser, R. J. 2000. “The Anatomy of Health Insurance,” Handbook of Health Economics, A. J. Culyer, and J. P. Newhouse (eds.), Amsterdam: Science Direct, vol. 1, pp. 563-643.

de Brantes, F., Rosenthal, M. B., and Painter, M. 2009. “Building a Bridge from Fragmentation to Accountability: The Prometheus Payment Model,” New England Journal of Medicine (361), pp. 1033-1036.

Demirezen, E. M., Kumar, S., and Sen, A. 2016. “Sustainability of Healthcare Information Exchanges: A Game-Theoretic Approach,” Information Systems Research (27:2), pp. 240- 258.

Desai, S. 2013. “Health Information Exchange and Market Competition: An Analysis of New York State,” presented at the Workshop on Health Information Technology, College Park Maryland.

Dey, D., Fan, M., and Zhang, C. 2010. “Design and Analysis of Contracts for Software Outsourcing,” Information Systems Research (21:1), pp. 93-114.

Dranove, D., Forman, C., Goldfarb, A., and Greenstein, S. 2014. “The Trillion Dollar Conundrum: Complementarities and

Health Information Technology,” American Economic Journal: Economic Policy (6:4), pp. 239-70.

Ellis, R. P., and McGuire, T. G. 1986. “Provider Behavior Under Prospective Reimbursement: Cost Sharing and Supply,” Journal of Health Economics (5:2), pp. 129-151.

Ellis, R. P., and McGuire, T. G. 1996. “Hospital Response to Prospective Payment: Moral Hazard, Selection, and Practice-Style Effects,” Journal of Health Economics (15:3), pp. 257- 277.

Fichman, R. G., Kohli, R., and Krishnan, R. 2011. “Editorial Overview: The Role of Information Systems in Healthcare: Current Research and Future Trends,” Information Systems Research (22:3), pp. 419-428.

Frank, R. G. 2016. Academic Keynote Address at the Annual Workshop on Health Information Technology and Economics (https://www.youtube.com/watch?v=XXDEsxJwKAg)

Fuloria, P. C., and Zenios, S. A. 2001. “Outcomes-Adjusted Reimbursement in a Health-Care Delivery System,” Management Science (47:6), pp. 735-751.

Furukawa, M. F., Patel, V., Charles, D., Swain, M., and Mostashari, F. 2013. “Hospital Electronic Health Information Exchange Grew Substantially in 2008-12,” Health Affairs (32:8), pp. 1346-54.

Garber, A. M., and Skinner, J. 2008. “Is American Health Care Uniquely Inefficient?,” Journal of Economic Perspectives (22:4), pp. 27-50.

Gibbons, R. 2005. “Incentives Between Firms (and Within),” Management Science (51:1), pp. 2-17.

Goitein, L. 2014. “The Argument Against Reimbursing Physicians for Value,” JAMA (174:6), pp. 845-846.

Grossman, J. M., Bodenheimer, T. S., and McKenzie, K. 2006. “Hospital-Physician Portals: The Role of Competition in Driving Clinical Data Exchange,” Health Affairs (25:6), pp. 1629-1636.

Gupta, D., and Mehrotra, M. 2015. “Bundled Payments or Healthcare Services: Proposer Selection and Information Sharing,” Operations Research (63:4), pp. 772-788.

Hao, L., Guo, H., and Easley, R. F. 2017. “A Mobile Platform’s In-App Advertising Contract Under Agency Pricing for App Sales,” Production and Operations Management (26:2), pp. 189-202.

Harris, K. M. 2003. “How Do Patients Choose Physicians? Evidence from a National Survey of Enrollees in Employment-Related Health Plans,” Health Services Research (38:2), pp. 711-732.

Hillestad, R., Bigelow, J., Bower, A., Girosi, F., Meili, R., Scoville, R., and Taylor, R. 2005. “Can Electronic Medical Record Systems Transform Health Care? Potential Health Benefits, Savings, and Costs,” Health Affairs (24:5), pp. 1103-1117.

Hitt, L. M., and Brynjolfsson, E. 1996. “Productivity, Business Profitability, and Consumer Surplus: Three Different Measures of Information Technology Value,” MIS Quarterly (20:2), 121-142.

Iacovou, C. L., Benbasat, I., and Dexter, A. S. 1995. “Electronic Data Interchange and Small Organizations: Adoption and Impact of Technology,” MIS Quarterly (19:4), 465-485.

Jha, A. K. 2013. “Time to Get Serious About Pay for

Performance,” JAMA (309:4), pp. 347-348.

Jiang, H., Pang, Z., and Savin, S. 2012. “Performance-Based Contracts for Outpatient Medical Services. Manufacturing & Service Operations Management (14:4), pp. 654-669.

Jung, K., Feldman, R., and Scanlon, D. 2011. “Where Would You Go for Your Next Hospitalization? Journal of Health Economics (30:4), 832-841.

Kim, Y., Ayvaci, M. U., Raghunathan, S., and Ayer, T. 2020. “When IT Creates Legal Vulnerability: Not Just Overutilization but Underprovisioning of Health Care Could Be a Consequence” (available at https://papers.ssrn.com/ sol3/papers.cfm?abstract\_id= 3487639).

Kocher, R. P., and Adashi, E. Y. 2011. “Hospital Readmissions and the Affordable Care Act: Paying for Coordinated Quality Care,” JAMA (306:16), pp. 1794-1795.

Koh, B., Raghunathan, S., and Nault, B. R. 2017. “Is Voluntary Profiling Welfare Enhancing? MIS Quarterly (41:1), pp. 23- 41.

Lee, C. H., Geng, X., and Raghunathan, S. 2013. “Contracting Information Security in the Presence of Double Moral Hazard,” Information Systems Research (24:2), pp. 295-311.

Lee, C. H., Geng, X., and Raghunathan, S. 2016. “Mandatory Standards and Organizational Information Security,” Information Systems Research (27:1), pp. 70-86.

Lee, D. K., and Zenios, S. A. 2012. “An Evidence-Based Incentive System for Medicare’s End-Stage Renal Disease Program,” Management Science (58:6), pp. 1092-1105.

Lee, J., McCullough, J., and Town, R. 2013. “The Impact of Health Information Technology on Hospital Productivity,” The RAND Journal of Economics (44:3), pp. 545-568.

Lee, T. H. 2014. “Improving Value Is Improving Health Care, Not Rationing,” JAMA: Internal Medicine (174:6), pp. 847- 848.

Mahajan, A. P. 2016. “Health Information Exchange: Obvious Choice or Pipe Dream?,” JAMA: Internal Medicine (176:4), 429-430.

McCullough, J. S., Parente, S., and Town, R. 2013. “Health Information Technology and Patient Outcomes: The Role of Organizational and Informational Complementarities” NBER Working Paper Series 18684 (https://www.nber.org/system/files/working\_papers/w1868 4/w18684.pdf).

McGuire, T. G. 2000. “Physician Agency,” in Handbook of Health Economics, A. J. Culyer, and J. P. Newhouse (eds.), Amsterdam: Science Direct, vol. 1, pp. 461-536.

Melville, N., Kraemer, K., and Gurbaxani, V. 2004. “Review: Information Technology and Organizational Performance: An Integrative Model of IT Business Value,” MIS Quarterly (28:2), 283-322.

Menon, N., and Lee., B. 2000. “Cost Control and Production Performance Enhancement by IT Investment and Regulation Changes: Evidence from the Healthcare Industry,” Decision Support Systems (30:2), 153-169.

Miller, A., and Tucker, C. 2014. “Health Information Exchange, System Size and Information Silos,” Journal of Health Economics (33), 28-42.

Mithas, S., Tafti, A. R., Bardhan, I., and Goh, J. M. 2012. “Information Technology and Firm Profitability:

Mechanisms and Empirical Evidence,” MIS Quarterly (36:1), 205-224.

Morris, G., Afsal, S., and Finney, D. 2012). Consumer Engagement in Health Information Exchange, Office of the National Coordinator for Health Information Technology (https://www.healthit.gov/sites/default/files/consumer\_medi ated\_exchange.pdf).

Nease Jr., R. F., Kneeland, T., O’Oonnor, G. T., Sumner, W., Lumpkins, C., Shaw, L., . . . Sox, H. C. 1995. “Variation in Patient Utilities for Outcomes of the Management of Chronic Stable Angina: Implications for Clinical Practice Guidelines,” JAMA (273:15), pp. 1185-1190.

Newhouse, J. P. 1996. “Reimbursing Health Plans and Health Providers: Efficiency in Production Versus Selection,” Journal of Economic Literature (34:3), pp. 1236-1263.

O’Malley, A. S. 2011. “Tapping the Unmet Potential of Health Information Technology,” New England Journal of Medicine (364), pp. 1090-1091.

ONC. 2014. “Report To Congress: Update on the Adoption of Health Information Technology and Related Efforts to Facilitate the Electronic Use and Exchange of Health Information,” The Office of the National Coordinator for Health Information Technology (https://www.healthit. gov/sites/default/files/rtc\_adoption\_and\_exchange9302014. pdf)

ONC. 2015. “Report To Congress: Report on Health Information Blocking,” The Office of the National Coordinator for Health Information Technology (https://www.healthit.gov/ sites/default/files/reports/info\_blocking\_040915.pdf).

Ozdemir, Z., Barron, J., and Bandyopadhyay, S. 2011. “An Analysis of the Adoption Of Digital Health Records Under Switching Costs,” Information Systems Research (22:3), 491-503.

Powell, A., Savin, S., and Savva, N. 2012. “Physician Workload and Hospital Reimbursement: Overworked Physicians Generate Less Revenue Per Patient,” Manufacturing & Service Operations Management (14:4), 512-528.

Premkumar, G., Ramamurthy, K., and Crum, M. 1997. “Determinants of EDI Adoption in the Transportation Industry,” European Journal of Information Systems (6:2), pp. 107-121.

Press, M. J., Rajkumar, R., and Conway, P. H. 2016. “Medicare’s New Bundled Payments: Design, Strategy, and Evolution,” JAMA (315:2), pp. 131-132.

Rahurkar, S., Vest, J. R., and Menachemi, N. 2015. “Despite The Spread of Health Information Exchange, There Is Little Evidence of its Impact on Cost, Use, and Quality of Care,” Health Affairs (34:3), 477-483.

Rau, J. 2013. “Methodology: How Value Based Purchasing Payments Are Calculated,” KHN (https://khn.org/news/ value-based-purchasing-medicare-methodology/).

Romanow, D., Cho, S., and Straub, D. 2012. “Editor’s Comments: Riding the Wave: Past Trends and Future Directions for Health IT Research,” MIS Quarterly (36:3), pp. iii-x.

Rosenthal, M. B. 2008. “Beyond Pay for Performance-Emerging Models of Provider-Payment Reform,” New England Journal of Medicine (359), pp. 1197-1200.

Rosenthal, M. B., and Dudley, R. A. 2007. “Pay-for-Performance: Will the Latest Payment Trend Improve Care?,” JAMA (297:7), 740-744.

Rowe, B. R. 2007. “Will Outsourcing IT security Lead to a Higher Social Level of Security?,” in Proceedings of the Sixth Workshop on the Economics of Information Security, Pittsburgh, PA.

Sassi, F. 2006. “Calculating QALYs, Comparing QALY and DALY Calculations,” Health Policy and Planning (21:5), 402-408.

Shah, Y. 2015. “U.S. Ranks Near Bottom Among Advanced Nations In Efficiency Of Health Care Spending, HuffPost, (https://www.huffpost.com/entry/us-health-careefficiency\_n\_4430101).

Shapiro, J. S., Crowley, D., Hoxhaj, S., Langabeer, J., Panik, B., Taylor, T. B., . . . Nielson, J. A. 2016. “Health Information Exchange in Emergency Medicine,” Annals of Emergency Medicine (67:2), 216-226.

Varian, H. 2004. “System Reliability and Free Riding,” In Economics of Information Security, L. J. Camp and S. Lewis (eds.), New York: Springer, pp. 1-15.

Vest, J. R., and Gamm, L. D. 2010. “Health Information Exchange: Persistent Challenges and New Strategies,” Journal of the American Medical Informatics Association (17:3), pp. 288-294.

Vlachy, J., Ayer, T., Ayvaci, M. U., and Raghunathan, S. 2020. “The Business of Healthcare: The Role of Physician Integration in Bundled Payments” (available at https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=35395 96).

Williams, C., Mostashari, F., Mertz, K., Hogin, E., and Atwal, P. 2012. “From the Office of the National Coordinator: The Strategy for Advancing the Exchange of Health Information,” Health Affairs (31:3), 527-536.

Wu, D. J., Ding, M., and Hitt, L. M. 2012. “IT Implementation Contract Design: Analytical and Experimental Investigation of IT Value, Learning, and Contract Structure,” Information Systems Research (24:3), pp. 787-801.

Yaraghi, N. 2015. “A Sustainable Business Model for Health Information Exchange Platforms: The Solution to Interoperability in Healthcare IT,” The Brookings Institution (https://www.brookings.edu/wp-content/uploads/2016/06/ HIE.pdf).

Yaraghi, N., Du, A. Y., Sharman, R., Gopal, R. D., and Ramesh, R. 2013. “Network Effects in Health Information Exchange Growth,” ACM Transactions on Management Information Systems (4), Article 1.

Yaraghi, N., Du, A. Y., Sharman, R., Gopal, R., and Ramesh, R. 2015. “Health Information Exchange as a Multisided Platform: Adoption, Usage and Practice Involvement in Service Co-Production,” Information Systems Research (26:1), 1-18.

Zablah, A. R., Bellenger, D. N., Straub, D. W., and Johnston, W. J. 2012. “Performance Implications of CRM Technology Use: A Multilevel Field Study of Business Customers and Their Providers in the Telecommunications Industry,” Information Systems Research (23:2), pp. 418-435.

Zeckhauser, R. 1970. “Medical Insurance: A Case Study of the

Tradeoff Between Risk Spreading and Appropriate Incentives,” Journal of Economic Theory (2:1), 10-26.

Zheng, K., Haftel, H. M., Hirschl, R. B., O'Reilly, M., and Hanauer, D. A. 2010. “Quantifying the Impact Of Health IT Implementations on Clinical Workflow: A New Methodological Perspective,” Journal of the American Medical Informatics Association (17:4), pp. 454-461.

Zhu, K., Kraemer, K., and Xu, S. 2003. “Electronic Business Adoption by European Firms: A Cross-Country Assessment of the Facilitators And Inhibitors,” European Journal of Information Systems (12), pp. 251-268.

## About the Authors

Mehmet Ayvaci is an associate professor of information systems in the Jindal School of Management at the University of Texas Dallas. Dr. Ayvaci broadly studies how to better utilize the available information and resources in support of operations and develop policies to address inefficiencies in healthcare. For his research, Dr. Ayvaci uses stochastic modeling, optimization, game theory, econometric methods, and machine learning. Dr. Ayvaci’s research is highly interdisciplinary; therefore, he collaborates with scholars from various fields and publish in premier journals both in management sciences and other disciplines such as medicine and informatics. His research efforts have been recognized for excellence by various academic societies including the Decision Analysis Society of INFORMS, Information Systems Society of INFORMS, eBusiness Section of INFORMS, and CHITA (Conference of Health IT and Analytics). His works have received publicity through a variety of channels including coverage in media, news stories in practitioner magazines, and editorials of academic journals. Dr. Ayvaci serves as an associate editor at Healthcare Management Science Journal and INFORMS Journal on Data Science. Dr. Ayvaci received his B.S. degree from Texas A&M University, his M.S. degree from Stanford University, and Ph.D. degree from the University of Wisconsin Madison.

Huseyin Cavusoglu is a professor of information systems in the Naveen Jindal School of Management at University of Texas at Dallas. His research lies at the intersection of economics and information systems. He is interested in exploring the economic implications of emerging information technologies and technology artifacts. His research studies have been published in various academic journals including Management Science, Operations Research, Information Systems Research, Production and Operations Management, INFORMS Journal on Computing, IEEE Transactions on Software Engineering, INFORMS Decision Analysis, Communications of the ACM, Journal of Management Information Systems, IEEE Transactions on Engineering Management, and International Journal of Electronic Commerce, among others. He has received several Best Paper awards and nominations at prestigious IS conferences, including the International Conference on Information Systems (ICIS) and the Workshop on Information Technology and Systems (WITS). Dr. Cavusoglu is also a recipient of the NYU Net Institute Grant in 2007. He serves on the steering committee of the Workshop on the Economics of Information Security. He has served as an associate editor for MIS Quarterly and Information Systems Research for a number of special issues. He also organized the Workshop on Information Systems and Economics (WISE) in 2015, the European Conference on Information Systems (ECIS) (Workshops and Tutorials) in 2016, and the Theory on Economics of Information Systems (TEIS) in 2019.

Yeongin Kim is an assistant professor of information systems in the School of Business at Virginia Commonwealth University (VCU). He received his M.S. from Texas A&M University and his Ph.D from the University at Texas at Dallas. His research is mainly focused on the economics of information technology (IT) in various contexts. In particular, his works examine the value of information sharing under decision conflicts, the vulnerabilities created by IT, and the implementation of artificial intelligence (AI)-enabled decision-making to improve operational efficiency. In studying these topics, he uses game theory, econometric methods, optimization, and statistics. His works have appeared in the proceedings of major IS conferences.

Srinivasan Raghunathan is the Ashbel Smith Professor of Information Systems in the Naveen Jindal School of Management at the University of Texas at Dallas. His research interests lie in the understanding of the economic implications of information technologies. His papers have been published in journals such as Management Science, Operations Research, Information Systems Research, MIS Quarterly, Decision Analysis, Journal of Management Information Systems, Decision Support Systems, as well as various IEEE transactions and IIE transactions, European Journal of Operational Research, and Production and Operations Management, among others. He has served on the editorial boards of Information Systems Research, Information Technology and Management, and Journal of Electronic Commerce Research.

## Appendix A

## Proofs for the Results

We assume the following on ?? throughout our analysis:

$$
\alpha <   m i n [ \frac {u _ {L} - \mu}{\delta}, \overline {{\alpha}} ],
$$

where

(11)

$$
\begin{array} { r l } & { \overline { { \alpha } } : = - ( U ^ { 4 } ( - 8 \delta + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) + U ^ { 3 } ( - 4 \delta ^ { 2 } ( 4 \epsilon - 7 ) + u _ { L } ^ { 2 } \tilde { \epsilon } } \\ & { + 8 \delta ( 4 \mu + 3 u _ { H } \epsilon - 4 \mu \epsilon ) - 2 u _ { L } \tilde { \epsilon } ( 4 \delta + 2 \mu + u _ { H } \epsilon - \mu \epsilon ) - \mu \tilde { \epsilon } ( - 3 \mu - 2 u _ { H } \epsilon + 2 \mu \epsilon ) ) } \\ & { 4 \delta ^ { 2 } ( u _ { H } ^ { 3 } \epsilon ^ { 2 } + u _ { H } ^ { 2 } \epsilon ( \delta ( - 2 \epsilon ^ { 2 } + 2 \epsilon + 2 ) + \mu ( - 2 \epsilon ^ { 2 } + \epsilon + 1 ) ) - \mu u _ { H } \tilde { \epsilon } \epsilon ( 4 \delta ( \epsilon - 2 ) - 3 \mu \tilde { \epsilon } ) } \\ & { \mu + \tilde { \epsilon } ^ { 2 } ( 8 \delta ^ { 2 } - 2 \delta \mu ( \epsilon - 2 ) + \mu ^ { 2 } \tilde { \epsilon } ) ) + U ^ { 2 } ( 8 \delta ^ { 3 } ( 7 \epsilon - 6 ) - 2 u _ { L } ^ { 2 } \tilde { \epsilon } ( 2 \delta + \mu + u _ { H } \epsilon - \mu \epsilon ) } \\ & { - \mu \tilde { \epsilon } ( u _ { H } ^ { 2 } \epsilon ^ { 2 } - 2 \mu u _ { H } ( \epsilon - 2 ) \epsilon + \mu ^ { 2 } ( \epsilon ^ { 2 } - 4 \epsilon + 3 ) ) + 4 \delta ^ { 2 } ( u _ { H } \epsilon ( 8 \epsilon - 1 3 ) - 8 \mu ( \tilde { \epsilon } ^ { 2 } + 1 ) ) } \\ & { - 4 \delta ( 2 u _ { H } ^ { 2 } \epsilon ( 2 \epsilon + 1 ) + 1 3 \mu u _ { H } \tilde { \epsilon } \epsilon + \mu ^ { 2 } ( 9 \epsilon ^ { 2 } - 1 9 \epsilon + 1 0 ) ) + u _ { L } \tilde { \epsilon } } \\ & { ( 1 2 \delta ^ { 2 } + u _ { H } ^ { 2 } \epsilon ^ { 2 } + 4 \delta ( u _ { H } \epsilon + \mu ( 5 - 3 \epsilon ) ) - 2 \mu u _ { H } ( \epsilon - 3 ) \epsilon + \mu ^ { 2 } ( \epsilon ^ { 2 } - 6 \epsilon + 5 ) ) } \\ & { + U ( - 3 2 \delta ^ { 4 } \tilde { \epsilon } + 1 6 \delta ^ { 3 } ( u _ { H } ( \epsilon - 2 ) \epsilon + \mu ( 3 \epsilon ^ { 2 } - 4 \epsilon + 1 ) ) + \mu ^ { 2 } \tilde { \epsilon } ( \mu + u _ { H } \epsilon - \mu \epsilon ) ^ { 2 } } \\ & { - 4 \delta ^ { 2 } ( u _ { H } ^ { 2 } \epsilon ( 4 \epsilon ^ { 2 } - 2 \epsilon - 3 ) - 2 \mu u _ { H } \epsilon ( 4 \epsilon ^ { 2 } - 7 \epsilon + 3 ) + \mu ^ { 2 } ( 4 \epsilon ^ { 3 } - 1 7 \epsilon ^ { 2 } + 2 1 \epsilon - 8 ) ) } \\ & { + 4 \delta ( 2 u _ { H } ^ { 3 } \epsilon ^ { 2 } + \mu u _ { H } ^ { 2 } \epsilon ( - 5 \epsilon ^ { 2 } + 3 \epsilon + 2 ) + \mu ^ { 2 } u _ { H } \epsilon ( 8 \epsilon ^ { 2 } - 1 5 \epsilon + 7 ) - \mu ^ { 3 } \tilde { \epsilon } ^ { 2 } ( 3 \epsilon - 4 ) ) } \\ & { + u _ { L } ^ { 2 } \tilde { \epsilon } - 4 \delta ^ { 2 } - 4 \delta ( u _ { H } \epsilon - \mu \tilde { \epsilon } ) + ( \mu \tilde { \epsilon } + u _ { H } \epsilon ) ^ { 2 } } \\ &  - 2 u _ { L } \tilde { \epsilon } ( 2 \delta + \mu ) ( - 4 \delta ^ { 2 } - 4 \delta ( u _ { H } \epsilon - \mu \tilde { \epsilon } ) + ( \mu \tilde { \epsilon } + u _ { H } \epsilon ) ^ { 2 } ) ) ) \\ & { / ( \delta ^ { 2 } \tilde { \epsilon } ( \delta + 2 U ) ( \mu \tilde { \epsilon } ( \mu \tilde { \epsilon } + 4 \delta ) + U ^ { 2 } - 2 U ( 2 \delta + \mu \tilde { \epsilon } + u _ { H } \epsilon ) + u _ { H } ^ { 2 } \epsilon ^ { 2 } + 2 \mu u _ { H } \tilde { \epsilon } ) ) . } \\ & . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\tag{12}
$$

This assumption ensures that the impact of HIE on social welfare due to prior episodes $( \mathrm { i } . \mathrm { e } . , \alpha )$ is sufficiently low such that the patients switching behavior is solely determined by the value generated from information sharing across different providers.

## Proof of Lemma 1

Given the patient switching behavior indicated by quadruple $( k _ { H } , l _ { H } , k _ { L } , l _ { L } )$ and HIE adoption status $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ , the social planner’s problem is formulated as follows.

$$
\begin{array}{l} \max _ {e _ {i 0}, \hat {e} _ {i 0}, e _ {i i}, \hat {e} _ {i i}, \forall i \in \{A, B \} e _ {k _ {y} A}, \hat {e} _ {k _ {y} A}, \forall k _ {y} \neq A, y \in \{H, L \} e _ {l _ {y} B}, \hat {e} _ {l _ {y} B}, \forall l \neq B, y \in \{H, L \}} \\ \text {Expected per patient social payoff when initial visit occurs at A and patient type is high} \\ \overbrace {\theta \epsilon [ \overbrace {- \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2}} + (1 - \beta_ {A 0} ^ {p}) ]} ^ {\text {Cost of initial visit to A}} \\ = \text {Expected per patient social payoff when initial visit occurs at A and patient type is low} \\ + \overbrace {\theta \tilde {\epsilon} [ - \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2} + (1 - \beta_ {A 0} ^ {p}) (- \delta e _ {k _ {L} A} ^ {2} - \delta \hat {e} _ {k _ {L} A} ^ {2} - d _ {k _ {L} A L} (1 - \beta_ {k _ {L} A} ^ {p})) ]} ^ {\text {Second visit probability}} \\ + \overbrace {(1 - \theta) \epsilon [ - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2} + (1 - \beta_ {B 0} ^ {p}) (- \delta e _ {l _ {H} B} ^ {2} - \delta \hat {e} _ {l _ {H} B} ^ {2} - d _ {l _ {H} B H} (1 - \beta_ {l _ {H} B} ^ {p})) ]} ^ {\text {Cost of second visit to k}} \\ + \overbrace {(1 - \theta) \tilde {\epsilon} [ - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2} + (1 - \beta_ {B 0} ^ {p}) (- \delta e _ {l _ {L} B} ^ {2} - \delta \hat {e} _ {l _ {L} B} ^ {2} - d _ {l _ {L} B L} (1 - \beta_ {l _ {L} B} ^ {p})) ]} ^ {\text {Expected per patient social payoff when initial visit occurs at B and patient type is high}} \\ - \overbrace {\theta (\mathbf {1} _ {S _ {\mathrm{A}}} C _ {\mathrm{HIE}}) - (1 - \theta) (\mathbf {1} _ {S _ {\mathrm{B}}} C _ {\mathrm{HIE}})} ^ {\text {Expected per patient social payoff when initial visit occurs at B and patient type is low}} \\ s. t. \\ V _ {k _ {y} A y} ^ {\mathbf {P}} \geq V _ {\bar {k} _ {y} A y} ^ {\mathbf {P}}, f o r k _ {y} \in \{A, B \}, y \in \{H, L \}, \\ V _ {l _ {y} B y} ^ {\mathbf {P}} \geq V _ {\bar {l} _ {y} B y} ^ {\mathbf {P}}, f o r l _ {y} \in \{A, B \}, y \in \{H, L \}, \end{array}\tag{13}
$$

where $\bar { k } _ { y } = A \operatorname { i f } k _ { y } = B$ and B otherwise and $\bar { l } _ { y } = A \mathrm { i f } l _ { Y } = B$ and B otherwise. Given a HIE adoption scenario $( S _ { A } , S _ { B } )$ and a possible patient switching scenario $( k _ { H } , l _ { H } , k _ { L } , l _ { L } )$ , we solve the simultaneous equations given by

$$
\frac {\partial \Pi^ {k _ {H} l _ {H} k _ {L} l _ {L}} (S _ {A} , S _ {B})}{\partial e _ {i j}} \bigg | _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (S _ {A}, S _ {B}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (S _ {A}, S _ {B}) \end{array} } = 0, \forall i \times j \in \{A, B \} \times \{0, A, B \},\tag{14}
$$

$$
\frac {\partial \Pi^ {k _ {H} l _ {H} k _ {L} l _ {L}} (S _ {A} , S _ {B})}{\partial \hat {e} _ {i j}} \bigg | _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (S _ {A}, S _ {B}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (S _ {A}, S _ {B}) \end{array} } = 0, \forall i \times j \in \{A, B \} \times \{0, A, B \},\tag{15}
$$

which gives the following optimal effort levels for the second visit:

$$
\begin{array}{r} e _ {i i} ^ {*} = \hat {e} _ {i i} ^ {*} = \frac {u _ {L}}{2 \delta}, \mathrm{if} k _ {H} \neq k _ {L}, l _ {H} \neq l _ {L} \mathrm{and} k _ {H} = B, l _ {H} = A, \\ e _ {i i} ^ {*} = \hat {e} _ {i i} ^ {*} = \frac {u _ {H}}{2 \delta}, \mathrm{if} k _ {H} \neq k _ {L}, l _ {H} \neq l _ {L} \mathrm{and} k _ {H} = A, l _ {H} = B. \end{array}\tag{16}
$$

Now, suppose to the contrary that a low type patient does not switch when a high type patient switches in the equilibrium. Then, the following IC constraints should hold:

$$
\begin{array}{l} V _ {(- j) j L} ^ {\mathbf {P}} \leq V _ {j j L} ^ {\mathbf {P}}, \text {for} j \in \{A, B \}, \\ V _ {(- j) j H} ^ {\mathbf {P}} > V _ {j j H} ^ {\mathbf {P}}, \text {for} j \in \{A, B \}. \end{array}\tag{17}
$$

Let us use $s _ { y }$ to denote switching behavior of a patient with type ?? where $s _ { y } = S$ if the patient with type ?? switches and $s _ { y } = N$ otherwise. Then, the conditions in (17) imply

$$
\begin{array}{r l} & {\frac {\mu}{u _ {L}} \leq \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {S N *} + \hat {e} _ {i i} ^ {S N *} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \},} \\ & {\frac {\mu}{u _ {H}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {N S *} + \hat {e} _ {i i} ^ {N S *} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \},} \end{array}\tag{18}
$$

where $e _ { i j } ^ { s _ { H } s _ { L ^ { * } } } \forall i , j \in \{ A , B \}$ is the optimal effort level for the second visit given the switching scenario indicated by pair $( s _ { H } , s _ { L } )$ and

$$
e ^ {\mathbf {P}} = \left\{ \begin{array}{c c} e _ {i 0} ^ {*} + \alpha , & \text { if } (S _ {A}, S _ {B}) = (\mathrm{H}, \mathrm{H}), \\ 0, & \text { otherwise }. \end{array} \right.\tag{19}
$$

By substituting the optimal effort levels we derived from (16) in (18), we have

$$
\begin{array}{r l} & {\frac {\mu}{u _ {L}} \leq \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {L}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \},} \\ & {\frac {\mu}{u _ {H}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {H}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \}.} \end{array}\tag{20}
$$

Observe that

$$
\frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {L}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}} <   \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {H}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \}.\tag{21}
$$

However, this is a contradiction because $\frac { \mu } { u _ { L } } > \frac { \mu } { u _ { H } }$

Now, we show that the if a low-type patient switches the provider for her second visit, then it is not necessary that the high-type patient also switches the provider for her second visit. Suppose to the contrary that a high type patient necessarily switches when a low type patient switches in the equilibrium. Then, the following IC constraints should hold in the equilibrium:

$$
\begin{array}{r} V _ {(- j) j L} ^ {\mathbf {P}} > V _ {j j L} ^ {\mathbf {P}}, \mathrm{for} j \in \{A, B \}, \\ V _ {(- j) j H} ^ {\mathbf {P}} > V _ {j j H} ^ {\mathbf {P}}, \mathrm{for} j \in \{A, B \}, \end{array}\tag{22}
$$

which implies

$$
\begin{array}{r l} & {\frac {\mu}{u _ {L}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {S N *} + \hat {e} _ {i i} ^ {S N *} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, j \in \{A, B \},} \\ & {\frac {\mu}{u _ {H}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {N S *} + \hat {e} _ {i i} ^ {N S *} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, j \in \{A, B \},} \end{array}\tag{23}
$$

where $e _ { i j } ^ { s _ { H } s _ { L ^ { * } } } \forall i , j \in \{ A , B \}$ is the optimal effort level for the second visit given the switching scenario indicated by pair $( s _ { H } , s _ { L } )$ and

$$
e ^ {\mathbf {P}} = \left\{ \begin{array}{c c} e _ {i 0} ^ {*} + \alpha , & \text { if } (S _ {A}, S _ {B}) = (\mathrm{H}, \mathrm{H}), \\ 0, & \text { otherwise }. \end{array} \right.\tag{24}
$$

By substituting the optimal effort levels we derived from (16) in (23), we have

$$
\begin{array}{r} \frac {\mu}{u _ {L}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {L}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \}, \\ \frac {\mu}{u _ {H}} > \frac {e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {H}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}{1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}}, i \in \{A, B \}, \end{array}\tag{25}
$$

which can be reduced to

$$
\begin{array}{r} \mu (1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}) > (e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {L}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}) u _ {L}, i \in \{A, B \}, \\ \mu (1 - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}) > (e _ {i 0} ^ {*} + \hat {e} _ {i 0} ^ {*} + \frac {u _ {H}}{\delta} - e _ {(- i) i} ^ {S S *} - \hat {e} _ {(- i) i} ^ {S S *} - e ^ {\mathbf {P}}) u _ {H}, i \in \{A, B \}. \end{array}\tag{26}
$$

However, the above conditions do not necessarily hold since $\begin{array} { r } { ( e _ { i 0 } ^ { * } + \hat { e } _ { i 0 } ^ { * } + \frac { u _ { L } } { \delta } - e _ { ( - i ) i } ^ { S S * } - \hat { e } _ { ( - i ) i } ^ { S S * } - e ^ { \mathbf { P } } ) < ( e _ { i 0 } ^ { * } + \hat { e } _ { i 0 } ^ { * } + \frac { u _ { H } } { \delta } - e _ { ( - i ) i } ^ { S S * } - } \end{array}$ $\hat { \pmb { e } } _ { ( - i ) i } ^ { S S * } - { \pmb { e } } ^ { \pmb { \operatorname { P } } } )$ and ${ \pmb u } _ { L } < { \pmb u } _ { H }$ , which contradicts the assumption.

## Proof of Lemma 2

Optimal effort levels: The optimal effort levels for different HIE adoption and patient switching scenarios are obtained by solving the following simultaneous equations.

$$
\begin{array}{r}\frac{\partial\Pi^{kl}(S_{A},S_{B})}{\partial e_{ij}}\bigg|_{\substack{e_{ij} = e_{ij}^{*}(S_{A},S_{B}),\\ \hat{e}_{ij} = \hat{e}_{ij}^{*}(S_{A},S_{B})}} = 0, \forall i\times j\in \{A,B\} \times \{0,A,B\} ,\\ \frac{\partial\Pi^{kl}(S_{A},S_{B})}{\partial\hat{e}_{ij}}\bigg|_{\substack{e_{ij} = e_{ij}^{*}(S_{A},S_{B}),\\ \hat{e}_{ij} = \hat{e}_{ij}^{*}(S_{A},S_{B})}} = 0, \forall i\times j\in \{A,B\} \times \{0,A,B\} . \end{array}\tag{27}
$$

(28)

The optimal social payoffs corresponding to the solutions under no HIE adoption and switching behavior of the low type patient, $( S _ { \mathrm { A } } , \bar { S _ { \mathrm { B } } } ) \in \{ ( \mathrm { N } , \mathrm { N } ) \}$ and $( k , l ) \in \{ ( \mathrm { A } , \mathrm { B } ) , ( \mathrm { B } , \mathrm { A } ) \}$ , are as follows:

$$
\begin{array}{r l} & {\left. \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N})} = \frac {U (- 8 \delta^ {3} + U ^ {3} + 4 \delta^ {2} U)}{8 \delta^ {2} (\delta + 2 U)},} \\ & {\left. \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N})} = \frac {u _ {L} ^ {4} (\epsilon - 1) ^ {2}}{8 \delta^ {2} (\delta + 2 u _ {H} \epsilon)} - \frac {u _ {L} ^ {3} (\epsilon - 1) ^ {2} (\delta + \mu)}{2 \delta^ {2} (\delta + 2 u _ {H} \epsilon)}} \\ & {+ \frac {u _ {L} (\epsilon - 1) (\delta + \mu) (2 \delta^ {2} - 2 \delta \mu (\epsilon - 1) + u _ {H} ^ {2} \epsilon - \mu^ {2} (\epsilon - 1))}{2 \delta^ {2} (\delta + 2 u _ {H} \epsilon)}} \\ & {+ \frac {u _ {L} ^ {2} (\epsilon - 1) (2 \delta^ {2} (\epsilon - 2) + 6 \delta \mu (\epsilon - 1) + u _ {H} ^ {2} (- \epsilon) + 3 \mu^ {2} (\epsilon - 1))}{4 \delta^ {2} (\delta + 2 u _ {H} \epsilon)}} \\ & {+ \frac {u _ {H} ^ {4} \epsilon^ {2} + 2 u _ {H} ^ {2} \epsilon (2 \delta^ {2} - 2 \delta \mu (\epsilon - 1) - \mu^ {2} (\epsilon - 1)) - 8 \delta^ {3} u _ {H} \epsilon}{8 \delta^ {2} (\delta + 2 u _ {H} \epsilon)}} \\ & {+ \frac {\mu (\epsilon - 1) (2 \delta + \mu) (- 4 \delta^ {2} + 2 \delta \mu (\epsilon - 1) + \mu^ {2} (\epsilon - 1))}{8 \delta^ {2} (\delta + 2 u _ {H} \epsilon)}.} \end{array}\tag{29}
$$

(30)

Applying envelope theorem, we verify that

$$
\frac {\partial \Pi^ {\mathbf {A B}} (\mathrm{N,N}) \big | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N})}}{\partial \mu} = 0, \frac {\partial \Pi^ {\mathbf {B A}} (\mathrm{N,N}) \big | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N})}}{\partial \mu} > 0.\tag{31}
$$

We define $\mu _ {  { \mathrm { N N } } }$ such that

$$
\left. \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N}), \mu = \mu_ {\mathrm{NN}}} = \left. \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N}), \mu = \mu_ {\mathrm{NN}}}\tag{32}
$$

holds. We ensure that the policy maker is indifferent between the two patient switching scenarios when $\mu = \mu _ { \mathrm { N N } }$ . Therefore, as we observe from (31), the policy maker prefers the patient to switch if $\mu > \mu _ { \mathrm { N N } }$

The optimal social payoffs corresponding to the solutions under HIE adoption and switching behavior of the low type patient, $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) \in$ {(H, H)} and $( k , l ) \overset { \cdot } { \in } \{ ( \mathrm { A } , \mathrm { B } ) , ( \mathrm { B } , \overset { \cdot } { \mathrm { A } } ) \}$ , are as follows:

$$
\begin{array}{r l} & {\left. \Pi^ {\mathrm{AB}} (\mathrm{H}, \mathrm{H}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H})} = \frac {U (- 8 (\alpha - 1) ^ {2} \delta^ {3} + U ^ {3} - 4 (\alpha - 1) \delta^ {2} U)}{8 \delta^ {2} (\delta + 2 U)} - C _ {\mathrm{HIE}},} \\ & {\left. \Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H})} = \frac {u _ {H} ^ {4} \epsilon^ {2}}{\psi} - \frac {8 (\alpha - 1) ^ {2} \delta^ {3} u _ {H} \epsilon}{\psi} + \frac {u _ {L} ^ {4} (\epsilon - 1) ^ {2}}{\psi}} \\ & {+ \frac {2 u _ {L} ^ {3} (\epsilon - 1) ^ {2} ((\alpha - 1) \delta - 2 \mu)}{\psi} + \frac {2 u _ {H} ^ {2} \epsilon (- 2 (\alpha - 1) \delta^ {2} + (\alpha - 1) \delta \mu (\epsilon - 1) - \mu^ {2} (\epsilon - 1))}{\psi}.} \\ & {+ \frac {\mu (\epsilon - 1) (- 8 (\alpha - 1) ^ {2} \delta^ {3} + 2 (\alpha - 1) \delta^ {2} \mu (\alpha (\epsilon - 1) - \epsilon + 3) - 2 (\alpha - 1) \delta \mu^ {2} (\epsilon - 1) + \mu^ {3} (\epsilon - 1))}{\psi}} \\ & {+ \frac {u _ {L} ^ {2} (- (2 u _ {H} ^ {2} (\epsilon - 1) \epsilon))}{\psi} + \frac {u _ {L} (u _ {H} ^ {2} (2 (1 - \alpha) \delta (\epsilon - 1) \epsilon + 4 \mu (\epsilon - 1) \epsilon))}{\psi}} \\ & {+ \frac {u _ {L} ^ {2} (2 (\alpha - 1) \delta^ {2} (\epsilon - 1) (\alpha (\epsilon - 1) - \epsilon + 3) - 6 (\alpha - 1) \delta \mu (\epsilon - 1) ^ {2} + 6 \mu^ {2} (\epsilon - 1) ^ {2})}{\psi}} \\ & {+ \frac {u _ {L} (8 (\alpha - 1) ^ {2} \delta^ {3} (\epsilon - 1) - 4 (\alpha - 1) \delta^ {2} \mu (\epsilon - 1) (\alpha (\epsilon - 1) - \epsilon + 3))}{\psi}} \\ & {+ \frac {u _ {L} (- 6 (1 - \alpha) \delta \mu^ {2} (\epsilon - 1) ^ {2} - 4 \mu^ {3} (\epsilon - 1) ^ {2})}{\psi} - C _ {\mathrm{HIE}},} \end{array}\tag{33}
$$

(34)

$$
\begin{array}{r l} & {\mathrm{where} \psi := 2 \delta (4 \delta^ {2} - 4 \delta \mu \tilde {\epsilon} + 8 \delta u _ {H} \epsilon - u _ {L} ^ {2} \tilde {\epsilon} ^ {2} + 2 u _ {L} \tilde {\epsilon} (\mu \tilde {\epsilon} + 2 \delta) + \mu^ {2} \tilde {\epsilon} ^ {2}). \mathrm{Applyingenvelopetheorem,weverifythat}} \\ & {\qquad \frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{H,H}) \big | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H,H})}}{\partial \mu} = 0, \frac {\partial \Pi^ {\mathrm{BA}} (\mathrm{H,H}) \big | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H,H})}}{\partial \mu} > 0.} \end{array}\tag{35}
$$

We define $\mu _ { \mathrm { H H } }$ such that

$$
\left. \Pi^ {\mathrm{AB}} (\mathrm{H}, \mathrm{H}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H}), \mu = \mu_ {\mathrm{HH}}} = \left. \Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) \right| _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H}), \mu = \mu_ {\mathrm{HH}}}\tag{36}
$$

holds. We ensure that the policy maker is indifferent between the two patient switching scenarios when $\mu = \mu _ { \mathrm { H H } }$ . Therefore, as we observe from (35), the policy maker prefers the patient to switch if $\mu > \mu _ { \mathrm { H H } }$

HIE adoption decision: We first show that $\mu _ { H H } < \mu _ { N N }$ . Let $\Pi ^ { k l } ( S _ { \mathrm { \tiny A } } , S _ { \mathrm { \tiny B } } ) ^ { \ast }$ be the maximized social payoff given the HIE adoption $( S _ { \mathrm { A } } , S _ { \mathrm { B } } )$ and patient switching scenario $( k , l ) \in \{ ( \mathrm { A } , \mathrm { B } ) , ( \mathrm { B } , \mathrm { A } ) \}$ . Let us first assume that $\alpha = 0$ . Then, we have

$$
\Pi^ {\mathrm{AB}} (\mathrm{H}, \mathrm{H}) ^ {*} + C _ {\mathrm{HIE}} = \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) ^ {*} = \frac {U (- 8 \delta^ {3} + U ^ {3} + 4 \delta^ {2} U)}{8 \delta^ {2} (\delta + 2 U)}.\tag{37}
$$

We verify that

$$
\Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) ^ {*} + C _ {\mathrm{HIE}} > \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) ^ {*}\tag{38}
$$

since the following inequality holds for any given efforts $e _ { i j } \forall i \times j \in \{ A , B \} \times \{ 0 , A , B \}$

$$
\begin{array}{r l} & {\Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) + C _ {\mathrm{HIE}} = \theta \epsilon ((1 - \beta_ {A 0} ^ {1}) (- u _ {H} (1 - \beta_ {A A} ^ {1}) - \delta e _ {A A} ^ {2} - \delta \hat {e} _ {A A} ^ {2}) - \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2})} \\ & {+ \theta \tilde {\epsilon} ((1 - \beta_ {A 0} ^ {1}) (- (u _ {L} - \mu) (1 - \beta_ {B A} ^ {1}) - \delta e _ {B A} ^ {2} - \delta \hat {e} _ {B A} ^ {2}) - \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2})} \\ & {+ \tilde {\theta} \epsilon ((1 - \beta_ {B 0} ^ {1}) (- u _ {H} (1 - \beta_ {B B} ^ {1}) - \delta e _ {B B} ^ {2} - \delta \hat {e} _ {B B} ^ {2}) - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2})} \\ & {+ \tilde {\theta} \tilde {\epsilon} ((1 - \beta_ {B 0} ^ {1}) (- (u _ {L} - \mu) (1 - \beta_ {A B} ^ {1}) - \delta e _ {A B} ^ {2} - \delta \hat {e} _ {A B} ^ {2}) - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2})} \\ & {> \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) = \theta \epsilon ((1 - \beta_ {A 0} ^ {0}) (- u _ {H} (1 - \beta_ {A A} ^ {0}) - \delta e _ {A A} ^ {2} - \delta \hat {e} _ {A A} ^ {2}) - \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2})} \\ & {+ \theta \tilde {\epsilon} ((1 - \beta_ {A 0} ^ {0}) (- (u _ {L} - \mu) (1 - \beta_ {B A} ^ {0}) - \delta e _ {B A} ^ {2} - \delta \hat {e} _ {B A} ^ {2}) - \delta e _ {A 0} ^ {2} - \delta \hat {e} _ {A 0} ^ {2})} \\ & {+ \tilde {\theta} \epsilon ((1 - \beta_ {B 0} ^ {0}) (- u _ {H} (1 - \beta_ {B B} ^ {0}) - \delta e _ {B B} ^ {2} - \delta \hat {e} _ {B B} ^ {2}) - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2})} \\ & {+ \tilde {\theta} \tilde {\epsilon} ((1 - \beta_ {B 0} ^ {0}) (- (u _ {L} - \mu) (1 - \beta_ {A B} ^ {0}) - \delta e _ {A B} ^ {2} - \delta \hat {e} _ {A B} ^ {2}) - \delta e _ {B 0} ^ {2} - \delta \hat {e} _ {B 0} ^ {2}).} \end{array}\tag{39}
$$

Therefore, it is sufficient to show that

$$
(\Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) ^ {*} + C _ {\mathrm{HIE}} - \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) ^ {*}) > (\Pi^ {\mathrm{AB}} (\mathrm{H}, \mathrm{H}) ^ {*} + C _ {\mathrm{HIE}} - \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) ^ {*}),\tag{40}
$$

when $\alpha > 0 . \mathrm { W }$ hen $\alpha > 0$ , The above inequality can be reduced to

$$
\begin{array}{r l} & {- \frac {\alpha U (2 (\alpha - 2) \delta + U)}{2 (\delta + 2 U)}} \\ & {<   \frac {- u _ {L} ^ {3} \tilde {\epsilon} ^ {2} + 8 (\alpha - 1) \delta^ {2} u _ {H} \epsilon + u _ {L} ^ {2} \tilde {\epsilon} (2 \delta (2 - \alpha \tilde {\epsilon} - \epsilon) + 3 \mu^ {2} \tilde {\epsilon}}{- 4 \delta^ {2} - 4 \delta (2 u _ {H} \epsilon - \mu \tilde {\epsilon}) + u _ {L} ^ {2} \tilde {\epsilon} ^ {2} - 2 u _ {L} \tilde {\epsilon} (2 \delta + \mu - \mu \epsilon) + \mu^ {2} \tilde {\epsilon} ^ {2}}} \\ & {+ \frac {u _ {H} ^ {2} \epsilon (2 \delta + \mu - \mu \epsilon) + u _ {L} (\epsilon - 1) (- 8 (\alpha - 1) \delta^ {2} + 4 \delta \mu (\alpha (\epsilon - 1) - \epsilon + 2) + u _ {H} ^ {2} \epsilon)}{- 4 \delta^ {2} - 4 \delta (2 u _ {H} \epsilon - \mu \tilde {\epsilon}) + u _ {L} ^ {2} \tilde {\epsilon} ^ {2} - 2 u _ {L} \tilde {\epsilon} (2 \delta + \mu - \mu \epsilon) + \mu^ {2} \tilde {\epsilon} ^ {2}}} \\ & {+\frac {\mu (\epsilon - 1) (8 (\alpha - 1) \delta^ {2} + 2 \delta \mu (\alpha (- \epsilon) + \alpha + \epsilon - 2) + \mu^ {2} (\epsilon - 1))}{- 4 \delta^ {2} - 4 \delta (2 u _ {H} \epsilon - \mu \tilde {\epsilon}) + u _ {L} ^ {2} \tilde {\epsilon} ^ {2} - 2 u _ {L} \tilde {\epsilon} (2 \delta + \mu - \mu \epsilon) + \mu^ {2} \tilde {\epsilon} ^ {2}},} \end{array}\tag{41}
$$

which holds when $\alpha < { \overline { { \alpha } } } .$

As a result, there exist three different scenarios in the equilibrium regarding HIE adoption and patient switching behavior as follows.

1. $\mu \leq \mu _ { H H } ;$ All the patients return to the same provider for the second visit regardless of HIE adoption.

2. $\mu _ { H H } < \mu \leq \mu _ { N N } ;$ the low type patient visits to the different provider for the second visit under HIE adoption but returns to the same provider for the second visit under no HIE adoption. The high type patients returns to the same provider for the second visit regardless of HIE adoption.

3. $\mu > \mu _ { N N }$ : The low type patient visits to the different provider for the second visit regardless of HIE adoption. The high type patients returns to the same provider for the second visit regardless of HIE adoption.

We define $\overline { { C } } _ { H I E }$ such that

$$
\overline {{C}} _ {H I E} := \left\{ \begin{array}{l l} \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N}), C _ {\mathrm{HIE}} = \overline {{c}} _ {H I E}} & \\ = \Pi^ {\mathrm{AB}} (\mathrm{H}, \mathrm{H}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H}), C _ {\mathrm{HIE}} = \overline {{c}} _ {H I E}}, & \text {if} \mu \leq \mu_ {H H}, \\ \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N}), C _ {\mathrm{HIE}} = \overline {{c}} _ {H I E}} & \\ = \Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H}), C _ {\mathrm{HIE}} = \overline {{c}} _ {H I E}}, & \text {if} \mu_ {H H} <   \mu \leq \mu_ {N N}, \\ \Pi^ {\mathrm{BA}} (\mathrm{N}, \mathrm{N}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{N}, \mathrm{N}), C _ {\mathrm{HIE}} = \overline {{c}} _ {\mathrm{HIE}}} & \\ = \Pi^ {\mathrm{BA}} (\mathrm{H}, \mathrm{H}) | _ {e _ {i j} = e _ {i j} ^ {*} (\mathrm{H}, \mathrm{H}), C _ {\mathrm{HIE}} = \overline {{c}} _ {H I E}}, & \text {if} \mu_ {N N} <   \mu . \end{array} \right.\tag{42}
$$

## Proof of Lemma 3

No HIE adoption: Consider the scenario where HIE is not induced $( S _ { \mathrm { A } } , S _ { \mathrm { B } } ) = ( \mathrm { N } , \mathrm { N } )$ .

Stage 5. We derive the solutions under no HIE adoption scenario provided in Lemma 5.1 by solving the following simultaneous equations.

$$
\begin{array}{l} \frac {\partial \pi_ {i i} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial \hat {e} _ {i l}} = 0, \forall i \in \{A, B \} \text {and} (k, l) = \{(A, B), (B, A) \}, \\ \frac {\partial \pi_ {i (- i)} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \} \text {and} (k, l) = (A, B). \end{array}\tag{43}
$$

(44)

Stage 3 and 4. First consider the scenario where the low type patient visits a different provider for the second visit. The first-order conditions (FOCs) give the following simultaneous equations.

$$
\left. \frac {\partial \pi_ {i _ {0}} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial e _ {i _ {0}}} \right| _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (\mathrm{N,N}) \end{array} } = \left. \frac {\partial \pi_ {i _ {0}} ^ {\mathrm{F}} (\mathrm{N,N})}{\partial \hat {e} _ {i _ {0}}} \right| _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (\mathrm{N,N}) \end{array} } = 0, \forall i, j \in \{A, B \}.\tag{45}
$$

Solving these equations, we have the following stationary point.

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \epsilon \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = - \frac {\epsilon \gamma_ {2} ^ {2}}{8 \delta^ {2}}.\tag{46}
$$

However, since $\begin{array} { r } { - \frac { \epsilon \gamma _ { 2 } ^ { 2 } } { 8 \delta ^ { 2 } } \leq 0 } \end{array}$ , the solution in (46) cannot be optimal. Now we construct provider ??’s Lagrangian which is formulated as

$$
L_{i0}(\mathrm{N},\mathrm{N}) = \pi_{i0}^{\mathrm{F}}(\mathrm{N},\mathrm{N})|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{N},\mathrm{N}),\\ \hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{N},\mathrm{N})}} + \lambda_{1}(e_{i0}) + \lambda_{2}(\hat{e}_{i0}) + \lambda_{3}(1 - e_{i0} - \hat{e}_{i0})\tag{47}
$$

Using Kuhn-Tucker (K-T) conditions, we have the following stationary point.

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \epsilon \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = 0.\tag{48}
$$

Now consider the scenario where the low type patient returns to the same provider for the second visit. The FOCs give the following simultaneous equations.

$$
\frac{\partial\pi_{i_{0}}^{\mathrm{F}}(\mathrm{N,N})}{\partial e_{i_{0}}}\Big|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{N,N}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{N,N})}} = \frac{\partial\pi_{i_{0}}^{\mathrm{F}}(\mathrm{N,N})}{\partial\hat{e}_{i_{0}}}\Big|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{N,N}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{N,N})}} = 0,\forall i\in \{A,B\} .\tag{49}
$$

Solving these equations, we have the following stationary point.

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = - \frac {\gamma_ {2} ^ {2}}{8 \delta^ {2}}.\tag{50}
$$

However, since $\begin{array} { r } { - \frac { \gamma _ { 2 } ^ { 2 } } { 8 \delta ^ { 2 } } \leq 0 } \end{array}$ , the solution in (50) cannot be optimal.

Now we construct provider ??’s Lagrangian which is formulated as

$$
L _ {i 0} (\mathrm{N}, \mathrm{N}) = \pi_ {i 0} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) | _ {e _ {i i} = e _ {i i} ^ {*} (\mathrm{N}, \mathrm{N}), \atop \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{N}, \mathrm{N})} + \lambda_ {1} (e _ {i 0}) + \lambda_ {2} (\hat {e} _ {i 0}) + \lambda_ {3} (1 - e _ {i 0} - \hat {e} _ {i 0})\tag{51}
$$

Using K-T conditions, we have the following stationary point for $\forall i \in \{ \mathsf { A } , \mathsf { B } \}$

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = 0.\tag{52}
$$

Stage 2. The HIE adoption is dominated because, regardless of patient behavior, the providers’ expected future payoff excluding the HIE adoption cost remains identical under HIE adoption and no HIE adoption scenarios, but HIE adoption has a cost of $C _ { \mathrm { H I E } } > 0$

Stage 1. The social planner chooses optimal contract parameters $\gamma _ { 1 } , \gamma _ { 2 }$ , and ?? that induce patient switching or induce no patient switching in order to maximize the social welfare. First consider the scenario where the low type patient switch to a different provider for the second visit. We define $\ddot { \gamma } _ { 1 } ^ { \mathrm { F } }$ and $\ddot { \gamma } _ { 2 } ^ { \mathrm { F } }$ such that

$$
\frac{\partial\Pi^{\mathrm{BA}}(\mathrm{N,N})}{\partial\gamma_{1}}\bigg|_{e_{ij} = e_{ij}^{*}(\mathrm{N,N}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{N,N}),}\\ = 0,\forall i\in \{0,A,B\} ,j\in \{A,B\} .\\ \gamma_{1}^{\mathrm{F}} = \ddot{\gamma}_{1}^{\mathrm{F}},\gamma_{2}^{\mathrm{F}} = \ddot{\gamma}_{2}^{\mathrm{F}}\tag{53}
$$

$$
\frac{\partial\Pi^{\mathrm{BA}}(\mathrm{N,N})}{\partial\gamma_{2}}\bigg|_{e_{ij} = e_{ij}^{*}(\mathrm{N,N}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{N,N}),} = 0,\forall i\in \{0,A,B\} ,j\in \{A,B\} ,\\ \gamma_{1}^{\mathrm{F}} = \ddot{\gamma}_{1}^{\mathrm{F}},\gamma_{2}^{\mathrm{F}} = \ddot{\gamma}_{2}^{\mathrm{F}}\tag{54}
$$

which gives

$$
1 6 \delta^ {2} (u _ {H} \epsilon - u _ {L} \epsilon + u _ {L} - \mu \tilde {\epsilon}) = - 6 (\ddot {\gamma} _ {1} ^ {\mathrm{F}}) ^ {2} \delta \tilde {\epsilon} + (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) \epsilon \big (4 \delta u _ {H} + (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) (2 \delta \epsilon - 6 \delta + \mu \tilde {\epsilon} - 2 u _ {H} - u _ {L} \tilde {\epsilon}) \big)
$$

$$
+ (\ddot {\gamma} _ {1} ^ {\mathrm{F}}) \big (8 \delta (- \delta \epsilon + 2 \delta - \mu \tilde {\epsilon} + u _ {H} \epsilon - u _ {L} \epsilon + u _ {L}) + (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) ^ {2} \tilde {\epsilon} \epsilon \big),\tag{55}
$$

$$
- (\ddot {\gamma} _ {1} ^ {\mathrm{F}}) ^ {2} (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) \delta \tilde {\epsilon} + 3 (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) ^ {2} \delta u _ {H} + 8 \delta^ {3} u _ {H} = 4 (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) \delta^ {2} (2 \delta - \mu \tilde {\epsilon} + 2 u _ {H} - u _ {L} \epsilon + u _ {L})
$$

$$
+ (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) ^ {3} (\delta (- \epsilon^ {2} + \epsilon + 3) + u _ {H}) + 2 (\ddot {\gamma} _ {1} ^ {\mathrm{F}}) \delta \big (2 \delta u _ {H} + (\ddot {\gamma} _ {2} ^ {\mathrm{F}}) (2 \delta \epsilon - 6 \delta + \mu \tilde {\epsilon} - 2 u _ {H} - u _ {L} \tilde {\epsilon}) \big)\tag{56}
$$

Therefore, $\ddot { \gamma } _ { 1 } ^ { \mathrm { F } }$ and $\ddot { \gamma } _ { 2 } ^ { \mathrm { F } }$ are the values that satisfy the above simultaneous equations.

We obtain the optimal $\tau ^ { \mathrm { F } }$ by solving the provider’s individual rationality (IR) constraints.

$$
\begin{array}{r} [ \theta \pi_ {A 0} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) + (1 - \theta) \tilde {\epsilon} (1 - \beta_ {A 0} ^ {0}) \pi_ {A B} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) ] | _ { \begin{array}{c} e _ {A 0} = e _ {A 0} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A 0} = \hat {e} _ {A 0} ^ {*} (\mathrm{N}, \mathrm{N}) \\ e _ {A B} = e _ {A B} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A B} = \hat {e} _ {A B} ^ {*} (\mathrm{N}, \mathrm{N}) \end{array} } \geq \omega_ {A} \\ \end{array}\tag{57}
$$

$$
[ (1 - \theta)\pi_{B0}^{\mathrm{F}}(\mathrm{N},\mathrm{N}) + \theta \tilde{\epsilon} (1 - \beta_{A0}^{0})\pi_{BA}^{\mathrm{F}}(\mathrm{N},\mathrm{N})]\big|_{\substack{e_{B0} = e_{B0}^{*}(\mathrm{N},\mathrm{N}),\hat{e}_{B0} = \hat{e}_{B0}^{*}(\mathrm{N},\mathrm{N})\\ e_{BA} = e_{BA}^{*}(\mathrm{N},\mathrm{N}),\hat{e}_{BA} = \hat{e}_{BA}^{*}(\mathrm{N},\mathrm{N})}}\geq \omega_{B}\tag{58}
$$

Ayvaci et al. / Designing Payment Contracts for Healthcare Services to Induce Information Sharing

Setting the minimum $\tau ^ { \mathrm { F } }$ that satisfies the IR constraints gives

$$
\begin{array}{r l} & {\tau^ {*} = \ddot {\tau} ^ {\mathrm{F}}} \\ & = m a x \{\frac {6 4 \omega_ {A} \delta^ {3} - 1 6 \ddot {\gamma} _ {2} ^ {2} \delta^ {2} \theta \epsilon - 2 \ddot {\gamma} _ {1} ^ {2} (\ddot {\gamma} _ {2} ^ {2} \widetilde {\theta} \tilde {\epsilon} \epsilon + 8 \delta^ {2} (1 - \widetilde {\theta} \epsilon)) + 8 \ddot {\gamma} _ {1} \ddot {\gamma} _ {2} ^ {2} \delta \theta \epsilon + 8 \ddot {\gamma} _ {1} ^ {3} \delta \widetilde {\theta} \tilde {\epsilon} + \dot {\gamma} _ {2} ^ {4} \theta (- \epsilon^ {2})}{8 \delta (- 4 \ddot {\gamma} _ {1} \delta \widetilde {\theta} \tilde {\epsilon} + \gamma_ {2} ^ {2} \tilde {\epsilon} \epsilon \tilde {\epsilon} + 8 \delta^ {2} \widetilde {\theta} \epsilon + 1))}, \\ & {\frac {6 4 \omega_ {B} \delta^ {3} - 1 6 \ddot {\gamma} _ {2} ^ {2} \delta^ {2} \widetilde {\theta} \epsilon - 2 \ddot {\gamma} _ {1} ^ {2} (\ddot {\gamma} _ {2} ^ {2} \theta \tilde {\epsilon} \epsilon + 8 \delta^ {2} (1 - \theta \epsilon)) + 8 \ddot {\gamma} _ {1} \ddot {\gamma} _ {2} ^ {2} \delta \widetilde {\theta} \epsilon + 8 \ddot {\gamma} _ {1} ^ {3} \delta \theta \tilde {\epsilon} + \dot {\gamma} _ {2} ^ {4} \widetilde {\theta} (- \epsilon^ {2})}{8 \delta (- 4 \ddot {\gamma} _ {1} \delta \theta \tilde {\epsilon} + \gamma_ {2} ^ {2} \tilde {\epsilon} \epsilon \tilde {\epsilon} + 8 \delta^ {2} \theta \epsilon + 1))}.} \end{array}\tag{59}
$$

Now consider the scenario where patients return to the same provider for the second visit. We derive the solution provided in Lemma 5.1 by solving the following simultaneous equations:

$$
\begin{array}{r l} & {\frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{N,N})}{\partial \gamma_ {1}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{N,N}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{N,N}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{N,N}), \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{N,N})} \\ & {= \frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{N,N})}{\partial \gamma_ {2}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{N,N}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{N,N}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{N,N}), \hat {e} _ {i i} = {\hat {e}} _ {i i} ^ {*} (\mathrm{N,N})} \\ & {= 0, \forall i \in \{A, B \}.} \end{array}\tag{60}
$$

(61)

The corresponding objective function becomes

$$
\Pi^ {\mathrm{AB} *} (\mathrm{N}, \mathrm{N}) := \frac {U (- 6 4 \delta^ {3} + U ^ {3} + 1 6 \delta^ {2} U)}{6 4 \delta^ {2} (\delta + U)}.\tag{62}
$$

Analogous to the switching case, We obtain the optimal $\tau ^ { \mathrm { F } }$ by solving the provider’s IR constraints as below.

$$
\begin{array}{r l} & {\tau^ {*} = \dot {\tau} _ {1} ^ {\mathrm{F}} := m a x \{\frac {\omega_ {A}}{\theta} - \frac {U ^ {4}}{6 4 \delta^ {3}} - \frac {(U ^ {3} + 8 \delta^ {2} U) ^ {2}}{4 \delta (4 \delta^ {2} + 4 \delta U) ^ {2}} - \frac {U ^ {2}}{4 \delta} + \frac {U ^ {2} (U ^ {3} + 8 \delta^ {2} U)}{8 \delta^ {2} (4 \delta^ {2} + 4 \delta U)},} \\ & {\frac {\omega_ {B}}{\widetilde {\theta}} - \frac {U ^ {4}}{6 4 \delta^ {3}} - \frac {(U ^ {3} + 8 \delta^ {2} U) ^ {2}}{4 \delta (4 \delta^ {2} + 4 \delta U) ^ {2}} - \frac {U ^ {2}}{4 \delta} + \frac {U ^ {2} (U ^ {3} + 8 \δ^ {2} U)}{8 \δ^ {2} (4 \δ^ {2} + 4 \δ U)} \}.} \end{array}\tag{63}
$$

Finally, we compare the objective function under switching behavior of the low type patient and the objective function under no switching behavior. Applying envelope theorem, we verify that

$$
\frac {\partial \Pi^ {\mathrm{AB} ^ {*}} (\mathrm{N,N})}{\partial \mu} = 0, \frac {\partial \Pi^ {\mathrm{BA} ^ {*}} (\mathrm{N,N})}{\partial \mu} > 0.\tag{64}
$$

By defining $\mu ^ { \mathrm { F } } ( \Nu , \Nu )$ such that

$$
\Pi^ {\mathrm{AB} *} (\mathrm{N}, \mathrm{N}) | _ {\mu = \mu^ {\mathrm{F}} (\mathrm{N}, \mathrm{N})} = \Pi^ {\mathrm{BA} *} (\mathrm{N}, \mathrm{N}) | _ {\mu = \mu^ {\mathrm{F}} (\mathrm{N}, \mathrm{N})},\tag{65}
$$

we ensure that the policy maker is indifferent between the two patient switching scenarios. Therefore, as we observe from (64), the policy maker prefers the patient to switch if ${ \bf \Pi } ^ { \prime } { \pmb { \mu } } > { \pmb { \mu } } ^ { \mathbf { F } } ( \mathbf { N } , \mathbf { N } )$

## Proof of Proposition 1

Proof follows from nonadoption of HIE and zero unobservable efforts.

## Proof of Lemma 4

We derive the optimal solution for each HIE adoption scenario and then derive the condition that ensures the corresponding HIE adoption decision.

No HIE adoption Case: Consider the scenario where HIE is not induced $( S _ { \mathrm { A } } , S _ { \mathrm { B } } ) = ( \mathrm { N } , \mathrm { N } )$

Stage 5. We derive the solutions under no HIE adoption scenario provided in Lemma 5.2 by solving the following simultaneous equations.

$$
\frac {\partial \pi_ {i i} ^ {\mathsf {P}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathsf {P}} (\mathrm{N,N})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = \{(\mathrm{A,B}), (\mathrm{B,A}) \},\tag{66}
$$

$$
\frac {\partial \pi_ {i (- i)} ^ {\mathrm{P}} (\mathrm{N,N})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{P}} (\mathrm{N,N})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (\mathrm{B,A}).\tag{67}
$$

Stage 3 and 4. First consider the scenario where the low type patient visits a different provider for the second visit. The following simultaneous equations give the solutions to the provider’s maximization problem under no HIE adoption and patient switching.

$$
\left. \frac {\partial \pi_ {i 0} ^ {\mathrm{P}} (\mathrm{N,N})}{\partial e _ {i 0}} \right| _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (\mathrm{N,N}) \end{array} } = \left. \frac {\partial \pi_ {i 0} ^ {\mathrm{P}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} \right| _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {*} (\mathrm{N,N}), \\ \hat {e} _ {i j} = \hat {e} _ {i j} ^ {*} (\mathrm{N,N}) \end{array} } = 0, \forall i, j \in \{B, A \}.\tag{68}
$$

Now consider the scenario where all the patients return to the same provider for the second visit. The following simultaneous equations give the solutions to the provider’s maximization problem under no HIE adoption and no patient switching.

$$
\frac{\partial\pi_{i0}^{\mathrm{P}}(\mathrm{N,N})}{\partial e_{i0}}\Big|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{N,N}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{N,N})}} = \frac{\partial\pi_{i0}^{\mathrm{P}}(\mathrm{N,N})}{\partial\hat{e}_{i0}}\Big|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{N,N}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{N,N})}} = 0,\forall i\in \{A,B\} .\tag{69}
$$

Stage 1. The social planner chooses optimal contract parameters $p _ { 1 } , p _ { 2 }$ , and $\tau ^ { \mathrm { P } }$ that induce patient switching or induce no patient switching in order to maximize the social welfare. First consider the scenario where the low type patient switches to the different provider for the second visit. We define $\ddot { p } _ { 1 }$ and $\ddot { p } _ { 2 }$ such that the following FOCs hold.

$$
\frac{\partial\Pi^{\mathrm{BA}}(\mathrm{N,N})}{\partial p_{1}}\Big|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{N,N}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{N,N}),\\ p_{1} = \ddot{p}_{1},p_{2} = \ddot{p}_{2}}} = 0,\forall i\in \{A,B\} \text{and} j\in \{0,A,B\} ,\tag{70}
$$

$$
\frac{\partial\Pi^{\mathrm{BA}}(\mathrm{N,N})}{\partial p_{2}}\Big|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{N,N}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{N,N}),\\ p_{1} = \ddot{p}_{1},p_{2} = \ddot{p}_{2}}} = 0,\forall i\in \{A,B\} \text{and} j\in \{0,A,B\} .\tag{71}
$$

which gives

$$
\begin{array} { r l } & 0 = \frac { 1 } { \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon } ( 2 \delta ^ { 2 } ( \ddot { p } _ { 2 } ) \epsilon ( 2 \delta + 4 \mu \tilde { \epsilon } + u _ { H } - 4 u _ { L } \tilde { \epsilon } ) - 4 \delta ^ { 3 } ( u _ { H } \epsilon + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) \\ & + \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( - 2 \delta + \mu \tilde { \epsilon } + 2 u _ { H } \epsilon - u _ { L } \tilde { \epsilon } ) - 3 \delta ( \ddot { p } _ { 1 } ) ^ { 2 } \tilde { \epsilon } ( \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon ) + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ^ { 2 } ( - \delta + \mu \tilde { \epsilon } - u _ { L } \tilde { \epsilon } ) \\ & + ( \ddot { p } _ { 1 } ) ( \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \tilde { \epsilon } \epsilon + 4 \delta ( \ddot { p } _ { 2 } ) \tilde { \epsilon } \epsilon ( \delta - 2 \mu + 2 u _ { L } ) + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \tilde { \epsilon } \epsilon ^ { 2 } + 2 \delta ^ { 2 } ( \delta ( - \epsilon ) + 2 \delta - 2 \mu + 2 u _ { H } \tilde { \epsilon } \epsilon \\ & + 2 u _ { L } \tilde { \epsilon } ) ) , \\ & 0 = \frac { 1 } { \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon } ( - 2 \delta ^ { 4 } ( 4 u _ { H } \epsilon + u _ { H } + 2 \tilde { \epsilon } ( u _ { L } - \mu ) ) + 2 \delta ^ { 3 } ( 4 \delta \epsilon + \delta + u _ { L } ( 4 \epsilon ^ { 2 } - 5 \epsilon + 1 ) \\ & + \mu ( - 4 \epsilon ^ { 2 } + 5 \epsilon - 1 ) ) ( \ddot { p } _ { 2 } ) - 3 \delta ^ { 2 } ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( u _ { H } - 2 \tilde { \epsilon } ( u _ { L } - \mu ) ) + \delta ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ( 3 \delta \\ & - 4 \epsilon ( 2 u _ { H } - \tilde { \epsilon } ( u _ { L } - \mu ) ) ) + 2 ( \ddot { p } _ { 2 } ) ^ { 4 } \epsilon ^ { 2 } ( 4 \delta - 3 u _ { H } \epsilon ) + 6 ( \ddot { p } _ { 2 } ) ^ { 5 } \epsilon ^ { 3 } \\ & + 2 \delta ( \ddot { p } _ { 1 } ) ^ { 3 } \tilde { \epsilon } ( \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon ) + ( \ddot { p } _ { 1 } ) ^ { 2 } ( 2 \delta ^ { 2 } ( \delta ( \epsilon - 3 ) + 2 \mu \tilde { \epsilon } - 4 u _ { H } \epsilon - 2 u _ { L } \tilde { \epsilon } ) \\ & 3 \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \tilde { \epsilon } \epsilon - \delta ( \ddot { p } _ { 2 } ) \tilde { \epsilon } ( \delta ( 4 \epsilon - 1 ) + 8 \epsilon ( u _ { L } - \mu ) ) + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \tilde { \epsilon } \epsilon ^ { 2 } ) \\ & + 2 ( \ddot { p } _ { 1 } ) ( \delta ^ { 3 } ( 2 \delta - 4 \mu \tilde { \epsilon } + 8 \epsilon + u _ { H } - 4 u _ { L } \epsilon + 4 u _ { L } ) \\ & - \delta ^ { 2 } ( \ddot { p } _ { 2 } ) ( \delta ( 4 \epsilon + 2 ) + u _ { L } ( 8 \epsilon ^ { 2 } - 9 \epsilon + 1 ) + \mu ( - 8 \epsilon ^ { 2 } + 9 \epsilon - 1 ) ) \\ & + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ^ { 2 } ( - \delta + \mu - u _ { L } \tilde { \epsilon } - \mu \epsilon ) - 3 \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( \delta + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) . \\ & = - i n e x t ] . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & .. \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & .; \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & . \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & .. \\ & ..; \\ & [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i g ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ d i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] = [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i f ] > [ D i | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I |I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N, N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,M ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,N ,n ,n ;< |content_end|>\tag{72}
$$

Therefore, $\ddot { p } _ { 1 } ( \mathrm { N } , \mathrm { N } )$ and $\ddot { p } _ { 2 } ( \mathrm { N } , \mathrm { N } )$ are the values of $\ddot { p } _ { 1 }$ and $\ddot { p } _ { 2 }$ , respectively, that satisfy the above simultaneous equations.

Let $\Pi ^ { \mathrm { B A * } } ( \mathsf { N } , \mathsf { N } )$ be the maximized objective function of the social planner. We obtain the optimal $\tau ^ { \mathrm { P } }$ by solving the provider’s IR constraints.

$$
\begin{array}{r} [ \theta \pi_ {A 0} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) + (1 - \theta) \tilde {\epsilon} (1 - \beta_ {B 0} ^ {0}) \pi_ {A B} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) ] | _ { \begin{array}{c} e _ {A 0} = e _ {i 0} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A 0} = \hat {e} _ {A 0} ^ {*} (\mathrm{N}, \mathrm{N}) \\ e _ {A B} = e _ {A B} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A B} = \hat {e} _ {A B} ^ {*} (\mathrm{N}, \mathrm{N}) \end{array} } \geq \omega_ {A}, \end{array}\tag{73}
$$

$$
\begin{array}{r} [ (1 - \theta) \pi_ {B 0} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) + \theta \tilde {\epsilon} (1 - \beta_ {A 0} ^ {0}) \pi_ {B A} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) ] | _ { \begin{array}{c} e _ {B 0} = e _ {B 0} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {B 0} = \hat {e} _ {B 0} ^ {*} (\mathrm{N}, \mathrm{N}) \\ e _ {B A} = e _ {B A} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {B A} = \hat {e} _ {B A} ^ {*} (\mathrm{N}, \mathrm{N}) \end{array} } \geq \omega_ {B}. \end{array}\tag{74}
$$

We let $\because ^ { \mathsf { P } } ( { \mathsf { N } } , { \mathsf { N } } )$ be the minimum $\tau ^ { \mathrm { P } }$ that satisfies both the IR constraints.

Now consider the scenario where all the patients return to the same provider for the second visit. The FOCs give the following simultaneous equations.

$$
\begin{array}{r l} & {\frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{N,N})}{\partial p _ {1}} \Big | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{N,N}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{N,N}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{N,N}), \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{N,N})} \\ & {= \frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{N,N})}{\partial p _ {2}} \Big | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{N,N}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{N,N}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{N,N}), \hat {e} _ {i i} = \widehat {e} _ {i i} ^ {*} (\mathrm{N,N})} \end{array} = 0, \forall i \in \{A, B \}. \nonumber\tag{75}
$$

(76)

Solving the equation above, we have the following stationary point.

$$
\{p _ {1} = 0, p _ {2} = U \}\tag{77}
$$

Analogous to the switching case, we obtain the optimal $\tau ^ { \mathrm { P } }$ by solving the providers’ IR constraints.

$$
\begin{array}{r l} & {\omega_ {A} = \theta \pi_ {A 0} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) | _ {e _ {A 0} = e _ {A 0} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A 0} = \hat {e} _ {A 0} ^ {*} (\mathrm{N}, \mathrm{N})}} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad e _ {A A} = e _ {A A} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {A A} = \hat {e} _ {A A} ^ {*} (\mathrm{N}, \mathrm{N})} \\ & {\omega_ {B} = (1 - \theta) \pi_ {B 0} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) | _ {e _ {B 0} = e _ {B 0} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {B 0} = \hat {e} _ {B 0} ^ {*} (\mathrm{N}, \mathrm{N})}.} \\ & {\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad e _ {B B} = e _ {B B} ^ {*} (\mathrm{N}, \mathrm{N}), \hat {e} _ {B B} = \hat {e} _ {B B} ^ {*} (\mathrm{N}, \mathrm{N})} \end{array}\tag{78}
$$

Let $\dot { \tau } ^ { \mathrm { P } } ( \mathsf { N } , \mathsf { N } )$ be the minimum $\tau ^ { \mathrm { P } }$ that satisfies both the IR constraints.

Finally, we compare the objective function under patient switching behavior and the objective function under no patient switching behavior. Applying envelope theorem, we verify that

$$
\frac {\partial \Pi^ {\mathrm{AB} ^ {*}} (\mathrm{N,N})}{\partial \mu} = 0, \frac {\partial \Pi^ {\mathrm{BA} ^ {*}} (\mathrm{N,N})}{\partial \mu} > 0.\tag{79}
$$

Let us define $\mu ^ { \mathrm { P } } ( \Nu , \Nu )$ such that

$$
\Pi^ {\mathrm{AB} *} (\mathrm{N}, \mathrm{N}) = \Pi^ {\mathrm{BA} *} (\mathrm{N}, \mathrm{N}).\tag{80}
$$

We ensure that the policy maker is indifferent between the two patient switching scenarios. Therefore, as we observe from (79), the policy maker prefers the patient to switch if $\dot { \mu } > \mu ^ { \sf P } ( { \sf N } , { \sf N } )$ .

HIE adoption Case: Consider the scenario where HIE is not induced $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( \mathrm { { H } , \mathrm { { H } ) } }$

Stage 5. We derive the solutions under HIE adoption scenario provided in Lemma 5.2 by solving the following simultaneous equations.

$$
\begin{array}{l} \frac {\partial \pi_ {i i} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \} \text {and} (k, l) = \{(\mathrm{A,B}), (\mathrm{B,A}) \}, \\ \frac {\partial \pi_ {i (- i)} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \} \text {and} (k, l) = (\mathrm{B,A}). \end{array}\tag{81}
$$

(82)

Stage 3 and 4. First consider the scenario where the low type patient visits a different provider for the second visit. The following simultaneous equations give the solutions to the provider’s maximization problem under HIE adoption and patient switching.

$$
\frac{\partial\pi_{i0}^{\mathrm{P}}(\mathrm{H,H})}{\partial e_{i0}}\bigg|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{H,H}),\\ \hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{H,H})}} = \frac{\partial\pi_{i0}^{\mathrm{P}}(\mathrm{H,H})}{\partial\hat{e}_{i0}}\bigg|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{H,H}),\\ \hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{H,H})}} = 0,\forall i,j\in \{A,B\} .\tag{83}
$$

Now consider the scenario where all the patients return to the same provider for the second visit. The following simultaneous equations give the solutions to the provider’s maximization problem under HIE adoption and no patient switching.

$$
\frac {\partial \pi_ {i _ {0}} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial e _ {i _ {0}}} \Big | _ { \begin{array}{c} e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}), \\ \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{H,H}) \end{array} } = \frac {\partial \pi_ {i _ {0}} ^ {\mathrm{P}} (\mathrm{H,H})}{\partial \hat {e} _ {i _ {0}}} \Big | _ { \begin{array}{c} e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}), \\ \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{H,H}) \end{array} } = 0, \forall i \in \{A, B \}.\tag{84}
$$

Stage 1. The social planner chooses optimal contract parameters $p _ { 1 } , p _ { 2 } ,$ , and $\tau ^ { \mathrm { P } }$ that induce patient switching or induce no patient switching in order to maximize the social welfare. First consider the scenario where the low type patient switches to the differen provider for the second visit. We define $\ddot { p } _ { 1 }$ and $\ddot { p } _ { 2 }$ such that the following FOCs hold.

$$
\begin{array}{r}\frac{\partial\Pi^{\mathrm{BA}}(\mathrm{H},\mathrm{H})}{\partial p_{1}}\Big|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{H},\mathrm{H}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{H},\mathrm{H}),\\ p_{1} = \ddot{p}_{1},p_{2} = \ddot{p}_{2}}} = 0, \forall i\in \{A,B\} \text{and} j\in \{0,A,B\} ,\\ \frac{\partial\Pi^{\mathrm{BA}}(\mathrm{H},\mathrm{H})}{\partial p_{2}}\Big|_{\substack{e_{ij} = e_{ij}^{*}(\mathrm{H},\mathrm{H}),\hat{e}_{ij} = \hat{e}_{ij}^{*}(\mathrm{H},\mathrm{H}),\\ p_{1} = \ddot{p}_{1},p_{2} = \ddot{p}_{2}}} = 0, \forall i\in \{A,B \} \text{and} j\in \{0,A,B\}. \end{array}\tag{85}
$$

(86)

which gives

$$
\begin{array} { r l } & { \frac { 1 } { \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon } ( 3 \delta ( \ddot { p } _ { 1 } ) ^ { 2 } ( \tilde { \epsilon } ) ( \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon ) + ( \ddot { p } _ { 1 } ) ( - \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \tilde { \epsilon } \epsilon - 4 \delta ( \ddot { p } _ { 2 } ) \tilde { \epsilon } \epsilon ( - \alpha \delta + \delta - 2 \mu + 2 u _ { L } ) - 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \tilde { \epsilon } \epsilon ^ { 2 } } \\ & { + 2 \delta ^ { 2 } ( \delta ( \alpha ( - \epsilon ) + \alpha + \epsilon - 2 ) + 3 \mu - 2 u _ { H } \epsilon - 3 u _ { L } \tilde { \epsilon } - 3 \mu \epsilon ) ) - 2 \delta ^ { 2 } ( \ddot { p } _ { 2 } ) \epsilon ( u _ { H } - ( \alpha - 1 ) } \\ & { ( 2 \delta + 3 \mu - 3 u _ { L } \tilde { \epsilon } - 3 \mu \epsilon ) ) + 2 \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( \delta - \mu - u _ { H } \epsilon + u _ { L } ( - \epsilon ) + u _ { L } + \mu \epsilon ) } \\ & { + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ^ { 2 } ( \delta + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) + ( \alpha - 1 ) \delta ^ { 3 } ( - 4 u _ { H } \epsilon - 5 u _ { L } \tilde { \epsilon } + 5 \mu \tilde { \epsilon } ) ) = 0 , } \\ & { \frac { 1 } { \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon } ( 2 \delta ( \ddot { p } _ { 1 } ) ^ { 3 } \tilde { \epsilon } ( \delta + 2 ( \ddot { p } _ { 2 } ) \epsilon ) + ( \ddot { p } _ { 1 } ) ^ { 2 } ( 3 \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \tilde { \epsilon } \epsilon + \delta ( \ddot { p } _ { 2 } ) \tilde { \epsilon } ( - 4 \tilde { \epsilon } \delta \epsilon + \delta + 8 \epsilon ( \mu - u _ { L } ) ) + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \tilde { \epsilon } \epsilon ^ { 2 } } \\ & { + 2 \delta ^ { 2 } ( \delta ( \alpha ( - \epsilon ) + \alpha + \epsilon - 3 ) - 4 ( u _ { H } \epsilon - \mu \tilde { \epsilon } ) - 4 u _ { L } \tilde { \epsilon } ) ) - 3 \delta ^ { 2 } ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( u _ { H } - ( \alpha - 1 ) \tilde { \epsilon } ( u _ { L } - \mu ) ) } \\ & { - 2 ( \ddot { p } _ { 1 } ) ( 2 \delta ^ { 2 } ( \ddot { p } _ { 2 } ) ( - 2 ( \alpha - 1 ) \delta \epsilon - \mu \tilde { \epsilon } ( 3 ( \alpha - 1 ) \epsilon + 1 ) + \delta + u _ { L } \tilde { \epsilon } ( 3 ( \alpha - 1 ) \epsilon + 1 ) ) } \\ & { + 2 ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ^ { 2 } ( \delta + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) + 3 \delta ( \ddot { p } _ { 2 } ) ^ { 2 } \epsilon ( \delta + u _ { L } ( - \epsilon ) + u _ { L } - \mu \tilde { \epsilon } ) + \delta ^ { 3 } ( u _ { H } ( 8 ( \alpha - 1 ) \epsilon - 1 ) } \\ &  + ( \alpha - 1 ) ( 2 \delta + 7 u _ { L } \tilde { \epsilon } - 7 \mu \tilde { \epsilon} ) ) ) + \delta ( \ddot { p } _ { 2 } ) ^ { 3 } \epsilon ( - 2 a {\mu} e ^ { 2 } + 2 a {\mu} e + 3 {\delta} - {\mu} - 8 u _ { H } e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e n t h e m a x i o n d i s i o n g . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . c o m p o r o f i o n s i o n g i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g ; i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g ~ ; ~ i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g , i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o m a x i o n d i s i o n g ~ ; ~ i o l l a y ~ ; ~ i o l l a y ~ ; ~ i j k l a y ~ ; ~ i j k l a y ~ ; ~ i j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y ~ ; ~ j k l a y~ ; ~ j k l a y ~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~ ; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k l a y~; ~ j k | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
\end{array}
$$

Therefore, $\ddot { p } _ { 1 } ( \mathrm { H } , \mathrm { H } )$ and $\ddot { p } _ { 2 } ( \mathrm { H } , \mathrm { H } )$ are the values of $\ddot { p } _ { 1 }$ and $\ddot { p } _ { 2 } .$ , respectively, that satisfy the above simultaneous equations.

Let $\Pi ^ { \mathrm { B A * } } ( \mathrm { H } , \mathrm { H } )$ be the objective function evaluated at the optimal effort levels. We obtain the optimal $\tau ^ { \mathrm { P } }$ by solving the provider’s IR constraints.

$$
\begin{array}{r l} & {\omega_ {A} \leq [ \theta \pi_ {A 0} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) + (1 - \theta) \tilde {\epsilon} (1 - \beta_ {B 0} ^ {1}) \pi_ {A B} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) - \theta C _ {\mathrm{HIE}} ] | _ {e _ {A 0} = e _ {t 0} ^ {*} (\mathrm{H}, \mathrm{H}), \hat {e} _ {A 0} = \hat {e} _ {A 0} ^ {*} (\mathrm{H}, \mathrm{H})},} \\ & {\omega_ {B} \leq [ (1 - \theta) \pi_ {B 0} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) + \theta \tilde {\epsilon} (1 - \beta_ {A 0} ^ {1}) \pi_ {B A} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H})} \\ & {- (1 - \theta) C _ {\mathrm{HIE}} ] | _ {e _ {B 0} = e _ {B 0} ^ {*} (\mathrm{H}, \mathrm{H}), \hat {e} _ {B 0} = \hat {e} _ {B 0} ^ {*} (\mathrm{H}, \mathrm{H})}.} \\ & {\qquad e _ {B A} = e _ {B A} ^ {*} (\mathrm{H}, \mathrm{H}), \hat {e} _ {B A} = \hat {e} _ {B A} ^ {*} (\mathrm{H}, \mathrm{H})} \end{array}\tag{87}
$$

(88)

We let $\because ^ { \mathrm { P } } ( \mathrm { H } , \mathrm { H } )$ be the minimum $\tau ^ { \mathrm { P } }$ that satisfies both the IR constraints.

Now consider the scenario where all the patients return to the same provider for the second visit. The FOCs give the following simultaneous equations.

$$
\begin{array}{r l} & {\frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{H,H})}{\partial p _ {1}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{H,H}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{H,H}), \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{H,H})} \\ & {= \frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{H,H})}{\partial p _ {2}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{H,H}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{H,H}), \hat {e} _ {i i} = {\hat {e}} _ {i i} ^ {*} (\mathrm{H,H})} \\ & {= 0, \forall i \in \{A, B \}.} \end{array}\tag{89}
$$

(90)

Solving the equation above, we have the following stationary point.

$$
\{p _ {1} = 0, p _ {2} = U \}\tag{91}
$$

Analogous to the switching case, we obtain the optimal $\tau ^ { \mathrm { P } }$ by solving the providers’ IR constraints.

$$
\omega_ {A} \leq [ \theta \pi_ {A 0} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) - \theta C _ {\mathrm{HIE}} ] | _ {e _ {A 0} = e _ {A 0} ^ {*} (\mathrm{H}, \mathrm{H}), \hat {e} _ {A 0} = \hat {e} _ {A 0} ^ {*} (\mathrm{H}, \mathrm{H})},\tag{92}
$$

$$
e _ {A A} = e _ {A A} ^ {*} (\mathrm{H,H}), \hat {e} _ {A A} = \hat {e} _ {A A} ^ {*} (\mathrm{H,H})
$$

$$
\omega_{B}\leq [(1 - \theta)\pi_{B0}^{\mathrm{P}}(\mathrm{H},\mathrm{H}) - (1 - \theta)C_{\mathrm{HIE}}]\big|_{\substack{e_{B0} = e_{B0}^{*}(\mathrm{H},\mathrm{H}),\hat{e}_{B0} = \hat{e}_{B0}^{*}(\mathrm{H},\mathrm{H}),\\ e_{BB} = e_{BB}^{*}(\mathrm{H},\mathrm{H}),\hat{e}_{BB} = \hat{e}_{BB}^{*}(\mathrm{H},\mathrm{H})}}.\tag{93}
$$

Let $\scriptstyle { \dot { \tau } } ^ { \mathrm { P } } ( \mathrm { H } , \mathrm { H } )$ be the minimum $\tau ^ { \mathrm { P } }$ that satisfies both the IR constraints.

Finally, we compare the objective function under patient switching behavior and the objective function under no patient switching behavior. Applying envelope theorem, we verify that

$$
\frac {\partial \Pi^ {\mathrm{AB} *} (\mathrm{H,H})}{\partial \mu} = 0, \frac {\partial \Pi^ {\mathrm{BA} *} (\mathrm{H,H})}{\partial \mu} > 0.\tag{94}
$$

Let us define $\mu ^ { \mathrm { P } } ( \mathrm { H } , \mathrm { H } )$ such that

$$
\Pi^ {\mathrm{AB} *} (\mathrm{H}, \mathrm{H}) = \Pi^ {\mathrm{BA} *} (\mathrm{H}, \mathrm{H}).\tag{95}
$$

We ensure that the policy maker is indifferent between the two patient switching scenarios. Therefore, as we observe from (94), the policy maker prefers the patient to switch i $\mathrm { { } ^ { : } } \mu > \mu ^ { \mathrm { P } } ( \mathrm { { H } , \mathrm { { H } ) } }$

Sufficient Conditions for no HIE adoption: Suppose there exists a threshold, $\tilde { C } _ { H I E }$ , such that the providers do not adopt HIE if $C _ { \mathrm { H I E } } >$ $\tilde { C } _ { H I E }$ . Consider the scenario where all the patients return to the same provider for the second visit and the providers do not adopt HIE Given a set of contract parameters, $p _ { 1 } , p _ { 2 }$ , and $\tau ^ { \mathrm { P } }$ , the expected future payoffs of the providers become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) := \frac {\theta (8 \delta^ {3} \tau_ {1} - 8 \delta^ {2} p _ {2} (\delta - 2 \tau_ {1}) + 4 \delta^ {2} p _ {2} ^ {2} + 4 \delta^ {2} p _ {1} ^ {2} - 4 \delta p _ {1} (2 \delta^ {2} + p _ {2} ^ {2}) + p _ {2} ^ {4})}{8 \delta^ {2} (\delta + 2 p _ {2})},} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) := (\frac {1}{\theta} - 1) \dot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}).} \end{array}\tag{96}
$$

Next, consider the scenario where the low type patient switches to the different provider for the second visit, the high type patient returns to the same provider for the second visit, and the providers do not adopt HIE. Given a set of contract parameters, $p _ { 1 } , p _ { 2 }$ , and $\tau ^ { \mathrm { P } }$ , the expected future payoffs of the providers become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) = \ddot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) := - \frac {(\delta + (\theta - 1) p _ {1}) (- 2 \delta \tau_ {1} + 2 \delta p _ {1} - p _ {1} ^ {2})}{2 \delta^ {2}},} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{P}} (\mathrm{N}, \mathrm{N}) = \ddot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) := - \frac {(\delta - \theta p _ {1}) (- 2 \delta \tau_ {1} + 2 \delta p _ {1} - p _ {1} ^ {2})}{2 \delta^ {2}}.} \end{array}\tag{97}
$$

Now consider the scenario where the patients return to the same provider for the second visit and the providers adopt HIE. Given a set of contract parameters, $p _ { 1 } , p _ { 2 }$ , and $\tau ^ { \mathrm { P } }$ , the expected future payoffs of the providers become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}) := - (\theta) C _ {\mathrm{HIE}}} \\ & {+ \frac {\theta (8 \delta^ {3} \tau_ {1} + p _ {1} (8 (\alpha - 1) \delta^ {3} - 4 \delta p _ {2} ^ {2}) - 8 \delta^ {2} p _ {2} ((\alpha - 1) ^ {2} \delta - 2 \tau_ {1}) - 4 (\alpha - 1) \delta^ {2} p _ {2} ^ {2} + 4 \delta^ {2} p _ {1} ^ {2} + p _ {2} ^ {4})}{8 \delta^ {2} (\delta + 2 p _ {2})},} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) := (\frac {1}{\theta} - 1) \dot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}).} \end{array}\tag{98}
$$

Finally, suppose the patients visits to the different provider for the second visit and the providers adopt HIE. Given a set of contract parameters, $p _ { 1 } , p _ { 2 }$ , and $\tau ^ { \mathrm { P } }$ , the total expected payoffs of the providers become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) = \ddot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}) := - \theta C _ {\mathrm{HIE}} + (1 - \theta) (1 - \epsilon) (2 (1 - \alpha) \delta^ {2} - 2 \delta p _ {1} + p _ {2} ^ {2} \epsilon)} \\ & {\big (\frac {p _ {1} \big (4 (\alpha - 1) \delta^ {2} + 4 (\alpha - 1) \delta p _ {2} \epsilon - p _ {2} ^ {2} \epsilon \big) + 4 \delta \tau_ {1} (\delta + 2 p _ {2} \epsilon) + 4 p _ {1} ^ {2} (\delta + p _ {2} \epsilon)}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}}} \\ & {+ (\theta \delta + 2 p _ {2} \epsilon) \Big (\frac {4 \delta p _ {1} \big (2 (\alpha - 1) \delta^ {2} - p _ {2} ^ {2} \epsilon \big) + 4 \delta^ {2} p _ {1} ^ {2}}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}} + \frac {p _ {2} \epsilon \big (- 8 (\alpha - 1) ^ {2} \delta^ {3} - 4 (\alpha - 1) \delta^ {2} p _ {2} + p _ {2} ^ {3} \epsilon \big) + 8 \delta^ {2} \tau_ {1} (\delta + 2 p _ {2} \epsilon)}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}} \Big) \Big),} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{P}} (\mathrm{H}, \mathrm{H}) = \ddot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) := - (1 - \theta) C _ {\mathrm{HIE}} + (\theta) (1 - \epsilon) (2 (1 - \alpha) \delta^ {2} - 2 \delta p _ {1} + p _ {2} ^ {2} \epsilon)} \\ & {\big (\frac {p _ {1} \big (4 (\alpha - 1) \delta^ {2} + 4 (\alpha - 1) \delta p _ {2} \epsilon - p _ {2} ^ {3} \epsilon \big) + 4 \delta \tau_ {1} (\delta + 2 p _ {2} \epsilon) + 4 p _ {1} ^ {2} (\delta + p _ {2} \epsilon)}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}}} \\ & {+ ((1 - \theta) \delta + 2 p _ {2} \epsilon) \Big (\frac {4 \delta p _ {1} \big (2 (\alpha - 1) \delta^ {2} - p _ {2} ^ {3} \epsilon \big) + 4 \delta^ {2} p _ {1} ^ {2}}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}} + \frac {p _ {2} \epsilon \big (- 8 (\alpha - 1) ^ {2} \delta^ {3} - 4 (\alpha - 1) \delta^ {2} p _ {3} + p _ {3} ^ {3} \epsilon \big) + 8 \delta^ {2} \tau_ {1} (\delta + 2 p _ {2} \epsilon)}{8 \delta^ {2} (\delta + 2 p _ {2} \epsilon) ^ {2}} \Big) \Big).} \end{array}\tag{99}
$$

We use $p _ { 1 } ^ { * } , p _ { 2 } ^ { * }$ , and $\tau ^ { \mathrm { P * } }$ to denote the optimal parameter values when $\mu < \mu ^ { \mathrm { P } } ( \mathrm { N } , \mathrm { N } )$ and $C _ { \mathrm { H I E } } \geq \tilde { C } _ { H I E }$ . Define a threshold, $C _ { 1 }$ such that $\hat { \pi } _ { A } ^ { F } ( \mathbb { N } , \mathbb { N } ) | _ { p _ { 1 } = p _ { 1 } ^ { * } , p _ { 2 } = p _ { 2 } ^ { * } , r ^ { \mathbb { P } } = \mathbb { r } ^ { * } , C _ { \mathrm { H L E } } = C _ { 1 } } = m a x [ \hat { \pi } _ { A } ^ { F } ( \mathbb { H } , \mathbb { H } ) | _ { p _ { 1 } = p _ { 1 } ^ { * } , p _ { 2 } = p _ { 2 } ^ { * } , r ^ { \mathbb { P } } = \mathbb { r } ^ { * } , C _ { \mathrm { H E } } = C _ { 1 } } , \hat { \pi } _ { A } ^ { F } ( \mathbb { H } , \mathbb { H } ) | _ { p _ { 1 } = p _ { 1 } ^ { * } , p _ { 2 } = p _ { 2 } ^ { * } , r ^ { \mathbb { P } } = \mathbb { r } ^ { * } , C _ { \mathrm { H E } } = C _ { 1 } } ]$ (100)

Define another threshold, $C _ { 2 }$ such that

$$
\dot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {2}} = m a x [ \dot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {2}}, \ddot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {2}} ].\tag{101}
$$

We now use $p _ { 1 } ^ { * } , p _ { 2 } ^ { * }$ , and $\tau ^ { \mathrm { P * } }$ to denote the optimal parameter values when $\mu \geq \mu ^ { \mathrm { P } } ( \mathrm { N } , \mathrm { N } )$ and $C _ { \mathrm { H I E } } \geq \tilde { C } _ { H I E }$ . Let us define a threshold, $C _ { 3 }$ such that

$$
\ddot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {3}} = m a x [ \dot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {3}}, \ddot {\pi} _ {A} ^ {P} \mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {3}} ]\tag{102}
$$

We define another threshold, $C _ { 4 }$ such that

$$
\ddot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {4}} = m a x [ \dot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {4}}, \ddot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {4}} ].\tag{103}
$$

We set

$$
\tilde {C} _ {H I E} := \max [ C _ {1}, C _ {2}, C _ {3}, C _ {4} ].\tag{104}
$$

Sufficient Conditions for HIE adoption: Suppose there exists a threshold, $\dot { C } _ { H I E }$ , such that the providers adopt HIE if $C _ { \mathrm { H I E } } \leq \dot { C } _ { H I E }$ . We use $p _ { 1 } ^ { * } , p _ { 2 } ^ { * }$ , and $\tau ^ { \mathrm { P * } }$ to denote the optimal parameter values when $\mu < \mu ^ { \mathrm { p } } ( \mathrm { H } , \mathrm { H } )$ and $C _ { \mathrm { H I E } } \leq \dot { C } _ { H I E } .$ . Define a threshold, $C _ { 5 }$ such that

$$
\dot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {5}} = m a x [ \dot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {5}}, \ddot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {5}} ]\tag{105}
$$

Define another threshold, $C _ { 6 }$ such that

$$
\dot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {6}} = m a x [ \dot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {6}}, \ddot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {6}} ].\tag{106}
$$

Let us now use $p _ { 1 } ^ { * } , p _ { 2 } ^ { * } .$ , and $\tau ^ { \mathrm { P * } }$ to denote the optimal parameter values when $\mu \geq \mu ^ { \mathrm { P } } ( \mathrm { N } , \mathrm { N } )$ and $C _ { \mathrm { H I E } } < \tilde { C } _ { H I E }$ . Let us define a threshold, $C _ { 7 }$ such that

$$
\ddot {\pi} _ {A} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {7}} = m a x [ \dot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {7}}, \ddot {\pi} _ {A} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {7}} ]\tag{107}
$$

Let us define another threshold, $C _ { 8 }$ such that

$$
\ddot {\pi} _ {B} ^ {P} (\mathrm{H}, \mathrm{H}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {8}} = m a x [ \dot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {8}}, \ddot {\pi} _ {B} ^ {P} (\mathrm{N}, \mathrm{N}) | _ {p _ {1} = p _ {1} ^ {*}, p _ {2} = p _ {2} ^ {*}, \tau^ {\mathrm{P}} = \tau^ {\mathrm{P} *}, C _ {\mathrm{HIE}} = C _ {8}} ].
$$

We set

(108)

$$
\dot {C} _ {H I E} := m i n [ C _ {5}, C _ {6}, C _ {7}, C _ {8} ].\tag{109}
$$

Finally we define,

$$
\overline {{C}} _ {H I E} ^ {\mathrm{P}} := \left\{ \begin{array}{l l} \tilde {C} _ {H I E}, & \text {if} C _ {\mathrm{HIE}} \geq m a x [ C _ {1}, C _ {2}, C _ {3}, C _ {4} ], \\ \dot {C} _ {H I E}, & \text {if} C _ {\mathrm{HIE}} \leq m i n [ C _ {5}, C _ {6}, C _ {7}, C _ {8} ]. \end{array} \right.\tag{110}
$$

## Proof of Proposition 2

Part (i) and (ii) can be obtained simply by substituting $p _ { 1 }$ and $p _ { 2 }$ with the optimal contract parameters into the optimal effort levels we obtained in the analysis of Stage 5 and Stage 4. For part $( \mathrm { i i i } )$ , suppose to the contrary that P4P payment model can induce the first best solutions when patients switch. This implies that for $( S _ { \mathrm { { A } } } , S _ { \mathrm { { B } } } ) = ( \mathrm { { H } , \mathrm { { H } ) } }$ there exist $p _ { 1 }$ and $p _ { 2 }$ such that

$$
\frac {2 \delta p _ {1} - p _ {2} \epsilon (4 (\alpha - 1) \delta + p _ {2})}{4 \delta (\delta + 2 p _ {2} \epsilon)} = e _ {i 0} ^ {F B *}, \frac {2 \delta p _ {1} - p _ {2} \epsilon (4 (\alpha - 1) \delta + p _ {2})}{4 \delta (\delta + 2 p _ {2} \epsilon)} = \hat {e} _ {i 0} ^ {F B *} \neq e _ {i 0} ^ {F B *},
$$

$$
\frac {p _ {1}}{2 \delta} = \hat {e} _ {i (- i)} ^ {F B *} = \frac {u _ {L} - \mu}{2 \delta}, \frac {p _ {2}}{2 \delta} = \hat {e} _ {i i} ^ {F B *} = \frac {u _ {H}}{2 \delta}, \forall i \in \{A, B \},\tag{111}
$$

where $e _ { i j } ^ { F B * } \forall i , j$ denotes the optimal efforts under the first best. Suppose to the contrary that there exist $\pmb { p _ { 1 } }$ and ${ \pmb p } _ { 2 }$ that induce the firstbest effort levels. Then, ${ \pmb p } _ { 1 } ^ { * } = { \pmb u } _ { L } - { \pmb \mu }$ and ${ \pmb p } _ { 2 } ^ { * } = { \pmb u } _ { H }$ must hold. Substituting $\pmb { p _ { 1 } ^ { * } }$ and $\pmb { p } _ { 2 } ^ { * }$ respectively for $\pmb { p _ { 1 } }$ in in $\frac { 2 \delta p _ { 1 } - p _ { 2 } \epsilon ( 4 ( \alpha - 1 ) \delta + p _ { 2 } ) } { 4 \delta ( \delta + 2 p _ { 2 } \epsilon ) }$ and $\pmb { p } _ { 2 } \mathrm { i n } \frac { 2 \delta p _ { 1 } - p _ { 2 } \epsilon ( 4 ( \alpha - 1 ) \delta + p _ { 2 } ) } { 4 \delta ( \delta + 2 p _ { 2 } \epsilon ) }$ do not satisfy $\begin{array} { r } { \frac { 2 \delta p _ { 1 } - p _ { 2 } \epsilon ( 4 ( \alpha - 1 ) \delta + p _ { 2 } ) } { 4 \delta ( \delta + 2 p _ { 2 } \epsilon ) } = e _ { i 0 } ^ { F B * } \mathrm { ~ a n d ~ } \frac { 2 \delta p _ { 1 } - p _ { 2 } \epsilon ( 4 ( \alpha - 1 ) \delta + p _ { 2 } ) } { 4 \delta ( \delta + 2 p _ { 2 } \epsilon ) } = \hat { e } _ { i 0 } ^ { F B * } } \end{array}$ <sup>∗</sup>, which is a contradiction.

## Proof of Proposition 3

The EBP contract should induce the benchmark efforts as in the first-best solution with the desired HIE adoption and patient switching scenario as in Lemma 4. We derive the optimal solution for the desired scenario using contract parameters of the EBP model and then ensure the desired HIE adoption and patient switching scenario. For each desired HIE adoption and patient switching scenario, we use $e _ { i j } ^ { * } \forall i , j$ to denote the corresponding first-best effort levels.

$\pmb { C } _ { H I E } \geq \overline { { \pmb { C } } } _ { H I E }$ and $\pmb { \mu } \le \pmb { \mu } _ { N N }$

Suppose HIE is not adopted.

Stage 5. We solve the simultaneous equations given by

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (A, B),\tag{112}
$$

$$
\frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (B, A),\tag{113}
$$

which leads to the following results:

$$
e _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}, \hat {e} _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}
$$

$$
e _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}, \hat {e} _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}\tag{114}
$$

(115)

We let $P _ { 2 N S } = P _ { 2 C S } - 2 \delta e _ { i i } ^ { * }$ and $P _ { 2 C D } = P _ { 2 N D }$ , and find

$$
e _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta} = \hat {e} _ {i i} ^ {*}\tag{116}
$$

$$
e _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta} = 0, \hat {e} _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta} = 0\tag{117}
$$

Stage 3. Suppose all the patients return to the same provider for the second visit. We solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \}.\tag{118}
$$

Substituting $P _ { 2 N S } = P _ { 2 C S } - 2 \delta e _ { i i } ^ { * }$ in equations (118) gives the following results.

$$
e _ {i 0} = e _ {i 0} ^ {*} = \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*}, \forall i \in \{\mathrm{A,B} \}\tag{119}
$$

The corresponding providers’ expected future payoffs then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := (1 - \theta) \big (8 e _ {i 0} ^ {* 2} b \delta + 2 e _ {i 0} ^ {* 2} \delta + 2 e _ {i i} ^ {* 2} \delta - 2 e _ {i i} ^ {*} \delta + P _ {2 \mathrm{CS}} + \tau_ {1} + \tau_ {2} \big),} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := (\frac {1}{\theta} - 1) \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}),} \end{array}\tag{120}
$$

where $\dot { \pi } _ { i } ^ { \mathrm { E } } ( \mathsf { N } , \mathsf { N } )$ denotes the provider’s expected future payoff evaluated under no patient switching.

Stage 4. We choose zero values for the free variables relevant to the patient switching scenario. Given the contract parameter values we have found, the patient does not switch for the second visit regardless of HIE adoption decision since $V _ { i i y } ^ { \mathbf { P } } \geq V _ { ( - i ) i y } ^ { \mathbf { P } }$

Stage 2. To induce no HIE adoption, we need to choose parameter values for the free variables which can give the providers greater utility under no HIE adoption than that under HIE adoption. Given the parameter values we have found, we solve the providers optimization problem for the scenario where HIE is adopted and the patient returns to the same provider. Therefore, we reexamine the solutions under HIE adoption starting with Stage 5 problem and make the welfare comparison under HIE adoption and no HIE adoption cases.

In Stage 5, we solve the simultaneous equations given by

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \}.\tag{121}
$$

which gives the following results:

$$
e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}.\tag{122}
$$

In Stage 3, we solve the simultaneous equations given by

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \},\tag{123}
$$

which leads to the following results:

$$
e _ {i i} = \hat {e} _ {i i} = e _ {i 0} ^ {*} - \frac {2 \alpha e _ {i i} ^ {*}}{4 e _ {i i} ^ {*} + 1}.\tag{124}
$$

The corresponding providers’ expected future payoffs then becomes

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := \frac {\alpha \theta (8 e _ {i 0} ^ {*} e _ {i i} ^ {*} \delta + 2 e _ {i 0} ^ {*} \delta)}{4 e _ {i i} ^ {*} + 1} - \frac {2 \alpha^ {2} e _ {i i} ^ {*} \delta \theta}{4 e _ {i i} ^ {*} + 1} - \theta C _ {\mathrm{HIE}}} \\ & {+ \frac {\theta (3 2 e _ {i 0} ^ {* 2} e _ {i i} ^ {* 2} \delta + 1 6 e _ {i 0} ^ {* 2} e _ {i i} ^ {*} \delta + 2 e _ {i 0} ^ {* 2} \delta + 8 e _ {i i} ^ {* 3} \delta - 6 e _ {i i} ^ {* 2} \delta + (4 e _ {i i} ^ {*} + 1) P _ {2 C S})}{4 e _ {i i} ^ {*} + 1}} \\ & {+ \frac {\theta (- 2 e _ {i i} ^ {*} \delta + 4 e _ {i i} ^ {*} \tau_ {1} + 4 e _ {i i} ^ {*} \tau_ {2} + \tau_ {1} + \tau_ {2})}{4 e _ {i i} ^ {*} + 1},} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := (\frac {1}{\theta} - 1) \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}).} \end{array}\tag{125}
$$

Comparing $\dot { \pi } _ { i } ^ { \mathrm { E } } ( \mathrm { H } , \mathrm { H } )$ and $\dot { \pi } _ { i } ^ { \mathrm { E } } ( \mathsf { N } , \mathsf { N } )$ for ∀?? gives

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) \geq \dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) \mathrm{ifandonlyif} C _ {\mathrm{HIE}} \geq - \frac {\alpha \theta U (2 (\alpha - 2) \delta + U)}{2 (\delta + 2 U)} = \overline {{C}} _ {H I E}\tag{126}
$$

We let $\tau _ { 1 } ^ { \mathrm { E } } = \dot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathrm { N } , \mathrm { N } )$ where $\dot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathsf { N } , \mathsf { N } )$ is a value such that

$$
\dot {\tau} _ {1} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = m a x [ \dot {\tau} _ {A} ^ {E} (\mathrm{N}, \mathrm{N}), \dot {\tau} _ {B} ^ {E} (\mathrm{N}, \mathrm{N}) ],\tag{127}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) | _ {\tau_ {1} ^ {\mathrm{E}} = \dot {\tau} _ {i} ^ {E} (\mathrm{N}, \mathrm{N})} = \omega_ {i}, \forall i \in \{A, B \}.\tag{128}
$$

Finally, we choose zero values for the free variables.

$\pmb { C } _ { H I E } \geq \overline { { \pmb { C } } } _ { H I E }$ and $\pmb { \mu } > \pmb { \mu } _ { N N }$

Suppose that HIE is not adopted.

Stage 5. We solve the simultaneous equations given by

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \},\tag{129}
$$

$$
\frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \},\tag{130}
$$

which leads to the following results:

$$
e _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}, \hat {e} _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}\tag{131}
$$

$$
e _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}, \hat {e} _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}\tag{132}
$$

We let $P _ { 2 N D } \colon = P _ { 2 C D } - 2 e _ { i ( - i ) } ^ { \ast } \delta$ and $P _ { 2 N S } \mathrm { : } = P _ { 2 C S } - 2 e _ { i i } ^ { \ast } \delta$ , and find

$$
e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}, e _ {i (- i)} = e _ {i (- i)} ^ {*}, \hat {e} _ {i (- i)} = \hat {e} _ {i (- i)} ^ {*}\tag{133}
$$

Stage 3. We solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \},\tag{134}
$$

Substituting $P _ { 2 N D } \colon = P _ { 2 C D } - 2 e _ { i ( - i ) } ^ { \ast } \delta$ and $P _ { 2 N S } \mathrm { : } = P _ { 2 C S } - 2 e _ { i i } ^ { \ast } \delta$ in equations (134) gives the following results:

$$
\begin{array}{r l} & {e _ {i 0} = \hat {e} _ {i 0} =} \\ & {- \frac {- 2 e _ {i (- i)} ^ {*} (\epsilon - 1) P _ {C D} + (2 e _ {i (- i)} ^ {*} - 1) (\epsilon - 1) P _ {1 N D} - P _ {C} + \epsilon P _ {2 C S} + 2 (e _ {i i} ^ {*} - 2) e _ {i i} ^ {*} \delta \epsilon + \tau_ {2} \epsilon}{2 (4 e _ {i i} ^ {*} \delta \epsilon + \delta)},} \\ & {\forall i \in \{A, B \}.} \end{array}\tag{135}
$$

We let $P _ { 1 c } = \tilde { P } _ { 1 c } ( \mathrm { N } , \mathrm { N } ) : = 2 \delta ( e _ { i i } ^ { * } \epsilon ( 4 e _ { i 0 } ^ { * } + e _ { i i } ^ { * } - 2 ) + e _ { i 0 } ^ { * } ) - 2 e _ { i ( - i ) } ^ { * } ( \epsilon - 1 ) P _ { 1 c D } + ( 2 e _ { i ( - i ) } ^ { * } - 1 ) ( \epsilon - 1 ) P _ { 1 N D } + \epsilon P _ { 2 c S } + \tau _ { 2 } e _ { i 0 } ^ { * } ,$ , and find

$$
e _ {i 0} = \hat {e} _ {i 0} = e _ {i 0} ^ {*} = \hat {e} _ {i 0} ^ {*}, \forall i \in \{A, B \}.\tag{136}
$$

The corresponding expected future payoffs for providers then becomes

$$
\begin{array} { r l } &  \overline { { \pi } } _ { A } ^ { \mathrm{E} } ( \mathrm{N} , \mathrm{N} ) = \ddot { \pi } _ { A } ^ { \mathrm{E} } ( \mathrm{N} , \mathrm{N} ) : = ( 1 - \epsilon ) ( 4 e _ { i 0 } ^ { * 2 } \delta \theta + 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * 2 } \delta \theta - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * 2 } \delta - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \delta \theta ) \\ &  + ( 1 - \epsilon ) ( + 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \delta - 2 e _ { i ( - i ) } ^ { * 2 } \delta \theta + 2 e _ { i ( - i ) } ^ { * 2 } \delta + 2 e _ { i ( - i ) } ^ { * } \delta \theta - 2 e _ { i ( - i ) } ^ { * } \delta - 2 e _ { i i } ^ { * } \delta \theta - 8 e _ { i 0 } ^ { * 2 } e _ { i i } ^ { * } \delta \theta ) \\ &  + ( 1 - \epsilon ) \big ( + 3 2 e _ { i 0 } ^ { * 2 } e _ { i i } ^ { * } \delta \theta \epsilon - 4 e _ { i 0 } ^ { * } e _ { i i } ^ { * 2 } \delta \theta + 8 e _ { i 0 } ^ { * } e _ { i i } ^ { * 2 } \delta \theta \epsilon + 8 e _ { i 0 } ^ { * } e _ { i i } ^ { * } \delta \theta - 1 6 e _ { i 0 } ^ { * } e _ { i i } ^ { * } \delta \theta \epsilon + 2 e _ { i i } ^ { * 2 } \delta \theta \big ) \\ &  + 2 e _ { i ( - i ) } ^ { * } \theta ( 1 - \epsilon ) ( e _ { i 0 } ^ { * } ( 2 - 4 \epsilon ) + 1 ) P _ { 1 C D } + ( 2 e _ { i 0 } ^ { * } - 1 ) ( \theta - 1 ) ( 1 - \epsilon ) P _ { 2 C D } \\ &  + ( 1 - \epsilon ) P _ { 1 N D } ( - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \theta + 8 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \theta \epsilon + 2 e _ { i 0 } ^ { * } \theta - 4 e _ { i 0 } ^ { * } \theta \epsilon - 2 e _ { i ( - i ) } ^ { * } \theta + \theta ) \\ &  + ( 1 - \epsilon ) P _ { 2 C S } ( - 2 e _ { i 0 } ^ { * } \theta + 4 e _ { i 0 } ^ { * } \theta \epsilon + \theta ) \\ &  + \tau _ { 1 } + ( 1 - \epsilon ) ( 2 e _ { i 0 } ^ { * } \theta - 2 e _ { i 0 } ^ { * } + \theta + 1 ) + \tau _ { 2 } ( 1 - \epsilon ) ( - 2 e _ { i 0 } ^ { * } \theta + 4 e _ { i 0 } ^ { * } \theta \epsilon + \theta ) , \\ &  \overline { { \pi } } _ { B } ^ { \mathrm{E} } ( \mathrm{N} , \mathrm{N} ) = \ddot { \pi } _ { B } ^ { \mathrm{E} } ( \mathrm{N} , \mathrm{N} ) : = ( 1 - \epsilon ) ( 4 e _ { i 0 } ^ { * 2 } \delta \tilde { \theta } + 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * 2 } \delta \tilde { \theta } - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * 2 } \delta - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \delta \tilde { \theta } ) \\ &  + ( 1 - \epsilon ) ( + 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \delta - 2 e _ { i ( - i ) } ^ { * 2 } \delta \tilde { \theta } + 2 e _ { i ( - i ) } ^ { * 2 } \delta + 2 e _ { i ( - i ) } ^ { * } \delta \tilde { \theta } - 2 e _ { i ( - i ) } ^ { * } \delta - 2 e _ { i i } ^ { * } \delta \tilde { \theta } - 8 e _ { i 0 } ^ { * 2 } e _ { i i } ^ { * } \delta \tilde { \theta }) \\ &  + ( 1 - \epsilon ) \big ( + 3 2 e _ { i 0 } ^ { * 2 } e _ { i i } ^ { * } \delta \tilde { \theta } \epsilon - 4 e _ { i 0 } ^ { * } e _ { i i } ^ { * 2 } \delta \tilde { \theta } + 8 e _ { i 0 } ^ { * } e _ { i i } ^ { * 2 } \delta \tilde { \theta } \epsilon + 8 e _ { i 0 } ^ { * } e _ { i i } ^ { * } \delta \tilde { \theta } - 1 6 e _ { i 0 } ^ { * } e _ { i i } ^ { * } \delta \tilde { \theta } \epsilon + 2 e _ { i i } ^ { * 2 } \delta \tilde { \theta } \big ) \\ &  + 2 e _ { i ( - i ) } ^ { * } \tilde { \theta } ( 1 - \epsilon ) ( e _ { i 0 } ^ { * } ( 2 - 4 \epsilon ) + 1 ) P _ { 1 C D } + ( 2 e _ { i 0 } ^ { * } - 1 ) ( \tilde { \theta } - 1 ) ( 1 - \epsilon ) P _ { 2 C D } \\ &  + ( 1 - \epsilon ) P _ { 1 N D } ( - 4 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \tilde { \theta } + 8 e _ { i 0 } ^ { * } e _ { i ( - i ) } ^ { * } \tilde { \theta } \epsilon + 2 e _ { i 0 } ^ { * } \tilde { \theta } - 4 e _ { i 0 } ^ { * } \tilde { \theta } \epsilon - 2 e _ { i ( - i ) } ^ { * } \tilde { \theta } + \tilde { \theta }) \\ & + ( 1 - \epsilon ) P _ {\mathrm{2CS}} ( - 2 e _ { i 0 } ^ { * } \tilde { \theta } + 4 e _ { i 0 } ^ { * } \tilde { \theta } \epsilon + \tilde { \theta }) \\ & + \tau _ { 1 } + ( 1 - \epsilon ) ( 2 e _ {\mathrm{i} o} ^ {\ast} \tilde {\theta} - 2 e _ {\mathrm{i} o} ^ {\ast} + \tilde {\theta} + 1 ) + \tau _ { 2 } ( 1 - \epsilon ) ( - 2 e _ {\mathrm{i} o} ^ {\ast} \tilde {\theta} + 4 e _ {\mathrm{i} o} ^ {\ast} \tilde {\theta} \epsilon + \tilde {\theta}) , . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\tag{137}
$$

where $\ddot { \pi } _ { i } ^ { \mathrm { E } } ( \mathsf { N } , \mathsf { N } )$ denotes the provider’s expected future payoff evaluated under patient switching and no HIE adoption.

Stage 4. To induce switching of providers, we need to choose parameter values for the free variables which can give the providers greater utility under switching. Given the parameter values we have found, we solve the providers’ optimization problem for the scenario where the low-type patients switch their providers for the second visit. Therefore, we reexamine the solutions when low type patients switch under no HIE adoption starting with Stage 5 problem and make the welfare comparison between switching and no switching cases.

Solving the first order conditions in Stage 5 gives

$$
e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}.\tag{138}
$$

We set

$$
\begin{array}{r l} {P _ {1 C D}} & {= \ddot {P} _ {1 C D} (\mathrm{N}, \mathrm{N}) := \frac {2 e _ {i 0} ^ {*} \delta - 2 \tilde {e} \delta - 4 \tilde {e} u _ {H} + 2 \delta e _ {i i} ^ {* 2} - 4 \delta e _ {i i} ^ {*} \epsilon - 2 e _ {i i} ^ {*} u _ {H} + 2 u _ {H}}{2 e _ {i (- i)} ^ {*} (\epsilon - 1)}} \\ & {+ \frac {8 e _ {i 0} ^ {*} \delta e _ {i i} ^ {*} \epsilon + (2 e _ {i (- i)} ^ {*} - 1) (\epsilon - 1) P _ {1 N D} + (\epsilon - 1) P _ {2 C S} + 2 \delta e _ {i i} ^ {* 2} \epsilon - \tau_ {2} + \tau_ {2} \epsilon}{2 e _ {i (- i)} ^ {*} (\epsilon - 1)},} \end{array}
$$

$$
\tilde {e} = - \frac {U (U - 4 \delta)}{4 \delta (\delta + 2 U)}.
$$

Then, solving the first order conditions in Stage 3 gives

$$
e _ {i 0} = \tilde {e}, \hat {e} _ {i 0} = \tilde {e}.\tag{139}
$$

The corresponding expected future payoffs for providers then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \theta (u _ {H} (4 \tilde {e} ^ {2} + 2 e _ {i i} ^ {*} - 1) + 2 \delta (\tilde {e} - e _ {i i} ^ {*}) (\tilde {e} + e _ {i i} ^ {*}) + P _ {2 C S} + \tau_ {1} + \tau_ {2}),} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \frac {1 - \theta}{\theta} \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}),} \end{array}\tag{140}
$$

We let $\tilde { P } _ { 2 c s } ( \Nu , \Nu )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {P} _ {2 C S} (\mathrm{N}, \mathrm{N}) = m i n [ \tilde {P} _ {2 C S A}, \tilde {P} _ {2 C S B} ],\tag{141}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) | _ {P _ {2 C S} = \tilde {P} _ {2 C S i}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.\tag{142}
$$

Stage 2. To induce no HIE adoption, we need to choose parameter values for the free variables which can give the providers greater utility under no HIE adoption. Given the parameter values we have found, we solve the providers’ optimization problem for the scenario where HIE is adopted and the patient switches to the different provider. Therefore, we reexamine the solutions under HIE adoption starting with Stage 5 problem and make the welfare comparison under HIE adoption and no HIE adoption cases.

In Stage 5, we solve the following simultaneous equations.

$$
\begin{array}{r} \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \}, \\ \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \} \end{array}\tag{143}
$$

which gives the following results:

$$
e _ {i (- i)} = e _ {i (- i)} ^ {*}, \hat {e} _ {i (- i)} = \hat {e} _ {i (- i)} ^ {*}, e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}.\tag{144}
$$

Suppose first that the low type patients do not switch their providers for the second visit. In Stage 3, we solve the following simultaneous equations:

Ayvaci et al. / Designing Payment Contracts for Healthcare Services to Induce Information Sharing

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (\mathrm{A,B}).\tag{145}
$$

Solving the simultaneous equations, we get the following results:

$$
e _ {i 0} = \hat {e} _ {i 0} = \tilde {e} - \frac {\alpha u _ {H}}{\delta + 2 u _ {H}}, \forall i \in \{A, B \}.\tag{146}
$$

The corresponding expected future payoffs of provider A and B then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := \frac {\theta (2 \delta^ {2} (b (\alpha + b) - d ^ {2}) + (\delta + 2 u _ {H}) (P _ {2 \mathrm{CS}} + \tau_ {1} + \tau_ {2}))}{\delta + 2 u _ {H}}} \\ & {+ \frac {\theta (2 \delta^ {2} (b (\alpha + b) - d ^ {2}) + (\delta + 2 u _ {H}) (P _ {2 \mathrm{CS}} + \tau_ {1} + \tau_ {2}))}{\delta + 2 u _ {H}} - \theta C _ {\mathrm{HIE}},} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := \frac {1 - \theta}{\theta} \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}).} \end{array}\tag{147}
$$

We let $\tilde { P } _ { 2 C S } ( \mathrm { H } , \mathrm { H } )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {P} _ {2 C S} (\mathrm{H}, \mathrm{H}) = m i n [ \tilde {P} _ {2 C S _ {A}}, \tilde {P} _ {2 C S _ {B}} ],\tag{148}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) | _ {P _ {2 C S} = \tilde {P} _ {2 C S _ {i}}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.\tag{149}
$$

Suppose next that the low type patients switch their providers for the second visit. In Stage 3, we solve the following simultaneous equations:

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (\mathrm{B,A}).\tag{150}
$$

We set $P _ { 1 N D } = P _ { 1 C D }$ and solve the simultaneous equations, which leads the following.

$$
e _ {i 0} = \hat {e} _ {i 0} = \frac {4 e _ {i 0} ^ {*} e _ {i i} ^ {*} \epsilon + e _ {i 0} ^ {*} - 2 \alpha e _ {i i} ^ {*} \epsilon}{4 e _ {i i} ^ {*} \epsilon + 1}, \forall i \in \{A, B \}.\tag{151}
$$

We denote the corresponding utility of provider A and B using $\ddot { \pi } _ { i } ^ { \mathrm { E } } ( \mathrm { H } , \mathrm { H } ) \forall i \in \{ \mathrm { A } , \mathrm { B } \}$ , and we verify that

$$
\frac {\partial \ddot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial P _ {2 C S}} > 0, \forall i \{\mathrm{A,B} \}.\tag{152}
$$

We let $\tilde { \tilde { P } } _ { 2 C S } ( \mathrm { H } , \mathrm { H } )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {\tilde {P}} _ {2 C S} (\mathrm{H}, \mathrm{H}) = m i n [ \tilde {\tilde {P}} _ {2 C S _ {A}}, \tilde {\tilde {P}} _ {2 C S _ {B}} ],\tag{153}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) | _ {P _ {2 C S} = \tilde {P} _ {2 C S _ {i}}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.\tag{154}
$$

We let $P _ { 2 C S } = \ddot { P } _ { 2 C S } ( \mathrm { N } , \mathrm { N } )$ where

$$
\ddot {P} _ {2 C S} (\mathrm{N}, \mathrm{N}) = m i n [ \tilde {P} _ {2 C S} (\mathrm{N}, \mathrm{N}), \tilde {P} _ {2 C S} (\mathrm{H}, \mathrm{H}), \tilde {\tilde {P}} _ {2 C S} (\mathrm{H}, \mathrm{H}) ].\tag{155}
$$

This ensures that the providers do not adopt HIE and the low type patients switch their providers for the second visit.

We let $\tau _ { 1 } ^ { \mathrm { E } } = \ddot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathrm { N } , \mathrm { N } )$ is a value such that

$$
\ddot {\tau} _ {1} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = m a x [ \ddot {\tau} _ {A} ^ {E} (\mathrm{N}, \mathrm{N}), \ddot {\tau} _ {B} ^ {E} (\mathrm{N}, \mathrm{N}) ],\tag{156}
$$

where

$$
\ddot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) | _ {\tau_ {1} ^ {\mathrm{E}} = \ddot {\tau} _ {i} ^ {E} (\mathrm{N}, \mathrm{N})} = \omega_ {i}, \forall i \in \{A, B \}.\tag{157}
$$

Finally, we choose zero values for the free variables.

$\pmb { C } _ { H I E } < \overline { { \pmb { C } } } _ { H I E }$ and $\pmb { \mu } \le \pmb { \mu } _ { H H }$

Suppose that all the patients return to the same provider for the second visit and HIE is adopted.

Stage 5. We solve the simultaneous equations given by

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \},\tag{158}
$$

$$
\frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \},\tag{159}
$$

which leads to the following results:

$$
\begin{array}{r l} & {e _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}, \hat {e} _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}} \\ & {e _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}, \hat {e} _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}} \end{array}\tag{160}
$$

(161)

We let $P _ { 2 N S } = P _ { 2 C S } - 2 e _ { i i } ^ { * } \delta$ and $P _ { 2 C D } = P _ { 2 N D }$ , and find

$$
\begin{array}{r l} & e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} \\ & e _ {i (- i)} = 0, \hat {e} _ {i (- i)} = 0 \end{array}\tag{162}
$$

(163)

Stage 3. We solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \}.\tag{164}
$$

Substituting $P _ { 2 N S } = P _ { 2 C S } - 2 e _ { i i } ^ { * } \delta$ and $P _ { 2 C D } = P _ { 2 N D }$ in equations (164) gives the following results.

$$
e _ {i 0} = \hat {e} _ {i 0} = e _ {i 0} ^ {*} = \hat {e} _ {i 0} ^ {*}, \forall i \in \{A, B \}.\tag{165}
$$

The corresponding providers’ expected future payoffs then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := - \theta C _ {\mathrm{HIE}}} \\ & {+ \theta \big (8 e _ {i 0} ^ {* 2} e _ {i i} ^ {*} \delta + 2 e _ {i 0} ^ {* 2} \delta + 2 \alpha e _ {i 0} ^ {*} \delta + 8 \alpha e _ {i 0} ^ {*} e _ {i i} ^ {*} \delta + 2 e _ {i i} ^ {* 2} \delta + 2 \alpha^ {2} e _ {i i} ^ {*} \delta - 2 e _ {i i} ^ {*} \delta + P _ {2 \mathrm{CS}} + \tau_ {1} + \tau_ {2} \big)} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := (\frac {1}{\theta} - 1) \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}).} \end{array}\tag{166}
$$

Stage 4. We choose zero values for the free variables relevant to the patient switching scenario. Given the contract parameter values we have found, the patient does not switch for the second visit regardless of HIE adoption decision since $V _ { i i y } ^ { \mathbf { P } } \geq V _ { ( - i ) i y } ^ { \mathbf { P } }$

Stage 2. To induce HIE adoption, we need to choose parameter values for the free variables which can give the providers greater utility under HIE adoption. Given the parameter values we have found, we solve the providers’ optimization problem for the scenario where

HIE is not adopted and the patient returns to the same provider. Therefore, we reexamine the solutions under no HIE adoption starting with Stage 5 problem and make the welfare comparison under HIE adoption and no HIE adoption cases.

In Stage 5, we solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \},\tag{167}
$$

which gives

$$
e _ {i i} = e _ {i i} ^ {*} = \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}.\tag{168}
$$

In Stage 3, we solve the following simultaneous equations:

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (A, B),\tag{169}
$$

which gives

$$
e _ {i 0} = \hat {e} _ {i 0} = - \frac {U (U - 4 \delta)}{4 \delta (\delta + 2 U)}.\tag{170}
$$

The corresponding expected future payoffs for providers then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \frac {\theta (U (4 \delta^ {2} U - 8 \delta^ {3} + U ^ {3}))}{8 \delta^ {2} (\delta + 2 U)}} \\ & {+ \frac {\theta (8 \delta^ {2} P _ {2 C S} (\delta + 2 U) + 8 \delta^ {2} \tau_ {1} (\delta + 2 U))}{8 \delta^ {2} (\delta + 2 U)}} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \frac {\widetilde {\theta} (U (4 \delta^ {2} U - 8 \delta^ {3} + U ^ {3}))}{8 \delta^ {2} (\delta + 2 U)}} \\ & {+ \frac {\widetilde {\theta} (8 \delta^ {2} P _ {2 C S} (\delta + 2 U) + 8 \delta^ {2} \tau_ {1} (\delta + 2 U))}{8 \delta^ {2} (\delta + 2 U)}} \end{array}\tag{171}
$$

Comparing $\dot { \pi } _ { i } ^ { \mathrm { E } } ( \mathrm { H } , \mathrm { H } )$ and $\dot { \pi } _ { i } ^ { \mathrm { E } } ( \mathsf { N } , \mathsf { N } )$ for ∀?? gives

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) <   \dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) \mathrm{ifandonlyif} C _ {\mathrm{HIE}} <   - \frac {\alpha U (2 \alpha \delta - 4 \delta + U)}{2 (\delta + 2 U)} = \overline {{C}} _ {H I E}.\tag{172}
$$

We let $\tau _ { 1 } ^ { \mathrm { E } } = \dot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathrm { H } , \mathrm { H } )$ where $\dot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathrm { H } , \mathrm { H } )$ is a value such that

$$
\dot {\tau} _ {1} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = m a x [ \dot {\tau} _ {A} ^ {E} (\mathrm{H}, \mathrm{H}), \dot {\tau} _ {B} ^ {E} (\mathrm{H}, \mathrm{H}) ],\tag{173}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) | _ {\tau_ {1} ^ {\mathrm{E}} = \dot {\tau} _ {i} ^ {E} (\mathrm{H}, \mathrm{H})} = \omega_ {i}, \forall i \in \{A, B \}.\tag{174}
$$

Finally, we choose zero values for the free variable.

$\pmb { C } _ { H I E } < \overline { { \pmb { C } } } _ { H I E }$ and $\pmb { \mu } > \pmb { \mu } _ { H H }$

Suppose the low type patient visits to the different provider for the second visit and HIE is adopted.

Stage 5. We solve the simultaneous equations given by

$$
\begin{array}{r} \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \}, \\ \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \hat {e} _ {i (- i)}} = 0, \forall i \in \{A, B \}, \end{array}\tag{175}
$$

(176)

which leads to the following:

$$
e _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta}, \hat {e} _ {i i} = \frac {(P _ {2 C S} - P _ {2 N S})}{2 \delta},
$$

(177)

$$
e _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}, \hat {e} _ {i (- i)} = \frac {(P _ {2 C D} - P _ {2 N D})}{2 \delta}.\tag{178}
$$

We let $P _ { 2 N D } = P _ { 2 C D } - 2 e _ { i ( - i ) } ^ { * } \delta $ and $P _ { 2 N S } = P _ { 2 C S } - 2 e _ { i i } ^ { * } \delta$ , and find

$$
e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}, e _ {i (- i)} = e _ {i (- i)} ^ {*}, \hat {e} _ {i (- i)} = \hat {e} _ {i (- i)} ^ {*}.\tag{179}
$$

Stage 3. We solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{H,H})}{\partial \dot {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (\mathrm{B,A}),\tag{180}
$$

We substitute $P _ { 2 N D } = P _ { 2 C D } - 2 e _ { i ( - i ) } ^ { * } \delta $ and $P _ { 2 N S } = P _ { 2 C S } - 2 e _ { i i } ^ { * } \delta$ in equations (180), and let

$$
\begin{array}{r l} & P _ {1 C D} = \frac {2 \delta (e _ {i 0} ^ {*} - \hat {e} _ {i 0} ^ {*})}{(\epsilon - 1) (e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1)} + P _ {1 N D}, \\ & P _ {1 C} = \frac {2 \delta \left(- (e _ {i 0} ^ {*}) ^ {2} - \alpha e _ {i 0} ^ {*} + 2 e _ {i 0} ^ {*} \hat {e} _ {i 0} ^ {*} - 2 e _ {i 0} ^ {*} e _ {i (- i)} ^ {*} + (\hat {e} _ {i 0} ^ {*}) ^ {2} + 2 \alpha \hat {e} _ {i 0} ^ {*} + 2 \hat {e} _ {i 0} ^ {*} e _ {i (- i)} ^ {*} - \hat {e} _ {i 0} ^ {*}\right)}{e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1} \\ & + \frac {2 \delta (e _ {i i} ^ {*} \epsilon (e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1) (2 e _ {i 0} ^ {*} + 2 \alpha + 2 \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {*} - 2))}{e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1} + \epsilon (P _ {\mathrm{2CS}} - P _ {\mathrm{ND}} + \tau_ {2}) + P _ {\mathrm{ND}} \end{array}\tag{181}
$$

(182)

Then, equations (180) give

$$
e _ {i 0} = e _ {i 0} ^ {*}, \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*}, \forall i \in \{A, B \}.\tag{183}
$$

The corresponding providers’ expected future payoffs then become

$$
\begin{array} { r l } &  \overline { { \pi } } _ { A } ^ { \mathrm{E} } ( \mathrm{H} , \mathrm{H} ) = \ddot { \pi } _ { A } ^ { \mathrm{E} } ( \mathrm{H} , \mathrm{H} ) : = 2 e _ { i ( - i ) } ^ { * } \delta ( 1 - \theta ) ( 1 - \epsilon ) ( - e _ { i 0 } ^ { * } - \alpha - \hat { e } _ { i 0 } ^ { * } + 1 ) ( e _ { i 0 } ^ { * } + \alpha + e _ { i ( - i ) } ^ { * } - 1 ) \\ & { \frac { 1 } { e _ { i 0 } ^ { * } + \alpha + \hat { e } _ { i 0 } ^ { * } - 1 } ( \delta \big ( e _ { i 0 } ^ { * 3 } ( 2 e _ { i i } ^ { * } \epsilon - 1 ) + \hat { e } _ { i 0 } ^ { * 3 } ( 2 e _ { i i } ^ { * } \epsilon + 1 ) + 2 ( \alpha - 1 ) e _ { i i } ^ { * } \epsilon ( \alpha ^ { 2 } + e _ { i i } ^ { * } - 1 ) } \\ & { ( 3 \alpha - 1 ) + \hat { e } _ { i 0 } ^ { * 2 } ( 2 e _ { i i } ^ { * } \epsilon + 1 ) + 2 \hat { e } _ { i 0 } ^ { * } \big ( 2 e _ { i ( - i ) } ^ { * } + \alpha ^ { 2 } ( 3 e _ { i i } ^ { * } \epsilon + 1 ) - 2 \alpha e _ { i i } ^ { * } \epsilon + ( e _ { i i } ^ { * } - 1 ) e _ { i i } ^ { * } \epsilon \big ) } \\ & { + e _ { i 0 } ^ { * 2 } ( 6 \hat { e } _ { i 0 } ^ { * } e _ { i i } ^ { * } \epsilon + \hat { e } _ { i 0 } ^ { * } + \alpha ( 6 e _ { i i } ^ { * } \epsilon - 1 ) - 2 e _ { i i } ^ { * } \epsilon - 1 ) + e _ { i 0 } ^ { * } ( - 2 \alpha - 4 e _ { i ( - i ) } ^ { * } + 2 ( e _ { i i } ^ { * } - 1 ) e _ { i i } ^ { * } \epsilon } \\ & { \hat { e } _ { i 0 } ^ { * 2 } ( 6 e _ { i i } ^ { * } \epsilon + 3 ) + 4 \hat { e } _ { i 0 } ^ { * } ( \alpha + 3 \alpha e _ { i i } ^ { * } \epsilon - e _ { i i } ^ { * } \epsilon ) + 6 \alpha ^ { 2 } e _ { i i } ^ { * } \epsilon - 4 \alpha e _ { i i } ^ { * } \epsilon ) \Big ) \theta ) - \theta C _ { \mathrm{HIE} } } \\ & { \overline { { \pi } } _ { B } ^ { \mathrm{E} } ( \mathrm{H} , \mathrm{H} ) = \ddot { \pi } _ { B } ^ { \mathrm{E} } ( \mathrm{H} , \mathrm{H} ) : = 2 e _ { i ( - i ) } ^ { * } \tilde { \delta } ( 1 - \theta ) ( 1 - \epsilon ) ( - e _ { i 0 } ^ { * } - \alpha - \hat { e } _ { i 0 } ^ { * } + 1 ) ( e _ { i 0 } ^ { * } + \alpha + e _ { i ( - i ) } ^ { * } - 1 ) } \\ &  \frac { 1 } { e _ { i 0 } ^ { * } + \alpha + \hat { e } _ { i 0 } ^ { * } - 1 } ( \tilde { \delta } \big ( e _ { i 0 } ^ { * 3 } ( 2 e _ { i i } ^ { * } \epsilon - 1 ) + \hat { e } _ { i 0 } ^ { * 3 } ( 2 e _ { i i } ^ { * } \epsilon + 1 ) + 2 ( \alpha - 1 ) e _ { i i } ^ { * } \epsilon ( \alpha ^ {2 } + e _ { i i } ^ { * } - 1 ) \\ & ( 3 \alpha - 1 ) + \hat { e } _ { i 0 } ^ { * 2 } ( 2 e _ { i i } ^ { * } \epsilon + 1 ) + 2 \hat { e } _ { i 0 } ^ { * } \big ( 2 e _ { i ( - i ) } ^ { * } + \alpha ^ { 2 } ( 3 e _ { i i }^{ * }\epsilon + 1 ) - 2 \alpha e _ { i i} ^ { * }\epsilon + ( e _ { i i} ^ { * } - 1 ) e _ { i i} ^ { * }\epsilon \big ) \\ & + e _ { i 0 } ^ { * 2 } ( 6 \hat { e } _ { i 0 } ^ { * } e _ { i i} ^ { * }\epsilon + \hat { e } _ { i 0 } ^ { * } + \alpha ( 6 e _ { i i} ^ {* }\epsilon - 1 ) - 2 e _ { i i} ^ {*} \epsilon - 1 ) + e _ { i 0 } ^ { * } ( - 2 \alpha - 4 e _ { i ( - i ) } ^ {*} + 2 ( e _ {i i} ^ {*} - 1 ) e _ {i i} ^ {*} \epsilon \\ & \hat { e } _ { i 0 } ^ { * 2 } ( 6 e _ { i i} ^ {* }\epsilon + 3 ) + 4 \hat { e } _ { i 0 } ^ { * }( \alpha + 3 \alpha e _ { i i} ^ {* }\epsilon - e _ {i i} ^ {* }\epsilon ) + 6 \alpha ^ { 2 } e _ { i i} ^ {* }\epsilon - 4 \alpha e _ {i i} ^ {* }\epsilon ) \Big ) \tilde {\theta}) - \tilde {\theta} C _ {\mathrm{HIE} .} . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .\tag{184}
$$

Stage 4. To induce switching of providers, we need to choose parameter values for the free variables which can give the providers greater utility under switching. Given the parameter values we have found, we solve the providers’ optimization problem for the scenario where the low-type patients switch their providers for the second visit. Therefore, we reexamine the solutions when low type patients switch under HIE adoption starting with Stage 5 problem and make the welfare comparison between switching and switchin cases.

We set

$$
\begin{array}{r l} & P _ {1 N D} = \ddot {P} _ {1 N D} (\mathrm{H}, \mathrm{H}) \\ & := \frac {(4 e _ {i i} ^ {*} + 1) \delta}{- 1 + \epsilon} \bigg (- \frac {2 (e _ {i 0} ^ {* 2} - \hat {e} _ {i 0} ^ {* 2} - 2 \hat {e} _ {i 0} ^ {*} e _ {i (- i)} ^ {*} + (\alpha - 1) e _ {i i} ^ {*} (2 \alpha + e _ {i i} ^ {*} - 2))}{(4 e _ {i i} ^ {*} + 1) (e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1)} - \frac {2 \tilde {e}}{\epsilon - 1} \\ & - \frac {2 (e _ {i 0} ^ {*} (\alpha - 2 \hat {e} _ {i 0} ^ {*} + 2 e _ {i (- i)} ^ {*} + e _ {i i} ^ {*} (2 \alpha + e _ {i i} ^ {*} - 2)) + \hat {e} _ {i 0} ^ {*} (e _ {i i} ^ {*} - 1) (2 \alpha + e _ {i i} ^ {*} - 1))}{(4 e _ {i i} ^ {*} + 1) (e _ {i 0} ^ {*} + \alpha + \hat {e} _ {i 0} ^ {*} - 1)} \\ & + \frac {2 e _ {i i} ^ {*} \epsilon (2 e _ {i 0} ^ {*} + 2 \alpha + 2 \hat {e} _ {i 0} ^ {*} + e _ {i i} ^ {*} - 2)}{4 e _ {i i} ^ {*} + 1} + \frac {(\epsilon - 1) P _ {2 C S}}{4 e _ {i i} ^ {*} \delta + \delta} + \frac {\tau_ {2} (\epsilon - 1)}{4 e _ {i i} ^ {*} \delta + \delta} \bigg), \\ & \tilde {e} = - \frac {U (4 (\alpha - 1) \delta + U)}{4 \delta (\delta + 2 U)}. \end{array}\tag{185}
$$

Then, solving the first order conditions in Stage 3 gives

Ayvaci et al. / Designing Payment Contracts for Healthcare Services to Induce Information Sharing

$$
e _ {i 0} = \tilde {e}, \hat {e} _ {i 0} = \tilde {e}.\tag{186}
$$

The corresponding expected future payoffs for providers then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := \theta (P _ {2 C S} + 2 \delta ((e _ {i i} ^ {*}) ^ {2} + e _ {i i} ^ {*} (\alpha + 2 \tilde {e} - 1) (\alpha + 2 \tilde {e} + 1) + \tilde {e} (\alpha + \tilde {e}))} \\ & {+ \tau_ {1} + \tau_ {2} - C _ {\mathrm{HIE}}),} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) := \frac {1 - \theta}{\theta} \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}),} \end{array}\tag{187}
$$

We let $\tilde { P } _ { 2 C S } ( \mathrm { H } , \mathrm { H } )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {P} _ {2 C S} (\mathrm{H}, \mathrm{H}) = m i n [ \tilde {P} _ {2 C S _ {A}}, \tilde {P} _ {2 C S _ {B}} ],\tag{188}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) | _ {P _ {2 C S} = \tilde {P} _ {2 C S _ {i}}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.\tag{189}
$$

Stage 2. To induce HIE adoption, we need to choose parameter values for the free variables which can give the providers greater utilit under HIE adoption. Given the parameter values we have found, we solve the providers’ optimization problem for the scenario where HIE is not adopted and the patient switches to the different provider. Therefore, we reexamine the solutions under HIE adoption starting with Stage 5 problem and make the welfare comparison under HIE adoption and no HIE adoption cases.

In Stage 5, we solve the following simultaneous equations.

$$
\frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i (- i)}} = \frac {\partial \pi_ {i (- i)} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i (- i)}} = 0, \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \},\tag{190}
$$

which gives the following results.

$$
e _ {i i} = e _ {i i} ^ {*}, \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*}, e _ {i (- i)} = e _ {i (- i)} ^ {*}, \hat {e} _ {i (- i)} = \hat {e} _ {i (- i)} ^ {*}, \forall i \in \{A, B \}.\tag{191}
$$

Suppose first that the low type patients do not switch their providers for the second visit. In Stage 3, we set

$$
\begin{array}{r l} & P _ {2 C D} = \ddot {P} _ {2 C D} (\mathrm{H}, \mathrm{H}) := - 2 (e _ {i (- i)} ^ {*}) ^ {2} \delta + 2 e _ {i (- i)} ^ {*} \delta + P _ {2 C S} + 2 (e _ {i i} ^ {*}) ^ {2} \delta + 4 \alpha e _ {i i} ^ {*} \delta \\ & - 4 e _ {i i} ^ {*} \delta + 8 e _ {i i} ^ {*} \delta \tilde {e} - \tau_ {1} + \tau_ {2} \end{array}\tag{192}
$$

We solve the following simultaneous equations:

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (A, B).\tag{193}
$$

Solving the simultaneous equations, we get the following results:

$$
e _ {i 0} = \hat {e} _ {i 0} = \tilde {e}, \forall i \in \{A, B \}.\tag{194}
$$

The corresponding expected future payoffs of provider A and B then become

$$
\begin{array}{r l} & {\overline {{\pi}} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \theta (P _ {2 C S} + 2 \delta ((e _ {i i} ^ {*}) ^ {2} + 2 e _ {i i} ^ {*} (\alpha + 2 \tilde {e} - 1) + \tilde {e} ^ {2}) + \tau_ {1} + \tau_ {2})} \\ & {\overline {{\pi}} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) = \dot {\pi} _ {B} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) := \frac {1 - \theta}{\theta} \dot {\pi} _ {A} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}).} \end{array}\tag{195}
$$

(196)

We let $\tilde { P } _ { 2 C S } ( \Nu , \Nu )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {P} _ {2 C S} (\mathrm{N}, \mathrm{N}) = m i n [ \tilde {P} _ {2 C S _ {A}}, \tilde {P} _ {2 C S _ {B}} ],\tag{197}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) | _ {P _ {2 C S} = \tilde {P} _ {2 C S _ {i}}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.
$$

(198)

Suppose next that the low type patients switch their providers for the second visit. In Stage 3, we solve the following simultaneous equations:

$$
\frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial e _ {i 0}} = \frac {\partial \pi_ {i 0} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial \hat {e} _ {i 0}} = 0, \forall i \in \{A, B \} \mathrm{and} (k, l) = (\mathrm{B,A}),\tag{199}
$$

which leads the following.

$$
\begin{array}{r l} & {e _ {i 0} = \hat {e} _ {i 0} = \frac {(\hat {e} _ {i 0} ^ {*}) ^ {2} (2 e _ {i i} ^ {*} \epsilon + 1) - 4 (\alpha - 1) e _ {i i} ^ {*} \tilde {e} \epsilon + \hat {e} _ {i 0} ^ {*} (2 \alpha (e _ {i i} ^ {*} \epsilon + 1) - 2 e _ {i i} ^ {*} (2 \tilde {e} \epsilon + \epsilon) - 1)}{a + \alpha + \hat {e} _ {i 0} ^ {*} - 1}} \\ & {+ \frac {a ^ {2} (2 e _ {i i} ^ {*} \epsilon - 1) + a (\hat {e} _ {i 0} ^ {*} (4 e _ {i i} ^ {*} \epsilon + 2) + \alpha (2 e _ {i i} ^ {*} \epsilon - 1) - 2 e _ {i i} ^ {*} (2 \tilde {e} + 1) \epsilon)}{a + \alpha + \hat {e} _ {i 0} ^ {*} - 1}, \forall i \in \{A, B \}.} \end{array}\tag{200}
$$

We denote the corresponding utility of provider A and B using $\ddot { \pi } _ { i } ^ { \mathrm { E } } ( \mathrm { N } , \mathrm { N } ) \forall i \in \{ \mathrm { A } , \mathrm { B } \}$ , and we verify that

$$
\frac {\partial \ddot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N,N})}{\partial P _ {2 C S}} > 0, \forall i \{\mathrm{A,B} \}.\tag{201}
$$

We let $\tilde { \tilde { P } } _ { 2 C S } ( \Nu , \Nu )$ be a value of $P _ { 2 C S }$ such that

$$
\tilde {\tilde {P}} _ {2 C S} (\mathrm{N}, \mathrm{N}) = m i n [ \tilde {\tilde {P}} _ {2 C S _ {A}}, \tilde {\tilde {P}} _ {2 C S _ {B}} ],\tag{202}
$$

where

$$
\dot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) | _ {P _ {2 C S} = \tilde {\bar {P}} _ {2 C S _ {i}}} = \omega_ {i}, \forall i \in \{\mathrm{A}, \mathrm{B} \}.\tag{203}
$$

We let $P _ { 2 C S } = \ddot { P } _ { 2 C S } ( \mathrm { H } , \mathrm { H } )$ where

$$
\ddot {P} _ {2 C S} (\mathrm{H}, \mathrm{H}) = m i n [ \tilde {P} _ {2 C S} (\mathrm{H}, \mathrm{H}), \tilde {P} _ {2 C S} (\mathrm{N}, \mathrm{N}), \tilde {\tilde {P}} _ {2 C S} (\mathrm{N}, \mathrm{N}) ].\tag{204}
$$

This ensures that the providers adopt HIE and the low type patients switch their providers for the second visit.

We let $\tau _ { 1 } ^ { \mathrm { E } } = \ddot { \tau } _ { 1 } ^ { \mathrm { E } } ( \mathrm { N } , \mathrm { N } )$ is a value such that

$$
\ddot {\tau} _ {1} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) = m a x [ \ddot {\tau} _ {A} ^ {E} (\mathrm{H}, \mathrm{H}), \ddot {\tau} _ {B} ^ {E} (\mathrm{H}, \mathrm{H}) ],\tag{205}
$$

where

$$
\ddot {\pi} _ {i} ^ {\mathrm{E}} (\mathrm{H}, \mathrm{H}) | _ {\tau_ {1} ^ {\mathrm{E}} = \ddot {\tau} _ {i} ^ {E}} (\mathrm{H}, \mathrm{H}) = \omega_ {i}, \forall i \in \{A, B \}.\tag{206}
$$

Finally, we choose zero values for the free variables.

## Proof of Proposition 4

(i): We breach the notation and write the optimal efforts under payment model $M \in \{ \mathrm { F } , \mathrm { P } , \mathrm { E } \}$ be given by $e _ { i j } ^ { M }$ and $\hat { e } _ { i j } ^ { M }$ . We then observe that

$$
\Pi^{\mathrm{AB}}(\mathrm{N},\mathrm{N})\big|_{\substack{e_{ij} = e_{ij}^{\mathrm{E}}(\mathrm{N},\mathrm{N})\\ e_{ij} = \hat{e}_{ij}^{\mathrm{E}}(\mathrm{N},\mathrm{N})}} = \frac{U(4\delta^{2}U - 8\delta^{3} + U^{3})}{8\delta^{2}(\delta + 2U)},\tag{207}
$$

$$
\left. \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N})} = \frac {U (1 6 \delta^ {2} U - 6 4 \delta^ {3} + U ^ {3})}{6 4 \delta^ {2} (\delta + U)},\tag{208}
$$

$$
\Pi^{\mathrm{AB}}(\mathrm{N},\mathrm{N})\big|_{\substack{e_{ij} = e_{ij}^{\mathrm{P}}(\mathrm{N},\mathrm{N})\\ e_{ij} = \hat{e}_{ij}^{\mathrm{P}}(\mathrm{N},\mathrm{N})}} = \frac{U(4\delta^{2}U - 8\delta^{3} + U^{3})}{8\delta^{2}(\delta + 2U)}.\tag{209}
$$

Clearly, $\begin{array} { r } { \left. \Pi ( { \bf N } , { \bf N } ) \right| _ { e _ { i j } = e _ { i j } ^ { { \bf E } } ( { \bf N } , { \bf N } ) } = \left. \Pi ( { \bf N } , { \bf N } ) \right| _ { e _ { i j } = e _ { i j } ^ { { \bf P } } ( { \bf N } , { \bf N } ) } . } \\ { e _ { i j } = \hat { e } _ { i j } ^ { { \bf E } } ( { \bf N } , { \bf N } ) \quad \quad \quad \quad e _ { i j } = \hat { e } _ { i j } ^ { { \bf P } } ( { \bf N } , { \bf N } ) } \end{array}$

Define

$$
\begin{array}{r} f (U) := \left. \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N})} - \left. \Pi^ {\mathrm{AB}} (\mathrm{N}, \mathrm{N}) \right| _ {e _ {i j} = e _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N})} \\ e _ {i j} = \hat {e} _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) \qquad \qquad \qquad \qquad \qquad \qquad e _ {i j} = \hat {e} _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) \end{array}
$$

Ayvaci et al. / Designing Payment Contracts for Healthcare Services to Induce Information Sharing

$$
= \frac {U ^ {2} (8 0 \delta^ {3} + 6 U ^ {3} + 7 \delta U ^ {2})}{6 4 \delta^ {2} (\delta + U) (\delta + 2 U)}.\tag{210}
$$

We observe that $f ( U ) > 0$ and $f ( U ) = 0$ at $U = 0$

(ii): Observe that

$$
\Sigma (\mathrm{N}, \mathrm{N}) | _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) \\ e _ {i j} = \hat {e} _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) \end{array} } = \frac {(2 \delta^ {2} + U ^ {2}) (- 2 \delta^ {2} + 2 \delta U + 3 U ^ {2})}{4 \delta^ {2} (\delta + 2 U) ^ {2}} + 1\tag{211}
$$

$$
\Sigma (\mathrm{N}, \mathrm{N}) | _ { \begin{array}{c} e _ {i j} = e _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) \\ e _ {i j} = \hat {e} _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N}) \end{array} } = \frac {8 0 \delta^ {2} U ^ {2} + 1 6 0 \delta^ {3} U + 4 \delta U ^ {3} + 3 U ^ {4}}{6 4 \delta^ {2} (\delta + U) ^ {2}}\tag{212}
$$

$$
\Sigma (N,N)\big|_{\substack{e_{ij} = e_{ij}^{\mathsf{P}}(N,N)\\ e_{ij} = \hat{e}_{ij}^{\mathsf{P}}(N,N)}} = \frac{(2\delta^{2} + U^{2})(- 2\delta^{2} + 2\delta U + 3U^{2})}{4\delta^{2}(\delta + 2U)^{2}} +1\tag{213}
$$

Define

$$
\begin{array}{c} g (U) \text {:} = \Sigma (\mathrm{N}, \mathrm{N}) | _ {e _ {i j} = e _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N})} - \Sigma (\mathrm{N}, \mathrm{N}) | _ {e _ {i j} = e _ {i j} ^ {\mathrm{F}} (\mathrm{N}, \mathrm{N})} \\ e _ {i j} = \hat {e} _ {i j} ^ {\mathrm{E}} (\mathrm{N}, \mathrm{N}) \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \\ = \frac {U (1 6 0 \delta^ {5} + 1 0 0 \delta U ^ {4} + 9 1 \delta^ {2} U ^ {3})}{6 4 \delta^ {2} (\delta + U) ^ {2} (\delta + 2 U) ^ {2}} + \frac {U (2 8 \delta^ {3} U ^ {2} + 2 4 0 \delta^ {4} U + 3 6 U ^ {5})}{6 4 \delta^ {2} (\delta + U) ^ {2} (\delta + 2 U) ^ {2}}. \end{array}\tag{214}
$$

We observe that $g ( U ) > 0$ and $g ( U ) = 0$ at $U = 0$

## Proof of Proposition 5

The value of HIE is calculated as the social payoff realized under the optimal choices of efforts by providers when providers adopt HIE minus the social payoff under the optimal choices of efforts by providers when providers do not adopt HIE.

Note that the EBP model and the P4P model induces the first-best solutions when the low type patient returns to the same provider regardless of HIE adoption decision. Therefore, the value of HIE under the EBP model and the P4P model can be calculated using th social payoff expressions provided in (29) and (33). The value of HIE under the EBP model and the P4P model is given as

$$
V ^ {\mathrm{E}} = V ^ {\mathrm{P}} = - C _ {\mathrm{HIE}} - \frac {\alpha U (U - 2 \delta (- \alpha + 2))}{2 (\delta + 2 U)}\tag{215}
$$

However, the FFS model does not induce HIE adoption in the equilibrium as shown in Lemma 5.1. Therefore, in order to calculate the value of HIE under the FFS model, we derive the social payoff under the FFS model when the both providers are forced to adopt HIE and the low type patient does not switch.

Consider the scenario where HIE is induced under the FFS model. Then in Stage 5 of the game, we derive the solutions under HIE adoption scenario by solving the following simultaneous equations. Solving for

$$
\frac {\partial \pi_ {i i} ^ {\mathrm{F}} (\mathrm{H,H})}{\partial e _ {i i}} = \frac {\partial \pi_ {i i} ^ {\mathrm{F}} (\mathrm{H,H})}{\partial \hat {e} _ {i i}} = 0, \forall i \in \{A, B \},\tag{216}
$$

gives

$$
e _ {i i} = \frac {\gamma_ {2}}{2 \delta}, \hat {e} _ {i i} = 0, \forall i \in \{A, B \}.\tag{217}
$$

In Stage 3 and 4, the FOCs indicate the following simultaneous equations.

$$
\frac{\partial\pi_{i0}^{\mathrm{F}}(\mathrm{H,H})}{\partial e_{i0}}\bigg|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{H,H}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{H,H})}} = \frac{\partial\pi_{i0}^{\mathrm{F}}(\mathrm{H,H})}{\partial\hat{e}_{i0}}\bigg|_{\substack{e_{ii} = e_{ii}^{*}(\mathrm{H,H}),\\ \hat{e}_{ii} = \hat{e}_{ii}^{*}(\mathrm{H,H})}} = 0,\forall i\in \{A,B\} .\tag{218}
$$

Solving these equations, we have the following stationary point.

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = - \frac {\gamma_ {2} ^ {2}}{8 \delta^ {2}}.\tag{219}
$$

However, since $\begin{array} { r } { - \frac { \gamma _ { 2 } ^ { 2 } } { 8 \delta ^ { 2 } } \leq 0 } \end{array}$ , the solution in (219) cannot be optimal. Now we construct provider ??’s Lagrangian which is formulated as

$$
L _ {i 0} (\mathrm{H}, \mathrm{H}) = \pi_ {i 0} ^ {\mathrm{F}} (\mathrm{H}, \mathrm{H}) | _ {e _ {i i} = e _ {i i} ^ {*} (\mathrm{H}, \mathrm{H}), \atop \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{N}, \mathrm{H})} + \lambda_ {1} (e _ {i 0}) + \lambda_ {2} (\hat {e} _ {i 0}) + \lambda_ {3} (1 - e _ {i 0} - \hat {e} _ {i 0})\tag{220}
$$

Using K-T conditions, we have the following stationary point for $\forall i \in \{ \mathsf { A } , \mathsf { B } \}$

$$
e _ {i 0} = \frac {4 \gamma_ {1} \delta - \gamma_ {2} ^ {2}}{8 \delta^ {2}}, \hat {e} _ {i 0} = 0.\tag{221}
$$

In Stage 1 of the game, we derive the optimal payment term $\gamma _ { 1 }$ and $\gamma _ { 2 }$ by solving the following simultaneous equations:

$$
\begin{array}{r l} & {\frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{H,H})}{\partial \gamma_ {1}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{H,H}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{H,H}), \hat {e} _ {i i} = \hat {e} _ {i i} ^ {*} (\mathrm{H,H})} \\ & {= \frac {\partial \Pi^ {\mathrm{AB}} (\mathrm{H,H})}{\partial \gamma_ {2}} \bigg | _ {e _ {i 0} = e _ {i 0} ^ {*} (\mathrm{H,H}), e _ {i i} = e _ {i i} ^ {*} (\mathrm{H,H}),}} \\ & {\qquad \hat {e} _ {i 0} = \hat {e} _ {i 0} ^ {*} (\mathrm{H,H}), \hat {e} _ {i i} = {\hat {e}} _ {i i} ^ {*} (\mathrm{H,H})} \end{array} = 0, \forall i \in \{A, B \},\tag{222}
$$

(223)

The solution to above gives

$$
\gamma_ {1} ^ {*} = \frac {U (U ^ {2} - 8 (\alpha - 1) \delta^ {2})}{4 \delta (\delta + U)}, \gamma_ {2} ^ {*} = U.\tag{224}
$$

The corresponding objective function becomes

$$
\Pi^ {\mathrm{AB} *} (\mathrm{H}, \mathrm{H}) := \frac {U (- 6 4 (\alpha - 1) ^ {2} \delta^ {3} + U ^ {3} - 1 6 (\alpha - 1) \delta^ {2} U)}{6 4 \delta^ {2} (\delta + U)} - C _ {\mathrm{HIE}}.\tag{225}
$$

Next, we derive the value of HIE under the FFS model using the social payoff expressions provided in (62) and (225).

$$
V ^ {\mathrm{F}} = - C _ {\mathrm{HIE}} - \frac {\alpha U (U - 4 \delta (- \alpha + 2))}{4 (\delta + U)}\tag{226}
$$

Finally, we compare the expression provided in (226) and the expression provided in (215). We show that $V ^ { \mathrm { F } } - V ^ { \mathrm { E } } > 0$ holds if and only if

$$
\alpha \delta U (\delta + U) (\delta + 2 U) (8 (\alpha - 2) \delta + (1 2 \alpha - 2 5) U) <   0,\tag{227}
$$

which is true since $\alpha < 1$

## Appendix B

## Numerical Comparison of Payment Models

## Total Healthcare Costs

![](/api/attachments/G23RDAG8/fulltext/images/437ef5e0455fcb7b7cba6c92ca764496b3f2a1db5e70374060314927607ad2c6.jpg)  
(d) Low-type patients do not switch regardless of HIE adoption under EBP $( \mu = 1 0 )$

![](/api/attachments/G23RDAG8/fulltext/images/64cb7d47eda8a98a32e2f8b8c5e48e025922daad5d4a116f33e993330953060b.jpg)  
(e) Low-type patients switch regardless of HIE adoption under EBP (?? = 60)

![](/api/attachments/G23RDAG8/fulltext/images/19671870c35f6b48fb63ed3634bd232384c6f17b6d5118901f8ea9a60d633f9b.jpg)  
(f) Low-type patients switch only when HIE is adopted under EBP (?? = 25)

Note: We set $\delta = 5 0 0 0 , \theta = 0 . 7 , \alpha = 0 . 0 1 , u _ { H } = 1 0 0 0 , u _ { L } = 3 5 0 , \epsilon = 0 .$

Figure B1. Comparison of the Total Healthcare Cost across Different Payment Models.

Quality of Care  
![](/api/attachments/G23RDAG8/fulltext/images/fac9a66c7faac8f07c551a096e1a4e02f92e1dfbfcec0db34c846ffe0f7bfd5b.jpg)

(a) Low-type patients do not switch regardless of HIE adoption under EBP (?? = 10)  
![](/api/attachments/G23RDAG8/fulltext/images/9472009b987932064ac1b2ee6c447a1f3abc4f32cb8f63551c109189d861ba3d.jpg)  
(b) Low-type patients switch regardless of HIE adoption under EBP $( \mu = 6 0 )$

![](/api/attachments/G23RDAG8/fulltext/images/3bb5432f2d0509b5da90c42e56048d18e8ce4c402c2c3c6c94ca3558776a8231.jpg)  
(c) Low-type patients switch only when HIE is adopted under EBP (?? = 25)  
Note: We set $\delta = 5 0 0 0 , \theta = 0 . 7 , \alpha = 0 . 0 1 , u _ { H } = 1 0 0 0 , u _ { L } = 3 5 0 , \epsilon = 0 .$

## Total Payment

![](/api/attachments/G23RDAG8/fulltext/images/ea67fe6f8e67f28bbf78d18e6592cb9c20b69f7e69678cf0870905f137e010f2.jpg)  
(a) Low-type patients do not switch regardless of HIE adoption under EBP (?? = 10)

![](/api/attachments/G23RDAG8/fulltext/images/d6f781d13e83c3863eb6788004030d76bf27cb46e33a615afc4ba95bb020c9eb.jpg)  
(b) Low-type patients switch regardless of HIE adoption under EBP $( \mu = 6 0 )$

![](/api/attachments/G23RDAG8/fulltext/images/84482de7ec625f4b681d816d1d0c45f6e3c08f9af9d30707873f0dfb9de2cf97.jpg)  
(c) Low-type patients switch only when HIE is adopted under EBP (?? = 25)

$$
\text { Note:   We   set } \delta = 5 0 0 0, \theta = 0. 7, \alpha = 0. 0 1, u _ {H} = 1 0 0 0, u _ {L} = 3 5 0, \epsilon = 0.
$$
