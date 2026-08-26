---
otero_id: 15714
otero_key: "SZH5YAVA"
title: "PROACTIVE VERSUS REACTIVE SECURITY INVESTMENTS IN THE HEALTHCARE SECTOR"
authors: "Juhee Kwon; M. Johnson"
year: "2014"
journal: "MIS Quarterly"
doi: "10.25300/misq/2014/38.2.06"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# PROACTIVE VERSUS REACTIVE SECURITY INVESTMENTS IN THE HEALTHCARE SECTOR<sup>1</sup>

Juhee Kwon

Department of Information Systems, College of Business, City University of Hong Kong, Kowloon Tong, HONG KONG {juhee.kwon@cityu.edu.hk}

M. Eric Johnson Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203 U.S.A. {m.eric.johnson@owen.vanderbilt.edu}

This study identifies the effects of security investments that arise from previous failures or external regulatory pressure. Building on organizational learning theory, the study focuses on the healthcare sector where legislation mandates breach disclosure and detailed data on security investments are available. Using a Cox proportional hazard model, we demonstrate that proactive security investments are associated with lower security failure rates. Coupling that result with the economics of breach disclosure, we also show that proactive investments are more cost effective in healthcare security than reactive investments. Our results further indicate that this effect is amplified at the state level, supporting the argument that security investments create positive externalities. We also find that external pressure decreases the effect of proactive investments on security performance. This implies that proactive investments, voluntarily made, have more impact than those involuntarily made. Our findings suggest that security managers and policy makers should pay attention to the strategic and regulatory factors influencing security investment decisions.

Keywords: Security investment, organizational learning, proactive, reactive, healthcare

## Introduction

With the rapid escalation of information security breaches, organizations in every industry have struggled to learn how to defend themselves against an evolving set of threats. In the healthcare sector, protecting patient data—a rich source of personal information—has long been a concern. Thanks to recent federal funding provided by the HITECH Act,<sup>2</sup> more and more patient data is moving into electronic medical records (EMR), and consequently healthcare information security has become a growing public concern. Researchers have documented numerous cases in the United States where criminals, seeking to commit medical or financial identity theft, have maliciously exploited patient data (Johnson 2009; Lohmeyer et al. 2002). The resulting public concern has fueled both federal and state legislation mandating breach notification (Roberds and Schreft 2009; Romanosky et al. 2011). Federal regulations such as HIPAA<sup>3</sup> and HITECH, as well as a menagerie of state regulations, now require healthcare providers to follow various notification guidelines to disclose breaches. Such public notifications are costly and result in negative publicity (Kannan et al. 2007; Kolfal et al. 2010; Wang, Rees, and Kannan 2008). Both legislation and breaches have forced organizations to make security investments.

Our study compares the effects of security investments made in reaction to a breach to others made proactively, as well as investigating how external pressure interacts with the investments. We conduct our analysis in the context of the healthcare sector, which—given its strict breach reporting rules— provides a unique context to investigate the impacts of proactive and reactive security investments.

Effective IT investments have long been a topic of active economics research. However, in the security context, some scholars have argued that security investments, unlike other IT investments, depend on political or regulatory decisions as well as economic decisions (Anderson 2001; Bodin et al. 2005; Rowe and Gallaher 2006; Ryan and Ryan 2005). For example, Anderson (2001) argued that neither technical solutions nor economic markets alone could solve security problems. Rather, more holistic approaches are required that combine technical and economic factors with legal and policy factors. Moreover, accurate inputs to an economic analysis are difficult to estimate because success is “nothing happened,” and thus the potential outcomes (benefits or loss) are often intangible—for example, benefits such as regulatory compliance and public credibility or losses such as brand damage. Consequently, most organizations simply react to breaches and end up spending whatever it takes to solve an existing problem or meet regulatory mandates, rather than undertake a sophisticated economic analysis prior to experiencing a failure (Liberti 2008).

Given these economic, political, and regulatory challenges, organizational perspectives nicely complement economic analysis. Organizational researchers have viewed investments in performance improvement as triggers of organizational learning, promoting organizations to acquire the knowledge and skills necessary to achieve their performance goals (Salomon and Martin 2008; Zollo and Winter 2002). This organizational learning perspective has been used to explain the effects of investments in manufacturing quality improvement, because such improvement often includes unobservable organizational changes (e.g., knowledge acquisition) (Dorroh et al. 1994; Fine 1986; Hatch and Mowery 1998; Ittner et al. 2001; Mukherjee et al. 1998; Salomon and Martin 2008).

Similarly, the improvement of security processes also requires knowledge of evolving attackers’ strategies and everchanging technologies. Thus, with the organizational learning perspective, we can examine the impact of investments on security improvement including unobservable changes in organizational security culture (Culnan et al. 2008; Culnan and Williams 2009). Coupled with an economic perspective, we can evaluate both the learning and the cost effectiveness of security investments.

Further, we examine the public-good nature of information security. In the healthcare sector, organizations often share patient information as patients move between local clinics, small hospitals, tertiary care centers, and long-term rehabilitation centers. Security investments at any point in the healthcare system benefit all players (Appari and Johnson 2009). This makes it possible to study the effects of network externalities stemming from the public good nature of information security. Moreover, HIPAA addresses the interchange of information between organizations by mandating that organizations comply with privacy and security standards. Thus, regulatory pressure is relevant at both the individual organization level and for groups of organizations.

Our study contributes to the literature on information security investments in several ways. First, through an empirical analysis, it provides a deeper understanding of the effects of security investments—both proactive and reactive—on subsequent performance. We demonstrate the different effects of proactive and reactive security investments based on the different types of organizational learning that they facilitate. Second, it identifies the impact of learning from regulatory pressure and the interactions with learning from the different types of security investment. Third, it extends the scope from individual organizations to a regional level (in our case, the state level in the United States). We do so by examining the shared benefit of an individual organization’s investment for all organizations within the same state.

The paper is organized as follows: First, we review relevant theoretical background and then propose our research hypotheses. Next, we describe the research methodology and data collection followed by our results and discussion of the economic effects. Finally, implications and conclusions are presented.

## Theoretical Background

Theoretical analyses on investments fall into two broad categories: organizational and economic. While economic analysis considers investments as the purchase of durable equipment, software, processes, knowledge, etc., in anticipation of favorable future economic returns (Chari et al. 2008; Teisberg 1994; Van Mieghem 1998), organizational analysis considers investments as the quest for improvement in the learning processes for problem-solving heuristics (Carrillo and Gaimon 2000; Ittner et al. 2001; Winter 1994; Zantek et al. 2002).

Security decision makers often rely on qualitative assessments of their security needs (Liang and Xue 2009). Operational researchers have argued that investments in quality improvement are frequently precipitated by failures or external mandates, and the investments result in organizational learning that ultimately yield better quality or performance (Haunschild and Rhee 2004; Ittner et al. 2001; Salomon and Martin 2008). Security researchers also have begun to explore the impact of organizational learning on the relationship between security investment and security performance (Cavusoglu et al. 2008; Herath and Herath 2008; Puhakainen and Siponen 2010).

While prior security literature examined the impact of organizational learning on investment decisions or resource allocation (see Cavusoglu et al. 2008; Smith et al. 2010), our study focuses on antecedent factors (i.e., security failures or external mandates) for security investments and how they and their interaction result in learning that improves security performance. We first categorize security investments as proactive if they occur before any incident and reactive if they occur after an incident (with or without external regulatory pressure). Given that security investments lead to organizational learning through security resource allocation and deployment, the differential effects between proactive and reactive investments likely reside in the difference between their learning effects during the resource allocation and deployment processes. This observation motivated us to investigate whether proactive or reactive security investments perform differently as well as how regulatory pressures affect security performance. Answering these questions will help policy makers and researchers understand the potential impact of new regulation and the value of carrot (investment incentives) versus stick (breach reporting) policies.

We further consider the economic impact of proactive and reactive investments. The security economics literature can be generally segmented into two approaches. One approach, which is based on the cost-effectiveness of investments, tries to answer the question, “How much is saved (or earned) by investing in security?” (Wang, Chaudhury, and Rao 2008). The other approach addresses the question, “How much should be invested?” (Gordon and Loeb 2002). The challenge for either approach is the lack of relevant and applicable data, making it difficult to estimate the monetary costs and benefits of protecting against evolving threats, compromises, and vulnerabilities. Thus, security researchers and practitioners have often used indirect estimation of the financial loss associated with security breaches (HHS 2009; Mulligan and Bamberger 2007) or changes in firm market value resulting from public breach announcements (Cavusoglu et al. 2004; Kannan et al. 2007).

In our case of the healthcare industry, less than 1 percent of healthcare organizations are publicly traded (in the study period, 2005 to 2010),<sup>4</sup> thus estimating the stock market reaction to breaches is not useful. The boards and hospital executives are not focused on maximizing shareholder value. Rather they are focused on their mission related to patients and the community (Appari and Johnson 2009). Of course, they also want to make good technology investments considering the relevant economic trade-offs. Therefore, in our study, we focus on the cost-effectiveness of security decisions by measuring the presence of a collection of security applications and estimating the notification cost of a breach using data on the number of patient records compromised.

## Hypotheses Development

Organizational learning resulting from investments in problem solving, like root cause analysis, enables organizations to discover potential opportunities for shaping a better future (Nonaka 1994). Attewell (1992) argued that investments in advanced technologies are a special category of innovative actions because of the organizational learning burden they impose on employees. Security technologies such as encryption and user authentication impact the workflow processes of employees throughout a healthcare organization. In this environment, where speed and availability of data directly impact patient care, security technologies must be thoughtfully adopted. For example, in our related field research, we have observed cases where poorly implemented authentication technologies were rolled out too quickly, slowing nurse and doctor access to critical patient data—in some cases leading to project failure when the new technology was abandoned. In other cases, where the evaluation and technology rollout process stimulated significant organizational learning, such failures were avoided and significant security performance was achieved.

Although security investments generally provide learning opportunities for all employees through the newly adopted security systems, there have been different views of proactive and reactive investments. Various research has further examined the distinction between proactive and reactive actions (Barth et al. 2010; Ittner et al. 2001; Yue and Cakanyildirim 2007). Commonly, proactive actions are believed to result in different organizational learning occurring from the process of deciding to act (Fine 1986; Li and Rajagopalan 1998), while reactive actions triggered by failures facilitate more remedial learning (Marcellus and Dada 1991). For proactive investments, an organization must make decisions about how and where to invest and deploy security controls. Thus, proactive investments facilitate autonomous learning, which occurs as a by-product of making an investment decision or allocating the investment (Fine 1986; Li and Rajagopalan 1998). Reactive investments give rise to induced learning from failure resolution actions, creating a defense against future failures (Marcellus and Dada 1991).

Consistent with these arguments, the evolving security literature posits that organizational learning influences the link between security investment and security performance. Iheagwara et al. (2004) argue that proactive approaches actively mitigate security risks by examining and analyzing vulnerabilities and threats that might be exploited in the future, while reactive approaches passively carry out postmortem analysis of existing problems. Security practitioners further argue that reactive approaches are not effective in filling the gaps between existing vulnerabilities and future threats because they simply chase existing problems (Kark et al. 2009; Pironti 2005). On the other hand, game-theoretic security researchers argue that reactive policies (quickly learning from past attacks) may be effective enough to discourage rational attackers by focusing efforts on thwarting real attacks and showing agility (Barth et al. 2010; Cavusoglu et al. 2008).

Considering that 22 percent of patient data breaches are related to lost or stolen devices mainly due to negligence (HIMSS 2012), we can expect that both autonomous and failure-induced learning would help healthcare organizations avoid negligence (see Tucker et al. 2007) as well as more serious threats. Thus, despite the mixed theoretical perspectives, we hypothesize that organizational learning from both proactive and reactive investments result in better security performance, implying the following:

H1a. Proactive security investments will result in the reduction of subsequent security failures.

H1b. Reactive security investments will result in the reduction of subsequent security failures.

While testing the association between these two types of security investment and performance will help us better understand investment effectiveness, it is also meaningful to examine the difference between the approaches (it can help illuminate the antecedent factor of an investment).

Advocates of reactive strategies argue that as long as an organization focuses on learning from past attacks instead of simply reacting to the attacks, reactive approaches can be competitive with the best proactive approaches. For example, Barth et al. (2010) demonstrated cases where reactive strategies could out-perform proactive ones when defending against previous or similar incidents. Of course, recovering from repeated failures does not lead to customer satisfaction; however, recovery from a few failures through rapid remedial action typically avoids significant dissatisfaction and in some cases can further build customer confidence (Karande et al. 2007). Haunschild and Sullivan (2002) also provide evidence that the learning associated with failure experiences in manufacturing can allow an organization to cope with future failures more efficiently.

On the other hand, advocates of proactive strategies argue that since proactive approaches don’t rely on failure experiences to discover potential critical or weak points, they require developing a deeper understanding of security vantage points (definition and vision), government and public expectations, perceived security concerns, and determinants of security. These requirements of proactive approaches are typically met using a top-down approach (Frakes and Kang 2005). The target domain (i.e., security) is analyzed, and then controls for the domain are defined and implemented considering foreseeable variations. Such proactive strategies coupled with organizational leadership are believed to be effective in remaining ahead of intelligent adversaries (Kark et al. 2009).

However, from economic perspective, the proactive approach tends to require a large upfront investment—particularly with security because the threat models are constantly evolving, making it difficult to prepare for every possible failure (Rowe and Gallaher 2006). Hence, as Bohme and Moore (2010) found, rather than overinvest proactively, some organizations wait to observe attacks and use this knowledge to better allocate security spending. Bohme and Moore suggest that increasing uncertainty over the weakest links in information security makes it difficult for the organization to know which assets to protect. That uncertainty can lead the organization to decide against security investments until a failure or weak point is realized. Thus in cases with high uncertainty, it may be rational to peruse reactive strategies.

The healthcare industry is generally considered less sophisticated and lags in adoption of the latest information systems and security technologies, as compared to other industries.

This observation supports the conclusion that uncertainty over the weakest links in healthcare may be lower than in other industries with a long history of cyber attacks and defense. Lower uncertainty means that healthcare organizations often have not yet addressed known vulnerabilities that represent weak links. Such a situation favors proactive security investment from both a learning-based approach and costeffectiveness.

Thus, given the low levels of uncertainty about the weakest links (low hanging fruit) across the healthcare sector and the learning benefits of proactive actions, we hypothesize that the effect of proactive investments (and the learning required to understand the uncertainties) should be larger than that of reactive investments.

H2. The effectiveness of proactive security investments on the reduction of subsequent security failures is larger than that of reactive security investments.

It is also important to consider the impact of external mandates, such as government requirements, on investment decisions. Testing the effect of external pressure can identify whether organizations learn better in response to internal initiation or external mandates. Prior literature provides conflicting answers to this question.

Some studies found that external pressures are important for organizational learning because external pressures help an organization explore problems and prevent future failures by providing a baseline with which it should comply (March 1991; Naveh and Marcus 2004; Ocasio 1997). Commonly, they have considered government requirements as the activation of attention that can make organizations focus on a problem area. Since government requirements addressing a failure tend to be well-publicized pressures, organizations may be forced to learn more from these pressures—thus overcoming inertia and stimulating organizational change (Ocasio 1997). March (1991) argues that organizations are apt to engage in exploitation of well-known practices, rather than exploration of new ones. This supports the idea that regulatory pressures can stimulate organizational learning and change. Such regulatory pressures promote learning because they cause organizational members to pay more attention to failures, exploit them more deeply, and work to prevent them in the future.

On the other hand, Haunschild and Rhee (2004) demonstrate that involuntary actions induced from external mandates restrict organizational learning (where performance improvement is a key learning outcome) because the voluntary nature of an organizational activity is better accepted by organizational members and result in more permanent change in routines and practices. They further explain that involuntary recalls result in shallower learning processes, and conclude that organizational volition is important to increase commitment and problem analyses, whereas external pressures likely lead to defensive reactions that rarely help the organization.

Likewise, in security, there has been a very active debate concerning the effectiveness of government regulation with security experts on both sides. Some argue that directive security policy is counterproductive because it pushes firms to reach a certain level of controls regardless of idiosyncratic (IT or security) maturity (Bulgurcu et al. 2010; Zhulei et al. 2008). Thus, regulation may waste firm resources and create a compliance mind-set (check the box) rather than a security mind-set.

Over the last decade, breach notification laws have required organizations to notify the information owners of security breaches. In healthcare, breaches often create unusually strong public reactions because of the private nature of medical information. Breach notification laws create significant organizational pressure, both because of the cost of notification and because of negative press coverage (Mulligan and Bamberger 2007). However, some have argued that such public shaming has done little to help affected patients or improve security. Nevertheless, the cost and the attentiongetting aspects of breach notifications may help overcome organizational inertia and initiate learning by doing when action is taken.

Given the rapidly changing threats and vulnerabilities, today’s security problems are different than last year’s or even last month’s problems. Under this high uncertainty, external regulatory mandates can only show a basic direction for healthcare organizations to make security investments. Accordingly, such external regulatory pressure is likely to draw organizational attention to security breaches, provide critical security guidelines, and result in new organizational processes aimed at reducing future failures. This leads to the following hypothesis:

## H3. External pressure will result in the reduction of subsequent security failures.

In addition to the independent effects of external pressure and investments (both proactive and reactive), there are likely to be interaction effects as well: in particular, interaction between the learning effects of external pressure and investments.

First, regulation-induced learning from external mandates can affect autonomous learning from proactive investments. While the regulatory mandates may effectively grant organizations latitude on how to take actions (Majumdar and Marcus 2001), passive focus on these points may cause organizations to ignore the broader understanding of security that is required for a proactive approach. Since the advantage of proactive investments lies in autonomous learning from deciding how and where to invest, the directive nature of regulatory requirements leads organizations to simply focus on the indicated layers rather than assess security at all operational layers (see Radner and Rothschild 1975; Winter 1981). Therefore, proactive investments under external regulatory pressure may not result in the deep learning required to enable the detection and correction of evolving risks.

Also, regulation-induced learning can influence failureinduced learning from reactive investments. Since, in the case of reactive investments, an organization learns about its weak points from failure experiences rather than examining its vulnerabilities and threats, the investments are more likely to focus on improving the weak points revealed by its failure. In this case the attention, forced or directed by external regulatory mandates, can enhance the depth and width of failureinduced learning. Some researchers have argued that reactive investments are generally targeted toward existing problems, and thus the information provided by government requirements might extend the focus of reactive investments or force organizations to address them more deeply (Rowe and Gallaher 2006; Zollo and Winter 2002). However, the mandated changes from security failures and regulatory mandates are unlikely to result in any type of knowledge that penetrates an organization’s daily operations. Thus, the recurrence of similar problems in the future is likely (Bowie and Jamal 2006).

Given the mixed theoretical support (and the low uncertainty about weakest links in healthcare organizations), we do not have a clear basis for the direction of the regulatory impact. Thus in our study, we test how mandated procedures influence proactive and reactive investments and subsequently security performance (without hypothesizing a positive or negative affect). We hypothesize that

H4a. External pressure influences the effect of proactive security investments on the reduction of subsequent security failures.

H4b. External pressure influences the effect of reactive security investments on the reduction of subsequent security failures.

## Research Methodology

Figure 1 illustrates our research model and the hypotheses discussed in the previous section. We test our hypotheses using a Cox proportional hazard model and conduct t-tests for cost-effectiveness comparisons.

## The Cox Proportional Hazard Model

Our data on security failures and security investment within healthcare organizations includes breach timing and the adoption timing of security controls. This allows us to employ a statistical method that considers the dependence of the organization’s security survival or failure on the explanatory variables. Hazard functions are particularly useful for such analysis, examining the impact of explanatory variables on the timing or probabilities of failure at an organization level. For example, Eliashberg et al. (1997) employed a proportional hazard model to assess the size of a reserve needed by a manufacturer to meet future warrantee claims. Kauffman et al. (2000) adopted a hazard model to test for a market-wide network effect on network adoption. Li et al. (2010) used a Cox model to relate software firms’ capabilities to their failure rates. These studies analyzed “time to events” and explored the effects of a variety of explanatory variables.

Among hazard models, the Cox model includes other attractive features. The model does not depend on distributional assumptions of survival time, provides flexibility for time dependent explanatory variables, and allows the hazard ratio to be defined as the relative risk based on a comparison of event rates. In particular, information security requires large capital expenditures and significant ongoing maintenance costs, because security features quickly grow obsolete as needs evolve with changing attacker strategies or technologies. Therefore, we employ the Cox model to examine the relative association between the effects of explanatory variables (i.e., security investment and external pressure) and subsequent security failures.

## Research Model

The hazard function, h(t), refers to the failure rate of a subject per unit of time (t). The model assumes that the elapsed time to fail, T, is conditional on the explanatory variables. In our study, T measures the time from investment until either the event of interest—security failure—occurs or the end of the observation period. Thus, our hazard ratio represents the relative risk of security failures within a time unit (where the time unit is one month). The Cox model is expressed as

![](/api/attachments/SZH5YAVA/fulltext/images/f1001459b4ed098626844ead0ecbe06e3db1c292aa12f6088a55a84e1446fed2.jpg)  
Figure 1. Conceptual Framework

$$
h _ {i} (t) = h _ {0} (t) e ^ {\sum_ {j = 1} ^ {K} \beta_ {j} x _ {i j}}
$$

where $\beta _ { j }$ is a vector of regression parameters to be estimated for $j \ = \ 1 , . . . , \ K .$ The baseline hazard function $h _ { 0 } ( t )$ corresponds to the case where $x _ { j } = 0$ , involving time but not explanatory variables. The second component is the exponential functions with the sum of $\beta _ { j } x _ { i j } ,$ which involves explanatory variables but not time at an organization i. The model is referred to as a semi-parametric model since one part of the model involves the unspecified baseline function over time and the other part involves a finite number of regression parameters (Cox 1972). The semi-parametric Cox model is flexible and robust because it does not require assumptions about the baseline distribution.

The hazard ratio, or relative hazard, indicates the expected change in the risk of the terminal event from zero to one when x changes. If the hazard ratio is one, x has no effect. If the hazard ratio is greater than one, x is associated with the increased probability of failure, and vice versa.

$$
\frac {h _ {i} (t)}{h _ {0} (t)} = e ^ {\sum_ {j = 1} ^ {K} \beta_ {j} x _ {i j}}
$$

Cox regression coefficients $\beta _ { j }$ are estimated by partial likelihood (L), which is determined by the product of individuals’ failure risks at each time (t). The failure likelihood of each individual is the hazard ratio, $h _ { i } ( t )$ , of an individual (i) divided by the hazard, $h _ { i } ^ { c } ( t )$ , of all the other organizations (R ) (May et al. 2008).

$$
L (t) = \prod_ {i = 1} ^ {N} \frac {h _ {i} (t)}{h _ {i} ^ {c} (t)} = \prod_ {i = 1} ^ {N} \frac {e ^ {\left(\beta_ {1} x _ {1 i} + \dots + \beta_ {k} x _ {k i}\right)}}{\sum_ {l \in R _ {i}} e ^ {\left(\beta_ {1} x _ {1 l} + \dots + \beta_ {k} x _ {k l}\right)}}
$$

Most commonly, this examination entails the specification of a linear-like model for the log hazard. The Cox model maximizes the log-likelihood function (LL) with respect to the parameters of interest, $\beta _ { j }$

$$
\begin{array}{l} L L (t) = \sum_ {i = 1} ^ {N} \left(h _ {i} (t) - h _ {i} ^ {c} (t)\right) \\ = \sum_ {i = 1} ^ {N} \beta_ {i} \left(x _ {i} - x _ {l} ^ {c}\right) = \beta_ {0} + \beta_ {1} \hat {x} _ {1 l} +... \beta_ {k} \hat {x} _ {k l} \end{array}\tag{1}
$$

Generalizing the above equation, our Cox model examines the effects of security investment and external regulatory pressure on the time until security failures.

## Self-Selection and Strategic Decisions: Accounting for Endogeneity

It is well known that organizational strategy self-selection complicates the empirical estimation of strategy performance, since an organization’s propensity to make strategic decisions may be endogenously determined (Greene 1981; Susarla and Barua 2011). Failing to account for endogeneity in organizational performance could lead to potentially misspecified and biased results (Greene 2003). In our study, there may be inherent differences between organizations that proactively invested and those that did not. For instance, those organizations that proactively invested might have better resources, IT budget or technological expertise than those that did not.

In order to account for endogeneity, we use a two-step econometric procedure proposed by Heckman (1979). Shaver (1998) extended the Heckman correction and showed that accounting for strategy self-selection changes the interpretation of how entry mode choice affects a firm’s direct investment survival, distinguishing between greenfield entry and entry via acquisition. Following Shaver, we use a probit model to estimate the probability that an organization proactively makes a security investment as a function of resources, IT budget, or technological expertise. Proactive<sup>\*</sup><sub>i</sub> is defined as the difference in the expected performance of proactive and reactive investments.

$$
\text { Proactive } _ {i} ^ {*} = \gamma^ {\prime} w _ {i} + u _ {i}, \text {   such   that   }\tag{2}
$$

$$
\text { Proactive } _ {i} ^ {*} = 1 \text {   if   } \text { Proactive } _ {i} ^ {*} > 0, 0 \text {   otherwise }
$$

Proactive is the binary variable that indicates whether an investment is proactively made or not. The error term, $u _ { i }$ is attributable to unobservable characteristics that affect proactive decisions. $u _ { i }$ captures effects that would be included in the explanatory variables, $w _ { i } ,$ but cannot be measured. With respect to proactive decisions, Sinha and Noble (2008) argued that organizations proactively adopt technology when they possess larger IT budgets and better technological expertise. Some measurable factors for $w _ { i }$ such as IT budget and IT fulltime employees are included in the proactive decision model. We rewrite Equation (1) and (2) as follows:

$$
L L (t) = \beta_ {0} + \beta_ {1} \hat {x} _ {1 l} +... + \beta_ {k} \hat {x} _ {k l} + \delta P r o a c t i v e _ {i} + \in_ {i}\tag{3}
$$

where $x _ { i }$ includes explanatory variables that affect survival, $L L ( t )$ , and $\epsilon _ { i }$ is an error term that is normally distributed with zero mean and variance $\sigma _ { \epsilon } ~ \epsilon _ { i }$ represents unobservable characteristics that influence survival from failures. If unobservable effects captured in $\epsilon _ { i }$ are the same as in $u _ { i }$ from (2), then $\epsilon _ { i }$ and $u _ { i }$ will be correlated. For example, with respect to investment performance, regardless of whether an investment is proactively made or not, one would expect an organization with better practices, such as security training, or policies to outperform organizations lacking these practices. Therefore, $\epsilon _ { i }$ and $u _ { i }$ will have correlation $( \rho )$ unless these factors can be measured and included in $x _ { i \cdot }$ . Without addressing the potential endogeneity of the investment decision, the hazard model will lead to biased estimates of δ (Heckman 1979; Shaver 1998). The treatment model controls for potential endogeneity, nonzero $\rho ,$ and the final model can be specified as

$$
L L (t) = \beta^ {\prime} X _ {i} + \delta P r o a c t i v e _ {i} + \beta_ {\lambda} \lambda_ {i} + \zeta
$$

$$
\text {   Where   } \lambda_ {i} = \phi (\gamma^ {\prime} w _ {i}) / \Phi (\gamma^ {\prime} w _ {i}) \text {   if   } P r o a c t i v e _ {i} = 1,\tag{4}
$$

$$
\lambda_ {i} = - \phi (\gamma^ {\prime} w _ {i}) / \{1 - \Phi (\gamma^ {\prime} w _ {i}) \text {   if   } P r o a c t i v e _ {i} = 1
$$

where, $\phi$ and Φ are the probability density function and cumulative distribution function of the standard normal distribution, respectively.

## Empirical Analysis

## Data Sources

We employed data from the Healthcare Information and Management Systems Society (HIMSS) Analytics™ Database<sup>5</sup> from 2005 to 2009. The database provides information about the adoption of health information technologies—EMR and security applications—in healthcare organizations. Our focus was data on the adoption of specific security applications such as encryption and user authentication. It also includes various descriptive variables, which we used as control variables such as the size of a healthcare organization, location, academic status, and so on. The data have been widely used in previous studies to examine the impact of healthcare information systems (Angst and Agarwal 2009; Hillestad et al. 2005; Miller and Tucker 2009). For the period 2005–2009, we initially gathered data on 4,487 organizations. Of these, 2,101 were dropped because of missing data, and thus our final sample includes 2,386 organizations. To determine whether our sample is representative of all organizations in the healthcare industry, we compared the sample with all organizations on several measures (bed size, IT equipment, security investment, and revenue) by conducting two-sample t-tests. The t-tests indicated that all p-values are larger than 0.1. Thus, we cannot reject the null hypothesis that the two sample means are the same on each measure and conclude that the healthcare organizations in our study are representative of the healthcare industry.

Next, we matched the sample data with 281 reported healthcare security breaches from January 2005 to June 2010. The trend of all reported breaches is plotted in Figure 2. We employed three sources to obtain information breaches: Health & Human Services (HHS),<sup>6</sup> Identity Theft Resource Center (ITRC),<sup>7</sup> and Data Loss Database.<sup>8</sup>

![](/api/attachments/SZH5YAVA/fulltext/images/c491794238f134c545f1c477c3120eb2b26250f0797daca9204335e44abf5d6d.jpg)

<table><tr><td></td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td></tr><tr><td>- ◆ - Internal failures</td><td>4</td><td>21</td><td>22</td><td>13</td><td>12</td><td>13</td></tr><tr><td>accidental disclosure</td><td>3</td><td>11</td><td>9</td><td>9</td><td>5</td><td>9</td></tr><tr><td>malicious insiders</td><td>1</td><td>10</td><td>13</td><td>4</td><td>7</td><td>4</td></tr><tr><td>External failures</td><td>14</td><td>29</td><td>34</td><td>40</td><td>31</td><td>48</td></tr></table>

Note: 234 organizations experienced at least one breach from 2005 to 2010.  
Figure 2. The Trend of Data Breaches in Healthcare

## Variable Definitions

## Proactive Decision Model

As shown in Equation (2), Proactive is the dependent variable in the proactive decision model. Proactive takes a value of one when an organization makes a security investment without any breach in its affiliated group within one prior year; otherwise zero. Healthcare organizations are often affiliated with a group that consists of a main organization named as parent and other suborganizations affiliated to the parent. Given this structure, if an organization made a security investment within one year after any member of its group experienced a breach, it is a reactive investment, and thus Proactive has a value of zero. For instance, if a hospital has a data breach in year 1 and then another in year 4, its security investment in year 3 is considered proactive. However, if the investment occurs in year 2, it is a reactive investment.

In addition, we distinguish whether post-incident investments were reactions to breaches or were already planned prior to breaches. The HIMSS database indicates whether the adoption of security applications is planned for a specific year. If an organization experienced a data breach while planning a security investment at year t-1 and then carried out the plan in year t, Proactive is coded as one, not zero. Alternatively, if this organization makes an additional security investment in year t without any plan in year t-1, the investment is categorized as a reactive investment. Further, we are interested in the full deployment of security controls. HIMSS helps us here as it uses a rolling survey approach each year, providing dates when they observe that a new system becomes “current.” So to be conservative, we used the date when the system is shown to be in use (thus implemented). If a breach occurs after that date, the investment is coded as “proactive” (Proactive = 1), otherwise “reactive” (Proactive = 0). If more than one breach occurs within a year after making an investment, the survival time is the duration from the updated investment time to the first breach time. Table 1 illustrates how we coded the survival or death of proactive and reactive investments.

The set (w ) of independent variables are factors identified in other studies as likely to affect a proactive investment decision (but not a data breach). With respect to proactive and reactive IT investment decisions, strategy researchers have argued that organizations rely on their resources as drivers effectively determining the strategy that each organization will use to approach investment decisions (Ho et al. 2011; Sinha and Noble 2008). Likewise, in the security context, important resources such as capital (IT-budget) and employees (IT-FTE) (prior to investment) allow firms to proactively adopt security applications (Chen et al. 2011). Controlling for an organization’s overall financial resources with its annual revenue (Revenue), we employed IT-budget as the total amount budgeted by the IT department, and IT-FTE as the total number of IT full-time employees.

## Hazard Model

The security performance we measure is survival from security failure—it takes on a value of one if an organization has a data breach after a security investment, zero otherwise. The survival duration is modeled as the length of time that an organization remains free of breaches (in months). Table 1 shows the possible cases of survival or death. We further separately investigate security failures from inside and outside an organization. Internal failure takes a value of one with a data breach from inside the organization, while external failure takes a value of one with a data breach from outside the organization. The distinction is often important because the technologies to prevent internal and external failures can be different and the risks related to misuse of breached data are different.

<table><tr><td colspan="2">↓: Proactive ↑: Reactive x: A breach x: A breach in an affiliated group ↔: Survival (or death)</td></tr><tr><td></td><td>(1) and (2) proactive investments and no breach</td></tr><tr><td></td><td>(3) and (4) proactive investments and two breaches (the first breach is only considered for survival time)</td></tr><tr><td></td><td>(5) and (6) proactive investments and two breaches in a year (the first breach is only considered for survival time)(7) reactive investment and no breach</td></tr><tr><td></td><td>(8) reactive investment and a breach(9) proactive investment (a breach before one year) and no breach</td></tr><tr><td></td><td>(10) reactive investment and a breach(11) reactive investment and no breach</td></tr><tr><td></td><td>(12) and (13) reactive investments with a breach in a year and a subsequent breach(14) proactive investment and a breach</td></tr></table>

For security investment, we counted the number of security applications that have been adopted. HIMSS provides data on the adoption of antivirus, encryption, firewall, intrusion detection, user authentication, and spam filter. These data are examined in three ways: Total, Proactive, and Reactive Inv. The terms proactive and reactive depend on organizations decisions based on whether the decisions are responding to a prior breach, rather than the functionalities. We examined the distribution of security controls for proactive and reactive investments (see Appendix A). Our comparison shows that there is little difference between the types of security controls for proactive and reactive investment. It also shows similar patterns with/without state laws. In some instances, we can see some small differences—for example, proactive investments seem to favor firewalls while reactive investments seem to favor authentication. Overall, the differences seem slight, indicating that there is no specific investment pattern or size differences between reactive and proactive.

As external pressure, state breach notification laws (Law) are incorporated into our models. Data on state legislation over the observation period were collected from the National Conference of State Legislatures (NCSL).<sup>9</sup> Total affected is employed to examine cost-effectiveness of security investment. This variable reports the number of affected patients by a breach.

Control variables include IT equipment, licensed bed size, and academic and hospital type. IT equipment is the number of computer/laptops operated, and this variable represents the level of an organization’s EMR adoption. Bed size is the number of licensed beds, which has been widely used to represent a healthcare organization’s size and available resources. Academic and hospital are dummy variables used to describe organization type. If an organization includes an academic institute, academic was set to one; otherwise zero. Hospital was set to one if the organization is an acute care hospital, while zero includes all other types such as subacute, ambulatory, and integrated delivery systems (IDS). Years (2005 to 2010) were coded as dummy variables, which have a value of one for a particular year and zero otherwise.

To examine the network effects of security investment at the state level, we aggregated by organization type (e.g., academic), the proactive and reactive investments, bed size, IT equipment, IT-budget, IT-FTE, and revenue as an extended organization for every observed event time (i.e., investment time (mm/yyyy), breach time (mm/yyyy)) in the dataset.

Table 2 provides descriptive statistics for the variables in our models. With the defined variables, we can describe the following empirical models based on Equation (4):

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Model (1)

$LL(t) = \beta_{1,0} + \beta_{1,1} Total\ Inv_i + \beta_{1,2} Law_i$ $+ \beta_{1,3}(Law_i \times Proactive_i) + \beta_{1,4}(Law_i \times Total\ Inv_i)$ $+ \delta Proactive_i + \beta_{1,\lambda} \lambda_i + \beta_{1,5} IT\ equipment_i + \beta_{1,6} Bed\ size_i$ $+ \beta_{1,7} Academic_i + \beta_{1,8} Hospital_i + \sum_y \beta_{1,9y} Years_{iy} + \zeta_1$

Model (2)

$LL(t) = \beta_{2,0} + \beta_{2,1} Proactive\ Inv_i + \beta_{2,10} Reactive\ Inv_i$ $+ \beta_{2,2} Law_i + \beta_{2,11}(Law_i \times Proactive\ Inv_i)$ $+ \beta_{2,12}(Law_i \times Reactive\ Inv_i) + \beta_{2,\lambda} \lambda_i + \beta_{2,5} IT\ equipment_i$ $+ \beta_{2,6} Bed\ size_i + \beta_{2,7} Academic_i + \beta_{2,8} Hospital_i$ $+ \sum_y \beta_{2,9y} Years_{iy} + \zeta_2$
</div>

## Results

First, we assessed the correlations between the explanatory variables of our models. Table 3 displays the correlation matrix with the tolerance (Tol) values and the variance inflations (VIFs). Most of the correlations among the variables show low values, and multicollinearity diagnostics exhibit tolerance values between 0.18 and 0.97, which are above the common cutoff threshold of 0.1 (Hair et al. 2005). The VIFs of all variables are less than 5.54. A usual threshold of VIFs is 10.0, which corresponds to a tolerance of 0.1. Therefore, the multicollinearity is not a concern for our models.

To estimate the effects of proactive and reactive investment on survival, we employed Heckman’s (1979) method as previously described. First, we predicted and saved the value for the correction of self-selection (λ) using a probit model, and then the Cox proportional hazard was evaluated with the correction (λ) as a control variable to estimate hazard rates with security investment and other explanatory variables. As shown in Equation (2), the vector $w _ { i }$ includes logs of IT full-time employees and IT budget, controlling with revenue. At the organization level, more IT employees (0.002 at $p <$ $\phantom { - } 0 . 0 I )$ and budget (1.223 at $p < 0 . 0 I )$ lead to more proactive decisions. Likewise, in a state, IT employees (0.103 at $p <$ $\phantom { - } 0 . 0 I )$ and IT budgets (0.120 at $p < 0 . 0 I )$ are significantly associated with organizations’ proactive investment decisions.

Next, we ran the hazard model from Equation (4) to evaluate organization-specific variables (X ) as determinants of survival from security failure. The analyses were performed by Models (1) and (2) on two levels: organization level and state level. While Model (1) tests the effect of total security investments across all our analyses, Models (2) separately investigates the effects of proactive and reactive security investments.

Table 4 presents the estimates of the parameters $( \beta _ { j , \lambda } )$ and hazard rates, h(t) for the models. H1a and H1b argue that proactive and reactive security investments reduce the subsequent security failures of an investing organization. We first tested the total investment in Model (1) and found that investment is associated with decreases in subsequent security failures (–0.304 at ${ \cdot } p { < } 0 . 0 1 )$ with a hazard rate $( h ( t ) = 0 . 7 3 7 )$ Next, we separately examined proactive and reactive investments in Model (2). The estimation supports H1a with a negative coefficient (–0.763 at $p < 0 . 0 I )$ for proactive investments, but it does not support H1b. Note that proactive investment has a hazard rate of 0.466 (less than one). This observation implies that proactive investments reduce the likelihood of a security failure by about 53.4 percent, while reactive investments do not have any significant effect on security failures.

To further investigate the social effects from security investments, we conducted the same analysis at the state level. As Table 4 shows, the state-level analysis significantly supports both H1a and H1b with –1.272 (p < 0.01, h(t) = 0.280) and $- 0 . 9 5 3 \left( p < 0 . 0 1 , h ( t ) = 0 . 3 8 6 \right) .$ , respectively. While reactive investments do not have any significance at the organization level, they are significantly associated with reduced subsequent security failures at the state level. Comparing the coefficients suggests that proactive investments reduce subsequent security failures more than reactive investments at both levels. In addition, the magnitude of proactive investments becomes larger at the state level than the organization level (72.0% versus 53.4% in reduction). The effect of total investments also results in less security failures at the state level $( \beta _ { 1 } \mathrm { = } \mathrm { - } 0 . 5 1 2 \mathrm { a t } p \mathrm { < } 0 . 0 1 , h ( t ) = 0 . 5 9 9 )$ than at the organization level $( \beta _ { 1 } = - 0 . 3 0 4$ at $p < 0 . 0 1$ , h(t) = 0.737) (40.1% versus 26.3% in reduction).

<table><tr><td colspan="6">Table 2. Descriptive Statistics for Variables</td></tr><tr><td>Variable</td><td>Description</td><td>Mean</td><td>StdD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">The  $1^{st}$  Stage: Variables (for Proactive Decision Model)</td></tr><tr><td>Proactive</td><td>1 if a security investment occurs without a breach experience within a previous year, otherwise 0.</td><td>0.43</td><td>0.49</td><td>0.00</td><td>1.00</td></tr><tr><td>Revenue</td><td>Log(annual revenue)</td><td>20.01</td><td>2.10</td><td>14.52</td><td>24.36</td></tr><tr><td>IT-FTE</td><td>Log (IT Full-Time Employees)</td><td>2.38</td><td>1.48</td><td>-1.39</td><td>8.29</td></tr><tr><td>IT-Budget</td><td>Log(IS Budget)</td><td>0.03</td><td>0.08</td><td>0.00</td><td>1.23</td></tr><tr><td colspan="2">The  $2^{nd}$  Stage: Variables (for Hazard Model)</td><td></td><td></td><td></td><td></td></tr><tr><td>Security failure</td><td>1 if a breach occurs at year t, otherwise 0.</td><td>0.09</td><td>0.28</td><td>0.00</td><td>1.00</td></tr><tr><td>Internal</td><td>1 if a beach maliciously or accidentally occurs from inside an organization; otherwise 0</td><td>0.03</td><td>0.16</td><td>0.00</td><td>1.00</td></tr><tr><td>External</td><td>1 if a breach occurs from outside an organization; otherwise 0</td><td>0.06</td><td>0.24</td><td>0.00</td><td>1.00</td></tr><tr><td>Survival Time</td><td>The length of time (months) that an organization remains without any breach.</td><td>18.13</td><td>13.95</td><td>1.00</td><td>65.00</td></tr><tr><td>Total inv.</td><td>The number of IT security controls implemented at different layers.</td><td>1.54</td><td>2.10</td><td>0.00</td><td>6.00</td></tr><tr><td>Proactive Inv.</td><td>The number of security investments without a breach experience within a previous year.</td><td>1.18</td><td>1.92</td><td>0.00</td><td>6.00</td></tr><tr><td>Reactive Inv.</td><td>The number of security investments with a breach experience within a previous year.</td><td>0.35</td><td>1.23</td><td>0.00</td><td>6.00</td></tr><tr><td>Law</td><td>1 if a state has breach notification laws, otherwise 0</td><td>0.89</td><td>0.30</td><td>0.00</td><td>1.00</td></tr><tr><td colspan="6">Control variable</td></tr><tr><td>IT equipment</td><td>Log (the number of computers and laptops operated)</td><td>3.58</td><td>1.61</td><td>0.00</td><td>8.00</td></tr><tr><td>Bed size</td><td>Log (the number of licensed beds)</td><td>5.04</td><td>1.01</td><td>1.79</td><td>7.47</td></tr><tr><td>Academic</td><td>1 if the organization is academic, otherwise 0</td><td>0.07</td><td>0.26</td><td>0.00</td><td>1.00</td></tr><tr><td>Hospital</td><td>1 if the organization is an acute-care hospital, otherwise 0</td><td>0.92</td><td>0.27</td><td>0.00</td><td>1.00</td></tr><tr><td>Years</td><td>Dummy variables for each year between 2005 and 2010</td><td>-</td><td>-</td><td>0.00</td><td>1.00</td></tr></table>

Table 3. Correlation Matrix

<table><tr><td colspan="2">Variable</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>Tol</td><td>VIFs</td></tr><tr><td>1.</td><td>Total Inv.</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-</td><td>-</td></tr><tr><td>2.</td><td>Proactive Inv.</td><td>0.64</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.53</td><td>1.88</td></tr><tr><td>3.</td><td>Reactive Inv.</td><td>0.23</td><td>-0.61</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.48</td><td>2.07</td></tr><tr><td>4.</td><td>Law</td><td>-0.06</td><td>-0.06</td><td>0.09</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.97</td><td>1.03</td></tr><tr><td>5.</td><td>IT Equipment</td><td>0.02</td><td>0.09</td><td>0.05</td><td>0.04</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td>0.38</td><td>2.61</td></tr><tr><td>6.</td><td>Bed Size</td><td>0.01</td><td>0.01</td><td>0.09</td><td>0.03</td><td>0.68</td><td>1.00</td><td></td><td></td><td></td><td></td><td>0.18</td><td>5.54</td></tr><tr><td>7.</td><td>Academic</td><td>0.01</td><td>-0.01</td><td>0.06</td><td>0.02</td><td>0.32</td><td>0.30</td><td>1.00</td><td></td><td></td><td></td><td>0.81</td><td>1.23</td></tr><tr><td>8.</td><td>Hospital</td><td>0.10</td><td>0.27</td><td>-0.13</td><td>0.04</td><td>-0.05</td><td>-0.08</td><td>0.08</td><td>1.00</td><td></td><td></td><td>0.93</td><td>1.08</td></tr><tr><td>9.</td><td>Revenue</td><td>-0.07</td><td>-0.06</td><td>0.00</td><td>0.03</td><td>0.28</td><td>0.31</td><td>0.09</td><td>-0.33</td><td>1.00</td><td></td><td>0.51</td><td>1.98</td></tr><tr><td>10.</td><td>IT-FTE</td><td>0.09</td><td>0.04</td><td>0.07</td><td>0.09</td><td>0.75</td><td>0.78</td><td>0.42</td><td>-0.08</td><td>0.26</td><td>1.00</td><td>0.27</td><td>3.74</td></tr><tr><td>11.</td><td>IT-Budget</td><td>0.02</td><td>0.01</td><td>0.00</td><td>0.02</td><td>-0.02</td><td>-0.06</td><td>-0.01</td><td>0.04</td><td>0.13</td><td>-0.01</td><td>0.93</td><td>1.08</td></tr></table>

Note: Bold represents statistically significant correlation coefficients with p < 0.05.

<table><tr><td colspan="9">Table 4. Hazard Model Results</td></tr><tr><td rowspan="3">Independent Variable</td><td colspan="4">Organization</td><td colspan="4">State</td></tr><tr><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td></tr><tr><td>Total Inv.</td><td>-0.304***(0.093)</td><td>0.737</td><td></td><td></td><td>-0.512***(0.094)</td><td>0.599</td><td></td><td></td></tr><tr><td>Proactive Inv.(H1a)</td><td></td><td></td><td>-0.763***(0.141)</td><td>0.466</td><td></td><td></td><td>-1.272***(0.188)</td><td>0.280</td></tr><tr><td>Reactive Inv.(H1b)</td><td></td><td></td><td>-0.110(0.091)</td><td>0.896</td><td></td><td></td><td>-0.953***(0.197)</td><td>0.386</td></tr><tr><td>Proactive (H2)</td><td>-0.885***(0.298)</td><td>0.413</td><td></td><td></td><td>-1.963***(0.301)</td><td>0.140</td><td></td><td></td></tr><tr><td>Law (H3)</td><td>-1.357***(0.173)</td><td>0.258</td><td>-1.250***(0.189)</td><td>0.287</td><td>-1.137***(0.284)</td><td>0.321</td><td>-0.728***(0.258)</td><td>0.483</td></tr><tr><td>Proactive × Law</td><td>0.316(0.357)</td><td>1.256</td><td></td><td></td><td>0.745**(0.304)</td><td>2.107</td><td></td><td></td></tr><tr><td>Total Inv. × Law</td><td>0.295***(0.100)</td><td>1.234</td><td></td><td></td><td>0.102*(0.058)</td><td>1.108</td><td></td><td></td></tr><tr><td>Proactive Inv. × Law(H4a)</td><td></td><td></td><td>0.351**(0.158)</td><td>1.421</td><td></td><td></td><td>0.224***(0.081)</td><td>1.252</td></tr><tr><td>Reactive Inv. × Law(H4b)</td><td></td><td></td><td>0.122(0.101)</td><td>1.130</td><td></td><td></td><td>0.096(0.079)</td><td>1.101</td></tr><tr><td colspan="9">Controls</td></tr><tr><td>Correction for self-Selection (I)</td><td>-1.696***(0.386)</td><td>0.183</td><td>-1.541***(0.389)</td><td>0.214</td><td>-1.236***(0.458)</td><td>0.291</td><td>-1.630***(0.503)</td><td>0.196</td></tr><tr><td>IT equipment</td><td>-0.023(0.055)</td><td>0.977</td><td>-0.035(0.056)</td><td>0.966</td><td>-0.060(0.064)</td><td>0.941</td><td>-0.023(0.063)</td><td>0.977</td></tr><tr><td>Bed size</td><td>-0.116(0.067)</td><td>0.890</td><td>-0.094(0.065)</td><td>0.910</td><td>0.341***(0.113)</td><td>1.406</td><td>0.551***(0.118)</td><td>1.735</td></tr><tr><td>Academic</td><td>1.578***(0.244)</td><td>4.845</td><td>1.555***(0.242)</td><td>4.735</td><td>0.956***(0.181)</td><td>2.601</td><td>0.635***(0.180)</td><td>1.887</td></tr><tr><td>Hospital</td><td>-4.439***(0.194)</td><td>0.012</td><td>-4.362***(0.192)</td><td>0.013</td><td>-4.215***(0.217)</td><td>0.015</td><td>-4.252***(0.217)</td><td>0.014</td></tr><tr><td colspan="9">Years</td></tr><tr><td>LL+</td><td colspan="2">-2667.71</td><td colspan="2">-2655.68</td><td colspan="2">-2051.81</td><td colspan="2">-2031.83</td></tr></table>

Notes. Number of observations = 3,982 in organizations and 1,836 in states. Standard errors are in parentheses. P-values are represented by \* Significant at $p < 0 . 1 , { ^ { \star \star } }$ Significant at $p < 0 . 0 5 ,$ , \*\*\* Significant at $p < 0 . 0 1$ . <sup>+</sup>Hazard models are estimated using log likelihood(LL) functions and LL indicates the fit of the model with higher values indicating a better fit.

We next statistically compared the effect of proactive and reactive investments on subsequent security failures (H2). The above tests, where proactive and reactive investments were examined as separate variables for H1a and H1b, already demonstrated that proactive investments had a larger negative effect (coefficient) and smaller hazard rate than reactive investments at both levels. It is not uncommon for researchers to separately compare the effects of different variables on a focal variable. However, a simple comparison using separate variables is not completely satisfying because we cannot perform a formal statistical test of the difference between the coefficients. Even though the coefficients are (individually) statistically significant, the differences between them may not be significant. For this comparison, a formal statistical analysis through an indicator is preferable because it provides a means of formally testing the difference between the coefficients (Jaccard 2001).

Therefore, Model (1) includes an indicator (Proactive ), which represents proactive investments, to test H2. The coefficient of proactive type is –0.885 $( p < 0 . 0 1 , h ( t ) = 0 . 4 1 3 )$ at the organization level, and is –1.963 (p < 0.01, h(t) = 0.140) at the state level. The coefficients are negative at both organizational and state levels, and further the magnitude is larger at the state level. This indicates that proactive investments result in lower failure rates than reactive investments at both levels and the impact of proactive investments is amplified at the state level. Therefore, we can conclude that fewer security failures are associated with proactive investments (as opposed to reactive investments) and the impact of the investments is larger at an aggregate level (likely due to information sharing and learning effects).

External pressure, like government regulations, is another important focal variable that affects organizational learning. H3 argues that external pressure can reduce subsequent security failures. We test H3 by investigating how the existence of breach notification laws affects subsequent security failures in a state. We find full support for this hypothesis with Models (1) and (2). Model (1) estimates the coefficients of the laws, –1.357 (p < 0.01, h(t) = 0.258) at the organization level, and –1.137 (p < 0.01, h(t) = 0.321) at the state level. Likewise, Models (2) has –1.250 at p < 0.01 (h(t) = 0.287) at the organization level, and –0.728 at p < 0.01 (h(t) = 0.483) at the state level. Our models consistently indicate that externally mandated requirements are associated with improved security performance.

Finally, in order to test H4a and H4b, we examine the interaction effects of external pressure and security investments through the addition of product terms. At the organization level, external pressure significantly attenuates the effects of proactive investments on subsequent security failures with a positive coefficient, 0.351 at p < 0.05 (h(t) = 1.421). However, external pressure does not significantly affect the effect of reactive investment. Similarly, at the state level, external regulatory pressure also significantly influences the effect of proactive investments with a coefficient, 0.224 at p < 0.01 (h(t) = 1.252), but does not affect reactive investments. An analysis at the state level where all organizations were aggregated into a single organization (rather than by organization type) produced consistent results.

While the number of security controls best represents organizational learning (based on security functionalities rather than the relative cost of controls), the invested monetary values may provide a different viewpoint. Thus, to provide a robustness check, we further examined the firm-level effects of security investment sizes in monetary terms. We estimated the investment costs of security controls based on industry and analyst reports of the major security vendors. Next, the total costs of security controls (including software licensing, implementation, and annual maintenance) were estimated considering the organization size. Interestingly, we found that the results from this monetary analysis were consistent with those based on the number of security controls. This new analysis provides strong evidence for the robustness of our results (see Appendix B).

## Cost-Effectiveness

Effective information security programs can be measured by how well data breaches are prevented or if a data breach occurs (because prevention cannot be always perfect), the effectiveness of limiting breach impact, and costs to remediate. In terms of the effectiveness in preventing a data breach, we demonstrated proactive investments are associated with lower hazard (or failure) rates. In this section, we further compare the cost-effectiveness of proactive and reactive investments in case a data breach occurs.

Due to the difficulty in measuring economic costs and benefits, our cost analysis focuses on indirect losses imposed by breach notification. Recently, HHS (Department of Health and Human Services) conducted a cost analysis of patient data breaches in order to contextualize penalties (HHS 2009). Their analysis estimated total breach cost by multiplying the number of affected individuals by a per-record cost<sup>10</sup> of notifying (including such costs as credit monitoring).

Following this framework, we used totalAffected, which represents the number of affected patient records, to compare the cost-effectiveness of proactive and reactive investments. Table 5 presents the cost-effectiveness of both investments. The result shows that organizations with proactive investments experienced 192 breaches while organizations with reactive investments had 124. However, the proactive group had a much smaller number of affected patients (8,418) per breach than the reactive group (59,059). Keep in mind that the numbers of compromised patient records may be correlated to the organization size. Thus, we tested to see if there was a difference in organization size (as measured by number of beds) between the reactive and proactive group and found no difference (see Table 5). However, we did find a significant difference when comparing the number of affected records per bed. As shown in Table 5, the proactive group has a significantly smaller number of affected records per bed. Again, this points to the superiority of proactive investments. Using the HHS cost-analysis, the average number of affected patients was multiplied by the average notification cost per patient (\$191).<sup>11</sup> The proactive group resulted in average of \$1.6M/breach, whereas the reactive resulted \$11.2M/breach. Thus, we can argue that the severity of the breach is lower in the proactive group with correspondingly lower breach notification costs than the reactive group. Moreover, considering the hazard rate (0.413 at the organization level) of the proactive decision from Table 4, proactive investments are less likely (58.7%) to experience a breach. Thus considering both breach size and likelihood, it is easy to see that reactive investments are not as economically effective as proactive investments.

<table><tr><td colspan="4">Table 5. Cost-Effectiveness</td></tr><tr><td></td><td>Proactive</td><td>Reactive</td><td>t-value</td></tr><tr><td>Total affected records from breaches</td><td>1,616,327</td><td>7,323,269</td><td>3.03***</td></tr><tr><td>Breaches over study period</td><td>192</td><td>124</td><td></td></tr><tr><td>Bed size</td><td>437.7</td><td>478.1</td><td>1.20</td></tr><tr><td>Affected records per breach</td><td>8,418</td><td>59,059</td><td></td></tr><tr><td>Affected records per bed</td><td>26.3</td><td>129.5</td><td>2.99***</td></tr><tr><td>Average cost/breach (Average affected records*$191+)</td><td>$1,607,909</td><td>$11,280,197</td><td></td></tr></table>

Notes. Standard errors are in parentheses. P-values are represented by \*Significant at p < 0.1, \*\*Significant at p < 0.05, \*\*\*Significant at p < 0.01. <sup>+</sup>We used \$191 as the average cost per record from 2005 to 2010. Ponenmon Institute, LLC, estimates of per-record breached cost:\$221 in 2010, \$204 in 2009, \$202 in 2008, \$197 in 2007, \$182 in 2006, and \$138 in 2005.

## Internal Versus External Threats

Security breaches stem from both internal failures (e.g., accidental disclosure or malicious insiders) and external threats (e.g., external theft or attacks) (see Figure 2). An issue we have not addressed is the learning effects associated with specific types of security failures. Our analysis of organizational learning thus far makes no distinction between internal and external threats. However, security researchers point out that organizations often focus on preventing external attacks rather than internal threats, even though internal threats are not less harmful (Liu et al. 2009; McFadzean et al. 2007).

Prior literature from various disciplines has noted that an organization’s perceptions of a problem affect the actual learning and future performance (Hurley and Hult 1998; Ryu et al. 2005; Zakay et al. 2004). If the organization views external threats as more critical than internal threats, it may pay more attention to external threats and indeed learn to better protect against them.

To investigate this question, we divided security failures into two groups: internal and external. Since greater concern about a problem leads to greater effort (or more resource allocation) to resolve the problem, we expect that the learning effect would be larger in preventing external failures than internal failures. Table 6 shows the results. The results for external failures have similar significance patterns as those from the total failures in Table 4. However, the results for internal failures exhibit weaker associations.

The failure in preventing external threats has significant negative associations with proactive investments (–0.683 at p < 0.01, h(t) = 0.505 and –0.826 at p<0.01, h(t) = 0.438) at both the organization and state levels. On the other hand, reactive investments are only significantly associated (negative) with external failures at the state level (–0.447 at p < 0.01, h(t) = 0.639). External pressure is negatively associated with breaches from outsiders at both levels (–1.259, h(t) = 0.284 and –1.177, h(t) = 0.308 at p < 0.01); however it significantly weakens the effect of proactive investments (0.381, h(t) = 1.464 and 0.208, h(t) = 1.231 at p < 0.01).

## Endogeneity of Breach Disclosure Laws

Breach notification laws represent another endogeneity issue since regulation might be systematically enacted in states with higher breach incidents. Romanosky et al. (2011) raised the issue of endogenous adoption of breach notification laws and tested whether laws were adopted due to a sudden rise in identity theft. If laws were endogenous, we would expect to see that states would have an increased identity theft rate immediately before the adoption of legislation. Romanosky et al. demonstrated there has been no such systematic increase for states that adopted a breach disclosure law.

<table><tr><td></td><td colspan="8">Organization</td><td colspan="8">State</td></tr><tr><td></td><td colspan="4">External</td><td colspan="4">Internal</td><td colspan="4">External</td><td colspan="4">Internal</td></tr><tr><td rowspan="2">Independent Variable</td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td></tr><tr><td>Total Inv.</td><td>-0.25***(0.10)</td><td>0.78</td><td></td><td></td><td>-11.70(&gt;100)</td><td>0.00</td><td></td><td></td><td>-0.43***(0.10)</td><td>0.65</td><td></td><td></td><td>-5.02*(2.48)</td><td>0.01</td><td></td><td></td></tr><tr><td>Proactive Inv.(H1a)</td><td></td><td></td><td>-0.68***(0.14)</td><td>0.51</td><td></td><td></td><td>-13.50(&gt;100)</td><td>0.00</td><td></td><td></td><td>-0.83***(0.12)</td><td>0.44</td><td></td><td></td><td>-29.10(&gt;100)</td><td>0.00</td></tr><tr><td>Reactive Inv.(H1b)</td><td></td><td></td><td>-0.02(0.09)</td><td>0.98</td><td></td><td></td><td>-13.09(&gt;100)</td><td>0.00</td><td></td><td></td><td>-0.45***(0.12)</td><td>0.64</td><td></td><td></td><td>-12.00(&gt;100)</td><td>0.00</td></tr><tr><td>Proactive (H2)</td><td>-0.82***(0.31)</td><td>0.44</td><td></td><td></td><td>-4.78(&gt;100)</td><td>0.01</td><td></td><td></td><td>-1.96***(0.35)</td><td>0.14</td><td></td><td></td><td>-16.70(&gt;100)</td><td>0.00</td><td></td><td></td></tr><tr><td>Law (H3)</td><td>-1.26***(0.19)</td><td>0.28</td><td>-1.15***(0.19)</td><td>0.32</td><td>-1.43(0.99)</td><td>0.24</td><td>-1.41(0.9)</td><td>0.25</td><td>-1.18***(0.31)</td><td>0.31</td><td>-0.82***(0.26)</td><td>0.44</td><td>-2.23(1.77)</td><td>0.11</td><td>-1.73(1.55)</td><td>0.18</td></tr><tr><td>Proactive × Law</td><td>0.10***(0.38)</td><td>1.11</td><td></td><td></td><td>5.04(&gt;100)</td><td>&gt;100</td><td></td><td></td><td>0.79**(0.38)</td><td>2.21</td><td></td><td></td><td>15.00(&gt;100)</td><td>&gt;100</td><td></td><td></td></tr><tr><td>Total Inv. × Law</td><td>0.29***(0.10)</td><td>1.33</td><td></td><td></td><td>11.07(&gt;100)</td><td>&gt;100</td><td></td><td></td><td>0.11*(0.06)</td><td>1.12</td><td></td><td></td><td>3.70(1.98)</td><td>40.40</td><td></td><td></td></tr><tr><td>Proactive Inv. × Law (H4a)</td><td></td><td></td><td>0.38***(0.16)</td><td>1.46</td><td></td><td></td><td>13.00(&gt;100)</td><td>&gt;100</td><td></td><td></td><td>0.21***(0.07)</td><td>1.23</td><td></td><td></td><td>27.63(&gt;100)</td><td>&gt;100</td></tr><tr><td>Reactive Inv. × Law (H4b)</td><td></td><td></td><td>0.18*(0.10)</td><td>1.19</td><td></td><td></td><td>12.90(&gt;100)</td><td>&gt;100</td><td></td><td></td><td>0.08(0.07)</td><td>1.09</td><td></td><td></td><td>10.90(&gt;100)</td><td>&gt;100</td></tr><tr><td colspan="17">Controls</td></tr><tr><td>Correction for self-selection (I)</td><td>-5.09***(1.27)</td><td>0.01</td><td>-5.40***(1.30)</td><td>0.01</td><td>8.03**(3.43)</td><td>0.62</td><td>8.12**(3.40)</td><td>&gt;100</td><td>0.91(1.60)</td><td>2.48</td><td>-0.95(1.62)</td><td>0.39</td><td>-27.62*(15.90)</td><td>0.000</td><td>-25.70(17.60)</td><td>0.00</td></tr><tr><td>IT equipment</td><td>0.39***(0.07)</td><td>1.48</td><td>0.38***(0.07)</td><td>1.47</td><td>-0.48**(0.19)</td><td>1.25</td><td>-0.48**(0.19)</td><td>0.62</td><td>0.01(0.01)</td><td>1.01</td><td>0.04***(0.02)</td><td>1.04</td><td>0.43***(0.15)</td><td>1.54</td><td>0.40**(0.16)</td><td>1.59</td></tr><tr><td>Bed size</td><td>-0.24***(0.08)</td><td>0.78</td><td>-0.24***(0.07)</td><td>0.79</td><td>0.22(0.18)</td><td>0.05</td><td>0.23(0.18)</td><td>1.25</td><td>0.04***(0.02)</td><td>1.05</td><td>0.05***(0.02)</td><td>1.05</td><td>-0.27*(0.15)</td><td>0.77</td><td>-0.26*(0.15)</td><td>0.77</td></tr><tr><td>Academic</td><td>2.97***(0.47)</td><td>19.40</td><td>3.09***(0.48)</td><td>22.00</td><td>-2.92*(1.63)</td><td>0.01</td><td>-2.97*(1.62)</td><td>0.05</td><td>0.94***(0.25)</td><td>2.57</td><td>0.96***(0.24)</td><td>2.62</td><td>1.20(1.80)</td><td>3.32</td><td>1.02(1.95)</td><td>2.76</td></tr><tr><td>Hospital</td><td>-4.78***(0.24)</td><td>0.01</td><td>-4.74***(0.24)</td><td>0.01</td><td>-4.76***(0.67)</td><td>0.62</td><td>-4.76***(0.66)</td><td>0.01</td><td>-4.15***(0.24)</td><td>0.02</td><td>-4.30***(0.24)</td><td>0.01</td><td>-4.93***(0.58)</td><td>0.01</td><td>-5.43***(0.57)</td><td>0.00</td></tr><tr><td colspan="17">Years</td></tr><tr><td>LL+</td><td colspan="2">-2264.11</td><td colspan="2">-2249.43</td><td colspan="2">-371.99</td><td colspan="2">-371.93</td><td colspan="2">-2264.11</td><td colspan="2">-2249.43</td><td colspan="2">-197.57</td><td colspan="2">-201.84</td></tr></table>

Notes: Number of observations = 3,982 in organizations and 1,836 in states. Standard errors are in parentheses. p-values are represented by \*Significant at p < 0.1, \*\*Significant at p < 0.05, \*\*\*Significant at p < 0.01. <sup>+</sup>Hazard models are estimated using log likelihood(LL) functions and LL indicates the fit of the model with higher values indicating a better fit

In the healthcare context, we examined the difference between the number of breaches in states immediately before the adoption of legislation and those of states without such laws by conducting a two-sample t-test (at the state level). The t-test shows a p-value of 0.23. Thus, we conclude that the two sample means of the number of breaches with and without the adoption of legislation are not different, and the endogeneity of breach notification laws is not a concern.

## Discussion and Conclusions

Security researchers have posited that organizational learning influences the link between security investment and security performance. This study focused on empirically examining the effects of proactive versus reactive security investments and the influence of external pressure on their effects. Our results provide evidence that proactive security investment is significantly associated with fewer security failures. However, reactive security investment only is significant at a state level, whereas organizational researchers have demonstrated that general reactive investment triggered by failures (e.g., defect rates) efficiently prevent future failures (Haunschild and Sullivan 2002). This finding suggests some interesting conditions on learning effects in healthcare security. Typically, performance in manufacturing depends on internal factors such as well-designed, repetitive processes, while healthcare security faces an evolving set of both internal and external threats. That, in the context of routine-based systems, learning from failure experiences is an effective approach to continuous improvement. However, with everchanging security threats, reactive strategies seem not to be as effective. One possibility is that reactive investment may focus on myopic bug chasing or solving obsolete threats rather than strategically reacting to discourage both internal and external attackers (or reducing the security negligence within an organization). Thus, our results support those who argue that attackers’ abilities and resulting threats evolve so quickly that learning from proactive initiatives is particularly important. Hence, the findings, such as reactive and proactive learning on information security, may not be directly generalized to other environments, since the effects of the types of learning may depend on task uncertainty (see Carrillo and Gaimon 2004).

In our economic analysis, we found that the proactive group experiences smaller breaches and lower breach notification costs than the reactive group. This may seem surprising as prior literature argued that a reactive strategy may generally be more cost effective than a proactive one because proactive strategies are likely to overinvestment stemming from uncertainty in the weakest links (Rowe and Gallaher 2006). However, considering the observation that healthcare lags many other industries in adoption of the latest security technologies, its uncertainty over where to invest may be substantially lower (healthcare can easily learn from industries with a long history of attacks). Thus by proactively investing in well-known weaknesses, healthcare organizations can enhance the cost effectiveness of their security investments.

We further found that the learning effects vary with the types of internal and external security failures. Organizations have different perceptions in the threats of internal and external security failures, and the threats that are perceived to be more significant tend to enhance the learning effects of security investment with more efforts and resources. Our results show that security investments have more significant effects on external failures than internal failures. This implies that organizations may be more concerned about external threats and thus focus more investments on IT security to curb external threats rather than internal threats. Our finding is consistent with arguments (based on other industries) that firms are often familiar with external sources of attack and tend to focus on handling outsider threats (Crinson 2008; Liu et al. 2009). We note, however, that our investment data was measured by the adoption of security technologies, and that preventing accidental disclosures or malicious data breaches from insiders depends heavily on human factors (that are harder to observe), security training, and policies.

Considering the public-good nature of information security, our results indicate that the effects of both proactive and reactive investments are larger at the state level than at the organization level. This supports the argument that security investments create positive externalities (investments in one organization improve security for everyone). As more patient information is shared between healthcare organizations, positive externalities may increase but could also lead to free rider problems.

External pressure, like government regulation, is also significantly associated with security failures at both the organization and state level. Our results show that when proactive investments were made under external pressure, the learning effect was diminished (0.351 at $p < 0 . 0 5 )$ The finding suggests that proactive investments, voluntarily made, are associated with better performance than those initiated by external pressure. However, although external pressure hurts the effect of proactive investment on security performance, the main effects of proactive investment and external pressure (–0.763 at p < 0.01 and –1.250 at $p < 0 . 0 1$ , respectively) are still larger than the moderating effect (0.351 at $p < 0 . 0 5 )$ This indicates that while external regulatory pressure effectively provides problem-solving guidelines, the regulationinduced learning partially harms the effect of the autonomous learning from proactive decision making or resource allocation. With external regulatory mandates, an organization may passively try to meet the mandates rather than actively conduct its own problem analysis.

On the other hand, external pressure does not significantly influence the effect of reactive investments on security performance. Reactive investment may focus on existing problems, since an organization learns its weak points from failure experiences. Here, the problem-solving guidelines of external regulatory mandates may positively influence the scope of failure-induced learning by incorporating regulation-induced learning including more common or critical failures. This implies that whereas external regulatory requirements significantly hurt autonomous learning of proactive investments, the requirements may help, or at least not hurt, failure-induced learning from reactive investments despite their involuntary nature. This outcome may be the case for reactive strategies where regulation pushes organizations to extend the scope of investment beyond common problem areas (or simply chasing existing problems).

In summary, healthcare organizations have faced two types of task uncertainty over finding their own weak links (internally) and understanding the evolving security threats (externally). Because healthcare organizations have not heavily invested in security, there are relatively low levels of uncertainty over the weak links. However, patient data, as a rich source of personal information, have faced a highly evolving set of security threats. The high uncertainty over the threats has made the effects of autonomous and regulation-induced learning greater than that of failure-induced learning. Likewise, the low uncertainty over weak links has made proactive investments more cost effective than reactive investments. These uncertainties also allow us to draw some implications from the interactions between autonomous, failure-induced and regulation-induced learning. Although government regulations can provide useful security guidelines, we argue that external pressure has partially turned proactive strategies, which can cope with evolving threats as well as potential weak links, into a passive focus or defensive reactions. On the other hand, despite the passive focus by external pressure, reactive strategies focusing on existing weak links may leverage the external security guidelines that can provide useful information on the vulnerabilities not yet addressed in healthcare organizations.

Our findings have important implications for both security managers and policy makers. First, security managers and governments should pay considerable attention to decision processes in security investment in order to maximize the effectiveness of the investments. Such effectiveness is particularly important for organizations operating with constrained resources and evolving security threats. Based on these results, we advise chief information security officers to place greater emphasis on proactive initiatives rather than maintaining a purely reactive posture. Second, policy makers should consider regulation that combines proactive initiatives and external pressures—for example, mandating that a portion of the overall IT budget be dedicated to security while allowing the organizations to decide on the types of security investment. Alternatively, financial incentives like those in the HITECH legislation could be earmarked specifically for security. Since the incentives could encourage more organizations to make investments, the organizations can take advantage of the network effects of the investment.

Some important issues remain for future research. We considered only the adoption of security applications without addressing the issue of security policies and training programs. While implementing controls such as training would have a direct learning effect, our study mainly focuses on indirect learning effects through learning by doing or learning by using IT security controls. Future research could also consider longer periods. One limitation of survival models is the fact that it is common to observe organizations that never experience an event within the study period. However, this limitation is of no great consequence because our interest centers on the hazard rates, rather than the survival time. Nonetheless, data covering longer periods would provide more opportunities for interesting analysis.

## Acknowledgments

This work was conducted while both authors were at the Center for Digital Strategies at the Tuck School of Business, Dartmouth College. The authors thank the MIS Quarterly editorial review team and participants of the Tenth Workshop on the Economics of Information Security (WEIS 2011) for their insightful feedback on this paper. This research was partially supported by the National Science Foundation, Grant Award Numbers CNS-0910842 (under the auspices of the Institute for Security, Technology, and Society) and CNS-1329686.

## References

Anderson, R. 1996. “A Security Policy Model for Clinical Information Systems,” in Proceedings of the IEEE Symposium on Security and Privacy, Los Alamitos, CA: IEEE Computer Society, pp. 30-43.

Anderson, R. 2001. “Why Information Security Is Hard: An Economic Perspective,” in Proceedings of the 17<sup>th</sup> Annual Computer Security Applications Conference, Los Alamitos, CA: IEEE Computer Society, pp. 358-365.

Angst, C. M., and Agarwal, R. 2009. “Adoption of Electronic Health Records in the Presence of Privacy Concerns: The Elaboration Likelihood Model and Individual Persuasion,” MIS Quarterly (33:2), pp. 339-370.

Appari, A., and Johnson, M. E. 2009. “Information Security and Privacy in Healthcare: Current State of Research,” International Journal of Internet and Enterprise Management (6:4), pp. 279-314.

Attewell, P. 1992. “Technology Diffusion and Organizational Learning: The Case of Business Computing,” Organization Science (3:1), pp. 1-19.

Barth, A., Rubinstein, B., Sundararajan, M., Mitchell, J, Song, D., and Bartlett, P. 2010. “A Learning-Based Approach to Reactive Security,” Financial Cryptography and Data Security: Lecture Notes in Computer Science (6052), Berlin: Springer-Verlag, pp. 192-206.

Bodin, L. D., Gordon, L. A., and Loeb, M. P. 2005. “Evaluating Information Security Investments Using the Hierarchy,” Communications of the ACM (48:2), pp. 79-83.

Bohme, R., and Moore, T. 2010. “The Iterated Weakest Link,” IEEE Security & Privacy (8:1), pp. 53-55.

Bowie, N. E., and Jamal, K. 2006. “Privacy Rights on the Internet: Self-Regulation or Government Regulation?,” Business Ethics Quarterly (16:3), pp. 323-342.

Bulgurcu, B., Cavusoglu, H., and Benbasat, I. 2010. “Information Security Policy Compliance: An Empirical Study of Rationality-Based Beliefs and Information Security Awareness,” MIS Quarterly (34:3), pp. 523-548.

Carrillo, J. E., and Gaimon, C. 2000. “Improving Manufacturing Performance through Process Change and Knowledge Creation,” Management Science (46:2), pp. 265-288.

Carrillo, J. E. and Gaimon, C. 2004. “Managing Knowledge-Based Resource Capabilities under Uncertainty,” Management Science (50:11), pp. 1504-1518.

Cavusoglu, H., Mishra, B., and Raghunathan, S. 2004. “The Effect of Internet Security Breach Announcements on Market Value: Capital Market Reactions for Breached Firms and Internet Security Developers,” International Journal of Electronic Commerce (9:1), pp. 69-104.

Cavusoglu, H., Raghunathan, S., and Yue, W. T. 2008. “Decision-Theoretic and Game-Theoretic Approaches to IT Security Investment,” Journal of Management Information Systems (25:2), pp. 281-304.

Chari, M. D. R., Devaraj, S., and David, P. 2008. “The Impact of Information Technology Investments and Diversification Strategies on Firm Performance,” Management Science (54:1), pp. 224-234.

Chen, P. Y., Kataria, G., and Krishnan, R. 2011. “Correlated Failures Diversification and Information Security Risk Management,” MIS Quarterly (35:2), pp. 397-422.

Cox, D. R. 1972. “Regression Models and Life-Tables,” Journal of the Royal Statistical Society Series B—Statistical Methodology (34:2), pp. 187-220.

Crinson, I. 2008. “Assessing the ‘Insider–Outsider Threat’ Duality in the Context of the Development of Public–Private Partnerships Delivering ‘Choice’ in Healthcare Services: A Sociomaterial Critique,” Information Security Technical Report (13:4), pp. 202-207.

Culnan, M. J., Foxman, E. R., and Ray, A. W. 2008. “Why IT Executives Should Help Employees Secure Their Home Computers,” MIS Quarterly Executive (7:1), pp. 49-56.

Culnan, M. J. and Williams, C. C. 2009. “How Ethics Can Enhance Organizational Privacy: Lessons from the ChoicePoint and TJX Data Breaches,” MIS Quarterly (33:4), pp. 673-687.

Dorroh, J. R., Gulledge, T. R. and Womer, N. K. 1994. “Investment in Knowledge: A Generalization of Learning by Experience” Management Science (40:8), pp. 947-958.

Eliashberg, J., Singpurwalla, N. D., and Wilson, S. P. 1997. “Calculating the Reserve for a Time and Usage Indexed Warranty,” Management Science (43:7), pp. 966-975.

Fine, C. H. 1986. “Quality Improvement and Learning in Productive Systems,” Management Science (32:10), pp. 1301-1315.

Frakes, W. B., and Kang, K. 2005. “Software Reuse Research: Status and Future,” IEEE Transactions on Software Engineering (31:7), pp. 529-536.

Gordon, L., and Loeb, M. 2002. “The Economics of Information Security Investment,” ACM Transactions on Information and System Security (5:4), pp. 438-458.

Gordon, L. A., and Loeb, M. P. 2006. “Budgeting Process for Information Security Expenditures,” Communications of the ACM (49:1), pp. 121-125.

Greene, W. H. 1981. “Sample Selection Bias as a Specification Error-Comment,” Econometrica (49:3), pp. 795-798.

Greene, W. H. 2003. Econometric Analysis (5<sup>th</sup> ed.), Upper Saddle River, NJ: Prentice Hall.

Hair, J. F., Tatham, R. L., Anderson, R. E., and Black, W. 2005. Multivariate Data Analysis (6<sup>th</sup> ed.), Upper Saddle River, NJ: Prentice Hall.

Hatch, N. W., and Mowery, D. C. 1998. “Process Innovation and Learning by Doing in Semiconductor Manufacturing,” Management Science (44:11), pp. 1461-1477.

Haunschild, P. R., and Rhee, M. 2004. “The Role of Volition in Organizational Learning: The Case of Automotive Product Recalls,” Management Science (50:11), pp. 1545-1560.

Haunschild, P. R. and Sullivan, B. N. 2002. “Learning from Complexity: Effects of Prior Accidents and Incidents on Airlines’ Learning,” Administrative Science Quarterly (47:4), pp. 609-643.

Heckman, J. J. 1979. “Sample Selection Bias as a Specification Error,” Econometrica (47:1), pp. 153-161.

Herath, H. S. B., and Herath, T. C. 2008. “Investments in Information Security: A Real Options Perspective with Bayesian Postaudit,” Journal of Management Information Systems (25:3), pp. 337-375.

HHS. 2009. “Breach Notification for Unsecured Protected Health Information; Interim Final Rule,” Federal Register (74:162), pp. 42740-42770 (http://www.gpo.gov/fdsys/pkg/FR-2009-08-24/ pdf/E9-20169.pdf).

Hillestad, R., Bigelow, J., Bower, A., Girosi, F., Meili, R., Scoville, R., and Taylor, R. 2005. “Can Electronic Medical Record Systems Transform Health Care? Potential Health Benefits, Savings, and Costs,” Health Affairs (24:5), pp. 1103-1117.

HIMSS. 2012. “2012 HIMSS Analytics Report: Security of Patient Data,” Kroll Advisory Solutions (http://www.krollcybersecurity. com/media/Kroll-HIMSS\_2012\_-\_Security\_of\_Patient\_Data\_ 040912.pdf).

Ho, J. L. Y., Wu, A., and Xu, S. X. 2011. “Corporate Governance and Returns on Information Technology Investment: Evidence from an Emerging Market,” Strategic Management Journal (32:6), pp. 595-623.

Hurley, R. F., and Hult, G. T. M. 1998. “Innovation, Market Orientation, and Organizational Learning: An Integration and Empiri cal Examination,” Journal of Marketing (62:3), pp. 42-54.

Iheagwara, C., Blyth, A., and Singhal, M. 2004. “Cost Effective Management Frameworks for Intrusion Detection Systems,” Journal of Computer Security (12:5), pp. 777-798 .

Ittner, C. D., Nagar, V., and Rajan, M. V. 2001,”An Empirical Examination of Dynamic Quality-Based Learning Models,” Management Science (47:4), pp. 563-578.

Jaccard, J. 2001. Interaction Effects in Logistic Regression, Thousand Oaks, CA: Sage Publications, Inc.

Johnson, M. E. 2009. “Data Hemorrhages in the Health-Care Sector,” Financial Cryptography and Data Security: Lecture Notes in Computer Science (5628), Berlin: Springer-Verlag, pp. 71-89.

Kannan, K., Rees, J., and Sridhar, S. 2007. “Market Reactions to Information Security Breach Announcements: An Empirical Analysis,” International Journal of Electronic Commerce (12:1), pp. 69-91.

Karande, K., Magnini, V.P., and Tam, L. 2007. “Recovery Voice and Satisfaction After Service Failure: An Experimental Investigation of Mediating and Moderating Factors,” Journal of Service Research (10:2), pp. 187-203.

Kark, K., Penn, J., and Dill, A. 2009. “CISO Priorities: The Right Objectives But the Wrong Focus,” Forrester Research. Cambridge, MA.

Kauffman, R. J., McAndrews, J., and Wang, Y. M. 2000. “Opening the ‘Black Box’ of Network Externalities in Network Adoption,” Information Systems Research (11:1), pp. 61-82.

Kolfal, B., Patterson, R., and Yeo, L. 2010. “Market Impact on IT Security Spending,” in Proceedings of the Ninth Workshop on the Economics of Information Security, Harvard University.

Li, G., and Rajagopalan, S. 1998. “Process Improvement, Quality, and Learning Effects,” Management Science (44:11), pp. 1517-1532.

Li, S. L., Shang, J., and Slaughter, S. A. 2010. “Why Do Software Firms Fail? Capabilities, Competitive Actions, and Firm Survival in the Software Industry from 1995 to 2007,” Information Systems Research (21:3), pp. 631-654.

Liang, H. G., and Xue, Y. J. 2009. “Avoidance of Information Technology Threats: A Theoretical Perspective,” MIS Quarterly (33:1), pp. 71-90.

Liberti, L. 2008. “Survey Results: Reduce the Cost of Compliance While Strengthening Security,” CA Advisor: Security Management Newsletter.

Liu, D. B., Wang, X. F., and Camp, L. J. 2009. “Mitigating Inadvertent Insider Threats with Incentives,” Financial Cryptography and Data Security (5628), pp. 1-16.

Lohmeyer, D. F., McCrory, J., and Pogreb, S. 2002. “Managing Information Security,” The McKinsey Quarterly, June.

Majumdar, S. K., and Marcus, A. A. 2001. “Rules Versus Discretion: The Productivity Consequences of Flexible Regulation,” Academy of Management Journal (44:1), pp. 170-179.

Marcellus, R. L., and Dada, M. 1991. “Interactive Process Quality Improvement,” Management Science (37:11), pp. 1365-1376.

March, J. G. 1991. “Exploration and Exploitation in Organizational Learning,” Organization Science (2:1), pp. 71-87.

May, S., Hosmer, D. W., and Lemeshow, S. 2008. Applied Survival Analysis: Regression Modeling of Time-to-Event Data, Hoboken, NJ: Wiley-Interscience.

McFadzean, E., Ezingeard, J. N., and Birchall, D. 2007. “Perception of Risk and the Strategic Impact of Existing IT on Information Security Strategy at Board Level,” Online Information Review (31), pp. 622-660.

Miller, A. R., and Tucker, C. 2009. “Privacy Protection and Technology Diffusion: The Case of Electronic Medical Records,” Management Science (55:7), pp.1077-1093.

Mukherjee, A. S., Lapre, M. A., and Van Wassenhove, L. N. 1998. “Knowledge Driven Quality Improvement,” Management Science (4:11), pp. 535-549.

Mulligan, D. K., and Bamberger, K. A. 2007. “Security Breach Notification Laws: Views from Chief Security Officers,” Samuelson Law, Technology & Public Policy Clinic, University of California-Berkeley School of Law (http://www.law. berkeley.edu/files/cso\_study.pdf).

Naveh, E., and Marcus, A. A. 2004. “When Does the ISO 9000 Quality Assurance Standard Lead to Performance Improvement? Assimilation and Going Beyond,” IEEE Transactions on Engineering Management (51:3), pp. 352-363.

Nonaka, I. 1994. “A Dynamic Theory of Organizational Knowledge Creation,” Organization Science (5:1), pp. 14-37.

Ocasio, W. 1997. “Towards an Attention-Based View of the Firm,” Strategic Management Journal (18), pp. 187-206.

Pironti, J. P. 2005. “Key Elements of an Information Security Program,” Information Systems Control Journal (1), (http://www.isaca.org/Journal/Past-Issues/2005/Volume-1/ Documents/jpdf051-Key-Elements-of-an-is-program.pdf)

Puhakainen, P., and Siponen, M. 2010. “Improving Employees Compliance through Information Systems Security Training: An Action Research Study,” MIS Quarterly (34:4), pp. 757-778.

Radner, R., and Rothschild, M. 1975. “Allocation of Effort,” Journal of Economic Theory (10:3), pp. 358-376.

Roberds, W., and Schreft, S. L. 2009. “Data Breaches and Identity Theft,” Journal of Monetary Economics (56:7), pp. 918-929.

Romanosky, S., Telang, R., and Acquisti, A. 2011. “Do Data Breach Disclosure Laws Reduce Identity Theft?,” Journal of Policy Analysis and Management (30:2), pp. 256-286.

Rowe, B. R., and Gallaher, M. P. 2006. “Private Sector Cyber Security Investment Strategies: An Empirical Analysis,” in Proceedings of the Eighth Workshop on the Economics of Information Security, Cambridge, UK (http://weis2006.econinfosec. org/docs/18.pdf).

Ryan, J. and Ryan, D. J. 2005. “Proportional Hazards in Information Security,” Risk Analysis (25:1), pp. 141-149.

Ryu, C., Kim, Y. J., Chaudhury, A., and Rao, H. R. 2005. “Knowledge Acquisition via Three Learning Processes in Enterprise Information Portals: Learning-by-Investment, Learning-by-Doing, and Learning-from-Others,” MIS Quarterly (29:2), pp. 245-278.

Salomon, R., and Martin, X. 2008. “Learning, Knowledge Transfer, and Technology Implementation Performance: A Study of Time-to-Build in the Global Semiconductor Industry,” Management Science (54:7), pp. 1266-1280.

Shaver, J. M. 1998. “Accounting for Endogeneity When Assessing Strategy Performance: Does Entry Mode Choice Affect FDI Survival?,” Management Science (44:4), pp. 571-585.

Sinha, R. K. and Noble, C. H. 2008. “The Adoption of Radical Manufacturing Technologies and Firm Survival,” Strategic Management Journal (29:9), pp. 943-962.

Smith, H. A., McKeen, J. D., Cranston, C., and Benson, M. 2010. “Investment Spend Optimization: A New Approach to IT Investment at BMO Financial Group,” MIS Quarterly Executive (9:2), pp. 65-81.

Susarla, A., and Barua, A. 2011. “Contracting Efficiency and New Firm Survival in Markets Enabled by Information Technology,” Information Systems Research (22:2), pp. 306-324.

Teisberg, E. O. 1994. “An Option Valuation Analysis of Investment Choices by A Regulated Firm,” Management Science (40:4), pp. 535-548.

Tucker, A. L., Nembhard, I. M., and Edmondson, A. C. 2007. “Implementing New Practices: An Empirical Study of Organizational Learning in Hospital Intensive Care Units,” Management Science (53:6), pp. 894-907.

Van Mieghem, J. A. 1998. “Investment Strategies for Flexible Resources,” Management Science (44:8), pp. 1071-1078.

Wang, J., Chaudhury, A., and Rao, H. R. 2008. “A Value-at-Risk Approach to Information Security Investment,” Information Systems Research (19:1), pp. 106-120.

Wang, T. W., Rees , J., and Kannan , K. N. 2008. “Reading the Disclosures with New Eyes: Bridging the Gap Between Infor-

mation Security Disclosures and Incidents,” working paper, Krannert Graduate School of Business, Purdue University.

Winter, S. G. 1981. “Attention Allocation and Input Proportions,” Journal of Economic Behavior & Organization (2:1), pp. 31-46.

Winter, S. G. 1994. Organizing for Continuous Improvement: Evolutionary Theory Meets the Quality Revolution, New York: Oxford University Press.

Yue, W. T. and Cakanyildirim, M. 2007. “Intrusion Prevention in Information systems: Reactive and Proactive Responses,” Journal of Management Information Systems (24:1), pp. 329-353.

Zakay, D., Ellis, S., and Shevalsky, M. 2004. “Outcome Value and Early Warning Indications as Determinants of Willingness to Learn from Experience,” Experimental Psychology (51:2), pp. 150-157.

Zantek, P. F., Wright, G. P., and Plante, R. D. 2002. “Process and Product Improvement in Manufacturing Systems with Correlated Stages,” Management Science (48:5), pp. 591-606.

Zhulei, T., Yu, H., and Smith, M. D. 2008. “Gaining Trust through Online Privacy Protection: Self-Regulation, Mandatory Standards, or Caveat Emptor,” Journal of Management Information Systems (24:4), pp. 153-173.

Zollo, M., and Winter, S. G. 2002. “Deliberate Learning and the Evolution of Dynamic Capabilities,” Organization Science (13:3), pp. 339-351.

## About the Authors

Juhee Kwon is an assistant professor in the Information Systems Department at the College of Business, City University of Hong Kong. Her research interests include information security, healthcare IT, IT business values, and business–IT alignment. She earned a Ph.D. from the Krannert School of Management, Purdue University. Her research articles have appeared in such academic journals as MIS Quarterly, Journal of Management Information Systems, Journal of the American Medical Informatics Association, and Journal of Information Systems.

M. Eric Johnson is dean of the Owen Graduate School of Management at Vanderbilt University. His teaching and research focuses on the impact of information technology on the extended enterprise. Through grants from the National Science Foundation and the Department of Homeland Security, he is studying how information technology improves process execution but also how security failures create friction throughout the extended enterprise. His recent book, The Economics of Financial and Medical Identity Theft (Springer 2012) examines the security failures and economic incentives that drive identity theft. He holds patents on interface design and has testified before the U.S. Congress on information security. Eric has a Ph.D. in Engineering from Stanford University.

# PROACTIVE VERSUS REACTIVE SECURITY INVESTMENTS IN THE HEALTHCARE SECTOR

Juhee Kwon

Department of Information Systems, College of Business, City University of Hong Kong, Kowloon Tong, HONG KONG {juhee.kwon@cityu.edu.hk}

M. Eric Johnson Owen Graduate School of Management, Vanderbilt University, Nashville, TN 37203 U.S.A. {m.eric.johnson@owen.vanderbilt.edu}

## Appendix A

## The Distribution of Security Controls

![](/api/attachments/SZH5YAVA/fulltext/images/58dfbcc0b4833b2ab0cc8dca5b510eec6cba88b2551465faef0d4aee3bc91abd.jpg)

Figure A1. Security Controls in Proactive Versus Reactive Investments

![](/api/attachments/SZH5YAVA/fulltext/images/bc667a0442c3eca84d125809185733e568fb522674c1b2cb2fbd48312a571914.jpg)

Figure A2. Security Controls With Law Versus Without Law

![](/api/attachments/SZH5YAVA/fulltext/images/3e8db5bed7dad49556b1fa80b2e654ebebc66b00b2c39e4189ad66500e5d3650.jpg)  
Figure A3. Security Controls With/Without Law in Proactive Investments

![](/api/attachments/SZH5YAVA/fulltext/images/d7e5512680e54eab4e2d0d94fdfe7b410cb67a8a18e7e440a9d47655599f1f90.jpg)

Figure A4. Security Controls With/Without Law in Reactive Investments

## Appendix B

## The Results with the Monetary Values of Security Controls

We estimated the investment costs of security controls based on industry and analyst reports of the major security vendors. Next, the total costs of security controls (including software licensing, implementation, and annual maintenance) were estimated considering the organization size. Interestingly, we found that the results from this monetary analysis were consistent with those based on the number of security controls. This new analysis provides strong evidence for the robustness of our results.

Table B1. The Average Prices of Security Controls

<table><tr><td>One user / 3 year</td><td>Antivirus</td><td>Encryption</td><td>Firewall</td><td>Intrusion Detection</td><td>Spam</td><td>User Authentication</td></tr><tr><td>License</td><td>$80.6</td><td>$15.9</td><td>$67</td><td>$230.0</td><td>$60</td><td>$22.4</td></tr><tr><td>Maintenance</td><td>$9.4</td><td>$8.1</td><td>$51</td><td>$124.5</td><td>$13.5</td><td>$86.0</td></tr><tr><td>Total</td><td>$90.0</td><td>$24.0</td><td>$118.0</td><td>$354.5</td><td>$73.5</td><td>$108.4</td></tr></table>

Note: Dollar values = security control × price × organization size

<table><tr><td colspan="5">Table B2. The Results from the Hazard Model With the Monetary Values of Security Controls</td></tr><tr><td rowspan="2"></td><td colspan="2">Model (1)</td><td colspan="2">Model (2)</td></tr><tr><td> $\beta_j$ </td><td>h(t)</td><td> $\beta_j$ </td><td>h(t)</td></tr><tr><td>Total Inv.</td><td>-0.042**(0.016)</td><td>0.958</td><td></td><td></td></tr><tr><td>Proactive Inv.(H1a)</td><td></td><td></td><td>-0.041**(0.017)</td><td>0.960</td></tr><tr><td>Reactive Inv.(H1b)</td><td></td><td></td><td>0.002(0.018)</td><td>0.998</td></tr><tr><td>Proactive (H2)</td><td>-2.876***(0.873)</td><td>0.056</td><td></td><td></td></tr><tr><td>Law (H3)</td><td>-1.762***(0.636)</td><td>0.172</td><td>-1.550***(0.660)</td><td>0.212</td></tr><tr><td>Proactive × Law</td><td>1.383(0.839)</td><td>3.985</td><td></td><td></td></tr><tr><td>Total Inv. × Law</td><td>0.036**(0.016)</td><td>1.037</td><td></td><td></td></tr><tr><td>Proactive Inv. × Law (H4a)</td><td></td><td></td><td>0.032**(0.017)</td><td>1.032</td></tr><tr><td>Reactive Inv. × Law (H4b)</td><td></td><td></td><td>0.016(0.019)</td><td>1.016</td></tr><tr><td colspan="5">Controls</td></tr><tr><td>Correction for self-Selection (λ)</td><td>-2.837**(1.473)</td><td>0.059</td><td>-0.959(1.202)</td><td>0.383</td></tr><tr><td>IT equipment</td><td>0.050(0.124)</td><td>1.051</td><td>-0.002(0.121)</td><td>0.999</td></tr><tr><td>Bed size</td><td>1.681***(0.239)</td><td>5.371</td><td>1.573***(0.202)</td><td>4.821</td></tr><tr><td>Academic</td><td>0.954**(0.400)</td><td>2.598</td><td>0.798**(0.416)</td><td>2.222</td></tr><tr><td>Hospital</td><td>-0.261(0.244)</td><td>0.770</td><td>-0.118(0.226)</td><td>0.889</td></tr><tr><td colspan="5">Years</td></tr><tr><td> $LL^+$ </td><td colspan="2">-2787.94</td><td colspan="2">-2779.19</td></tr></table>

Notes: Number of observations = 3,982. Standard errors are in parentheses. P-values are represented by \*Significant at p <0.1, \*\*Significant at $p < 0 . 0 5 ,$ , \*\*\*Significant at $p < 0 . 0 1$
