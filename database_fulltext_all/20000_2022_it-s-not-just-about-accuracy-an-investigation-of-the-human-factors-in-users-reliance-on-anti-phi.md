---
otero_id: 20000
otero_key: "44ARMRF4"
title: "It's not just about accuracy: An investigation of the human factors in users' reliance on anti-phishing tools"
authors: "Sebastian W. Schuetz; Zachary R. Steelman; Rhonda A. Syler"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113846"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# It’s not just about accuracy: An investigation of the human factors in users reliance on anti-phishing tools

![](/api/attachments/44ARMRF4/fulltext/images/6594d4636082146ff1d0e043a1d16bf03b564c08a927f9ff211563dc9b3f3b01.jpg)

Sebastian W. Schuetz <sup>a,\*</sup>, Zachary R. Steelman <sup>b</sup>, Rhonda A. Syler <sup>c</sup>

<sup>a</sup> Department of Information Systems and Business Analytics, College of Business, Florida International University, Miami, FL, United States of America

<sup>b</sup> Department of Information Systems, Sam M. Walton College of Business, University of Arkansas, Fayetteville, AR, United States of America

<sup>c</sup> Department of Computer Information Systems & Business Analytics, College of Business, James Madison University, Harrisonburg, VA, United States of America

## A R T I C L E I N F O

Keywords: Phishing Anti-phishing tool Accuracy Trust Distrust Reliance Under-reliance

## A B S T R A C T

Phishing attacks pose substantial threats to the security of individuals and organizations. Although current antiphishing tools achieve high accuracy rates and present a potential solution to this problem, users are often reluctant to rely on the predictions of these competent tools. However, we continue to lack a means of resolving this reluctance—or even an explanation for it. To address this need and advance toward a solution, we inves tigate the factors that influence users’ reliance on anti-phishing tools. Over the course of two studies, we test the effects of tool attributes (i.e., accuracy and frequency of phishing email predictions) and develop a model based on the notions of trust and distrust. Countering the common conjecture that tools are not accurate enough, we find that users’ under-reliance is not an artifact of the insufficient accuracy of tools, as even in a 100% accuracy condition, users were under-reliant on tools. Rather, we find that while accuracy increases users’ trust in tools, full reliance is inhibited by users’ distrust, which is driven by a lack of transparency regarding tools’ function alities and the quantity of predictions provided. Thus, overall, our study shows the limits of accuracy in engendering reliance and explains the under-reliance phenomenon by showing that due to lack of knowledge or understanding, some users prefer to rely on their own inferior judgment instead of trusting and relying on the predictions provided by highly accurate tools.

## 1. Introduction

Phishing attacks pose substantial threats to the security of in dividuals and organizations [1,2,3,4,5]. In the last decade, successful phishing attacks have caused billions of dollars in damages [6]. The bulk of these damages are faced by organizations, which, on average, accrue losses of \$3.7 million per successful phishing attack [6]. Even before the uptick in phishing attacks during the COVID-19 pandemic, hundreds of thousands of new, unique phishing attacks were executed every year [7]—a number that has since further increased [8].

To defend against phishing attacks, anti-phishing tools (hereafter, tools) were developed. These tools can be found as part of security software packages (e.g., McAfee SiteAdvisor) and email service pro viders such as Google Mail [9]. Modern tools typically rely on machine learning techniques to learn suspicious patterns or cues and, based on the presence of such patterns and cues, predict the legitimacy of incoming emails [10,11]. The results of these predictions are typically made visible in warning messages, pop-ups, flags, or labels that indicate whether an email is believed to be phishing or legitimate. For example, the “junk” folder in popular email clients represents a prediction that emails in that folder may be spam or phishing. Frequently, these tools achieve about 90+% accuracy $[ 1 1 , 1 2 ]$ ] and should protect users most of the time if they rely on the predictions. Thus, users’ reliance on the tool, i. $\boldsymbol { \mathrm { e } } _ { \cdot \boldsymbol { s } }$ the extent to which a user follows the tool’s predictions [13], is a key factor for tools to be effectively utilized. If users fully relied on and thus heeded the predictions of accurate tools, the danger of phishing attacks could likely be minimized.

Unfortunately, users often disregard tools’ predictions and apply their own judgment [1,10], i.e., by ignoring warning labels or retrieving phishing emails from junk folders. This is hazardous because users are typically overly confident in their own abilities to detect phishing messages and hence render themselves vulnerable to attacks [14].<sup>1</sup> For example, in 2011, an employee restoring flagged phishing emails from his junk folder caused the famous RSA Security data breach [15]. More famously, the 2016 Clinton Campaign hack was also caused by an em ployee’s mishandling of a phishing message [16]. Experimental research has consistently shown that users heed tool predictions in only about 80% of cases [17,10,18]. This rate of reliance is clearly insufficient to fend off phishing attacks, as hundreds of thousands of such attacks are executed every year [19]. Therefore, it may not be surprising that thousands of users continue to fall victim to phishing emails every day [20]. Considering the availability of highly accurate tools and users likelihood of making blunders when identifying phishing messages, resolving the phishing threat hinges on persuading users to rely on tool predictions that organizations have put into place.

It is unclear what would induce users to rely on anti-phishing tools. Given that technology is typically seen as offering more reliable and credible sources of information than humans [21], one would expect users to rely on tools. However, a considerable array of empirical studies investigating users’ responses to highly accurate tools [e.g., 17,18,22] has shown that users’ under-reliance is a systematic, consistent problem. Nevertheless, a compelling explanation for users’ under-reliance on tools is still lacking. One plausible conjecture is that tools are simply not accurate enough. Previous research has shown that tool accuracy is a strong driver of user reliance [17,10,13]. However, the evidence sug gests that even with 97% accurate tools, users do not fully rely on their predictions [10]. This finding may imply that (a) tools are not yet suf ficiently accurate and thus require further improvements, or (b) there are human factors at play that lead users to engage in irrational be haviors, even when tools are highly accurate. In this research, we attempt to clarify which option is actually the case.

Notably, the issue of user reliance connects to a broader archetypal problem that pertains to a variety of contexts in which tools deliver predictions and could thus potentially be helpful in solving a number of other related problems. For example, in healthcare contexts, diagnostic tools can identify diseases with similarly high levels of accuracy [23] and can thus assist physicians in making accurate diagnoses, should they choose to appropriately rely on algorithmic predictions. Similarly, research has shown that decision makers are reluctant to rely on insights generated from Big Data analytics, and resolving that reluctance ha been referred to as a great challenge [24]. Thus, to inform potential solutions to this archetypal problem, we examine what explains users under-reliance on prediction tools.

Formally, we ask the research question: What drives and inhibits users reliance on anti-phishing tools? We address this research question by developing a model of tool attributes and user reliance that explains how tool attributes affect user reliance and why users are sometimes reluc tant to rely on tools. We develop the model over the course of two studies. Study 1 begins with a randomized field experiment in which we manipulate tool attributes. The findings of this experiment confirm the expectation that users’ reliance is higher when tool predictions are more accurate. We also find that the effect is moderated by frequency, which refers to the number of emails flagged by a tool. However, Study 1 shows that even with a highly accurate tool, some users refuse to rely on the tool’s predictions. These findings highlight the limitations of tool attri butes alone to engender reliance, as there appears to be a human factor involved that inhibits reliance on even highly accurate tools. Impor tantly, these findings refute the conjecture that tools are not accurate enough to make users fully reliant on them. Consequently, an explana tion for the perplexing phenomenon of users’ reluctance to fully rely on highly accurate tool predictions is needed.

Study 2 addresses this gap by developing explanatory knowledge on how tool attributes affect user reliance and why users are reluctant to fully rely on tool predictions, even when they are highly accurate. To that end, we develop an explanation based on users’ trust and distrust of the tool. Specifically, we contribute by introducing trust and distrust as predictors of user reliance on tool predictions and propose the accuracy, transparency, and frequency of tool recommendations as context-specific antecedents. We validate this model by conducting a second survey experiment with a highly accurate tool. We find that while accuracy and transparency increase trust, frequency actually leads to increased distrust of the tool. More importantly, we find that while trust increases reliance, distrust has a negative effect on user reliance, even though participants in this study had never used the tool (i.e., an inherent distrust of a tool may exist even prior to utilizing a specific tool because of prior experience). Thus, our theory makes a revelatory contribution in that it explains users’ under-reliance emerging from users’ lingering distrust of a tool’s competency (the expectation that a tool might fail). Our theory further contributes by explaining the contextual drivers of users’ distrust—in particular, frequency as well as users’ trust and un derstanding of the tool. These findings have important implications for the anti-phishing tool literature as well as the broader literature on user reliance and inform the development of security-relevant tools and managerial interventions such as training to tackle the issue of underreliance. Combined, the insights provided in our study shape a new way forward toward a more efficacious use of tools by expanding our understanding of users’ under-reliance.

## 2. Background

## 2.1. Phishing

Phishing is a method of social engineering that aims to trick victims into revealing sensitive information, typically by leading users to a phishing website that mimics an authentic user interface in which users are asked to disclose sensitive information (e.g., contact details, user/ network credentials, credit card details) [12]. Phishing is typically executed via email and targets a mass audience [25]. For phishing to be effective, successful messages must be both believable and persuasive [12]. Believability is often achieved by mimicking communications from reputable persons or organizations [25]. A variety of techniques exist to boost persuasiveness. For example, Wright, Jensen, Thatcher, Dinger and Marett [26] found that messages built upon liking, reciprocity, so cial proof, and scarcity are effective at promoting deception. Also, the technique of asking recipients to open an attachment or follow a link has been found to be more persuasive than the technique of simply asking recipients to respond immediately with personal information [27]. Thus, if users do not pay close attention and recognize cues, they are likely to be victimized [4]. Given the sheer amount of phishing emails sent out in a single phishing attack, victimizing even a small percentage of email recipients is sufficient for a phishing campaigns to be successful [26].

Unfortunately, users are ill prepared to identify phishing messages. For generic phishing messages, studies report phishing victimization rates of between about 5% and 30% [28,3,5,14,29,25]. For more so phisticated and tailored spear-phishing messages, victimization rates can be considerably higher [12,3], with the most extreme findings reporting victimization rates of around 70% [27,28] to 90% [30]. Considering these numbers, it is unsurprising that phishing remains one of the most popular fraud methods for criminals.

Attempts to train users to defend themselves against these attack have shown some promise [3,31], but their ability to build a foundation for a pervasive solution may be limited for three reasons. First, research has pointed out that users are seldom motivated to learn about phishing [32] or security in general [33]. One reason for that might be that users are often already overconfident in their abilities [30,14], making it difficult to motivate them to pay attention to anti-phishing training. Second, training may only lead to short-term effects, as training effects have been shown to diminish over time [32,34]. For instance, Ngyuen, Jensen and Day [34] showed that as soon as eight weeks after training, users become less cautious toward phishing emails. Hence, training based solutions need to be used regularly (i.e., multiple times a year). Third, even among users who are motivated to regularly learn about phishing attacks, training can only reduce—but not eliminate—users vulnerability to phishing emails [3,31]. Despite training efforts, users still remain highly vulnerable to sophisticated phishing emails [27].

Thus, it may be unrealistic to rely solely on users’ prior knowledge and abilities to defend against unescapable phishing threats. Given that anti phishing tools are typically more accurate than human judgment and cheaper than training, if organizations can persuade users to fully rely on them, implementing such tools can provide organizations with an effective defense strategy.

## 2.2. Anti-phishing tools

A more promising approach to combatting phishing threats is the use of automated phishing detection technologies. Anti-phishing tools refer to any kind of protective technology that is designed to protect users against phishing attacks [17]. There are currently two approaches used to automatically identify phishing emails: lookup and classification [17]. When using a lookup approach, anti-phishing tools detect phishing emails by looking up received emails in a curated blacklist (e.g., Google Safe Browsing, PhishTank.com). Thus, detection requires other users or organizations to report phishing emails to such lists [35]. Such anti phishing tools were initially implemented in toolbars [18] but are now frequently a standard feature of today’s browsers (i.e., Google Chrome, Safari, Firefox, and Opera all use the Google Safe Browsing blacklist). Unfortunately, lookup approaches are inapt to detect novel attacks. Because only known phishing emails can be listed on a curated blacklist, any new attack can easily bypass lookup-based anti-phishing tools. Further, it has been shown that it may take >48 hours for a novel attack to be identified through a blacklist [35]. Consequently, lookup-based anti-phishing tools offer little to no protection against novel attacks, of which there are thousands every day [19].

To detect novel phishing attacks, classification-based approaches were developed. This approach uses heuristics or features sourced from existing phishing emails to predict the legitimacy of an email [10,11]. This probability-based approach uses existing knowledge of phishing attacks to estimate the likelihood of an email being fraudulent [11]. Frequently, these tools achieve 90+% accuracy in their predictions [11,12] and can be found as part of security software packages (e.g., McAfee SiteAdvisor) and mail service providers such as Google Mail [9].

These tools typically produce some kind of prediction (e.g., a warning) when a phishing email (or website) is detected [cf. 1]. These predictions can come in various forms, such as pop-ups, redirects, or even flags in email clients (e.g., Google Mail). If tools were able to achieve 100% accuracy, the threat of phishing would likely be defeated because tools could reliably filter these out. Unfortunately, because the underlying methods are probabilistic, not deterministic, it is theoreti cally impossible for classification detectors to achieve 100% accuracy. Consequently, tools still need to show even suspicious emails to users so that they can access them in case the tool made a mistake (i.e., stored in a junk or spam folder that users must still check occasionally for missing emails). That said, some tools achieve very high accuracy rates—such a the phishing website classifier developed by Abbasi, Zahedi, Zeng, Chen, Chen and Nunamaker [10], which achieved 97%; a phishing email detection neural network developed by Smadi, Aslam and Zhang [36], which achieved 98.6%; and the phishing website detection algorithm developed by Ramesh, Krishnamurthi and Kumar [37], which achieved 99%. Given the blunders users can make when identifying phishing messages [4,5,14], users would be well advised to trust these extremely accurate tools.

## 2.3. Users’ under-reliance on warning messages

Paradoxically, users have demonstrated an unexplainable reluctance to adhere to anti-phishing tool warning messages. As various studies on users’ reliance on phishing website detection tools have shown (Table 1), even in best-case scenarios, users follow the system’s pre dictions in 91% of cases and disregard warning predictions in only about 9% of cases [10]. However, that relatively low number was obtained under experimental conditions in which subjects were asked to judge the legitimacy of a subset of websites. Whenever experiments attempt to establish ecologically valid conditions by deceiving users into thinking that they are supposed to carry out an everyday task, users disregard the anti-phishing tool warnings at substantially higher rates, ranging be tween 17% to 79% [17,18,38,22]. Analogously, a recent field experi ment showed that over 50% of users click on phishing websites even when a warning is presented, and over 2% ended up transacting on them [1]. These numbers were obtained by studies on users’ reliance on phishing website detection tools but are illustrative of the generic issue of users’ reliance on tool-based security warnings, which are frequently ignored [39]. Thus, these numbers suggest that a staggering number of users are susceptible to phishing attacks, despite the availability of warnings from highly accurate tools. The underlying reason that users are reluctant to fully rely on tool predictions remains unclear. Research has shown that tool attributes, specifically accuracy and speed, may increase users’ reliance on tools’ predictions [17,10,13].

Table 1  
Experimental studies on anti-phishing tool reliance.

<table><tr><td>Study</td><td>Artifact</td><td>Deception</td><td>Info on Tool</td><td>Accuracy</td><td>Reliance</td></tr><tr><td>Wu, Miller and Garfinkel [22]</td><td>Toolbar warnings</td><td>Yes</td><td>Yes &amp; No</td><td>100%*</td><td>17% to 45%</td></tr><tr><td>Egelman, Cranor and Hong [18]</td><td>Web browser warning</td><td>Yes</td><td>No</td><td>100%*</td><td>79%</td></tr><tr><td>Abbasi, Zahedi and Chen [17]</td><td>Anti-phishing tool warnings and web warnings</td><td>Yes</td><td>No</td><td>60% to 90%</td><td>60% to 79%</td></tr><tr><td>Egelman and Schechter [38]</td><td>Web browser warning</td><td>Yes</td><td>No</td><td>100%*</td><td>67%</td></tr><tr><td>Abbasi, Zahedi, Zeng, Chen, Chen and Nunamaker [10]</td><td>Web browser warning</td><td>No</td><td>No</td><td>71% to 97%</td><td>55% to 91%</td></tr><tr><td>Zahedi, Abbasi and Chen [13]</td><td>Web browser warning</td><td>Yes</td><td>No</td><td>60%, 90%</td><td>Not reported</td></tr><tr><td>Chen, Zahedi, Abbasi and Dobolyi [40]</td><td>Web browser warning</td><td>No</td><td>No</td><td>60%, 90%</td><td>66% to 81%**</td></tr></table>

These studies only showed valid warnings.  
Reliance after 10 iterations of tool usage.

Thus, based on previous research, one plausible explanation for users’ insufficient reliance might be that tools are not accurate enough or too slow. However, as shown in Table 1, this explanation is not supported by the reported empirical evidence, as some of these experi ments were conducted with perfectly accurate tools that immediately displayed warnings yet users still disregarded them [18,38]. Another potential explanation is that users had not yet established trust in the tools. However, as Chen, Zahedi, Abbasi and Dobolyi [40] show, even after 10 iterations of tool use, users’ reliance was still lower than the actual tool’s accuracy (i.e., 81% reliance with a 90% accurate tool), suggesting that users continued to under-rely on the tool, even though they had amply experienced the accuracy of the tool. Clearly, there are reasons to suspect that even if tools were 100% accurate, users would remain susceptible to phishing attacks [17].

The lack of clarity on why users are reluctant to rely on tool pre dictions is problematic. Without an understanding of why, scholars and practitioners are left without guidance on how to get users to rely on them. Perhaps the lack of theory explains why scholars and practitioners have continued to focus on developing more accurate tools to induce users to rely on them. However, if perfectly accurate tools do not engender full reliance, as the evidence suggests (Table 1), these efforts might be misguided. Thus, understanding users’ reluctance to fully rely on predictions requires a theory of user reliance on tool predictions. Such a theory could not only help improve the design of current tools but also spawn future research on the development of theoretical angles that explain how to motivate users to rely on tools.

## 3. Study 1: Problem investigation

## 3.1. Study 1: Tool attributes

Our theory development begins with an investigation of the effects of tool attributes on user reliance and whether a fully accurate tool would engender full user reliance. Prior phishing research has devoted much attention to accuracy as an important design variable of anti-phishing tools. Intuitively, as the purpose of such tools is to identify phishing emails, higher levels of accuracy increase a tool’s utility. The more ac curate tools are, the more advantageous it is for users to rely on them because reliance on the tool can improve users’ ability to detect phishing attempts [10]. Thus, accuracy is widely seen as a key driver of user reliance [17,38,22,13] and perhaps one of the most important design variables influencing user reliance:

## H1. : Higher tool accuracy results in higher user reliance.

While accuracy might be an important driver of user reliance, the specifics of the phishing tool context require consideration of a related tool attribute, frequency, as another design variable. Frequency refers to the number of predictions made (e.g., 5, 10, or 200). The need to reflect frequency in conjunction with accuracy arises from the multidecision context that exists in practice, with many users receiving hundreds of unique emails a week. As users typically receive multiple potential phishing emails throughout their day, they need to make multiple judgments on the legitimacy of these emails every day. If these judg ments are aided by tool-based predictions, then users’ reliance may be influenced not only by accuracy but also the number of predictions provided (frequency).

A higher frequency of predictions affords users more opportunities to adjust their expectations of tool performance [40]. If a tool performs poorly, lower frequency will obscure that performance, as users will have less opportunity to observe the tool making mistakes. In contrast, if users have more opportunities to observe a tool making mistakes (high frequency), users form more negative expectations about the tool’s performance. Thus, in conditions of low accuracy, we expect high fre quency to amplify users’ expectations that a tool will make erroneous predictions. This factor might be aggravated by the “exaggerated ex pectations” bias, referring to an individual’s irrational exaggeration of unlikely probabilities [41]. This bias suggests that users might exag gerate the probabilities of a tool making errors. Under conditions of low accuracy, we thus expect users to rely less on tools that provide higher levels of frequency, meaning more predictions.

Second, in conditions of high accuracy, frequency increases the utility of reliance to users because high frequency affords users more opportunities to witness the good or acceptable performance of a tool, leading to expectations that a highly accurate tool will do an adequate job. While users may choose to inspect each email on their own, a large number of emails can render this a cognitively demanding task. Tools offer a reduction of this cognitive demand by offering users the option to delegate that judgment to the tool. As humans are cognitive misers (i.e., strive to conserve their cognitive capacities), higher frequency makes it more attractive to users to just blindly follow the tool’s predictions, especially if they have expectations that these predictions will be ac curate. Hence, we expect users to rely more on high-accuracy tools that provide higher levels of prediction frequency. Taken together, we hypothesize:

H2. : In conditions of low accuracy, higher prediction frequency leads to decreases in user reliance, while in conditions of high accuracy, higher prediction frequency leads to increases in user reliance.

## 3.2. Study 1: Empirical approach

We conducted a randomized experiment to test the effect of these two tool attributes on user reliance using a replicated email inbox sys tem. We chose to conduct an experiment because of our aim to examine the causal effect of improving accuracy (up to 100%) on users’ reliance. The experimental method was preferable for this purpose, as it offers high internal validity but at the cost of external validity [42]. In this experiment, we manipulated the actual frequency and accuracy of the tool’s prediction to validate our hypotheses. This resulted in a 2 (fre quency levels: low and high) x 3 (accuracy levels: 20%, 60%, and 100%) factorial design with six treatment groups. Importantly, participants were informed about the actual accuracy and frequency levels through the description of the tool. We chose these levels based on theoretical and practical reasons that are discussed in the manipulation section.

The experiment was designed to maximize user reliance. As such, we did not deceive subjects and only requested that they do their best to identify phishing emails in an experimental inbox. Moreover, we explained how the tool worked and informed subjects of the tool’s ac curacy and frequency levels before they began their task. Related ex periments have shown that such conditions aid users’ ability to identify phishing messages (see Table 1).

## 3.2.1. Study 1: Experimental environment

We developed an experimental tool and mock email inbox modeled after Google’s Gmail inbox as to recreate a realistic environment.<sup>2</sup> The tool was developed in JavaScript and embedded in a Qualtrics survey. The tool was preloaded with 20 emails—10 of which were phishing emails (with related cues) and 10 of which were legitimate emails. Appendix A and B provides a screenshot of the tool and more details on the emails.

## 3.2.2. Study 1: Procedure

The experiment was conducted using an online experimental survey, which began with a written request for informed consent, followed by the provision of demographic information and controls. Then, using the Qualtrics randomizer function, subjects were randomly assigned to a treatment group and shown a brief introduction to phishing taken from Jensen, Dinger, Wright and Thatcher [3]. This was followed by a brief introductory vignette that explained the tool and decision tasks as well as the specific treatment condition (e.g., “Your tool covers 50% of the emails in your inbox with an accuracy of 60%.”). To proceed, partici pants had to then answer several questions on their comprehension of the functionality of the tool. Next, subjects were exposed to the exper imental inbox; they had to identify phishing emails with the help of the anti-phishing tool or no help in the control condition. When finished, subjects responded to our focal constructs, manipulation checks, and open feedback regarding the study before the experiment ended.

## 3.2.3. Study 1: Manipulations

The manipulations were delivered through flags on each processed email. Before the experiment was initiated, subjects were informed about the availability of an anti-phishing tool that supports their deci sion task by flagging emails covered by the tool as either phishing or legitimate emails. The availability of the tool’s prediction (i.e., the fre quency) was indicated through blue highlighting. If the tool determined that a specific email was likely phishing, a red warning sign was dis played at the end of the subject line and if it determined that a specific email was likely legitimate, a green checkmark was displayed in the same position. All covered emails had a prediction that varied in accu racy based on the specific treatment. We provided participants with the instructions needed to use the tool and tested their understanding with comprehension check questions prior to displaying the experimental inbox.

To manipulate frequency, we varied the number of predictions $( \mathrm { i . e . , }$ the number of emails with red or green flags), whereas our manipulation of accuracy varied the correctness of these predictions. Importantly, we split frequency and accuracy 50–50 between phishing and legitimate emails. To illustrate, in the low-frequency condition, 10 emails were flagged, of which five were phishing emails and five were legitimate. In the 60% accuracy condition, three of these five phishing emails would have been correctly flagged as phishing, and the remaining two would have been wrongfully flagged as legitimate, whereas three of the five legitimate emails would have been flagged correctly as legitimate, and the other two wrongly flagged as phishing. Students were not informed of our specific splits in these conditions. Furthermore, we ensured that no new emails were flagged in the accuracy treatment conditions. This means that whether in a 20%, 60%, or 100% accuracy condition, the same emails were flagged either correctly or incorrectly as phishing or legitimate. This helped ensure that the difficulty of the decision task remained the same, only to be influenced by changes in frequency and accuracy.

To ensure that our manipulations led to perceptual changes in ac curacy and frequency, we included manipulation checks that captured these perceptions. We conducted two one-way ANOVAs to analyze the success of our manipulations on these variables. Our accuracy manip ulations yielded significant effects on perceived accuracy, and our fre quency manipulations yielded significant effects on perceived frequency (Table 2). As expected, increases in actual accuracy and frequency led to increases in perceived accuracy and frequency. The success of our ma nipulations was further shown by participants spending significantly more time on unflagged than on flagged emails, both correctly (ΔM $= 0 . 3 2 , p \leq 0 . 0 0 1 )$ and incorrectly flagged $( \Delta \mathbf { M } = 0 . 3 4 , p \leq 0 . 0 0 1 )$

## 3.2.4. Study 1: Participants

We collected 272 full and valid responses from a convenience sample of graduate and undergraduate students at a mid-sized US-based uni versity. We ensured attentiveness through multiple attention checks and recorded the mouse movements of participants as well as their time spent answering the questionnaire. Responses provided from mobile phones were prohibited and not counted. We offered course credit as a reward for participation. Our sample comprised about 57% men with an average age of 24 years and an average email experience of 10 years. About 53% had never received anti-phishing training, and about 81% claimed they had never fallen victim to a phishing attack. These important characteristics remained reasonably stable across all treat ment groups, and the differences were insignificant; therefore, we concluded that the randomization was successful.

Table 2  
Manipulation Checks.

<table><tr><td rowspan="2">Accuracy Manipulation</td><td>Perceived Accuracy</td><td rowspan="2">Frequency Manipulation</td><td>Perceived Frequency</td></tr><tr><td>Mean (SD)</td><td>Mean (SD)</td></tr><tr><td>20%</td><td>3.51 (1.69)</td><td>Low - 10 predictions</td><td>4.23 (1.42)</td></tr><tr><td>60%</td><td>4.31 (1.38)</td><td>High - 20 predictions</td><td>5.74 (1.13)</td></tr><tr><td>100%</td><td>5.17 (1.46)</td><td></td><td>F = 97.94</td></tr><tr><td rowspan="2">ANOVA</td><td>F = 56.13</td><td>ANOVA</td><td></td></tr><tr><td>p ≤ 0.001</td><td></td><td>p ≤ 0.001</td></tr></table>

## 3.2.5. Study 1: Measurements

We operationalized the dependent variable, reliance, by calculating the percentage of choices that were made by the participant in line with the available tool predictions. For example, if the tool suggested that five emails were phishing and another five were legitimate, and the user chose to flag the five phishing emails in line with the predictions but also flagged the five legitimate emails as phishing, then the tool reliance was only 50%. The full measurement is reported in Appendix A and B.

## 3.3. Study 1: Results

We hypothesized that more accurate tools would increase reliance (H1), while frequency would decrease reliance on less accurate tools (H2). We conducted an ANCOVA to test H1 and H2. The ANCOVA was computed using IBM SPSS v25. We controlled for gender, age, educa tion, email experience, online transaction experience, prior antiphishing training, and prior phishing experience as covariates. Only online transaction experience (paying bills online) had a significant ef fect on reliance $( \mathrm { F } _ { 2 5 2 } = 1 0 . 6 8 6 , p = 0 . 0 1 2 ,$ , Partial $\eta ^ { 2 } = 0 . \dot { 0 4 } ) .$ . Overall, the analysis explained 39% of the variance in users’ reliance $( \mathrm { R } ^ { 2 } = 0 . 3 9 )$

Next, we explored the effects of accuracy and frequency on reliance. As shown in Fig. 1, higher accuracy consistently led to higher levels of tool reliance. Hence, we found a significant and strong main effect for our accuracy $( \mathrm { F } _ { 2 5 2 } = 5 1 . 3 4 , \leq 0 . 0 0 1$ , Partia $\eta ^ { 2 } = 0 . 2 9 )$ manipulation on reliance, indicating support for H1. Further, as hypothesized in H2, higher frequency only led to higher reliance when accuracy was high. In conditions of imperfect accuracy (i.e., 60% or 20% accuracy), offering more predictions decreased users’ likelihood of reliance on these pre dictions. The collected evidence supports H2, as both the main $( \mathrm { F } _ { 2 5 2 } =$ $4 . 1 3 , p = 0 . 0 4 0$ , Partial $\eta ^ { 2 } = 0 . 0 2 )$ and interaction effects $( \mathrm { F } _ { 2 5 2 } = 4 . 1 2 , p$ $= 0 . 0 1 7 , \eta ^ { 2 } = 0 . 0 3 )$ were found to be significant.

Interestingly, although we offered a 100% accurate tool across two conditions, the reliance rate was only 92%, although one would ratio nally expect the reliance rate to be closer to 100% if the tool attributes were the only drivers of reliance. Importantly, this lower-than-expected reliance rate aligns with findings of prior research which, for example, reported a 91% reliance rate resulting from the use of a 97% accurate tool [10], thus hinting that users’ lower-than-expected reliance rate might be a consistent phenomenon. To further investigate this obser vation, we performed a post hoc student t-test, which revealed that the observed 92% reliance rate was statistically significantly different from the 100% reliance rate that we would have expected in this condition $( \mathrm { t } _ { 5 1 } = 5 . 3 0 , p \le 0 . 0 0 1 )$ , thus rejecting the possibility that under-reliance on the tool was observed by chance and corroborating a consistent under-reliance on highly accurate tools.

Taken together, the collected evidence shows that higher tool ac curacy does indeed lead to increased user reliance on tools (H1) and indicates that in conditions of imperfect accuracy (i.e., 20% and 60%), higher frequency decreases user’s reliance on tools while high accuracy and high frequency increase user’s reliance on tools (H2). Further, we found statistical evidence that users’ under-reliance on highly accurate tools is systematic and not attributable to the tool attributes alone. Consequently, insufficient tool accuracy can be ruled out as the only explanation of why users do not fully rely on tool predictions, as indi cated by the significant focus of prior literature. Similarly, high levels of frequency did not explain users’ reluctance to rely on tool predictions, as frequency only produced a detrimental effect in low-accuracy condi tions. The findings imply that even with further improvements in tool accuracy, users would still not fully rely on tools’ predictions and hence remain vulnerable to phishing attacks. Thus, Study 1 helped confirm that users’ under-reliance cannot be fully resolved by accuracy—even 100% accuracy—and illuminated the independent and joint effects of accuracy and frequency on user reliance.

![](/api/attachments/44ARMRF4/fulltext/images/bf2e3c31319525418fc4dfd0381dbf7e8e369865b629ae51fb59d78b551043d0.jpg)  
Fig. 1. Tool effects on reliance.

## 4. Study 2: Explanation development

To further understand why users are reluctant to fully rely on tools, we turn our focus to users’ cognitive beliefs and biases. Specifically, we build upon the notion that users do not fully trust tools’ predictions. This has been repeatedly suggested in the phishing literature through anec dotal evidence [e.g., 23, 87] but, to the best of our knowledge, this notion has never been formally explored in this context. However, in the related literature on decision support aids, trust has already been shown to be a major factor influencing users’ reliance [e.g., 44, 71, 77]. For example, Wang, Jamieson and Hollands [43] showed that users’ per ceptions of the reliability of a decision aid are closely correlated with users’ trust in and reliance on the decision aid. Similarly, van Dongen and van Maanen [44] showed that users who have higher trust in the decision aid than in their own judgments are more likely to rely on decision aids. Analogously, in the literature on recommendation agents [e.g., 37, 79, 80], trust has been shown to be a key determinant of users acceptance of tool-based predictions. Taken together, these literatures make a strong case for trust being a key driver of user reliance.

However, these literatures are less informative in terms of what might inhibit users’ reliance on a tool’s predictions. Plausibly, a lack of trust might be one explanation. Lee and See [45] propose that users under-reliance might also be the product of distrust—a notion that is further elaborated on by Komiak and Benbasat [46] in the context of recommender systems. However, the effect of distrust on user reliance has not yet been empirically tested. Further, if distrust is indeed a factor contributing to users’ under-reliance, then understanding its anteced ents is crucial for addressing the issue of users’ under-reliance on anti phishing tools. Consequently, there is a unique opportunity to add to these literatures by examining reliance from a dual angle of trust and distrust and their antecedents.

## 4.1. Background on trust and distrust

The concept of trust has received much attention in the literature. With thousands of papers published in business disciplines,<sup>4</sup> trust has been studied from many angles, in various contexts, and in different forms—such as trust in other humans, organizations, and technology [e. g., 47,48,49]. Specifically relevant to our work is the literature on trust in technologies that support decisions. The literature suggests that for users to trust a technology, such as an anti-phishing tool, two conditions must be met. First, users must have favorable expectations toward the tool’s performance (i.e., in making accurate predictions). Second, users must understand how the tool functions (i.e., how it makes its pre dictions). These two factors—prediction accuracy and trans parency—have thus emerged as powerful predictors of trust across an array of studies [e.g., 50,40,51,52,53,54,55]. Thus, based on the literature, we identify accuracy and transparency as antecedents of trust.<sup>5</sup>

Considerably less work has been devoted to understanding the distrust of technologies, which has only recently emerged as a separate construct from trust and not simply the opposite end of a continuum. While few studies have attempted to examine its antecedents, Komiak and Benbasat [46] showed that there are similarities and differences between the processes that lead to trust and distrust—specifically, competence considerations may increase trust and decrease distrust. Likewise, Hsiao [56] suggested that the lack of reliability or familiarity with a technology can lead to distrust of the technology. Importantly, neither of these two studies tested the effects of accuracy and trans parency and distrust using methods of statistical inferences, meaning that their actual effects on distrust remain to be determined. However, based on these initial insights, we consider accuracy and transparency to be antecedents to distrust. Based on Study 1, which revealed that high frequency leads to a negative effect, we also consider frequency as a new antecedent to distrust.

## 4.2. Study 2: Hypotheses

Next, we develop a research model that helps explain users’ underreliance on a tool’s predictions. This research model, as depicted in Fig. 2, explicitly taps into the cognitive realm of users’ decision-making and incorporates users’ perceptions about tool attributes, their general understanding of the tool, and the role of their trust and distrust.

We define trust as the extent to which a user believes in the func tionality, helpfulness, and reliability of anti-phishing tools [57]. Likewise, we define distrust as the user’s expectations that a tool will provide erroneous predictions. This definition is an adaptation of the distrust construct from the recommendation agent literature, which typically defines distrust as buyers’ negative expectations toward a seller’s conduct [58,46].<sup>6</sup>

Like the original conceptualizations of trust and distrust [46,59,60],

<sup>6</sup> Including a reconceptualization of distrust in our research is important because, as Komiak and Benbasat [52] note in their research on trust and distrust in recommendation agents, “focusing solely on trust may provide an incomplete picture of various relationships” (p. 743). We believe this statement is especially true in high-stakes contexts such as phishing, in which wrongfully following an erroneous prediction can lead to devastating consequences. Related research on decision aids has shown that users quickly stop relying on tools once they observe mistakes [51]. In such high-stakes contexts, including distrust can be helpful for capturing the extent to which users are cautious about fully relying on tools’ predictions. Furthermore, including distrust in our theorizing enabled us to provide a more nuanced explanation of why users are reluctant to rely on tools’ predictions.

![](/api/attachments/44ARMRF4/fulltext/images/48e1a466fc199bdb2bd62df0278ca888dd725896f1bab537ccaf85004f2ce9df.jpg)  
Fig. 2. User reliance model.  
Note: dashed lines depict negative relationships.

our contextualization of trust and distrust does not reflect two sides of the same coin but rather two distinct constructs. Along these lines, Dimoka [58] shows that trust and distrust emerge with activation in different brain areas; McKnight and Chervany [61] argue that trust and distrust arise from different thought processes. Building on this notion, our definition of trust is derived from users’ expectations that a tool wil make reliable predictions, whereas distrust is derived from users’ ex pectations that a tool will make erroneous predictions. Thus, while users can have general expectations that a tool’s predictions will be generally reliable, they may simultaneously have the expectation that the tool will also make occasional errors. To give an analogy, while I might trust the reliability of my car (i.e., I’ve never had problems before), I may simultaneously believe it is possible that my car will break down. If I were to use my car in a high-stakes context (e.g., going on a long road trip), I would therefore take precautions (e.g., enrolling in roadside assistance service) instead of taking the road trip fully unprotected. While trust captures the general expectation about the reliability of the car, distrust captures the expectation that the car may nonetheless have problems at some point. Further, one’s level of distrust is influenced not only by expectations about a specific technology but also by one’s prior experience and knowledge about similar technologies. Returning to our example, while I might trust the reliability of my own car, I might also harbor some distrust toward cars in general because of (my or others’) prior negative experiences with other cars.

Since we expect users’ accuracy perceptions to increase trust in the tool and decrease distrust, in Study 2, accuracy refers to the extent to which the user perceives the anti-phishing tool’s predictions to be cor rect, compared to the actual accuracy manipulation in Study 1.<sup>7</sup> Based on [13], we argue above that more accurate tools lead to stronger beliefs in the functional reliability of the tool. Similarly, users trust decision support systems that they perceive as reliable [62,43]. In contrast, research has shown that a lack of reliability is a significant source of users’ distrust [56,46]. Hence, we expect that users will have higher trust and lower distrust toward tools that are perceived as highly ac curate, and hypothesize:

H3a. : Perceived accuracy increases users’ trust in a tool.

## H3b. : Perceived accuracy decreases users’ distrust of a tool.

The literature further suggests that tool transparency, or the avail ability of details regarding how the tool works, increases trust [50,54]. Perceived transparency refers to the extent to which the user understands how the anti-phishing tool makes its predictions. Thus, if it is unclear how a tool arrives at its predictions, explanations are needed to increase users’ understanding [63]. When users begin to understand how pre dictions are made (i.e., through information sharing) the tool’s func tionality becomes more transparent to the user and users begin to trust the tool [52,46]. Since we anticipate that tool transparency increases users’ trust [50,54], we hypothesize:

## H4. : Perceived transparency increases users’ trust in a tool.

We also expect that transparency decreases users’ distrust of a tool. While this relationship has not been heretofore proposed or tested, our rationale is that a better understanding of a tool’s functionality will clarify users’ expectations about the accuracy of the tool’s predictions and give users the sense that the tool’s failures can, to some extent, be predicted and alleviated by the user. We argue that distrust arises because users do not understand the tool and thus err on side of caution regarding its predictions; further, knowing that one cannot know (i.e., knowing that it is impossible to know when a tool makes an erroneous prediction) has been shown to contribute to distrust of recommendation agents [46]. Hence, we hypothesize:

## H5. : Perceived transparency decreases users’ distrust of a tool.

Similarly, we also argue that high levels of frequency can lead to an increase in distrust. Perceived frequency is defined here as the userperceived number of anti-phishing tool predictions made. In Study 1, we argued that increased frequency elevates users’ expectations that at least one of the many predictions will be erroneous. The results of Study 1 corroborate that increased frequency can indeed cause less reliance among users. Hence, as frequency increases, users may harbor greater distrust of a tool based on their prior experiences indicating that the tool makes errors. Therefore, we now formally test this explanation by conceptualizing distrust as partially driven by frequency because of the increased chance of erroneous predictions associated with higher fre quency levels. Hence, we hypothesize:

## H6. : Higher perceived frequency leads to increases in users’ distrust of a tool.

Next, we also suggest that trust decreases distrust. This follows from expectations that the functionality and reliability of the tool will reduce but not eradicate the expectation that the tool could fail. In this vein, Xiao and Benbasat [64] showed that customers with high levels of trust are less likely to detect deception—likely because they are less cautious in general. Further studies have shown that trust in recommendation agents, which can be amplified through explanation, decreases distrust of the predictions made by the agents [59,65,66]. Similarly, we hypothesize:

## H7. : Increases in trust lead to decreases in users’ distrust.

We also argue that while trust increases reliance on tools, distrust decreases reliance on them. Trust has been shown to be a key determi nant of user responses to predictions [67,44,43]. Further, it has been shown that if recommendation agents are seen as trustworthy, then users are generally more likely to rely on their predictions [68]. We extend this notion to the context of phishing tools, arguing that users who trust a tool are more likely to rely on its predictions. Similarly, distrust would be expected to decrease user reliance on the tool, as users expectancy of predictions being erroneous gives users reason to not rely on the tool’s predictions. Thus, we argue:

H8. : Increased trust in a tool leads to increases in user reliance.

## H9. : Increased distrust of a tool leads to decreases in user reliance.

Finally, the literature suggests further factors capturing tool attri butes that might influence trust and user reliance. Specifically, in the trust literature, perceived usefulness (users’ beliefs that a system enhances their performance [69]) and perceived ease of use (users’ beliefs that they can use a system without effort [69]) have been positioned as ante cedents to trust [e.g., [70,71,72]]. In the literature on phishing website detection tools, the cost of error (users’ perceptions of the harm caused by an error made by a phishing detector) and detector speed (users perceptions of whether a detector works sufficiently quickly) have been considered as antecedents to trust and reliance [40,13]. Likewise, threat severity (users’ belief about the harm of falling victim to a phishing attack), threat susceptibility (users’ belief about the possibility of falling victim to a phishing attack), detector response efficacy (users’ belief about the effectiveness of a detector in avoiding phishing attacks), and self efficacy (users’ belief about their own ability to use a detector) have been identified as potential antecedents to reliance [13]. These constructs present alternative explanations of user reliance and trust. To contrast our hypotheses against these alternative explanations, we include them in our research model as control variables. Importantly, because de tector speed was fixed (and immediate) in our study, we omitted this variable, as there was no variance that we could have captured. Furthermore, four of these controls had conceptual overlap (i.e., use fulness and detector efficacy, perceived ease of use, and self-efficacy in using the detector); thus, we focused on the constructs that were closely contextualized with our research (i.e., detector efficacy and self-efficacy of using the detector). In addition to these controls, we also captured fear (a negative emotion representing a response to a recognized danger [73]) because trust might have an emotional component or may be influenced by emotions [52]. Finally, following other work in the phishing literature [74], we also considered users’ risk propensity (users orientation to take risks) as an antecedent to reliance.

## 4.3. Study 2: Empirical approach

## 4.3.1. Study 2: Participants

We conducted a second experiment utilizing our prior tool design and collected 553 full and valid responses from a convenience sample of graduate and undergraduate students at a mid-sized US-based univer sity. We ensured attentiveness through three attention checks and recorded the mouse movements of participants as well as their time spent answering the measurement questionnaire. Responses provided from mobile phones were not counted. We offered course credit as a reward for participation. On average, our participants were 21.5 year old, had 7.4 years of email experience, and received about 25.8 emails per day. The sample comprised 47% women (53% men); 59% of par ticipants indicated they had no experience with phishing, 81% reported having never received anti-phishing training, and 75% said they had never used an anti-phishing tool.

## 4.3.2. Study 2: Procedure

Study 2’s procedure was almost identical to that of Study 1. The only differences were that no manipulations were performed. Instead, to allow us to further explore why users might be reluctant to use our theoretically perfectly accurate tool, all participants were presented with the 100% accuracy, high frequency condition. We further included an information screen that explained how the tool made its decisions to increase users’ perceived transparency. The rationale for these choices was to create an environment that motivates the highest possible reli ance (as Study 1 showed, 100% accuracy and 100% frequency led to the highest possible outcomes, and the literature suggests that high levels of transparency can increase trust) in order to explore user reliance under such conditions. Although the development of a 100% accurate tool may be impossible in practical terms, it is nevertheless theoretically inter esting to examine users’ reliance on tools under such conditions—since only under such conditions can we exclude the explanation that a lack of accuracy causes users’ seemingly irrational reliance behaviors. Furthermore, several studies have developed tools that come very close to perfect levels of accuracy [e.g., 37,36].

## 4.3.3. Study 2: Measurement & validation

We mostly relied on established measures to measure accuracy, transparency, and trust [75,76,59,77]. The measurement for frequency was self-developed and pilot tested and the measurement for distrust was adapted from [59] and also pilot tested. Appendix A and B contains the full measurement instrument.

We used confirmatory factor analysis to evaluate the measurement model [78]. We estimated the model using SmartPLS3.0 [79]. After initial estimation, we dropped items with low loadings, and re-estimated the measurement model. All item loadings were at least 0.76 or higher, significant, and thus above the widely accepted 0.50 threshold. Next, we assessed convergent validity using Cronbach’s alpha and the average variance extracted (AVE). As evident from Table 3, both validity criteria are above the required thresholds of 0.70 and 0.50, respectively [80]. Next, we assessed discriminant validity by comparing construct correlations to the square root of the AVE [81] and found that for each construct, the square root of the AVE was greater than the off-diagonal correlation values. Moreover, we estimated variance inflation factors (VIFs) to evaluate multicollinearity. All VIFs were below the recom mended 3.0 threshold [82]. Further, item-construct loadings and crossloadings were higher on their designated constructs than on others [83]. Collectively, these findings suggest that the measurement model meets established standards.

## 4.3.4. Study 2: Common method Bias (CMB)

In Study 2, we used perceptual measurements for the independent variables, as all participants received the same actual conditions in the study. The dependent variable, user reliance, was observed from users actual behaviors. As argued by Sharma, Yetton and Crawford [84], this type of research design is very robust to CMB. However, we further controlled for CMB affecting other relationships in our model using the measured latent marker variable approach.<sup>8</sup>

<sup>8</sup> The measured latent marker variable (MLMV) approach can help to “partial out” potential CMB [86]. We followed the method of MLMV with constructlevel correction [87]. We used fantasizing as a theoretically unrelated MLMV and measured it with four items. Chin, Thatcher, Wright and Steel [87] suggest that a four-item MLMV can reduce CMB by about 72%. Thus, we are confident that our path estimates are reliable estimates of the true relationships.

Measurement validity statistics.

<table><tr><td>Constructs</td><td>M</td><td>SD</td><td>CA</td><td>CR</td><td>AVE</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>(1) Distrust</td><td>3.30</td><td>1.31</td><td>0.91</td><td>0.94</td><td>0.80</td><td>0.89</td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Perceived accuracy</td><td>5.72</td><td>1.10</td><td>0.95</td><td>0.96</td><td>0.87</td><td>-0.64</td><td>0.93</td><td></td><td></td><td></td></tr><tr><td>(3) Perceived frequency</td><td>6.33</td><td>0.83</td><td>0.82</td><td>0.88</td><td>0.71</td><td>-0.08</td><td>0.28</td><td>0.84</td><td></td><td></td></tr><tr><td>(4) Perceived transparency</td><td>5.29</td><td>1.30</td><td>0.80</td><td>0.88</td><td>0.72</td><td>-0.53</td><td>0.52</td><td>0.22</td><td>0.85</td><td></td></tr><tr><td>(5) Trust</td><td>5.58</td><td>1.24</td><td>0.96</td><td>0.96</td><td>0.74</td><td>-0.56</td><td>0.67</td><td>0.28</td><td>0.46</td><td>0.86</td></tr><tr><td>(6) Reliance</td><td>91.86</td><td>14.88</td><td colspan="2">Observed measure</td><td></td><td>-0.39</td><td>0.51</td><td>0.06</td><td>0.25</td><td>0.39</td></tr></table>

CA = Cronbach’s Alpha; CR = Composite Reliability; AVE = Average Variance Extracted. The square root of the AVE is displayed on the diagonal in bold.

## 4.4. Study 2: Results

Overall, we found that users relied on our tools’ predictions in 91.86% of the cases, well below the anticipated 100% reliance mark. This result is very similar to the results of the 100% accuracy condition from Study 1, which resulted in 91.92% reliance. Across the sample, perceptions of accuracy $( \mathbf { M } = 5 . 7 2 )$ , transparency $( \mathrm { M } = 5 . 2 9 )$ , and fre quency $( \mathbf { M } = 6 . 3 3 )$ ranked high on the 7-point Likert scales, as expected, contributing to generally high levels of trust (M = 5.58) and low levels of distrust (M = 3.30).

Next, we tested our research model. We estimated a model via PLS-SEM using 5000 bootstrapped samples [82]. The estimated model with the controls excluded displayed a standardized root mean square re sidual (SRMR) score of 0.072, which represents a good fit with the data (restrictive cut-off at <0.080) [83]. The $\chi ^ { 2 }$ value was 4471.84 and sig nificant $( p \le 0 . 0 0 1 )$ . Unfortunately, other covariance-based model fit criteria cannot be applied directly to components-based structural equation modeling (SEM) because of a lack of established thresholds [83]. One potential criterion for PLS-SEM is the root mean square error correlation, abbreviated as RMS theta, which for our model scored 0.119. Fig. 3 displays the estimated model with the controls included.

We found significant support for our research model. Overall, our model explained 59% of the variance in trust, 57% of the variance in distrust, and 23% of the variance in reliance. We found support that perceived accuracy $( \beta = 0 . 5 0 , p \leq 0 . 0 0 1 )$ and perceived transparency (β $= 0 . 0 9 , p = 0 . 0 0 7 )$ exert a positive and significant effect on trust. Thus, H3a and H4 are supported. We further found evidence that perceived accuracy $( \beta = - 0 . 3 3 , p \leq 0 . 0 0 1 )$ ), transparency $( \beta = - 0 . 2 6 , p \leq 0 . 0 0 1 )$ and trust $( \beta = - 0 . 3 4 , p \leq 0 . 0 0 1 )$ lead to significant decreases in distrust. Thus, H3b, H5 and H7 are supported. As predicted, we found that in creases in perceived frequency led to significant increases in distrust (β $= 0 . 1 3 , p \leq 0 . 0 0 1 )$ , indicating support for H6. Finally, we find that trust leads to significant increases in user reliance $( \beta = 0 . 3 4 , p \leq 0 . 0 0 1 )$ and distrust exerts a similar but negative significant effect on reliance (β = $- 0 . 1 8 , p \leq 0 . 0 0 1 )$ , indicating support for H8 and H9. Overall, we can confirm that trust and distrust have opposing influences on users’ reli ance, which can, in turn, be explained by users’ perceptions of the tool’s accuracy, transparency, and frequency. Among the controls, only per ceptions of threat severity showed a significant positive effect on reli ance. Furthermore, in an additional robustness check, reported in Appendix C, we show that a high trust/low distrust sub group achieved the highest average reliance with 97.4%, which is the highest level of reliance that has been reported so far (compare Table 1).

## 5. Discussion

We set out to find an answer to our research question: What drives and inhibits users’ reliance on anti-phishing tools? In Study 1, we began by exploring the effects of tool attributes on user reliance, specifically ac curacy and frequency. Using a randomized experiment in which we manipulated accuracy and frequency, we found that while accuracy increases reliance (H1), higher frequency reduces reliance if accuracy i low (H2). We further found evidence that users exhibit lower-thanexpected reliance on even highly accurate tools. Thus, Study 1 ruled out the obvious conjecture that the tools were just not accurate enough and indicated that certain cognitive factors of the user must be at play.

![](/api/attachments/44ARMRF4/fulltext/images/6e3db53958bfb72801c7ad4fff0ce7aed55a78e8f0e87f99917e3f8adf78d9f9.jpg)  
Fig. 3. Estimated user reliance model.  
$^ { * } p \leq 0 . 0 5 0 , ^ { * * } p \leq 0 . 0 1 0 , ^ { * * * } p \leq 0 . 0 0 1$ ; dashed lines depict negative relationships.

In Study 2, we validated a model that provides an explanation for the findings of Study 1. To that end, we conceptualized trust and distrust as the opposing drivers of user reliance. Using a survey experiment, we put subjects through the same experiment as in Study 1 but using only the 100% accuracy and high-frequency condition (which was the bestperforming condition in Study 1). While we found comparable levels of reliance, this time we collected evidence that shed more light on users’ under-reliance. Specifically, we found that trust (H8) and distrust (H9) are important factors of user reliance in that trust increases and distrust decreases user reliance. We further found that users’ perceptions of accuracy (H3a, H3b), transparency (H4, H5), and frequency (H6) predict the trust and distrust of a tool. Finally, we found that if users have high levels of trust in a tool and low levels of distrust, then the average reliance moves to 97.4%. This is the highest degree ever reported in any related study, as previous studies have never breached the 91% mark (see Table 1). This represents a substantial improvement—particularly because every additional 1% increase is harder to obtain than the pre vious one. Furthermore, given that hundreds of thousands of new phishing attacks are executed every year, any 1% increase in reliance could save thousands of users from being victimized. The insights from Study 1 and Study 2 allow us to explain user reliance and offer insights into how to address the issue of under-reliance.

## 5.1. Implications for theory

The theory and findings of our two studies provide novel and reve latory insights into the phenomenon of user reliance on tool predictions

## Table 4

Theoretical contributions.

<table><tr><td>New Findings</td><td>New Insights</td><td>Implication</td></tr><tr><td>Study 1: Overall users&#x27; reliance did not exceed 92%, even with 100% accurate tools.</td><td>There is a limit (i.e., ceiling) to which accuracy drives users&#x27; reliance. The effect is nonlinear. Users consistently under-rely on even highly accurate tools.</td><td>Transformative: Tool accuracy is insufficient to explain users&#x27; reliance.Researchers need to examine more human factors that drive and inhibit reliance.</td></tr><tr><td>Study 2: Trust and distrust influence user reliance.</td><td>Distrust as a new antecedent to reliance. Distrust explains why users do not fully rely on even highly accurate tools.</td><td>Revelatory: Users&#x27; trust and distrust are key human factors that influence how users rely on tools.Distrust, in particular, is critical for understanding users&#x27; under-reliance.Revelatory: Developers should be cautious in displaying tool warnings when they are not sufficiently confident about their accuracy. A larger number of flags will reduce reliance when accuracy is low or moderate.</td></tr><tr><td>Study 1: Frequency moderates the effects of accuracy on reliance.</td><td>Frequency as a new antecedent to distrust. Less is more when accuracy is low or moderate.</td><td rowspan="2">Confirmatory: Users&#x27; understanding of the tool must be developed to reduce distrust. Anti-phishing training should convey knowledge of how tools work to reduce distrust.</td></tr><tr><td>Study 2: Transparency strongly reduces distrust.</td><td>Transparency as a critical antecedent to distrust. Users need to know more about the tools they are supposed to trust and rely on.</td></tr></table>

(Table 4). We offer several contributions related to the effects of tool attributes on user reliance. First, we extend our understanding of the role of accuracy. Although accuracy has already been known to be a key antecedent to reliance, prior research had assumed that more accuracy always leads to more reliance [e.g., 10,17,18,38]. However, in our studies, we showed that there is a ceiling effect, so that even with 100% accurate tools, the average user’s reliance was only between 90% and 92%. Thus, our work offers the novel insight that the effect of accuracy on user reliance is nonlinear. This finding helps explain why the phe nomenon of under-reliance arises.

Because even the most accurate tools will not resolve the issue of users’ under-reliance, our second contribution lies in explaining users under-reliance. Although the issue of users’ under-reliance had already been noted in various other studies (see Table 1), an explanation of the phenomenon has been lacking. Our study advances an explanation based on trust and distrust. Whereas trust has only recently been introduced as a central determinant of users’ reliance on anti-phishing tools [40], our study confirms the central role of trust and extends the literature by showing that distrust is an equally important inhibitor of reliance. Furthermore, since trust and distrust explain 20% of the vari ance in users’ reliance—a high number for variables that capture users actual behaviors—they are a powerful explanation of users’ under reliance. Specifically, we found that users who reported high levels of trust and low levels of distrust had reliance levels around the 97.4% mark. This is the highest reliance level ever observed, and we are therefore confident that trust and distrust are key factors for explaining users’ under-reliance.

Third, our findings reveal a new antecedent of distrust. Regarding tool attributes, we found that not only accuracy but also frequency in fluences trust and distrust. To the best of our knowledge, frequency has not yet been considered in the key reference literatures on phishing, human-computer interaction, and recommendation agents. However, our results show that in conditions with low and moderate accuracy, high frequency actually decreases user reliance (H2) and, even in con ditions of high accuracy, high frequency is associated with users distrust (H6). Consequently, our study advances frequency as a new antecedent to reliance and distrust. The prescriptive, revelatory impli cation is that tools with imperfect accuracy should provide fewer pre dictions (less is more). With an increased number of predictions, users are more likely to observe or expect the tool to make errors—therefore, their distrust of the tool increases and reliance decreases. Consequently, this finding suggests that tools may stimulate higher levels of reliance if they do not make predictions for emails below a specific accuracy threshold. thus also indicating the tool provider's confidence in the re: sults, which may mitigate users’ distrust. However, future research should explore what such thresholds should be to determine the level of confidence that would increase users’ trust in the tool and reduce their distrust.

Fourth, to understand the drivers of trust and distrust, our study confirms accuracy and transparency as antecedents to trust and distrust. While much research has already shown that accuracy and transparency increase trust in technology [e.g., 40,50–55], their effect on driving distrust remains understudied—largely because prior research, such as Komiak and Benbasat [46] and Hsiao [56], never employed quantitative methods such as regression analysis to actually quantify the effects of these factors on distrust. Our study offers new insights by providing a robust test of effects and effect estimates. Specifically, our evidence shows that accuracy and transparency are strong inhibitors of users distrust, making tool accuracy and transparency key factors for reducing distrust and in turn stimulating reliance. Therefore, in addition to making tools as accurate as possible, tool developers should consider providing better explanations of how their tools work. Additionally, managers should consider including content on the accuracy and func tion of tools in anti-phishing training exercises.

Furthermore, we wish to highlight that under-reliance not only pertains to the phishing context but could potentially also resurface in other contexts in which tools offer predictions to users. For example, in the medical field, current advances in predictive technologies allow for the development of diagnostic tools capable of diagnosing diseases with similarly high accuracy levels—i.e., 90% and above [23]. However, if oncologists only partially rely on the predictions of these tools, patients are unnecessarily put at risk. Clearly, user reliance is a pivotal issue in many high-stakes contexts in which tools can provide more accurate predictions than users. For these contexts, our findings also offer important insights into how to persuade users to rely on highly accurate tools.

## 5.2. Implications for practice

Our findings have several practical implications that can help improve the effectiveness of anti-phishing tools. First, we show that tool accuracy is a strong driver of trust and reliance (H1, H3a and H8). Hence, we recommend that developers continue to aim for the highest accuracy possible. If that is not possible, we suggest reducing the number of predictions that do not correspond to the highest-accuracy conditions, given that higher frequency leads to lower reliance in lowaccuracy conditions (H2) and increases distrust (H6). Further, our research suggests that tools must enhance their transparency (i.e., through explanations) to increase users’ trust (H4) and mitigate thei distrust (H5).

Our findings suggest that managers and security professionals who support the implementation, rollout, and publication of anti-phishing tools must find ways of increasing users’ trust and mitigating distrust. We believe that amending anti-phishing training to cover topics on both how the tool works and how it differs and is better than existing/prior technologies could help mitigate this problem. Further, we also suspect that penetration tests that disseminate feigned phishing emails might undermine users’ trust in the tools, because such feigned attacks circumvent typical anti-phishing defenses and thus convey to users the message that current anti-phishing defenses cannot be trusted. Therefore, relaying failures of anti-phishing technologies to users through these feigned attacks increases users’ perceptions of flaws in the system and subsequently their level of distrust toward the technology. Addi tionally, for tools with extremely high levels of accuracy, our study further suggests that developers should consider not including the user in decisions if complete reliance is the goal of the technology. Depending on the context, this might produce better outcomes than users insuffi ciently relying on highly accurate tools. However, we acknowledge that there may be instances in which complete reliance on a technology is not necessarily the end goal (e.g., physicians leveraging a prediction tool to explore treatment options).

## 5.3. Limitations and future work

Our research has several limitations. First, a caveat to our findings is that the actual tool that participants were asked to use was a completely new tool that had not been previously used by any of the participants. As Chen, Zahedi, Abbasi and Dobolyi [40] showed, with more experience, users calibrate their reliance on tools. However. Chen et al. also found that even with substantial experience, users are insufficiently reliant on highly accurate tools. In any case, we expect our findings to hold even when users have more experience with the tool, given that even normal users with years of experience do not trust tools, as evident by them regularly checking their junk folders.

Second, one might argue that achieving 100% user reliance is un realistic. Countering this argument, we note that, in other contexts, users have even been shown to exhibit over-reliance, relying more on a tool than would be appropriate. For example, it has been argued that pilots rely excessively on auto-piloting systems [85]. We see no reason to doubt that achieving full user reliance is unreasonable in this context. Furthermore, the reliance levels reported in this study are especially high because of the experimental conditions we chose. We chose these conditions intentionally to create the highest reliance outcomes possible in order to verify whether 100% reliance is achievable even with 100% accurate tools in favorable conditions. As our literature review revealed (see Table 1), subjects in more ecologically valid conditions (i.e., with deception) are by magnitudes less likely to follow tool predictions and more likely to fall victim to phishing attacks. Hence, although the goal of 100% might not ever be reached, every small improvement in reliance could prevent thousands of victimizations.

Third, we did not manipulate the transparency aspect of tools— primarily because our core interest was to understand whether a perfectly accurate tool could engender full reliance. To that end, we provided all users with explanations of the tool so that they were aware of the accuracy levels it could provide and what 100% accuracy really means. Adding explanations as a third manipulation would have doubled the treatment conditions in our research design. As we already had six treatment conditions, we chose the benefit of higher power over the benefit of adding another manipulation of a variable that has obvious effects.

Fourth, future research could further extend our model by inte grating various factors that influence human cognition—for example, biases, personality traits such as conscientiousness and trust tendencies, and other emotions. Doing so would afford the opportunity to extend the flourishing research stream on users’ reliance on security messages and detectors [e.g., 13, 73, 89]—which is becoming increasingly important in an increasingly digitalized and interconnected world.

## CRediT authorship contribution statement

Sebastian W. Schuetz: Conceptualization, Methodology, Valida tion, Formal analysis, Investigation, Resources, Data curation, Writing – original draft, Writing – review & editing, Project administration, Visualization. Zachary R. Steelman: Conceptualization, Methodology, Software, Validation, Investigation, Resources, Data curation, Writing – review & editing, Project administration. Rhonda A. Syler: Conceptu alization, Methodology, Validation, Investigation, Resources, Data curation, Writing – review & editing, Project administration.

## Appendix. Supplementary data

Supplementary data to this article can be found online at https://doi. org/10.1016/i.dss.2022.113846.

## References

[1] A. Abbasi, D.G. Dobolyi, A. Vance, F.M. Zahedi, The phishing funnel model: a design artifact to predict user susceptibility to phishing websites, Inf. Syst. Res. 32 (2) (2021) 410–436.

[2] R. Chen, J. Gaia, H.R. Rao, An examination of the effect of recent phishing encounters on phishing susceptibility, Decis. Support. Syst. 133 (2020).

[3] M.L. Jensen, M. Dinger, R.T. Wright, J. Thatcher, Training to mitigate phishing attacks using mindfulness techniques, J. Manag. Inf. Syst. 34 (2) (2017) 597–626.

[4] A. Vishwanath, T. Herath, R. Chen, J. Wang, H.R. Rao, Why do people get phished? Testing individual differences in phishing vulnerability within an integrated, information processing model, Decision Support Systems 51 (3) (2011) 576–586.

[5] J. Wang, Y. Li, H.R. Rao, Coping responses in phishing detection: an investigation of antecedents and consequences, Inf. Syst. Res. 28 (2) (2017) 378–396.

[6] I. Ponemon, The Cost of Phishing & Value of Employee Training, 2015.

[7] Anti-Phishing Working Group, Phishing Attack Trends Report - 1Q 2021, 2021.

[8] M. Rosenthal, Must-Know Phishing Statistics: Updated 2021, 2021.

[9] L.H. Newman, Inside Google’s global campaign to shutdown phishing, in, (Wired), 2017.

[10] A. Abbasi, F.M. Zahedi, D. Zeng, Y. Chen, H. Chen, J.F. Nunamaker, Enhancing predictive analytics for anti-phishing by exploiting website genre information, J. Manag. Inf. Syst. 31 (4) (2015) 109–157.

[11] A. Abbasi, Z. Zang, D. Zimbra, H. Chen, J.F. Nunamaker, Detecting fake websites:

[12] J. Hong, The current state of phishing attacks, Commun. ACM 55 (1) (2012) 74–81

[13] E.M. Zahedi, A. Abbasi. Y. Chen, Fake-website detection tools: identifving elements that promote individuals' use and enhance their performance. J. Assoc. Inf. Syst. 16 (6) (2015) 448–484.

[14] J. Wang, Y. Li. H.R. Rao, Overconfidence in phishing email detection, J. Assoc, Inf

[15] R. Richmond, The RSA hack: how they did it, 2011, p. 1.

[16] E. Osnos, D. Remnick, J. Yaffa, Trump, Putin, and the new cold war, in, The New Yorker (2017). https://www.newyorker.com/magazine/2017/03/06/trump-pu tin-and-the-new-cold-war.

[17] A. Abbasi, F. Zahedi, Y. Chen, Impact of anti-phishing tool performance on attack success rates. in: International Conference on Intelligence and Security Informatics (ISI), (Washington, D.C., USA), 2012, pp. 12–17.

[18] S. Egelman, L.F. Cranor, J. Hong, You’ve Been Warned: An Empirical Study of the Effectiveness of Web Browser Phishing Warnings, in: CHI, ACM, Florence, Italy, 2008, pp. 1065–1074.

[19] APWG, 4Q 2016, in: Phishing Activity Trends Report, 2017.

[20] Department of Public Safety, Phishing: How Many Take the Bait, 2015.

[21] S. Tseng, B.J. Fogg, Credibility and computing technology, Commun. ACM 42 (5) (1999) 39–44.

[22] M. Wu, R.C. Miller, S.L. Garfinkel, Do security toolbars actually prevent phishing attacks?, in: CHI '06, (Montréal, Ouébec, Canada, 22-27), 2006, pp. 601–610.

[23] A. Burt, A. Volchenboum, How Health Care Changes When Algorithms Start Making Diagnoses. Havard Business Review, 2018.

[24] A. McAfee, Big Data’s Biggest Challenge? Convincing People NOT to Trust thei Judgment, in, 2013.

[25] R.T. Wright, K. Marett, The influence of experiential and dispositional factors in phishing: an empirical investigation of the deceived, J. Manag. Inf. Syst. 27 (1) (2010) 273–303.

[26] R.T. Wright, M.L. Jensen, J.B. Thatcher, M. Dinger, K. Marett, Research note—influence techniques in phishing attacks: an examination of vulnerability and resistance, Inf. Syst. Res. 25 (2) (2014) 385–400.

[27] R.C. Dodge, C. Carver, A.J. Ferguson, Phishing for user security awareness, Computers and Security 26 (1) (2007) 73–80.

[28] S. Goel, K. Williams, E. Dincelli, Got phished: internet security and human vulnerability, J. Assoc. Inf. Syst. 18 (1) (2017) 22–44.

[29] R.T. Wright, M.L. Jensen, J.B. Thatcher, M. Dinger, K. Marett, Influence techniques in phishing attacks: an examination of vulnerability and resistance, Inf. Syst. Res. 25 (2) (2014).385–400.

[30] K.W. Hong, C.M. Kelley, R. Tempa, E. Murphy-Hill, C.B. Mayhorn, Keeping up with the Joneses: Assessing phishing susceptibility in an email task, in: Proceedings of the Human Factors and Ergonomics Society Annual Meeting, (SAGE Publications, Los Angeles, CA, 2013, pp. 1012–1016.

[31] P. Kumaraguru, S. Sheng, A. Acquisti, L.F. Cranor, J. Hong, Teaching Johnny not to fall for phish, ACM Trans. Internet Technol. 10 (2) (2010) 1–31.

[32] P. Kumaraguru, Y. Rhee, S. Sheng, S. Hasan, A. Acquisti, L.F. Cranor, J. Hong, Getting Users to Pay Attention to Anti-Phishing Education: Evaluation of Retention and Transfer. in: APWG eCrime Researchers Summit. (Pittsburgh. PA. USA). 2007. pp. 70–81.

[33] J. Leach, Improving user security behaviour, Computers & Security 22 (8) (2003) 685–692

[34] C. Ngvuen, M.L. Jensen, E. Day, Learning Not to Take the Bait: A Longitudinal Examination of Digital Training Methods and Overlearning on Phishing Susceptibility, European Journal of Information Systems, 2021. Online Preprint.

[35] S. Sheng, B. Wardman, G. Warner, L.F. Cranor, J. Hong, An empirical analysis of phishing blacklists, in: Sixth Conference on Email and Anti-Spam (CEAS), (Mountain View, CA, USA). 2009.

[36] S. Smadi, N. Aslam, L. Zhang, Detection of online phishing email using dynamic evolving neural network based on reinforcement learning, Decis. Support. Syst. 107 (2018) 88–102.

[37] G. Ramesh, I. Krishnamurthi, K.S.S. Kumar, An efficacious method for detecting phishing webpages through target domain identification, Decis. Support. Syst. (2014) 12–22.

[38] S. Egelman, S. Schechter, The Importance of Being Earnest [in Security Warnings], in: International Conference on Financial Cryptography and Data Security Springer, Berlin, Heidelberg, 2013, pp. 52–59.

[39] A. Vance, J.L. Jenkins, B.B. Anderson, D.K. Bjornn, C.B. Kirwan, Tuning out security warnings: a longitudinal examination of habituation through fMRI, eye tracking, and field experiments, MIS Q. 32 (2) (2018) 355–380.

[40] Y. Chen, F. Zahedi, A. Abbasi, D.G. Dobolyi, Trust calibration of automated security IT artifacts: a multi-domain study of phishing-website detection tools, Inf. Manag. 58 (1) (2021).

[41] M. Hilbert, Toward a synthesis of cognitive biases: how Noisy information processing can Bias human decision making, Psychol. Bull. 138 (2) (2012)

[42] E. Karahanna, I. Benbasat, R. Bapna, A. Rai, Editor’s comments: opportunities and challenges for different types of online experiments, MIS Q. 42 (4) (2018) iii–x.

[43] L. Wang, G.A. Jamieson, J.G. Hollands, Trust and reliance on an automated combat identification system. Hum. Factors 51 (3) (2009) 281–291.

[44] K. van Dongen. P.-P. van Maanen, A framework for explaining reliance on decisior aids, International Journal of Human-Computer Studies 71 (2013) 410–424.

[45] J.D. Lee, K.A. See, Trust in Automation: designing for appropriate reliance, Hum. Factors 46 (1) (2004) 50–80.

[46] S.Y.X. Komiak, I. Benbasat, A two-process view of trust and distrust building in recommendation agents : a process-tracing study. J. Assoc, Inf, Syst, 9 (12) (2008)

[47] G. Bansal. Restoring trust after an insider breach: both the genders matter—CEOs and users J Comput Inf Syst, 61 (1) (2019) 11-29

[48] N. Lankton, D.H. McKnight, J.B. Thatcher, Incorporating trust-in-technology into expectation disconfirmation theory, J. Strateg, Inf, Syst. 23 (2) (2014) 128–145.

[49] I. Qureshi, Y. Fang, N. Haggerty, D.R. Compeau, X. Zhang, IT-mediated social interactions and knowledge sharing: role of competence-based trust and background heterogeneity, Inf. Syst. J. 28 (5) (2018) 929–955.

[50] A. Bussone, S. Stumpf, D. O’Sullivan, The role of explanations on trust and reliance in clinical decision support systems, in: International Conference on Healthcare Informatics, IEEE, 2015, pp. 160–169.

[51] M.T. Dzindolet, S.A. Peterson, R.A. Pomranky, L.G. Pierce, H.P. Beck, The role of trust in automation reliance. International Journal of Human-Computer Studies 58 (2003) 697–718.

[52] S.Y.X. Komiak, I. Benbasat, The effects of personalization and familiarity on trust and adoption of recommendation agents, MIS O. 30 (4) (2006) 941–960

[53] J.M. Leimeister, W. Ebner, H. Krcmar, Design, implementation, and evaluation of trust-supporting components in virtual communities for patients, J. Manag. Inf. Syst. 21 (4) (2005) 101–135.

[54] W. Wang, I. Benbasat, Empirical assessment of alternative designs for enhancing different types of trusting beliefs in online recommendation agents, J. Manag. Inf. Syst. 33 (3) (2016) 744–775.

[55] W.Q. Wang, M. Wang, Effects of sponsorship disclosure on perceived integrity of biased recommendation agents: psychological contract violation and knowledge based trust perspectives, Inf. Syst. Res. 30 (2) (2019) 507–522

[56] R.L. Hsiao, Technology fears: distrust and cultural persistence in electronic marketplace adoption, J. Strateg. Inf. Syst. 12 (3) (2003) 169–199.

[57] D.H. McKnight, M. Carter, J.B. Thatcher, P.F. Clay, Trust in a Specific Technology: an investigation of its components and measures, ACM Trans. Manag. Inf. Syst. 2 (2) (2011) 12.

[58] A. Dimoka, What does the brain tell us about trust and distrust? Evidence from a Functional Neuroimaging Study, MIS Quarterly 34 (2) (2010) 373–396.

[59] P.B. Lowry, D.W. Wilson, W.L. Haig, A picture is worth a thousand words: source credibility theory applied to logo and website design for heightened credibility and consumer trust, International Journal of Human-Computer Interaction 30 (1) (2013) 63–93.

[60] H. McKnight, C. Kacmar, V. Choudhury, Whoops... did I use the wrong concept to predict e-commerce trust? Modeling the risk-related effects of trust versus distrust concepts, in: 36th Annual Hawaii International Conference on System Sciences, (Big Island, HI, USA) 6-9, 2004, pp. 10–20.

[61] D. McKnight, N.L. Chervany, What trust means in e-commerce custome relationships: an interdisciplinary conceptual typology, Int. J. Electron. Commer. 6 (2) (2002) 35–53.

[62] G. Ho, D. Wheatley, C.T. Scialfa, Age differences in trust and reliance of a medication management system, Interact. Comput. 17 (2005) 690–710.

[63] W. Wang, I. Benbasat, Recommendation agents for electronic commerce: effects of explanation facilities on trusting beliefs, J. Manag. Inf. Syst. 23 (4) (2o07 217-246.

[64] B. Xiao. I. Benbasat. Product-related deception in E-commerce: a theoretical perspective. MIS 0. 35 (1) (2011) 169–195.

[65] D. McKnight, V. Choudhury, Distrust and Trust in B2C E-Commerce: Do they Differ?, in: International Conference on Electronic Commerce (ICEC). Frederiction Canada, 2006.

[66] D. McKnight, C. Kacmar, V. Choudhury, Dispositional trust and distrust distinctions in predicting high- and low-risk internet expert advice site perceptions, e-Service Journal 3 (2) (2004) 33–55

[67] U. Panniello, Gorgoglione, Tuzhilin, research note - in CARSs we trust: how context-aware recommendations affect Customers' Trust and other business performance measures of recommender systems, Inf. Syst. Res, 27 (1) (2016) 182-196.

[68] M. Sollner, ¨ J.M. Leimeister, D. Gefen, P.A. Pavlou, Trust, in: A.B.A.A. Ra (Ed.), An MIS Quarterly Research Curation, 2016, pp. 1–9.

[69] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Q. 13 (3) (1989) 319–340

[70] N.F. Awad, A. Ragowsky, Establishing trust in electronic commerce through online word of mouth: an examination across genders, J. Manag. Inf. Syst. 24 (4) (2008) 101–121.

[71] A. Vance, C. Elie-Dit-Cosaque, D.W. Straub, Examining trust in information technology artifacts: the effects of system quality and culture, J. Manag. Inf. Syst. 24 (4) (2008) 73–100

[72] W. Wang, I. Benbasat, Trust in and adoption of online recommendation agents, J. Assoc. Inf. Syst. 6 (3) (2005) 72–101.

[73] S.R. Boss, D.F. Galletta, P.B. Lowry, G.D. Moody, P. Polak, What do systems users have to fear? Using fear appeals to engender threats and fear that motivate protective security behaviors, MIS Quarterly 39 (4) (2015) 837–864.

[74] S.W. Schuetz, P.B. Lowry, D.A. Pienta, J.B. Thatcher, Effectiveness of abstract versus concrete fear appeals in information security, J. Manag. Inf. Syst. 37 (3) (2020) 723–757.

[75] Y. Chen, F. Zahedi, Individual’s internet security perceptions and behaviors: Polycontextual contrasts between the United States and China, MIS Q. 40 (1)

[76] N.K. Lankton, D.H. McKnight, J. Tripp, Technology, humanness, and trust: rethinking Trust in Technology, J. Assoc, Inf, Syst, 16 (10) (2015) 880–918

[77] W. Wang, L. Oui, D. Kim, I. Benbasat. Effects of rational and social appeals of online recommendation agents on cognition- and affect-based trust. Desicion Support Syst. 86 (2016) 48–60.

[78] D.W. Straub. M.-C. Boudreau, D. Gefen, Validation guidelines for IS positivist

[79] C.M. Ringle, S. Wende, J.-M. Becker, SmartPLS 3, in: SmartPLS (Bonningstedt)¨

[80] D. Gefen, D. Straub, M.-C. Boudreau, Structural equation modeling techniques and regression: guidelines for research practice, Communications of AIS 4 (7) (2000) 1–77.

[81] C. Fornell, D.F. Larcker, Evaluating structural equation models with unobservable variables and measurement error, J. Manag. Res. 18 (1) (1981) 39–50.

[82] J. Hair, C.L. Hollingsworth, A.B. Randolph, A. Chong, An updated and expanded assessment of PLS-SEM in information systems research, Ind. Manag. Data Syst. 117 (3) (2017) 442–458.

[83] J. Henseler, G.S. Hubona, P.A. Ray, Using PLS path modeling in new technology research: updated guidelines. Ind. Manag. Data Syst. 116 (1) (2016) 2–20.

[84] R. Sharma, P. Yetton, J. Crawford, Estimating the effect of common method variance: the method—method pair technique with an illustration from TAM research, MIS Q. 33 (3) (2009) 473–490.

[85] D. Dalcher, Why the pilot cannot be blamed: a cautionary note about excessive reliance on technology, International Journal on Risk and Assessment Management 7 (3) (2007) 350–366.

[86] P.M. Podsakoff, S.B. MacKenzie, N.P. Podsakoff, Sources of method bias in social science research and recommendations on how to control it. Annu. Rey. Psychol. 63 (2012) 539–569.

[87] W.W. Chin, J.B. Thatcher, R.T. Wright, D. Steel, Controlling for common method variance in PLS analysis: The measured latent marker variable approach, in: New Perspectives in Partial Least Squares and Related Methods, (Springer Science+ Business Media, New York, NY, US, 2013, pp. 231–239.

Sebastian W. Schuetz is an Assistant Professor at Florida International University. He received his Ph.D. in information systems from the City University of Hong Kong in 2017. His research interests relate to information security management. His work has appeared in Management Science, Journal of Applied Psychology, Journal of the AIS, Journal of Man agement Information Systems, European Journal of Information Sysems, Information Systems Journal, Information Technology & People, Internet Research, International Journal of Infor mation Manggement. and several international conferences.

Zachary R. Steelman is an Associate Professor of Information Systems in the Walton College of Business at the University of Arkansas. He has authored refereed publications in prominent IS journals and conferences such as Information Systems Research, MIS Quarterly, MIS Quarterly Executive, Information Systems Journal, Communications of the Association of Information Systems, Americas Conference on Information Systems, and the Hawaii Interna tional Conference on System Sciences. He was recently awarded the 2020 Association of Information Systems Early Career Award which “recognizes individuals in the early stages of their careers who have already made outstanding research, teaching, and/or service contributions to the field of information systems”. His research interests include the se lection, development, and management of IT portfolios for individuals, teams, and orga nizations. He has worked with a variety of Fortune 500 organizations to examine the impact of IT infrastructure and policy changes on individuals and the organization, spe cifically within the context of IT consumerization.

Rhonda A. Syler is Associate Professor, R. Jarl Bliss Faculty Fellow, and Department Chair of the Computer Information Systems & Business Analytics Department of the College of Business at James Madison University. Dr. Syler has researched, taught, and consulted in analytics, cybersecurity, IoT and blockchain, and her current research focuses on behav ioral and organizational aspects of cybersecurity and the societal and organizational im pacts of disruptive technologies such as the Internet of Things (IoT). Syler’s interests also include smart city design and the use of emerging technologies in rural community development, resiliency, and sustainability. Syler has co-developed an Internet of Things Lab designed to provide a learning and innovation environment for big data, security, ERP, mobile development, and cloud computing and has developed data- and analytic-driven curriculum projects with Fortune 500 companies. Syler was previously the coordinator of the cybersecurity and data management program in the Walton College of Business at the University of Arkansas. She is the co-chair of ICIS 2025 and has previously served as a Vice President for the Association of Information Systems and president of the AIS Specia Interest Group for Information Systems Education.
