---
otero_id: 508
otero_key: "2A5M9XHH"
title: "Metrics for characterizing the form of security policies"
authors: "Sanjay Goel; InduShobha N. Chengalur-Smith"
year: "2010"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2010.10.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Metrics for characterizing the form of security policies

Sanjay Goel ⇑, InduShobha N. Chengalur-Smith

Information Technology Management Department, School of Business, University at Albany, Albany, NY 12222, United States

a r t i c l e i n f o

Article history: Received 26 April 2007 Received in revised form 4 October 2008 Accepted 23 September 2010 Available online 30 October 2010

Keywords: Security policies Information quality Breadth Clarity Brevity

## a b s t r a c t

Security policies are widely used tools for the implementation of organizational security, however neither do we have metrics for measuring their effectiveness, nor are there universal standards that can serve as benchmarks. There is considerable variability in security policies based on the way they are written but we have no quantifiable evidence to determine if one kind of policy is better than another. This paper examines the literature on policies and identifies three dimensions (breadth, clarity and brevity) that could be used to characterize how well a security policy is written. These dimensions are validated through a survey of user perceptions. Informed by this empirical evidence, we propose objective metrics (along with algorithms for calculating these metrics), that can be used to assess each of these dimensions. The objective metrics are cross validated with user perceptions and found to be consistent, thus providing a standardized process to characterize the form of a security policy. Such a set of metrics would facilitate the process of evaluating the effectiveness of security policies.

\- 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

The economic impact of information security failures on organizations has been a topic of research for several years under the rubric of risk analysis (Straub and Welke, 1998; Gordon and Loeb, 2002). Research on security technologies such as cryptography, secure protocol development, software security, forensics, anti-virus and intrusion detection tools has also been very active. However, security (or lack thereof) in an organization, is a function of the interaction between people and technology. In order to manage security effectively, both social and technical factors need to be considered concurrently. Security policies integrate these elements into a cohesive plan that organizations use for enforcing security (Parker, 1998; Barman, 2002; Baskerville and Siponen, 2002; Goel et al., 2006). Security policies are at the core of the security strategy in an organization (Warman, 1992; Hinde, 2002; von Solms and von Solms, 2004a,b) but little attention has been devoted to understanding them.

The term security policy is used primarily in two different contexts: (1) computer/network security, and (2) information security management in organizations. Security policy in the context of computer/ network security is most commonly used for formally describing access control rules in a computer system/network (Sandhu and Samarati, 1994). Organizational information security policy describes the overall strategy and plan for ensuring information security in an organization. For the purpose of this paper, we use the term security policy to mean organizational information security policy.

Security policies form the glue that links security research and its implementation in practice, Organizations are diligent in the creation and enforcement of security policies; however, these policies are routinely criticized at all levels of the organization as being ineffective, unnecessary, and unenforceable. Employees find security policies an impediment to productivity (Hone and Eloff, 2002c). They think of security policies as an instrument that management uses for monitoring and control. Nevertheless, the enforcement of security policies is critical to organizational survival as it ensures the integrity and confidentiality of information, availability of services, and uninterrupted operation of business processes (Hone and Eloff, 2002a,b). In fact, recent legislation mandates the deployment of security policies in organizations.

There are two elements of security policies that can have a bearing on its effectiveness: content and form (Dhillon and Backhouse, 1996). Most organizations focus on developing the content of the security policies. Literature on the content of security policies suggests the use of industry standards and guidelines for developing security policies (Gaskell, 2000; Janczewski, 2000). Hone and Eloff (2002a,b) provide a detailed structure of security policies in the context of information security standards. Dhillon (1997) distinguishes between strategy, policy, and operating procedures. Similarly, Baskerville and Siponen (2002) define a three level structure with a high-level overall plan, information security methods at the middle, and a meta-level that determines how security policies are created, implemented and enforced. Sterne (1991) and Abrams and Bailey (1995) also consider policies to be three tiered depending on their level specificity i.e., policy objective, organizational policy, and automated policy. We draw on this literature to define security policies as follows: a high level abstract that discusses the management objectives, stakeholders, and scope of the policy, a middle tier that provides issue-specific policy incorporating rationale, guidelines, and enforcement mechanisms and at the lowest level is a system specific policy with implementation details for different systems.

Dhillon and Torkzadeh (2006) explored socio-organizational aspects of IS security using a value-focused approach. Their survey of managers identified fundamental categories of security objectives and related means objectives to achieve the fundamental objectives. They list clusters of objectives such as increase trust, provide open communication, maximize awareness, etc, as ways to achieve security, Given that a security policy is one of the tools that an organization uses to achieve security, an effective security policy must capture these objectives.

While security policy content has been investigated extensively, there is very little literature on the form of the security policy. The basic contention of this research is that two policies with the same basic content can have vastly different impacts on the organization based on their form. Since the form of the policy influences its success, it is important to understand how to articulate the form of a security policy. Currently, it is not possible to correlate the outcomes of security policy deployment to the quality of the security policy. If the means to characterize security policies were to be developed, the impact of specific changes to a policy could be measured. Metrics for a security policy will allow researchers to correlate characteristics of a security policy to its impact on improvement in information security.

The focus of this research is on the form of a security policy and the paper provides a framework for its characterization. Through a literature review, a broad set of characteristics of policies are identified, and detailed metrics to estimate these characteristics are developed. These metrics are empirically validated by capturing user perceptions about email policies through a survey. Once the metrics are validated, we create procedures and algorithms that can automate the process of assessing the efficacy of a policy through the calculation of such metrics.

The paper is organized as follows: Section 2 provides an overview of security policies and discusses policy and document metrics from related fields, Section 3 assesses user perceptions of security policies, and Section 4 presents techniques that could be used to calculate policy metrics. Section 5 discusses the results of our analyses and their implications and Section 6 presents the contributions and limitations of our work. Section 7 provides the conclusions as well as directions for future research.

## 2. Informing literature and conceptual model

Creating a security policy involves gaining an understanding of the organization’s mission and assessing its needs for information security for deployment of appropriate security controls. A group of researchers (Palmer et al., 2001) have proposed a security policy framework that delineates the best practices for creating security policies. According to them, highlevel policies define information security objectives that are technology and solution independent. Their framework advocates minimal changes to high-level policies, and recommends that organizations rely on policy interpretations for different target audiences or technologies.

Barman (Barman, 2002) defines security policies as social, political, legal, economic, and technological stipulations about security enforcement in an organization. A security policy is a document that states how an organization plans to protect its information assets from external and internal threats, operationalizes the implementation of security, and provides guidelines for employee and management conduct. Organizations typically develop policies piecemeal allowing redundancy and incoherence to creep into the document over time. Although, standard policies are available from several security organiza tions, a good security policy is not a simple ‘‘plug-and-play” component. There are guidelines for the creation of good policies; however, the metrics to characterize or measure the resultant policies are unavailable. It is thus difficult to find out if the policy is effective in managing security or what impact a policy had in improving security.

Security policy development should be an iterative process where the policy is incrementally refined and its impact on the organization measured. As a first step in this direction, we propose metrics that can be used to characterize a security policy. Once validated, these metrics can later be correlated with security metrics, allowing the organization to iteratively refine the policy based on its impact on security. Since there are no established metrics for security policies, we expanded our search to include relevant metrics from related fields such as information retrieval, information quality and monetary policies.

## 2.1. Dimensions of the form of a security policy

A security policy is a tool that translates the management of security expectations into clear, specific, and measurable objectives and mandates, such that employees act and behave in a manner consistent with the organization’s information systems security requirements. At a technological level, they provide guidelines for implementing systems and processes within the organization. At the user level, these policies provide appropriate behavior attributes for employees. Policies should specify the mechanisms through which these requirements can be met as well as the repercussions of violations or failures of policies (Whitman, 2003). From the enforcement and legal perspective, policies empower security personnel to control access, monitor, and maintain security, as well as to investigate and handle incidents. Thus a security policy must comprehensively cover all elements of the security program and provide a top-down view of security in the organization.

Research (Doherty and Fulford. 2005: Hong et al. 2006) on the impact of information security policies on security levels emphasizes the importance of the breadth of coverage of the policy. The international standard for drafting security policies (ISO, 2000) describes the minimum contents of a security policy. Policies should contain operational procedures, including: deployment of access control rules as well as the institution of application, system, network, and physical controls. They may also contain guidelines and standards for software development, configuring host systems, networks, enterprise applications, email, and databases. Thus security policies need to be comprehensive in their scope and extensive in their reach across an organization. In fact, Hong et al. (2006) conclude that the more comprehensive the content of the policy, the more effective it is. This is reinforced in a white paper published by the SANS Institute (Diver, 2007) where the comprehensiveness of a security policy is said to be essential.

As a policy document is essentially information, the field of Information Quality is also a rich source of metrics. Information quality is considered a multi-dimensional concept and it has been determined to have over one hundred attributes (Wang and Strong, 1996) which can be combined into four major categories: (1) intrinsic quality, (2) contextual quality, (3) representation, and (4) accessibility (Pipino et al., 2002). One of the basic dimensions of information quality is completeness of information, describing the extent to which data is of sufficient depth, breadth and scope for a given task (Wang and Strong, 1996). The completeness dimension belongs to the Contextual category of Information Quality (Wang and Strong, 1996), suggesting that completeness cannot be assessed in a vacuum. Thus if the framework is that of a security policy, the items that are used to assess completeness or breadth have to be tailored to that milieu. In order for the security policy to be of requisite depth, all relevant aspects of the security policy must be present

In the field of information retrieval, when asked to make judgments about the relevance of text or web documents, depth is one of the criteria that emerge as relevant (Barry, 1994, 1998; Barry and Schamber, 1998). A more recent study of health information users searching the web for information on environmental issues found that these users judged the relevance of the documents they found on the basis of how focused or restricted the document was to a particular context (Crystal and Greenberg, 2006). Thus scope was identified as one of the key criteria that users relied on when evaluating the relevance of documents. Thus across a variety of fields, the concept of breadth appears as a consistent metric that is used to assess documents.

For a security policy to be effective, it must become integrated into the processes and procedures of a business and manifest itself into the company’s culture (von Solms and von Solms, 2004a,b). Russell (2002) and Voss (2003) support this argument by emphasizing that human error is often the root cause of problems in most technological applications. People are generally considered the weakest link in an information security program and to improve staff compliance, the policies need to be precise and clear with detailed procedures to follow (von Solms and von Solms, 2004a,b). Information quality metrics from the representation category that are relevant to security policies include interpretability and ease of understanding (Wang and Strong, 1996; Pipino et al., 2002).

Research on assessing privacy policies has found that online privacy policies related to health care are mostly incomprehensible to the general population (Sheehan, 2005; Anton et al., 2007). More recent empirical research on privacy policies (Vail et al., 2008) found that users were more likely to retain the information in a policy when it was presented in succinct manner. Information characterization metrics are also available from other fields. For instance, information transparency has been proposed as a metric for monetary policies. It is defined as the degree of understanding of the policy process and related decisions, including aspects of openness and clarity (Winkler, 2000). Similar research on the impact of using structured abstracts on clarity of information is available (Hartley and Sydes, 1997; McIntosh et al., 1999). In the field of psychology, Hartley (2003) used both objective (computer-based) and subjective (reader-based) measures of readability. Hartley (2003) used word length, information content, and readability as measures of clarity and found that the structured abstracts were judged more informative, readable, and clear than the traditional abstracts.

In the finance and accounting literature, narrative disclosures in annual reports have been analyzed using text classification techniques and the Fog index was used as a measure of readability (Li, 2008). Changes in the fog index were found to be correlated with earnings prospects; specifically, annual reports of firms with lower earnings had a higher fog index. In general, this suggested an incentive for managers to alter the readability of their disclosures. Subsequently, Balakrishnan et al. (2010) investigated clarity (based on changes in the fog index), tone and risk sentiment as three meta-features used to cap ture the information in the 10 K document filings. These three meta-features were used as predictors of a company’s market performance and were found to be systematically related to performance differentials. Specifically, firms that were predicted to out-perform or under-perform had a higher fog index. Thus clarity emerges as a vital feature of information quality or document assessment across various fields of inquiry.

Two different pieces of text may have the same information content but different length. For a more verbose document (greater length) users have to filter the information from the text, while for a terser document, users may not be able to conceptualize the information clearly. In the financial policy arena the SEC has consistently recommended that public companies should avoid unnecessarily lengthy or verbose writing in their disclosure filings as the average investor may not understand complex documents, which could lead to market inefficiencies (SEC, 1998). Li (2008) found a negative relationship between firm performance and length of the annual report, suggesting that length could be used as a strategic deterrent to investors.

Additional explanation may be useful for some users to completely understand a concept, but this same explanation could lead to confusion for others. It has been suggested that (Edmunds and Morris, 2000) information overload can be reduced by eradicating duplicate information as well as by customizing information such that constituents receive only what is relevant. Several fields use complexity as a measure of the level of difficulty. For instance in organizational theory, the hrair limit is used as a complexity measure. The hrair limit (Dembski, 1998) is the point where a person is overwhelmed by concepts or change. It is defined as the number of projects that can be managed simultaneously before chaos starts to manifest. A person who reaches the hrair limit is not only unable to understand a new concept, but is also not able to continue working as effectively as before. In a meta-analysis of 18 empirical studies it was found that information diversity as well as information repetitiveness led to a reduction in decision quality (Hwang and Lin, 1999). Since users are sensitive to both overload and deficit of information, complexity should be optimized. Using these concepts, verbosity or brevity metrics can be defined.

Related research on privacy in the field of marketing found that consumers are more likely to trust privacy policies that are perceived as comprehensible, comprehensive and concise (Milne et al., 2004). Thus, three recurring themes emerge from the literature as vital characteristics of effective policies. The first is the breadth or scope of coverage of the policy (Doherty and Fulford, 2005; Hong et al., 2006; Diver, 2007). In addition, the policy must be clear, i.e. written in language that is user friendly, non-technical and easy to understand. Concurrent with that is the necessity that the policy document be short, to the point (Hone and Eloff, 2002a,b,c; Pahnila et al., 2007), and not unnecessarily verbose, otherwise the user will not read it.

We focus on these three characteristics as the dimensions of effective security policies, i.e., breadth, clarity, and brevity. Although we do not claim that these dimensions form a complete set of conditions for an effective policy we believe that they are necessary for effectiveness. Since there has been no previous research that attempts to link the form of the security policy to its effectiveness, we propose a parsimonious model that uses these three metrics to characterize the form of a security policy and believe that this collection of metrics can be used to evaluate a security policy and relate it to performance, i.e. organizational security effectiveness.

## 3. Methodology

In order to establish the linkages between the form of the security policy and its effectiveness, a longitudinal study is required. However a necessary first step in the research process is to establish detailed metrics to measure and validate each of the proposed dimensions of the form of the security policy. Thus the goal of this research is to use a multi-method process to develop and validate metrics that can be used to characterize the form of security policies.

Metrics can be assessed by the subjective perceptions of those using the information or through objective measures (Pipino et al., 2002). In this study we utilize both assessment methods for our metrics. We draw from the above mentioned literature to develop metrics to assess the breadth, clarity and brevity of security policies in various organizations. We first identify items that can be used to capture user perceptions and once these have been validated, we develop more objective metrics that can be automatically calculated for each dimension. As a final cross validation measure we observe how closely the subjective perceptions match the objective measures.

Since users are the key to successful implementation of security policies, we begin by assessing user perceptions of the three characteristics of security policies. We capture their perceptions using a subset of security policies, those pertaining to email. By restricting our investigation to email policies, we are able to reduce extraneous variability among the policies and also tailor our metrics to that particular environment. Informed by the relevant research discussed in the previous sections, we created a pool of metrics that captured the three dimensions we are focusing on.

The steps involved in assessing user perceptions follow. First we established criteria for the selection of the email policies that form the corpus for our analysis. Next, we developed and validated a survey instrument to gather user perceptions of the policy. Finally, once the data was collected, we analyzed it to determine any groupings or patterns in the data. Each of these steps is described in detail below.

## 3.1. Data source

Data for this research was email policies that were collected from public sources. Policies may differ based on the type of organization such as public, private, educational, etc. To reduce such extraneous variation, we limited our search to university email policies. Also, since regulations differ across nations, the policies considered were only from US universities. Additionally, we narrowed our focus to public and non-religious private schools to reduce any confounding differences between policies due to religious beliefs

A set of 65 email policies from institutions that met the above criteria and were publicly available on the Internet was collected. Email policies differ in the topics they cover as well as the length. They can vary in length from less than a page of text with brief instructions, to detailed documents that list every aspect of implementation and the consequence of each possible violation. Descriptive statistics for the sample of email policies revealed that the length of the policies ranged from 80 words to 4300 words.

## 3.2. Research design

A survey instrument was created to capture user perceptions about security policies. We adapted candidate items that emerged from our literature search to fit within the framework of email policies. As there are few academic papers explicitly addressing the quality of information security policies, the literature was used to gain insight rather than as a source of specific questions and item measures that could be directly used in this study.

Under the Clarity dimension we had items that captured comprehension, including ‘‘The policy is easy to understand” (Pipino et al., 2002) and ‘‘The policy presented the information clearly” (Wang and Strong, 1996). Given the inherently contextual nature of the Breadth dimension, we were unable to use previously validated items but we captured the essence of completeness and depth with items like ‘‘The policy contains all the essential elements” and ‘‘The policy specifies the ramifications of violations”. For brevity, we used items such as ‘‘The policy presented the information compactly” (Pipino et al., 2002).

The validation process consisted of three phases. The draft questionnaire was initially validated through a series of pretests, first with experienced information security researchers and then by security experts to ensure that the three dimensions we were investigating had face validity. Our experts were drawn from information security units in various organizations and their titles ranged from State Information Security Officer to security professionals who had direct responsibility for implementing security in their organizations. Pre-testers were asked to critically appraise the questionnaire focusing on issues of content, clarity, question wording, and validity. We then held intensive one on one interviews with the experts and recorded their open ended responses to the draft questionnaire. They provided input into the wording (more specific or generic) of the items as well as the appropriateness of some of the items. Based on their feedback and using a recursive editing process, we deleted or modified some items and included some new ones. Thus rather than waiting for a consensus, we used a sequential process of modifying the questionnaire so that changes made, based on one expert’s opinions, could be tested and verified by the next expert.

For the second phase of our validity testing, a representative policy from the data set was selected to pilot test the resulting survey instrument. Our ten pilot test participants included a mix of IT staff, faculty, and graduate students. They reviewed the questionnaire with us, in the context of the sample email policy and suggested adding and deleting items or re-phrasing questions.

Based on their feedback, the questionnaire was further modified by revising the wording on some items to reduce ambi guity and deleting items that were clearly redundant, resulting in a parsimonious list of questions that could be completed in about 15 min (Sheehan, 2001). Through these two phases we established content validity for our questionnaire (Straub et al., 2004). The final instrument contained 22 items on a 7 point Likert scale with anchors at Strongly Agree and Strongly Disagree as shown in Table 1. In order to reduce method bias, we did not present the items categorized according to the factor we believed they represented (King et al., 2007). In addition, some of the items were negatively phrased in order to reduce mechanistic responses.

## 3.3. Data collection and analysis

Since the task involved assessing university email policies, our target audience was graduate students from a public university. Although their education level may exceed that of the average worker, in other ways, our participants reflected the demographics of the typical workforce. For instance, the proportion of females was approximately 41%. In general, using students is advantageous because they have better comprehension of survey questions and instructions, and being a more homogenous population, the within-cell variance in the sample is reduced (Malaviya et al., 2001). Also, given that the artifact being studied is email policies, and students' familiarity with email, we believe that they make ideal subiects for such an experiment.

We designed our study so that each respondent assessed multiple email policies and each email policy was assessed by multiple people. This ensured that the results were not artifacts of any particular policy or person. Given the extreme variation in lengths in our original set of 65 policies, we used outlier analysis to remove some policies from consideration, based on their lengths. We further culled the set to create a survey corpus of 27 relatively homogenous policies, ranging in length from about 200 to 1000 words. We randomly distributed the 27 email policies to 68 graduate students, such that each student read about 5 policies. This ensured that each participant was exposed to, and could remark upon, a relatively broad set of policies.

The respondents first read the policy and then recorded their impressions of the policy using the Likert scaled items listed in Table 1. Each student took about 15–20 min to read and comment on each policy. We allocated the policies to the students in a random pattern designed to rotate the order in which each policy was read and judged. This reduced the bias associated with assessing the (n + 1)th policy after having assessed the previous n policies. Also by informing respondents about the anonymity and confidentiality of their responses, we were able to diminish any social desirability effects (King et al., 2007).

Table 1  
Items that measure perceptions of the policy.

<table><tr><td>#</td><td>Items</td></tr><tr><td>1</td><td>The policy is long</td></tr><tr><td>2</td><td>The policy is repetitive</td></tr><tr><td>3</td><td>The policy presented the information compactly</td></tr><tr><td>4</td><td>The policy presented the information clearly</td></tr><tr><td>5</td><td>The policy is verbose/wordy</td></tr><tr><td>6</td><td>The policy is terse/succinct</td></tr><tr><td>7</td><td>The policy is easy to read</td></tr><tr><td>8</td><td>The policy is easy to understand</td></tr><tr><td>9</td><td>The policy uses a lot of acronyms</td></tr><tr><td>10</td><td>The policy has a broad scope</td></tr><tr><td>11</td><td>The policy contains all the elements essential to security</td></tr><tr><td>12</td><td>The policy provides in-depth coverage of topics</td></tr><tr><td>13</td><td>The policy is clearly structured</td></tr><tr><td>14</td><td>The policy is generic</td></tr><tr><td>15</td><td>The policy is tailored to the different functional areas</td></tr><tr><td>16</td><td>The policy uses security specific terminology</td></tr><tr><td>17</td><td>The policy can be understood without reference materials</td></tr><tr><td>18</td><td>Technical expertise is required to decipher the policy</td></tr><tr><td>19</td><td>The policy is written using common English words and phrases</td></tr><tr><td>20</td><td>The policy specifies the legal ramifications of violations</td></tr><tr><td>21</td><td>The policy protects the organization from the legal consequences of violations</td></tr><tr><td>22</td><td>Different elements of the policy are clearly distinct</td></tr></table>

The responses were run through an exploratory factor analysis to identify any grouping patterns among the items. We used maximum likelihood extraction with oblimin rotation (Costello and Osborne, 2005). We used Kaiser’s criterion (a cut-off of 1 for the eigenvalues) and the scree plot, in combination, to determine the number of factors. Three factors emerged that together accounted for about 59% of the variance explained. The KMO measure of sampling adequacy was 0.844 and Bartlett’s test of sphericity was highly significant, indicating the suitability of the data for factor analysis and adequate correlation among the items, respectively.

The survey results were used to establish the validity and reliability of our instrument. In this third and last phase of validity testing, we wished to establish construct validity for our factors. In order to do this, we evaluated convergent and discriminant validity. To demonstrate convergent validity we considered both item and composite reliabilities. We determined item reliability and discriminant validity by examining construct item loadings. In general, loadings at or above 0.50 demonstrate adequate item reliability (Hair et al., 2006). Discriminant validity is present when items load higher on their own construct rather than other constructs. Cronbach alphas provide evidence of composite reliability and values above 0.700 demonstrate adequate reliability (Nunnally, 1978).

Using 0.5 as a cut-off for loadings led us to discard five items. Five items that had high cross loadings were also discarded. The loadings for the remaining 12 items along with the reliabilities for the three factors are displayed in Table 2. In every case, the item loadings exceeded 0.6 and their loadings on their own constructs were higher than the loadings on any other construct. In addition, the Cronbach’s alphas are 0.7 or above. All the statistics demonstrate adequate convergent and discriminant validity, and hence we have established construct validity for the three factors.

The first factor captures the Clarity of the policy, whether it was unambiguous and easy to understand. The second factor Breadth represents the scope, range, or coverage of the policy and the third factor reflects the verbosity or brevity of the policy. The three factors reflect the fact that the policy needs to cover the minimum requirements and do so with the shortest possible length and still be readable. Our measurement model is reflected in Figs. 1 and 2.

## 4. Calculating policy metrics

The input from policy users attests to the significance of the three dimensions. It is not however feasible to conduct a new survey to measure the characteristics of a policy each time. In addition, user perceptions are subjective and can vary significantly. It is imperative to define objective metrics that can be computed based on the perceptions of the user. We use the dimensions that emerged above as the foundation for developing computable metrics for security policies, Our goal is to create a set of quantifiable and objective metrics that are comparable across policies. We develop some potential metrics for each of the three dimensions, recognizing that this is only a subset of metrics that could be used to characterize how well a policy is written.

For our computed metrics, we draw heavily from the field of content analysis. Content analysis is a research tool used to determine the presence of certain words or concepts within texts. Content analysis can be applied to examine writing or recorded communication across diverse domains including, marketing and media studies (Kassarjian, 1977; Jin and Cameron, 2003) literature and rhetoric (Horton, 1986; Herzog, 1973), ethnography and cultural studies (Altheide, 1987), gender and age issues (Craig, 1992), sociology and political science (Riffe et al., 1998; Webb et al., 1966), and psychology and cognitive science (Laffal, 1987). Content analysis has been used extensively by sociologists to investigate content of the mass media in order to discover how particular issues are presented.

Table 2 Factor analysis results.

<table><tr><td>Factors and items</td><td>Loadings (reliabilities)</td></tr><tr><td>Factor 1: Clarity (5 items)</td><td>(0.878)</td></tr><tr><td>C1: The policy is easy to understand</td><td>0.908</td></tr><tr><td>C2: The policy is easy to read</td><td>0.851</td></tr><tr><td>C3: The policy presented the information clearly</td><td>0.750</td></tr><tr><td>C4: The policy is written using common English words and phrases</td><td>0.701</td></tr><tr><td>C5: The policy can be understood without reference materials</td><td>0.624</td></tr><tr><td>Factor 2: Breadth (3 items)</td><td>(0.759)</td></tr><tr><td>R1: The policy protects the organization from the legal consequences of violations</td><td>0.784</td></tr><tr><td>R2:The policy specifies the legal ramifications of violations</td><td>0.735</td></tr><tr><td>R3:The policy contains all the elements essential to security</td><td>0.648</td></tr><tr><td>Factor 3: Brevity (4 items)</td><td>(0.849)</td></tr><tr><td>B1: The policy is long</td><td>0.840</td></tr><tr><td>B2: The policy presented the information compactlya</td><td>0.823</td></tr><tr><td>B3: The policy is verbose/wordy</td><td>0.727</td></tr><tr><td>B4: The policy is repetitive</td><td>0.677</td></tr></table>

<sup>a</sup> This item was reverse coded.

![](/api/attachments/2A5M9XHH/fulltext/images/77cd641e24ea58b5972a8cdd1df478e54f278386aef3cad8731b3a324987f99c.jpg)  
Fig. 1. Conceptual model.

The basic premise of content analysis is that words and phrases mentioned most often are those reflecting important concerns in every communication (Krippendorff, 2004). The underlying assumption of content analysis is that text can be coded using semantic labels and the frequencies of occurrence of labels provide us with quantifiable data about issues being raised. Content analysis involves determining the concepts of labels or concepts a priori and then determining the presence of certain words, concepts, themes, phrases, characters, or sentences within texts and to quantify this presence in an objective manner. To conduct a content analysis on a piece of text, the text is coded, or broken down, into categories on a variety of levels such as word, word sense, phrase, sentence, or theme. Content analysis relies extensively on word frequencies to determine the themes (focus areas) and relative frequencies of the themes (or emphasis on focus areas).

Security policies are communications from management to its employees, to ensure compliance with security guidelines, making content analysis applicable. There has been extensive work on the analysis of communication (Berelson, 1971; Budge & Hans-Dieter. 2001). There has been some work on analvzing policies using content analysis, Content analysis has been used to compare school bullying policies to identify the limitations and lack of coverage in specific areas (Smith et al., 2008). Hite et al. (1988) perform content analysis of ethics policies in organization determine the frequency and types of topics which are covered in the ethics policy statements of large US corporations. Their results indicate that the topics covered most frequently were: misuse of funds/improper accounting, conflicts of interest, political contributions, and confidential information. Hessink et al. (2007) analyze the contents of whistle-blowing policies, and parts of corporate codes of conduct and codes of ethics, describing such policies of 56 leading European companies. Bodle (1992) has done a content analysis of student and community news papers to verify if stories were readable, interesting, and thorough. The metrics of clarity and breadth correspond with the first and third attribute that this study defines. White et al. (2004) performed content analysis on patient email to physicians. They coded each message based on tone in which the categories included formality, conciseness, and courteousness. While they used manual coding, we define metrics that facilitate automated computation of brevity (or verbosity).

![](/api/attachments/2A5M9XHH/fulltext/images/1b3bde2b39a1057d9bb043398e5f71919f8bb9a05f065311856989946e236309.jpg)  
Fig. 2. Measurement model.

## 4.1. Clarity

Clarity has connotations of ease of reading and ease of understanding of text. Rudolf Flesch developed a method for determining readability and interest levels through content analysis (Flesch, 1949). Flesch measured the number of words in each sentence and the number of syllables per 100 words to define a quantitative score for readability. A number of different metrics have been defined to measure the readability of a text. The Flesch Reading Ease Score (FRES) and Flesch-Kincaid Grade Level (FGL) score methods are most widely used to quantify the readability of text documents. The FRES and FGL methods provide a standardized and statistical metric to objectively analyze the text contained in documents. Both these readability metrics are based on formulae that consider the average number of syllables per word and words per sentence to determine the overall readability of a document (see equations).

$$
\mathrm{FGL} = (0. 3 9 * \mathrm{ASL}) + (1 1. 8 * \mathrm{ASW}) - 1 5. 5 9
$$

$$
\mathrm{FRES} = 2 0 6. 8 4 - (1. 0 1 5 * \mathrm{ASL}) - (8 4. 6 * \mathrm{ASW})\tag{1}
$$

ð2Þ

where

$$
\begin{array}{l} \text { ASL } = (\# \text { of   words }) / (\text { the   \#   of   sentences }) \\ \text { ASW } = (\# \text { of   syllables }) / (\# \text { of   words }). \end{array}
$$

The Flesch metrics give an approximate measure of a text’s difficulty. The FRES is based on a 100 point scale; the higher the score, the easier it is to comprehend. The average sentence length for a score of 0 (a very difficult document to read) is 37 words and for a score of 100 is 12 words or less (Anton et al., 2007). The FRES has been used to evaluate legal documents and regulate the complexity of insurance policies (Jensen and Potts, 2004) in several states. The FGL is a number that estimates the number of years of schooling required for an individual to be able to read and understand a document; for example, a score of 9.0 means that a ninth grader would be able to understand a document. An additional metric that is used less often is the Gunning fog index which is defined as the number of years of formal education that a reader requires to be able to understand the text on first reading. It is defined as follows

$$
\text { Fog } = 0. 4 ((\# \text {   of   words   } / \# \text {   of   sentences }) + 1 0 0 \times (\# \text {   of   complex   words   } / \# \text {   of   words })\tag{3}
$$

Three University email policies are included in the Appendix and used to illustrate these computed metrics. The values of FRES, FGL, and Fog for the email policy in Appendix A are 14.25, 17.43, and 20.17 respectively. For this policy, FRES is relatively low, indicating it is difficult to read, and the FGL and Fog index indicate that reading the policy requires education beyond a college degree. Thus all the measures suggest that the policy is relatively difficult to read. The minimum, average, and maximum levels in our original data set of 65 sample email policies are {6.6, 8.72, 12.12} for FRES, {23.37, 14.55, 18.01} for FGL, and {54.19, 21.83, 26.40} for the Fog indices. Given that email is pervasive through the entire organization; such difficult readability levels can have an impact on its implementation, making it an important metric. We show two contrasting policies in Appendices B and C to show the difference in the readability. The values of FRES, FGL, and Fog for the email policy in Appendix B are 54.19, 9.81, and 12.17 respectively and the values of FRES, FGL, and Fog for the email policy in Appendix C are 2.92, 17.08, and 21.98 respectively. Obviously the Policy in Appendix B is much easier to read with simpler words and shorter sentences compared to the Policy in Appendix C.

## 4.2. Breadth

Breadth is a measure of how comprehensive the policy is. Bodle (1992) has defined a thoroughness measure in content analysis of news paper articles by categorizing sentences in news items as facts, details, and reactions with the number of detail statements being a measure of thoroughness. Since there are no widely accepted metrics for breadth, we devise our own metric in the context of security policies.

We define thoroughness in security policies by measuring the number of different elements of security contained in the policy. This can be estimated by identifying the security-specific terms used in the document and estimating the breadth of the security terms. To compute this metric, a master glossary of security terms was created. This master glossary comprises twelve security glossaries selected from reliable sources on the Internet, including Microsoft, government agencies such as National Institute of Standards and Technology (NIST), and security research organizations such as SANS. Glossary size varied between 22 and 496 terms with a mean of 167 and a standard deviation of 132.

The master glossary was implemented in a relational database. Terms from all the glossaries were added to the database which linked the terms to their definitions and the source. Where applicable, a list of acronyms and their definitions were also added to the database. Each term in the database was also linked to its synonym(s). The database thus created contained 1515 terms, 2006 definitions, 26 synonyms, and 140 acronyms. The terms were categorized into distinct information security domains. Twenty categories were created, e.g., software development, network security, and security policies. A breadth metric is computed by identifying technical terms in the security policies, where we define a technical term as one that occurs in the security database but not in the dictionary (e.g. denial-of-service, domain hijacking, darknet and honeypot). The policy document is first scrubbed by removing all stop<sup>1</sup> words and a breadth metric is calculated as follows:

n = total number of (non-stop) words in the document

n = number of technical terms in the document.

$$
\text { Breadth } = 1 0 0 * n _ {t} / n\tag{4}
$$

This metric is bounded by zero and 100 and a value closer to 100 suggests greater breadth. The value of breadth for the sample email security policy in Appendix A is 6.49 which is close to the average value of 6.13 for the 65 policies that were evaluated. The maximum value of the metric was 13.71 and the minimum value was 2.88. The policies in Appendices B and C have a breadth value of 4.47 and 7.31 respectively which suggests the use of more technical terms in the policy in Appendix C. This difference in their metrics also reflects the fact that the policy in Appendix B is limited in terms of its scope (note that it is restricted to a discussion of email quota), whereas the policy in Appendix C covers a much wider spectrum of issues related to email.

## 4.3. Brevity

For a text document, it is generally believed that wordiness typically adds nothing but confusion. A well written docu: ment would eliminate redundancy, wordiness, jargon, evasiveness and circumlocution. In the context of security policies we measure the repetitiveness in the document. We compute linguistics characteristics of the document by removing stop words and calculating the total number of unique words. Based on this, a brevity metric is defined below:

n: total number of (non-stop) words in the document

$n _ { r } \mathrm { : }$ number of unique words

$$
\text { Brevity } = 1 0 0 * n _ {r} / n\tag{5}
$$

This metric is again bounded by zero and 100 and a value closer to 100 suggests greater brevity. The value of brevity for the sample email policy in Appendix A is 53.14 which is close to the average value of 51.98 across our sample of 65 policies. The maximum value of brevity was 73.87 and the minimum value was 21.27. The policies in Appendices B and C have brevity values of 42.35 and 59.73 respectively which suggest that the policy in Appendix C is much briefer. It should be noted that the policy in Appendix C is longer than that in Appendix B, yet it is able to cover a wider spectrum (hence the better score on brevity).

Kolmogoroy Complexity, which is a measure of the true information content of a text can also be construed as a brevity metric since it is defined as the shortest computer program capable of generating a given string (Li and Vitanyi, 1997). Even though it is non-computable, accurate estimates of Kolmogorov complexity have been developed using compression algorithms which work by stripping redundant information from data (Evans and Bush, 2002). Several algorithms such as entropy, Lempel Ziv (Ziv and Lempel, 1978), and zip-based compression (Evans and Bush, 2002; Goel and Bush, 2004) are available. However, Kolmogorov complexity is based on syntax and does not consider the semantics of the writing making it irrelevant for policy evaluation. Consequently, it was dropped from consideration.

## 4.4. Validation

In order to cross validate the survey findings with the computed metrics, correlations among all the metrics were calcu lated as shown in Table 3. Note that there is a significant negative correlation between clarity and brevity, illustrating the difficulty of striking the right balance between providing enough explanation and being verbose.

Comprehension or clarity is the most widely researched factor of the three form dimensions, and we were able to benchmark it against three established metrics (FRES, FGL and Fog). We found a significant, positive correlation of the Clarity factor F(clarity), extracted though the survey, with FRES and a significant negative correlation with the Fog index and FGL. (This is consistent as the latter two actually measure difficulty in comprehension.). Similarly, the Breadth factor, F(breadth) from the survey, is significantly positively related to the calculated metric of Breadth, which measures the number of technical words in the document (see Eq. (4)). Finally, the Brevity factor, F(brevity) from the survey, is significantly negatively related to the brevity metric. A close perusal of the items constituting the Brevity factor reveals that they actually measure verbosity; hence the negative association with the metric calculated using Eq. (5). Thus the human perceptions of the form of the policy closely track our proposed calculated metrics.

## 5. Contributions and limitations

There has been active research on effectiveness of public policies in context of several disciplines including social behavior (Howlett and Ramesh, 2003; Sanderson, 2000), technology transfer (Bozeman, 2000), finance (Galí and Gertler, 2007) economics (Besley and Case, 2003; Schmidt, 1999), and environment (Hammond et al., 1995). Work has been done on both formative evaluation which assesses policy implementation and identifies potential improvements as well as summative evaluation which evaluates if the policy has achieved its intended goals. Information security policy has become a key instrument for managing security in organizations however its impact on improving security has not been evaluated empirically (Kotulic and Clark, 2004). Evaluation is required to determine both how well the policy objectives are achieved and to identify the suitable changes to the policy to improve its success in meeting organizational objectives. Such an endeavor would involve identifying organizational goals, measuring performance outcomes, and linking the outcomes to policy characteristics. Research exists on both identification of organizational goals and defining metrics corresponding to the goals (Singhal and Ou, 2009; Frigault et al., 2008; Jaquith, 2007); however, currently we do not have metrics for characterization of security policies which are important to identify the impact of policy changes/differences on the policy outcomes.

Our aim in characterizing security policies was to facilitate the investigation of this link between the form of a security policy and its effectiveness. This study has taken the first step towards that objective by developing metrics to characterize the form of a security policy. In order to uncover the appropriate metrics, we utilized a two-pronged approach. We first assessed user perceptions through a survey and using factor analysis, we identified three dimensions that were validated statistically. Second, we devised computational algorithms based on prior literature to automatically compute them. This work on the characterization of security policies in terms of its form and deriving computable metrics for the characteristics is foundational and will open up research in summative evaluation of information security policies. Once security policies can be characterized with a certain degree of confidence, it can be looped back to the success of the policies. This will allow us to determine the impact of policy changes on organizational outcomes within the confines of an organizational context. Certain security policies may be more effective than others, based on the specific social, cultural, and technological environment in the organization. This research will facilitate further research on understanding such linkages between the policy form, outcomes, and organizational context. Organizational outcomes to consider in context of security policy enactment include employee morale and productivity, and security posture of the organization, and the organizational factors to consider are demographics, education, type of business, and management style. Given that this was one of the first studies of its kind, its scope was necessarily limited. However, before we can make any general conclusions, we need to further test the robustness of our results. A follow-up study needs to investigate a larger pool of policies that encompass a wider range of complexity to truly test the efficacy of the proposed metrics. The scope of the current policies is limited to email policies and should also be expanded to other types of information security policies. In addition, the survey constituency could use a more diverse group of respondents. Future research could also study the phases of the security policy enactment, i.e., creation, enforcement, audit and revision.

Table 3  
Cross validation of empirically derived metrics with computed metrics.

<table><tr><td></td><td>F(clarity)</td><td>F(breadth)</td><td>F(brevity)</td><td>Brevity</td><td>FRES</td><td>Fog</td><td>FGL</td><td>Breadth</td></tr><tr><td>F(clarity)</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F(breadth)</td><td>-0.316</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>F(brevity)</td><td>-0.641**</td><td>0.375</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Brevity</td><td>0.382*</td><td>-0.187</td><td>-0.771**</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>FRES</td><td>0.495**</td><td>-0.334</td><td>-0.119</td><td>-0.038</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Fog</td><td>-0.523**</td><td>0.285</td><td>0.181</td><td>0.042</td><td>-0.963**</td><td>1</td><td></td><td></td></tr><tr><td>FGL</td><td>-0.490**</td><td>0.219</td><td>0.171</td><td>0.063</td><td>-0.939**</td><td>0.991**</td><td>1</td><td></td></tr><tr><td>Breadth</td><td>-0.179</td><td>0.613**</td><td>0.216</td><td>-0.057</td><td>-0.355</td><td>0.315</td><td>0.304</td><td>1</td></tr></table>

<sup>\*</sup> Significant at the 0.05 level.  
<sup>\*\*</sup> Significant at the 0.01 level.

## 6. Conclusions and future research

Quantifiable metrics for security policies can form the basis on which policy enforcement success can be correlated with the characteristics of the policy. Our aim in characterizing security policies was to enable the investigation of any link between the form of a security policy and its effectiveness. This study has taken the first step towards that objective by revealing three distinct dimensions in the context of email policies. These factors were verified using user perceptions and statistically validated. We also identified several techniques to compute the three dimensions that characterize security policies. Some of these metrics are based on text analysis of security policies while others on readability of documents. These measures map to the dimensions discussed above and would lead to future work on investigating the efficacy of policies. The metrics could be used to ascertain the impact of security policies on organizational outcomes in subsequent research. We have defined metrics for brevity and breadth; however we have used the standardized readability indices as measures of clarity. The readability indices do not consider the difficulty of absorbing the actual content. For instance one policy may be written logically while the other policy may be disorganized so that the reader understands the first policy better. In order to incorporate such capabilities, in future, we may resort to the use of linguistic analysis to compute document characteristics based on semantics

## Acknowledgements

The authors thank Damira Pon and Rachel Niebour for editorial support and collection of security policies from online sources. Thanks also to our associate editor Dr. Gurpreet Dhillon and the anonymous reviewers for their insightful comments that have helped us improve this paper.

## Appendix A. Virginia Commonwealth University, Student Email Policy

## POLICY STATEMENT AND PURPOSE

Electronic mail or ‘‘email” is considered an official method for communication at VCU because it delivers information in a convenient, timely, cost effective, and environmentally aware manner. This policy ensures that all students have access to this important form of communication. It ensures students can be reached through a standardized channel by faculty and other staff of the University as needed, Mail sent to the VCU email address may include notification of University-related actions, including disciplinary action.

WHO SHOULD READ THIS POLICY

All members of the VCU community should read this policy.

RELATED DOCUMENTS

VCUnet Security Policy.

VCU Computer and Network Resources Use Policy.

Family Educational Rights and Privacy Act of 1974 (FERPA).

CONTACTS

Questions or comments about this policy should be directed to the Assistant Vice President for Technology Services. Changes to this policy will be authorized by the approval of the University Information Technology Advisory Committee (UI TAC) with concurrence by the Vice Presidents.

## DEFINITIONS

Forwarded Email: Email sent to an address that is automatically sent via computer code to another email account.

Nickname Email Account: An email account, issued by an internet service provider or web-based email service, in which the name of the account is a nickname or is otherwise unrelated to the name of the account owner.

Official Email Account: An email account, issued by the University, which is based on a person’s first name, middle initial, and last name, and ends in the domain name. “ycu.edu".

## PROCEDURES

University Use of Email

Email is an official method for communication at VCU. Students are responsible for the consequences of not reading, in a timely fashion, University-related communications sent to their official VCU student email account.

Application for Student Email Accounts

All students are required to obtain an official VCU student email account within one week of the beginning of the first semester of enrollment. Students-both currently enrolled and incoming-may obtain their account over the Web at anytime by going to the ‘‘Academic” section of the ‘‘Getting a Computer Account” Web page. A student email account created on the VCU Web is the official email address to which the University will send email communications. This official address will be recorded in the University’s electronic directories and records for that student. The official address will end in the domain name ‘‘vcu.edu”. email addresses that end in ‘‘vcu.org” are not official email addresses; students are required to have an email address that ends in ‘‘vcu.edu”.

Expectations Regarding Student Use of Email

Students are expected to check their official VCU email on a frequent and consistent basis in order to remain informed of University-related communications. The University recommends checking email daily. VCU offices cannot validate that a communication coming by email is from a student unless it comes from a valid VCU address. If students make queries to VCU administrative offices or faculty from ‘‘nickname” email accounts (Hotmail, AOL, etc.), they may be asked to resubmit their query using an official VCU account.

## Faculty Expectations and Educational Uses of Email

Faculty members may require email for course content delivery, class discussion, and instructor conferencing and may specify course-related email policies in their syllabi. Faculty may also require students to confirm their subscription to University-provided mailing lists.

## Appropriate Use of Student Email

All use of email will be consistent with other University policies and local, state, and federal law, including the VCU Computer and Network Resources Use Policy, VCUnet Security Policy, and the Family Educational Rights and Privacy Act of 1974 (FERPA).

## Forwarding Email

Students will not be permitted to set automatic forwarding on their VCU email to another non-university email account. Exceptions to this requirement may be authorized for valid academic purposes and when requested by the dean of the student’s school and approved by the Assistant Vice President for Technology Services. However, having email lost because of forwarding does not absolve a student from the responsibilities associated with communication sent to his or her officia email address. The University is not responsible for the handling of email by outside vendors or systems.

## Privacy of Email

Virginia Commonwealth University uses various methods to protect the security of its computer and network resources and of its users’ accounts. Users should be aware that any electronic communications and data utilizing University-owned computer and network resources potentially may be disclosed under the provisions of the Virginia Freedom of Information Act and other University, state and federal laws and regulations or for appropriate university business needs.

Initial Policy Approved May 20, 2002 by the VCU Vice Presidents.

Policy Last Revised March 24, 2005 by UITAC.

## Appendix B. Culverhouse College of Commerce & Business Administration, Email Policy

Notice: The Technology Group does not back up student data. It is your responsibility to back up both Email and data on network storage to removable media.

The Technology Group enforces Mailbox size limits (quotas) on all C&BA Email accounts. We believe that this strategy improves the reliability of our email servers by keeping the system databases down to a reasonable size. To limit confusion amongst end users regarding how the quota works and what some of the automatically generated messages really mean we provide this overview:

## QUOTA LEVELS

The quota levels are the following:

Receive Warning at 90 MB (92,160 KB).

Unable to send mail at 100 MB (102,400 KB).

Unable to send or receive email at 200 MB (204,800 KB).

PROCEDURES

At this time, we are imposing quotas on one mailbox at a time. We are doing this so that we can spend time with each end user and Help them to determine the best strategy for their email usage. Unfortunately, the warning message that is automatically generated is somewhat confusing. Here is an example:

Your mailbox has exceeded one or more size limits set by your administrator.

Your mailbox size is 92,160 KB.

Mailbox size limits:

\* You will receive a warning when your mailbox reaches 102,400 KB.

\* You cannot send mail when your mailbox reaches 102,400 KB. You may not be able to send or receive new mail until you reduce your mailbox size.

\* To make more space available, delete any items that you are no longer using or move them to your personal folder file (.pst).

\* Items in all of your mailbox folders including the Deleted Items and Sent Items folders count against your size limit.

\* You must empty the Deleted Items folder after deleting items or the space will not be freed.

\* See client Help for more information.

Please note that there is no provision within the Exchange Mail Server to allow us to modify these messages.

Basically, the message is just warning you that you have reached a certain limit set in the email system. It states that the email box has reached 92,160 KB which roughly equals 90 MB. It’s important to note that you may not receive this message before you actually exceed your quota. That’s because a single message with a large attachment could cause you to greatly exceed your limit.

If you are under your 100 MB limit and receive the warning message above and clean out items in your mailbox, you will not experience any further problems.

If you exceed your 100 MB limit, you will not be able to send any more mail out until you clean out some mail. Incoming mail (up to another 100 MB) will be delivered to your box, so you should not lose any important messages.

## FUTURE MESSAGES

Once all C&BA Email boxes have been cleaned and had a quota imposed upon them, we will be able to apply the quota to the entire system. At this time, the warning message will become more informative:

Your mailbox has exceeded one or more size limits set by your administrator.

Your mailbox size is 97,280 KB.

Mailbox size limits:

\* You will receive a warning when your mailbox reaches 92,160 KB.

\* You cannot send mail when your mailbox reaches 102,400 KB.

\* You cannot send or receive mail when your mailbox reaches 204,800 KB.

\* You may not be able to send or receive new mail until you reduce your mailbox size.

\* To make more space available, delete any items that you are no longer using or move them to your personal folder file (.pst).

\* Items in all of your mailbox folders including the Deleted Items and Sent Items folders count against your size limit.

\* You must empty the Deleted Items folder after deleting items or the space will not be freed.

See client Help for more information.

This message states more clearly what is happening. The mailbox in this example is 97,280 KB (or 97,280/1024 = 95 MB). The text states that this person will receive a warning when their mailbox has reached 92,160 KB (90 MB).

It states that when they reach 102,400 KB (100 MB) they will be unable to send email until they clean up their mailbox. And finally it states that if they reach 200 MB (204,800) they will be unable to send or receive any mail until they clean up their mailbox.

Information regarding how to clean up your email box.

General information regarding email at C&BA.

## Appendix C. Western Michigan University, WMU Strategic Plan for Information Technology, Electronic Mail Policy (draft), Effective 2/2002

## Purpose:

To inform WMU employees about the electronic mail policy, to create awareness of the associated privacy and security issues, and to address the uses of electronic mail in compliance with the policy.

## Policy Statement:

Introduction: Western Michigan University encourages the business use of electronic mail. Electronic communications systems, and all messages generated on or handled by electronic communications systems, including back-up copies, are considered WMU property.

Authorized Usage: WMU’s electronic communications systems are provided primarily for the support of the University’s mission including business, research, and educational activities. Incidental personal use is permissible if it does not interfere with the University’s mission or preempt normal business and educational activity, does not impede employee productivity, and does not consume more than a trivial amount of resources. Employees are not to use WMU’s email for commercial activities, support of charitable endeavors, or to send or forward chain mail. By default, WMU’s electronic communications systems are not encrypted. Do not send sensitive information via email.

User Identity: All electronic mail systems must have unique user-IDs and associated passwords to isolate the communications of different users. Misrepresenting, obscuring, suppressing, or replacing a user’s identity on an electronic communications system is forbidden. The user name, electronic mail address, organizational affiliation, and related information included with electronic messages or postings must reflect the actual originator of the messages or postings.

No Guaranteed Message Privacy: Western Michigan University cannot guarantee that email will be private. Electronic mail can be forwarded, intercepted, printed, and stored by others. WMU respects the rights of its employees, including their reasonable expectation of privacy. WMU is also responsible for servicing and protecting its electronic communications networks. To accomplish this, it may be necessary for technical support to intercept, disclose, or review electronic communications during the course of problem resolution. WMU may permit the inspection, monitoring, or disclosure of email when it is required by or consistent with applicable law or policy or any appropriately issued subpoena or court order. The Electronic Communications Privacy Act of 1986 also permits messages stored on University systems to be accessed by authorized personnel in certain circumstances.

Contents of Messages: Employees must not use profanity, obscenities, or derogatory remarks in electronic mail. Such remarks – even when made in jest – may create legal problems such as libel, sexual harassment, and defamation of character. Special caution is warranted because back-up and archival copies of electronic mail may be more permanent and more readily accessed than traditional paper communications.

Harassing or Offensive Materials: Sexual, ethnic, and racial harassment is strictly prohibited and is cause for disciplinary action that could result in termination. Western Michigan University retains the right to remove from its information systems any material it views as offensive or potentially illegal.

Purging Electronic Messages: Electronic mail systems are not intended for archival storage. Employees are responsible for periodically purging email messages from their personal storage areas.

Contact:

Office of Information Technology,

Planning & Policy Development,

(269)387-5430.

## References

Abrams, M.D., Bailey, D., 1995. Abstraction and refinement of layered security policy. In: Abrams, M.D., Jajodia, S., Podell, H.J. (Eds.), Information Security – An Integrated Collection of Essays. Berlin:. IEEE Computer Society Press, New York, NY.

Altheide, D.L., 1987. Ethnographic content analysis. Qualitative Sociology 10, 65–77.

Anton, A.I., Eart, J.B., Vail, M.W., Jain, N., Gheen, C.M., Frink, J.M., 2007. HIPAA’s effect on web site privacy policies. IEEE Security & Privacy 5 (1), 45–52.

Balakrishnan, R., Qiu, X., Srinivasan, P., 2010. On the predictive ability of narrative disclosures in annual reports. European Journal of Operational Research 202 (3), 789–801.

Barman, S., 2002. Writing Information Security Policies. New Riders Publishing, NY, New York.

Barry, C., Schamber, L., 1998. Users’ criteria for relevance evaluation: a cross-situational comparison. Information Processing and Management 34, 219–236.

Barry, C.L., 1994. User-defined relevance criteria: an exploratory study. Journal of the American Society for Information Science 45, 149–159.

Barry, C.L., 1998. Document representations and clues to document relevance. Journal of the American Society for Information Science 49 (14), 1293–1303.

Baskerville, R., Siponen, M., 2002. An information security meta-policy for emergent organizations. Logistics Information Management 15 (5/6), 337–346. Berelson, B. 1971, Population policy: personal notes, Population Studies 25 (2) 173–182 Berelson, B., 1971. Population policy: personal notes. Population Studies 25 (2), 173–182.

Besley, T., Case, A., 2003. Political Institutions and policy choices: evidence from the United States. Journal of Economic Literature 41 (1), 7–73.

Bodle, J.V., 1992. Are student newspapers as readable, interesting and thorough as community newspapers? A content analysis of student and community daily newspapers. In: Proceedings of 75th Annual Meeting of the Association for Education in Journalism and Mass Communication Montreal. Quebec, Canada, August 5-8, 1992.

Bozeman, B., 2000. Technology transfer and public policy: a review of research and theory. Research Policy 29 (4–5), 627–655.

Budge, I., Hans-Dieter, K., 2001. Finally! Comparative over-time mapping of party policy movement. In: Budge, I., Hans-Dieter, K., Volkens, A., Bara, J., Tanenbaum, E., Fording, R.C., Hearl, D.J., Kim, H.M., McDonald, M.D., Mendes, S.M. (Eds.), Map-ping Policy Preferences. Estimates for Parties, Electors, and Governments 1945-1998. Oxford University Press, Oxford, pp. 19–50.

Costello, A.B., Osborne, J.W., 2005. Best practices in exploratory factor analysis: four recommendations for getting the most from your analysis. Practica Assessment, Research & Evaluation 10 (7).

Crystal, A., Greenberg, J., 2006. Relevance criteria identified by health information users during web searches. Journal of the American Society fo Information Science and Technology 57 (10), 1368–1382.

Dembski, W.A., 1998. The Design Inference. Cambridge University Press, Cambridge, United Kingdom.

Dhillon, G., Backhouse, J., 1996. Risks in the use of information technology within organizations. International Journal of Information Management 16 (1), 65–74.

Dhillon, G., 1997. Managing Information Systems Security. MacMillan Press, London, England.

Dhillon, G., Torkzadeh, G., 2006. Value focused assessment of information system security in organizations. Information Systems Journal 16 (3).

Diver, S., 2007. An Information Security Policy Development Guide for Large Companies. SANS Institute. <http://www.sans.org/reading\_room/whitepapers policyissues/> (retrieved 10.10.08).

Doherty, N.F., Fulford, H., 2005. Do information security policies reduce the incidence of security breaches: an exploratory analysis. Information Resources Management 18 (4), 21–39.

Edmunds, A., Morris, A., 2000. The problem of information overload in business organizations: a review on the literature. International Journal of Information Management 20. 17–28.

Evans, S., Bush, S.F., 2002. Symbol compression ratio for string compression and estimation of Kolmogorov complexity. In: IEEE International Symposium on Information Theory.

Flesch, R., 1949. The Art of Readable Writing. Harper & Brothers, New York.

Frigault, M., Wang, L., Singhal, A., Jajodia, S., 2008. Measuring network security using dynamic bayesian network. In: Proceedings of the 4th ACM Workshop on Quality of Protection, October 27, 2008, Alexandria, Virginia, USA.

Galí, J., Gertler, M., 2007. Macroeconomic modeling for monetary policy evaluation. The Journal of Economic Perspectives 21 (4), 25–46.

Gaskell, G., 2000. Simplifying the onerous task of writing security policies. 1st Australian Information Security Management Workshop. Deakin University, Geelang, Victoria.

Goel, S., Bush, S.F., 2004. Biological models of security for virus propagation in computer networks. Login 29 (6), 49–59

Goel, S., Pon, D., Menzies, J., 2006. Managing information security: demystifying the audit process for security officers. Journal of Information System Security 2 (2), 25–45.

Gordon, L., Loeb, M., 2002. The economics of information security investment. ACM Transactions on Information and System Security 5 (4), 438–457

Hair, J.F., Anderson, R.E., Tatham, R.L., Black, W.C., 2006. Multivariate data analysis with readings. Pearson Prentice Hall, Upper Saddle River, NJ.

Hammond, A., Adriaanse, A., Rodenburg, E., Bryant, D., Woodward, R., 1995. Environmental Indicators: A Systematic Approach to Measuring and Reporting on Environmental Policy Performance in the Context of Sustainable Development. World Resources Institute. <http://www.pdf.wri.org environmentalindicators. bw pdf>

Hartley, J., 2003. Improving the clarity of journal abstracts in psychology: the case for structure. Science Communication 24, 366–379.

Hartley, J., Sydes, M., 1997. Are structured abstracts easier to read than traditional ones? Journal of Research in Reading 20, 122–136

Herzog, A., 1973. The B.S. Factor: The Theory and Technique of Faking it in America. Simon and Schuster, New York.

Hessink, H., Bollen, L., Steggink, M., 2007. Symmetrical versus asymmetrical company-investor communications via the internet. Corporate Communications: An International Journal 12, 145–160.

Hinde, S., 2002. Security surveys spring crop. Computers and Security 21 (4), 310–321.

Hite, R.E., Bellizzi, J.A., Fraser, C., 1988. A content analysis of ethical policy statements regarding marketing activities. Journal of Business Ethics 7 (10), 771– 776.

Hone, K., Eloff, J.H.P., 2002a. Information security policy-what do international information security standards say? Computers & Security 21 (5), 402–409.

Hone, K., Eloff, J.H.P., 2002b. What makes an effective information security policy? Network Security 6, 14–16.

Hone, K., Eloff, J.H.P., 2002c. Information security policy-what do international information security standards say? Computers & Security 21 (5), 402–409.

Hong, K.-S., Chi, Y.-P., Chao, L.R., Tang, J.-H., 2006. An empirical study of information security policy on information security elevation in Taiwan. Information Management & Computer Security 14 (2), 104–115.

Horton, N.S., 1986. Young adult literature and censorship: A content analysis of seventy-eight young adult books. Ph.D. diss., University of North Texas, 1986. Abstract in Dissertation Abstracts International 47 (11A), 4038.

Howlett, M., Ramesh, M., 2003. Studying public policy. Policy cycles and policy subsystems. Oxford University Press, Canada.

Hwang, M.I., Lin, J.W., 1999. Information dimension, information overload, and decision quality. Journal of Information Science 25 (3), 213–218.

SO, I., 2000. ISO/IEC 17799 Information Technology Code of Practice for Information Services. ISO, Geneva

Janczewski, L., 2000. Managing security functions using security standards. In: Janczewski, L. (Ed.), Internet and Intranet Security Management: Risks and Solutions. Idea Group Publishing, Hershey, PA, pp. 81–105.

Jaquith, A., 2007. Security Metrics: Replacing Fear, Uncertainty, and Doubt. Addison-Wesley Professional, US.

Jensen, C., Potts, C., 2004. Privacy policies as decision-making tools: an evaluation of online privacy notices. In: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (Vienna, Austria, April 24–29, 2004). CHI ‘04. ACM, New York, NY, pp. 471–478.

Jin, Y., Cameron, G.T., 2003. A Content Analysis of Direct Marketing Emails. Paper Presented at the Annual Meeting of the International Communication Association, Marriott Hotel, San Diego, CA.

Kassarjian, H.H., 1977. Content analysis in consumer research. Journal of Consumer Research 4, 8–18.

King, W.R., Liu, C.Z., Haney, M.H., He, J., 2007. Method effects in his survey research: an assessment and recommendation. Communications of the AIS 20 (1).

Kotulic, A.G., Clark, G.J., 2004. Why there aren’t more information security research studies. Information & Management 41 (5), 597–607.

Krippendorff, K., 2004. Content Analysis: An Introduction to its Methodology, second ed. Sage, Thousand Oaks, CA

Laffal, J., 1987. Concept analysis of language in psychotherapy. In: Russell, R.L. (Ed.), Language in Psychotherapy: Strategies of Discovery. Plenum Press, New York.

Li, Feng, 2008. Annual report readability, current earnings, and earnings persistence. Journal of Accounting and Economics 45 (2–3), 221–247.

Li, M., Vitanyi, P.M.B., 1997. An Introduction to Kolmogorov Complexity and its Applications. Springer-Verlag, NY.

Malaviya, P., John, D.R., Sternthal, B., Barnes, J., 2001. Human participants – respondents and researchers. Journal of Consumer Psychology 10 (1–2), 115– 121.

McIntosh, N., Duc, G., Sedin, G., 1999. Structure improves content and peer review of abstracts. Scientific meetings. European Science Editing 25, 43–47

Milne, G.R., Rohm, A.J., Bahl, S., 2004. Consumers’ protection of online privacy and identity. Journal of Consumer Affairs 38 (2), 217–232.

Nunnally, H., 1978. Psychometric Theory. McGraw-Hill, New York, NY.

Pahnila, S., Siponen. M., Mahmood. A., 2007. Emplovee's behavior toward IS Security Policy Compliance, In: Proceedings of the 40th Hawaii International Conference on System Sciences (HICSS ‘07).

Palmer, M.E., Robinson, C., Patilla, J.C., Moser, E.P., 2001. Information security policy framework: best practices for security policy in the E-commerce age. Security Management Practices 10 (2), 13–17.

Parker, D.B., 1998. Fighting Computer Crime: A New Framework for Protecting Information. John Wiley & Sons, New York, NY.

Pipino, L., Lee, Y.W., Wang, R.Y., 2002. Data quality assessment. Communication of the ACM 45 (4), 211–218.

Riffe, D., Lacy, S., Fico, F., 1998. Analyzing Media Messages: Quantitative Content Analysis. Lawrence Erlbaum Associates, Inc., New Jersey.

Russell, C., 2002. Security Awareness – Implementing an Effective Strategy. <http://www.sans.org/aware/sec\_aware.phg> (retrieved 3.01.06).

Sanderson, I., 2000. Evaluation in complex policy systems. Evaluation 6 (4), 433–454.

Sandhu, R.S., Samarati, P., 1994. Access control: principles and practice. IEEE Communications 32 (9), 40–48.

SEC, 1998. A Plain English Handbook: How to Create Clear SEC Disclosure Documents. US Securities and Exchange Commission, Washington, DC.

Schmidt, C.M., 1999. Knowing What Works: The Case for Rigorous Program Evaluation. IZA Discussion Paper No. 77. Available at SSRN: <http:// www.ssrn.com/abstract=217752>.

Sheehan, K., 2001. Email survey response rates: a review. Journal of Computer-Mediated Communication 6 (2).

Sheehan, K., 2005. In poor health: an assessment of privacy policies at direct-to-consumer web sites. Journal of Public Policy & Marketing 24 (2), 273–283

Singhal, A., Ou. X., 2009, Technigues for enterprise network security metrics, In: Proceedings of the 5th Annual Workshop on Cyber Security and Information Intelligence Research: Cyber Security and Information Intelligence Challenges and Strategies, April 13–15, 2009, Oak Ridge, Tennessee.

Smith, P.K., Smith, C., Osborn, R., Samara, M., 2008. A content analysis of school anti-bullying policies: Progress and limitations. Educational Psychology in Practice 24, 1–12.

Sterne, D.F., 1991. On the buzzword ‘security policy’. In: Proceedings of the IEEE Computer Society Symposium on Research in Security and Privacy, pp. 219- 230.

Straub, D.W., Welke, R.J., 1998. Coping with systems risk: security planning models for management decision making. MIS Quarterly 22 (4), 441–464.

Straub, D., Boudreau, M.C., Gefen, D., 2004. Validation guidelines for IS positivist research. Communications of the Association for Information Systems 13, 380–427.

Vail, M.W., Earp, J.B., Anton, A.I., 2008. An empirical study of consumer perception and comprehension of web site privacy policy. IEEE Transactions on Engineering Management 5 (3), 442–454.

von Solms, R., von Solms, B., 2004a. From policies to culture. Computers & Security 23 (4), 275–279.

von Solms, B., von Solms, R., 2004b. The 10 deadly sins of information security management. Computers & Security 23 (5), 371–376

Voss. B.D. 2003. The ultimate defense of depth-security awareness in vour company. <http://www.sans.org/reading room/whitepapers/awareness/> (retrieved 22.10.08).

Wang, R.Y., Strong, D.M., 1996. Beyond accuracy: what data quality means to data consumers. Journal of Management Information Systems 12 (4), 5–34.

Warman, A.R., 1992. Organizational computer security policy: the reality. European Journal of Information Systems 1 (5), 305–310

Webb, E.J., Campbell, D.T., Schwartz, R.D., Sechrest, L., 1966. Unobtrusive Measures: Nonreactive Research in the Social Sciences. Rand McNally & Company, Chicago.

White, C.B., Moyer, C.A., Stern, D.T., Katz, S.J., 2004. A content analysis of e-mail communication between patients and their providers: patients get the message. Journal of the American Medical Information Association 11 (4), 260–267.

Whitman, M., 2003. Enemy at the gate: threats to information security. Communications of the ACM 46, 91–95.

Winkler, B., 2000. Which kind of transparency? On the need for clarity in monetary policy-making. Working paper #26 European Centra Bank. Frankfurt Germany.

Ziv, J., Lempel, A., 1978. Compression of individual sequences via variable-rate coding. IEEE Transactions on Information Theory 24, 530–536.
