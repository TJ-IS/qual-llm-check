---
otero_id: 820
otero_key: "7DXXMT87"
title: "Taking stock of organisations’ protection of privacy: categorising and assessing threats to personally identifiable information in the USA"
authors: "Clay Posey; Uzma Raja; Robert E. Crossler; A. J. Burns"
year: "2017"
journal: "European Journal of Information Systems"
doi: "10.1057/s41303-017-0065-y"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
EMPIRICAL RESEARCH

# Taking stock of organisations’ protection of privacy: categorising and assessing threats to personally identifiable information in the USA

Clay Posey<sup>1</sup>, Uzma Raja<sup>2</sup>, Robert E. Crossler<sup>3</sup> and A. J. Burns<sup>4</sup>

<sup>1</sup>Department of Management, College of Business Administration, University of Central Florida, P.O. Box 161400, Orlando, FL 32816, USA; <sup>2</sup>Department of Information Systems, Statistics, and Management Science, Culverhouse College of Commerce, The University of Alabama, Tuscaloosa, AL 35487, USA; <sup>3</sup>Department of Management, Information Systems, and Entrepreneurship, Carson College of Business, Washington State University, Pullman, WA 99164, USA; <sup>4</sup>Department of Computer Science, College of Business and Technology, The University of Texas at Tyler, Tyler, TX 75799, USA

Correspondence: Clay Posey, Department of Management, College of Business Administration, University of Central Florida, P.O. Box 161400, Orlando, FL 32816, USA. Tel: 1 (407) 823-5569: E-mail: Clay.Posey@ucf.edu

Special Issue Editors: Paul Benjamin Lowry, Tamara Dinev, Robert Willison

Electronic supplementary material The online version of this article (doi:10.1057/ s41303-017-0065-y) contains supplementary material which is available to authorized users

Received: 31 January 2016 Last Revised: 12 June 2017 Accepted: 18 June 2017

## Abstract

Many organisations create, store, or purchase information that links individuals’ identities to other data. Termed personally identifiable information (PII), this information has become the lifeblood of many firms across the globe. As organisations accumulate their constituencies’ PII (e.g. customers’, students’, patients’, and employees’ data), individuals’ privacy will depend on the adequacy of organisations’ information privacy safeguards. Despite existing protections, many breaches still occur. For example, US organisations reported around 4,500 PII-breach events between 2005 and 2015. With such a high number of breaches, determining all threats to PII within organisations proves a burdensome task. In light of this difficulty, we utilise text-mining and cluster analysis techniques to create a taxonomy of various organisational PII breaches, which will help drive targeted research towards organisational PII protection. From an organisational systematics perspective, our classification system provides a foundation to explain the diversity among the myriad of threats. We identify eight major PII-breach types and provide initial literature reviews for each type of breach. We detail how US organisations differ regarding their exposure to these breaches, as well as how the level of severity (i.e. number of records affected) differs among these PII breaches. Finally, we offer several paths for future research.

European Journal of Information Systems (2017). doi:10.1057/s41303-017-0065-y

Keywords: personally identifiable information (PII); breach analysis; taxonomy development; privacy; confidentiality

## Introduction

In the course of normal operations, organisations across the globe collect personally identifiable information (PII) about their employees, as well as those individuals to whom they provide products or services. PII is defined as ‘(1) any information that can be used to distinguish or trace an individual’s identity, such as name, social security number, date, and place of birth, mother’s maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information’ (McCallister et al, 2010, p. 2-1). As organisations more frequently collect, store, and disseminate such sensitive information for legitimate business purposes, the potential threats to individuals’ privacy rise. Thus, the increased collection of personal information presents increased opportunities for both legitimate and illegitimate uses of individuals’ PII (Burns et al, 2015).

Breaches of personal information regularly occur in many nations around the world and across industries, including governmental organisations, financial industries, health institutions, and education providers (Ausick, 2016; DutchNews, 2016; Heller, 2016; Information Commissioner’s Office, 2016; Kish, 2016). Complicating the issue is the reality that privacy concerns are not monolithic across cultures, societies, or individuals, but rather, context informs much of the differences among various privacy perceptions (Nissenbaum, 2009). Philosophical differences among nations, for example, drive disparate priorities when it comes to protecting the privacy of the citizenry. In this paper, we focus on a comprehensive view of the breach ecosystem in the USA, in particular, because of the availability of data and the international interest in the privacy protections afforded by US organisations.

A comprehensive approach is warranted given the many high-profile data breaches affecting both the public and private sectors in the USA. For example, in the public sector in the USA, both the Internal Revenue Service (IRS) and Office of Personnel Management (OPM) suffered large breaches, and in the private sector, insurer Anthem, telecommunications giant AT&T, and retailer Target have all suffered high-profile breaches. For corporations, data breaches often result in negative press, which erodes public trust and ultimately may lead to a decrease in market share (Cavusoglu et al, 2004; Goel & Shawky, 2009). For example, breaches within public agencies have led to agency director resignations and workflow disruptions caused by a need to revert to paper-and-pencil processes (Davis, 2015; Katz, 2015). However, in a global economy, one person’s inconvenience may be a violation of another person’s fundamental right to privacy (Shaffer, 2000).

To assist organisational decision-makers in the protection of PII, it is important to take stock of how organisations have fared with past PII-related threats. Specifically, we believe that a historical analysis of publicly reported breaches is needed so that organisations across industries and sectors can better learn where their protective emphases have worked well and where room for improvement exists. In addition, the current study can help institutions residing in countries outside the USA that wish to engage with US organisations.

From a theoretical perspective, not only is it important for the IS community to develop its own theories and concepts in a systematic way (Hassan & Lowry, 2015; Markus & Saunders, 2007). A discipline must first be able to elicit and determine how its objects of interest relate to one another before moving on to in-depth explanations and assessments of the antecedents to or consequences of those objects. Specifically, from the viewpoint of organisational systematics (McKelvey, 1978, 1982), researchers should leverage the science of diversity to guide the science of universal activities (Lee & Baskerville, 2003). Unless and until these objects are classified via formal classification systems, researchers cannot be certain how, and even whether, the findings obtained from an examination of one type of object can extend to and benefit another (Posey et al, 2013). For these practical and theoretical reasons, we develop a data-driven taxonomy of PII-related breaches via text-mining and cluster analysis efforts and then assess whether discrepancies exist among how organisations within individual US states have performed within the last decade.

Our findings are fourfold. First, our initial exploratory analysis of breach density across different US states reveals state-level differences in the source and frequency of PII breaches. Second, we create a taxonomy that provides information about eight well-defined classes of breaches related to PII. Third, we follow with summary information on the current literature within each identified cluster. Finally, our in-depth assessment of PII breaches assigned to each class underscores important discrepancies among different types of organisations, as well as organisations across the USA.

## Background

Protecting sensitive information is a complicated endeavour, requiring consideration of diverse multidimensional threat vectors. For example, take the threat vector stemming from employees. Employees are a significant source of unauthorised dissemination because of simple human error (Im & Baskerville, 2005; Liginlal et al, 2009), circumvention of security measures because of perceived hindrances or stress in their jobs (i.e. workarounds) (Burns et al, 2015; D’Arcy et al, 2014; Dhillon & Torkzadeh, 2006), and even intentionally deviant actions (Hu et al, 2011; Willison & Warkentin, 2013). All of these threats are challenging to control, regardless of the approach chosen. The insider threat represents only one threat category identified by the Privacy Rights Clearinghouse (PRC), which classifies breaches as (1) unintended disclosure, (2) hacking or malware, (3) payment card fraud, (4) insider, (5) physical loss, (6) portable device, or (7) stationary device.

As reported by the PRC, a myriad of organisations publicly reported almost 4,500 PII-related breaches from 2005 through 2015 in the USA alone. Forty-eight per cent of these breaches reported an estimate for the number of records affected by the respective breaches, which totalled nearly 900 million breached records. Interestingly, breach reports from organisations within EU member states indicate they suffered from a 645-million-record loss during roughly the same time period (Howard & Gulyas, 2014). Unfortunately, there is no way to provide an accurate estimate of total harm inflicted because many breach reports (i.e. about half) indicate an ‘unknown’ number of records affected, while yet other breaches are not publicly reported at all (Kotulic & Clark, 2004). Even with this deficiency in the reporting, it is evident that PII-related breaches have presented significant issues for organisations across various industries and countries and will continue to do so in the future.

Although PII-related breaches cause significant issues for organisations, limited organisational-level privacy research exists (Be´langer & Crossler, 2011; Pavlou, 2011; Smith et al, 2011), with much of this research discussing how organisations provide privacy protection (Be´langer & Crossler, 2011). Since the publication of these papers, more research has tried to present a theoretical understanding of why privacy breaches occur at the organisational level (e.g. Parks et al, 2016; Wall et al, 2015). Parks et al (2016) utilised a grounded theory approach to identify the effectiveness of privacy compliance in the context of healthcare organisations; the findings indicate that organisational-level decisions are not based on a privacy calculus, but rather focus on an imbalance challenge, that is, the unintended consequences of privacy safeguards are compared against the intended positive impacts. When the unintended consequences outweigh the intended positive impacts, healthcare organisations then have to react with different privacy safeguards. Wall et al (2015) theoretically explored why organisations are in violation of privacy regulations designed to keep consumers and protected health information secure. Although the authors did not empirically test their research model, the researchers used the TJX case to demonstrate that top managers’ low view of risks, external factors such as economic strain, lack of monitoring controls and penalties, lack of negative outcomes for prior non-compliant behaviour and lack of rules related to policy compliance resulted in increased privacy regulation violations.

To guide further research in organisational-level privacy research, however, it is vital that the academic community obtain a solid understanding of the PII-threat landscape. This understanding can occur via formal taxonomic-development efforts. From an organisationa systematics perspective (McKelvey, 1978, 1982), taxonomies are classification systems using sets of objects of interest that help uncover the differences among the classified or grouped objects, helping fulfil the requirements of the science of diversity. These classification activities must occur prior to assessing the universal laws that govern those objects, termed the science of universals. In other words, it is a requisite that researchers understand the components residing within a system before attempting to model them and their antecedents or consequences (Lee & Baskerville, 2003; McKelvey, 1982). Once this identification has been achieved, future research may further engage in strategy formation to mitigate the identified threats before they can reach the organisation. Additionally, a taxonomy of the threats wil assist organisations, nations, and societies in formulating appropriate responses to these specific threat vectors that are adversely affecting organisations across their respective industries and host countries – including suggesting precautions to take before the attack and remediation efforts afterwards (i.e. the ‘left of bang’ and ‘right of bang’ strategies, respectively) (Baskerville et al, 2014; Willison & Warkentin, 2010). For this reason, we assert that a formal taxonomy of PII-related threats derived from historical evidence is essential for the protection of global information flows (i.e. with respect to the study of privacyrelated threats) and can provide the ability to inform and empirically test the propositions suggested by Wall et al (2015).

Given the importance of information threats and the amount of diversity present among these threats, numerous classification systems have been proposed to help describe the various components of this complex environment in a parsimonious manner (Igure & Williams, 2008). For example, researchers have created taxonomies for security technologies and response mechanisms (Jayaram & Morse, 1997; Venter & Eloff, 2003), as well as intrusion and attack techniques and other threats in a myriad of environments (Friedman & Hoffman, 2008; Lindqvist & Jonsson, 1997; Roosta et al, 2006). More closely related to PII-focused threats, basic taxonomies for identity crimes and confidentiality breaches also exist (Brann & Mattson, 2004; Koops et al, 2009; Pemble, 2008).

Notwithstanding their importance, the taxonomies focusing on identity crimes and confidentiality are limited in that they were developed either without quantitative data, or they focus on a single industry (i.e. health). What is needed, then, is a more holistic classification system that takes into account the available historical evidence gathered from breaches occurring across various organisations and industries. Once this classification system is created and the amount of diversity among members uncovered, we can then assess whether discrepancies exist in how certain geographical areas have fared relative to these identified breach types. Weaknesses found in one geographical area might indicate a lack of appropriate funding or employee training for that type of PII-related breach category. Conversely, information about organisations faring better in one region could be leveraged by organisations in areas found to have significant weaknesses. Furthermore, once the relevant literature within each classification type is examined, the current research gaps become more evident.

In the remainder of this manuscript, we detail our efforts in creating such a formal taxonomy of PII-related threats to help fill the need to focus on the science of diversity in organisational-level privacy research. We then provide an in-depth analysis of the current literature regarding each PII-breach type. We also assess the distinct types of threats across the USA (i.e. 50 states and the District of Columbia) to help identify potential strengths and deficiencies among the geographical regions. Finally, we discuss our findings, note the limitations, and highlight potential future research efforts.

## Taxonomy development

## Data collection

To develop our taxonomy, we utilised the historical breach information provided by PRC, as mentioned earlier. This repository, which begins with data from 1 January 2005, contained almost 4,500 unique breach reports when we obtained the data in January 2015. The final publicised PII breach included in the analysis occurred on 7 January 2015.

## Exploratory analysis of breach density

The total number of PII breaches for the assessment period was 4,489. The data set contains information on the state where the attack occurred (captured as the attacked organisation’s headquarters), the attack’s origin, the nature of the attacked organisation, the number of records affected (if reported), and the textual report of the breach itself. However, before performing text mining and cluster analysis on the breach reports to form a datadriven taxonomy, we perform two exploratory analyses of the reported attacks.

First, we review the data to determine how the number of attacks was geographically dispersed across the USA. To be able to make comparisons across states, we normalise the count of breaches by using each states average gross domestic product (GDP) from 2005 to 2014 as reported by the US Bureau of Economic Analysis. Normalising for state-level GDP helps to account for differences in the population and workforce within each state while also accounting for increased overall opportunities for breaches in economically stronger areas over weaker ones (Sen & Borle, 2015). Figure 1 shows the overall distribution of the normalised reported PII breaches across the USA. The results indicate that when controlling for GDP, organisations in Vermont, Montana, and Rhode Island had more PII-related breaches than other states for the given period. Given the states’ GDPs, organisations in New Hampshire, Indiana, and Colorado also experienced relatively high levels of PII-breach events since 2005. Some large population centres (e.g. California and New York) experienced high overall PIIbreach counts; however, when normalising for GDP, the resulting breach density is shown to be moderate. Texas, on the other hand, faired rather well in terms of breach density considering its population.

To explore the basic geographical dispersion in a bit more detail, we examined how the volume of insiderresponsible PII breaches (as classified by PRC) varied across states. Given that insiders are a significant threat vector to confidential data and information (Crossler et al, 2013; Warkentin & Willison, 2009), we believe this exploration will help organisations within individual states in the USA determine their exposure to internal PII threats relative to organisations residing in other states. Figure 2 shows the distribution of insider-sourced attacks across various states, again controlling for state-level GDP.

The insider-sourced analysis summarised in Figure 2 reveals several disparities from the overall breach density map shown in Figure 1. Specifically, insider-sourced attacks were more prevalent in Hawaii, Florida, Minnesota, and Alabama, whereas these states were not prominent in the overall breach analyses of Figure 1. Other states with relatively high insider incidence despite relatively low overall breach levels were Texas, Arkansas, and Arizona. These findings show that although organisations in a given state might not succumb to the wide variety of PII-related breaches possible, they may be more vulnerable to certain breach categories.

![](/api/attachments/7DXXMT87/fulltext/images/9819996e9c7d65005947048266d9bb6dc4cf733ace5ec8d9d7afc89c2a3150e3.jpg)  
Figure 1 Normalised PII-breach density.

![](/api/attachments/7DXXMT87/fulltext/images/40d71bcee0f5cde998ac261156e8566907ce6adde4d5c499b040cd3650702fd7.jpg)  
Figure 2 Normalised PII-breach density from organisational insiders.

## Taxonomy creation

To develop a taxonomy, archival reports can be used to derive knowledge about the nature of the events (Kemerer & Slaughter, 1999). Whereas the descriptive language of unstructured breach reports within the PRC archive provides detailed information, hand coding of such extensive data can become expensive and difficult, especially as the number of events increases. Thus, automated categorisation techniques were an attractive option. Although previous research has used key terms and tags to create basic taxonomies, we developed our PII-breach classification system using text mining. Unstructured textual information can provide a useful tool to identify underlying themes and develop taxonomies (Evangelopoulos et al, 2012; Sidorova et al, 2008). Text-mining techniques can be used to classify the reports into categories based on word-occurrence patterns within the archival reports. Wang et al (2013) cluster the security risk disclosures to identify risk mitigation themes. We use a similar technique to develop our taxonomy.

Each breach-announcement report contained multiple tokens. A token is a string of continuous characters without a separator (e.g. comma, period). A term consists of one or multiple tokens that have a useful meaning. The PRC breach reports all have textual descriptions. For this study, the complete description for each PII breach was used to allow for a rich content analysis. Text mining allowed for tracking the occurrence of the tokens and terms over the corpus. A corpus is the entire collection of textual documents. In this study, corpus refers to the collection of all the breach reports made available through PRC.

After collecting the corpus, we created lists of stop and start terms. Stop terms are terms in the documents that do not contain useful information (e.g. ‘afterwards’, ‘however’, ‘yesterday’) and are trivial for the analysis and thus ignored by the text-mining algorithms. Other common terms, such as prepositions, articles, common verbs, and adjectives, are included in stop lists. In contrast, a start list contains words that are to be included in the analysis. When using start lists, only the terms in the start list are considered in the analysis. These lists are suitable when analysing documents with technical language or where the focus is on a specific domain. Start and stop lists can be used together. A default stop list can be used to generate word frequencies in the corpus. Domain experts can then identify the terms that are relevant to the analysis. Once all the relevant terms have been identified, the resulting list can be used as a custom start list.

Next, we performed word stemming, which is a standard practice in natural language processing. Porter’s algorithm for stemming (Porter, 1980) is one of the most widely used and accepted stemming algorithms, and we employ it in this research. All derived forms of a word are attributed to a single stem. For example, the words ‘start, starts, started, starting’ can all be derived from the same stem word. 'start'. Word stemming can also cover terms rather than just single words (e.g. ‘start process’ and ‘starts process’) if used as a word group. A synonym list can be created that identifies similar word groups. This action also allows for domain-specific verbiage, such as equating ‘denial of service’ with ‘DOS’.

Table 1 Emergent taxonomy of PII breaches

<table><tr><td>Cluster</td><td>%age</td><td>Number of breaches</td><td>Terms</td><td>Label</td></tr><tr><td>1</td><td>9.6</td><td>429</td><td>+ School + security + student + university current faculty social staff students + server ‘social security’ + computer ‘personal information’ posted personal</td><td>Threats to educational data</td></tr><tr><td>2</td><td>11.9</td><td>534</td><td>‘Credit card information’ ‘credit card numbers’ + breach + card + credit + customer + expiration + payment cards charges compromised credit customers debit fraudulent</td><td>Threats to financial data</td></tr><tr><td>3</td><td>26.6</td><td>1195</td><td>‘Email addresses’ + breach accessed email hackers online passwords posted unauthorised + account affected accounts exposed + company + number</td><td>Threats to user account data</td></tr><tr><td>4</td><td>5.7</td><td>256</td><td>‘Health information’ + ‘patient information’ + burglary + car + laptop + office + theft exposure health information patient patients protected resulted stolen</td><td>Threats to health data</td></tr><tr><td>5</td><td>11.5</td><td>516</td><td>‘Dates of birth’ + ‘medical record’ + ‘patient information’ + birth + centre + hospital + patient + record dates health insurance medical patient patients records</td><td>Threats to medical data</td></tr><tr><td>6</td><td>8.4</td><td>379</td><td>+‘Identity theft’ + fraud + identity + theft charged charges dishonest fraudulent guilty prison sentenced years accounts + update + employee</td><td>Threats to data potentially leading to identity theft and fraud</td></tr><tr><td>7</td><td>22.1</td><td>994</td><td>‘Personal information’ ‘social security’ + car + employee + laptop + office + security contained containing current documents employees files found included</td><td>Threats to sensitive data residing on portable computing devices</td></tr><tr><td>8</td><td>4.1</td><td>186</td><td>+‘Flash drive’ + ‘hard drive’ + drive + hard drives flash lost missing contained current + computer containing social stolen employees</td><td>Threats to sensitive data residing on portable storage devices</td></tr></table>

+ = word stemming.

Following the stemming, we then created a term-byterm or word frequency matrix (WFM) based on the individual word counts. This matrix was improved by utilising weight functions for word occurrences. The weight is a statistical measure of the significance of a word in a document or in an entire corpus. To avoid any bias towards larger documents, we used this process to normalise the reports for document size. Of the several available weighting methods that adjust the weights to the frequency of word occurrences, we used an entropy weight system for weight assignment (Raja & Tretter, 2011).

Given the size of the corpus acquired from the PRC, the resulting WFM was very large. Thus, the technique of latent semantic indexing (LSI) was used to reduce the dimensionality of the WFM. LSI is used to transform a matrix into a lower-dimensional form (Berry & Browne, 2005) by using singular value decomposition (SVD) for dimensionality reduction. SVD preserves the original information and transforms the term-document matrix to reduce the dimensionality. An SVD projection is a linear combination of the values in a row or column of the WFM. Decomposition of the matrix into eigenvalues and eigenvectors creates linearly independent components of the data (Deerwester et al, 1990). The SVD terms were generated and sorted in the order of significance. We then performed a cluster analysis of these SVD terms to extract knowledge from our large data set (McCallum et al, 2000) through an entropy minimisation algorithm, which was deemed the most suitable for SVD clustering (Li & Qin, 2017; Tremblay et al, 2009; Wang et al, 2013).

Starting with the default maximum number of 40 clusters in SAS Text Miner, the results were analysed. During this preliminary analysis, no more than ten clusters emerged. For further refinement of the results, a feature of the SAS software was employed that creates start and stop lists through an interactive analysis of the preliminary results. This interactive analysis of the clusters was used to identify irrelevant terms affecting the clustering. During this iterative process, some wellformed clusters emerged, while others were not clustering cleanly.

Investigating the descriptive terms provided insight into clustering anomalies. First, the inclusion of rare terms was influencing the clustering results. Second, misspellings within the corpus were also a cause of clustering problems. Thus, a labour-intensive selection of relevant terms was required. This selection effort minimised noise while ensuring the integrity of the analysis.

The expectation maximisation method, used for clustering, estimates the mean vectors and the covariance matrices of the distributions of the number of clusters, and several iterations with this technique led to the optimal solution (Wang et al, 2013). Although all the breach reports were from a single repository, the domain, nature, and reporting mechanism varied. Thus, there was a resulting variation in the nature, frequency, and style of PII-breach reports. The number of resulting clusters, along with the significant terms within each, is displayed in Table 1. The key descriptive terms are simple descriptions of the clusters and can be used to label the categories. However, these key terms alone cannot be used to categorise a new incoming PII-breach report. Rather, a mathematical weight that is assigned to the terms and patterns of the various terms determines how a new report would be categorised.

The labels assigned were based on the representative descriptive terms, and they have no statistical meaning regarding the taxonomy itself. However, labelling allowed us to characterise the breaches that fall into each category. To validate the labels given to each cluster, we sought the assistance of a chief information security officer (CISO) at a large US university who had over 20 years’ professional experience in the information protection and security domain. Additionally, this individual holds both the Certified Information Systems Security Professional (CISSP) and Certified Information Systems Auditor (CISA) credentials. Several conversations occurred between the researchers and the CISO to hone in on the best labels associated with the key terms for each cluster. To further validate the labelling of the clusters, we conducted another test where we provided the identified labels and clusters to another information security professional. This person has over 20 years of experience in designing and implementing internal and external security measures, has served as chief technology officer (CTO) for three different organisations, holds a Certified Computer Forensic Examiner (CCFE) certification from the Information Assurance Security Review Board (IACRB), and is qualified as a court-accepted expert witness for computer forensics. After reviewing the identified clusters and corresponding labels, this person believed that the labels accurately reflected the clustered terms.

Interestingly, the first six clusters focus on PII breaches related to sensitive data on traditional, immobile computing devices within organisational walls. On the other hand, the last two clusters represent PII breaches related to private data on more contemporary, mobile storage devices that can be introduced into or removed from organisational premises rather easily. Also of interest is the difference between clusters 4 and 5 (i.e. threats to health data and threats to medical data, respectively).<sup>1</sup> Though the differentiation might initially seem negligible, it is quite substantial. In the medical field, a medical record is a container for data regarding a patient’s single visit to a physician, whereas a health record is a compilation of many previously created medical records. Specifically, the medical records are the entries created during patients’ individual appointments, which are then often submitted by personnel to insurance companies for financial reimbursement, whereas health records are typically entire dossiers regarding a single patient’s health over a specified period.

We believe our approach’s ability to mathematically classify these seemingly similar breach types into distinct categories is an important benefit. It is important to note that a breach announcement is a single point in the taxonomy domain space. Accordingly, the breach type’s assignment to a particular cluster depends on its distance to the various clusters. Thus, a single breach may reside between two cluster boundaries, but because it is a bit closer to one instead of another (due to lexical similarities), it will be assigned to the first rather than the second although it still has some similarities with the second.

As an example, one breach report might state ‘Company ABC reported yesterday that an employee left a laptop in a car, and the laptop was stolen’, whereas another might read ‘Hospital XYZ reports today that one of their nurses took a laptop without authorisation from the building premises. The laptop was stolen from the employee’s automobile. The laptop contained information about patients’ health records, including data about immunisations, known diseases, current medications and other sensitive information. The number of records breached is estimated to be 30,000’. Both examples share similarities, but the second is much more specific to the industry. Thus, the more specific the information in the breach announcement was, the more likely the breach would be assigned to one of the less general clusters, hence why these breaches would likely be assigned to different clusters in our taxonomy. Unfortunately, we could not control the level of specificity provided in the breach reports. However, despite similarities among the clusters and breaches, the cluster analysis classifies each breach into one cluster only. For example, clusters 4 and 7 both include the term ‘laptop’. This is because an incident involving a lost or stolen laptop can be a threat to health data or to sensitive data residing on portable computing devices. However, our approach indicates that threats to health data, regardless of the media, differ from other threats to portable computing devices, thus resulting in the emergence of two distinct clusters. The emergent taxonomy of PII breaches is depicted in Table 1.

As shown in Table 1, in the PRC data set, threats to user account data is the leading category of PII breaches (over one-quarter of the breaches), followed closely by threats to sensitive data residing on portable computing devices. The results also indicate the presence of attacks against educational-, financial-, and health-related data, as well as threats to PII data for identity theft and fraud purposes. In addition, as stated earlier, some breaches can be attributed to the availability of portable storage media devices. Malicious insiders can threaten these portable storage media devices through their inappropriate use, or well-meaning employees might inadvertently lose the devices or have them stolen.

To further validate the diversity among the PII-related breaches, we conducted literature reviews for each resulting cluster. The goal was to verify that these clusters each represent individual streams of existing research and to uncover the significant research gaps existing within each cluster. The full results of our initial literature review are available in Online Appendix B. Table 2 summarises this literature to demonstrate the similarities and differences across the clusters. Although there are some similarities in the research being conducted in each cluster, each cluster is being researched from different perspectives. Such findings further validate the uniqueness of each cluster that emerged from the text analysis.

Table 2 Distinct research topics by cluster

<table><tr><td>Cluster</td><td>Current research topic</td><td>Examples of related articles</td></tr><tr><td>Cluster 1: Threats to educational data</td><td>Educational institutions compliance with legal mandates (e.g. FERPA, US Patriot Act)Effective information security and privacy pedagogyStudents&#x27; use of social media and electronic forms of communicationEfficacy of privacy notices displayed on university websites</td><td>Daggett (2008), Humphries (2008), Nicholson and O&#x27;Rearson (2009), Young (2015)Harris et al (2011), Hoffman et al (2005) and Meso et al (2013)Chai et al (2006), Kurkovsky and Syta (2011) and Mensch and Wilkie (2011)Culnan and Carlin (2009)</td></tr><tr><td>Cluster 2: Threats to financial data</td><td>Liability to consumers for credit card breachesLiability to companies for breachesBreach notification lawsCorporate governanceInvestigation of individual (high-profile) breach events (e.g. TJMaxx and Target)Novel approaches to safeguarding financial data (e.g. information policies and technical solutions)Organised crime and the dark web</td><td>Gerard et al (2005b) and Pinson (2007)Black (2013) and Hanson (2008)Faulkner (2007), Picanso (2006)Trautman and Altenbaumer-Price (2010)Berg et al (2008), Gray and Ladig (2015), Tipton and Choi (2014) and Xu et al (2008)Barker et al (2008), Beales and Muris (2008), Elson and LeClerc (2006), Gray and Ladig (2015) and Upendar and Rao (2013)Ben-Itzhak (2009), Kim et al (2011) and Peretti (2008)</td></tr><tr><td>Cluster 3: Threats to user account data</td><td>Black market for user dataIndividuals&#x27; password creation, storage, and maintenance behavioursHacking techniques (e.g. doxing, phishing, hijacking)Privacy threats in the cloud</td><td>Ablon et al (2014), Tuttle (2015)Ayyagari and Tyks (2012), Bishop and Klein (1995), Furnell (2014), Ives et al (2004) and Zviran and Haga (1999)Alim et al (2011), Beye et al (2012), Engebretson et al (2013), Podhradsky et al (2013) and Wang and Nepali (2015)Ion et al (2011), Krutz and Vines (2010), Mather et al (2009), Pearson (2009) and Ranchal et al (2010)</td></tr><tr><td>Cluster 4: Threats to health data</td><td>Descriptive research regarding hacking attacks and individual privacy breachesTechnical solutions (e.g. encryption and policy)Managerial solutions (e.g. organisational policy)</td><td>Ayyagari (2012) and Chang (2013)Blanke and McGrady (2016)Fathima and Ahmed (2013)</td></tr><tr><td>Cluster 5: Threats to medical data</td><td>Adoption and implementation of electronic medical recordsIndividuals&#x27; use of personal medical recordsPersonally controlled online medical dataGrounded theory approaches to balance effectiveness and unintended consequences of privacy safeguards</td><td>Harrison et al (2007)Halamka et al (2008) and Tang et al (2006)Steinbrook (2008)Parks et al (2016)</td></tr><tr><td>Cluster 6: Threats to identity theft and fraud</td><td>Individuals&#x27; proneness to identity theftIdentity theft regulationsUnderstating the mindset of identity thievesInternal control frameworks to control identity theftOrganisational differences relating to identity theft occurrence</td><td>Hedayati (2012)Kim et al (2011)Copes and Vieraitis (2009)Gerard et al (2005a)Kim (2015)</td></tr><tr><td>Cluster 7: Threats to sensitive data on portable computing devices</td><td>Distinguishing between technology as the target and data as the target for stolen devicesUsing log data to understand the use of stolen devicesDistinguishing threats of mobile and stationary computing devices</td><td>Cate et al (2009)Dimkov et al (2010)French and Shropshire (2011)</td></tr><tr><td>Cluster 8: Threats to sensitive data on portable storage devices</td><td>Lost or stolen portable storage devices (e.g. USB-enabled devices)Portable storage devices as the delivery mechanism of the threat (e.g. malware)Portable device as mechanism for data exfiltration (e.g. &#x27;pod slurping&#x27; or &#x27;slurping&#x27; for short)Data remanence (i.e. digital data that resides on storage devices even after attempts to remove such data are made)</td><td>Van Wijk and Holmes (2007)Abraham and Chengalur-Smith (2010) and Pham et al (2011)Verma and Singh (2012)Chaerani et al (2011), Sansurooah and Szewczyk (2012).</td></tr></table>

![](/api/attachments/7DXXMT87/fulltext/images/192d77bff531b901957bf02ffaea7894ec9b721bd5b1df2c3975ec257bd1a789.jpg)  
Figure 3 Cluster 1 normalised breach-event occurrence.

## Taxonomy assessment

Our analysis classified and assigned each PII breach to one of eight clusters. Following these assignments, we assessed whether variation existed across the individual states for each PII cluster. Again, we want to stress that the label of each cluster is based on the terms appearing in the textual terms that are significant in that cluster; they have no other statistical impact on the analysis.

Previous researchers found a significant relationship between state-level laws and data-breach risk in the USA for organisations within certain industries (i.e. financial, educational, medical, and the non-government sector) (Sen & Borle, 2015). Extending this previous work, we performed a state-level examination of the identified threat clusters that emerged from our text-mining and clustering efforts. Figures 3, 4, 5, 6, 7, 8, 9, and 10 show the geographical distribution of each PII-breach type across the USA. The darker the state, the greater the actual number of breach events for that state relative to the others. As in Figures 1 and 2, data for Figures 3, 4, 5, 6, 7, 8, 9, and 10 were normalised for state-level GDP. Also, as mentioned earlier, we normalised the breach events by figures other than state-level GDP. These additional results are in Online Appendix A.

Basic analysis of the various figures shows some interesting findings. Vermont, Montana, and Nebraska appear to suffer more from attacks on educational data, whereas threats to financial data seem to be focused on Vermont, New Hampshire, and Maine. Threats to user account data was widely dispersed, having only a few focused areas. However, significantly more ‘hot spots’ appear with health- and medical-related data threats. For example, Oregon, North Dakota, Georgia, Kentucky, Indiana, and Vermont were highlighted in cluster 4, and Figure 7 highlights Montana, Colorado, Alaska, Tennessee, and New Hampshire. Identity theft events were more pronounced in Alabama, Florida, and Vermont. Finally, threats to data residing on portable computing devices were dispersed, but threats to data residing on portable storage devices were seen more in Idaho, Colorado, Kentucky, Ohio, Maryland, and Vermont. For additional information about these dispersions, see Appendix A.

Although graphical depictions provide basic insight into potential issues, it is impossible to state whether the differences among the states are statistically significant. For this purpose, we utilised simple z-score calculations to determine how many standard deviations a state is from the mean across all states on the normalised breach events. Given that the data were skewed, a natural log transformation of the normalised breach-event data was performed such that they could be assessed through traditional methods. One result was that across all breaches, the District of Columbia (z = -3.154) and Vermont (z = -2.874) performed significantly worse (a = 0.05) than the USA as a whole, whereas North Dakota (z = 2.320) and Wyoming (2.384) performed significantly better. The statistically significant (a = 0.05) results for the individual clusters using the data normalised by GDP were as follows: (1) educational data: top – Washington; bottom – Vermont and Montana; (2) financial data: top – Louisiana; bottom – Vermont; (3) user account data: top – none; bottom – District of Columbia and Vermont; (4) health data: top – Michigan; bottom – none; (5) medical data: top – New Jersey and Nebraska; bottom – none; (6) identity theft:

![](/api/attachments/7DXXMT87/fulltext/images/123b1b0f7120292c6fb5913e9567101dc78d1ffa648b7adf5d0b9bacd9a1eafb.jpg)  
Figure 4 Cluster 2 normalised breach-event occurrence.

![](/api/attachments/7DXXMT87/fulltext/images/e0e724dffb06bc2b27de948e057fc47b1c1b28acece3fb1cabe47bf759c87301.jpg)  
Figure 5 Cluster 3 normalised breach-event occurrence.

top – none; bottom – Vermont and Alabama; (7) portable computing: top – Mississippi and Alaska; bottom – District of Columbia; (8) portable storage: top – Wisconsin; bottom – none. The complete analysis results for all the zscore assessments are in Appendix A.

Next, for a more in-depth analysis of organisational exposure to PII threats, we examined the distribution of PII-breach events across various organisational types for

![](/api/attachments/7DXXMT87/fulltext/images/9525843b30dc7bede79657e414fb679600b2808952b1c85c9864f32320b1ec2a.jpg)  
Figure 6 Cluster 4 normalised breach-event occurrence.

![](/api/attachments/7DXXMT87/fulltext/images/12ea0c980b7278606a94f5be87a59ebdd668abf9cbe33908012580df63c472c5.jpg)  
Figure 7 Cluster 5 normalised breach-event occurrence.

each cluster type identified by the taxonomy. These main organisational classifications were provided by PRC and provide a way to help cross-validate our classification taxonomy. This assessment is provided in Table 3. As shown in Table 3, the dispersion for PII breaches within our taxonomy was uneven across some organisationa types, whereas some breach types were fairly well dispersed. Attacks on educational data (i.e. cluster 1) were heavily centralised within educational institutions (i.e. 95% concentration), which is to be expected. In similar fashion, the vast majority of PII breaches regarding sensitive health and medical data (i.e. clusters 4 and 5) targeted healthcare and medical institutions, and retail and merchant businesses experienced the brunt of PII breaches related to attacks on financial data (i.e. cluster 2). Also expected, there was a fairly even distribution of threats to user account data (i.e. cluster 3) among all organisational types, whether public or private.

![](/api/attachments/7DXXMT87/fulltext/images/11111026b2c60fd5f5891385ba8f6b3f999bc168ba9ba6d1a442f2d5b6ff8f27.jpg)  
Figure 8 Cluster 6 normalised breach-event occurrence.

![](/api/attachments/7DXXMT87/fulltext/images/df226e9c946aab62b26e79dbd2b65a42c8487623615e93610a2565e791dbcab8.jpg)  
Figure 9 Cluster 7 normalised breach-event occurrence.

Privacy breaches potentially leading to identity theft and fraud, the theft or loss of portable computing devices, and the utilisation or loss of portable storage devices (i.e. clusters 6, 7, and 8, respectively) show some interesting patterns. All three had relatively decent dispersions across the organisational types identified by the PRC; however, identity theft and fraud-related attacks focused on the healthcare and medical institutions, whereas PII breaches due to theft or loss of computing devices occurred more frequently in government and military organisations. Educational, government, and military and healthcare and medical institutions suffered a similar number of breaches from use or loss of portable device drives, such as USB and external hard drives. Interestingly, with so much emphasis on bringyour-own-device policies and procedures within organisations (Crossler et al, 2014; French et al, 2014; Jaramillo et al, 2013), over 26% of the PII-related breaches focused on sensitive data residing on portable computing devices and storage media.

![](/api/attachments/7DXXMT87/fulltext/images/444cbb0e58c3abf6ffee8e443a9cc5bdec81e082dd351431cdfdf776c33ee8d8.jpg)  
Figure 10 Cluster 8 normalised breach-event occurrence.

Given the above information and despite some variance, these results show the relative stability of the taxonomy and its eight PII-breach clusters. Although the taxonomy was created completely based on the textual content of the reports provided by PRC and no other variables were used while assigning the categories, the results clearly indicate that the textual content is a stable mechanism for classification of historical breaches, as well as breaches that will occur in the future.

As a final assessment of our taxonomy with respect to how the eight different PII-breach types impacted organisations, we evaluated whether the breach types differed statistically in the number of records affected. For this purpose, we performed a one-way analysis of variance (ANOVA) test on the 2,264 events, providing an estimate for the number of records breached. The data were non-normally distributed; however, the distribution indicated that a natural log transformation could be useful. Therefore, we transformed the number of records affected using the ln(num of records), and the resulting distribution was near normal. Finally, we assessed the homogeneity of the variances using Levene’s test, which revealed a lack of variance homogeneity (p \ 0.001). For this purpose, a Welch’s test was conducted instead of the regular ANOVA test (Asiribo &

Gurland, 1990; Brown & Forsythe, 1974a, b; Welch, 1951). The Welch statistic indicated significant differences in the number of records breached across the clusters identified by the taxonomy $( F = 4 . 8 9 5 , d f = 7 ,$ df den = 584.5, p \ 0.0001). Table 4 shows the descriptive statistics for the transformed data.

To determine which clusters are statistically different from one another regarding their impact, we performed a Tukey–Kramer HSD test. The ordered-difference report displays the difference between PII breaches’ impact across the clusters in pairwise fashion. Only comparisons exhibiting a statistically significant difference are shown in the report. According to this analysis, seven comparisons exhibited significant differences in their impacts (i.e. number of records affected), with attacks on websites for user account information exhibiting the largest difference with attacks potentially leading to identity theft and/or fraud. In other words, this analysis provides evidence that, on average, all PII-breach types are not equal in the harm caused to organisations. The results are displayed in Table 5.

## Discussion

Our research is among the first to provide a formal, datadriven classification system for one of the most contentious outcomes of increased personal information collection – threats to confidentiality generally and PII specifically. As mentioned earlier, formal taxonomic efforts fulfil the first of two requirements of systematics research (i.e. the science of diversity) (McKelvey, 1978, 1982). Only after a domain has been examined and the various relevant members identified can researchers adequately ascertain the factors affecting those individual components within the domain (i.e. the science of universals). Therefore, the results from this research provide a classification system that provides the requisite foundation from which future research can explore PII breaches, as well as understand why discrepancies exist among them through the development and extension of theory. Through the literature review presented in Table 2, researchers can begin the process of understanding why breaches occur by drawing on the research in other clusters and applying them to different contexts. Doing so will provide the theoretical underpinning necessary to further understand why these various types of breaches occur.

Table 3 PII-breach events by organisational type

<table><tr><td rowspan="2">Major PRC classifications</td><td colspan="9">Clusters</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>Total</td></tr><tr><td>Businesses – financial and insurance services</td><td>2</td><td>64</td><td>239</td><td>13</td><td>5</td><td>71</td><td>186</td><td>12</td><td>592</td></tr><tr><td>Businesses – other</td><td>2</td><td>124</td><td>244</td><td>10</td><td>3</td><td>36</td><td>166</td><td>18</td><td>603</td></tr><tr><td>Businesses – retail/merchant</td><td>0</td><td>272</td><td>121</td><td>8</td><td>1</td><td>47</td><td>86</td><td>6</td><td>541</td></tr><tr><td>Educational institutions</td><td>406</td><td>29</td><td>120</td><td>8</td><td>14</td><td>20</td><td>105</td><td>43</td><td>745</td></tr><tr><td>Government and military</td><td>13</td><td>21</td><td>241</td><td>11</td><td>19</td><td>67</td><td>280</td><td>47</td><td>699</td></tr><tr><td>Health care – medical providers</td><td>5</td><td>14</td><td>195</td><td>201</td><td>471</td><td>131</td><td>132</td><td>56</td><td>1205</td></tr><tr><td>Non-profit organisations</td><td>1</td><td>10</td><td>35</td><td>5</td><td>3</td><td>7</td><td>39</td><td>4</td><td>104</td></tr><tr><td>Total</td><td>429</td><td>534</td><td>1195</td><td>256</td><td>516</td><td>379</td><td>994</td><td>186</td><td>4489</td></tr></table>

Table 4 Descriptive statistics by cluster

<table><tr><td>Clusters</td><td>Count</td><td>Mean ln(recs)</td><td>Std error</td><td>Lower 95%</td><td>Upper 95%</td></tr><tr><td>1</td><td>330</td><td>7.9076</td><td>0.1592</td><td>7.5954</td><td>8.2198</td></tr><tr><td>2</td><td>225</td><td>7.3075</td><td>0.1928</td><td>6.9294</td><td>7.6857</td></tr><tr><td>3</td><td>489</td><td>8.3797</td><td>0.1307</td><td>8.1235</td><td>8.6360</td></tr><tr><td>4</td><td>73</td><td>7.9032</td><td>0.3385</td><td>7.2394</td><td>8.5671</td></tr><tr><td>5</td><td>223</td><td>7.7655</td><td>0.1937</td><td>7.3857</td><td>8.1454</td></tr><tr><td>6</td><td>227</td><td>7.1161</td><td>0.1920</td><td>6.7396</td><td>7.4926</td></tr><tr><td>7</td><td>585</td><td>8.0356</td><td>0.1196</td><td>7.8011</td><td>8.2701</td></tr><tr><td>8</td><td>112</td><td>8.3515</td><td>0.2733</td><td>7.8156</td><td>8.8875</td></tr></table>

Table 5 Ordered-difference report from Tukey–Kramer HSD test

<table><tr><td>Cluster</td><td>Cluster</td><td>Diff</td><td>Std err diff</td><td>Lower CL</td><td>Upper CL</td><td>p value</td></tr><tr><td>3</td><td>6</td><td>1.2636</td><td>0.2322</td><td>0.5591</td><td>1.9681</td><td>0.000</td></tr><tr><td>8</td><td>6</td><td>1.2354</td><td>0.3340</td><td>0.2222</td><td>2.2486</td><td>0.005</td></tr><tr><td>3</td><td>2</td><td>1.0722</td><td>0.2329</td><td>0.3656</td><td>1.7788</td><td>0.000</td></tr><tr><td>8</td><td>2</td><td>1.0440</td><td>0.3345</td><td>0.0293</td><td>2.0587</td><td>0.039</td></tr><tr><td>7</td><td>6</td><td>0.9195</td><td>0.2262</td><td>0.2334</td><td>1.6057</td><td>0.001</td></tr><tr><td>1</td><td>6</td><td>0.7915</td><td>0.2494</td><td>0.0349</td><td>1.5481</td><td>0.033</td></tr><tr><td>7</td><td>2</td><td>0.7281</td><td>0.2269</td><td>0.0398</td><td>1.4164</td><td>0.029</td></tr></table>

We also found initial evidence of the dispersion of the eight different PII-breach types across organisational types within the USA. One very interesting finding was the sheer amount of PII threats that emerged from the theft or loss of portable computing or storage devices (clusters 7 and 8, respectively). When combined, these threats comprised over 26% of all attacks on PII, almost the same number as attacks on websites for user account information (cluster 3), which accounted for the highest number of PII attacks among the identified clusters. Additionally, these device-based attacks were well dispersed across all organisational types. These findings provide evidence of the need to better understand the role that individual users (i.e. insiders) play in the organisational protection of sensitive information. Although many breaches are the result of lost laptops, the importance of research in this area increases as more information becomes accessible on smaller mobile devices and as organisations begin to formulate and implement BYOD policies. As organisations consider the types of breaches that affect them most often and the states in which they do business, they could begin targeting their training to combat these specific types.

Another major contribution of our research rests with the identification of target-rich environments for PII attacks. Although no organisation – public, private, or military – is immune to PII breaches, our findings indicate significant differences across the eight PII-breach categories. For the statistical analyses, the chosen technique required a natural log transformation of the number of records of breached data. However, the nontransformed data showed that the average number of records affected between the attacks on websites for user account information and attacks leading to identity theft and fraud is more than a sevenfold difference (2.8 million vs. 366,000, respectively). If the estimate of monetary loss per record breached (when 1,000 records are breached) is correct at US\$52 to US\$87 (Verizon, 2015), then the difference is an estimated US\$126 million to US\$211 million discrepancy.

Similarly, those responsible for deciding how to allocate scarce organisational resources to protect sensitive information across many threat vectors can now utilise the differences uncovered by our research to better justify certain expenditures in focused areas. For example, decision-makers in organisations responsible for the protection of medical data and who operate in the states of Montana, Colorado, Alaska, and Tennessee might find that additional expenditures on protective mechanisms are warranted. Likewise, our efforts provide a voice to those decision-makers whose responsibility it is to curb identity theft in Alabama and Florida when they request additional organisational resources to perform their duties.

Of additional note is that organisations in certain states industries are well poised to form collaborative task forces to combat various types of attacks. Some organisations fail to provide accurate or timely data-breach notifications because of potential negative repercussions in the media and the stock market, and that concern is not without merit. However, to alleviate some of this concern, our research provides evidence of commonalities within the PII-breach ecosystem – commonalities that can be used to foster collaboration. In other words, organisations and industries that are the least and most victimised by a specific threat stand to gain the most from concerted interaction. An organisation reaching out to another for assistance in how to best handle a breach when it occurs, as well as how to minimise subsequent attacks, is not necessarily commonplace. Fortunately, we see significant value in our results in that they can be used to direct the sharing of breach information and protective strategies. Moreover, we are hopeful such interaction will become standard given that several of the breach clusters were quite focused on critical infrastructures in the USA, which by definition must remain operational for citizens to go on with life as normal.

As a final discussion point, our post hoc analysis identified the types of PII attacks most likely to generate reports that have an estimated number of records breached. In general, around 50% of all the reported attacks did not contain any estimates of the potential number of records affected; however, the variance in this percentage differed across the PII-breach types. Specifically, the percentage of records within each PII-attack type ranged from

28.5% to over 76%. These percentages for each cluster in ascending order were as follows: health data (28.5%); user account data (40.9%); financial data (42.1%); medical data (43.2%); portable computing devices (58.9%); identity theft and fraud (59.9%); portable storage devices (60.2%); and educational data (76.9%). Thus, considerable variance exists among the likelihood of an estimated number of records affected accompanying the PII-breach report across the eight clusters, especially between the health and educational data contexts.

## Limitations and future research

As with most research dealing with real information threat incidents, a key limitation of this work is the reliance on the accuracy of the PII-breach data. Published breach announcements may be limited in number and accuracy in that governments, militaries, educational institutions, for-profit corporations, and so forth are likely hesitant to report accurate numbers about an information breach because of organisational leaders’ fear of potential backlash (Cavusoglu et al, 2004; Goel & Shawky, 2009; Kotulic & Clark, 2004). Additionally, many breached organisations and individuals may never discover the full extent of some breaches. Despite this potential deficiency within the data, our taxonomy is relatively robust to non-systematic underreporting in that we are not seeking to catalogue all extant breaches, but rather want to define the domain of organisational PII breaches via taxonomic methods using nearly 4,500 breach events over an entire decade. Nonetheless, it is important to note that our classification is based on breaches that are reported rather than all breaches that occur. Also, our methodology does not provide a tool for detecting PII breaches in the future, but rather, it offers the necessary underpinnings for a robust research programme into the understanding of breach incidents and differences in impact for PII breaches (i.e. number of records likely affected). Finally, the breach reports can be linked to the headquarters of an organisation because it is the organisation that reports the data breach. Thus, breach information may have affected individuals across the USA or the world but was only attributed to a particular state for our analysis.

Further, this research focused on breaches reported in the USA. In the USA, privacy is expected to be controlled, for the most part, by a free-market system where individuals’ expression of choice, through commerce, rewards organisations that protect privacy and punishes those that do not (Marotta-Wurgler, 2016). Whereas it is recognised that individuals have certain rights to privacy (e.g. in healthcare or public education), there is no comprehensive legal framework for privacy protections in the USA. However, differences in legal protections across industrialised nations have proven to be a significant issue for global commerce, whereby privacy rights and protections guaranteed to one constituency are attached to the information and, therefore, travel beyond the bounds of traditional legal jurisdiction (Shaffer, 2000). Given the importance of global data flows, particularly between the USA and Europe, mechanisms have been put in place to certify privacy protections across national boundaries (N Loideain, 2016). However, as they pertain to data flows across nations, these privacy standards do not apply to all organisations. Complicating the issue is the myriad of courts and constituencies involved in the establishment and enforcement of international standards (Ni Loideain, 2016; Tracol, 2016). Therefore, statutory differences and the overall approach to privacy across various countries might lead to differences in the type and scope of breach information reported.

It is also important to note that information security efforts within organisations target the concepts identified by the CIA triad. Specifically, information security comprises efforts to ensure the confidentiality, integrity, and availability of important and sensitive data, information, and associated systems. For the purposes of this research, we focus on those threats that would lead to a loss in confidentiality (i.e. privacy) only. Thus, organisationa efforts to ensure integrity and availability, although important, are beyond the scope of our efforts.

In the future, our methodology can also be used to assess the reportage of breach incidences. For example, where systematic underreporting of breaches is expected – whether by industry, organisational type, or attack cluster – our methodology may shed light on that phenomenon by comparing multiple sources of data. In this way, comparing the proportion of a breach type reported to some other benchmark may identify those breaches that are less likely to be reported. Moreover, our methodology is replicable and can be used to categorise and assess reported attacks beyond confidentiality to those targeting integrity (e.g. alteration of sensitive data) and availability (e.g. distributed denial-of-service attacks) within organisations. Future research can also use our methodology in classifying novel breaches that emerge in the future but are not yet experienced (or recognised) by organisations currently.

One opportunity of having a formal taxonomy of PII breaches based on the textual content is the ability to use it as an early warning system of the impact future breaches might have. Because many organisations are not able to adequately estimate the impact of breaches until in-depth investigative efforts have been completed, our taxonomy and the subsequent analyses provide a valuable tool to estimate potential harm early in the investigative process. From a monetary standpoint, it has been estimated that for a breach of 1,000 records, each record lost costs organisations from US\$52 to US\$87 (Verizon, 2015). If it can be established that the emergent text-based classification can indicate an attack’s impact based on the number of records potentially compromised and affected, future reports could be used as an early warning system. Because the taxonomy requires only a textual report, new breaches can be scored and classified into one of the categories, and an early estimate of the impact could be computed.

As a final recommendation for future research, we encourage an in-depth examination of whether, and if so how, state- and national-level legislation has affected organisations’ exposure to different forms of PII threats identified by our taxonomy. Our research highlights certain states whose organisations performed better or worse than organisations in other states, and these could serve as the starting points for such an investigation. Previous researchers found a significant relationship between state-level regulation and industry segment for data-breach risk (Sen & Borle, 2015). Our research provides a significant extension of this prior work by examining the risk from specific threats, not simply in the industry, but for individual states. We urge researchers to delve into the content of state-level regulations<sup>2</sup> to compare how different types of organisations have responded and whether those responses have any association with the eight major types of PII breaches discovered in our study. In this way, the individual states can leverage their potential as ‘states as laboratories’ (Gardner, 1996). In fact, we believe there are some fundamental advantages to the free-market solution to privacy concerns, and future research should examine and compare the level of breaches for organisations covered by the EU Privacy Shield and those not covered, both in the USA and globally. Because of the contextual nature of privacy, future research should also examine how cultural and demographic characteristics, whether local, national, or even corporate, might also show important relationships with the breach data across our classification system.

## Conclusion

Organisations in the USA reported experiencing around 4,500 unique breaches of sensitive and private information between 2005 and 2015. We examined these breaches by first creating a formal taxonomy using textmining and cluster analysis techniques and then assessing how organisations within each state fared relative to each PII-breach cluster identified by our classification system. Although organisations in some states might be more likely to succumb to an attack on the PII they use, store, or disseminate, organisations in others are likely to endure more severe attacks (i.e. number of records affected) when an attack is successful. Both researchers and industry professionals can use our findings to better understand the types of attacks possible on PII within organisations and to assess the reasons why discrepancies exist among the types of attacks and the organisations that experience them.

<sup>2</sup>The National Conference of State Legislatures (www.ncsl.org) provides information on breach notification laws by state. As of the writing of this manuscript, 47 states and the District of Columbia have enacted breach notification legislations.

## About the Authors

Clay Posey is an Associate Professor of Management with a joint appointment in the Institute for Simulation & Training at University of Central Florida. His research has appeared in various journals including MIS Quarterly, Journal of Management Information Systems, European Journal of Information Systems, and Information & Management, among others.

Uzma Raja is Professor of MIS at the University of Alabama. She received her PhD from Texas A&M University. Her research area is systems evolution, text mining, and open source ecosystems. She has published in journals such as IEEE Transactions on Software Engineering, Decision Sciences, and IIE Transactions.

## References

ABLON L, LIBICKI MC and GOLAY AA (2014) Markets for cybercrime tools and stolen information: Hackers’ Bazaar. RAND Corporation. [WWW document] http://www.rand.org/content/dam/rand/pubs/research\_ reports/RR600/RR610/RAND\_RR610.pdf (accessed 10 October 2016).

ABRAHAM S and CHENGALUR-SMITH I (2010). An overview of social engineering malware: trends, tactics, and implications. Technology in Society 32(3), 183–196.

ALIM S, NEAGU D and RIDLEY M (2011). Axioms for vulnerability measurement of online social network profiles. In International Conference on Information Society (i-Society), pp 241–247, IEEE, London.

ASIRIBO O and GURLAND J (1990) Coping with variance heterogeneity. Communications in Statistics-Theory and Methods 19(11), 4029–4048.

A P (2016) Data breaches up 15% to date in 2016. [WWW document] http://247wallst.com/technology-3/2016/09/09/data-breaches-up-15- to-date-in-2016/ (accessed 15 September 2016).

AYYAGARI R (2012) An exploratory analysis of data breaches from 2005–2011: trends and insights. Journal of Information Privacy and Security 8(2). 33–56.

AYYAGARI R and TYKS J (2012) Disaster at a university: a case study in information security. Journal of Information Technology Education 11, 85–96.

BARKER KJ, D’AMATO J and SHERIDON P (2008) Credit card fraud: Awareness and prevention. Journal of Financial Crime 15(4), 398–410.

BASKERVILLE R, SPAGNOLETTI P and KIM J (2014) Incident-centered information security: managing a strategic balance between prevention and response. Information & Management 51(1), 138–151.

BEALES JH and MURIS TJ (2008) Choice or consequences: Protecting privacy in commercial information. The University of Chicago Law Review 75(1), 109–135.

BE´LANGER F and CROSSLER RE (2011) Privacy in the digital age: a review of information privacy research in information systems. MIS Quarterly 35(4)1017-1041

BEN-ITZHAK Y (2009) Organised cybercrime and payment cards. Card Technology Today 21(2), 10–11.

BERG GG, FREEMAN MS and SCHNEIDER KN (2008) Analyzing the TJ Maxx data security fiasco: lessons for auditors. The CPA Journal 78(8), 34–37.

BERRY MW and BROWNE M (2005) Email surveillance using non-negative matrix factorization. Computational & Mathematical Organization Theory 11(3), 249–264.

B M, J AJ, E Z, H P, L RL and T Q (2012) Privacy in online social networks. In Computational Social Networks (A A, Ed), pp 87–113, Springer, London.

BISHOP M and KLEIN DV (1995) Improving system security via proactive password checking. Computers & Security 14(3), 233–249.

Robert E. Crossler is an Assistant Professor of Information Systems at Washington State University. His research has been published in leading MIS journals, including MIS Quarterly, Decision Support Systems, and The DATA BASE for Advances in Information Systems, where his manuscript on privacy was recognised as best paper in 2014.

A. J. Burns is an Assistant Professor in the College of Business and Technology at the University of Texas at Tyler. He earned his DBA in Computer Information Systems from Louisiana Tech University. His research interests include behavioural cybersecurity, complex adaptive systems, and health information security and privacy.

BLACK J (2013) Developments in data security breach liability. The Business Lawyer 69, 199–206.

BLANKE SJ and MCGRADY E (2016) When it comes to securing patient health information from breaches, your best medicine is a dose of prevention: A cybersecurity risk assessment checklist. Journal of Healthcare Risk Management 36(1), 14–24.

BRANN M and MATTSON M (2004) Toward a typology of confidentiality breaches in health care communication: an ethic of care analysis of provider practices and patient perceptions. Health Communication 16(2), 231–251.

BROWN MB and FORSYTHE AB (1974a) The ANOVA and multiple comparisons for data with heterogeneous variances. Biometrics 30(4), 719–724.

B MB and F AB (1974b) Robust tests for the equality of variances. Journal of the American Statistical Association 69(346), 364–367.

BURNS AJ, YOUNG JA, ROBERTS TL, COURTNEY JF and ELLIS TS (2015) Exploring the role of contextual integrity in electronic medical record (EMR) system workaround decisions: an information security and privacy perspective. AIS Transactions on Human-Computer Interaction 7(3), 142–165.

CATE FH. ABRAMs ME. BRUENING PL and SwINDLF O (2009) Dos and don'ts of data breach and information security policy. Articles by Maurer Faculty. [WWW document] http://www.repository.law.indiana.edu/facpub 234 (accessed October 10. 2016).

CAVUSOGLU H, MISHRA B and RAGHUNATHAN S (2004) The effect of Internet security breach announcements on market value: capital market reactions for breached firms and Internet security developers. International Journal of Electronic Commerce 9(1), 70–104.

CHAERANI W, CLARKE N and BOLAN C (2011) Information leakage through second hand USB flash drives within the United Kingdom. In Australian Digital Forensics Conference, Perth Western Australia.

C S, B -S S, M C, R H and U S (2006) Role of perceived importance of information security: an exploratory study of middle school children’s information security behavior. Issues in Informing Science and Information Technology 3, 127–135.

CHANG JL (2013) The dark cloud of convenience: how the HIPAA omnibus rules fail to protect electronic personal health information. Loyola of Los Angeles Entertainment Law Review 34(2), 119–154.

C H and V LM (2009) Bounded rationality of identity thieves: using offender-based research to inform policy. Criminology & Public Policy 8(2), 237–262.

C RE, J AC, L PB, H Q, W M and B R (2013) Future directions for behavioral information security research. Computers & Security 32(1), 90–101.

CROSSLER RE, LONG JH, LORAAS TM and TRINKLE BS (2014) Understanding compliance with bring your own device policies utilizing protection motivation theory: bridging the intention-behavior gap. Journal of Information Systems 28(1), 209–226.

CULNAN MJ and CARLIN TJ (2009) Online privacy practices in higher education: Making the grade? Communications of the ACM 52(3), 126–130.

D’ARCY J, HERATH T and SHOSS MK (2014) Understanding employee response to stressful information security requirements: A coping perspective. Journal of Management Information Systems 31(2), 285–318.

DAGGETT LM (2008) FERPA in the twenty-first century: Failure to effectively regulate privacy for all students. Catholic University Law Review 58, 59–114.

DAVIS JH (2015) Katherine Archuleta, Director of Personnel Agency, Resigns. The New York Times. [WWW document] http://www. nytimes.com/2015/07/11/us/katherine-archuleta-director-of-officeof-personnel-management-resigns.html?\_r=0 (accessed 22 January 2016).

DEERWESTER S, DUMAIS ST, FURNAS GW, LandAUER TK AND HARSHMAN R (1990) Indexing by latent semantic analysis. Journal of the American Society for Information Science 41(6), 391–407.

DHILLON G and TORKZADEH G (2006) Value-focused assessment of information system security in organizations. Information Systems Journal 16(3), 293–314.

DIMKOV T, PIETERS W and HARTEL P (2010) Effectiveness of physical, social and digital mechanisms against laptop theft in open organizations. In Green Computing and Communications (GreenCom), 2010 IEEE/ACM Int’l Conference on & Int’l Conference on Cyber, Physical and Social Computing (CPSCom), pp 727–732, IEEE, Hangzhou.

DUTCHNEWS (2016) ‘Massive data breach’ at Almelo municipality. [WWW document] http://www.dutchnews.nl/news/archives/2016/09 massive-data-breach-at-almelo-municipaility/ (accessed 15 September 2016).

ELSON RJ and LECLERC R (2006) Customer information: protecting the organization’s most critical asset from misappropriation and identity theft. Journal of Information Privacy and Security 2(1), 3–15.

ENGEBRETSON P, PODHRADSKY A and CASEY C (2013) An analysis of security yulnerabilities of the Xbox 360 and Xbox Live mobile network International Journal of Mobile Network Design and Innovation 5(1), 9-16.

EVANGELOPOULOS N, ZHANG X and PRYBUTOK VR (2012) Latent semantic analysis: five methodological recommendations. European Journal of Information Systems 21(1), 70–86.

FATHIMA A and AHMED B (2013) Making data breach prevention a matter of policy in corporate governance. International Journal of Scientific Engineering and Technology 2(1), 1–7.

FAULKNER B (2007) Hacking into data breach notification laws. Florida Law Review 59, 1097–1125.

FRENCH A and SHROPSHIRE J (2011) Handheld versus traditional computer security threats and practices. The Journal of Internet Electronic Commerce Research 11(2), 153–171.

FRENCH AM, GUO C and SHIM J (2014) Current status, issues, and future of bring your own device (BYOD). Communications of the Association for Information Systems 35(10), 191–197.

F J and H DV (2008) Protecting data on mobile devices: A taxonomy of security threats to mobile computing and review of applicable defenses. Information, Knowledge, Systems Management 7(1), 159–180.

FURNELL S (2014) Password practices on leading websites–revisited. Computer Fraud & Security (12), 5–11.

G JA (1996) The ‘states-as-laboratories’ metaphor in state consti tutional law. Valparaiso University Law Review 30(2), 475–491.

GERARD GJ, HILLISON W and PACINI C (2005a) Identify theft: an organization’s responsibilities’. [WWW document] http://ruby.fgcu.edu/courses/ cpacini/courses/common/idtheftjoffincrim.pdf (accessed September 27).

GERARD GJ, HILLISON W and PACINI C (2005b) Identity theft: the US legal environment and organisations’ related responsibilities. Journal of Financial Crime 12(1), 33–43.

GOEL S and SHAWKY HA (2009) Estimating the market impact of security breach announcements on firm values. Information & Management 46(7), 404–410.

GRAY D and LADIG J (2015) The implementation of EMV chip card technology to improve cyber security accelerates in the US following target corporation’s data breach. International Journal of Business Administration 6(2), 60–67.

HALAMKA JD, MandL KD AND TANG PC (2008) Early experiences with personal health records. Journal of the American Medical Informatics Association 15(1), 1–7.

HANSON JB (2008) Liability for consumer information security breaches: deconstructing FTC complaints against businesses victimized by consumer information security breaches. Shidler Journal of Law, Commerce & Technoloay 4. 11-13

HARRIS AL, LANG M, YATES D and KRUCK S (2011) Incorporating ethics and social responsibility in IS education. Journal of Information Systems Education 22(3), 183.

HARRISON MI, KOPPEL R and BAR-LEV S (2007) Unintended consequences of information technologies in health care – an interactive sociotechnical analysis. Journal of the American Medical Informatics Association 14(5), 542–549.

HASSAN NR and LOWRY PB (2015) Seeking middle-range theories in information systems research. In International Conference on Information Systems (ICIS 2015), pp 13–18, AIS, Fort Worth, TX.

HEDAYATI A (2012) An analysis of identity theft: motives, related frauds, techniques and prevention. Journal of Law and Conflict Resolution 4(1), 1–12.

HELLER M (2016) Voter data breach leads to questions of tampering and state security. [WWW document] http://searchsecurity.techtarget.com/news/ 450303431/Voter-data-breach-leads-to-questions-of-tampering-andstate-security (accessed 15 September 2016).

HOFFMAN LJ, ROSENBERG T, DODGE R and RAGSDALE D (2005) Exploring a national cybersecurity exercise for universities. IEEE Security & Privacy 3(5), 27–33.

H PN and G O (2014) Data Breaches in Europe: Reported Breaches of Compromised Personal Records in Europe. 2005–2014 [WWW document] https://cmds.ceu.edu/sites/cmcs.ceu.hu/files/ attachment/article/663/databreachesineurope\_1.pdf (accessed 27 January 2017).

HU Q, XU Z, DINEV T and LING H (2011) Does deterrence work in reducing information security policy abuse by employees? Communications of the ACM 54(6), 54–60.

HUMPHRIES S (2008) Institutes of higher education, safety swords, and privacy shields: reconciling FERPA and the common law. Journal of College and University Law 35, 145–216.

IGURE V and WILLIAMS R (2008) Taxonomies of attacks and vulnerabilities in computer systems. IEEE Communications Surveys & Tutorials 10(1), 6–19.

I GP and B RL (2005) A longitudinal study of information system threat categories: The enduring problem of human error. The DATA BASE for Advances in Information Systems 36(4), 68–79.

I C ’ O (2016) Data security incident trends. [WWW document] https://ico.org.uk/action-weve-taken/datasecurity-incident-trends/ (accessed 15 September 2016).

ION I, SACHDEVA N, KUMARAGURU P and C<sup>ˇ</sup> APKUN S (2011) Home is safer than the cloud!: privacy concerns for consumer cloud storage. Paper presented at the Symposium on Usable Privacy and Security, Pittsburgh, PA, Article No. 13.

I B, W KR and S H (2004) The domino effect of password reuse. Communications of the ACM 47(4), 75–78.

J D, K N, B B, T W, S R and C T (2013) Cooperative solutions for bring your own device (BYOD). IBM Journal of Research and Development 57(6), 5: 1–5: 11.

JAYARAM N and MORSE P (1997) Network security – a taxonomic view. In European Conference on Security and Detection (ECOS), pp 124–127, IET, London.

KATZ E (2015) OPM’s return to paper security clearance processing roils contractors, lawmakers. [WWW document] http://www.govexec.com/ oversight/2015/07/opms-return-paper-security-clearance-processingroils-contractors-lawmakers/117031/?oref=relatedstories (accessed 22 January 2016).

KEMERER CF and SLAUGHTER S (1999) An empirical approach to studying software evolution. IEEE Transactions on Software Engineering 25(4), 493-509.

KIM JH (2015) Information theft within different organizational types: a rational choice analysis PhD dissertation, Rutgers, The State University

of New Jersey. [WWW document] http://dx.doi.org/doi:10.7282/ T3HD7XHF (accessed 27 January 2017).

KIM W, JEONG O-R, KIM C and SO J (2011) The dark side of the Internet: Attacks, costs and responses. Information Systems 36(3), 675–705.

KISH M (2016) One of Portland’s largest financial firms warns of possible data breach. [WWW document] http://www.bizjournals.com/ portland/news/2016/09/12/one-of-portlands-largest-financial-firmswarns-of.html (accessed 15 September 2016).

KOOPS B-J, LEENES R, MEINTS M, VAN DER MEULEN N and JAQUET-CHIFFELLE D-O (2009) A typology of identity-related crime: conceptual, technical, and legal issues. Information, Communication & Society 12(1), 1–24.

KOTULIC AG and CLARK JG (2004) Why there aren’t more information security research studies. Information & Management 41(5), 597–607.

KRUTZ RL and VINES RD (2010) Cloud Security: A Comprehensive Guide to Secure Cloud Computing. Wiley Publishing.

KURKOVSKY S and SYTA E (2011). Monitoring of electronic communications at universities: policies and perceptions of privacy. In 44th Hawaii International Conference on System Sciences (HICSS), pp 1–10, IEEE, Kauai, HI.

LEE AS and BASKERVILLE RL (2003) Generalizing generalizability in information systems research. Information Systems Research 14(3), 221–243.

LI X-B and QIN J (2017) Anonymizing and sharing medical text records. Information Systems Research, forthcoming.

L D, S I and K L (2009) How significant is human error as a cause of privacy breaches? An empirical study and a framework for error management. Computers & Security 28(3), 215–228.

LINDQVIST U and JONSSON E (1997) How to systematically classify computer security intrusions. In The 1997 IEEE Symposium on Security and Privacy, pp 154–163, IEEE Computer Society, Oakland, CA.

MARKUS ML and SAUNDERS C (2007) Editor’s comments: Looking for a few good concepts… and theories… for the information systems field. MIS Quarterly 31(1), iii–vi.

MAROTTA-WURGLER F (2016) Self-regulation and competition in privacy policies. The Journal of Legal Studies 45(S2), S13–S39.

MATHER T, KUMARASWAMY S and LATIF S (2009) Cloud Security and Privacy: An Enterprise Perspective on Risks and Compliance (Theory in Practice). O’Reilly Media, Inc.

MCCALLISTER E, GRANCE T and SCARFONE K (2010) Guide to protecting the confidentiality of personally identifiable information (PII). NIST Special Publication. [WWW document] http://ws680.nist.gov/publication/ get\_pdf.cfm?pub\_id=904990 (accessed 27 January 2017).

MCCALLUM A, NIGAM K and UNGAR LH (2000) Efficient clustering of highdimensional data sets with application to reference matching. In The Sixth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp 169–178, ACM.

MCKELVEY B (1978) Organizational systematics: taxonomic lessons from biology. Management Science 24(13), 1428–1440.

MCKELVEY B (1982) Organizational Systematics: Taxonomy, Evolution, Classification. University of California Press, Los Angeles, California.

MENSCH S and WILKIE L (2011) Information security activities of college students: An exploratory study. Academy of Information and Manage ment Sciences Journal 14(2), 91–116.

MESO P, DING Y and XU S (2013) Applying protection motivation theory to information security training for college students. Journal of Informa tion Privacy and Security, 9(1), 47–67.

NI LOIDEAIN N (2016) The end of safe harbor: Implications for EU digital privacy and data protection law. Journal of Internet Law 19(8), 7–14.

N JL and O’R ME (2009) Data protection basics: a primer for college and university counsel. Journal of College and University Law 36, 101.

N H (2009) Privacy in Context: Technology, Policy, and the Integrity of Social Life. Stanford University Press, Stanford, California.

PARKS R, XU H, CHU C-H and LOWRY PB (2016) Examining the intended and unintended consequences of organisational privacy safeguards. Euro pean Journal of Information Systems 26(1), 37–65.

Payiou PA (2011) State of the information privacy literature: where are we now and where should we go? MIS Quarterly 35(4), 977–988.

PEARSON S (2009) Taking account of privacy when designing cloud computina services. Paper presented at the ICSE Workshop on Software Engineering Challenges of Cloud Computing, Vancouver, Canada, 44–52.

PEMBLE M (2008) Don’t panic: taxonomy for identity theft. Computer Fraud & Security, 2008(7), 7–9.

PERETTI KK (2008) Data breaches: what the underground world of carding reveals. Santa Clara Computer and High Technology Journal 25, 375–413.

PHAM DV, SYED A and HALGAMUGE MN (2011) Universal serial bus based software attacks and protection solutions. Digital Investigation 7(3), 172–184.

PICANSO KE (2006) Protecting information security under a uniform data breach notification law. Fordham Law Review 75, 355.

PINSON C (2007) New legal frontier: Mass information loss and security breach. SMU Science and Technology Law Review 11, 27.

PODHRADSKY A, DOVIDIO R, ENGEBRETSON P and CASEY C (2013) Xbox 360 hoaxes, social engineering, and gamertag exploits. In 46th Hawaii International Conference on System Sciences (HICSS), pp 3239–3250, IEEE, Wailea, HI.

PORTER MF (1980) An algorithm for suffix stripping. Program: Electronic Library and Information Systems 14(3), 130–137.

P C, R TL, L PB, B RJ and C JF (2013) Insiders’ protection of organizational information assets: development of a systematics-based taxonomy and theory of diversity for protectionmotivated behaviors. MIS Quarterly 37(4), 1189–1210.

RAJA U and TRETTER MJ (2011) Classification of software patches: a text mining approach. Journal of Software Maintenance and Evolution: Research and Practice 23(2), 69–87.

RANCHAL R, BHARGAVA B, OTHMANE LB, LILIEN L, KIM A, KANG M, ET AL (2010) Protection of identity information in cloud computing without trusted third party. Paper presented at the IEEE Symposium on Reliable Distributed Systems, New Delhi, India, pp 368–372.

ROOSTA T, SHIEH S and SASTRY S (2006) Taxonomy of security attacks in sensor networks and countermeasures. In The First IEEE International Conference on System Integration and Reliability Improvements, IEEE, Hanoi, Vietnam.

SANSUROOAH K and SZEWCZYK P (2012) A study of remnant data found on USB storage devices offered for sale on the Australian second hand market in 2011. In 10th Australian Information Security Management Conference, Perth, Australia.

SEN R and BORLE S (2015) Estimating the contextual risk of data breach: an empirical approach. Journal of Management Information Systems 32(2), 314-341.

SHAFFER G (2000) Globalization and social protection: the impact of EU and international rules in the ratcheting up of US data privacy standards. Yale Journal of International Law 25(1), 1–88.

SIDOROVA A, EVANGELOPOULOS N, VALACICH JS and RAMAKRISHNAN T (2008) Uncovering the intellectual core of the information systems discipline. MIS Quarterly 32(3), 467–482.

SMITH HJ, DINEV T and XU H (2011) Information privacy research: an interdisciplinary review. MIS Quarterly 35(4), 989–1015.

STEINBROOK R (2008) Personally controlled online health data-the next big thing in medical care? New England Journal of Medicine 358(16), 1653–1656.

TANG PC, ASH JS, BATES DW, OVERHAGE JM and SANDS DZ (2006) Personal health records: definitions, benefits, and strategies for overcoming barriers to adoption. Journal of the American Medical Informatics Association 13(2), 121–126.

T S and C Y (2014) The rise in payment system breaches: the TargetCase. International Journal of Computer and Information Technology 3(5), 1060–1064.

TRACOL X (2016) EU–U.S. Privacy shield: the saga continues. Computer Law & Security Review 32(5), 775–777.

T LJ and A -P K (2010) The board’s responsibility for information technology governance. The John Marshall Journal of Information Technology & Privacy Law 28, 313–341.

TREMBLAY MC, BERNDT DJ, LUTHER SL, FOULIS PR and FRENCH DD (2009) Identifying fall-related injuries: text mining the electronic medical record. Information Technology and Management 10(4), 253–265.

TUTTLE H (2015) Implications of the Ashley Madison hack. Risk Management 62(8). 8–9

UPENDAR J and RAO EG (2013) An overview of plastic card frauds and solutions for avoiding fraudster transactions. International Journal of Research in Engineering and Technology 2(8), 215–222.

VAN WIJK ER and HOLMES TR (2007) Gone in a flash: a misplaced USB drive prompts internal auditing to rethink its coverage of security risks. Internal Auditor 64(3), 75–77.

VENTER H and ELOFF JH (2003) A taxonomy for information security technologies. Computers & Security 22(4), 299–307.

VERIZON (2015. Last updated). 2015 Data Breach Investigations Report. [WWW document] http://www.verizonenterprise.com/resources/ reports/rp\_data-breach-investigation-report\_2015\_en\_xg.pdf (accessed 27 January 2017).

VERMA S and SINGH A (2012) Data theft prevention & endpoint protection from unauthorized USB devices –Implementation. In Internationg Conference on Advanced Computing (ICoAC), pp 1–4, IEEE, Chennai, India.

WALL JD, LOWRY PB and BARLOW JB (2015) Organizational violations of externally governed privacy and security rules: Explaining and predicting selective violations under conditions of strain and excess. Journal of the Association for Information Systems 17(1), 39–76.

WANG T, KANNAN KN and ULMER JR (2013) The association between the disclosure and the realization of information security risk factors. Information Systems Research 24(2), 201–218.

WANG Y and NEPALI RK (2015) Privacy threat modeling framework for online social networks. In International Conference on Collaboration Technologies and Systems, pp 358–363, IEEE, Atlanta, Georgia.

WARKENTIN M and WILLISON R (2009) Behavioral and policy issues in information systems security: the insider threat. European Journal of Information Systems 18(2), 101–105.

WELCH B (1951) On the comparison of several mean values: an alternative approach. Biometrika 38(3/4), 330–336.

WILLISON R and WARKENTIN M (2010) The expanded security action cycle: a temporal analysis ‘Left of Bang’. In The Dewald Roode Workshop on Information Systems Security Research, IFIP WG8.

WILLISON R and WARKENTIN M (2013) Beyond deterrence: an expanded view of employee computer abuse. MIS Quarterly 37(1), 1–20.

XU W, GRANT G, NGUYEN H and DAI X (2008) Security breach: the case of TJX Companies, Inc. Communications of the Association for Information Systems 23(31), 575–590.

YOUNG E (2015) Educational privacy in the online classroom: FERPA, MOOCs, and the big data conundrum. Harvard Journal of Law & Technology 28, 549–593.

ZVIRAN M and HAGA WJ (1999) Password security: an empirical study. Journal of Management Information Systems 15(4), 161–185.
