---
otero_id: 25385
otero_key: "8NXA5XV5"
title: "Mitigating the Adverse Effect of Monetary Incentives on Voluntary Contributions Online"
authors: "Dandan Qiao; Shun-Yang Lee; Andrew B. Whinston; Qiang Wei"
year: "2021"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2021.1870385"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mitigating the Adverse Effect of Monetary Incentives on Voluntary Contributions Online

Dandan Qiao, Shun-Yang Lee, Andrew B. Whinston & Qiang Wei

To cite this article: Dandan Qiao, Shun-Yang Lee, Andrew B. Whinston & Qiang Wei (2021) Mitigating the Adverse Effect of Monetary Incentives on Voluntary Contributions Online, Journal of Management Information Systems, 38:1, 82-107, DOI: 10.1080/07421222.2021.1870385

To link to this article: https://doi.org/10.1080/07421222.2021.1870385

![](/api/attachments/8NXA5XV5/fulltext/images/422d882dcc904f87e68396b43b76a887213bf7a87d45758f633f4f71b99e29fe.jpg)

View supplementary material

![](/api/attachments/8NXA5XV5/fulltext/images/76114ce46920ddd04c54cbdb1cd87856a19e227a01f0dc0108ba65eb57d8701f.jpg)

Published online: 02 Apr 2021.

![](/api/attachments/8NXA5XV5/fulltext/images/af36c28bf3f821c2fbde22e0328befcfa6df02bc60f1f5ca2402f6f3f64a02f8.jpg)

Submit your article to this journal

![](/api/attachments/8NXA5XV5/fulltext/images/fe709738e8dc8802f69aeb61af60b89f5cb288c3792ae4528921834828765e16.jpg)

Article views: 106

![](/api/attachments/8NXA5XV5/fulltext/images/cd6bae50e9ad2f6e49bc910fb290d394c14bb07c07443842c42df8f010bf558f.jpg)

View related articles

![](/api/attachments/8NXA5XV5/fulltext/images/7cf22cc0ebe496ed0f36d1716287e5700834cd445dd91bfb635002177450a87b.jpg)

View Crossmark data

Check for updates

# Mitigating the Adverse Efect of Monetary Incentives on Voluntary Contributions Online

Dandan Qiao<sup>a</sup>, Shun-Yang Lee<sup>b</sup>, Andrew B. Whinston<sup>c</sup>, and Qiang Wei <sup>d</sup>

<sup>a</sup>National University of Singapore, Singapore; <sup>b</sup>Northeastern University, Boston, MA, USA; <sup>c</sup>University of Texas at Austin, Austin, TX, USA; <sup>d</sup>Tsinghua University, Beijing, P.R. China

## ABSTRACT

Numerous online information systems (e.g., question and answer [Q&A] forums, citizen science communities, and review websites) rely heavily on volunteer contributions. Managers have used monetary incentives to induce individuals to increase their contribution level. However, monetary incentives could also generate adverse efects, which could dampen individuals’ intrinsic motivation and lead to lower contribution quality when incentives are small. To address this issue, we propose two intervention strategies, goal-setting and challenge-seeking, and conduct a series of randomized experiments. We find that small monetary incentives, when combined with the appropriate intervention strategies, can motivate users to increase contribution quantity while simultaneously sustaining high quality. Thus, integrating such intervention strategies with small incentives can be a cost-efective way to encourage voluntary contributions. Our research contributes to the literature on incentive provision and provides theoretical and practical implications for platforms relying on voluntary contributions.

## KEYWORDS

Co-creation; online incentives; intrinsic motivation; extrinsic motivation; altruism; monetary incentives; goalsetting; challenge-seeking; user-generated content; UGC

## Introduction

Voluntary contribution by individuals has become a key component of many online platforms. For example, the content of Wikipedia, the largest online encyclopedia, is provided and edited mainly by more than 91 million voluntary contributors as of August 2020.<sup>1</sup> Many open source software projects similarly rely on volunteer contributions to develop and maintain them. Other examples of online volunteer behavior include content-sharing communities such as review websites, blogs, financial advice platforms, and question and answer (Q&A) forums. Users on these content-sharing communities voluntarily contribute time and efort creating and sharing content [15, 22, 60]; this is also known as online public goods [59]. In addition, non-profit organizations (NPOs) seek volunteers to engage in both online and ofline tasks, such as correction and transcription, contextualization, and complementing collections [2]. A popular example is the website Zooniverse,<sup>2</sup> which engages millions of active volunteers to facilitate citizen science via unpaid crowdsourcing work. In summary, many entities, including content-sharing websites and NPOs rely on voluntary contributions by individuals.

Although tremendous value may be derived from this variety of online voluntary contribution, one important question concerns how best to direct and sustain individual participation and behavior. Research shows that showing contributions from friends can encourage individuals to increase their own contribution in an online review community [36]. There have also been numerous attempts and eforts to use monetary incentives to motivate online voluntary behavior on platforms including e-commerce websites, Q&A forums, open source software websites, and financial opinion sharing websites. These incentives tend to be small so as to lessen the financial burden on the platforms, especially platforms with a large user base. The use of monetary incentives to encourage voluntary contributions leads to concerns regarding the efectiveness of such incentives [6, 12]. Although there could be a quantitative increase in engagement volume, monetary incentives do not ensure quality improvement and can even undermine contributor performance. For example, evidence shows that reviewers tend to reduce review length and show biased sentiments in their postings [6, 7, 38, 51, 58]. In the context of an investment-related website, Seeking Alpha, H. Chen et al. find that monetary incentives are efective in increasing the amount of content produced but not the quality of the stock recommendations [12]. Even the use of virtual organizational rewards can undermine individuals knowledge-sharing behavior [61].

One main reason why monetary incentives have a negative efect is that individuals’ attribution changes due to the incentives. Based on the self-perception theory [4, 20, 31], individuals are inclined to seek to explain their own behavior. In the context of voluntary activities, individuals observe their own voluntary contribution and conclude that they themselves must be somewhat altruistic. However, if monetary incentives are ofered, these individuals shift their focus from altruism to the incentives [20, 31], which leads them to discount their prosocial motivation. This reduction in prosocial motivation can lead to a decreased desire to be helpful, less efort invested, and lower-quality performance. As an example, a post from Zooniverse<sup>3</sup> states that “payments distort the motivations of participants in citizen science projects and could hence bring potential negatives.” Thus, we hope to identify solutions to help mitigate monetary incentives’ negative efect on prosocial contribution quality while still motivating individuals to increase their contribution quantity.

To the best of our knowledge, few studies investigate ways to mitigate the adverse efect of incentives. Burtch et al. proposed combining social norms with financial incentives in soliciting review writing [6]; this may serve as a starting point in alleviating the adverse efect. Our paper aims to fill the gap in the literature by exploring strategies to counter the adverse efect of monetary incentives in various online prosocial contexts. Specifically, we propose a goal-setting approach and a challenge-seeking approach. Since the adverse efect is a result of individuals’ attention shift from the altruistic nature of voluntary behavior to the monetary rewards [31], a potential intervention strategy could try to discount the role of monetary incentives by directing individuals to refocus on intrinsic motivation. We believe that both goal-setting and challenge-seeking can help achieve this goal, for the following two reasons. First, goal-setting has been shown to be efective in increasing individuals’ intrinsic motivation to perform better [41, 43], such as improving productivity in work environments [28, 47] and athletic performance [58]. This is because reaching a goal can foster a sense of achievement and competence, thereby motivating individuals to exert more efort and engagement, which are generally associated with higher performance quality. Second, prior studies show that a certain level of challenge in tasks can serve as a stimulus for performance improvement [8, 48, 49] because the desire to overcome challenges stimulates individuals to increase their eforts. We hence expect that the challenging-seeking strategy can help increase individuals’ intrinsic motivation in conducting voluntary tasks, thereby mitigating monetary incentives’ negative efects.

We conducted a series of experiments to examine the efectiveness of goal-setting and challenge-seeking in mitigating the adverse efect of monetary incentives. In the first experiment, we recruited subjects from Amazon Mechanical Turk (MTurk) and provided them with various levels of monetary incentives to help with an audio transcription task.<sup>4</sup> In this experiment, we explicitly combined monetary incentives with either a goal-setting or a challenge-seeking condition. We then observed how subjects’ behavior changed in response to the monetary incentive and how goal-setting and challenge-seeking strategies could moderate the efect of the monetary incentive. Our results show that individual contribution quality decreases as a result of receiving small monetary incentives, where contribution quality is measured by transcription error rate. This finding is consistent with earlier studies that demonstrate the crowding-out efect of small-scale monetary incentives [24, 26]. More importantly, we find that individuals who were assigned to the goal-setting or challenge-seeking conditions did not appear to sufer from such adverse efect. This finding suggests that goal-setting and challenge-seeking strategies can be used in conjunction with monetary incentives to motivate voluntary contributions without sacrificing contribution quality. These results are robust to diferent experimental designs and tasks.

Although information systems researchers have begun to study the interplay of monetary incentives and voluntary contributions, previous studies are limited mainly to discussing monetary incentives’ negative efects on voluntary behavior. We contribute to the literature by identifying actionable and cost-efective methods to mitigate monetary incentives negative efects on contribution quality while preserving their positive efects on contribution quantity. This is particularly important for practitioners, because many online platforms rely on voluntary contributions to operate, and NPOs often hope to attract online volunteers. Our findings may help managers better design their incentive provision strategies, thereby promoting improved voluntary contributions.

## Hypothesis Development

## Voluntary Behavior and Monetary Incentives

While monetary incentives are often used to motivate individual behavior, such as in the workplace and in prosocial settings [46], they can backfire and lead to undesired outcomes, known as the crowding-out efect [21]. For example, research shows that introducing monetary incentives reduces volunteers’ efort in collecting donations [26]. This is because external incentives can decrease individuals’ intrinsic motivations and subsequently lead to performance deterioration. The crowding-out efect can be explained by the self-perception theory: people tend to develop attitudes/motives to which their behavior can be attributed [4, 20, 42]. In a prosocial context, individuals use altruism to rationalize why they are performing a specific prosocial activity. When external rewards are ofered, the salience of the original intrinsic motivation (i.e., altruism) decreases. People tend to enter an economic thinking mode in which they are more likely to attribute their behavior to external rewards [31]. Consequently, individuals’ prosocial contributions tend to deteriorate as a result of the decrease in their intrinsic motivations.

## Potential Impact on Quality vs. Quantity

The literature shows that the crowding-out efect from the introduction of extrinsic incentives impacts quality more than quantity [34]. Cerasoli et al. compared the relative importance of incentives and intrinsic motivation in predicting performance [10]. These authors argue that incentives can be the dominant factor in quantity-based performance criteria. This is because incentives tie financial outcome directly to performance quantity. Thus, incentives can help individuals focus their attention and behavior toward increasing quantity. Jenkins et al. show that incentives are good predictors of performance outcomes measured by quantity [34]. Taken together, these arguments suggest that contribution quantity should respond positively to incentives.

In contrast, quality-based criteria require individuals to be absorbed in the task and work autonomously, and intrinsically motivated individuals are more likely to behave in these ways [10]. Additionally, Cerasoli et al. find that intrinsic motivation is a better predictor of quality than incentives [10]. These arguments suggest that contribution quality should respond positively to intrinsic motivation. Recall that introduction of incentives tends to decrease individuals’ intrinsic motivation [6, 16, 38]. Therefore, it follows that contribution quality will decrease with introduction of incentives as intrinsic motivation is decreased and individuals consequently exert less efort.

Diferences in the impact of extrinsic incentives on performance quality versus quantity are also found in online prosocial contributions. For example, studies show that ofering monetary incentives not only leads to a large increase in review quantity, but also a decrease in review quality as manifested by reduced review length [38] and sentiment biases [7, 38, 58]. These studies provide additional evidence that incentives’ crowding-out efect may have diferential impacts on contribution quality and quantity.

Moreover, previous studies find that the negative impacts of monetary incentives on performance quality are most pronounced for small incentives [24, 26]. Based on the self-perception theory, introduction of monetary incentives leads individuals to focus on the payments and to discount their intrinsic motivations. In the presence of such monetary incentives, people enter an exchange mode, in which they extend eforts commensurate with payments [31]. When monetary incentives are ofered at a small scale, people tend to exert only the minimum efort required [38]. Together with the decrease in intrinsic motivation, the negative crowding-out efect on contribution quality is particularly notable. In contrast, as incentive size increases, the relative price efect of incentives begins to dominate [25, 26], leading individuals to exert more efort. As a result, a large enough incentive can potentially lead to an increase in contribution quality. This nonlinear relationship in the efect of monetary incentives on prosocial behavior is referred to in the literature as the W efect, where small payments may significantly reduce contribution eforts and quality [24, 25, 26, 55]. We therefore propose the following hypothesis:

Hypothesis 1 (HQ1): Small incentives decrease contribution quality in a prosocial context.

## Mitigating the Adverse Efect of Monetary Incentives

Due to the discussed change in attribution and decrease in intrinsic motivation, a small monetary incentive could stimulate more participation and contribution quantity in voluntary activities at the cost of decreased quality. Therefore, an efective strategy of mitigating the adverse efect of monetary incentives would need to restore intrinsic motivation to engage in prosocial activities [14, 29, 30]. We propose two such strategies in the following sections.

## Goal-Setting

According to goal-setting theory, setting goals can improve individual performance, because goals help individuals direct their attention and efort toward goal-relevant activities, increase persistence, and activate task-relevant knowledge [43]. The motivational efect of goal-setting has been demonstrated in diferent contexts [47]. For example, managers often introduce goals to solicit higher employee work performance [40]. In online forums such as Q&A communities, goal-setting plays a critical role in user content contributions [27, 37]. Generally speaking, a goal-setting approach is efective because it helps increase individuals’ intrinsic motivations [19, 52].

In addition, goals represent concrete standards to assess individual performance, and fulfillment of such standards can make individuals feel competent. Goals can encourage individuals to focus on performing competently, consequently promoting intrinsic motivation [19]. Research shows that individuals display higher levels of intrinsic motivation when exposed to pre-set goals [18] and the need for competence plays a mediating role in this process [3]. To the extent that attaining a goal satisfies individuals’ need for competence, their intrinsic motivations in conducting the activities increase. Consequently, individuals are more committed to and exert more efort toward these goal-relevant activities [43]. Research also finds a strong association between efort/engagement investment and performance quality [10, 13, 18, 54]. Thus, we expect that goal-setting can help improve contribution quality by promoting intrinsic motivation and encouraging efort investment. The efectiveness of goal-setting in improving individual performance quality can also be found in domains such as sports [57] and work environments [47].

Recall that our objective is to mitigate the adverse efect of external incentives on prosocial contributions. Since quality crowding-out is driven mainly by decreased intrinsic motivation, we expect goal-setting to restore lost intrinsic motivation, thus attenuating quality deterioration. Therefore, we set forth the following hypothesis:

Hypothesis 2 (HQ2): Goal-setting can mitigate the quality reduction efect induced by small incentives in a prosocial context.

## Challenge-Seeking

In addition to goal-setting, we propose challenge-seeking as another strategy to mitigate the crowding-out efect of external incentives on prosocial contributions. The challenge of a task refers to the degree to which a considerable amount of cognitive or physical efort is required to complete the task [9, 49]. For example, challenges are found to be beneficial to employees’ career success because individuals who face challenging experiences internalize high performance standards, which motivate them to develop better task-related attitudes and increase motivation to complete challenging tasks [9, 56].

Similar to goals, challenges represent standards that help stimulate individuals to expend more efort and increase engagement in corresponding tasks [9, 56]. Specifically, the amount of efort individuals intend to invest in performing a task is proportionally dependent on the task dificulty level up to the point where individuals no longer consider the task worthwhile [5, 9]. The more dificult individuals perceive a task, the more they become motivated, and the more efort they are willing to devote to accomplishing the task. The motivating efect of challenges on efort promotion is also found in the physiology literature [23]. As efort is positively correlated with performance quality [10, 13, 18, 54], we expect challenge-seeking to increase individuals’ contribution quality. The motivational efects of challenge-seeking are also found in the design of videogames [49], educational materials [48], and gamification tasks [39]. Furthermore, recall that the introduction of external incentives leads individuals to attribute their prosocial behavior to the external reason. Introducing challenges can serve as an internal reason for individuals to attribute their behavior. Consequently, we expect challenge-seeking to restore lost intrinsic motivation and attenuate incentives’ crowding-out efect. Accordingly, we formulate the following hypothesis:

Hypothesis 3 (HQ3): Challenge-seeking can mitigate the quality reduction efect induced by small incentives in a prosocial context.

## Experimental Design

We recruited participants from MTurk, an online labor market, for our experiment. MTurk allows “requesters” (employers) to post projects to be finished in a series of small tasks. “Workers” (employees) are then able to complete tasks they are interested in and receive payments. The crowdsourcing nature of MTurk has made it an ideal platform to outsource human-intelligence tasks (HITs), as MTurk workers are regularly involved in tasks such as natural language processing, image transcriptions, and audio transcriptions. MTurk also has the advantage of easy access to a large subject pool; this has attracted researchers across disciplines to conduct experiments on MTurk [44]. For example, Mason and Watts conducted behavioral experiments on MTurk to study the efects of pay rate on output quantity and quality [45]. Studies have also demonstrated that the behavior of MTurk subjects is comparable to the behavior of laboratory subjects [32, 50]. In addition, Deng et al. show that regard for others is an important aspect driving crowd workers to participate in MTurk tasks, which suggests that MTurk workers exhibit prosocial tendencies [17]. Thus, we believe that MTurk is an appropriate platform for our experiment, as our goal is to explore how diferent intervention strategies can help mitigate monetary incentives’ crowding-out efects on prosocial behavior.

We assigned MTurk workers to complete audio transcription tasks, as audio/image transcription is a common task; thus, participants would unlikely be aware of our experimental conditions. We told participants that the audio transcriptions will be used as educational materials to help facilitate learning for hearing-impaired students. Participants were instructed to transcribe a series of audio files. In addition, we used only audio files containing known words, which allowed us to evaluate participants’ transcription performance. We evaluated participant performance by checking their transcription error rates; transcriptions with a low error rate are considered high quality, while those with a high error rate are considered low quality. This quality metric is important as we aim to understand how individual behavior would change, both in terms of contribution quantity and quality, in response to monetary incentives, when the monetary incentive is accompanied by a goal-setting strategy or a challenge-seeking strategy.

Our experiment consisted of three sessions. The first session was identical to a regular MTurk assignment, where subjects were paid \$0.20 to transcribe a series of 10 audio files. At the end of the first session, a message was shown to request further transcription help. Subjects who agreed to help with additional transcriptions proceeded to transcribe five more audio files without receiving any payment. As no payment was given for these extra transcriptions, subjects who stayed to help can be considered altruistic, which helped us establish a prosocial context. After these altruistic subjects completed the five unpaid transcriptions, they entered the third session, where they were displayed a message according to a pre-assigned condition. This message described an “incentive” � “intervention strategy” combination based on the treatment condition to which the user was assigned. For example, one such combination is the “small incentive” � “goal-setting” condition. We denote our three sessions as the regular session, prosocial session, and experiment session.

Recall that, following the literature, we hypothesized in H1 that a small monetary incentive will cause a negative efect on the performance quality of prosocial behavior [24, 26, 55]. To test this hypothesis, we manipulated the scale of incentives in the experimental session. Specifically, the monetary incentive levels included None, Small, and Large, the amount of which correspond to 0 percent, 50 percent, and 100 percent of the payment given in the regular session, respectively;<sup>5</sup> strategies implemented to mitigate the adverse efect in the experimental session include None, Goal-Setting, and Challenge-Seeking. In other words, our experiment is a 3 x 3 design.

Using the MTurk interface, we recruited 1350 subjects to participate in our task (HIT). The subjects were randomly assigned to 9 diferent conditions—leading to 150 subjects per condition—as soon as they accepted the MTurk HIT and began participating in the regular session. Specifically, randomization of subjects to conditions is based on their arrival order to the experiment, consistent with the sequential stratification strategy proposed in the literature [11,32].<sup>6</sup> The advantages of the sequential stratification design include an equal number of assignments across groups and improved balance in terms of user demographics. In addition, because subjects do not know and cannot control their arrival order, this sequential assignment mechanism meets the unconfoundedness requirement for a valid experimental design. For example, in our research context, the first participant to arrive was assigned to the first condition, the second participant to arrive was assigned to the second condition, and the ninth participant was assigned to the ninth condition. The 10th participant would then be assigned to the first condition. Unknown to the participants, this assignment was initiated by their clicking on the “accept” button on our experiment page. In other words, a subject’s condition assignment was dependent only on order of arrival.

We tracked participants’ MTurk IDs to prevent the same user from participating in the experiment multiple times. Those who reported having technical problems and those who did not complete the regular session were removed from the analysis, yielding 1,299 valid responses. The descriptive statistics of our collected dataset, shown in Table 1, indicate that subjects across diferent conditions are comparable in terms of characteristics, including age, gender, and income.

Table 1. Descriptive statistics on all recruited subjects.

<table><tr><td colspan="2"></td><td colspan="6">Age</td><td colspan="4"> $Income\_Index^a$ </td></tr><tr><td>Incentive</td><td>Intervention Strategy</td><td>Obs.</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td><td>Ratio of Males (Percent)</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td></tr><tr><td>None</td><td>Default</td><td>145</td><td>34.33</td><td>18</td><td>67</td><td>12.04</td><td>39.31</td><td>5.49</td><td>2</td><td>10</td><td>2.65</td></tr><tr><td>None</td><td>Challenge</td><td>142</td><td>33.79</td><td>18</td><td>73</td><td>11.29</td><td>37.32</td><td>5.50</td><td>2</td><td>10</td><td>2.45</td></tr><tr><td>None</td><td>Goal</td><td>144</td><td>33.68</td><td>18</td><td>74</td><td>12.19</td><td>42.36</td><td>5.50</td><td>2</td><td>10</td><td>2.50</td></tr><tr><td>Small</td><td>Default</td><td>144</td><td>34.90</td><td>19</td><td>69</td><td>11.36</td><td>32.64</td><td>5.45</td><td>2</td><td>10</td><td>2.38</td></tr><tr><td>Small</td><td>Challenge</td><td>147</td><td>34.48</td><td>18</td><td>78</td><td>12.16</td><td>42.18</td><td>5.35</td><td>2</td><td>10</td><td>2.70</td></tr><tr><td>Small</td><td>Goal</td><td>144</td><td>34.48</td><td>18</td><td>77</td><td>12.67</td><td>36.81</td><td>5.55</td><td>2</td><td>10</td><td>2.50</td></tr><tr><td>Large</td><td>Default</td><td>145</td><td>35.46</td><td>18</td><td>69</td><td>11.63</td><td>38.62</td><td>5.67</td><td>2</td><td>10</td><td>2.69</td></tr><tr><td>Large</td><td>Challenge</td><td>146</td><td>33.54</td><td>18</td><td>74</td><td>11.67</td><td>36.30</td><td>5.59</td><td>2</td><td>10</td><td>2.52</td></tr><tr><td>Large</td><td>Goal</td><td>142</td><td>32.89</td><td>18</td><td>69</td><td>11.39</td><td>35.92</td><td>5.15</td><td>2</td><td>10</td><td>2.36</td></tr><tr><td>PayCut</td><td>Default</td><td>146</td><td>33.73</td><td>18</td><td>72</td><td>11.05</td><td>33.56</td><td>5.99</td><td>2</td><td>10</td><td>2.62</td></tr><tr><td>PayCut</td><td>Challenge</td><td>146</td><td>35.34</td><td>18</td><td>69</td><td>11.96</td><td>31.51</td><td>5.42</td><td>2</td><td>10</td><td>2.39</td></tr><tr><td>PayCut</td><td>Goal</td><td>145</td><td>33.90</td><td>18</td><td>76</td><td>11.17</td><td>26.90</td><td>5.42</td><td>2</td><td>10</td><td>2.71</td></tr></table>

<sup>a</sup>We coded “Income\_Index” as 1-10, corresponding to diferent categorical levels, which include “Less than \$12,500,” “\$12,500-\$24,999,” “\$25,000-\$37,499,” “\$37,500-\$49,999,” “\$50,000-\$62,499,” “\$62,500-\$74,999,” “\$75,000-\$87,499,” “\$87,500-\$99,999,” and “\$100,000 or more.”

Subjects who proceeded to the third session (i.e., experimental session) are the focus of our analysis, as the treatment manipulations occurred during this session. Note that subjects were allowed to leave at any point in the experiment (e.g., some subjects did not complete the regular session, others chose not to participate in the prosocial session, and still others began but did not finish the prosocial session). Therefore, there were significantly fewer subjects who remained in the experiment by proceeding to the experimental session. Descriptive statistics of the remaining subjects are shown in Table 2 and Table 3. To ensure the remaining subjects were still comparable across conditions, we conducted a randomization check on these subjects in terms of both their demographic and performance-related variables observed in the prosocial session. As shown in Table 4, statistical tests show no significant diferences in these observable variables across diferent treatment groups, suggesting that the remaining subjects were still comparable across conditions. As subjects followed the exact same procedure in both the regular and prosocial sessions and encountered diferent conditions only in the experimental session, their behavior diferences observed in the experimental session can be attributed to the diferent experimental conditions assigned to them.

Table 2. Descriptive statistics of focused subjects.<sup>a</sup>

<table><tr><td colspan="2"></td><td colspan="6">Age</td><td colspan="4">Income_Index</td></tr><tr><td>Incentive</td><td>Intervention Strategy</td><td>Obs.</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td><td>Ratio of Males (Percent)</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td></tr><tr><td>None</td><td>Default</td><td>31</td><td>36.03</td><td>18</td><td>67</td><td>11.73</td><td>32.26</td><td>5.90</td><td>2</td><td>10</td><td>2.84</td></tr><tr><td>None</td><td>Challenge</td><td>35</td><td>36.69</td><td>22</td><td>72</td><td>11.07</td><td>37.14</td><td>5.83</td><td>2</td><td>10</td><td>2.62</td></tr><tr><td>None</td><td>Goal</td><td>33</td><td>33.52</td><td>19</td><td>64</td><td>12.54</td><td>39.39</td><td>5.67</td><td>2</td><td>10</td><td>2.57</td></tr><tr><td>Small</td><td>Default</td><td>40</td><td>35.85</td><td>19</td><td>65</td><td>11.47</td><td>30.00</td><td>5.88</td><td>2</td><td>10</td><td>2.23</td></tr><tr><td>Small</td><td>Challenge</td><td>37</td><td>34.32</td><td>19</td><td>59</td><td>9.29</td><td>24.32</td><td>5.19</td><td>2</td><td>10</td><td>2.71</td></tr><tr><td>Small</td><td>Goal</td><td>38</td><td>36.55</td><td>18</td><td>72</td><td>14.20</td><td>21.05</td><td>5.21</td><td>2</td><td>10</td><td>2.71</td></tr><tr><td>Large</td><td>Default</td><td>46</td><td>36.26</td><td>18</td><td>58</td><td>11.83</td><td>41.30</td><td>6.04</td><td>2</td><td>10</td><td>2.96</td></tr><tr><td>Large</td><td>Challenge</td><td>38</td><td>32.42</td><td>18</td><td>57</td><td>11.35</td><td>39.47</td><td>5.84</td><td>2</td><td>10</td><td>2.41</td></tr><tr><td>Large</td><td>Goal</td><td>40</td><td>35.05</td><td>18</td><td>69</td><td>13.99</td><td>30.00</td><td>5.05</td><td>2</td><td>10</td><td>2.49</td></tr><tr><td>PayCut</td><td>Default</td><td>40</td><td>36.60</td><td>19</td><td>72</td><td>12.28</td><td>22.50</td><td>5.75</td><td>2</td><td>10</td><td>2.63</td></tr><tr><td>PayCut</td><td>Challenge</td><td>32</td><td>39.06</td><td>18</td><td>67</td><td>14.00</td><td>28.13</td><td>6.50</td><td>2</td><td>10</td><td>2.49</td></tr><tr><td>PayCut</td><td>Goal</td><td>37</td><td>35.46</td><td>21</td><td>60</td><td>9.08</td><td>24.32</td><td>5.16</td><td>2</td><td>10</td><td>2.84</td></tr></table>

<sup>a</sup>“Focused Subjects” refers to subjects who proceded to the experimental session. These subjects form the sample used in the empirical analyses.

aWe use the prosocial session as the baseline session for those focused subjects because subject behavior in this session was driven by altruism.  
Table 3. Descriptive statistics on baseline performance of focused subjects.a

<table><tr><td rowspan="2">Incentive</td><td rowspan="2">Intervention Strategy</td><td rowspan="2">Obs.</td><td colspan="4">Baseline CError</td><td colspan="4">Baseline WError</td><td colspan="4">Baseline Difficulty</td></tr><tr><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td><td>Mean</td><td>Min</td><td>Max</td><td>Std.</td></tr><tr><td>None</td><td>Default</td><td>31</td><td>0.0261</td><td>0</td><td>0.0996</td><td>0.0233</td><td>0.0593</td><td>0</td><td>0.1739</td><td>0.0431</td><td>1.4839</td><td>1</td><td>2.2</td><td>0.3532</td></tr><tr><td>None</td><td>Challenge</td><td>35</td><td>0.0240</td><td>0</td><td>0.0784</td><td>0.0251</td><td>0.0515</td><td>0</td><td>0.1429</td><td>0.0471</td><td>1.3714</td><td>1</td><td>2.4</td><td>0.4315</td></tr><tr><td>None</td><td>Goal</td><td>33</td><td>0.0299</td><td>0</td><td>0.1217</td><td>0.0309</td><td>0.0699</td><td>0</td><td>0.2195</td><td>0.0601</td><td>1.4303</td><td>1</td><td>2.2</td><td>0.3046</td></tr><tr><td>Small</td><td>Default</td><td>40</td><td>0.0346</td><td>0</td><td>0.1872</td><td>0.0344</td><td>0.0695</td><td>0</td><td>0.2500</td><td>0.0510</td><td>1.3700</td><td>1</td><td>2.2</td><td>0.3524</td></tr><tr><td>Small</td><td>Challenge</td><td>37</td><td>0.0258</td><td>0</td><td>0.0820</td><td>0.0210</td><td>0.0625</td><td>0</td><td>0.1628</td><td>0.0360</td><td>1.4486</td><td>1</td><td>2.2</td><td>0.2996</td></tr><tr><td>Small</td><td>Goal</td><td>38</td><td>0.0232</td><td>0</td><td>0.0818</td><td>0.0209</td><td>0.0550</td><td>0</td><td>0.1628</td><td>0.0428</td><td>1.3895</td><td>1</td><td>2</td><td>0.3220</td></tr><tr><td>Large</td><td>Default</td><td>46</td><td>0.0263</td><td>0</td><td>0.1033</td><td>0.0244</td><td>0.0613</td><td>0</td><td>0.1750</td><td>0.0488</td><td>1.4087</td><td>1</td><td>2.2</td><td>0.3450</td></tr><tr><td>Large</td><td>Challenge</td><td>38</td><td>0.0354</td><td>0</td><td>0.1899</td><td>0.0330</td><td>0.0697</td><td>0</td><td>0.2449</td><td>0.0482</td><td>1.4421</td><td>1</td><td>2.4</td><td>0.3753</td></tr><tr><td>Large</td><td>Goal</td><td>40</td><td>0.0295</td><td>0</td><td>0.1422</td><td>0.0319</td><td>0.0651</td><td>0</td><td>0.1842</td><td>0.0477</td><td>1.4400</td><td>1</td><td>2.2</td><td>0.3144</td></tr><tr><td>PayCut</td><td>Default</td><td>40</td><td>0.0268</td><td>0</td><td>0.1000</td><td>0.0277</td><td>0.0551</td><td>0</td><td>0.2000</td><td>0.0479</td><td>1.3350</td><td>1</td><td>2.2</td><td>0.3340</td></tr><tr><td>PayCut</td><td>Challenge</td><td>32</td><td>0.0332</td><td>0</td><td>0.1207</td><td>0.0316</td><td>0.0636</td><td>0</td><td>0.2558</td><td>0.0544</td><td>1.4062</td><td>1</td><td>2.4</td><td>0.3501</td></tr><tr><td>PayCut</td><td>Goal</td><td>37</td><td>0.0255</td><td>0</td><td>0.1111</td><td>0.0288</td><td>0.0563</td><td>0</td><td>0.1915</td><td>0.0496</td><td>1.4486</td><td>1</td><td>2.2</td><td>0.3899</td></tr></table>

Table 4. Randomization check on focused subjects.

<table><tr><td rowspan="2">Variables</td><td colspan="2">ANOVA</td><td colspan="2">Kruskal-Wallis Test</td></tr><tr><td>F-ratio</td><td>P-value</td><td>Chi2</td><td>P-value</td></tr><tr><td>Age</td><td>0.71</td><td>0.7276</td><td>9.589</td><td>0.5677</td></tr><tr><td>Ratio of Males</td><td>0.92</td><td>0.5248</td><td>12.872</td><td>0.3018</td></tr><tr><td>Income_Index</td><td>0.99</td><td>0.4555</td><td>10.676</td><td>0.4708</td></tr><tr><td>CError</td><td>0.81</td><td>0.6331</td><td>10.092</td><td>0.5221</td></tr><tr><td>WError</td><td>0.63</td><td>0.8072</td><td>8.712</td><td>0.6485</td></tr><tr><td>Perceived Difficulty</td><td>0.54</td><td>0.8769</td><td>4.215</td><td>0.9632</td></tr></table>

Notes: CError, WError, and Perceived Dificulty represent subject behavior in the prosocial session (i.e., the purely voluntary session), which can be used as the baseline before they enter the experimental session. All data are from subjects who remain in the experimental session; these subjects also form the sample used in the main regression analysis.

At the beginning of the experimental session, each participant was shown an instruction including: 1) a message to thank them for completing the unpaid transcriptions in the prosocial session; 2) a request to complete additional transcriptions to help audio digitization and promote education; and 3) a message indicating the incentive amount as well as applying a specific intervention strategy, if applicable. For example, if a participant was assigned to the goal-setting condition, the message “if you could achieve a 95 percent transcription accuracy, you will help these students to understand a complete story in each audio file” would be included in the instruction; for participants assigned to the challenge-seeking condition, the message “based on the feedback from other users, it is dificult to identify the content in the following set of audio fragments. Your answers can help us obtain better education materials and improve the education quality” would be displayed.<sup>7</sup> A sample instruction is shown in Figure A4 in the Online Supplemental Appendix. Each subject was asked to complete five audio transcriptions in the experimental session. We observed whether they participated, and, if they did participate, the number of transcriptions completed. Both the participation decision and the number of transcriptions completed reflect their contribution quantity. We also computed their transcription error rates, which reflect their contribution quality.

In all three sessions of the experiment, we made sure to randomize the order of audio files displayed to eliminate any ordering efect. Finally, we collected subjects’ gender, age, and annual income level to control for basic demographic information in the following empirical analyses.

## Altruism in MTurk Workers

Although MTurk is a payment-based environment, our experimental design allowed us to recruit workers willing to make voluntary contributions in a prosocial context. Specifically, the subjects of interest all completed the prosocial session without receiving any payments, suggesting these subjects were altruistic. Only these workers proceeded to the experimental session and experienced diferent treatments. This design ensures that our findings are based on a sample of altruistic individuals. Furthermore, our cover story stated that workers’ transcriptions would help digitize educational materials for hearing-impaired students, which strengthened the task’s prosocial context.

Screenshots of the cover story and instructions are shown in Figure A1. A sample transcription is shown in Figure A2. A diagram of the experimental flow is shown in Figure A5. Finally, we summarize experimental conditions in Online Supplemental Table A1.

## Experimental Results

This section presents our experimental results. As previously stated, we focus on the experimental session and measure subjects’ word-level transcription error rate, WError, and character-level transcription error rate, CError. WError is defined as the ratio of incorrect words to all words contained in each audio file, and CError is defined as the ratio of incorrect characters to all characters contained in each audio file. In the following sections, we analyze how subjects’ behavior changes in response to diferent monetary incentives and how diferent intervention strategies can help mitigate the adverse efect of monetary incentives.

## Adverse Efect of Monetary Incentives

We first examine the adverse efect of monetary incentives on individuals’ voluntary behavior. With the introduction of monetary incentives, individuals’ intrinsic motivation is crowded out by an extrinsic motivation regarding monetary incentives, thereby leading to reduced efort and lower-quality contributions. Based on hypothesis H1, we expect transcription error rates to increase for subjects receiving small monetary incentives. We construct generalized linear models to test this hypothesis. Specifically, we specify the linear component as follows:

$$
\nu = \beta_ {0} + \sum_ {j = 1, 2} \beta_ {1, j} I n c e n t i v e _ {j} + C o n t r o l s,\tag{1}
$$

where Incentive<sub>j</sub> is a series of dummy variables representing diferent reward sizes (small and large) with the baseline being a reward size of zero (i.e., no reward), and Controls include demographic variables, transcription dificulty, and subjects’ performance in the prosocial session. Given the linear component, we analyze WError and CError using generalized linear regressions with logit as the link function and binomial as the family function, as both variables are bounded between 0 and 1. In addition, we analyze two outcome variables that reflect contribution quantity. Specifically, Participation is a dummy variable indicating whether the subject agreed to participate in the experimental session and is analyzed through a probit model. A Poisson count model is used to analyze the Number of Transcriptions the subject completed in the experimental session.

As shown in columns (1) and (2) of Table 5, we found that both the word-level and character-level error rates were significantly higher for subjects receiving a small incentive. This observation is consistent with H1 that a small incentive can negatively afect voluntary behavior, leading to lower contribution quality. Meanwhile, we found no significant changes in contribution quality when the subjects received a large incentive. This is consistent with the W efect found in previous studies [24, 25, 26], which states that small rewards lead to the worst performance. Therefore, H1 is supported.

Table 5. Impacts of monetary incentives on prosocial contributions.

<table><tr><td>Variables</td><td>(1) $^b$ WError</td><td>(2) $^b$ CError</td><td>(3) $^b$ Participation</td><td>(4) $^b$ Number of Transcriptions</td></tr><tr><td>Small Incentive $^c$ </td><td>0.428***(0.134)</td><td>0.518***(0.167)</td><td>0.517**(0.232)</td><td>0.341**(0.167)</td></tr><tr><td>Large Incentive</td><td>0.0115(0.129)</td><td>0.0479(0.165)</td><td>0.607***(0.225)</td><td>0.408***(0.158)</td></tr><tr><td>Constant</td><td>-3.786***(0.367)</td><td>-4.363***(0.400)</td><td>0.287(0.579)</td><td>1.133***(0.370)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>117</td><td>117</td><td>205</td><td>205</td></tr><tr><td>Pseudo R-squared</td><td></td><td></td><td>0.0903</td><td>0.0500</td></tr><tr><td>AIC</td><td>0.585</td><td>0.428</td><td></td><td></td></tr><tr><td colspan="5">Notes: Robust standard errors are in parentheses. *** p&lt;0.01; ** p&lt;0.05; * p&lt;0.1.</td></tr></table>

<sup>a</sup>We controlled for demographic variables, transcription dificulty, and subject transcription errors in the baseline (prosocial) session. <sup>b</sup>Generalized linear regression is used for WError and CError with logit as the link function and binomial as the family function. Probit estimation is used for Participation, and Poisson estimation is used for the count variable Number of Transcriptions. The same specifications are adopted in other estimations unless noted otherwise. <sup>c</sup>The coeficients on “Small Incentive” in columns (1) and (2) indicate that monetary incentives can generate quality crowding-out on voluntary contributions, supporting H1.

In addition, monetary incentives are known to have potential in improving contribution quantity. As shown in Table 5, column (3), we found that both small and large incentives led to more participation. In addition, column (4) in Table 5 shows that both small and large incentives led subjects to complete more transcriptions. These findings are consistent with the positive price efect of monetary incentives on contribution quantity, as shown in previous studies [6, 25, 38].

In all regressions, we controlled for user demographic variables and baseline error rates (i.e., subjects’ error rates in the prosocial session) to account for potential heterogeneity in subject ability levels. We also controlled for the dificulty of each transcription as some audio files appeared to be more dificult than others.<sup>8</sup> In summary, we found that incentives lead to higher contribution quantity, but a small incentive leads to lower contribution quality. These results demonstrate the need to design efective strategies to help mitigate any decrease in quality while sustaining increased quantity.

## Mitigating the Adverse Efect of Monetary Incentives

As discussed above, we observed that monetary incentives increased contribution quantity but decreased contribution quality, which is undesirable. In this section, we investigate whether the proposed intervention strategies, goal-setting and challenge-seeking, can help mitigate the negative efects of incentives while preserving quantity-inducing efects. We specify the linear component as follows:

$$
\begin{array}{l} v = \beta_ {0} + \sum_ {j = 1, 2} \beta_ {1, j} \text { Intervention } _ {j} + \sum_ {j = 1, 2} \beta_ {2, j} \text { Incentive } _ {j} + \sum_ {i = 1, 2} \sum_ {j = 1, 2} \beta_ {3 i j} \text { Intervention } _ {i} * \text { Incentive } _ {j} \\ + \text { controls } \end{array}\tag{2}
$$

where Incentive<sub>j</sub> is defined similarly as previously described, and Intervention<sub>i</sub> represents either goal-setting or challenge-seeking. The coeficients of interest are the interaction terms between Intervention<sub>i</sub> and Incentive<sub>j</sub>, which allow us to study intervention strategy mitigation efects. Definitions of the controls used in the regression models are as in Equation (1). Given the linear component, we again analyze WError and CError using generalized linear regressions with logit as the link function and binomial as the family function, Participation through a probit model, and Number of Transcriptions through a Poisson count model.

We first analyze the efectiveness of goal-setting in mitigating incentives’ adverse efect. As shown in Table 6, the coeficient of Goal \* Small Incentive is significantly negative in both the word-level and character-level analyses, suggesting that the combined usage of small monetary incentives and goal-setting can mitigate the adverse efect of small incentives on contribution quality. In contrast, participants receiving small incentives but not presented with the goal-setting treatment showed higher error rates. This suggests that goal-setting is an efective strategy in overcoming the adverse efect induced by small incentives. This also suggests that goal-setting has the ability to increase participants’ intrinsic motivation to

Table 6. Mitigation efects of goal-setting and challenge-seeking.

<table><tr><td>VARIABLES</td><td>(1) WError</td><td>(2) CError</td><td>(3) $^b$ Participation</td><td>(4) $^b$ Number of Transcriptions</td></tr><tr><td>Challenge</td><td>-0.111(0.149)</td><td>-0.0253(0.175)</td><td>0.216(0.218)</td><td>0.170(0.174)</td></tr><tr><td>Goal</td><td>-0.0274(0.181)</td><td>-0.00533(0.214)</td><td>0.186(0.222)</td><td>0.135(0.182)</td></tr><tr><td>Small Incentive $^c$ </td><td>0.487***(0.140)</td><td>0.537***(0.171)</td><td>0.458**(0.225)</td><td>0.318*(0.167)</td></tr><tr><td>Large Incentive</td><td>-0.0225(0.133)</td><td>0.0678(0.166)</td><td>0.560**(0.219)</td><td>0.389**(0.158)</td></tr><tr><td>Challenge_Small $^d$ </td><td>-0.552***(0.213)</td><td>-0.590**(0.277)</td><td>-0.353(0.315)</td><td>-0.238(0.229)</td></tr><tr><td>Challenge_Large</td><td>-0.0243(0.191)</td><td>-0.238(0.240)</td><td>-0.469(0.310)</td><td>-0.321(0.221)</td></tr><tr><td>Goal_Small $^e$ </td><td>-0.557**(0.257)</td><td>-0.636**(0.301)</td><td>-0.373(0.317)</td><td>-0.235(0.234)</td></tr><tr><td>Goal_Large</td><td>-0.0360(0.221)</td><td>-0.0895(0.278)</td><td>-0.270(0.315)</td><td>-0.174(0.221)</td></tr><tr><td>Constant</td><td>-3.881***(0.265)</td><td>-4.947***(0.320)</td><td>0.507(0.331)</td><td>1.300***(0.236)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>338</td><td>338</td><td>607</td><td>607</td></tr><tr><td>AIC</td><td>0.420</td><td>0.275</td><td></td><td></td></tr><tr><td>Pseudo R-squared</td><td></td><td></td><td>0.0517</td><td>0.0314</td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. $\mathsf { \# \varkappa \varkappa ^ { \ast } p } < 0 . 0 1 ; \mathsf { \# \varkappa \mathtt { p } < 0 . 0 5 ; \mathsf { \# } \mathsf { p } < 0 . 1 . \mathsf { \Psi } ^ { \flat } F r o m }$ columns (3) and (4), it is evident that the efect of incentives on quantity is positive, and that the mitigation strategies do not moderate the efect. <sup>c</sup>The coeficients on “Small Incentive” in columns (1) and (2) show the quality harm of monetary incentives on prosocial contributions, i.e., H1. <sup>d</sup>The coeficients on “Challenge\_Small” in columns (1) and (2) demonstrate the mitigation efectiveness of challenge-seeking on monetary incentives’ crowding-out efect, supporting H3. <sup>e</sup>The coeficients on “Goal\_Small” in columns (1) and (2) demonstrate the mitigation efectiveness of goal-setting on monetary incentives crowding-out efects, supporting H2.

engage in voluntary activities when incentives are small. Therefore, H2 is supported. We also found that the goal-setting strategy did not seem to change the monetary incentives quantity-inducing efect, as the interaction terms in the regressions of Participation, Table 6 column (3), and Number of Transcriptions, Table 6 column (4), are insignificant. This suggests that the overall efect of monetary incentives on contribution quantity is positive. These findings suggest that the goal-setting strategy not only mitigates the adverse efect on quality but also preserves the positive price efect on quantity.

Similar to the analysis of the goal-setting strategy, we found significant mitigation efects from the challenge-seeking strategy on the adverse efect of small incentives in both the word- and character-level analyses, as shown in Table 6. Note that we accounted for subjectlevel ability heterogeneity by controlling for subject transcription accuracy in the prosocial session. Therefore, H3 is supported. Our findings suggest that intervention strategies can be used in conjunction with small incentives to induce higher contribution quantity while sustaining quality. This suggests that the monetary reward used to induce contribution need not be large if appropriate intervention strategies are implemented.

Interaction of Small Incentive x Challenge Seeking on Word-Level Error Rate (GLM with Logit Link)  
![](/api/attachments/8NXA5XV5/fulltext/images/a1147db4f1ac464e87081be0a6cb0da63538dda06e7cbb4744f140d6c95665d7.jpg)

![](/api/attachments/8NXA5XV5/fulltext/images/c9320cb983bfaa38130eae74041d542abf7346de509cc312674e1e38af193440.jpg)

Interaction of Small Incentive x Goal-Setting on Word-Level Error Rate (GLM with Logit Link)  
![](/api/attachments/8NXA5XV5/fulltext/images/c05f2c68581e227d53369e6de0d8000d0946ac559adb816d465d8d5fdffd560d.jpg)

![](/api/attachments/8NXA5XV5/fulltext/images/688f0a7912c1f01bb165dfa673c9c424440a6cae00cab6ddbaaf56b86e1be3d5.jpg)  
Figure 1. Marginal efect analysis of small incentive � intervention strategy on word-level transcription error rate. The two graphs on the left plot the marginal efect of the interaction term for each subject on the subject’s predicted word-level transcription error rate. The two graphs on the right plot the z-statistics of the interaction term for each subject. The three horizontal lines in these graphs represent $z = 1 . 9 6 , 0 ,$ , and -1.96, respectively. Therefore, points above the z = 1.96 line or below the z = -1.96 line are significant at the 5 percent level. It is evident that the interaction efect is significantly negative for all subjects in the challenge-seeking condition, as well as for most subjects in the goal-setting condition.

Interaction of Small Incentive x Challenge Seeking on Character-Level Error Rate (GLM with Logit Link)  
![](/api/attachments/8NXA5XV5/fulltext/images/0eefacec27d1c02149c25df6a350f0b028d9dd4772e87d4688c7adbc5e8ada7b.jpg)

![](/api/attachments/8NXA5XV5/fulltext/images/3ff7cab9d994dc6b7caeb859c63ff7ddcce2823657e4648fa9d0cfa5aecdc556.jpg)

Interaction of Small Incentive x Goal-Setting on Character-Level Error Rate (GLM with Logit Link)  
![](/api/attachments/8NXA5XV5/fulltext/images/b85cf9e8253feb77e1c1e6a145ae6f1c0917552c4e28f49cfa0ad7d9b3729c1f.jpg)

![](/api/attachments/8NXA5XV5/fulltext/images/b673b02b5fe602eb2b8d00576dabb9458fb5b6437649ddd435507621abe66b90.jpg)  
Figure 2. Marginal efect analysis of small incentive � intervention strategy on character-level transcription error rate. The two graphs on the left plot the marginal efect of the interaction term for each subject on the subject’s predicted character-level transcription error rate. The two graphs on the right plot the z-statistics of the interaction term for each subject. The three horizontal lines in these graphs represent $z = 1 . 9 6 , 0 ,$ and -1.96, respectively. Therefore, points above the z = 1.96 line or below the z = -1.96 line are significant at the 5 percent level. It is evident that the interaction efect is significantly negative for most subjects in both the challenge-seeking and goal-setting conditions.

Following recommendations from the literature on interpreting interaction terms in nonlinear models [1], we plotted the marginal efects of the interaction terms as a function of the predicted outcome variable. The results, shown in Figure 1 and Figure 2, show that the marginal efect of the interaction terms is significantly negative for the vast majority of subjects, suggesting that a small incentive combined with a proposed intervention strategy can consistently mitigate the adverse efect of small incentives on contribution quality.

## Divergent Results on Quality- vs. Quantity-based Outcomes

Note that the intervention strategies did not further increase contribution quantity. We believe these divergent results were driven by fundamental diferences between measures of quantity and quality.

In the experiment, we used two outcome variables to measure quantity: (1) whether a subject agreed to participate, reflecting the quantity of participants, and (2) how many transcriptions a subject completed, reflecting the quantity of a subject’s contribution. Our results, shown in Table 5, show that both measures of quantity responded positively to incentives, and larger incentives lead to higher contribution quantity. This suggests that the standard price efect of incentives is significant in improving contribution quantity.

In addition, we used both word- and character-level transcription error rates to measure quality. Our results show consistent findings: individuals receiving a small incentive produced lower-quality contributions compared to those who received no incentives. Frey and Oberholzer-Gee argue that in situations where the intrinsic motivation has been crowded out, use of monetary incentives conveys a standard price efect [21]; Gneezy described this non-monotonic relationship between contribution performance and payment as the W efect [24]. Our results support this line of argument: ofering only small incentives leads to quality decrease; large incentives are able to ofset the loss of intrinsic motivation with a price efect to sustain quality.

The arguments previously outlined suggest that quantity measures are best predicted through incentives, and that quality measures are best predicted through intrinsic motivation. We examine the decrease in intrinsic motivation due to incentives, and we propose intervention strategies to mitigate such decreases while still providing the same level of incentives. Recall that our intervention strategies work via increasing individuals intrinsic motivation. As quality measures are best predicted by intrinsic motivation, we expect the use of intervention strategies to improve quality to function via increasing intrinsic motivation. This is verified in our main (three-session) experiment and in twosession experiments reported in the robustness check section. That is, intervention strategies help ofset small incentives’ adverse efect on quality, as measured in lowered transcription error rates. Note that the only diference between the [small incentive � no strategy] and [small incentive � intervention strategy] conditions is the presence of a strategy, while the incentive is fixed at a small level. In contrast, since quantity is best predicted by incentives and the incentives are the same across these conditions, we do not expect an intervention strategy to lead to observable diferences in quantity. This explains why participation and number of transcriptions completed, both quantity-based outcomes, were not significantly diferent with or without the use of intervention strategies.

## Robustness Checks

## Perceived Transcription Dificulty vs. Experimental Conditions

In the process of using challenge-seeking to mitigate the adverse efects of small incentives, we exploited the human tendency to overcome dificulty. This ofers an alternative intrinsic motivation for individuals to rationalize their conduct while discounting the salience of monetary incentives. To achieve this, we framed the tasks as being challenging and argue that such explicit statements can stimulate individuals’ inner desire to overcome challenges. The mechanism underlying this process is explained by the framing theory [35], which suggests that a particular statement can convey relevant information that influences individual behavior. Applied to the current research context, the emphasis on challenge in transcription tasks could influence individuals to behave in certain ways, that is, increasing intrinsic motivation and exerting greater efort to cope with challenges. Meanwhile, it is possible that individuals assigned to the challenge-seeking condition perceived the transcription tasks to be easier (therefore making fewer errors), which could confound our analysis. To rule out this alternative explanation, we asked subjects to rate the dificulty level of each audio transcription (1 = easy, 2 = neutral, 3 = dificult). We then regressed subjects assessment of transcription dificulty on the experimental conditions (i.e., the intervention strategy dummies). As shown in Table 7, there is no significant relationship between subject assessment of transcription dificulty and the specific treatments they were assigned to, which means the results we observed are not attributable to easier tasks being used in the challenging-seeking condition.

## Subject Performance in the Baseline (Prosocial) Session

In our three-session experimental design, subjects volunteered to complete transcriptions with no payment during the prosocial session. The purpose of this design was to ensure that subjects functioned in a prosocial environment as they proceeded to the experimental session. Since subjects across all conditions went through the identical regular session and prosocial session, we expect all subjects to show similar behavior during these sessions. As we are particularly interested in these subjects’ prosocial behavior, we analyzed the focal subjects’ transcription error rates in the prosocial session, shown in Table 8. We found that transcription error rates did not vary

Table 7. Perceived dificulty vs. experimental conditions.<sup>a</sup>

<table><tr><td>VARIABLES</td><td>(1)  $Difficulty^b$ </td></tr><tr><td>Challenge</td><td>0.0397(0.0990)</td></tr><tr><td>Goal</td><td>-0.0945(0.0930)</td></tr><tr><td>Small Incentive</td><td>0.0600(0.0929)</td></tr><tr><td>Large Incentive</td><td>-0.121(0.0827)</td></tr><tr><td>Challenge_Small</td><td>-0.0956(0.130)</td></tr><tr><td>Challenge_Large</td><td>0.135(0.125)</td></tr><tr><td>Goal_Small</td><td>0.0323(0.128)</td></tr><tr><td>Goal_Large</td><td>0.0605(0.115)</td></tr><tr><td>Constant</td><td>1.618***(0.105)</td></tr><tr><td>Controls for Demographics</td><td>Yes</td></tr><tr><td>Observations</td><td>338</td></tr><tr><td>R-squared</td><td>0.062</td></tr><tr><td>Pseudo R-squared</td><td>0.00913</td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. \*\*\*p < 0.01. \*\*p < 0.05. \*p < 0.1 <sup>b</sup>The insignificance of coeficients across experimental condi tions suggests that transcription dificulty does not appear to confound the observed crowdingout and mitigation efects.

Table 8. Estimations on subject behavior in the prosocial session.<sup>a</sup>

<table><tr><td>VARIABLES</td><td>(1) $^b$ WError</td><td>(2) $^b$ CError</td></tr><tr><td>Challenge</td><td>-0.0480(0.125)</td><td>-0.0414(0.144)</td></tr><tr><td>Goal</td><td>0.126(0.136)</td><td>0.0814(0.158)</td></tr><tr><td>Small Incentive</td><td>0.201(0.141)</td><td>0.258(0.175)</td></tr><tr><td>Large Incentive</td><td>0.0535(0.120)</td><td>0.00723(0.140)</td></tr><tr><td>Challenge_Small</td><td>0.0685(0.116)</td><td>0.00550(0.156)</td></tr><tr><td>Challenge_Large</td><td>0.0596(0.120)</td><td>0.111(0.146)</td></tr><tr><td>Goal_Small</td><td>-0.0271(0.124)</td><td>-0.0730(0.144)</td></tr><tr><td>Goal_Large</td><td>0.0994(0.130)</td><td>0.0630(0.158)</td></tr><tr><td>Constant</td><td>-3.411***(0.227)</td><td>-4.256***(0.247)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>338</td><td>338</td></tr><tr><td>AIC</td><td>0.477</td><td>0.324</td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. $^ { \ast \ast \ast } \mathsf { p } < 0 . 0 1 . ^ { \ast \ast } \mathsf { p } <$ $0 . 0 5 . { } ^ { * } { \mathsf { p } } < 0 . 1$ . <sup>b</sup>The insignificance of coeficients across experimental conditions suggests that there is no diference in subject performance in the unpaid, prosocial session.

significantly across groups, suggesting that subjects assigned to diferent treatment conditions were comparable.

## Small Incentive vs. Pay Cut

Recall that the incentive amount we used in the small incentive condition was an amount equal to 50 percent of the regular session payment. One concern is that the observed negative efects of small incentives might have been caused by subjects’ perceiving the small incentive as a pay cut. While a pay cut should also decrease individual performance, it is fundamentally diferent from our hypothesized mechanism, which states that the introduction of incentives in an initially unincentivized environment can cause quality deterioration. To further distinguish a small incentive’s efect from that of a pay cut, we designed and implemented three additional conditions in our experiment. Specifically, in the message shown to the subjects assigned to the pay cut conditions, we explicitly stated that “for the remaining additional transcriptions, we will provide payment for your work but have to cut the reward amount in half (\$0.01 per audio clip transcribed) due to budget constraint.” Note that \$0.01 per transcription is the same amount given in the small incentive conditions. We combined this pay cut message with the goal-setting strategy, the challenge-seeking strategy, or no intervention strategy. We then compared the pay cut conditions with the small incentive conditions and no-incentive conditions.<sup>9</sup> The results, shown in Table 9, column 2, suggest that a pay cut led to a further quality decrease compared with the small incentive and baseline conditions, measured in character-level transcription errors. These results suggest that individuals would have performed even worse had they perceived the small incentive as a pay cut. In contrast, in the small incentive conditions, we merely stated the dollar amount of payment and avoided comparing the payment with that received in the regular session. In addition, the provision of small incentives occurred after the prosocial session, which further distanced the subjects from recalling the regular session payment. Therefore, we believe that while a pay cut leads to a quality decrease, a small incentive by itself can also lead to a quality decrease. Note that the additional quality decrease due to a pay cut is more salient in the character-level error rate and less clear in the word-level error rate. Therefore, while our analyses provide preliminary evidence that the small incentive’s efect is not driven solely by its perception as a pay cut, more research is needed to clarify the efect of pay cuts vs. small incentives. Also note that there is some evidence that our intervention strategies may mitigate the negative efect of a pay cut, but the result is inconclusive due to lack of consistent statistical significance.

Table 9. Small incentives vs. pay cut.<sup>a</sup>

<table><tr><td>VARIABLES</td><td>(1)WError</td><td>(2)CError</td></tr><tr><td>Challenge</td><td>-0.0911(0.147)</td><td>-0.00824(0.175)</td></tr><tr><td>Goal</td><td>-0.0363(0.183)</td><td>-0.0140(0.222)</td></tr><tr><td> $Small\ Incentive^b$ </td><td>0.464***(0.145)</td><td>0.481***(0.185)</td></tr><tr><td> $Pay\ Cut^b$ </td><td>0.500***(0.148)</td><td>0.719***(0.186)</td></tr><tr><td>Challenge_Small</td><td>-0.581***(0.216)</td><td>-0.582**(0.285)</td></tr><tr><td>Challenge_Cut</td><td>-0.383*(0.210)</td><td>-0.531**(0.252)</td></tr><tr><td>Goal_Small</td><td>-0.536**(0.263)</td><td>-0.576*(0.316)</td></tr><tr><td>Goal_Cut</td><td>-0.527**(0.263)</td><td>-0.469(0.313)</td></tr><tr><td>Constant</td><td>-3.891***(0.279)</td><td>-4.884***(0.320)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>323</td><td>323</td></tr><tr><td>AIC</td><td>0.449</td><td>0.303</td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. $^ { * * * } \mathfrak { p } < 0 . 0 1 . ^ { * * } \mathfrak { p } <$ $0 . 0 5 . { } ^ { * } { \mathsf { p } } < 0 . 1$ . <sup>b</sup>There appears to be a magnitude diference between the coeficients of “Small Incentive” and “Pay Cut” in column (2). This suggests that the efects of pay cut and small incentives are likely diferent. However, the small magnitude diference in column (1) as well as in the mitigation strategies suggest further research is needed to distinguish between the efects of small incentives and pay cuts.

## Two-Session Experiments

Our main analyses presented above demonstrate the efectiveness of the goal-setting and challenge-seeking strategies in mitigating the adverse efect of small incentives on contribution quality. Note that the experiment presented in our main analyses consists of three sessions, where we included an unpaid, prosocial session in the middle to ensure that subjects who proceeded to the experimental session had altruistic motivation. In this section, we present results from additional experiments that implement a two-session approach similar to those used in the literature [33] to demonstrate the robustness of our results. The two-session design consists of only a regular session followed by an experimental session, and therefore the prosocial context is emphasized only through the cover story. Specifically, in the regular session, subjects were asked to complete a regular MTurk task where they each transcribed 10 audio files and received payments. After subjects completed the regular session, we requested their help with five more audio files in the experimental session. In the experimental session, each subject was shown a message corresponding to one of nine randomly assigned conditions similar to those used in the experimental session of the three-session design, [no incentive, small incentive, large incentive] � [no strategy, goal-setting, challenge-seeking].<sup>10</sup> We initially recruited 100 users for each of the nine groups and received 890 efective responses after removing incomplete responses. Out of these 890 individuals, 559 subjects agreed to enter the experimental session. We used these 559 subjects’ responses and repeated our earlier analyses. As shown in Table 10, we observed qualitatively similar results, suggesting our findings are robust.

To ensure our results generalize to contexts other than audio transcription tasks, we conducted another two-session experiment, replacing audio transcription with a series of image transcription tasks. A sample image transcription task is shown in Figure A3. We created a cover story for the image transcription task by stating that each image contains a manuscript fragment from a famous writer, and that digitizing these manuscripts is important for educational purposes. Similar to the audio transcription experiments, subjects who proceeded to the experimental session each saw a message corresponding to one of the nine experimental conditions. We recruited 50 subjects for each condition and received 442 valid responses. As shown in Table 11, the results from the image transcription experiments are qualitatively similar to the audio transcription experiments and show that the proposed intervention strategies can help mitigate the adverse efect of small incentives. Therefore, we believe that our findings are generalizable to diferent prosocial contexts.

Table 10. Robustness checks on mitigation efects in two-session audio transcription experiment.<sup>a</sup>

<table><tr><td>VARIABLES</td><td>(1) WError</td><td>(2) CError</td><td>(3) Participation</td><td>(4) Transcription Number</td></tr><tr><td>Challenge</td><td>0.0147(0.147)</td><td>0.0171(0.135)</td><td>0.457(0.316)</td><td>0.340(0.215)</td></tr><tr><td>Goal</td><td>0.0651(0.170)</td><td>0.0520(0.156)</td><td>-0.00188(0.328)</td><td>0.0265(0.235)</td></tr><tr><td>Small Incentive</td><td>0.269**(0.121)</td><td>0.262**(0.125)</td><td>2.124***(0.327)</td><td>1.070***(0.179)</td></tr><tr><td>Large Incentive</td><td>0.149(0.114)</td><td>0.0312(0.118)</td><td>2.026***(0.331)</td><td>1.059***(0.181)</td></tr><tr><td>Challenge_Small</td><td>-0.367**(0.179)</td><td>-0.334**(0.160)</td><td>-0.00123(0.469)</td><td>-0.228(0.227)</td></tr><tr><td>Challenge_Large</td><td>-0.173(0.174)</td><td>0.0126(0.155)</td><td>-0.167(0.470)</td><td>-0.301(0.232)</td></tr><tr><td>Goal_Small</td><td>-0.347*(0.198)</td><td>-0.385**(0.182)</td><td>0.444(0.483)</td><td>0.0588(0.246)</td></tr><tr><td>Goal_Large</td><td>-0.187(0.193)</td><td>-0.104(0.176)</td><td>0.625(0.493)</td><td>0.0548(0.249)</td></tr><tr><td>Constant</td><td>-3.395***(0.197)</td><td>-3.741***(0.173)</td><td>-0.360(0.705)</td><td>0.391(0.265)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>559</td><td>559</td><td>890</td><td>890</td></tr><tr><td>Pseudo R-squared</td><td></td><td></td><td>0.199</td><td>0.109</td></tr><tr><td>AIC</td><td>0.481</td><td>0.387</td><td></td><td></td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. \*\*\*p < 0.01. \*\*p < 0.05. \*p < 0.1. The results shown in this table are consistent with those found in the main experiment (shown in Table 6).

Table 11. Robustness checks on mitigation efects in two-session image transcription experiment.<sup>a</sup>

<table><tr><td>VARIABLES</td><td>(1)WError</td><td>(2)CError</td><td>(3)Participation</td><td>(4)Transcription Number</td></tr><tr><td>Challenge</td><td>-0.0785(0.169)</td><td>-0.122(0.172)</td><td>0.466*(0.259)</td><td>0.442*(0.243)</td></tr><tr><td>Goal</td><td>-0.0495(0.207)</td><td>-0.166(0.193)</td><td>0.114(0.260)</td><td>0.0583(0.274)</td></tr><tr><td>Small Incentive</td><td>0.354**(0.143)</td><td>0.359**(0.163)</td><td>1.272***(0.281)</td><td>0.868***(0.216)</td></tr><tr><td>Large Incentive</td><td>0.145(0.149)</td><td>0.128(0.154)</td><td>1.790***(0.316)</td><td>1.045***(0.208)</td></tr><tr><td>Challenge_Small</td><td>-0.389*(0.201)</td><td>-0.409*(0.214)</td><td>-0.444(0.395)</td><td>-0.417(0.269)</td></tr><tr><td>Challenge_Large</td><td>-0.0925(0.200)</td><td>0.0619(0.195)</td><td>-0.620(0.431)</td><td>-0.455*(0.257)</td></tr><tr><td>Goal_Small</td><td>-0.438*(0.236)</td><td>-0.438*(0.228)</td><td>0.0222(0.406)</td><td>0.0473(0.295)</td></tr><tr><td>Goal_Large</td><td>-0.0964(0.244)</td><td>0.0326(0.225)</td><td>-0.417(0.423)</td><td>-0.161(0.289)</td></tr><tr><td>Constant</td><td>-3.200***(0.272)</td><td>-5.334***(0.280)</td><td>-0.825(0.547)</td><td>0.858***(0.284)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>308</td><td>308</td><td>442</td><td>442</td></tr><tr><td>Pseudo R-squared</td><td></td><td></td><td>0.198</td><td>0.109</td></tr><tr><td>AIC</td><td>0.446</td><td>0.241</td><td></td><td></td></tr></table>

Notes: <sup>a</sup>Robust standard errors are in parentheses. ${ \texttt { \tiny k K } } _ { \texttt { p } < 0 . 0 1 . } { \stackrel { \ast \ast } { } } { \mathfrak { p } } < 0 . 0 5$ $^ { \ast } \mathsf { p } < 0 . 1$ . The results shown in this table are consistent with those found in the main experiment (shown in Table 6).

## Discussion and Conclusion

Monetary incentives are often used to encourage voluntary activities. However, small incentives can result in an adverse efect on contribution quality. Through a series of randomized experiments conducted on MTurk in which we recruited subjects to complete audio and image transcription tasks, this study shows that small incentives, when combined with an appropriate intervention strategy (i.e., goal-setting or challenge-seeking) can induce individuals to increase their contribution quantity without sacrificing quality.

This study contributes to the literature on incentive efects and voluntary contributions. Although prior studies examine the adverse efect of monetary incentives on prosocial/ voluntary behavior, a minimal amount is known regarding how to mitigate the negative efect of incentives on quality. We ofer two intervention strategies to mitigate this negative efect. Our findings have important practical implications because they suggest that combining small incentives with intervention strategies can be a cost-efective way for platforms relying on user contributions to increase contribution quantity without sacrificing quality.

Specifically, we identify strategies that allow voluntary activity organizers to use monetary rewards to motivate more high-quality contributions. This is important, as many information systems rely primarily on altruistic user voluntary contributions to operate. In fact, our results suggest that voluntary activity organizers do not necessarily need to provide large monetary rewards; instead, a small monetary incentive combined with a goal-setting or a challenge-seeking strategy can be as efective. We believe these findings will also be helpful for policy design for NPOs, such as those striving to promote biodiversity and ecosystem service conservation through providing economic incentives [53]. Moreover, the Internet is becoming a popular channel for NPOs, such as Citizen Science Alliance, to recruit volunteers. Our research may also help the design and development of platforms such as Zooniverse, where scientists and educators rely on volunteer participation to advance scientific studies.

We believe our research also contributes to the literature by proposing the three-session experimental design to study prosocial activities on MTurk or similar platforms that typically rely on payments to operate. Specifically, by introducing an unpaid session between the regular paid session and the experimental session, our design enables researchers to construct a prosocial environment on any for-fee platform, thus increasing experimental validity.

Our study opens up important avenues for future research in the area of online voluntary behavior and provides practical guidelines for better design of voluntary platforms. That said, the current study has several limitations. First, in our analyses, the experiments were conducted on MTurk, whereas voluntary activities might be captured more realistically in a field setting. Thus, collaboration with online voluntary platforms can further verify the efectiveness of our intervention strategies. Second, individuals’ voluntary contributions are often a dynamic process, as individuals tend to contribute more than once. Further studies are required to understand whether the proposed intervention strategies can promote voluntary contribution in the long run. Third, the types and levels at which goals and challenges are set could vary, and further studies are needed to understand whether diferent forms/levels of goals or challenges can provide diferent mitigation efects. Fourth, our comparison between small incentives and pay cuts is inconclusive, and further research on this issue is necessary. Finally, the adverse efect of monetary incentives and subsequent intervention strategy efectiveness might difer across users based on their heterogeneous altruism levels. Additional studies are needed to understand whether individuals’ level of altruism moderates the efects identified in this study.

## Notes

1 https://meta.wikimedia.org/wiki/List\_of\_Wikipedias#Grand\_Tota

2 https://www.zooniverse.org/

3 https://www.zooniverse.org/talk/15/689351

4 We ask MTurk workers to help transcribe either audio files or images in a series of experiments. Such transcription tasks are common on MTurk.

5 Since we initially specified the price of our task as \$0.20, the payments in the experimental session were separately delivered to participants’ accounts through MTurk’s bonus functionality.

6 This stratification strategy has been used in social science experiments using MTurk [11] and is mathematically demonstrated to be efective in achieving balance across experimental groups. See http://john-joseph-horton.com/allocating-online-experimental-subjects-to-cells-doing-bet ter-than-random/

7 We used JavaScript programming to implement the display of messages and audio files in diferent experimental conditions.

8 Based on our experimental design, each transcription was randomly assigned to a group of subjects. We asked each subject to rate the dificulty level of a given transcription. We then computed the average dificulty level for each transcription and included it as a control in the analyses.

9 We included samples from nine groups including, None\_Default, None\_Challenge, None\_Goal, Small\_Default, Small\_Challenge, Small\_Goal, PayCut\_Default, PayCut\_Challenge, PayCut\_Goal and repeat the same estimations as in Equation (2).

10 In the two-session experiments, subjects assigned to the goal-setting conditions saw the message “we are now just 10% away from completing all our transcriptions.” Such a goal can be classified as a collective goal, while in the main experiments the goal is an individual goal.

## Acknowledgements

The authors would like to express gratitude to Dr. Vladimir Zwass and three anonymous reviewers for their helpful comments and suggestions. The authors also thank for participants at the 2018 International Conference on Information Systems for their valuable comments.

## Funding

This study was supported by the National University of Singapore Academic Research Fund (AcRF) Tier 1 Start-up Research Grant [R-253-000-145-133] and National Natural Science Foundation of China (grant number 71772101).

## ORCID

Qiang Wei http://orcid.org/0000-0002-8397-7129

## References

1. Ai, C.; and Norton, E.C. Interaction terms in logit and probit models. Economics Letters, 80, 1 (2003), 123–129.

2. Alam, S.L.; and Campbell, J. Temporal motivations of volunteers to participate in cultural crowdsourcing work. Information Systems Research, 28, 4 (2017), 744–759.

3. Bandura, A.; and Schunk, D.H. Cultivating competence, self-eficacy, and intrinsic interest through proximal self-motivation. Journal of Personality and Social Psychology, 41, 3 (1981), 586–598.

4. Bem, D.J. Self-perception theory. Advances in Experimental Social Psychology, 6, 1 (1972), 1–62.

5. Brehm, J.W. The intensity of emotion. Personality and Social Psychology Review, 3, 1 (1999), 2–22.

6. Burtch, G.; Hong, Y.; Bapna, R.; and Griskevicius, V. Stimulating online reviews by combining financial incentives and social norms. Management Science, 64, 5 (2018), 2065–2082.

7. Cabral, L.; and Li, L. (Ivy). A dollar for your thoughts: Feedback-conditional rebates on Ebay. Management Science, 61, 9 (2015), 2052–2063.

8. Campbell, D.J. Task complexity: A review and analysis. Academy of Management Review, 13, 1 (1988), 40–52.

9. Capa, R.L.; Audifren, M.; and Ragot, S. The efects of achievement motivation, task dificulty, and goal dificulty on physiological, behavioral, and subjective efort. Psychophysiology, 45, 5 (2008), 859–868.

10. Cerasoli, C.P.; Nicklin, J.M.; and Ford, M.T. Intrinsic motivation and extrinsic incentives jointly predict performance: A 40-year meta-analysis. Psychological Bulletin, 140, 4 (2014), 980–1008.

11. Chen, D.L.; and Horton, J.J. Are online labor markets spot markets for tasks? A field experiment on the behavioral response to wage cuts. Information Systems Research, 27, 2 (2016), 403–423.

12. Chen, H.; Hu, Y.J.; and Huang, S. Monetary incentive and stock opinions on social media. Journal of Management Information Systems, 36, 2 (2019), 391–417.

13. Christian, M.S.; Garza, A.S.; and Slaughter, J.E. Work engagement: A quantitative review and test of its relations with task and contextual performance. Personnel Psychology, 64, 1 (2011), 89–136.

14. Cialdini, R.B.; Eisenberg, N.; Green, B.L.; Rhoads, K.; and Bator, R. Undermining the undermining efect of reward on sustained interest. Journal of Applied Social Psychology, 28, 3 (1998), 249–263.

15. Daugherty, T.; Eastin, M.S.; and Bright, L. Exploring consumer motivations for creating user-generated content. Journal of Interactive Advertising, 8, 2 (2008), 16–25.

16. Deci, E.L. Efects of externally mediated rewards on intrinsic motivation. Journal of Personality and Social Psychology, 18, 1 (1971), 105–115.

17. Deng, X.N.; Joshi, K.D.; and Galliers, R.D. The duality of empowerment and marginalization in microtask crowdsourcing: Giving voice to the less powerful through value sensitive design. MIS Quarterly, 40, 2 (2016), 279–302.

18. Donovan, J.J.; Hafsteinsson, L.G.; and Lorenzet, S.J. The interactive efects of achievement goals and task complexity on enjoyment, mental focus, and efort. Journal of Applied Social Psychology, 48, 3 (2018), 136–149.

19. Elliot, A.J.; and Harackiewicz, J.M. Goal setting, achievement orientation, and intrinsic motivation: A mediational analysis. Journal of Personality and Social Psychology, 66, 5 (1994), 968–980.

20. Frey, B.S.; and Jegen, R. Motivation crowding theory. Journal of Economic Surveys, 15, 5 (2001), 589–611.

21. Frey, B.S.; and Oberholzer-Gee, F. The cost of price incentives: An empirical analysis of motivation crowding-out. American Economic Review, 87, 4 (1997), 746–755.

22. Gallus, J. Fostering public good contributions with symbolic awards: A large-scale natural field experiment at Wikipedia. Management Science, 63, 12 (2016), 3999–4015.

23. Gendolla, G.H.E.; and Richter, M. Cardiovascular reactivity during performance under social observation: The moderating role of task dificulty. International Journal of Psychophysiology, 62, 1 (2006), 185–192.

24. Gneezy, U. The W Efect of Incentives. Working paper, 2003.

25. Gneezy, U.; Meier, S.; and Rey-Biel, P. When and why incentives (don’t) work to modify behavior. Journal of Economic Perspectives, 25, 4 (2011), 191–210.

26. Gneezy, U.; and Rustichini, A. Pay enough or don’t pay at all. Quarterly Journal of Economics, 115, 3 (2000), 791–810.

27. Goes, P.B.; Guo, C.; and Lin, M. Do incentive hierarchies induce user efort? Evidence from an online knowledge exchange. Information Systems Research, 27, 3 (2016), 497–516.

28. Gómez-Miñambres, J. Motivation through goal setting. Journal of Economic Psychology, 33, 6 (2012), 1223–1239.

29. Grusec, J.E. The socialization of altruism. In M. S. Clark (Ed.), Review of Personality and Social Psychology. Newbury Park, CA: Sage, 1991, pp. 9–33.

30. Hagger, M.S.; and Chatzisarantis, N.L.D. Causality orientations moderate the undermining efect of rewards on intrinsic motivation. Journal of Experimental Social Psychology, 47, 2 (2011), 485–489.

31. Heyman, J.; and Ariely, D. Efort for payment— a tale of two markets. Psychological Science, 15, 11 (2004), 787–793.

32. Horton, J.J.; Rand, D.G.; and Zeckhauser, R.J. The online laboratory: Conducting experiments in a real labor market. Experimental Economics, 14, 3 (2011), 399–425.

33. Hossain, T.; and Li, K.K. Crowding out in the labor market: A prosocial setting is necessary. Management Science, 60, 5 (2014), 1148–1160.

34. Jenkins, G.D.; Gupta, N.; Mitra, A.; and Shaw, J.D. Are financial incentives related to performance? A meta-analytic review of empirical research. Journal of Applied Psychology, 83, 5 (1998), 777–787.

35. Kamenica, E. Behavioral economics and psychology of incentives. Annual Review of Economics, 4, 1 (2012), 427–452.

36. Ke, Z.; Liu, D.; and Brass, D. Do online friends bring out the best in us? The efect of friend contributions on online review provision. Information Systems Research, 31, 4 (2020), 1322– 1336.

37. Khansa, L.; Ma, X.; Liginlal, D.; and Kim, S.S. Understanding members’ active participation in online question-and-answer communities: A theory and empirical analysis. Journal of Management Information Systems, 32, 2 (2015), 162–203.

38. Khern-am-nuai, W.; Kannan, K.; and Ghasemkhani, H. Extrinsic versus intrinsic rewards for contributing reviews in an online platform. Information Systems Research, 29, 4 (2018), 871–892.

39. Landers, R.N.; Bauer, K.N.; and Callan, R.C. Gamification of task performance with leaderboards: A goal setting experiment. Computers in Human Behavior, 71(2017), 508–515.

40. Latham, G.P. Motivate employee performance through goal setting. Handbook of Principles of Organizational Behavior, 107(2000), 161–178.

41. Lee, T.W.; Locke, E.A.; and Phan, S.H. Explaining the assigned goal-incentive interaction: The role of self-eficacy and personal goals. Journal of Management, 23, 4 (1997), 541–559.

42. Lepper, M.R.; Greene, D.; and Nisbett, R.E. Undermining children’s intrinsic interest with extrinsic reward: A test of the “overjustification” hypothesis. Journal of Personality and Social Psychology, 28, 1 (1973), 129–137.

43. Locke, E.A.; and Latham, G.P. Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. American Psychologist, 57, 9 (2002), 705–717.

44. Mason, W.; and Suri, S. Conducting behavioral research on Amazon’s Mechanical Turk. Behavior Research Methods, 44, 1 (2012), 1–23.

45. Mason, W.; and Watts, D.J. Financial incentives and the “performance of crowds.” In Proceedings of the ACM SIGKDD Workshop on Human Computation—HCOMP ‘09. New York: ACM Press, 2009, 77–85.

46. Meier, S. A survey of economic theories and field evidence on pro-social behavior. In Bruno S. Frey and Alois Stutzer (Eds.), Economics and Psychology: A Promising New Cross-Disciplinary Field. Cambridge, MA: MIT Press, 2007, pp. 51–87.

47. Mento, A.J.; Steel, R.P.; and Karren, R.J. A meta-analytic study of the efects of goal setting on task performance: 1966-1984. Organizational Behavior and Human Decision Processes, 39, 1 (1987), 52–83.

48. Miller, S.D. How high- and low-challenge tasks afect motivation and learning: Implications for struggling learners. Reading and Writing Quarterly, 19, 1 (2003), 39–57.

49. Orvis, K.A.; Horn, D.B.; and Belanich, J. The roles of task dificulty and prior videogame experience on performance and motivation in instructional videogames. Computers in Human Behavior, 24, 5 (2008), 2415–2433.

50. Paolacci, G.; Chandler, J.; and Ipeirotis, P.G. Running experiments on Amazon Mechanical Turk. Judgment and Decision Making, 5, 5 (2010), 411–419.

51. Qiao, D.; Lee, S.-Y.; Whinston, A.B.; and Wei, Q. Financial incentives dampen altruism in online pro-social contributions: A study of online reviews. Information Systems Research, 31, 4 (2020), 1361–1375.

52. Rawsthorne, L.J.; and Elliot, A.J. Achievement goals and intrinsic motivation: A meta-analytic review. Personality and Social Psychology Review, 3, 4 (1999), 326–344.

53. Rode, J.; Gómez-Baggethun, E.; and Krause, T. Motivation crowding by economic incentives in conservation policy: A review of the empirical evidence. Ecological Economics, 117(2015), 270–282.

54. Schroeder, J.; and Fishbach, A. How to motivate yourself and others? Intended and unintended consequences. Research in Organizational Behavior, 35(2015), 123–141.

55. Seabright, P. Continuous preferences can cause discontinuous choices: An application to the impact of incentives on altruism. IDEI Working Paper, 2004.

56. Taylor, M.S. The motivational efects of task challenge: A laboratory investigation. Organizational Behavior and Human Performance, 27, 2 (1981), 255–278.

57. Vansteenkiste, M.; Matos, L.; Lens, W.; and Soenens, B. Understanding the impact of intrinsic versus extrinsic goal framing on exercise performance: The conflicting role of task and ego involvement. Psychology of Sport and Exercise, 8, 5 (2007), 771–794.

58. Wang, S.A.; Pavlou, P.; and Gong, J. Monetary incentives, online reviews, and product sales: An empirical investigation. In Proceedings of the 37th International Conference on Information Systems. Dublin, Ireland, 2016.

59. Zhang, X.; and Wang, C. Network positions and contributions to online public goods: The case of Chinese Wikipedia. Journal of Management Information Systems, 29, 2 (2012), 11–40.

60. Zhang, X.M.; and Zhu, F. Group size and incentive to contribute : A natural experiment at Chinese Wikipedia. American Economic Review, 101, 4 (2011), 1601-1615.

61. Zhao, L.; Detlor, B.; and Connelly, C.E. Sharing knowledge in social Q&A sites: The unintended consequences of extrinsic motivation. Journal of Management Information Systems, 33, 1 (2016), 70–100.

## About the Authors

Dandan Qiao (qiaodd@nus.edu.sg) is an Assistant Professor in the Department of Information Systems & Analytics at National University of Singapore. She received her Ph.D. from Tsinghua University and visited University of Texas at Austin as a research scholar. Her research interests focus on online crowd wisdom, economics of information platforms, and the analytics of user-generated content (UGC). Dr. Qiao’s work has been published in MIS Quarterly, Information Systems Research, and ACM Transactions on Knowledge Discovery from Data.

Shun-Yang Lee (sh.lee@northeastern.edu) is an Assistant Professor of Marketing at the D'Amore-McKim School of Business, Northeastern University. He received his Ph.D. from the University of Texas at Austin. His research focuses on the intersection of information systems and marketing, with an emphasis on behavioral issues in social networks and online platforms. Dr. Lee’s work has been published in Production and Operations Management, MIS Quarterly, Information Systems Research, and other journals.

Andrew B. Whinston (abw@uts.cc.utexas.edu) is the Hugh Cullen Chair Professor in the Information, Risk, and Operation Management Department at the McCombs School of Business at the University of Texas at Austin. He is Director of the Center for Research in Electronic Commerce. He has published over 300 papers in the major economic and management journals, and has coauthored 27 books. His recent work has appeared in Information Systems Research, MIS Quarterly, Management Science, and other journals.

Qiang Wei (corresponding author; qiangwei@tsinghua.edu.cn) is an Associate Professor in the Department of Management Science and Engineering, School of Economics and Management, Tsinghua University, China. His research interests include deep learning, UGC analysis, intelligent recommendation, and business analytics. His recent work has appeared in MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, and ACM Transactions on Knowledge Discovery from Data.
