---
otero_id: 5664
otero_key: "BNQRV3JD"
title: "A multi-level influence model of COVID-19 themed cybercrime"
authors: "Rennie Naidoo"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1771222"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multi-level influence model of COVID-19 themed cybercrime

Rennie Naidoo

To cite this article: Rennie Naidoo (2020): A multi-level influence model of COVID-19 themed cybercrime, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1771222 To link to this article: https://doi.org/10.1080/0960085X.2020.1771222

![](/api/attachments/BNQRV3JD/fulltext/images/aedca5c0f52e12e517ac87a7bdbe9475458fbb05f39681ac9693c464e693b5fa.jpg)

Published online: 31 May 2020.

![](/api/attachments/BNQRV3JD/fulltext/images/c2c5e7bd72ccf1cc34c403b4ceaba05811aba5133328ce7b2118722a535de0ac.jpg)

Submit your article to this journal

![](/api/attachments/BNQRV3JD/fulltext/images/fb3ae8d43376bddf140301da8b050ac9d139b56c8262e90dacd33b5a0aa64df3.jpg)

Article views: 353

![](/api/attachments/BNQRV3JD/fulltext/images/2f6d4ca4be8d2f03be82c688c0d9e9e6607e92803c1419d11463b075ece76a60.jpg)

View related articles

![](/api/attachments/BNQRV3JD/fulltext/images/172404696b1e835adafb825bbea034f8c826521a58e9cf22e073a61918031f4d.jpg)

View Crossmark data

Check for updates

# A multi-level influence model of COVID-19 themed cybercrime

Rennie Naidoo

Department of Informatics, University of Pretoria, Pretoria, South Africa

## ABSTRACT

The recent severity and frequency of cybercrime has been dominated by a single theme – the COVID-19 pandemic. This research develops a multi-level in<sup>fl</sup>uence model to explore how cybercriminals are exploiting the COVID-19 pandemic by assessing situational factors, identifying victims, impersonating trusted sources, selecting attack methods, and employing social engineering techniques. The model extends upon prior work on in<sup>fl</sup>uence techniques and emotional appeals that cybercriminals employ, by bringing into sharper focus the role of situational factors in COVID-19 related cybercrime attacks. Content and thematic analysis was conducted on 185 distinct COVID-19 cybercrime scam incident documents, including text, images, and photos, provided by a global online fraud and cybersecurity company tracking COVID-19 related cybercrime. The analysis reveals interesting patterns about the sheer breadth and diversity of COVID-19 related cybercrime and how these crimes are continually evolving in response to changing situational factors. It is hoped that these insights and recommendations for end-users and organisations can contribute to a safer digital world as we cope with many other pressing challenges during the COVID-19 pandemic.

ARTICLE HISTORY

Received 3 May 2020

Accepted 15 May 2020

KEYWORDS

COVID-19; cybersecurity;

cybercrime; social

engineering; infodemic;

pandemic

## 1. Introduction

An ‘Unprecedented’ Wave Of Coronavirus Scams Is Coming.

FBI sees spike in cyber crime reports during coronavirus pandemic.<sup>2</sup>

COVID-19-related phishing attacks up by 667%.<sup>3</sup>

## [Recent headlines from Online Media]

As borne out by the headlines cited above, the COVID-19 pandemic has become the dominant theme in the recent upsurge of cybercrime. The critical dependency on virtual environments by organisations and individuals during the COVID-19 pandemic is being exploited by cybercriminals. During the pandemic, computer systems and virtual environments are providing essential communication services, such as local and international news updates, telework, online education, social connectivity, and entertainment. The convergence of digital technology and computing and communication devices has radically transformed the way in which people are socialising and doing business during the pandemic. For many of those individuals practicing social and physical distancing during the lockdown period, there has been a sharp rise in the use of social technologies to maintain and develop deep emotional and social ties. Many individuals are getting their reassurances and comfort from social media, video communications and email contact. For example, research in the US shows a 17% increase in Internet use (Muncaster, 2020). The same study found that online visits to tutoring sites grew by 400% in just four weeks, while categories such as politics (320%), TV (210%) and gardening (200%) also saw sharp increases.

Telework software has become a vital technology for organisations to enable employees to continue to work remotely. A number of organisations had to suddenly adopt a teleworking model, thus the priority was to get users ready as expediently as possible, consequently delivering inadequate security safeguards for remote employees. Many users are now working outside the normal security protections provided by their employers’ internal computer systems. For example, a number of employee home networks may contain insecure IoT devices and outdated PCs, and for many organisations, the crucial issue of educating employees about remote work safety has been lacking.

Notwithstanding the COVID-19 pandemic, cybercrime remains one of the greatest threats facing society. At the 2015 IBM Security Summit, Ginni Rometty, IBM’s chairman, president and CEO, stated that cybercrime is “the greatest threat to every profession, every industry, every company in the world” (Morgan, 2017). At an annual shareholders meeting in 2017, legendary businessman Warren Bu<sup>f</sup>et, described cybercrime as “the number one problem with mankind” (Morgan, 2017). While these views may sound like overstatements, it nevertheless conveys a sense of urgency that is required to improve cybersecurity across the globe. As expected, the catastrophic impact of cybercrime on society is also re<sup>fl</sup>ected in the hard facts. In 2019, the World Economic Forum (WEF) ranked cybercrime among the top 5 risks facing the globe (World Economic Forum, 2019). Accenture estimates the total value at risk from cybercrime globally to be around USD 5.2 trillion over a <sup>fi</sup>ve year period, from 2019 to 2023 (Accenture, 2019). A more recent study by Cybersecurity Ventures predicts that cybercrime’s global cost of damages will reach 6 USD trillion annually by 2021(Morgan, 2019).

Despite the terrible human su<sup>f</sup>ering caused by the coronavirus, cybercrimes are escalating dramatically. More alarming is the high volumes of COVID-19 themed scams that are exploiting the increasing reliance on electronic communication networks and information systems. In addition to 18 million daily malware and phishing emails related to COVID-19 in just one week in April, Google’s blog reported more than 240 million COVID-related spam messages daily. Phishing and hacking attacks and threats have increased by 5 to 6 times their usual numbers in the month of March (Kumaran & Lugani, 2020). By the end of March, more than 42,000 websites with domains containing “COVID” and “corona” had been registered – the majority of these appear to be suspicious (Kumaran & Lugani, 2020). Researchers also observed a substantial spike of 667% in COVID-19 phishing messages recently (Shi, 2020). Between March 1 and March 23, over 9000 email attacks were related to COVID-19 compared to 1,188 in February, and just 137 in January (Shi, 2020). In April, the FBI’s Internet Crime Complain Centre (IC3) received between 3,000 and 4,000 cybersecurity complaints daily compared to an average 1,000 daily complaints before COVID-19 (Cimpanu, 2020). Not surprisingly, Web credit card skimming increased by 26 percent in March due to the recent growth in online shopping (Segura, 2020).

The COVID-19 pandemic has exposed technological and end-user vulnerabilities that cybercriminals are seeking to exploit. Cybercriminals are exploiting telework vulnerabilities, as more employees grapple with communicating and sharing information over the Internet. Cybercriminals are also exploiting our substantial reliance on technologies for socially connecting by taking advantage of the widespread discussion of COVID-19 in emails and across the web. Cybercriminals are also preying on the emotional vulnerability of people brought about by the uncertainty and di<sup>fi</sup>culties during this pandemic. It is estimated that more than 80% of exploits are successful because of social engineering techniques employed by cybercriminals (Brum<sup>fi</sup>eld, 2020). Experts agree that endusers remain the “weakest link” in cybersecurity. This study focuses on how cybercriminals set about targeting end-users. However, no understanding of cybercrime can be complete without a sense of the context. The pandemic provides an ideal opportunity to get a glimpse into how context can in<sup>fl</sup>uence cybercrime.

Several IS studies have improved our understanding of cybercrime through investigating the individual characteristics of victims and the characteristics of the cybercrime (Chen et al., 2011; Sheng et al., 2010; Wang et al., 2009; RT Wright et al., 2014; Wright & Marett, 2010). However, a more holistic and integrated approach to cybercrime research that seeks to understand cybercrime from the cybercriminal’s perspective is also required (Holt & Bossler, 2008; Yar, 2005). This study seeks to further develop this body of knowledge by developing a multi-level model of cybercrime that simultaneously explores key situational factors, targets, attack methods, and social engineering techniques. The model can also be used by cybersecurity experts to assess the key situational factors, vulnerabilities, and attack targets that could emerge. The model also enables cybersecurity experts to identify and mitigate some of the novel cyber risks facing their organisations and pre-empt targeted attacks during COVID-19, and perhaps any other future crisis impacting business continuity.

This research relied on secondary data supplied by a reputable global online fraud and cybersecurity services company that is collecting COVID-19 themed cybercrime data from around the globe. Data was subjected to deductive and inductive coding and theme development. This was supplemented with visual thematic analysis for scam documents that contained photos and images. The results of the study demonstrate that COVID-19 cybercrimes are consistently shifting in breadth, diversity, and method of attack by aligning to situational changes during the COVID-19 pandemic. COVID-19 attacks are seeking to increase the susceptibility of end-user targets to social engineering techniques by selecting COVID-19 relevant impersonation targets and cyber technologies. The study also <sup>fi</sup>nds that COVID-19 cybercrimes are <sup>fl</sup>exible and evolving, and tapping into a much broader range of social in<sup>fl</sup>uence techniques and emotional appeals than those documented in previous cybercrime studies. It o<sup>f</sup>ers practical guidelines for improving cybersecurity during the pandemic that is perhaps also applicable in a post-pandemic future.

## 2. Literature review

Gordon and Ford (2006) de<sup>fi</sup>ne cybercrime as “any crime that is facilitated or committed using a computer, network, or hardware device” (p. 14). Like many other de<sup>fi</sup>nitions of cybercrime, emphasis is placed on any criminal activity targeting organisations or end-users that is conducted through the IT infrastructure via internal or external networks, or the Internet (Ciardhuáin,

2004; Yue et al., 2019). Cybercrime examples include but are not limited to phishing, spam, data breaches, data/ information theft, identity theft, fraud, cyberstalking, cyberbullying and harassment, child predation, extortion, blackmail, stock market manipulation, espionage, attacks on critical infrastructure and information systems, and cyberterrorism (Maimon & Louderback, 2019). Crimeware refers to software tools that are used to commit cybercrimes. These can include but are not limited trojans, viruses, bots (e.g., FriendBot), keyloggers, backdoors, e-skimming, spyware, ransomware, scareware, adware, worms, malicious code, and denial-ofservice (Gordon & Ford, 2006). Crimeware excludes legitimate programs which may also be exploited by a cybercriminal (Gordon & Ford, 2006). For example, although targeted applications, such as email and Web browsers are part of the crime, they are not crimeware. Apart from using crimeware, cybercriminals also exploit news stories, hyperlinks, photos, videos, and applications. Cybercrime targets are both technological and nontechnological – exploiting vulnerabilities in endusers and IT.

While cybercrimes can lead to physical attacks, this study is concerned with cyber attacks. The literature suggests it is easier for cybercriminals to “crack the human <sup>fi</sup>rewall” versus technical vulnerabilities – i.e. it is easier to exploit human vulnerabilities (Algarni et al., 2014; Jensen et al., 2017; Luo et al., 2011; Mitnick & Simon, 2003; P<sup>fl</sup>eeger et al., 2014). Furthermore, while some cybercrime is mostly technological in nature, our focus here is on cybercrime that also has a large human component (Gordon & Ford, 2006). For example, while phishing relies on email technologies, websites, and crimeware to steal personal, <sup>fi</sup>nancial or any other sensitive information, it also entails the use of social engineering techniques to trick the recipient into providing information (Jagatic et al., 2007; Mitnick & Simon, 2003; R Wright et al., 2010).

Social engineering techniques refer to the deceptive use of social in<sup>fl</sup>uence techniques and emotional appeals by cybercriminals to manipulate end-users into compliance so that they divulge con<sup>fi</sup>dential or personal information that may be used for the commission of cybercrime (Algarni et al., 2014; Krombholz et al., 2015). Social engineering techniques share similarities with “con<sup>fi</sup>dence games” (or “cons”) run by con operators (“con men”) who lure their victims (the “marks”) into compliance by gaining their trust and disarming them (Orbach, 2018). According to Petty and Cacioppo (1986), people will either think systematically (elaborate) about an issue or take cognitive shortcuts (heuristics) to make a decision. The goal of social engineering techniques is to alter the cognitive and emotional conditions of the victim so that instead of operating mindfully victims will tend to rely on heuristics to make a judgement (Cialdini & Goldstein, 2004; Ferreira et al., 2015) . Relying on heuristics is an e<sup>fi</sup>cient approach to forming judgements in everyday life (Gigerenzer & Todd, 1999), but is vulnerable to the exploits of cybercriminals (Luo et al., 2013). Social engineering techniques aim to arrest elaborate thought long enough to trick the victim (Cialdini & Goldstein, 2004; Jagatic et al., 2007; Mitnick & Simon, 2003).

Cybercriminals assume a false identity to manipulate end-users into providing sensitive information or performing tasks (Abbasi et al., 2010; Bose & Leung, 2007; Jensen et al., 2017). Cybercriminals often impersonate sources that have expertise, authority, competence, and integrity to gain the trust of their victim and make them feel safe (Algarni et al., 2014, 2017). Impersonation is a type of identity crime and identity fraud which is facilitated by the use of false identities (Clough, 2010). Since impersonation is not di<sup>fi</sup>cult to achieve in cyberspace, many cybercriminals exploit the ease of anonymity by targeting and mimicking credible sources. Cybercriminals can impersonate friends on social media, product brands, and technology brands (Westerman et al., 2014). For example, cybercriminals committing phishing attacks mimic email messages from legitimate sources and create mock-ups of trusted websites (Abbasi et al., 2010). According to source credibility theory, the end-user’s perceived credibility or the believability of the person or organisation being impersonated is more likely to lead to compliance (Bhattacherjee & Sanford, 2006; Boss et al., 2015; Hovland & Weiss, 1951).

Apart from impersonation, there are various other in<sup>fl</sup>uence techniques that cybercriminals can exploit to persuade a target into divulging sensitive information (R Wright et al., 2010). The cybersecurity literature has relied on Cialdini’s six persuasion principles to analyse the techniques that cybercriminals employ in their scams (Ferreira et al., 2015; Krombholz et al., 2015). According to Cialdini’s social in<sup>fl</sup>uence model that is drawn from the psychology of compliance literature, these six principles include: authority, consistency, liking, scarcity, reciprocity, and social proof (Cialdini, 2001). Authority refers to the tendency in people to unthinkingly accept the statements and directions of individuals and organisations who appear to be authorities on a subject (Milgram, 1974; Zimbardo, 2008). They apply the heuristic rule: “If an expert says so, it must be true” (Cialdini, 2001). Instead of being persuaded by the quality of an expert’s arguments (Sussman & Siegal, 2003), people tend to be persuaded solely by the expert’s status (Cialdini, 2001). This technique invokes the peripheral (heuristic) and not the central routes (systemic) to persuasion (Petty & Cacioppo, 1986).

Cybercriminals also take advantage of people’s tendency to perform automatically in line with their commitments. The victim’s strong need to be consistent with their commitment can be exploited for the cybercriminal’s bene<sup>fi</sup>t (Akbar, 2014; Ferreira et al., 2015). According to the scarcity principle, something can appear more valuable when there is limited availability. Cybercriminals take advantage of this principle by claiming on their website that a fake product is in short supply or is quickly running out. Reciprocation is another technique that cybercriminals employ in their scams for gaining the enduser’s compliance (Ferreira et al., 2015; Stajano & Wilson, 2011). For example, cybercriminals take advantage of people’s generosity or strong sense of obligation to return a favour in online donation scams. Liking and friendship pressures are also employed by cybercriminals to get their victims to comply (Ferreira et al., 2015). For example, cybercriminals exploit the tendency that people are more willing to perform favours for their friends on social networking sites (SNSs). Social proof refers to people’s tendency to view a particular behaviour as being correct if people similar to them are performing the same behaviour (Stajano & Wilson, 2011). Cybercriminals can induce the similarity principle by providing false evidence of broad support.

The role of emotional factors has been downplayed in understanding cybercrime victimisation. Emotions generally play an important role in compliance behaviour (Boss et al., 2015; Richins, 1997). Cybercriminals who are able to manipulate the emotional state of their victims have a better chance of manipulating endusers into compliance (Mitnick & Simon, 2003). In invoking the scarcity principle mentioned above, the cybercriminal often resorts to emotional appeals by appearing to reward the end-user for prompt action or penalise them for delayed action. For example, the cybercriminal impersonating a bank may use penalties as a scare tactic. This is likely to lead to an intense feeling and therefore induce users to react quickly out of fear, to avoid a bad credit record or the inconvenience of having their account placed on hold. Emotional appeals are not limited to negative a<sup>f</sup>ective states such as anger, fear or threat (Boss et al., 2015), cybercriminals can also exploit positive a<sup>f</sup>ective states, such as pride, relief and enjoyment (Agarwal & Karahanna, 2000; Richins, 1997). The role of emotional appeals is to distract the victim thus preventing them from analysing the content of the message carefully (Workman, 2008). The Dual-Systems Model of A<sup>f</sup>ect can account for both positive and negative a<sup>f</sup>ective states (Dillard & Peck, 2006), while the Extended Parallel Process Model is used in cybercrime research to account for fear/threat appeals (Boss et al., 2015; Witte, 1992).

The role of situational factors has also been downplayed in understanding cybercrime victimisation (Cohen & Felson, 1979; Jagatic et al., 2007; Miethe et al., 1990; Yar, 2005). The dominant approach in the literature is to provide individual dispositional explanations of cybercrime victimisation (Luo et al., 2011; Wright & Marett, 2010). However, these individualistic explanations of cybercrime fail to account for the role of situational trends and patterns (Ngo & Paternoster, 2011; Ngwenyama & Lee, 1997). Some researchers predict that cybercriminals will incorporate greater elements of context into their scam designs (Jagatic et al., 2007). The Routine Activity Theory (RAT) postulates that high trends in cybercrime rates are related to the changes in the “routine activities” of everyday life (Cohen & Felson, 1979). Three theoretical constructs from routine activities theory include (1) exposure to motivated criminals, (2) target suitability, and (3) capable guardianship (Holt & Bossler, 2008; Moneva et al., 2020) . For example, during COVID-19, the theory predicts that cybercriminals will be motivated by the recent, abrupt changes to remote work and reliance on online tools (exposure) as remote workers (target suitability) are no longer operating under the same strict security provided in the workplace (capable guardianship) (Yar, 2005). Some studies on crime in general show that situational factors lead people to lower their guard and make themselves signi<sup>fi</sup>cantly more vulnerable and suitable targets for victimisation (Holt et al., 2020; Moneva et al., 2020). Table 1 summarises the interdisciplinary approach pursued in this study.

## 3. Research methodology

The study of situational factors, targets of cybercrime, attack methods, in<sup>fl</sup>uence techniques and emotional appeals employed in cybercrime during a pandemic is not easily examinable using conventional research approaches (see Figure 1). Even under normal conditions, researchers have to rely on secondary data to get a momentary peek into the cloaked world of cybercriminals and their criminal activities. Consequently, published secondary sources become a pivotal source of data for the researcher (Myers, 2009; Sørensen et al., 1996). Secondary documents and records speci<sup>fi</sup>c to COVID-19 related cybercrime were supplied by FraudWatch International. FraudWatch International is a global online fraud and cybersecurity services company that collects cybercrime data from around the globe. The author receives daily updates of FraudWatch International’s “COVID-19 Cyber Intelligence Datafeed”.

Theories and key sensitising concepts.

<table><tr><td>Theory</td><td>Area</td><td>Sensitising concepts</td></tr><tr><td>Routine Activity Theory (RAT)(Cohen &amp; Felson, 1979; Holt &amp; Bossler, 2008)</td><td>Situational Factors</td><td>Online behavioursSuitable targets for impersonation and victimisationPeople and technology vulnerabilities</td></tr><tr><td>Source Credibility Theory(Hovland &amp; Weiss, 1951; Sussman &amp; Siegal, 2003)</td><td>Source Credibility</td><td>Impersonation</td></tr><tr><td>Social Influence Model(Cialdini, 2001; Cialdini &amp; Goldstein, 2004)</td><td>Social Engineering</td><td>Social influence principles</td></tr><tr><td>Dual-Systems Model of Affect(Dillard &amp; Peck, 2006)</td><td>Social Engineering</td><td>Positive and negative emotions</td></tr></table>

![](/api/attachments/BNQRV3JD/fulltext/images/7c9c1dc35d564ac60e80a9d01b0ce850b766a8c2e2c6acdf4f042669d348f846.jpg)  
Exploratory sensitising model for cybercrimes.

The archived documents and records of COVID-19 related cybercrime between mid-March and mid-April 2020 were coded for situational factors, targets of cybercrime, attack methods, in<sup>fl</sup>uence techniques and emotional appeals using content and thematic analysis. The use of the multi-level in<sup>fl</sup>uence framework allowed the researcher to make an informed analysis of the data. The intention here was not to generalise the <sup>fi</sup>ndings to a wide range of cybercrime scam designs (Lee & Baskerville, 2003; Ruddin, 2006). Instead the goal was to perform an analytical generalisation – that is, to generalise a particular set of results to the study’s theoretical propositions about cybercriminals and cybercrime scam designs. The completeness of the dataset is recognised as a limitation of this study. Each record contains the type of scam (phishing or social network sites) and a brief description. In some cases, only phishing website information was provided and not the accompanying phishing email. The phishing email data would have been more explicit about the emotional appeals used. Furthermore, it was di<sup>fi</sup>cult to assess to what extent the phishing email and phishing website were using the consistency principle. Moreover, the archive documents were limited to active scams.

The data were analysed using Fereday & Muir-Cochrane’s (Fereday & Muir-Cochrane, 2006) guidelines for conducting a hybrid approach to deductive and inductive coding and theme development. The deductive analysis began with the development of a coding template (Crabtree & Miller, 1992). The coding template contained codes informed by the literature study (See Table 1). Major sensitising coding categories were identi<sup>fi</sup>ed. For social engineering, these included: in<sup>fl</sup>uence techniques and emotional appeals. A number of lower-level operational codes were also identi<sup>fi</sup>ed. For example, “in<sup>fl</sup>uence techniques” was broken down into six possible categories “authority”, “consistency”, “liking”, “scarcity”, “reciprocity”, and “social proof”). These tables also provide formal de<sup>fi</sup>nitions of each of the techniques.

The next step in the analysis involved testing the applicability of these codes. This was done by coding the documents and assigning the predetermined codes from the coding template. As the researcher worked through the scam texts line by line to assign the predetermined codes, inductive codes were assigned to segment data where the units of meaning could not be appropriately captured by the predetermined codes. This allowed for new insights to emerge as these codes either constituted something new, re<sup>fi</sup>ned or extended the existing codes. Gleeson’s (2011) guidelines for visual thematic analysis were adopted to analyse the scam documents that contained photos (examples: health workers, patients) and images (examples: virus) (See Figure A2). The researcher analysed the photos and images iteratively. To avoid restricting interpretations in the initial stages, the visual data were analysed independently of the coding template and textual data contained in the scams. Initially, a tentative set of visual themes that seemed to be portrayed by the images was recorded. A short descriptive note was also written for each theme that emerged. Only then were the coding template and textual data revisited to help re<sup>fi</sup>ne the initial analysis.

185 unique documents were analysed. Examples representing the di<sup>f</sup>erent ways in which these in<sup>fl</sup>uence techniques and emotional techniques were employed are also provided. Furthermore, a quantitative content analysis was performed to establish the prevalence and robustness of the study’s main themes from these documents (Table 2). Version 6.2 of ATLAS.ti – a qualitative research software tool – was used to store and analyse all the documents. The author independently coded the content and achieved consensus with an assistant researcher in case of any discrepancies. An independent judge, not familiar with project, acted as an auditor and reviewed the key categories and operational de<sup>fi</sup>nitions, and provided reasonable veri<sup>fi</sup>cation of the accuracy of the coding procedure. The judge was provided with 20 randomly chosen documents, assigning 75 out of 100 of the same categories as the author, yielding a 75% level of agreement. Triangulation was assured by comparing archived documents and records from di<sup>f</sup>erent sources to provide further con<sup>fi</sup>rmation of the themes found, and to throw more light on the contextual detail of the competing discourses (Mckenna et al., 2017). The types of cybercrime identi<sup>fi</sup>ed in our FraudWatch International dataset are not unique and the <sup>fi</sup>ndings are generally applicable to many other monitoring services across the globe. Similar scam incidents can be found in the FBI and Google’s datasets.

Several categories were observed in the documents and entered into a database. For example, in<sup>fl</sup>uence techniques and emotional appeals reported in the tables were selected on the following basis: (1) the example is unambiguous as an indicator of the category; (2) it is representative of a number of statements in the dataset; (3) it re<sup>fl</sup>ects important cybercriminal activities related to the pandemic. The most illustrative of these were included in this article. The documents and records were also categorised by key situational factors (examples: remote work, social connectivity via SNS, unemployment), by key victimisation targets (example: SNS users, remote workers), the type of cybercrimes (examples: phishing, fake products, fake social media pro<sup>fi</sup>les), the type of crimeware (examples: FriendBot, keyloggers), the online technologies targeted (examples: email, social media technologies, video telephony and online chat services, cloud <sup>fi</sup>le hosting services, and streaming media services) and the types of organisations that were the targets of impersonation (examples: banks, technology brands, product brands, and government agencies). Secondary themes were derived from primary themes. For example, the \` social network site users ‘ were inferred from the fact that major social media organisations were being targeted. Version 6.2 of ATLAS.ti and Excel was used to code and store the categories and themes. Content analysis was performed using frequency analysis to establish the prevalence and robustness of the study’s themes from the records and documents.

## 4. Analysis and results

Figure 2 shows the number of new domains that are being registered to take advantage of both the online and o<sup>fl</sup>ine media attention given to COVID-19. Registrations of COVID-19 related sites, from March 28 to April 20, averaged approximately 1900 - per day. During this same period, over 43,000 new domains were registered. While many of these sites may be legitimate, an equally high number may be fraudulent. Some suspiciously named domains include: whatkillscovid-19.com; usacaresfundcovid-19.com; windowcleaningcovid19.com; worldaftercovid19.in.

The domain name “worldaftercovid19.in.” mentioned above captures the suspected cybercriminal’s preparedness for the changing situational context of the COVID-19 pandemic. Overall, cybercriminals are currently exploiting the following key situational factors brought about by the COVID-19 pandemic: the need for social connectivity, the change to remote work, rising unemployment and the availability of relief funds, the need for entertainment/leisure as a result of the lockdown and stay-at-home orders, and the growing support of charities (See Tables 4 and 5).

Figure 3 shows that phishing contributes to more than half (61%) of cybercrime incidents, thus remaining the dominant choice of attack. However COVID-19 cybercriminals have also been targeting the vulnerabilities of people using SNSs (39%) to socially connect. A wide array of COVID-19 linked situational factors are in<sup>fl</sup>uencing the process of target-selection.

Summary of secondary sources.

<table><tr><td>No</td><td>Data Source</td><td>Period</td><td>Description</td></tr><tr><td>1</td><td>COVID-19 Cyber Intelligence DatafeedReports on the daily number of incidents, open or closed status, and types of open incidents</td><td>17/03/2020 – 17/04/2020</td><td>Type: Email data feedFormat: Text onlyTotal number of incidents: 43,131</td></tr><tr><td>2</td><td>COVID19 Active Scam/IncidentsDocuments providing details about active incidents</td><td>26/03/2020 – 17/04/2020</td><td>Type: Online archiveFormat: Text and ImagesTotal number of distinct archived incidents: 185</td></tr></table>

![](/api/attachments/BNQRV3JD/fulltext/images/365f8368d7c9c50ef4c58852d2abd65e04136d74ed007aecf775c9c1ce5e573c.jpg)  
Cumulative number of new COVID-related domains registered.

![](/api/attachments/BNQRV3JD/fulltext/images/bd6edcde3ee9924476261d2ef99f43642ff90911fb25e2886822758d2b24233f.jpg)  
Share of active cybercrime incidents.

The top types of organisations that are targets for impersonation are, currently, Social Networking Sites (39%), Banks (24%), Technology Firms (21%), Government Agencies (9%), Intergovernmental Agencies (2%) and other (5%) (Table 3). The majority of SNS scams targeted Facebook (82%). The detailed information of technology organisations and other key organisations impersonated is also listed in Tables 4 and 5. The key user categories being victimised includes: online banking consumers, social network site users, remote workers, online shopping users, unemployed, donors, and airline customers. Tables 4 and 5 shows that the following situation factors, such as Stay-at-home orders, Remote work, Rising unemployment, Online shopping, Social connectivity, Entertainment/Leisure, Charities, Donations, Treatments, Infections, Illness, Death, Safety measures, Loans/Financial Relief, and Airline booking refunds, were facilitating the commission of cybercrimes.

Types of organisations targeted for impersonation.

<table><tr><td>Type of Organisation</td><td>Freq</td><td>%</td></tr><tr><td>Social Networking Sites (SNS)</td><td>72</td><td>39%</td></tr><tr><td>Financial Services Organisations</td><td>45</td><td>24%</td></tr><tr><td>Technology Firms</td><td>39</td><td>21%</td></tr><tr><td>Government agencies</td><td>16</td><td>9%</td></tr><tr><td>Intergovernmental Organisations</td><td>3</td><td>2%</td></tr><tr><td>Other</td><td>10</td><td>5%</td></tr><tr><td>Grand Total</td><td>185</td><td>100%</td></tr></table>

Technologies and technology brands targeted.

<table><tr><td>Technology Type</td><td>Technology Brands Targeted/Impersonated</td><td>Situational factors</td><td>Cybercrime</td></tr><tr><td>Email</td><td>Gmail</td><td>DonationsCharities</td><td>Fake emails (Phishing)MalwareMalicious Websites</td></tr><tr><td>Social Media Technologies</td><td>FacebookInstagram</td><td>Social distancingSocial connectivityDonationsCharities</td><td>Fake Social Media ProfilesMisinformationFake Charities</td></tr><tr><td>Videotelephony and online chat services</td><td>ZoomMicrosoft TeamsWhatsappApple</td><td>Remote workVirtual Meetings</td><td>Fake Products</td></tr><tr><td>Cloud File Hosting Services</td><td>One DriveDropBox</td><td>Remote workVirtual Meetings</td><td>Fake Products</td></tr><tr><td>Streaming media service of television and movies</td><td rowspan="2">NetflixYouTube</td><td rowspan="2">Entertainment/LeisureEntertainment/Leisure</td><td rowspan="2">Fake ProductsFake Products</td></tr><tr><td>Video sharing website</td></tr><tr><td>Broadband and Telecoms Companies</td><td>4 G (Fake company)</td><td>Free Data/Internet</td><td>Fake Products</td></tr><tr><td>Online payments system</td><td>Paypal</td><td>Small business loans</td><td>Fake Website domain</td></tr></table>

Impersonations of organisations.

<table><tr><td>Types of Impersonated</td><td>Organisations/Brands</td><td>Organisational Brands Targeted/ Impersonated</td><td>Situational factors</td><td>Cybercrime</td></tr><tr><td colspan="2">Banks and Investment Companies</td><td>Banco do BrasilHSBCRBC Royal BankBank Of MontrealING</td><td>Relief ProgramsDonationsCharitiesHigh growth stocks for drug treatments and cure</td><td>Fake CharitiesFake Trading Scam</td></tr><tr><td colspan="2">Government Agencies</td><td>Federal government of the United StatesCanada Revenue AgencyGovernment of CanadaInternal Revenue Service (IRS)</td><td>Relief Programs</td><td>Fake Relief Programs</td></tr><tr><td colspan="2">Intergovernmental Agencies/</td><td>World Health Organisation</td><td>Pandemic InformationSafety MeasuresRelief Programs</td><td>DisinformationFake Relief Programs</td></tr><tr><td colspan="2">Humanitarian Organisations</td><td>Red CrossCathay Pacific</td><td>CharitiesRefunds</td><td>Fake CharitiesFake Refunds</td></tr><tr><td colspan="2">Other Brands</td><td>WoolworthsNike</td><td>FoodProtective Clothing</td><td>Fake Products</td></tr></table>

Social in<sup>fl</sup>uence principle occurrences.

<table><tr><td rowspan="2">Principle</td><td colspan="2">Phishing</td><td colspan="2">Fake SNS</td><td colspan="2">Overall Freq</td></tr><tr><td>(Freq)</td><td>%</td><td>(Freq)</td><td>%</td><td>%</td><td>%</td></tr><tr><td>Liking</td><td>102</td><td>37%</td><td>72</td><td>50%</td><td>174</td><td>42%</td></tr><tr><td>Social Proof</td><td>3</td><td>1%</td><td>72</td><td>50%</td><td>75</td><td>18%</td></tr><tr><td>Scarcity</td><td>73</td><td>27%</td><td>0</td><td>0%</td><td>73</td><td>17%</td></tr><tr><td>Authority</td><td>68</td><td>25%</td><td>0</td><td>0%</td><td>68</td><td>16%</td></tr><tr><td>Reciprocity</td><td>19</td><td>7%</td><td>0</td><td>0%</td><td>19</td><td>5%</td></tr><tr><td>Consistency</td><td>10</td><td>4%</td><td>0</td><td>0%</td><td>10</td><td>2%</td></tr><tr><td></td><td>275</td><td>100%</td><td>144</td><td>100%</td><td>317</td><td>100%</td></tr></table>

While the analysis suggests that all 6 in<sup>fl</sup>uence principles are relevant, the top three in<sup>fl</sup>uence principles are currently, Liking (42%), Social Proof (18%), and Scarcity (17%). Only Liking (50%) and Social Proof (50%) were adopted by Fake SNS (Table 6). Some examples of these in<sup>fl</sup>uences can be found in Table 8.

Emotional appeal occurrences.

<table><tr><td rowspan="2">Emotional Appeal</td><td colspan="2">Phishing</td><td colspan="2">Fake SNS</td><td colspan="2">Overall Freq</td></tr><tr><td>(Freq)</td><td>%</td><td>(Freq)</td><td>%</td><td>%</td><td>%</td></tr><tr><td>Relief</td><td>30</td><td>33%</td><td>0</td><td>0%</td><td>30</td><td>30%</td></tr><tr><td>Fear</td><td>16</td><td>18%</td><td>6</td><td>60%</td><td>22</td><td>22%</td></tr><tr><td>Hope</td><td>21</td><td>23%</td><td>1</td><td>10%</td><td>22</td><td>22%</td></tr><tr><td>Enjoyment</td><td>15</td><td>17%</td><td>0</td><td>0%</td><td>15</td><td>15%</td></tr><tr><td>Threat</td><td>3</td><td>3%</td><td>3</td><td>30%</td><td>6</td><td>6%</td></tr><tr><td>Compassion</td><td>5</td><td>6%</td><td>0</td><td>0%</td><td>5</td><td>5%</td></tr><tr><td></td><td>90</td><td>100%</td><td>10</td><td>100%</td><td>100</td><td>100%</td></tr></table>

Despite the seriousness of the COVID-19 threat, both positive and negative emotional appeals are being used in scams. The top three emotional principles are currently, Relief (30%), Fear (22%), and Hope (22%) (Table 7). The results suggest that cybercriminals are relying more on positive emotional appeals as opposed to negative emotional appeals to manipulate their targeted victims. Some examples of these emotional in<sup>fl</sup>uences can be found in Table 9. Ironically, the coronavirus image, which under normal circumstances may be categorised as a threat or disgust, is now being used as a familiarity device by cybercriminals to develop trust. Meanwhile, some of the disinformation crimes were attempting to stir panic among end-users.

Table 8. Evidence of influence techniques applied to COVID-19 crime.

<table><tr><td colspan="5">Table 8. Evidence of influence techniques applied to COVID-19 crime.</td></tr><tr><td>Principle</td><td>Propositions</td><td>Example</td><td>Theme</td><td>Sample texta</td></tr><tr><td>Authority</td><td>People tend to comply with a request that comes from an authority figure.</td><td>The WHO serves as a respected authority on the pandemic for society.</td><td>Safety measures</td><td>&quot;Distributed via the CDC Health Network&quot;</td></tr><tr><td>Consistency</td><td>People, who make a commitment, tend to feel compelled to perform consistently in line with that commitment.</td><td>Completing short and easy survey commits one to disclose personal details.</td><td>Free Entertainment</td><td>&quot;Answer 3 simple questions&quot;</td></tr><tr><td>Liking</td><td>People&#x27;s tendency for liking another person or product affects their tendency to comply with that person&#x27;s request.</td><td>Familiarity of popular banking brands.Front line healthcare worker.</td><td>DonationDonation</td><td>&quot;Select your Financial Institution&quot;See Figure A.2Photo:Photograph of a front line healthcare worker feeding an intubated Corona virus patient</td></tr><tr><td>Scarcity</td><td>People tend to value those opportunities that have limited availability (Cialdini 2009, p. 179).</td><td>Free groceries.COVID-19 relief funds by government agency.Credit relief by banks.ImpersonatingInvestment company.</td><td>Food vouchersRelief FundsPayment HolidayOverdraft supportInterest reductionInvest in &quot;hot&quot; new stocks related to curing the diseaseUsing AI to maximise returns from stock marketDrug scarcity</td><td>&quot;Hurry up! Collect your free voucher here&quot;&quot;Opps, You are not qualified&quot;&quot;Find out instantly if you are eligible to obtain urgent aid&quot;&quot;Corona Millionaire&quot;(context)&quot;The drug will be shortages fast&quot;</td></tr><tr><td>Reciprocity</td><td>People tend to comply to a requester who presents them with an initial favour or initial concession (Cialdini 2009, p. 38).</td><td>Fake Technology brand offers reward for completing COVID-19 survey.</td><td rowspan="2">Free Internet Access and DataMake new friendsCharity</td><td>&quot;500 GB of 4 G + Internet for free and for everyone!&quot;</td></tr><tr><td>Social Proof</td><td>People tend to view a particular behaviour as being more correct to the degree with which they see others in a similar situation performing the same behaviour (Cialdini 2009, p. 88).</td><td>Fake Social Media Profiles.</td><td>&quot;Increasing Corona virus fundraising statistics&quot;</td></tr></table>

<sub>ed</sub> <sub>verbat</sub>i<sub>m</sub>. <sub>Spe</sub>lli<sub>ng</sub> <sub>e</sub>r<sup>rors</sup> <sup>are</sup> <sup>from</sup> <sup>th</sup> <sub>rawn</sub> <sub>from</sub> <sub>w</sub>w<sup>w</sup>.<sup>fraudwatch</sup>i<sup>nternat</sup>i<sup>ona</sup>l.<sup>com</sup>

<table><tr><td colspan="5">Table 9. Evidence of emotional elements employed in COVID-19 cybercrime messages.</td></tr><tr><td>Element</td><td>Propositions</td><td>Example</td><td>Theme</td><td>Sample texta</td></tr><tr><td>Fear/Panic</td><td>People will tend to be persuaded by fear appeals when they feel vulnerable to an environmental threat.</td><td>Keeping informed about the local spread of the virus.</td><td>Pandemic Information</td><td>“coronavirus update disease (COVID-19) your neighbours tested positive”</td></tr><tr><td>Threat/Panic</td><td>People will tend to be persuaded by threat appeals when they feel vulnerable to an environmental threat.</td><td>Corona virus taking over the world.</td><td>Pandemic Information</td><td>Use of the virus images“Youre next”</td></tr><tr><td>Enjoyment</td><td>People will tend to be persuaded by positive appeals such as enjoyment.</td><td>Coping with lockdown and social distancing.</td><td>Entertainment</td><td>“Staying safe and enjoying the Internet at home”Images of movie covers</td></tr><tr><td>Relief</td><td>People will tend to be persuaded by positive appeals such as relief, when they feel they will gain a positive outcome such as gaining control over their lives.</td><td>Keeping informed about possible cure/treatment.</td><td>Treatment information</td><td>“Breaking!!! COVID-19 solution announced by WHO At Last.”See Figure A.1</td></tr><tr><td>Hope</td><td>People will tend to be persuaded by positive appeals such as hope.</td><td>Global relief funds.National Relief Funds.</td><td>Relief funds</td><td>Photo: Joining handsImage: Flags of nations/individual nation</td></tr><tr><td>Compassion</td><td>People will tend to show compassion for others similar to them.</td><td>Empathic concern for patient.</td><td>Widespread suffering Donation</td><td>Photo: See A2</td></tr></table>

Table 9 provides more details about the nature of the emotional appeals that are being used in COVID-19 cybercrimes.

## 5. Discussion

Understanding cybercrime during the same period as a social crisis such as the COVID-19 pandemic is crucial, given the catastrophic consequences of the resulting emotional costs, <sup>fi</sup>nancial losses, and reputational damage. Analysis of the COVID-19 cybercrime attacks shows that cybercriminals tend to follow a dynamic process that comprises four broad levels: gather information about situational factors, identify targets, select attack methods, and employ social engineering techniques. Based on the analysis, this study develops a multi-level in<sup>fl</sup>uence model of cybercrime (see Figure 4).

While prior studies on cybercrime in IS have commented on the importance of context (Abbasi et al., 2010; Jagatic et al., 2007), this study is among the <sup>fi</sup>rst in IS to adopt an approach to cybercrime that recognises the importance of the facilitating context, such as a global pandemic. This study <sup>fi</sup>nds that cybercriminals are resorting to increasingly more devious compliance techniques by integrating greater elements of situational factors into their scam designs. IS scholars seem to have paid little attention to employing criminological theories to account for these situational factors. Routine Activity Theory (RAT) appears to be a promising approach to understand the ecosystem of cyber-crimes (Holt & Bossler, 2008; Holt et al., 2020). The results show how cybercrimes work in concert with publicly available information about COVID-19. For example, the social credibility of the WHO has made them a perfect target for impersonation (Algarni et al., 2017). The study also con<sup>fi</sup>rms that cybercriminals are taking advantage of both technical and social vulnerabilities (Mitnick & Simon, 2003). For example, criminals are targeting remote workers by mimicking technology <sup>fi</sup>rms that o<sup>f</sup>er videotelephony, online chat services and cloud <sup>fi</sup>le hosting services. This study found that a large percentage of cybercrimes targeted SNSs like FaceBook, con<sup>fi</sup>rming <sup>fi</sup>ndings from previous research that SNSs are turning into a major technology target (Algarni et al., 2017). The study also con<sup>fi</sup>rms prior <sup>fi</sup>ndings that in<sup>fl</sup>uence principles and emotional features are important factors that are exploited by cybercriminals. Furthermore, it also <sup>fi</sup>nds that liking, authority and scarcity principles are the most popular principles employed in phishing scams (RT Wright et al., 2014), while liking and social proof are popular principles employed in SNS scams (Algarni et al., 2017). Cybercriminals are also exploiting multiple social in<sup>fl</sup>uence principles in a single scam. For example, they often use a combination of liking (I am familiar with the Red Cross and trust this humanitarian organisation), and social proof (other people similar to me are donating to this Red Cross COVID-19 charity, therefore I should too). Conventional wisdom suggests that cybercriminals aim to capitalise on the fear and uncertainty of their intended victims (Boss et al., 2015). Despite the seriousness of the COVID-19 threat, both positive and negative emotional appeals are being exploited (Richins, 1997). The pandemic represents both a period of human uncertainty and solidarity so cybercriminals are preying on both the hopes and fears of people (Workman, 2008). Although mainly empirically supporting prior studies mentioned above, by focusing on the pandemic this study’s major contribution is in explicating the facilitating role of the cybercrime context (Holt et al., 2020; Yar, 2005). Furthermore, the results con<sup>fi</sup>rm the integrated and process nature of cybercrime that includes gathering information about situational factors; identifying targets, selecting attack methods, and employing social engineering techniques, which represents an important <sup>fi</sup>nding.

![](/api/attachments/BNQRV3JD/fulltext/images/0afcc95b78d61b1e035b0782ea5b3bb457b113d5b9f1f7c34ab2b973d32dbf11.jpg)  
A multi-level in<sup>fl</sup>uence model of cybercrime.

## 6. Implications for theory

Theory building e<sup>f</sup>orts in prior cybercrime studies has generally been framed at a single-level of analysis or on selected aspects, focusing on either the characteristics of victims and the characteristics of the cybercrimes (Chen et al., 2011; Sheng et al., 2010; Wang et al., 2009; RT Wright et al., 2014; Wright & Marett, 2010). The multi-level in<sup>fl</sup>uence model of cybercrime o<sup>f</sup>ers a way for researchers to move beyond an individual level of analysis to assess cybercrime in a more holistic and integrated way. More importantly, the model underscores the important facilitating role of situational factors in developing a more comprehensive understanding of cybercrime (Cohen & Felson, 1979; Holt & Bossler, 2008; Miethe et al., 1990; Yar, 2005). Furthermore, the model is not only pertinent to the development of a theoretical framework on cybercrime victimisation but also has the potential to advance scholarship in areas such as social engineering, fake news, and the dark side of IT (D’Arcy et al., 2014). Moreover, this model expands the concept of social engineering by combining in<sup>fl</sup>uence principles and emotional appeals that goes beyond the use of fear appeals (Boss et al., 2015). The role of situational factors in in<sup>fl</sup>uencing perceived source credibility (impersonating someone with credibility) can be valuable in future research on disinformation campaigns and cyberpropaganda (D’Arcy et al., 2014).

This study also makes a theoretical contribution to COVID-19 and pandemic research in general. Apart from the cybersecurity <sup>fi</sup>eld, the conceptualisation of cybercrime o<sup>f</sup>ered in this study has implications for the <sup>fi</sup>elds of consumer health informatics and public health informatics (Eysenbach, 2011). These <sup>fi</sup>elds have long observed the major information challenge that outbreaks or pandemics present to society (Eysenbach, 2002). In particular, information epidemiology or “infodemiology” studies have analysed the spread of health information of varying quality and misinformation during outbreaks and pandemics (Eysenbach, 2011). The term “infodemic” has been popularised recently to characterise the sheer abundance of COVID-19 misinformation and disinformation (Zarocostas, 2020). Infodemiology researchers tend to attribute the information challenge posed during a pandemic to rumours and questionable information spread by social media users, errors or lack of accuracy in traditional mass media reporting, and health experts or authority <sup>fi</sup>gures lacking scienti<sup>fi</sup>c rigour and evidence-based knowledge (Eysenbach, 2011; Zarocostas, 2020). However, this study has shown that the co-existence of pandemics with infodemics also provides a fertile information ecosystem for cybercriminals to exploit. Therefore, there is an urgent need to broaden the conception of infodemiology, to include the role of cybercriminals and to examine the determinants of cybercrime during outbreaks or pandemics, to better inform public health and public policy. The integrated, multi-level, process approach proposed here could also have greater practical utility compared to cybercrime models that only assess the vulnerabilities of cybercrime victims.

## 7. Implications for practice

This multi-level conceptualisation of cybercrime raises a number of practical implications for cybersecurity during times of catastrophic change to society. The proposed model can be used as a systematic framework in threat modelling processes. Many threat response models used by cybersecurity experts rely on techniques such as brainstorming to identify potential cybersecurity threats and vulnerabilities (Myagmar et al., 2005). One of the limitations of brainstorming is that it is likely to omit signi<sup>fi</sup>cant threats and vulnerabilities. By understanding cybercrime from the o<sup>f</sup>ender’s perspective, security experts can provide a more comprehensive perspective about potential threats and vulnerabilities, thus placing them in a more proactive position to prevent targeted attacks. For example, COVID-19 cybercrimes are taking advantage of the situation that many companies are shifting to remote work during the pandemic as they attempt to keep employees as safe and as productive as possible. The remote work environment is a major change for many employees and consequently presents more security vulnerabilities. For a start, cybersecurity or IT departments should make users aware of the scams targeting remote workers (Anderson & Agarwal, 2010; Hart, 2009). While users working remotely can ensure that their home computer and other devices are protected by installing the latest anti-spam, anti-spyware and anti-virus software and by keeping their operating system up to date, cybersecurity or IT departments can assist by installing anti-malware and anti-phishing solutions to the home devices of remote workers to prevent many of these malicious emails and payloads from reaching them. Furthermore, IT departments should monitor and <sup>fi</sup>lter email phishing scams with headers, such as “Coronavirus Sensitive Matter” or “COVID-19 update”. Additionally, phishing emails that mimic credible institutions, such as the World Health Organisation (WHO) should be <sup>fi</sup>ltered (Figure A1). For example, WHO’s email address does not end as follows: “@who.com”, “@who.org” or “@who-safety. org”.

In the past, disaster recovery and business continuity plans focused on natural disasters, however, the current health and cybersecurity crisis suggests that these plans need a major review. These plans need to consider risks, such as future pandemics and even the possibility of a cyberwar. Parts of the multi-level model can be used to re-assess disaster recovery and business continuity plans, especially with regards to technological vulnerabilities that can hamper the organisation’s response and recovery. The model can also be used to help improve the e<sup>f</sup>ectiveness of training by informing simulation exercises during a crisis (Jalali et al., 2019). Situational factors can play an important role in providing information about speci<sup>fi</sup>c security threats that may arise. As society moves from the lockdown phase of the pandemic to the re-entry phase, the model predicts that cybercrime will evolve with these trends. For example, employment-related cybercrime scams targeting the unemployed will increase signi<sup>fi</sup>cantly given the burgeoning rate of unemployment expected. Proactive technology-based countermeasures and user education can help to combat the next wave of COVID-19 cybercrime. An increase in collaboration within the broader cybersecurity community will also be required to <sup>fi</sup>ght this great threat facing society.

## 8. Conclusion

This study analysed and interpreted COVID-19 related cybercrime data from across the globe. The sheer scale of COVID-19 cybercrimes observed is alarming. The study <sup>fi</sup>nds that these cybercrimes are consistently shifting in breadth, diversity and method of attack by adapting to situational changes during the COVID-19 pandemic. A relatively comprehensive multi-level in<sup>fl</sup>uence model of cybercrime is proposed that integrates prior IS research with an existing criminological framework – the lifestyle-routine activities theory. Due to methodological limitations, this study could not investigate individual vulnerability di<sup>f</sup>erences to cybercrimes. Although key social in<sup>fl</sup>uence mechanisms and emotional appeals were identi<sup>fi</sup>ed, the extent to which individual di<sup>f</sup>erences contribute to cybercrime victimisation as opposed to situational factors remains to be seen. For example, it is possible that despite the situational factors, individuals with a high degree of self-control may not fall prey to cybercrime victimisation. Despite these limitations, it was important to explore how cybercriminals are attempting to exploit situational factors to deceive end-users in the context of a pandemic. Future studies could use experimental research designs to predict the relative vulnerability of end-users in a simulated social crisis. Hopefully more cybercrime research is done and more e<sup>f</sup>ective countermeasures are put in place to ensure a safer digital world while the world continues to be plagued by COVID-19. A safer digital world can help us to cope better with many of the other pressing challenges during the pandemic and new challenges that can be expected in the postpandemic future.

## Notes

1. https://www.forbes.com/sites/thomasbrewster/2020 03/18/how-americas-cyber-defenders-are-preparingto-save-you-from-an-unprecedented-wave-ofcoronavirus-scams.

2. https://thehill.com/policy/cybersecurity/493,198-fbisees-spike-in-cyber-crime-reports-duringcoronavirus-pandemic.

3. https://ciso.economictimes.indiatimes.com/news/ covid-19-related-phishing-attacks-up-by-667-report /74,839,322.

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the author.

## ORCID

Rennie Naidoo http://orcid.org/0000-0001-8392-1136

## References

Abbasi, A., Zhang, Z., Zimbra, D., & Chen, H. (2010). Detecting fake websites: The contribution of statistical learning theory. MIS Quarterly, 34(3), 435–461. https:/ doi.org/10.2307/25750686

Accenture (2019) The cost of cybercrime. Retrieved 25 April, 2020 from https://www.accenture.com/us-en/insights security/cost-cybercrime-study

Agarwal, R., & Karahanna, E. (2000). Time <sup>fl</sup>ies when you’re having fun: Cognitive absorption and beliefs about information technology usage. MIS Quarterly, 24(4), 665–694. https://doi.org/10.2307/3250951

Akbar, N. (2014) Analysing Persuasion principles in phishing emails. Masters Thesis. University of Twente.

Algarni, A., XU, Y., & Chan, T. (2014) Social engineering in social networking sites: The art of impersonation. In 2014 IEEE International Conference on Services Computing pp 797–804, IEEE, Anchorage, AK, USA.

Algarni, A., XU, Y., & Chan, T. (2017). An empirical study on the susceptibility to social engineering in social

networking sites: The case of Facebook. European Journal of Information Systems, 26(6), 661–687. https:// doi.org/10.1057/s41303-017-0057-y

Anderson, C. L., & Agarwal, R. (2010). Practicing safe computing: A multimethod empirical examination of home computer user security behavioral intentions. MIS Quarterly, 34(3), 613–643. https://doi.org/10.2307/ 25750694

Bhattacherjee, A., & Sanford, C. (2006). In<sup>fl</sup>uence processes for information technology acceptance: An elaboration likelihood model. MIS Quarterly, 30(4), 805–825. https:// doi.org/10.2307/25148755

Bose, I., & Leung, A. C. M. (2007). Unveiling the mask of phishing: Threats, preventive measures, and responsibilities. Communications of the Association for Information Systems, 19(24), 544–566. https://doi.org/ 10.17705/1CAIS.01924

Boss, S. R., Galletta, D. F., Lowry, P. B., Moody, G. D., & Polak, P. (2015). What do systems users have to fear? Using fear appeals to engender threats and fear that motivate protective security behaviors. MIS Quarterly, 39(4), 837–864. https://doi.org/10.25300/MISQ/2015/39.4.5

Brum<sup>fi</sup>eld, C. (2020) Beware malware-laden emails ofering COVID-19 information, US secret service warns. CSO. Retrieved 24 April, 2020 from https://www.csoonline. com/article/3536696/us-secret-service-warns-ofmalicious-emails-o<sup>f</sup>ering-covid-19-information.html

Chen, R., Wang, J., Herath, T., & Rao, H. R. (2011). An investigation of email processing from a risky decision making perspective. Decision Support Systems, 52(1), 73–81. https://doi.org/10.1016/j.dss.2011.05.005

Cialdini, R. B. (2001). Influence: Science and practice (4th ed.). Allyn and Bacon.

Cialdini, R. B., & Goldstein, N. J. (2004). Social in<sup>fl</sup>uence: Compliance and conformity. Annual Review of Psychology, 55(1), 591–621. https://doi.org/10.1146/ annurev.psych.55.090902.142015

Cialdini, R.B. (2009). In<sup>fl</sup>uence: The psychology of persuasion (Kindle ed.). HarperCollins.

Ciardhuáin, S. Ó. (2004). An Extended Model of Cybercrime Investigations. International Journal of Digital Evidence, 3(1), 1–22. https://dblp.org/rec/jour nals/ijde/Ciardhuain04

Cimpanu, C. (2020) FBI says cybercrime reports quadrupled during COVID-19 pandemic. Retrieved 20 April, 2020 from https://www.zdnet.com/article/fbi-says-cybercrime -reports-quadrupled-during-covid-19-pandemic

Clough, J. (2010). Principles of Cybercrime. Cambridge University Press.

Cohen, L. E., & Felson, M. (1979). Social change and crime rate trends: A routine activity approach. American Sociological Review, 44(4), 588–608. https://doi.org/10. 2307/2094589

Crabtree, B. F., & Miller, W. L. (1992). A template approach to text analysis: Developing and using codebooks. In B. F. Crabtree & W. L. Miller (Eds.), Doing qualitative research (pp. 93–109). Sage Publications.

D’Arcy, J., Gupta, A., Tarafdar, M., & Turel, O. (2014). Re<sup>fl</sup>ecting on the “dark side” of information technology use. Communications of the Association for Information Systems, 35(5), 109–118. https://doi.org/10.17705/1CAIS. 03505

Dillard, J., & Peck, E. (2006). Persuasion and the structure of a<sup>f</sup>ect. Human Communication Research, 27(1), 38–68. https://doi.org/10.1111/j.1468-2958.2001.tb00775.x

Eysenbach, G. (2002). Infodemiology: The epidemiology of (mis)information. The American Journal of Medicine, 113

(9), 763–765. https://doi.org/10.1016/S0002-9343(02) 01473-0

Eysenbach, G. (2011). Infodemiology and Infoveillance. American Journal of Preventive Medicine, 40(5), S154– S158. https://doi.org/10.1016/j.amepre.2011.02.006

Fereday, J., & Muir-Cochrane, E. (2006). Demonstrating rigor using thematic analysis: A hybrid approach of inductive and deductive coding and theme development. International Journal of Qualitative Methods, 5(1), 80–92. https://doi.org/10.1177/160940690600500107

Ferreira, A., Coventry, L., & Lenzini, G. (2015). Principles of Persuasion in social engineering and their use in phishing. In T. Tryfonas & I. Askoxylakis (Eds.), Human aspects of information security, privacy, and trust (pp. 36–47). Springer International Publishing.

Gigerenzer, G., & Todd, P. M. (1999). Simple heuristics that make us smart. Oxford University Press.

Gleeson, K. (2011). Polytextual thematic analysis for visual data. In P. Reavey (Ed.), Visual methods in psychology: Using and interpreting images in qualitative research (pp. 314–329). Psychology Press.

Gordon, S., & Ford, R. (2006). On the de<sup>fi</sup>nition and classi-<sup>fi</sup>cation of cybercrime. Journal in Computer Virology, 2 (1), 13–20. https://doi.org/10.1007/s11416-006-0015-z

Hart, J. (2009). Remote working: Managing the balancing act between network access and data security. Computer Fraud & Security, 2009(11), 14–17. https://doi.org/10. 1016/S1361-3723(09)70141-1

Holt, T. J., & Bossler, A. M. (2008). Examining the applicability of lifestyle-routine activities theory for cybercrime victimization. Deviant Behavior, 30(1), 1–25. https://doi. org/10.1080/01639620701876577

Holt, T. J., Van Wilsem, J., Van De Weijer, S., & Leukfeldt, R. (2020). Testing an integrated self-control and routine activ ities framework to examine malware infection victimization. Social Science Computer Review, 38(2), 187–206. https://doi. org/10.1177/0894439318805067

Hovland, C. I., & Weiss, W. (1951). The in<sup>fl</sup>uence of source credibility on communication e<sup>f</sup>ectiveness. The Public Opinion Quarterly, 15(4), 635–650. https://doi.org/10. 1086/266350

Jagatic, T. N., Johnson, N. A., Jakobsson, M., & Menczer, F. (2007). Social phishing. Communications of the ACM, 50 (10), 94–100. https://doi.org/10.1145/1290958.1290968

Jalali, M. S., Siegel, M., & Madnick, S. (2019). Decisionmaking and biases in cybersecurity capability development: Evidence from a simulation game experiment. The Journal of Strategic Information Systems, 28(1), 66–82. https://doi.org/10.1016/j.jsis.2018.09.003

Jensen, M. L., Dinger, M., Wright, R. T., & Thatcher, J. B. (2017). Training to mitigate phishing attacks using mindfulness techniques. Journal of Management Information Systems, 34(2), 597–626. https://doi.org/10.1080 07421222.2017.1334499

Krombholz, K., Hobel, H., Huber, M., & Weippl, E. (2015). Advanced social engineering attacks. Journal of Information Security and Applications, 22, 113–122. https://doi.org/10.1016/j.jisa.2014.09.005

Kumaran, N., & Lugani, S. (2020) Identity and security. Protecting businesses against cyber threats during COVID-19 and beyond. Retrieved 20 April, 2020 from https://cloud.google.com/blog/products/identity-security /protecting-against-cyber-threats-during-covid-19-andbeyond

Lee, A. S., & Baskerville, R. L. (2003). Generalizing generalizability in information systems research. Information

Systems Research, 14(3), 221–243. https://doi.org/10. 1287/isre.14.3.221.16560

Luo, X., Brody, R., Seazzu, A., & Burd, S. (2011). Social engineering: The neglected human factor for information security management. Information Resources Management Journal, 24(3), 1–8. https://doi.org/10. 4018/irmj.2011070101

Luo, X., Zhang, W., Burd, S., & Seazzu, A. (2013). Investigating phishing victimization with the heuristic– systematic model: A theoretical framework and an exploration. Computers & Security, 38, 28–38. https:// doi.org/10.1016/j.cose.2012.12.003

Maimon, D., & Louderback, E. R. (2019). Cyber-dependent crimes: An interdisciplinary review. Annual Review of Criminology, 2(1), 191–216. https://doi.org/10.1146/ annurev-criminol-032317-092057

Mckenna, B., Myers, M. D., & Newman, M. (2017). Social media in qualitative research: Challenges and recommendations. Information and Organization, 27(2), 87–99. https://doi.org/10.1016/j.infoandorg.2017.03.001

Miethe, T. D., Sta<sup>f</sup>ord, M. C., & Sloane, D. (1990). Lifestyle changes and risks of criminal victimization. Journal of Quantitative Criminology, 6(4), 357–376. https://doi.org/ 10.1007/BF01066676

Milgram, S. (1974). Obedience to authority. Harper.

Mitnick, K. D., & Simon, W. L. (2003). The art of deception: Controlling the human element of security. John Wiley & Sons, Inc.

Moneva, A., Miró-Llinares, F., & Hart, T. C. (2020). Hunter or prey? Exploring the situational pro<sup>fi</sup>les that de<sup>fi</sup>ne repeated online harassment victims and o<sup>f</sup>enders. Deviant Behavior, 1–16. https://doi.org/10.1080/ 01639625.2020.1746135

Morgan, S. (2017) Is cybercrime the greatest threat to every company in the world? CSO. Retrieved 24 April, 2020 from https://www.csoonline.com/article/3210912/is-cybercrimethe-greatest-threat-to-every-company-in-the-world.html

Morgan, S. (2019) Oficial annual cybercrime report. Cybersecurity Ventures. Retrieved 24 April, 2020 from https://www.herjavecgroup.com/the-2019-o<sup>fi</sup>cial-annual -cybercrime-report/

Muncaster, P. (2020) Cyber-attacks up 37% over past month as #COVID19 bites. Infosecurity Magazine. Retrieved 25 April, 2020 from https://www.infosecurity-magazine. com/news/cyberattacks-up-37-over-past-month

Myagmar, S., AJ, L., & Yurcik, W. (2005) Threat modeling as a basis for security requirements. In Symposium on requirements engineering for information security (SREIS), paris, france, pp 1–8.

Myers, M. D. (2009). Qualitative research in business and management (1st ed.). Sage Publications.

Ngo, F. T., & Paternoster, R. (2011). Cybercrime victimization: An examination of individual and situational level factors. International Journal of Cyber Criminology, 5(1), 773–793.

Ngwenyama, O. K., & Lee, A. S. (1997). Communication richness in electronic mail: Critical social theory and the contextuality of meaning. MIS Quarterly, 21(2), 145–167. https://doi.org/10.2307/249417

Orbach, B. (2018). Con men and their enablers: The anatomy of con<sup>fi</sup>dence games. Social Research: An International Quarterly, 85(4), 795–822. https://muse. jhu.edu/article/716115

Petty, R. E., & Cacioppo, J. T. (1986). The elaboration likelihood model of persuasion. In L. Berkowitz (Ed.), Advances in experimental social psychology (pp. 123–205). Academic Press.

P<sup>fl</sup>eeger, S. L., Sasse, M. A., & Furnham, A. (2014). From weakest link to security hero: Transforming sta<sup>f</sup> security behavior. Journal of Homeland Security and Emergency Management, 11(4), 489–510. https://doi.org/10.1515 jhsem-2014-0035

Richins, M. L. (1997). Measuring emotions in the consumption experience. Journal of Consumer Research, 24(2), 127–146. https://doi.org/10.1086/209499

Ruddin, L. P. (2006). You can generalize stupid! social scientists, bent <sup>fl</sup>yvbjerg, and case study methodology. Qualitative Inquiry, 12(4), 797–812. https://doi.org/10. 1177/1077800406288622

Segura, J. (2020) Online credit card skimming increased by 26 percent in March. accessed 20 April, 2020 from https:/ blog.malwarebytes.com/cybercrime/2020/04/onlinecredit-card-skimming-increases-by-26-in-march/

Sheng, S., Holbrook, M., Kumaraguru, P., Cranor, L. F., & Downs, J. (2010) Who falls for phish?: A demographic analysis of phishing susceptibility and e<sup>f</sup>ectiveness of interventions. In Proceedings of the 28th international conference on Human factors in computing systems - CHI ’10 p. 373, ACM Press, Atlanta, GA, USA.

Shi, F. (2020) Coronavirus-related phishing. Retrieved 10 April, 2020 from https://blog.barracuda.com/2020/03 26/threat-spotlight-coronavirus-related-phishing

Sørensen, H. T., Sabroe, S., & Olsen, J. (1996). A framework for evaluation of secondary data sources for epidemiological research. International Journal of Epidemiology, 25 (2), 435–442. https://doi.org/10.1093/ije/25.2.435

Stajano, F., & Wilson, P. (2011). Understanding scam victims: Seven principles for systems security. Communications of the ACM, 54(3), 70–75. https://doi. org/10.1145/1897852.1897872

Sussman, S. W., & Siegal, W. S. (2003). Informational in<sup>fl</sup>uence in organizations: An integrated approach to knowledge adoption. Information Systems Research, 14(1), 47–65. https://doi.org/10.1287/isre.14.1.47.14767

Wang, J., Chen, R., Herath, T., & Rao, H. R. (2009). Visual e-mail authentication and identi<sup>fi</sup>cation services: An investigation of the e<sup>f</sup>ects on e-mail use. Decision Support Systems, 48(1), 92–102. https://doi.org/10.1016 j.dss.2009.06.012

Westerman, D., Spence, P. R., & Van Der Heide, B. (2014). Social media as information source: Recency of updates and credibility of information. Journal of Computer

Mediated Communication, 19(2), 171–183. https://doi. org/10.1111/jcc4.12041

Witte, K. (1992). Putting the fear back into fear appeals: The extended parallel process model. Communication Monographs, 59(4), 329–349. https://doi.org/10.1080/ 03637759209376276

Workman, M. (2008). Wisecrackers: A theory-grounded investigation of phishing and pretext social engineering threats to information security. Journal of the American Society for Information Science and Technology, 59(4), 662–674. https://doi.org/10.1002/ asi.20779

World Economic Forum (2019) The global risks report 2019. World Economic Forum. Retrieved 25 April, 2020 from https://www.weforum.org/reports/the-global-risksreport-2019

Wright, R., Chakraborty, S., Basoglu, A., & Marett, K. (2010). Where did they go right? Understanding the deception in phishing communications. Group Decision and Negotiation, 19(4), 391–416. https://doi.org/10.1007/ s10726-009-9167-9

Wright, R. T., Jensen, M. L., Thatcher, J. B., Dinger, M., & Marett, K. (2014). Research note —In<sup>fl</sup>uence techniques in phishing attacks: An examination of vulnerability and resistance. Information Systems Research, 25(2), 385–400. https://doi.org/10.1287/isre.2014.0522

Wright, R. T., & Marett, K. (2010). The in<sup>fl</sup>uence of experiential and dispositional factors in phishing: An empirical investigation of the deceived. Journal of Management Information Systems, 27(1), 273–303. https://doi.org/10. 2753/MIS0742-1222270111

Yar, M. (2005). The novelty of ‘cybercrime’: An assessment in light of routine activity theory. European Journal of Criminology, 2(4), 407–427. https://doi.org/10.1177/ 147737080556056

Yue, W. T., Wang, Q.-H., & Hui, K.-L. (2019). See no evil, hear no evil? Dissecting the impact of online hacker forums. MIS Quarterly, 43(1), 73–95. https://doi.org/10. 25300/MISQ/2019/13042

Zarocostas, J. (2020). How to <sup>fi</sup>ght an infodemic. The Lancet, 395(10225), 676. https://doi.org/10.1016/S0140-6736(20) 30461-X

Zimbardo, P. (2008). The Lucifer efect: Understanding how good people turn evil. Random House.

## Appendix

![](/api/attachments/BNQRV3JD/fulltext/images/c272856a7b5658b74fbe6b6576b0c6416a772a94a06de55aa85e0e3e629d6514.jpg)  
Phishing Email.

![](/api/attachments/BNQRV3JD/fulltext/images/6bf6fd85f5bfb4934fa1d6f9d7ec9aecca6178d2187dcb9f36843f28641dd776.jpg)  
Fake Web Site.
