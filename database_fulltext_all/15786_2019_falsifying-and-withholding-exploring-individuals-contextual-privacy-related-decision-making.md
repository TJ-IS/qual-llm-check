---
otero_id: 15786
otero_key: "FAEUHSJV"
title: "Falsifying and withholding: exploring individuals’ contextual privacy-related decision-making"
authors: "Caroline Lancelot Miltgen; H. Jeff Smith"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.11.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Falsifying and withholding: exploring individuals’ contextual privacyrelated decision-making

![](/api/attachments/FAEUHSJV/fulltext/images/4cb043f0d06641e1c1366ff9bcc64a0fb071c71c4db21ca6d504a805c2d32da2.jpg)

Caroline Lancelot Miltgen<sup>a,⁎</sup>, H. Jef Smith<sup>b</sup>

<sup>a</sup> Audencia Business School, 8 Route de la Jonelière, 44312 Nantes, France

<sup>b</sup> Department of Information Systems and Analytics, Farmer School of Business, Miami University, Oxford, OH USA

## A R T I C L E I N F O

Keywords: Information privacy Falsification Disclosure Withholding Personal data Privacy tradeof Context

## A B S T R A C T

As firms rely increasingly on “big data” to segment and target current and potential customers, the challenge of data falsification—individuals providing incorrect personal data in response to requests—is becoming a significant problem. Based on public opinion surveys, within some demographic groups, over three-quarters of individuals confirm that they have given inaccurate information in response to data requests. Obviously, firms that embrace a covert assumption of honesty in online data disclosures are deluding themselves and are likely falling into the trap of “garbage in, garbage out” in their segmenting and targeting.

Despite the frequency and importance of falsification, however, it has received scant attention in the privacy research stream. Most researchers focus on the act of disclosure (and its counter-construct, withholding of data) and overlook that many of the data elements being disclosed may in fact be falsified. To address this weakness in the literature stream, we develop a nomological model that predicts both falsification and withholding behavior, and we test it using a sample collected with the assistance of an online panel provider. We find strong support for the model and show how context could play a significant role in moderating some of the proposed relationships. We then discuss important implications for practice and research

The Pizza Shack, a small pizza delivery service, created a social media application that asked visitors to enter (among other things) their date of birth when configuring their profile on the app. The Pizza Shack’s owners envisioned the creation of a birthday-related promotion that would send a coupon to each registered customer one week in advance of his or her birthday each vear. However, when their IT staff personnel attempted to test the “birthday coupon” notification feature, they were astounded to find that 43% of the coupons were scheduled for distribution on Christmas Day, December 25. Confused, the staf looked carefully at the database and discovered that almost half of the registrants had chosen “1″ and “January” as their day and month of birth, respectively. After randomly querying some of these customers who were willing to discuss the matter, the staf concluded that a large number of registrants had not wanted to reveal their actual birthdate to the Pizza Shack so had simply chosen a year (from the “year” pulldown menu) that made them over 18 years old and had selected the first day and month that appeared on the “day” and “month” pulldown menus. Before totally canceling the promotion, the company decided to conduct further interviews to better understand why registrants had

reacted this way.

Most of the interviewees said they were unsure of what could be done with this information, suggesting a lack of trust in the company running the app. Following this feedback, Pizza Shack decided to better explain, in the registration screen, why this specific information was needed at that point and how it would be used (i.e., to send people some promotion coupons for their birthday), two elements which had been omitted in the first version of the app. This resulted in a significant reduction of registrants claiming to be born on January 1 in the data base and led to a successful promotion campaign.

## 1. Introduction

When faced with a request for personal data, an individual has three basic and mutually exclusive alternatives to the request:

a) Honestly disclose the information;

b) Withhold the information (sometimes called “non-disclosure”); and c) Disclose false information.1

FALSIFICATION BY DATA TYPE. Answers to the query “Have you ever made up and submitted incorrect information to a website, service or a mobile form that asked for personal information? (Please check all that apply.)”.  
Source: [3]. Total respondents: 1,615, geographically distributed U.S. residents, aged 18 and older.

<table><tr><td>I have provided...</td><td>Percentage</td></tr><tr><td>...an incorrect phone number</td><td>34.24%</td></tr><tr><td>...a poor or “spam” email address</td><td>33.62%</td></tr><tr><td>...an incorrect birthday</td><td>33.50%</td></tr><tr><td>...an incorrect name</td><td>31.64%</td></tr><tr><td>...incorrect identity information</td><td>22.11%</td></tr><tr><td>...incorrect preferences</td><td>15.85%</td></tr><tr><td>...incorrect employment information</td><td>13.81%</td></tr></table>

Unfortunately, firms often ignore the possibility of individuals embracing the third option and instead assume that the decision is a binary one (disclose or withhold). This leads them to the inaccurate conclusion that all disclosed data are accurate. Similarly, researchers tend to focus on options a and b, whereas we focus on option c.

The Pizza Shack scenario—disguised but based on an actual situation—illustrates the danger of firms’ relying on the accuracy of users self-reported inputs. Indeed, one industry observer has lamented that the increasing preponderance of such a phenomenon could destroy the value of “big data” [1]. A recent survey found that “two in three [consumers] admit…to deliberately giving incorrect information” ([2], p. 1), and the frequency of such falsification varies across age groups, with 81% of those between ages 18 and 24 “admitting to provide, at least occasionally, wrong information when asked for personal information” ([2], p. 1). As can be seen in Table 1, the frequency of falsification varies for diferent data types, with about one-third of individuals in one survey reporting that they have falsified their birthday to a “website, service, or a mobile form that asked for personal information” ([3], p. 2). Given these survey findings, it is hardly surprising that the firm in our opening vignette found that the data collected in its “birthday promotion” were flawed.

In spite of this problematic phenomenon, it is quite rare for in formation systems (IS) researchers to focus on its occurrence or factors associated therewith. This is indeed ironic, because digital disclosure of personal information from an individual to an online firm (our focus here) appears to be the most frequently employed dependent variable (DV) in empirical privacy-related IS research [4]. However, most re searchers seem to rely on a covert assumption that individuals’ disclosures of personal information are accurate ones. Appendix 1 shows that 42 studies employing online disclosure to an organizational entity as a DV have appeared in the top IS journals,<sup>2</sup> but only one addressed the phenomenon of individuals providing false information during digital disclosure to a firm: Son and Kim [5].<sup>3</sup> Son and Kim [5] examined Internet users’ “privacy-protective responses,” which included two alternatives associated with “information provision" (refusal and mis. representation), two alternatives associated with “private action” (removal and negative word-of-mouth), and two alternatives associated with “public action” (complaining directly to online companies and complaining indirectly to third-party organizations). However, only one of their independent variables (perceived justice) was significant in predicting misrepresentation behavior, and that relationship explained only 3% of the variance in misrepresentation.

Looking beyond these top IS journals, we found another IS article that has addressed this issue of false information: Keith et al. [6] included a DV that addressed whether individuals’ data disclosures were in fact honest ones. They discovered that what at first appeared to be a weak relationship between subjects’ stated disclosure intentions and their actual disclosures was actually a strong one when they considered honest disclosures instead of disclosures. However, their assessment of falsification was conducted in a post hoc survey, and it was not the focus of their model or theoretical derivation.

As it turns out, this lack of attention to falsification in disclosure to online firms is not restricted to IS journals. Our search of the top marketing journals and our overarching search of titles in other disciplines through Google Scholar revealed only five articles that have directly addressed this topic through empirical studies ([7,8]; [9] [10,11];). Although some of the studies did yield quite interesting findings (e.g., Malheiros et al. [7] found that perceptions of “fairness” were associated with levels of falsification), none of those five viewed falsification as a primary focus of an overarching theoretical model.

We can conclude that despite the obvious importance of the topic of falsification, surprisingly little attention has been paid to this topic in the IS literature and, for that matter, in academic research as a whole. Generally speaking, studies that attempt to explain individuals’ disclosure of personal data covertly assume that the mere disclosure of data is suficient to enable subsequent use. However, as highlighted by the old adage “garbage in, garbage out,” to the extent that the integrity of databases is reduced through falsification, the implications are stark, especially when juxtaposed against greater analytical use of “big data” to both categorize and target specific consumers. As was noted by a Chief Technology Oficer, "… more and more people are lying to their service providers. A big part of the… ecosystem is big data, analytics and the power of information. That starts falling to pieces if we find a lot of people are lying” ([1], p. 1).

To understand better what is contributing to such behavior, we attempt to answer the following research questions:

1) To what extent does a privacy tradeof – based on perceived benefits, perceived risks, and trust – explain a) individuals’ data disclosure decisions, such as withholding, and b) the phenomenon of individuals providing falsified data in privacy-related decisions?

2) To what extent can individuals’ perceptions of risks, benefits, and trust in privacy-related decisions be explained by the contextual factor of perceived relevance?

Further, we consider an exploratory question that, while not having been addressed with much theoretical rigor in the past, deserves consideration in the future research stream:

1) How does the context of a data request influence individuals’ decisions regarding data disclosure (including withholding) and falsifi cation?

We derive a model that explains not only disclosure (more precisely, withholding) of personal information but also falsification thereof. With the cooperation of a French online access panel provider, we conducted an online experiment in which participants confronted a real-world situation that would prompt an online request for personal data from a commercial website. Our results confirm that large percentages of the variance in both withholding and falsification can be explained by a tradeof among perceptions of risks, benefits, and trust, each of which, in turn, is associated strongly with the contextual factor of perceived relevance. These findings are particularly unique for the DV of falsification, as this is the first study to have demonstrated this phenomenon.

In the following section, we propose a research model with several specific hypotheses and one proposition. We then provide a literature review that justifies those hypotheses and explains that proposition. We follow this with a discussion of methods of this study and an analysis of our data. We conclude with a discussion of implications for research and practice.

## 2. Background and model development

As is obvious from the discussion above, no theory regarding falsification of data in response to disclosure requests from organizational entities has emerged yet in any literature stream. Therefore, we appeal to the literature on disclosure itself and derive an exploratory model that incorporates both withholding and falsification as DVs in an umbrella construct known as “privacy protective behavior” that we borrow from Jiang et al. [12].<sup>4</sup> At its core, consistent with a thorough literature review in the domain of data disclosure (Appendix 1), our model considers the privacy tradeof that is most often associated with the privacy calculus paradigm and some extensions thereto—in particular, perceived relevance. Also, in an attempt to consider our third, exploratory research question regarding context, we test for moderating efects of some contextual factors across the model. Fig. 1 and Table 2 summarize our model and hypotheses/proposition, which we explain below.

## 2.1. The privacy tradeof

To the extent that one theoretical perspective has been more broadly embraced than others in attempts to explain data disclosures, that perspective would undoubtedly be the privacy calculus, which assumes that individuals perform a “risk-benefit analysis to assess the outcomes they would face in return for the [data] and respond accordingly” ([4], p. 1001). In the past, the concept of “respond accordingly” within the privacy calculus subdomain has usually been construed as disclosing the data or refusing to do so (i.e., withholding). As discussed earlier, in this study, we extend these previous findings by postulating that another option is conceivable: an individual might provide falsified data.

As can be seen in Appendix 1, of the 36 (out of 42) studies that claimed a reliance on one or more theoretical bases, privacy calculu (or a closely related variant such as utility maximization) was embraced more often than any other theory (by 14 of the studies claiming a theoretical basis, or 39%). Although privacy calculus’s tradeof assumption has been challenged as relying on a sometimes unrealistic assumption of high-efort cognitive processing on individuals’ parts [13], its widespread use in disclosure-focused studies suggests that it should be embraced as the starting point for our model.

The fundamental theoretical argument undergirding privacy cal culus was stated succinctly by [14], p. 327) as follows:

People disclose personal information to gain the benefits of a relationship; the benefits of disclosure are balanced with an assessment of the risks of disclosure…In other words, individuals will exchange personal information as long as they perceive adequate benefits will be received in return—that is, benefits which exceed the perceived risks of information disclosure…

This perspective, which has since been widely embraced across the privacy literature stream, has been adopted in investigations of various forms of data disclosure, and it has proven robust across almost all of them. The few articles that have empirically examined falsification behavior have not relied on this theory, per se, although Xie et al. [11] refer to utility theory and did consider “rewards” (a correlate to perceived benefits) as an antecedent to the provision of accurate personal information. Because theoretical development for falsification has not yet emerged, we postulate a simple converse efect to that for disclosure in these core privacy tradeof hypotheses:

H1. : Higher levels of perceived benefits will be associated with lower levels of a) withholding and b) falsification.

H2. : Higher levels of perceived risks will be associated with higher levels of a) withholding and b) falsification.

Although the privacy tradeof forms the core of our model, we have also included some additional constructs in our investigation of the deeper complexities of privacy decision-making.

## 2.2. Impact of trust on dependent variables

The trust construct has played a role in a large number of studies in the overall IS privacy research stream and, especially, in those studies that have embraced disclosure as their DV. As can be seen in Appendix 1, of the 42 studies employing online disclosure to an organizational entity as a DV, 18 (i.e., 42.8%) included a trust-related construct in their model. None of the studies that measured falsification as a DV included trust in their model, although Xie et al. [11] did consider a requesting firm’s “reputation,” and Metzger [8] showed that reputation did impact trust. Although trust is often viewed as an interpersonal dyadic variable in psychological research, the perspective in privacy studies (and, for that matter, most IS studies in general) has been trust in an organizational entity, and that is the perspective we embrace here.

A consistent finding with the privacy literature stream—which is supported by the entries in Appendix 1—is that individuals are less likely to withhold personal data when they trust the entity in the context of the request. From a theoretical perspective, authors’ arguments are varied. Recently, for example, Bansal et al. [15] relied on prospect theory and argued that trust increases individuals’ perceived utility in disclosing information, and Ozdemir et al. [16] relied on previous research into trustor-trustee relationships to confirm a similar hypothesis regarding disclosure. We expect the same result to hold here, and it stands to reason that the converse efect will hold for withholding and falsification:

H3. : Higher levels of trust will be associated with lower levels of a) withholding and b) falsification.

## 2.3. Perceived benefits and risks

Although both perceived benefits and perceived risks are important components in the privacy calculus tradeof, it remains unclear to what extent the two constructs impact one another. Based on previous precedent (e.g., [17]), we hypothesize that higher levels of perceived benefits will be associated with lower levels of perceived risks. [17], p. 302), who also relied on privacy calculus as the core of their model, explained as follows:

The notion of privacy calculus assumes that there is a consequential tradeof of costs and benefits salient in an individual’s privacy decisionmaking. Overall, the calculus perspective of privacy suggests that when asked to provide personal information to service providers or companies, consumers…behave in ways that they believe will result in the most fa vorable net level of outcomes. Consequently, we argue that consumers are more likely to accept the potential risks that accompany the disclosure of personal information as long as they perceive that they can achieve a positive net outcome. Hence, when a positive outcome of information disclosure is anticipated, risk beliefs are hypothesized to decrease.

We embrace this same logic and hypothesize:

H4. : Higher levels of perceived benefits will be associated with lower levels of perceived risk.

## 2.4. Trust and perceived risk

While the nomological role of trust has not been fully clarified [4], it is widely viewed as being an important input into disclosure decisions What has never been established—not only in the domain of privacy research but also in the broader domain of IS research in general—is the specific relationship between perceived trust, perceived risk, and intended behaviors. Looking across a sample of models that have included these constructs (e.g., [18]; [19]; [20]; [21,114]), one can find numerous combinations of mediation and moderation among these constructs.

In our model, we follow the path of Zimmer et al. [[[114]], who demonstrated in a privacy-related study that perceived trust impacts

![](/api/attachments/FAEUHSJV/fulltext/images/d13a4dc2861310f65c099888256bc346ffb3e195c23a4047115ff279af739be3.jpg)  
Fig. 1. RESEARCH MODEL.

## Table 2

```txt
SUMMARY OF HYPOTHESES/PROPOSITION.

H1: Higher levels of perceived benefits will be associated with lower levels of a) withholding and b) falsification.

H2: Higher levels of perceived risks will be associated with higher levels of a) withholding and b) falsification.

H3: Higher levels of trust will be associated with lower levels of a) withholding and b) falsification.

H4: Higher levels of perceived benefits will be associated with lower levels of perceived risk.

H5: Higher levels of trust will be associated with lower levels of perceived risk.

H6: Higher levels of perceived relevance will be associated with a) lower levels of perceived risk, b) higher levels of perceived benefits, and c) higher levels of trust.

P1: Relationships in H1-H6 (above) will be moderated by contextual factors associated with data disclosure requests.
```

perceived risk (which, in our model, impacts privacy protective beha viors). Zimmer et al. [[[114]](p. 117) argued that “[c]onsumers that trust a website believe that there is more predictability regarding usage of information by the exchange party, reducing transaction risk for the consumer.” They extended those concepts to include disclosure, and we follow their path with our hypothesis:

H5. : Higher levels of trust will be associated with lower levels of perceived risk.

## 2.5. Context

Context has been defined as “situational opportunities and constraints that afect the occurrence and meaning of organizational behavior as well as functional relationships between variables” ([23], p. 112). Nissenbaum [24] noted that there are four interpretations of context that may prove salient: context as technology system or platform. context as business model or business practice, context as sector or industry, and context as social domain. In terms of a definitional boundary, “context encompasses stimuli and phenomen[a] that surround and thus exist in the environment external to the individual” ([15], p. 2, italics added). In that light, one would consider contextual variables to include those that cannot be controlled by an individual decision-maker but which may well impact the outcome of his/her decision-making process. Factors that are internal to the decision-maker (e.g., personality traits such as introversion/extroversion) are not examples of context but are, rather, components that can be considered for inclusion in the basic decision-making model itself.

As was clearly detailed by Hong et al. [23], contextual theory can be developed in one of two ways, although only one is salient for our immediate purposes. The approach that is meaningful in our study is what is termed “single-context theory contextualization,” which assumes at least a moderately well-developed theory exists in a particular domain of interest. By adding or removing core constructs, the theory is then contextualized to ac count for new factors. As can be seen in Fig. 2, this can occur through either “Level 2a,” in which additional contextual factors are added as antecedents or through “Level 2b,” in which contextual factors are added as moderators. As shown below, our model will be contextualized in both ways.<sup>5</sup>

In our model, we incorporate the perceived relevance factor under Level 2a and the moderating impacts of important contextual factors across our model under Level 2b.

Against that background, we now consider the “Level 2a” antecedent in our model: perceived relevance.

## 2.5.1. Contextual antecedent: perceived relevance

As can be seen from the underlined constructs in the “Antecedents to DVs” column of Appendix 1, a large number of contextual factors have been considered in studies associated with data disclosure, but the domain has not converged on a single and theoretically justified grouping. Because it would obviously be impossible to incorporate all of them in a single model, we include only one important contextual antecedent in our model: perceived relevance. We are persuaded by the findings of Zimmer et al. [115] who demonstrated the important role of perceived relevance in explaining perceived risk—our core mediating variable—and we extend their own model by hypothesizing relationships not only with perceived risk but with the full mediating block in our model including also perceived benefits and trust.

## 2.5.2. Perceived relevance and perceived risks

Frequently, an individual who receives a data request assesses it in light of the context of the request: that is, does the individual view the data as salient for the intended transaction(s)? In a 2003 study (Hodder et al., 2003), 1553 out of 1704 (91%) respondents acknowledged that they withheld or submitted incorrect information at a website or mobile app. A reason cited by 67.5% of those 1533 was as follows: “I was afraid of what the site or app would do with the information.” Only limited research attention has been focused on this relationship: Li et al. [25] showed that individuals usually consider the relevance of a particular data element to an intended transaction in the rubric of “exchange fairness,” and this is associated with their “privacy risk belief” in their privacy calculus. Also, Knij nenburg et al. [26] hypothesized that perceived risk is influenced by a subject’s perception of “purpose specificity” in a data request, such that, for a given website, “perceived risk is lower for the type of information that clearly matches the purpose of the website,” and for a given type of information, “perceived risk is lower for the website that has a clear purpose for requesting the information” ([26], p. 4). They found significant support for this hypothesis. Additionally, Zimmer et al. [115] found that perceived relevance strongly influences perceived risk.

While one might argue that such an inference is unwarranted rationally (after all, the risk of providing the data is rationally a function of protections for the data against unintended uses, intrusion, etc., rather than the intended use itself), individuals’ perceptions are not always formed through purely rational assessments (e.g., [27] [28];). On the basis of limited previous findings and the argument above, we hypothesize

H6a. : Higher levels of perceived relevance will be associated with lower levels of perceived risks.

## 2.5.3. Perceived relevance and perceived benefits

Although previous research has included little focus on the relationship between perceived relevance and perceived benefits, we expect that it will be the converse as for perceived risks: that is, individuals will (perhaps irrationally) infer that a transaction itself will provide greater benefits when they perceive the data request as relevant to that transaction. This is largely due to an afective contextual efect: an individual will infer that the situation is a positive one [29] and will therefore infer that greater benefits will accrue. Acknowledging the exploratory inference, we ofer the following hypothesis:

H6b. : Higher levels of perceived relevance will be associated with higher levels of perceived benefits.

## 2.5.4. Perceived relevance and trust

Two studies shed tangential light on the linkage between perceived relevance and trust. Liu et al. [30] found strong support for a relationship between an individual’s understanding of how data would be used after its collection and trust, suggesting that being convinced that the data were relevant for a particular transaction was important in building trust. Suh and Han [31] tested the relationships between several subconstructs of “control”—which is related to relevance due to the individual's ability to dictate that data may be used for only what (s)he deems as relevant purposes—and trust and found mixed support across the various subconstructs. Looking across these two studies, we conclude that, while it appears that there is some evidence of a relationship between perceived relevance and trust, the precise parameters of that relationship have not previously been clarified.

Extending these earlier findings, we postulate that, if an individual perceives that an entity is requesting personal data that are germane neither to an immediate transaction nor to the individual’s ongoing relationship with the entity, (s)he will often perceive that the entity is attempting to garner personal data inappropriately, and this will reduce his or her level of trust in the entity making the request:

H6c. : Higher levels of perceived relevance will be associated with higher levels of trust.

Having established these hypotheses for the “Level 2a” antecedent of perceived relevance, we turn now to our “Level 2b” proposition re garding moderation.

## 2.5.5. Moderation

In the spirit of the approach embraced by Bansal et al. [15], we manip ulate the context in which personal data are requested from individuals and consider the moderating efects of this “manipulated” context on the overall model (i.e., moderating efects on hypotheses H1 through H6). Unlike Bansal et al. [15], we do not consider industry as a representation of context but rather consider two contextual cues that could influence disclosure decisions: the amount of data requested (low or high) (e.g. [32],) and the incentive behind the data request (pecuniary vs. nonpecuniary) (e.g. [33],).

![](/api/attachments/FAEUHSJV/fulltext/images/9c6306f6a619d7449e0aa81e221506c97d89ef0b0e6b673d0c5647cb92783cdb.jpg)  
Fig. 2. Approaches to incorporating context into theorizing.<sup>6</sup>

As can be seen in the “Moderators” column of Appendix 1, only a few contextual items have been considered as moderators in previous research, and no theoretical framework has emerged. In fact, it is even dificult, a priori, to make directional predictions regarding moderating efects. One can, at best, postulate that some contextual efect may be likely, but whether it is likely to strengthen or weaken the numerous relationships within the model is largely dependent on 1) the contextual cue studied (and its manipulation thereof) and 2) the independent and dependent variables being considered in the model. Because of the exploratory nature of our study and because we are interested in testing whether (or not) the context can influence the privacy-related decisionmaking of individuals (especially to explain falsification) rather than decomposing each moderating efect, we state the as a proposition (rather than a hypothesis) the following:

P1: Relationships in H1-H6 (above) will be moderated by contextual factors associated with data disclosure requests.

## 2.6. Control variables

In addition to the tested hypotheses above, we also include some control variables. Many prior studies have gathered some demographic data about the involved subjects, but this has almost always been done without any a priori hypothesizing regarding demographic relationships to other constructs.<sup>7</sup> In keeping with this tradition, we include three demographic facets (age, gender, and education) and one experiential element (Internet experience) as control factors.

Having now established the research model and hypotheses for our study, we turn to a discussion of the research method.

## 3. Method

## 3.1. Research design

We conducted an online experiment to test the proposed model. All participants confronted a real-world situation that would prompt an online request for personal data from a commercial website. Participants were randomly assigned to one of four diferent treat ments. Those treatments correspond to two contextual cues that are interesting to test both from a theoretical and a managerial perspective: 1) the size of the request (i.e., amount of data requested) and 2) the inferred incentive to accrue from fulfilling the request (i.e., why the individual might respond to the data request).

In both experimental conditions, subjects were told to think of their current main mobile phone provider. Half of the participants were told they could create–by filling in an online form–a personal profile on the homepage of the website of their mobile phone provider; by doing so, the subject would be provided with exclusive and personalized information and ofers. The other half of the participants were ofered the opportunity to participate in a lottery sponsored by their mobile phone provider. In both cases, the basic form was identical, although the detailed data that were requested on the form were also manipulated, so that half of the participants received a short form containing only five fields (name, postal address, zip code, city, and email), whereas the other half received a longer form (same fields as the short form and 15 additional fields, which included some items such as mobile preferences and behavior). These forms and details were designed to match the forms that web surfers typically fill in when considering ofers within these contexts (see Appendices 2 and 3).

One hundred and sixty eight web users from a French online access panel participated in the study. The access panel company was told to build a sample of 180<sup>8</sup> French web users who represented the population of interest (mobile phone users) on the basis of two criteria: age and gender. A total of 300 people were contacted to participate in the study. After excluding those who did not answer or participate (104) and those who did not answer all the questions (8), we obtained a total of 188 participants, of whom 20 did not match the quotas, thus resulting in a final sample size of 168 people, with an efective response rate of 168/300 = 56%. In general, a probability sample is better than a convenience sample (e.g., students) whose homogeneous characteristics (e.g., age and education level) sometimes lead to questions regarding the generalizability of results. However, because this study employed randomized assignment to treatment conditions, the most salient question regarding sampling is whether the treatments are germane from the subjects’ perspective. While generalizability is enhanced in this study through the broad characteristics of the sample, it is in fact achieved through randomized treatments and their understandable context. Sample characteristics are presented in Appendix 4.

As the goal of this paper is to investigate Internet users’ privacyrelated decision-making processes, the online survey presented participants with sample screen pages describing the scenario and showing the online forms to be filled in. Screen page samples are efective for eliciting perceptions in typical situations such as those associated with online data disclosure decision-making [34]. To make the situation as realistic as possible, participants were asked the name of their mobile provider at the beginning of the experiment, and the screenshot presented to them later in the survey included the logo of their mobile provider to make participants feel as if they were really on their mobile provider’s website. Because of the policies of the access panel provider, especially the assured anonymity of the participants, subjects could not be asked to provide actual data in the experimental form and could only be asked whether they would provide the requested data elements as shown in the screenshots. Although this might be viewed as a limitation of this study (discussed later in this paper), this approach reduced the time required for administrating the survey, thus diminishing participants’ fatigue and ensuring their willingness to participate.

As a manipulation check, we conducted an ANOVA and found that the data requested were perceived as less relevant in the long form condition (3.30) as compared to the short form (4.58, F = 17.98 and p = 0.000 for relevance), but no diference in terms of relevance appeared when the homepage (4.07) and lottery contexts were compared (3.81, F = 0.746 and $\mathbf { p } = 0 . 3 8 9 )$ .

## 3.2. Measurement

This study measured the model constructs using single or multi-item scales. In accordance with our agreement with the access panel company, the survey could require no more than 10 min in total to be answered, including the time necessary to read the scenario and the forms. Therefore, when possible, we adapted scales from the orthodox literature while choosing the more parsimonious alternatives to reduce the time necessary to answer the questionnaire and to minimize participants’ cognitive burden. As a consequence, we employed no more than four items per scale, and we favored single-item scales whenever possible, especially for easy-to-understand constructs [35] such as perceived relevance.

Specifically, withholding was measured by three items assessing whether the participants would have (or not) disclosed the requested data (see Appendix 5). One of the items was measured on a 1 to 5 scale from 1 (“not at all”) to 5 (“yes certainly”), while the two others were measured using a more classical 1 to 7 Likert format. The falsification item asked whether the participants would have lied about at least one item, a scale adapted from Malhotra et al. [36] and Son and Kim [5]. This item was measured on a 1 to 5 scale from 1 (“not at all”) to 5 (“yes certainly”). Perceived relevance and trust were both measured with one item each assessing, respectively, whether the data requested were perceived to fit the situation and how much the participants trusted the firm requesting those data. Both were measured using a classic Likert 1 to 7 format, with 1 meaning “not agree at all” and 7 “totally agree.” On the basis of the literature in the corresponding research streams and one qualitative study, we developed multi-item scales for perceived risks (3 items) and benefits (4 items). Both used a semantic diferential scale in a 1 to 7 format (i.e., 1 “not at all useful’’ to 7 ‘’very useful’’).

As the scales corresponding to the risks and the benefits were selfdeveloped, we conducted a pilot test with a convenience sample of 53 students to assess the dimensionality and internal reliability of the scales. The EFA concluded that all measures loaded distinctly on their corresponding factors. All Cronbach’s alphas were also above 0.7, thus indicating that the scales were reliable (see Appendix 6).

## 4. Analysis and results

We used a structural equation modeling (SEM) approach to validate the measures and test the relationships between all the constructs. A variance-based partial least squares (PLS) method, using Smart PLS 3.2.6 [37], ofers greater benefits than covariance-based methods, because a least-squares estimation procedure avoids restrictive assump tions such as multivariate normality and residual distributions [38]. As PLS does not generate an overall goodness-of-fit index, model validity is assessed by examining the structural paths and $R ^ { 2 }$ values [39]. In addition, following recent advice from Henseler et al. [40], we provide the standardized root mean square residual (SRMR) for the PLS estimation (0.055), which is below the cutof value of 0.08 suggested by Hu and Bentler [41] by applying covariance-based SEM. Although it has recently been argued that the cutof value of 0.08 is probably too low for PLS-SEM [42], the fact that our SRMR is well below that value shows that our model has a good fit.

STATISTICS FOR CONSTRUCTS.

<table><tr><td></td><td>Number of items</td><td>Loadings (min - max)</td><td>CR</td><td>AVE</td><td>Cronbach&#x27;s alpha</td><td> $R^2$ </td><td> $Q^2$ </td></tr><tr><td>Relevance</td><td>1</td><td>1.000</td><td>1.000</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>Benefits</td><td>4</td><td>0.798 - 0.866</td><td>0.897</td><td>0.686</td><td>0.848</td><td>0.192</td><td>0.114</td></tr><tr><td>Risks</td><td>3</td><td>0.761 - 0.862</td><td>0.858</td><td>0.669</td><td>0.752</td><td>0.349</td><td>0.204</td></tr><tr><td>Trust</td><td>1</td><td>1.000</td><td>1.000</td><td>1.000</td><td></td><td>0.187</td><td>0.177</td></tr><tr><td>Withholding</td><td>3</td><td>0.842 - 0.928</td><td>0.924</td><td>0.802</td><td>0.876</td><td>0.546</td><td>0.392</td></tr><tr><td>Falsification</td><td>1</td><td>1.000</td><td>1.000</td><td>1.000</td><td></td><td>0.210</td><td>0.162</td></tr></table>

## 4.1. Test for common method Bias

We checked for common method bias (CMB) in our data. First, we used a priori methods to limit CMB as suggested by Podsakof et al. [43]. For example, we controlled a priori for item ambiguity through the feedback received from the pilot study with students. The choice of single-item or small number-item scales also reduced the chance that the participants “become fatigued by a seemingly unending stream of questions” ([43], p. 561). We additionally reduced proximity efects by separating items related to a same construct. Finally, we included some reversed items (for example, for the perceived relevance construct) in the survey.

In addition to these a priori methods that should have limited the chances for CMB to occur, we also addressed CMB a posteriori by statistical analysis [44]. There is some controversy in the current literature concerning the eficiency of currently available a posteriori methods in detecting and correcting CMB. Given our restrictions regarding the number of questions to be included in our questionnaire, we could not include a marker variable in addition to the constructs already present. We therefore used two other methods to statistically assess CMB a posteriori—methods that have been widely used in previous studie published in IS journals. We first employed Harman’s single-factor test as suggested by Podsakof et al. [44]. All the variables were loaded into an EFA, and the un-rotated factor solution was examined. CMB may exist if (1) a single factor emerges from the un-rotated factor solution o (2) one general factor accounts for the majority of the covariance in the variables [44]. Neither occurred here, suggesting that the CMB is not an issue in this study. We also followed the approach used by Liang et al. [45]. Using SmartPLS, we specified a method factor together with the original latent variables in the measurement model, and we calculated the squared factor loadings for both the method factor and the substantive factors (i.e., original latent variables). The average variance explained by the substantive factors was approximately 0.92, while that explained by the method factor was approximately 0.10, thus confirming that CMB is not a major concern in our study (see Appendix 7).

## 4.2. Measurement model: instrument validation

PLS models require a two-stage analysis: the measurement model and the structural model [38]. The measurement model, which consists of the relationships between the constructs and the measurement in dicators, assesses the psychometric properties of the scales through item loadings, internal consistency (reliability), and convergent and discriminant validity. The bootstrap sampling procedure enables testing of the magnitude and significance of the loadings using well-established guidelines regarding the convergent validity, discriminant validity, and reliability of the scales ([38] [46];).

In our model, each construct exhibits consistent positive loadings (see Table 3), indicating general convergence. The standardized item construct loadings are high $( > 0 . 7 6 1 )$ and statistically significant at the 0.001 level, with t-statistics well above 1.96. The results also indicate satisfactory item reliability for all the measures. The CRs, similar to Cronbach’s alpha but considering actual factor loadings instead of assuming that each item is equally weighted, range from 0.858 to 0.924 (excluding constructs measured with a single item), thus above 0.70, indicating good internal consistency. In addition, all average variance extracted (AVE) values are greater than the suggested 0.50, thus indicating good convergent validity for the measurement model [47].

We assessed the discriminant validity of reflective scales ([46] [48];) by comparing the AVE of each construct with the shared variances between a single construct and all the other constructs [47]. Comparison of the square root of the AVE (figures on diagonal, Appendix 8) with the correlations among the constructs indicates that the items load higher on their intended construct than on any other construct, thus indicating satisfactory discriminant validity of all the constructs [49]. Recent research on discriminant validity assessment has shown that a new approach based on the multitrait-multimethod matrix, called the heterotrait-monotrait (HTMT) ratio of correlations, provides a performance superior to the previously adopted methods such as the Fornell-Larcker criterion [50]. In our case, the HTMT assessment indicates that all the construct correlations hold for the most conservative criterion HTMT (0.85) (see Appendix 9), thus suggesting that discriminant validity is established also using this more conservative criterion [50]. Overall, these results suggest suficient reliability and convergent/discriminant validity, which allow an interpretation of the structural parameters.

## 4.3. Structural model assessment and hypothesis testing

Following the structural model assessment procedure [42], we first need to check the structural model for collinearity issues by examining the VIF values of all sets of predictor constructs in the structural model. All our VIF values (which range between 1.321 and 1.375) are clearly below the threshold of 5, which indicates that collinearity is not a critical issue in the structural model, and we can accordingly assess the structural model results. The examination of the path coeficients and the variance explained (R<sup>2</sup>) in the endogenous variables enables the assessment of the structural model. Following the recommendation of Chin [38], we tested for the statistical significance of each path coefficient by t-tests using bootstrapping with 500 subsamples. Only one control variable out of the four that were included in the model (i.e., age, gender, education, and Internet experience) is significant: gender significantly influences falsification as women tend to falsify less often than men (beta = - 0.252, p < 0.001).

Tables 3 and 4, and Fig. 3 show the results of the structural model estimation, including the significant standardized path coeficients, tstatistics, and the significance and amount of variance explained (R²) along with the model-predictive relevance with regard to each endogenous construct (Q²). The model explains a substantial amount of variance for both intentions to disclose $( \mathrm { R } ^ { 2 } = 0 . 5 4 6 )$ and falsify $( \mathrm { R } ^ { 2 } = 0 . 2 1 0 )$ , greater than the recommended level of 0.10 (Falk and Miller 1992). The model also explains a great part of the variance of all mediating variables, with $\mathbb { R } ^ { 2 }$ ranging from 0.187 (for trust) to 0.349 (for perceived risks). We also assess the structural model’s predictive va lidity by the $Q ^ { 2 }$ value of the predictive relevance [51,52]. After running the blindfolding procedure [50,53] in SmartPLS, we obtain the $Q ^ { 2 }$ values well above zero for all DVs, indicating the predictive relevance of the PLS path model (see Table 3).

Table 4 TESTS OF HYPOTHESES.

<table><tr><td>Hyp</td><td>Paths (from -&gt; to)</td><td>Beta</td><td>St Dev</td><td>T Stat.</td><td>P-value</td><td>Result</td></tr><tr><td>H1a</td><td>Perceived Benefits -&gt; Withholding</td><td>-0.264</td><td>0.067</td><td>3.932</td><td>***</td><td>Supported</td></tr><tr><td>H1b</td><td>Perceived Benefits -&gt; Falsification</td><td>-0.076</td><td>0.089</td><td>0.854</td><td>&gt;.05</td><td>Not Supported</td></tr><tr><td>H2a</td><td>Perceived Risks -&gt; Withholding</td><td>0.296</td><td>0.063</td><td>4.714</td><td>***</td><td>Supported</td></tr><tr><td>H2b</td><td>Perceived Risks -&gt; Falsification</td><td>0.176</td><td>0.085</td><td>2.063</td><td>*</td><td>Supported</td></tr><tr><td>H3a</td><td>Trust -&gt; Withholding</td><td>-0.378</td><td>0.067</td><td>5.609</td><td>***</td><td>Supported</td></tr><tr><td>H3b</td><td>Trust -&gt; Falsification</td><td>-0.229</td><td>0.092</td><td>2.485</td><td>**</td><td>Supported</td></tr><tr><td>H4</td><td>Perceived Benefits -&gt; Perceived Risks</td><td>-0.225</td><td>0.075</td><td>3.000</td><td>**</td><td>Supported</td></tr><tr><td>H5</td><td>Trust -&gt; Perceived Risks</td><td>-0.161</td><td>0.078</td><td>2.069</td><td>*</td><td>Supported</td></tr><tr><td>H6a</td><td>Perceived Relevance -&gt; Perceived Benefits</td><td>0.438</td><td>0.073</td><td>5.990</td><td>***</td><td>Supported</td></tr><tr><td>H6b</td><td>Perceived Relevance -&gt; Perceived Risks</td><td>-0.351</td><td>0.071</td><td>4.948</td><td>***</td><td>Supported</td></tr><tr><td>H6c</td><td>Perceived Relevance -&gt; Trust</td><td>0.432</td><td>0.069</td><td>6.236</td><td>***</td><td>Supported</td></tr><tr><td></td><td>Gender -&gt; Falsification</td><td>-0.252</td><td>0.061</td><td>4.152</td><td>***</td><td></td></tr></table>

LEGEND (two-tailed tests): $^ { * } \mathrm { ~ p ~ < ~ } 0 . 0 5 ^ { * * } \mathrm { ~ p ~ < ~ } 0 . 0 1 ^ { * * * } \mathrm { ~ p ~ < ~ } 0 . 0 0 1$

![](/api/attachments/FAEUHSJV/fulltext/images/a0159b67c23f2f6c2beb744fe5c8e189f8514bc1b940bb9cd75e57b626fea204.jpg)  
Fig. 3. RESEARCH MODEL RESULTS.

The results support 10 out of our 11 hypotheses (as H1 to H3 are decomposed in two for each DV and H6 has 3 subhypotheses). As we proposed, the perceived relevance of the data requested influences the perceived risks associated with the disclosure of those data (-0.351, $\mathsf { p } < 0 . 0 0 1 )$ , the perceived benefits to do so (0.438, p < 0.001) and the trust in the company asking for those data (0.432, $\mathsf { p } < 0 . 0 0 1 )$ , thus supporting H6 (a, $\mathbf { b } ,$ and c). As also anticipated, both perceived benefits $( - \ 0 . 2 2 5 , \ \mathrm { p \ < \ 0 . 0 1 ) }$ and trust (- 0.161, p < 0.05) significantly influ ence the perceived risks associated with data disclosure, thus sup porting both H4 and H5.

In turn, all three mediating variables (perceived benefits, perceived risks, and trust) significantly influence the decision to withhold personal data (-0.264, $\mathrm { ~ p ~ < ~ } 0 . 0 0 1 , 0 . 2 9 6 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 , - 0 . 3 7 8 , \mathrm { ~ p ~ < ~ } 0 . 0 0 1 ,$ respectively), thus supporting H1a, H2a, and H3a. Trust is the most influential driver of withholding behavior followed by perceived risks (positive impact).<sup>9</sup> Regarding the second DV, contrary to our expectations, perceived benefits have no significant efect $( - 0 . 0 7 6 , \texttt { p } > 0 . 0 5 )$ on the tendency to falsify the data. However. both trust and perceived risks have significant relationships with falsification, with trust having a stronger negative efect (-0.229, p < 0.01) than the positive efect of perceived risks (0.176, p < 0.05). Taken together, these findings provide no support for H1b but validate both H2b and H3b.

## 4.4. Tests for moderating efects (P1)

To test P1 (moderating efects), we conducted two post hoc multigroup analyses (MGA) to compare our model based on the amounts of data requested to the applicants (low vs. high) and on the incentive (pecuniary vs. nonpecuniary) behind the data request (i.e., lottery vs. homepage) (see Appendix 10 for details on this analysis).

The results regarding the support for P1 are rather complex as 11 moderation efects are tested for two diferent contextual cues. The bottomline results can be seen in Table 5. Figs. 4 and 5 show the full model for each of the manipulated conditions in our $2 \times 2$ experiment. Globally, P1 is partially supported as we found some diferences between the diferent treatments (i.e., hypotheses validated in one context but not the other).

According to the MGA results (Table 5), one statistically significant diference (underlined in dark gray) is noted. Interestingly, the efect of trust on falsification is significantly diferent when considering the incentive behind the data request $( \mathbf { p } = 0 . 0 1 6 ,$ , dark gray) so that the efect holds in the lottery (i.e., pecuniary) context (-0.435, p < 0.001) but not in the homepage (i.e., nonpecuniary) context $( - 0 . 0 6 2 , \mathrm { p } \ > \ 0 . 0 5 )$ . In the lottery context, therefore, trust has a strong negative impact on falsification (i.e., the more people trust the company asking them personal details in order for them to participate in a lottery, the less they will tend to falsify). This does not seem to be the case in the homepage context where trust does not result in a reduced tendency to falsify.

Also noteworthy is the diference in the efect of trust on falsification when considering the amount of the data requested, although this diference is not statistically validated in the MGA results $( { \bf p } = 0 . 2 7 9 ,$ light gray). Here, the efect of trust holds when the form to be filled in is long (- 0.268, $\rho < 0 . 0 5 )$ but not when only a small quantity of information is asked (- 0.165, p > 0.05). Therefore, when the amount of information to provide is high, trust has an important impact on the tendency to falsify, but this is no longer the case when the amount of requested information is small.

Three other hypotheses involving perceived risks as a driver or a consequence also yield some interesting results, although they do not show statistical significance in the MGA results (light gray). In parti cular, when looking at the influence of risks on falsification, we can see that this efect holds only for the long form $( 0 . 2 2 7 , \mathrm { ~ p ~ < ~ } 0 . 0 5 )$ and in the homepage context (0.235, $\mathsf { p } < 0 . 0 5 )$ . In both conditions, perceived risk results in a stronger tendency to falsify the data, which does not seem to happen in a lottery context or when the amount of requested information is small.

Table 5  
MGA RESULTS FOR BOTH CONTEXTUAL CUES (SIZE OF REQUEST AND INFERRED INCENTIVE OF THE REQUEST).

<table><tr><td rowspan="2">Hyp</td><td rowspan="2">Paths (from -&gt; to)</td><td colspan="6">MGA Results for Size of Request</td><td colspan="6">MGA results for Inferred Incentive of the Data Request</td></tr><tr><td>β for Short Form</td><td>Sig</td><td>β for Long Form</td><td>Sig</td><td>p-value of the difference</td><td>Sig. diff. ?</td><td>β for Homepage Context</td><td>Sig</td><td>β for Lottery Context</td><td>Sig</td><td>p-value of the difference</td><td>Sig. diff. ?</td></tr><tr><td>H1a</td><td>Perceived Benefits -&gt; Withholding</td><td>-0.197</td><td>*</td><td>-0.325</td><td>**</td><td>0.818</td><td>No</td><td>-0.256</td><td>**</td><td>-0.276</td><td>**</td><td>0.556</td><td>No</td></tr><tr><td>H1b</td><td>Perceived Benefits -&gt; Falsification</td><td>-0.058</td><td></td><td>-0.067</td><td></td><td>0.472</td><td>No</td><td>-0.196</td><td></td><td>0.058</td><td></td><td>0.920</td><td>No</td></tr><tr><td>H2a</td><td>Perceived Risks -&gt; Withholding</td><td>0.389</td><td>***</td><td>0.227</td><td>**</td><td>0.904</td><td>No</td><td>0.328</td><td>***</td><td>0.259</td><td>***</td><td>0.712</td><td>No</td></tr><tr><td>H2b</td><td>Perceived Risks -&gt; Falsification</td><td>0.164</td><td></td><td>0.227</td><td>*</td><td>0.626</td><td>No</td><td>0.235</td><td>*</td><td>0.087</td><td></td><td>0.198</td><td>No</td></tr><tr><td>H3a</td><td>Trust -&gt; Withholding</td><td>-0.303</td><td>**</td><td>-0.428</td><td>***</td><td>0.820</td><td>No</td><td>-0.332</td><td>**</td><td>-0.426</td><td>***</td><td>0.740</td><td>No</td></tr><tr><td>H3b</td><td>Trust -&gt; Falsification</td><td>-0.165</td><td></td><td>-0.268</td><td>*</td><td>0.279</td><td>No</td><td>-0.062</td><td></td><td>-0.435</td><td>***</td><td>0.016</td><td>Yes</td></tr><tr><td>H4</td><td>Perceived Benefits -&gt; Perceived Risks</td><td>-0.143</td><td></td><td>-0.320</td><td>**</td><td>0.119</td><td>No</td><td>-0.188</td><td></td><td>-0.246</td><td>*</td><td>0.342</td><td>No</td></tr><tr><td>H5</td><td>Trust -&gt; Perceived Risks</td><td>-0.232</td><td>*</td><td>-0.096</td><td></td><td>0.805</td><td>No</td><td>-0.100</td><td></td><td>-0.212</td><td>**</td><td>0.241</td><td>No</td></tr><tr><td>H6a</td><td>Perceived Relevance -&gt; Perceived Benefits</td><td>0.399</td><td>***</td><td>0.451</td><td>***</td><td>0.354</td><td>No</td><td>0.517</td><td>***</td><td>0.364</td><td>***</td><td>0.860</td><td>No</td></tr><tr><td>H6b</td><td>Perceived Relevance -&gt; Perceived Risks</td><td>-0.384</td><td>***</td><td>-0.310</td><td>***</td><td>0.306</td><td>No</td><td>-0.413</td><td>***</td><td>-0.308</td><td>***</td><td>0.232</td><td>No</td></tr><tr><td>H6c</td><td>Perceived Relevance -&gt; Trust</td><td>0.392</td><td>***</td><td>0.427</td><td>***</td><td>0.410</td><td>No</td><td>0.510</td><td>***</td><td>0.357</td><td>***</td><td>0.861</td><td>No</td></tr><tr><td></td><td>Gender -&gt; Falsification</td><td>-0.199</td><td>*</td><td>-0.329</td><td>***</td><td>0.153</td><td>No</td><td>-0.218</td><td>**</td><td>-0.315</td><td>***</td><td>0.211</td><td>No</td></tr></table>

![](/api/attachments/FAEUHSJV/fulltext/images/c4eb3bdbde935862f4189c9632fbf0c418ec94421d1684333e8021158b42f0b9.jpg)  
Fig. 4. Model results for size of the request (short vs. long forms).

![](/api/attachments/FAEUHSJV/fulltext/images/8b672b49c2bebe8296a6c64c0029b14c952e0c834d06afdd60d9e1cefd8fec41.jpg)  
Fig. 5. Model results for inferred incentive of the request (homepage vs. lottery context).

In addition, the impact of perceived benefits on perceived risks is validated only in the long form $( - \ 0 . 3 2 0 , \ \mathbf { p } \ < \ 0 . 0 1 )$ and in the lottery (- 0.246, $\rho < 0 . 0 5 )$ conditions. Finally, trust translates into reduced perceived risks only when the number of details requested is low $( - ~ 0 . 2 3 2 ,$ $\underline { { \mathsf { p } } } \ < \ 0 . 0 5 )$ and in the lottery (i.e., pecuniary) context $( - 0 . 2 1 2 , \mathtt { p } < 0 . 0 1 )$ .

Globally, the drivers of withholding are afected by neither the amount of data requested nor the incentive (pecuniary vs. nonpecuniary) behind the data request, whereas the two drivers of falsification $( \mathrm { i . e . , }$ trust and perceived risks) are impacted by both contextual cues (i.e., data quantity and inferred incentive). In addition, both antecedents of perceived risks are also significantly afected by the amount of information asked and the incentive (pecuniary vs. nonpecuniary) behind the data request.

## 5. Discussion

This study makes three important contributions to the literature stream, each of which can be linked to one of research questions of the study as stated at the outset.

The first research question was “To what extent does a privacy tradeof – based on perceived benefits, perceived risks, and trust – explain a) individuals’ data disclosure decisions (i.e., withholding) and b) the phenom enon of individuals providing falsified data in privacy-related decisions?” First, it was seen that this model explained a significant portion (54.6%) of the variance in withholding. In addition, context matters in explaining withholding: with respect to the amount of data requested, in the “short form” condition, a reduction of risks is most likely to reduce withholding, and this is followed by an increase in trust. In the “long form” condition, trust is most important in reducing withholding, with perceived benefits following closely behind. With respect to the inferred incentive, in the lot tery (pecuniary) context, trust is the most important driver, followed by perceived benefits. In the personalized homepage (nonpecuniary) context, trust and a reduction in perceived risks are the most important factors in reducing withholding. Second, as one of the first studies within the privacy domain to consider the notion of falsification as a DV, our explanation of 21% of the variance in that construct is notable and represents one of the main contributions of this study. We ofer potential explanations for this phenomenon that will be worth considering in future privacy-related studies. In this area also, context matters, with the influence of trust on falsification being very diferent depending on the context of the data request (amount of data requested and incentive behind the request).

Of particular interest are the findings related to the influence of benefits on each of our DVs, especially their non-significant efect on falsification. In our model, we incorporated trust as an antecedent to privacy-related decisions, in addition to the classical privacy-calculus elements (benefit/risk trade-of). Our findings confirm trust as the most important driver of both withholding and falsification decisions. Specifically, falsification seems to be driven by a trust/risk trade-of, as opposed to the classical privacy calculu (benefit/risk) paradigm. Interestingly, when trust is taken out of the model, benefits, in turn, have a significant efect on falsification<sup>10</sup>. Trust thus play a suppressor efect: when people trust how firms are handling their data, no matter how much benefit they will be given in exchange of the data, it will significantly reduce the chances that they provide falsified information. This finding complements previous literature on privacy, especially the work by

Norberg et al. [54] which already discussed the corresponding influence of trust and risks on disclosure behavior. Contrary to the popular paradigm that consider the calculus perspective of privacy (benefit/risk trade-of) as ‘the most useful framework for analyzing contemporary consumer privacy concerns’ ([14] p. 326; [55], p. 139), this framework may only or mainly be useful when there is no (or not enough) trust in the firm collecting the data.

The second research question was “To what extent can individuals perceptions of risks, benefits, and trust in privacy-related decisions be explained by the contextual factor of perceived relevance?” In contrast with many privacy studies that view perceived benefits, perceived risks, and even trust as purely exogenous variables, this study indeed considered a contextual antecedent to each of these constructs (i.e., perceived relevance) (see Fig. 2). Because all these relationships proved to be significant, we confirm the interest of considering contextual antecedents to these key privacy-related decision drivers. In addition, we found that our context-specific antecedent (perceived relevance) influenced perceived benefits, risks, and trust in the four treatment conditions of our manipulated context, thus providing some generalizability to this context-specific driver.

The third, exploratory research question was “How does the context of a data request impact individuals’ decisions regarding disclosure and falsification?” We found that our manipulated contextual cues had a moderating efect on four of the 11 hypotheses in our model. This provides suggestive evidence regarding the importance of contextual factors in decisions associated with data disclosure and falsification and indicates the need for additional research in this area.

Researchers should find that their future eforts can be enlightened by these findings regarding our three research questions.

## 5.1. Implications for research and future research avenues

As noted above, this study is the first to look across a nomological model of important drivers of privacy-related decisions while considering the fact that individuals may respond to data requests in various ways: by honestly supplying the requested information, by refusing to provide the information, or by providing false information. As such, it makes a substantive contribution to the literature stream on its own. However, its greatest contribution may be as a motivator for future research that builds on this nomological model and, especially, considers how other contextual factors may come into play. Additionally, future researchers can benefit by considering other cognitive processing models that go well beyond those considered in this study.

## 5.1.1. Context

Because this is one of the first studies to consider the option of falsification in individuals’ response patterns, we intentionally limited our consideration of contextual factors to an exploratory zone (Research Questions 2 and 3). Following the path outlined by Hong et al. [23], we considered one contextual antecedent (perceived relevance) and the potential moderating efects of two manipulated variables (size and inferred incentive of the request). Even with this modest objective, we found the following:

The context-specific antecedent (perceived relevance) has a very significant impact on perceived benefits, perceived risks, and trust in all manipulated conditions.

• For four of the 11 hypotheses in our model, relationships were moderated by manipulated contexts, although in only one of these conditions (inferred incentive of the data request as a moderator of the relationship between trust and falsification), the diference between both treatments (i.e., between the lottery [pecuniary incentive] and the homepage [nonpecuniary incentive]) was significant at the 0.05 level.

These findings suggest that in our exploratory contextual initiative, the contextual antecedent (perceived relevance) has proven to have a significant role in explaining individuals’ response patterns. We therefore recommend that future researchers be especially mindful of its role when crafting their own models.

The findings from our work also suggest that although our initial foray into the moderating efects should be viewed as exploratory, we already show some interesting results that will need to be confirmed in future research. As can be seen in the “Moderators” column of Appendix 1, we are obviously engaged in a domain that has received little previous re search attention. Of the 42 studies listed in the appendix, in our judgment, only six considered any contextual factors (based on the definition proffered earlier) as moderators ([56]; [15,57]; [58] [22,59];). Most importantly, only one of these six studies [15] found evidence of significant moderating efects based on the contextual factors they tested. This points to a need for a deep focus in future research. Future studies could benefit from both additional attention to contextual antecedents and moderators (“Levels 2a and 2b,” respectively, per Hong et al. [23]. We discuss each.

Contextual antecedents. As was noted earlier, this study has gone further than most studies in the privacy domain by considering one contextual antecedent to both perceived risks and perceived benefits in our model. While our approach was obviously a fruitful one (our model explained 35% and 19% of the variance in perceived risks and perceived benefits, respectively), it is obvious that additional work could be done to strengthen the explanatory structure associated with these two important privacy calculus inputs. For example, it might be possible to provide an even stronger explanation for perceived risk by considering other factors that simultaneously were being processed by a decision-maker. One might conjecture that all other things being equal, an individual might perceive more risk in a certain data-seeking situation if (s)he was already in an anxious afective state or under some level of time pressure [29]. Regarding perceived benefits, we also embraced a somewhat simplistic ap proach in light of the paucity of past research in this domain, by including only one antecedent variable (perceived relevance) in our model. An expanded consideration of perceived benefits might well include an addi tional level of calculus that addressed both the size of probable benefits as well as the likelihood of those benefits accruing, thus inducing a stochastic modeling process. Such an approach would obviously deepen the model and also enable interesting experimental treatments in which, for example, decisions could be manipulated to test the impact of both size and prob ability in impacting benefits directly and other DVs indirectly.

Contextual moderators. In looking across the research stream as depicted in Appendix 1 “Moderators” column and considering this study, one can see that only a few contextual moderators have been tested to date:

• Industry/type of data ([56]; [15]; [58] [22];)

Website attributes [57,59]

• Requester properties [56]

Amount of data – this study

• Intended use of data/disclosure incentives – [56], this study.

Obviously, the most frequently considered moderator has been the type of information (sometimes implied by the industry). This is indeed an important area for consideration, as it is certainly conceivable that an individual’s perceptions and responses across an entire research model could difer based on such a context. For example, consider again our introductory scenario regarding the Pizza Shack and a data request for consumers’ birthdays. It is quite conceivable that, had a financial institution (rather than a pizza delivery service) been the requesting entity, individuals might have responded diferently to a request for their birthday or, even more importantly, more sensitive information such as their income. Driving such a diference in response patterns could well have been diferent perceptions of benefits/risks, diferent levels of trust, etc.—that is, many of the components that comprised our basic decision-making model.<sup>11</sup>

Although these five areas seem to be those on which researchers have focused to date in assessing contextual moderating efects, the list is obviously far from an exhaustive one. Future research would benefit from a broader consideration of such potential moderators, which could well include constructs such as government regulation, industry norms, and technological alternatives (e.g., difering platforms and diferent devices).

Having noted the extreme importance of addressing context in future research, we now turn to some specific areas in which our present model—whether embraced as a base for future studies on its own or incorporated into broader models—merits attention: the role of trust, additional drivers for falsification, and additional consideration of de mographic and experiential relationships.

## 5.1.2. Focal areas in the present model

The role of trust. Smith et al. [4] noted that, while trust is widely viewed as an important construct in privacy research, its specific role in terms of its antecedents and direct/moderating efects has not been clearly established in the past. Based on some previous (in some cases, conflicting) findings and our own argumentation, we posited four hypotheses that included trust. For all four, our study did confirm the postulated direction, and in all cases, the relationship exhibited the strength associated with statistical significance. This suggests that our model’s treatment of the trust construct was generally correct, but obviously much additional work is required to fully develop the relationships.

We recommend, therefore, that additional work be done to clarify the precise nature of the trust construct(s) that are salient in privacy-related decisions. We noted earlier that trust is usually viewed as a dyadic construct in psychological research, and most theoretical development therefore relies on relationships from that perspective. However, in IS privacy research, trust is usually conceptualized as an individual’s trust in an entity that is requesting data. We suggest that this distinction needs even further clarification, as the components of privacy-related trust may be even more complex than in other areas addressed in the general IS research stream. For example, there may be some parameters associated with data types or combinations thereof that would be reflected in privacy-related trust but that would not be salient in other contexts. We can only speculate regarding the nature of all such dimensions, but the meager support for the trust-related hypotheses in this study – an outcome consistent with the mixed findings in the overall IS privacy research domain – suggests that much additional attention is needed.

Additional drivers for falsification. The importance of the falsification construct in privacy research cannot be overstated, as one phenomenon often cited by privacy observers is that of a “privacy paradox." in which individuals’ stated that privacy concerns are inconsistent with their actual behavior [4]. As was aptly noted by [6], p. 1171), “[r]esearchers may mistakenly identify the privacy paradox phenomenon in their studies if their..design does not assess the accuracy of the data provided." In that spirit, we note that much more could be done to further our understanding of falsification behavior in response to data requests. Although the vast majority of research has been in an organizational (rather than online or consumer) context, the discipline of business ethics has devoted some attention to the factors associated with this phenomenon (e.g., [60,61]; [62] [63];). Additionally, some applied psychologists have considered some contextual factors associated with falsification through various communication media [64]. Obviously, much additional investigation would be required to expand our theoretical modeling of falsification behavior as a response to data requests, and even more work would be needed to test those models. We certainly acknowledge the nontrivial nature of further investigation of this phenomenon, but we also highlight the relatively unexplored nature of this important context in privacy research.

Additional consideration of demographic and experiential relationships. A few prior studies (e.g., [65] [9];) have noted demographic diferences in individuals’ perceptions and responses in privacy-related contexts. In this study, we found that one demographic variable (gender) had a significant efect on falsification. We are unaware, however, of any prior theoretical development that would explain such a diference. One positive interpretation of the very limited impact of demographic variables could be that our model is indeed a robust one. However, the development of strong theory to explain potential diferences associated with gender and other demographic variables could prove a significant contribution to the research stream.

These three areas— the role of trust, additional drivers for falsification, and additional consideration of demographic and experiential relation ships—are ripe for additional consideration in all situations in which our current model is embraced as a baseline. However, we also wish to highlight and question a basic assumption that undergirds not only most research to date in this particular domain but also in many other IS contexts: the level of cognitive efort that individuals devote to their decision-making processes.

## 5.1.3. Consideration of low-efort cognitive processing

Although not overtly mentioned in the published privacy articles to date, a covert assumption is that individuals who are engaging in privacy calculus are embracing what is viewed as “high efort” cognitive processing, in which they attempt to rationally evaluate the benefits and risks. Indeed, a perusal of the article in Appendix 1 reveals no examples of studies that challenge this basic premise (Note that the level of efort in cognitive processing constitutes a decision-making state at the individual level. It is not an external contextual factor as defined earlier). Yet there are many situations in which individuals instead embrace “low efort” cognitive processing routes; for example, individuals in happy moods are much more likely to expend low amounts of cognitive efort and instead to rely on heuristics and biases in making decisions [29]. Within the larger privacy research stream, a few authors (e.g., [27] [25,66–68];) have begun to investigate privacy-related decisions under conditions associated with low-efort processing [13].

[69] [70];)’s heuristic-systematic model and Petty and Wegener [71]’s elaboration likelihood model (ELM) both distinguish more and less effortful information processing and decision-making—with the ELM terming the high-efort route as “central” and the low-efort route as “peripheral.” For any given decision, an individual can be expected to rely on a mixture of high and low efort cognitive processing. In a privacy related context, high-efort processing is characterized by “responses to external stimuli result[ing] in deliberate analyses, which lead to fully informed privacy-related attitudes and behaviors” ([13], pp. 641–642). Lowefort processing is characterized by “relatively little cognitive efort or conscious awareness” and a “relatively greater reliance on automatic heuristics” ([13], p. 642). Such heuristics may be grounded in, or accompanied by, peripheral cues, biases, and misattributions.<sup>12</sup>

The relative apportionment of cognitive resources to the low- and high-efort routes is determined by factors such as afect (mood and emotion), cognitive resources, motivation, and time constraints. This suggests that researchers could plow a fruitful research path by conducting a series of experiments that manipulate subjects’ relative allo cation of resources to low- and high-efort processes, with measurement of cognitive, perceptual, and behavioral responses associated with each. This could be done within the context of basic model of this study, although it may well be found that, especially for decisions that are driven primarily by low-efort processes, some of the constructs in our model may become inoperative. For example, rather than form conscious perceptions of risks and benefits, individuals who are driven primarily by low-efort processing may instead make disclosure/falsification decisions based primarily on heuristics or biases, thus bypassing several components of the basic model.<sup>13</sup> Obviously, future studies focused on disclosure and/or falsification would benefit greatly from a consideration of both low-efort and high-efort cognitive processing.

## 5.2. Implications for practice

In addition to the implications for the research stream (above), this study has significant implications for practice in several areas. We highlight five.

First, those who request personal data from individuals should be aware that many of the same factors that drive data disclosure also—in converse—drive falsification of data. Thus, data requesters should be wary of accepting self-reported data from individuals at face value. In some cases, it may be important to cross-validate certain data elements (for example, some credit reporting firms are now ofering instantaneous identity verifications for a small fee). It is also worth noting, however, that falsification of data was seen to decline significantly when individuals trust the firm requesting the data and perceive that the risks have been mitigated. This suggests that entities may profitably invest both in education (regarding risks) and in data protection (along with marketing thereof). Our study on drivers of data falsification provides a meaningful way for organizations to be aware of the possibility of false data during data collection along with some factors that might mitigate it (e.g., enhanced trust and reduced risks). Interestingly, our results show that the impact of each of those two factors might difer significantly depending on the situation in which data are requested (size of request and inferred incentive in our case). Organizations should therefore adapt their investments and communicate diferently depending on the con texts in which they request data from their customers.

Second, the fact that trust afects privacy-related decisions such as withholding and falsification, although not entirely new (at least regarding its influence on disclosure), is an important finding. This sug gests that firms should be encouraged to invest resources in initiatives that lead to a general enhancement of trust across society. Such initiatives may include industry codes of conduct, privacy seals, consumer education, or even lobbying for regulations that provide a baseline level of protection for all consumers. To the extent that trust is enhanced across the consumer spectrum, all organizations that rely on consumer data will benefit

As the European Union’s General Data Protection Regulation (GDPR) took efect in mid-2018, many of its legally mandated actions for data collection and handling are forcing European firms that handle citizens’ data to embrace steps that will improve trust levels [72]. Even U.S. firms that handle Europeans’ data (e.g., credit card transaction processors) are being impacted [73] and will need to consider registering under the EU-U.S. “Privacy Shield” program, which will dictate most of the same provisions [74].

Third, as can be seen in Table 5, the efect of trust on falsification depends both on the size of the data request and on the inferred in centive for the request, such that higher trust levels are associated with reduced falsification only in a lottery context and when the quantity of requested data asked is large. The influence of perceived risks on falsification shows a similar although slightly diferent pattern: a reduced level of perceived risks is associated with reduced falsification when personalization is ofered in exchange for the data and when the quantity of requested data is large. The same is true for withholding, with its drivers having diferent weights depending on the context. For example, in the lottery and long form contexts, withholding is driven first by trust followed by benefits, whereas for a short form, a reduction of risks is the most likely to reduce withholding. These complex relationships suggest that initiatives to maintain or enhance trust or to reduce the perceived risks associated with data disclosure must be formulated carefully; practitioners should consider these boundary conditions to maximize their initiatives’ eficiency.

Fourth, the (non)influence of perceived benefits is noteworthy. One might conjecture that people falsify data because they want to reap the benefits out of disclosure while minimizing the associated risks. This does not seem to be totally the case, however, as perceptions of more benefits do not lead to a reduction in falsification. Therefore, although proposing interesting benefits to consumers can certainly increase their disclosures, it will not reduce the risk of data falsification. Practitioners initiatives to enhance benefits should thus be considered carefully to avoid misleading returns.

Fifth, relevance of the data matters. Big data principles could lead practitioners to try to collect as much data as possible from their customers, but consumers care about the legitimacy of each granular data request. In many cases, less data may lead to more disclosure and, more importantly, to a higher level of accuracy.

## 5.3. Potential limitations

While this study makes significant contributions to the literature, there are three potential limitations, though we argue that none of them stands as a significant threat to the validity of the study.

First, because our sampling relied on a panel research firm, we were constrained from gathering identifiable data–and thus real disclosure–from the subjects. We therefore measured their stated inten tions, rather than their actual behavior, in our model. This approach is fairly common in the privacy research stream, and the distinct diferences that were observed in stated intentions suggest that findings of this study are robust ones (see Table 5).

Second, in an attempt to minimize the length of our data collection time with subjects, we relied on single-item measures for some of the constructs in our model. Although there are support [35] and precedent (e.g., certain constructs in [65] [75,76];) for this approach, we do ac knowledge that multi-item measures are frequently used by many IS researchers. This choice was constrained by our partnership with the access panel company and our desire to capture participants’ behavior and decision-making process in a real-life situation. Given the observed validity of our measurement model, this is not a significant limitation, but we do recommend that researchers who extend this research stream consider devoting additional attention to the measurement of the con structs in the model.

Third, the solicitation of our sample from a single country (France) may be argued by some to limit the generalizability of the results. However, the fact that the subjects were recruited through an online panel, that they exhibited broad demographic dispersion, and that they were randomly assigned to diferent treatment conditions, all lend credence to the generalizability of the results. While it might be fruitful for the study to be replicated with a worldwide sample, the strong relationships that were demonstrated in the model, coupled with the fact that objectives of the study did not include an evaluation of cross-cultural diferences, suggest that the use of subjects from a single country was not a substantive limitation.

## 6. Conclusion

In this study, we attempted to move the privacy research domain forward by demonstrating the importance of considering not only individuals’ data disclosures but also falsification thereof. We hope that other researchers will benefit from our steps and will now work with us to extend this important subdomain of IS privacy research.

## Special Note

This article is dedicated to H. Jef Smith and his family.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

Appendix 1 Articles in Top IS Journals with Disclosure/Falsification to an Organizational Entity as Dependent Variable<sup>14</sup>

<table><tr><td>Reference</td><td>Salient dependent variables (DVs)</td><td>Antecedents to DVs (sig. indicated by *):n-1: $^{15}$  Immediate; n-2: Secondary (if any);n-3: Tertiary (if any);n-4: Quaternary (if any)</td><td>Moderators considered (if any)</td><td>Theoretical framework(s) relied upon (if any)</td></tr><tr><td>[56]</td><td>Willingness to provide access to personal health info (implied disclosure)</td><td>n-1: Health status emotion *</td><td>Type of info, intended purpose, requesting stakeholder $^{16}$ </td><td>Privacy boundary theory, risk as feelings</td></tr><tr><td>[88]</td><td>Opt-in intention to adopt electronic health records (implied disclosure)</td><td>n-1: Concern for Information Privacy *, post-attitude *n-2: Argument frame *, issue involvement *</td><td>Concern for information privacy</td><td>Elaboration likelihood model</td></tr><tr><td>[89]</td><td>Intention – willingness to be profiled online for personalized service/advertising (implied disclosure)</td><td>n-1: Previous online privacy invasion (mixed *), privacy concern, importance of privacy policies *, importance of information transparency *n-2: Demographics (gender, education, income), previous online privacy invasion *, privacy concern *, importance of privacy policies *</td><td></td><td>Utility maximization (akin to privacy calculus) $^a$ </td></tr><tr><td>[18]</td><td>Intention to disclose health information</td><td>n-1: Health info privacy concern *, trust in the health website b *, prior positive experience with the website *n-2: Health info privacy concern, prior positive experience with the website *, risk beliefs health info *n-3: Perceived health info sensitivity *, previous online privacy invasion*n-4: Personality (5 factors) (mixed *), poor health status *</td><td>Industrial context(health, finance, e-commerce website)</td><td>Utility theory (akin to privacy calculus)a</td></tr><tr><td>[15]</td><td>Intention to disclose information</td><td>n-1:- Trust in the website b *- Positive experience with the website *- Internet privacy concerns *n-2:- Positive experience with the website *- Internet privacy concerns (mixed *)- Previous online privacy invasion *- Personality (Big 5) (mixed *)</td><td>Privacy concerns</td><td>The contextualization of the theory of reasoned action and its synthesis with prospect theory</td></tr><tr><td>[90]</td><td>Intention to disclose</td><td>n-1: Trust (in the website)b *n-2:- Argument quality/Adequacy of a privacy policy statement(regarding collection, errors, secondary use, improper access) *- Peripheral cues (website info quality, availability of company info, design appeal, reputation) *</td><td>Privacy concerns</td><td>Elaboration likelihood model</td></tr><tr><td>[91]</td><td>Facebook content sharing and disclosure (through wall posts, private messages)</td><td>n-1: Facebook privacy policy change *, growth in Facebook friendship network (mostly *)</td><td></td><td>Privacy calculus, communication privacy managementa</td></tr><tr><td>[92]</td><td>Self-reported knowledge-sharing behaviors on blogs (disclosures)</td><td>n-1: Social ties *, reciprocity *, trustb *, information privacy concernsn-2: reciprocity (on social ties) *, social ties on trust *, trust on info privacy concerns *</td><td></td><td>Social capital theory</td></tr><tr><td>[93]</td><td>Privacy-preserving and sharing actions on Facebook</td><td>n-1: Gender (mixed *),friends' behaviors *</td><td></td><td>Social capital theory, activity theory of aging, social role theory</td></tr><tr><td>[94]</td><td>Privacy self-disclosure behaviors (self-reported)</td><td>n-1: Attitude *n-2: Extroversion *, Perceived critical mass *, Perceived Internet risk *</td><td>Privacy</td><td>Information disclosure behavior, expectancy-value theory</td></tr><tr><td>[95]</td><td>Self-disclosure extent (declared behavior)</td><td>n-1: SNS usage rate *n-2: Attitude toward using the SNS *n-3: Extroversion *, Perceived Networking Assistance *, Perceived Cyber Risk *, Social Influence *</td><td>Gender</td><td>Learning theories</td></tr><tr><td>[96]</td><td>Willingness to delegate (information disclosure to apps through Facebook)</td><td rowspan="2">n-1: Transactional privacy concerns *n-2: Privacy attributes (info collection and profile control) *n-1: Intrapersonal characteristics (censorship attitude, self-efficacy, behavioral-based inertia, previous similar experience), perceptions of the controlling agent (trustworthinessb, privacy concerns), perceived system characteristics (granularity, efficacy, inconvenience)n-2: Reputation</td><td rowspan="2">General privacy concerns</td><td rowspan="2">Communication privacy management theoryPrivacy calculus, social exchange theorya(Note: Model tested across three domains, so significance levels not captured here)</td></tr><tr><td>[97]</td><td>Intentions to use identity ecosystem (disclosures)</td></tr><tr><td>[98]</td><td>Willingness to provide personal info</td><td>n-1: Internet privacy concerns *, Internet trustb *, personal Internet interest *, perceived Internet privacy risk *n-2: Perceived Internet privacy risk *</td><td></td><td>Privacy calculusa</td></tr><tr><td>[99]</td><td>Willingness to provide personal information to transact on the Internet (PPIT)</td><td>n-1: Privacy concerns related to information abuse (PCIA) *, privacy concerns related to information finding (PCIF) *, perceived need for governmental surveillance (PNGS) *, government intrusion concerns (GIC)n-2: Linkages between PCIA and PNGS *, PCIF and GIC *, PCIA and GIC *</td><td></td><td>Privacy calculus, asymmetric information theorya</td></tr><tr><td>[100]</td><td>Willingness to disclose</td><td>n-1: Perceived privacy risk *,privacy policy permissivenessn-2: Privacy policy permissiveness (on perceived privacy risk) *</td><td></td><td></td></tr><tr><td>[75]</td><td>Actual disclosure</td><td rowspan="2">n-1: Manipulations: no privacy assurance; assurance through privacy statement *; assurance through privacy statement and seal; variable money incentives *.Measured: propensity to trust *, prior experience with info misuse *, prior Internet shopping experience *, privacy concernsn-1:- Interpersonal privacy identity (info and interaction management)*- Privacy calculus/benefits (socialization, self-expression, pleasing others) *</td><td rowspan="2">None</td><td>Choice theory using utility function (akin to privacy calculus)a</td></tr><tr><td>[115]</td><td>Intentions to disclose (data items and parties who gain access)</td><td>Privacy calculusa</td></tr><tr><td>[57]</td><td>Willingness to share information</td><td>n-1: Disposition to value privacy (DTVP) *, level of personalization *,transparency features</td><td>DTVP, transparency features</td><td>Information boundary theory</td></tr><tr><td>[101]</td><td>Intention to disclose</td><td>n-1: Perceived privacy *, general privacy concerns *, general institutional trustbn-2: Perceived risks of information disclosure *, perceived benefits of information disclosure *n-3: Information sensitivity *</td><td>Affect</td><td>Privacy calculusa</td></tr><tr><td>[102] - Study 2</td><td>Disclosure</td><td>n-1: Privacy concern, privacy settings *, age *, gender, ethnicity, perceived risk *, perceived benefit *, mobile computing self-efficacy (MCSE) *n-2: privacy concern *, MCSE *</td><td></td><td>Privacy calculus, trust theorya</td></tr><tr><td>[103]</td><td>Willingness to communicate personal health info</td><td>n-1: Expected positive personal outcomes *, expected positive community outcomes *, privacy concern *, affective commitment</td><td>Affective commit-ment</td><td>Privacy calculus, affective commit-menta</td></tr><tr><td rowspan="3">[112]</td><td rowspan="3">Self-disclosure (self-reported)</td><td>n-1: Perceived privacy risk *, convenience *, relationship building *, self-presentation, enjoyment *</td><td></td><td rowspan="3">Privacy calculusua</td></tr><tr><td>n-2: Trust in other OSN members, perceived control *, trust in OSN provider b *</td><td></td></tr><tr><td>n-3: Perceived control</td><td></td></tr><tr><td>[104]</td><td>Disclosure behavior and protection behavior</td><td>n-1: Privacy concerns including 4 foci (Control, protection and regulation, trust, and responsibility)</td><td></td><td>(Note: Qualitative study through focus groups)</td></tr><tr><td rowspan="3">[59]</td><td rowspan="3">Behavioral intention</td><td>n-1: Perceived benefits *, site-specific privacy concerns *</td><td rowspan="2">Website reputation, website familiarity</td><td rowspan="3">Privacy as control, levels of privacy, developmental theory of privacy</td></tr><tr><td>n-2: Website reputation b *, disposition to privacy *, website familiarity *</td></tr><tr><td>n-3: Privacy experience *, gender, age, education</td><td></td></tr><tr><td>[105]</td><td>Disclosure (intention)</td><td>n-1: PC *, Liking *, Motive consistency *, Perceived Privacy control *, Covariates: gender, shopping experience *, past invasion of privacy *, task type</td><td>- Perceived privacy control</td><td>Multidimensional development theory, cognitive appraisals, emotions</td></tr><tr><td rowspan="3">[58]</td><td rowspan="3">Willingness to provide info</td><td>n-2: Motive consistency, Perceived Privacy control</td><td></td><td>Privacy calculusua</td></tr><tr><td>n-1: Likelihood of using online personalization *</td><td>- Industry Domain</td><td rowspan="2">Past Experience</td></tr><tr><td>n-2: Privacy Concerns * and Privacy Protection, Perceived Quality of Personalization *</td><td></td></tr><tr><td>[106]</td><td>Disclosure breadth and depth, sensitive vs. less sensitive disclosure</td><td>n-1: Gender and age *, account rating *, number of friends *, number of blogs *, blog length</td><td>- Gender and age</td><td>Communication privacy management theory</td></tr><tr><td rowspan="4">[107]</td><td rowspan="4">Use of instant messaging (implied disclosure)</td><td>n-1: Behavioral intention to use IM *</td><td></td><td>Social exchange theory</td></tr><tr><td>n-2: Attitude toward IM technology *</td><td></td><td rowspan="3">(Note: US and China samples)</td></tr><tr><td>n-3: Information privacy concerns *, desire for awareness *</td><td></td></tr><tr><td>n-4: Masculinity, uncertainty avoidance, power distance, collectivism (Mixed *-- see Fig. 4 in article)</td><td></td></tr><tr><td rowspan="3">[36]</td><td rowspan="3">Behavioral intention to disclose information</td><td>n-1: Trusting beliefs b *, risk beliefs *, type of info requested *</td><td></td><td></td></tr><tr><td>n-2: Internet privacy concerns *</td><td></td><td></td></tr><tr><td>n-3: Type of info requested *</td><td></td><td></td></tr><tr><td rowspan="3">[108]</td><td rowspan="3">Intention to share information with web vendor</td><td>n-1: Perceived web risk, trusting intention (willingness to depend on web vendor), trusting beliefs in web vendor b</td><td></td><td></td></tr><tr><td>n-2: Perceived vendor information, perceived site quality, structural assurance of the web</td><td></td><td></td></tr><tr><td>(Note: Due to model's complexity, significance levels not shown here)</td><td></td><td></td></tr><tr><td rowspan="2">[16]</td><td rowspan="2">Information disclosure (declared)</td><td>n-1: Benefits *, Trust *, PC *</td><td>None</td><td>Antecedents - privacy concerns - outcomes framework</td></tr><tr><td>n-2: Risks *, Privacy Experiences * and Privacy Awareness *</td><td></td><td></td></tr><tr><td rowspan="6">[109]</td><td rowspan="6">Disclosure (declared)</td><td>n-1: Social influence *</td><td>Culture (Fr vs. UK)</td><td>Social exchange theory, social penetration theory, cross-cultural theory (individualism-collectivism)</td></tr><tr><td>- Perceived benefit (reciprocity) *</td><td></td><td></td></tr><tr><td>- Perceived trust b *</td><td></td><td></td></tr><tr><td>- Risk beliefs *</td><td></td><td></td></tr><tr><td>- Perceived collectivism *</td><td></td><td></td></tr><tr><td>- Education and Age</td><td></td><td></td></tr><tr><td rowspan="2">[110]</td><td rowspan="2">Behavioral intention</td><td>n-1: Attitude *, PC *</td><td></td><td></td></tr><tr><td>n-2: PC, Individual differences (alienation, self-esteem, computer anxiety) *, Attributes of an information practice (permission, transfer, interaction with IT) *</td><td></td><td></td></tr><tr><td rowspan="2">[111]</td><td rowspan="2">Online self-disclosure (intention)</td><td>n-1: Switching cost *, Dependency *, Cognitive Trust b *, Affective Trust b</td><td></td><td>Constraint-based (lock-in) and dedication-based (trust-building) mechanisms, social identity theory</td></tr><tr><td>n-2: Cognitive social identity *, Affective social identity (mixed *), Evaluative social identity *</td><td></td><td></td></tr><tr><td>[5]</td><td>Info privacy-protective responses, including refusal to disclose, misrepresentation c</td><td>n-1: Information privacy concerns (mixed *), perceived justice, societal benefits</td><td></td><td>Justice theory</td></tr><tr><td>[113]</td><td>Sharing on Facebook</td><td>n-1: Context, value</td><td></td><td>(Note: Qualitative study based on interviews and observation)</td></tr><tr><td rowspan="3">[67]</td><td rowspan="3">Intentions to disclose</td><td>n-1: Website trust b *, positive affect *, negative affect *, website privacy *</td><td></td><td>Cognitive consistency theory, motivational model</td></tr><tr><td>n-2: Internet security (mixed *)</td><td></td><td></td></tr><tr><td>(Note: Also some relationships between n-1 variables (all *))</td><td></td><td></td></tr><tr><td rowspan="3">[55]</td><td rowspan="3">Intention to disclose personal information</td><td>n-1: Privacy benefits *, Privacy risks *</td><td></td><td>Privacy calculus, justice theory a</td></tr><tr><td>n-2: Compensation (mixed *), Industry self-regulation *, government regulation (mixed *)</td><td></td><td></td></tr><tr><td>(Note: ran model twice - for pull and push; some control variables were significant, but not included here)</td><td></td><td></td></tr><tr><td rowspan="3">[68]</td><td rowspan="3">Self-disclosures on social networking websites</td><td>n-1: Expression, Self-presentation *, Social acceptance *, Reciprocity *, Social rejection, Privacy risk</td><td></td><td>Direct causation theory, affect heuristic theory</td></tr><tr><td>n-2: Affect toward self-disclosures *, Affect toward SN websites (mixed *)</td><td></td><td></td></tr><tr><td>(Note: For "indirect" model. Study also tested a "direct" model.)</td><td></td><td></td></tr><tr><td rowspan="2">[113]</td><td rowspan="2">Actual disclosure</td><td>n-1: Disclosure intent *, benefits</td><td>Dyadic condition</td><td>Social response theory, principle of reciprocity</td></tr><tr><td>n-2: Trust b *, privacy *</td><td></td><td></td></tr><tr><td rowspan="2">[[114]]</td><td rowspan="2">Disclosure intention (email address, postal address, weight, and medical history)</td><td>n-1: Usefulness, Attitude *</td><td>Type of data</td><td>Theory of reasoned action, transaction cost economics</td></tr><tr><td>n-2: Trust b *, Risk *, Relevance *</td><td></td><td></td></tr></table>

<sup>a</sup>Studies that use the privacy calculus (or a closely related variant) as their main theoretical framework  
<sup>b</sup>Studies that include Trust (or a trust-related construct) in their model  
<sup>c</sup>Studies that include Falsification (or a closely related variant) in their model

![](/api/attachments/FAEUHSJV/fulltext/images/15fe1b96e19c5872df78a2173c5687e88953fb57d729ba691883b46b3036e3e0.jpg)

![](/api/attachments/FAEUHSJV/fulltext/images/628799aae985f4c4efabfa386f06ebba4346824c271684762701dcf287aca44c.jpg)  
Appendix 2 Sample Screenshots corresponding to Data Request Forms (Original version)

Short Form/Homepage/One of the main mobile service providers in France (Orange)

Créez votre ESPACE PERSONNEL Vous y RETROUVEREZ toutes les informations sur VOTRE COMPTE, des informations EXCLUSIVES et de nombreuses offres PERSONNALISEES Inscrivez-vous dès maintenant en COMPLETANT le formulaire ci-dessous

![](/api/attachments/FAEUHSJV/fulltext/images/ffa960e597fb12487c424cd4024ed3bd31ed186e237a7f3b33db00be7d452912.jpg)

Long Form/Lottery/Another main mobile service provider in France (SFR) Pour participer à notre grand JEU-CONCOURS Et peut être gagner un des nombreux LOTS en jeu Dont un SAFARI au Kenya COMPLETEZ le formulaire ci-dessous

![](/api/attachments/FAEUHSJV/fulltext/images/3dd9b24e1a0ac55f3c6ed496b9d8c6133a9670bb867f740c18f6fe83ba6cef8a.jpg)

Je désire recevoir les bons plans de vos partenaires

Appendix 3 Data Request Forms translated in English

Short Form/Homepage

Logo of the participant's

mobile phone supplier (e.g., Orange)

<table><tr><td colspan="3">To get a personal space where you would find all details about your account along with exclusive information and personalized offers,Create your profile by filling in the form just below:</td></tr><tr><td></td><td></td><td><img src="/api/attachments/FAEUHSJV/fulltext/images/55f273ab885477f5c0664091e126b0ba53d487586679aaad57732f465f72ea0e.jpg"/></td></tr><tr><td colspan="3">(* required information)</td></tr><tr><td>Name*:</td><td>Address*:</td><td></td></tr><tr><td>City*:</td><td>Zip Code*:</td><td></td></tr><tr><td>Email Address*:</td><td>@</td><td></td></tr><tr><td>I wish to receive offers by email</td><td>YES</td><td>NO</td></tr><tr><td>I wish to receive offers from partner companies</td><td>YES</td><td>NO</td></tr></table>

Long Form/Lottery

Logo of the participant's mobile phone supplier (e.g., SFR)

<table><tr><td>To participate in our Lottery and be able to win several prizes including a Kenya Safari, Fill in the form just below:</td><td><img src="/api/attachments/FAEUHSJV/fulltext/images/d70f12e5690a099278afc39e2c5eafcced0fed67af395f77709b57946a3a060c.jpg"/></td></tr></table>

(\* required information)

Title \*:

Last Name \*: First Name \*:

Address \*:

City\*: Zip Code\*:

Email Address \*: @

Phone Number \*:

Country \*:

Birth Date:

Education \*:

Profession \*:

Marital Status \*: Number of children:

Hobbies \*:

Time spent phoning \*:

Cell phone date of purchase \*:

To sponsor a friend. indicate his/her email address here\*: @

I wish to receive offers from partner companies 6 YES NO

Appendix 4 Sample characteristics

<table><tr><td>Variables</td><td>Values</td><td>%</td></tr><tr><td colspan="3">Demographics</td></tr><tr><td rowspan="2">Gender</td><td>M</td><td>51%</td></tr><tr><td>F</td><td>49%</td></tr><tr><td rowspan="5">Age (years)</td><td>18-24</td><td>30%</td></tr><tr><td>25-34</td><td>30%</td></tr><tr><td>35-44</td><td>17%</td></tr><tr><td>45-54</td><td>14%</td></tr><tr><td>55+</td><td>9%</td></tr><tr><td rowspan="3">Profession</td><td>White collars</td><td>18%</td></tr><tr><td>Blue collars</td><td>42%</td></tr><tr><td>Inactive (incl. students)</td><td>40%</td></tr><tr><td rowspan="4">Education level</td><td>Less than high school</td><td>24%</td></tr><tr><td>Graduate</td><td>50%</td></tr><tr><td>Postgraduate</td><td>15%</td></tr><tr><td>PhD</td><td>11%</td></tr><tr><td colspan="3">Experiences</td></tr><tr><td>Internet experience</td><td>Beginner</td><td>6%</td></tr><tr><td rowspan="2"></td><td>Familiar</td><td>64%</td></tr><tr><td>Expert</td><td>30%</td></tr><tr><td rowspan="3">E-mail usage</td><td>More than once a day</td><td>69%</td></tr><tr><td>Once a day</td><td>22%</td></tr><tr><td>More than once a week</td><td>9%</td></tr><tr><td rowspan="4">Web usage</td><td>More than once a day</td><td>73%</td></tr><tr><td>Once a day</td><td>14%</td></tr><tr><td>More than once a week</td><td>11%</td></tr><tr><td>Even less</td><td>2%</td></tr><tr><td rowspan="4">Online purchase experience(number of online purchases/year)</td><td>No</td><td>6%</td></tr><tr><td>Less than 5</td><td>29%</td></tr><tr><td>5 to 20</td><td>35%</td></tr><tr><td>More than 20</td><td>30%</td></tr></table>

Appendix 5 Survey items and statistics

<table><tr><td colspan="5">Measures</td></tr><tr><td>For each of the following statements state if you tend to agree or not</td><td>Scale</td><td>Mean</td><td></td><td>SD</td></tr><tr><td>(REL1) I don&#x27;t see why the company is asking me some of these details (inv.)</td><td>1 - 7</td><td>4.19</td><td></td><td>1.973</td></tr><tr><td>(TRU1) I trust the company asking these information</td><td>1 - 7</td><td>4.35</td><td></td><td>1.898</td></tr><tr><td>Do you consider filling in this form as ...</td><td>Scale</td><td></td><td>Mean</td><td>SD</td></tr><tr><td>(RIS1) Secure (7) to Insecure (1) (inv.)</td><td>1 - 7</td><td>4.98</td><td></td><td>1.735</td></tr><tr><td>(RIS2) Unsafe (7) to Safe (1)</td><td>1 - 7</td><td>4.23</td><td></td><td>1.799</td></tr><tr><td>(RIS3) Risky (7) to Not risky (1)</td><td>1 - 7</td><td>3.89</td><td></td><td>1.613</td></tr><tr><td>(BEN1) Beneficial (7) to Not beneficial (1)</td><td>1 - 7</td><td>4.04</td><td></td><td>1.732</td></tr><tr><td>(BEN2) Useful (7) to Not useful (1)</td><td>1 - 7</td><td>4.39</td><td></td><td>1.672</td></tr><tr><td>(BEN3) Valuable (7) to Not valuable (1)</td><td>1 - 7</td><td>4.13</td><td></td><td>1.589</td></tr><tr><td>(BEN4) Appealing (7) to Unappealing (1)</td><td>1 - 7</td><td>3.64</td><td></td><td>1.754</td></tr><tr><td>For each of the following statements state if you tend to agree or not</td><td>Scale</td><td></td><td>Mean</td><td>SD</td></tr><tr><td>(WIT1) I am willing to answer those questions (inv.)</td><td>1 - 7</td><td>4.69</td><td></td><td>1.910</td></tr><tr><td>(WIT2) I see no issue in providing those details (inv.)</td><td>1 - 7</td><td>4.49</td><td></td><td>1.901</td></tr><tr><td>(WIT3) I would have filled in and validated this form (inv.)</td><td>1 - 5</td><td>3.54</td><td></td><td>1.303</td></tr><tr><td>(FAL1) I would have given false information to some of the items in the form</td><td>1 - 5</td><td>1.94</td><td></td><td>1.134</td></tr></table>

Appendix 6 Results of the Exploratory Factor Analysis (EFA) from the pilot test

<table><tr><td rowspan="2" colspan="2">Items</td><td rowspan="2">Communalities</td><td colspan="2">Loadings</td><td rowspan="2">Cronbach&#x27;s alpha</td></tr><tr><td>BEN</td><td>RISK</td></tr><tr><td>BEN1</td><td>Beneficial (7) to Not beneficial (1)</td><td>0.734</td><td>0.897</td><td></td><td>0.80</td></tr><tr><td>BEN2</td><td>Useful (7) to Not useful (1)</td><td>0.731</td><td>0.887</td><td></td><td></td></tr><tr><td>BEN3</td><td>Valuable (7) to Not valuable (1)</td><td>0.680</td><td>0.783</td><td></td><td></td></tr><tr><td>BEN4</td><td>Appealing (7) to Unappealing (1)</td><td>0.678</td><td>0.767</td><td></td><td></td></tr><tr><td>RIS1_i</td><td>Secure (7) to Insecure (1) (inv.)</td><td>0.662</td><td></td><td>0.727</td><td>0.76</td></tr><tr><td>RIS2</td><td>Unsafe (7) to Safe (1)</td><td>0.767</td><td></td><td>0.796</td><td></td></tr><tr><td>RIS3</td><td>Risky (7) to Not risky (1)</td><td>0.737</td><td></td><td>0.776</td><td></td></tr><tr><td>Percentage of Variance</td><td></td><td></td><td>51%</td><td>19%</td><td></td></tr></table>

Appendix 7 Test for Common Method Bias (CMB)

<table><tr><td>Construct</td><td>Indicator</td><td>Item Factor Loadings</td><td>Variance explained by the Factors</td><td>Method Factor Loadings</td><td>Variance explained by the Methods</td></tr><tr><td>Perceived Relevance</td><td>REL1</td><td>1.000</td><td>1.000</td><td>0.273</td><td>0.074</td></tr><tr><td rowspan="4">Perceived Benefits</td><td>BEN1</td><td>0.866</td><td>0.750</td><td>0.282</td><td>0.079</td></tr><tr><td>BEN2</td><td>0.834</td><td>0.695</td><td>0.320</td><td>0.102</td></tr><tr><td>BEN3</td><td>0.817</td><td>0.667</td><td>0.360</td><td>0.130</td></tr><tr><td>BEN4</td><td>0.798</td><td>0.636</td><td>0.298</td><td>0.089</td></tr><tr><td rowspan="3">Perceived Risks</td><td>RIS1</td><td>0.761</td><td>0.579</td><td>-0.315</td><td>0.099</td></tr><tr><td>RIS2</td><td>0.862</td><td>0.744</td><td>-0.334</td><td>0.112</td></tr><tr><td>RIS3</td><td>0.829</td><td>0.687</td><td>-0.287</td><td>0.083</td></tr><tr><td>Trust</td><td>TRU1</td><td>1.000</td><td>1.000</td><td>0.273</td><td>0.075</td></tr><tr><td rowspan="3">Withholding</td><td>WIT1</td><td>0.928</td><td>0.862</td><td>0.319</td><td>0.102</td></tr><tr><td>WIT2</td><td>0.914</td><td>0.836</td><td>0.298</td><td>0.089</td></tr><tr><td>WIT3</td><td>0.842</td><td>0.708</td><td>0.339</td><td>0.115</td></tr><tr><td>Falsification</td><td>LY1</td><td>1.000</td><td>1.000</td><td>-0.296</td><td>0.088</td></tr><tr><td>Average</td><td></td><td>0.921</td><td>0.852</td><td>0.165</td><td>0.098</td></tr></table>

Appendix 8 Discriminant validity: Correlations and Squared roots of AVEs [47]

<table><tr><td></td><td>REL</td><td>TRU</td><td>RIS</td><td>BEN</td><td>WIT</td><td>FAL</td></tr><tr><td>REL</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>TRU</td><td>0.438</td><td>0.828</td><td></td><td></td><td></td><td></td></tr><tr><td>RIS</td><td>-0.519</td><td>-0.448</td><td>0.818</td><td></td><td></td><td></td></tr><tr><td>BEN</td><td>0.432</td><td>0.428</td><td>-0.409</td><td>1.000</td><td></td><td></td></tr><tr><td>WIT</td><td>-0.530</td><td>-0.558</td><td>0.568</td><td>-0.612</td><td>0.896</td><td></td></tr><tr><td>FAL</td><td>-0.329</td><td>-0.259</td><td>0.294</td><td>-0.332</td><td>0.468</td><td>1.000</td></tr></table>

Appendix 9 Discriminant validity: The HeteroTrait-MonoTrait (HTMT) ratio ( [50])

<table><tr><td></td><td>REL</td><td>TRU</td><td>RIS</td><td>BEN</td><td>WIT</td></tr><tr><td>TRU</td><td>0.432</td><td></td><td></td><td></td><td></td></tr><tr><td>RIS</td><td>0.596</td><td>0.464</td><td></td><td></td><td></td></tr><tr><td>BEN</td><td>0.472</td><td>0.464</td><td>0.545</td><td></td><td></td></tr><tr><td>WIT</td><td>0.561</td><td>0.649</td><td>0.698</td><td>0.642</td><td></td></tr><tr><td>FAL</td><td>0.329</td><td>0.332</td><td>0.342</td><td>0.273</td><td>0.501</td></tr></table>

REL: Perceived Relevance of the data request  
BEN: Disclosure Benefits  
RIS: Perceived Risks of data disclosure  
TRU: Trust in the Company requesting the data  
WIT: Withholding Intention  
FAL: Falsification Intention

## Appendix 10 Multi-Group Analysis

The first step in comparing two groups is to establish measurement invariance [50]. We followed the three-step Measurement Invariance of Composite Models (MICOM) procedure suggested by Henseler et al. [50] for each of the contextual cues separately (see Appendices APP10-1, APP10- 2). By using identical indicators per model and treating the data in the same manner, we established the first necessary step, configural invariance, in the MICOM procedure, both for the size of the request (amount of data) and the inferred incentive. We also established the second step, compositional invariance, for both contextual cues, by observing that the composite score correlation mean is larger than the 5% quantile of the empirical distribution of correlation between scores [50].

Continuing with the third step of the MICOM procedure, we checked the variances (MICOM step 3.a) and mean values (MICOM step 3.b) between the construct scores. We first checked, for each contextual cue, if the observations that belong to the first group (low quantity and lottery) have the same variance in their latent variable score as the observations of the second group (high quantity and homepage) (MICOM step 3.a). We confirmed that variances are equal in both cases, therefore establishing at least partial measurement invariance. The last step (MICOM step 3.b) requires testing if means are equal in both groups for each contextual cue. This step is verified for the inferred incentive (lottery versus homepage) but not for the size of the request. We have thus established full measurement invariance for the inferred incentive and partial measurement invariance for the size of the request, which allows us to conduct a MGA and compare standardized path coefi cients across groups for both contextual cues. In particular, the group with low data quantity (n = 42) was compared to the group with high data quantity (n = 42), and separately, the group with the lottery context (n = 42) was compared to the group with the homepage context (n = 42) using the MGA function of SmartPLS (see Table 5).

Table A10.1 MICOM Results for Data Quantity Groups (Low vs. High)

<table><tr><td>Composite</td><td>C value (= 1)</td><td>95% Confidence Interval</td><td>Compositional Invariance?</td></tr><tr><td>Perceived Relevance</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr><tr><td>Perceived Benefits</td><td>0.999</td><td>[0.994; 1.000]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>0.988</td><td>[0.987; 1.000]</td><td>Yes</td></tr><tr><td>Trust</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr><tr><td>Withholding</td><td>1.000</td><td>[0.998; 1.000]</td><td>Yes</td></tr><tr><td>Falsification</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr></table>

<table><tr><td>Composite</td><td>Logarithm of the composite's variances ratio (= 0)</td><td>95% Confidence Interval</td><td>Equal variances?</td></tr><tr><td>Perceived Relevance</td><td>-0.122</td><td>[-0.289; 0.260]</td><td>Yes</td></tr><tr><td>Perceived Benefits</td><td>-0.246</td><td>[-0.395; 0.384]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>-0.129</td><td>[-0.440; 0.405]</td><td>Yes</td></tr><tr><td>Trust</td><td>0.069</td><td>[-0.359; 0.332]</td><td>Yes</td></tr><tr><td>Withholding</td><td>-0.119</td><td>[-0.337; 0.359]</td><td>Yes</td></tr><tr><td>Composite</td><td>Difference of the composite's mean value (= 0)</td><td>95% Confidence Interval</td><td>Equal mean values?</td></tr><tr><td>Perceived Relevance</td><td>-0.626</td><td>[-0.301; 0.290]</td><td>No</td></tr><tr><td>Perceived Benefits</td><td>0.213</td><td>[-0.294; 0.290]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>-0.264</td><td>[-0.308; 0.277]</td><td>Yes</td></tr><tr><td>Trust</td><td>0.310</td><td>[-0.323; 0.284]</td><td>No</td></tr><tr><td>Withholding</td><td>0.291</td><td>[-0.294; 0.274]</td><td>No</td></tr><tr><td>Falsification</td><td>-0.268</td><td>[-0.312; 0.312]</td><td>Yes</td></tr></table>

Table A10.2 MICOM Results for Inferred Incentive Groups (Lottery vs. Homepage)

<table><tr><td>Composite</td><td>C value (= 1)</td><td>95% Confidence Interval</td><td>Compositional Invariance?</td></tr><tr><td>Perceived Relevance</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr><tr><td>Perceived Benefits</td><td>0.998</td><td>[0.994; 1.000]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>0.999</td><td>[0.986; 1.000]</td><td>Yes</td></tr><tr><td>Trust</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr><tr><td>Withholding</td><td>1.000</td><td>[0.998; 1.000]</td><td>Yes</td></tr><tr><td>Falsification</td><td>1.000</td><td>[1.000; 1.000]</td><td>Yes</td></tr></table>

<table><tr><td>Composite</td><td>Logarithm of the composite&#x27;s variances ratio (= 0)</td><td>95% Confidence Interval</td><td>Equal variances?</td></tr><tr><td>Perceived Relevance</td><td>0.172</td><td>[-0.290; 0.255]</td><td>Yes</td></tr><tr><td>Perceived Benefits</td><td>0.005</td><td>[-0.429; 0.408]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>-0.217</td><td>[-0.415; 0.395]</td><td>Yes</td></tr><tr><td>Trust</td><td>-0.099</td><td>[-0.337; 0.344]</td><td>Yes</td></tr><tr><td>Withholding</td><td>-0.010</td><td>[-0.400; 0.373]</td><td>Yes</td></tr><tr><td>Falsification</td><td>-0.235</td><td>[-0.534; 0.548]</td><td>Yes</td></tr></table>

<table><tr><td>Composite</td><td>Difference of the composite&#x27;s mean value (= 0)</td><td>95% Confidence Interval</td><td>Equal mean values?</td></tr><tr><td>Perceived Relevance</td><td>-0.127</td><td>[-0.301; 0.313]</td><td>Yes</td></tr><tr><td>Perceived Benefits</td><td>0.124</td><td>[-0.306; 0.275]</td><td>Yes</td></tr><tr><td>Perceived Risks</td><td>-0.169</td><td>[-0.302; 0.313]</td><td>Yes</td></tr><tr><td>Trust</td><td>0.065</td><td>[-0.310; 0.284]</td><td>Yes</td></tr><tr><td>Withholding</td><td>0.115</td><td>[-0.322; 0.296]</td><td>Yes</td></tr><tr><td>Falsification</td><td>-0.111</td><td>[-0.268; 0.290]</td><td>Yes</td></tr></table>

## References

[1] J. Lima, Lving Consumers Could Destroy Big Data. June 10. 2015, available at (2015) http://www.cbronline.com/news/internet-of-things/consumer/lyingconsumers-could-destrov-big-data-4597794)

[2] B. Lobel, Quality of Data Sufers As Consumers Are Reluctant to Disclose Persona Information, (2015) smallbusiness.co.uk.

[3] M. Hodder, E. Churchill, J. Cobb, Customercommons.org/research, Lying and Hiding in the Name of Privacy, (2013) accessed on December 5, 2017.

[4] H. Smith, T. Dinev, H. Xu, Information privacy research: an interdisciplinary review, Mis Q. 35 (4) (2011) 989–1015.

[5] J.Y. Son, S.S. Kim, Internet users’ information privacy-protective responses: A taxonomy and a nomological model, Mis Q. 32 (3) (2008) 503–529.

[6] M.J. Keith, S.C. Thompson, J. Hale, B. Lowry, C. Greer, Information disclosure on mobile devices: Re-examining privacy calculus with actual user behavior, Int. J. Hum, Stud, 71 (12) (2013) 1163–1173

[7] M. Malheiros, S. Preibusch, M.A. Sasse, "Fairly truthful": the impact of perceived efort, fairness, relevance, and sensitivity on personal data disclosure, Trust and Trustworthy Computing: Lecture Notes in Computer Science 7904 (2013), pp. 250–266.

[8] M.J. Metzger, Efects of site, vendor, and consumer characteristics on web site trust and disclosure, Communic, Res, 33 (3) (2006) 155–179

[9] K.B. Sheehan, M. Hoy, Flaming, complaining, abstaining: how online users respond to privacy concerns, J. Advert. 28 (3) (1999) 37–51.

[10] J. Wirtz, M.O. Lwin, J.D. Williams, Causes and consequences of consumer online privacy concern, Int. J. Sery, Ind, Manag, 18 (4) (2007) 326–348.

[11] E. Xie, H.H. Teo, W. Wan, Volunteering personal information on the internet: effects of reputation, privacy notices, and rewards on online consumer behavior.

Mark. Lett. 17 (1) (2006) 61–74.

[12] Z. Jiang, C.S. Heng, B.C.F. Choi, Research note - privacy concerns and privacyprotective behavior in synchronous online social interactions, Inf. Syst. Res. 24 (3) (2013) 579–595

[13] T. Dinev, A.R. McConnell, H.J. Smith, Informing privacy research through in formation systems, psychology, and behavioral economics: thinking outside the “APCO” box, Inf. Syst. Res. 26 (4) (2015) 639–655.

[14] MJ. Culnan, RJ. Bies. Consumer privacy: balancing economic and justice con: siderations, J. Soc, Issues 59 (2) (2003) 323–342.

[15] G. Bansal, F.M. Zahedi, D. Gefen, Do context and personality matter? Trust and privacy concerns in disclosing private information online, Inf. Manag. 53 (1) (2016) 1–21.

[16] Z.D. Ozdemir. H.J. Smith, J.H. Benamati, Antecedents and outcomes of information privacy concerns in a peer context: an exploratory study, Eur. J. Inf, Syst. 26 (2017) 642–660.

[17] T. Dinev, H. Xu, H.J. Smith, P. Hart, Information privacy and correlates: an empirical attempt to bridge and distinguish privacy-related concepts. Eur. J. Inf. Syst 22 (2013) 295–316.

[18] G. Bansal, F.M. Zahedi, D. Gefen, The impact of personal dispositions on information sensitivity, privacy concern and trust in disclosing health information online, Decis. Support Syst. 49 (2) (2010) 138–150.

[19] O.B. Buttner, A.S. Goritz, Perceived trustworthiness of online shops, Journal of Consumer Behavior 7 (1) (2008) 35–50.

[20] A.I. Nicolaou, D.H. McKnight, Perceived information quality in data exchanges: efects on risk, trust, and intention to use, Inf. Syst. Res. 17 (4) (2006) 332–351

[21] L.P. Robert, A.R. Dennis, Hung Y-TC, Individual swift trust and knowledge-based trust in face-to-face and virtual team members, J. Manag. Inf. Syst. 26 (2) (2009) 241-279.

[22] W. Hong, F.K.Y. Chan, J.Y.L. Thong, L.C. Chasalow, G. Dhillon, A framework and

guidelines for context-specific theorizing in information systems research, Inf. Syst. Res. 25 (1) (2014) 111–136.

[23] H. Nissenbaum, Respect for context as a benchmark for privacy online: what it is and isn’t, in: C. Dartiguepeyrou (Ed.), The Futures of Privacy, Fondation Télécom, Institut Mines-Télécom, 2014, pp. 19–30.

[24] H. Li, R. Sarathy, H. Xu, Understanding situational online information disclosure as a privacy calculus, J. Comput. Inf. Syst. 51 (1) (2010) 62–71.

[25] B.P. Knijnenburg, A. Kobsa, H. Jin, Counteracting the negative efect of form auto completion on the privacy calculus, Thirty Fourth International Conference on Information Systems Milan, 2013, (2013).

[26] A. Acquisti, J. Grossklags, ) Privacy and rationality in individual decision making, IEEE Secur. Priv. 3 (2005) 26–33.

[27] P. Goes, Information systems research and behavioral economics, Mis Q. 37 (3) (2013) 3–8.

[28] R. Petty, J.T. Cacioppo, Communication and Persuasion: Central and Peripheral Routes to Attitude Change. Springer-Verlag. New York. 1986.

[29] C. Liu, J.T. Marchewka, J. Lu, C.S. Yu, Beyond concern: a privacy-trust-behavioral intention model of electronic commerce. Inf. Manag, 42 (1) (2004) 127–142

[30] B. Suh, I. Han, The impact of customer trust and perception of security control on the acceptance of electronic commerce. Int. J. Electron. Commer. 7 (3) (2o03) 135–161.

[31] L. Kanuk, C. Berenson, Mail surveys and response rates: a literature review, J. Mark, Res, (1975) 440–453.

[32] A. Acquisti, L.K. John, G. Loewenstein, What is privacy worth? J. Legal Stud. 42 (2) (2013) 249–274.

[33] J. Finch, The vignette technique in survey research, Sociology 21 (1) (1987) 105–114.

[34] L. Bergkvist, J.R. Rossiter, The predictive validity of multiple-item versus singleitem measures of the same constructs, J. Mark. Res. 44 (2) (2007) 175–184.

[35] K.N. Malhotra, S.S. Kim, J. Agarwal, Internet users’ information privacy concerns (IUIPC): the construct, the scale, and a causal model, Inf. Syst. Res. 15 (4) (2004) 336-355.

[36] C.M. Ringle, S. Wende, J.M. Becker, Smartpls 3, SmartPLS GmbH, Boenningstedt, 2015.

[37] W.W. Chin, V.E. Vinzi, W.W. Chin, J. Henseler, H. Wang (Eds.), How to Write up and Report PLS Analyses in Handbook of Partial Least Squares, Springer, Berlin, 2010, pp. 655–690.

[38] P. Chwelos, I. Benbasat, A.S. Dexter, Research report: empirical test of an EDI adoption model, Inf, Syst, Res, 12 (3) (2001) 304–321.

[39] J. Henseler, T.K. Dijkstra, M. Ssarstedt, C.M. Ringle, A. Diamantopoulos, D W Straub. R J Calantone. Common beliefs and reality about PLS: comments on Ronkko and Evermann, Organ, Res, Methods 17 (2) (2013) 182–209

[40] L.T. Hu, P.M. Bentler, Fit indices in covariance structure modeling: sensitivity to underparameterized model misspecificiation, Psychol. Methods 3 (4) (1998) 424.

[41] J.F. Hair, G.T.M. Hult, C.M. Ringle, M. Sarstedt, A Primer on Partial Least Squares Structural Equation Modeling. 2nd ed., Sage Publications. Thousand Oaks. CA 2017.

[42] P.M. Podsakof, S.B. MacKenzie, N.P. Podsakof, Sources of method bias in social science research and recommendations on how to control it, Annu. Rey. Psychol 63 (2012) 539–569.

[43] P. Podsakoff, S. MacKenzie. J. Lee, N. Podsakoff, Common method bias in beha: vioral research: a critical review of the literature and recommended remedies, J. Appl, Psychol, 88 (5) (2003) 879–903.

[44] H. Liang, N. Saraf, O. Hu. Y. Xue, Assimilation of enterprise systems: the effect of institutional pressures and the mediating role of top management, Mis Q. 31 (1) (2007) 59–87

[45] D. Gefen, D. Straub, A practcial guide to factorial validity using PLS-Graph: tutorial and annotated example. Commun. Assoc, Inf, Syst. 16 (5) (2005) 91–109.

[46] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, J. Mark. Res. 18 (1) (1981) 39–50.

[47] P.B. Lowry, N.C. Romano, J.L. Jenkins, R.W. Guthrie, The CMC interactivity model: how interactivity enhances communication quality and process satisfactior in lean-media groups, J. Manag, Inf, Syst, 26 (1) (2009) 155–196.

[48] J.F. Hair, C.M. Ringle, M. Sarstedt, PLS-SEM: indeed a silver bullet, J. Mark. Theory Pract. 19 (2) (2011) 139–152.

[49] J. Henseler, C.M. Ringle, M. Sarstedt, A new criterion for assessing discriminant validity in variance-based structural equation modeling, J. Acad. Mark. Sci. 43 (1) (2015) 115–135.

[50] S. Geisser, A predictive approach to random efect model, Biometrika 61 (1) (1974) 101–107.

[51] M. Stone, Cross-validatory choice and assessment of statistical predictions, J. R. Stat, Soc, Ser, B 36 (2) (1974) 111–147

[52] W.W. Chin, Commentary: issues and opinion on structural equation modeling, Mis Q. 22 (1) (1998) vii–xvi.

[53] P.A. Norberg, D.R. Horne, D.A. Horne, The privacy paradox: personal information disclosure intentions versus behaviors, J. Consum, Aff, 41 (1) (2007) 100–126.

[54] H. Xu, H.-H. Teo, B.C.Y. Tan, R. Agarwal, The role of push-pull technology in privacy calculus: the case of location-based services, J. Manag. Inf. Syst. 26 (3) (2009) 135–174.

[55] C.L. Anderson, R. Agarwal, The digitalization of healthcare: boundary risks, emotion, and consumer willingness to disclose personal health information. Inf Syst, Res, 22 (3) (2011) 469–490.

[56] S. Karwatzki, O. Dytynko, M. Trenz, D. Veit, Beyond the personalization-privacy paradox: privacy valuation, transparency features, and service personalization, J. Manag. Inf. Syst. 34 (2) (2017) 369–400.

[57] T. Li, T. Unger, Willing to pay for quality personalization? Trade-of between

quality and privacy, Eur. J. Inf. Syst. 21 (2012) 621–642.

[58] Y. Li, The impact of disposition to privacy, website reputation and website familiarity on information privacy concerns, Decis. Support Syst. 57 (2014) 343–354.

[59] L.F. Acke, B.K. Chu, X. Kuang, L. Qi, Lying: an experimental investigation of the role of situational factors, Bus. Ethics Q. 21 (4) (2011) 605–632.

[60] N.E. Bowie, Lying and deception, Bus. Ethics Q. 22 (3) (2012) 579–585

[61] S.L. Grover, C. Hui, The influence of role conflict and self-interest on lying in organizations, J. Bus. Ethics 13 (4) (1994) 295–303.

[62] T. Takala, J. Urpilainen, Managerial work and lying: a conceptual framework and an explorative case study, J. Bus. Ethics 20 (3) (1999) 181–195.

[63] C.E. Naquin, L.Y. Belkin, T.R. Kurtzberg, The finer points of lying online: E-mail versus pen and paper, J. Appl. Psychol. 95 (2) (2010) 387–394.

[64] M.J. Culnan, P.K. Armstrong, Information privacy concerns, procedural fairness and impersonal trust: an empirical investigation, Organ. Sci. 10 (1) (1999) 104–115.

[65] H. Li, R. Sarathy, J. Zhang, The role of emotions in shaping consumers’ privacy beliefs about unfamiliar online vendors, J. Inf. Priv. Secur. 4 (3) (2008) 36–62

[66] R. Wakefield. The influence of user affect in online information disclosure. J. Strateg. Inf. Syst. 22 (2) (2013) 157–174.

[67] J. Yu, P.J.H. Hu, T.H. Cheng, Role of afect in self-disclosure on social network websites: a test of two competing models, J. Manag. Inf. Syst. 32 (2) (2015) 239–277.

[68] S. Chaiken, The Use of Source Versus Messaeg Cues in Persuasion: an Information Processing Analysis, University of Massachusetts Amherst, MA. 1978

[69] S. Chaiken, Heuristic versus systematic information processing and the use of source versus message cues in persuasion, J. Pers. Soc. Psychol. 39 (1980) 752–766.

[70] R. Petty, D. Wegener, Attitude Change: Multiple Roles of Persuasion Variables, 4 ed., McGraw-Hill, New York, 1998.

[71] C. Tankard, What the gdpr means for businesses, Netw. Secur. 2016 (6) (2016) 5–8.

[72] F. Gilbert, EU general data protecton regulation: what impact for businesses established outside the European Union, Journal of Internet Law 19 (11) (2016) 3–8.

[73] L. Downes, The business implications of the EU-US, "Privacy shield", (2016) accessed on December 8, 2017 https://cb.hbsp.harvard.edu/cbmp/product/ H02NUX-PDF-ENG

[74] K.L. Hui, H.H. Teo, S.Y.T. Lee, The value of privacy assurance: an exploratory field experiment, Mis O. 31 (1) (2007) 19–33.

[75] H.J. Smith, J.S. Milberg, J.S. Burke, Information privacy: measuring individuals concerns about organizational practices, Mis Q. 20 (2) (1996) 167–196.

[76] H. Krasnova, N.F. Veltri, O. Gunther, Self-disclosure and privacy calculus on socia networking sites: the role of culture, Bus. Inf. Syst. Eng. 4 (3) (2012) 1.

[77] H. Treiblmaier, S. Chong, Antecedents of the Intention to Disclose Personal Information on the Internet: A Review and Model Extension Sixth Annua Workshop on HCI Research in MIS, Montreal, 2007, (2007), pp. 30–34.

[78] M. Martin, On the induction of mood, Clin. Psychol. Rev. 10 (6) (1990) 669–697.

[79] N. Schwarz, G.L. Clore, Mood, misattribution, and judgments of well-being: informative and directive functions of afective states, J. Pers. Soc. Psychol. 45 (3) (1983) 513–523

[80] G. Sutherland. B. Newman, S. Rachman, Experimental investigations of the relations between mood and inensive unwanted cognitions. Br. J. Med. Psychol. 55 (2 (1982) 127–138.

[81] E. Velten, A laboratory task for induction of mood states, Behav. Res. Ther. 6 (4) (1968) 473–482.

[82] R. Westerman, K. Spies, G. Stahl, F.W. Hesse, Relative efectiveness and validity of mood induction procedures: a meta-analysis, Eur. J. Soc. Psychol. 26 (4) (1996) 557–580.

[83] S.E. Ainsworth, R.F. Baumeister, D. Ariely, K.D. Vohs, Ego depletion decreases trust in economic decision making, J. Exp. Soc. Psychol. 54 (2014) 40–49.

[84] F. Gino, M.E. Schweitzer, N.L. Mead, D. Ariely, Unable to resist temptation: how self-control depletion promotes unethical behavior, Organ, Behay, Hum, Decis Process. 115 (2) (2011) 191–203.

[85] R.F. Pohl. E. Erdfelder. B.E. Hilbig, L. Liebke, D. Stahlberg, Effort reduction after self-control depletion: the role of cognitivie resources in use of simple heuristics, J Cogn. Psychol. 25 (3) (2013) 267–276.

[86] B.J. Schmeichel, Attention control, memory updating, and emotion regulation temporarily reduce the capacity for executive control. J. Exp. Psychol. Gen. 136 (2) (2007) 241–255.

[87] C.M. Angst, R. Agarwal, Adoption of electronic health records in the presence of privacy concerns: the elaboration likelihood model and individual persuasion, Mis Q. 33 (2) (2009) 339–370.

[88] N.F. Awad, M.S. Krishnan, The personalization privacy paradox: an empirical evaluation of information transparency and the willingness to be profiled for personalization, Mis Q. 30 (1) (2006) 13–28.

[89] G. Bansal, F.M. Zahedi, D. Gefen, The role of privacy assurance mechanisms in building trust and the moderating role of privacy concern, Eur. J. Inf. Syst. 24 (2015) 624–644.

[90] H. Cavuscoglu, T.Q. Phan, H. Cavuscoglu, E.M. Airoldi, Assessing the impact of granular privacy controls on content sharing and disclosure on Facebook, Inf. Syst. Res. 27 (4) (2016) 848–879

[91] Chai S, Sanjukta D, and Rao HR (2011-2012) Factors afecting bloggers’ knowledge sharing: An investigation across gender. Journal of Management Information Systems 28(3), 309-341.

[92] R. Chakraborty, C. Vishik, H.R. Rao, Privacy preserving actions of older adults on social media: exploring the behavior of opting out of information sharing, Decis.

Support Syst. 55 (2013) 948–956.

[93] R. Chen, Living a private life in public social networks: an exploration of membe self-disclosure, Decis. Support Syst. 55 (2013) 661–668.

[94] R. Chen, S.K. Sharma, Learning and self-disclosure behavior on social networking sites: the case of Facebook users, Eur. J. Inf. Syst. 24 (2015) 93–106.

[95] B.C.F. Choi, L. Land, The efects of general privacy concerns and transactional privacy concerns on Facebook apps usage, Inf. Manag. 53 (7) (2016) 868–877.

[97] T. Dinev, P. Hart, An extended privacy calculus model for e-commerce transac tions, Inf. Syst. Res. 17 (1) (2006) 61–80.

[98] T. Dinev, P. Hart, M.R. Mullen, Internet privacy concerns and beliefs about government surveillance - an empirical investigation, J. Strateg. Inf. Syst. 17 (2008) 214–233.

[99] J. Gerlach, T. Wiljaja, P. Buxmann, Handle with care: how online social network providers’ privacy policies impact users’ information sharing behavior, J. Strateg. Inf. Syst. 24 (2015) 33–43.

[100] F. Kehr, T. Kowatsch, D. Wentzel, E. Fleisch, Blissfully ignorant: the efects of general privacy concerns, general institutional trust, and afect in the privacy calculus. Inf, Syst. J. 25 (2015) 607–635

[101] M.J. Keith, J.S. Babb, P.B. Lowry, C.P. Furner, A. Abdullat, The role of mobile computing self-eficacy in consumer information disclosure, Inf. Syst. J. 25 (2015) 637–667.

[102] N. Kordzadeh, J. Warren, Communicating personal health information in virtua health communities: an integration of privacy calculus model and affective commitment, J. Assoc. Inf. Syst. 18 (1) (2017) 45–81

[103] C. Lancelot Miltgen, D. Peyrat-Guillard, Cultural and generational influences on privacy concenrs: a qualitative study in 7 European countries, Eur. J. Inf. Syst. 23 (1) (2014) 103–125.

[104] H. Li, X. Luo, H. Xu, Resolving the privacy paradox: toward a cognitive appraisa and emotion approach to online privacy behaviors, Inf. Manag. (2017) In press.

[105] K. Li, Z. Lin, X. Wang, An empirical analysis of users’ privacy disclosure behaviors on social network sites, Inf. Manag. 52 (2015) 882–891.

[106] P.B. Lowry, J. Cao, A. Everard, Privacy concerns versus desire for interpersonal awareness in driving the use of self-disclosure technologies: the case of instant messaging in two cultures, J. Manag. Inf. Syst. 27 (4) (2011) 163–200.

[107] D.H. McKnight, V. Choudhury, C. Kacmar, Developing and validating trust measures for e-commerce: an integrative typology, Inf. Syst. Res. 13 (3) (2002) 334-359

[108] C. Posey, P.B. Lowry, T.L. Roberts, T.S. Ellis, Proposing the online community self disclosure model: the case of working professsionals in France and the U.K. Who use online communities, Eur. J. Inf. Syst. 19 (2010) 181–195.

[109] K.S. Schwaig, A.H. Segars, V. Grover, K.D. Fiedler, A model of consumers’ perceptions of the invasion of information privacy, Inf. Manag. 50 (2013) 1–12.

[110] H.-P. Shih, K.-H. Lai, T.C.E. Cheng, Constraint-based and dedication-based mechanisms for encouraging online self-disclosure: Is personalization the only thing that matters? Eur. J. Inf, Syst. 26 (2017) 432–450

[111] S. Spiekermann, H. Krasnova, K. Koroleva, T. Hildebrand, Online social networks: why we disclose, J. Inf. Technol. 25 (2) (2010) 109–125.

[112] W.N.-F.H. Tow, P. Dell, J. Venable, Understanding information disclosure beha viour in australian facebook users, J. Inf. Technol. 25 (2010) 126–136.

[113] J.C. Zimmer, R. Arsal, M.M.D. Al-Marzouq, V. Grover, Knowing your customers: using a reciprocal relationship to enhance voluntary information disclosure, Decis. Support Syst. 48 (2010) 395–406.

[114] J.C. Zimmer, R.E. Arsal, M. Al-Marzouq, V. Grover, Investigating online information disclosure: efects of information relevance, trust and risk, Inf. Manag. 47 (2010).115–123.

[115] T.L. James, M. Warkentin, S.E. Collignon, A dual privacy decision model for online social networks. Information & Management 52 (2015) 893–908

Caroline Lancelot Miltgen is Professor in Marketing at Audencia Business School, France. Her research interests include information privacy, e-commerce and digital services, and advertising and technology acceptance. She was the leader and principal investigator of two research contracts funded by the European Commission on “Privacy and electronic identification systems” (2007) and “Personal data Identity Management” (2009). She is the author of several academic articles and book chapters in the field of Information Systems and Marketing. Her research has appeared in the European Journal of Information Systems, Decision Support Systems, Information and Management, and the Journal of Business Research. She currently serves at Audencia Business School as co-Chair of the Marketing Department. She holds a PhD in Management Sciences from the University of Paris Dauphine, France.

H. Jef Smith was the George and Mildred Panuska Professor in Business in the Farmer School of Business at Miami University in Oxford, Ohio. His research focused on ethical, societal, and regulatory issues associated with strategic uses of information technology. His research has appeared in California Management Review, Communications of the ACM, Harvard Business Review, Information Systems Research, MIS Quarterly, MIT Sloan Management Review, Organization Science, and in other journals. He served as a Senior Editor of Decision Sciences Journal. He served on the editorial board of MIS Quarterly from 2003 to 2006 and as a Senior Editor at Information Systems Management from 2007 to 2015. He served at Miami University (Ohio) as Chair of the Department of Decision Sciences and Management Information Systems from July 2006 until July 2011 and as Interim Chair of the Department of Finance during 2015-2016. He holded B.S. degrees in Computer Science and Mathematics from North Carolina State University; an M.B.A. degree from the University of North Carolina in Chapel Hill; and a D.B.A. degree from Harvard University. He worked for the International Business Machines (IBM) Corporation for several years in software development.
