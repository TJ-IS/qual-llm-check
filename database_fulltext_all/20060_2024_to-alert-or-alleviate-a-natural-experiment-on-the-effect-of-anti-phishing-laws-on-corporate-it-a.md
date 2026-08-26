---
otero_id: 20060
otero_key: "2VGUNMTN"
title: "To alert or alleviate? A natural experiment on the effect of anti-phishing laws on corporate IT and security investments"
authors: "Xiaoxiao Wang; Wilson Weixun Li; Alvin Chung Man Leung; Wei Thoo Yue"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2024.114173"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# To alert or alleviate? A natural experiment on the effect of anti-phishing laws on corporate IT and security investments

![](/api/attachments/2VGUNMTN/fulltext/images/369cf45fb293e3c1bba5ec90e674bbf370e4c89c2351e3692bb3c3ce04290316.jpg)

Xiaoxiao Wang <sup>a</sup>, Wilson Weixun Li <sup>b,\*</sup>, Alvin Chung Man Leung <sup>a</sup>, Wei Thoo Yue <sup>a</sup>

<sup>a</sup> Department of Information Systems, College of Business, City University of Hong Kong, Hong Kong, China

<sup>b</sup> Department of Information Systems and Business Analytics, Deakin Business School, Deakin University, Melbourne, Australia

## A R T I C L E I N F O

Keywords: Anti-phishing laws Security investment IT investment Signaling effect Difference-in-difference

## A B S T R A C T

In the United States, between 2005 and 2017, 23 states enacted anti-phishing laws to prosecute those suspected of phishing. As the primary targets of phishing attacks, firms’ interpretations and reactions toward these laws are worth investigating. Utilizing a unique dataset in a natural experimental setting, this study employed the difference-in-differences method to contrast firms' investment decisions related to IT and cybersecurity in states in which such laws had been enacted and those in states without such laws, both before and after their enact ment. We found that firms with different operational experiences react to the enactment of the anti-phishing laws in different ways. We further demonstrate the moderating roles of the industry risk landscape and IT capability. Specifically, firms with high-IT increased investments in both IT and cybersecurity while the risk landscape stimulated investments in cybersecurity only. This suggests that the risk landscape facilitates sensitivity to the immediate risk signaled by enactment of the laws, and IT capability further enables the alignment between IT investments and security objectives. This study also discusses the policy implications of our findings

## 1. Introduction

Phishing is considered one of the most common methods for at tackers to breach organizations [1]. The 2020 “State of the Phish” report stated around 57% of organizations experienced phishing attacks [2]. Phishing attacks across the globe cause millions of dollars of losses per year [3], often in the form of damage to firms’ reputation and loss of customer confidence [4,5]. Furthermore, phishing is often used as the initial attack vector to launch other attacks such as data breaches and malware [6,7]. Phishing is challenging to curb because it costs almost nothing for “phishers” to execute attacks [8], and such attacks often target unsuspecting end users [9,10].

In the United States, California was the first state to pass legislation targeting phishing in 2005. Since then, 23 states have enacted antiphishing laws. These laws formally define phishing and dictate pun ishment for attackers. For example, Michigan’s anti-phishing laws focus on the use of false electronic communication or webpages representing a business to solicit personal information, whereas Oregon’s laws emphasize the false representation of a third person to solicit personal information, with specific conditions for law enforcement (as shown in Table B in Appendix B). Unlike anti-phishing laws, certain other cybersecurity legislations like Data Breach Notification Laws (DBNLs) and Consumer Privacy Acts impose regulatory obligations directly on entities, pushing firms toward enhanced investments in security and IT infrastructure to ensure compliance [111. These laws not only signal the escalating threat landscape but also mandate or incentivize firms to bolster their security measures, showcasing a direct, tangible impact on firms’ operational landscape. Moreover, statewide cybersecurity task forces, by enhancing state cybersecurity infrastructure and fostering a collaborative ecosystem, provide positive incentives that spur firms to bolster their security and IT investments [12]. These proactive efforts send a strong, positive signal, potentially confounding the threat signals perceived by firms. Therefore, it’s pivotal to discern the nuanced signaling effects of various cybersecurity laws and measures. Antiphishing laws, focusing on legal recourse against adversaries, serve as a more straightforward signal of threat to firms, contrasting with laws like DBNLs and Consumer Privacy Acts which mandate firms to enhance security measures. This distinct focus simplifies the investigation of signaling effect of anti-phishing laws, allowing for a more precise ex amination amidst the dynamic threat landscape.

Given cybersecurity laws are constantly evolving to adapt to cyber criminals’ tactics, and vice versa, the implementation of anti-phishing laws provides us with a unique setting in which to examine whether such laws extend to influencing the behaviors of firms that attackers target.<sup>1</sup> We conjecture two possible firm reactions: First, anti-phishing laws may give firms a misleading comfort in digital safety, potentially fostering complacency in cybersecurity—a reflection of the ‘Peltzman effect’ [13]. To illustrate, while airbags are designed to enhance passenger safety in vehicles, there is evidence suggesting that their presence may encourage some drivers to take more risks, under the assumption that they are better protected [14]. As a result, firms may regard such anti-phishing laws as a substitute for investments in new security measures. Second, anti-phishing legislation demonstrates the government’s serious commitment to tackling phishing crimes. Hence, such laws may serve as a threat-signaling mechanism for firms and encourage them to recognize the clear threat posed by phishing crimes. For example, De Silva and Torgler [15] found medical marijuana laws have a signaling effect that draws people’s attention to the risks of using marijuana. These two competing mechanisms may influence how firms deploy resources to fight phishing, specifically, and cybersecurity attacks, in general.

To protect users against phishing, firms often rely on conventional measures like security awareness training, firewalls, and spam filters, which have been criticized as being insufficient to combat sophisticated phishing threats.<sup>2</sup>’<sup>3</sup> Security experts advocate firms consider comprehensive solutions, such as integrating security into IT designs and leveraging advanced technologies to combat phishing threats [16,17]. Thus, in this study, we examine how the implementation of antiphishing laws affects firms’ IT and security investment decisions. We further contrast single-state firms and multi-state firms to understand the role of institutional factors (e.g., cybersecurity-related scope and experience). Prior studies have identified displacement effects [18] of the laws from the “attacker’s side,” which means more attacks are shifted toward less protected digital assets, and a larger scope of busi nesses could be affected if these “weakest links” are compromised. Considering this, our subsequent analysis seeks to address the ‘spillover effect,’ examining whether firms should enhance site-specific security or overall safeguards to mitigate broader risks from displacement strategies.

We used panel data, collected between 2010 and 2017, from approximately 400,000 firms. The study period began five years after the 2005 enactment of the first anti-phishing legislation in the United States, which ensures most firms had already become aware of phishing attacks and anti-phishing laws. During the research period, four U.S. states (i.e., Michigan, Alabama, Oregon, and Arizona) enacted statelevel anti-phishing laws in 2011, 2012, 2015, and 2016, respectively. However, Alabama and Arizona also enacted other cybersecurity-related acts to address denial of service attacks or spyware in the same year. To alleviate the potential confounding effects, we only considered firms in Michigan and Oregon as treatment firms.

This study makes several important contributions to current infor mation security literature and holds several important implications for practice: First, we enrich the existing research on the signaling effect of laws by demonstrating with empirical evidence that firms perceive the enactment of anti-phishing laws as a signal of increasing threats. Second, we explain the disparate organizational behaviors of single- and multi state firms in cybersecurity. Third, our findings suggest that policymakers should pay greater attention to the possible side effects of anti-phishing laws, as well as that appropriate legislation can help firms implement proactive security management by providing proper IT support.

The study is structured as follows: In Section 2, we review the related literature and develop our conceptual model and hypotheses. Section 3 describes our data source and the methodology we undertook. In Section 4, we present our analysis and discuss the results. In the final section, we provide the conclusions. We present the results of various additional analysis in Appendix A and C and the details of the anti-phishing acts in Michigan and Oregon in Appendix B.

## 2. Literature review and hypotheses development

Our work is closely related to the following four streams of literature: the indirect effect of regulations and law enactments; the effect of cybersecurity-related laws and policies; firm-level factors affecting se curity investments; and the spillover effect in cybersecurity research. We summarize and discuss the related concepts of each stream of research below.

The indirect effect⁴ of regulations and laws often refers to the effect on unregulated entities [19]. For example, Zhang [20] identifies that affirmative action bans enforced on public sectors also affect privatesector executives’ decision-making in regard to recruiting minorities. Peukert et al. [21] found the enactment of the general data protection regulation (GDPR) reduces the interactions between websites and web technology providers; the relationship is even extended to those firms that are not regulated by GDPR. Prior studies propose two mechanisms to explain the indirect effect. The first is sending a signal to the unreg ulated entities [21,20], and the second is altering the market structure [19]. The unregulated entities may interpret the policies as a signal, indicating a similar future regulation [21] or as revealing social norms [20], which ultimately motivate and change the unregulated entities behaviors. Regardless of the unregulated entities’ interpretation, some policies enforced on regulated entities directly change the market structure. For example, The Sarbanes–Oxley Act of 2002 places stricter requirements on public firms’ internal controls, which stimulates the demand for auditing services but also increases the audit fees for un regulated nonprofit organizations [19]. In the context of this work, we consider firms to be unregulated entities, as the anti-phishing laws penalize the adversaries launching phishing attacks (as shown in Table B in Appendix B), and the mechanism of the indirect effect is more aligned with the signaling effect argument and less relevant to the context of altering the market structure. The enactment of anti-phishing laws serves as a clear signal of an escalating threat landscape. As risks become more tangible, firms prompt reassessment and necessary adjustments to IT and security infrastructures [22,23]. In addition, the enactment strengthens the signal to the market by defining crimes and penalties, guiding firms to align their practices and policies to prevent potential brand damage.

Regarding the research on cybersecurity-related laws and policies, scholars mainly focus on firm-specific regulations, like GDPR, DBNL, and the Cybersecurity Information Sharing Act (CISA), which require firms to fulfill privacy protection or security incident disclosure re quirements. This stream of studies investigates the effects of the laws on firms’ security investments [24] and security outcomes (e.g., rates of identity theft and spam volumes) [25,26]. Furthermore, prior studies have revealed firms may undertake undesirable behaviors when facing related laws, including compromising the readability and details of data breach disclosures [27,28], hoarding bad news, strategically timing data breach disclosures [29,30], or slowing down digitalization [11].

However, firms’ responses to regulations are mainly understood from the perspective of complying with regulations and reducing (or trans ferring) compliance costs. There is little discussion regarding how firms interpret the laws and shape their understanding of the risk land scape—or what factors moderate firms’ interpretations and reactions to such laws. Overlooking firms’ interpretations may undermine the importance of firms’ proactively leveraging regulations and policies to advocate for more cybersecurity attention and resources [31]. More over, law enforcement signals a national commitment to ensuring a secure environment, which can also encourage firms to allocate more resources to profit reinvestment [32,33]. Thus, investigating how firms interpret law enforcement and what factors moderate the process is important to the development of a comprehensive understanding regarding the interaction between policymakers and firms, as well as provide more insight into future cybersecurity-related legislation.

Firms’ interpretations of and reactions toward legislation can be dependent upon their capabilities and prior experience. Prior literature identifies firm-level factors like senior management’s degree of commitment to security and the security awareness of top managers as important for firms’ implementation of security solutions [34,35,36]. Moreover, firm understanding of security threats and technology solu tions has been shown to positively affect the firm’s security management [37,38]. According to organizational learning literature [39,40,41], security awareness and capabilities can be nurtured during the proces of addressing relevant issues. In the context of this work, firms operating in multiple states have richer security-related experience than single state firms because multi-state firms have encountered a wider scope of security issues and security-related regulations. Conceptually, multi state firms can leverage prior experience and quickly adapt in response to new legislation.

The spillover effect in cybersecurity research focuses on market re actions, including the non-breached firms, in response to data breach incidents. Islam et al. [42] and Kelton and Pennington [43] find in vestment contagion effects on non-breached rivals due to the un certainties caused by the breached firms. Li et al. [44] note that non breached firms adjust their security strategies when industrial peers experience security breaches. Jeong et al. [45] observe the market in terprets the security investment of one firm after a breach, which can increase the overall security level in the industry. The spillover effect further extends to other business behaviors such as increasing cash holdings [46]. These findings support the view that the dynamic risk landscape signaled by the actual incidents or the market can affect firms actions. Kelton and Pennington [43] and Kashmiri et al. [47] conclude firms with extensive understanding of security issues can effectively respond to evolving threats and act to mitigate negative spillover effects. However, such a viewpoint has not been extended to the context of security-related policies.

Building on previous research, in the current study, we seek to develop a conceptual model to examine the signaling effect of antiphishing laws on firms’ investment decisions in IT and security. We highlight the importance of the moderating role played by firms’ multi state operational experience, which facilitates knowledge-sharing among sites and sensitivity to evolving threats. Fig. 1 presents our conceptual model.

## 2.1. Signaling effect

As discussed. we base the conceptual model on the signaling effects of the laws, as identified in previous studies [21,20]. A distinctive feature of anti-phishing laws is their classification under civil jurisdic tion in two-thirds of states, leading to financial penalties for adversaries rather than imprisonment, unlike other computer crime statutes which are typically criminal across states.<sup>5</sup> For instance, laws against hacking, unauthorized access, and other cybercrimes fall under criminal juris diction.<sup>v</sup> On the other hand, spyware laws exhibit a split, with an equal division between civil and criminal categorization across states.<sup>v</sup> Antiphishing laws, with their slant toward civil penalties such as fines, may seem less intimidating to businesses because the consequences for cybercriminals aren’t as harsh. This perception may shape how com panies invest in security differently than they would under more strin gent cybersecurity regulations.

Building on the discussion of perceived deterrence, there’s a realm of law-induced ‘false’ sense of security as illustrated by [48,49]. For instance, the Adam Walsh Child Protection and Safety Act, which targets low-risk offenders but sometimes misses high-risk culprits, could give a misleading signal about the relative safety of certain environments [48]. Translating this to the realm of cybersecurity, one might assume that firms would perceive anti-phishing laws as providing an adequate shield and thereby become passive about ramping up their security in vestments. However, the adequacy of civil penalties as deterrents is debatable [50,51], especially when compared with the potential lucra tive gains from successful cyberattacks. Beyond individual laws, the broader legal framework encompassing new cybersecurity laws, irre spective of their punitive nature, also echoes across the business land scape, heightening stakeholder threat awareness [52], leading to a cascading impact on the corporate world. The signaling effect combined with regulatory compliance has been known to spike the demand for security products [53]. Similarly, researchers have argued higher risk awareness at the organizational level can motivate users to seek addi tional measures to manage risks [54].

Given the nuances and the weight of the signaling effect, especially in the backdrop of these laws being civil in nature, we hypothesize that enacting anti-phishing laws will amplify the security consciousness of firms operating in states with such regulations, prompting them to bolster their security investments.

H1a. Anti-phishing laws motivate firms operating in anti-phishing law states to increase security investments.

## 2.2. Integration of IT and security investment strategies

Rather than solely focusing on security investment, firms must strengthen IT competency to counteract threats effectively. This perspective aligns with the resource-based view emphasizing that proper IT competency requires implementing all facets of IT practices [40]. General IT investment, aimed at holistically enhancing a firm’s IT infrastructure, fosters a more robust strategy in handling security chal lenges [55,56].

Previous studies underline the crucial role of IT within security management, broadening firms’ avenues for tackling security challenges [57,58,59]. This view is supported by several essential insights. First, IT plays a vital role in pinpointing and remedying vulnerabilities rooted in flawed design [60,61]. Second, strong IT infrastructures facilitate the alignment of IT and security objectives [62,63]. Li et al. [64] suggest a lack of such alignment might undermine the effectiveness of security measures. Third, various IT solutions can nurture a security-conscious culture, reducing errors in IT execution [65] and bridging the existing divide between IT and security [66,35]. Specifically, Li et al. [67] pro vides empirical support that firms are investing more in general IT following heightened threat awareness, which not only addresses im mediate security needs but also strengthens the overall IT framework to prevent future incidents.

In light of previous empirical findings $[ 6 6 , 6 5 , 6 7 ]$ , we propose that anti-phishing laws may elevate firms’ security consciousness, leading to an increased investment in IT infrastructure. These investments repre sent a strategic move toward a unified approach to security manage ment, recognizing the interdependence of IT and security measures.

![](/api/attachments/2VGUNMTN/fulltext/images/3266e359e4c0bb97b647d2ce298e3b826593a250f19e6258be4699f5f6d63d29.jpg)  
Fig. 1. Conceptual model.

H1b. Anti-phishing laws motivate firms operating in anti-phishing law states to increase general IT investments.

## 2.3. The moderating role of multi-state operational experience

Firms operating across multiple states face a complex regulatory environment, which often necessitates increased investment in IT se curity, fostering heightened resilience to cyber threats. Three perspec tives shape this necessity: the broader spectrum of security risks and experience gained in handling them; prior experience with similar reg ulations and acts across different jurisdictions; and knowledge sharing among operational units in various states [68,69,70]. The expansive operational footprint exposes multi-state firms to diverse risks, which drives them to develop comprehensive risk assessments and manage ment [69]. With prior experience enabling swift alignment to new reg ulatory changes, such firms are more likely to pool resources to counter significant risks in more efficient ways. Knowledge sharing within a firm’s diverse units leads to the quick dissemination of best practices and effective risk management strategies [68,71,72], emphasizing the need for careful security measures [70]. Consequently, we posit multi-state operation experience has a positive moderating effect on security investment.

## H2a. Multi-state operation positively moderates the positive effect of the anti-phishing laws on security investments.

Multi-state operational experience could significantly influence firms’ approach to IT investment decisions, extending beyond mere se curity measures. Such firms are poised to leverage their diverse regu latory exposure to sharpen their IT strategies [61]. This advantage fosters a preventive investment focus, addressing the foundational IT issues rather than transient problems. This broader, insight-driven approach to IT planning echoes the preventative ethos found in prior research on security awareness and comprehensive cybersecurity in vestment [67]. Thus, we propose that multi-state operation experience has a positive moderating effect on IT investment.

H2b. Multi-state operation positively moderates the positive effect of the anti-phishing laws on general IT investments.

## 3. Data and methodology

## 3.1. Data

We obtained annual IT and security investment data from >400,000 organizations located in the United States from Harte-Hanks Market Intelligence. Our data set contains each site's annual IT-related in vestments, currently installed IT, and anticipated future IT purchase from 2010 to 2017. A site refers to a representative office or a branch office of a firm. Referring to reports by the National Conference of State Legislatures, we identified 23 states with anti-phishing laws. Nineteen states had implemented anti-phishing laws prior to the study period, that is, before 2010.<sup>6</sup> We focused on firms (i.e., treatment firms) that have sites in two states that enacted anti-phishing laws after 2010, which are Michigan (enacted in 2011) and Oregon (enacted in 2015). The laws in these two states do not mandate that firms implement antiphishing measures or make specific IT investments. Following previous studies utilizing DID model [73,74], we used data from three years (the year before the enactment year, the enactment year, and the year after the enactment year) to study the law’s impacts. We aggregated site-level data for a firm in each state to construct firm-state-level data.<sup>7</sup> The firmstate-level data enables us to analyze the effect of the legislation on firms’ investment decisions within a state and to conduct additional analysis on the spillover and displacement effects. Based on firms operating locations, we divided treatment firms into four cases to compare the investment decisions of firms in different locations to test our hypotheses. We chose our control firms from firms operating in the 27 states without anti-phishing laws. Table 1 illustrates these details. We provide the details of the matching process in the next subsection.

Table 2 summarizes the variables in this study. We used the total IT budget to measure IT investments. To measure security investments, we applied principal component analysis (PCA) to aggregate the purchase likelihood score (PLS) of security software and the PLS of antivirus software following the method suggested by Santhanam et al. [75].<sup>8</sup> Antivirus software, which includes email spam filters, is considered to help deter attacks and detect hacking launched by emails [76]. Table 3 shows the summary statistics of the four cases from before and after the enactment of anti-phishing laws.

## 3.2. Propensity score matching

Although our research context provides a natural experiment setting for examining the impacts of anti-phishing laws, each firm’s specific characteristics, such as revenue and firm size, may influence firms’ in vestment decisions. To eliminate the influence of external factors [77] and satisfy the parallel trend assumption [78,79], we applied the pro pensity score matching (PSM) method to identify the control firms that resembled the treatment firms in all relevant attributes before enact ment of the anti-phishing laws. In the matching process, we used data from the year before the law was enacted. We applied a logit model when

Table 1  
The treatment groups and control groups in four cases.

<table><tr><td>Cases</td><td>Treatment groups</td><td>Control groups</td></tr><tr><td>Single-state firms</td><td>The firms are only operating in one of the two states with anti-phishing laws passed between 2010 and 2017.</td><td>The firms are only operating in one of the states not enacting anti-phishing laws.</td></tr><tr><td>Multi-state firms in focal states</td><td>The firms are operating in one of the two states with anti-phishing laws passed between 2010 and 2017, and have sites in other states.</td><td>The firms are operating in more than one states not enacting anti-phishing laws.</td></tr><tr><td>Multi-state firms in other phishing law state</td><td>The firms are operating in states enacting anti-phishing laws before 2010, and have sites in other states that include one of the two states with anti-phishing laws passed between 2010 and 2017.</td><td>The firms are operating in more than one states not enacting anti-phishing laws.</td></tr><tr><td>Multi-state firms in other non-phishing law states</td><td>The firms are operating in states not enacting anti-phishing laws, and have sites in other states that include one of the two states with anti-phishing laws passed between 2010 and 2017.</td><td>The firms are operating in more than one states not enacting anti-phishing laws.</td></tr></table>

applying the PSM because the treatment (the enactment of the law) is binary. The variables used in the matching process include the number of employees, revenue, the number of IT staff, and “hq” (see Table 2 for further details). We used these control variables in PSM to reflect firm size and firm capability, which may influence firms’ subsequent in vestment decisions. Moreover, headquarters and subsidiaries may have different reactions [80], and subsidiaries’ decisions may be influenced differently [81]. We applied exact matching to control “hq”, which means the variables of the matched group should have the same value as those of the treatment group. We subsequently estimated the propensity score. In each case and industry, we separately matched the firms from the two target states. For example, for single-state firms, we matched the IT industry firms in Michigan with control firms of IT industry, and so on. To identify more control firms and ensure consistency, we applied 1:30 nearest neighbor matching to identify the matched group with the most similar estimated propensity score. Meanwhile, we set the caliper (the maximum allowable difference between two participants) to equal to or <0.05. About 75% of treated firms were successfully matched. After implementing PSM, we ran a t-test to check the similarity of the matching results by comparing the means of each matching character istics variable in the treatment group and the matched group. We also obtained the standardized percentage bias, which measures the per centage of the sample means in the treated and matched samples [82]. As shown in Table 4, the standardized percentage biases were <10%, and the t-test results show an insignificant difference between the two groups, indicating the treated and matched samples are quite similar. We created charts to compare the changing trends of the treatment and control groups before the enactment year. The parallel trend assumption argues the treatment and control groups have similar trends in the absence impact from the implementation of anti-phishing laws. Fig. 2 shows the trends of total IT investments and the aggregated security investments of firms in anti-phishing law states and the matched control firms. “Year” equals zero if it is the year of implementation of antiphishing laws. Other cases also show parallel trends between the treatment and control groups.

Table 3  
Summary statistics of treatment firms in four cases

<table><tr><td></td><td colspan="2">Before the law was enforced</td><td colspan="2">After the law was enforced</td></tr><tr><td>Variables</td><td>Mean</td><td>Std. Dev.</td><td>Mean</td><td>Std. Dev.</td></tr><tr><td colspan="5">Single-state firms</td></tr><tr><td>Security investment</td><td>0.6551</td><td>0.9371</td><td>0.2944</td><td>0.8029</td></tr><tr><td>IT investment</td><td>0.4306</td><td>0.6752</td><td>0.0227</td><td>0.6035</td></tr><tr><td colspan="5">Multi-state firms in focal states</td></tr><tr><td>Security investment</td><td>0.2366</td><td>0.9221</td><td>0.2848</td><td>0.9309</td></tr><tr><td>IT investment</td><td>0.1750</td><td>0.7052</td><td>0.2664</td><td>0.7529</td></tr><tr><td colspan="5">Multi-state firms in the other phishing law states</td></tr><tr><td>Security investment</td><td>0.2103</td><td>0.9189</td><td>0.3894</td><td>1.0524</td></tr><tr><td>IT investment</td><td>0.1528</td><td>0.7032</td><td>0.4328</td><td>0.8347</td></tr><tr><td colspan="5">Multi-state firms in the other non-phishing law states</td></tr><tr><td>Security investment</td><td>0.1692</td><td>0.8983</td><td>0.3237</td><td>1.0560</td></tr><tr><td>IT investment</td><td>0.1272</td><td>0.6971</td><td>0.3844</td><td>0.8627</td></tr></table>

## 3.3. Difference in differences model

After applving PSM. we performed the difference in differences (DID) model to test our hypotheses. The DID model can eliminate invariant estimation bias and is widely used to estimate causal relationship [83,84]. We used Antiph as the treatment dummy, which equals one if the firm i is in a state with an anti-phishing law. We used timeD as the time dummy, which equals one if the year t is equal to or larger than the year when an anti-phishing law was enacted in a particular state. The interaction term “Antiph × timeD ” captures the interaction effect.

Table 2  
The definition of variables.

<table><tr><td>Type</td><td>Name</td><td>Definition</td></tr><tr><td rowspan="12">Control variable (Treatment independent variable)</td><td>Emple</td><td>The number of employees</td></tr><tr><td>Reven</td><td>Estimated revenue</td></tr><tr><td>IT_staff</td><td>The number of IT or IS employees</td></tr><tr><td>Internet_users</td><td>The number of employees using the Internet</td></tr><tr><td>Storage</td><td>Gigabytes used for storage</td></tr><tr><td>Outsourcing/</td><td rowspan="2">Whether the third-party services (e.g., data center management, disaster recovery, hardware services, server maintenance) or software-as-a-service (SaaS) being used in the firm</td></tr><tr><td>SaaS</td></tr><tr><td>Hq</td><td>Whether the firm has a headquarter in the state.</td></tr><tr><td>install_flag</td><td>Whether the firm installed any one security-related software (ID/Access software, security software, third-party firewall services, and third-party intrusion detection services) before the law was published</td></tr><tr><td>Breach</td><td>Whether the firm experienced data breaches in that year</td></tr><tr><td>Report</td><td>The number of data breach reports in the state</td></tr><tr><td>Numsites</td><td>The amounts of sites that the firm is operating in the state</td></tr><tr><td rowspan="3">Dependent variables</td><td>Security</td><td>The average PLS of security software and antivirus software</td></tr><tr><td>Investment</td><td></td></tr><tr><td>IT Investment</td><td>The total IT budget</td></tr><tr><td>Time dummy</td><td> $timeD_t$ </td><td>Equal to 1 if the year t is equal to or larger than the year when the anti-phishing law was acted in a certain state</td></tr><tr><td>Treatment dummy</td><td> $Antiph_i$ </td><td>Equal to 1 if the firm i is in a state with anti-phishing law</td></tr></table>

Covariate comparison before and after matching.

<table><tr><td rowspan="2" colspan="3"></td><td colspan="2">Mean</td><td rowspan="2">Standardized percentage biases</td><td rowspan="2">t-stat(p-value)</td></tr><tr><td>Treated</td><td>Control</td></tr><tr><td rowspan="8">Michigan</td><td rowspan="2">Emple*</td><td>Unmatched</td><td>-0.1529</td><td>-0.3226</td><td>17.5</td><td>0.000</td></tr><tr><td>Matched</td><td>-0.1529</td><td>-0.1429</td><td>-1.0</td><td>0.057</td></tr><tr><td rowspan="2">Reven*</td><td>Unmatched</td><td>-0.0387</td><td>-0.1375</td><td>12.0</td><td>0.000</td></tr><tr><td>Matched</td><td>-0.0387</td><td>-0.0414</td><td>0.3</td><td>0.577</td></tr><tr><td rowspan="2">IT Staff*</td><td>Unmatched</td><td>0.5727</td><td>0.5272</td><td>12.4</td><td>0.000</td></tr><tr><td>Matched</td><td>0.5727</td><td>0.5689</td><td>1.0</td><td>0.042</td></tr><tr><td rowspan="2">Hq</td><td>Unmatched</td><td>0.1036</td><td>0.0860</td><td>6.0</td><td>0.000</td></tr><tr><td>Matched</td><td>0.1036</td><td>0.1036</td><td>0.0</td><td>1.000</td></tr><tr><td rowspan="8">Oregon</td><td rowspan="2">Emple*</td><td>Unmatched</td><td>0.3244</td><td>-0.0449</td><td>42.0</td><td>0.000</td></tr><tr><td>Matched</td><td>0.3244</td><td>0.3115</td><td>1.5</td><td>0.285</td></tr><tr><td rowspan="2">Reven*</td><td>Unmatched</td><td>0.2761</td><td>-0.0431</td><td>30.8</td><td>0.000</td></tr><tr><td>Matched</td><td>0.2761</td><td>0.2785</td><td>-0.2</td><td>0.882</td></tr><tr><td rowspan="2">IT Staff*</td><td>Unmatched</td><td>0.0379</td><td>-0.3189</td><td>37.1</td><td>0.000</td></tr><tr><td>Matched</td><td>0.0379</td><td>0.0136</td><td>2.5</td><td>0.060</td></tr><tr><td rowspan="2">Hq</td><td>Unmatched</td><td>0.1277</td><td>0.1111</td><td>5.1</td><td>0.000</td></tr><tr><td>Matched</td><td>0.1277</td><td>0.1277</td><td>-0.0</td><td>1.000</td></tr></table>

Note: \* Log transformed and standardized.

![](/api/attachments/2VGUNMTN/fulltext/images/d7854577e03dd0adf16f0475f92ceac2a31c323a4e40cbecbdc0619faf536901.jpg)

![](/api/attachments/2VGUNMTN/fulltext/images/8c7e32bc2c5a6cd27890dc5a8a2e522566880cf1115faaab196f49753e0f8b6e.jpg)  
Fig. 2. The change trend of the total IT investment and security investment.

Because our target states enacted anti-phishing laws in different years, we followed Autor [85] and He et al. [86] and built a multipleperiod DID model as follows:

$$
\begin{array}{r l} \text { Dependent   variables } _ {i, t} & = \beta_ {0} + \beta_ {1} \text { Antiph } _ {i} \times \text { timeD } _ {t} + \gamma_ {1} \text { Control   variables } _ {i, t} \\ & + \gamma_ {2} \text { YearDummy } _ {t} + \gamma_ {3} \text { FirmDummy } _ {i} + \varepsilon_ {i, t} \end{array}
$$

$\beta _ { 1 }$ is the coefficient estimate of the treatment effect after enactment of an anti-phishing law in a state. It is the main variable of interest in our empirical analyses. We used YearDummy to control for time-fixed ef fects common to all firms and FirmDummy to control for mean differ ences in investments across firms. We included control variables like prior data breach incidents at the state level, as poor security perfor mance may accelerate the enactment of anti-phishing laws. We further controlled the number of sites a firm operates in a state and the firm’s present installed software, which may influence a firm’s investment strategies when anti-phishing laws are enacted.

## 4. Results and discussion

4.1. Anti-phishing laws stimulate security investments but dampen IT investments

We first estimated the overall impacts of anti-phishing laws on firms in states that enacted anti-phishing laws. We combined single-state and

## Table 5

The impacts of anti-phishing law on IT and security investments.<sup>a</sup>

<table><tr><td rowspan="3">Results</td><td colspan="2">Dependent variables</td></tr><tr><td>(1)</td><td>(2)</td></tr><tr><td>Security investment</td><td>IT investment</td></tr><tr><td>Antiph × timeD</td><td>0.0205**(0.0032)</td><td>-0.0795**(0.0025)</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td></tr><tr><td>Year dummies</td><td>Yes</td><td>Yes</td></tr><tr><td>Firm dummies</td><td>Yes</td><td>Yes</td></tr><tr><td>N</td><td>476,440</td><td>476,440</td></tr><tr><td> $R^2$ </td><td>0.1163</td><td>0.1962</td></tr></table>

Note: Standard errors in parentheses: \* denotes $p < 0 . 0 5$ and $^ { * * }$ denotes $p <$ $_ { 0 . 0 1 }$  
<sup>a</sup> We conducted an additional robustness test clustering standard errors at the firm level, the results are consistent with our main model, which uses the robust estimator of variance

multi-state firms located in states that enacted anti-phishing laws. Col umn 1 of Table 5 demonstrates anti-phishing laws had a significant positive effect on firms’ security investments, with firms in states that enacted the law increasing their security investments by an additional 0.0205 standard deviations compared to firms in states that did not enact the law $( \beta _ { 1 } = 0 . 0 2 0 5 , p < 0 . 0 1 )$ . This result indicates the anti phishing laws raise firms’ awareness of security threats, which further drives firms to revisit their security strategies. Firms interpret the leg islation’s signals as an increasing threat level and react by increasing security investment instead of relying on the government.

Table 6  
The moderating effect of multi-state operation.

<table><tr><td rowspan="3">Results</td><td colspan="2">Single-state firms</td><td colspan="2">Multi-state firms</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td></tr><tr><td>Antiph × timeD</td><td>-0.0005(0.0034)</td><td>-0.0986**(0.0027)</td><td>0.1287**(0.0083)</td><td>0.0127*(0.0065)</td></tr><tr><td>N</td><td>402,386</td><td>402,386</td><td>74,054</td><td>74,054</td></tr><tr><td> $R^2$ </td><td>0.1233</td><td>0.2046</td><td>0.0963</td><td>0.1667</td></tr></table>

Note: Standard errors in parentheses: \* denotes $\mathfrak { p } < 0 . 0 5$ and $^ { * * }$ denotes $p <$ 0.01. All analyses include control variables, year dummies, and firm dummies.

In contrast, Column 2 shows firms in states with the anti-phishing law, on average, reduced their IT investments by an additional 0.0795 standard deviations relative to firms in states that did not enact the law $( \beta _ { 1 } = - 0 . 0 7 9 5 , p < 0 . 0 1 )$ ). This result shows anti-phishing laws further affect firms’ IT investment. Hence, H1a is supported whereas H1b is not. This trend could be attributed to a reactive posture adopted by some firms, aiming to reduce potential losses by minimizing exposure to threats. This posture is often driven by the uncertainties involved in identifying and addressing security weaknesses. Such a strategy is in line with the findings from Li et al. [23], which suggest that higher IT in vestments might inadvertently lead to increased vulnerabilities exploitable by hackers. Further. Zhang et al. [11] observes that heightened cybersecurity requirements can prompt firms to reassess their IT investment strategies, particularly when these investments heighten the risk of exposing sensitive data. This observation echoes our findings, implying a strategic recalibration of IT and security in vestments in response to the evolving cybersecurity landscape. The observed negative impact of anti-phishing laws on IT investment may not necessarily be a failure to recognize IT’s role in security. Rather, it appears to be a strategic adaptation to reduce risks associated with increased IT vulnerability.

Moreover, the discrepancies between our findings and those of Li et al. [67] could stem from the differences in our analytical focus. Whereas Li et al. [67] delves into actual disclosed firm-level security awareness of materialized data breach incidents, our study centers on examining perceived escalating phishing threats at the state level. This uniform approach to threat perception across firms within a state might explain the noted variance.

## 4.2. Firms with multi-state operations increase more investments in both security and IT

To estimate the moderating effect of the operational experience of multi-state firms, we compare single-state and multi-state firms’ re actions to the enactment of anti-phishing laws after controlling for firmlevel characteristics, such as firm size and industry. Columns 1 and 2 in Table 6 reveal that while the anti-phishing laws led single-state firms to slightly decrease their security investments (though not significantly, with $\beta _ { 1 } = - 0 . 0 0 0 5 ) ,$ <sup>9</sup> they significantly reduced their IT investments by an additional 0.0986 standard deviations $( \beta _ { 1 } = - 0 . 0 9 8 6 , p < 0 . 0 1 )$ . In contrast, Columns 3 and 4 in Table 6 show multi-state firms responded to the laws by significantly ramping up their investments in both secu rity $( \beta _ { 1 } = 0 . 1 2 8 7 , p < 0 . 0 1 )$ and IT $( \beta _ { 1 } { = } 0 . 0 1 2 7 , p < 0 . 0 5 )$ , increasing them by an additional 0.1287 and 0.0127 standard deviations, respec tively. We further conducted a comparison test [87,88] to determine whether the differences between the estimated coefficients of the two groups were significant. The results show significant inter-group dif ferences in both security $( t = - 7 1 4 1 . 4 4 , p < 0 . 0 0 1 )$ and IT $( t =$ − 7803.28, $p < 0 . 0 0 1 )$ , indicating the laws’ effects on security and IT with respect to single-state firms are smaller than those among multistate firms. The difference in effects between single-state firms and multi-state firms indicates the moderating role of the multi-state oper ation. Firms with a larger geographic scope tend to gain more experience in addressing security-related issues, like identifying security loopholes (e.g., lack of multi-factor authentication, failure to configure and update email filters/firewalls) that may lead to phishing attacks and imple menting suitable solutions to address the issues. Ultimately, branches with little experience can benefit from such knowledge and invest in security and IT effectively. Therefore, both H2a and H2b are supported.

## 4.2.1. Spillover effects of anti-phishing laws are stronger among sites located in other states with anti-phishing laws

Analyzing the spillover effects of cybersecurity laws reveals cyber security laws’ impact on firms’ strategies across states, amid known risks of attacker displacement to less-secured assets [18]. In the context of this work, the spillover effect occurs when legislation affects firms in other states in ways like the effect on firms in focal states. For example, firms in focal states and other states both increase (decrease) IT assets, anticipating the security environment will become more secure (risky). In contrast, the displacement effect means the laws have contrary effects on firms in focal states and other states. For example, firms in focal states reallocate their IT assets to other states (or vice versa), anticipating the security environment becoming riskier in the focal states (or other states). Note that, in both cases, “firms” refer to sites of the same en terprise operating in different states.

We first conducted additional analysis on the changes in investments in IT and security among these firms before and after the enactment. According to Table 7, both types of firms—those in states with and without enacted anti-phishing laws—registered significant upticks in IT investments, with increases of 0.0664 standard deviations for firms in non-phishing law states $( \beta _ { 1 } = 0 . 0 6 6 4 , p < 0 . 0 1 )$ and 0.0993 standard deviations for firms in phishing law states $( \beta _ { 1 } = 0 . 0 9 9 3 , \mathrm { ~ p ~ < ~ } 0 . 0 1 )$ Similarly, security investments rose by 0.0957 standard deviations for firms in non-phishing law states $( \beta _ { 1 } = 0 . 0 9 5 7 , \mathrm { p } < 0 . 0 1 )$ and 0.1559 standard deviations for firms in phishing law states $( \beta _ { 1 } = 0 . 1 5 5 9 , \mathtt { p } <$ 0.01). These significant increases across the board suggest that antiphishing laws have a ripple effect, influencing multi-state firms even in regions where such laws haven’t been legislated. This aligns with our Hypothesis 2, positing that anti-phishing laws intensify the demand for a more secure digital infrastructure, with multi-state firms acting as con duits for disseminating best practices and security knowledge. Further more, evidence of the spillover effects indicates a firm-wide scope to address security threats among multi-state firms. Thus, multi-state firms interpret the state-level laws as a signal of global threats more than local threats $( \mathrm { i . e . , }$ within the focal states). In contrast, multi-state firms consider firm-wide efforts to address phishing threats, given adversaries may leverage the interconnectedness of the sites to target the weakest links (i.e., the most vulnerable sites) and compromise the firm. There fore, firms in both focal states and other states must work together to consolidate their security strategies.

The spillover effects of anti-phishing law on IT and security investments.

<table><tr><td rowspan="3">Results</td><td colspan="2">Multi-state firms in other anti-phishing law states</td><td colspan="2">Multi-state firms in other non-phishing law states</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td></tr><tr><td>Antiph × timeD</td><td>0.1559**(0.0080)</td><td>0.0993**(0.0055)</td><td>0.0957**(0.0085)</td><td>0.0664**(0.0061)</td></tr><tr><td>N</td><td>104,375</td><td>104,375</td><td>90,989</td><td>90,989</td></tr><tr><td> $R^2$ </td><td>0.0782</td><td>0.1650</td><td>0.0811</td><td>0.1584</td></tr></table>

Notes: Standard errors in parentheses: \* denotes $p < 0 . 0 5$ and \*\* denotes $p <$ 0.01. All analyses include control variables, year dummies, and firm dummies.

Moreover, the comparison test shows multi-state firms in other anti phishing law states increase their IT investments $( t = 1 2 5 3 . 4 3 , p < 0 . 0 1 )$ and security investments $( t = 1 6 1 1 . 4 5 , p < 0 . 0 1 )$ significantly more than those in non-anti-phishing law states. The results corroborate previous research findings that firms with accumulated technology adoption experience can more effectively shorten the learning curve and reduce uncertainty in adopting new technologies [89,90], thereby promoting IT implementation [91,92]. In contrast, firms without experience may hesitate to invest in IT, and the spillover effect is not so promising. Note we are comparing sites of the same firm operating in different states —hence, the major differences are the experience with earlier enact ment of a law and the capabilities nurtured during the process.

## 4.2.2. Robustness tests

We conducted two robustness tests to validate our main findings. First, we utilized a seemingly unrelated regression (SUR) model [93] to take into account that firms’ decision on security investment, and IT investment is correlated instead of being an independent decision. As shown in Panel A of Table 8, all results are consistent with the results in Table 6, except that anti-phishing laws had a positive but not significant effect on multi-state firms’ IT investments. The results indicate a less salient effect on IT investments, and such an effect is less than security investments. One possible reason for this is that firms perceive phishing as an immediate and significant threat, thereby maintaining a focus on specific security measures like encryption, two-factor authentication, or intrusion detection systems. Additionally, the strategy within many firms could be more focused on training existing IT personnel to deal with phishing threats, rather than investing in new technologies. This training might not be captured by IT investments. We further conducted a comparison test to determine whether the differences between the estimated coefficients of the two groups were significant. The results show significant inter-group differences in both security $( t = - 5 2 4 1 . 7 1$ $p < 0 . 0 0 1 )$ ) and IT $( t = - 6 4 0 9 . 7 5 , p < 0 . 0 0 1 )$ ), indicating the laws’ effects on security and IT with respect to single-state firms are smaller than those among multi-state firms.

Concerning potential influences from other cybersecurity regulations on our DID analysis: our thorough review revealed that only Nevada, among control states, enacted a relevant law in 2011 (the same year as Michigan’s Anti-phishing Act), with 11 others doing so within a year before or after. While this might affect the perceived significance of our treatment, it does not undermine our overall findings. To ensure robustness, we conducted an analysis excluding all control states that had introduced any additional cybersecurity laws and regulations dur ing the analysis window. The results from this subsample analysis, presented in Panel B of Table 8, align consistently with those reported in Table 6—except anti-phishing laws had a positive and significant effect on single-state firms’ security investments. This variance suggests that our main results might underestimate the anti-phishing acts’ impact on single-state firms’ security investments. This could be due to othe cybersecurity regulations influencing control group firms. By isolating these confounding factors, we offer a clearer assessment of anti-phishing laws’ effects on such firms’ security investments. Additionally, the comparison test shows multi-state firms increased their security $( t =$ $- 1 6 9 1 . 9 9 , p < 0 . 0 1 )$ and IT investments $( t = - 3 0 3 7 . 9 4 , p < 0 . 0 1 )$ more than single-state firms, which corroborates our main findings.

To construct a more comparable control group, we focused on six states with the closest internet crime complaint rates to each treated state<sup>10</sup> based on the data collected from the Internet Crime Complaint Center [94]. Panel C of Table 8 shows the results of the subsample analysis, and all results are consistent with the results in Table 6—except anti-phishing laws had a negative and not significant effect on multistate firms’ IT investments. This result further emphasizes the distinc tion between the impacts of anti-phishing laws on security measures and broader IT investments, reflecting firms’ prioritization of immediate security threats over general technological enhancements. The com parison test shows multi-state firms increased their security $( t \ =$ $3 0 1 7 . 3 6 , p < 0 . 0 1 )$ and IT investments and IT investments $( t = - 1 5 2 3 . 3 9 , p < 0 . 0 1 )$ more more than single-state firms, which corroborates our main findings.

## 5. Conclusion

Phishing attacks are known to cause severe financial loss [95,96]. Considering cyberattacks, which include phishing, are ubiquitous and difficult to prevent, developing appropriate countermeasures is extremely important. To achieve this goal, all involved parties must cooperate to improve the overall cybersecurity risk landscape. Previous studies mainly highlight the important role of firms in so doing [45,97]. This study extends the discussion by examining the indispensable role of the government in affecting firms' security investment strategies. We find that firms interpret the enactment of cybersecurity-related policies as a signal of the overall threat landscape and adjust their investment strategies accordingly. Furthermore, firms’ interpretations and reactions depend on a firm’s characteristics. Specifically, multi-state operation has positive moderating effects in stimulating proactive strategies, such as increasing investments in both IT and security. We thus enrich the understanding of firms’ security strategies by revealing the interactions between legislative action and firms’ interpretations thereof. Such in sights can inform planning and coordination to ensure successful col lective efforts in the collective fight against cybersecurity risks. Table 9 summarizes the results of the hypothesis testing.

## 5.1. Limitations and future research

This study has several limitations: First, it only considers investments in security and IT. Future researchers could further the discussion by investigating the effects of other non-monetary approaches (e.g., adopting new security or information privacy policies, mandating training), if such data are available. Second, because of the limitations of the data sources, we measured firms’ information security investments according to purchase intentions rather than actual budgets. However, such measurements do not invalidate our analysis because we did not compare security with IT. Additionally, we considered Michigan and Oregon as treatment groups to rule out other state-level legislations, enhancing the validity of our approach at the cost of generalizability. Future researchers could explore these aspects further, broadening the scope of our findings. Third, in this study, we reveal the laws’ signaling effect on the threat landscape. However, because of data limitations, we did not capture the effect of laws as instruments, such as reducing phishing incidents. Future researchers could develop a more compre hensive understanding if such data are available. It would also be interesting to investigate how laws play a mediating role between the threat landscape and firms’ behavior changes, which could provide deeper insights into the complex relationship among legal frameworks, security threats, and organizational responses. Finally, future re searchers could consider analyzing the signaling effect of anti-phishing laws on employees and consumers because end-users are on the front line of phishing deterrence and must work to avoid succumbing to phishing schemes. Previous researchers mainly analyzed employees attitudes toward information security rules implemented within the company [98,99]. Therefore, studying the impact of state and federal laws on employee behavior could provide additional insights into this topic.

Table 8 Robustness tests results.

<table><tr><td rowspan="3">Results</td><td colspan="2">All firms</td><td colspan="2">Single-state firms</td><td colspan="2">Multi-state firms</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td></tr><tr><td colspan="7">Panel A Seemingly Unrelated Regression Estimation</td></tr><tr><td>Antiph × timeD</td><td>0.0205**(0.0040)</td><td>-0.0794**(0.0029)</td><td>-0.0005(0.0043)</td><td>-0.0986**(0.0031)</td><td>0.1287**(0.0120)</td><td>0.0126(0.0083)</td></tr><tr><td>N</td><td>476,440</td><td>476,440</td><td>402,386</td><td>402,386</td><td>74,054</td><td>74,054</td></tr><tr><td colspan="7">Panel B Matched Sample without Enacting Cybersecurity Regulations during the Analysis Window</td></tr><tr><td>Antiph × timeD</td><td>0.1987**(0.006)</td><td>-0.0132**(0.0045)</td><td>0.1913**(0.0076)</td><td>-0.0425**(0.0055)</td><td>0.2749**(0.0115)</td><td>0.0682**(0.0087)</td></tr><tr><td>N</td><td>170,913</td><td>170,913</td><td>130,450</td><td>130,450</td><td>40,463</td><td>40,463</td></tr><tr><td> $R^2$ </td><td>0.084</td><td>0.1135</td><td>0.0803</td><td>0.109</td><td>0.1085</td><td>0.1400</td></tr><tr><td colspan="7">Panel C Matched Sample with Internet Crime Complaints Rate closest to Treated States</td></tr><tr><td>Antiph × timeD</td><td>0.1105**(0.0075)</td><td>-0.0237**(0.0058)</td><td>0.0081(0.0103)</td><td>-0.0793**(0.0075)</td><td>0.2055**(0.0112)</td><td>-0.0039(0.0089)</td></tr><tr><td>N</td><td>112,854</td><td>112,854</td><td>70,376</td><td>70,376</td><td>42,478</td><td>42,478</td></tr><tr><td> $R^2$ </td><td>0.1088</td><td>0.2384</td><td>0.1198</td><td>0.2783</td><td>0.1038</td><td>0.1834</td></tr></table>

Note: Standard errors in parentheses: \* denotes p < 0.05 and \*\* denotes p < 0.01. All analyses include control variables, year dummies, and firm dummies

<table><tr><td colspan="2">Summary of hypothesis results.</td></tr><tr><td>H1a: Anti-phishing laws motivate firms operating in anti-phishing law states to increase security investments.</td><td>Supported</td></tr><tr><td>H1b: Anti-phishing laws motivate firms operating in anti-phishing law states to increase general IT investments.</td><td>NOT Supported</td></tr><tr><td>H2a: Multi-state operation positively stimulates the positive effect of the anti-phishing laws on security investments.</td><td>Supported</td></tr><tr><td>H2b: Multi-state operation positively stimulates the positive effect of the anti-phishing laws on general IT investments.</td><td>Supported</td></tr></table>

## 5.2. Theoretical contributions

Our findings lend support to the argument regarding the positive effect of cybersecurity laws [52] by revealing the laws’ role in raising firms’ awareness of threats. In addition, prior studies primarily inves tigated the effects of cybersecurity laws on firms or attackers that are directly affected by the respective regulations [100,27]. However, the anti-phishing laws we studied are mainly designed to deter attackers; therefore, the reactions we observed from firms—the targets of phishing attacks—demonstrate the indirect effects of such laws. These insights broaden our understanding of the laws’ impacts and contribute to thi body of research.

We further demonstrate that firms’ institutional factors, such as their operational scope, significantly moderate their reactions to antiphishing laws. Our research enriches the literature by revealing that the effect of regulatory changes on IT and security investments is not uniformly distributed but is contingent on a firm’s operational breadth and accumulated experience. Single-state firms adopt a narrow approach by intensifying security measures while curtailing IT in vestments. In contrast, multi-state firms take a more proactive and comprehensive stance by intertwining security with IT investments. This divergence in investment strategies adds depth to the discourse on how a firm’s operational expanse, akin to the concept of threat awareness highlighted by Li et al. [67], is pivotal in informing comprehensive IT and security investment decisions.

This study reveals the intra-firm spillover effects induced by cyber security laws, which complement information security literature on the interfirm spillover effects induced by data breach incidents [42,43]. Our findings demonstrate cybersecurity laws can raise firms’ sensitivity to security threats and drive firms to consolidate their security at the firm level. Such a holistic view of firms’ IT is essential to deter attacks tar geted at the firms’ IT systems’ “weakest links.” This is especially true in light of evidence showing cybersecurity laws induce more attacks on digital assets with little protection (i.e., displacement effects on at tackers) [100,18]. Thus, future researchers could provide further in sights into the reasons behind the different behaviors of firms and attackers.

## 5.3. Practical contributions

We found some firms proactively increase security and IT in vestments in response to the enactment of anti-phishing laws. Moreover, we found some firms, such as single-state firms, become reluctant and reactive in investing in security and IT, possibly due to lack of experi ence and capability in dealing with phishing threats. Previous studies have indicated proactive security investments can improve security performance [97,79], and a reactive approach may hurt firms’ future performance in security and business [35,97]. Meanwhile, it should be noted that arresting phishers is generally difficult [101], partly because attackers are adept at adjusting their tactics according to the changing environment. For example, because of COVID-19, more people work from home, which provides opportunities for attackers and causes an increase in cybercrime [1]. Taken together, these present implications for both policymakers and firms.

Policymakers should pay attention to the diverse effects of proposed policies on all stakeholders. To alleviate undesirable side effects (e.g., discouraging IT investment), policymakers should inform stakeholders (e.g., firms’ senior management) about the latest threats and encourage firms to implement protections against them. In this regard, policy makers can facilitate knowledge- and experience-sharing workshops/ summits to assist inexperienced firms. Firms should recognize the importance of being informed about the practices of peer firms, and the industry as whole, in developing security solutions. Baselining and benchmarking their own practices with respect to others can facilitate a broader perspective of cybersecurity issues.

## CRediT authorship contribution statement

Xiaoxiao Wang: Data curation, Formal analysis. Wilson Weixun Li: Data curation, Formal analysis, Methodology. Alvin Chung Man Leung: Writing – original draft, Writing – review & editing, Conceptu alization, Methodology, Supervision. Wei Thoo Yue: Supervision, Writing – original draft, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Data availability

Data will be made available on request.

## Appendix A. Additional analysis of the moderating effects of risk landscape and IT capability

## A.1. Risk landscape heightens firms’ sensitivity to threats signals

Firms operating in a complex risk landscape are considered to have nurtured a sense of threat, prompting risk reduction [69]. This is evident as they become more vigilant with new technology use when faced with elevated security risks [102]. This heightened attentiveness aligns with previous research that correlates higher risk perception with increased preventive actions [69,103]. With cybersecurity regulations indicating an increased threat level, one would expect such firms to respond more robustly.

Specifically, financial and IT sectors, acknowledged as high-risk for phishing [104], were studied to assess how the risk landscape affects their response to anti-phishing laws. A DID analysis differentiated the responses of these high-risk firms from those in low-risk sectors. Panel A of Table A showed that high-risk firms were prompted by anti-phishing laws to boost security investments substantially $( \beta _ { 1 } = 0 . 2 1 8 1 , p < 0 . 0 1 )$ , yet these laws didn’t significantly change their IT investments $( \beta _ { 1 } = - 0 . 0 0 4 6 , p > 0 . 1 0 )$ . Conversely, low-risk firms raised security investments marginally (β = 0.0067, p < 0.05) but decrease IT investments $( \beta _ { 1 } = - 0 . 0 6 3 1 , p < 0 . 0 1 )$ . Comparative analysis confirmed that high-risk firms outpaced low-risk ones in both security and IT investments (t = 10,556.12 and t = 3956.97 respectively, p < 0.01) than low-risk firms, underscoring that risk perception deeply influences firm responses to legal changes.

The results showed that high-risk firms do not see IT investment as a burden and thus refrain from curtailing their IT budgets. This suggests an understanding of IT’s importance in embedding security measures, although not all such firms can seamlessly merge IT with security in their planning. Facing heightened phishing threats, high-risk firms seem to prefer maintaining their current IT investment while increasing security funding, taking a cautious “wait-and-see” strategy. This reflects an optimistic belief in IT’s facilitation paired with practicality toward threats and regulatory changes.

## Table A

The moderating effects of risk landscape, and IT capability.

<table><tr><td colspan="5">Panel A</td></tr><tr><td rowspan="3">Results</td><td colspan="2">High-risk firms</td><td colspan="2">Low-risk firms</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td></tr><tr><td>Antiph × timeD</td><td>0.2181**(0.0100)</td><td>-0.0046(0.0074)</td><td>0.0067*(0.0034)</td><td>-0.0631**(0.0025)</td></tr><tr><td>N</td><td>76,570</td><td>76,570</td><td>399,870</td><td>399,870</td></tr><tr><td> $R^2$ </td><td>0.1460</td><td>0.1907</td><td>0.1225</td><td>0.2672</td></tr></table>

<table><tr><td colspan="7">Panel B</td></tr><tr><td rowspan="3">Results</td><td></td><td></td><td colspan="2">IT firms</td><td colspan="2">Financial firms</td></tr><tr><td></td><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td></td><td></td><td>Security investment</td><td>IT investment</td><td>Security investment</td><td>IT investment</td></tr><tr><td>Antiph × timeD</td><td>0.2897**(0.0201)</td><td>0.0415**(0.0089)</td><td>0.0897**(0.0074)</td><td>-0.0346*(0.0101)</td><td></td><td></td></tr><tr><td>N</td><td>23,158</td><td>23,158</td><td>53,412</td><td>53,412</td><td></td><td></td></tr><tr><td> $R^2$ </td><td></td><td></td><td>0.3157</td><td>0.3092</td><td>0.2958</td><td>0.1840</td></tr></table>

Note: Standard errors in parentheses: \* denotes p < 0.05 and \*\* denotes p < 0.01. All analyses include control variables, year dummies, and firm dummies.

## A.2. Firms with high IT capability increase investments in both security and IT

Firms with high IT capability are expected to identify and implement suitable solutions against escalating threats. Researchers have found that technology competence positively influences IT adoption [105,106]. Furthermore, increased IT human resources can provide better knowledge to support technology adoption [107.108], and greater technical knowledge can help firms understand how to implement and use IT more effectively ir the organizational context [109]. Therefore, we posit that firms with greater IT capability will proactively respond to anti-phishing laws with heightened security and IT investment.

To assess IT capability’s moderating role, we compared IT firms and financial firms.<sup>11</sup> IT firms will likely have higher IT capability than financial firms. Despite a general increase in investment prompted by anti-phishing legislation, IT firms’ inherent technological orientation may lead to a greater proclivity for adopting new IT measures. We used DID analysis, as with our primary analysis, to measure this effect among control groups from both sectors. Panel B of Table A reveals that post-law, IT firms’ security investments rose $( \beta _ { 1 } = 0 . 2 8 9 7 , p < 0 . 0 1 )$ , and while IT investments grew $( \beta _ { 1 } =$ $0 . 0 4 1 5 , p < 0 . 0 1 )$ , financial firms saw a decline $( \beta _ { 1 } = - 0 . 0 3 4 6 , p < 0 . 0 1 )$ ). Comparative tests show that IT firms enhanced their security $( t = 2 0 0 7 . 1 8 , p$ $< 0 . 0 1 )$ and IT investments $( t = 9 9 1 . 7 5 , p < 0 . 0 1 )$ significantly more than financial firms. This supports the notion that IT capability amplifies the positive influence of anti-phishing laws on both security and IT spending.

The differential impact of anti-phishing laws between IT and financial firms suggests that the former may not change general IT investments due to their lesser expertise in marrying IT and security strategies. Deloitte’s findings corroborate this, indicating a talent gap in cybersecurity within financial firms, which hampers their ability to implement sophisticated cyber defenses [110]. On the other hand, IT-savvy firms might preemptively expand IT outlays to counteract phishing risks, acknowledging IT’s integral role in ensuring security. Hence, the presence of IT capability—rather than the mere existence of a risk landscape—plays a pivotal role in utilizing IT resources to safeguard against phishing threats.

## Appendix B. Comparisons of anti-phishing acts in michigan and oregon

Comparisons of anti-phishing acts in michigan and oregon.

<table><tr><td></td><td>Michigan (Michigan Compiled Laws, Chapter 445. Trade and Commerce § 445.67 A)</td><td>Oregon (Oregon Revised Statutes Trade Regulations and Practices § 646 A.808)</td></tr><tr><td>Definition of Phishing</td><td>(a) Making electronic mail or other communication under false pretenses on behalf of a business without approval, to solicit personal identifying information.(b) Creating or operating a webpage that falsely represents itself as belonging to a business, to solicit personal identifying information.(c) Altering a user&#x27;s computer settings to cause the user to view a false communication associated with a business, to solicit personal identifying information.</td><td>Using a website, electronic mail message, text message, or other electronic means to solicit, request, or induce another person to provide personal information by representing to the other person directly, indirectly, or by implication that the person is a third person, without the third person&#x27;s knowledge, authorization, and consent.</td></tr><tr><td>Enforcement Mechanisms</td><td>Attorney General or Interactive Computer Service Provider: May bring a civil action against a person who has violated the Act.Attorney General: May investigate business transactions if there is reason to believe that a person has violated the section.</td><td>Prosecuting attorney may bring a suit to restrain unlawful practices, approve assurances of voluntary compliance, and seek civil penalties. Court may award attorney fees.</td></tr><tr><td>Penalties</td><td>Actual damages, reasonable attorney fees, or $5000 per violation or $250,000 for each day that a violation occurs.</td><td>Civil penalties up to $25,000 per violation for willful violations of injunctions, assurances of voluntary compliance, or willful use of unlawful methods. Court may award reasonable attorney fees and costs at trial and on appeal.</td></tr></table>

Remark: Our search in Thomson Reuters Westlaw database reveals that the Michigan anti-phishing act (MCL 445.67 A) has been cited on 45 occasions, while the Oregon anti-phishing act (ORS 646 A.808) has been referenced 4 times. These citations appear in various primary legal sources, encompassing Cases, Statutes & Court Rules, Appellate Court Documents, and Trial Court Documents, providing substantial evidence of the acts’ significance and application within the legal landscape. Sources: https://codes.findlaw.com/mi/chapter-445-trade-and-commerce/mi-comp-laws-445-67a https://codes.findlaw.com/or/title-50-trade-regulations-and-practices/or-rev-st-sect-646a-808.html

As shown in Table B, both states have taken legal measures to address phishing by defining and criminalizing the deceptive electronic practices aimed at obtaining personal information. Michigan’s law details specific phishing methods, including false communication and fake webpages, and sets monetary penalties, whereas Oregon’s law broadly focuses on false representation and categorizes phishing as an unlawful trade practice, subject to general trade regulations. The penalties in Michigan are explicitly monetary, whereas Oregon refers to general trade practice regulations.

## Appendix C. A relative time model of pretreatment trends

To strengthen the validity of our analysis, we augmented our dataset with an additional pre-treatment period of IT investment data. This enabled us to employ a relative time model for a more rigorous examination of the parallel trend assumption. Following previous studies [111.112]. the model is specified as follows,

$$
\Upsilon_ {i, t} = \sum_ {\eta = - 3} ^ {0} \beta_ {\eta} P r e _ {\eta} + \sum_ {\eta = - 3} ^ {0} T r e a t _ {i} \times P r e _ {\eta} + \varepsilon_ {i, t},
$$

where $P r e _ { \eta }$ is a dummy variable equals one if the current year is η years prior to the treatment. In our analysis, we designated the year preceding the treatment as the baseline period. We plotted the dynamic effects of the interaction terms with 95% confidence intervals. As shown in the Fig. C1, the coefficients of the variables are not significantly different from zero. That is. there is no evidence of significant differences in the pre-treatment trends between the treatment group and control group, thereby validating the parallel trend assumption for IT investments. Given the unavailability of additional pre-treatment security investment data, we drew inferences about security trends from the observed IT investment patterns. While this approach offers insights, we acknowledge this methodological limitation and advise caution in the interpretation of these inferred security trends.

![](/api/attachments/2VGUNMTN/fulltext/images/5aff81beab3360632601841b500a7166189c145e65b218c0a0890e35ed504f57.jpg)  
Fig. C1. Estimated coefficients of treatment effects on pre-treatment periods.

## References

[1] C. Singleton, S. Carruthers, State of the Phish: IBM X-Force Reveals Current Phishing Attack Trends. https://securityintelligence.com/posts/state-of-the-ph ish-ibm-x-force-reveals-current-phishing-attack-trends/, 2020 (accessed May 4 2020).

[2] Statista, Volume of Successful Phishing Attacks on Businesses Worldwide in 2021. https://www.statista.com/statistics/1149241/share-organizations-worldwi de-phishing-attack/, 2022 (accessed Nov 1st 2022).

[3] Ponemon, The Ponemon 2021 Cost of Phishing Study. https://www.proofpoint. com/us/resources/analyst-reports/ponemon-cost-of-phishing-study, 2021 (accessed Jun 21st 2022).

[4] X. Chen, I. Bose, A.C.M. Leung, C. Guo, Assessing the severity of phishing attacks: a hybrid data mining approach, Decis. Support. Syst. 50 (4) (2011) 662–672.

[5] M. Rothman, Email-Based Threat Intelligence: Industrial Phishing Tactics (New Series). https://securosis.com/blog/email-based-threat-intelligence-industr al-phishing-tactics, 2013 (accessed May 3, 2020).

[6] K. Sheridan, 85% of Data Breaches Involve Human Interaction: Verizon DBIR. https://www.darkreading.com/operations/85–of-data-breaches-involve-human-i nteraction-verizon-dbir/d/d-id/1341012. 2021 (accessed Jun 21st 2022)

[7] J. Vijayan, Phishing Attacks for Initial Access Surged 54% in Q1. https://www. darkreading.com/risk/phishing-attacks-for-initial-access-surged-q1, 2022 (accessed Jun 21st 2022).

[8] M. Sorensen, The New Face of Phishing. https://apwg.org/the-new-face-of -phishing, 2018 (accessed May 4 2020)

[9] D. Brecht, Phishing: Who is being targeted by phishers?. https://resources infosecinstitute.com/topic/who-is-being-targeted-by-phishers, 2019 (accessed January 25 2021).

[10] A. Vishwanath, T. Herath, R. Chen, J. Wang, H.R. Rao, Why do people get phished? Testing individual differences in phishing vulnerability within an integrated, information processing model, Decis. Support. Syst. 51 (3) (2011 576–586.

[11] T. Zhang, T. Havakhor, D. Biros, Does cybersecurity slow down digitization? A quasi-experiment of security breach notification laws, in: Proceedings of the 40th International Conference on Information Systems, Munich, Germany, 2019.

[12] K. Maruri, Which States Have Cybersecurity Task Forces?. https://www.govtech. com/security/which-states-have-cybersecurity-task-forces, 2022 (accessed Oct 15 2023).

[13] S. Peltzman, The effects of automobile safety regulation, J. Polit. Econ. 83 (4)

[14] S.P. Peterson, G.E. Hoffer, The impact of airbag adoption on relative personal injury and absolute collision insurance claims, J. Constr. Res. 20 (4) (1994) 657–662.

[15] N. De Silva, B. Torgler, Smoke Signals and Mixed Messages: Medical Marijuana & Drug Policy Signalling Effects. https://www.econstor.eu/handle/10419/214501, 2011.

[16] E. Bishop, The Art Of Impersonation: Can Your Employees Spot A Spear-Phishing Attack?. https://www.forbes.com/sites/forbestechcouncil/2022/04/08/the-artof-impersonation-can-your-employees-spot-a-spear-phishing-attack/, 2022 (accessed Jun 21st 2022).

[17] E. Chickowski, Why Security Awareness Training Should Be Backed by Security by Design. https://www.darkreading.com/threat-intelligence/why-security-awa reness-training-should-be-backed-by-security-by-design/d/d-id/1339538. 2020 (accessed May 14th 2021).

[18] I.P. Png, C.-Y. Wang, Q.-H. Wang, The deterrent and displacement effects of information security enforcement: international evidence, J. Manag. Inf. Syst. 25 (2) (2008) 125–144.

[19] R. Duguay, M. Minnis, A. Sutherland, Regulatory spillovers in common audit markets, Manag, Sci, 66 (8) (2020) 3389–3411.

[20] L. Zhang, Regulatory spillover and workplace racial inequality, Adm. Sci. Q. 67 (3) (2022) 595–629.

[21] C. Peukert, S. Bechtold, M. Batikas, T. Kretschmer, Regulatory spillovers and data governance: evidence from the GDPR, Mark. Sci. 41 (4) (2022) 318–340.

[22] M. Ashraf, The role of peer events in corporate governance: evidence from data breaches, Account, Rey, 97 (2) (2022) 1–24.

[23] H. Li, S. Yoo, W.J. Kettinger, The roles of IT strategies and security investments in reducing organizational security breaches. J. Manag. Inf. Syst. 38 (1) (2021) 222–245.

[24] R. Murciano-Goroff. Do data breach disclosure laws increase firms' investment in securing their digital infrastructure?. in: Proceedings of 18th Annual Workshop on the Fconomics of Information Security Massachusetts USA Boston, 2019

[25] F. Bisogni, H. Asghari, More than a suspect: an investigation into the connection between data breaches, identity theft, and data breach notification laws, J. Inf. Policy 10 (1) (2020) 45–82.

[26] J. Ju, D. Cho, J.K. Lee, J.H. Ahn, Can it clean up your inbox? Evidence from South Korean Anti-spam, Legislat. Prod. Operat. Manag. 30 (8) (2021) 2636–2652

[27] S. Jackson, N. Vanteeva, C. Fearon, An investigation of the impact of data breach severity on the readability of mandatory data breach notification letters: Evidence from US firms, J. Assoc. Inf. Sci. Technol. 70 (11) (2019) 1277–1289.

[28] J. Tian, L. Xue, S. Cao, Y. Long, Transparency or perception manipulation? A study of it disclosure tone in the context of data breaches, in: Proceedings of the 14th China Summer Workshop on Information Management, Chongqing, China, 2021, pp. 183–194.

[29] M. Ashraf, J.X. Jiang, I.Y. Wang, Are there Trade-Offs with Mandating Timely Disclosure of Cybersecurity Incidents? Evidence from State-Level Data Breach Disclosure Laws. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstrac t id=4068575. 2022

[30] I. Obaydin, L. Xu, R. Zurbruegg, The unintended cost of data breach notification Laws: evidence from managerial bad news hoarding, SSRN (2021), https://doi. org/10.2139/ssrn.3926962.

[31] E. Karanja, J. Zaveri, Ramifications of the Sarbanes Oxley (SOX) act on IT governance, Int. J. Account. Inf. Manag. 22 (2) (2014) 134–145.

[32] W. He, T.W. Tong, M. Xu, How property rights matter to firm resource (2022) 293–310

[33] H. Sakaki. K. Thapar. Trade secrets protection and corporate tax avoidance J. Acco. Fina. 18 (4) (2018) 114–132

[34] K.A. Barton, G. Tejay, M. Lane, S. Terrell, Information system security commitment: a study of external influences on senior management, Comput. Secur, 100 (59) (2016) 9–25.

[35] C. Hsu, J.-N. Lee, D.W. Straub, Institutional influences on information systems

[36] V. Viduto, C. Maple, W. Huang, D. Lopez-Per´ ´ez, A novel risk assessment and optimisation model for a multi-obiective network security countermeasure selection problem, Decis, Support, Syst, 53 (3) (2012) 599–610.

[37] J.L. Spears, H. Barki, User participation in information systems security risk

[38] D. Straub, R. Welke, Coping with systems risk: security planning models for management decision making, MIS Q. 22 (4) (1998) 441–469.

[39] A. Ahmad, K.C. Desouza, S.B. Maynard, H. Naseer, R.L. Baskerville, How integration of cyber security management and incident response enables organizational learning, J. Assoc. Inf. Sci. Technol. 71 (8) (2020) 939–953.

[40] R. Baskerville, P. Spagnoletti, J. Kim, Incident-centered information security: managing a strategic balance between prevention and response, Inf. Manag. 51 (1) (2014) 138–151.

[41] H.R. Yen, W. Wang, C.-P. Wei, S.H.-Y. Hsu, H.-C. Chiu, Service innovation readiness: dimensions and performance outcome, Decis. Support. Syst. 53 (4) (2012) 813–824.

[42] M.S. Islam, T. Wang, N. Farah, T. Stafford, The spillover effect of focal firms cybersecurity breaches on rivals and the role of the CIO: evidence from stock trading volume, J. Account. Public Policy 41 (2) (2021).

[43] A.S. Kelton, R.R. Pennington, Do voluntary disclosures mitigate the cybersecurity breach contagion effect? J. Inf. Syst. 34 (3) (2020) 133–157.

[44] H. Li, S. Yoo, W. Kettinger, The changing tides of investments and strategies and their impacts on security breaches, in: Proceedings of the 40th International Conference on Information Systems, Munich, Germany, 2019.

[45] C.Y. Jeong, S.-Y.T. Lee, J.-H. Lim, Information security breaches and IT security investments: impacts on competitors, Inf. Manag. 56 (5) (2019) 681–695.

[46] P. Garg, Cybersecurity breaches and cash holdings: spillover effect, Financ. Manag. 49 (2) (2020) 503–519.

[47] S. Kashmiri, C.D. Nicol, L. Hsu, Birds of a feather: intra-industry spillover of the target customer data breach and the shielding role of IT, marketing, and CSR, J. Acad. Mark. Sci. 45 (2) (2017) 208–228.

[48] N.J. Freeman, J.C. Sandler, The Adam Walsh Act: a false sense of security or an effective public policy initiative? Crim. Justice Policy Rev. 21 (1) (2010) 31–49.

[50] H. Grant, H. Crowther, How effective are fines in enforcing privacy?, enforcing privacy: regulatory, Legal Technol. Approach. (2016) 287–305.

[51] J. Wolff, N. Atallah, Early GDPR penalties: analysis of implementation and fines through may 2020, J. Inf. Policy 11 (2021) 63–103.

[52] S. Chai, M. Kim, H.R. Rao, Firms’ information security investment decisions: stock market evidence of investors’ behavior, Decis. Support. Syst. 50 (4) (2011) 651–661.

[53] L. Khansa, D. Liginlal, The influence of regulations on innovation in information security, in: Proceedings of the 13th America Conference on Information Systems, Keystone, Colorado, USA, 2007, pp. 180–191.

[54] D.J. Houston, L.E. Richardson, Risk compensation or risk reduction? Seatbelts, state laws, and traffic fatalities, Soc. Sci. Q. 88 (4) (2007) 913–936.

[55] M.G. Aboelmaged, Predicting e-readiness at firm-level: an analysis of technological. organizational and environmental (TOE) effects on e-maintenance readiness in manufacturing firms, Int. J. Inf, Manag, 34 (5) (2014) 639–651.

[57] P.-Y. Chen, G. Kataria, R. Krishnan, Correlated failures, diversification, and information security risk management. MIS O. 35 (2) (2011) 387–422.

[56] S.E. Chang, C.B. Ho, Organizational factors to the effectiveness of implementing information security management. Ind. Manag. Data Syst. 106 (3) (2006) 345-361.

[58] C.W. Hsu, Frame misalignment: interpreting the implementation of information systems security certification in an organization, Eur. J. Inf. Syst. 18 (2) (2009) 140–150.

[59] L. Sun, R.P. Srivastava, T.J. Mock, An information systems security risk assessment model under the Dempster-Shafer theory of belief functions, J. Manag. Inf, Syst, 22 (4) (2006) 109–142

[60] M. Heidt, J.P. Gerlach, P. Buxmann, Investigating the security divide between SME and large companies: how SME characteristics influence organizational IT security investments, Inf. Syst. Front. 21 (6) (2019) 1285–1305

[61] P. Loft, Y. He, H. Janicke, I. Wagner, Dying of a hundred good symptoms: why good security can still fail-a literature review and analysis, Enterprise Inform. Syst. 15 (4) (2021) 448–473.

[62] J. D’Arcy, A. Hovav, D. Galletta, User awareness of security countermeasures and its impact on information systems misuse: a deterrence approach, Inf. Syst. Res. 20 (1) (2009) 79–98.

[63] R. Palanisamy, A.A. Norman, M.L. Mat Kiah, BYOD policy compliance: risks and strategies in organizations, J. Comput. Inf. Syst. (2020) 1–12.

[64] H. Li, W.G. No, J.E. Boritz, Are external auditors concerned about cyber incidents? Evidence from audit fees, Auditing: J. Pract. Theory 39 (1) (2020)

[65] T.C. Herath. H.S. Herath. J. D'Arcy, Organizational adoption of information security solutions: an integrative lens based on innovation adoption and the technology-organization-environment framework, ACM SIGMIS Database: DATABASE Ady, Inform, Syst, 51 (2) (2020) 12–35.

[66] C.M. Angst, E.S. Block, J. D’Arcy, K. Kelley, When do IT security investments matter? Accounting for the influence of institutional factors in the context of healthcare data breaches, MIS O. 41 (3) (2017) 893–916.

[67] W.W. Li, A.C.M. Leung, W.T. Yue, Where is IT in information security? The interrelationship among IT investment, security awareness, and data breaches MIS Q. 47 (1) (2023) 317–342.

[68] L. Argote. B. McEvily. R. Reagans, Managing knowledge in organizations: an integrative framework and review of emerging themes, Manag, Sci. 49 (4) (2003) 571-582.

[69] N T Brewer N D Weinstein C L. Cuite JE Herrington Risk perceptions and their relation to risk behavior, Ann. Behav. Med. 27 (2) (2004) 125–130.

[70] E. Gelbstein, IS audit basics: auditing IS/IT risk management. Part 1. in. ISACA J.

[71] V.Z. Chen, J. Li, D.M. Shapiro, International reverse spillover effects on parent firms: evidences from emerging-market MNEs in developed markets, Eur. Manag. J. 30 (3) (2012) 204–218.

[72] D. Liu, Y. Ji, V. Mookerjee, Knowledge sharing and investment decisions in information security, Decis. Support. Syst. 52 (1) (2011) 95–107.

[73] Y. Chen, L. Che, D. Zheng, H. You, Corruption culture and accounting quality, J. Account. Public Policy 39 (2) (2020) 106698.

[74] T. Homonoff, B. Willage, A. Will´en, Rebates as incentives: the effects of a gym membership reimbursement program. J. Health Econ. 70 (2020) 102285.

[75] R. Santhanam, D. Liu, W.-C.M. Shen, Research note—gamification of technologymediated training: not all competitions are the same, Inf. Syst. Res. 27 (2) (2016) 453–465.

[76] S. Purkait, Examining the effectiveness of phishing filters against DNS based phishing attacks, Inform. Comp. Security 23 (3) (2015) 333–346.

[77] K. Xie, Y.-J. Lee, Social media and brand purchase: quantifying the effects of exposures to earned and owned social media activities in a two-stage decision making model, J. Manag. Inf. Syst. 32 (2) (2015) 204–238

[78] M. Lemmon, M.R. Roberts, The response of corporate financing and investment to changes in the supply of credit, J. Financ. Quant. Anal. 45 (3) (2010) 555–587.

[79] Y. Zhang, C. Zhang, Y. Xu, Effect of data privacy and security investment on the value of big data firms, Decis. Support. Syst, 146 (2021) 113543.

[80] N. Nohria, S. Ghoshal, Differentiated fit and shared values: alternatives for managing headquarters-subsidiary relations, Strateg. Manag. J. 15 (6) (1994) 491–502.

[81] T.C. Ambos, J. Birkinshaw, Headquarters’ attention and its effect on subsidiary performance, Manag. Int. Rev. 50 (4) (2010) 449–469.

[82] P.R. Rosenbaum, D.B. Rubin, Constructing a control group using multivariate matched sampling methods that incorporate the propensity score, Am. Stat. 39 (1) (1985) 33–38.

[83] H.-L. Chang, Y.-C. Chou, D.-Y. Wu, S.-C. Wu, Will firm’s marketing efforts on owned social media payoff? A quasi-experimental analysis of tourism products, Decis. Support. Syst. 107 (2018) 13–25.

[84] J. Schreyogg, ¨ M.M. Grabka, Copayments for ambulatory care in Germany: a natural experiment using a difference-in-difference approach, Eur. J. Health Econ, 11 (3) (2010) 331–341

[85] D.H. Autor, Outsourcing at will: the contribution of unjust dismissal doctrine to the growth of employment outsourcing, J. Labor Econ. 21 (1) (2003) 1–42.

[86] S. He, J. Peng, J. Li, L. Xu, Impact of platform owner’s entry on third-party stores, Inf. Syst. Res. 31 (4) (2020) 1467–1484.

[87] M. Keil, B.C. Tan, K.-K. Wei, T. Saarinen, V. Tuunainen, A. Wassenaar, A crosscultural study on escalation of commitment behavior in software projects, MIS Q. 24 (2) (2000) 299–325.

[88] C.-H. Tan, J. Sutanto, C.W. Phang, A. Gasimov, Using personal communication technologies for commercial communications: a cross-country investigation of email and SMS Jnf Syst, Res, 25 (2) (2014) 307–327

[89] P.-F. Hsu, S. Ray, Y.-Y. Li-Hsieh, Examining cloud computing adoption intention, pricing mechanism, and deployment model, Int. J. Inf. Manag. 34 (4) (2014) 474-488.

[90] B. Ramdani, D. Chevers, D.A. Williams, SMEs’ adoption of enterprise applications: a technology-organisation-environment model, J. Small Bus. Enterp. Dev. 20 (4) (2013) 735–753.

[91] Y. Alshamaila, S. Papagiannidis, F. Li, Cloud computing adoption by SMEs in the north east of England: a multi-perspective framework. J. Enterp. Inf. Manag. 26 (3) (2013) 250–275

[92] B.S. Neo, Factors facilitating the use of information technology for competitive advantage: an exploratory study, Inf. Manag. 15 (4) (1988) 191–201.

[93] S. Dewan, F. Ren, Information technology and firm boundaries: impact on firm risk and return performance, Inf. Syst. Res. 22 (2) (2011) 369–388.

[94] IC3, Internet Crime Complaint Center. https://www.ic3.gov/Home/Annu alReports. 2023 (accessed Aug 1st 2023).

[95] G. Aaron, R. Rasmussen, Global Phishing Survey. https://apwg.org/globalphish ingsurvey, 2017 (accessed Jun 1st 2022).

[96] I. Bose, A.C.M. Leung, Do phishing alerts impact global corporations? A firm value analysis, Decis. Support. Syst. 64 (2014) 67–78.

[97] J. Kwon, M.E. Johnson, Proactive versus reactive security investments in the healthcare sector, MIS Q. 38 (2) (2014) 451–471.

[98] B. Bulgurcu, H. Cavusoglu, I. Benbasat, Information security policy compliance: an empirical study of rationality-based beliefs and information security awareness, MIS Q. 34 (3) (2010) 523–548

[99] M. Siponen, A. Vance, Neutralization: new insights into the problem of employee information systems security policy violations. MIS O. 34 (3) (2010) 487–502

[100] K.-L. Hui, S.H. Kim, Q.-H. Wang, Cybercrime deterrence and internationa legislation: evidence from distributed denial of service attacks, MIS Q. 41 (2) (2017) 497–523.

[101] V.A. Kini, Anti-Phishing Legislation: Catch Me if You Can?. https://www.the globaltreasurer.com/2005/10/03/anti-phishing-legislation-catch-me-if-you-can, 2005 (accessed May 5 2020).

[102] K.A. Salleh, L. Janczewski, Security considerations in big data solutions adoption: lessons from a case study on a banking institution, Proc. Comp. Sci, 164 (2019

[103] L.-C. Chen, D. Farkas, An investigation of decision-making and the tradeoffs involving computer security risk, in: Proceedings of the 15th America Conference on Information Systems, California, USA, San Francisco, 2009, pp. 610–617.

[104] M. Vergelis, N. Demidova, T. Shcherbakova, Spam and phishing in Q2. https://sec urelist.com/spam-and-phishing-in-q2-2021/103548/. 2018 (accessed Jun 21st 2022).

[105] T. Oliveira, M.F. Martins, Understanding e-business adoption across industries in European countries, Ind. Manag. Data Syst. 110 (9) (2010) 1337–1354.

[106] K. Zhu, K.L. Kraemer, J. Dedrick, Information technology payoff in e-business environments: an international perspective on value creation of e-business in the financial services industry. J. Manag. Inf, Syst. 21 (1) (2004) 17–54

[107] H.-S. Kim, Y.-G. Kim, C.-W. Park, Integration of firm’s resource and capability to implement enterprise CRM: a case study of a retail bank in Korea, Decis. Support. Syst. 48 (2) (2010) 313–322.

[108] K. Zhu, K.L. Kraemer, Post-adoption variations in usage and value of e-business by organizations: cross-country evidence from the retail industry, Inf. Syst. Res. 16 (1) (2005) 61–84.

[109] S.K. Lippert, C. Govindarajulu, Technological, organizational, and environmental antecedents to web services adoption, Commun. IIMA 6 (1) (2006) 14.

[110] S. Friedman, Taking Cyber Risk Management to the Next Level. https://www2. deloitte.com/us/en/insights/topics/cyber-risk/cyber-risk-management-financialservices-industry.html, 2016 (accessed Jun 21st 2022).

[111] Z. Li, Y. Hong, Z. Zhang, The empowering and competition effects of the platform based sharing economy on the supply and demand sides of the labor market. J. Manag. Inf. Syst. 38 (1) (2021) 140–165.

[112] Z. Li, C. Liang, Y. Hong, Z. Zhang, How do on-demand ridesharing services affect traffic congestion? The moderating role of urban compactness, Prod. Oper. Manag. 31 (1) (2022) 239–258.

[113] H. Cavusoglu, B. Mishra, S. Raghunathan, The value of intrusion detection systems in information technology security architecture, Inf. Syst. Res. 16 (1) (2005) 28–46.

Xiaoxiao Wang received her Ph.D. from Department of Information Systems in City University of Hong Kong. Her research interests focus on information security, innovation, and firm investment strategy. Her research works were published in the proceedings of PACIS 2019 and presented in BIGS 2019.

Wilson Li is a Lecturer in Department of Information Systems and Business Analytics, Deakin Business School, Deakin University. He received his Ph.D. in Management Infor mation Systems from City University of Hong Kong. His current research focuses on in formation security, data protection and cybersecurity regulation and information systems governance. His research works were published in MIS Quarterly and Internet Research, and presented in academic conferences such as INFORMS. PACIS. WeB and BIGS.

Alvin Leung is an Associate Professor in the Department of Information Systems, City University of Hong Kong. He received his Ph.D. in Information Management from McCombs School of Business, the University of Texas at Austin. His research interests include IT business value, financial technology, technology-mediated learning, and in formation security. His work has appeared in MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Management Science, Decision Support Systems and other journals.

Wei Thoo Yue is a Professor of Management Information Systems in the Department of Information Systems at City University of Hong Kong. He received his Ph.D. in Manage ment Information Systems from Purdue University. Prior to joining City University of Hong Kong, he was a faculty member at the University of Texas, Dallas. His research interests focus on the economic and operational aspects of information security and information systems. His work has appeared in Management Science, Information Systems Research, MIS Quarterly, Journal of Management Information Systems, Decision Support Systems, and other journals.
