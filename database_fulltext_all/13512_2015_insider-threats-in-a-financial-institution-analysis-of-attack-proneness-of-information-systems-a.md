---
otero_id: 13512
otero_key: "YBHAFQ55"
title: "INSIDER THREATS IN A FINANCIAL INSTITUTION: ANALYSIS OF ATTACK-PRONENESS OF INFORMATION SYSTEMS APPLICATIONS"
authors: "Jingguo Wang; Manish Gupta; H. Raghav Rao"
year: "2015"
journal: "MIS Quarterly"
doi: "10.25300/misq/2015/39.1.05"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INSIDER THREATS IN A FINANCIAL INSTITUTION: ANALYSIS OF ATTACK-PRONENESS OF INFORMATION SYSTEMS APPLICATIONS<sup>1</sup>

Jingguo Wang Information Systems and Operations Management, College of Business, University of Texas at Arlington, Arlington, TX 76019 U.S.A. {jwang@uta.edu}

Manish Gupta and H. Raghav Rao

Management Science and Systems, School of Management, State University of New York at Buffalo, Buffalo, NY 14260-4000 U.S.A. {mgupta3@buffalo.edu} {mgmtrao@buffalo.edu}

This study investigates the risk of insider threats associated with different applications within a financial institution. Extending routine activity theory (RAT) from criminology literature to information systems security, hypotheses regarding how application characteristics, namely value, inertia, visibility, accessibility, and guardians, cause applications to be exposed to insider threats are developed. Routine activity theory is synthesized with survival modeling, specifically a Weibull hazard model, and users’ system access behavior is investigated using seven months of field data from the institution. The inter-arrival times of two successive unauthorized access attempts on an application are employed as the measurement of risk. For a robustness check, the daily number of unauthorized attempts experienced by an application as an alternative measurement of risk are introduced and a zero-inflated Poisson-Gamma model is developed. The Markov chain Monte Carlo (MCMC) method is used for model estimations. The results of the study support the empirical application of routine activity theory in understanding insider threats, and provide a picture of how different applications have different levels of exposure to such threats. Theoretical and practical implications for risk management regarding insider threats are discussed. This study is among the first that uses behavioral logs to investigate victimization risk and attack proneness associated with information assets.

Keywords: Information security, insider threats, routine activity theory, information systems applications, MCMC, risk quantification, dark side of IS

## Introduction

Insider threats to information security are considered to be a critical issue for organizations (Baracaldo and Joshi 2013; Harrington 1996; Huth et al. 2013; Loch et al. 1992; Straub

1990; Wang et al. 2008; Warkentin and Willison 2009). Insiders can be current or former employees, contractors, and other “insiders” who with a valid username and password regularly interact with the information assets of the organization (Randazzo et al. 2004; Warkentin and Willison 2009). Because they usually possess elevated privileges and have skills, knowledge, resources, access, and motives (Willison and Siponen 2009) regarding internal systems and data, insiders can easily circumvent security countermeasures, steal valuable data, and cause damage. Perimeter and host-based countermeasures like firewalls, intrusion detection systems, and antivirus software are ineffective in preventing and detecting insider threats. The 2013 Strategic Security Survey carried out by InformationWeek (Davis 2013) as well as the 2013 Vormetric Insider Threat Report from the Enterprise Strategy Group (Oltsik 2013) have suggested that authorized users and employees are among the top sources posing threats to information security of an organization, and that threats initiated by those insiders are increasingly difficult to prevent and detect. Financial institutions are especially susceptible to insider threats because of their dependence on information technologies and the highly sensitive nature of the stored data (Randazzo et al. 2004).<sup>2</sup>

However, research on quantification of risk of insider threats on information assets is sparse. Despite the availability of much anecdotal information regarding insider threats (Richardson 2008), research efforts relying on field data and designed to advance the understanding of insider threats are still greatly needed (Mahmood et al. 2010). Extending from the original context of explaining predatory crimes in the physical environment, this paper synthesizes routine activity theory (RAT) with survival modeling, and makes the following main contributions: In order to understand what causes applications to be exposed to insider threats, the study conceptualizes and operationalizes the main constructs of RAT (value, inertia, visibility, accessibility (VIVA), and absence of guardians) (Cohen and Felson 1979) in the domain of information systems security. Using inter-arrival times between consecutive unauthorized attempts on an information systems (IS) application as the measurement of risk, a survival model, specifically a Weibull hazard model, is developed and provides a novel way to quantify the risk of insider threats associated with an application. For a robustness check, a zero-inflated Poisson-Gamma model using an alternative measurement of risk—the daily number of unauthorized attempts experienced by an application—has been constructed. The models allow quantification and comparisons of the risk of insider threats associated with different applications. Our study provides a picture of how different applications have different levels of exposure to insider threat, and is the first to provide empirical evidence supporting the utility of RAT-based risk assessment and mitigation approaches (Choi 2008; Willison 2006a, 2006b; Willison and Backhouse 2006; Willison and Siponen 2009).

For our empirical analysis, we collected log data of an enterprise single sign-on (ESSO) system and information regarding integrated IS applications from a regional financial institution, one of the top 20 financial institutions located in the northern United States. The log data contain users’ system access behavior regarding applications, spanning about seven months from September 12, 2008, to April 1, 2009. While most prior studies on insider behavior have used survey or qualitative data (D’Arcy and Herath 2011; Siponen and Vance 2014; Warkentin and Willison 2009), our study is among the first that uses behavioral logs to investigate victimization risk and attack proneness associated with information assets. Such data has enabled us to develop an objective observation of insiders’ behavior related to IS applications in the organization. Despite being arguably the most important sector from an information security standpoint, the banking industry is particularly conservative in sharing security-related data (Kotulic and Clark 2004). Access to these data presented a unique opportunity to conduct analyses of system access behavior in a real-world setting.

## Related Literature and Theoretical Background

## Insider Threats and Criminology Theories

Insiders (internal perpetrators) make rational decisions that are influenced by personal factors, work situations, and opportunities (Dhillon and Moores 2001). Wood (2000) posited that internal perpetrators must have the intention to attack (i.e., motive), must identify a target (i.e., opportunity), and must be able to launch an attack (i.e., capability). Skills, knowledge, resources, authority, and motives have all been considered important personal factors to understand computer crimes including intentional perpetrations (Parker 1998). Schultz (2002) suggests that there are behavioral cues that signal insiders’ propensity to malicious attempts, and any security department that investigates insider threats must pay attention to them. These clues include insiders’ unusual behavior, correlated usage patterns, and personality traits.

To develop more effective prevention and intervention strategies for insider threats, criminology theories provide useful theoretical lenses to understand computer criminals and their behaviors (Harrington 1996; Hartel et al. 2010; Straub and Welke 1998). Such theories enable us to understand social psychological causes of such deviant behaviors. Among these theories, general deterrence theory was introduced earliest to the IS field for the examination of the effects of countermeasures and security policies on information security behavior (D’Arcy et al. 2009; Harrington 1996; Straub 1990; Straub and Nance 1990; Straub and Welke 1998). Following rational choice theory, deterrence theory assumes that people choose to commit a crime after calculating the gain and consequences of their behavior. It predicts that if the punishment of offenders is severe, certain, and swift, a person will be deterred from violating the law given the expected loss is greater than the expected gain. In other words, deterrence theory focuses primarily on the effect of penalties, which typically form post-event policies (Willison and Warkentin 2013).

## Routine Activity Theory

Similar to deterrence theory, routine activity theory (RAT) assumes people make rational choices when they commit violations (Cohen and Felson 1979). Instead of focusing on the effect of punishment, RAT argues that the features of environmental settings (such as target suitability and the presence or absence of guardians) impact criminal activities. The theory by itself does not explain why some people are motivated to commit a crime while others are not, given the same structured situation.

RAT was first proposed to explain predatory crimes. Rather than considering crimes as aberrant behavior, it considers that crimes occur when normal everyday activities of offenders and victims converge in the absence of a capable guardian. The theory assumes that there is a perpetual supply of motivated offenders and variations in the rates and distributions of crime can arise from changes in the structured situation or environmental setting (Cohen and Felson 1979). Targets of a crime per routine activity theory can be a place, a person, or an object. Four main elements affect the target suitability. These are value, inertia, visibility, and access (VIVA) (Cohen and Felson 1979). The essential requirement to prevent a crime is the presence of capable guardians (persons or objects that discourage a crime from taking place).

In the context of predatory crime, the value of a target refers to an assessment of the gain in case the perpetrator carries out the crime. For example, a burglar may want to possess a stolen item or trade it for profit and material gain (Bernasco 2006). The value may not necessarily be considered in terms of economic benefit. A person may get value through enjoyment, for example, in vandalizing public property, but may not directly benefit financially by the act. Value is one of the most important aspects of a target for an offender to become motivated to commit the crime. The higher the value of a target, the more suitable the target becomes for the perpetrator.

Inertia refers to how easily a target can be removed or overcome by the offender. It is traditionally the size or weight of a target in the scenario of predatory crimes. Often a negative relationship exists between inertia and target suitability, and smaller (or lightweight) items are stolen more than larger (or heavy) items (Felson and Clarke 1998). Increasing the inertia of an item to make it less easily removable by instituting control hurdles results in target hardening, which makes theft impractical (Cohen and Felson 1979) and allows the deflection of offenders from the target.

Visibility refers to the extent to which an offender knows the existence and whereabouts of a target. It forms the exposure factor of targets to offenders. The visibility of a target can affect its suitability (Bennett 1991). For example, a valuable good placed by a window can draw more attention from an offender (Felson and Clarke 1998).

Accessibility refers to the ability of an offender to get to the target and then get away from the scene of the crime. The greater accessibility a target has, the more suitable it is for theft. According to Bernasco (2006), the probability of a motivated offender choosing a neighborhood as a burglary target increases with the physical accessibility of the properties in the neighborhood. Beavon et al. (1994) found that the number of physical routes through which a target is accessible is a significant variable in the distribution of property crimes.

According to RAT, a capable guardian is a person or object that discourages a crime from taking place. The guardian’s (such as a doorman, a neighbor, or a coworker) presence or proximity would discourage crime (Felson 2010). Guardians could be physical security measures such as security cameras, lighting, and alarm systems (Tseloni et al. 2004). The theory suggests that the mere presence of a capable guardian near a potential target will help prevent a crime and serve as a crucial deterrence.

RAT has been applied to study violent and property crimes, including features of products making them attractive to thieves (Cohen and Felson 1979; Felson 2010), aspects of locations making them crime hot spots (Sherman et al. 1989), and individuals’ risk factors making them vulnerable to computer crimes (Choi 2008; Yucedal 2010). Depending upon the specific goals of the research, different studies incorporated varying explanatory concepts as well as levels of analyses (Bennett 1991). All of the literature incorporates the essential premise of RAT: the probability that a crime will occur at any specific time and place may be taken as a function of the convergence of motivated offenders, suitable targets, and the absence of capable guardians against the crime (Cohen and Felson 1979).

## A Framework for Risk of Unauthorized Access Attempts on IS Applications

To mitigate and address the risk of insider threats, understanding the relationship between insiders and the context during the perpetration of insider attacks is important. Such an understanding has an impact on enhancing knowledge of the IS environment (the range of technical and managerial controls that can address systems risk) and knowledge of system characteristics (local systems risk and the threats that form part of such risk) (Willison 2006b). These enhancements can lead to improved security management and reduced systems risk (Goodhue and Straub 1991; Straub and Welke 1998).

RAT provides a theoretical lens to investigate how situational and environmental factors (such as application characteristics and their protection measures in place) impact the risk to applications of insider threats. It allows the researcher to take the perspective of the offender, and to explore how situational change (for example, altering target suitability and guardianship) may reduce available opportunities for criminal acts. In his series of papers (Willison 2006a, 2006b; Willison and Backhouse 2006), Willison suggests that routine activity theory could help understand insider risk to information systems, and such an investigation could lead to situational crime prevention by changing the conditions and circumstances that foster crimes (Choi 2008; Willison and Siponen 2009).

Guided by routine activity theory, and considering IS applications to be potential targets of insiders, we hypothesize that value, visibility, and accessibility of an IS application increase, while inertia and guardian-in-place reduce, the risk of insider threats in the form of experiencing unauthorized attempts. In Table 1, we summarize the phenomenon to be explained and extend the definitions of VIVA and guardian in the scenario of predatory crimes to the scenario of insider threats to IS applications.

## Risk of Unauthorized Access Attempts on IS Applications

As IS applications have been widely used to support business operations and to store operating data in organizations, insider threats arise because internal perpetrators try to gain access to applications to which they do not have access rights (Chinchani et al. 2006). Unauthorized access attempts on IS applications are one major indication of insider threats, as suggested by prior studies and industry practices (Davis 2010, 2011; Randazzo et al. 2004). Such attempts often lead to system breach and data loss (Cappelli et al. 2012). In a survey of security professionals in 2010, Davis (2010) found that 55 percent of respondents said they monitor sensitive data to reduce unauthorized attempts. A subsequent survey indicated that analyzing attempts to access sensitive applications or data is one of the top three activities used to monitor employees as part of organizations’ risk management strategy (Davis 2011).

One way to quantify the risk that an application will experience unauthorized access attempts is to follow survival modeling.<sup>3</sup> Survival modeling is a method for data analysis in which the dependent variable is the time until occurrence of an event of interest. We considered the event of our interest to be an unauthorized access attempt, and an application’s survival times are the inter-arrival times between consecutive unauthorized attempts on an application. An application with more unauthorized access attempts experiences shorter survival times and has a higher risk. Survival times have been widely used in diverse fields such as medicine, biology, public health, epidemiology, and reliability engineering for risk quantification. For example, in the area of medicine, survival times are used to understand patients’ mortality risk from a specific cause, duration of response to treatment, recurrence risk of a disease, and development of a disease (Allison 1995; Collett 2003; Klein and Moeschberger 2003).

## Value of IS Applications

We consider value of an application for an internal perpetrator to be the value of information contained and of functionality processed by an application. We argue that the value of an IS application increases its risk of insider attacks. Randazzo et al. (2004) examined 22 insider incidents that occurred in the banking and finance sector between 1996 and 2002 and suggested that financial gain was the most prevalent goal among the most motivated perpetrators. Stolen data such as credit card, bank account numbers, and consumer information (including name, billing address, phone, and Social Security number) can be traded on a black market (Geer 2005; Panda Security 2010; Zeller 2005), and the price of the stolen data depends on the details the data contain (Panda Security 2010). In addition, bank transfers and check cashing services for money laundering can also be traded to move stolen money from victims’ accounts into untraceable accounts (Panda

Table 1. Definitions of Routine Activity Theory (RAT) Construct in Different Scenarios

<table><tr><td>RAT Construct</td><td>Predatory Crimes</td><td>Insider Threats to IS Applications</td></tr><tr><td>Phenomenon to be explained (or dependent variable)</td><td>The risk of a target being stolen (Cohen and Felson 1979; Felson and Clarke 1998).</td><td>The risk of an IS application experiencing unauthorized access attempts.</td></tr><tr><td>Value</td><td>An assessment of a target by an offender for what he/she may gain or the effect he/she may have on it (Bernasco 2006; Cohen and Felson 1979).</td><td>The value of information contained and of functionality processed by an application for an internal perpetrator (Geer 2005; Panda Security 2011; Randazzo et al. 2004; Zeller 2005).</td></tr><tr><td>Inertia</td><td>How easily a target can be removed or overcome by an offender (Cohen and Felson 1979; Felson and Clarke 1998).</td><td>The strength of application controls that can make it difficult for an internal perpetrator to either steal data/functionality from an application or achieve a malicious purpose within an application (Baskerville 1993; Laudon and Laudon 2012; Mishra and Dhillon 2008; Weber 1998; Wilkinson et al. 1999).</td></tr><tr><td>Visibility</td><td>Whether an offender knows that a target exists and knows about its whereabouts (Bennett 1991; Cohen and Felson 1979; Felson and Clarke 1998).</td><td>The extent to which an internal perpetrator may know the existence and the whereabouts of the application (Agarwal and Prasad 1997; Colwill 2009; Magklaras and Furnell 2001; Moore and Benbasat 1991; Neumann 1999; Parker 1998; Sarkar 2010; Wood 2000).</td></tr><tr><td>Accessibility</td><td>The ability of an offender to get to the target and then get away from the scene of crime (Beavon et al. 1994; Bernasco 2006; Cohen and Felson 1979).</td><td>The degree of openness and ease of access to the data and functionality of an application for an internal perpetrator (Culnan 1983; DeLone and McLean 1992; Fidel and Green 2004; Goodhue 1995; Karahanna and Straub 1999; Xu et al. 2012).</td></tr><tr><td>Guardian</td><td>A capable guardian is anything, either a person or an object that discourages a crime from taking place (Cohen and Felson 1979; Felson and Clarke 1998; Tseloni et al. 2004).</td><td>The protection mechanisms placed around an application with the purpose of preventing and deterring an internal perpetrator (Calder and von Bon 2006; Gorge 2008; Smith et al. 2010; Straub and Welke 1998; Willison and Backhouse 2006; Willison and Siponen 2009; Yar 2005).</td></tr></table>

Security 2010). While different applications vary in their data/functionality and attract different valuations, such valuations are likely to impact the suitability of the target when viewed from an insider perspective. Therefore, along a similar line of reasoning for predatory crimes, where the value of an object increases its likelihood of being stolen (Bernasco 2006; Cohen and Felson 1979), we propose that

H1: The value of an IS application increases its risk of unauthorized access attempts.

## Inertia of IS Applications

We consider inertia of an application as the strength of application controls that make it difficult for an internal perpetrator to steal information/functionality from an application or achieve a malicious purpose with regard to an application. We argue that the inertia of an IS application (in the form of application controls) reduces its risk to insider attacks. Application controls embody inertia by introducing an internal resistance to the improper use of the system functionality and/or the improper change/movement of system data, as well as timely discovery of these acts if they were committed (Laudon and Laudon 2012; Weber 1998; Wilkinson et al. 1999). Application controls are internal and usually unique to each application, and are often incorporated at the development phase of a system (Baskerville 1993). Such controls include input, processing, and output controls with a purpose to ensure completeness, accuracy, and validity of an application’s operations and maintenance (Cardinal et al. 2004; Laudon and Laudon 2012; Wilkinson et al. 1999). Some applications are more tightly controlled than others; they have more levels of approval for the deletion or modification of information/systems, or more frequent penetration testing and access recertification requirements (Mishra and Dhillon 2008). Therefore, following the argument of RAT, which suggests inertia of an item is negatively associated with target suitability and the chance of being stolen (Cohen and Felson 1979; Felson and Clarke 1998), we propose that

H2: The inertia of an IS application (in the form of application controls) decreases its risk of unauthorized access attempts.

## Visibility of IS Applications

We considered the visibility of an application as the extent to which an internal perpetrator may know about the existence of an application and the whereabouts of the application. We argue that visibility of an IS application increases its risk of insider attacks. Compared to outsiders, insiders are often considered to be more aware of the location of valuable information and have more detailed information about the target, and consequently impose a higher risk (Colwill 2009; Magklaras and Furnell 2001; Neumann 1999; Wood 2000). If an application is not visible to an offender, it is less likely to be targeted for an attack (Wood 2000). High visibility of an application implies that the application itself and application usage are highly exposed to insiders (Moore and Benbasat 1991). Such exposure allows insiders to be more aware of and have more knowledge about the application. This kind of knowledge is essential in initiating insider attacks (Parker 1998; Sarkar 2010). In addition, the high visibility of an application may also engender curiosity among insiders and create a temptation to try-out the application (Agarwal and Prasad 1997). Prior studies in the area of technology innovation adoption have shown that the visibility of a technology (such as a Web system) is one critical factor influencing users’ acceptance of a technology, and can be used to explain both initial system usage and usage intentions (Agarwal and Prasad 1997; Moore and Benbasat 1991). Therefore, as suggested by RAT that more visible objects are more likely to become targets and have a higher chance to be stolen (Bennett 1991; Cohen and Felson 1979; Felson and Clarke 1998), we propose that

H3: The visibility of an IS application increases its risk of unauthorized access attempts.

## Accessibility of IS Applications

We consider accessibility of an application as the degree of openness and ease of access to the functionality and the data of an application for an internal perpetrator. We argue that accessibility of an IS application increases its risk of insider attacks. In the area of IS success, the ease and costless manner in which users can access a system (or an information source) has been suggested to be one of critical factors influencing their usage behavior (Culnan 1983; DeLone and McLean 1992; Goodhue 1995; Karahanna and Straub 1999). The conceptualization of accessibility of an IS application or an information source has been shifted with the development of technology. Accessibility is dependent on physical costs and constraints of system accessing (for example, waiting time for access, and availability of terminals for access), ease of use of system interface, and the quality of information retrieved after initial use (for example, timeliness, accuracy, and relevance) (Culnan 1985; Fidel and Green 2004). In the area of information security, access control mechanisms limit access to system functionality and data availability for IS applications. In the commonly used role-based access control method (RBAC), users’ roles and responsibilities are always defined and documented, and corresponding system privileges are then assigned (Sandhu et al. 1996). RBAC has been an important measure for mitigating security risk and protecting data from being abused and stolen (Spears and Barki 2010). Data or systems that are more open to access are subject to high privacy and security breach risk (Xu et al. 2012). Therefore, along the same lines as suggested in RAT that accessibility increases the suitability of a target (Beavon et al. 1994; Bernasco 2006; Cohen and Felson 1979), we propose that

H4: The accessibility of an IS application increases its risk of unauthorized access attempts.

## Guardian of IS Applications

We consider capable guardians as protection measures placed around applications with the purpose of deterring and preventing an internal perpetrator from accessing data that they are not authorized to access. Security technologies ranging from firewalls, intrusion detection systems, and antivirus systems serve as technological guardians, while network administrators, application administrators, application auditors, and security staff who watch over their electronic charges serve as social guardians (Yar 2005). An important distinction from inertia is that such guardians and their constituents are external to an application and are not application specific. Thus we can consider that the external data security measures embody guardians.

Protection measures may be categorized into four types: deterrence, prevention, detection, and remedy (Straub and Welke 1998). Organizations must make efforts to maximize deterrence and prevention efforts, while minimizing the need for detection and remedy. Deterring potential internal perpetrators is an organization’s first effort to address insider threats. Preventive measures are the next effort with a purpose of stopping the commission of computer crime/abuse if deterrent measures fail. Detection and remedies are the consequent efforts when a threat cannot be deterred or prevented. The likelihood that application data are inadequately protected by deterrent and preventive measures presents more criminal opportunities (Willison and Backhouse 2006), and constitutes a risk of insider threats (Straub and Welke 1998).

The external data security measures in this paper refer to protection measures on the data operated by applications. These include a mix of deterrence, prevention, detection, and remedy technologies and policies to ensure the data is properly stored, transmitted, and accessed, both physically and electronically. We argue that these data security measures of IS applications reduce the risk of insider attacks. As different types of data have different levels of sensitivity, classifying data into different classes and then implementing corresponding levels of protection measures has been suggested as an important security management practice in standards such as ISO27001 and ISO17799 (Calder and von Bon 2006; Smith et al. 2010). As these measures are assigned based on data classification, they are implemented at the security defensive layer that lies external to the application and covers all the channels that access that data. Gorge (2008) found that classification of data, structured or unstructured, makes it easier for an organization to locate and protect the data, while following “need-to-know” security principles, and that the classification provides a target level of security for concerned entities. Minimum-security requirements corresponding to the level of data sensitivity are often specified to safeguard against intentional and accidental abuse of information. The more sensitive the data, the greater is the need for protection measures.

Consider the financial institution in our field study as an example. Highly sensitive data in the institution would include personal identification numbers and non-masked credit or debit card numbers. There are a number of security measures that are required for such data: (1) encryption of such data is required for electronic storage and transmission of data on public networks; (2) access to the data is restricted through proper authentication; (3) access to the data must be approved and authorized; (4) physical transport of the data must be compliant with the ANSI-approved ASC X9 standards, or approval of the information security department; (5) such data cannot be sent using Internet e-mail or stored using portable media; (6) the data cannot be published on the intranet or on external sources; (7) nonemployees must sign nondisclosure agreements to access the data; (8) physical storage of the data must be at areas with restricted physical access. These protection measures reduce criminal opportunities, leading to lower risk of insider threats to an application (Straub and Welke 1998; Willison and Backhouse 2006; Willison and Siponen 2009). Therefore, using the same logic of RAT, which suggests capable guardians discourage a crime from happening (Cohen and Felson 1979; Felson 2010; Tseloni et al. 2004), we propose that

H5: Data security measures of an IS application reduce its risk of unauthorized access attempts.

## Measurement

In empirical validations, the constructs of routine activity theory (VIVA and the presence—or absence—of a guardian) are usually operationalized based on the context (Akers and Sellers 2008). For example, in analyzing crime rate trends and cycles, Cohen and Felson (1979) measured the routine activities of victims and capable guardians based on labor force participation and household composition. To understand hot spots of predatory crime, Sherman et al. (1989) assumed victim vulnerability and guardianship follow from the social characteristics of the victims. In explaining street robbery, Smith et al. (2000) used racial composition and distance from the city center to count the number of motivated offenders, the number of stores and other commercial land use to determine the number of suitable targets, and the number of owner-occupied homes to determine the number of capable guardianships.

However, the principle constructs of routine activity theory have (to date) neither been operationalized nor measured in the context of insider threats regarding IS applications. In this section, we detail our measurement of the constructs in our model. Table 2 lists the operationalization of measurement of RAT constructs. To measure the risk of unauthorized access attempts, we used inter-arrival times between two successive unauthorized access attempts of an application, relying on the observed user behaviors related to an application. To measure VIVA and the presence of a guardian, we relied on the characteristics of IS assets (i.e., IS applications in our scenario). We interviewed application owners and security managers for relevant information regarding the applications. A Delphitype exercise with application owners and security managers was also carried out to confirm the mapping and measurement relationship between constructs and application characteristics. The details are summarized in Appendix B.

<table><tr><td>Constructs</td><td>Measurement</td><td>Brief Explanation</td></tr><tr><td>Risk of unauthorized access attempts</td><td>Survival Times</td><td>Inter-arrival times between two consecutive unauthorized access attempts on an application.</td></tr><tr><td>Value</td><td>Business Value Measure</td><td>Criticality and value of an application supporting business operations. This score is derived by the financial institution through a detailed questionnaire completed by business owners and sponsors of each application for the purpose of business continuity and risk management.</td></tr><tr><td>Inertia</td><td>Application Control Strength</td><td>Strength of internal and environmental controls of an application, to ensure integrity and consistency of its operations.</td></tr><tr><td>Visibility</td><td>Number of Authorized Users</td><td>Number of unique authorized users of the application.</td></tr><tr><td>Accessibility</td><td>On-demand Live Information Modification</td><td>Whether an application allows its users to modify production data, live on the fly, due to business necessity and need for functional support.</td></tr><tr><td>Guardian</td><td>Data Protection Level</td><td>Classification of the data processed by an application based on its value or importance to the organization. Each level is associated with a corresponding protection specification.</td></tr></table>

Risk of Unauthorized Access Attempts: To measure the dependent variable, risk of unauthorized access attempts associated with each application, we used the survival times (i.e., the inter-arrival times between two consecutive authorization rejections) for each application. The survival times are generally not symmetrically distributed (which is the case with the data used in this paper as well), and a histogram constructed from the times will tend to be positively skewed. Therefore, it will not be reasonable to assume the data have a normal distribution, and a more satisfactory approach is to adopt an alternative distributional model (e.g., Weibull distribution) for the data in the analysis (Collett 2003).

Value of an IS Application: We measured the value of an IS application based on its criticality and value-supporting business operations (termed here as business value measure, BVM). Having distinct functionalities, the applications may have different levels of criticality and value for business operations from a perspective of business continuity and risk management. This is in line with previous studies that have suggested value-focused approaches to develop objectives about IS security (Abercrombie and Sheldon 2009; Dhillon and Torkzadeh 2006) and business process-based valuation of IT security (Neubauer et al. 2005).

We used the existing scores of BVM for the applications shared by the financial institution. The scores were derived based on a questionnaire completed by business owners and sponsors of each application as part of a risk assessment. The technical manager responsible for an application and the application owner both participated in the assessment. The questionnaire was based on the system characterization step of risk assessment per NIST Special Publication 800-30 (Stoneburner et al. 2002). It is normally utilized for business impact analysis (BIA) at the time of creation of the applications. BIA is one of the most important considerations for business continuity (Hiles 2007). In the analysis, there were five impact areas evaluated, including financial, customer, operational, regulatory/legal, and recovery time objective. Recovery time objective specifies the time window within which the application should be brought back up after a disaster. Each impact area was assessed by using a criticality ranking. The ranks were critical, vital, sensitive, and noncritical. The highest rank of any impact area drove the overall ranking. For example, a rank of critical in the area of operational impact caused the application to be ranked as critical, even if all other areas were ranked lower. Depending on the BVM value of an application, appropriate and proportional continuity management plans were created and implemented. BVM also helped determine whether an application should be hosted at a hot, warm, or cold disaster recovery site and how often the data must be backed up for the application. BVM reflects the value of business functions an application supports to an organization. All applications have been reassessed on a two-year cycle. The BVM scores can take one of the following values: 0 = noncritical, 1 = sensitive, 2 = vital, and 3 = critical.

Inertia of an IS Application: We measured the inertia of an IS application based on its strength of application controls.

Application controls can be classified into corrective, preventive, and detective based on the risk aversion (Wilkinson et al. 1999). Corrective controls reduce the loss from an incident, preventive controls reduce the probability of an incident, and detective controls reduce both. Examples of preventive controls include transaction authorization procedures, inbuilt data validation controls, and policy compliance for information exchange. Examples of detective controls include reviews of outputs and tests to source documents by users, feeding application logs to security information and event systems for analysis, and software process audit. Examples of corrective controls include marking deletion for approvals, code review, and access recertification. The higher the strength of the controls, the more effort will be needed to compromise the integrity of the system. While these different types of controls have different purposes, they are inherent and specific to each application, making attacks on an IT asset more difficult.

Because there is no existing single value that can be used to measure application control strength (CSTR) in the financial institution, a composite metric was developed based on our interviews with the application managers. Considering that an application may have multiple controls, and each control carries different weights, we asked each application manager to list and rank all controls based on the importance of the control for his or her application(s). We approximated the weight of a control for the application based on the rank order centroid method (Barron and Barret 1996) for two reasons. First, ranking is relatively easy and reliable compared with other weight elicitation methods (Eckenrode 1965; Kirkwood and Sarin 1985). Second, the rank order centroid method is known to be more accurate than other rank-based formulae in approximating attribute weights (Barron and Barret 1996). Then, for each control of an application, the application manager rated its strength on a five-point scale, with one being the weakest and five the strongest. We used the weighted average of the strengths of all controls to measure control strength for an application. Appendix C provides some examples of application controls.

Visibility of an IS Application: We measured the visibility of an IS application using the number of unique authorized users of the application (including employees, contractors, vendors, and partners). More users lead to greater visibility of that application’s functions and access mechanisms. In HIPAA risk assessment (University of Maine System 2005; Washington University in St Louis 2005), the number of users of a system is an important measure for the factor that affects system risk. It is commonly believed that the rate of attacks, in which perpetrators attempt to steal user accounts and passwords of a system through psychological manipulation, or through password guessing of others’ accounts, is higher for applications with more users. This can be attributed to two logical explanations: (1) the probability of unauthorized users who know user names of other users is higher, since there are more users around who have legitimate access to an application, and (2) the probability that authorized users are aware of higher-level functions of the application is greater since they are already users of the application, or they may hear about it through word-of-mouth from other users.

Accessibility of an IS Application: We measured the accessibility of an IS application based on whether it allows its users to modify production data live on the fly due to business necessity and need for functional support—on-demand live information modification (OLIM). Thus applications that allow OLIM may result in a higher possibility of permitting those with malicious intentions to compromise the confidentiality and integrity of the data (for example, changing the account number of the recipient of a funds transfer). Usually such illegitimate access and changes can only be detected after the fact. An interesting anecdote that drives the point home in our case is of Societe Generale Bank incident in 2008 that resulted in about \$7.2 billion loss to the bank, the largest trading loss in banking history. An employee was able to make illegal trades violating the company policies (Cleary 2008). The employee had access to a trading application, in which transactions were made online. This made it easy for him to make illegal trades and difficult for the company to detect and prevent in real time. The incident was only revealed on analysis of the loss after the trades were made. It has also been argued that if an application is more open to access, it could potentially allow an attacker to more easily get into a system and extract data. This would result in greater insecurity (Manadhata and Wing 2011). We used a binary variable to indicate OLIM (0 = no, 1 = yes) for each application based on our interview with application managers or owners in the financial institution.

Data Security Measures: We measured the external data security measures of an IS application using its data protection level (DPL). Consumer and corporate data are often classified according to the levels of risk associated with the unauthorized use or disclosure of that data. This classification commonly reflects the importance and value of the data to an organization. It determines the enterprise’s minimum-security requirements for the protection of the data. In the financial institution, data are separated into six classifications: restricted (5), private (4), proprietary (3), internal (2), public (1), and not applicable (0). Each level results in a corresponding protection specification on the data. Appendix D details these classifications including example data types and related protection requirements in the financial institution.

## Data

## ESSO Logs

We observed user behaviors related to different IS applications and determined unauthorized attempts made on an application based on an analysis of log data of an enterprise single sign-on (ESSO) system. Contingent on an authentication interaction, an ESSO system enables users to access all applications or resources (for example, a HTML page, or a file with an application) to which they have been granted access. The ESSO system tracks two types of user events: system login and application access. It logs an authentication acceptance for a successful user login, and an authentication rejection for a failed user login (for example, due to a wrong password). After a user successfully logs in, the ESSO system tracks the user’s application (or resource) access behavior. If the user attempts to access an application (or resource) to which he/she was granted access, the ESSO system logs an authorization acceptance. If the user attempts to access an application or resource to which he/she was not granted access, the ESSO system logs an authorization rejection. Each entry in the ESSO logs contains a user identification, a timestamp, the application or resource the user requested, and the result of an event that could be one of the four values: authentication acceptance/rejection related to system logins and authentication acceptance/rejection related to application accesses. The ESSO system used by the financial institution is the SiteMinder Web Access Manager by Computer Associates<sup>®</sup>. Appendix A provides a detailed description about the architecture and functionality of the ESSO system.

We collected the ESSO logs from September 12, 2008, to April 1, 2009, when it became available in May 2009. The logs contain a total of 14,680 unique users who had at least one successful login during the observation period, and 4,326 users who made at least one unauthorized attempt. We tracked unauthorized attempts made to the 40 most commonly used applications in the ESSO system. Among these 40, the maximum number of unauthorized attempts experienced by an application was 6,228, and the minimum was 2. The average number of unauthorized attempts per application was 673.85 with a standard deviation of 1347.29.

The dependent variable in this paper is the risk of unauthorized access attempts associated with each application. The risk was measured in terms of the survival times for each application within the observation period. The survival times are the inter-arrival times (unit of hours), between the rejections of two successive authorization requests for access to the application.<sup>5</sup> As a nonparametric method, we estimated the survival function for an application using the Kaplan– Meier method (also called the product limit method) (Kaplan and Meier 1958). A survival function evaluated at t is the instantaneous probability that the survival time of an application exceeds t, that is, $S ( t ) = \operatorname* { P r } ( T > t )$ , where S(t) denotes the survival function and T is the survival time of an application. Suppose we have observed $K _ { i }$ rank-ordered survival times for an application $i ( i = 1 , 2 , . . . , N ) , t _ { i 1 } , \le t _ { i 2 } \le . . . \le t _ { i K _ { i } }$ Let $n _ { i j }$ denote the number of observations that have survived up to a time just prior to time $t _ { i j }$ (or are “at risk of dying” at time $t _ { i j } ) _ { \cdot }$ , and $d _ { i j }$ denote the observed number of intervals having a value of $t _ { i j } \left( \mathrm { i . e . } \right.$ , that have died at time $t _ { i j } )$ . For $t _ { i 1 } \leq t \leq t _ { i K _ { i } }$ , the Kaplan–Meier estimator of the survival function is defined as

$$
\hat {S} _ {i} (t) = \prod_ {j: t _ {i j} <   t} \left(1 - \frac {d _ {i j}}{n _ {i j}}\right)\tag{1}
$$

Figure 1 plots the estimated survival functions of each application. We can see that each application has a distinct survival function. The log-rank test (Mantel 1966; Peto and Peto 1972) examines whether the difference was significant. The log-rank test is the best known and most widely used nonparametric test, which enables us to compare the survival functions among the applications without assuming the exact nature of the underlying survival distribution. The log-rank test had a p-value less than 0.01, indicating that the survival functions across different applications differed significantly. The result implied that some applications experienced unauthorized attempts more frequently and had shorter survival times than others.

## Descriptive Statistics of Measuring Characteristics

We interviewed application managers to collect the characteristics for the 40 applications. The mean access prevalence level (APL) (i.e., the number of users) per application was 4760.75 with a standard deviation of 7963.16 and a median of 700. Because the distribution of the number of users was highly skewed, we used its logarithmic value in regressions. For control strength (CSTR), we calculated a mean of 3.89, a median of 3.93, and a standard deviation of 0.51. The descriptive statistics for other application characteristics are presented in Table 3. Table 3 shows the number of applications and the mean number of observed rejections per application within a category of each discrete variable. To assess the effect of the independent variables on the survival times, we performed a log-rank test for a given variable to examine whether the survival times of the applications with different values systematically differed. Our tests suggested that different value groups systematically differed in their survival times $( p \mathrm { - v a l u e s < 0 . 0 1 } )$ for all variables. The results indicate these individual variables could significantly impact the survival times of an application.

![](/api/attachments/YBHAFQ55/fulltext/images/8278bbdb82c43532438df97c273b763bbc978269f09ee54294a19cd656006d0f.jpg)  
Figure 1. Survival Distribution Functions for Different Applications

Table 3. Descriptive Statistics and Log-Rank Test for Discrete Variables

<table><tr><td colspan="2">Variables</td><td>Category</td><td># of App. Within the Category</td><td>Mean # of Rejections per App. Within the Category</td><td>Log-Rank Test p-value</td></tr><tr><td rowspan="4">BVM</td><td rowspan="4">Business Value Measure</td><td>0: Noncritical</td><td>6</td><td>924.17</td><td rowspan="4">&lt; 0.01</td></tr><tr><td>1: Sensitive</td><td>11</td><td>90.00</td></tr><tr><td>2: Vital</td><td>17</td><td>550.94</td></tr><tr><td>3: Critical</td><td>6</td><td>1842.17</td></tr><tr><td rowspan="2">OLIM</td><td rowspan="2">On-demand live information modification</td><td>0: No</td><td>20</td><td>549.25</td><td rowspan="2">&lt; 0.01</td></tr><tr><td>1: Yes</td><td>20</td><td>798.45</td></tr><tr><td rowspan="6">DPL</td><td rowspan="6">Data Protection level</td><td>0: Not Applicable</td><td>1</td><td>40.00</td><td rowspan="6">&lt; 0.01</td></tr><tr><td>1: Public</td><td>0</td><td>N/A</td></tr><tr><td>2: Internal</td><td>1</td><td>4399.00</td></tr><tr><td>3: Proprietary</td><td>20</td><td>772.50</td></tr><tr><td>4: Private</td><td>17</td><td>413.29</td></tr><tr><td>5: Restricted</td><td>1</td><td>39.00</td></tr><tr><td colspan="6">Table 4. Correlations of Application Characteristics</td></tr><tr><td></td><td>BVM</td><td>CSTR</td><td>APL</td><td>OLIM</td><td>DPL</td></tr><tr><td>BVM</td><td>1.00</td><td>-0.19</td><td>-0.35*</td><td>0.14</td><td>-0.19</td></tr><tr><td>CSTR</td><td></td><td>1.00</td><td>-0.20</td><td>-0.02</td><td>-0.10</td></tr><tr><td>APL</td><td></td><td></td><td>1.00</td><td>0.12</td><td>0.20</td></tr><tr><td>OLIM</td><td></td><td></td><td></td><td>1.00</td><td>0.47**</td></tr><tr><td>DPL</td><td></td><td></td><td></td><td></td><td>1.00</td></tr></table>

\*p-value < 0.05; \*\*p-value < 0.01

Table 4 presents the correlations of these variables. We noticed that the correlation between BVM and APL and between OLIM and DPL had p-values less than .05. To assess whether there was a serious multicollinearity problem in our data, we performed a simple linear regression using the log-transformed survival times as the dependent variable to examine the variance inflation factor (VIF) for each independent variable. We found that all VIFs were well below 3.3, indicating that multicollinearity was not a cause of concern for our data.

## Model and Data Analysis

## A Weibull Hazard Model

The Weibull distribution is central to the parametric analysis of survival data (Collett 2003). The Weibull hazard model has long been the most popular parametric model in the biostatistical literature for analyzing duration data (Allison 1995). The model has a relatively simple survival function that is easy to manipulate mathematically. It can be presented in the form of a proportional hazards model (which is the form we use) or an accelerated failure time model. Therefore, the impact of covariates can be interpreted based on relative hazard ratios, or interpreted directly on the change of the failure time (or its transformation). In addition, the shape parameter (denoted as γ in Equation (2)) provides the flexibility of the Weibull model. By changing the parameter value, Weibull distributions can empirically fit a wide range of data histogram shapes. For example, when its value is 1, a Weibull distribution is identical to the exponential distribution; if it is 2, a Weibull distribution is identical to the Rayleigh distribution; if it is between 3 and 4, a Weibull distribution approximates the normal distribution. A Weibull distribution with a shape value less than 1 has a hazard rate that decreases with time (also known as infantile or early-life failures). A Weibull distribution with a shape value close to or equal to 1 has a fairly constant hazard rate, indicative of random failures. A Weibull distribution with a shape value greater than 1 has a hazard rate that increases with time (known as wear-out failures). Further, unlike the Kaplan– Meier method or the Cox proportional hazards model, which are nonparametric or semiparametric defined up until the last observed failure, the Weibull model is a parametric model that may be used for forecasting.

Let t denote the inter-arrival times between the consecutive authorization rejections of an application. We consider that t follows a Weilbull distribution (denoted as W(λ, γ) where λ and γ are scale and shape parameters, respectively (Kim and Ibrahim 2000)). To model the impact of application characteristics on the hazard function, we used a proportional form<sup>6</sup> (Congdon 2003):

$$
h (t) = \lambda \gamma t ^ {\gamma - 1} e ^ {X B}\tag{2}
$$

where $X = ( x _ { I } , x _ { 2 } , . . . , x _ { K } )$ is a set of covariates , and $\beta ^ { \prime } = ( \beta _ { 1 }$ $\beta _ { 2 } , . . . , \beta _ { K } )$ is a set of coefficients to be estimated. The part $\lambda \gamma t ^ { \gamma - 1 }$ in Equation (2) is commonly referred to as the baseline hazard defining the nonparametric part of the function that is not influenced by the explanatory variables. The coefficient of $x _ { k } , \beta _ { k } ,$ can be interpreted as the logarithm of a hazard ratio. The hazard ratio (or the relative risk-type ratio, $e ^ { \beta _ { k } } )$ measures the effect of an explanatory variable on the risk of an application experiencing unauthorized attempts. If $e ^ { \beta _ { k } } < 1$ $( \mathrm { i } . \mathrm { e } . , \beta _ { k } < 0 )$ , the variable decreases the hazard rate (or the instantaneous probability of an application experiencing unauthorized attempts). If $e ^ { \beta _ { k } } > 1 \mathrm { \ i } \cdot \mathrm { e } . , \beta _ { k } > 0 )$ , the variable increases the hazard rate. If $e ^ { \beta _ { k } } = 1 ( \mathrm { i . e . , } \beta _ { k } = 0 )$ , the variable does not change the hazard rate. The median survival time for an application, which can be used as a benchmark to compare the risk among applications and identify high-risk applications, is $\left[ \frac { \log 2 } { \lambda e ^ { X \beta } } \right] ^ { 1 / \gamma }$

The survival function corresponding to Equation (2) is

$$
S (t) = \exp \left\{- \lambda t ^ {\gamma} e ^ {X \beta} \right\}\tag{3}
$$

We can transform Equation (3) by taking the natural logarithm (base e logarithm), multiplying by -1, and taking another logarithm on both sides:

$$
\log \left\{- \log S (t) \right\} = \log \lambda + X \beta + \gamma \log t\tag{4}
$$

This equation provides us a way to assess whether the Weibull distribution for our data is plausible. We can substitute the Kaplan–Meier estimate of the survival function $\hat { S } ( t )$ (defined in Equation (1)) for S(t) on the left side of Equation (4). If the Weibull assumption is tenable, then a plot of $\log \Bigl \{ - \log \hat { S } \{ t \} \Bigr \}$ against log t will give an approximately straight line as suggested in Equation (4) (Collett 2003). Our plots (shown in Appendix E) for the survival times of different applications confirmed that the Weibull distribution is appropriate for our data. We also noticed from our plots that different applications have different intercepts and slopes (which are defined by (logλ+ Xβ) and γ in Equation (4), respectively). While the difference in the intercepts can be explained by the independent variables, we used different shape parameters γ<sub>i</sub> $( i = 1 , 2 , . . . , \mathrm { N } )$ for different applications to take into account the unobserved heterogeneity of applications.

## Estimation Method

We estimated the model using Markov chain Monte Carlo (MCMC) method to obtain the posterior distributions of the model parameters. MCMC essentially draws samples from the required distribution, and then forms sample averages to approximate expectations by running a cleverly constructed Markov chain for a long time (for a detailed discussion of MCMC, see Gelman et al. 2003). The estimation was carried out using WinBUGS, a tool for performing Bayesian inference using Gibbs Sampling (Spiegelhalter et al. 2003).

Following prior studies (Dellaportas and Smith 1993; McGilchrist and Aisbett 1991), we used uninformative but proper priors and hyperpriors for our Weibull hazard model. Particularly, the regression coefficient $\beta$ (Equation (5)) is specified to independently follow normal distributions with a mean of zero and a variance of 100. The shape parameter $\gamma _ { i }$ $( i = 1 , 2 , . . . , \mathrm { N } )$ (Equation 5) is specified to independently follow gamma distributions with a shape parameter of $\varsigma$ and a scale parameter of ν, and $\varsigma$ and ν to follow independent gamma distributions with a shape of 1 and a scale of 0.001. We chose these commonly used prior distributions and their parameter values to represent high uncertainty or prior ignorance (Ntzoufras 2009). Given our large sample size, the prior distributions would not have much influence on the parameter estimates or on convergence of the estimates (Sinharay 2004). To confirm this, we performed sensitivity analyses (used different values for the prior distributions and different forms of prior distributions). We obtained similar results.

We simulated two chains. Each chain had 12,000 iterations, and the first 6,000 were discarded as an initial burn-in. To reduce the autocorrelation in the sample, each chain was thinned by three.<sup>7</sup> In other words, given the last 6,000 iterations of each chain, we kept one sample from every three iterations to calculate the statistics of the posterior distributions of the model parameters. We monitored and plotted the traces of each model parameter for all chains to confirm the adequacy of convergence of the model. All plots showed convergence. The values of the Gelman–Rubin convergence statistic (i.e., Rhat calculated by WinBUGS) for all estimated model parameters are about 1, suggesting the absence of chain effects and therefore convergence of the estimates (Brooks and Gelman 1998).

## Estimation Results

Table 5 summarizes the estimated model parameters, along with the 95 percent credible intervals (i.e., the intervals bounded by the 2.5 percent and 97.5 percent percentiles of the posterior distributions) calculated from the MCMC simulations. We also present the hazard ratios $e ^ { \beta _ { t } }$ , the posterior probabilities, and the Bayes factors (BFs) (i.e., posterior odds)<sup>8</sup> (Kass and Raftery 1995) in favor of ${ \bf \nabla } \cdot \beta _ { i } = 0$

<table><tr><td colspan="9">Table 5. Estimated Parameters with a Weibull Hazard Model</td></tr><tr><td>Model Parameters</td><td>Mean</td><td>Standard Deviation</td><td>2.5%</td><td>Median</td><td>97.5%</td><td>Hazard  $Ratio^{e^{\beta_1}}$ </td><td>Posterior Probability of β &gt; 0</td><td>BF in favor of β = 0</td></tr><tr><td>Constant (logλ)</td><td>1.49</td><td>0.12</td><td>1.29</td><td>1.48</td><td>1.71</td><td>4.46*</td><td>1.00</td><td>0</td></tr><tr><td>BVM ( $\beta_1$ )</td><td>0.22</td><td>0.01</td><td>0.19</td><td>0.22</td><td>0.24</td><td>1.24</td><td>1.00</td><td>0</td></tr><tr><td>CSTR ( $\beta_2$ )</td><td>-0.33</td><td>0.02</td><td>-0.36</td><td>-0.33</td><td>-0.30</td><td>0.72</td><td>0.00</td><td>0</td></tr><tr><td>Log $_{10}$ (APL) ( $\beta_3$ )</td><td>0.20</td><td>0.02</td><td>0.17</td><td>0.21</td><td>0.23</td><td>1.23</td><td>1.00</td><td>0</td></tr><tr><td>OLIM ( $\beta_5$ )</td><td>0.14</td><td>0.02</td><td>0.11</td><td>0.14</td><td>0.17</td><td>1.15</td><td>1.00</td><td>0</td></tr><tr><td>DPL ( $\beta_6$ )</td><td>-0.33</td><td>0.01</td><td>-0.35</td><td>-0.33</td><td>-0.30</td><td>0.72</td><td>0.00</td><td>0</td></tr><tr><td>ζ</td><td>18.32</td><td>4.53</td><td>10.75</td><td>17.82</td><td>28.14</td><td>-</td><td>-</td><td>-</td></tr><tr><td>v</td><td>73.06</td><td>17.80</td><td>42.69</td><td>71.26</td><td>112.00</td><td>-</td><td>-</td><td>-</td></tr></table>

\*Estimated scale parameter $( \hat { \lambda } )$ of the baseline hazard.

Our results indicated that the business value of an application (BVM) increased the risk of an application experiencing unauthorized attempts $( \hat { \beta } _ { 1 } = 0 . 2 2 )$ , supporting H1. One level increase in BVM increased the instantaneous probability (or the hazard rate) of an application experiencing unauthorized attempts by 24 percent on average with everything else being equal $( e ^ { \hat { \beta } _ { 1 } } = 1 . 2 4 )$ . Control strength (CSTR) decreased the risk of an application experiencing unauthorized attempts $( \hat { \beta } _ { 2 }$ = -0.33), supporting H2 and one level of increase in CSTR decreased the hazard rate of an application by 28 percent $( e ^ { \hat { \beta } _ { 2 } }$ = 0.72). Access prevalence level (log (APL)) increased the risk of an application experiencing unauthorized attempts $( \hat { \beta } _ { 3 }$ = 0.20), supporting H3. If the number of the users of an application increased 10 times, the application had a hazard rate of 23 percent higher $( e ^ { \hat { \beta } _ { 3 } } = 1 . 2 3 )$ . OLIM increased the risk of an application experiencing unauthorized attempts $( \hat { \beta } _ { 5 }$ = 0.14), supporting H4. An application with OLIM was seen to have a 15 percent higher hazard rate $( e ^ { \hat { \beta } _ { 5 } } = 1 . 1 5 )$ . We also found that data protection level (DPL) decreased the risk of an application experiencing unauthorized attempts $( \hat { \beta } _ { 6 } = - 0 . 3 3 )$ R strongly supporting H5. An application with one level higher of DPL had a 28 percent lower hazard rate on average $( e ^ { \hat { \beta } _ { 6 } } =$ 0.72). None of the Bayes factors supported the null hypotheses $\mathrm { H } _ { 0 } \colon \ \beta _ { i } = 0$ In addition, 95 percent credible intervals for the estimated coefficients did not contain 0. This evidence further indicated the rejection of the null hypothesis $\beta _ { i } = 0$

Figure 2 presents the histogram of the estimated shape parameters $( \hat { \gamma } _ { i } )$ for different app lications. As we can see, the range of $\hat { \gamma } _ { i }$ was between 0.17 and 0.44. This indicated the hazard rate of all applications experiencing unauthorized attempts decreased with time. In other words, the longer an application went without experiencing an unauthorized attempt, the lower the probability of experiencing one.

Figure 3 presents the estimated median survival times and their 95% confidence intervals for each application. The estimated median survival times of an application vary from 0.001 (Application 10) to 2.073 (Application 7) hours, suggesting that Application 10 experienced unauthorized access attempts the most frequently, and Application 7 the least frequently. The shorter the estimated median survival time, the higher is the risk of an application experiencing unauthorized attempts.

![](/api/attachments/YBHAFQ55/fulltext/images/27acc77080297ac33276c49ae68d9e179fb90472cb236ef2b5b2babb357e81c8.jpg)  
Figure 2. Histogram of Estimated λ

![](/api/attachments/YBHAFQ55/fulltext/images/cf724e5efa959aa4462e55176c588043fb023bdbbcde4321454ed72137384c51.jpg)  
Figure 3. Estimated Median Survival Time of Applications with 95 Percent Confidence Interval (n = 1, 2, …, 40)

## Robustness Checking With a Zero-Inflated Poisson-Gamma Model

A second way to quantify insider threat regarding an application is to consider unauthorized attempts experienced by an application as recurrent risky events (Cook and Lawless 2007). We used the daily number of successive unauthorized attempts experienced by an application as an alternative measurement of risk. We developed a zero-inflated Poisson-

Gamma model using the daily number as the dependent variable and the same set of independent variables. Because a simple Poisson model does not allow for the variance to be adjusted independently of the mean, we used a Poisson-Gamma mixture model. The Poisson-Gamma mixture model is a common approach to account for over-dispersion present in the count data (Ntzoufras 2009). In this case, overdispersion was manifested by the fact that the observed variance of the daily number of unauthorized attempts exceeded the variance that a simple Poisson model can expect. Because a significant number of applications did not experience unauthorized attempts on a daily basis, we further extended the model to a zero-inflated model to capture an excess of zero values in our data that cannot be estimated sufficiently by the Poisson-Gamma model (Ntzoufras 2009). The excessive number of zero values for an application may result from (1) the cyclical nature of the supported business function such as month-end or weekend processing and reporting or (2) its specific position in a sequence of operations for the end-toend transaction consummation.

<table><tr><td colspan="8">Table 6. Estimated Coefficients with a Zero-Inflated Poisson-Gamma Model</td></tr><tr><td>Variables</td><td>Mean</td><td>Standard Deviation</td><td>2.5%</td><td>Median</td><td>97.5%</td><td>Posterior Probability of β &gt; 0</td><td>BF in Favor of β = 0</td></tr><tr><td>Constant</td><td>4.36</td><td>0.23</td><td>3.90</td><td>4.38</td><td>4.78</td><td>1.00</td><td>0.00</td></tr><tr><td>BVM</td><td>0.38</td><td>0.03</td><td>0.33</td><td>0.38</td><td>0.43</td><td>1.00</td><td>0.00</td></tr><tr><td>CSTR</td><td>-0.62</td><td>0.04</td><td>-0.70</td><td>-0.62</td><td>-0.54</td><td>0.00</td><td>0.00</td></tr><tr><td>Log10(APL)</td><td>0.64</td><td>0.04</td><td>0.58</td><td>0.64</td><td>0.71</td><td>1.00</td><td>0.00</td></tr><tr><td>OLIM</td><td>0.45</td><td>0.06</td><td>0.34</td><td>0.45</td><td>0.57</td><td>1.00</td><td>0.00</td></tr><tr><td>DPL</td><td>-0.86</td><td>0.03</td><td>-0.92</td><td>-0.86</td><td>-0.79</td><td>0.00</td><td>0.00</td></tr></table>

Let Y be the daily number of unauthorized attempts of an application. We consider that the probability of Y having y occurrences on a day (denoted by f(y)) is

$$
f (y) = \pi_ {0} I (y = 0) + (1 - \pi_ {0}) f _ {P} (y; \eta)
$$

where $\pi _ { 0 }$ is the proportion of additional zeros, I(y – 0) is the distribution with probability of zero value equal to one and all other values zero, and $f _ { P } ( y ; \eta )$ is probability mass function of Poisson distribution with arrival rate of $\eta .$ Following prior studies (Ntzoufras 2009), we specify $\pi _ { 0 }$ follows a Bernoulli distribution with a success probability of $p .$ As different applications have different frequency of zeros, we used different $p$ for different applications. Essentially, the Bernoulli distribution was used to model whether or not an application was used on a given day, and the Poisson distribution was used to model the daily numbers of unauthorized attempts experienced by the application if used. To examine the impact of application characteristics, we modeled the logarithm of the arrival rate η, as a function of application characteristics: $\log ( \eta ) = X \alpha + \varepsilon ,$ where $X = ( x _ { I } , x _ { 2 } , . . . , x _ { K } )$ is the independent variables (i.e., application characteristic measures), $a ^ { \prime } = ( \alpha _ { 1 } , \ : \alpha _ { 2 } , \ : . . . , \ : \alpha _ { K } )$ are the coefficients to be estimated, and ε is the error term. A logarithmic transform ensures the positivity of η. We specify ε follows a gamma distribution.

We estimated the model using MCMC with WinBUGS to obtain posterior distributions of model parameters. We used uninformative but proper priors and hyperpriors for the model. Particularly, we assumed the regression coefficients α to independently follow normal distributions with a mean of zero and a variance of 100, and the success probability of an application $p _ { i } ( i = 1 , 2 , . . . , \mathrm { N } )$ to independently follow a uniform distribution between 0 and 1. As α includes a constant term to make the model identifiable, we have the same shape parameter and a scale parameter for the gamma distribution of the error term across the applications, which follow gamma distributions with a shape of 1 and a scale of 0.001. The estimation model and results are summarized in Table 6. The results are consistent with those in Table 5 based on the Weibull hazard model.

## Discussion

In this study, to understand the reasons for IS applications to have different levels of exposure to insider threats, we extended routine activity theory from criminology literature to information systems security. We synthesized RAT with survival modeling and investigated the risk of insider threats associated with different applications within a financial institution. We developed hypotheses regarding how value, inertia, visibility, accessibility, and guardians impact the risk of insider threats confronted by an application. We introduced two measurements of the risk of insider threats associated with an application: the inter-arrival times of two consecutive unauthorized access attempts, and the daily number of unauthorized attempts. We developed two regression models, a Weibull hazard model and a zero-inflated Poisson-Gamma model, to quantify the risk of insider threats and identify the relevant causes. In response to the call for studies to utilize field data and advance our understanding of insider behavior (Mahmood et al. 2010), our study utilized ESSO log files collected from a regional financial institution for empirical investigation. The results showed how value, inertia, visibility, accessibility and guardians play significant roles in predicting an application’s exposure to risks from unauthorized access attempts.

The study is timely today when both (1) misuse and abuse of IS applications and (2) accidental data disclosures by internal employees are on the rise, as suggested anecdotally in various surveys (e.g., CSI Computer Crime and Security Surveys 2011). Unauthorized attempts to access information launched from within a corporate network have a significant potential for damage, especially when performed by people who are trusted and have knowledge about the corporate systems and processes. Given the scope and scale of such risk, application access monitoring practices are not optional for companies in many sectors, but are required by regulations. The results of the study show how actionable intelligence can be extracted from data gathered through the day-to-day activity of employees’ access and security monitoring. Further, the assessed characteristics of applications shown in this paper can serve as relevant key risk indicators needed for implementing appropriate safeguards that can decrease hazard rates.

## Theoretical Implications

It has been suggested that “proper measurement of information will lead to advances in effectiveness and performance of management” (Drucker 2001, pp. 120-121). One of the implications of this study for researchers in the domain of information security lies in the introduction of measurements for managing risks against insider threats within an organization. We conceptualized and operationalized the risk of insider threats associated with information assets, thus providing a foundation for future research in risk management of digital assets. Risk metrics and models developed in the paper enable us to further investigate causes of the risks. More importantly, these can be used as tools to evaluate the effectiveness of risk mitigation and intervening strategies.

This study extended and empirically validated the applicability of routine activity theory to understand insider threats on IS applications. Consistent with RAT, the results showed that application characteristics (value, inertia, visibility, accessibility) and presence of guardians (i.e., data protection measures) significantly affect an application’s risk of insider threats. The results provided empirical support to the ideas proposed in prior studies on risk assessment and situational crime prevention in the context of insider threats.

Visibility and accessibility of an IS application have been primarily studied in the area of understanding IS success and IS usage. The two constructs are shown to have significant effects explaining usage intention, system acceptance, and system usage (Agarwal and Prasad 1997; Culnan 1983; DeLone and McLean 1992; Goodhue 1995; Karahanna and Straub 1999; Moore and Benbasat 1991). However their effects on the dark side of IS use have never been explored. Our study suggested that these two factors are also important in influencing insiders’ unauthorized access attempts made on an application. This brings home the realization that visibility and accessibility are double-edged swords. Mechanisms to promote positive use and success of an IS application while thwarting risks from insiders could be further investigated.

While inertia is important and essential in explaining traditional criminal behavior (such as predatory crimes), it has been considered irrelevant in digital space because it is very difficult to operationalize due to the “weightlessness” of digital goods (Leadbetter 2000; Yar 2005). Our study extends the concept of inertia to the domain of insider threats to IS applications and introduces a novel operationalization of inertia. The conceptualization and operationalization of inertia are tested based on expert opinions and field data. Our study has indicated that the relevance of inertia in the digital space and virtual world could be further explored within different context of security threats.

## Practical Implications

Effective security management through accurate understanding of risks is increasingly considered an essential business requirement and enabler of business. Our study suggested that practice of risk management of IS applications should be adapted to the organizational context, and account for users’ behavioral patterns. Our study suggested a viable way to conduct quantitative risk assessment of IS applications based on logs that represent user behavior. In the wake of increasing complexities of IS applications and growing interdependencies between business processes that are supported by such applications, quantitative risk assessment can provide richer insights into the risk posture of organizations. The proposed Weibull hazard model and the zero-inflated Poisson-

Gamma models could be used to help security managers quantify localized insider risk, while allowing them to understand the relative attack-proneness of some applications against others in the organizational context. This may allow managers to construct coherent and cohesive risk scenarios and identify risk factors to develop emerging risk profiles of their applications. High-risk applications may be identified based on the estimated median survival times (see Figure 3). Resources for protection and hardening of applications could be allocated based on their relative risk levels. Due to the ever-evolving nature of threat actions and agents, the results of the study provided a much needed basis for risk prioritization and risk response selection.

The results of this study will enable security managers to understand sources of risks to IS applications based on the five aspects suggested by RAT: VIVA and the presence (or absence) of guardians. The insights could be utilized when security managers prioritize their resources and continuously improve their risk management practices. To achieve maximum cost-effectiveness, identified risk factors can be used to employ distinct situational crime prevention techniques to change insiders’ perception of value, inertia, visibility, accessibility, and presence of safeguards. This will aid in risk response selection based on an organization’s own risk appetite and tolerance. The managers can then select risk response options based on their capability to implement responses and the effectiveness of applied responses. One of the important implications of our study, as per our conversation with a vice president at the financial institution, is that it could be used to uncover risks that are hidden and layered within the mundaneness of day-to-day operational (routine) happenings. Analyzing the behavioral predispositions buried inside the access logs can present a unique risk landscape for applications, which managers can use to develop different security strategies for applications.

The study suggested that greater visibility (APL) and accessibility (OLIM) increased, while greater inertia (control strength, CSTR) decreased the risks to application. In most cases, visibility and accessibility requirements are driven by business needs, and could potentially hamper business functions if they are decreased. This provides a unique recommendation for application and security managers to improve control strength for applications needing higher visibility and accessibility to provide effective mitigation against increased risks. The study showed that one level of increase in CSTR decreased the hazard rate of an application by 28 percent. This finding becomes pertinent in practice owing to the fact that each application works within several controls; enhancing an existing or implementing a new (exclusive or compensatory) control can have a far-reaching impact on improving the overall security of an application.

Our discussion with the vice president of the financial institution revealed other interesting insights as well. Most of the applications that showed higher survival mean times were related to the company’s asset management applications rather than transaction systems. Examples include applications managing commercial and retail loans. These applications contain and process a customer’s financial information, including both an historical and a current account of financial health. At the same time, the applications witnessing less survival times were the ones containing information to which employees could relate, such as compensation management systems and other departmental document management systems. This provides a unique view into how employees were attracted by different types of information within the financial institution. The results of the quantitative risk analysis present insights that are relatively unintuitive or experience driven. For example, applications 4, 10, 24, 34, and 40 had survival times less than 1 minute and hence should have higher priority during risk response planning. These applications are from different departments and serve contrastingly different business and support functions of the financial firm from which the data were collected. Application (#4) is an internal talent and career management application, which is only available to internal employees (user base of around 15,000), while two of the others (#34 and #40) are retail customer facing (with a potential user base of 1.2 million) and the fourth is a departmental collaboration application (with about 120 users). The awareness that applications, serving such contrasting business functions, could share similar risk profiles would not be possible for managers without insights from the study. Overall, the results of our study are valuable for effective risk management for organizations.

## Conclusions

Insiders pose serious threats to organizations’ digital assets that are difficult to prevent and mitigate. This study considers unauthorized access attempts as one major indication of insider threats to information systems applications. To quantify insider risk associated with applications, we synthesized routine activity theory with survival modeling. The results of the study provided empirical evidence supporting the utility of RAT-based risk assessment and mitigation approaches. The regression models developed in the study can be used as tools for security risk quantification as well as investigating the contributing factors or the effectiveness of risk mitigation approaches within the user base and application portfolio of an enterprise.

Our study has several limitations. First, we assessed application risk based on historical access logs. The underlying assumption for the assessment is that the patterns observed are an appropriate basis to infer future patterns. This assumption might not hold when there are organizational or infrastructural changes in the organization. Second, routine activity theory only focuses on a limited set of factors (characterized by VIVA and the presence of a guardian) to explain the risk of insider threats; other influences such as overall organizational culture or external factors are beyond what routine activity theory can explain. Third, the study relies on the data from a single organization, and the generalizability of our results could be improved by using the data from different organizations. Fourth, based on the log data, we were not able to recognize whether an unauthorized attempt is an honest mistake (which may depend on users’ frequency of access and the length of their experience with the system) or carries malicious intention.

Future work can extend the results of the study in a number of ways. First, we considered unauthorized attempts regarding an application as the event under risk. The relationship between the frequency of unauthorized attempts and the frequency of security incidents experienced by an application could be explored in future. Second, we noticed that, in our logs, about two-thirds of the ESSO users never made a single unauthorized attempt on an application in our observation period. The difference between the users who made at least one attempt and those who made no attempt could be investigated. In addition, users may differ in terms of their criminal inclination and their ability to act on that inclination (Williams 2008), and there could be behavioral heterogeneity in their target selection. Users may be clustered based on the level of risk they impose on IS applications. Fourth, we also wonder whether an insider’s behavior will evolve over time in terms of their unauthorized attempts. For example, when a malicious insider is new to the system, he may not be aware of applications in the organization or the presence of safeguards. He may not make many unauthorized attempts. As time goes by, he becomes familiar with applications and the placement of safeguards. And he may be able to make more calculated attempts. Consequently, his number of unauthorized attempts could increase over time. But this phenomenon may not occur for a benign user, because she becomes more aware of her system privileges and is less likely to make errors as time goes by.

## Acknowledgments

We thank the senior editor, the associate editor, and the referees for their critical comments that have greatly improved the paper. We thank the various vice presidents and managers of the financial institution for their time regarding this paper. This research was supported by the National Science Foundation under grants SES-1420758 and SES-1419856 . The usual disclaimer applies.

## References

Abercrombie, R., and Sheldon, F. 2009. “Managing Complex IT Security Processes with Value Based Measures,” in Proceedings of the 2009 IEEE Symposium on Computational Intelligence in Cyber Security, Nashville, TN, April 1.

Agarwal, R., and Prasad, J. 1997. “The Role of Innovation Characteristics and Perceived Voluntariness in the Acceptance of Information Technologies,” Decision Sciences (28:3), pp. 557-582.

Akers, R. L., and Sellers, C. S. 2008. Criminological Theories: Introduction, Evaluation, and Application $( 5 ^ { \mathrm { t h } } \mathrm { e d . } )$ , New York: Oxford University Press.

Allison, P. D. 1995. Survival Analysis Using SAS: A Practical Guide, Cary, NC: SAS Institute Inc.

Baracaldo, N., and Joshi, J. 2013. “An Adaptive Risk Management and Access Control Framework to Mitigate Insider Threats,” Computers & Security (39), ), pp. 237-254.

Barron, F. H., and Barret, B. E. 1996. “Decision Quality Using Ranked Attribute Weights,” Management Science (42), pp. 1515-1523.

Baskerville, R. 1993. “Information Systems Security Design Methods: Implications for Information Systems Development,” ACM Computing Surveys (25:4), pp. 375-414.

Beavon, D., Brantingham, P. L., and Brantingham, P. J. 1994. “The Influence of Street Networks on the Patterning of Property Offenses,” in Crime Prevention Studies, R. V. Clarke (ed.). New York: Willow Tree Press, pp. 149-163.

Bennett, R. 1991. “Routine Activities: A Cross-National Assessment of a Criminological Perspective,” Social Forces (70), pp. 147-163.

Bernasco, W. 2006. “Co-Offending and the Choice of Target Areas in Burglary,” Journal of Investigative Psychology and Offender Profiling (3), pp. 139-155.

Brooks, S., and Gelman, A. 1998. “Alternative Methods for Monitoring Convergence of Iterative Simulations,” Journal of Computational and Graphical Statistics (7), pp. 434-455.

Calder, A., and von Bon, J. 2006. Information Security Based on ISO 27001/ISO 17799: A Management Guide, Zaltbommel, The Netherlands: Van Haren Publishing.

Cappelli, D. M., Moore, A. P., and Trzeciak, R. F. 2012. The CERT Guide to Insider Threats: How to Prevent, Detect, and Respond to Information Technology Crimes (Theft, Sabotage, Fraud), Boston: Addison-Wesley.

Cardinal, L. B., Sitkin, S. B., and Long, C. P. 2004. “Balancing and Rebalancing in the Creation and Evolution of Organizational Control,” Organization Science (15:4), pp. 411-431.

Chinchani, R., Ha, D., Iyer, A., Ngo, H., and Upadhyaya, S. 2006. “Insider Threat Assessment: Model, Analysis and Tool,” in Network Security, S. Huang, D. MacCallum, and D. Du (eds.). New York: Springer, pp. 143-174.

Choi, K.. 2008. “Computer Crime Victimization and Integrated Theory: An Empirical Assessment “ International Journal of Cyber Criminology (2:1), pp. 308-333.

Cleary, B. 2008. “Employee Role Changes and SocGen: Good Lessons from a Bad Example,” SC Magazine, April 1 (http://www.scmagazine.com/).

Cohen, L. E., and Felson, M. 1979. “Social Change and Crime Rate Trends: A Routine Activity Approach,” American Sociological Review (44:4), pp. 588-608.

Collett, D. 2003. Modeling Survival Data in Medical Research (2<sup>nd</sup> ed.), Boca Raton, FL: Chapman and Hall/CRC.

Colwill, C. 2009. “Human Factors in Information Security: The Insider Threat—Who Can You Trust These Days?,” Information Security Technical Report (14:4), pp. 186-196.

Congdon, P. 2003. Applied Bayesian Modeling, Hoboken, NJ: Wiley & Sons Ltd.

Cook, R. J., and Lawless, J. F. 2007. The Statistical Analysis of Recurrent Events, New York: Springer.

CSI. 2011. 2010/2011 Computer Crime and Security Survey (available at http://reports.informationweek.com/cart/index/ downloadasset/id/7377; accessed October 10, 2014).

Culnan, M. 1983. “Environmental Scanning: The Effects of Task Complexity and Source Accessibility on Information Gathering Behavior,” Decision Sciences (14:2), pp. 194-206.

Culnan, M. J. 1985. “The Dimensions of Perceived Accessibility to Information: Implications for the Delivery of Information Systems and Services,” Journal of the American Society for Information Science (36:5), pp. 302-308.

D’Arcy, J., and Herath, T. 2011. “A Review and Analysis of Deterrence Theory in the IS Security Literature: Making Sense of the Disparate Findings,” European Journal of Information Systems (20), pp. 643-658.

D’Arcy, J., Hovav, A., and Galletta, D. 2009. “User Awareness of Security Countermeasures and Its Impact on Information Systems Misuse: A Deterrence Approach,” Information Systems Research (20:1), pp. 79-98.

Davis, M. A. 2010. “Research: 2010 Strategic Security Survey: Global Threat Local Pain,” Information Week, April 30 (http://reports.informationweek.com/).

Davis, M. A. 2011. “Research: 2011 Strategic Security Survey: CEOs Take Notice,” InformationWeek, April 2 (http://reports. informationweek.com/).

Davis, M.A. 2013. “Research: 2013 Strategic Security Survey: A Seat at the Table,” InformationWeek, May 2 (http://reports. informationweek.com/).

Dellaportas, P., and Smith, A. F. M. 1993. “Bayesian Inference for Generalized Linear and Proportional Hazards Model Via Gibbs Sampling,” Applied Statistics (42), pp. 443-460.

DeLone, W. H., and McLean, E. R. 1992. “Information Systems Success: The Quest for the Dependent Variable,” Information Systems Research (3:1), pp. 60-95.

Dhillon, D., and Torkzadeh, G. 2006. “Value-Focused Assessment of Information System Security in Organization,” Information Systems Journal (16), pp. 293-314.

Dhillon, G., and Moores, S. 2001. “Computer Crimes: Theorizing About the Enemy Within,” Computers and Security (20:8), pp. 715-723.

Drucker, P. 2001. The Essential Drucker. New York: Harper Business.

Eckenrode, R. T. 1965. “Weighting Multiple Criteria,” Management Science (12), pp. 180-192.

Felson, M. 2010. Crime and Everyday Life (4<sup>th</sup> ed.), Thousand Oaks, CA: Sage Publications.

Felson, M., and Clarke, R. V. 1998. “Opportunity Makes the Thief: Practical Theory for Crime Prevention,” Home Office, Policing and Reducing Crime Unit Research, Development and Statistics Directorate, London.

Fidel, R., and Green, M. 2004. “The Many Faces of Accessibility: Engineers’ Perception of Information Sources,” Information Processing & Management (40), pp. 563-581.

Geer, D. 2005. “Security Technologies Go Phishing,” Computer (38:6), pp. 18-21.

Gelman, A., Carlin, J. B., Stern, H. S., and Rubin, D. B. 2003. Bayesian Data Analysis (2<sup>nd</sup> ed.), Boca Raton, FL: Chapman & Hall/CRC.

Goodhue, D. 1995. “Understanding User Evaluations of Information Systems,” Management Science (41:12), pp. 1827-1844.

Goodhue, D., and Straub, D. 1991. “Security Concerns of Systems Users: A Study of Perceptions of the Adequacy of Security Measures,” Information and Management (20:1), pp. 13-27.

Gorge, M. 2008. “Data Protection: Why Are Organisations Still Missing the Point? ,” Computer Fraud & Security (2008:6), pp. 5-8.

Harrington, S. 1996. “The Effects of Ethics and Personal Denial of Responsibility on Computer Abuse Judgements and Intentions.,” MIS Quarterly (20:3), pp. 257-277.

Hartel, P., Junger, M., and Wieringa, R. 2010. “Cyber-Crime Science = Crime Science + Information Security,” Centre for Telematics and Information Technology University of Twente, Enschede, The Netherlands.

Hiles, A. 2007. The Definitive Handbook of Business Continuity Management, Hoboken, NJ: John Wiley and Sons.

Huth, C. L., Chadwick, D. W., Claycomb, W. R., and You, I. 2013. “Guest Editorial: A Brief Overview of Data Leakage and Insider Threats,” Information Systems Frontiers (15:1), pp. 1-4.

Kaplan, E. L., and Meier, P. 1958. “Nonparametric Estimation from Incomplete Observations “ Journal of the American Statistical Association (53:282), pp. 457-481.

Karahanna, E., and Straub, D. W. 1999. “The Psychological Origins of Perceived Usefulness and Ease-of-Use,” Information & Management (35), pp. 237-250.

Kass, R. E., and Raftery, A. E. 1995. “Bayes Factors,” Journal of the American Statistical Association (90), pp. 773-795.

Kim, S. W., and Ibrahim, J. G. 2000. “Default Bayes Factors for Generalized Linear Models,” Journal of Statistical Planning and Inference (87), pp. 301-315.

Kirkwood, C. W., and Sarin, R. K. 1985. “Ranking with Partial Information: A Method and an Application,” Operations Research (33), pp. 38-48.

Klein, J. P., and Moeschberger, M. L. 2003. Survival Analysis: Techniques for Censored and Truncated Data, New York: Springer.

Kotulic, A., and Clark, J. G. 2004. “Why There Aren’t More Information Security Research Studies,” Information & Management (41), pp. 597-607.

Laudon, K., and Laudon, J. 2012. Essentials of MIS (10<sup>th</sup> ed.), Upper Saddle River, NJ: Prentice Hall.

Leadbetter, C. 2000. The Weightless Society, New York: W. W. Norton.

Loch, K. D., Carr, H. H., and Warkentin, M. E. 1992. “Threats to Information Systems: Today’s Reality, Yesterday’s Understanding,” MIS Quarterly (16), pp. 173-186.

Magklaras, G., and Furnell, S. 2001. “Insider Threat Prediction Tool: Evaluating the Probability of It Misuse,” Computers & Security (21:1), pp. 62-73.

Mahmood, A. M., Siponen, M., Straub, D. W., Rao, R., and Raghu, T. S. 2010. “Moving toward Black Hat Research in Information Systems Security,” MIS Quarterly (34:3), pp. 431-433.

Manadhata, P. K., and Wing, J. M. 2011. “An Attack Surface Metric,” IEEE Transactions on Software Engineering (37:3), pp 371-286.

Mantel, N. 1966. “Evaluation of Survival Data and Two New Rank Order Statistics Arising in its Considerations,” Cancer Chemotherapy Reports (50), pp. 163-170.

McGilchrist, C., and Aisbett, C. 1991. “Regression with Frailty in Survival Analysis,” Biometrics (47), pp. 461-466.

Mishra, S., and Dhillon, G. 2008. “Defining Internal Control Objectives for Information Systems Security: A Value Focused Assessment,” in Proceedings of 16<sup>th</sup> European Conference on Information Systems, Galway, Ireland.

Moore, G. C., and Benbasat, I. 1991. “ Development of an Instrument to Measure the Perceptions of Adopting an Information Technology Innovation,” Information Systems Research (2:3), pp. 192-222.

Neubauer, T., Klemen, M., and Biffl, S. 2005. “Business Process-Based Valuation of IT-Security,” in Proceedings of the Seventh International Workshop on Economics-Driven Software Engineering Research, International Conference on Software Engineering, St. Louis, MO, pp. 1-5.

Neumann, P. 1999. “The Challenges of Insider Misuse,” paper presented at the Workshop on Preventing, Detecting, and Responding to Malicious Insider Misuse, Santa Monica, CA, August 16-18, pp. 16-18.

Ntzoufras, I. 2009. Bayesian Modeling Using WinBUGS, Hoboken, NJ: John Wiley & Sons.

Oltsik, J. 2013. “The 2013 Vormetric/ESG Insider Threat Report,” The Enterprise Strategy Group, Inc., Milford, MA.

Panda Security. 2010. “The Cyber-Crime Black Market: Uncovered,” Panda Security, Madrid, Spain.

Parker, D. B. 1998. Fighting Computer Crime: A New Framework for Protecting Information, New York: John Wiley and Sons.

Peto, R., and Peto, J. 1972. “Asymptotically Efficient Rank Invariance Test Procedures (with Discussion),” Journal of the Royal Statistical Association (Series A) (135), pp. 185-206.

Randazzo, M. R., Keeney, M., Kowalski, E., Cappelli, D., and Moore, A. 2004. “Insider Threat Study: Illicit Cyber Activity in the Banking and Finance Sector,” U.S. Secret Service and CERT Coordination Center/Carnegie Mellon University Software Engineering Institute.

Richardson, R. 2008. “2008 CSI Computer Crime & Security Survey,” Computer Security Institute (available at http://i.zdnet. com/blogs/csisurvey2008.pdf ; accessed October 10, 2014).

Sandhu, R. S., Coyne, E. J., Feinstein, H. L., and Youman, C. E. 1996. “Role-Based Access Control Models “ Computer (29:2), pp. 38-47.

Sarkar, K. R. 2010. “Assessing Insider Threats to Information Security Using Technical, Behavioural and Organisational Measures,” Information Security Technical Report (15:1), pp. 112-133.

Schultz, E. E. 2002. “A Framework for Understanding and Predicting Insider Attacks,” Computers and Security (21:6), pp. 526-531.

Sherman, L. W., Gartin, P. R., and Buerger, M. E. 1989. “Hot Spots of Predatory Crime: Routine Activities and the Criminology of Place,” Criminology (27), pp. 27-55.

Sinharay, S. 2004. “Experiences with Markov Chain Monte Carlo Convergence Assessment in Two Psychometric Examples,” Journal of Educational and Behavioral Statistics (29:4), pp. 461-488.

Siponen, M., and Vance, A. 2014. “Guidelines for Improving the Contextual Relevance of Field Surveys: The Case of Information Security Policy Violations,” European Journal of Information Systems (23:3), pp. 289-305.

Smith, S., Winchester, D., Bunker, D., and Jamieson, R. 2010. “Circuits of Power: A Study of Mandated Compliance to an Information Systems Security De Jure Standard in a Government Organization,” MIS Quarterly (34:3), pp. 463-486.

Smith, W .R., Frazee, S. G., and Davison, E. L. 2000. “Furthering the Integration of Routine Activity and Social Disorganization Theories: Small Units of Analysis and the Study of Street Robbery as a Diffusion Process,” Criminology (38:2), pp. 489-524.

Spears, J. L., and Barki, H. 2010. “User Participation in Information Systems Security Risk Management,” MIS Quarterly (34:3), pp. 503-522.

Spiegelhalter, D., Thomas, A., Best, N., and Lunn, D. 2003. WinBUGS User Manual, Version 1.4,, MRC Biostatistics Unit, Cambridge Institute of Public Health, Cambridge, UK.

Stoneburner, G., Goguen, A., and Feringa, A. 2002. “Risk Management Guide for Information Technology Systems: Recommendations of the National Institute of Standards and Technology,” NIST Special Publication 800-30, U.S. Department of Commerce (http://csrc.nist.gov/publications/nistpubs/800-30/ sp800-30.pdf).

Straub, D. 1990. “Effective IS Security: An Empirical Study,” Information Systems Research (1:3), pp. 255-276.

Straub, D., and Nance, W. 1990. “Discovering and Disciplining Computer Abuse in Organizations: A Field Study,” MIS Quarterly (14:1), pp. 45-60.

Straub, D., and Welke, R. 1998. “Coping with Systems Risk: Security Planning Models for Management Decision Making,” MIS Quarterly (22:4), pp. 441-469.

Tseloni, A., Wittebrood, K., Farrell, G., and Pease, K. 2004. “Burglary Victimization in England and Wales, the Unites States and the Netherlands: A Cross-National Comparative Test of Routine Activities and Lifestyle Theories,” British Journal of Criminology (44), pp. 66-91.

University of Maine System. 2005. “University of Maine System HIPAA General Operating Policy #102 Risk Analysis,” University of Maine, Orono, ME.

Wang, J., Chaudhury, A., and Rao, H. R. 2008. “A Value-at-Risk Approach to Information Security Investment,” Information Systems Research (19:1), pp. 106-120.

Warkentin, M., and Willison, R. 2009. “Behavioral and Policy Issues in Information Systems Security: The Insider Threat,” European Journal of Information Systems (18), pp. 101-105.

Washington University in St Louis. 2005. “HIPAA Security Procedure #2, Risk Assessment and Management Report,” School of Medicine, Department of Radiation Oncology, Washington University in St Louis, St Louis, MO.

Weber, R. A. 1998. Information Systems Control and Audit, Upper Saddle River, NJ: Pearson Education.

Wilkinson, J. W., Cerullo, M. J., Raval, V., and Wong-On-Wing, B. 1999. Accounting Information Systems: Essential Concepts and Applications (4<sup>th</sup> ed.), Hoboken, NJ: John Wiley & Sons, Inc.

Williams, K. S. 2008. Textbook on Criminology, Oxford, UK: Oxford University Press.

Willison, R. 2006a. “Understanding the Offender/Environment Dynamic for Computer Crimes,” Information Technology & People (19:2), pp. 170-186.

Willison, R. 2006b. “Understanding the Perpetration of Employee Computer Crime in the Organizational Context,” Information and Organization (16), pp. 304-324.

Willison, R., and Backhouse, J. 2006. “Opportunities for Computer Abuse: Considering Systems Risk from the Offender’s Perspective,” European Journal of Information Systems (15), pp. 403-414.

Willison, R., and Siponen, M. 2009. “Overcoming the Insider: Reducing Employee Computer Crime through Situational Crime Prevention,” Communications of the ACM (52:9), pp. 133-137.

Willison, R., and Warkentin, M. 2013. “Beyond Deterrence: An Expanded View of Employee Computer Abuse,” MIS Quarterly (37:1), pp. 1-20.

Wood, B. J. 2000. “An Insider Threat Model for Adversary Simulation,” in Rand Conference Proceedings: Research on Mitigating the Insider Threat to Information Systems–#2, R. H. Anderson, T. Bozek, T. Longstaff, W. Meitzler, M. Skroch, and K. Van Wyk (eds.), Arlington, VA.

Xu, H., Teo, H.-H., Tan, B. C. Y., and Agarwal, R. 2012. “Effects of Individual Self-Protection, Industry Self-Regulation, and Government Regulation on Privacy Concerns: A Study of Location-Based Services,” Information Systems Research (23:4), pp. 1342-1363.

Yar, M. 2005. “The Novelty of ‘Cyber Crime’: An Assessment in Light of Routine Activity Theory,” European Society of Criminology (2), pp. 407-427.

Yucedal, B. 2010. “Victimization in Cyberspace: An Application of Routine Activity and Lifestyle Exposure Theories,” unpublished doctoral dissertation, Department of Political Science, Kent State University, Kent, OH.

Zeller, T. 2005. “Black Market in Stolen Credit Card Data Thrives on Internet,” The New York Times, Technology, June 21.

## About the Authors

Jingguo Wang is an associate professor of information systems at the University of Texas at Arlington. He received his Ph.D. in Management Science and Systems from the State University of New York at Buffalo. His current research interests are in the areas of cyber crime and information security, information search, and decision making. His work has been published in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, ACM Transactions on Management Information Systems, IEEE Transactions on Systems, Man and Cybernetics (Part C), European Journal of Operational Research, Decision Support Systems, among others.

Manish Gupta is an adjunct assistant professor at State University of New York at Buffalo and also Vice President of Information Security at M&T Bank. He earned his Ph.D. and MBA from State University of New York at Buffalo. He has authored or coauthored more than 60 research articles published in journals, books, and conference proceedings, and has coedited seven books, primarily in the area of information assurance and security. Manish has more than 15 years of professional experience in various aspects of IT risk management and cyber security.

H. Raghav Rao is SUNY Distinguished Service Professor at the University at Buffalo. He graduated from Purdue University. He has published over 150 articles in archival journals and has received best paper awards from Information Systems Research and best paper and best paper runner-up awards from several conferences such as the International Conference on Information Systems.

# INSIDER THREATS IN A FINANCIAL INSTITUTION: ANALYSIS OF ATTACK-PRONENESS OF INFORMATION SYSTEMS APPLICATIONS

Jingguo Wang Information Systems and Operations Management, College of Business, University of Texas at Arlington, Arlington, TX 76019 U.S.A. {jwang@uta.edu}

Manish Gupta and H. Raghav Rao Management Science and Systems, School of Management, State University of New York at Buffalo, Buffalo, NY 14260-4000 U.S.A. {mgupta3@buffalo.edu} {mgmtrao@buffalo.edu}

## Appendix A

## System Architecture and Functionality of SiteMinder Web Access Manager (WAM)

WAM is an enterprise single sign-on (ESSO) system providing centralized authentication, authorization and auditing to those integrated web based applications and portals. It consists of three core components:

1. Policy Server: This component provides centralized policy management and decisions on authentication and authorization requests made by WAM agent on behalf of the users attempting to access protected resources. The policy server performs key security operations including the following:

Authentication—The policy server supports a range of authentication methods. It can authenticate users based on user names and passwords, via tokens, using forms-based authentication, or through public-key certificates.

Authorization—The policy server is responsible for managing and enforcing access control rules established by the policy server administrator. These rules define the operations allowed for a user on each protected resource.

Administration—The policy server allows for creation and management of authentication and authorization rules for protected web applications. This information is used whenever a user attempts to access a protected application.

Accounting—The policy server generates log files that contain auditing information about the events that occur within the system. These logs can be printed in the form of predefined reports, so that security events or anomalies can be analyzed.

2. Agent: Installed and configured within the context of a standard web server or application server, agents enable SiteMinder to manage access to Web applications according to predefined security policies.

3. Policy Store: This is a repository where all the information managed by the policy server resides.

Figure A1 illustrates an example of the interaction between different components of the system. A user accesses a web resource (typically a web application) through an Internet browser. All requests for application resources will be intercepted by the Siteminder agent installed on the web server running the application before going to the application. The agent will query the policy server to check whether the requested resource is protected or not. If the resource is protected, it will show the user a login page for him/her to enter credentials such as a user name and password. The agent then passes this information to the policy server, which checks a configured user directory for correctness of the user name and password. At the same time, the policy server also looks up the policy store to retrieve any authorization information. If the user is authenticated (i.e., the supplied credentials are correct), the agent passes the authorization information to the application to restrict the privileges of the user. The session is created (commonly through a transient browser-resident cookie) for the user. For any subsequent access to different resources of the application, the agent queries the policy server for an authorization decision. A cookie is also used to create a single-sign-on experience for the user. For example, if the user tries to access protected resources in a different application, the agent running on that server validates the cookie in the browser. If the session is found to be valid, the user is not prompted for login information because the existing session contains the information that the user has already been authenticated. However, different authorization rules are checked for privilege levels within the new application and passed along to the application, so that the user only gets access to authorized resource across multiple applications.

![](/api/attachments/YBHAFQ55/fulltext/images/ec5b0e5f634e5d4634f24d8ef066c03f1a5c61d552ad69ba92e930b8aca85bee.jpg)

Figure A1. ESSO Architecture and Components

## Appendix B

## Mapping Application Characteristics to Routine Activity Theory Constructs: A Delphi Exercise

We carried out a Delphi-type exercise to understand and establish the connection between each application characteristic and routine activity theory constructs. The Delphi method is a commonly used research methodology for building and reporting consensus derived from initial divergent decisions and opinions by subject experts (Yoon 2011). To build consensus it requires an iterative process and anonymity of experts. The experts in our exercises were 13 application owners who were ultimately responsible for the security and risk management of their applications. These application owners had an average of 15 years of direct and relevant experience in managing applications and any associated risks. Their level of domain knowledge, which is the most important factor (Reb and Connolly 2009), would ensure the accuracy and validity of results.

Table B1. Application Characteristics and Routine Activity Theory Constructs

<table><tr><td>Variable</td><td>Application Characteristic</td><td>Routine Activity Theory Construct</td><td>Delphi 2ndRound Mean (STD)</td></tr><tr><td>BVM</td><td>Business Value Measure</td><td>Value</td><td>4.3 (0.48)</td></tr><tr><td>CSTR</td><td>Application Control Strength</td><td>Inertia</td><td>3.8 (0.63)</td></tr><tr><td>APL</td><td>Access Prevalence Level</td><td>Visibility</td><td>3.8 (2.10)</td></tr><tr><td>OLIM</td><td>On-demand Live Information Modification</td><td>Accessibility</td><td>3.9 (0.74)</td></tr><tr><td>DPL</td><td>Data Protection Level</td><td>Guardian</td><td>2.5 (2.64)</td></tr></table>

In the exercise, we asked the experts to identify routine activity theory construct(s) that would best connect to the application characteristics and also rate their confidence on an ordinal scale of 1 to 5 (1 being least confident to 5 being extremely confident). We performed two iterations of data collection. In the first round of data collection, we initially provided a brief primer on routine activity theory and application characteristics to each of the 13 experts (application owners) via e-mail. Then we followed up with a questionnaire to assign ratings for any routine activity theory construct with the application characteristics. We also solicited free-form comments and notes on their choices (which were suggested as optional). After receiving the completed questionnaires, during the second round of data collection, one author had about 30 minutes of telephonic conversation with each expert to explain the overall results regarding routine activity theory constructs and shared other participants’ reasons of their selections. After this, the completed questionnaire was returned to each participant to revise their selections and ratings, if they wished to do so, based on the discussion about other participants’ selections and comments. Ten experts returned usable results. We observed convergence in opinions of the experts in the second round of the study. Table B1 presents the mapping between an application characteristic and the routine activity theory construct to which it relates as well as the means and standard deviations of experts ratings after the second round (on a scale of 1 to 5).

## References

Reb, J., and Connolly, T. 2009. “Myopic Regret Avoidance: Feedback Avoidance and Learning in Repeated Decision Making,” Organizational Behavior and Human Decision Processes (109:2), pp. 182-189.

Yoon, C. 2011. “Theory of Planned Behavior and Ethics Theory in Digital Piracy: An Integrated Model,” Journal of Business Ethics (100:3), pp. 405-417.

## Appendix C

## Sample List of Application Controls

Access re-certification frequency

• A policy to specify the frequency for validation of users who have access to the application

Access to system controlled by enterprise web access management system

• This allows for secure and seamless provisioning, auditing and de-provisioning of user accounts

All deletions are marked for multiple approvals

• To mitigate against attempts to cover tracks and also to minimize accidental deletions

Annual audit of software business process

• Detailed auditing and testing of processes going through the application

Annual training on the system

• This is required for application users and their supervisors, reducing human errors

## Application logs fed to SIEM system

• This allows for stronger and quicker detection of attempts of fraud, drawing events from across multiple applications

## Approval and staging based version control system

• Several layers of approval and strict code migration policy

## Automated fraud detection on select input screens

Implementation of latest technology for analyzing screen inputs for potential fraud (based on correlation of other activities across other modules of same application or other interfacing applications)

## Automated workflow of loan approval with connection with external third party systems to detect/investigate anomalies

• This allows for independent validation of loan-related decisions (often based on provided risk tolerance and other policies)

## Common criteria–based software evaluation

Extensive of standard accredited evaluations of deployed software

## Complex password requirements

• Stronger and more complex requirements than other enterprise applications

## Complies with policies associated with Internet-facing applications

• Much stricter policies for access and management of vulnerabilities

## Continuous surveillance of shared machines that can be used for access to the financial information

• This allows for complete auditing of all the operations done on shared machines for select applications

## Encryption of data in all stages except display

• Stronger security for data processed by the application

## Enforced peer-review process to ensure integrity of BCP (Business Continuity plans)

• Each of these plans are reviewed through simulation by more than 3 independent peer groups

## Enforcement of data segregation

• This is achieved through design of modules and screens; and application roles

## Extensive documentation of use-policy and confidentiality disclosures

• This provides an important aspect of user/human-related risks

## Financial-based controls for integrity and consistency checks

This allows tiered and independent check of financial transactions

## Group-based authorization

• These applications have authorization based on functional and business groups

## Highly detailed functional and technical documentation

• The documentation is explicitly expanded to include much more information than is included in any standard package/implementation

## Inbuilt escalation controls and process

• Automatic queuing of transactions for additional review and approval for certain transactions and processes

## Job rotation

• Express application-based forced rotation for users belonging to specific roles per defined policies

## Output management controls

• This limits the ways data/output can be shared and produced thereby limiting leak and steal

## Part of operational risk oversight program

• This provides additional layers of closer scrutiny or design of application and ensuing operations on the application

## Proprietary encryption for data manipulation and transmission

• This allows for security through obscurity and also keeps data secure

## Real time monitoring of access attempts

These applications have access logs fed to systems that are monitored in real time as opposed to just logging and collection at a central location

## Results of monitoring and testing are maintained by the Compliance Department

• Reviews and audits are overseen by compliance in addition to usual groups

## Second factor authentication for access to specified classification data

Additional authentication enforced for access to higher classification of data

## Strict server and file access limited to firewall procedure only

• Stronger access management and audit trail for access to data

## Strict session controls

• This allows for tight monitoring of user’s actions during a session (also across applications)

## Stringent separation of duties through application role design

• Checks to ensure complete separation of duties per application roles and functions

## Tighter change control within application

• Additional layers of change management for approval and execution

## Use of FIPS (Federal Information Processing) standards for interfacing tools and utilities

• A control for stronger security over transactions and processing

## Real-time backup of images offsite

Strong mitigation against threats to availability of services and data

## Reporting and exception tracking

Transactions and processes outside of baselines are tracked and reported

## Conciliation of vendor records with internal through monthly review process

• A control to reconcile financial numbers and transactions to detect anomalies

## Quarterly penetration testing

• Technical vulnerability assessment of application

## Code Review Controls

• Source code is reviewed on a regular basis, including every time a change is scheduled for implementation

## Appendix D

## Six Levels of Data Protection

The following describes the types of data and the required security protection for the five levels of data protections in the financial institutions used in the field study.

Restricted (5): Information that is extremely sensitive and is intended for use only by select individuals within the company. Examples include personal identification numbers (PIN), PIN offsets, PIN generation keys (PGKs), credit or debit card data (Plastic Card #, ATM card #, etc.) (non-masked), card validation value or code (CAV, CVC, CVV, CSC, CID, CAV2, CVC2, CVV2 numbers, etc.), and “usable” encryption keys.

The following are the minimum security requirements for protection of the data: Encryption on such data is required for electronic storage and all non-trusted connections on public network transmissions. Access to the data is restricted through proper authentication. Physical transport of the data must be compliant with the ANSI approved ASC X9 standards or approval by the information security department. Such data cannot be sent using Internet e-mails or stored using portable media, nor can these data be published on intranet or external sources. Access to the data must be approved and authorized. A nonemployee must sign a nondisclosure agreement to access the data. Physical storage of the data must be in areas with restricted physical access.

Private (4): Information that is intended for use on a need-to-know basis. Data are highly sensitive and are generally governed by governmental privacy laws and regulatory requirements. Examples include nonpublic personal consumer and/or commercial information (e.g., Social Security # (SSN), TIN #, or EIN #) (non-masked), commercial customers’ data, financials, and information about their clients, personnel files, personal health information, merger/acquisition documentation, nonpublished financial information, wire transfer transactions.

Different from Restricted (5) data on the minimum security requirements for protection of the data, encryption on such data is required only for all non-trusted connections on public network transmissions. If encrypted, such data may be sent using Internet e-mails or stored using portable media. Physical transport of the data may be carried out by employees, approved nonemployees, or other approved carriers. Access to such data must be approved and authorized. It can be published on an intranet with proper authentication mechanisms implemented, but not on external sources.

Proprietary (3): Information is intended for use only by specified groups of employees because of its corporate/restrictive nature. Examples include account numbers, market analysis, budget information, operational risk data, and patents, trademarks, or trade secrets, confidential consumer and/or corporate information secured on the intranet (insider). The minimum security requirements for protection of the data are similar with those on Private (4).

Internal (2): Information that is available to all employees. Examples include asset tracking, internal communications, nonconfidential consumer and/or corporate information placed on the intranet (insider). Different from Proprietary (3) and Private (4) data on the minimum security requirements for protection of the data, encryption on such data is not required for electronic transmission and storage. Such data may be sent using Internet e-mails or stored using portable media without encryption. There is no authorization requirement on the access to such data. It can be published on an intranet with proper authentication mechanisms implemented as well as on external sources. Physical storage of the data can be in the possession of an employee or approved nonemployee.

Public (1): Nonsensitive information that is available for general viewing (internal or external) because it is entirely nonsensitive. Examples include information in the public domain, approved press releases, approved marketing information, masked data with no other nonpublic personal consumer and/or commercial information (e.g., Social Security # (SSN), TIN #, or EIN #). There are no minimum security requirements for protection of the data

Not Applicable (0): Information that does not relate to any specific entity or operation. Examples include binary data logged at routers and dropped or lost network datagrams.

## Appendix E

Plot of Against log log logS t <sub>{ }</sub>− ( ) t for Different Applications <sup></sup>  
![](/api/attachments/YBHAFQ55/fulltext/images/7b92d750eeb4d8c7fb944446f5de23f2382c4963e47abaf063e45ba8643899cd.jpg)
