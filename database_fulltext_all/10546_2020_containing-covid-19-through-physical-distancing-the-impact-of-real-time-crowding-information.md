---
otero_id: 10546
otero_key: "J5NYHVAP"
title: "Containing COVID-19 through physical distancing: the impact of real-time crowding information"
authors: "Martin Adam; Dominick Werner; Charlotte Wendt; Alexander Benlian"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1814681"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Containing COVID-19 through physical distancing: the impact of real-time crowding information

Martin Adam , Dominick Werner , Charlotte Wendt & Alexander Benlian

To cite this article: Martin Adam , Dominick Werner , Charlotte Wendt & Alexander Benlian (2020): Containing COVID-19 through physical distancing: the impact of real-time crowding information, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1814681

To link to this article: https://doi.org/10.1080/0960085X.2020.1814681

![](/api/attachments/J5NYHVAP/fulltext/images/d393db756c48866607fb46aff329839cc574f49ce2c9097ab281caa363d4d0e9.jpg)

Published online: 08 Sep 2020.

![](/api/attachments/J5NYHVAP/fulltext/images/e09e962de9b4e4243deb385489ad87c9c3950365e2eeb90aace323f47315ec8a.jpg)

Submit your article to this journal

![](/api/attachments/J5NYHVAP/fulltext/images/88345b8ed41dd53d7ff0d8fe6bd8fdc581de6baf242495545b57938dc1482bcd.jpg)

View related articles

![](/api/attachments/J5NYHVAP/fulltext/images/dc15b598256d25d8521cf4f79dd320038d480d019a91565b99b1bf86d1f76445.jpg)

View Crossmark data

EMPIRICAL RESEARCH

Check for updates

# Containing COVID-19 through physical distancing: the impact of real-time crowding information

Martin Adam , Dominick Werner , Charlotte Wendt and Alexander Benlian

Institute of Information Systems and Electronic Services, Technical University of Darmstadt, Darmstadt, Germany

## ABSTRACT

With the rise of COVID-19, decision support systems (DSS) increasingly display crowding information (CI) (e.g. how crowded a medical practice is) to encourage physical distancing when users select locations. Despite important implications for containing COVID-19, little is known about the causal efect of CI on user selection behaviour and how the immediacy of CI (e.g. “updated 2 minutes ago“) as well as users’ health anxiety further influence the efect of CI. Drawing on literature on digital choice environments and construal level theory, we conducted a multi-national online experiment to investigate the efect of CI on selecting diferently crowded medical practices. Our results demonstrate that present (vs. absent) CI in DSS increases the likelihood of users selecting less crowded medical practices, while the efect is strongest when employed with real-time (vs. historical average) CI and, surprisingly, when users’ health anxiety is low (vs. high). Overall, our study adds to the growing body of research on IS in the age of pandemics and provides actionable insights for DSS providers and policymakers to endow users with information to identify and select less crowded locations, thus containing COVID-19 through improved physical distancing without paternalistically restricting users’ freedom of choice.

Protect yourself, protect others: Avoid going to crowded places. Why? Where people come together in crowds, it is more dificult to maintain physical distance.

– World Health Organisation, COVID-19 advice for the public <sup>1</sup>

## 1. Introduction

As long as an efective medication and vaccine are still being developed, physical distancing<sup>2</sup> is one of the most potent means to curb the spread of COVID-19. As such, many policymakers recommend or even fiercely enforce physical distancing of their citizens through lockdowns and curfews to ensure compliance. The prevalence of enforced physical distancing reached unprecedented levels when in March 2020 almost one in every five people around the globe were placed under lockdown (Davidson, 2020). In sum, physical distancing has become an unwanted but needed global practice, opposing the social nature of humans and thus – if enforced – embodying undesired paternalistic infringements of citizens’ freedom of choice.

To facilitate physical distancing without restricting citizens’ personal freedom, decision support systems (DSS) increasingly display crowding information (CI), which we define as information that indicates to what extent a location’s available capacity for visitors is

ARTICLE HISTORY Received 15 July 2020 Accepted 20 August 2020

occupied. For example, the website DocClocker informs patients how exposed they are to other patients at diferent doctors (Pennic, 2020), the app Crowdless shows which supermarkets are currently crowded (BBC, 2020) and the popular times feature of Google Maps displays how busy locations (e.g. restaurants and bars) are (Google, 2020) (see Figure 1 for an example). By employing CI, DSS make the diferent crowding levels at real-world locations digitally visible and thus allow users to identify diferently crowded locations. If users then select less crowded locations, physical distancing increases because this selection not only reduces the likelihood of crowded locations becoming overcrowded (e.g. inhibiting users from keeping the recommended levels of physical distance at the locations) but also leads to a more equally distributed crowding level and thus to less congestion across all locations, thereby minimising the number of possible encounters and thus potential risk of infection between all users (see D’Angelo and West 2000). As such, DSS can potentially facilitate physical distancing by displaying CI and therefore provide an important contribution to the containment of the COVID-19 pandemic.

SPECIAL ISSUE EDITORS Pär Ågerfalk; Kieran Conboy and Michael Myers

COVID-19; pandemic; crowding information; immediacy of information; real-time; health anxiety

Although DSS increasingly display CI to assist users in identifying and selecting less crowded options, knowledge is lacking whether and how CI indeed influences (user) selection behaviour. Specifically when users are uncertain about the quality of each location, users face a dilemma when interpreting CI: Given the COVID-19 pandemic, more crowded locations entail a heightened risk of infection through increased encounters and congestion (Bayham et al., 2015), whereas less crowded locations may be perceived to exhibit poor quality, based on an apparent lack of demand for these options (e.g. Becker, 1991; Bikhchandani et al., 1992; X. Li & Wu, 2018). Previous information systems (IS) research related to CI primarily investigated how users interpret demand information, such as the number of patient recommendations for a doctor (Khurana et al., 2019; Li et al., 2019). Findings mainly indicate that individuals are attracted to highly demanded and thus often crowded locations as high demand is interpreted as a signal of high quality (Becker, 1991; Chen & Davison, 2019; X. Li & Wu, 2018). For example, highly demanded doctors are believed to provide greater service quality (Khurana et al., 2019; Li et al., 2019), reflecting expertise and safety to receive competent support, which seems particularly important during the COVID-19 pandemic. Yet, this attraction to demanded and thus often crowded locations implies a serious threat in times of COVID-19: If users are attracted to crowded locations, do DSS that display CI in good faith unintentionally make users select more crowded locations and hence add fuel to the fire of spreading COVID-19? To address this concern, insights on the causal efect of displaying CI on selection behaviour are urgently required and of significant practical value in view of the containment of COVID-19.

![](/api/attachments/J5NYHVAP/fulltext/images/2a79d6941d4c2e52a714aff3e3b8c6a9263227b0ed7739de51a5b284bd9358d8.jpg)  
Figure 1. CI provided by Google Maps (Google, 2020) with usual CI based on historical visits (left) and live CI reflecting current visits (right).

In addition to the main efect of CI on selection behaviour, we also investigate two salient and COVID-19-relevant factors that potentially interact with the way CI is processed by users. First, CI is usually not displayed in isolation but accompanied by immediacy cues (e.g. “updated 2 minutes ago”), which indicate how closely the CI relates to the present point in time. For instance, Google’s popular times feature not only informs users how crowded locations are, but also whether the information reflects “live” (i.e. real-time) or “usual” (i.e. average over the past) representations (see Figure 1) (Google, 2020).

Similarly, CI with immediacy cues can be found for locations and services particularly impacted by COVID-19, such as real-time occupancy of emergency rooms (NSW, 2020) and utilisation of public transport (Transit, 2020). Although DSS increasingly employ more immediate (up to real-time) CI (e.g. X. Li & Wu, 2018; Qiu et al., 2018), it is unknown whether users select less crowded locations more or less often when CI becomes more immediate. Indeed, previous research on time-related cues has not explicitly considered the immediacy of dynamically changing information (e.g. CI in which the crowding level notably varies over time) and instead only analysed the efects of time cues on static information about occurrences (e.g. timestamps of when products or reviews were published) (e.g. Chen et al., 2011; Huang et al., 2018) or highly predictable events (e.g. countdowns for the limited availability of purchase options) (e.g. Amirpur & Benlian, 2015; G. Li & Wang, 2019). As such, besides the main efect of CI on selection behaviour, it seems fruitful to investigate how the immediacy of CI further shapes users’ information processing and thus selection behaviour.

Second, the immediacy of CI is not processed in a vacuum but is dependent on a user’s responsiveness to the immediacy cue, which, in times of COVID-19, is most likely shaped by a user’s health anxiety. We refer to health anxiety as a user’s “exaggerated estimates of the likelihood and severity of having an illness” (Abramowitz et al., 2007, p. 873). Health anxiety has become a common and critical theme in pandemics (Wheaton et al., 2011), as it results in unusual and partly irrational user behaviour, such as generally avoiding crowded places (Lau et al., 2010; Morganstein et al., 2017), making unnecessary preemptive visits at doctors or avoiding doctors altogether (Wong et al., 2020) and even developing dangerous self-medications like drinking bleach (Spinney, 2020). Whereas previous studies have demonstrated that higher levels of health anxiety can lead to selecting less crowded locations (Lau et al., 2010), little is known about how health anxiety interacts with the processing of diferently immediate CI. This insight, however, is important because health anxiety is particularly relevant in times of COVID-19 and may shape the processing of immediacy cues in an unknown direction, thus impacting the overall efectiveness of CI and hence selection behaviour. As such, investigating diferent levels of immediacy together with diferent levels of health anxiety appears to be of high theoretical and practical interest to uncover potential complementary or substitutive interaction efects.

Against this backdrop, this study first investigates whether and how the presence of CI impacts users selections of diferently crowded locations in the context of COVID-19. Second, we explore the presence of CI more deeply by investigating the efect of CI at diferent levels of immediacy and health anxiety. Overall, we ask the following two research questions:

RQ1: Whether and how does the presence (vs. absence) of CI influence users’ selections of diferently crowded locations?

RQ2: If CI is present, how does the level of immediacy of CI influence users’ selections of diferently crowded locations at diferent levels of health anxiety?

To answer our research questions, we integrate literature on digital choice environments with construal level theory and conducted an online experiment in which 343 participants from Germany and Italy selected between diferently crowded medical practices. Our results demonstrate that present (vs. absent) CI increases the likelihood of users selecting less crowded medical practices, in that users are 4.6 times as likely to select less crowded options. Moreover, this efect is strongest when employed with more immediate CI and when users show lower levels of health anxiety.

This study adds to the emerging body of initiatives on IS in the age of pandemics (Laato et al., 2020; Naidoo, 2020) and answers the call of Ågerfalk et al. (2020) for IS studies whose results have important and immediate practical implications to contain the COVID-19 pandemic and beyond. Specifically, our insights can help DSS providers and policymakers in the design of emerging apps to achieve an immediate impact on physical distancing by endowing users with CI and making them voluntarily select less crowded locations. Consequently the infection risk for individuals, service providers (e.g. medical practitioners) and ultimately the society as a whole is reduced without infringing individuals’ freedom of choice. Beyond these practical implications, this study also ofers theoretical contributions regarding IS in times of the COVID-19 pandemic – a context that may afect users’ usual processing of information and thus selection behaviour. Besides introducing CI as a new DSS feature in digital choice environments and assessing its impact, we extend construal level theory by investigating immediacy as a new facet of temporal distance and by examining the joint efect of immediacy and health anxiety inducing mental construal in diferent ways. As such, we highlight the importance and efects of an emerging form of information within and beyond the context of pandemics.

## 2. Theoretical background

In this section, we first introduce CI as a DSS feature and position it in related literature on demand information in digital choice environments. Subsequently, we introduce construal level theory as a theoretical lens through which we shed light on the facets of immediacy and health anxiety.

## 2.1. Crowding information as a DSS feature

CI as an increasingly prevalent DSS feature in digital choice environments builds upon the abundantly employed DSS feature of visualisation of demand information, which signals how many users have already selected a given option (e.g. number of checkins at a restaurant, aggregated statistics displaying product purchases) (Chen et al., 2011; Thies et al., 2016). High demand is often interpreted as a signal of high quality (e.g. Bikhchandani et al., 1992; X. Li & Wu, 2018; Thies et al., 2016). In particular, when faced with uncertainty, users usually rely on such DSS features and use those signals to imitate previous selection behaviours, thereby selecting highly demanded options (e.g. Chen & Davison, 2019; Duan et al., 2009; Walden & Browne, 2009). Thus, interpreting high demand as a signal of high quality induces users to opt for more crowded locations (Becker, 1991).

Since the rise of the COVID-19 pandemic, DSS providers for real-world services increasingly display DSS features in the form of CI – similar to announcing wait times in call centres (Yu et al., 2018). CI addresses the rival nature of locations with limited capacity, which entails that increasing crowding by users results in growing congestion (Casson, 1982) (e.g. multiple patients competing for the attention of one medical practitioner at the same time). With increasing congestion, individuals impose rising costs on each other (Wang & Ackerman, 2019; Weimer & Vining, 2005), such as unwanted physical proximity to others, increased wait times and impaired service quality (Becker, 1991; Villarica, 2011). Particularly in times of pandemics, costs in the form of intensity and duration of exposure to others are highly relevant as they undermine physical distancing. Therefore, it is important to investigate whether and how CI alters users selections of diferently crowded locations and thus physical distancing during the COVID-19 pandemic.

## 2.2. Construal level theory and its role for immediacy and health anxiety

Beyond consideration of presence (vs. absence) of CI as a DSS feature, we draw on construal level theory to understand how processing of CI is afected by related immediacy of CI and users' health anxiety. Construal level theory refers to the cognitive processing of goals (e.g. selecting a location) and related messages (e.g. CI of a location) by delineating how closer psychological distance from an event or object leads to a more concrete mental representation of it (Trope & Liberman, 2010). Psychological distance hereby describes an individual’s “subjective experience that something is close [to] or far away” (Trope & Liberman, 2010, p. 440) with regard to, for instance, time (i.e. temporal distance) and likelihood (i.e. hypothetical distance) (Bar-

Anan et al., 2006). For example, individuals think about an upcoming visit to a medical practice in concrete terms (e.g. how to get there), whereas general awareness of one’s health is conceived in more abstract terms (e.g. why to go to medical practices).

DSS providers can afect users’ construal of events and objects by accompanying CI with immediacy cues to alter users’ perceived temporal distance towards the event or object (Huang et al., 2018). We refer to immediacy of CI as how closely the presented CI relates to the present point in time, reaching up to an instantaneous, real-time representation. Accordingly, higher levels of immediacy (e.g. the CI relates to “right now”) represent a closer temporal distance than lower levels of immediacy (e.g. the CI relates to an average over the past) and therefore induce users to think about the respective location more concretely, compared to a more abstract construal when immediacy is low (Bar-Anan et al., 2006; Broniarczyk & Grifin, 2014; Trope & Liberman, 2010). Previous IS studies found that closer temporal distance derived from time-related information (e.g. timestamps of reviews, product release dates, countdown timers) changes how users respond to information, for example, by evaluating recent product reviews as more helpful (Huang et al., 2018), by increasing funding of crowdfunding campaigns close to their completion date (G. Li & Wang, 2019) and by imitating others’ behaviours more strongly when products are new (Chen et al., 2011). Yet, whereas previous IS studies mainly analysed DSS features in the form of static information, it is unclear how DSS features in the form of dynamically changing information (e.g. CI) and corresponding levels of immediacy impact selection behaviour.

Aside from immediacy’s influence on temporal distance, health anxiety (i.e. a user’s perception of increased likelihood of having an illness) can shift a user’s hypothetical distance. Accordingly, high (vs. low) health anxiety induces a closer (vs. farther) hypothetical distance towards health threats as the risk of contracting a disease is perceived as more probable to the respective user (Trope & Liberman, 2010). Previous research on hypothetical distance mainly investigated its influence on individuals’ construal in isolation, without considering potential interaction efects with other dimensions of psychological distance, such as temporal distance (McDonald et al., 2015; Trope & Liberman, 2010). Hence, it is unclear how health anxiety interacts with immediacy of CI and how both jointly impact the main efect of CI on selection behaviour.

## 3. Hypothesis development

In the following, we first hypothesise the efect of CI on selection behaviour (H1). Subsequently, we hypothesise how the efect of CI changes with diferent levels of immediacy (H2) and how this influence of immediacy is subject to health anxiety (H3).

## 3.1. The efect of CI on selection behaviour

In digital choice environments, CI is increasingly applied as a DSS feature to assist users in identifying and selecting their preferred option (e.g. location). In case CI is not provided (i.e. CI absent), crowding levels of diferent locations cannot be considered in the selection process and we expect users to select a location at random, all else being equal (e.g. distance to the location). Conversely, in case CI is provided (i.e. CI present), users are able to compare locations based on the trade-ofs associated with the crowding level of each alternative. Specifically, the presence of many individuals at one location represents high demand and is interpreted as a signal of high quality (e.g. Bikhchandani et al., 1992; X. Li & Wu, 2018; Thies et al., 2016), while at the same time high demand, and thus crowding, implies costs of congestion such as wait times and proximity to others (Becker, 1991; Casson, 1982). Although previous findings in the area of real-world services indicate a dominating influence of CI’s quality signals (Becker, 1991), this influence can be countervailed when CI simultaneously signals a heightened risk of infection through increased encounters (Bayham et al., 2015). Particularly under the extraordinary circumstances attributed to the COVID-19 pandemic, the costs of congestion related to CI may prevail over CI’s quality signals and shift users’ selection behaviour towards less crowded locations to minimise exposure to individuals (Lau et al., 2010; Morganstein et al., 2017).

H1: In times of pandemics, users are more likely to select less crowded locations when CI is present (vs. absent).

## 3.2. The efect of immediacy of CI on selection behaviour

Construal level theory posits that a construal fit occurs when the construal levels of a goal and its respective goal-related message match (Hansen & Wänke, 2010; Kim et al., 2009; A. Lee et al., 2010). Regarding the construal level of a goal, the goal of selecting a location is often spontaneous (Parboteeah et al., 2009) and frequently refers to a highly immediate and concrete future (e.g. “I suddenly feel sick; I should see a doctor as soon as I can”), inducing a close temporal distance and thus low-level construal (Trope & Liberman, 2003). On the other hand, a goal-related message can often be subject to diferent levels of immediacy (e.g. “updated 2 minutes ago” vs. “updated sometime in the past”) and thus diferent levels of temporal distance, such that the construal level of the goal-related message is not always low. Still, the two construal levels of goal and goal-related message match better when the immediacy of a goal-related message is high (vs. low) (Hansen & Wänke, 2010; Semin et al., 2005).

Accordingly, we argue that high (vs. low) immediacy of CI leads to the selection of less crowded locations. Specifically, we assert that this change in selection behaviour results from an increased construal fit and its evoked processing fluency, increasing the impact of the perceived cost of congestion in the user decision-making through two mechanisms: First, when immediacy of CI is high (vs. low), the increased processing fluency makes the CI more likely to be assessed as true, resulting in increased perceived validity of the CI (Hansen & Wänke, 2010). As a result, when immediacy is high (vs. low), ambiguity on the cost of congestion and related optimism bias – which makes “people interpret ambiguous information or uncertain situations in a self-serving direction” (Rhee et al., 2005, p. 13) – is reduced (e.g. “this usually highly crowded location might not be that crowded today” vs. “this highly crowded location is actually crowded right now”). Consequently, more crowded locations appear to have higher costs of congestion and thus are less attractive. Second, when immediacy of CI is high (vs. low), the increased processing fluency helps in comprehending the cost implications of diferent crowding levels, which requires an efortful reasoning process (Cheung et al., 2014; Kahneman, 2011) in contrast to the heuristically processed quality signal of demand (Sun, 2013). Therefore, the increased processing fluency due to high (vs. low) immediacy of CI causes the diferent costs of congestion at each location to be processed better, making less crowded locations more attractive. In conclusion, when the immediacy of CI is high (vs. low), users are more likely to selec less crowded locations.

H2: Users are more likely to select less crowded locations when immediacy of CI is high (vs. low).

## 3.3. The moderating role of health anxiety

As presented in the theoretical background, we refer to health anxiety as a user’s exaggerated perception of the likelihood and severity of contracting a disease such as COVID-19, resulting in a closer hypothetical distance and a more concrete conception of the health risk associated with visiting locations (Abramowitz et al., 2007; Trope & Liberman, 2010).

Building on these insights, we argue that the more health anxious a user is, the more likely will the user be to select a more crowded location in the presence of highly immediate CI. When immediacy is low, processing fluency is similarly impeded for users of any level of health anxiety and consequently leads to comparable selections between users. On the other hand, when immediacy is high and thus processing fluency increased, we believe that health anxiety amplifies the deterring efect of high immediacy mentioned in H2. This is because users with high (vs. low) levels of health anxiety give even more weight to costs of congestion when immediacy of CI is high, as they think more concretely about the infection risk (e.g. “how could I get infected at each location”). As such, health anxious users are deterred particularly strongly from selecting crowded locations in the presence of highly immediate CI.

H3: Health anxiety moderates the efect of immediacy of CI on location selection, such that more health anxious users are more likely to select less crowded locations when CI is immediate.

## 4. Method

To test our hypotheses, we conducted a betweensubject online experiment with three conditions investigating the efect of CI and related immediacy cues on selecting diferently crowded medical practices. We chose participants from Germany and Italy as the severity of the pandemic difers between the two otherwise comparable European countries,<sup>3</sup> thereby allowing us to test our findings for robustness against cultural diferences and diferences due to the impact and stage of the COVID-19 pandemic in the respective countries. We collected our data in the first week of June 2020, when physical distancing policies were in place to cope with the COVID-19 pandemic.

We chose to investigate the selection of medical practices for three reasons: First, COVID-19 is primarily transmitted between people during close contact, especially by coughing and sneezing (ECDC, 2020; WHO, 2020). As such, the risk of infection in waiting rooms of medical practices filled with potentially ill patients is significant (Shaw, 2019). Second, users who plan to visit a medical practice often have an urgent need to avoid their condition from deteriorating (Wong et al., 2020) and therefore particularly value information (e.g. CI) aiding their spontaneous decision. Third, as the quality of diferent medical practices is hard to assess in advance, users strongly rely on information about others’ behaviours to make a decision (X. Li & Wu, 2018).

## 4.1. Experimental DSS and manipulations

We created a fictitious website “find-your-doctor.org” for the purpose of the experiment. The website claimed to support its users with a map showing diferent medical practices with no further details on crowding levels in the control condition (i.e. CI absent). In the two treatment conditions, we operationalised CI with four crowding levels using manikin icons symbolising “few” (1 manikin) to “many” (4 manikins) patients at each respective medical practice. Similarly, we operationalised immediacy of CI with an immediacy cue displaying “usual amount of patients (past 2 months)” in the case of historical average CI and “live amount of patients (updated just now)” in the case of real-time CI. See Figure 2 for details on all three conditions.

## 4.2. Experimental procedure

Figure 3 visualises the experimental procedure: (1) First, we explained the online experiment to the participants, ascertained anonymity and asked them to consider going to a medical practice because of an intensified back pain. As their usual medical practice was claimed to be closed, participants were asked to look for an alternative in their proximity by using our experimental website. (2) Next, participants were randomly assigned to one of the three treatment groups and were introduced to the general layout of the website including – if applicable – CI and immediacy cues. (3) Thereafter, we presented participants the map, manipulated in accordance to their condition and showing four medical practices as well as the participant’s own (fictitious) location. We also pointed out that all medical practices were comparable with respect to distance, capacity and specialisation. Participants then selected the medical practice they would preferably go to. (4) To conclude, participants completed a questionnaire covering their perceptions of the selection process as well as manipulation checks and controls.

![](/api/attachments/J5NYHVAP/fulltext/images/4cb6d534d6115b7e3280a90c606a3b93417f52ea48baa37a8f98d9f00b3f7e8d.jpg)  
Figure 2. Manipulations.

![](/api/attachments/J5NYHVAP/fulltext/images/5f2ef365d9010d38f9a4eae137f02b9183e8b5b7deeffaaa4294d5eeda85e3d5.jpg)  
Figure 3. Experimental procedure.

## 4.3. Measurements

We measured our dependent variable location selection by recording which of the four given medical practices participants selected (i.e. which crowding level they selected). As our moderating variable, we measured participants’ health anxiety (Abramowitz et al., 2007), rated on a seven-point Likert-type scale ranging from strongly disagree (1) to strongly agree (7). As controls we measured participants’ country of residence (Germany vs. Italy), the time participants spent reading the instructions and selecting a medical practice and participants’ product involvement (Zaichkowsky, 1985) towards medical practices using three bipolar items rated on a seven-point scale. In addition, we asked for participants’ age, given the widespread conception that particularly older people are at higher risk for severe illness caused by COVID-19 (WHO, 2020) which may impact their selection behaviour beyond their overall health anxiety. Furthermore, we used seven-point Likert-type scales to measure three manipulation checks: perceived crowding of the most crowded location (Machleit et al., 2000), perceived immediacy of the CI (Y. Lee & Strong, 2003) as well as processing fluency (A. Lee & Aaker, 2004). Table A1 lists all employed items. Besides, we included four attention checks to identify how carefully the participants read each item and understood the visualisations. Lastly, we asked how realistic participants perceived the scenario.

## 5. Analysis and results

## 5.1. Sample description

We recruited 360 participants from the crowdsourcing platform Prolific.co which ofers a particularly suitable environment for experiments in behavioural research with survey results providing reliable, high-quality data (Palan & Schitter, 2017; Peer et al., 2017). We limited participation to participants with German or Italian residency as well as a high approval rating of 95% or more to ensure high data quality (Goodman & Paolacci, 2017). Out of the 360 participants, 343 passed all four attention checks. Table A2 summarises the descriptive statistics of our conditions.

Two one-way analyses of variance for the control variables provide evidence of comparability and balance across our three conditions, as we did not find significant diferences $\mathrm { ( p > 0 . 1 ) }$ in terms of participants’ age, product involvement, and health anxiety. Therefore, we find support for the successful randomisation of assignment to the experimental conditions. We also conducted three manipulation checks: Perceived crowding was significantly higher for the two CI-present-conditions than for the CI-absent condition (p < 0.001) and perceived immediacy was significantly higher for the CI real-time condition than for the CI historical average condition (p < 0.001). As such, our experimental treatments worked as intended. Additionally, participants confirmed that they found the experiment realistic (mean = 5.60; SD = 1.63). Comparing the results for the two countries included in our sample (Germany and Italy), we found no significant diference (p > 0.05) in selection behaviour, manipulation checks or age, except for Italian participants being more health anxious and exhibiting a greater product involvement towards medical practices than their German counterparts (p < 0.001), which likely reflects the diferences in severity of the COVID-19 pandemic in the two countries.

## 5.2. Reliability and validity

A confirmatory factor analysis provided evidence for adequate convergent and discriminant validities. For convergent validity, the values of average variance extracted (AVE) were all above the threshold of 0.50 and the loadings of all items were significant (p < 0.01) and above the recommended level of 0.70. For internal consistency, the values of composite reliability and Cronbach’s α were all greater than the threshold of 0.70. Discriminant validity was assessed using Heterotrait-Monotrait (HTMT) analysis with all values below the recommended maximum of 0.90.

## 5.3. Hypothesis testing

We coded our independent variables CI and immediacy of CI as binary variables (i.e. CI absent = 0, CI present = 1; historical average = 0, real-time = 1). We coded our dependent variable location selection as an ordinal variable with four levels (i.e. crowding level of selected location 0%, 33%, 67%, 100%). To test our hypotheses, we used ordinal logistic regression, ensuring that all required assumptions were met, including proportional odds (Lund & Lund, 2020). In addition, we found good model fit through a significant improvement of the final model containing the full set of predictors compared to an intercept-only model (p < 0.001) and non-significant test-results of the Deviance chi-square test and the Pearson chi-square test (p > 0.1).

Table 1 provides the results of three ordinal logistic regressions on location selection. Model 1 includes all conditions and compares the efect of presence vs. absence of CI. Model 2 focuses on the CI-present conditions to analyse the main efect of immediacy of CI. Model 3 furthermore considers the moderating efect of users’ health anxiety on immediacy. The regression estimates represent the predicted change in logarithmic odds of selecting a more crowded location per unit increase on the independent variable. In other words, the higher the estimate of an independent variable, the higher is the probability of selecting a more crowded location.

The results of model 1 support H1 in that presence (vs. absence) of CI makes users 4.6 (=exp(1.52)) times as likely to select a less crowded location. Looking more closely how CI is processed at diferent levels of immediacy, the results of model 2 support H2 in that higher levels of immediacy lead to selecting less crowded locations.<sup>4</sup> However, contrary to H3, the results of model 3 indicate that health anxiety does not amplify the efect of high immediacy. Instead, the results suggest a significant opposite efect, in that when real-time (vs. historical average) CI is provided and health anxiety is low (i.e. one standard deviation below mean, at a level of 2.36), users are 6.4 (=exp(2.80 +(−0.40)\*2.36)) times as likely to select less crowded locations. In contrast, when users exhibit high health anxiety (i.e. one standard deviation above mean, at a level of 4.76), real-time (vs. historical average) CI makes users only 2.5 (=exp(2.80+(−0.40)\*4.76)) times as likely to select less crowded locations. We, therefore, reject H3. See Figure 4 for the interaction plot.

Table 1. Ordinal logistic regression on location selection.

<table><tr><td rowspan="2">Independent variables</td><td colspan="2">Model 1</td><td colspan="2">Model 2</td><td colspan="2">Model 3</td></tr><tr><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td><td>Estimate</td><td>Std. error</td></tr><tr><td>CI</td><td>-1.52***</td><td>0.23</td><td>-</td><td>-</td><td>-</td><td>-</td></tr><tr><td>Immediacy of CI</td><td>-</td><td>-</td><td>-1.35***</td><td>0.28</td><td>-2.80**</td><td>0.88</td></tr><tr><td>Immediacy of CI x Health anxiety</td><td>-</td><td>-</td><td>-</td><td>-</td><td> $0.40^†$ </td><td>0.23</td></tr><tr><td>Controls</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Health anxiety</td><td>0.04</td><td>0.09</td><td>0.14</td><td>0.12</td><td>-0.03</td><td>0.16</td></tr><tr><td>Age</td><td>0.02</td><td>0.01</td><td>0.04*</td><td>0.02</td><td>0.04*</td><td>0.02</td></tr><tr><td>Country of residence</td><td>0.06</td><td>0.21</td><td>-0.23</td><td>0.27</td><td>-0.25</td><td>0.27</td></tr><tr><td>Product involvement</td><td>0.12</td><td>0.08</td><td>0.05</td><td>0.11</td><td>0.03</td><td>0.11</td></tr><tr><td>Time instructions</td><td>0.00</td><td>0.00</td><td>-0.01*</td><td>0.00</td><td>-0.01*</td><td>0.00</td></tr><tr><td>Time selection</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Pseudo  $R^2$ </td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Cox &amp; Snell</td><td>0.14</td><td></td><td>0.15</td><td></td><td>0.16</td><td></td></tr><tr><td>Nagelkerke</td><td>0.16</td><td></td><td>0.16</td><td></td><td>0.18</td><td></td></tr><tr><td>McFadden</td><td>0.06</td><td></td><td>0.07</td><td></td><td>0.08</td><td></td></tr></table>

Note: <sup>†</sup>p < 0.1, \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

![](/api/attachments/J5NYHVAP/fulltext/images/6ed9601c377249f139163dffab826ca8e13bf100523b2add6485a0797bab3e54.jpg)  
Figure 4. Interaction plot of real-time vs. historical average CI and users’ health anxiety.

## 6. Discussion

Does the presence (vs. absence) of CI in DSS make users more or less likely to select less crowded locations? And, if the presence of CI makes users more likely to select less crowded locations, at what levels of immediacy and users' health anxiety is CI mos efective? Our study addresses these two questions and provides robust findings – across Germany and Italy – that largely support our assertion that CI displayed in DSS can facilitate physical distancing and thus help in containing the COVID-19 pandemic. We demonstrate the causal efect of CI on selection behaviour, in that people are 4.6 times as likely to select less crowded places when CI is present (vs. absent). Whereas high (vs. low) immediacy amplifies the efect of CI, we surprisingly find that under high immediacy of CI, health anxiety increasingly draws users to select more crowded locations. Indeed, real-time (vs. historical average) CI makes users with high health anxiety only 2.5 times as likely to select less crowded places compared to 6.4 times when health anxiety is low. In light of this counterintuitive finding, we speculate that when faced with highly immediate CI, more health anxious users may use the increased processing fluency to put greater emphasis on the quality of each location than their less health anxious peers. In other words, for a high (vs. low) health anxious user, when immediacy and thus processing fluency is high, visiting any location inherently bears an acute uncertainty and high infection risk (e.g. “no matter where I go, I run a high risk of getting infected anyway”), so that they select more crowded locations to comfort their health anxiety, given that the higher demand can be interpreted as a signal of high quality (e.g. Bikhchandani et al., 1992; X. Li & Wu, 2018; Thies et al., 2016).

## 6.1. Practical implications for managing the COVID-19 pandemic

By uncovering how displaying CI shapes selection behaviour, our findings ofer pragmatic insights and actionable implications for DSS providers and policymakers to achieve an immediate impact on containing the COVID-19 pandemic. As such, we add to the emerging body of initiatives on IS in the age of pandemics (e.g. Laato et al., 2020; Naidoo, 2020; Trang et al., 2020) and answer the call of Ågerfalk et al. (2020) for IS studies to generate urgently required impetus that can immediately support practitioners in the fight against the COVID-19 pandemic and beyond. Our contributions are summarised in Table 2.

First, our study highlights CI as a powerful tool for DSS providers and policymakers to facilitate physical distancing by endowing their citizens with information to identify and select less crowded places. In the past, policymakers mainly focused on whether or not it is necessary to enforce physical distancing through traditional paternalistic interventions like lockdowns and curfews as ultima ratio. Our insights now provide a more liberal, state-of-the-art solution that supports users in their physical distancing eforts without infringing their personal freedom of choice. As such, DSS providers who display CI in general, and highly immediate CI in particular, enable a self-regulating mechanism for users to unwittingly contribute to the containment of COVID-19, thus complementing and partially mitigating the necessity of paternalistic governmental interventions. Moreover, this approach not only helps to safeguard civil rights, but also allows policymakers to avert economic loss, such as from forcing service providers to (temporarily) close shops. Moreover, while this risk containment is particularly relevant to control pandemics like COVID-19, it can also serve to curb the spread of other infectious diseases (e.g. seasonal flues). As such, our findings are valuable to protect individuals within and beyond the context of pandemics.

Second, our study urges DSS providers and policymakers to consider the role of health anxiety and its efects on processing information in IS in times of COVID-19. In particular, DSS providers and policymakers can learn from our insights that immediate CI is most efective in encouraging the selection of less crowded locations when users have not (yet) built high levels of health anxiety. We conjecture that this counterintuitive efect is caused by health anxiety urging users to place greater emphasis on the quality of each location, which users infer from the level of crowding. As anxiety may increase throughout the stages of a pandemic, immediate CI is probably most efective at the beginning of a pandemic, when the estimates of the likelihood and severity of having an illness have not yet reached exaggerated levels, but also at later stages, such as after the first or second wave of a pandemic, when users turn back to old habits and beliefs. Still, our results inform DSS providers and policymakers that displaying CI is better than not displaying CI and that the more immediate the CI, the merrier – even if users exhibit high levels of health anxiety.

Table 2. Summary of the main contributions of the current study.

<table><tr><td></td><td>Existing thinking/practice</td><td>Contribution of this paper</td></tr><tr><td colspan="3">COVID-19 practical implications</td></tr><tr><td>Containment strategy</td><td>Policy makers mainly focused on whether or not it is necessary to enforce physical distancing through traditional paternalistic interventions like lockdowns and curfews as ultima ratio (Our World in Data, 2020).</td><td>Our insights unveil a self-regulating mechanism for users to unwittingly contribute to the containment of COVID-19, thus complementing and partially mitigating the necessity of paternalistic governmental interventions.</td></tr><tr><td>Collection of information</td><td>Policy makers are encouraged to develop and refine IS and technologies to collect and analyse disease status data, such as infections, recoveries and deaths (Pietz et al., 2020).</td><td>We extend the range of information required to successfully combat the pandemic by highlighting the role of CI in DSS as an implicit warning signal of infection risk.</td></tr><tr><td>Communication of information</td><td>Pandemic-related information must not only be collected and analysed, but also communicated to the general public in real-time to encourage behaviour compliant with policies and recommendations (Pietz et al., 2020).</td><td>We confirm the criticality of providing timely information by demonstrating the effect of displaying CI and by uncovering how real-time (vs. historical average) information elicits a more desired response.</td></tr><tr><td>Cognitive processing of information</td><td>Substantial resources are directed towards IS increasing the transparency of infection risk, for example, by promoting disease status dashboards (Pietz et al., 2020) and by optimising communication strategies to increase user adoption of tracing apps (Trang et al., 2020).</td><td>We build on this unprecedented level of transparency of infection risk and study its implications by investigating user selection behaviour in light of differently crowded locations. Thereby, we shed light on the processing of and reaction to DSS-provided information.</td></tr><tr><td>Influence of health anxiety</td><td>During the COVID-19 pandemic, health anxiety has emerged as a critical factor influencing user attitudes and behaviour, for example, with respect to spreading information online (Laato et al., 2020) and accepting tracing apps (Trang et al., 2020).</td><td>We confirm the relevance of taking users&#x27; health anxiety into account when investigating their behaviour in the context of COVID-19. Specifically, we uncover a surprising tendency of health anxious users to engage less in physical distancing when presented with real-time information, thereby emphasising the intriguing influence of users&#x27; health anxiety in interactions with DSS on real-world location selection.</td></tr><tr><td colspan="3">Theoretical contributions beyond COVID-19</td></tr><tr><td>Contextual information</td><td>Context may alter users&#x27; usual processing of information and thus users&#x27; selection behaviour (e.g. Hong et al., 2014; Thaler &amp; Sunstein, 2009; Tversky &amp; Kahneman, 1973). Previous research indicated that time-related contextual information in digital choice environments (e.g. timestamps and countdowns) affect user behaviour (e.g. Amirpur &amp; Benlian, 2015; Chen et al., 2011; G. Li &amp; Wang, 2019).</td><td>We corroborate the importance of considering context by uncovering that temporal context shaped through immediacy cues can alter user decision-making in digital choice environments. As such, we unveil immediacy of dynamically changing information as a new facet of previously investigated time-related contextual information.</td></tr><tr><td>Demand information</td><td>Previous research investigating demand-related information concentrated on how the display of demand sparks users&#x27; perceptions of quality and thus draws users to select highly demanded options (e.g. X. Li &amp; Wu, 2018; Thies et al., 2016).</td><td>Our study is among the first to investigate CI as a new and increasingly prevalent DSS feature comparing current demand to available capacity and thus reflecting so far disregarded costs of congestion.</td></tr><tr><td>Construal level theory</td><td>The multitude of studies investigating construal level theory largely analysed psychological distances in isolation and separately (see Huang et al. (2018) for an overview).</td><td>We extend our understanding of multiple psychological distances by examining the joint effect of temporal distance and hypothetical distance on user information processing and decision making.</td></tr></table>

Third and last, service providers such as medical practitioners benefit from users selecting less crowded locations: Crowding levels are more equally distributed across all locations and thereby allow service providers to optimise their planning and service ofering to efectively operate despite an ongoing pandemic. As such, service providers should consider to actively participate in the endowment of users through IS, for instance, by sharing CI with DSS providers.

## 6.2. Research and theoretical contributions

Our study also ofers theoretical contributions with a particular consideration of the context of COVID-19, whose context-specific influences may alter users usual processing of information and thus selection behaviour (e.g. Hong et al., 2014; Thaler & Sunstein, 2009; Tversky & Kahneman, 1973).

First, we advance our understanding of how DSS as digital choice environments influence selection behaviour. Whereas previous research on digital choice environments mainly analysed how demand-related information sparks perceptions of quality (e.g. X. Li & Wu, 2018; Thies et al., 2016), we introduce CI as an increasingly prevalent DSS feature during COVID-19 which compares current demand to available capacity and thus additionally reflects associated costs of congestion. Furthermore, we shed light on the impact of diferent levels of immediacy of CI on users’ processing. Specifically, higher immediacy of CI (e.g. realtime) seems to induce a more vivid perception of crowding and its related costs. Crowded locations are thus perceived as more deterring – especially in times of the COVID-19 pandemic where infection risks soar.

Second, we extend construal level theory by unveiling immediacy as a new facet of previously investigated temporal cues (e.g. Amirpur & Benlian, 2015; Chen et al., 2011; G. Li & Wang, 2019) and by examining the joint efect of two dimensions of psychological distance (i.e. temporal and hypothetical distance) by further considering the efect of health anxiety during the COVID-19 pandemic. As such, our joint investigation of two dimensions extends the multitude of studies that largely analyse psychological distances in isolation and separately (see Huang et al. (2018) for an overview).

## 6.3. Limitations and directions for future research

Our study to explore the role of CI is subject to limitations that ofer directions for future research. First, our results are based on an online experiment conducted with participants from two European countries with largely comparable COVID-19 policies, in which users selected among diferently crowded medical practices. Future research could extend the generalisability of our findings by testing our hypotheses in a field setting, potentially involving countries with diferent governmental approaches and cultural contexts, and by investigating further real-world locations where physical distancing is required and where interaction among visitors is considered part of the experience, such as in the case of restaurants and bars. More importantly, field data are required to assess whether the observed efects of displaying CI are strong enough to circumvent lockdowns and curfews.

Second, whilst our study focused on the main efect of CI on selection behaviour under varying levels of immediacy of CI as well as users’ health anxiety, we encourage future research to uncover underlying and interacting efects. Specifically, insights on the mediating role of diferent types of costs of congestions (e.g. wait times, infection risks), the extent to which DSS can influence users’ health anxiety in the long run and potentially at diferent stages of the pandemic as well as the broader role of health anxiety in user decisionmaking would be valuable to extend our findings.

Third, ofering up to real-time CI across several locations mandates centralised data collection and automated processing, which requires substantial data infrastructure investments and approval of users or service providers to the collection. Even though these barriers have been conquered by large DSS providers like Google, most service providers are dependent on collaborating with other parties (e.g. service providers, DSS providers). As such, future research could account for these restrictions by examining eforts that are needed to fulfil the infrastructural and legal requirements when several parties are involved.

## 7. Conclusion

DSS have become increasingly relevant to help in containing the COVID-19 pandemic. To contribute to the emergent discussion and “war” against the invisible enemy, our study investigates whether and how displaying CI in DSS afects selections of realworld locations and thus encourages physical distancing. Specifically, by conducting an online experiment with participants from two European countries, we empirically show not only that present (vs. absent) CI causally afects the selection of less crowded locations, but also that immediacy of CI and health anxiety play an influential role in the overall efect of displaying CI. Beyond the impetus for scholars to better understand user behaviour in digital environments, our study first and foremost provides insights into levers of IS that have immediate impact on containing the COVID-19 pandemic.

## Notes

1. https://www.who.int/emergencies/diseases/novelcoronavirus-2019/advice-for-public

2. Often referred to as “social distancing“ in media. We refrain from using the term social distancing, because information and communication technologymediated social interactions (e.g. phone, chat, video streaming) are not restrained by the COVID-19 pandemic.

3. As of June 20<sup>th</sup>, 2020, Italy reported 58 COVID-19- related deaths per 100,000 citizens, whereas Germany reported only 11 COVID-19-related deaths per 100,000 citizens (Johns Hopkins University, 2020).

4. In a separate analysis, we find that processing fluency is significantly higher for real-time rather than historical average CI (p < 0.001), indicating support for our proposition of enhanced construal fit.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Martin Adam http://orcid.org/0000-0001-9369-7203 Dominick Werner http://orcid.org/0000-0002-4605- 5395

Charlotte Wendt http://orcid.org/0000-0003-2271-5253 Alexander Benlian http://orcid.org/0000-0002-7294- 3097

## References

Abramowitz, J., Deacon, B., & Valentiner, D. (2007). The short health anxiety inventory: Psychometric properties and construct validity in a non-clinical sample. Cognitive Therapy and Research, 31(6), 871–883. https://doi.org/10. 1007/s10608-006-9058-1

Ågerfalk, P., Conboy, K., & Myers, M. (2020). Information systems in the age of pandemics: COVID-19 and beyond. European Journal of Information Systems, 29(3), 203–207. https://doi.org/10.1080/0960085x.2020.1771968

Amirpur, M., & Benlian, A. (2015). Buying under pressure: Purchase pressure cues and their efects on online buying decisions. In ICIS 2015 proceedings. Fort Worth, TX, US.

Bar-Anan, Y., Liberman, N., & Trope, Y. (2006). The association between psychological distance and construal level: Evidence from an implicit association test. Journal of Experimental Psychology, 135(4), 609–622. https://doi. org/10.1037/0096-3445.135.4.609

Bayham, J., Kuminof, N., Gunn, Q., & Fenichel, E. (2015). Measured voluntary avoidance behaviour during the 2009 A/H1N1 epidemic. Biological Sciences Proceedings, 282(1818). https://doi.org/10.1098/rspb.2015.0814

BBC. (2020). Coronavirus: Crowdless app ofers shoppers supermarket crowd levels [online]. Retrieved June 18, 2020, from https://www.bbc.com/news/uk-englandoxfordshire-52446658

Becker, G. (1991). A note on restaurant pricing and other examples of social influences on price. Journal of Political Economy, 99(5), 1109–1116. https://doi.org/10.1086 261791

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. Journal of Political Economy, 100(5), 992–1026. https://doi.org/10.1086/261849

Broniarczyk, S., & Grifin, J. (2014). Decision dificulty in the age of consumer empowerment. Journal of Consumer Psychology, 24(4), 608–625. https://doi.org/10.1016/j. jcps.2014.05.003

Casson, M. (1982). The entrepreneur: An economic theory. Barnes & Noble Books.

Chen, X., & Davison, R. (2019). Self-awareness or context-awareness? The role of awareness in herd behavior. In ICIS 2019 proceedings, Munich, Germany.

Chen, Y., Wang, Q., & Xie, J. (2011). Online social interactions: A natural experiment on word of mouth versus observational learning. Journal of Marketing Research, 48(2), 238–354. https://doi.org/10.2139/ssrn.1501843

Cheung, C., Xiao, B., & Liu, I. (2014). Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase decisions. Decision Support Systems, 65, 50–58. https://doi.org/10. 1016/j.dss.2014.05.002

D’Angelo, J., & West, D. (2000). Mathematical thinking: Problem-solving and proofs (2nd ed.). Prentice Hall.

Davidson, H. (2020). Around 20% of global population under coronavirus lockdown [online]. Retrieved July 1, 2020, from https://www.theguardian.com/world/2020/mar/24 nearly-20-of-global-population-under-coronaviruslockdown

Duan, W., Gu, B., & Whinston, A. (2009). Informational cascades and software adoption on the internet: An empirical investigation. MIS Quarterly, 33(1), 23–48. https://doi.org/10.2307/20650277

ECDC. (2020). European centre for disease prevention and control: Q&A on COVID-19 [online]. Retrieved June 18, 2020, from https://www.ecdc.europa.eu/en/covid-19 questions-answers

Goodman, J., & Paolacci, G. (2017). Crowdsourcing consumer research. Journal of Consumer Research, 44(1), 196–210. https://doi.org/10.1093/jcr/ucx047

Google. (2020). Popular times, wait times, and visit duration [online]. Retrieved June 18, 2020, from https://support. google.com/business/answer/6263531?hl=en

Hansen, J., & Wänke, M. (2010). Truth from language and truth from fit: The impact of linguistic concreteness and level of construal on subjective truth. Personality and Social Psychology Bulletin, 36(11), 1576–1588. https:// doi.org/10.1177/0146167210386238

Hong, W., Chan, F., Thong, J., Chasalow, L., & Dhillon, G. (2014). A framework and guidelines for context-specific

theorizing in information systems research. Information Systems Research, 25(1), 111–136. https://doi.org/10. 1287/isre.2013.0501

Huang, L., Tan, C.-H., Ke, W., & Wei, K. (2018). Helpfulness of online review content: The moderating efects of temporal and social cues. Journal of the Association for Information Systems, 19(6), 503–522. https://doi.org/10.17705/1jais.00499

Johns Hopkins University. (2020). COVID-19 Dashboard by the CSSE at JHU [online]. Retrieved June 26, 2020, from https://gisanddata.maps.arcgis.com/apps/opsdashboard/ index.html#/bda7594740fd40299423467b48e9ecf6

Kahneman, D. (2011). Thinking, fast and slow. Macmillan.

Khurana, S., Qiu, L., & Kumar, S. (2019). When a doctor knows, it shows: An empirical analysis of doctors responses in a Q&A forum of an online healthcare portal. Information Systems Research, 30(3), 872–891. https:// doi.org/10.1287/isre.2019.0836

Kim, H., Rao, A., & Lee, A. (2009). It’s time to vote: The efect of matching message orientation and temporal frame on political persuasion. Journal of Consumer Research, 35(6), 877–889. https://doi.org/10.1086/593700

Laato, S., Islam, A., Islam, M., & Whelan, E. (2020). What drives unverified information sharing and cyberchondria during the COVID-19 pandemic? European Journal of Information Systems, 29(3), 288–305. https://doi.org/10. 1080/0960085x.2020.1770632

Lau, J., Grifiths, S., Choi, K., & Tsui, H. (2010). Avoidance behaviors and negative psychological responses in the general population in the initial stage of the H1N1 pandemic in Hong Kong. BMC Infectious Diseases, 10(139), 1–13. https://doi.org/10.1186/1471-2334-10-139

Lee, A., & Aaker, J. (2004). Bringing the frame into focus: The influence of regulatory fit on processing fluency and persuasion. Journal of Personality and Social Psychology, 86(2), 205–218. https://doi.org/10.1037/0022-3514.86.2.205

Lee, A., Keller, P., & Sternthal, B. (2010). Value from regulatory construal fit: The persuasive impact of fit between consumer goals and message concreteness. Journal of Consumer Research, 36(5), 735–747. https://doi.org/10. 1086/605591

Lee, Y., & Strong, D. (2003). Knowing-why about data processes and data quality. Journal of Management Information Systems, 20(3), 13–39. https://doi.org/10. 1080/07421222.2003.11045775

Li, G., & Wang, J. (2019). Threshold efects on backer motivations in reward-based crowdfunding. Journal of Management Information Systems, 36(2), 546–573. https://doi.org/10.1080/07421222.2019.1599499

Li, J., Tang, J., Jiang, L., Yen, D., & Liu, X. (2019). Economic success of physicians in the online consultation market: A signaling theory perspective. International Journal of Electronic Commerce, 23(2), 244–271. https://doi.org/10. 1080/10864415.2018.1564552

Li, X., & Wu, L. (2018). Herding and social media word-ofmouth: Evidence from groupon. MIS Quarterly, 42(4), 1331–1351. https://doi.org/10.25300/MISQ/2018/14108

Lund, A., & Lund, M. (2020). Ordinal regression using SPSS statistics [online]. Retrieved April 20, 2020, from https:// statistics.laerd.com/spss-tutorials/ordinal-regression using-spss-statistics.php

Machleit, K., Eroglu, S., & Mantel, S. (2000). Perceived retail crowding and shopping satisfaction: What modifies this relationship? Journal of Consumer Psychology, 9(1), 29–42. https://doi.org/10.1207/s15327663jcp0901\_3

McDonald, R., Chai, H., & Newell, B. (2015). Personal experience and the ‘psychological distance’ of climate

change: An integrative review. Journal of Environmental Psychology, 44, 109–118. https://doi.org/10.1016/j.jenvp. 2015.10.003

Morganstein, J., Fullerton, C., Ursano, R., Donato, D., & Holloway, H. (2017). Pandemics: Health care emergencies. In B. Raphael, C. S. Fullerton, L. Weisaeth, & R. J. Ursano Eds., Textbook of disaster psychiatry (2 ed., pp. 270–284). Cambridge University Press. https://doi. org/10.1017/9781316481424.019

Naidoo, R. (2020). A multi-level influence model of COVID-19 themed cybercrime. European Journal of Information Systems, 29(3), 306–321. https://doi.org/10. 1080/0960085x.2020.1771222

NSW. (2020). Emergency department waiting times in major NSW hospitals [online]. Retrieved April 16, 2020, from https://www.emergencywait.health.nsw.gov.au/#a

Our World in Data. (2020). COVID-19: Government response stringency index [online]. Retrieved July 29 2020, from https://ourworldindata.org/grapher/covid-stringencyindex

Palan, S., & Schitter, C. (2017). Prolific.ac - A subject pool for online experiments. Journal of Behavioral and Experimental Finance, 17, 22–27. https://doi.org/10.1016 j.jbef.2017.12.004

Parboteeah, D., Valacich, J., & Wells, J. (2009). The influence of website characteristics on a consumer’s urge to buy impulsively. Information Systems Research, 20(1), 60–78. https://doi.org/10.1287/isre.1070.0157

Peer, E., Brandimarte, L., Samat, S., & Acquisti, A. (2017). Beyond the turk: Alternative platforms for crowdsourcing behavioral research. Journal of Experimental Social Psychology, 70, 153–163. https://doi.org/10.1016/j.jesp. 2017.01.006

Pennic, F. (2020). New app prevents exposure to coronavirus in medical waiting rooms [online]. Retrieved June 18, 2020, from https://hitconsultant.net/2020/03/17/newapp-prevents-exposure-to-coronavirus-in-medicalwaiting-rooms/#.Xut7zWgzZm9

Pietz, J., McCoy, S., & Wilck, J. (2020). Chasing John Snow: Data analytics in the COVID-19 era. European Journal of Information Systems. https://doi.org/10.1080/0960085X. 2020.1793698

Qiu, L., Shi, Z., & Whinston, A. (2018). Learning from your friends’ check-ins: An empirical study of location-based social networks. Information Systems Research, 29(4), 1044–1061. https://doi.org/10.1287/isre.2017.0769

Rhee, H.-S., Ryu, Y., & Kim, C. (2005). I am fine but you are not: Optimistic bias and illusion of control on information security. In ICIS 2005 proceedings, Las Vegas, NV, USA.

Semin, G., Higgins, E., De Montes, G., Estourget, L., & Valencia, J. (2005). Linguistic signatures of regulatory focus: How abstraction fits promotion more than prevention. Journal of Personality and Social Psychology, 89(1), 36–45. https://doi.org/10.1037/0022-3514.89.1.36

Shaw, D. (2019). The hidden risks of the waiting room: Confidentiality and cross-infection. British Journal of General Practice, 69(683), 299. https://doi.org/10.3399 bjgp19X703925

Spinney, L. (2020). Bleach baths and drinking hand sanitiser: Poison centre cases rise under Covid-19 [online]. Retrieved June 29, 2020, from https://www.theguardian.com/world 2020/jun/08/bleach-baths-and-drinking-hand-sanitiserpoison-centre-cases-rise-under-covid-19

Sun, H. (2013). A longitudinal study of herd behavior in the adoption and continued use of technology. MIS

Quarterly, 37(4), 1013–1041. https://doi.org/10.25300/ MISQ/2013/37.4.02

Thaler, R., & Sunstein, C. (2009). Nudge: Improving decisions about health, wealth, and happiness. Penguin.

Thies, F., Wessel, M., & Benlian, A. (2016). Efects of social interaction dynamics on platforms. Journal of Management Information Systems, 33(3), 843–873. https://doi.org/10.1080/07421222.2016.1243967

Trang, S., Trenz, M., Weiger, W., Tarafdar, M., & Cheung, C. (2020). One app to trace them all? Examining app specifications for mass acceptance of contact-tracing apps. European Journal of Information Systems. https://doi.org/ 10.1080/0960085X.2020.1784046

Transit. (2020). You can avoid crowds on public transit with new, real-time crowding info [online]. Retrieved June 18, 2020, from.https://medium.com/transit-app/you-canavoid-crowds-on-public-transit-with-new-real-timecrowding-info-b61e60f5502

Trope, Y., & Liberman, N. (2003). Temporal construal. Psychological Review, 110(3), 403–421. https://doi.org/ 10.1037/0033-295X.110.3.403

Trope, Y., & Liberman, N. (2010). Construal-level theory of psychological distance. Psychological Review, 117(2), 440–463. https://doi.org/10.1037/a0018963

Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. Cognitive Psychology, 5(2), 207–232. https://doi.org/10. 1016/0010-0285(73)90033-9

Villarica, H. (2011). Study of the day: There are no winners in an overcrowded mall. The Atlantic. Retrieved April 16, 2020, from https://www.theatlantic.com/health/archive/ 2011/12/study-of-the-day-there-are-no-winners-in-anovercrowded-mall/250217/

Walden, E., & Browne, G. (2009). Sequential adoption theory: A theory for understanding herding behavior in early adoption of novel technologies. Journal of the Association for Information Systems, 10(1), 31–62. https://doi.org/10. 17705/1jais.00181

Wang, I., & Ackerman, J. (2019). The infectiousness of crowds: Crowding experiences are amplified by pathogen threats. Personality and Social Psychology Bulletin, 45(1), 120–132. https://doi.org/10.1177/0146167218780735

Weimer, D., & Vining, A. (2005). Policy analysis: Concepts and practice (4th ed.). Prentice Hall.

Wheaton, M., Abramowitz, J., Berman, N., Fabricant, L., & Olatunji, B. (2011). Psychological predictors of anxiety in response to the H1N1 (Swine Flu) pandemic. Cognitive Therapy and Research, 36(3), 210–218. https://doi.org/10. 1007/s10608-011-9353-3

WHO. (2020). Q&A on coronaviruses (COVID-19) [online]. Retrieved June 18, 2020, from https://www.who.int/emer gencies/diseases/novel-coronavirus-2019/question-andanswers-hub/q-a-detail/q-a-coronaviruses

Wong, L., Hawkins, J., Langness, S., Murrell, K., Iris, P., & Sammann, A. (2020). Where are all the patients? Addressing Covid-19 fear to encourage sick patients to seek emergency care. NEJM Catalyst, 1(3), 1–12. https:// doi.org/10.1056/CAT.20.0193

Yu, Q., Allon, G., Bassamboo, A., & Iravani, S. (2018). Managing customer expectations and priorities in service systems. Management Science, 64(8), 3942–3970. https:// doi.org/10.1287/mnsc.2017.2785

Zaichkowsky, J. (1985). Measuring the involvement construct. Journal of Consumer Research, 12(3), 341–352. https://doi.org/10.1086/208520

## Appendix

Table A1. Constructs.

<table><tr><td>Construct</td><td>Items</td></tr><tr><td>Health anxiety(Abramowitz et al., 2007)(α = 0.78, CR = 0.85, AVE = 0.59)</td><td>I worry about my health.I fear of having serious illnesses.I hear about an illness and think I have it.My family/friends say I worry about my health.</td></tr><tr><td>Product involvement (Zaichkowsky, 1985)(α = 0.90, CR = 0.94, AVE = 0.83)</td><td>In general, going to a doctor for me ...is unimportant ... is important.doesn&#x27;t matter to me ... matters to me.is nonessential ... is essential.</td></tr><tr><td>Perceived crowding(Machleit et al., 2000)(α = 0.92, CR = 0.95, AVE = 0.82)</td><td>The office of Dr. Baum seemed very crowded to me.The office of Dr. Baum was very busy.There was NOT much traffic at Dr. Baum&#x27;s.There were a lot of patients at Dr. Baum&#x27;s.</td></tr><tr><td>Perceived immediacy(Y. Y. Lee &amp; Strong, 2003)(α = 0.83, CR = 0.90, AVE = 0.74)</td><td>The presented information about the amount of patients at each doctor was ...... current.... timely.... up-to-date.</td></tr><tr><td>Processing fluency(A. A. Lee &amp; Aaker, 2004)(α = 0.91, CR = 0.94, AVE = 0.85)</td><td>The information presented by the website was ...... easy to process.... easy to understand.... straightforward.</td></tr></table>

Note: “Dr. Baum” was the most crowded medical practice in the experiment.

Table A2. Descriptive statistics.

<table><tr><td rowspan="2">Condition</td><td colspan="2">1: CI absent (N = 114)</td><td colspan="2">2: Historical average CI (N = 113)</td><td colspan="2">3: Real-time CI (N = 116)</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Health anxiety</td><td>3.57</td><td>1.49</td><td>3.55</td><td>1.18</td><td>3.58</td><td>1.22</td></tr><tr><td>Age</td><td>27.47</td><td>8.43</td><td>28.04</td><td>7.49</td><td>28.43</td><td>8.55</td></tr><tr><td>Product involvement</td><td>5.05</td><td>1.55</td><td>5.34</td><td>1.19</td><td>5.04</td><td>1.45</td></tr><tr><td>Perceived crowding</td><td>3.98</td><td>0.80</td><td>6.16</td><td>0.93</td><td>6.36</td><td>0.69</td></tr><tr><td>Perceived immediacy</td><td>-</td><td>-</td><td>3.43</td><td>1.31</td><td>5.99</td><td>0.96</td></tr><tr><td>Processing fluency</td><td>5.44</td><td>1.24</td><td>5.97</td><td>1.03</td><td>6.53</td><td>0.65</td></tr><tr><td>Average selected crowding levela</td><td colspan="2">50.6%</td><td colspan="2">32.8%</td><td colspan="2">14.9%</td></tr></table>

<sup>a</sup>Location with lowest crowding level = 0%, highest crowding level = 100%
