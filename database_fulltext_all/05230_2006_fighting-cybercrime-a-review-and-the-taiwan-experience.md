---
otero_id: 5230
otero_key: "W9FN9HWC"
title: "Fighting cybercrime: a review and the Taiwan experience"
authors: "Wingyan Chung; Hsinchun Chen; Weiping Chang; Shihchieh Chou"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.06.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# Fighting cybercrime: a review and the Taiwan experience

Wingyan Chung<sup>a,\*</sup>, Hsinchun Chen<sup>b</sup>, Weiping Chang<sup>c</sup>, Shihchieh Chou<sup>c</sup>

<sup>a</sup>Department of Information and Decision Sciences, The University of Texas at El Paso, TX 79912, USA <sup>b</sup>Department of Management Information Systems, The University of Arizona, Tucson, AZ 85721, USA <sup>c</sup>Department of Information Management, National Central University, Taiwan

Available online 2 September 2004

## Abstract

Cybercrime is becoming ever more serious. Findings from the 2002 Computer Crime and Security Survey show an upward trend that demonstrates a need for a timely review of existing approaches to fighting this new phenomenon in the information age. In this paper, we define different types of cybercrime and review previous research and current status of fighting cybercrime in different countries that rely on legal, organizational, and technological approaches. We focus on a case study of fighting cybercrime in Taiwan and discuss problems faced. Finally, we propose several recommendations to advance the work of fighting cybercrime.

<sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Cybercrime; Fighting cybercrime; High-tech crime; Legal issues; Data mining

## 1. Introduction

As the Internet becomes a part of our daily lives, criminals increasingly are using it to conduct cybercrime. According to the 2002 Computer Crime and Security Survey conducted by Computer Security Institute and the U.S. Federal Bureau of Investigation, the threat of cybercrime and other information security breaches continues unabated and the financial toll is mounting [18]. The findings show that 90% of respondents detected computer security breaches over the past 12 months, 80% acknowledged financial losses due to computer breaches, and 71% detected unauthorized access by insiders. The total amount of annual financial losses in 2002 has reached a record high of \$455,848,000, since the survey was conducted in 1997. The problem of cybercrime is so serious that many countries are adopting various defensive approaches such as regulating the use of the Internet, setting up new organizations dealing with cybercrime issues, and developing new forensics technologies.

Because cybercrime is an emerging phenomenon of the information age, much research is at the inception stage. There is a need for a timely review of this field in order to summarize current status and to stimulate new research ideas. In this paper, we define different types of cybercrime, review related research and the current status of fighting cybercrime in different countries. Through providing high-level summaries and critical comments, our review should bring insights to researchers and practitioners. To provide readers with specific examples, we present a case study of fighting cybercrime in Taiwan, where cybercrime cases have soared in recent years. Finally, we propose recommendations to the community of researchers, policy makers, and practitioners who are involved in fighting cybercrime. Overall, the paper contributes to better understanding of fighting cybercrime and to promote research in this area.

## 2. An overview of cybercrime

What is cybercrime? Many researchers agree that it is any illegal activities conducted through computer, but some disagree on where cybercrime takes place. Parker [15] considers information system (which may not be computerized) as the channel that cybercrime is committed. In contrast, Philippsohn [16] views cybercrime to appear mainly on the Internet. Considering its nature and place of occurrence (see Table 1), we define <sup>b</sup>cybercrime<sup>Q</sup> as illegal computer-mediated activities that often take place in the global electronic networks.

What are the different types of cybercrime? Many researchers consider them to include computer hacking, Internet fraud, virus spreading, and theft of confidential information. Thomas and Loader [27] also included smuggling and illegal arms trafficking with the help of computer. Richards [20] considers intrusion of telephone systems (packet switched network) as a type of cybercrime, as well as intrusion of computer systems. Power considers hardware theft as a type of cybercrime, as well as theft of proprietary information [18]. As software vendors and media companies are more concerned with illegal transfer and sales of music or other digital products, we also include cyber-piracy among the types of crime that are conducted through the use of computer. We describe each major type of cybercrime and its subtypes as follows.

## 2.1. Major types of cybercrime

Computer hacking or network intrusion refers to the unauthorized access of a computer or a computer network. Motives for engaging in computer hacking can be political or personal. Political hackers attack a computer or a computer network with a view to publicizing their beliefs or protesting against certain government policies. Hacking for personal reasons may be related to personal pleasure, financial benefit, or hatred. Email spamming and sending junk/hostile email can seriously disrupt computer networks. In an extreme case, computer hacking can appear as cyberterrorism, which can result in human deaths (e.g., arising from malfunctioning of medical systems in hospitals) and destruction of critical infrastructure (e.g., banking networks).

Internet fraud refers to deceptive behavior conducted through the Internet in an illegal manner. Financial and personal benefits are the major motivations for Internet fraud, types of which include credit card fraud, fraudulent Internet banking sites, and advance fee fraud. In credit card fraud, the fraudster obtains credit card numbers of other cardholders and uses them illegally. Fraudulent Internet banking sites are set up to offer bogus banking services. In advance fee fraud, investors are lured by promises of an extremely high rate of return but are required to make prior payment. Other fraud crimes have also been greatly facilitated by the Internet (e.g., Internet auction scams, stock inflation scams, pyramid schemes, emails telling about sharing a large amount of money).

Spreading of malicious code refers to the sending of a virus, a Trojan horse (a computer program that can invite many viruses into an infected computer), or other malicious codes through a computer network to affect its normal operation.

Cyber-piracy is the illegal copying and trading of software through the Internet. The software can be computer programs, music, movies, or pornographic materials.

Other types of cybercrime include identity theft, electronic property theft, money laundering, and cyber-pornography. Identity theft often appears in international trade and e-commerce in which a criminal may pretend to be an actual seller to obtain payment from buyers. Electronic property theft involves stealing of confidential information such as trade secrets and credit card numbers. In money laundering, the criminals use a bank computer network to conceal an illegal source or application of income, and then disguise that income so as to make it appear legitimate. Cyber-pornography refers to the promotion of pornography through the Internet.

Table 1 An overview of cybercrime

<table><tr><td colspan="7">Definition</td></tr><tr><td>Author</td><td>Definition/characteristics of “cybercrime”</td><td>Internet fraud</td><td>Computer hacking</td><td>Cyber piracy</td><td>Spreading of malicious code</td><td>Others</td></tr><tr><td>Thomas and Loader [27]</td><td>Illegal computer-mediated activities which can be conducted through global electronic networks.</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Richards [20]</td><td>The illegitimate use of computer to conduct criminal activities.</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Parker [15]</td><td>Encompasses any abuse and misuse of information that entails using knowledge of information systems.</td><td>√</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Philippsohn [16]</td><td>Criminal activities conducted through the Internet.</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td></tr><tr><td>Power [19]</td><td>The intentional access of a computer without authorization or by exceeding authorization and thereby obtain information to which the person is not entitled.</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr></table>

<table><tr><td colspan="3">Categories and related work</td></tr><tr><td>Category of cybercrime</td><td>Sub-types of cybercrime</td><td>Related work</td></tr><tr><td>Internet fraud</td><td>Advanced fee fraud, credit card fraud, fraudulent Internet banking</td><td>[1,3]</td></tr><tr><td>Computer hacking/ network intrusion</td><td>Hacking for political reasons, hacking for personal reasons, email spamming or sending junk/hostile emails</td><td>[2,13,21,26]</td></tr><tr><td>Cyber piracy</td><td>Software piracy, piracy of music or movies</td><td>[6,11,12]</td></tr><tr><td>Spreading of malicious code</td><td>Spreading of virus or Trojan horse, spreading of other malicious codes</td><td>[8,14,22,25]</td></tr><tr><td>Others</td><td>Identity theft, electronic property theft, money laundering, cyber-pornography, etc.</td><td>[7,23]</td></tr></table>

<table><tr><td colspan="4">Research and techniques</td></tr><tr><td>Research</td><td>Description</td><td>Sub-type of cybercrime</td><td>Techniques</td></tr><tr><td>Androutsopoulos et al. [2]</td><td>Evaluates the performance of Naive Bayesian classifier in filtering unsolicited bulk email (spam). Attribute-set size, training-corpus size, lemmatization, and stop-lists are explored. Concludes that additional safety nets are needed for the Naive Bayesian anti-spam filter.</td><td>Email spamming</td><td>Naive Bayesian classifier</td></tr><tr><td>Chan et al. [3]</td><td>Studies three issues in credit card fraud detection: efficiency of highly distributed databases and detection systems, skewed distributions, and non-uniform cost per error. Proposes methods to solve these problems by training on subsets of distributed data with a “desired distribution” and combining multiple learned fraud detectors under a “cost model”. Empirical results show that the methods can significantly reduce loss due to fraud.</td><td>Credit card fraud</td><td>C4.5, CART, RIPPER, Bayes learning algorithms</td></tr><tr><td>de Vel et al. [6]</td><td>Employs a Support Vector Machine learning algorithm for mining the email content based on the structural characteristics and linguistic patterns.</td><td>Software piracy</td><td>Support Vector Machine</td></tr><tr><td>Droz et al. [7]</td><td>Presents a theft-deterrent system called WANTED which relies on credits and blacklists, with each protected device periodically requesting new credit in order to continue operating. The system resists attacks and guarantee privacy and scalability.</td><td>Electronic property theft</td><td>Simple credit-based tracking mechanism</td></tr><tr><td>Forrest et al. [8]</td><td>Proposes a method for virus detection based on the idea of artificial immune system. Defines self for privileged Unix processes, in terms of normal patterns of short sequences of system calls. The method is computationally efficient and could provide basis for online computer immune system.</td><td>Spreading of virus</td><td>Deviation analysis</td></tr><tr><td>Research</td><td>Description</td><td>Subtype of cybercrime</td><td>Techniques</td></tr><tr><td>Gray et al. [11]</td><td>Proposes methods for examining the authorship of computer programs, which involves the area of author discrimination, identification, characterization, and intent analysis. Linguistic and software metrics are used in performing software forensics.</td><td>Software piracy</td><td>Classification and linguistic analysis</td></tr><tr><td>Jankowitz [12]</td><td>Proposes a model for detecting plagiarism in students' Pascal programs. Based on programming style features and procedure execution features, a template is constructed for each program and is compared against each other to characterize students' programming style.</td><td>Software piracy</td><td>Statistical analysis</td></tr><tr><td>Lee et al. [13]</td><td>Uses data mining techniques (such as link analysis, classification rules, and time-based sequence analysis) to detect, predict and prevent network intrusion.</td><td>Network intrusion</td><td>Clustering, classification, sequence analysis</td></tr><tr><td>Longstaff and Schultz [14]</td><td>Discusses the evolution and authorship of WANK and OILZ worms by manually analyzing code structures and features. Program authorship and authors' styles are concluded from the discussion.</td><td>Spreading of virus</td><td>Manual examination</td></tr><tr><td>Sahami et al. [21]</td><td>Proposes a Bayesian approach to filtering junk emails. Considers domain-specific features of the problem in addition to raw text of email messages in order to create more accurate filters.</td><td>Sending junk emails</td><td>Bayesian networks</td></tr><tr><td>Schultz et al. [22]</td><td>Presents a data-mining framework for detecting malicious executables. Three classifier algorithms are implemented: RIPPER, Naive Bayes, and a Multi-Classifier system and were shown to perform better than signature-based methods. The proposed methods are being implemented as a network email filter.</td><td>Spreading of virus</td><td>RIPPER, Naive Bayes, and a Multi-Bayes Classifier</td></tr><tr><td>Senator et al. [23]</td><td>Uses link analysis techniques to identify similar transactions in the Financial Crimes Enforcement Network (FinCEN) AI System (FAIS). The system exploits the Bank Secrecy Act data to support the detection and analysis of operations engaged in money laundering and other financial crimes.</td><td>Money laundering</td><td>Clustering, classification, sequence analysis</td></tr><tr><td>Spafford [25]</td><td>Analyzes the Internet Worm program and manually examines three independently reversed-engineered versions of the program. Infers author's abilities and intent through analysis of coding style and methods used in the program.</td><td>Spreading of virus</td><td>Manual examination</td></tr><tr><td>Spertus [26]</td><td>Describes approaches to abusive messages recognition and presents a system, called Smokey, that builds a 47-element feature vector based on the syntax and semantics of each sentence. A C4.5 decision tree generator was used to determine feature-based rules and was able to correctly categorize 64% of abusive messages and 98% of nonabusive messages.</td><td>Sending hostile emails</td><td>C4.5 tree classification</td></tr></table>

When classifying the above cybercrime types, several factors have been considered: channels that criminals use to commit crime, damage to the victims, nature of the illegal activities, and criminals’ motivations. New types of cybercrime can be classified according to these factors as well.

## 2.2. Related technical work

Many previous efforts to combat cybercrime have employed data mining techniques to identify anomalies or detect cyber-attacks. To deal with the problems of network intrusion, virus spreading, and related cyberattack, Gray et al. proposed methods for examining the authorship of computer programs. The methods involve analysis of author identification, characterization, and intent. Linguistic and software metrics have been used to perform software forensics [11]. However, the methods may not provide adequate authorship evidence for use within a legal context. A comprehensive method of validating the results is necessary before the results could be presented as evidence in court.

To reveal the identity of authors who misuse an email system by sending out unsolicited email or junk mail, de Vel et al. [6] employed a Support Vector Machine learning algorithm for mining the email content based on its structural characteristics and linguistic patterns. Sahami et al. [21] proposed a Bayesian approach to filtering junk mail. They considered domain-specific features of the problem in addition to the raw text of email messages in order to create more accurate filters. Although these techniques achieve good results in automatically identifying email authors, privacy issues increasingly raise concern. The risk of these techniques being abused by cybercriminals should not be overemphasized.

Using link analysis techniques to identify similar transactions, the Financial Crimes Enforcement Network (FinCEN) AI System (FAIS) exploited Bank Secrecy Act data to support the detection and analysis of operations engaged in money laundering and other financial crimes [23]. In another research, Lee et al. used data mining techniques to detect, predict and prevent network intrusion. Link analysis was used to construct normal usage profiles, classification rules were used to determine whether unseen audit data was normal, and time-based sequence of audit event patterns indicated which temporal statistical measures should be included in intrusion detection models [13]. These techniques can reveal deeper knowledge in criminals’ behavioral patterns. However, as technologies evolve, the techniques should be adapted to changes in new ways of committing crimes by cyber-criminals.

From the above review, we summarized different definitions, types and research of cybercrime in Table 1. It compares different views of cybercrime, presents different categories of cybercrime, and summarizes related research and techniques. We found that data mining is a promising approach to identifying meaningful structure in a large amount of data. However, fighting cybercrime requires not only techniques or heuristics, but also involves government, public and private organizations, legislation, technologies, and cooperation from other countries.

## 3. Fighting cybercrime in different countries

Owing to the worldwide impact of cybercrime, various countries are using legal, organizational, and technological approaches to fight against it. The legal approach aims to restrict cybercrime activities through legislation. The organizational approach aims to enforce laws, to promote cooperation, and to educate the public through the establishment of dedicated organizations. The technological approach aims to increase the effectiveness and efficiency of cybercrime analysis and investigation with the help of new technologies. Based on these three approaches, we review the current status of fighting cybercrime in different countries. Under each approach, we divide our review into within-country and across-country strategies in order to provide both national and international views of fighting cybercrime. Most countries in this study were selected from the member countries of the Group of Eight (G8), which has established international conventions on fighting cybercrime. We also have chosen Japan and Australia because of their economic importance in their respective continents.

## 3.1. Legal approach

## 3.1.1. Within-country strategies

To protect the interests of Internet businesses or to regulate activities on the Internet, many countries create new laws or modify the current laws as shown in Table 2. With the first digital signature law in the world, the US has established a number of regulations on cybercrime [9,10]. The British parliament passed two cybercrime-related acts: the Data Protection Act of 1984 and the Computer Misuse Act of 1990. The Canadian parliament passed the Criminal Law Amendment Act. The Australian parliament passed the Australian Cybercrime Act of 2001. The Japanese parliament passed the <sup>b</sup>Unauthorized Computer Access Law<sup>Q</sup> in 1999. The Taiwan parliament amended 10 articles of the Criminal Law in 1997 and added Articles 358 and 359 to the Criminal Code in 2003.

From these legislation efforts, we found that the transborder nature of cybercrime is in conflict with the territoriality of national law enforcement authorities. However, unlawful behaviors on the Internet should be punished in every country and the laws should be uniform permitting greater cooperation. Table 2 shows that legislations on unauthorized access to computer systems have been revised or amended in many countries at different times. This time difference provided criminals chances to escape the penalty, and created difficulties for local law enforcement agencies to investigate cybercrime activities. For example, the creator of the <sup>b</sup>I love you<sup>Q</sup> virus was arrested in Philippines on May 8, 2000, but was not punished by any law at that time. To avoid this problem from occurring again, different countries should have the same standard and penalty to deal with cybercrime.

Table 2  
New laws related to fighting cybercrime in countries

<table><tr><td>Countries</td><td>New laws</td><td>Description of new laws</td></tr><tr><td rowspan="4">The United States</td><td>Federal Law: 18 U.S.C. §1029, §1030, §1362, §2511, §2701, §2702, §2703</td><td>Restricting activity in connection with access devices, computers, communication lines, stations, or systems. Prohibiting interception and disclosure of wire, oral, or electronic communications, unlawful access to stored communications, and disclosure of contents.</td></tr><tr><td>The National Infrastructure Protection Act of 1996</td><td>Providing for the protection of all US government computers, covering computer use in electronic commerce, and punishing as a felony any recklessness that causes damage to critical infrastructure.</td></tr><tr><td>The Cyberspace Electronic Security Act of 1999</td><td>Enabling law enforcement agencies and officers to obtain criminal evidence legally from encrypted data.</td></tr><tr><td>The “Patriot Act of 2001”</td><td>Expanding surveillance powers of the FBI by allowing it to monitor lines of electronic communication, including phone conversations, email and voice mail.</td></tr><tr><td rowspan="3">England</td><td>The Data Protection Act of 1984</td><td>Dealing with the actual procurement and use of personal data</td></tr><tr><td>The Computer Misuse Act of 1990</td><td>Hacking, destruction of material, modification of material and some unauthorized access without explicit intent are forbidden.</td></tr><tr><td>The Regulation of Investigatory Powers Bill</td><td>Giving law enforcement agencies authority to obtain passwords to encrypted messages and to access computer files and email for investigative purpose.</td></tr><tr><td>Canada</td><td>The Criminal Law Amendment Act</td><td>Forbidding unlawful entry into a computer system and interception of transmissions and criminalizes the actual destruction, alteration, or interruption of data.</td></tr><tr><td>Australia</td><td>The Australian Cybercrime Act of 2001</td><td>Defining criminal behaviors related to unauthorized activities. Forbidding persons to access, modify or impair data or electronic commerce without authorization.</td></tr><tr><td>Japan</td><td>The Unauthorized Computer Access Law</td><td>Defining criminal behaviors related to unauthorized activities.</td></tr><tr><td>Taiwan</td><td>Articles 358 and 359 of the Criminal Code</td><td>Defining criminal behaviors related to unauthorized access to proprietary computer systems</td></tr></table>

## 3.1.2. Across-country strategies

3.1.2.1. Group of eight (G8). In 1997, the G8 released a Ministers Communique´ that includes an action plan and principles to combat cybercrime. The Communique´ requires member countries to ensure that appropriate measures are taken to criminalize cybercrime, to protect the confidentiality, integrity, and availability of data and systems from unauthorized impairment, and to preserve quick access to electronic data.

3.1.2.2. The Council of Europe (CE). The Council of Europe (CE) was established in 1949 by West

European countries and now has over 40 member countries. In 2001, the CE, the US, Canada, South Africa, and Japan co-drafted and passed the Cybercrime Convention, the first international convention aimed at Internet criminal behaviors. The convention mandates member countries to have unified legislation on cybercrime in order to promote the ability to fight against cybercrime in the international arena.

## 3.2. Organizational approach

## 3.2.1. Within-country strategies

A number of agencies have been set up to fight against cybercrime as shown in Table 3.

## 3.2.2. Across-country strategies

3.2.2.1. Group of eight (G8). G8 mandates that all law enforcement personnel must be trained and equipped to address cybercrime, and designates all member countries to have a point of contact on a 247 basis.

Table 3  
New agencies of fighting cybercrime in countries

<table><tr><td>Countries</td><td colspan="2">Agencies/subagencies</td><td>Responsible cases or duties</td></tr><tr><td rowspan="12">The United States</td><td rowspan="4">The Federal Bureau of Investigation</td><td>Field Offices</td><td>Hacking, denial of service, computer virus, copyright piracy, theft of trade secrets, trademark counterfeiting, counterfeiting of currency, child pornography or exploitation, Internet bomb threats, trafficking in explosive or incendiary devices or firearms over the Internet.</td></tr><tr><td>The National Infrastructure Protection Center</td><td>Protecting critical infrastructures, investigating computer intrusion, illegal drug trafficking, and providing professional training.</td></tr><tr><td>The Computer Analysis Response Team</td><td>Computer forensics and providing assistance in the search and seizure of computer evidence.</td></tr><tr><td>The Technical Support Center of the FBI</td><td>Technical support to federal, state, and local law enforcement agencies regarding data encryption and decryption.</td></tr><tr><td colspan="2">The National White Collar Crime Center</td><td>Providing support to law enforcement agencies on preventing, investigating, and prosecuting economic or high-tech criminal cases.</td></tr><tr><td colspan="2">The Internet Fraud Complaint Center</td><td>Offering a central repository for complaints related to Internet fraud, working to quantify fraud patterns, and providing timely statistical data on current fraud trends.</td></tr><tr><td colspan="2">The Computer Crime and Intellectual Property Section (CCIPS)</td><td>Advising and coordinating prosecution of computer intrusion and intellectual property cases.</td></tr><tr><td colspan="2">The Computer Hacking and Intellectual Property Unit</td><td>Complementing the highly trained network of prosecutors at CCIPS and the US Attorneys&#x27; Offices.</td></tr><tr><td colspan="2">The United States Secret Service</td><td>Financial crimes including financial fraud, identity theft, computer fraud, telecommunications fraud, and computer-based attacks.</td></tr><tr><td colspan="2">The United States Customs Service</td><td>Copyright piracy (software, movies, and music), trademark counterfeiting, child pornography or exploitation.</td></tr><tr><td rowspan="2" colspan="2">The United States Postal Inspection Service Bureau of Alcohol, Tobacco and Firearms</td><td>Internet fraud related to postal service.</td></tr><tr><td>Internet bomb threats, explosive or incendiary devices or firearms over the Internet.</td></tr><tr><td>England</td><td colspan="2">National Criminal Intelligence Service</td><td>Investigating attacks on critical national infrastructures, major Internet based offenses of pedophilia, fraud or extortion, information from seized electronic media.</td></tr><tr><td>Canada</td><td colspan="2">The Information Technology Security Branch of the Royal Canadian Mounted Police</td><td>Security Evaluation and Inspection Team, Computer Investigative Support Unit, and Counter Technical Intrusion Unit</td></tr><tr><td>Australia</td><td colspan="2">The Federal Police Computer Crime Unit</td><td>Executing the Telecommunication Act.</td></tr><tr><td>Japan</td><td colspan="2">The Central Police Administration</td><td>High-tech Crime Technology Division and High-tech Crime Technological Support Center under.</td></tr><tr><td rowspan="3">Taiwan</td><td colspan="2">Cybercrime Prevention and Fighting Center in the Ministry of Justice</td><td>Making policy and proposing new laws.</td></tr><tr><td colspan="2">Telecommunication Police Squad of the Directorate General of Telecommunication</td><td>Computer-related crimes</td></tr><tr><td colspan="2">The Computer Crime Squad of the Criminal Investigation Bureau</td><td>Computer-related crimes</td></tr></table>

3.2.2.2. The Council of Europe (CE). CE requires member countries to set up organizations to execute Chapter Three of the Cybercrime convention, which describes international cooperation and extradition, and rules for obtaining evidence for investigation. The convention requires member countries to operate a connection network on a 247 basis and to provide essential training and equipment to relevant personnel.

## 3.3. Technological approach

## 3.3.1. Within-country strategies

To fight against cybercrime, many countries have launched technological initiatives, including the establishments of new agencies, systems, or programs. Table 4 indicates that countries have applied such technologies as intrusion detection, filtering, rating, data encryption and data decryption to cybercrime investigation. Most of these technologies are mature and have been used by businesses.

Table 4  
Technologies applied to fighting cybercrime

<table><tr><td>Countries</td><td>Systems/agencies</td><td>Description</td></tr><tr><td>The United States</td><td>Carnivore</td><td>Developed by the FBI, a computer surveillance system to assist in the investigation of cybercrime [24]. Intercepts all packets that are sent to and from the ISP where it is installed. Includes a one-way tap into an Ethernet data stream, a general-purpose computer to filter and collect data, and additional components to control collection and examine data.</td></tr><tr><td>England</td><td>The National Criminal Intelligence Service</td><td>Established a unit dedicated to decrypting criminal material, and applying technologies of filtering and rating to protect minors from inappropriate materials on the Web [17].</td></tr><tr><td>Canada</td><td>The Royal Canadian Mounted Police</td><td>Designed and introduced Internet training for police officers to improve the ability to deal with crimes.</td></tr><tr><td>Australia</td><td>Australian Computer Crime Program</td><td>Developed and provided investigative tools and a training regime for police investigators fighting computer crime.</td></tr><tr><td>Japan</td><td>The Cyber Force Center of National Police Administration</td><td>Established and developed the Real Time Intrusion Detection Network System to detect and trace terrorist activities in 2001.</td></tr><tr><td>Taiwan</td><td>The Criminal Investigation Bureau</td><td>Set up the Criminal Knowledge Base System (CKBS) in 2003. CKBS integrates 50 million criminal documents from court, prosecution, and police systems. Developed proprietary software tools and hardware equipment for investigating cybercrime cases, such as Internet Patrol Agent, Globe IP Tracer, Packet Analyzer, and Remote Monitor.</td></tr></table>

## 3.3.2. Across-country strategies

3.3.2.1. Group of eight (G8). G8 recommends to member countries to use information technology to prevent and detect network abuse, facilitate the tracing of criminals, and collect evidence.

3.3.2.2. The Council of Europe (CE). Two articles, Articles 20 and 21, in Cybercrime Convention by CE deal with applying information technology to collect and intercept traffic data for law enforcement agencies.

## 4. Fighting cybercrime in Taiwan: a case study

Drawing from the experience of the authors of this paper, we present the following case study of fighting cybercrime in Taiwan (Mr. Weiping Chang is the director of the Information System Office of Criminal Investigation Bureau (National Police Administration) and has over 5 years of cybercrime investigation experience in over 300 cases in Taiwan).

## 4.1. Cybercrime in Taiwan

Compilation of official statistics for Taiwan cybercrime was initiated in 1999. According to the Taiwan police regulations, each cybercrime case is recorded on a criminal record form that contains many such fields as event time, event place, suspect’s birth date, education, and vocation. All criminal record forms are sent to the Criminal Investigation Bureau and the data are input to a criminal database. The statistics reported here were collected between 1999 and 2002.

With an average annual growth rate of 17%, the Internet-using population has been growing much faster than the total population in Taiwan. Table 5 shows an overview of cybercrime in Taiwan. It should be noted that the numbers of cybercrime cases and suspects, with annual growth rates over 170%, have been increasing much faster than even the Internet population and reached a record high in 2002. Also of note is that cybercrime suspects are becoming younger, as shown in the increasing proportion of suspects aged below 18. Again, the year 2002 had the highest number of suspects, more than the total of all the previous 3 years. With regard to education, only 21% (1050) of all 5035 suspects in cybercrime cases from 1999 to 2002 had not completed high school, compared with about 60% of all suspects of general criminal cases in Taiwan. This suggests that cybercrime is mainly conducted by highly educated people. Of all crime types, sex trading on the Internet accounts for most cybercrime cases (34%) and stealing <sup>b</sup>treasure<sup>Q</sup> (money credits) for cyber-games is ranked second to sex trading (20.4%) between 1999 and 2002. Sex trading or spreading messages of sex trading on the Internet is against Article 29 of Taiwan’s Child and Youth Sexual Transaction Prevention Act (CYSTPA) passed in 1999. Stealing <sup>b</sup>treasure,<sup>Q</sup> which means hacking into the server of cyber-game providers and stealing the money credits recorded in it, is against the Criminal Code in Taiwan and is increasingly popular due to the popularity of Internet Cafe´ houses and on-line games.

Table 5  
Overview of cybercrime in Taiwan

<table><tr><td rowspan="3">Year</td><td rowspan="3">Total populationa</td><td rowspan="3">Internet populationb</td><td colspan="5">Number of cybercrime cases</td><td colspan="7">Number of cybercrime suspects</td></tr><tr><td rowspan="2">Sexc</td><td rowspan="2">Pd</td><td rowspan="2">Porne</td><td rowspan="2">Stealf</td><td rowspan="2">Other</td><td colspan="4">By age</td><td colspan="3">By education</td></tr><tr><td>&lt;12</td><td>12–17*</td><td>18–23</td><td>&gt;23</td><td>B. H.*g</td><td>H.h</td><td>C.i</td></tr><tr><td></td><td></td><td></td><td colspan="5">Total: 128</td><td colspan="7">Total: 158</td></tr><tr><td>1999</td><td>22,034,096</td><td>4,800,000</td><td>2</td><td>24</td><td>33</td><td>0</td><td>69</td><td>0</td><td>7(4%)</td><td>49</td><td>102</td><td>35(22%)</td><td>103</td><td>20</td></tr><tr><td></td><td></td><td></td><td colspan="5">Total: 444</td><td colspan="7">Total: 516</td></tr><tr><td>2000</td><td>22,216,107</td><td>6,260,000</td><td>97</td><td>144</td><td>78</td><td>4</td><td>121</td><td>1</td><td>32(6%)</td><td>145</td><td>338</td><td>98(19%)</td><td>341</td><td>77</td></tr><tr><td></td><td></td><td></td><td colspan="5">Total: 982</td><td colspan="7">Total: 1102</td></tr><tr><td>2001</td><td>22,339,759</td><td>7,820,000</td><td>414</td><td>177</td><td>131</td><td>34</td><td>226</td><td>1</td><td>102(9%)</td><td>340</td><td>659</td><td>220(20%)</td><td>700</td><td>182</td></tr><tr><td></td><td></td><td></td><td colspan="5">Total: 2945</td><td colspan="7">Total: 3259</td></tr><tr><td>2002</td><td>22,520,776</td><td>8,590,000</td><td>1015</td><td>119</td><td>355</td><td>882</td><td>574</td><td>7</td><td>837(26%)</td><td>1206</td><td>1209</td><td>697(21%)</td><td>2090</td><td>472</td></tr><tr><td></td><td></td><td></td><td colspan="5">Average: 189%</td><td colspan="7">Average: 179%</td></tr><tr><td>Annual growth</td><td>0.73%</td><td>17%</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sup>a</sup> Population Statistics Annual Report, Department of Statistics, Ministry of Interior, Republic of China.  
b Internet Population Statistics Report, The Institute for Information Industry, 2002.  
<sup>c</sup> Sex stands for <sup>b</sup>spreading message of sex trading or sex trading on the Internet.<sup>Q</sup>  
<sup>d</sup> P stands for <sup>b</sup>selling pirate CDs on the Internet.<sup>Q</sup>  
<sup>e</sup> Porn stands for <sup>b</sup>cyber-pornography.<sup>Q</sup>  
<sup>f</sup> Steal stands for <sup>b</sup>stealing treasure (money credits) of cyber-game on the Internet.<sup>Q</sup>  
<sup>g</sup> B.H. stands for <sup>b</sup>below high school.<sup>Q</sup>  
<sup>h</sup> H. stands for <sup>b</sup>high school.<sup>Q</sup>  
<sup>i</sup> C. stands for <sup>b</sup>college or above.<sup>Q</sup>  
Percentage proportion among all cybercrime suspects.

Faced with the rapid increase of cybercrime, the Taiwan government actively uses legal, organizational and technological approaches to fighting it.

## 4.1.1. Legal approach

Because existing laws could not keep pace with the development and proliferation of cybercrime, the Taiwan parliament in 1997 amended 10 articles of Criminal Law to deal with cybercrime. In the new amendments, computer files have been classified as <sup>b</sup>movable property.<sup>Q</sup> Stealing, copying, or downloading computer files onto a computer or other medium without the owners’ permission are regarded as criminal acts. Those who commit such a crime could face a maximum sentence of a 5-year imprisonment.

Two new articles, Articles 358 and 359, were added to the Criminal Code in June 2003 to deal with hackers who gain unauthorized access to proprietary computer systems. Article 358 stipulates that anyone who uses any other person’s password without previous permission and/or otherwise gains unauthorized access to proprietary computer systems shall be sentenced to a prison term not more than 3 years and fined not more than NT\$100,000. According to Article 359, any person who tries to steal, erase or otherwise change information stored on discs of any person, and whose said act results in serious damage to the latter, shall be sentenced to a prison term of not more than 5 years and fined not more than NT\$200,000 (US\$1=NT\$35).

## 4.1.2. Organizational approach

To fight cybercrime, the Taiwan government has set up the Cybercrime Prevention and Fighting Center in the Ministry of Justice. This center has integrated and coordinated the resources of related departments since 1997. The Ministry of Interior has extended the Computer Crime Unit of the Criminal Investigation Bureau of National Police Administration to make it the Computer Crime Squad in 1999 and established a Computer Crime Unit in every county police department in 2000. A new law enforcement agency in the Ministry of Transportation and Communication called the Telecommunication Police Squad was set up under the Directorate General of Telecommunication in 1997. The main responsibilities of the Telecommunication Police Squad are clamping down on illegal use of radio frequencies and investigating cybercrime.

Additionally, to fight against cybercrime, the Taiwan government has set up Department of Information Management in the Central Police University (entering the Central Police University is the only way to be a police officer in Taiwan). Computer crime investigation, computer forensics, and applying IT to deal with crimes are among the department’s core courses.

Also, the Taiwan police has established a computer crime unit in every county police department. There are three to five police officers in each unit. All officers of computer crime unit either are graduated from Department of Information Management of Central Police University or are investigators with some computer specialty. They combine information technology and criminal investigation skill to effectively fight against cybercrime. The National Police Administration of

Taiwan evaluates the county police department’s performance on cybercrime fighting every 3 months.

To promote commerce, Taiwan’s government convened the Conference of National Knowledge Economy in 2000. The objectives of the conference were to enhance Taiwan’s economic liberation and internationalization, to strengthen the flow of personnel, goods and funds, and to attract multinational and domestic investments. One of the conference themes was to prevent economic development from being interfered with by cybercrime and to develop methods to fight against computer crime. Many experts and scholars proposed good suggestions, such as increasing detection rates, elevating investigative techniques, expanding investigative software and hardware equipment, coordinating with ISPs to assist in investigating cybercrime cases, and enhancing international cooperation [5].

With regards to international cooperation, the Taiwan government actively joins the various international organizations such as the International Criminal Police Organization (INTERPOL) and cooperates with law enforcement agencies of other countries to combat transborder crime. To establish relationships with law enforcement agencies fighting cybercrime in other countries, the Taiwan police actively participate in related conferences such as High Technology Crime Conference hosted by the FBI.

## 4.1.3. Technological approach

In 2003, the Criminal Investigation Bureau, the main task force fighting against cybercrime, set up the Criminal Knowledge Base System (CKBS) that integrates heterogeneous data from court, prosecution, and police departments. Each data table in the system contains a large number of fields. For instance, a criminal record table from the police department contains 315 fields, such as criminal tools, criminal methods, criminal scenes, prepared matters, criminal causes, criminal habits, and so on. CKBS supports criminal pattern analysis, accomplice relationship analysis, and social network analysis via data mining technology. The Cybercrime Dedicated Portion (CDP) applies the technology of automatic document classification to classifying cybercrime cases precisely. CDP provides an efficient full-text search function for investigators. The Criminal Investigation Bureau also has developed the following proprietary software tools and hardware equipment for cybercrime investigation. Internet Patrol Agent can collect illegal information (e.g., child pornographic materials) on the Internet and save it in a database. Globe IP Tracer can identify the location and ISP of a given IP address. Packet Analyzer can intercept and analyze the network packets. Remote Monitor can remotely monitor the computer screen of victims of hacking.

## 4.2. Problems of fighting cybercrime in Taiwan

There are several unique problems relating to cybercrime in Taiwan. First, limited identification of Internet and cellular phone users hinders cybercrime investigation. Owing to ISP’s simple application procedure, customers could easily falsify personal data when seeking ISP or cell phone services. This provides a great convenience for cyber-criminals who conduct illegal activities. Second, it is difficult to trace the activities of many illegal, overseas-hosted Web sites. The lack of formal channels for Taiwan cybercrime investigators to communicate with other countries’ law enforcement agencies hinders effective investigation. Third, many ISPs, Internet Content Providers (ICPs), and Internet companies keep users log files for only a short time (1–3 months) also hinders cybercrime investigation. The Taiwan Ministry of Transportation and Communication tried to create a new law to extend this period but these companies objected because of cost and privacy issues. Fourth, because Internet Cafe´ Houses do not require users to present identification, many criminals commit cybercrimes there and it is very difficult for law enforcement agencies to obtain information of these criminals.

## 5. Recommendations

To relieve the problems, we propose the following recommendations to governments, lawmakers, international organizations, intelligence and law enforcement agencies, and researchers.

## 5.1. Regularly updating existing laws

Lawmakers should regularly update existing laws related to cybercrime as new technologies are being developed. For example, laws regulating ISPs’ operations need to be updated frequently. Because criminals often commit cybercrime in countries with less stringent laws, countries should work together to adopt a unified standard of fighting cybercrime that prevents criminals from taking advantages of countries having less stringent rules. This will create a cooperative foundation for countries to fight against cybercrime. In particular, regulations should be developed to mandate that ISPs keep communication records and log files for a reasonable period of time so they could be available for investigative purposes. Individual privacy need not be adversely affected in the process.

## 5.2. Enhancing specialized task forces

Law enforcement agencies should recruit qualified investigators with technical and legal knowledge so as to keep up with the development of cybercrime and its social impacts. Government and schools need to provide training to update these investigators’ technical and legal knowledge. Computer forensics laboratories should be established to collect digital evidence from computer equipment.

## 5.3. Utilizing civic resources

In addition to doing their own investigation, law enforcement agencies should utilize civic resources to enhance the effectiveness and efficiency of their work. They should look to university or research organizations for obtaining technical support and also should cooperate with private businesses (e.g., ISPs) to obtain first-hand information about cybercrime. These can speed up the processing of cybercrime cases and prevent more Internet users from becoming victims.

## 5.4. Promoting cybercrime research

Research should be promoted to enhance understanding of cybercrime by considering cybercrime causes and characteristics, cyber-criminals’ motives, educational level, age distribution, and affiliations, and the differences between cybercrime and other crimes. To fight against and prevent cybercrime efficiently, and to develop policies for combating cybercrime, we need to understand the nature of the crime further. Knowledge in criminology can help in this context.

## 5.5. Applying information technologies

Future trend will be to increasingly apply IT to cybercrime investigation. Research in intelligence analysis and knowledge management systems has shown that IT enabled law enforcement agencies to manage different kinds of criminal and intelligence data, information, and knowledge more effectively and to sift through tons of related criminal information efficiently [4]. The Taiwan police’s CKBS applies data mining technology to criminal investigation and has achieved promising results by producing suspect lists and solving many larceny cases with a lack of clues and evidence. However, more work needs to be done because, different from conventional crimes, cybercrime lacks unique identification such as fingerprints and DNA, making it difficult to match criminal records with suspect information. Developing IT to facilitate such matching can potentially help analyze and detect criminals’ behavioral patterns. Automatically analyzing authorship of electronic evidence is one promising way to accomplish this.

## 6. Summary and the future

Cybercrime greatly affects individuals, businesses, and national security. Increasingly, cybercrime is emerging as a major crime type in the 21st century. In this paper, we have defined different types of cybercrime and reviewed previous research and the current status of cybercrime fighting in different countries. We have focused on a detailed case study of fighting cybercrime in Taiwan. Finally, we recommend four future directions for fighting cybercrime: updating existing laws, enhancing specialized task forces, utilizing civic resources, and promoting cybercrime research. We believe that our review is timely and our Taiwan case study provides insights on how to combat cybercrime.

Since the 9/11 attacks, many experts have warned that terrorists will attempt to use the Internet to damage key Web sites and information infrastructure around the world. For example, the US government has been warned repeatedly that the electrical power grid, including some nuclear facilities, may be at risk from cyber attacks. It is thus imperative for countries to plan for the best and prepare for the worst—to take necessary legal, organizational and technological approaches to fight against cybercrime and to protect themselves from cyber-terrorism in the post-911 era.

## Acknowledgments

This research was partly supported by NSF Digital Government Program, <sup>b</sup>COPLINK Center: Information and Knowledge Management for Law Enforcement<sup>Q</sup>, #9983304, July 2000–June 2003 and NSF Information Technology Research, <sup>b</sup>Developing A Collaborative Information and Knowledge Management Infrastructure,<sup>Q</sup> NSF/IIS #0114011, September 2001– August 2004. We thank Barbara Sears and the anonymous reviewers for their comments and suggestions.

## References

[1] J.M. Adams, Controlling cyberspace: applying the computer fraud and abuse act to the internet, Santa Clara Computer and High-Technology Law Journal 12 (1996) 403–434.

[2] I. Androutsopoulos, G. Paliouras, V. Karkaletsis, G. Sakkis, Learning to filter spam e-mail: a comparison of naive bayesian and a memory-bases approach, Proceedings of the 4th European Conference on Principles and Practice of Knowledge Discovery in Database, Springer, Haidelberg, 2000, pp. 1 – 13.

[3] P.K. Chan, W. Fan, A.L. Prodromidis, S.J. Stolfo, Distributed data mining in credit card fraud detection, IEEE Intelligent System 14 (6) (1999) 67 – 74.

[4] H. Chen, D. Zeng, H. Atabakhsh, W. Wyzga, J. Schroeder, COPLINK: managing law enforcement data and knowledge, Communications of the ACM 46 (1) (2003) 28 – 34.

[5] P.-C. Chen, A plan of knowledge economy development, The Council for Economic Planning and Development, Executive Yuan, Taiwan, 2001, pp. 64 – 75.

[6] O. de Vel, A. Anderson, M. Corney, G. Mohay, Mining e-mail content for author identification forensics, SIGMOD Record 30 (4) (2001) 55– 64.

[7] P. Droz, C. G<sup>¨</sup> ulc¨u, R. Haas, WANTED: a theft deterrent solution for the pervasive computing world, Proceedings of the 9th IEEE International Conference on Computer Communications and Networks, IEEE Computer Society, New York, 2000, Las Vegas, NV.

[8] S. Forrest, S.A. Hofmeyr, A. Somayaji, T.A. Longstaff, A sense of self for unix processes, Proceedings of the 1996 IEEE Symposium on Research in Security and Privacy, IEEE Computer Society Press, New York, 1996, pp. 120– 128, Oakland, CA, USA.

[9] L.J. Freeh, Statement for the Record of Louis J. Freeh, Director, Federal Bureau of Investigation on Cybercrime Before the Senate Committee on Judiciary Subcommittee for the Technology, Terrorism, and Government Information,

U.S. Department of Justice, http://www.usdoj.gov/criminal/ cybercrime/freeh328.htm, 2000.

[10] L. Garrison, M. Grand, Network defense: the legal aspects of retaliation, National Infrastructure Protection Center Highlights (2001) 2 (Issue 7-01).

[11] A. Gray, P. Sallis, S. MacDonell, Software forensics: extending authorship analysis techniques to computer programs, Proceedings of the 3rd Biannual Conference of the International Association of Forensic Linguistics (IAFL), International Association of Forensic Linguistics (IAFL), 1997, pp. 1 – 8, Durham NC, USA.

[12] H.T. Jankowitz, Detecting plagiarism in student PASCAL programs, Computer Journal 31 (1) (1988) 1988.

[13] W. Lee, S.J. Stolfo, Data mining approaches for intrusion detection, Proceedings of the 7th USENIX Security Symposium, Advanced Computing Systems Association, Berkeley, 2000, pp. 66 – 72, San Antonio, TX.

[14] T. Longstaff, E. Schultz, Beyond preliminary analysis of the WANK and OILZ worms: a case study of malicious code, Computers & Security 12 (1993) 61 – 77.

[15] D.B. Parker, Fighting Computer Crime: A New Framework for Protecting Information, Wiley Computer Publishing, Chichester, England, 1998.

[16] S. Philippsohn, Trends in cybercrime—an overview of current financial crimes on the internet, Computers & Security 20 (1) (2001) 53–69.

[17] P.O.S.T., Regulating internet content, Parliamentary Office of Science and Technology 159 (2001) 1– 4.

[18] R. Power, 2002 CSI/FBI computer crime and security survey, Computer Security Issues & Trends 8 (1) (2002) 1 – 22.

[19] R. Power, Tangled Web: Tales of Digital Crime from the Shadows of Cyberspace, Que Corporation, Indianapolis, Indiana, 2000.

[20] J.R. Richards, Transnational Criminal Organizations, Cybercrime, and Money Laundering: A Handbook for Law Enforcement Officers, Auditors, and Financial Investigators, CRC Press, Boca Raton, FL, 1999.

[21] M. Sahami, S. Dumais, D. Heckerman, E. Horvitz, A Bayesian approach to filtering junk e-mail, Proceedings of the AAAI Workshop on Learning for Text Categorization, AAAI Press, Madison, WI, USA, 1998, pp. 55 – 62.

[22] M.G. Schultz, E. Eskin, E. Zadok, S.J. Stolfo, Data mining methods for detection of new malicious executables, IEEE Symposium on Security and Privacy, IEEE Computer Society Press, Oakland CA, USA, 2001, pp. 38 – 49.

[23] T. Senator, H. Goldberg, J. Wooton, A. Cottini, A. Umar, C. Klinger, W. Llamas, M. Marrone, R. Wong, The FinCEN artificial intelligence system: identifying potential money laundering from reports of large cash transactions, Proceedings of the 7th Conference on Innovative Applications of AI, AAAI, Menlo Park, CA, 1995.

[24] S.P. Smith, H. Perrit, H. Krent, S. Mencik, Independent Technical Review of the Carnivore System, http://www.usdoj. gov/jmd/publications/carniv<sup>\_</sup>final.pdf (2000).

[25] E. Spafford, The internet worm program: an analysis, Computer Communication Review 19 (1) (1989) 17 – 49.

[26] E. Spertus, Smokey: automatic recognition of hostile messages, Proceedings of Innovative Applications of Artificial Intelligence, Providence, Rhode Island, 1997, pp. 1058–1065

[27] D. Thomas, B.D. Loader, Introduction—cybercrime: law enforcement, security and surveillance in the information age, Cybercrime: Law Enforcement, Security and Surveillance in the Information Age, Taylor & Francis Group, New York, NY, 2000.

![](/api/attachments/W9FN9HWC/fulltext/images/4a0c5b8ebc695f926b72d6a7f86b4479bd31dacc8fa1ca05ae2e4615cb108bd1.jpg)

Wingyan Chung is an Assistant Professor in the Information and Decision Sciences Department of the University of Texas at El Paso. He received his Ph.D. in Management Information Systems from the University of Arizona. He also received his Bachelor of Business Administration and M.S. in Information and Technology Management degrees from the Chinese University of Hong Kong. His research interests include

knowledge management, data and text mining, web computing, intelligence and security informatics, and human-computer interaction. His research work has been published or will appear in Communications of the ACM, IEEE Computer, International Journal of Human-Computer Studies, and Journal of the American Society for Information Science and Technology. Contact him at wchung@utep.edu.

![](/api/attachments/W9FN9HWC/fulltext/images/aeafa0961421de410d9ada40d28a0bb80b41f0cd5d617f120e7d1ecce4126e0e.jpg)

Hsinchun Chen is McClelland Professor of MIS at the Eller College of the University of Arizona and Andersen Consulting Professor of the Year (1999). He received the PhD degree in Information Systems from New York University in 1989, MBA in Finance from SUNY-Buffalo in 1985, and BS in Management Science from the National Chiao-Tung University in Taiwan. He is author of more than 120 articles cove-

ring medical informatics, homeland security, semantic retrieval, search algorithms, knowledge management, and Web computing in leading information technology publications. Contact him at hchen@eller.arizona.edu.

![](/api/attachments/W9FN9HWC/fulltext/images/017197c5652c552b892e61817d9524047d0128501dec567db96b0c3d296264e7.jpg)

Mr. Weiping Chang is currently a doctoral candidate in the Department of Information Management at National Central University, Taiwan, and Director of Information System Office of Criminal Investigation Bureau (CIB) of National Police Administration in Taiwan. He has been a member of CIB for 6 years. He has extensive experience in cybercrime investigation, computer forensics and developing investigative tools for Taiwan

investigators. He earned his bachelor’s degree from Central Police University in 1984 and his master’s degree in law enforcement administration from Western Illinois University in 1995. His research topics are knowledge management, information retrieval, and computer forensics. He can be reached at wpchang@mgt.ncu.edu.tw.

![](/api/attachments/W9FN9HWC/fulltext/images/3cb2f70e04b9653fe1f0c9bf07fdfcfd3d778c03812de2a8f38cebdd5ffa1534.jpg)

Dr. Shihchieh Chou is an Associate professor of the Department of Information Management at National Central University in Taiwan since 1987. He had been a project manager at the Institute for Information Industry (III) of Taiwan from 1985 to 1987. He received his PhD from Texas A&M University in 1984 with a major in computer and adult education. His research focuses on knowledge management, software engi-

neering and distance learning. He has developed some software engineering tools. He can be reached at scchou@mgt.ncu.edu.tw.
