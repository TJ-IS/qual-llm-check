---
otero_id: 13482
otero_key: "8SKXW8FC"
title: "An Empirical Validation of Malicious Insider Characteristics"
authors: "Nan (Peter) Liang; David P. Biros; Andy Luse"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1205925"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Empirical Validation of Malicious Insider Characteristics

Nan (Peter) Liang, David P. Biros & Andy Luse

To cite this article: Nan (Peter) Liang, David P. Biros & Andy Luse (2016) An Empirical Validation of Malicious Insider Characteristics, Journal of Management Information Systems, 33:2, 361-392, DOI: 10.1080/07421222.2016.1205925

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1205925

![](/api/attachments/8SKXW8FC/fulltext/images/b98de840938e05a67ee0b58bdb3b9213c3a45f89f870a510638849263132067c.jpg)

Published online: 05 Oct 2016.

![](/api/attachments/8SKXW8FC/fulltext/images/5b6189b7d55f2291068b3fec72827205ba2f22c086f11d4561716104308deb43.jpg)

Submit your article to this journal

![](/api/attachments/8SKXW8FC/fulltext/images/8cba2f4a21fcb1f84d48e403eed481e25751fbb94dd2e6ad6be2e8b0f9063b71.jpg)

Article views: 48

![](/api/attachments/8SKXW8FC/fulltext/images/d1ae678df86a7d0418150c5a82ffd59a82f366b24d8d779db0d7aa227ff2c955.jpg)

View related articles

![](/api/attachments/8SKXW8FC/fulltext/images/914929b18ead5f0f079c9fd43a4c90699b9611a7421ff3e970f4b7cda74c0632.jpg)

View Crossmark data

# An Empirical Validation of Malicious Insider Characteristics

NAN (PETER) LIANG, DAVID P. BIROS, AND ANDY LUSE

NAN (PETER) LIANG (nan.liang@okstate.edu) is a doctoral candidate in the Management Science and Information Systems Department at Oklahoma State University. His research focuses on deception detection, data analytics, and information system security. His work has been published in the Proceedings of the Hawaii International Conference on Systems Sciences and Americas Conference on Information Systems.

DAVID P. BIROS (david.biros@okstate.edu; corresponding author) is an associate professor of management science and information systems at Oklahoma State University. His research interests included deception detection and information system trust. He has published in MIS Quarterly, Decision Support Systems, Group Decision and Negotiation, and other journals. He is serving as president of the AIS Special Interest Group on Information Security (SIGSEC).

ANDY LUSE (andyluse@okstate.edu) is an assistant professor of management science and information systems in the Spears School of Business at Oklahoma State University. He received his Ph.D. from Iowa State University. His research interests include security, technology adoption, and research methodology.

ABSTRACT: Malicious insiders continue to pose a great threat to organizations. With their knowledge and access to organizational resources, malicious insiders could launch attacks more easily that result in more damaging impacts compared to outsiders. However, empirical research about malicious insiders is rare due to the unavailability of data. With few exceptions, many studies focus on a small number of cases. In order to identify common characteristics of a large number of malicious insiders, this study employs text mining to analyze 133 real-world cases of offenders from military units, intelligence agencies, and business organizations with data available to the public. Contributions of this study reside in two aspects: first, we use public data from documented malicious insider cases, implying a potentially valuable data source for future studies in this domain; second, we validate malicious insider characteristics identified in previous research, thereby establishing a foundation for more comprehensive research in the future.

KEY WORDS AND PHRASES: data classification, insider attacks, insider threat, malicious insider, text mining.

Insider attack is nothing new. In the famous book The Art of War, about 2,500 years ago Sun Tzu described five different kinds of spies. In a more recent case, the notorious spy Aldrich Ames was first evaluated as an “enthusiastic employee” at the beginning of his CIA career. As recognition for his outstanding performance, he eventually gained top-level clearances and access to countless classified intelligence documents. However, trust in him finally turned out to be a CIA nightmare [97].

Unlike outsiders, insiders like Ames are legitimately empowered to access and manipulate an organization’s information resources [9]. Insider attacks are not only easier to launch but also can be more devastating. Damages from insider attack involve financial loss, disruption to the organization, loss of reputation, and a longterm impact on the organizational culture [49].

The threat of malicious insiders has drawn attention from both practitioners and academia [15]. For practitioners, the U.S. Secret Service and Carnegie Mellon University conducted a series of studies in this area [21], involving the comparison of sabotage and espionage [5], sabotage in critical infrastructures [59], and insider threat in financial sectors [71]. With respect to academic research, this area of study demands more comprehensive and in-depth research because the temporal precedents of malicious insiders’ attacks are currently underresearched [99].

In order to investigate and aid in the mitigation of the threat posed by potential malicious insiders, it is necessary to shed light on the characteristics of known malicious insider abusers [24]. Researchers focusing on known insider incidents have suggested a number of characteristics thought to be prevalent in malicious insiders [16, 51, 98]; however, current research has several problems and limitations. Many studies focus on a single case as the unit of analysis and derive their findings in the form of technical reports that lack peer review [5, 66]. Academic research endeavors often lack empirical testing with sufficient numbers of real-world malicious insider cases [51, 66]. While the current body of research posits a number of potential characteristics of insider threat, they come from multiple and distinct perspectives resulting in the lack of a systematic framework to integrate all characteristics for a clear and solid foundation to facilitate future studies [16, 51, 66, 85].

Part of the reason for the aforementioned shortcomings is a lack of data [65]. Organizations are reluctant to disclose malicious insider data in fear of negative effects on their reputation [100]. One potential way to overcome this issue and gain access to a larger number of malicious insider cases is to mine data from non-security-related sources [24]. Twyman et al. [92] have suggested an autonomous scientifically controlled screening system to detect hidden information, including insider threat intention, via screening interview results. However, it might be economically inefficient to interview all employees. In this research we employ text mining techniques [31] to evaluate a sample of 133 malicious insider threat cases pulled from public data in order to validate malicious insiders’ characteristics and answer the research question:

1. Can text mining be employed to validate characteristics of malicious insiders? Researchers have suggested a number of characteristics of malicious insiders [24, 98, 99]. The prevalence of such characteristics has not been examined in a large sample of malicious insiders. We take the keywords garnered from our text mining and code them according to characteristics identified in previous research [24, 98, 99]. We extrapolate the proportion of individuals with the given characteristics, but question how this compares to the proportion of individuals in the population at large who display these same characteristics. It would be useful to determine whether there is a significant proportional difference that allows the identification of characteristic areas more prevalent in malicious insiders. By comparing these proportions, we are able to answer the research question:

2. Do malicious insiders exhibit different levels of characteristics from those exhibited by the general public?

## Literature Review

As noted, previous research on malicious insiders includes academic research, technical reports, and various other sources. In this section, we suggest theoretical considerations and we will present definitions or descriptions of characteristics from the literature in related domains.

## Theoretical Considerations

The extant literature suggests that malicious insiders exhibit certain characteristics; however, malicious insider attacks include other relevant aspects including the attacker, organizational factors, environment, and systems [15, 70]. A recent leadership study review [64] shows that effective leadership is related to leader skills and traits, leader behavior, influence process, and other situational behaviors. In addition, in early leadership studies in the 1930s and 1940s, the trait approach was popular and considerable research was conducted to investigate the unique traits an effective leader possesses [105]. Although criticized for its lack of consideration for situational and mitigating factors [105], traits of leaders are still starting points for recent leadership research [30], such as leaders charisma traits [10], leaders’ skills [55], or leaders’ attributes and behaviors [93].

Similar to the way in which researchers have investigated leaders, we believe that trait theory can help in explaining malicious insider threats. If traits or characteristics can be identified and attributed to malicious insiders, it could prove useful to future research in profiling and catching them.

## Terminology and Definitions

One of the challenges insider threat studies face is the lack of a well-accepted definition of insiders [49]. Different researchers define the term in different ways: Willison and Warkentin [99] define insiders from the perspective of their privilege as employees or others who have access privileges as well as intimate knowledge of the organization. Bishop and Gates [9] define insiders based on their actions, as one who violates organizational security policies. Others define insiders from the aspect of their relations with organization such as a trusted person who has access to internal information [11]. Bishop and Gates [9] argue that the definition of an insider is contingent on the definition of the perimeter such that the one inside the perimeter is the insider. Hunker and Probst [49] further state that the definition of an insider depends on the research questions.

In the current research, our subjects are not confined to information systems. The subject pool includes all kinds of insider-attacked information or information systems. In addition, the malicious actions performed by these insiders include a broad range of activities. Therefore, in this research we use the broad definition of an insider by Bishop et al. [9, p. 5]:

An insider is a person that has been legitimately empowered with the right to access, represent, or decide about one or more assets of the organization’s structure.

Consistent with the definition of an insider, we use the Predd et al. [70, p. 67] definition of insider threat as:

Insider threat is an insider’s action that puts an organization or its resources at risk.

As indicated by Crossler et al. [24], insiders whose actions cause damage to the organization can be differentiated by their intentions: those who intentionally harm the organization with deviant behaviors and those who unintentionally do something wrong but are often labeled as insider threats. Also, any investigation focusing on this field should not mix these two different types of subjects. Other research that supports their arguments proposes an insider threat continuum [99] from passive, nonvolitional noncompliance behavior to volitional but not malicious noncompliance and finally, these intentional, malicious insiders. This continuum is also proposed by other researchers [46, 48]. The wording might be different, but intention is consistently the key to differentiating different types of insiders within this continuum. Therefore, in this study, we modify Predd et al.’s definition by integrating intention factors, so as to narrow down the definition to our subjects, the malicious insiders:

Malicious insiders are insiders who intentionally put an organization or its resources at risk.

## Characteristics of Malicious Insiders

Previous research has identified a number of characteristics that one or more malicious insiders have exhibited. As previously stated, many studies focused on a single case and very few considered larger samples. Therefore, characteristics of malicious insiders across a large number of cases have not yet been determined. In the following sections, we review some of the potential malicious insider characteristics noted in the literature to date.

## Personality Problems

Personality disorders include classic Axis II personality disorders [35], such as antisocial personality disorder [77], narcissistic personality disorder [75, 77, 102], and psychopathy [77]. Research suggests that malicious insiders [21] may have a sense of entitlement [5, 66, 76] and grandiosity [38] and tend to have an inappropriate sense of self-importance or self-esteem [38, 91] such as Machiavellianism [56, 66]. Some have engaged in unrealistic fascination with spy work, imaginary activities [21], power, or reputation [66].

## Mental Health Disorder

Mental health disorder involves evidence of Axis I Psychiatric Diagnoses derived from the American Psychiatric Association’s Diagnostic Manual [35]. Research reports mental health disorders such as alcohol and drug addiction, panic attacks, or seizure disorders being observed in malicious insiders [5, 59]. Addictive behavior seems to be associated with malicious insider attacks [50]. These mental disorders and addictions often result in an exploitable or vulnerable lifestyle [21].

## Ethical Issues

Ethical beliefs are found to be relevant in regard to insiders’ rule violation behaviors [14, 94]. Ethical issues are described as lack of empathy, conscience [76], lack of personal integrity [66], no remorse for the harm imposed on others, and an unscrupulous manner. Other issues include being superficial and lacking conscientiousness [21]. Malicious insiders’ lack of ethics is usually accompanied by reduced loyalty or attachment to the organization [66]. Employee fraud, which is one type of malicious attack, is also found to be related to ethical flexibility [62].

## Social Isolation

Band et al. [5] define social isolation problems as “chronic problems getting along and working with others.” Shaw and Fischer [76, p. 75] find in their case study that malicious insiders lack social skills, which increases their propensity for social isolation. Shaw et al. [75] find that malicious insiders are typically introverts, and some are overly dependent on computers. Moore et al. [59] also report a lack of social skills as one characteristic of malicious insiders.

## Personal or Work-Related Events

Band et al. [5, p. 18] define personal or work-related events as “events that cause concerning behaviors in individuals predisposed to malicious acts.” Moore et al. [59] also confirm that malicious insiders typically experience stressful work-related events such as sanctions or internal audits. Also, the stressful experience of employees might result in a higher probability of security breach [26]. Furthermore, personal issues such as loss of a family member, a relationship breakup, or significant personal injury could also indicate a potential malicious insider [21].

## Emotional Characteristics

It is suggested that malicious insiders are emotionally unstable [21] and might react to work-related issues negatively instead of constructively. This includes feelings of being betrayed or isolated [5] and fear of being excluded [66]. As a result of their inappropriate feelings, they might exhibit anger [5], poor work attitude, or stress. However, some research states that instead of feeling negative, malicious insiders might seek sensation as an emotional response [66].

## Disgruntlement

Many studies [45, 66, 96, 100] find that malicious insiders are also disgruntled employees. A study examining the Department of Agriculture and information technology (IT) sabotage in the U.S. critical infrastructure program proposes disgruntlement as a potential characteristic of malicious insiders. The disgruntlement might be a result of unmet expectations [59], lack of appreciation, and feelings of injustice or inequality [66].

## Social and Cultural Conflict

Shaw and Fischer [75, p. 16] define social and cultural conflict as “differences between social, racial, or technical groups leading to tensions and conflict between the subject and others.” For example, one malicious insider made a racial comment about his African-American supervisor [75]. Shaw et al. [74] find that malicious insiders are frustrated with their personal or social relations.

## Behavior Precursor

Behavioral characteristics preceding malicious attack include suspicious verbal behavior [73], confrontation with peers or supervisors [5], sexual harassment, hygiene problems [59], problems with accepting feedback and criticism, and anger management issues [44]. Being defensive when criticized also appears to be a behavior precursor [91].

## Negative Experience

Lastly, Shaw and Fischer [75] found that malicious insiders experience disappointment with family or friends. As such, they might have a negative history such as history of rule violation [59] and/or criminal and mental disorder [66].

## Other Factors

While the previous section presented characteristics of malicious insiders found in the extant literature, insider attacks could also be enabled by other factors. In addition, before the attack is launched, other characteristics might exist beyond the psychology of the perpetrator. These might be conditions or precursors that promote or support the malicious act. In this section, we will review and present other factors that could enable a malicious insider attack.

## Overdependence

By definition, insiders have access to and knowledge of the organization, which could facilitate the attack if they turn to malicious acts [102]. Furthermore, malicious insiders are often recruited by organizations because they are domain experts or they are familiar with the work they are responsible for in the organization [102]. In short, the organization needs them. Once malicious insiders have managerial control or access that is out of proportion to their technical or managerial duties, they can be a threat unless they are sufficiently supervised [5].

## Preparatory Behavior

Schultz [73] argues that malicious insiders might leave deliberate marks to make a statement, make mistakes during preparation, and exhibit observable behaviors as part of preparation for the malicious action. These behaviors include information collection behaviors, information transmittal behaviors, and recruitment behaviors [103]. Specifically, insiders might perform technical precursors such as downloading hacking software [59], establishing backdoor entry to information systems [5], violating security policy, or undertaking unauthorized handling of classified materials [21].

## Financial Status

Some malicious insiders are motivated by profit [78, 102] because of debt [5, 23]; and as a result, they might exhibit characteristics of illegal income such as a sudden change of lifestyle or excess spending. For example, when interviewed about his spying activities, Robert Hansen told investigators his motive was profit [101].

## Rationalization

Research finds that malicious insiders might rationalize their behavior [96] by self-deception [91], blaming others, or arguing that the information or asset they comprise are not important [38, 51]. Individuals who conduct Internet fraud, which is a subtype of malicious attack, tend to rationalize their behaviors [3, 17, 23, 62]. A summary of all the aforementioned characteristics is presented in Table 1.

Table 1. Summary of Characteristics in Previous Research

<table><tr><td>Characteristic</td><td>Subcharacteristic examples</td><td>Citation</td></tr><tr><td rowspan="3">Personality disorder</td><td>1. Sense of entitlement</td><td>1. Band et al. [5]; Nurse et al. [66]; Shaw and Stock [76]</td></tr><tr><td>2. Grandiosity</td><td>2. Gelles [38]</td></tr><tr><td>3. Sense of self-importance</td><td>3. Gelles [38]; Turner and Gelles [91]</td></tr><tr><td rowspan="3">Mental health disorder</td><td>1. Addictive behavior</td><td>1. Johnson [50]</td></tr><tr><td>2. Exploitable behavior</td><td>2. Shaw and Stock [76]</td></tr><tr><td>3. Panic attack</td><td>3. Band et. al. [5]; Moore et al. [59]</td></tr><tr><td rowspan="3">Ethical issues</td><td>1. Lack of empathy</td><td>1. Nurse et al. [66]</td></tr><tr><td>2. Lack of conscience</td><td>2. Shaw and Stock [76]</td></tr><tr><td>3. Superficiality</td><td>3. Shaw and Stock [76]</td></tr><tr><td rowspan="2">Social isolation</td><td>1. Dependent on computer</td><td>1. Shaw et al. [74]</td></tr><tr><td>2. Introverted</td><td>2. Shaw et al. [74]</td></tr><tr><td rowspan="3">Related event</td><td>1. Demotion</td><td>1. Band et al. [5]</td></tr><tr><td>2. Change in supervisor</td><td>2. Nurse et al. [66]; Moore et al. [59]</td></tr><tr><td>3. Personal conflict;</td><td>3. Nurse et al. [66]</td></tr><tr><td rowspan="3">Emotional characteristics</td><td>1. Feeling of being betrayed</td><td>1. Shaw and Fischer, 2011</td></tr><tr><td>2. Fear of being excluded</td><td>2. Nurse et al. [66]</td></tr><tr><td>3. Anger</td><td>3. Band et al. [5]</td></tr><tr><td rowspan="3">Disgruntlement</td><td>1. Unmet expectation</td><td>1. Moore et al. [59]</td></tr><tr><td>2. Lack of appreciation</td><td>2. Nurse et al. [66]</td></tr><tr><td>3. Feeling of injustice</td><td>3. Nurse et al. [66]</td></tr><tr><td rowspan="2">Social and cultural conflict</td><td>1. Racial comment</td><td>1. Shaw and Stock [76]</td></tr><tr><td>2. Frustrated with relations</td><td>2. Shaw et al. [74]</td></tr><tr><td>Behavior precursor</td><td>1. Verbal behavior</td><td>1. Schultz [73]</td></tr></table>

<table><tr><td rowspan="2"></td><td>2. Sexual harassment</td><td>2. Moore et al. [59]</td></tr><tr><td>3. Defensive upon criticism</td><td>3. Turner and Gelles [91]</td></tr><tr><td rowspan="3">Negative experience</td><td>1. Disappointment with friends</td><td>1. Shaw and Fischer, 2011</td></tr><tr><td>2. History of arrest</td><td>2. Moore et al. [59]</td></tr><tr><td>3. History of mental disorder</td><td>3. Nurse et al. [66]</td></tr><tr><td rowspan="3">Overdependence</td><td>1. Managerial control</td><td>1. Shaw and Stock [76]</td></tr><tr><td>2. Root administrator</td><td>2. Shaw and Stock [76]</td></tr><tr><td>3. Without supervision</td><td>3. Shaw and Stock [76]</td></tr><tr><td rowspan="3">Preparatory behavior</td><td>1. Download hack software</td><td>1. Moore et al. [59]</td></tr><tr><td>2. Creating backdoor account</td><td>2. Band et al. [5]</td></tr><tr><td>3. Information collection</td><td>3. Wood et al. [103]</td></tr><tr><td rowspan="3">Financial status</td><td>1. Debt</td><td>1, 2. Band et al. [5];</td></tr><tr><td>2. Illegal income</td><td>3. Wood [102]</td></tr><tr><td>3. Change of lifestyle</td><td></td></tr><tr><td rowspan="3">Rationalization</td><td>1. Self-deception</td><td>1.Turner and Gelles [91]</td></tr><tr><td>2. Blaming others</td><td>2. Kamoun and Nicho [51]; Gelles [38]</td></tr><tr><td>3. Bragging or joking about classified information</td><td>3. Kamoun and Nicho [51]; Gelles [38]</td></tr></table>

As implied by previous research, malicious insiders might exhibit some personality cues, be in a certain state, or exhibit suspicious behaviors. However, most research lacks sufficient data, resulting in a lack of strong empirical analysis. In the following section, we propose a method designed to verify the aforementioned characteristics as well as extract characteristics that emerge in cases but are not mentioned in previous research.

## States and Traits

The current research investigates the characteristic commonality among known malicious insiders; as identified in the previous research, characteristics should be considered as either traits or states [13]. Although they do not explicitly define the terms, Allport and Odbert [2, p. 26] describe traits as “consistent and stable modes of an individual’s adjustment to his environment” and states as “present activity, temporary states of mind and mood.”

For the purpose of validation, in the current study we will shed light on the commonality of traits or characteristics, including trait-like conditions, among malicious insiders. On the contrary, by the definition of states, they should be very sensitive to the uniqueness of each individual case, such that we do not expect certain behaviors or events presented in one case to be commonly observed in other cases.

## Propositions

As noted, previous research has identified a number of potential characteristics believed to be common to malicious insiders. The potential characteristics have yet to be validated across a large sample of malicious insiders. The question then becomes, do malicious insiders exhibit these characteristics differently from the rest of the general population?

Narcissistic personality disorder is characterized by grandiosity and a sense of entitlement [35]. Those with a sense of grandiosity and superiority typically believe that they possess unparalleled skills or talent [38]; and with their self-perceived abilities, they are prone to fantasizing about power, success, and attractiveness [77], and perceive themselves as deserving special, or preferential, treatment [75]. Once their craving for admiration and special attention cannot be met, they might seek validation and affirmation of their self-importance from other sources such as competitors or opponents [38]. Even if they do not seek ego fulfillment themselves, their eagerness for recognition subjects them to showboating and manipulation [77].

On the other hand, if individuals have an antisocial personality disorder, which is defined as a pervasive disregard for the law and the rights of others [34], they tend to aim at whatever they want, regardless of whether it is illegal or others might be hurt. Since these insiders know more about the organization [9] and it is hard for them to form an attachment and loyalty to the organization [38], they are prone to attack the organization from inside.

Avoidant personality disorder is characterized by social inhibition and unwillingness to get involved with people [35]. However, teamwork is essential in organizations and social skills are essential in team settings [60]. The inability to work and communicate effectively with others decreases the odds of confronting colleagues with legitimate work-related complaints [5]. When the employee experiences stressful personal or work-related events such as demotion or the death of significant others [5, 66], isolation resulting from avoidant personality disorder jeopardizes the possibility that they can solve problems constructively [77]. Instead, they might engage in more destructive behavior and launch an insider attack. Given this, we propose the following:

Proposition 1-1: Prevalence of narcissistic personality disorder in malicious insiders is higher compared to the general population.

Proposition 1-2: Prevalence of antisocial disorder in malicious insiders is higher compared to the general population.

Proposition 1-3: Prevalence of avoidant personality disorder in malicious insiders is higher compared to the general population.

Disruptive mood dysregulation disorder (DMDD) is one type of mental health disorder that features persistent outbursts of temper and often irritable moods [4]. DMDD [34] is structurally linked to emotion regulation and is highly associated with negative emotional response such as emotional instability or bursts of anger [33]. Studies on malicious insiders report a high correlation between presence of emotional dysregulation and malicious intent [44].

Therefore, we propose:

Proposition 2: Prevalence of disruptive mood dysregulation disorder in malicious insiders is higher compared to the general population.

Comorbidities of substance abuse and anxiety disorder as well as personality disorder are observed in a nationwide survey [41, 42]. Coupled with the fact that the addiction behaviors could impair professional abilities [5], employees who have a substance addiction probably fail to work effectively and productively, making mistakes that might result in poor performance reviews, disciplinary action [43], and sanctions [59]. These events might cause the individual stress, and lead to a malicious attack from the inside [77]. Given this, we propose:

Proposition 3-1: Prevalence of alcohol abuse in malicious insiders is higher compared to the general population.

Proposition 3-2: Prevalence of substance abuse in malicious insiders is higher compared to the general population

Workplace disgruntlement is associated with perceived organizational injustice [96, 100]. Adams [1] claims that individuals who feel a sense of inequality may attempt to mitigate this feeling by behavioral means such as acting out in some manner. In extreme cases, these behavioral means might include malicious attacks such as computer crime [96, 100]. Further, the devalued or dissatisfied feelings of disgruntled employees [45] might affect their emotional state [66] resulting in negative feelings toward the employer or colleagues. Once such negative feelings turn severe or even destructive, disgruntled employees tend to launch attacks [21]. We therefore propose:

Proposition 4: Prevalence of disgruntlement in malicious insiders is higher compared to the general population.

Considering these propositions we now focus on a method for evaluating them. The following section describes our process for validating characteristics of malicious insiders compared to those of the general population. We believe malicious insiders exhibit the characteristics noted above at greater levels than those found in the general U.S. population. At this point, our validation efforts focus on individual characteristics only. While consideration of interactions of characteristics is necessary at some point, it is beyond the scope of our current study.

## Method

In this study, we will compare the percentage of malicious insiders who have certain characteristics with the percentage of the same characteristics in the general public. With respect to malicious insiders, the methods employed in the current study include three steps: in the first step we use the names of malicious insiders (n = 133) to collect relevant documents about them. In the second step we use a random subset of samples (n = 30) to construct and update our dictionary. Finally, we use this dictionary to search and extract characteristics in malicious insider portfolios. As for the general public, we use the reported percentages from previous studies and surveys. In this section, we first describe the procedure employed to collect data and construct the dictionary, then the extraction process will be introduced. Finally, we will introduce sources of data about the general public as well as describing how we will compare the malicious insiders in our sample and the general population.

Figure 1 shows a process flow diagram of the first and second steps. Dictionary creation includes four parts: data collection, dictionary construction, characteristic retrieval, and dictionary update. Note that the process starts at the upper left and bottom middle and ends at the upper right.

## Sampling Criteria and Data Collection

The malicious insiders to be analyzed in this study are drawn from population of malicious insiders who were convicted by U.S. courts from 2000 to 2015. The malicious attacks of those convicted include spying, espionage, economic espionage, illegal exports, and other security-related acts.

![](/api/attachments/8SKXW8FC/fulltext/images/7dfd2018dc1544ccbeee966a9a09d27072932c2aaa146ccd46ae4fe763bc4282.jpg)  
Figure 1. Method Process Flow

Due to the infrequency of malicious insider cases, previous research suggests that it is impractical to draw a random sample [5]. In the current study, we use the eminence criterion proposed by Simonton [83] to select the sample. This criterion has been applied in studies to investigate personality or social psychology when direct analysis of the subjects is far more difficult and even practically or ethically impossible [83]. For example, it is almost impossible to ask Edward Snowden to fill out a personality assessment questionnaire . This type of research includes the investigation of the relationship between creativity and leadership [95], the mad-genius controversy [81], the relation between mental health and achievement [84], and other phenomena [69, 88].

Under this criterion, eminence of an individual or prominence of the event associated with the individual could be used as a sampling criterion [80], and in practice, the eminence of this person or the prominence of the event could be evaluated by the comprehensiveness of representation in archival sources [83].

Eminence can be good or bad [80], which means eminent people can be famous or notorious. In the current study, since we are using the press media releases as data sources, we use the extent of media coverage as an index of eminence and it is operationalized as the number of reports for an individual.

We start with the names of malicious insiders such as “Aldrich Ames,” “Robert Hanssen,” and other known malicious insiders as keywords. Next, we retrieve documents from the Internet containing these name keywords, using information retrieval techniques [12]. The documents retrieved may be news articles, court transcripts, or other accounts of insider incidents associated with the named keywords. All cases have multiple articles reporting on the incident, hereafter referred to as a “portfolio.”

## Dictionary Construction and Update

A random subset (n = 30) of eminent malicious insiders in the data sets is used in constructing the dictionary. The documents retrieved are separated by paragraph for analysis with each record in the database consisting of a paragraph from an article. In addition, when each paragraph is stored, a name tag is added indicating which malicious insider this paragraph is describing.

## Dictionary Construction

Construction of the dictionary is a dynamic process with the dictionary updated after each portfolio of a malicious insider is analyzed. The basis of this dictionary is derived from the attributes in the extant literature (see Table 1). The characteristic dictionary has two attributes, keyword and characteristic. “Keyword” contains target words or phrases we are searching for in documents; the “characteristic” implies what the corresponding target words or phrases indicate. For example, the keyword “being caught” implies the characteristic of “rule violation.”

## Extracting Keywords from the Portfolio

In this step, we first prepare documents via parsing and stemming. Then we employ computer-aided information extraction techniques used in previous research [63] to retrieve keywords from prepared documents that are listed in the characteristics dictionary.

## Dictionary Update

After keywords were extracted with text mining software, we read through cases and manually extracted keywords or phrases present in the documents but missed by computer-aided extraction, in an effort to refine the dictionary. For example, there may be synonyms for the dictionary words and phrases not picked-up by the automated process. These missed characteristics are then added to the dictionary.

After these four steps, we start over again using a new insider’s name, but with an updated version of the dictionary. Finally, these iterations will cease once the number of updates drops and the returns become marginal.

## Characteristics Extraction

The fourteen characteristics proposed in the aforementioned literature have been classified into two groups with different extracting strategies. Group I includes behavioral precursor, predatory behavior, financial status, personal or work-related event, negative experience, ethical issues, disgruntlement, overdependence, social and cultural conflict, and rationalization. For this group, all characteristics will either be present or not. Therefore, once at least one keyword has been found in the portfolio, this characteristic will be considered present in this malicious insider case. Characteristics in Group II consist of clinical disorders, including personality disorder (narcissistic personality disorder, antisocial personality disorder, and avoidant personality disorder) and mental health disorder (disruptive mood dysregulation disorder, substance use disorder, and alcohol use disorder). The presence of a keyword only indicates the presence of one symptom for a certain disorder. We used the procedure recommended by Diagnostic and Statistical Manual of Mental Disorders (DSM-V) [4] to assess the exhibition of these characteristics. In DSM-V [4], clinical disorders are diagnosed by standardized criteria. Typically, several symptoms are described for a certain disorder and then the disorder is confirmed if the number of symptoms exhibited exceeds a certain threshold. The thresholds vary by disorder. For example, seven symptoms are described for antisocial personality disorder (e.g., impulsivity and lack of remorse). If three or more symptoms are exhibited, then the diagnostic criteria are met. Therefore, for characteristics in Group II, keywords belonging to each characteristic are first coded into symptoms of the characteristic described by DSM-V by two raters. Then when using the dictionary to scan a malicious insider’s portfolio, the presence of a keyword represents the existence of one symptom into which the keyword has been coded. Finally, if the number of symptoms identified exceeds the threshold defined by DSM-V diagnostic criteria, the disorder is considered as being exhibited for this malicious insider.

## Validity of Data Collected from Press Media and the “Distant” Assessment Method

News media data have been used in malicious insider studies to identify clinical disorders in previous research [5]. The U.S. Department of Defense’s Personnel Security Research Center (PERSEREC) has created an espionage database from publicly available data such as news media [5, 104]. Media data have been used to analyze the characteristics of employees who conducted internal fraud [3] and managers’ behavior in corporate fraud [17]. We argue that the secondary data, specifically, media data we used in this research offer a valid foundation for analyzing malicious insider characteristics.

Secondary data are data collected by someone other than the current researcher [68]. When conducting “distant” measures of subjects who are not accessible for direct assessment or when direct measurements are physically or ethically impossible [80], various materials can be used to analyze the individual differences of subjects, such as biographies, speeches, academic literature, and newspapers [86]. Materials collected from these sources might provide unobtrusive observations of subjects being investigated, thus reducing the interface of the researcher or measurement instruments with the subjects [90]. Various academic endeavors have validated that results from the “distant” measures using archival or historical data are comparable with findings resulting from traditional direct assessment methods, such as Simonton and Song’s research on the mental health of eminent people [84], Simonton’s work on the personality of U.S. presidents [82] and geniuses [79], Mumford et al.’s findings on leadership violence [61], and Ligon et al.’s study of famous leaders’ lifestyles [54].

Distant measures can all be quite useful when direct inquiry methods such as questionnaire or interviewing involves asking questions that might be sensitive, embarrassing, or even incriminating [27]. Social desirability can severely bias the response [89]. For example, Robertson argues that managers are reluctant to report their true ethical preferences, because they do not want their ethics to be observed [72].

Newspaper reports generated at the same time as the investigation of an event or an individual [47] can overcome the social desirability bias caused by direct assessment. Newspaper or press articles as a data source have been used in numerous academic endeavors about individual differences, such as DeChurch et al.’s [28] research on leadership styles, Harris’s [47] research on business ethics, and Bardi et al.’s [6] research on value and value behaviors. While some might claim that such data are incomplete or incorrect, research shows that the findings from newspaper data may be comparable with results derived from traditional direct assessments [6]. With these advantages noted, the current study uses news articles along with court documents and biographies as a data source to analyze individual differences of malicious insiders.

Admittedly, newspapers do have bias in their contents; however, we argue that bias in news articles will not be a serious issue, as discussed below. Criticism and concerns about newspaper reports are based on two aspects: news articles selectively report events associated with an individual (selection bias) and for the event they report, and information on the event is manipulatively reported (description bias) [58].

With regard to selection bias, critics maintain that many factors affect the “newsworthiness” of an event, and that coverage of events associated with an individual will be selectively biased [7]. Specifically, factors affecting selection bias include event characteristics, publisher characteristics, and issue characteristics [67].

However, in the current study we use the Google search engine to find news article entries, and our data sources are not limited to a specific newspaper or a specific time frame. Articles used in the analysis include those from local, national, and in some cases international newspapers. Samples in this research contain only malicious insider attacks that draw national media attention. The three factors affecting selection bias will not significantly reduce the media coverage of events.

For description bias, research has identified three sources of inaccurate or even erroneous description: omission, misrepresentation, and framing [57]. These factors are mitigated by our research methods; since we employ the Google search engine, multiple sources are combined as a data source. Therefore, omitted information in a specific newspaper is less likely to be omitted by all other newspapers, especially considering that we only use eminent malicious insider cases. In addition, the misrepresentation and framing problem can also be mitigated by multiple sources; various sources reporting on the same event can help to account for differences in reporting.

It should be noted that, although we argue for the validity of news articles, it does not mean distortion will not happen in these materials. Our intention is to show that we can overcome some bias in newspaper articles. We could also argue that data collected from the malicious insider himself (or herself) or authorities can also be biased because all actors have a stake in how the events are portrayed [32].

## Data About the General Population

Since we are comparing malicious insiders with the general public in the current study, in this section, we will describe the source of the data on the general population with respect to each characteristic we plan to compare. A summary of the prevalent data about the general public is presented in Table 2.

The percentage of narcissistic personality disorder in the general public was derived from the Wave 2 national epidemiological survey on alcohol and related conditions [87]. This survey involved face-to-face interviews with 34,653 subjects nationwide. It used the fully structured diagnostic interview proposed by the DSM. As reported by Stinson et al. [87], narcissistic personality disorder has a prevalence of 6.2 percent in the subjects being interviewed.

Antisocial personality disorder, avoidant personality disorder, and substance use disorder data for the general public are from the National Epidemiologic Survey conducted during 2001–2002 [40, 41]. In this survey, all regions in the United States were sampled, including the District of Columbia, Alaska, and Hawaii. The minority was oversampled to produce enough respondents. With an 81percent response rate $( n = 4 3 , 0 9 3 )$ , 3.63 percent of the general public have antisocial personality disorder and 2.63 percent have avoidant personality disorder. The respondents were interviewed using the Alcohol Use Disorder and Associated Disabilities Interview Schedule—DSM-IV version [35]. Using the same data, Grant et al. [41] reported a substance use disorder in 9.35 percent of the general public.

Table 2. Summary of General Population Data Source

<table><tr><td>Characteristics</td><td>Sources</td></tr><tr><td>Narcissistic personality disorder</td><td>Stinson et al. [87]</td></tr><tr><td>Antisocial personality disorder</td><td>Grant et al. [40]</td></tr><tr><td>Avoidant personality disorder</td><td>Grant et al. [40]</td></tr><tr><td>Disruptive mood dysregulation disorder</td><td>Copeland et al. [20]</td></tr><tr><td>Alcohol use disorder</td><td>Grant et al. [39]</td></tr><tr><td>Substance use disorder</td><td>Grant et al. [41]</td></tr><tr><td>Disgruntlement</td><td>Conference Board Mail Survey[18]</td></tr></table>

Prevalence data for disruptive mood dysregulation disorder (DMDD) were estimated using samples from three community studies. With 7,881 observations covering 3,258 subjects, the prevalence of disruptive mood dysregulation disorder ranged from .8 percent to 3.3 percent in these three communities [20]. With respect to choosing general public statistics, we intentionally chose the highest prevalence from previous research. Copeland et al. [20] found DMDD as high as 3.3 percent in segments of the general population. We used that higher proportion to represent the general public prevalence.

Prevalence of alcohol use disorder was estimated using 36,309 subjects of U.S. noninstitutionalized civilian adults [39]. Data were collected from 2012 through 2013 based on face-to-face interviews. The results show that 29.1 percent of the subjects could be diagnosed as having an alcohol use disorder at least once during their lifetime.

For disgruntlement, data were derived from a mail survey about job dissatisfaction conducted by the Conference Board on a sample of 5,000 households with a response rate of 33.5 percent [19]. The Conference Board is an independent and international research institution that has conducted job satisfaction surveys since 1987 [18]. The characteristic of disgruntlement is operationalized as job dissatisfaction in both dictionary construction and keyword search. Therefore, the results for malicious insiders and the general public are comparable.

## Methodological and Statistical Control in Comparing the Malicious Insiders Group with the General Population

We compare the different levels of prevalence for certain characteristics of malicious insiders with the general public. In research studies of the general population, structured interviews or surveys were used to diagnose disorders. However, in our research, text mining is used to extract the corresponding characteristics of malicious insiders. While the data come from different sources, we took precautions in regard to both the methodological and statistical aspects.

With respect to the diagnosis method, we use a process similar to that used in clinical settings. In the structured interview and in our method, symptoms exhibited by the subject are first grouped into diagnosis criteria, which are used to make the final diagnosis decision. In our research, keywords describing the malicious insiders are first coded into each diagnosis criterion, then the presence of single or multiple keywords themselves will not be considered as the indicating the existence of a clinical disorder. The presence of a certain disorder will only be confirmed if the number of diagnosis criteria meets the limit required by DSM-V.

Statistically, we employ the Fisher’s exact test [36] to check for difference in proportions within two independent samples. This test has been criticized as being too conservative and as sometimes not finding results that are are really there [8, 25, 53]. Combined with the fact that we intentionally choose the highest percentage among reported results about general public, these precautions effectively bridge the gap between different data sources for the general public and for malicious insiders.

## Analysis and Results

In this section, we first report on the data collection and dictionary refinement results. Then we present the characteristic extraction process and conclude by presenting newly identified characteristics that we did not see in the literature.

## Data Collection

We randomly chose 133 malicious insider threat cases for the current study. All the malicious insiders were found guilty and convicted by a U.S. court. We see this as a check to ensure all our cases were indeed malicious insider incidents.

## Dictionary Construction

We extracted 380 keywords from malicious insiders’ attributes proposed in the extant literature, we refined 345 characteristics from these keywords using the characteristic dictionary. Using two example statements below, we describe the process. The first statement is an example of characteristics in Group I and the second statement is an illustration of characteristics in Group II.

## Example Statement:

1. Disgruntlement: Employee observed to be dissatisfied in current position; chronic indications of discontent, such as strong negative feelings about being passed over for a promotion or being underpaid, undervalued; may have a poor fit with current job [44].

2. Antisocial Personality Disorder: The employee engages in persistent lying or stealing, disregard for the safety of self or others, and possessing a superficial charm or wit [77].

In the first example statement, three keywords/phrases are extracted: “dissatisfied,” “discontent,” and “passed over for a promotion,” which belong to the characteristic of disgruntlement. After these three records are added to the dictionary, they are used to extract the same keywords for cases examined later. If the keyword is found, we consider it a “hit” for the corresponding characteristic.

Table 3. Part of Characteristic Dictionary

<table><tr><td>Characteristic ID</td><td>Keywords</td><td>Characteristic/diagnosis criteria</td><td>Origins</td></tr><tr><td>1</td><td>Dissatisfied</td><td>Disgruntlement</td><td>Example Statement 1</td></tr><tr><td>2</td><td>Discontent</td><td>Disgruntlement</td><td>Example Statement 1</td></tr><tr><td>2</td><td>Pass over for a promotion</td><td>Disgruntlement</td><td>Example Statement 1</td></tr><tr><td>3</td><td>Lie</td><td>ASPD2</td><td>Example Statement 2</td></tr><tr><td>4</td><td>Disregard the safety</td><td>ASPD5</td><td>Example Statement 2</td></tr></table>

In the second example statement, two keywords are extracted: “lying” and “disregard.” These keywords are coded into the second and fifth diagnosis criteria of antisocial personality disorder (ASPD) in DMS-V [4]. The second criterion is “deceitfulness, as indicated by repeated lying, use of aliases, or conning others for personal profit or pleasure” and the fifth criterion is “reckless disregard for safety of self or others.” When used in scanning the malicious insider portfolios, if the keyword is found, we consider it a “hit” for the corresponding diagnosis criteria. The extraction result for these two statements is shown in Table 3.

## Final Coding

Using the final dictionary, thematic analysis was used to code all the keywords. Given the existence of a predefined set of characteristics, a deductive approach was used to code the keywords [22]. The coding started with two separate coders, separately coding 10 percent of the keywords for the identified overarching characteristics of antisocial personality disorder, narcissistic personality disorder, avoidant personality disorder, alcohol use disorder, and disruptive mood dysregulation disorder, and then comparing results. Cohen’s kappa coefficient for interrater reliability between the raters was 0.84, indicating excellent [37] to almost perfect [52] agreement between the raters. Afterward, the two coders categorized each keyword within its respective higher category into the individual characteristic codes within each category. Cohen’s kappa coefficient was 0.97, indicating excellent to almost perfect alignment. At this point, one of the two raters coded the rest of the keywords.

## Characteristic Extraction Results

The proportion of malicious insiders identified with substance use disorder is significantly greater than in the overall population, $( p < 0 . 0 0 1 )$ with the proportion confidence interval from 0.27 to 0.45 greater for malicious insiders, supporting P3-2. The proportion of malicious insiders with antisocial disorder is significantly greater than in the overall population, $( p < 0 . 0 0 1 )$ , supporting P1-2, the proportion confidence interval is only 0.01 to 0.13 greater for malicious insiders. The proportion of malicious insiders who are dissatisfied is significantly greater than in the overall population, $( p < 0 . 0 0 1 )$ with the proportion confidence interval from 0.37 to 0.47 greater for malicious insiders, supporting P4.

Table 4. Propositions Comparison Between Malicious Insiders Sample and the General Population

<table><tr><td rowspan="2">Prop.</td><td rowspan="2">Characteristics</td><td colspan="2">Study</td><td colspan="2">Population</td><td colspan="3">Difference test</td><td rowspan="2">Support</td></tr><tr><td>Proportion</td><td>Sample</td><td>Proportion [source]</td><td>Sample</td><td>p-value</td><td colspan="2">Confidence interval</td></tr><tr><td>P1-1</td><td>Narcissistic personality disorder</td><td>.023</td><td></td><td>.062 [87]</td><td>34653</td><td>0.09</td><td>-0.01</td><td>-0.07</td><td>No</td></tr><tr><td>P1-2</td><td>Antisocial personality disorder</td><td>.105</td><td></td><td>.036 [40]</td><td>43093</td><td>&lt;0.001</td><td>0.01</td><td>0.13</td><td>Yes</td></tr><tr><td>P1-3</td><td>Avoidant personality disorder</td><td>.023</td><td></td><td>.024 [40]</td><td>43093</td><td>1</td><td>-0.03</td><td>0.03</td><td>No</td></tr><tr><td>P2</td><td>Disruptive mood dysregulation disorder</td><td>.015</td><td>133</td><td>.033 [20]</td><td>918</td><td>0.40</td><td>-0.05</td><td>0.01</td><td>No</td></tr><tr><td>P3-1</td><td>Alcohol use disorder</td><td>.010</td><td></td><td>.291 [39]</td><td>36,309</td><td>&lt;0.001</td><td>-0.26</td><td>-0.30</td><td>No</td></tr><tr><td>P3-2</td><td>Substance use disorder</td><td>.451</td><td></td><td>.094 [41]</td><td>43093</td><td>&lt;0.001</td><td>0.27</td><td>0.45</td><td>Yes</td></tr><tr><td>P4</td><td>Disgruntlement</td><td>.940</td><td></td><td>.523 [19]</td><td>1673</td><td>&lt;0.001</td><td>0.37</td><td>0.47</td><td>Yes</td></tr></table>

Conversely, the proportion of malicious insiders with narcissistic personality disorder, avoidant personality disorder, and disruptive mood dysregulation disorder is not significantly greater than in the overall population, $( p = 0 . 0 9 ,$ 1, and 0.40 respectively), which does not support P1-1, P1-3, or P2. While significant, the proportion of alcohol use disorder among malicious insiders is significantly less than in the overall population, $( p < 0 . 0 0 1 )$ with the proportion confidence interval from 0.26 to 0.30 less for malicious insiders, contrary to P4. Detailed statistics could be found in Table 4.

If we lower the number of diagnosis criteria by 1, P1-3 and P2 are supported with regard to avoidant personality disorder and dysregulation disorder, as seen in Table 5.

Under the revised criteria, the proportion of malicious insiders with avoidant personality disorder is significantly higher than in the general public, $( p < 0 . 0 0 1 )$ with the proportion confidence interval from 0.02 to 0.13, supporting P1-3. The proportion of malicious insiders with disruptive mood dysregulation disorder is significantly greater than in the overall population, $( p = 0 . 0 0 3 )$ , supporting P2, the proportion confidence interval is 0.003 to 0.11 greater for malicious insiders.

On the contrary, the proportion of malicious insiders with narcissistic personality disorder is still not significantly different from the proportion in the general public $( p = 0 . 6 5 )$ . Also, the proportion of malicious insiders with alcohol use disorder is still significantly less than the proportion in the general public, $( p < 0 . 0 0 1 )$ with the proportion confidence interval of 0.09 to 0.22 less than in general public.

Several issues should be noted in the results of our analysis. First, when strictly applying the number of symptoms required by the DSM diagnosis criteria, most of the propositions regarding personality or mental health disorders are not supported. However, if we just lower the required number by one, all of them except narcissistic and alcohol use disorders are significant. This might because the diagnosis criteria are applied more strictly in our analysis than in a clinical diagnosis; in our study, one symptom is labeled as only one diagnosis criterion. In clinical practice, one symptom might infer multiple diagnosis criteria. For example, if a subject is described as “always drunk,” then it might indicate both (1) the subject is consuming a large amount of alcohol, and (2) the subject is spending a lot of time consuming alcohol and recovering from its effects. However, in our research, if the keyword “always drunk” is found in the portfolio, it is only classified a one criterion.

In Grant et al.’s research [41], substance use disorder includes alcohol use disorder. However, in our research, alcohol use disorder is excluded from substance use disorder. The proportion of malicious insiders having a substance use disorder is still higher than the proportions in Grant et al.’s research, indicating additional support for our P3-2.

## Discussion and Limitations

We learned that text mining can be used in a malicious insider study; specifically, the information extraction techniques can extract characteristics based on our dictionary.

Table 5. Propositions Comparison Between Malicious Insiders Sample and the General Population (lowering diagnosis criteria by 1)

<table><tr><td rowspan="2">Prop.</td><td rowspan="2">Characteristics</td><td colspan="2">Study</td><td colspan="2">Population</td><td colspan="3">Difference test</td><td rowspan="2">Support</td></tr><tr><td>Proportion</td><td>Sample</td><td>Proportion [source]</td><td>Sample</td><td>p-value</td><td colspan="2">Confidence interval</td></tr><tr><td>P1-1</td><td>Narcissistic personality disorder</td><td>.075</td><td></td><td>.062 [87]</td><td>34653</td><td>0.65</td><td>-0.04</td><td>0.06</td><td>No</td></tr><tr><td>P1-2</td><td>Antisocial personality disorder</td><td>.421</td><td></td><td>.036 [40]</td><td>43093</td><td>&lt;0.001</td><td>0.30</td><td>0.47</td><td>Yes</td></tr><tr><td>P1-3</td><td>Avoidant personality disorder</td><td>.098</td><td></td><td>.024 [40]</td><td>43093</td><td>&lt;0.001</td><td>0.02</td><td>0.13</td><td>Yes</td></tr><tr><td>P2</td><td>Disruptive mood dysregulation disorder</td><td>.090</td><td>133</td><td>.033 [20]</td><td>918</td><td>0.003</td><td>0.003</td><td>0.11</td><td>Yes</td></tr><tr><td>P3-1</td><td>Alcohol use disorder</td><td>.135</td><td></td><td>.291 [39]</td><td>36,309</td><td>&lt;0.001</td><td>-0.09</td><td>-0.22</td><td>No</td></tr><tr><td>P3-2</td><td>Substance use disorder</td><td>.451</td><td></td><td>.094 [41]</td><td>43093</td><td>&lt;0.001</td><td>0.27</td><td>0.45</td><td>Yes</td></tr><tr><td>P4</td><td>Disgruntlement</td><td>.940</td><td></td><td>.523 [19]</td><td>1673</td><td>&lt;0.001</td><td>0.37</td><td>0.47</td><td>Yes</td></tr></table>

More important, it enabled us to validate, and in some cases question, characteristics of malicious insiders found in previous research.

When compared to the general population, malicious insiders exhibited greater proportions of most of the characteristics posited, thus confirming the characteristics found in previous research. Malicious insiders have more personality problems, mental health disorders, and substance abuse problems. Interestingly, one trait or characteristic that seems to come up often in the previous literature is narcissistic personality disorder. However, our findings suggest that malicious insiders actually exhibit less narcissism than people in the general population. This may be for a number of reasons. First, narcissism suggests that individuals want positive attention and recognition. Carrying out a malicious act would be contrary to their objectives. Second, as Deluga [29] notes, narcissism is not necessarily a destructive trait: in an extensive study of biographies of U.S. presidents, many were found to be narcissistic.

As shown in Table 6, all characteristics proposed by previous research are identified in our cases, however, with different commonalities. In this study we only offer propositions about characteristics in which we could find data on the greater population. Nonetheless, out text-mining techniques enable us to identify the most prevalent characteristics from a large sample. Among these characteristics, behavioral precursors, predatory behavior, personal or work-related events, and financial status were found in all cases. It remains to be seen how these events influence the perpetration of incidents by malicious insiders.

More than 90 percent of the malicious insiders in our study have experienced mental health disorder symptoms such as paranoia and gender confusion. Other prominent traits include emotional instability (i.e., temper outbursts), ethical issues such as lying, lack of empathy, or disregard for others’ needs, disgruntlement such as dissatisfaction with the current job, and personality disorder symptoms such as arrogance, fantasizing behavior, or manipulative behaviors. Almost 90 percent of malicious insiders exhibit social isolation or felt that the organization they attacked is overly dependent on them. Of the other characteristics noted in the previous literature, rationalization and social isolation score relatively low.

Table 6. Frequency of Characteristics in Previous Research

<table><tr><td>Characteristics</td><td>Number of cases</td><td>Percentage of total cases</td></tr><tr><td>Predatory behavior</td><td>133</td><td>100</td></tr><tr><td>Personal or work-related event</td><td>133</td><td>100</td></tr><tr><td>Negative experience</td><td>133</td><td>100</td></tr><tr><td>Financial status</td><td>133</td><td>100</td></tr><tr><td>Behavioral precursor</td><td>133</td><td>100</td></tr><tr><td>Emotional issues</td><td>132</td><td>99</td></tr><tr><td>Ethical issues</td><td>130</td><td>98</td></tr><tr><td>Mental health symptoms</td><td>128</td><td>96</td></tr><tr><td>Disgruntlement</td><td>125</td><td>94</td></tr><tr><td>Personality disorder symptoms</td><td>125</td><td>94</td></tr><tr><td>Social isolation</td><td>118</td><td>89</td></tr><tr><td>Overdependence</td><td>118</td><td>89</td></tr><tr><td>Rationalization</td><td>88</td><td>66</td></tr><tr><td>Social and cultural conflict</td><td>40</td><td>30</td></tr></table>

Table 7. Frequency of Newly Found Characteristics

<table><tr><td>Characteristics</td><td>Number of cases</td><td>Percentage of total cases</td></tr><tr><td>Dedication to family or work</td><td>122</td><td>92</td></tr><tr><td>Agreeable</td><td>121</td><td>91</td></tr><tr><td>Professional</td><td>119</td><td>89</td></tr><tr><td>High academic performance</td><td>118</td><td>89</td></tr><tr><td>Successful career</td><td>92</td><td>69</td></tr><tr><td>Intellectual</td><td>88</td><td>66</td></tr><tr><td>Nonimpulsive</td><td>86</td><td>65</td></tr><tr><td>Love affairs</td><td>85</td><td>64</td></tr><tr><td>Well-trained</td><td>83</td><td>62</td></tr><tr><td>Reputation problem</td><td>66</td><td>50</td></tr></table>

We also identified other characteristics not found in previous research. Interestingly, some positive characteristics were revealed in our study such as: dedication to family or work (92 percent) and once being described as agreeable (91 percent). Since these were not reported in previous studies, they require further investigation. A summary of the new characteristics is presented in Table 7.

## Limitations of the Current Study

The current study employs a keyword-based method to extract characteristics from text; however, some keywords represent different meanings in different contexts. For example, the keyword “bully” is defined as a characteristic with respect to relations with coworkers. However, the appearance of “bully” might indicate that the subject bullies others, the subject is bullied, or the subject was bullied in his/her childhood. As we continue to refine the dictionary, these issues should wane.

The primary focus of this study is to empirically validate characteristics or traits of malicious insiders. Although states such as events, activities, and emotions could not be validated for commonalities in this study, they could be useful in future research. An abnormality-based detection approach in which a set of normal events, activities, or emotions are defined might aid in the usefulness of examining states. Anything outside the defined parameters could trigger an alarm.

Furthermore, we recognize that data (text) in our sample are based on news reports, court documents, and other third-party documents. It is possible that some characteristics were left out in the interview and reporting process. However, we believe our sample size of 133 eminent cases is more than enough to mitigate problems due to omitted information. In addition, due to the challenge of finding relevant data, we compared our text-mined data on malicious insiders to surveybased data on the general population. However, as noted, we took precautions in order to bridge the gap between the two data sets.

We stress that this research is in its infancy and not to a point where prediction of malicious insiders is possible. No single characteristic can be used to predict a malicious insider. Rather, we must continue to refine our methods and determine whether some set of the characteristics can be used for prediction.

## Implications for Research and Practitioners

This study sought to validate a number of characteristics of malicious insiders suggested in previous research. Much of the previous research was either based on single cases studies or worked with rather small sample sizes. With our large sample size of 133 cases we believe scholars can have increased confidence in the validity of the characteristics in which we found support.

As for practitioners, malicious insiders are a significant threat to organizations because of their large potential impact. While we stress that we are nowhere near capable of predicting whether a person is a malicious insider, the validation of these characteristics may one day lead to better tools and techniques for screening employees. Additional research on the state-based characteristics may also prove useful.

## Future Orientations

Future research will focus on improving the characteristic extraction algorithm. One possible approach is to employ a rule-based method instead of extracting characteristics using keywords. Specifically, we propose to build rules that could represent a set of context. An example of the “bully” rule proposed would be “[set1] bully [set2],” in which set1 contains words such as insider’s last name, full name, and personal pronouns. Set 2 contains words such as peer, coworker, and colleague. Then if combination “[set1] bully [set2]” appears in a document, it is definitely a hit for the subject bullies his/her coworkers.

Another limitation concerns the subjects in the current study. While this study investigated “eminent” malicious insiders who are widely reported, we are also interested in malicious insiders who do not draw such attention and cause less severe consequences. In future studies we would like to work closely with the practitioners who are willing to share the data, in order to fully understand the characteristics of malicious insiders.

We will also examine the impact of states on malicious insiders. While this study focused on traits, we believe that states may have a moderating effect on malicious insider intent and action. Future work will consider the interaction between states and traits. Additional future research will seek to identify any interaction effect between traits. Finally, the characteristics we validated have the potential to be used as input for autonomous agents to allow for better screening of those individuals who might try to purposely conceal information and carry out insider attacks.

## Conclusion

The study of malicious insiders is extremely important due to the large negative impact on organizations. Previous studies proposed characteristics that might be exhibited by malicious insiders, paving the way for future research on this group. However, these studies in the field are mostly based on a small number of cases or experts’ opinions without empirical testing on a large number of real-world cases. In this study we investigated the sample of malicious insiders who were convicted by U.S. courts. Furthermore, we examined and validated a number of characteristics of malicious insiders noted in the extant literature. We also found some new, candidate characteristics that warrant further study. These findings validate some of the characteristics proposed in previous research, offering a solid foundation for future academic endeavors.

The use of text mining to examine a large sample of malicious insider cases proved to be effective and efficient. With refinement, it should become even more so. Mitigating the threat of malicious insiders is of utmost importance, and continued research in this domain is essential.

## NOTE

1. Thanks to one of the reviewers for prompting this example.

## REFERENCES

1. Adams, J.S. Inequity in social exchange. In L. Berkowitz (ed.), Advances in Experimental Social Psychology. New York: Academic Press, 1965, pp. 267–299.

2. Allport, G.W., and Odbert, H.S. Trait-names: A psycho-lexical study. Psychological Monographs, 47, 1 (1936), 1–38.

3. Andon, P.; Free, C.; and Scard, B. Pathways to accountant fraud: Australian evidence and analysis. Accounting Research Journal, 28, 1 (2015), 10–44.

4. APA. Diagnostic and Statistical Manual of Mental Disorders. Arlington, VA: American Psychiatric Publishing, 2013.

5. Band, S.R.; Cappelli, D.M.; Fischer, L.F.; Moore, A.P.; Shaw, E.D.; and Trzeciak, R.F. Comparing insider IT sabotage and espionage: A model-based analysis. Carnegie Mellon University, 2006.

6. Bardi, A.; Calogero, R.M.; and Mullen, B. A new archival approach to the study of values and value-behavior relations: Validation of the value lexicon. Journal of Applied Psychology, 93, 3 (2008), 483–497.

7. Barranco, J., and Wisler, D. Validity and systematicity of newspaper data in event analysis. European Sociological Review, 15, 3 (1999), 301–322.

8. Berkson, J. In dispraise of the exact test: Do the marginal totals of the 2X2 table contain relevant information respecting the table proportions? Journal of Statistical Planning and Inference, 2, 1 (1978), 27–42.

9. Bishop, M., Gollmann, D.; Hunker, J.; and Probst, C.W. Countering insider threats. In Dagstuhl Seminar Proceedings, Dagstuhl, Germany, Number 08302, 2008. Available: http:// drops.dagstuhl.de/opus/volltexte/2008/1793/pdf/08302.SWM.1793.pdf

10. Bono, J.E., and Ilies, R. Charisma, positive emotions and mood contagion. Leadership Quarterly, 17, 4 (2006), 317–334.

11. Brackney, R.C., and Anderson, R.H. Understanding the insider Threat. Proceedings of a March 2004 Workshop. Santa Monica, CA: RAND, 2004.

12. Chakraborty, G.; Pagolu, M.; and Garla, S. Text Mining and Analysis: Practical Methods, Examples, and Case Studies Using SAS. Cary, NC: SAS Institute, 2014.

13. Chaplin, W.F.; John, O.P.; and Goldberg, L.R. Conceptions of states and traits: Dimensional attributes with ideals as prototypes. Journal of Personality and Social Psychology, 54, 4 (1988), 541–557.

14. Chatterjee, S.; Sarker, S.; and Valacich, J.S. The behavioral roots of information systems security: Exploring key factors related to unethical IT use. Journal of Management Information Systems, 31, 4 (2015), 49–87.

15. Chen, Y.; Ramamurthy, K.; and Wen, K.-W. Organizations’ Information Security Policy Compliance: Stick or Carrot Approach? Journal of Management Information Systems, 29, 3 (2012), 157–188.

16. Claycomb, W.R.; Huth, C.L.; Phillips, B.; Flynn, L.; and McIntire, D. Identifying indicators of insider threats: Insider IT sabotage. In Proceedings of Security Technology (ICCST), 2013 Forty-Seventh International Carnahan Conference. IEEE, 2013, pp. 1–5.

17. Cohen, J.; Ding, Y.; Lesage, C.; and Stolowy, H. Corporate fraud and managers’ behavior: Evidence from the press. In R. Cressy, D. Cumming, and C. Mallin (eds.), Entrepreneurship, Governance and Ethics. Netherlands: Springer, 2012, pp. 271–315.

18. Conference Board. www.conference-board.org/(accessed on March 14, 2016).

19. Cheng, B.; Kan, M.; Lavanon, G.; and Ray, R. Conference Board Job Satisfaction: 2014 Edition. www.conference-board.org/publications/publicationdetail.cfm?publicationid=2785 (accessed on March 14, 2016).

20. Copeland, W.E.; Angold, A.; Costello, E.J.; and Egger, H. Prevalence, comorbidity, and correlates of DSM-5 proposed disruptive mood dysregulation disorder. American Journal of Psychiatry, 170, 2 (2013), 173–179.

21. Centre for the Protection of National Infrastructure. CPNI Data Collection Study. 2013. www.cpni.gov.uk/advice/personnel-security1/insider-threats/(accessed on May 15, 2016).

22. Crabtree, B.F., and Miller, W.L. Doing Qualitative Research. Thousand Oaks, CA: Sage, 1999.

23. Cressey, D.R. Other People’s Money: A Study of the Social Psychology of Embezzlement. New York: Free Press, 1953.

24. Crossler, R.E.; Johnston, A.C.; Lowry, P.B.; Hu, Q.; Warkentin, M.; and Baskerville, R. Future directions for behavioral information security research. Computers and Security, 32 (2013), 90–101.

25. D’Agostino, R.B.; Chase, W.; and Belanger, A. The appropriateness of some common procedures for testing the equality of two independent binomial populations. American Statistician, 42, 3 (1988), 198–202.

26. D’Arcy, J.; Herath, T.; and Shoss, M.K. Understanding employee responses to stressful information security requirements: A coping perspective. Journal of Management Information Systems, 31, 2 (2014), 285–318.

27. Dalton, D.R., and Metzger, M.B. Towards candor, cooperation, and privacy in applied business ethics research: The randomized response technique (RRT). Business Ethics Quarterly, 2, 2 (1992), 207–221.

28. DeChurch, L.A.; Burke, C.S.; Shuffler, M.L.; Lyons, R.; Doty, D.; and Salas, E. A historiometric analysis of leadership in mission critical multiteam environments. Leadership Quarterly, 22, 1 (2011), 152–169.

29. Deluga, R.J. Relationship among American presidential charismatic leadership, narcissism, and rated performance. Leadership Quarterly, 8, 1 (1997), 49–65.

30. Dinh, J.E.; Lord, R.G.; Gardner, W.L.; Meuser, J.D.; Liden, R.C.; and Hu, J. Leadership theory and research in the new millennium: Current theoretical trends and changing perspectives. Leadership Quarterly, 25, 1 (2014), 36–62.

31. Dumais, S.T. Latent semantic analysis. Annual Review of Information Science and Technology, 38, 1 (2004), 188–230.

32. Earl, J.; Martin, A.; McCarthy, J.D.; and Soule, S.A. The use of newspaper data in the study of collective action. Annual Review of Sociology, 30 (2004), 65–80.

33. Etkin, A., and Wager, T.D. Functional neuroimaging of anxiety: A meta-analysis of emotional processing in PTSD, social anxiety disorder, and specific phobia. American Journal of Psychiatry, 164, 10 (2007), 1476–1488.

34. First, M.B. Diagnostic and Statistical Manual-Text Revision. Washington, DC: American Psychiatric Association, 2000.

35. First, M.B. Diagnostic and Statistical Manual of Mental Disorders. Washington, DC: American Psychiatric Association, 1994.

37. Fleiss, J.L.; Levin, B.; and Paik, M.C. Statistical Methods for Rates and Proportions. Hoboken, NJ: Wiley, 2013.

38. Gelles, M. Exploring the Mind of the Spy. 2005. www.itsi-inc.com/opsec/Treason/ Mind.htm (accessed on May 15, 2016).

Results from the National Epidemiologic Survey on Alcohol and Related Conditions III. JAMA Psychiatry, 72, 8 (2015), 757–766.

40. Grant, B.F.; Hasin, D.S.; Stinson, F.S.; Dawson, D.A.; Chou, S.P.; Ruan, W.J.; and Pickering, R.P. Prevalence, correlates, and disability of personality disorders in the United States: Results from the National Epidemiologic Survey on Alcohol and Related Conditions. The Journal of Clinical Psychiatry, 65, 7 (2004), 478–958.

41. Grant, B.F.; Stinson, F.S.; Dawson, D.A.; Chou, S.P.; Dufour, M.C.; Compton, W.; Pickering, R.P.; and Kaplan, K. Prevalence and co-occurrence of substance use disorders and independentmood and anxiety disorders: Results from the National Epidemiologic Survey on Alcohol and Related Conditions. Archives of General Psychiatry, 61, 8 (2004), 807–816.

42. Grant, B.F.; Stinson, F.S.; Dawson, D.A.; Chou, S.P.; Ruan, W.J.; and Pickering, R.P. Co-occurrence of 12-month alcohol and drug use disorders and personalitydisorders in the United States: Results from the National Epidemiologic Survey on Alcohol and Related Conditions. Archives of General Psychiatry, 61, 4 (2004), 361–368.

43. Greitzer, F.L., and Frincke, D.A. Combining traditional cyber security audit data with psychosocial data: Towards predictive modeling for insider threat mitigation. In C.W. Probst, J. Hunker, D. Gollmann, and M. Bishop (eds.), Insider Threats in Cyber Security. New York, NY: Springer, 2010, pp. 85–113.

44. Greitzer, F.L.; Kangas, L.J.; Noonan, C.F.; Brown, C.R.; and Ferryman, T. Psychosocial modeling of insider threat risk based on behavioral and word use analysis. e-Service Journal, 9, 1 (2013), 106–138.

45. Greitzer, F.L.; Paulson, P.; Kangas, L.; Edgar, T.; Zabriskie, M.; Franklin, L.; and Frincke, D.A. Predictive modelling for insider threat mitigation. Pacific Northwest National Laboratory, Richland, WA, Technical Report PNNL-60737, 2008, pp. 1–13.

46. Guo, K.H.; Yuan, Y.; Archer, N.P.; and Connelly, C.E. Understanding nonmalicious security violations in the workplace: A composite behavior model. Journal of Management Information Systems, 28, 2 (2011), 203–236.

47. Harris, H. Content analysis of secondary data: A study of courage in managerial decision making. Journal of Business Ethics, 34, 3–4 (2001), 191–208.

48. Hu, Q.; Xu, Z.; Dinev, T.; and Ling, H. Does deterrence work in reducing information security policy abuse by employees? Communications of the ACM, 54, 6 (2011), 54–60.

49. Hunker, J., and Probst, C.W. Insiders and insider threats: An overview of definitions and mitigation techniques. Journal of Wireless Mobile Networks, Ubiquitous Computing, and Dependable Applications, 2, 1 (2011), 4–27.

50. Johnson, P.R. Trusted Insiders Are Committing Fraud and Embezzlement Within Organizations: Is There a Connection to Addiction, as the Motivating Factor for Their Illegal Activities? Monterey, CA: Naval Postgraduate School, 2014.

51. Kamoun, F., and Nicho, M. Multiple case study approach to identify aggravating variables of insider threats in information systems. Communications of the Association for Information Systems, 35, 1 (2014), 1–23.

52. Landis, J.R., and Koch, G.G. The measurement of observer agreement for categorical data. Biometrics, 33, 1 (1977), 159–174.

53. Liddell, D. Practical tests of 2 × 2 contingency tables. Statistician, 25, 4 (1976), 295–304.

54. Ligon, G.S.; Harris, D.J.; and Hunter, S.T. Quantifying leader lives: What historiometric approaches can tell us. Leadership Quarterly, 23, 6 (2012), 1104–1133.

55. Lord, R.G., and Hall, R.J. Identity, deep structure and the development of leadership skill. Leadership Quarterly, 16, 4 (2005), 591–615.

56. Maasberg, M.; Warren, J.; and Beebe, N.L. The dark side of the insider: Detecting the insider threat hrough examination of dark triad personality traits. In Forty-Eighth Hawaii International Conference on System Sciences (HICSS), Kauai, HI. IEEE, January 2015, pp. 3518–3526.

57. McCarthy, J.D., and McPhail, C. The institutionalization of protest in the United States. In D.S. Meyer and S. Tarrow (eds.), The Social Movement Society: Contentious Politics for a New Century. Oxford: Rowman and Littlefield, 1998, pp. 83–110.

58. McCarthy, J.D.; McPhail, C.; Smith, J.; and Crishock, L.J. Electronic and print media representations of Washington DC demonstrations, 1982 and 1991: A demography of description bias. In D.S. Meyer and S. Tarrow (eds.), Acts of Dissent: New Developments in the Study of Protest. Oxford: Rowman and Littlefield, 1999, pp. 113–130.

59. Moore, A.P.; Cappelli, D.M.; and Trzeciak, R.F. The “big picture” of insider IT sabotage across US critical infrastructures. In S.J. Stolfo, S.M. Bellovin, S. Hershkop, A.D. Keromytis, S. Sinclair, and S. Smith (eds.), Insider Attack and Cyber Security. Pittsburgh, PA: Springer, 2008, pp. 17–52.

60. Morgeson, F.P.; Reider, M.H.; and Campion, M.A. Selecting individuals in team settings: The importance of social skills, personality characteristics, and teamwork knowledge. Personnel Psychology, 58, 3 (2005), 583–611.

61. Mumford, M.D.; Espejo, J.; Hunter, S.T.; Bedell-Avers, K.E.; Eubanks, D.L.; and Connelly, S. The sources of leader violence: A comparison of ideological and non-ideological leaders. Leadership Quarterly, 18, 3 (2007), 217–235.

62. Murphy, P.R., and Dacin, M.T. Psychological pathways to fraud: Understanding and preventing fraud in organizations. Journal of Business Ethics, 101, 4 (2011), 601–618.

63. Nahm, U.Y., and Mooney, R.J. Text mining with information extraction. In AAAI 2002 Spring Symposium on Mining Answers from Texts and Knowledge Bases, Palo Alto, CA, March 2002, pp. 60–67.

64. Northouse, P.G. Leadership: Theory and Practice. Los Angeles: Sage, 2015.

65. Noy, N.F., and McGuinness, D.L. Ontology development 101: A guide to creating your first ontology. Stanford Knowledge Systems Laboratory Technical Report KSL-01-05 and Stanford Medical Informatics Technical Report SMI-2001-0880, 2001.

66. Nurse, J.R.; Buckley, O.; Legg, P.A.; Goldsmith, M.; Creese, S.; Wright, G.R.; and Whitty, M. Understanding insider threat: A framework for characterising attacks. In IEEE Security and Privacy Workshops (SPW), San Jose, CA. IEEE, May 2014, pp. 214–228.

67. Oliver, P.E., and Myers, D.J. How events enter the public sphere: Conflict, location, and sponsorship in local newspaper coverage of public events. American Journal of Sociology, 105, 1 (1999), 38–87.

68. Pienta, A.M.; O’Rourke, J.M.; and Franks, M.M. Getting started: Working with secondary data. In K.H. Trzesniewski, M.B. Donnellan, and R.E. Lucas (eds.), Secondary Data Analysis: An Introduction for Psychologists. Washington, DC: American Psychological Association, 2011, pp. 13–25.

69. Post, F. Creativity and psychopathology. British Journal of Psychiatry, 165, 1 (1994), 22–34.

70. Predd, J.; Pfleeger, S.L.; Hunker, J.; and Bulford, C. Insiders behaving badly. IEEE Security and Privacy, 6, 4 (2008), 66–70.

71. Randazzo, M.; Keeney, M.; Kowalski, E.; Cappelli, D.; and Moore, A. Insider threat study: Illicit cyber activity in the banking and finance sector. (CMU/SEI-2004-TR-021), Software Engineering Institute, Carnegie Mellon University, 2005. Retrieved August 16, 2016 from http://resources.sei.cmu.edu/library/asset-view.cfm?AssetID=7227

72. Robertson, D.C. Empiricism in business ethics: Suggested research directions. Journal of Business Ethics, 12, 8 (1993), 585–599.

73. Schultz, E.E. A framework for understanding and predicting insider attacks. Computers and Security, 21, 6 (2002), 526–531.

74. Shaw, E.; Ruby, K.; and Post, J. The insider threat to information systems: The psychology of the dangerous insider. Security Awareness Bulletin, 2, 98 (1998), 1–10.

75. Shaw, E.D., and Fischer, L.F. Ten tales of betrayal: The threat to corporate infrastructure by information technology insiders analysis and observations. Defense Personnel Security Research Center (PERSEREC), Monterey, CA, Technical Report 05–13, 2005.

76. Shaw, E.D., and Stock, H.V. Behavioral risk indicators of malicious insider theft of intellectual property: Misreading the writing on the wall. White Paper, Symantec. Mountain View, CA, 2011.

77. Shechter, O.G., and Lang, E.L. Identifying personality disorders that are security risks: Field test results. (No. PERSEREC-TR-11-05). Defense Personnel Security Research Center, Monterey, CA, 2011.

78. Shropshire, J. A canonical analysis of intentional information security breaches by insiders. Information Management and Computer Security, 17, 4 (2009), 296–310.

79. Simonton, D.K. Historiometric studies of genius. In D.K. Simonton (ed.), The Wiley Handbook of Genius. Oxford: Wiley, 2014, pp. 87–106.

80. Simonton, D.K. Historiometry in personality and social psychology. Social and Personality Psychology Compass, 3, 1 (2009), 49–63.

81. Simonton, D.K. More method in the mad-genius controversy: A historiometric study of 204 historic creators. Psychology of Aesthetics, Creativity, and the Arts, 8, 1 (2014), 53–61.

82. Simonton, D.K. Presidential personality: Biographical use of the Gough Adjective Check List. Journal of Personality and Social Psychology, 51, 1 (1986), 149–160.

83. Simonton, D.K. Significant samples: The psychological study of eminent individuals. Psychological Methods, 4, 4 (1999), 425–451.

84. Simonton, D.K., and Song, A.V. Eminence, IQ, physical and mental health, and achievement domain Cox’s 282 geniuses revisited. Psychological Science, 20, 4 (2009), 429–434.

85. Siponen, M., and Vance, A. Neutralization: New insights into the problem of employee information systems security policy violations. MIS Quarterly, 34, 3 (2010), 487–502.

86. Spangler, W.D.; Gupta, A.; Kim, D.H.; and Nazarian, S. Developing and validating historiometric measures of leader individual differences by computerized content analysis of documents. Leadership Quarterly, 23, 6 (2012), 1152–1172.

87. Stinson, F.S.; Dawson, D.A.; Goldstein, R.B.; Chou, S.P.; Huang, B.; Smith, S.M.; Ruan, W.J.; Pulay, A.J.; Saha, T.D.; and Pickering, R.P. Prevalence, correlates, disability, and comorbidity of DSM-IV narcissistic personality disorder: Results from the Wave 2 National Epidemiologic Survey on Alcohol and Related Conditions. Journal of Clinical Psychiatry, 69, 7 (2008), 1033–1045.

88. Suedfeld, P., and Bluck, S. Changes in integrative complexity accompanying significant life events: Historical evidence. Journal of Personality and Social Psychology, 64, 1 (1993), 124–130.

89. Thomas, K.W., and Kilmann, R.H. The social desirability variable in organizational research: An alternative explanation for reported findings. Academy of Management Journal, 18, 4 (1975), 741–752.

90. Trochim, W.; Donnelly, J.; and Arora, K. Research Methods: The Essential Knowledge Base. Boston, MA: Nelson Education, 2015.

91. Turner, J.T., and Gelles, M. Threat Assessment: A Risk Management Approach. New York: Routledge, 2012.

92. Twyman, N.W.; Lowry, P.B.; Burgoon, J.K.; and Nunamaker, J.F., Jr. Autonomous scientifically controlled screening systems for detecting information purposely concealed by individuals. Journal of Management Information Systems, 31, 3 (2014), 106–137.

93. Uhl-Bien, M. Relational leadership theory: Exploring the social processes of leadership and organizing. Leadership Quarterly, 17, 6 (2006), 654–676.

94. Vance, A.; Lowry, P.B.; and Eggett, D. Using accountability to reduce access policy violations in information systems. Journal of Management Information Systems, 29, 4 (2013), 263–290.

95. Vessey, W.B.; Barrett, J.D.; Mumford, M.D.; Johnson, G.; and Litwiller, B. Leadership of highly creative people in highly creative fields: A historiometric study of scientific leaders. Leadership Quarterly, 25, 4 (2014), 672–691.

96. Warkentin, M.; Willison, R.; and Johnston, A.C. The role of perceptions of organizational injustice and techniques of neutralization in forming computer abuse intentions. In Proceedings of the 17th Americas Conference on Information Systems (AMCIS), Detroit, MI, August 2011 (pp 1–8). http://aisel.aisnet.org/amcis2011\_submissions/318/

97. Weiner, T.; Johnston, D.; and Lewis, N.A. Betrayal: The Story of Aldrich Ames, an American Spy. New York: Random House, 2014.

98. Willison, R. Understanding the perpetration of employee computer crime in the organisational context. Information and Organization, 16, 4 (2006), 304–324.

99. Willison, R., and Warkentin, M. Beyond deterrence: An expanded view of employee computer abuse. MIS Quarterly, 37, 1 (2013), 1–20.

100. Willison, R., and Warkentin, M. Motivations for employee computer crime: Understanding and addressing workplace disgruntlement through the application of organisational justice. In Proceedings of the IFIP TC8 International Workshop on Information Systems Security Research. International Federation for Information Processing, New Delhi, India, March 2009, pp. 127–144.

101. Wise, D. Spy: The Inside Story of How the FBI’s Robert Hanssen Betrayed America. New York: Random House, 2002.

102. Wood, B. An insider threat model for adversary simulation. SRI International, Research on Mitigating the Insider Threat to Information Systems, 2 (2000), 1–3.

103. Wood, S.; Crawford, K.S.; and Lang, E.L. Reporting of counterintelligence and security indicators by supervisors and coworkers. (No. PERS-TR-05-6). Defense Personnel Security Research Center, Monterey, CA, 2005.

104. Wood, S., and Wiskoff, M.F. Americans who spied against their country since World War II. Technical Report PERS-TR-92-005, Defense Personnel Security Research and Education Center (PERSEREC), 2002.

105. Yukl, G.A. Leadership in Organizations. Upper Saddle River, NJ: Prentice Hall, 2002.
