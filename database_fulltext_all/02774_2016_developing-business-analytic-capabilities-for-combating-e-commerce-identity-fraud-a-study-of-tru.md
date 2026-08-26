---
otero_id: 2774
otero_key: "6P3VUGP8"
title: "Developing business analytic capabilities for combating e-commerce identity fraud: A study of Trustev’s digital verification solution"
authors: "Felix Ter Chian Tan; Zixiu Guo; Michael Cahalane; Daniel Cheng"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.07.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Developing business analytic capabilities for combating e-commerce identity fraud: A study of trustev’s digital verification solution

Author: Felix Ter Chian Tan Zixiu Guo Michael Cahalane Daniel Cheng

![](/api/attachments/6P3VUGP8/fulltext/images/92669cf44f0cd02b57ee61bfe32af26aca16da2af05c800f2f4f437ebf6699ad.jpg)

PII: S0378-7206(16)30075-1

DOI: http://dx.doi.org/doi:10.1016/j.im.2016.07.002

Reference: INFMAN 2926

To appear in: INFMAN

Received date: 20-9-2015

Revised date: 3-6-2016

Accepted date: 10-7-2016

Please cite this article as: Felix Ter Chian Tan, Zixiu Guo, Michael Cahalane, Daniel Cheng, Developing business analytic capabilities for combating e-commerce identity fraud: A study of trustev’s digital verification solution, Information and Management http://dx.doi.org/10.1016/j.im.2016.07.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

## DEVELOPING BUSINESS ANALYTIC CAPABILITIES FOR COMBATING e-COMMERCE IDENTITY FRAUD: A STUDY OF TRUSTEV’s DIGITAL VERIFICATION SOLUTION

Author, Affiliation and Email

Felix Ter Chian Tan

UNSW Business School

UNSW Australia, Sydney 2052

Email: f.tan@unsw.edu.au

Zixiu Guo

UNSW Business School

UNSW Australia, Sydney 2052

Email: z.guo@unsw.edu.au

Michael Cahalane

UNSW Business School

UNSW Australia, Sydney 2052

Email: m.cahalane@unsw.edu.au

Daniel Cheng

UNSW Business School, Commonwealth Bank Australia

Australia, Sydney

Email: danielcheng@live.com.au

#

## Abstract

Given the significant growth in e-commerce, organizations are seeking novel capabilities and technological innovations to deal simultaneously with the volume of data generated and the need to combat potentially damaging fraudulent activity. Although recent studies identify business analytics (BA) as a potential means of combating fraud, significant inroads into the interrelationships between capabilities and the articulation of a pathway to analytical capability have yet to be made. This study presents an investigation of Trustev, a global provider of digita verification technology, and its development of the profile-based social fingerprinting fraud detection solution. Adopting an interpretive structural modeling technique for data analysis, we construct a framework and reveal a road map for organizations to become analytically capable in online fraud detection. Our study adds to the discourse of the application of BA to combat online fraud.

Keywords: Online Fraud Detection, Business Analytics Capabilities, Social Fingerprinting

## 1. Introduction

Identity fraud involves the use of a fabricated identity for financial gain or other benefit [1]. As society is moving deeper toward a digital economy, there has been a simultaneous growth in fraudulent transactions [2]. In 2013, an estimated US\$ 3.5 billion in retailer’s revenue was reportedly lost to online fraud, representing a significant increase over the years [3]. Often, security infrastructures in organizations are incapable of keeping up with the changing techniques and trends in criminal behavior, introducing a significant risk of such organizations becoming a target for fraudulent activities [4]. In an effort to reduce the impact of fraud, organizations are now making inroads in the advancement of security among their e-commerce initiatives [1, 4]. In fact, the vendor market for third-party fraud detection tools has substantially changed in recent years, with a number of smaller new players introducing a variety of innovative functionalities dependent on complex data-driven analysis or analytics [5, 6].

#

Correspondingly, the application of business analytics (BA) for controlling identity fraud to drive decisions and actions in organizations is an emergent research area [5, 7, 8].

Despite the possible use of BA to tackle fraud, organizations take a long time to become capable of competing in BA, requiring enormous investments in resources [7]. BA capability – that is, the ability to compete in analytics through organizing, standardizing, and manipulating data – is an important determinant of an organization’s competitive advantage in today’s rapidly changing business environment [7]. Existing literature points to the argument that in leveraging resources to establish a competitive advantage, firms must bundle those resources to create technology-enabled capabilities rooted in processes and business routines [9, 10]. Furthermore, organizations require a nuanced description of not only key components required for analytical capability in online fraud detection but also the relationships and interdependences that exist among analytical capability and organizational factors [7].

Against the above backdrop, this study proposes a framework that identifies a pathway for organizations to become analytically capable for fraud detection. Specifically, this framework seeks to answer the following two research questions: (1) What are the preconditions for organizations to become analytically capable for fraud detection? (2) How do preconditions and BA capabilities interrelate to address fraud detection? Answering these questions provides insights that allow organizations to maximize the value of technological and analytical capability frameworks. While a number of recent studies have proposed BA frameworks that highlight the preconditions for analytic capability [11-15], these frameworks are either conceptual in nature in that they are without empirical justification or they fail to answer the most basic question of how these conditions interrelate to achieve an organization’s goals. Although there has been some indication of such interrelationships among key analytical capability factors [7], a lack of empirical examination hinders the discovery of the nature of these relationships. We argue that an understanding of these relationships will allow organizations to not only identify their analytical capabilities but also leverage better the existing capabilities.

The relevance of this research is established against an increasing use of “big data” and BA in providing innovative solutions to combat fraud [16], such that the maximization of the organizational value from investments made in BA has become a central point of concern for senior executives [13]. In taking advantage of new big data applications, organizations must provide extensive analyses of heterogeneous datasets at unprecedented scales and speeds. We present the exploratory case of Trustev, a global provider of digital verification technology specializing in real-time online identity validation. The organization aims to eliminate fraud from e-commerce transactions using a variety of fraud detection methods. In our study of BA capabilities in fraud detection, we have adopted the theoretical notions of dynamic capabilities and the means–end chain (MEC) theory [17, 18] as a guide to develop a framework. Based on the data gathered from interviews, we have adopted the interpretive structural modeling (ISM) technique [19], a well-established methodology for identifying and developing relationships within a system of related variables. Through our adoption of the ISM technique, we reveal a road map for practitioners who aspire to become analytically capable for online fraud detection.

This paper is structured as follows. First, we discuss online identity fraud and highlight the concept of capabilities in a BA context. Next, we examine the application of the MEC in developing the hierarchical framework for our study. This is followed by an explanation of the research method employed in our work and the results of our investigative findings. This paper concludes with a discussion of the contributions and implications of our work.

## 2. The Need for Analytical Capabilities to Tackle Online Identity Fraud

With the emergence of the digital economy, identity fraud has evolved and taken root among online transactions, affecting banks, e-commerce merchants, and the general public [2]. Identity fraud involves the adoption of another’s personal information to commit fraudulent activity (identity theft) or the intentional misrepresentation of identity for unlawful purposes (identity deception) [1]. Research suggests that identity-related crimes not only have a financial impact [20] but also compromise consumer confidence and trust in service providers [21]. As online activities have become more complicated in recent decades, the ability to effectively manage the risks and costs associated with online fraud has become a major industry challenge [22]. This is because the data involved are qualitatively different in that it is representative of a large “heterogeneous spectrum” of online transactions and interactions [23]. Huge volumes of digital information are required from myriad sources to combat identity fraud, such as sensors, mobile phones, e-commerce websites, GPS, and social media, and this information needs to be analyzed for organizations to understand relationships, predict needs, and avert fraud and waste [24]. Hence, research suggests that higher-performing organizations are implementing BA in their core business functions, allowing for rapid, repeatable, and accurate decisionmaking processes to maximize the potential value of their data [25-27].

Of course, the use of analytics to combat fraud is not new, and contemporary BA is rooted in advances in decision support systems [28]. Taking advantage of data analysis in this manner,

#

credit card companies have conducted fraud detection for many years [2]. While most of the data available are unstructured, a number of important signals can be identified through rigorous data analysis, such as sequences of information access and durations of information exposure, thus enabling better decision making [29]. Such data-driven decision making enables organizations to turn insights into outcomes and consequently generate value. In fact, since 2009, analytics has remained in the top five technology investment priorities in Gartner’s annual survey of chief communication officers [30], with business intelligence/analytics ranked as the first priority in its latest annual report [5]. Moreover, Gartner [5] has predicted that in 2016 25% of large global organizations will adopt big data analytics for use in at least one security or fraud detection case, and it is expected that these organizations will achieve a positive return on investment within the first six months of implementation. Data-driven analytics has enabled fraud solutions to move from traditional identity proofing through verification of credit card, address, telephone, and order history data to more innovative techniques involving geolocation, social networking sites, and biometric indicators as well as vendor-specific fraud-scoring models. Recent studies describe the growing value of using BA to motivate statistical and quantitative analyses, create explanatory and predictive models, and support fact-based management to reach decisions and drive actions [8, 27]. In fact, profitability rates are 5–6% higher for firms with analytics capabilities than for those without [31, 32].

In existing literature, many scholars, including Joshi et al. [33] and Kim et al. [34], confirm the role of technology in creating a strong foundation for the rapid data acquisition and analysis necessary to build organizational capabilities. More recently, scholars have referred to analytics as a form of IT-enabled capability [14, 34]. However, scholars also warn that any IT-enabled shift involves the closer examination of internal business changes, the reconfiguration of resource bases, and the development of new capabilities [35]. Hence, like Cosic et al. [36] and Chae et al. [37], we postulate that a discourse on dynamic capabilities from a resource-based perspective is relevant and useful to reveal how BA capabilities lead to resource exploitation. Dynamic capabilities, a term that describes the capacity of an organization to purposefully create, extend, or modify its resource base [38], stem from the notion that organizational resources are the basis for improved firm performance and sustainable competitive advantages [39]. To clarify, the premise is that although a more complex and large base of organizational resources and IT assets is advantageous when launching a competitive action [40], a firm’s competitive advantage is attributed more to its capabilities and competencies that coordinate, redeploy, and leverage resources [9]. Thus, a resource-based perspective has been identified

#

by several scholars as offering an integrated view of the relationships among IT capabilities and business value [41], such as within a BA context [7, 37].

## 3. The Foundations of a BA Capability Framework

As highlighted earlier, BA capability – which reflects the ability to compete in analytics through organizing, standardizing, and manipulating large volumes of data – is increasingly imperative for organizations to gain a competitive advantage [7]. In recent times, a number of studies have attempted to identify and classify these capabilities and other elements of BA. We present some of them in Table 1 and describe their characteristics. For example, governance, culture, technology, and people have been identified as generic capability areas [14, 36], while multiple sources of data, analytic models, organizational transformation capabilities, strategies, and technology have been identified as supportive capabilities for advanced analytics [14, 31]. These frameworks help us to better understand the notion of BA and the development of BA capabilities.

However, although existing frameworks, as highlighted in Table 1, are useful for identifying BA capabilities, they present some inadequacies, particularly in the context of our research. For instance, some frameworks enclose dynamic BA capabilities as one entity without explaining the interrelationships among identified factors. This impedes us from understanding how identified factors influence one another and how such factors should be prioritized in an analytical organization so as to direct the transformation of business operations. Transitioning from simply identifying BA preconditions and requirements to actually being analytically capable is, understandably, a complex process [42]. While there has been some useful discussion on how to generate BA capabilities [7], there is a lack of consensus on what these capabilities are and how they are linked in a pathway to reveal the achievement of analytical capability. Although there is no straightforward methodology for organizations to adopt when it comes to being analytically capable, there is value in the creation and use of frameworks that not only identify the key elements required for organizations to become analytically capable for fraud detection but also generate a pathway to becoming analytically capable. In sum, we argue that existing research does not provide a clear consensus on BA frameworks, nor does it reveal the necessary pathway to becoming capable of BA in a fraud detection context.

Based on the literature reviewed, we have developed a theoretical framework to guide our investigation of BA capabilities and to create a pathway for fraud detection. Specifically, we have used the theoretical approach of a MEC to consolidate the relationships between preconditions for becoming analytically capable, BA capabilities from a resource-based perspective, and the pathway to achieving fraud detection in our framework.

MEC theory is rooted in the work of Simon [48], who argues that decision makers act in order to achieve desired outcomes or end states. Gutman [17] applied this theory to marketing and advertising research and defined MEC as a model that seeks to explain how product or service attributes facilitate consumers’ achievement of desired end states. Specifically, MEC focuses on the cognitive linkages between the relative concrete attributes (the “means”) of a product or service (or activity or event), the abstract consequences these attributes provide to users, and the highly abstract goals (the “ends”) these consequences help reinforce [18].

Attributes are physical features or observable characteristics of products/service that may be preferred or sought by users. Consequences, which can be functional or psychosocial, reflect the perceived benefits associated with specific attributes. It is consequences, rather than attributes, of a product that represent the reasons why an attribute is important to consumers [49]. Personal values/goals, which are a powerful force in governing individual behaviors for all aspects of people’s lives, are the ultimate factors that drive consumer preference and choice behavior [50]. Overall, MEC perceives consumers as goal-directed decision makers, choosing products that seem most likely to lead to desired outcomes. The attribute–consequence–goal sequence explains how and why product attributes are important.

The MEC theory can be directly applied to an organizational context to uncover underlying intentions and decision processes [17, 18]. In considering the increasing number of features that are important in developing BA capability, we extend the notion of the MEC theory to BA capability development in fraud detection. Organizations that aim to become analytically capable are decision makers aiming to become analytical capable in fraud detection (goals). The factors required for being capable (benefits) are attributes. The framework of such an interrelationship could provide a guide for understanding what is necessary, but it is not sufficient for organizations to achieve the goal of possessing capabilities in fraud detection. It is particularly evident when organizations must balance between resources and increase in capability through funding prioritization. As a result, first, organizations need to select the preconditions among resources and capabilities necessary to achieve BA capability, and second, they need to prioritize investments in a number of preconditions (e.g., human capita expertise, technology) to become analytically capable. We believe that the MEC approach is

#

appropriate as it focuses on the connections among product attributes, decision consequences, and personal values, which are a chain of hierarchically related variables [18].

As shown in Fig. 1, adopting the MEC approach in this study provides us the research opportunity to reveal a sequential structure among the preconditions and a ladder of priorities among such conditions for businesses to become capable of BA for fraud detection. In our framework, “attributes” refer to factors or preconditions that are necessary (but not sufficient) to determine the desired ends of generating values from analytics; “consequences” refer to BA capabilities achieved from experience with preconditions; and “value” refers to the goal of fraud detection. In our framework, we use this sequential structure (see Section 6) to identify a pathway for organizations to become analytically capable for the purpose of fraud detection.

## 4. Research Methodology

The research objective of this study is to develop an empirically guided framework that identifies a pathway for organizations to become analytically capable for the purpose of fraud detection. This objective is operationalized through two research questions: (1) What are the preconditions for organizations to become capable of BA for fraud detection? (2) How do preconditions and BA capabilities interrelate to address fraud detection? In answering these questions, our study provides insights that allow organizations to maximize the value of technological and analytical capability frameworks.

A two-phase interpretive research methodology has been adopted to address the research objective and questions of our study (Table 2). First, we adopted a case study approach [51, 52] to identify and explore how organizations acquire the components required to become analytically capable for fraud detection. The case study approach is appropriate, as the study phenomenon is complex, multifaceted, and embedded within a firm context, which makes examining the phenomenon through stakeholders’ interpretations more suitable than a quantitative approach [53]. Three criteria formed the basis for the case study selection. First, the case organization should be a firm that develops BA capabilities for combating identity fraud. Second, the case organization should be serving customers in identifying online fraud so that the underlying mechanisms can be studied. Third, and related to the first two criteria, the operations of the selected firm should be sophisticated enough, in that the firm should be demonstrating both BA and non-BA capabilities in combatting online fraud. Based on these

criteria, the case study chosen was Trustev, a global provider of digital verification technology. Trustev applies a big data approach coupled with profile-based digital identity management to develop social fingerprinting, an IT-enabled capability to combat identity fraud.

Second, based on data collected from interviews, we adopted the ISM technique to develop a hierarchical framework for BA capabilities in fraud detection used by Trustev. Developed by Warfield [19], ISM is an interactive learning process whereby a set of unique interrelated variables affecting the system under consideration are structured into a comprehensive systemic model [54, 55]. The use of ISM is widespread, and since its inception, various researchers have applied ISM as a technique for modeling a diverse range of complex issues to develop a better understanding of complex systems [56]. The primary objective of ISM is to create a structured model based on interrelated variables from collected data. This method is considered interpretive because identifying the existence of constructs and relationships, and the level to which constructs are related, is left to the judgment of the coder [55]. In other words, we are able to extrapolate implicit relationships from interviews and follow up for further validation. Furthermore, this method is also considered structural because an overall structure is extracted from a complex set of variables based on relationships.

By using the practical experience and knowledge of individuals or groups, ISM provides a means by which people can impose order and direction in complex relationships [57]. For complex relationships, such as the one considered in this study, a number of factors may cause organizations to become analytically capable for online fraud detection. Because people are limited in their ability to address complex issues involving a significant number of variables at one time [58, 59], the use of ISM can advance our collective understanding of such relationships by providing a comprehensive model of an inherently complex and usually impenetrable system [60, 61]. In this way, ISM has enabled us to explore the dynamics of direct and indirect relationships between concepts in analytic fraud detection. Taken in conjunction, the direct and oft hidden indirect relationships between social fingerprinting elements describe the situation far more accurately than do individual factors taken in isolation [62].

## 4.1. Case Study: Trustev

Trustev is a global software platform that develops real-time online identity verification solutions to prevent fraud in e-commerce transactions. The company was named one of Forbes Magazine’s hottest global startups in 2013 and has recently merged with TransUnion in a

#

US\$ 44 million deal in December 2015 to address the global challenge of e-commerce fraud protection [63]. Since its launch in 2013, it has raised almost US\$ 8 million in seed funding.

Trustev [64] is the first hybrid antifraud platform that fuses human intelligence with machine learning. Applying state-of-the-art big data techniques to the traditional concept of fingerprinting (which posits that the impact of skin friction ridges could be used to determine personal identity) and the social side of business, Trustev offers what it calls social fingerprinting. Social fingerprinting is a combination of the elements of a digital identity with dynamic verification technology to formulate a score. Those with a low score have a “suspicious” social fingerprint and thus are more likely to be conducting fraudulent activities. In essence, the company integrates its social fingerprinting technology with other systems to provide authentication services for online retailers and other businesses where verifying customer identity is of paramount importance. The Trustev social fingerprinting solution has proven to be successful since its inception, as its big data initiatives have turned insights into outcomes. Trustev tackles the problem using multiple dynamic data sources (behavioral, transactional, and social) instead of restrictive rules-based decision making and profiling. This enables Trustev to gain maximum insights and therefore maximum trust regarding the actual identities of online merchants’ customers through social media account information.

## 4.2. Data Collection

Various ISM methods for data collection are recommended and used in the literature. Many researchers (including [65-68]) rely on a literature review to generate variables. A literature review to identify variables is commonly conducted when there is a rich theoretical background for the research topic. On the other hand, Cagno et al. [69] have used the results in the literature as a basis for conducting a focus group discussion to identify their variables for occupational safety performance. The intention of the focus group was to refine definitions of factors, content, and links in the literature to their study context. Guo et al. [56] have used interviews to identify the key variables affecting student online learning motivation systems. The rationale for using semi-structured interviews in the present study is that they have enabled us to elicit context-specific and rich content, which was essential for a description of factors and identified interrelationships. Semi-structured interviews allow for the use of open-ended questions to which interviewees can freely respond without being directed or pressured. Hence, semi-structured interviews can be useful in describing processes and systems, integrating perspectives and viewpoints, and fostering an understanding of how and why key factors

interplay in phenomena such as online fraud detection. This was considered vital for the development of our framework.

Thus, in order to use the ISM technique to develop a pathway for organizations to become analytically capable for online fraud detection, we first conducted semi-structured interviews to identify the key components required to foster online fraud detection BA capabilities. Specifically, we conducted 13 semi-structured interviews, mainly with employees of Trustev, to discuss relevant information regarding analytical capabilities and fraud detection. The job titles of the interviewees and the interview topics are summarized in Table 3.

Primary data collection was conducted through face-to-face and telephonic interviews. Each interview lasted 60–90 minutes. The interviews were recorded and transcribed to ensure a complete record was maintained [70, 71], and data analysis was conducted at the same time as the data were gathered. We analyzed the statements from each interviewee and compared the other details of each interview with our theoretical underpinnings. We continued to compare statements with each subsequent set of interview notes. By constantly moving back and forth between the initial statements, the first sets of statements from the interview data and the theoretical perspectives while consulting relevant literature became the foundation of data analysis. We also reviewed secondary data sources, including two product descriptions and customer testimonials from Trustev website and its vendor Datameer on the Trustev solution. Furthermore, several online articles on Trustev’s fraud detection capabilities were gathered from TechCrunch, WIRED, The Next Web, Forbes, and The Huffington Post. Using secondary sources along with interview data enhanced our ability to comprehend the richness of the contextual data. The collected data ensured we were able to identify key elements in the online fraud detection process.

## 5. Data Analysis and Model Development

## 5.1. Trustev’s Fraud Detection Solution

The Trustev strategy for identity verification during online transactions is to combine the elements of a digital identity with dynamic verification technology to formulate a score. This formula is known as a social fingerprinting score (out of 100) and is presented to the merchant or customer. The process of executing the formula during the scoring process resembles a pyramid structure wherein all available profiling scores are grouped in categories; with algorithm and machine learning, these will eventually go to the top of the pyramid and become a single Trustev score.

Social data, behavioral data, transactional data, and historical data are key categories of information that assist in the scoring process. For example, in the social data category, if the investigated account (e.g., a user’s Facebook account) is determined to be fake, the social score is weighted down to zero. This has a significant impact on the overall Trustev score, as it indicates that the account is either compromised or illegitimate. During a transaction scenario, the user or requestor of the transaction will be rejected. During data collection, it was recognized that it is not essential for customers to have social data:

Our logic doesn’t require customer or social input because not everybody has social and not every site has social. So our decision logic is actually dynamic. It recognizes social data and reweights all the other inputs. (Director of Fraud and Data Strategy, Trustev)

According to our respondents, the implementation of Trustev’s social fingerprinting scores consists of many elements. These include adapting machine learning and algorithms to consumer behavior on a customer’s website, establishing profilers, implementing the Trustev real-time decision engine, which calculates the Trustev score, and supporting a customer’s integration of the Trustev solution. The profilers include static, activity, interaction, contact, location, and transaction profiles, which are drawn from various data sources to calculate a score. Those scores are then weighted, and eventually a full Trustev score out of 100 is presented:

You see, all these sources of data that are available create a social graph. Dynamic information that is literally kept up to date by the user, every minute, every day, is being added to . . . their friends, the age profile, what ties in with the profile. All that is part of what builds up the social score . . . If I’m using all the different features in Facebook with the frequent updates, frequent picture updates . . . you can consider a pretty good profile. (CMO, Trustev)

Merchants can use the full Trustev score to verify a customer. A Trustev score below a defined threshold indicates fraudulent activity, and the transaction should be rejected. According to our investigation, this integration is supported by advanced analytics that provide big data visualizations to Trustev customers in a fast and effective way.

## 5.2. Identifying Components of Analytic Fraud Detection Solution

#

To facilitate the interpretation of interview data, we performed content analysis [72] to create thematic categories from the constructs present in the data. The collected data were imported into NVivo 10®, and open coding was applied. We took a systematic approach to the content analysis by looking for distinct concepts in our collected data. More specifically, through open coding, we conceptualized on the first level of abstraction, meaning that whenever an “entity” appeared, it was coded as a construct. We sought out top-level concepts of Trustev’s analytic fraud detection solutions and data fingerprinting. Any subsequent concepts were coded as nextlevel constructs and were categorized as potential preconditions. This process enabled us to code the concepts as constructs with their associated properties and dimensions. Then, after data reduction, constructs were grouped into categories to generate a list of components, as per Corbin and Strauss [73].

Furthermore, we followed the categorization of constructs through an adjusted generic corecategorization procedure outlined by Jankowicz [74]. The process resulted in 58 unique constructs being consolidated into ten categories. These categories became the variables used to establish relationships using the ISM data analysis methodology. As discussed in the previous section, it is common in studies adopting the ISM methodology to use the literature to support the derivation of variables [See 56, 69, 75]. Correspondingly, Schwab [76] asserts that a theoretical definition from the literature can act as a guiding tool to generate items. For example, we derived the term “domain expertise” from the definition of “expertise” by Gartner [5] and Cosic et al. [36].

Table 4 summarizes the coding results in our analysis of the components incorporated in Trustev’s analytic fraud detection solution. These components include (1) algorithm analysis, (2) authentication data, (3) customer requirements, (4) data preprocessing, (5) decision optimization, (6) domain expertise, (7) identity verification, (8), machine learning, (9) record integration, and (10) technology infrastructure. Table 4 provides a definition for each of these components as well as presents sample quotes from our interviews, highlighting their role in Trustev’s fraud detection solution. Having identified these ten components, the next stage of our analysis was to interpret the interrelationships between them, revealing a pathway for exercising BA capabilities for combating online identity fraud.

## 5.3. Relationships among Components of the Fraud Detection Solution

As explained earlier, the function of ISM is to identify relationships between variables (represented by the components in our study) identified in preliminary research and to present a structural model illustration. Based on the ISM process and the set of variables considered for ISM development presented previously in Table 4, we first denoted these variables as V<sub>i</sub> in sequence, where i = 1,2,3,4,5,6,7,8,9,10. Next, we needed to establish the contextual relations between each variable pair to indicate the type of ISM structure to use. In other words, we wanted to find the pairwise relationships between the ten components of analytic fraud detection The identification of contextual relationships is one of the fundamental concepts of the ISM methodology [77], in which the main requirement for developing contextual relations is the use of expert opinions based on various management techniques, such as brainstorming or the nominal technique [65, 78, 79]. Thus, in this study we applied a mixed-method approach using the literature review, semi-structured interviews, and follow-up expert opinions to gather variables and identify the contextual relationships among them.

The literature review provided us with an initial understanding of the variables influencing BA capabilities in general. We approached three Trustev fraud detection experts to seek their opinions about the contextual relationships among the 10 identified variables. Then we reviewed the interview transcripts to validate the relationships indicated by the experts. We followed the intent structure, whereby contextual relations include clarifying, thinking about, or explaining what an organization aims to accomplish and providing a basis for action [80]. This provided us with a foundation to begin structuring a framework. Then, by taking majority opinions, we obtained a total of 55 pairwise relationships [81]. With the variables and their contextual relations, we could perform the remaining steps in the ISM analysis to construct the framework, as presented in Appendix 1.

After obtaining the contextual relationships among all the identified constructs, we followed the ISM procedure to establish the framework for developing BA capabilities. First, we categorized the contextual relations to map out a structural self-interaction matrix (SSIM). Next, we followed the MatLab codes described in Guo et al. [56] to obtain a reachability matrix from the binary matrix. Appendix 1 summarizes the development of the SSIM, the reachability matrix, the partitioning level, and the canonical matrix. Finally, and from the development of the metrics, we were able to develop a diagraph (see Fig. 2). The purpose of the diagraph is to visually represent the contextual relationships between all the analytic fraud detection variables in a hierarchy, as derived from the ISM process. With the diagraph constructed, we substituted the variable numbers with their respective variable names to produce the interpretive structural framework for this study, as shown later in Fig. 3 (see Section 6). In the diagraph, we can identify the 10 components of analytic fraud detection structured into six levels indicated on the left. The arrows connecting the components indicate their interrelationships, through which certain components lead to the development of other components. For explanatory purposes, we discuss the interpretation of these relationships in our findings.

## 6. Findings: Toward a Framework for Combating Identity Fraud

Our analysis reveals a framework that elucidates the development of BA capabilities and a pathway to developing specific BA capabilities for combating online identity fraud (Fig. 3). In light of earlier conceptualizations in Fig. 1 (i.e., attributes → consequences → value), our framework purports the interrelationships between five preconditions for firms to become capable of BA (attributes) and develop three BA capabilities (consequence) and two new capabilities for fraud detection (value), revealing a pathway to combat online fraud in the framework above. Again, we refer our readers to Table 4, which specifies each component of our framework and provides representative quotes from our interviews.

Our framework has implications for both research and practice. Against the background of prior research identifying business intelligence capabilities [for example 13, 82, 83], we extend this understanding and discuss how our study reveals that these capabilities work together and cannot be viewed in isolation. Our framework sheds new light on how the isolated factors of BA capabilities identified in previous studies are interrelated, allowing for the development of a clear consensus on the necessary preconditions and a road map for similar businesses toward BA capability. In practice, we give information about the formation of BA capabilities, representing the first steps to accelerating business objectives, leading to value creation, competitive advantage, and firm performance [7, 11, 14, 84], and reducing risks to the long-term sustainability of an organization as well as adverse effects on its employees and investors [85].

Further analysis of the ISM (Fig. 3) shows that, among the wide spectrum of BA capability components identified for fraud detection, they play different roles in the pathway of developing fraud detection capability. First, authentication data, domain expertise, data preprocessing, customer requirements, and technological infrastructure, which are located at the bottom of the framework, are highly important but interrelated preconditions required for developing BA capability in fraud detection. Among them, authentication data is one of the fundamental conditions for being analytically capable. In fact, [47] notes that the accessibility of (online) data is key to becoming an analytically transformed organization. In their study, the PADIE technique

#

highlights the identification of “who, what, where, when, why, and how” as sources of data. Then the online authentication data are used to drive analytic inquiries and gain insights. From our case study, we have identified four categorical sources of data that assist in the scoring process: social data, behavioral data, transactional data, and historical data. In the case of the Trustev solution, the user’s online profile is captured, and the published content on social media platforms is analyzed (including location tagging, number of friends, age group, and other public information linking the user and the activities associated with his or her online profile). Our study reveals that combining information on both physical and digital locations is crucial, especially in light of increasing numbers of mobile device users [8, 86]. For instance, the geolocation tagging feature on smartphones allows platforms to digitally record a user’s location via uploaded content based on where photos are taken, and both status updates and conversation histories include attached locations. With this information, social fingerprinting matches the digital location of data and the physical location of a user, a mismatch which, according to respondents, presents a strong indicator of fraud. Other data sources include the various types of user interactions, frequency of activity on social media, and web browsing history. This behavioral data is used to provide significant information about the user and alert vendors to the possible use of compromised devices by their customers.

Our framework also reveals that having sufficient domain skills and knowledge of fraud specialists is equally important for developing fraud detection capability. In support of this notion of a domain of expertise, Davenport and Harris [7] note that analytic capabilities are driven by “analytic people.” The project manager at Trustev has attributed the success of social fingerprinting to the teams of people using the tools effectively, who can draw meaningful information from the data. Broadly, the people who can use the tools and develop methods that are more effective in terms of accuracy and speed will be able to advance the BA capability of an organization. Our model reveals that the right people coupled with authentication data determine the data preprocessing capability. Data preprocessing involves creating tables and classification metrics to allow analytic experts to easily navigate and explore data. We find data preprocessing allows for rich data and technological infrastructure.

Next, a scalable and reliable technological infrastructure, which results from data preprocessing, is required for record integration and the facilitation of analytics. For scalability, the modular architecture of the solution enables “up and down” scaling while remaining adaptive to different environments. In terms of security and control, techniques such as IP detection, proxy piercing, and real-time mobile lookup provide a continued service. The relationship found between data

preprocessing and technological infrastructure is in line with Schroeck [87], in which the most effective big data solutions identify business requirements first and then tailor the infrastructure to support data sources and analytics for business opportunities. A scalable data infrastructure is indicative of the shift from static views to optimal physical and logical views of structured and unstructured databases.

Although the component of customer requirements has not much connection with other preconditions, it does influence other variables, especially important to set up the correct configuration for business record integration and to understand the risk baseline of an online platform. While there has been some indication of understanding customer requirements, studies are not concerned with providing an analytic solution but rather a business case for achieving customer-centric outcomes – such as customer preference, loyalty, and experience [87].

Overall, although Davenport et al. [88] indicated that having good data is a prerequisite for being analytically capable and having a skillful analytical expert is also the key for developing capability, which is related to other precondition factors, they have not empirically tested the relationships. Our study confirmed the fundamental role authentication data plays in developing organization’s business analytical capability and proved the existence of interrelationships among the key driving factors leading to business analytical capability.

As the structural relationship moves toward the section on BA capabilities, we find that record integration requires a scalable technological infrastructure and clear customer requirements. Record integration is the first of the three BA capabilities identified toward fraud detection. A number of interrelationships around record integration have been implicitly mentioned in Delen and Demirkan's [12] paper. However, their paper and other studies [11, 36] do not clarify which of those interrelationships are antecedents or consequents. It is noteworthy that Delen and Demirkan’s paper [12] suggests that BA capability must incorporate an integrated approach toward descriptive (data warehousing), predictive (text and web mining), and prescriptive (model building for optimization) techniques. We find similarities in our framework. To clarify, descriptive techniques can be viewed as having a scalable technological infrastructure and predictive and prescriptive techniques contribute to algorithm analysis and machine learning. Algorithm analysis is driven by data, record integration, and experts reinforcing the accuracy of the true identity of a user. On the other hand, machine-learning models are built to continuously measure and learn, supported by tools integrated to the platform. In the case of Trustev,

algorithm analysis determines the age of the user’s profile (from the creation date and historical updates by the user) and records and categorizes their digital activity – all of which is used to produce a social fingerprinting score. The algorithm’s pattern recognition can be further calibrated with additional techniques such as analysis of the user’s browser ID, device ID, and site velocity, thus contributing to a network effect to enhance the social fingerprinting technique for vendors of the Trustev platform. Through algorithmic analysis of data, vendors are able to make decisions within a fraction of a second. This is similar to the notion of “data in motion” [47].

While the existence of such an algorithmic code that performs identity profiling is critical, it is the mining of user data through machine-learning models that provides proactive detection, adding reliability to real-time decision making. Based on empirical data, we found that machine-learning models are designed to recognize complex patterns and evolve to understand what represents as fraudulent behavior. On the other hand, we find that algorithmic analysis is necessary for decision optimization in delivering real-time information to recommend optimal courses of action. Hence, we come to the “value” end point of our framework or what may be interpreted as the capabilities of fraud detection.

At the top of our framework, there are two end-point components or the goal of the framework – capabilities for fraud detection. As shown in Fig. 3, both identify verification and decision optimization are highly dependent on the other components identified here, and actions on any other variables will have an impact on them. In particular, algorithm analysis and machinelearning capabilities are necessary for verifying identities and optimizing decisions for potential fraud detection. An identity profile plays the role of an authenticating reference [89], providing essential information such as location and transactional data regarding the user.

In summary, the road map revealed in our framework in Fig. 3 suggests that authentication data (such as consumer transaction records, consumer social media data, and consumer geolocation data) are used in conjunction with domain expertise to enable organizations to conduct data preprocessing. Traditional data management techniques found in data preprocessing evolves into scalable and reliable technological infrastructures to support BA. Both customer requirements and a scalable technological infrastructure enable the successful integration of data records. These capabilities will enable businesses to choose the type of analytics to be embedded. In this case, we found that algorithm analysis and machine-learning are the key BA capabilities

#

developed. Subsequently, these developed BA capabilities establish decision optimization and identity verification for fraud detection.

## 7. Discussion

Our study contributes to the existing literature in a number of ways. Responding to calls to further IS research because of the emergence of multisided platforms [90, 91], we have demonstrated how the emergent uses of big data, business intelligence, and analytics herald opportunities for research and for new business value for firms. While research on BA has seen growth in recent years, scholars have recently cited the need to address a general lack of theory and empirical studies [8, 83]. Our study adds to a handful of examples that provide deeper insights into existing frameworks, which tend to be either conceptual or descriptive in nature. By adopting the case study approach and ISM, this study has empirically examined the process of analytical capability development. Our study is among one of the first to identify a structured framework that encapsulates all components in an empirical analysis of the capabilities for online fraud detection. Thus, this study not only supports the findings of prior studies in BA but also builds upon a very applicable use of analytics to detect fraud. Furthermore, our framework highlights the importance of interrelationships among components, in which antecedents exist for achieving certain components.

The combination of dynamic capabilities and MEC theory as a theoretical lens and conceptual approach, with ISM as our research methodology, has proven to be an effective way of understanding the key components of analytic fraud detection where empirical studies are scant. Thus, this study makes an important methodological contribution to the BA literature by using ISM techniques to uncover the pathway from data to BA capability. Given the attention paid in both academic and practitioner literature to the potential value BA could create for organizations, there is an increasing need to understand how organizations can create this value [42]. As a result, there are increasing calls for a full understanding of the processes from data to insight, insight to decision, and decision to value [42]. By adopting semi-structured interviews and ISM, this study has taken an initial step in understanding the path from data to insight by illustrating how BA capabilities can be developed. ISM has the ability to allow researchers to reveal both direct and indirect relationships among variables and to ascertain chains of influences as well as the most fundamental factors driving a process [56, 75]. We encourage future research to adopt this data analysis technique to reveal paths from data to value creation.

#

This study also has practical implications for technology business leaders, BA vendors, and even cybercrime specialists who wish to enhance their understanding of how to become capable of BA for fraud detection. This research has demonstrated, through a structural model, that the components of analytic fraud detection are interrelated with antecedents. In fact, it is the flow of causal influence and contextual development that has enabled us to formulate a clear pathway through the framework presented in our findings. As a result, BA vendors who wish to develop analytic fraud detection capabilities are able to do so by systematically interpreting our framework. The antecedents of our model create new opportunities for decision makers to assess their organizational resources and dynamic capabilities to determine whether they have the necessary preconditions to become capable of BA for fraud detection. Given the structural model presented, we advise practitioners to also consider adjusting their investment and strategic focus to particular components to develop the necessary capabilities or preconditions for fraud detection.

Thus, the findings of this study also provide significant implications for BA vendors to plan out their strategy against fraud. The technical flow of the data fingerprinting solution can be used to enhance current fraud detection methods used by technology organizations and service providers. The data fingerprinting process can be used as a foundation for fraud detection cases in organizations. This will give confidence to decision makers that big data analysis is a suitable and effective tool to perform fraud detection. In fact, new technologies and techniques used in the data fingerprinting solution highlight the importance of tackling fraud with methods adequate to handle data at large volumes and accurately detect fraud, in other words, providing an optimized decision on fraud with accurate identity verification. Gartner [5] has recognized that algorithm analysis and machine learning are emerging analytic capabilities among BA vendors; therefore, it may be worthwhile to investigate these new technology designs in an effort to detect and reduce the impact of fraud.

## 8. Research Limitations

This study is not without its limitations. First, a common criticism of research that adopts the case study approach is the problem of transferability or generalizability [51]. While we acknowledge that full statistical generalization is impossible, we contend that – through the application of ISM – our findings are nevertheless generalizable beyond the current context, and they are corroborated by and built on the findings of other studies in the literature. Future research could be directed toward further statistically validating our findings so that the boundary conditions of the framework developed in this article can be better defined. However,

#

and specifically with regard to identity verification and decision optimization, we have identified and discussed the development of BA capabilities using the concept of resource-based views and business dynamic capabilities to explain their function. Based on our case study of Trustev, these capabilities seek to collectively establish the profiles of service users using the location advice and sociotechnical expertise offered by the innovative social fingerprinting solution.

A second limitation of this study concerns the dependability [92] of our interview data, given the general inability of any researcher to account fully for the dynamic context within which research occurs. We were restricted in whom we could speak to, and as such, our interview data could be susceptible to bias and errors of recall. Nonetheless, from our analysis of the interview responses, we believe our study makes several practical contributions. With the increasing incidence of digital identity fraud, we illustrate how creating a robust profile identity management system will make significant inroads toward reducing fraud and its associated costs. The Trustev solution posits that the identity profile of the user is a strong indicator of whether the user is conducting fraudulent activities. As a result, the user’s identity profile is used to verify information for specific business decisions and, in this case, for the protection of transactions on websites and the minimization of any potential fraudulent activity on e-commerce platforms. We suggest that this requires the establishment of conditions for information processing capabilities to gather, interpret, synthesize, and disseminate information properly in order to cope with uncertainties (e.g., in technology, demand, and supply) and improve decision making [93, 94].

Finally, we propose that our findings support the application of sociotechnical information processing techniques to ICT tools. Kiron and Shockley [46] note that a data-oriented culture enables an organization to derive insights from data and foster analytical people. In the social fingerprinting solution discussed in this study, the people behind the technology are essential, as they are able to produce the results. The sociotechnical profile has implications for the scalability, security, reliability, and analytics of the Trustev solution.

## 9. Conclusion

While e-commerce enables significant growth, online identity fraud has emerged as one of the biggest challenges for organizations. This has led to the increased demand for the development of novel BA capabilities to leverage a growing volume of data and resources. In this study, we have uncovered the key components of BA capabilities, their interrelationships, and a pathway to being analytically capable in the context of fraud detection. In doing so, we have presented significant insights into theory and practice, particularly a systematic understanding of the applications of BA in giving information about strategies for fraud detection. We conclude by calling for future work to further assess and validate the components and interrelationships of analytic fraud detection revealed through our BA framework.

#

## Acknowledgments

The authors would like to sincerely thank Pat, Donal, and the rest of the Trustev team for their time on this project. The authors would also like to thank Dr Jan Ondrus for his kind advice and invaluable comments on the previous drafts of this paper.

## Appendix: Applying ISM

## ISM procedure

By using the practical experience and knowledge of individuals and groups, ISM provides a means by which order and direction can be imposed on the complex relationships among the elements of a system [55], and the limitations that individuals have in dealing with complex issues involving a significant number of variables at one time can be overcome [54]. ISM provides a comprehensible model of an inherently complex and usually impenetrable system [66] and provides a means of integrating diverse viewpoints. ISM has been extensively applied to evaluating IS effectiveness [95], information technology enablers and barriers for knowledge management [96, 97], and students’ motivations for using information and communication technologies in their learning contexts [56, 75].

In this study, we followed the steps described below to develop the interpretive structural model of the data analytics fraud detection capability, which was well elaborated by Guo et al. [56]:

1. Variables affecting the online fraud detection analytics system are identified by using previous literature, brainstorming, and interviews.

2. From the variables identified in the first step, a contextual relationship between each variable pair (pair-wise comparison) is established by seeking opinions from the experts and verified with interview data (discussed in Section 6).

3. An SSIM is developed for variables, which indicates pair-wise relationships among the variables of the system under consideration.

4. A reachability matrix is developed from the SSIM and the matrix is checked for transitivity. The transitivity of the contextual relation is a basic assumption made in ISM. It states that if a variable A is related to B and B is related to C, then A is necessarily related to C.

5. The reachability matrix obtained in the fourth step is partitioned into different levels.

6. Based on the relationships given above in the reachability matrix, a canonical matrix is mapped.

#

7. A diagraph is drawn from the canonical matrix and transitive links are removed.

8. The resultant diagraph is converted into an ISM, by replacing variable nodes with statements. Then the interpretive structural model is reviewed to check for conceptual inconsistency and any necessary modifications are made.

## ISM step-by-step results:

We have presented Steps 1 and 2 listed above in the paper. Now we describe the findings of the remaining ISM analysis steps.

The purpose of generating the SSIM is to prepare for the development of the interpretative structural model. The four symbols, ${ } ^ { \mathrm { s } } \mathsf { V } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { A } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { X } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { O } _ { \mathrm { 3 } } ^ { \mathrm { 3 } } ,$ ” denote the direction of the relationship between any two variables:

V: Variable i will help achieve j.

Variable j will help achieve i.

X: Variables i and j will help achieve each other.

O: Variables i and j are unrelated.

In the first instance, “Variable i will help achieve j” is a forward relationship, typically denoted as ${ } ^ { 6 6 } \nabla ^ { 5 }$ in the ISM literature. In the second instance, “Variable j will help achieve i” is the reverse, symbolized by $" \mathsf { A } . "$ For the third option, “Variables i and j will help achieve each other” is symbolized by $^ { \mathrm { * } } \mathsf { X } ,$ ” which is a two-way relationship and $" \bigcirc '$ is where “Variables i and j are unrelated.” Thus, by using the four symbols from the ISM methodology as a guide, we were able to capture the pair-wise relationships and represent them by the four symbols, ${ } ^ { \mathrm { s } } \mathsf { V } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { A } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { X } ^ { \mathrm { 3 } } , { } ^ { \mathrm { s } } \mathsf { O } _ { \mathrm { 3 } } ^ { \mathrm { 3 } } ,$ as shown in Table A1.

The SSIM shows the pair-wise relationships for all the variables of analytic fraud detection. For example, variable $\vee _ { 1 }$ to $\vee _ { 1 0 }$ is denoted by the symbol $^ { \ast } \mathsf { A } .$ This means that $\vee _ { 1 }$ has a backward relationship with $\mathsf { V } _ { 1 0 } ,$ whereby V<sub>10</sub>influences $\vee _ { 1 }$ . In the next cell, $\vee _ { 1 }$ has a forward relationship with $\vee _ { 9 }$ , whereby $\mathsf { V } _ { 1 }$ influences $\vee _ { 9 }$

Once the SSIM was developed, we converted the symbols into a binary matrix first in order to generate the reachability matrix. The importance of the reachability matrix is that it shows all the direct and indirect relationships that are possible among the variables. We first needed to convert the SSIM into a binary matrix, A, called an adjacency matrix, by substituting V, A, X, and O with 1 or 0, accordingly. The rules for substitution were as follows:

 If the (i, j) entry in the SSIM is V, then the (i, j) entry in the adjacency matrix becomes 1 and the (j, i) entry becomes 0.

 If the (i, j) entry in the SSIM is A, then the (i, j) entry in the adjacency matrix becomes 0 and the (j, i) entry becomes 1.

 If the (i, j) entry in the SSIM is X, then the (i, j) entry in the adjacency matrix becomes 1 and the (j, i) entry also becomes 1.

 If the (i, j) entry in the SSIM is O, then the (i, j) entry in the adjacency matrix becomes 0 and the (j, i) entry also becomes 0.

Then we followed the MatLab codes described by Guo et al. [56] to obtain the reachability matrix from the binary matrix. Table A2 shows our reachability matrix. The reachability matrix includes transitive links, which show the indirect relationships among the variables. In other words, it is possible to be related to a certain variable through another relationship.

Level partition was then conducted on the reachability matrix, to determine the ISM hierarchy of all variables. For example, taking into account the first row $\vee _ { 1 }$ in the reachability matrix, it shows that variable $\mathsf { V } _ { 1 }$ can reach itself and variables $\mathsf { V } _ { 5 }$ and $\vee _ { 7 } .$ . Therefore, the reachability set for $\vee _ { 1 }$ is R $( \mathsf { V } _ { 1 } ) = \{ 1 , 5 , 7 \}$ . Similarly, in the first column, all the even number variables are $0 ,$ but the odd number variables are 1, indicating that variable $\mathsf { V } _ { 1 }$ can be reached by those odd number variables. Thus, the antecedent set of variable $\vee _ { 1 } , \mathsf { A } \left( \vee _ { 1 } \right) = \{ 1 , 2 , 4 , 9 , 1 0 \}$ . Finally, the intersection set shows the common variables in both sets. In this study, we found that the intersection for $\mathsf { V } _ { 1 }$ results in R∩A = {1}. This process was repeated for all other variables to complete the first iteration of the partitioning process, as shown in Table A3.

This table includes the reachability set, antecedent set, and intersection set for all variables. According to this table, the variables of $\mathsf { V } _ { 5 }$ and $\vee _ { 7 }$ have the same reachability and intersection sets, therefore, forming the first hierarchy. Hence, $\mathsf { V } _ { 5 }$ and $\vee _ { 7 }$ would be positioned at the top of the ISM hierarchy. In successive iterations, the variables identified as “level variables” in the previous iterations were deleted and new variables were selected for successive levels using the process, until the level of each variable was found. The results for iterations 2–6 are also summarized in Table A3.

With the level partitioning complete, we then arranged the variables to form a canonical matrix, as shown in Table A4. The purpose of forming the canonical matrix is to show the variables as per their levels. As a result, the canonical matrix should reflect a “lower triangular” matrix, as most of the upper triangular entries are 0, while the lower triangular entries are 1.

## References

[1] Jamieson, R., Wee Land, L.P., Winchester, D., Stephens, G., Steel, A., Maurushat, A., and Sarre, R.: ‘Addressing identity crime in crime management information systems: Definitions, classification, and empirics’, Computer Law & Security Review, 2012, 28, (4), pp. 381-395

[2] Van Vlasselaer, V., Bravo, C., Caelen, O., Eliassi-Rad, T., Akoglu, L., Snoeck, M., and Baesens, B.: ‘APATE: A novel approach for automated credit card transaction fraud detection using network-based extensions’, Decision Support Systems, 2015, 75, pp. 38-48

[3] http://www.cybersource.com/en-ANZ/company/news/view.php?page\_id=2172, accessed 25/07/14 2014

[4] Roberts, L.D., Indermaur, D., and Spiranovic, C.: ‘Fear of cyber-identity theft and related fraudulent activity’, Psychiatry, Psychology and Law, 2013, 20, (3), pp. 315-328

[5] http://www.gartner.com/technology/reprints.do?id=1-1QLGACN&ct=140210&st=sb, accessed 15 April 2014

[6] http://dario.meximas.com/intranet/wp-content/uploads/2015/03/Magic-Quadrant-for-Business-Intelligence-and-Analytics-Platforms-2015.pdf2015

[7] Davenport, T.H., and Harris, J.G.: ‘Competing on analytics: The new science of winning’ (Harvard Business Press, 2007. 2007)

[8] Chen, H., Chiang, R.H., and Storey, V.C.: ‘Business Intelligence and Analytics: From Big Data to Big Impact’, MIS Quarterly, 2012, 36, (4), pp. 1165-1188

[9] Teece, D., and Pisano, G.: ‘The dynamic capabilities of firms: an introduction’, Industrial and Corporate Change, 1994, 3, (3), pp. 537-556

[10] Prahalad, C.K., and Hamel, G.: ‘The core competence of the corporation’ (Springer, 2006. 2006)

[11] Shanks, G., Sharma, R., Seddon, P., and Reynolds, P.: ‘The impact of strategy and maturity on business analytics and firm performance: A review and research agenda’, ACIS 2010 Proceedings, 2010

[12] Delen, D., and Demirkan, H.: ‘Data, information and analytics as services’, Decision Support Systems, 2013, 55, (1), pp. 359-363

[13] Wixom, B.H., Yen, B., and Relich, M.: ‘Maximizing Value from Business Analytics’, MIS Quarterly Executive, 2013, 12, (2)

[14] Gillon, K., Aral, S., Lin, C.-Y., Mithas, S., and Zozulia, M.: ‘Business Analytics: Radical Shift or Incremental Change?’, Communications of the Association for Information Systems, 2014, 34, (1), pp. 13

[15] vom Brocke, J., Debortoli, S., Müller, O., and Reuter, N.: ‘How in-memory technology can create business value: Insights from the Hilti case’, Communications of the Association for Information Systems, 2014, 34, (1), pp. 7

[16] Cardenas, A.A., Manadhata, P.K., and Rajan, S.P.: ‘Big Data Analytics for Security’, Security & Privacy, IEEE, 2013, 11, (6), pp. 74-76

[17] Gutman, J.: ‘A means-end chain model based on consumer categorization processes’, The Journal of Marketing, 1982, pp. 60-72

[18] Reynolds, T.J., and Olson, J.C.: ‘Understanding consumer decision making: the means-end approach to marketing and advertising strategy’ (Psychology Press, 2001. 2001)

[19] Warfield, J.N.: ‘On arranging elements of a hierarchy in graphic form’, Systems, Man and Cybernetics, IEEE Transactions on, 1973, (2), pp. 121-132

[20] http://www.acfe.com/uploadedFiles/ACFE\_Website/Content/rttn/2012-report-to-nations.pdf, accessed 19 July 2014

[21] Turner, T., Schwager, A., and Guo, Z.: ‘Verifying e-Government Market Segments’, in Editor (Ed.)^(Eds.): ‘Book Verifying e-Government Market Segments’ (Academic Conferences Limited, 2005, edn.), pp. 441

[22] Kiron, D., Shockley, R., Kruschwitz, N., Finch, G., and Haydock, M.: ‘Analytics: The widening divide’, MIT Sloan Management Review, 2011, 53, (3), pp. 1-22

[23] Constantiou, I.D., and Kallinikos, J.: ‘New games, new rules: big data and the changing context of strategy’, Journal of Information Technology, 2015, 30, (1), pp. 44-57

[24] Woerner, S., and Wixom, B.H.: ‘Big data: extending the business strategy toolbox’, Journal of Information Technology, 2015, 30, (1), pp. 60-62

[25] Hopkins, M.S., Lavalle, S., and Balboni, F.: ‘The New Intelligent Enteprise 10 Insights’, MIT Sloan Management Review, 2010, 52, (1), pp. 22

[26] Mulani, N.: ‘The Million Dollar Opportunity: Reaping Returns from Analytics’, Information Management, 2013

[27] Abbasi, A., Albrecht, C., Vance, A., and Hansen, J.: ‘Metafraud: a meta-learning framework for detecting financial fraud’, MIS Q., 2012, 36, (4), pp. 1293-1327

[28] Holsapple, C., Lee-Post, A., and Pakath, R.: ‘A unified foundation for business analytics’, Decision Support Systems, 2014, 64, pp. 130-141

[29] Bhimani, A.: ‘Exploring Big Data's Strategic Consequences’, Journal of Information Technology, 2015, 30, (1), pp. 66-69

[30] http://www.gartner.com/imagesrv/cio/pdf/cio\_agenda\_insights2013.pdf, accessed 15 April 2014

[31] Barton, D.C., David: ‘Making Advanced Analytics Work For You’, Harvard business review, 2012, 90, (10), pp. 78-83, 128

[32] Brynjolfsson, E., and McAfee, A.: ‘Winning the race with ever-smarter machines’, MIT Sloan Management Review, 2012, 53, (2), pp. 53-60

[33] Joshi, K., Chi, L., Datta, A., and Han, S.: ‘Changing the competitive landscape: Continuous innovation through IT-enabled knowledge capabilities’, Information Systems Research, 2010, 21, (3), pp. 472-495

[34] Kim, G., Shin, B., Kim, K.K., and Lee, H.G.: ‘IT Capabilities, Process-Oriented Dynamic Capabilities, and Firm Financial Performance’, Journal of the Association for Information Systems, 2011, 12, (7)

[35] Yoo, Y., Boland Jr, R.J., Lyytinen, K., and Majchrzak, A.: ‘Organizing for innovation in the digitized world’, Organization Science, 2012, 23, (5), pp. 1398-1408

[36] Cosic, R., Shanks, G., and Maynard, S.: ‘Towards a business analytics capability maturity model’, in Editor (Ed.)^(Eds.): ‘Book Towards a business analytics capability maturity model’ (ACIS, 2012, edn.), pp. 1-11

[37] Chae, B., Olson, D., and Sheu, C.: ‘The impact of supply chain analytics on operational performance: a resource-based view’, International Journal of Production Research, 2013, (ahead-ofprint), pp. 1-16

[38] Helfat, C.E., Finkelstein, S., Mitchell, W., Peteraf, M., and SINGH, H.: ‘Dynamic Capabilities: Understanding Strategic Change in Organizations.’ (Blackwell, 2007. 2007)

[39] Barney, J.B.: ‘Firm resources and sustained competitive advantage’, Journal of Management, 1991, 17, pp. 99-120.

[40] Ferrier, W.J., Smith, K.G., and Grimm, C.M.: ‘The role of competitive action in market share erosion and industry dethronement: A study of industry leaders and challengers’, Academy of management journal, 1999, 42, (4), pp. 372-388

[41] Sharma, R., and Shanks, G.: ‘The role of dynamic capabilities in creating business value from IS assets’, 2011

[42] Sharma, R., Mithas, S., and Kankanhalli, A.: ‘Transforming decision-making processes: a research agenda for understanding the impact of business analytics on organisations’, European Journal of Information Systems, 2014, 23, (4), pp. 433-441

[43] Seddon, P.B., Constantinidis, D., and Dod, H.: ‘How Does Business Analytics Contribute to Business Value?’. Proc. International Conference on Information Systems, Orlando2012 pp. Pages

[44] Cosic, R., Shanks, G., and Maynard, S.B.: ‘A business analytics capability framework’, Australasian Journal of Information Systems, 2015, 19

[45] Bose, R.: ‘Advanced analytics: opportunities and challenges’, Industrial Management & Data Systems, 2009, 109, (2), pp. 155-172

[46] Kiron, D., and Shockley, R.: ‘Creating business value with analytics’, MIT Sloan Management Review, 2011, 53, (1), pp. 56-63

[47] LaValle, S., Hopkins, M., Lesser, E., Shockley, R., and Kruschwitz, N.: ‘Analytics: The new path to value: How the smartest organizations are embedding analytics to transform insights into action’, IBM Institute for Business Value in collaboration with MIT Sloan Management review, 2010

[48] Simon, H.A.: ‘Administrative Behavior: A study of decision-making processes in administrative organization’, 1957

[49] Rokeach, M.: ‘The nature of human values’ (Free press New York, 1973. 1973)

[50] Claeys, C., Swinnen, A., and Abeele, P.V.: ‘Consumer's means-end chains for “think” and “feel” products’, International Journal of Research in Marketing, 1995, 12, (3), pp. 193-208

[51] Walsham, G.: ‘Doing Interpretive Research’, European Journal of Information Systems, 2006, 15, (1), pp. 320-330

[52] Walsham, G.: ‘Interpretive Case Studies in IS research: Nature and Method ’, European Journal of Information Systems, 1995, 4, (2), pp. 74-81

[53] Klein, H.K., and Myers, M.D.: ‘A Set of Principles for Conducting and Evaluating Interpretive Field Studies in Information Systems’, MIS Quarterly, 1999, 23, (1), pp. 67-93

[54] Warfield, J.N.: ‘Toward interpretation of complex structural models’, Systems, Man and Cybernetics, IEEE Transactions on, 1974, (5), pp. 405-417

[55] Sage, A.P.: ‘Methodology for large-scale systems’, 1977

[56] Guo, Z., Li, Y., and Stevens, K.J.: ‘Analyzing Students' Technology Use Motivations: An Interpretive Structural Modeling Approach’, Communications of the Association for Information Systems, 2012, 30

[57] Sage, A.P.: ‘Methodology for Large-Scale Systems ’ (McGraw-Hill, 1977. 1977)

[58] Waller, R.J.: ‘Application of interpretive structural modeling to priority-setting in urban systems management’, in M.Baldwin (Ed.): ‘Portraits of Complexity’ (Battelle Memorial Institute, 1975), pp. 104- 108

[59] Warfield, J.N.: ‘Societal Systems: Planning, Policy and Complexity’ (John Wiley and Sons, 1976. 1976)

[60] Anantatmua, V.: ‘The role of technology in the project manager performance model’, Project Management Journal, 2008, 39, (1), pp. 34-48

[61] Singh, M.D., and Kant, R.: ‘IT-enablement of knowledge management: The modeling of enablers’, International Journal of Internet and Enterprise Management, 2008, 5, (4), pp. 353-372

[62] Singh, R.K., and Garg, S.K.: ‘Interpretive structural modeling of factors for improving competitiveness’, International Journal of Productivity and Quality Management, 2007, 2, (4), pp. 423- 440

[63] Lunden, I.: ‘TransUnion Buys Trustev In \$44M Deal To Beef Up In E-Commerce Fraud Protection’, in Editor (Ed.)^(Eds.): ‘Book TransUnion Buys Trustev In \$44M Deal To Beef Up In E-Commerce Fraud Protection’ (2015, edn.), pp.

[64] http://www.trustev.com/about-us, accessed 17 Jan 2016

[65] Jharkharia, S., and Shankar, R.: ‘IT-enablement of supply chains: understanding the barriers’, Journal of Enterprise Information Management, 2005, 18, (1), pp. 11-27

[66] Anantatmula, V.S.: ‘The role of technology in the project manager performance model’, Project Management Journal, 2008, 39, (1), pp. 34-48

[67] Qureshi, M., Kumar, D., and Kumar, P.: ‘An integrated model to identify and classify the key criteria and their role in the assessment of 3PL services providers’, Asia Pacific Journal of Marketing and Logistics, 2008, 20, (2), pp. 227-249

[68] Faisal, M.N.: ‘Analysing the barriers to corporate social responsibility in supply chains: an interpretive structural modelling approach’, International Journal of Logistics: Research and Applications, 2010, 13, (3), pp. 179-195

[69] Cagno, E., Micheli, G., Jacinto, C., and Masi, D.: ‘An interpretive model of occupational safety performance for Small-and Medium-sized Enterprises’, International Journal of Industrial Ergonomics, 2014, 44, (1), pp. 60-74

[70] Bryman, A., and Bell, E.: ‘ Business Research Methods ’ (Oxford University Press, 2007, 2nd Edition edn. 2007)

[71] Seidman, I.: ‘Interviewing as qualitative research : a guide for researchers in education and the social sciences.’ (Teachers College Press., 2006, 3rd edn. 2006)

[72] Neuendorf, K.A.: ‘The Content Analysis Guidebook’ (Sage Publications, 2002. 2002)

[73] Corbin, J., and Strauss, A.: ‘Basics of qualitative research: Techniques and procedures for developing grounded theory’ (Sage, 2008. 2008)

[74] Jankowicz, D.: ‘The easy guide to repertory grids’ (John Wiley & Sons, 2005. 2005)

[75] Guo, Z., Lu, X., Li, Y., and Li, Y.: ‘A framework of students' reasons for using CMC media in learning contexts: A structural approach’, Journal of the American Society for Information Science and Technology, 2011, 62, (11), pp. 2182-2200

[76] Schwab, D.P.: ‘Construct validity in organizational behavior’, Research in organizational behavior, 1980, 2, (1), pp. 3-43

[77] Malone, D.W.: ‘An introduction to the application of interpretive structural modeling’, Proceedings of the IEEE, 1975, 63, (3), pp. 397-404

[78] Kannan, G., Haq, A.N., Sasikumar, P., and Arunachalam, S.: ‘Analysis and selection of green suppliers using interpretative structural modelling and analytic hierarchy process’, International Journal of Management and Decision Making, 2008, 9, (2), pp. 163-182

[79] Faisal, M.N., Banwet, D.K., and Shankar, R.: ‘Supply chain risk mitigation: modeling the enablers’, Business Process Management Journal, 2006, 12, (4), pp. 535-552

[80] Janes, F.: ‘Interpretive structural modelling: a methodology for structuring complex issues’, Transactions of the Institute of Measurement and Control, 1988, 10, (3), pp. 145-154

[81] Lyer, K.C., and Sagheer, M.: ‘Hierarchical structuring of PPP risks using interpretative structural modelling’, Journal of Construction of Engineering and Management, 2010, 136, (2), pp. 151-159

[82] Wixom, B.H., Watson, H.J., and Werner, T.: ‘Developing an Enterprise Business Intelligence Capability: The Norfolk Southern Journey’, MIS Quarterly Executive, 2011, 10, (2)

[83] Wixom, B., Ariyachandra, T., Douglas, D., Goul, M., Gupta, B., Iyer, L., Kulkarni, U., Mooney, B.J.G., Phillips-Wren, G., and Turetken, O.: ‘The Current State of Business Intelligence in Academia: The Arrival of Big Data’, Communications of the Association for Information Systems, 2014, 34, (1), pp. 1

[84] Seddon, P.B., Constantinidis, D., and Dod, H.: ‘How Does Business Analytics Contribute to Business Value?’, 2012

[85] Abbasi, A., Albrecht, C., Vance, A., and Hansen, J.: ‘Metafraud: a meta-learning framework for detecting financial fraud’, MIS Quarterly, 2012, 36, (4), pp. 1293-1327

[86] Park, S.-H., Huh, S.-Y., Oh, W., and Han, S.P.: ‘A social network-based inference model for validating customer profile data’, MIS Quarterly, 2012, 36, (4), pp. 1217-1237

[87] Schroeck, M., Shockley, R., Smart, J., Romero-Morales, D., and Tufano, P.: ‘Analytics: The realworld use of big data’, IBM Institute for Business Value—executive report, IBM Institute for Business Value, 2012

[88] Davenport, T.H., Harris, J.G., and Morison, R.: ‘Analytics at work: Smarter decisions, better results’ (Harvard Business Press, 2010. 2010)

[89] Yang, Y., Lewis, E., and Newmarch, J.: ‘Profile-based digital identity management—a better way to combat fraud’, in Editor (Ed.)^(Eds.): ‘Book Profile-based digital identity management—a better way to combat fraud’ (IEEE, 2010, edn.), pp. 260-267

[90] Agarwal, R., Gupta, A.K., and Kraut, R.: ‘Editorial Overview--The Interplay Between Digital and Social Networks’, Information Systems Research, 2008, 19, (3), pp. 243-252

[91] Tiwana, A., Konsynski, B., and Bush, A.A.: ‘Research commentary-Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics’, Information Systems Research, 2010, 21, (4), pp. 675-687

[92] Trochim, W.M.: ‘The Research Methods Knowledge Base, 2nd Revision’, in Editor (Ed.)^(Eds.): ‘Book The Research Methods Knowledge Base, 2nd Revision’ (2006, edn.), pp.

[93] Tushman, M.L., and Nadler, D.A.: ‘Information Processing as an Integrating Concept in Organizational Design’, Academy of Management Review, 1978, 3, (3), pp. 613-624

[94] Premkumar, G., Ramamurthy, K., and Saunders, C.S.: ‘Information Processing View of Organizations: An Exploratory Examination of Fit in the Context of Interorganizational Relationships’, Journal of Management Information Systems, 2005, 22, (1), pp. 257-294

[95] Kanungo, S., Duda, S., and Srinivas, Y.: ‘A structured model for evaluating information systems effectiveness’, Systems Research and Behavioral Science, 1999, 16, (6), pp. 495-518

[96] Anantatmula, V.S., and Kanungo, S.: ‘Modeling enablers for successful KM implementation’, Journal of Knowledge Management, 2010, 14, (1), pp. 100-113

[97] Bhattacharya, S., and Momaya, K.: ‘Interpretive structural modeling of growth enablers in construction companies’, Singapore Management Review, 2009, 31, (1), pp. 73-97

#

## Author biographies:

Felix Ter Chian Tan is a lecturer of Information Systems at the University of New South Wales (UNSW) Business School. His research interests include the development of electronic commerce platforms, impact of business analytics, Chinese IT management and practice, and the interaction of enterprise systems and people in organizations. His research work has been accepted in top-ranked academic journals and conferences, including Information and Management, Communications of the AIS, International Journal of Information Management, Australasian Journal of Information Systems, International Conference of Information Systems, and European Conference of Information Systems.

## E-mail: f.tan@unsw.edu.au

Zixiu Guo is a senior lecturer in the School of Information Systems, Technology and Management at the University of New South Wales, Sydney, Australia. Her papers appear in the Journal of the American Society for Information Science and Technology (JASIST), Communications of the Association for Information Systems (CAIS), Journal of Global Information Management (JGIM), IEEE Transactions on Professional Communication, the Australian Journal of Educational Technology, Computers in Human Behavior, and ICIS, ECIS, AMCIS, HICSS. She is the best paper award winner in the 2009 IEEE Transactions on Professional Communication, the winner of the AIS Award for Best Conference Paper in IS Education of year 2011, and the best paper winner 2011 AIS SIG-ED IAIM 2011 Conference. Her research interests include social media and online games, business analytics, and e-learning.

## E-mail: z.guo@unsw.edu.au

Michael Cahalane is a lecturer of Information Systems at the University of New South Wales (UNSW) Business School. His research interests include IT-enabled collaborative development, peer production, and virtual worlds. His research work has been accepted in top-ranked academic journals and conferences, including Cutter IT Journal, International Conference of Information Systems, and European Conference of Information Systems.

## E-mail: m.cahalane@unsw.edu.au

Daniel Cheng is a research student at the University of New South Wales (UNSW) Business School. His research interests include IT-enabled fraud detection and business analytics capabilities. His research work has been accepted in Pacific Asian Conference of Information systems. He is currently a security and technical consultant with a leading bank in Australia

E-mail: danielcheng@live.com.au

![](/api/attachments/6P3VUGP8/fulltext/images/7058da0718acd2d6595a2c40e49a4146482b60cae892e1421e4b110afcac7e83.jpg)  
Figure 1: Foundations of a BA capabilities framework using a means–end chain approach

![](/api/attachments/6P3VUGP8/fulltext/images/ab5ffacc3c800e6aa3b9a74821066bcd67cf4cfc7d9ff69eb081c221a5d0c5e8.jpg)  
Figure 2: Diagraph Derived from the ISM Process

![](/api/attachments/6P3VUGP8/fulltext/images/a427a144c354ba09db68a81621a4a0309145e9fc2f9f6d3d0451fed47abdf41c.jpg)  
Figure 3: A Framework for Developing BA Capabilities to Combat Online Fraud

##

Table 1: Sample Business Analytics Frameworks

<table><tr><td>No.</td><td>Description</td><td>Reference</td></tr><tr><td>1</td><td>A proposed BA success framework represented through two models. First, a process model for organizational benefits through analytic capabilities of (1) enabling technology and (2) analytical people. Second, a variance model that applies five elements to achieve business value: (1) data quality, (2) enterprise wide integrated BI platform, (3) leadership, (4) well-chosen targets, and (5) analytic leadership.</td><td>[43]</td></tr><tr><td>2</td><td>A three-level structured business analytic maturity model is the framework for evaluating an organization&#x27;s BA capabilities. BA capability characteristics of this framework include (1) BA governance, (2) BA culture, (3) BA technology, and (4) BA people. In this framework, these areas are suggested to lead to value and sustainable competitive advantage.</td><td>[36, 44]</td></tr><tr><td>3</td><td>A framework for business intelligence using advanced analytics highlights three key characteristics: (1) data integration, (2) processing capability, and (3) business intelligence delivery.</td><td>[45]</td></tr><tr><td>4</td><td>A framework that highlights three critical areas to successfully compete with analytics. These are (1) data-orientated culture, (2) information management practice, and (3) analytics expertise.</td><td>[46]</td></tr><tr><td>5</td><td>A BA framework structured as a three-step process named the process application data insight embed (PADIE) technique. This framework outlines the requirements for an organization to embed BA into its core operations.</td><td>[47]</td></tr></table>

##

Table 2: Research Methodology

<table><tr><td>Stage</td><td>Step</td><td>Technique</td><td>Output</td></tr><tr><td rowspan="2">1. Identify components required to be analytically capable in online fraud detection</td><td>1) Interview participants</td><td>Semi-structured interview</td><td>Data from 13 interviews</td></tr><tr><td>2) Analyze interview data</td><td>Content analysis</td><td>List of components of BA solution for combating identify fraud</td></tr><tr><td rowspan="2">2. Develop a framework for interrelationships in key components identified in stage 1</td><td>3) Identify direct and indirect relationships among components</td><td>ISM</td><td>Generate a framework for BA solution for combating identity fraud</td></tr><tr><td colspan="3">4) Develop a framework</td></tr></table>

##

Table 3: List of Interviewees

<table><tr><td rowspan="2">Title</td><td colspan="2">Interview Topics</td></tr><tr><td>Factors related to</td><td>Relationships</td></tr><tr><td>Chief Marketing Officer (CMO) (five interviews)</td><td>History of Trustev, marketing strategies, key elements of data fingerprinting</td><td>High-level strategy, analytics, fraud</td></tr><tr><td>Director of Fraud and Data Strategy (two interviews)</td><td>Data fingerprinting technologies, current mechanisms, logic behind systems, analytic technologies, Trustev score</td><td>Technologies, analytics systems, fraud</td></tr><tr><td>Project Manager</td><td>Technical flow of data fingerprinting, customer integration and onboarding, project methodology</td><td>Projects, process, integration</td></tr><tr><td>Chief Executive Officer</td><td>The market for Trustev, direction and vision, strategy, history</td><td>Strategy, data, fraud</td></tr><tr><td>Global Sales Officer</td><td>Attraction of the Trustev solution, how it can help the business based on website</td><td>Sales and fraud, customers</td></tr><tr><td>Fraud and data Specialist</td><td>Analysis techniques, data management, interaction between fraud and data</td><td>Fraud and data</td></tr><tr><td>Website users (two interviews)</td><td>Attraction of the company solution, how it can help the business</td><td>Nil</td></tr></table>

##

Table 4: Identifying the Components of the Trustev Analytic Fraud Detection Solution

<table><tr><td>No.</td><td>Component</td><td>Description</td><td>Sample Quotes and Evidence</td></tr><tr><td>1</td><td>Algorithm Analysis</td><td>Code that transforms data into information. The algorithm should be configurable and integrated into the business process. The algorithm works together with the machine-learning model as part of the fraud detection capability.</td><td>“Algorithm and the machine learning models basically adapt further to that logic, to that specific customer.” (Code logic) (Director of Fraud and Data)</td></tr><tr><td>2</td><td>Authentication Data</td><td>Collected data about customer activity and uploaded social content. In many organizations, the size and scope of online data have become too large or varied to manage within traditional systems, such as detailed transaction history and operational log data. As a result, much of this data are collected, but are not analyzed.</td><td>“The identification process starts with the online resources that are available. What we do is pull as many different information sources together and really do comparisons with the data from the different data sources.” (Project Manager) “Location is one of the strongest indicators of fraud as it is very hard to replicate location in terms of a fake account.” (Director of Fraud and Data Strategy)</td></tr><tr><td>3</td><td>Customer Requirements</td><td>Customer requirements refer to customers’ needs in relation to the deployment of the solution. With the growth of e-commerce and fraud, organizations face increasing demands to reduce the latency from data capture to action. Thus, the need to increase revenue while reducing fraud has led to an increasing demand for solutions.</td><td>“We’re working with customers doing over 65,000 transactions a day, so we’re in a position where [our solution] has to sit in the background and has to have absolutely no impact on any existing systems.” (Customer relationship) (Chief Executive Officer) “All customers have different use cases . . . but as a customer of Trustev, there’s a lot of options . . .” (CMO)</td></tr></table>

##

<table><tr><td>4</td><td>Data Preprocessing</td><td>Businesses must manage and categorize data into key areas that assist in the determination of fraudulent activity. For example, a key data source could be the digital and physical location of the user, which is commonly used to determine whether the transaction is fraudulent.</td><td>“Rich data structure where we can actually cross-reference the data set with industry standards information referencing specific data points.” (Data structure) (Director of Fraud and Data) “The information that we pulled from . . . we start to correlate this information. So the more information that is input from different sources, the better opportunity we&#x27;ve got, guaranteeing that it&#x27;s consistent.” (Data correlation) (Project Manager)</td></tr></table>

Table 4: Identifying the Components of the Trustev Analytic Fraud Detection Solution (continued)

<table><tr><td>No.</td><td>Component</td><td>Description</td><td>Sample Quotes and Evidence</td></tr><tr><td>5</td><td>Decision Optimization</td><td>Optimal courses of action. For fraud detection, decision optimization determines with accuracy and speed whether a transaction or user is fraudulent – this is assisted by algorithm analysis and machine-learning models.</td><td>“So we have metrics on things like fingerprints, session hijacking, proxy usage volumes, which is all live.” (Director of Fraud and Data).In Trustev, decision optimization also involves real-time prescriptive analytics, simulation, forecasting, and embedding analytics and business rules in repeatable and structured decision processes, as well as the integration of collaboration and social capabilities.</td></tr><tr><td>6</td><td>Domain</td><td>The domain skills and knowledge [36] required of</td><td>“So the key to data analytics is the people behind it, the people who look at it, the people</td></tr></table>

##

<table><tr><td></td><td>Expertise</td><td>specialists, including fraud and data management, reporting, and discovery.</td><td>who present it . . . it is and always will be that the people who design, people who build and the people who review are the key to successful analytics.” (Director of Fraud and Data)“Having the fraud expertise to look at the data, to improve our algorithms and to improve where and when we are making our decisions.” (People and expertise) (Project Manager)</td></tr><tr><td>7</td><td>Identity Verification</td><td>A combination of data sourcing through biometrics, OLAP, geospatial, and location intelligence is used to check the identity of the user. Identity verification should be automated, providing a clear output from query, reporting, and information delivery.</td><td>“A focus on verifying the identity of the customer rather than the payment/credit card within each of these categories, we collect social, behavioral, transactional and historical information, processing in real time and at incredible volumes.” (Global Sales Officer)</td></tr><tr><td>8</td><td>Machine Learning</td><td>A subspecialty of computer science concerned with the design and development of algorithms that allow computers to evolve behaviors based on empirical data. A major focus of machine-learning models is to automatically learn to recognize complex patterns and make intelligent decisions based on data.</td><td>“Our machine learning models develop new models, working closely to align with the fraud logic.” (Fraud and Data Specialist)“The ML [machine learning] model is trained basically to look at the behavioral pattern and expand that out to the entire spectrum . . . The ML model, was brought in because, when you&#x27;re looking at that level of complexity, there&#x27;s no human that can manually go through such a big volume of data.” (Director of Fraud and Data)These techniques include association rule learning, cluster analysis, classification, and regression.</td></tr></table>

##

Table 4: Identifying the Components of the Trustev Analytic Fraud Detection Solution (continued)

<table><tr><td>No.</td><td>Component</td><td>Description</td><td>Sample Quotes and Evidence</td></tr><tr><td>9</td><td>Record Integration</td><td>Supporting, creating, modifying, and embedding big data content into a customer&#x27;s business process and/or an application. These capabilities can reside outside the application (for example, reusing the analytic data infrastructure [5]), but should be easily accessible from inside the application.</td><td>“Simple to integrate with straightforward implementation, code change is minimal, integration is done in a clean interface that can be customized.” (Integration) (Project Manager)“And the function is to cross-reference that with all the other data points to bring that down to a meaningful level...” (Cross-referencing) (Director of Fraud and Data Strategy)</td></tr><tr><td>10</td><td>Technology Infrastructure</td><td>A scalable and reliable infrastructure is a prerequisite for facilitating analytics. For example, a distributed file system such as Hadoop (the Apache open-source software framework) to support the ebb and flow of data to enable users to access data when needed. A balanced configuration and deployment of servers and storage results in a more optimized infrastructure.</td><td>“Basically the data infrastructure and the quality and variety of that data allows you to do the fraud prevention . . . The architecture . . . the supporting data structure will support a fraud infrastructure.” (Infrastructure and architecture) (Director of Fraud and Data)“We are a shared platform for fraud prevention. The data we use and the information we have is actually shared on the platform for others to benefit from. It&#x27;s a network effect.” (Scalability and reliability) (Director of Fraud and Data Strategy)</td></tr></table>

Table A1: Structural Self-interaction Matrix

<table><tr><td>SSIM</td><td> $V_{10}$ </td><td> $V_9$ </td><td> $V_8$ </td><td> $V_7$ </td><td> $V_6$ </td><td> $V_5$ </td><td> $V_4$ </td><td> $V_3$ </td><td> $V_2$ </td><td> $V_1$ </td></tr><tr><td> $V_1$ </td><td>A</td><td>V</td><td>A</td><td>O</td><td>A</td><td>V</td><td>O</td><td>O</td><td>A</td><td>O</td></tr><tr><td> $V_2$ </td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>V</td><td>O</td><td>O</td><td></td></tr><tr><td> $V_3$ </td><td>A</td><td>O</td><td>O</td><td>V</td><td>O</td><td>V</td><td>V</td><td>A</td><td></td><td></td></tr><tr><td> $V_4$ </td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td>O</td><td></td><td></td><td></td></tr><tr><td> $V_5$ </td><td>V</td><td>O</td><td>A</td><td>O</td><td>O</td><td>O</td><td></td><td></td><td></td><td></td></tr><tr><td> $V_6$ </td><td>O</td><td>O</td><td>O</td><td>A</td><td>O</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $V_7$ </td><td>O</td><td>V</td><td>V</td><td>V</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $V_8$ </td><td>A</td><td>V</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $V_9$ </td><td>V</td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $V_{10}$ </td><td>O</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table A2: Reachability Matrix

<table><tr><td>RM</td><td> $V_1$ </td><td> $V_2$ </td><td> $V_3$ </td><td> $V_4$ </td><td> $V_5$ </td><td> $V_6$ </td><td> $V_7$ </td><td> $V_8$ </td><td> $V_9$ </td><td> $V_{10}$ </td></tr><tr><td> $V_1$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_2$ </td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td> $V_3$ </td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td> $V_4$ </td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td> $V_5$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_6$ </td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td> $V_7$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_8$ </td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $V_9$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $V_{10}$ </td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>1</td></tr></table>

##

Table A3: Partitioning Levels

<table><tr><td colspan="5">LEVEL 1</td></tr><tr><td>Var (Vi)</td><td>Reachability (R)</td><td>Antecedents (A)</td><td>Intersection (R∩A)</td><td>Level</td></tr><tr><td>1</td><td>1, 5,7</td><td>1, 2, 4, 9, 10</td><td>1</td><td rowspan="10"> $L_1 = \{V_5, V_7\}$ </td></tr><tr><td>2</td><td>1, 2, 4, 10</td><td>2</td><td>2</td></tr><tr><td>3</td><td>3, 9</td><td>3</td><td>3</td></tr><tr><td>4</td><td>1, 4, 8, 10</td><td>2, 4, 6</td><td>4</td></tr><tr><td>5</td><td>5</td><td>1, 5, 8, 9</td><td>5</td></tr><tr><td>6</td><td>4, 6, 9, 10</td><td>6</td><td>6</td></tr><tr><td>7</td><td>7</td><td>1, 7, 8</td><td>7</td></tr><tr><td>8</td><td>5, 7, 8,</td><td>4, 8, 9, 10</td><td>8</td></tr><tr><td>9</td><td>1, 5, 8, 9</td><td>3, 6, 9, 10</td><td>9</td></tr><tr><td>10</td><td>1, 8, 9, 10</td><td>2, 4, 6, 10</td><td>10</td></tr><tr><td colspan="5">LEVEL 2</td></tr><tr><td>1</td><td>1,</td><td>1, 2, 4, 9, 10</td><td>1</td><td rowspan="6"> $L_2 = \{V_1, V_8\}$ </td></tr><tr><td>2</td><td>1, 2, 4, 10</td><td>2</td><td>2</td></tr><tr><td>3</td><td>3, 9</td><td>3</td><td>3</td></tr><tr><td>4</td><td>1, 4, 8, 10</td><td>2, 4, 6</td><td>4</td></tr><tr><td>6</td><td>4, 6, 9, 10</td><td>6</td><td>6</td></tr><tr><td>8</td><td>8,</td><td>4, 8, 9, 10</td><td>8</td></tr></table>

##

<table><tr><td>9</td><td>1, 8, 9</td><td>3, 6, 9, 10</td><td>9</td><td rowspan="2"></td></tr><tr><td>10</td><td>1, 8, 9, 10</td><td>2, 4, 6, 10</td><td>10</td></tr><tr><td colspan="5">LEVEL 3</td></tr><tr><td>2</td><td>2, 4, 10</td><td>2</td><td>2</td><td rowspan="6"> $L_3 = \{V_9\}$ </td></tr><tr><td>3</td><td>3, 9</td><td>3</td><td>3</td></tr><tr><td>4</td><td>4, 10</td><td>2, 4, 6</td><td>4</td></tr><tr><td>6</td><td>4, 6, 9, 10</td><td>6</td><td>6</td></tr><tr><td>9</td><td>9</td><td>3, 6, 9, 10</td><td>9</td></tr><tr><td>10</td><td>9, 10</td><td>2, 4, 6, 10</td><td>10</td></tr><tr><td colspan="5">LEVEL 4</td></tr><tr><td>2</td><td>2, 4, 10</td><td>2</td><td>2</td><td rowspan="5"> $L_4 = \{V_3, V_{10}\}$ </td></tr><tr><td>3</td><td>3</td><td>3</td><td>3</td></tr><tr><td>4</td><td>4, 10</td><td>2, 4, 6</td><td>4</td></tr><tr><td>6</td><td>4, 6, 10</td><td>6</td><td>6</td></tr><tr><td>10</td><td>10</td><td>2, 4, 6, 10</td><td>10</td></tr><tr><td colspan="5">LEVEL 5</td></tr><tr><td>2</td><td>2, 4</td><td>2</td><td>2</td><td rowspan="3"> $L_5 = \{V_4\}$ </td></tr><tr><td>4</td><td>4</td><td>2, 4, 6</td><td>4</td></tr><tr><td>6</td><td>4, 6</td><td>6</td><td>6</td></tr><tr><td colspan="5">LEVEL 6</td></tr><tr><td>2</td><td>2</td><td>2</td><td>2</td><td> $L_6 = \{V_2, V_6\}$ </td></tr></table>

##

Table A4: Canonical Matrix

<table><tr><td>Var</td><td>Name</td><td> $V_5$ </td><td> $V_7$ </td><td> $V_1$ </td><td> $V_8$ </td><td> $V_9$ </td><td> $V_3$ </td><td> $V_{10}$ </td><td> $V_4$ </td><td> $V_2$ </td><td> $V_6$ </td></tr><tr><td> $V_5$ </td><td>Decision Optimization</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_7$ </td><td>Identity Verification</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_1$ </td><td>Algorithm Analysis</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_8$ </td><td>Machine Learning</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_9$ </td><td>Record Integration</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_3$ </td><td>Customer Requirements</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_{10}$ </td><td>Technology Infrastructure</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td> $V_4$ </td><td>Data Preprocessing</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td> $V_2$ </td><td>Authentication Data</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td> $V_6$ </td><td>Domain Expertise</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td></tr></table>
