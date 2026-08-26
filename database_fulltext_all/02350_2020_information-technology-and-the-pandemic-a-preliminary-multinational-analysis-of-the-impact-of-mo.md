---
otero_id: 2350
otero_key: "BJV7GDSN"
title: "Information Technology and the pandemic: a preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control"
authors: "Andrew Urbaczewski; Young Jin Lee"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1802358"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Technology and the pandemic: a preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control

Andrew Urbaczewski & Young Jin Lee

To cite this article: Andrew Urbaczewski & Young Jin Lee (2020): Information Technology and the pandemic: a preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1802358

To link to this article: https://doi.org/10.1080/0960085X.2020.1802358

![](/api/attachments/BJV7GDSN/fulltext/images/876128e11fa7431a3a381b69930fee0bdf12e764f209de4da8575c74596f3797.jpg)

Published online: 10 Aug 2020.

![](/api/attachments/BJV7GDSN/fulltext/images/a86a577e495fb27e74a883cefd87a804804c745ebed44b976c0c305f99a0d0e4.jpg)

Submit your article to this journal

![](/api/attachments/BJV7GDSN/fulltext/images/0218d7c49babae7f9fc1be9c633bc16d16546ff923573a306c4602bf32641ae0.jpg)

View related articles

![](/api/attachments/BJV7GDSN/fulltext/images/14be7f957328f43943c39f52069d7d15d6baf3744249638e986752f9ffb8571d.jpg)

View Crossmark data

EMPIRICAL RESEARCH

Check for updates

# Information Technology and the pandemic: a preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control

Andrew Urbaczewski <sup>a,b</sup> and Young Jin Lee<sup>c</sup>

<sup>a</sup>Business Information and Analytics, University of Denver, Denver, CO, USA; <sup>b</sup>Department of Management, United States Air Force Academy, Colorado Springs, CO, USA; <sup>c</sup>Business Information and Analytics, University of Denver, Denver, CO, USA

## ABSTRACT

This paper explores the benefits and drawbacks of government surveillance within a public health crisis, specifically the COVID-19 outbreak of 2020. We review the current state of COVID-19 infection tracking by public health authorities, and then we examine the efectiveness of voluntary and mandatory mobile contact-tracing apps by COVID-19-positive or suspected positive individuals in China, Germany, Italy, Singapore, South Korea, and the United States. Through a Diference-In-Diferences test, the apps were found to be highly significantly correlated with a reduction in the spread of COVID-19 in their countries. Robustness tests were run with four alternative models and the results are kept and presented within. In light of the success of these apps, ethical implications for their use during and beyond this public health crisis are discussed, including data governance and individual privacy issues.

ARTICLE HISTORY Received 16 May 2020 Accepted 24 July 2020

SPECIAL ISSUE EDITORS Pär Ågerfalk; Kieran Conboy; Michael Myers

KEYWORDS COVID-19 Pandemic Control; mobile tracking technology; surveillance; IT impact on society

## 1. Introduction

“Those who would give up essential Liberty, to purchase a little temporary Safety, deserve neither Liberty nor Safety” (Franklin, 1755)

“The greatest happiness of the greatest number is the foundation of morals and legislation.” (Bentham, 1830)

The COVID-19 pandemic of the 21<sup>st</sup> century is causing disruption to everyday life in ways few could have imagined before its arrival. Even though there were brushes with other outbreaks including SARS, MERS, Swine Flu, and Bird Flu, there has not been a pandemic on this global scale since the so-called Spanish Flu of 1918–1920. Few if any people today are alive who remember that pandemic, and as such history has relegated this tragedy with over 50 million deaths globally (Johnson & Mueller, 2002) to a side note overshadowed by World War I, with its comparatively fewer 15–22 million deaths (White, 2011).

As of July 13 2020, the Centre for Systems Science and Engineering at Johns Hopkins University is reporting over 13 million confirmed cases of COVID-19 and over 500,000 deaths globally. As countries shut down in an efort to control exposure to the virus, economic peril continues to increase. As examples, China reported economic contractions for the first time since the end of the Cultural Revolution, unemployment in the US jumped from 3.5% in February 2020 to 14.7% in April 2020, and EU oficials have warned that this could be the start of not just a recession but a depression. Oficials are desperate to stop people from getting ill from the virus but also to restart their economies.

One strategy used in epidemiology to stop the spread of the disease is contact tracing (Eames, 2007). Contact tracing is the process of identifying whom infected individuals may have contacted to quarantine potentially infected individuals to stop a disease’s forward spread, but also to identify where the disease may have started, or who might be “Patient Zero” in a particular area. For example, through contact tracing it is believed that the “Spanish” Flu started not in Spain but on an army base in Kansas, the US, and then spread through Europe through World War I but only really reported on by the free press in neutral Spain due to reporting restrictions (Barry, 2017). “Typhoid Mary” Mallon was another example, this time of a Typhoid carrier, identified in New York City in the early 20<sup>th</sup> century (Brooks, 1996).

A century after the mistitled Spanish Flu, the potential for contact tracing is radically changed by the advent of mobile technology. In 2019 over 2/3 of global citizens, and nearly 100% of the more highly developed world, had access to mobile phones, and in particular smartphones (Statista, 2020). Mobile phones constantly register their presence by “pinging” cellular towers in the area to obtain a connection to a network, and through a process of triangulation between signals from multiple towers, one’s more exact location can be calculated (Rao & Minakakis, 2003). If an individual is carrying his/her phone on his/her person, the location of the phone can be reasonably interpreted to also be that individual’s location. One’s location can also be confirmed through a phone’s ability to see known Wi-Fi networks, Bluetooth connections, as well as through recording GPS information if it is equipped with such a radio.

Many governments are using technology as a means to implement a contact tracing strategy. Some of these technologies using CCTV, drone camera footage, electronic payment location information, and wristbands to track and control the movement of individuals who may be COVID-19 positive or were ordered to quarantine for other proactive or reactive reasons. In this paper, however, we will look solely at mobile phone movement tracking apps. These are apps that are installed on a user’s phone allowing a third party, presumably from a government, to track and monitor and alert individuals about movement related to COVID-19 reduction activities. Although many governments move quickly to use mobile technology based on diferent policies or constitutions to bend the pandemic curve, the efectiveness of such mobile technology has not been studied, and, to the best of our knowledge, there is no timely empirical study discussing the impact. Therefore, as inspired by the call of Ågerfalk et al. (2020) to study information systems in times of pandemics, we strive to shed light on the impact of the use of mobile technology during the COVID-19 pandemic by analysing the pandemic curves of countries with the event of initiating a mobile tracing app.

As mentioned above, individuals’ location today can and often is tracked by the location of their mobile phones. Many a criminal has been caught in a lie when he or she has claimed to be nowhere near a crime scene and yet their phones tell a diferent story. This technology can now be as well to not just identify where on the earth an individual might be at a given time, but also near what other individuals. If a person is deemed to be infected with COVID-19, in theory, one’s phone location data could be compared with the location of other phones, and then to warn the owners of those phones that someone they have been near is a victim of COVID-19 and to now take appropriate precautions to prevent illness and further spread. Apps installed on phones can make collecting and disseminating this information much easier than comparing to telecommunication provider locator records.

There are many COVID-19 contact tracing apps available and being used by many governments. According to Woodhams (2020), as of July 3 2020 there are 80 documented contact tracing apps available globally being used in 50 countries (see Appendix A for the list). These apps use GPS and Bluetooth primarily to record locations. Some of these are used voluntarily, while in some nations it is a requirement to use this on your mobile phone if you have been in contact with infected individuals.

The purpose of the apps may be laudable, but the implementations may be more unreliable than the designers would hope. Stanley and Granick (2020) report that none of the apps they examined have enough accuracy to be able to reliably identify close contact. The work of Ferretti et al. (2020) suggests that 80% of all smartphone users would need to have installed an app for the epidemic control to work. Bay (2020), the product lead for the app primarily used in Singapore, TraceTogether, highlighted the limitations in relying on simply electronic technology for contact tracing.

The biggest barrier to the use of contact tracing apps may be the ethical concerns related to privacy, security, and anonymity. Due to the emergency nature of the pandemic, technical solutions may have been rolled out without a complete understanding of the side efects of the implementation. Privacy policies, anonymity requirements, and data retention policies may not have been fully developed before the implementation. It is also not clear if the data collected would be protected from other uses by other government agencies. Where laws like the EU’s General Data Protection Regulation (GDPR) were created to control the use of individual data by companies, it is not clear that such protections will be provided to citizens of a nation whose government is collecting this data. The European Commission (2020) has provided a set of guidelines that can be used to collect data and comply with the wishes of the member states. For example, the GDPR and NHS Act 2006 in the UK provide that governments can store the personally identifying information from contact tracing apps for a period of 20 years, so long as it is only used for the health emergency. Opponents of such a collection efort may counter that if the data are not collected and stored, there is no need for concern about what alternative purposes that they might be used.

As such, it is important to examine whether the use of mobile technology is indeed an efective strategy to slow the epidemic growth of a new virus in a pandemic. Because some countries mandate using mobile tracking apps while other countries only rely on voluntary participation (Halbfinger et al., 2020; Lee, 2020), we believe any empirical evidence of the impact of mobile tracking apps is quite valuable for governments to consider the trade-of between privacy and surveillance. Hence, our research is specifically designed to investigate timely the impact of mobile tracking apps on the outbreak of COVID-19. In the following sections, we first discuss our data collection and methods to answer this particular question. Then, we discuss results from data analysis and the implications of our findings.

## 2. Research design

We collected data on new confirmed COVID-19 cases per day from six diferent countries (China, Italy, Germany, Singapore, South Korea, and the US), as reported by https://coronaboard.kr.<sup>1</sup> Although the sample size of countries is quite small, they represent two diferent major cultural families (Western and Asian), diferent population sizes, and the use of mobile technology in their COVID-19 responses. These countries reached their ${ 1 0 0 } ^ { \mathrm { t h } }$ confirmed cases on diferent dates and also implemented diferent policies of using COVID-19-related mobile technology. Table 1 shows the summary statistics of confirmed cases per day (noncumulative) by countries over about 2 months since their ${ 1 0 0 } ^ { \mathrm { t h } }$ cases. For example, China reported its 100<sup>th</sup> confirmed case on January 21 2020 and we have collected the number of confirmed new cases per day in China for 66 days since then. Similarly, we collected the other five countries’ confirmed cases per day since their ${ 1 0 0 } ^ { \mathrm { t h } }$ reported confirmed cases. Note that this will construct our panel dataset (multiple countries and multiple daily observations for those countries). Among these six countries, China reached its 100<sup>th</sup> case earliest while the US was the most recent. Approximately 15 days after recording their ${ 1 0 0 } ^ { \mathrm { t h } }$ cases, Singapore and South Korea mandated that people who are or might be COVID-19- positive should use a COVID-19 related mobile app for government agencies to track and monitor them.

Figure 1 shows that each country has a quite distinct trend line from others in terms of the infection rate. Because Singapore and South Korea launched their mandatory mobile app in their COVID-19 responses approximately 15 days after their ${ 1 0 0 } ^ { \mathrm { t h } }$ confirmed cases (Kim & Rodriguez, 2020), Figure 1 pinpoints that day on the graph for easier viewing. Although South Korea’s trendline appears to be decreasing at that point, Singapore’s trendline continued to increase. Among the countries not mandating the mobile tracking apps, the trendline of China on day 15 shows a general downward slope while western countries such as Italy, Germany, and the US still have steep upward trendlines after day 15. Therefore, it is not clear whether the use of mobile tracking technology helped flatten the pandemic curve in general. In the following section, we explore our data further by featuring the time series of new daily cases by country to evaluate the impact of the use of mobile tracking technology in the fight against COVID-19.

## 3. Empirical analysis and results

This study aims to evaluate the impact of the use of mobile tracking technology on new COVID-19 outbreaks daily. We adopt a diference-in-diferences framework to address a potential endogeneity problem of unobservable country characteristics in this study. Information Systems and Marketing researches have used diference-in-diferences methods to study numerous IT policy questions $( \mathrm { e . g . } ,$ Chevalier & Mayzlin, 2006; Feng et al., 2019; Zhu & Zhang, 2010). The simplest set up is one where outcomes are observed for two groups for two time periods. In our context, one of the country groups is exposed to a treatment of mandating mobile app tracking in the second period but not in the first period. The second country group is not exposed to the treatment of mobile app tracking during either period. In the case where the same countries within a group are observed in each time period, the average gain in the second country (control) group is subtracted from the average gain in the first country (treatment) group. This removes biases in second-period comparisons between the treatment and control country group that could be the result of permanent diferences between those country groups, as well as biases from comparisons over time in the treatment country group that could be the result of trends (Imbens & Wooldridge, 2007).

Table 1. Descriptive statistics of COVID-19 daily confirmed cases by countries.

<table><tr><td>Country</td><td>Number $^{2}$  of days observed</td><td>Average Cases per day</td><td>Std. Dev.</td><td>Min</td><td>Max $^{3}$ </td><td>Date of 100th confirmed case (est.)</td><td>Mandated COVID-19 Mobile tracking?</td></tr><tr><td>China</td><td>66</td><td>1228.3</td><td>2114.3</td><td>11</td><td>15,136</td><td>1/21/20</td><td>No</td></tr><tr><td>Italy</td><td>62</td><td>3110.7</td><td>1855.7</td><td>54</td><td>6557</td><td>2/23/20</td><td>No</td></tr><tr><td>Germany</td><td>63</td><td>2603.2</td><td>2016.0</td><td>33</td><td>8759</td><td>3/1/20</td><td>No</td></tr><tr><td>Singapore</td><td>63</td><td>269.9</td><td>366.2</td><td>2</td><td>1426</td><td>2/29/20</td><td>Yes</td></tr><tr><td>South Korea</td><td>65</td><td>163.3</td><td>185.1</td><td>6</td><td>813</td><td>2/20/20</td><td>Yes</td></tr><tr><td>US</td><td>52</td><td>17,101.7</td><td>13,600</td><td>25</td><td>39,296</td><td>3/3/20</td><td>No</td></tr><tr><td>Total</td><td>372</td><td>3651.9</td><td>7638.71</td><td>2</td><td>39,296</td><td>-</td><td>-</td></tr></table>

![](/api/attachments/BJV7GDSN/fulltext/images/0e45f1ac995fff2374c8aba37a1fb9d9032268f26c045f505758184d2f0633e9.jpg)  
Figure 1. Daily trend of log scale of the number of cases per day by countries.

More specifically, suppose that there are two groups of countries by the use of mobile technology, COVID-19-App = 0, 1 where 0 indicates countries that do not use the mobile tracking technology, i.e. the control group, and 1 indicates countries who use mobile tracking technology, i.e. the treatment group. We also observe countries in two diferent time periods, t = 0, 1 where 0 indicates a time period before the use of the mobile tracking technology (COVID-19-App), i.e. pre-treatment, and 1 indicates a time period after the use of the mobile technology, i.e. post-treatment. Every observation is indexed by i = 1, . . ., n by country $j ;$ countries will typically have multiple observations each, multiple pretreatment periods, and multiple post-treatment periods. Therefore, the number of new COVID-19 cases per day i by a country j is modelled by the following equation,

$$
\begin{array}{r l} \operatorname{Log} (\text { COVID19 Cases }) _ {i, j} & = \alpha_ {j} + \beta (\text { COVID19 } _ {\text { App } _ {i, j}}) \\ & \quad + \gamma (t _ {i, j}) \\ & \quad + \delta (\text { COVID19\_App } _ {i, j} \times t _ {i, j}) \\ & \quad + \varepsilon_ {i, j} \end{array}\tag{1}
$$

where the coeficients are all unknown parameters and $\varepsilon _ { i , j } \mathrm { i } s$ a random, unobserved error term which contains all determinants of LogðCOVID19 CasesÞ which our model omits. By inspecting the equation, we should be able to see that the coeficients have the following interpretation:

α = constant term,

β = treatment group-specific efect to account for average permanent diferences between treatment (with COVID-19-app) and control (without COVID-19-app),

γ = time trend common to control and treatment groups, and

δ = true efect of treatment (with COVID-19-app).

The diference in diferences (DiD) estimator is used to estimate Equation (1) above as the diference in the average number of cases per day in the treatment group (with COVID-19-app) before and after treatment minus the diference in the average number of cases per day in the control group (without COVID-19-app) before and after treatment<sup>4</sup>: it is a “diference of diferences” (Angrist & Krueger, 1999; Stock & Watson, 2010).

Table 2 summarises the number of observations by COVID-19-App and the period of launching the mobile tracking app. The control group includes China, Germany, Italy, and the US who do not mandate the mobile tracking apps, while South Korea and Singapore compose the treated group who mandate the mobile tracking apps. Table 3 summarises the average log (number of cases per day)<sup>5</sup> by four diferent conditions. Note that the control group (the countries not mandating the mobile tracking apps) has a relatively greater average number of cases per day than the treated group (the countries mandating the mobile tracking apps). This could be attributed to being diferences between the control group and the treated group, in terms of population, policy, culture, or how to use technology, etc. in their COVID-19 responses. The diference in average log (number of cases per day) by COVID-19-app before and after the time of launching the app are statistically significant (Before: −1.984 and After: −3.168, p < 0.001). The diference in the diferences above, −1.184, shows the impact of mobile tracking technology (COVID-19- App) is highly significant. In other words, having mandatory mobile tracking and monitoring of people who are or may be COVID-19-positive may reduce new cases per day by 3.3 on average, ceteris paribus. Although the magnitude of the impact may appear small, this will dramatically flatten the exponential growth of new cases if this policy can be launched in the early stage of an outbreak.

Table 2. Number of observations in the Diference in Diferences.

<table><tr><td></td><td>Before</td><td>After</td><td>Total</td></tr><tr><td>Control (without COVID-19-App)</td><td>60</td><td>183</td><td>243</td></tr><tr><td>Treated (with COVID-19-App)</td><td>30</td><td>98</td><td>128</td></tr><tr><td>Total</td><td>90</td><td>281</td><td>371</td></tr></table>

Table 3. Diference in diferences estimation results.

<table><tr><td></td><td colspan="2">Average log (number of cases per day)</td></tr><tr><td></td><td>Before</td><td>After</td></tr><tr><td>Control (without COVID-19-App)</td><td>5.845</td><td>7.719</td></tr><tr><td>Treated (with COVID-19-App)</td><td>3.861</td><td>4.551</td></tr><tr><td rowspan="2">Diff (Treated -Control)</td><td>-1.984***</td><td>-3.168***</td></tr><tr><td>(0.386)</td><td>(0.216)</td></tr><tr><td rowspan="3">Difference in Difference</td><td colspan="2">(After) - (Before) = -1.184***</td></tr><tr><td colspan="2">(0.443)</td></tr><tr><td colspan="2">R-square = 0.44</td></tr></table>

Standard errors in parentheses. \*\* p < 0.01, \*\*\* p < 0.001

Table 4. DiD estimates with various model specifications.

<table><tr><td rowspan="2">DV:</td><td>Model (1)</td><td>Model (2)</td><td>Model (3)</td><td>Model (4)</td></tr><tr><td>DiD(OLS) Log (number of cases per day)</td><td>DiD(Random effects) Log (number of cases per day)</td><td>DiD(Fixed effects) Log (number of cases per day)</td><td>DiD(Poisson) number of cases per day</td></tr><tr><td> $\beta(COVID19\_App_{i,j})$ </td><td>-1.984***(0.423)</td><td>-1.984**(0.698)</td><td>n/a</td><td>-1.250(0.708)</td></tr><tr><td> $\gamma(t_{i,j})$ </td><td>1.874***(0.225)</td><td>1.977***(0.226)</td><td>1.985***(0.224)</td><td>2.392***(0.00485)</td></tr><tr><td> $\delta(COVID19\_App_{i,j} \times t_{i,j})$ </td><td>-1.184*(0.466)</td><td>-1.288***(0.388)</td><td>-1.296***(0.386)</td><td>-2.351***(0.0151)</td></tr><tr><td> $a$  (constant)</td><td>5.845***(0.172)</td><td>5.845***(0.403)</td><td>5.106***(0.159)</td><td>6.596***(0.409)</td></tr><tr><td>Observations</td><td>371</td><td>371</td><td>371</td><td>371</td></tr><tr><td>adj. R square</td><td>0.435</td><td>0.4392</td><td>0.171</td><td>n/a</td></tr><tr><td>Log-likelihood</td><td></td><td></td><td></td><td>-279,000.25</td></tr></table>

Standard errors in parentheses. \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001

## 3.1. Robustness check

To evaluate if our findings above are robust, we ran the model (1) with diferent specifications. In Table 4, Model (1) shows the full regression results from our initial DiD above. Model (2) in Table 4 extends the Model (1) by adding random efects within each country, which assumes that each country’s unobserved characteristics (let us say u ) are truly random and they are taken into account in the Model (2). Model (3) in Table 4 extends the Model (1) by adding fixed efects within a country, which means each country’s unobserved characteristics (u ) are not random but are removed in the fixed efects estimation method.<sup>6</sup> Model (4) in Table 4 assumes that the dependent variable should be the number of cases per day in Model (1) and the dependent variable may follow a Poisson distribution because the number of cases is discrete. All results in Table 4 are quite consistent and this demonstrates that our findings in the original DiD in the above section are quite robust.

## 4. Discussion and core conclusions

Our analysis shows that IT, specifically through contact-tracing apps, can be efective in reducing the spread of COVID-19. As epidemiologists become concerned about a second wave in the European autumn of 2020, contact tracing will be an important tool in fighting its spread.

It must be understood that the reports of COVID-19 positive results are at best estimates. Counting the number of cases of COVID-19 in a country is not as straightforward as counting the number of gumballs in a jar. There are many reasons why the number of cases might be higher or lower than what is reported. Access to testing, unknown test characteristics, and inaccuracies in communication channels lead to the lack of a clear understanding of the prevalence and mortality of COVID-19. An incubation period of 2 weeks, varied symptomatology and severity of illness all complicate identifying infected individuals. The dearth of tests also causes some people who are asymptomatic or experience mild symptoms to not be tested at all.

The data used in this paper are the best available to the authors at the time of writing. That being said, it must be noted that reported counts have been refined and re-reported throughout this pandemic. Inconsistent reporting may also occur in places regarding individuals reporting cases in unusual locations where the geographic claim is not always straightforward, such as on cruise ships. Lack of testing and numbers of asymptomatic spreaders may also afect the numbers of cases reported. Moreover, while this is a medical emergency, it also exists within the realm of politics. It may not be perceived by a political leader to be in his/her best interest to assure accurate reporting of cases. Two countries in this study, in particular, China and the US, have been accused of either underreporting cases and deaths or publicly indicating the results are not as intense as scientists are reporting (Tsang et al., 2020).

We also did not explicitly consider diferences in nations due to factors of geography or diferences within a culture. For example, some island nations like New Zealand that are relatively easy to isolate may have vastly diferent results to COVID-19 interventions than international crossroads such as Western European nations. Also, the cultures of some nations may be more or less willing to adopt or resist the use of apps, as we discuss in our future research below.

This paper shows that the use of contact tracing apps is correlated with reductions in COVID-19 cases. This is consistent with the work of Ferretti et al. (2020), who built a largely theoretical model suggesting outcomes when contacts were notified instantly through digital tracing versus traditional contact tracing. Our work expands upon theirs by examining actual outcomes from the field, as well as being both cross-cultural and cross-national in nature. This provides the community with more of a field experiment quality. As with all field studies, there always exists the possibility that there are other factors that we did not observe or could account for. The main limitation is that our results are preliminary and can only be kept and extended to the treatment group in comparison with the control group. Hence, there is a potential bias due to the selection of the limited countries in our dataset. In addition, although our method of DiD can successfully control for timeinvariant-omitted variables such as the country’s culture, constitution, population size, etc., our analysis may not control for time-varying omitted variables such as the country’s lockdown strategy and new regulations during the pandemic.

While the evidence modelled in this paper appears to show that tracking technology is efective in fighting the spread of COVID-19, we also may ask ourselves at what cost of civil liberties. At what point does the protection of the public outweigh the protection of the individual? To control infectious disease, we need to know who has it and who has been exposed. But what else do we expose in gaining this knowledge?

In the 21<sup>st</sup> century, governments that have acquired new powers to monitor and control their citizenry to meet a temporary need are loathed to give them up. For example, shortly after the 9/11 terrorist attacks in the US, its government passed the USA Patriot Act of 2001, giving it “temporary surveillance powers.” As of this writing, almost two decades later and one decade after the death of its architect Osama Bin Laden, the US government has retained most of these powers. We see similar cases in Israel with the Shin Bet Data Collection Act of 2002, and more recently in Turkey with its State of Emergency since its failed coup in 2016. Governments around the world may seize upon the pandemic scare of its people as an opportunity to gain more control over them (Economist, 2020).

An additional issue with this data tracking is the confusion that comes with the misidentification of individuals who are to be tracked. One case in Israel in March 2020 (Lin & Martin, 2020) found individuals required to stay home due to a data input error that indicated an individual they had been in contact with was COVID-19 positive when in fact he was not (and he himself was not required to be quarantined).

The most obvious part of future research is how to maximise the benefit to the public while minimising the potential harm to the individual. It appears that COVID-19 will be with us for some time, and may even see seasonal spikes due to weather conditions, relaxed social distancing regulations, and conventions, mutations, or other related reasons. Even if COVID-19 were to magically disappear, the lessons to be learned are not diferent than we have seen in the past or will almost certainly be part of our future. COVID-19 is not the first coronavirus to spark panic with its outbreak this century, as we saw with SARS and MERS, and we may see more novel coronaviruses in the future. It is not just the coronavirus family for which we need to be concerned. For example, in 2015, governments were trying to prevent the spread of Ebola from West Africa to other parts of the world, and flight bans between West Africa and the US were considered as well.

Two US companies, Apple and Google, have developed a solution to allow peer-to-peer tracking of COVID-19 victim exposure and movement. It works through the sharing of information between users rather than a central repository of information being kept by a governmental agency. It is believed by the companies that this solution strikes the balance of warning those who may have been exposed to the virus of the need to self-isolate but at the same time help to prevent potential violations of individual civil liberties (Schechner & Winkler, 2020). Continued testing and refinement of peer-to-peer apps, along with the willingness of civil authorities to accept their use for public health protection, maybe the key to striking this balance. Before the next pandemic or wave of the current pandemic hits, this should continue to be explored.

At the time of this pandemic, the GDPR is only 2 years old. Future research should examine how ECwide initiatives like GDPR stand up in the face of a public health emergency that GDPR was likely never truly designed to interoperate with fully. Additionally, we see many diferent vendors creating many diferent contact-tracing apps designed to work on a continent, or a country, or even a small part of a country representing an ethnic/language/cultural minority. These vendors are working in concert with their employers and may not have thought about how they may link with dozens of other vendors regionally or globally. Findikoglu et al. (2020) suggest that they will form partnerships and partner pools, but this is through the normal course of business as opposed to during a pandemic and the addition of variables present in an emergency may help extend their framework.

The current situation causes us to think once again about perceived voluntariness, a construct long studied in the IS literature. Almost two decades ago, Brown et al. (2002) asked in EJIS “Do I really have to?” when considering the use of mandated technology. Two decades ago, perhaps the lessons of the mislabelled Spanish Flu were still a distant memory, and the idea that in some cases people would not be able to leave their homes without the technology may have seemed like a far-of dystopia. In the year 2020 and for who knows how long beyond, this may be a reality.

Former US President Barack Obama adviser and former mayor of Chicago Rahm Emanuel is often credited with coining the phrase “never let a crisis go to waste.” He is credited with that quote during the great financial crisis of 2008 as a means to observe and try and study approaches that might not normally be available to study. We believe we have done that with this research efort. We have found evidence that supports the mandated use of contact-tracing apps in fighting a pandemic and the contributions that IT can make in a public health crisis. Our work can guide governments who are looking to share information and protect their people and potentially provide a roadmap to returning to a pre-2020 level of social engagement across the globe.

## Notes

1. All the information relies upon publicly available from multiple data sources that do not always agree.

2. Each country has a diferent day starting the COVID-19 outbreak and their dates reaching at the ${ 1 0 0 } ^ { \mathrm { t h } }$ confirmed cases are varying. At the time of our data collection (April 25th, 2020), US had passed its 52 days since its date (March 3<sup>rd</sup>, 2020) of its100<sup>th</sup> confirmed cases and US was the latest. Therefore, the number of days observed since their 100<sup>th</sup> confirmed cases of other countries are longer and diferent. This feature constructs our unbalanced panel dataset.

3. Although the number of cases per day by country may not be the actual number of new cases per day due to later revisions, we assume the trajectory of the pandemic curve within a country would remain the same qualitatively.

4. This would be the estimate one would get from an OLS estimate of a regression equation of the form given by the equation (1) on the entire data.

5. The results are also sustained when we use the original number of cases as our dependent variable without the log-transformation. The log-transformed number of cases as our dependent variable is preferred in our analysis because the skewness of the log-transformed number of cases is much lower than that of the original number of cases (the skewness of the log-transformed is −0.142 vs. the skewness of the original number of cases is 2.98). Besides, the R-square is 0.19 when we use the original variable, which is lower than 0.44 with the log-transformed number of cases in Table 3.

6. Fixed efects elimates all time invariant cariables within each country. This means that omitted variables such as population, policy, law, regulations, etc. do not confound with the variables of interest in our DiD esitmation.

## Disclosure statement

No potential conflict of interest was reported by the authors. The views expressed in this presentation are those of the authors and do not necessarily reflect the oficial policy or position of the Air Force, the Department of Defense, or the US Government. Distribution A: Approved for Public Release, Distribution Unlimited. USAFA-DF-2020-228.

## ORCID

Andrew Urbaczewski http://orcid.org/0000-0002-6481- 544X

## References

Ågerfalk, P. J., Conboy, K., & Myers, M. D. (2020). Information systems in the age of pandemics: COVID-19 and beyond. European Journal of Information Systems, 29(3), 1–5. https://doi.org/10.1080 0960085X.2020.1771968

Angrist, J. D., & Krueger, A. B. (1999). Chapter 23 Empirical strategies in labor economics. In Handbook of labor economics, 3(A), 1277–1366. Elsevier. https://doi.org/10. 1016/S1573-4463(99)03004-7

Barry, J. (2017). How the horrific 1918 influenza spread across America. Smithsonianmag.Com. https://www. smithsonianmag.com/history/journal-plagueyear–180965222

Bay, J. (2020). Automated contact tracing is not a coronavirus panacea. https://blog.gds-gov.tech/auto mated-contact-tracing-is-not-a-coronavirus-panacea -57fb3ce61d98

Bentham, J. (1830). The greatest happiness of the greatest number. In Bentham’s political thought (pp. 309–310).

Brooks, J. (1996). The sad and tragic life of typhoid Mary. CMAJ, 154(6), 915–916. https://www.cmaj.ca/content/ 154/6/915

Brown, S. A., Massey, A. P., Montoya-Weiss, M. M., & Burkman, J. R. (2002). Do I really have to? User acceptance of mandated technology. European Journal of Information Systems, 11(4), 283–295. https://doi.org/10. 1057/palgrave.ejis.3000438

Chevalier, J. A. J., & Mayzlin, D. (2006). The efect of word of mouth on sales: Online book reviews. Journal of Marketing Research, 43(3), 345–354. https://doi.org/10. 1509/jmkr.43.3.345

Eames, K. T. D. (2007). Contact tracing strategies in heterogeneous populations. Epidemiology and Infection, 135(3), 443–454. https://doi.org/10.1017/S0950268806006923

Economist. (2020). Autocrats see opportunity in disaster. The Economist. https://www.economist.com/leaders/ 2020/04/23/autocrats-see-opportunity-in-disaster

European Commission. (2020). eHealth network guidelines. https://ec.europa.eu/health/sites/health/files/ehealth/ docs/mobileapps\_interoperabilitydetailedelements\_en. pdf

Feng, J., Li, X., & Zhang, X. M. (2019). Online product reviews-triggered dynamic pricing: Theory and evidence. Information Systems Research, 30(4), 1107– 1123. https://doi.org/10.1287/isre.2019.0852

Ferretti, L., Wymant, C., Kendall, M., Zhao, L., Nurtay, A., Abeler-Dörner, L., Parker, M., Bonsall, D., & Fraser, C. (2020). Quantifying SARS-CoV-2 transmission suggests

epidemic control with digital contact tracing. Science, 368 (6491), eabb6936. https://doi.org/10.1126/science.abb6936

Findikoglu, N. M., Ranganathan, C., & Watson-Manheim, M. B. (2020). Partnering for prosperity: Small IT vendor partnership formation and the establishment of partner pools. European Journal of Information Systems, 1–26. https://doi.org/10.1080/0960085X.2020.1750309

Franklin, B. (1755). Pennsylvania Assembly: Reply to the Governor. Franklinpapers.Org.

Halbfinger, D., Kershner, I., & Bergman, R. (2020). To track coronavirus, Israel moves to tap secret trove of cellphone data. Nytimes. https://www.nytimes.com/2020/03/16/ world/middleeast/israel-coronavirus-cellphone-tracking. html

Imbens, G., & Wooldridge, J. (2007). Diference-indiferences estimation. What’s new in econometrics? NBER, Summer 2007. http://www.nber.org/WNE/lect\_ 10\_difindifs.pdf

Johnson, N. P. A. S., & Mueller, J. (2002). Updating the accounts: Global mortality of the 1918–1920 “Spanish” influenza pandemic. Bulletin of the History of Medicine, 76(1), 105–115. https://doi.org/10.1353/bhm.2002.0022

Kim, D., & Rodriguez, D. (2020). ‘There’s an app for that’: Use of COVID-19 apps in Singapore and South Korea. The Asia Pacific Foundation of Canada. https://www.asiapaci fic.ca/publication/theres-app-use-covid-19-appssingapore-and-south-korea

Lee, Y. (2020). Taiwan’s new “electronic fence” for quarantines leads wave of virus monitoring. Reuters. https:/ www.reuters.com/article/us-health-coronavirus-taiwansurveillanc-idUSKBN2170SK

Lin, L., & Martin, T. (2020). How coronavirus is eroding privacy. Wall Street Journal. https://www.wsj.com/arti cles/coronavirus-paves-way-for-new-age-of-digitalsurveillance–11586963028

Rao, B., & Minakakis, L. (2003). Evolution of mobile location-based services. Communications of the ACM, 46(12), 61. https://doi.org/10.1145/953460.953490

Schechner, S., & Winkler, R. (2020). Here’s how apple and google plan to track the coronavirus through your phone. Wall Street Journal. https://www.wsj.com/arti cles/heres-how-apple-and-google-plan-to-track-thecoronavirus-through-your-phone-11586618075?mod= article\_inline

Stanley, J., & Granick, J. (2020). The limits of location tracking in an epidemic. Aclu.Org. https://www.aclu.org/ report/aclu-white-paper-limits-location-trackingepidemic%0A%0A

Statista. (2020). Mobile phone user penetration as percentage of the population worldwide from 2013 to 2019. Statista. https://www.statista.com/statistics/470018/mobile-phone -user-penetration-worldwide

Stock, J. H., & Watson, M. W. (2010). Introduction to econometrics. In Addison-Wesley (3rd ed.) (pp. 477– 485). Addison-Wesley Series in Economics.

Tsang, T. K., Wu, P., Lin, Y., Lau, E. H. Y., Leung, G. M., & Cowling, B. J. (2020). Efect of changing case definitions for COVID-19 on the epidemic curve and transmission parameters in mainland China: A modelling study. The Lancet Public Health, 5(5), e289-e296. https://doi.org/10. 1016/S2468-2667(20)30089-X

White, M. (2011). Atrocities: The 100 deadliest episodes in human history (1st ed.). W. W. Norton & Company.

Woodhams, S. (2020). COVID-19 digital rights tracker. TOPVPN. https://www.top10vpn.com/research/investiga tions/covid-19-digital-rights-tracker

Zhu, F., & Zhang, X., (Michael). (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133–148. https://doi.org/10.1509/jm.74.2.133

COVID-19 Digital Rights Tracker Report at https://www.top10vpn.com/research/investigations/covid-19-digital-rightstracker/

<table><tr><td>Country</td><td>App Name</td><td>Downloads (Play store)</td><td>State/Private</td><td>iOS/Android</td><td>Privacy Policy</td><td>Bluetooth/GPS</td><td>Centralised/ Decentralised</td></tr><tr><td>Australia</td><td>COVIDSafe</td><td>500,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>Austria</td><td>Stopp Corona</td><td>100,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>Bahrain</td><td>BeAware Bahrain</td><td>100,000+</td><td>State</td><td>Both</td><td>X</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>Bulgaria</td><td>ViruSafe</td><td>10,000+</td><td>Public-Private</td><td>Both</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>Canada (Alberta)</td><td>ABTraceTogether</td><td>10,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>China</td><td>Close Contact Detector</td><td>N/A</td><td>Public-Private</td><td>Alipay, WeChat &amp; QQ</td><td>Unknown</td><td>Gov. surveillance data</td><td>Centralised</td></tr><tr><td>Cyprus</td><td>CovTracer</td><td>500+</td><td>Public-Private</td><td>Android</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>Czech Republic</td><td>Mapy.cz</td><td>1,000,000+</td><td>Private</td><td>Both</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>Czech Republic</td><td>eRouška (eFacemask)</td><td>100,000+</td><td>State</td><td>Android</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>Ghana</td><td>GH Covid-19 Tracker App</td><td>N/A</td><td>State</td><td>Both</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>Iceland</td><td>Rakning C-19</td><td>50,000+</td><td>State</td><td>Both</td><td>√</td><td>GPS</td><td>Decentralised</td></tr><tr><td>India</td><td>SAIYAM – Track &amp; Trace Together</td><td>50+</td><td>Private</td><td>Android</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>India</td><td>Aarogya Setu</td><td>50,000,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>India (Arunachal Pradesh)</td><td>COVID CARE</td><td>1,000+</td><td>Private</td><td>Android</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>India (Goa)</td><td>Covid Locator</td><td>10,000+</td><td>Private – Public</td><td>Android</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>India (Karnataka)</td><td>Corona Watch</td><td>100,000+</td><td>State</td><td>Android</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>India (Maharashtra)</td><td>MahaKavach</td><td>10,000+</td><td>State</td><td>Android</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>India (Odisha)</td><td>COVID-19 Odisha</td><td>1000+</td><td>State</td><td>Android</td><td>X</td><td>Bluetooth &amp; GPS</td><td>Unknown</td></tr><tr><td>India (Surat)</td><td>SMC COVID-19 Tracker</td><td>50,000+</td><td>State</td><td>Android</td><td>X</td><td>GPS</td><td>Centralised</td></tr><tr><td>India (Tamil Nadu)</td><td>COVID-19 Quarantine Monitor Tamil Nadu</td><td>100,000+</td><td>Private – Public</td><td>Android</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>India (Uttar Pradesh)</td><td>UP Self-Quarentine App</td><td>10,000+</td><td>State</td><td>Android</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>India</td><td>(Uttarakhand)</td><td>Uttarakhand CV 19 Tracking System</td><td>5,000+</td><td>State</td><td>Android</td><td>√</td><td>GPS</td></tr><tr><td>Centralised</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Indonesia</td><td>PeduliLindungi (Care Protect)</td><td>1,000,000+</td><td>State</td><td>Android</td><td>X</td><td>Bluetooth &amp; GPS</td><td>Decentralised</td></tr><tr><td>Israel</td><td>– “The Shield”</td><td>1,000,000+</td><td>State</td><td>Both</td><td>√</td><td>GPS</td><td>Decentralised</td></tr><tr><td>Israel</td><td>Track Virus</td><td>100,000+</td><td>Private</td><td>Both</td><td>X</td><td>Bluetooth &amp; GPS</td><td>Decentralised</td></tr><tr><td>Italy</td><td>SM_Covid19</td><td>10,000+</td><td>Private</td><td>Android</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>Kyrgyzstan</td><td>Stop COVID-19 KG</td><td>10,000+</td><td>State</td><td>Android</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>Mexico (Jalisco)</td><td>Plan Jalisco Covid-19</td><td>5,000+ *</td><td>State</td><td>Both</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>North Macedonia</td><td>StopKorona!</td><td>10,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>Norway</td><td>Smittestopp (Infection Stop)</td><td>100,000+</td><td>Public-Private</td><td>Both</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>Philippines (Cebu)</td><td>WeTrace</td><td>5,000+</td><td>Public-Private</td><td>Both</td><td>X</td><td>GPS</td><td>Decentralised</td></tr><tr><td>Poland</td><td>Home Quarentine (Kwarantanna domowa)</td><td>100,000+</td><td>State</td><td>Both</td><td>√</td><td>GPS</td><td>Unknown</td></tr><tr><td>Poland</td><td>ProteGO Safe</td><td>1,000+</td><td>State</td><td>Android</td><td>√</td><td>Bluetooth</td><td>Decentralised</td></tr><tr><td>Singapore</td><td>TraceTogether</td><td>500,000+</td><td>State</td><td>Both</td><td>√</td><td>Bluetooth</td><td>Centralised</td></tr><tr><td>Singapore</td><td>Contact Tracer</td><td>5+</td><td>Private</td><td>Android</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>Slovak Republic</td><td>Zostań Zdravy</td><td>100,000+</td><td>Private</td><td>Android</td><td>√</td><td>GPS</td><td>Unknown</td></tr><tr><td>South Korea</td><td>100 m (Corona 100 m)</td><td>1,000,000+</td><td>Private</td><td>Android</td><td>X</td><td>GPS</td><td>Unknown</td></tr><tr><td>South Korea</td><td>Shincheonji Location Notification</td><td>100,000+</td><td>Private</td><td>Both</td><td>√</td><td>GPS</td><td>Unknown</td></tr><tr><td>Spain (Basque Country)</td><td>COVID-19.eus</td><td>50,000+</td><td>Public-Private</td><td>Both</td><td>√</td><td>User-submitted geo-data</td><td>Centralised</td></tr><tr><td>Thailand</td><td>MorChana –</td><td>50,000+</td><td>Public-Private</td><td>Both</td><td>X</td><td>Bluetooth &amp; GPS</td><td>Unknown</td></tr><tr><td>U.S.</td><td>SafePaths</td><td>10,000+</td><td>Private</td><td>Both</td><td>X</td><td>GPS</td><td>Decentralised</td></tr><tr><td>U.S.</td><td>Contact Tracer</td><td>10,000+</td><td>Private</td><td>Android</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Unknown</td></tr><tr><td>U.S.</td><td>HEALTHLYNKED COVID-19 Tracker</td><td>5,000+ *</td><td>Private</td><td>Both</td><td>√</td><td>GPS</td><td>Unknown</td></tr><tr><td>U.S.</td><td>Contact Tracing</td><td>50,000+</td><td>Private</td><td>Both</td><td>√</td><td>Bluetooth &amp; GPS</td><td>Centralised</td></tr><tr><td>U.S.</td><td>Care19</td><td>10,000+</td><td>Private</td><td>Both</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>Ukraine</td><td>Дій вдома (Action at Home)</td><td>10,000+</td><td>State</td><td>Both</td><td>√</td><td>GPS</td><td>Centralised</td></tr><tr><td>United Kingdom</td><td>NHS Covid-19</td><td>5,000+</td><td>Public-Private</td><td>Android</td><td>√</td><td>Bluetooth</td><td>Centralised</td></tr></table>
