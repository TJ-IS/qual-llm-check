---
otero_id: 25582
otero_key: "CH3VFT5Y"
title: "Accounting for social media effects to improve the accuracy of infection models: combatting the COVID-19 pandemic and infodemic"
authors: "Sujin Bae; Eunyoung (Christine) Sung; Ohbyung Kwon"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2021.1890530"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Accounting for social media effects to improve the accuracy of infection models: combatting the COVID-19 pandemic and infodemic

## Sujin Bae, Eunyoung (Christine) Sung & Ohbyung Kwon

To cite this article: Sujin Bae, Eunyoung (Christine) Sung & Ohbyung Kwon (2021) Accounting for social media effects to improve the accuracy of infection models: combatting the COVID-19 pandemic and infodemic, European Journal of Information Systems, 30:3, 342-355, DOI: 10.1080/0960085X.2021.1890530

To link to this article: https://doi.org/10.1080/0960085X.2021.1890530

![](/api/attachments/CH3VFT5Y/fulltext/images/cb596ec2021b24bbf5f52eb5acbd4c2deb0a9125adfb9b557de860d1e8bae175.jpg)

Published online: 25 Feb 2021.

![](/api/attachments/CH3VFT5Y/fulltext/images/98fd5e7d7a990a138607f6d8b50883413523596b79343cc48881c1e0ffc060c1.jpg)

Submit your article to this journal

![](/api/attachments/CH3VFT5Y/fulltext/images/2ea9ee269fb12ad4e8f9c4f60b94d4ac991f87f2bea6a53778562fdb6e3c9fd7.jpg)

Article views: 363

![](/api/attachments/CH3VFT5Y/fulltext/images/b995ae5c2671c6dd2774e1a714459aca2a452781bc3411767daddbed723876e6.jpg)

View related articles

![](/api/attachments/CH3VFT5Y/fulltext/images/cef71190e769c186cc139ae0afa69b102574acdbc510d62fef58654a5fe1a9c7.jpg)

View Crossmark data

![](/api/attachments/CH3VFT5Y/fulltext/images/f0f8fa11532fd2b5e5248d042b895a159b1f3e6baa8bf2db041b63a344c2b1e3.jpg)

Citing articles: 1 View citing articles

EMPIRICAL RESEARCH

Check for updates

# Accounting for social media efects to improve the accuracy of infection models: combatting the COVID-19 pandemic and infodemic

Sujin Bae<sup>a</sup>, Eunyoung (Christine) Sung <sup>b</sup> and Ohbyung Kwon<sup>a</sup>

<sup>a</sup>School of Management, Kyung Hee University, Seoul, Korea (The Republic Of); <sup>b</sup>Jake Jabs College of Business & Entrepreneurship, Montana State University Bozeman, Bozeman, MT, United States

## ABSTRACT

During the COVID-19 pandemic, social media platforms such as Twitter, Facebook, etc. have played an important role in conveying information, both accurate and inaccurate, thereby creating mass confusion. As the response to COVID-19 has reduced face-to-face contact, communication via social media has increased. Evidence shows that social media afects disease (non-)prevention through the (im)proper distribution of information, and distorts the predictive accuracy of infection models, including legacy Susceptible–Exposed–Infectious– Recovered (SEIR) models. Our adjusted SEIR model reflects the efectiveness of information disseminated through social media by accounting for dimensions of social/informational motivation based on social learning/use and gratification theories, and uses Monte Carlo methodology and computational algorithms to predict efects of social media on the spread of COVID-19 (N = 2,095 cases). The results suggest that social media utilisation measures should be incorporated into SEIR models to improve forecasts of COVID-19 infections. Utilising IS to analyse the spread of digital information via social media platforms can inform eforts to combat the pandemic and infodemic. Agencies responsible for infection and disease control, policy makers, businesses, institutions and educators must accurately monitor infection rates to appropriately allocate funding and human resources and develop efective disease prevention marketing campaigns.

ARTICLE HISTORY Received 2 September 2020 Accepted 7 February 2021

SPECIAL ISSUE EDITORS Pär Ågerfalk, Kieran Conboy and Michael Myers

KEYWORDS COVID-19 infection; SEIR model; social media; big data analysis; monte carlo method

## 1. Introduction

In March 2020, the World Health Organization declared the Coronavirus Disease 2019 (COVID-19) a pandemic (i.e., a public health emergency of international concern). Human-to-human transmission of COVID-19 is believed to occur primarily through respiratory droplets. The virus is known to be contagious, even during its latency period, meaning that an infected person can spread the virus through contact with others before noticing any symptoms (Kuhn, 2020). The COVID-19 pandemic has had an immense impact on public health, the economy, politics, and society, prompting eforts all over the world to counteract it.

Many institutions are harnessing the power of big data to support prevention through global cooperation. Specifically, researchers are trying to forecast COVID-19 infections more accurately to support media campaigns for public awareness. Accurately forecasting COVID-19 infections helps governments develop appropriate disease prevention policies (e.g., closing or reopening businesses and schools), and helps medical workers estimate the number of patients that may need to be treated at a given time. The media can be a powerful tool in persuading citizens to follow measures designed to combat the pandemic, but the information conveyed must be accurate. Otherwise, it might have the opposite efect.

Secondary infection of COVID-19 often occurs when people are together for long periods in poorly ventilated indoor spaces, such as in family homes, medical institutions, and other gathering sites (Zhai, 2020). Ultimately, the spread of COVID-19 is tied to the behaviour of individual citizens; most disease prevention eforts involve limiting interpersonal contact (i.e., “untact”). As people adjust to the new normal, they are increasingly turning to social media as a mode of communication and interaction and a source of information, making social media efects more powerful than ever. The circulation of vast amounts of information and opinions about COVID-19 through both social media platforms and oficial governmental communications has created mass confusion. Information systems (IS) are used to collect, monitor, and analyse information in attempts to forecast COVID-19 infections more accurately. Although predictive measures support individuals’ disease prevention behaviour (e.g., social distancing, mask wearing, hand washing), we currently do not understand how social media afects responses to information about COVID-19.

Governments around the world have worked to implement preventive measures and are using IS to predict COVID-19 infections. Accurately forecasting the number of COVID-19 infections is vital to maintaining the public’s trust in governmental communications and compliance with health recommendations, as well as ensuring that economies and schools can reopen safely without overwhelming health systems. In this study, we improve the predictive accuracy of the Susceptible–Exposed–Infectious–Recovered (SEIR) model (Assiri et al., 2013) used to forecast COVID-19 infections by accounting for social media efects. It has proven dificult to accurately estimate future trends in COVID-19 infections using legacy infection prediction models. One important reason for this is the circulation of unverified information on social media platforms; this information, which may influence individual behaviour, often conflicts with information communicated via oficial governmental communication channels (Ma et al., 2020; Shiina et al., 2020). When face-to-face contact is limited, many people turn to social media to obtain information and communicate their own assessments of the situation (Han et al., 2020; Nabity-Grover et al., 2020), which may shape their disease prevention behaviour (Janz & Becker, 1984; Abraham & Sheeran, 2005). Obtaining accurate, up-to-date information about COVID-19 from social media can help prevent the disease, but fake news can have the opposite efect (Jo et al., 2020; S. Li et al., 2020; Wang et al., 2020).

Failing to consider the influence of these patterns of social communication on individual behaviour may be afecting the accuracy of infection-prediction models. Therefore, we propose an adjusted SEIR model for COVID-19 that reflects social media efects over a long incubation period. We contribute to the infection-prediction literature by showing how SEIR model accuracy improves when social media efects are considered. Improving IS to increase the accuracy of longterm forecasts could significantly strengthen the global response to the COVID-19 pandemic. This study (our improved SEIR model) contributes to the IS literature in the fight against COVID-19 (Ågerfalk et al., 2020; Mendling et al., 2020) by systematically collecting digital information from social media platforms and using computational algorithms to analyse the spread of digital information, thereby supporting policies and campaigns aimed at combatting the pandemic and infodemic.

## 2. Theoretical foundations

In addition to the SEIR, researchers use several models to predict infections, such as the Probabilistic Infection Model (PIM) and the Susceptible–Infected–Recovered (SIR) model (Anderson & May, 1992; He et al., 2020; Hou et al., 2020; M. Y. Li et al., 1999; Yang et al., 2020; Zhang & Ma, 2003). Here, we show how modifying the

SEIR model to account for social media efects improves the accuracy of COVID-19 infection forecasts.

It is important to understand factors that make individuals (un)willing to engage in disease prevention behaviour, because individual disease prevention behaviour and attitudes influence how quickly COVID-19 spreads. In our modified SEIR model for forecasting COVID-19, the motives for social media use are classified into information motivations and social motivations, which are further divided into positive function and negative function groups. Social media use driven by information motivations may be associated with a decrease or increase in the number of COVID-19 infections, and positive functions and negative functions are considered to follow the Poisson distribution. Furthermore, news concerning COVID-19 infections is assumed to stimulate social media use driven by social motivations. In this section, we present the theoretical foundations for this study. We review the history of epidemic models and evidence regarding the motivations and efects of social media use which underpins our modified SEIR model for forecasting COVID-19 infections (see Figure 1).

## 2.1. Epidemic prediction models

Various epidemic prediction models have been developed to understand the trajectories and efects of diseases throughout human history. For instance, a sudden outbreak with a high infection rate may result in ongoing economic stagnation. Some epidemics, such as the Great Plague, appear suddenly and spread intensely before disappearing, leaving behind an uninfected population. Models have been used to identify trends associated with the spread of severe diseases and immunity (Bell, 1924).

Epidemic prediction models have been developed to help theorise why diseases appear suddenly and then disappear without infecting all population groups. Using a difusion model of malaria as an epidemic carried by mosquitoes, Ross (1911) developed prevention and treatment protocols. Nine years after the Spanish flu pandemic of 1918, Kermack and McKendrick (1927) developed the first mathematical model of disease outbreaks, the K&M model, which compartmentalises diferent classes of the population and mathematically determines hourly rates of transmission from one compartment to another.

Developed more recently, SI and SIR are parceltype infectious disease models that describe disease progression through the following stages (Anderson & May, 1992; M. Y. Li et al., 1999; Zhang & Ma, 2003):

Susceptible (S): A person who is not immune to infection and can become infected if exposed;

![](/api/attachments/CH3VFT5Y/fulltext/images/8695f9229b6be9c111037a1e9853b1d58ec44db68c98f8905dfb696e8848fa2b.jpg)  
Figure 1. Research model.

Infectious (I): A person who is currently infected and can infect others by contact with a sensitive individual;

Recovered (R): A person who is immune to infection and does not infect others when in contact with other individuals.

The total population N is computed by the sum of the populations S +I +R. Each component must be an integer, but if N is large enough, S, I, and R can be considered continuous variables.

Lee et al. (2009) used a SIRS model, whereby people can become susceptible after recovering, to estimate the distribution of people infected with tsutsugamushi disease in South Korea using a hindsight formula. Despite their utility, SI and SIR models do not accurately predict infections for diseases with incubation periods. To overcome this limitation, Assiri et al. (2013) added a fourth stage, “Exposure,” to the SIR model, and used the resulting SEIR model to account for the incubation period for Middle East Respiratory Syndrome (MERS). Figure 2 compares existing epidemic prediction models.

In our empirical study, the SEIR model is appropriate because it accounts for the latency period of COVID-19. Detailed elements are extracted to predict COVID-19 infection, taking into account factors such as high infection rates, longer incubation periods of up to 14 days, and general mortality.

## 2.2. Motivations for social media use

Social learning theory (Bandura, 1978), which posits that a person’s behaviour is afected by observing the behaviour of others, explains the interaction between social media usage and COVID-19 infections in our study. In addition, Uses and Gratification theory (U&GT) has been used to study motivations for social media use According to U&GT, audiences choose to use specific media for hedonic, utilitarian, and social gratification purposes (Katz et al., 1974). From a U&GT perspective, the intent of social media use is determined by a range factors. For example, studies have shown that people use Facebook for various purposes, including hedonistic gratification (e.g., diversion); utilitarian gratification (e.g., selfrepresentation); and social gratification (e.g., relationships, voyeurism, social utility, and herd instincts) (Bumgarner, 2007). Forms of social gratification may be diverse; for example, Joinson (2008) identified social connection, shared identity, social investigation, and social network surfing as motivations for Facebook use, and Coursaris et al. (2010) identified championship, entertainment, escape, information, following new and cool trends, passing the time, professional advancement, relaxation, self-expression, and social interaction as motivations for Twitter use. An alternative model divides motivation into two main categories, social motivation and information motivation (Johnson & Yang, 2009), with only a few gratification factors. Rather than U&GT, some scholars have explained social media motivation by employing intrinsic motive theory (Allam et al., 2019) and goal system theory (Knoll et al., 2020). Until recently, however, little research has been done to identify motivations for using social media in a pandemic situation. Here, we adopt Johnson and Yang (2009) model and address the distinction between social motivations and information motivations.

![](/api/attachments/CH3VFT5Y/fulltext/images/79d9f78bd65246963c9df5a6d6fd9e8477d0574834aef64d20600914e2d5a9d3.jpg)  
Figure 2. Epidemic prediction models.

## 2.3. Influence of social media in healthcare

Studies have been conducted on the influence of social media on disease prevention behaviour. Work on the efects of social media on healthcare practices or disease prevention can be largely divided into positive function studies and negative function studies (Tables 1 and 2). First, social media are useful for collecting and distributing real-time information on disasters (Huang et al., 2010), identifying the status of diseases (Chou et al., 2009), conducting promotional campaigns and health education, and managing outbreaks to address disasters (D’Alessandro et al., 2012; Norman & Yip, 2012). Social media can also help individuals understand aspects of the problem. For example, after the 2009 outbreak of H1N1 became a pandemic (Chew & Eysenbach, 2010), keywords and emotional values on Twitter were highly correlated with the degree of H1N1 in particular locations. This means that what is expressed on social media can be used to measure the spread of disease. In addition, social media can be an important public resource for identifying the status of a disease (e.g., the type of people who are sick) (Chou et al., 2009).

Table 2. Negative functions of social media.

<table><tr><td>Type</td><td>Source</td></tr><tr><td>Finding targets for harassment</td><td>Mitchell et al. (2010)</td></tr><tr><td>Propagating bad behaviour (including drug use, suicidal tendencies)</td><td>Robertson et al. (2012)</td></tr><tr><td>Setting up criminal or other negative meetings</td><td>Blackwell (2009)</td></tr><tr><td>Disseminating product information that is harmful to health</td><td>Jenssen et al. (2009)</td></tr><tr><td>Exposure to negative emotional indicators such as stress</td><td>Egan and Moreno (2011)</td></tr><tr><td>Distributing fake news</td><td>Scanfeld et al. (2010)</td></tr></table>

Table 1. Positive functions of social media.

<table><tr><td>Type</td><td>Source</td></tr><tr><td>Spreading information about healthy behaviours and therapies</td><td>Rosselli et al. (2011)</td></tr><tr><td>Forming continuous channels with patients</td><td>Khosropour and Sullivan (2011)</td></tr><tr><td>Influencing positive behavioural and social change</td><td>Dowdell et al. (2011)</td></tr><tr><td>Public relations</td><td>Thackeray et al. (2012)</td></tr><tr><td>Contact point to meet customers to provide service</td><td>Oh and Lee (2012)</td></tr><tr><td>Recruitment</td><td>Ramo and Prochaska (2012)</td></tr><tr><td>Discovery of social pathology</td><td>Leighton et al. (2012)</td></tr><tr><td>Identifying public opinion</td><td>Stephenson et al. (2010)</td></tr><tr><td>Online doctor visits</td><td>Silenzio et al. (2009)</td></tr><tr><td>Data collection</td><td>Sullivan et al. (2011)</td></tr><tr><td>Information sharing</td><td>Weitzman et al. (2011)</td></tr><tr><td>Disseminating good news</td><td>Feldacker et al. (2011)</td></tr><tr><td>Potential behavioural correction</td><td>Feldacker et al. (2011)</td></tr></table>

Social media also have negative functions. For example, users may harass others on social media (Ybarra & Mitchell, 2008), share inaccurate information on risk behaviours (Young & Rice, 2011), promote harmful or useless products (Freeman & Chapman, 2010; Grifiths & Casswell, 2010), or circulate fake news (e.g., incorrect directions for drug use) (Scanfeld et al., 2010).

## 3. Research methodology

## 3.1. Data collection

We chose South Korea as the setting for our empirical study investigating social media efects on COVID-19 infection forecasts. Data on COVID-19 were collected from press releases distributed by the Korea Centers for Disease Control and Prevention (http://ncov.mohw.go.kr). social media data were taken from the news database search site, BigKinds (https://www.bigkinds.or.kr/). Rather than collecting frequency data for all information shared on social media, BigKinds classifies articles based on content, and classifies the positive functions and negative functions of social media.

Table 3. Media and social media platform frequency.

<table><tr><td rowspan="2">social media</td><td colspan="4">Frequency of mentions by media outlet (n = 2,067)</td></tr><tr><td>Kyunghyang Shinmun (n = 423)</td><td>Chosunilbo (n = 507)</td><td>Korea JoongAng Daily (n = 893)</td><td>Hankyoreh (n = 245)</td></tr><tr><td>YouTube</td><td>104</td><td>115</td><td>219</td><td>71</td></tr><tr><td>Facebook</td><td>171</td><td>201</td><td>343</td><td>98</td></tr><tr><td>Instagram</td><td>20</td><td>26</td><td>81</td><td>14</td></tr><tr><td>Twitter</td><td>86</td><td>121</td><td>141</td><td>41</td></tr><tr><td>Weibo, Wechat</td><td>1</td><td>5</td><td>9</td><td>1</td></tr><tr><td>KakaoTalk</td><td>3</td><td>8</td><td>25</td><td>1</td></tr><tr><td>Comments</td><td>38</td><td>30</td><td>75</td><td>19</td></tr><tr><td>Online Community Cafe</td><td>0</td><td>1</td><td>0</td><td>0</td></tr></table>

We collected social media data for four media companies based on circulation and political tendencies (e.g., right/left wing; see Table 3). We searched for keywords related to COVID-19 and particular forms of social media activities (e.g., comments, group chats) posted between February 15 and March 31 2020. This process yielded 2,095 social media posts; after eliminating posts with irrelevant content, we analysed 2,067 posts.

## 3.2. Research design

First, we classified the motives for social media use into information motivations and social motivations, and sub-divided them into positive function and negative function groups (see Table 4). We assumed a relationship between information motivation and a decrease or increase the number of COVID-19 infections, and that positive functions and negative functions followed a Poisson distribution. Furthermore, we assumed news concerning COVID-19 infections stimulated the social motivation for social media use. Using content analysis techniques, we classified social media use motivation in the context of COVID-19. The three authors discussed and resolved coding discrepancies based on patterns in the overall dataset (Table 5).

Second, to account for social media efects, we modified the SEIR model to reflect characteristics of the COVID-19 pandemic. For each social media activity that appears in the classification (Tables 3 and 5), the following efects are expected in the modified SEIR model (Table 6):

(1) Social media use rarely occurs when suspected infections or confirmed cases begin to occur. social media use at t = 0 has nothing to do with the number of infectious cases.

(2) Social media use driven by the information motivation precedes or follows the confirmed COVID-19 infection cycle.

(3) Social media use driven by the social motivation follows the confirmed infection cycle.

(4) Social media use with a negative function (e.g., fake/non-verified news/information) is associated with an increase in the number of infectious cases of COVID-19.

(5) Social media use with a positive function (e.g., verified news/information) is associated with a decrease in the number of infectious cases of COVID-19.

(6) The lifecycle of social media use driven by the information motivation increases as the number of infectious cases increases. In other words, the social media post lifecycle is a function of time t, where the first half is proportional to time, and the second half is inversely proportional to time.

(7) As the number of COVID-19 infections decreases, the lifecycle of social media use driven by the information motivation decreases.

(8) The extent of the increase in the lifecycle of social media posts is proportional to the extent of the increase in the number of infectious cases. Therefore, a multiplier for the scale of social media is included.

## 4. Results

4.1. Forecasting COVID-19 infections using a SEIR model

We used R software to analyse data from South Korea using our modified SEIR model. In a SEIR model, a forecast’s period and magnitude vary

Table 4. Social media classification of infection routes.

<table><tr><td>Motivation</td><td>Positive function(verified information)</td><td>Negative function(non-verified/fake information)</td></tr><tr><td>Information motivation</td><td>Type: information provision, publicity, guidance, etc.Time of occurrence: Before and after an outbreakEffects: Reducing the degree of infection (e.g., methods of disinfection); increasing the number of tests (i.e., sharing information about testing)(Lamb et al., 2013)</td><td>Type: Fake news, fraud, creating anxiety, etc.Time of occurrence: Before and after an outbreakEffects: Increasing the degree of infection (e.g., incorrect methods of quarantine) (Ali, 2020; Peters et al., 2018)</td></tr><tr><td>Social motivation</td><td>Type: Suggestions, campaigns, promoting rallies for empathy and encouragement, etc.Time of occurrence: After an outbreakEffects: Reducing the degree of infection (e.g., reduced contact with infectious agents) (Zhang et al., 2016)</td><td>Type: Unethical public opinion, relative abuse, illegal promotion, victim identity leakage, the promotion of addiction, etc.Time of occurrence: After an outbreakEffects: Not related to the degree of infection (Boberg et al., 2020)</td></tr></table>

Table 5. Frequency of social media motivation and function (n = 2,067).

<table><tr><td>Motivation</td><td>Function</td><td>Content</td><td>Frequency</td></tr><tr><td rowspan="13">Social motivation (n = 1429)</td><td rowspan="8">Positive function (n = 1109)</td><td>Social movement</td><td>375</td></tr><tr><td>Expression of opinion</td><td>334</td></tr><tr><td>Leisure</td><td>106</td></tr><tr><td>Economic activity</td><td>106</td></tr><tr><td>Education</td><td>70</td></tr><tr><td>Politics and society</td><td>54</td></tr><tr><td>Participation</td><td>39</td></tr><tr><td>Empathy</td><td>25</td></tr><tr><td rowspan="5">Negative function (n = 320)</td><td>Unethical public opinion</td><td>218</td></tr><tr><td>Harming others</td><td>78</td></tr><tr><td>Illegal promotion</td><td>15</td></tr><tr><td>Victim identity leakage</td><td>8</td></tr><tr><td>Addiction promotion</td><td>1</td></tr><tr><td rowspan="3">Information motivation (n = 639)</td><td rowspan="2">Positive function (n = 579)</td><td>Information provision</td><td>571</td></tr><tr><td>Breaking the digital divide</td><td>8</td></tr><tr><td>Negative function (n = 60)</td><td>Fake news</td><td>60</td></tr></table>

greatly depending on the values assigned for contact rate, transmission probability, contagious period, and latency period (Cauchemez & Ferguson, 2008; Lloyd, 2001; Wallinga & Lipsitch, 2007). We began our analysis by determining the initial values for these four factors (Cappé et al., 2007; Harville & Jeske, 1992). To find the most suitable initial value, we used the Monte Carlo methodology (Mooney, 1997) to identify how risk and uncertainty afect the SEIR forecasting model, which is based on computational algorithms (Kroese et al., 2014). It was important to accurately reflect the characteristics of COVID-19 when designating the range of initial values in the SEIR model. Using the incubation period and information on COVID-19 infections, we derived the initial SEIR model using the lowest value of the mean square error (MSE) between confirmed infections (not recovered or not dead) and forecasted infectionThen, we reexamined the prediction period using the initial values most suitable for the Korean situation (see Figure 3).

## 4.2. Impact of information-driven social media use on COVID-19 infection rates

We propose an adjusted SEIR model to more accurately predict the number of COVID-19 infections by accounting for the impacts of exposure to positive and negative information via social media (antecedents in Figure 1). The cumulative duration of an social media post is used as a proxy for the size of the efectðwÞ of social media on the number of COVID-19 infections (Grissom & Kim, 2005). Thus, four models are assumed, as shown in Table 7, to reflect the probability density function (i.e., normal and Poisson distributions) based on exposure to positive and negative information.

Model 1

Adjusted (I) =

$$
\sum_ {t = 1} ^ {n} w * I F _ {t} * N (\mu , \sigma^ {2}) + \sum_ {t = 1} ^ {n} w * I M _ {t} * P o i (\lambda)
$$

Model 2

Adjusted (I) =

$$
\sum_ {t = 1} ^ {n} w * I F _ {t} * N (\mu , \sigma^ {2}) + \sum_ {t = 1} ^ {n} w * I M _ {t} * N (\mu , \sigma^ {2})
$$

Model 3

Adjusted (I) =

$$
\sum_ {t = 1} ^ {n} w * I F _ {t} * P o i (\lambda) + \sum_ {t = 1} ^ {n} w * I M _ {t} * N (\mu , \sigma^ {2})
$$

Model 4

$$
\begin{array}{l} \text {Adjusted (I)} _ {n} = \\ \text {SEIR(I) - \sum_ {t = 1} w*IF_ {t}*Poi(\lambda) + \sum_ {t = 1} ^ {n} w*IM_ {t}*Poi(\lambda)} \end{array}
$$

Table 6. COVID-19 infection-prediction elements and formulas for the SEIR model.

<table><tr><td>Element</td><td>Description</td><td>Formula</td></tr><tr><td>S(t)</td><td>Number of susceptible individuals at time t</td><td>S(t-1) + dS</td></tr><tr><td>E(t)</td><td>Number of exposed individuals at time t</td><td>E(t-1) + dE</td></tr><tr><td>I(t)</td><td>Number of infectious individuals at time t</td><td>I(t-1) + dI-dM</td></tr><tr><td>R(t)</td><td>Number of recovered individuals at time t</td><td>R(t-1) + dR</td></tr><tr><td>M(t)</td><td>Number of deaths at time t</td><td>M(t-1) + dM</td></tr><tr><td>dS</td><td>Increase in susceptible individuals over a period of time</td><td>-beta * S(t-1) * I(t-1)</td></tr><tr><td>dE</td><td>Increase in exposed individuals over a period of time</td><td>[beta * S(t-1) * I(t-1)] - [delta * E(t-1)]</td></tr><tr><td>dI</td><td>Increase in infectious individuals over a period of time</td><td>dI = [delta * E(t-1)] - [gamma * I(t-1)]</td></tr><tr><td>dR</td><td>Increase in recovered individuals over a period of time</td><td>dR = gamma * I(t-1)</td></tr><tr><td>dM</td><td>Increase in deaths over a period of time</td><td>dM = epsilon * I(t-1)</td></tr><tr><td>beta</td><td>Transfer rate</td><td>contact_rate * transmission_probability</td></tr><tr><td>gamma</td><td>Recovery rate</td><td>1/infectious_period</td></tr><tr><td>delta</td><td>Infection rate</td><td>1/latent_period</td></tr><tr><td>contact_rate</td><td>Number of contacts per day</td><td>Default 20</td></tr><tr><td>transmission_probability</td><td>Transmission probability</td><td>Default 0.06</td></tr><tr><td>infectious_period</td><td>Infectious period</td><td>Default 7</td></tr><tr><td>latent_period</td><td>Incubation period</td><td>Default 14</td></tr></table>

SEIR epidemic  
![](/api/attachments/CH3VFT5Y/fulltext/images/b4ea1ceed0d597188ff2b62c54d50f0bf063cdbf2b3ba8887594077474fade5e.jpg)  
Figure 3. Initial SEIR model results for South Korea. (Note: # susceptible: blue; # exposed: purple; # infectious: red; # recovered: green. All data are shown in Table 6.).

Table 7. Classification of proposed models by distribution.

<table><tr><td rowspan="2">Negative information function (IM)</td><td colspan="2">Positive information function (IF)</td></tr><tr><td>Normal distribution</td><td>Poisson distribution</td></tr><tr><td>Poisson distribution</td><td>Model 1</td><td>Model 4</td></tr><tr><td>Normal distribution</td><td>Model 2</td><td>Model 3</td></tr></table>

[Note: IF = information function (positive); IM = information function (mal/negative); n = period (3 days–15 days); μ ¼ mean of normal distribution (n/2 + random number); σ ¼ standard deviation, (1– n=2increase per 0.05); w = efect size (10–100, decile value); λ = mean of Poisson distribution (1–n increase per 1)]

15 days after the incubation period, reflecting the time it takes for the infection rate to increase or decrease after information is spread via social media. Based on its efect size, each social media post was assigned a decile weight value between 10 and 100 (e.g., 20, 30, etc.). In addition, we used the Monte Carlo method to derive the best model based on MSE.

A distribution condition must be defined for the proposed model because the distribution afects the results. Using the Monte Carlo methodology, the period for determining the distribution was set to 3 to

The original SEIR model predicted mean square error of 679,566.3 of confirmed COVID-19 infections in South Korea. The adjusted SEIR model reflecting social media efects was run 4,579,600 times to produce optimal results. The conditions for the normal distribution and the Poisson distribution for the optimal MSE by model are presented in Table 8. Each represents the period, mean of normal distribution, standard deviation of normal distribution, mean Poisson distribution, and size of social media efect. Model 4 shows the best performance based on mean square error (approximately 48% lower than the initial SEIR model, nearly doubling its accuracy).

Table 8. Performance comparison of proposed models.

<table><tr><td>Model</td><td>Positive information motivation (IF)</td><td>Negative information motivation (IM)</td><td>Mean square error (MSE)</td></tr><tr><td rowspan="4">Model 1</td><td>n = 3</td><td>n = 15</td><td>364818.8</td></tr><tr><td>ω = 20</td><td>ω = 10</td><td></td></tr><tr><td>μ = 1.5</td><td>λ = 9</td><td></td></tr><tr><td>σ = 1.2</td><td></td><td></td></tr><tr><td rowspan="4">Model 2</td><td>n = 3</td><td>n = 9</td><td>368713.2</td></tr><tr><td>ω = 20</td><td>ω = 100</td><td></td></tr><tr><td>μ = 1.5</td><td>μ = 4.5</td><td></td></tr><tr><td>σ = 1.2</td><td>σ = 2.1</td><td></td></tr><tr><td rowspan="4">Model 3</td><td>n = 3</td><td>n = 9</td><td>366142.8</td></tr><tr><td>ω = 20</td><td>ω = 100</td><td></td></tr><tr><td>λ = 2</td><td>μ = 4.5</td><td></td></tr><tr><td></td><td>σ = 2.1</td><td></td></tr><tr><td rowspan="3">Model 4</td><td>n = 5</td><td>n = 11</td><td>359670.9</td></tr><tr><td>ω = 20</td><td>ω = 100</td><td></td></tr><tr><td>λ = 2</td><td>λ = 5</td><td></td></tr></table>

![](/api/attachments/CH3VFT5Y/fulltext/images/12e17f18ce2dcd00327a96a3dfa5a90bdfd6b2e37ccc6017efaa8124f8a96792.jpg)  
(a) Model 1

![](/api/attachments/CH3VFT5Y/fulltext/images/f7c6a3a24006d1dfa40d6b806d4abf1452491226cc2702d72e3bb93f69b22ce2.jpg)  
(c) Model 3  
Figure 4. Optimal values by proposed model.

Figure 4 visualises the results based on the conditional values from Table 8. The adjusted SEIR model reflecting social media efects appears in orange, the initial (legacy) SEIR model appears in grey, and the actual number of infections appears in blue for forecasting COVID-19 infections. The results for the adjusted model (particularly Model 4) more closely reflect the actual infection trend than those of the initial (legacy) SEIR model.

## 4.3. Efects of COVID-19 infection on social motivation for social media use

The social motivation for social media use (Tables 4 and 5) was assumed to be influenced by the number of COVID-19 infections, and then influence both positive and negative function in our proposed model (consequences in Figure 1). Social motivation may occur immediately on the day of impact, but also may continue over a certain period of time (± 3 days); to account for this, we used multiple regression analysis about the number of confirmed cases. We also incorporated data about information motivation. As shown in Table 9, the results show a positive relationship between the number of infections and social motivation for social media use on a given day $( \mathrm { S F } ( t ) , \ p = . 0 3 8 )$ and three days later $( \mathrm { S F } ( t + 3 ) , p =$ .086). These relationships are significant at the p < .10 level, a common threshold in the fields of biochemistry, medicine, and ecology (Cook & Day, 1998; Graham, 2003; Topliss & Costello, 1972). As the number of infections grew, individuals exhibited more social motivation to use social media, in the form of expressing opinions, joining campaigns, and encouraging rallies for empathy and encouragement immediately following the increase and again several days later. Moreover, the adjusted $R ^ { 2 }$ indicates that 54.9% of variance for the number of infections is explained by the variance in positive social motivation [SF(t), SF (t + 3)], and the positive [IF(t)] and negative [IM(t)] information function.

(b) Model 2  
![](/api/attachments/CH3VFT5Y/fulltext/images/8919524b9a3e46bbba27eda616a7f49a7cf464fdbf63f5fe64eb7e6144e9b723.jpg)

![](/api/attachments/CH3VFT5Y/fulltext/images/8ace8a2378b34c64348c8598cde9b265bbb4eccf0952bd756c31092fc8451bae.jpg)  
(d) Model 4

Table 9. Results of multiple regression analysis.

<table><tr><td rowspan="2">Independent variable</td><td colspan="2">Unstandardised regression coefficient</td><td>Standardised regression coefficient</td><td rowspan="2">t</td><td rowspan="2">p</td></tr><tr><td>B</td><td>Standard error</td><td>Beta</td></tr><tr><td>Constant</td><td>271.4</td><td>649.8</td><td></td><td>.418</td><td>.678</td></tr><tr><td>SF(t)</td><td>92.2</td><td>42.9</td><td>.375</td><td>2.151</td><td>.038</td></tr><tr><td>SM(t)</td><td>83.3</td><td>132.6</td><td>.120</td><td>.628</td><td>.534</td></tr><tr><td>SF(t +1)</td><td>26.0</td><td>48.0</td><td>.104</td><td>.541</td><td>.591</td></tr><tr><td>SM(t +1)</td><td>-105.8</td><td>108.4</td><td>-.152</td><td>-976</td><td>.335</td></tr><tr><td>SF(t +2)</td><td>75.5</td><td>46.9</td><td>.304</td><td>1.609</td><td>.116</td></tr><tr><td>SM(t +2)</td><td>-50.8</td><td>105.7</td><td>-.072</td><td>-.480</td><td>.634</td></tr><tr><td>SF(t +3)</td><td>68.4</td><td>38.8</td><td>.268</td><td>1.760</td><td>.086</td></tr><tr><td>SM(t +3)</td><td>-118.1</td><td>93.6</td><td>-.164</td><td>-1.262</td><td>.215</td></tr><tr><td>IF(t)</td><td>-121.7</td><td>63.5</td><td>-.340</td><td>-1.918</td><td>.062</td></tr><tr><td>IM(t)</td><td>855.8</td><td>320.5</td><td>.370</td><td>2.670</td><td>.011</td></tr></table>

R<sup>2</sup> = .641; Adjusted $R ^ { 2 } = . 5 4 9 ; \mathrm { d f } = 1 0 ; F = 6 . 9 5 7$  
Note: SF: social motivation function; SM: social motivation negative func tion; IF: information positive function; IM: information negative function

## 5. Discussion

Our findings show how using a modified SEIR model may help improve the accuracy of COVID-19 infection forecasts. Moreover, by providing evidence of social media efects, we reveal the need to establish efective IS support to ensure a more accurate epidemic infection-prediction model for a disease with a long incubation period. We discuss theoretical and practical implications of our findings, as well as limitations of our study and opportunities for future research. Overall, IS development could help improve the accuracy of infection models, thereby supporting efective infectious disease prevention behaviour campaigns and systematic information control during the pandemic.

First, we tested an adjusted SEIR model that accounts for the forecast period, COVID-19 contact rate, transmission probability, contagious period, and latency period (Cauchemez & Ferguson, 2008; Lloyd, 2001; Wallinga & Lipsitch, 2007) as well as social media efects. We found that our adjusted SEIR model which accounts for social media efects nearly doubles the predictive accuracy of the initial SEIR model. In other words, the results show that trends in COVID-19 infectious cases afect the use of social media, which in turn afects the number of COVID-19 infections. Ours is the first empirical study of COVID-19 to demonstrate that accounting for social media efects improves the accuracy of legacy infection models over a long incubation period. Supported by appropriate IS, the adjusted model can support efective infectious disease prevention marketing campaigns.

In particular, since the emergence of COVID-19, the total number of positive and negative social media posts has increased, and the number of positive posts (e.g., accurate information about disease prevention measures) has increased significantly relative to negative posts. This may be due to a change in the behaviour of people who want to address the pandemic by promoting disease prevention through social media. The increase in social media use is positively associated with the number of COVID-19 infections; in turn, the number of infections influences social motivation for social media use, such as empathy for others or criticism of scapegoats to shift responsibility.

In addition, the results show that social media serve as valid nonmedical intervention platforms and should be viewed as critical resources in the global response to the pandemic, not only at the individual level, but also at the government level. More accurate forecasts can help governments, agencies responsible for controlling infectious diseases, citizens, medical professionals, consumers, and retailers prepare for next steps during the pandemic. This study shows that social media can be used strategically to help reduce the spread of infectious diseases by influencing people’s psychological responses and reinforcing disease prevention behaviours.

Finally, we also found that as the number of COVID-19 infections grew, individuals exhibited more social motivation to use social media (e.g., expressing opinions, joining campaigns, and encouraging rallies for empathy and encouragement) to influence both positive and negative behaviours on the day of impact or over a certain period of time (e.g., ± 3 days) based on the number of confirmed (infected) cases in regression analysis.

The results of our empirical study have important theoretical implications for researchers, and practical implications for agencies responsible for disease prevention programmes, businesses and educational institutions, which we outline below.

## 5.1. Theoretical implications

Our findings make several theoretical contributions to the literature on predictive infection models, particularly in the context of a global pandemic, when controlling a disease depends largely on citizens’ disease prevention behaviour. First, we improved a predictive SEIR model with four factors – contact rate, transmission probability, contagious period, and latency period (Cauchemez & Ferguson, 2008; Lloyd, 2001; Wallinga & Lipsitch, 2007) – by accounting for social media efects in contemporary society. Our empirical findings demonstrate the importance of accurate information in combatting the infodemic in social media. Our adjusted SEIR model reflecting social media efects contributes to the literature of predictive infection models by improving the accuracy of traditional epidemic prediction models such as SI and SIR (Anderson & May, 1992; M. Y. Li et al., 1999; Zhang & Ma, 2003), SIRS (Lee et al., 2009), PIM and SER (Anderson & May, 1992; He et al., 2020; Hou et al., 2020; M. Y. Li et al., 1999; Yang et al., 2020; Zhang & Ma, 2003), and SEIR (Assiri et al., 2013).

Our empirical results contribute to the epidemic prediction literature by demonstrating how content analysis can be used to account for exposure to positive and negative information and adjust the initial values of the four factors (contact rate, transmission probability, contagious period, and latency period) to more accurately predict the number of COVID-19 infections. In addition, our study makes a methodological contribution by demonstrating the utility of the Monte Carlo methodology (Mooney, 1997) for identifying how risk and uncertainty (i.e., social media efects) afect the SEIR forecasting model (Kroese et al., 2014). Specifically, we have shown how computational algorithms can be used to reflect the probability density function (normal and Poisson distributions) based on exposure to positive and negative information via social media. To cope with the COVID-19 pandemic, accurate information that can help prevent infection is important, and false information or rumours can negatively afect the spread of infection and increase fear (Ali, 2020). Using the Monte Carlo methodology to account for the efects of exposure to false information on social media constitutes a major contribution to the disease infection and prediction model literature.

Second, our findings regarding social media efects that influence individual disease prevention behaviour also contribute to the social media literature by highlighting the utility of social learning theory (Bandura, 1978), which posits that a person’s behaviour is afected by observing the behaviour of others (e.g., interaction between social media usage and COVID-19 infections). In a networked society, information such as texts, videos of lectures, and interviews with experts can be easily accessed via social media (Park et al., 2014). If information is accurate social media can have a positive efect on social learning (Cai et al., 2020). Due to the untact life situation that has become the new norm during the pandemic, social media is playing an extremely critical role as a both a source of information about COVID-19 and a way to interact with the outside world. By accounting for social media efects to improve the accuracy of infection models, our study highlights how social learning theory can be used to inform eforts to combat the pandemic and infodemic which rely on individual disease prevention behaviour.

Furthermore, we contribute to literature regarding the theoretical motivation for social media usage based on Uses and Gratification theory (Katz et al., 1974), especially social gratification (Bumgarner, 2007; Joinson, 2008), leading to an alternative model of both social and informational motivation (Johnson & Yang, 2009). It is important to identify people’s moti vation for using social media during this pandemic. Our study provides empirical evidence of the positive and negative function of social media for informational and social motivations during the pandemic. Previously, social media usage was found to be driven primarily by a desire to escape normal life (Coursaris et al., 2010); however, during the pandemic, socia media usage has been driven by informational and social motivations. The influence of social media on global health behaviour during the pandemic is unprecedented. This social media usage diference between traditional escapist tendency and informational and social motivations is attributable to the use of social media to actively change the behaviour of individuals or groups to combat the COVID-19 pandemic and infodemic. Based on our findings, social media efects difered at diferent stages of the pandemic. For example, until February 18 when a super-spreading event was traced to a highly infectious patient in South Korea, the use of social media to obtain or share COVID-19 related information was not noticeable. When it became clear that COVID-19 would become a pandemic, an infodemic ensued, stirring up anxiety and impeding eforts to stop the spread. However, in later stages, eforts to stabilise the situation could be interpreted as increasing the positive function of social media as the number of infections increased, along with COVID-19 testing and the social threat of expo sure to COVID-19. Particularly, the positive function and negative function of social motivation could be interpreted as sources of protection and propagation, respectively, in a hazardous situation (Zhao et al., 2014). During the early stages, slandering and hate speech were the main focus, but as time went by, a sense of shared responsibility became a functional element. In sum, our study contributes to the motivation literature by empirically demonstrating the social and informational motivations of social media usage, and the positive and negative functions at diferent stages based on actual numbers of COVID-19 infections.

## 5.2. Practical implications

Our findings have some practical implications for agencies responsible for disease control and prevention, businesses, and educational institutions. First, the agencies responsible for controlling infectious diseases in each country may be able to more accurately predict COVID-19 infections and systematically control the pandemic situation by using IS that accounts for social media efects and implementing our adjusted SEIR model. Furthermore, because information-driven social media usage precedes the occurrence of infectious cases, we suggest utilising IS to perform social media analysis when developing disease prevention marketing campaigns to combat COVID-19 and the infodemic. In the future, agencies responsible for disease control should learn lessons from this pandemic and work cooperatively with social media platforms during early stages of an outbreak by consistently providing accurate information before a mal/negative function of social media leads to an uncontrollable infodemic. Because social media efects influence individual disease prevention behaviour during untact pandemic life, it is important to use the adjusted SEIR to improve the accuracy of information communicated via social media when a disease has a long incubation period. This is the first study to provide empirical evidence of the influence of specific social media efects on COVID-19 infection propagation and suppression. Supported by efective IS, the adjusted SEIR improves forecasts, thereby helping various stakeholders, including citizens, governments, medical workers, consumers, and retailers prepare for next steps (e.g., reopening or lock down strategies).

Second, to prepare their businesses for the next stages of the pandemic, businesses might monitor predicted infection rates based on our model. Doing so might enable them to predict how long it will take for the consumption environment to return to normal, and adjust their retail strategies accordingly. For example, retailers may reallocate human resources to online/virtual platforms, supply chain management (e.g., relationship with logistics company, inventory controls), and online consumer data analysis if the pandemic lasts longer. In addition, monitoring predicted infection rates may help firms make decisions regarding their work environments (e.g., remote working environment, video conferencing, etc.). An accurate infection model is important to enable businesses to survive during the pandemic and prepare for operations after the pandemic.

Third, educators and institutions should monitor predicted infection rates to appropriately prepare for transitions among various education formats such as face-to-face, online, and hybrid formats. Accurate information about the predicted infection rate can help educators know when to switch between teaching formats and make plans for upcoming semesters to minimise chaos among students, parents, educators, and administrators. Accurate information also can help administrators decide how to best allocate funding and human resources to facilitate transitions between formats.

## 5.3. Limitations and future research

We have focused on addressing the infodemic by accounting for social media efects over a long COVID-19 incubation period to increase the accuracy of infection prediction models. Nevertheless, our study has some limitations which highlight opportunities for future research.

First, we used actual data regarding the COVID-19 infection rate and analysed social media contents to more accurately predict infection rates in a single country. In future research, cross-cultural studies examining social media efects in multiple countries would be beneficial to validate our model in the global context. Specifically, it would be important to investigate which communication channels work best for sharing accurate information in each country. Importantly, our adjusted infection prediction model might not be useful in countries with insignificant social media efects or in countries that control social media usage. Models that consider other social impacts will need to be developed to accurately predict infection rates and support disease prevention behaviour in those countries.

Second, building on our findings about social media efects, scholars should investigate the best ways to use IS to support the spread of accurate disease prevention information. For example, social disease prevention campaign apps could be developed to support social education by detecting and refuting false information and providing the most up-to-date disease prevention guidelines from the agencies responsible for disease prevention and control in each country.

Finally, we investigated social media efects in the context of a infection prediction model. However, social media efects during the pandemic are also evident in other contexts, providing opportunities for future research. For example, in South Korea, small business owners/suppliers had to sell food and ingredients quickly to avoid food spoilage during the pandemic. Suppliers who were having dificulties disclosed their situation on social media; as information spread about what was available for sale, a proconsumption campaign ensued. Many other cities followed suit, and helped small business owners while preventing disease by creating drive-through street markets. In future research, it may be interesting to examine similar positive social media efects that help businesses and consumers maintain untact consumption behaviours necessary for disease prevention.

In conclusion, our analysis of data related to the COVID-19 pandemic reveals that developing efective IS is critical to improve the accuracy of predictive infection models and support disease prevention behaviour. To efectively combat the current pandemic, governments in each country should make an efort to develop proactive integrated disease prevention marketing campaigns to address social media efects and the associated infodemic. Our study emphasises the importance of efectively employing IS to improve the accuracy of information shared via social media and positively influence individuals’ disease prevention behaviour.

## Acknowledgments

Kyunghwa Hwang and Yujung Cho, master’s students, helped us prepare for data analysis by inputting codes into the software under supervision. We greatly appreciate their assistance.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

This work was supported by the Ministry of Education of the Republic of Korea and the National Research Foundation of Korea [NRF-2020S1A3A2A02093277].

## ORCID

Eunyoung (Christine) Sung http://orcid.org/0000-0003- 1903-8538

## References

Abraham,C., & Sheeran,P.2005. The health belief model. Predicting Health Behaviour, 2, 28–80. https://edc.iums. ac.ir/files/hshe-soh/files/predicting\_Health\_beh\_avior. pdf#page=45

Ågerfalk, P. J., Conboy, K., & Myers, M. D. (2020). Information systems in the age of pandemics COVID-19 and beyond. European Journal of Information Systems, 29(3), 203–207. https://doi.org/10. 1080/0960085X.2020.1771968

Ali, I. (2020). The COVID-19 pandemic: Making sense of rumor and fear: Op-ed. Medical Anthropology, 39(5), 1–4. https://doi.org/10.1080/01459740.2020.1745481

Allam, H., Bliemel, M., Spiteri, L., Blustein, J., & Ali-Hassan, H. (2019). Applying a multi-dimensional hedonic concept of intrinsic motivation on social tagging tools: A theoretical model and empirical validation. International Journal of Information Management, 45, 211–222. https://doi.org/10.1016/j.ijinfomgt.2018.11.005

Anderson, R. M., & May, R. M. (1992). Infectious diseases of humans: Dynamics and control. Oxford University Press.

Assiri, A., Al-Tawfiq, J. A., Al-Rabeeah, A. A., Al-Rabiah, F. A., Al-Hajjar, S., Al-Barrak, A., Flemban, H., Al-Nassir, W. N., Balkhy, H. H., Al-Hakeem, R. F., Makhdoom, H. Q., Zumla A. I., & Memish, Z. A. (2013). Epidemiological, demographic, and clinical characteristics of 47 cases of Middle East Respiratory Syndrome coronavirus disease from Saudi Arabia: A descriptive study. The Lancet Infectious Diseases, 13(9), 752–761. https://www.science direct.com/science/article/pii/S1473309913702044?via% 3Dihub

Bandura, A. (1978). Social learning theory of aggression. Journal of Communication, 28(3), 12–29. https://doi.org 10.1111/j.1460-2466.1978.tb01621.x

Bell, W. G. (1924). The Great Plague in London in 1665. John Lane.

Blackwell, C. W. (2009). Requests for safer sex among men who have sex with men who use the internet to initiate sexual relationships: Implications for healthcare providers. Journal of LGBT Health Research, 5(1–2), 4–9. https://doi.org/10.1080/15574090903327943

Boberg, S., Quandt, T., Schatto-Eckrodt, T., & Frischlich, L. (2020). Pandemic populism: Facebook pages of alternative news media and the Corona crisis—a computational content analysis. arXiv Preprint arXiv, 2004, 02566. https://arxiv.org/abs/2004.02566

Bumgarner, B. A. (2007). You have been poked: Exploring the uses and gratifications of Facebook among emerging adults. First Monday, 12, 11. https://firstmonday.org/arti cle/view/2026/1897

Cai, D., Liu, J., Zhao, H., & Li, M. (2020). Could social media help in newcomers’ socialization? The moderating efect of newcomers’ utilitarian motivation. Computers in Human Behavior, 107, 106273. https://doi.org/10.1016/j. chb.2020.106273

Cappé, O., Godsill, S. J., & Moulines, E. (2007). An overview of existing methods and recent advances in sequential Monte Carlo. Proceedings of the IEEE, 95(5), 899–924. https://doi.org/10.1109/JPROC.2007.893250

Cauchemez, S., & Ferguson, N. M. (2008). Likelihood-based estimation of continuous-time epidemic models from time-series data: Application to measles transmission in London. Journal of the Royal Society Interface, 5(25), 885–897. https://doi.org/10.1098/rsif.2007.1292

Chew, C., & Eysenbach, G. (2010). Pandemics in the age of Twitter: Content analysis of Tweets during the 2009

H1N1 outbreak. PloS One, 5(11), e14118. https://doi. org/10.1371/journal.pone.0014118

Chilvers, R., Gratton, S., & Bernard, S. H. (2013). Satisfaction with a child and adolescent mental health services (CAMHS) intellectual disability service. Advances in Mental Health and Intellectual Disabilities, 7(1), 49–58. https://doi.org/10.1108/20441281311294701

Chou, W. Y. S., Hunt, Y. M., Beckjord, E. B., Moser, R. P., & Hesse, B. W. (2009). Social media use in the United States: Implications for health communication. Journal of Medical Internet Research, 11(4), e48. https://doi.org/ 10.2196/jmir.1249

Cook, T. M., & Day, C. J. (1998). Hospital mortality after urgent and emergency laparotomy in patients aged 65 yr and over. Risk and prediction of risk using multiple logistic regression analysis. British Journal of Anaesthesia, 80 (6), 776–781. https://doi.org/10.1093/bja/80.6.776

Coursaris, C. K., Yun, Y., & Sung, J. (2010, June). Twitter users vs. quitters: A Uses and Gratifications and Difusion of Innovations approach in understanding the role of mobility in microblogging. In 2010 Ninth International Conference on Mobile Business and 2010 Ninth Global Mobility Roundtable (ICMB-GMR), Athens, Greece (pp. 481–486). IEEE.

D’Alessandro, A. M., Peltier, J. W., & Dahl, A. J. (2012). The impact of social, cognitive and attitudinal dimensions on college students’ support for organ donation. American Journal of Transplantation, 12(1), 152–161. https://doi. org/10.1111/j.1600-6143.2011.03783.x

Demircioglu, M. A., & Chen, C. A. (2019). Public employees’ use of social media: Its impact on need satisfaction and intrinsic work motivation. Government Information Quarterly, 36(1), 51–60. https://doi.org/10.1016/j.giq. 2018.11.008

Dowdell, E. B., Burgess, A. W., & Flores, J. R. (2011). Online social networking patterns among adolescents, young adults, and sexual ofenders. American Journal of Nursing, 111(7), 28–36. https://doi.org/10.1097/01.NAJ. 0000399310.83160.73

Egan, K. G., & Moreno, M. A. (2011). Prevalence of stress references on college freshmen Facebook profiles. Computers, Informatics, Nursing, 29(10), 586–592. https://doi.org/10.1097/NCN.0b013e3182160663 .

Fauci, A. S., Lane, H. C., & Redfield, R. R. (2020). Covid-19 —navigating the uncharted. New England Journal of Medicine, 382, 1268–1269. https://doi.org/10.1056/ NEJMe2002387

Feldacker, C., Torrone, E., Triplette, M., Smith, J. C., & Leone, P. A. (2011). Reaching and retaining high-risk HIV/AIDS clients through the Internet. Health Promotion Practice, 12(4), 522–528. https://doi.org/10. 1177/1524839909349178

Freeman, B., & Chapman, S. (2010). British American tobacco on Facebook: Undermining Article 13 of the global World Health Organization framework convention on tobacco control. Tobacco Control, 19(3), e1–e9. https://doi.org/10.1136/tc.2009.032847

Graham, M. H. (2003). Confronting multicollinearity in ecological multiple regression. Ecology, 84(11), 2809–2815. https://doi.org/10.1890/02-3114

Grifiths, R., & Casswell, S. (2010). Intoxigenic digital spaces? Youth, social networking sites and alcohol marketing. Drug and Alcohol Review, 29(5), 525–530. https://doi.org/10.1111/j.1465-3362.2010.00178.x

Grissom, R. J., & Kim, J. J. (2005). Efect sizes for research: A broad practical approach. Lawrence Erlbaum Associates Publishers.

Han, X., Wang, J., Zhang, M., & Wang, X. (2020). Using social media to mine and analyze public opinion related to COVID-19 in China. International Journal of Environmental Research and Public Health, 17(8), 2788. https://doi.org/10.3390/ijerph17082788

Harville, D. A., & Jeske, D. R. (1992). Mean squared error of estimation or prediction under a general linear model. Journal of the American Statistical Association, 87(419), 724–731. https://doi.org/10.1080/01621459.1992. 10475274

He, S., Peng, Y., & Sun, K. (2020). SEIR modeling of the COVID-19 and its dynamics. Nonlinear Dynamics, 101, 1667–1680. https://doi.org/10.1007/s11071-020-05743-y

Hou, C., Chen, J., Zhou, Y., Hua, L., Yuan, J., He, S., . . . Zhang, J. (2020). The efectiveness of quarantine of Wuhan city against the Corona Virus Disease 2019 (COVID-19): A well-mixed SEIR model analysis. Journal of Medical Virology, 92, 841–848. https://doi. org/10.1002/jmv.25827

Huang, C. M., Chan, E., & Hyder, A. A. (2010). Web 2.0 and Internet social networking: A new tool for disaster management? Lessons from Taiwan. BMC Medical Informatics and Decision Making, 10(1), 57. https://doi. org/10.1186/1472-6947-10-57

Janz, N. K., & Becker, M. H. (1984). The health belief model: A decade later. Health Education Quarterly, 11(1), 1–47. https://doi.org/10.1177/109019818401100101

Jenssen, B. P., Klein, J. D., Salazar, L. F., Daluga, N. A., & DiClemente, R. J. (2009). Exposure to tobacco on the internet: Content analysis of adolescents’ internet use. Pediatrics, 124(2), e180–e186. https://doi.org/10.1542 peds.2008-3838 .

Jo, W., Lee, J., Park, J., & Kim, Y. (2020). Online information exchange and anxiety spread in the early stage of the novel coronavirus (COVID-19) outbreak in South Korea: Structural topic model and network analysis. Journal of Medical Internet Research, 22(6), e19455. https://doi.org/10.2196/19455

Johnson, P. R., & Yang, S. (2009, August). Uses and gratifi cations of Twitter: An examination of user motivations and satisfaction of Twitter use [Paper presentation]. Annual Convention of the Association for Education in Journalism and Mass Communication.

Joinson, A. N. (2008, April). Looking at, looking up or keeping up with people? Motivations and use of Facebook. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Florence, Italy. (pp. 1027–1036).

Katz, E., Blumler, J., & Gurevitch, M. (1974). Uses and gratification theory. Public Opinion Quarterly, 37(4), 509–523. https://doi.org/10.1086/268109

Kermack, W. O., & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics. Proceedings of the Royal Society of London: Series A, 115 (772), 700–721. https://doi.org/10.1098/rspa.1927.0118

Khosropour, C. M., & Sullivan, P. S. (2011). Predictors of retention in an online follow-up study of men who have sex with men. Journal of Medical Internet Research, 13(3), e47. https://doi.org/http://dx.doi.org/10.2196/jmir.1717

Knoll, J., Matthes, J., & Heiss, R. (2020). The social media political participation model: A goal systems theory perspective. Convergence, 26(1), 135–156. https://doi. org/10.1177/1354856517750366

Kroese, D. P., Brereton, T., Taimre, T., & Botev, Z. I. (2014). Why the Monte Carlo method is so important today. WIREs Computational Statistics, 6(6), 386–392. https:/ doi.org/doi:10.1002/wics.1314 .

Kuhn, A. (2020). How a South Korean city is changing tactics to tamp down its COVID-19 surge. NPR. March 10.

Lamb, A., Paul, M., & Dredze, M. (2013, June). Separating fact from fear: Tracking flu infections on Twitter. In Proceedings of the 2013 Conference of the North American Chapter of the Association for Computationa Linguistics: Human Language Technologies (pp. 789–795).

Lee, J. H., Murshed, S., & Park, J. S. (2009). Estimation of infection distribution and prevalence number of Tsutsugamushi fever in Korea. Journal of the Korean Data and Information Science Society, 20(1), 149–158. https:// www.koreascience.or.kr/article/JAKO200908349655373. page

Leighton, J. W., Valverde, K., & Bernhardt, B. A. (2012). The general public’s understanding and perception of directto-consumer genetic test results. Public Health Genomics, 15(1), 11–21. https://doi.org/http://dx.doi.org/10.1159% 2F000327159

Li, M. Y., Graef, J. R., Wang, L., & Karsai, J. (1999). Global dynamics of a SEIR model with varying total population size. Mathematical Biosciences, 160(2), 191–213. https:// doi.org/10.1016/S0025-5564(99)00030-9

Li, S., Wang, Y., Xue, J., Zhao, N., & Zhu, T. (2020). The impact of COVID-19 epidemic declaration on psychological consequences: A study on active Weibo users. International Journal of Environmental Research and Public Health, 17(6), 2032. https://doi.org/10.3390/ ijerph17062032

Lloyd, A. L. (2001). Realistic distributions of infectious periods in epidemic models: Changing patterns of persistence and dynamics. Theoretical Population Biology, 60 (1), 59–71. https://doi.org/10.1006/tpbi.2001.1525

Ma, R., Deng, Z., & Wu, M. (2020). Efects of health information dissemination on user follows and likes during COVID-19 outbreak in China: Data and content analysis. International Journal of Environmental Research and Public Health, 17(14), 5081. https://doi.org/10.3390/ ijerph17145081

Mendling, J., Pentland, B., & Recker, J. (2020). Building a complementary agenda for business process management and digital innovation. European Journal of Information Systems, 29(3), 208–219. https://doi.org/10. 1080/0960085X.2020.1755207

Mitchell, K. J., Finkelhor, D., Jones, L. M., & Wolak, J. (2010). Use of social networking sites in online sex crimes against minors: An examination of national incidence and means of utilization. Journal of Adolescent Health, 47(2), 183–190. https://doi.org/10.1016/j.jadohealth. 2010.01.007

Mooney, C. Z. (1997). Monte Carlo simulation. Sage Publications.

Moreno, M. A., Jelenchick, L. A., Egan, K. G., Cox, E., Young, H., Gannon, K. E., & Becker, T. (2011). Feeling bad on Facebook: Depression disclosures by college students on a social networking site. Depression and Anxiety, 28(6), 447–455. https://doi.org/10.1002/da.20805

Nabity-Grover, T., Cheung, C. M., & Thatcher, J. B. (2020). Inside out and outside in: How the COVID-19 pandemic afects self-disclosure on social media. International Journal of Information Management, 55, 102188. https:// doi.org/10.1016/j.ijinfomgt.2020.102188

Norman, C. D., & Yip, A. L. (2012). eHealth promotion and social innovation with youth: Using social and visual media to engage diverse communities. Studies in Health Technology and Informatics, 172, 54–70. https://eur opepmc.org/article/med/22910502

Oh, H. J., & Lee, B. (2012). The efect of computer-mediated social support in online communities on patient empowerment and doctor–patient communication. Health Communication, 27(1), 30–41. https://doi.org/10.1080 10410236.2011.567449

Park, S. Y., Cha, S. B., Lim, K., & Jung, S. H. (2014). The relationship between university student learning outcomes and participation in social network services, social acceptance and attitude towards school life. British Journal of Educational Technology, 45(1), 97–111. https://doi.org/10.1111/bjet.12013

Peters, A., Tartari, E., Lotfinejad, N., Parneix, P., & Pittet, D. (2018). Fighting the good fight: The fallout of fake news in infection prevention and why context matters. Journal of Hospital Infection, 100(4), 365–370. https://doi.org/10. 1016/j.jhin.2018.08.001

Ramo, D. E., & Prochaska, J. J. (2012). Broad reach and targeted recruitment using Facebook for an online survey of young adult substance use. Journal of Medical Internet Research, 14(1), e28. https://doi.org/http://dx.doi.org/10. 2196/jmir.1878

Rice, E., Tulbert, E., Cederbaum, J., Barman Adhikari, A., & Milburn, N. G. (2012). Mobilizing homeless youth for HIV prevention: A social network analysis of the acceptability of a face-to-face and online social networking intervention. Health Education Research, 27(2), 226–236. https://doi.org/10.1093/her/cyr113

Robertson, L., Skegg, K., Poore, M., Williams, S., & Taylor, B. (2012). An adolescent suicide cluster and the possible role of electronic communication technology. Crisis, 33(4), 239–245. https://doi.org/10.1027/0227-5910/a000140

Ross, R. (1911). Some quantitative studies in epidemiology. Nature, 87, 466–467. https://doi.org/10.1038/087466a0

Rosselli, R., Onesti, A., Martini, M., Cartiglia, C., Sticchi, L., & Alberti, M. (2011). In the healthcare setting. Journal of Preventive Medicine and Hygiene, 52(2), 59–63. https:/ doi.org/10.15167/2421-4248/jpmh2011.52.2.251

Scanfeld, D., Scanfeld, V., & Larson, E. L. (2010). Dissemination of health information through social networks: Twitter and antibiotics. American Journal of Infection Control, 38(3), 182–188. https://doi.org/10. 1016/j.ajic.2009.11.004

Shiina, A., Niitsu, T., Kobori, O., Idemoto, K., Hashimoto, T., Sasaki, T., Igarashi, Y., Shimizu, E., Nakazato, M., Hashimoto, K., & Iyo, M. (2020). Relationship between perception and anxiety about COVID-19 infection and risk behaviors for spreading infection: A national survey in Japan. Brain, Behavior, & Immunity-Health, 6, 100101. https://doi.org/10.1016/j.bbih.2020.100101

Silenzio, V. M., Duberstein, P. R., Tang, W., Lu, N., Tu, X., & Homan, C. M. (2009). Connecting the invisible dots: Reaching lesbian, gay, and bisexual adolescents and young adults at risk for suicide through online social networks. Social Science & Medicine, 69(3), 469–474. https://doi.org/10.1016/j.socscimed.2009.05.029

Stephenson, R., Khosropour, C., & Sullivan, P. (2010). Reporting of intimate partner violence among men who have sex with men in an online survey. Western Journal of Emergency Medicine, 11(3), 242–246. https://www.ncbi. nlm.nih.gov/pmc/articles/PMC2941360

Sullivan, P. S., Khosropour, C. M., Luisi, N., Amsden, M., Coggia, T., Wingood, G. M., & DiClemente, R. J. (2011).

Bias in online recruitment and retention of racial and ethnic minority men who have sex with men. Journal of Medical Internet Research, 13(2), e38. https://doi.org/ http://dx.doi.org/10.2196/jmir.1797

Thackeray, R., Neiger, B. L., Smith, A. K., & Van Wagenen, S. B. (2012). Adoption and use of socia media among public health departments. BMC Public Health, 12(1), 242. https://doi.org/10.1186/1471-2458- 12-242

Topliss, J. G., & Costello, R. J. (1972). Chance correlations in structure-activity studies using multiple regression analysis. Journal of Medicinal Chemistry, 15(10), 1066–1068. https://pubs.acs.org/doi/pdf/10.1021/ jm00280a017

Wallinga, J., & Lipsitch, M. (2007). How generation intervals shape the relationship between growth rates and reproductive numbers. Proceedings of the Royal Society B: Biological Sciences, 274(1609), 599–604. https://doi. org/10.1098/rspb.2006.3754

Wang, T., Lu, K., Chow, K. P., & Zhu, Q. (2020). COVID-19 sensing: Negative sentiment analysis on social media in China via BERT Model. IEEE Access, 8, 138162–138169. https://doi.org/10.1109/ACCESS.2020.3012595

Weitzman, E. R., Adida, B., Kelemen, S., & Mandl, K. D. (2011). Sharing data for public health research by members of an international online diabetes social network. PloS One, 6(4), 1–8. https://doi.org/10.1371/journal.pone. 0019256

Yang, Z., Zeng, Z., Wang, K., Wong, S. S., Liang, W., Zanin, M., . . . Liang, J. (2020). Modified SEIR and AI prediction of the epidemics trend of COVID-19 in China under public health interventions. Journal of Thoracic Disease, 12(3), 165–174. https://doi.org/10.21037/jtd. 2020.02.64

Ybarra, M. L., & Mitchell, K. J. (2008). How risky are social networking sites? A comparison of places online where youth sexual solicitation and harassment occurs. Pediatrics, 121(2), e350–e357. https://doi.org/10.1542/ peds.2007-0693

Young, S. D., & Rice, E. (2011). Online social networking technologies, HIV knowledge, and sexual risk and testing behaviors among homeless youth. AIDS and Behavior, 15 (2), 253–260. https://doi.org/10.1007/s10461-010-9810-0

Zhai, J. (2020). Facial mask: A necessity to beat COVID-19. Building and Environment, 175, 106827. https://doi.org/ 10.1016/j.buildenv.2020.106827

Zhang, J., & Ma, Z. (2003). Global dynamics of an SEIR epidemic model with saturating contact rate. Mathematical Biosciences, 185(1), 15–32. https://doi.org/ 10.1016/S0025-5564(03)00087-7

Zhang, K., Liang, X., Ni, J., Yang, K., & Shen, X. S. (2016). Exploiting social network to enhance human-to-human infection analysis without privacy leakage. IEEE Transactions on Dependable and Secure Computing, 15 (4), 607–620. https://doi.org/10.1109/TDSC.2016. 2626288

Zhao, C., Zhang, Z., Li, H., & Zhao, S. (2014). A social network information propagation model considering different types of social relationships. In J.-S. Pan, P. Krömer, & V. Snášel (Eds.), Genetic and Evolutionary Computing (pp. 275–282). Springer. https://doi.org/10. 1007/978-3-319-01796-9\_29
