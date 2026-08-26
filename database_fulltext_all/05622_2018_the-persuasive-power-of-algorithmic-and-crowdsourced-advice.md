---
otero_id: 5622
otero_key: "RFQGFJHJ"
title: "The Persuasive Power of Algorithmic and Crowdsourced Advice"
authors: "Junius Gunaratne; Lior Zalmanson; Oded Nov"
year: "2018"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2018.1523534"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Persuasive Power of Algorithmic and Crowdsourced Advice

Junius Gunaratne, Lior Zalmanson & Oded Nov

To cite this article: Junius Gunaratne, Lior Zalmanson & Oded Nov (2018) The Persuasive Power of Algorithmic and Crowdsourced Advice, Journal of Management Information Systems, 35:4, 1092-1120. DOI: 10.1080/07421222.2018.1523534

To link to this article: https://doi.org/10.1080/07421222.2018.1523534

![](/api/attachments/RFQGFJHJ/fulltext/images/a77507eb274250a95378cb8b4aee27a716148317ca0606b9d0e92512e10561ab.jpg)

View supplementary material

![](/api/attachments/RFQGFJHJ/fulltext/images/cf71e1b4958c9463b0867ec3eff10523140a4a78677ffb8deba1dbf8ce30f20a.jpg)

Published online: 17 Dec 2018.

![](/api/attachments/RFQGFJHJ/fulltext/images/2c62e40af28a559f6b65feca5290eb4a4e51bf3b7a72c2d597671a1810b64e36.jpg)

Submit your article to this journal

![](/api/attachments/RFQGFJHJ/fulltext/images/7a92ffffb588e2cc166a7ee24e5b64054e1ab42bf04033958a348a17fec016fa.jpg)

Article views: 24

![](/api/attachments/RFQGFJHJ/fulltext/images/1cb90015e124f2fa0d144409f83b3fdc5e258469981e47fef7e191139d3e7983.jpg)

View Crossmark data

# The Persuasive Power of Algorithmic and Crowdsourced Advice

JUNIUS GUNARATNE, LIOR ZALMANSON, AND ODED NOV

JUNIUS GUNARATNE (junius@nyu.edu) is a recent Ph.D. graduate from New York University Tandon School of Engineering. His research interests include applying theory and principles of human-computer interaction and behavioral economics in the user interface design to help in decision-making.

LIOR ZALMANSON is a lecturer (assistant professor) at the Information and Knowledge Management Department, University of Haifa, Israel. His research interests include social media, online engagement, commitment, internet business models, creative experimentation, sharing economy, and algorithmic management. His research has won awards and grants from Fulbright Foundation, Dan David Prize, Google, Marketing Science Institute, and Social Informatics SIG among others.

ODED NOV is an Associate Professor of Technology Management at New York University Tandon School of Engineering. He received his Ph.D. from Cambridge University. Dr. Nov’s research interests include human-computer interaction and decision making, social computing, social influence, and citizen science. His research has been supported by the National Science Foundation, the National Academies, the Financial Industry Regulatory Authority Foundation, Google, and the MacArthur Foundation.

ABSTRACT: Prior research has shown that both advice generated through algorithms and advice resulting from averaging peers’ input can impact users’ decision-making. However, it is not clear which advice type is more closely followed and if changes in decision-making should be attributed to the source or the content of the advice. We examine the effects of algorithmic and social advice on decision-making in the context of an online retirement saving system. By varying both the advice’s message and the attributed messenger, we assess what it is about the advice that people follow. We find that both types of advice have a positive effect on users’ saving performance, and that users follow advice presented as coming from an algorithmic source more closely than advice presented as crowdsourced. Our results shed light on how people view and follow online advice, and on information systems’ persuasive effects under conditions of uncertainty.

KEYWORDS: and phrases: online advice, algorithmic advice, crowdsourcing, decisionmaking, investment advice, personal finance, retirement portfolios, crowdsourced advice, online persuasion, uncertainty.

## Introduction

When making decisions under uncertainty, individuals tend to be receptive to the advice of others and allow it to inform their own choices [14, 113, 115]. Specifically, decades of research in the social sciences have shown that individuals are persuaded by the voice of expertise, which delivers experience and research-based knowledge, and is perceived as informed and relevant [13, 24, 33, 54, 76, 100, 111]. In addition, individuals are shown to be persuaded by their peers’ choices in many areas including decisions about their health and finances [17, 35, 50, 109]. Individuals attempt to minimize their information uncertainties by learning how others have acted in similar situations.

Prior research has incorporated these insights into user interfaces in decision-support and expert systems. Such studies have tested different types of advice and recommendations and their ability to influence user decision-making [2, 4, 43, 60, 114].

Studies have looked at advice generated through crowdsourcing—the aggregation of independent choices of many individuals that in essence reduces the variance of the recommendation to its mean. Online crowdsourcing enables advice that harnesses the collective intelligence of different people [22]. Researchers have demonstrated the generation of such advice from the wisdom of the crowds [58, 59, 101] to be highly effective in many situations, including knowledge creation and capital investment [16, 63, 79].

Other studies have examined the replacement of human actors with computerized systems [1, 51] creating a wide array of possibilities with respect to providing advice. Recommendation systems incorporate algorithms that implement a set of heuristics and the resultant algorithmic advice can help users improve their decisionmaking [1, 51].

In recent years, practitioners and researchers alike build on big data [95] – whereby very large repositories of data are available for the analysis of individuals and organizations, resulting in more informed decisions. Additionally, research in areas such as machine learning is increasingly focused on exploring new ways in which to enable computers dynamically adapt to new circumstances represented in data, and help users with their decision-making [53].

Both crowdsourced and algorithmic advice were shown to enable superior decisionmaking and better performance compared to that of an individual acting alone. However, it is not clear which of these types of advice users find more persuasive, and why they act on the advice provided to them. Though prior research has found that users are persuaded by averaged opinions generated by crowds and by opinions that are presented by experts [23, 65, 87, 98], prior research did not compare the two.

In this study, we address this gap by studying to what extent people follow advice they perceive as algorithmic or crowdsourced. To that end, we use the context of retirement saving. Retirement saving is a useful decision-making setting: it requires repeated decision-making, and the decisions made must change over time in order to be effective. Extant research shows that people are poorly equipped to make good decisions in circumstances where calculating risk and long-term trade-offs are necessary, including when saving for retirement, [9, 10, 11, 55, 56, 109], and are, therefore, more inclined to depend on outside parties to provide advice that assists with decision-making. Research shows people who save for retirement tend to be persuaded by social comparison with peer groups [119] as well as by the guidance of experts [80]. These factors make retirement saving an ideal context to study the persuasive effects of online advice.

We developed a retirement saving simulator that enabled users to make 35 successive “yearly” decisions. We used it to analyze the persuasive effect of advice by recording the difference between the saving recommendations shown to users, and users’ actual saving choices [40, 41, 42]. To further study what is it about the advice that people follow, we conducted a between-subjects study of users, in which we separated between the possible combination of algorithmic and crowdsourced advice message (the content of the advice) and messenger (who the advice is presented to emanate from). This research design allows us to hold the message constant while varying the messenger.

In what follows, we review prior research on algorithmic and crowdsourced advice, describe our research design and environment, and report our findings. We discuss our contribution to the study of persuasion in information systems and to the understanding of computer-mediated decision-making under uncertainty.

## Literature Review

While extant research studied the role of crowds and algorithms in decision-making, little work focuses on contrasting the effects of algorithmic and crowdsourced advice.

Research on the role of crowd-based and algorithmic advice in decision-making has largely focused on decision performance and accuracy. Many of these studies [1, 16, 63] have concluded that crowds or algorithms can perform better than informed individuals or experts in many decision-making contexts.

Surowiecki [101] popularized the notion of the Wisdom of the Crowds, showing that consensus-based decisions outperform others in many scenarios. Research on Wikipedia showed that the crowdsourced encyclopedia compares favorably with respect to quality of expert-created content [26, 38, 96]. Other comparisons of performance between crowds and experts focused on various prediction tasks. Such research has demonstrated that aggregated crowd-based suggestions can be at least as accurate as knowledgeable individuals or better [16, 63, 79, 97, 107]. Mollick and Nanda [79], for example, showed that crowds and experts tend to agree on artistic projects worthy of funding.

One explanation for the wisdom of the crowd is that the aggregation of estimates or combination of judgements cancels the error of individual bias. Larrick and Soll [62] found that many individuals hold incorrect beliefs about averaging and demonstrated in a series of experiments that people falsely conclude that the average of two judges’ estimates would be no more accurate than that of an average judge. Mannes [71] showed that groups providing advice can influence an individual’s beliefs, but the size of the group only has a modest effect on its influence. Participants in Mannes’ study made suboptimal use of advice by overweighting their initial beliefs and underweighting the more valid judgment of the group.

Other research has compared the performance of algorithms to that of human decision-makers. Research in this field showed that algorithms can outperform human judgment in assessments of different kinds of pathologies [8, 39, 44], operational risk [103], and answering trivia questions [106]. Algorithms can weigh cues derived from data more appropriately than people do [28] and better assess emerging patterns. In fact, algorithms can even identify more predictive cues. Given the success of such expert computational methods, in recent years a number of consumer financial brokerage firms and startup companies have begun to offer automated systems where algorithms are used to provide expertise to rebalance retirement portfolios automatically [36]. These automated systems are intended to augment or replace the expertise of humans managing retirement portfolios.

In many financial contexts, people were shown to benefit from advice on the one hand, and from comparing themselves with others on the other. Research in finance has shown that when lenders and borrowers have access to financial data of others they are more likely to adjust incorrect inferences, thus improving lender decisions and help those seeking loans [118]. In a study of crowd-sourced stock picks in online forums, Hill and Ready-Campbell [46] used a genetic algorithm approach to identify experts within the crowd. The online crowd that used expert advice performed better, on average, than the S&P 500 [46]. When more weight was given to the votes of the experts in the crowd, this increased the accuracy of the verdicts, improving performance yields.

To summarize, both algorithmic and crowdsourced advice can lead to accurate predictions or improved decision making. However, prior research has not compared how persuasive these two types of advice are, that is, what their relative effect on users’ behavior is. Specifically, it is not clear how users behave when the advice is presented as coming from an algorithmic versus crowdsourced source. In what follows, we review the literature on source perception and persuasion, as well as the persuasiveness of experts and crowds in general.

## Perception and Persuasion

The identity of the advice giver in the act of persuasion has been acknowledged in prior research. Two prominent models for persuasion are the Heuristic-Systematic Model [20, 21] and the Elaboration Likelihood Model [19, 90, 91]. Both models discuss a dichotomy: the existence of two routes to persuasion of an advice.

The first is named the central or systematic route in which people carefully and deliberately weigh in the arguments, their consequences, and consider the evidence and principles cited. The second is named the peripheral route or heuristic route is which the individual attends to cues that are tangential to the message substance, emphasizing the perceived characteristics of the source such as its attractiveness or expertise, the number of the arguments or the existence of a consensus regarding the advice [19].

What prompts one route over the other is the relevance of the topic to the individual, the level of complexity of the issue, and how fatigued or distracted the individual is. Financial decision making is often considered complex for individuals who are not professional in the field of finance [21, 91]. The number of variables to consider, the dynamics and volatility of markets, can drive participants to look for expert characteristics or a form of social proof [93, 108]. That is, they might default to peripheral/heuristic processing rather than the more involved central/direct processing; and in peripheral processing, one uses heuristic cues, including source credibility (here, expertise or personal familiarity), rather than the argument or information itself. The question regarding which of these cues, the voice of the algorithmic expert, or rather the voice of the crowds will have a bigger effect on compliance is an open question in the information systems literature.

## Persuasive Power of Social Circles and Crowds

Under uncertainty, people look to others for information [29, 37]. Deutsch and Gerard [29] called this tendency informational social influence, where people form a new opinion that incorporates the beliefs of others.

Informational social influence can be the result of presenting users with information on the behavior of their peers. Human-computer interaction researchers have studied the effects of showing such social information to users [58, 61, 64, 81, 82, 85, 119]. For example, a study by Muralidharan et al. [82] showed that users tend to disregard social information from strangers with uncertain expertise, but simultaneously show interest in social information from knowledgeable friends or friends who demonstrated expertise.

Social influence appears to be persuasive in many different scenarios, such as driving user adoption of security features on websites [27], or user ratings of consumer products [86]. In a related context, recommendation systems researchers have studied how social factors affect users’ perception of a system and the perceived expertise of a system Zhu and Huberman [120] showed that other people’s opinions significantly influence users’ choices. Ye et al. [117] demonstrated that social influence can be quantitatively captured and used to influence users through recommendations. Work in recommendation systems and social networks has also shown that providing recommendations through social referrals influences users more than without such referrals [3] and that adding social information to recommendations increases user satisfaction with the system [15].

In the context of financial systems, research shows that seeing others’ choices can influence a user’s financial decision-making [119]. Zhao et al. [119] added social information to a retirement saving system and found that users changed their fund investment decisions and attitudes toward risk based on seeing what others around them did. Recently, Hardin et al. [43] utilized a retirement investmentsimulator and showed that participants appeared to weigh boththe advice by the and the credibility indicators in the form of crowdapproval, in their financial decision making.

## Persuasive Power of Expert Advice

When people seek information from their environment in the form of advice, they are persuaded differently based on the confidence and perceived expertise of the advice maker [87, 104, 105, 110]. Studies on persuasion show that individuals tend to follow others who appear as experts in a specific field [76, 23], and that when advice purportedly comes from an expert source it is generally more persuasive than advice coming from unknown, unattributed or inexperienced sources [3, 34]. Early research by Hovland and Weiss [49] compared how people react to the same opinion essay, when they believe it was written by an expert or a novice, and found that an essay with an expert signature led to greater attitude change.

Similarly, systems and algorithmic computations that provide expert advice can influence users in comparable ways to human experts giving advice [30, 52]. This is due, in part, to the perception of computers as social actors: even though individuals do not perceive computers as human, they do interact with them in a manner similar to how they would with an individual [83, 84]. Thus, it is not surprising that users tend to have confidence in advice that comes from intelligent systems and value such advice as being similar to advice coming from experts [32], as long as knowledge is conveyed as the result of expert procedure or research. In cases where advice was portrayed instead as a statistical model, as in the study conducted by Önkal et al. [87], it was discounted compared to the human expert.

## Research Context and Questions

For the purpose of studying the effects of crowdsourced and algorithmic advice, we focused on retirement saving, which is characterized by repeated decision-making in changing conditions and under uncertainty [43]. Users must decide how much of their retirement portfolio should be allocated towards three types of assets that represent different levels of risk—stocks, bonds, and cash—on an annual basis.

Prior research has shown how crowd advice affects decisions in areas varying from funding art [79] to economic forecasts [16]. Research has also shown that algorithms, such as recommendations from IBM Watson’s artificial intelligence algorithm, can influence decision-making [106] and how both algorithms and crowds affect users’ decision-making [4, 23, 65, 70, 74, 82, 86, 87, 98] . However, there has been little prior research contrasting the two types of advice. Our research seeks to address this gap. First, we seek to understand the influence of algorithmic and crowdsourced advice on saving performance. This first set of research questions is intended to study the effects advice has on saving performance in our given financial context. To do so, we first examine the users’ performance when faced with these two types of advice, compared to performance when no advice is provided:

Research Question 1.1: How will people’s saving performance differ when faced with crowdsourced compared to no advice at all?

Research Question 1.2: How will people’s saving performance differ when faced with algorithmic advice compared to no advice at all?

Furthermore, we seek to assess the differences in advice-taking behavior. Specifically, how the presentation of advice source affects users’ advice-taking decisions. Literature on persuasion has identified that the characteristics of the advice’s source may have an effect of persuasion [19, 21]. However, it is not clear how users will react to a source they believe to be crowdsourced or algorithmically computed. In other words, what would the difference in users’ advice-taking behavior be if they believe the advice is the result algorithmic or crowdsourced, controlling for the advice’s content? To do so, we break down advice into two components: the advice message (the content of the advice that the recipient is given), and the advice messenger (who the advice emanated from).

Research Question 2: Given the same advice message, how will people’s advicetaking behavior differ when faced with an advice they believe to come from an algorithmic compared to a crowdsourced messenger?

## Method

## Materials and Procedure

To address the study’s research questions, we developed a controlled experimental environment consisting of a 35-year retirement saving simulation (Figures 1 and 2), similar to ones used in prior research (e.g., [43]). We gave study participants the task of reaching a goal of \$1.5 million by retirement, with yearly contributions of \$10,000 to be allocated to different funds using the simulator. The design of the simulator resembled Vanguard Group’s popular retirement saving platform. Retirement saving requires understanding how different asset types can be used in a retirement portfolio over time. Stocks are the riskiest investment type, but provide the greatest return over time. Bonds are less risky, but provide a lower return. Cash has no risk and provides minimal return [99].

Participants began the experiment by reading instructions about the retirement simulation, accompanied by an interactive calculator that helped them learn about stocks, bonds and cash, as well as expected returns and volatility of each of those asset classes. Participants then started the simulation where we presented them with an allocation screen for choosing the percentage of their portfolio to allocate towards stock, bond and cash funds (Figure 2). For each year in the simulation, users could choose to either set that year’s savings mix, which changed how they saved new contributions for the year, or to optionally rebalance their entire savings, which changed how they divided the entire retirement saving account balance between funds.

![](/api/attachments/RFQGFJHJ/fulltext/images/1b8209b690afeaabb417b12273f4feec3d39188f9460bcb82d671ee66c14a721.jpg)

![](/api/attachments/RFQGFJHJ/fulltext/images/3a1927715eededd70539e35d286ff8f04aa2ce76fd5aec5fb012f97f9637aeba.jpg)

<table><tr><td>Date</td><td>Transaction</td><td>Amount</td></tr><tr><td>1/1/2019</td><td>Investment Grade Bond Fund G 27.0%Stock Index Fund Q 73.0%</td><td>$10,000.00</td></tr><tr><td>1/1/2018</td><td>Investment Grade Bond Fund G 11.0%Stock Index Fund Q 89.0%</td><td>$10,000.00</td></tr><tr><td>1/1/2017</td><td>Investment Grade Bond Fund G 16.0%Stock Index Fund Q 84.0%</td><td>$10,000.00</td></tr><tr><td>1/1/2016</td><td>Investment Grade Bond Fund G 12.0%Stock Index Fund Q 88.0%</td><td>$10,000.00</td></tr><tr><td>1/1/2015</td><td>Investment Grade Bond Fund G 10.0%Stock Index Fund Q 90.0%</td><td>$10,000.00</td></tr></table>

Figure 1. The retirement simulator allowed users to make repeated decisions for 35 simulated years

Participants could set percentages for asset classes when selecting funds for their retirement portfolio. A pie chart gave up-to-date information on how the portfolio allocation changed with market volatility, and a historical line chart showed how 285 participants’ savings grew over time (Figure 1). Pressing an allocate savings button led to a screen that allowed users to set annual savings allocations (Figure 2). Noncontrol conditions displayed asset allocation recommendation text in red (Figure 3) on the annual savings allocations screen. Accompanying the main functionality of the retirement simulator, we showed users one of two messengers (crowdsourced vs. algorithmic) and one of two message types: (1) the average fund allocation of other users in any given year (crowdsourced) or (2) an allocation of funds in any given year, based on financial research on optimal allocation [94] during one’s retirement saving career (algorithmic). In what follows, we will refer to a combination of a messenger-message as advice.

Financial advisers recommend setting a predefined savings goal [25, 45, 69] based on a retirement replacement income and taking an appropriate level of risk rather than trying to maximize funds through risky investments [74, 109]. Risk tends to be especially important to mitigate the closer one gets to retirement. Following the approach of achieving a retirement goal rather than maximizing returns or evading risks [75], we rewarded taking goal-driven moderate risk. Consequently, we based users’ compensation on a \$1.00 default pay and a maximum bonus of \$4.00 if they met the \$1.5 million retirement goal. Deviation from the goal either positively or negatively led to a proportionally lower bonus. This 4/1 bonus/default compensation ratio provided incentive to achieve the savings goal rather than maximizing returns with riskier behavior.

Set thisyear's savings mix for 2016 Specify how your savings for this year should be used to buy the funds below. Your choices will only affect this year.  
![](/api/attachments/RFQGFJHJ/fulltext/images/97efe9164258c4229b4110e1b0b752e934c58b35f42add773472d48798f93ab4.jpg)  
Figure 2. The retirement simulator’s asset allocation screen

In what follows we describe how the two possible values of the advice’s message: the crowdsourced and the algorithmic were calculated.

## Crowdsourced Message Allocation

Consistent with prior research on social influence and the wisdom of the crowds [16, 59, 63, 79], we treat crowdsourced message as the mean allocation of previous participants. We presented users with the average of their peers’ allocations as crowdsourced message. A pre-study with 117 users presented users of the retirement simulator with no advice. The average fund allocation in each year of the pre-study was then presented to users of the main study as their peer allocations. If users were to always follow the crowdsourced message, they would have reached within \$171,127 of their \$1,500,000 USD goal. It is important to note that users from the

## Set this year's savings mix for 2016

Specify how your savings for this year should be used to buy the funds below. Your choices will only affect this year

The percentages in the right column are the average allocations of \$10,000 made by other people in the study for the current year

<table><tr><td>Name</td><td>Your entire portfolio(all years)</td><td>This year</td><td>Based on other people&#x27;s average allocations in this study:</td></tr><tr><td>Amount saved</td><td>$0.00</td><td>10000</td><td></td></tr><tr><td>Investment Grade Bond Fund A</td><td>0.0%</td><td>0%</td><td>10%</td></tr><tr><td>Investment Grade Bond Fund E</td><td>0.0%</td><td>0%</td><td>7%</td></tr><tr><td>Investment Grade Bond Fund G</td><td>0.0%</td><td>0%</td><td>9%</td></tr><tr><td>Lifecycle Fund 4</td><td>0.0%</td><td>0%</td><td>12%</td></tr><tr><td>Lifecycle Fund 6</td><td>0.0%</td><td>0%</td><td>5%</td></tr><tr><td>Lifecycle Fund B</td><td>0.0%</td><td>0%</td><td>4%</td></tr><tr><td>Money Market Cash Fund</td><td>0.0%</td><td>0%</td><td>7%</td></tr><tr><td>Stock Index Fund N</td><td>0.0%</td><td>0%</td><td>19%</td></tr><tr><td>Stock Index Fund Q</td><td>0.0%</td><td>0%</td><td>18%</td></tr><tr><td>Stock Index Fund R</td><td>0.0%</td><td>0%</td><td>9%</td></tr><tr><td colspan="4">Total 0.00%</td></tr></table>

Figure 3. In advice conditions, the right column displayed recommended fund allocation percentages

pre-study could not participate in the main study, guaranteeing all participants in the main study had no prior exposure to the retirement simulator.

## Algorithmic Message Allocation

The algorithmic message provided to users in the study is an industry standard, based on finance research on how to rebalance stocks and bonds over time [94]. To calculate the total amount of the portfolio that should be allocated to stocks we used the initial recommended amount of a portfolio that should be allocated towards stock when an individual begins his or her saving career (90% of the portfolio should be in stock) minus the number of years the individual has been saving to date. We derived this rebalancing calculation from research in target-date retirement funds [6, 7, 72, 78, 92, 94, 102], also known as lifecycle funds, that recommend more conservative approaches towards asset allocation as retirement approaches. Following this approach, portfolio assets should be reallocated over time from stocks to bonds over time [92]. The benefits of lifecycle funds and how they reallocate assets over time have been studied extensively [6, 7, 92, 94]. For the purpose of our study lifecycle fund price data used a mix of data from a stock index fund (S&P 500) and a bond index fund (Fidelity Investment Grade Bond Fund, FBNDX), and dynamically changed allocation over time using a lifecycle fund allocation model formula [92, 94]. Lifecycle funds assume people should have more stocks in their saving portfolio when they are younger and can take risk, and more bonds as they get closer to retirement. Actual market data from 1980 represented the simulated year of 2016, 1981 represented 2017, and so on.

$$
s _ {p} = s _ {i} - \frac {(y _ {t} - y _ {r})}{1 0 0}
$$

where

$s _ { p }$ Percent of entire portfolio that should be in stock for the current year;

s<sub>i</sub> Percent of stock in the portfolio for the initial year 90% ;

y<sub>t</sub> Total years worked 35  ;

y<sub>r</sub> Remaining years until retirement:

To calculate how an individual should allocate the \$10,000 savings for the year, we used the percent of portfolio that should be in stock for the current year multiplied by the total amount saved in the portfolio to date plus the current year’s savings. We then subtracted the amount of the portfolio that should be in stock from the actual amount of the entire portfolio the user had saved in stock. Next, we divided the overall value calculated by the amount saved that year to generate a percentage. We set the minimum and maximum percentage values for recommended stock to 0% and 100%, respectively.

$$
s _ {r} = \frac {s _ {p} \left(a _ {t} + a _ {y}\right) - s _ {t}}{a _ {y}}
$$

where

$s _ { r } = \mathrm { R }$ ecommended stock percentage allocation for this year s saving amount;

$a _ { t } =$ Total amount saved in the portfolio to date in dollars;

a<sub>y ¼</sub> Amount that will be saved this year \$10 <sub>ð</sub> <sub>Þ</sub> ; 000 ;

## s<sub>t</sub> Totalstockamountofentireportfolioindollars

We calculated the recommended percent of bonds that the user should allocate of the \$10,000 savings for the year by taking one minus the recommended percent of stock that the user should allocate of the \$10,000 savings for the year. We set the cash recommendation to always be 0%.

$$
b _ {r} = 1 - s _ {r}
$$

where

$$
g = \sum_ {i = 1} ^ {y _ {t}} | p _ {s} - p _ {u} |.
$$

## Treatments

Utilizing the two messenger values and two message values, we arrive at four experimental conditions (Figure 4):

The two base conditions help us to answer Research Question 1 and identify the chief differences in responses to different advice types. These two conditions that will be referenced as the algorithmic messenger-algorithmic message and crowdsourced messenger-crowdsourced message, showed statements that accurately portrayed the underlying content (i.e., allocation percentage) presented to participants (Figure 4).

![](/api/attachments/RFQGFJHJ/fulltext/images/e657e1c23ab4aea4b05dc9e3928ba1c7d7362f623f0b656bc45015597beccdea.jpg)  
Figure 4. The text describing the advice (messenger) and the percentages displayed (message) differed in each condition

## Crowdsourced Messenger-Crowdsourced Message

The crowdsourced messenger-crowdsourced message condition provided adaptive advice by displaying the average asset allocations of prior participants in the study, at the same stage of the saving career, and was framed with the statement: “The percentages in the right column are the average allocations of \$10,000 made by other people in the study for the current year.” Here too, the asset allocation information presented to participants (i.e., the message) accurately reflected the information about the source of the message (i.e. the messenger).

## Algorithmic Messenger-Algorithmic Message

The algorithmic messenger-algorithmic message condition provided adaptive advice in the form of a target-retirement formula [72, 92, 94] for data that provided asset allocation recommendations framed with the statement: “Based on recent research, the right column shows the recommended allocation of your \$10,000 savings for the current year.” Framing the advice as ‘recent research’ helped us avoid a complex statistical explanation and presented the algorithmic advice, generated programmatically from a formula, similar to how a human expert would have phrased it.<sup>2</sup> The asset allocation information presented to participants (i.e., the message) accurately reflected the information about the source of the message (i.e. the messenger).

## Control Condition

The control condition did not display advice. In this condition participants moved through the retirement simulation without seeing any supplemental information to influence their decisions. We ran the control condition in a pre-study to obtain the data that was used in the crowdsourced advice conditions. The pre-study users could not participate in main study.

We then ran the control condition for the main study and compared the results it to the pre-study control condition data and found the data in both runs not significantly different (full results can be found in online Appendix 1).

To address Research Question 2 and study the effect of an advice’s messenger we added two additional associated conditions, crowdsourced messenger-algorithmic message and algorithmic messenger-crowdsourced message. These conditions used identical statements to the algorithmic messenger-algorithmic message and crowdsourced messenger-crowdsourced message conditions; however, in these conditions we switched the underlying data presented for asset allocation recommendations (Figure 4). In other words, in these conditions users were exposed to algorithmic advice content presented as crowdsourced advice, and crowdsourced advice content presented as algorithmic advice. These were shown in addition to the previous conditions so in fact. This allows it allowed us to separate the role of the messenger from the advice message. Details of each of the combinations are provided in in the following sections.

## Crowdsourced Messenger-Algorithmic Message

The crowdsourced messenger-algorithmic message condition used the crowdsourced statement (“The percentages in the right column are the average allocations of \$10,000 made by other people in the study for the current year.”) in the crowdsourced-crowdsourced condition, but used the target-retirement formula asset allocation advice of the algorithmic messenger-algorithmic message condition. By interchanging the attributed source and asset allocation content shown to the user we sought to understand how the framing of messenger and message itself affected decision-making.

## Algorithmic Messenger-Crowdsourced Message

The algorithmic messenger-crowdsourced message condition used the same statement as the algorithmic messenger-algorithmic message condition (“Based on recent research, the right column shows the recommended allocation of your \$10,000 savings for the current year.”), but used the average percentage allocation data from the crowdsourced messenger-crowdsourced message condition. Here too, we sought to understand how the framing of messenger and message itself affected decision-making by interchanging the attributed source and asset allocation content shown to the user.

## Measures

## Saving Performance

To address Research Question 1, we used the following measures to examine differences in users’ saving performance across different advice types.

We first measured users’ average difference from the saving goal of \$1,500,000 USD. It gives us a simple and comparable measure for differences in performance across different presentations of advice.

Our second measure was the likelihood of participants to end up within 10% of the saving goal. We note that a 10% range represents a reasonably achievable interval. Moreover, using a small range around the goal, and categorizing users as either within or outside it (rather than the full distance from the goal), ensures that outliers—users who are very far from their goal—are not given too much weight.

Our third measure captures users’ risk taking reflected in the allocation of stock in their portfolio. If users have chosen a significantly higher/lower percentage of stocks in the portfolio compared to the control, this can be attributed to the effect of the advice. Overall, in retirement saving, the advice tends to decrease their portfolio risk over time by gradually shifting their allocation from stocks to bonds. According to financial theory, exposure to stocks should be high at the beginning of one’s retirement saving career and low by the end of it.

## Advice-Taking

In Research Question 2 we focused on how closely users followed the advice. This was measured by the cumulative gap (in absolute value) between users’ asset allocation and the allocation recommended to them. In other words, for each year we calculated the sum of distances between the percentage allocation stated in the advices’ message part, and the allocation made by users. We then summed up the yearly distances to obtain the cumulative gap between advice given and allocation made. Therefore, in the extreme case, if a user allocated their investment exactly as recommended in the advice presented to them, their cumulative gap would be equal to zero. The more a user deviates from the recommended advice, the higher the cumulative gap. This measure is behavioral—focusing only on following the advice presented—and is independent from how users’ their investments performed.

The equation used was:

$$
b _ {r} = 1 - s _ {r}
$$

where

$$
y _ {t} = \text { Total   years   worked } (3 5);
$$

$$
p _ {s} = \text { System   percent   recommendation };
$$

$$
p _ {u} = \text { User   entered   percent };
$$

$$
g = \text { Cumulative   gap   across   all   years }
$$

## Participants

We recruited users via Amazon Mechanical Turk. This platform has been highly utilized for similar research in information systems [5, 18, 57, 73, 77]. Further, recent work has studied the demographics of MTurk participants, validated MTurk’s replication capabilities, and advocated its use in social sciences [12, 47, 48, 88]. Following these papers’ best practices, we have limited participation to U.S. users with at least 100 prior Human Intelligence Tasks (HITs) at an approval rate higher than 99%.

We gave participants up to one hour to complete the simulation.

Following a between-subjects experimental design, 314 users took part in the experiment. Their average age was 35.1 and 45.9% were women. Our study consisted of four crowdsourced influence conditions: algorithmic messenger-algorithmic message (n = 68), crowdsourced messenger-crowdsourced message (n = 57), crowdsourced-messenger-algorithmic message (n = 68) and algorithmic messenger-crowdsourced message (n = 60) as well as a control condition (n = 61).

To create a realistic simulation of the retirement saving experience, we gave users the option to rebalance their entire retirement portfolio during any year of the study. We did not provide any advice regarding when to rebalance. 62% of all users chose to rebalance their retirement portfolio an average of 2.55 times at some points during the study. We found no significant differences between algorithmic advice and crowdsourced advice conditions in terms of likelihood to rebalance and the average number of rebalances.

Since our research focused solely on decisions that include algorithmic advice and crowdsourced advice, and because we did not find significant differences in rebalancing behavior, we did not study rebalancing decisions any further.

## Results

# Effect of Advice on Saving Performance

To address Research Question 1.1, we first compared the crowdsourced advice condition (crowdsourced messenger–crowdsourced message) to the control condition (Table 1).

Crowdsourced message condition had a difference from the saving goal of \$147,620 which was not statistically significant compared to the goal (p = 0.4). However, when measuring the percentage of participants that were in the reach of 10% of the goal, we found that while only 48% have succeeded in this mission when no advice was given, 65% of users in the crowdsourced advice condition (p = 0.054) reached within 10% of the study goal.

To address Research Question 1.2, we compared algorithmic advice condition (algorithmic messenger-algorithmic message) to the control condition (Table 1). Users in the algorithmic advice condition have performed significantly different compared to control. They had a difference of 89,742\$ on average from the saving goal compared to 172,277\$ in the control group (p < 0.01). When measuring the percentage of participants that were in the reach of 10% of the goal, we found that while only 48% have succeeded in this mission when no advice were given, 79% in the algorithmic condition (p < 0.01)

Moreover, in both conditions, at the beginning of the study, users tended to allocate a large proportion of their portfolios to stocks and by the end of the study to decrease the proportion of stocks. However, in the control condition users were more likely, on average, to have a lower proportion of stock funds in their portfolios throughout the course of the study (Figure 5), demonstrating that the

Table 1. Comparison of Crowdsourced and Algorithmic Advice Performance Measure and Time Spent in the Study with the Control Condition

<table><tr><td></td><td>Difference from Saving Goal</td><td>Reach Within 10% of Goal</td><td>Minutes</td></tr><tr><td>Control (n = 61)</td><td>$172,277</td><td>48%</td><td>18.4</td></tr><tr><td>Crowdsourced Messenger Crowdsourced Message (n = 57)</td><td>$147,620</td><td> $65\%^{\dagger}$ </td><td>20.5</td></tr><tr><td>Algorithmic Messenger Algorithmic Message (n = 68)</td><td>$89,742**</td><td>79%**</td><td>14.6*</td></tr></table>

Notes: $^ { * * } \mathrm { \bf p } < 0 . 0 1 ,$ ${ } ^ { * } \mathbf { p } < 0 . 0 5 ,$ , †p < 0.1 (significance of difference from the control condition).

## Percent of Portfolio Allocated to Stock Funds

![](/api/attachments/RFQGFJHJ/fulltext/images/1c0790b75a929a4f5330c1f610a106e821384994ff1ea5a47e54281721a042cb.jpg)  
Figure 5. Differences in stock fund allocation of user portfolios over time

recommendations influenced user decision-making behavior, compared to how they would have behaved with no advice. In other words, showing any type of advice encouraged users to invest more in stock funds.

## Effect of the Messenger on Advice-Taking Behavior

To address Research Question 2 we conducted two comparisons, in which we varied the messenger while holding the message constant. This allowed us to study the effects of the perceived messenger on advice taking.

We first calculated the cumulative gap across all years for all conditions. These amounted to 23.7, 31.5, 41.8, and 16.7, respectively. Descriptive statistics of all conditions can be found in Table 2.<sup>3</sup>

We divided these four conditions into two comparisons based on the content in each of our two advice types. First, we selected the crowdsourced message which is a mean of past participants, a message that is relatively close to what a participant would choose freely. We compared between participants who were told this advice comes from an algorithmic expert and those who were told it is crowdsourced. We found a cumulative significant gap $( \mathtt { p } < 0 . 0 1 )$ demonstrating that users tended to follow an advice they believed to come from the result of an algorithmic calculation closer than an advice which is the result of crowdsourcing.

Second, we selected the algorithmic message, a formula that can lead to more extreme advice. Again, we compare between participants who were told this advice comes from an algorithmic expert and those who were told it is crowdsourced. We found significant cumulative gap difference $( \mathtt { p } < 0 . 0 1 )$ . In this case as well, users tended to follow an advice perceived as algorithmic closer than a crowdsourced one.

Third, we ran a linear regression (Table 3) with the cumulative gap difference as its outcome variable, controlling for demographic variables including: age, gender, and a dummy variable noting if the participant has retired, as well as level of experience. We added dummy variables that determine if this condition has a) an algorithmic messenger, b) an algorithmic message, or c) interaction of the algorithmic message and algorithmic messenger. Overall, we noted that controlling for all other variables, the algorithmic messenger was associated with $\mathbf { a } - 1 6 . 3 1 0$ decrease in the cumulative gap percentage points $( \mathtt { p } < 0 . 0 0 1 )$ ). The algorithmic message was associated with an 8.04 increase in the cumulative gap percentage points $( \mathtt { p } = 0 . 0 0 1 )$ and the interaction of the algorithmic messenger and message was statistically insignificant $( \mathtt { p } = 0 . 5 1 4 )$ Moreover, we noted that age does not play a role in the advice-taking behavior $( { \mathfrak { p } } =$ 0.548), but male gender $( \mathrm { B } = 4 . 0 8 9 , \mathrm { p } = 0 . 0 3 4 )$ , experience with the stock market (B $= 4 . 7 8 9 , \mathfrak { p } = 0 . 0 0 1 )$ and whether or not users have a $4 0 1 ( \mathrm { k } )$ retirement account $( \mathrm { B } =$ $5 . 0 6 5 , \mathfrak { p } = 0 . 0 2 1 )$ all decrease the cumulative gap.

Table 2. Descriptive Statistics for Each Condition in the Study

<table><tr><td></td><td>Control</td><td>Algorithmic Messenger Algorithmic Message</td><td>Algorithmic Messenger Crowdsourced Message</td><td>Crowdsourced Messenger Crowdsourced Message</td><td>Crowdsourced Messenger Algorithmic Message</td></tr><tr><td>Mean Age</td><td>36.41</td><td>34.75</td><td>33.92</td><td>34.35</td><td>35.9</td></tr><tr><td>Percent Male</td><td>0.66</td><td>0.54</td><td>0.48</td><td>0.56</td><td>0.47</td></tr><tr><td>Mean Experience Level</td><td>2.28</td><td>2.25</td><td>2.15</td><td>2.25</td><td>2.22</td></tr><tr><td>Has Retirement Account</td><td>0.64</td><td>0.66</td><td>0.62</td><td>0.68</td><td>0.62</td></tr><tr><td>Minutes Spent in Study</td><td>18.43</td><td>14.56</td><td>22.3</td><td>20.54</td><td>16.69</td></tr><tr><td>Recommendation Percent Cumulative Gap Across All Years</td><td>-</td><td>23.73</td><td>16.74</td><td>31.54</td><td>41.82</td></tr><tr><td>Difference from Saving Goal</td><td>172,277</td><td>89,742</td><td>1,322,517</td><td>147,620</td><td>98,363</td></tr><tr><td>Reach Within 10% of Goal</td><td>0.48</td><td>0.79</td><td>0.68</td><td>0.65</td><td>0.87</td></tr></table>

Table 3. Linear Regression on Recommendation Percent Cumulative Gap Across All Years Showing Differences Between Types of Advice and Allocations

<table><tr><td rowspan="2">Model</td><td colspan="2">Unstandardized Coefficients</td><td>Standardized Coefficients</td><td rowspan="2">t</td></tr><tr><td>B</td><td>Std. Error</td><td>Beta</td></tr><tr><td>(Constant)</td><td>19.773**</td><td>4.506</td><td></td><td>4.388</td></tr><tr><td>Algorithmic Messenger</td><td>-16.310***</td><td>2.612</td><td>-.415</td><td>-6.243</td></tr><tr><td>Algorithmic Message</td><td>8.604**</td><td>2.506</td><td>.221</td><td>3.433</td></tr><tr><td>Algorithmic Messenger X Algorithmic Message</td><td>-2.511</td><td>3.844</td><td>-.054</td><td>-.653</td></tr><tr><td>Age</td><td>-.062</td><td>.104</td><td>-.030</td><td>-6.834</td></tr><tr><td>Gender (Male=1)</td><td>4.089*</td><td>1.925</td><td>.106</td><td>2.124</td></tr><tr><td>Has Experience (Dummy Variable)</td><td>4.789**</td><td>1.394</td><td>.192</td><td>3.437</td></tr><tr><td>Has Retirement Plan (Dummy Variable)</td><td>.5.056*</td><td>2.174</td><td>.125</td><td>2.326</td></tr><tr><td colspan="5">*p&lt;0.05, **p&lt;0.01, ***p&lt;0.001 significance of difference.</td></tr></table>

## Discussion

This study examines the persuasive power of two types of advice, algorithmic advice and crowdsourced advice, in the context of retirement savings systems. Increasing use of data for decision making has made these two types of advice popular in a variety of online applications, and in particular in financial contexts.

Previous studies, both in information systems [30, 113] and finance [70, 80], have found both algorithmic advice and crowd advice to be persuasive in separate contexts. However, these types of advice have not been examined in relation to each other, using the same user context. In this study, we provided a detailed contrast of the two types of advice using a simulator designed to test participants’ reactions to different types of advice. First, we showed that the presence of these types of advice changed saving performance and improved participants’ likelihood of achieving a retirement saving goal compared to a condition where no advice was given at all (RQ1).

In addition, we separated the effects of the messenger of the advice and the advice’s message. We found that advice that is presented as the result of researchbased algorithmic calculation is significantly more persuasive than advice that presents itself as an aggregation of peer behavior (RQ2). This result contributes directly to the literature that recognized the influential power of both “authority” and the presence of “social proof” [24, 67, 68] in the framing of decision-making situations on individual behavior. Specifically, previous studies on persuasion showed that when people are faced with a complex decision-making situation, they often resort to putting more weight on the qualities of the advice giver [19]. That is, they default to peripheral processing rather than the more involved direct processing. In peripheral processing, there is a tendency to use heuristic cues, including source credibility rather than the argument or information itself [19, 20, 21, 90, 91]. Our findings show that a statement conveying professional algorithmic authority appears to be a more persuasive heuristic cue than a statement conveying social proof conveyed through the behavior of investing peers. These findings are intriguing given that in the algorithmic condition, the calculation underlying the algorithm remains opaque (no information is provided to users other than framing it as resulting from research), while in the crowdsourced condition users have more information about the way the advice was calculated (i.e., average of past allocations of other users).

## Implications for Practitioners and Policy Makers

Our research highlighting how advice is conveyed and attributed in information systems has implications for user decision-making. Advice can be used to the benefit of individuals to help them make better decisions, which in turn may lead to better financial outcomes. However, the persuasive power of advice and the relative ease with which it can be manipulated through the use of text means that one must be cautious and thoughtful about how advice is presented. Our results do not endorse deception through crafty wording or by mislabeling data to increase its influence, rather they are a warning—to financial institutions, policy makers, and designers in particular—that certain presentation of data can lead to unintended and undesired consequences. System designers should accurately represent the source of information to reflect the information provided. Today’s automated retirement portfolio saving systems, which include start-up companies such as Betterment and Wealthfront [66], use algorithms to provide automated investing to their customers [112]. However, automated investing algorithms differ from one company to another, with each company’s algorithm leading to different investment performance and outcomes. Our results indicate that users are likely to be persuaded by any system that provides recommendations coming from an algorithm, regardless of the actual historical performance of the system. Therefore, rather than stating information is coming from an algorithm, we recommend the use of carefully worded text that increases transparency for the user. Furthermore, a number of financial websites, such as Estimize [89], use crowdsourced data to predict company earnings data. Information in some online outlets present such data as coming from a consensus of authoritative sources rather than saying it is the consensus of other people using the website [89]. While our results show that presenting data as coming from an authoritative source versus the crowd will make it more persuasive, and may possibly contribute to improved financial performance, such practice should not be an excuse to mislead people about the source of the advice they receive.

Government regulators can encourage financial firms to provide more insight to consumers regarding how algorithmic advice is generated. Illustrating the inner working of algorithms to the general public may prove challenging in many cases. However, it may be useful to be transparent about what can be explained and what not, that is, to provide consumers information about how the algorithm makes recommendation as well as a clear picture of how user peers are doing on financial systems. Providing both sets of information could potentially keep the algorithmic advice in check in addition to making it seem more credible.

## Limitations and Future Work

This study includes a design of a research environment to understand how algorithms and crowds persuade individuals in the context of retirement saving. However, one should note that the ability to make similar conclusions about how saving performance is affected by the same types of advice is limited. First, we built our simulator based on data on the stock and bond markets from 1980 to 2014. Market performance could change in the future, leading users to change their inclination with respect to how closely they follow investment advice. Second, algorithm advice may vary in quality according to the choice of model and heuristics. Some algorithms may provide better advice than others.

In our study, the algorithmic advice provided used a calculation that in most cases allocates money to only one or two funds at any given year, to counteract deviation from an “optimal” portfolio, while averaging overall peer decisions yields a more uniform distribution of allocations among the ten funds. In comparison to algorithmic advice, crowdsourced advice is not as extreme in terms of its variance of funds allocation. Crowdsourced advice may fit well with users who wish to be more careful and diversified when exposed to volatility, preferring not to put all their eggs in one basket. Having said that, given that this is a lab experiment and past market performance is no indication of what may happen in the future, users may choose different portfolio allocations in other settings and a crowdsourced message could be proven more influential in future scenarios.

Our findings on advice-taking show that people will be more likely to follow advice portrayed as the result of an algorithm than those portrayed as the wisdom of the crowds. Future research may examine if this effect changes when the crowds are presented as crowds-experts, a group of financially savvy individuals or if crowds are replaced by social circles of the users (i.e., averaging over investments of their social network friends). Moreover, it may be useful to combine insights from past studies on expert systems advice that have used explanations for the advice [116], to find out if providing further explanations about the mechanism behind the calculation will change user advice-taking behavior. More specifically, an interesting question concerns how advice-taking behavior will change when there is a high degree of process transparency. In an age of growing use of algorithmic and statistic methods for day-to-day predictions, it is not clear if a view “under the hood” to the process behind the algorithm will strengthen their persuasion or end up in confusion or information overload that will then lower persuasion. These are important questions for further inquiry.

Another limitation of the research is that it focuses only on the specific context of retirement saving decisions. While the results might be generalizable to other contexts, a number of domain-specific considerations may affect decision-making. For instance, artificial intelligence systems such as IBM’s Watson use algorithms to generate medical treatment suggestions that are then examined by a team of doctors who make a final decision on patient treatment. Such a workflow is effectively a combination of different sources of advice and is demonstrated to be better than either approach used separately [31]. This is in contrast to choosing and acting on algorithmically-generated advice over human-generated advice or vice versa. Given the varying circumstances under which advice is provided and used, we hope that future research can help apply our findings to other fields to understand how the persuasiveness of message and messenger affects decision-making.

## Conclusion

After decades of research on the effects of perceived expertise and social proof on persuasion, we still know relatively minimal amount regarding their impact in the context of computer-based financial decision-making. In the present study we examine the relative persuasive effects of these two factors in the context of algorithmic and crowdsourced advice, in an online financial saving system. Fundamentally, our results point to the importance of theorizing and testing the interactions between the online advice’s content and attributed source (i.e., message and messenger) to obtain an accurate picture of how certain advice persuades users to make certain financial choices. Overall, our results shed light on how people view and follow online advice and on information systems’ persuasive effects under uncertainty. Future research can build on this work to study other decision contexts, combining different algorithms and social influences, and testing for the heterogeneity of reactions among different countries and cultures.

## NOTES

The bonus is calculated is calculated in the following way: reward in USD = ((1 - | (totalvalue - 1500000) / 1500000| \* 9) \* 400) / 100 where total value is total amount the participant saved. If the reward is negative, no reward is given.

## Supplemental Material

Supplemental data for this article can be accessed on the publisher’s website.

## ORCID

Oded Nov http://orcid.org/0000-0001-6410-2995

## REFERENCES

1. Adomavicius G.; and Tuzhilin A. Context-aware recommender systems. In: Ricci F., Rokach L., Shapira B., Kantor P. (eds) Recommender Systems Handbook. Springer, Boston: MA, 2011, pp. 191–226.

2. Adomavicius, G.; and Tuzhilin, A. Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Transactions on Knowledge and Data Engineering, Dublin, Ireland, 17, 6 (2005), 734–749.

3. Amin, M.S.; Yan, B.; Sriram, S.; Bhasin, A.; and Posse, C. Social referral: Leveraging network connections to deliver recommendations. Proceedings of the Sixth ACM Conference on Recommender Systems. ACM, 2012, pp. 273–276.

4. Aral, S.; and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (2011), 1623-1639.

5. Archak, N.; Ghose, A.; and Ipeirotis, P.G. Deriving the pricing power of product features by mining consumer reviews. Management Science, 57, 8 (2011), 1485–1509.

6. Basu, A.K.; and Drew, M.E. Portfolio size effect in retirement accounts: What does it imply for lifecycle asset allocation funds? The Journal of Portfolio Management, 35, 3 (2009), 61–72.

7. Basu, A.K.; Byrne, A.; and Drew, M.E. Dynamic lifecycle strategies for target date retirement funds. The Journal of Portfolio Management, 37, 2 (2011), 83–96.

8. Beck, J.S. Cognitive Behavior Therapy: Basics and Beyond. New York, NY: Guilford Press, 2011.

9. Benartzi, S.; and Thaler, R.H. Behavioral economics and the retirement savings crisis. Science, 339, 6124 (2013), 1152–1153.

10. Benartzi, S.; and Thaler, R.H. Heuristics and biases in retirement savings behavior. The Journal of Economic Perspectives, 21, 3 (2007), 81–104.

11. Benartzi, S.; and Thaler, R.H. Risk aversion or myopia? Choices in repeated gambles and retirement investments. Management Science, 45, 3 (1999), 364–381.

12. Berinsky, A.J.; Huber, G.A.; and Lenz, G.S. Evaluating online labor markets for experimental research: Amazon. com’s Mechanical Turk. Political Analysis, 20, 3 (2012), 351–368.

13. Biggart, N.W.; and Hamilton, G.G. The power of obedience. Administrative Science Quarterly (1984), 29(4), 540–549.

14. Bonaccio, S.; and Dalal, R.S. Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences. Organizational Behavior and Human Decision Processes, 101, 2 (2006), 127–151.

15. Bourke, S.; McCarthy, K.; and Smyth, B. Power to the people: Exploring neighbourhood formations in social recommender system. Proceedings of the Fifth ACM Conference on Recommender Systems. Chicago, IL, USA: ACM, 2011, pp. 337–340.

16. Budescu, D.V.; and Chen, E. Identifying expertise to extract the wisdom of crowds. Management Science, 61, 2 (2014), 267–280.

17. Bursztyn, L.; Ederer, F.; Ferman, B.; and Yuchtman, N. Understanding mechanisms underlying peer effects: Evidence from a field experiment on financial decisions. Econometrica, 82, 4 (2014), 1273–1301.

18. Buser, T.; and Dreber, A. The flipside of comparative payment schemes. Management Science, 62, 9 (2015), 2626–2638.

19. Cacioppo, J. T.; and Petty, R.E. The Elaboration Likelihood Model of Persuasion. Advances in Consumer Research, 11, (1984), 673–675.

20. Chaiken, S. Heuristic versus systematic information processing and the use of source versus message cues in persuasion. Journal of Personality and Social Psychology, 39, 5 (1980), 752.

21. Chaiken, S.; and Eagly, A.H. Heuristic and systematic information processing within and. Unintended Thought, 212(1989), 212–252.

22. Chiu, C.-M.; Liang, T.-P.; and Turban, E. What can crowdsourcing do for decision support? Decision Support Systems, 65(2014), 40–49.

23. Cialdini, R. B. Influence: Science and Practice. Boston: Pearson Education, 2009.

24. Cialdini, R. B. Influence: The Psychology Of Persuasion. New York, NY: Collins. 1984

25. Clark, R.L.; and d’Ambrosio, M.B. Ignorance is not bliss: The importance of financial education. TIAA-CREF Research Dialogue, 78(2003), 1–14.

26. Clauson, K.A.; Polen, H.H.; Boulos, M.N.K.; and Dzenowagis, J.H. Scope, completeness, and accuracy of drug information in Wikipedia. Annals of Pharmacotherapy, 42, 12 (2008), 1814-1821.

27. Das, S.; Kramer, A.D.; Dabbish, L.A.; and Hong, J.I. The role of social influence in security feature adoption. Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing. ACM, 2015, pp. 1416–1426.

28. Dawes, R.M. The robust beauty of improper linear models in decision making. American Psychologist, 34, 7 (1979), 571.

29. Deutsch, M.; and Gerard, H.B. A study of normative and informational social influences upon individual judgment. The Journal of Abnormal and Social Psychology, 51, 3 (1955), 629.

30. Dietvorst, B.J.; Simmons, J.P.; and Massey, C. Overcoming algorithm aversion: People will use imperfect algorithms if they can (even slightly) modify them. Management Science, 64, 3 (2016), 1155–1170.

31. Edwards, C. Using patient data for personalized cancer treatments. Communications of the ACM, 57, 4 (2014), 13–15.

32. Ehrlich, K.; Kirk, S.E.; Patterson, J.; Rasmussen, J.C.; Ross, S.I.; and Gruen, D.M. Taking advice from intelligent systems: The double-edged sword of explanations. Proceedings of the 16th International Conference on Intelligent User Interfaces. BC, Canada: ACM, Vancouver; 2011, pp. 125–134.

33. Einarsen, S.; Aasland, M.S.; and Skogstad, A. Destructive leadership behaviour: A definition and conceptual model. The Leadership Quarterly, 18, 3 (2007), 207–216.

34. Evans, B.M.; Kairam, S.; and Pirolli, P. Do your friends make you smarter?: An analysis of social strategies in online information seeking. Information Processing & Management, 46, 6 (2010), 679–692.

35. Eysenbach, G.; Powell, J.; Englesakis, M.; Rizo, C.; and Stern, A. Health related virtual communities and electronic support groups: systematic review of the effects of online peer to peer interactions. BMJ, 328, 7449 (2004), 1166.

36. Faubion, B. Effect of Automated Advising Platforms on the Financial Advising Market. Accounting Theses University of Arkansas, 24, (2016).

37. Festinger, L. A theory of social comparison processes. Human Relations, 7, 2 (1954), 117–140.

38. Giles, J. Internet encyclopaedias go head to head. Nature Publishing Group, Palo Alto, CA, 2005.

39. Goldman, L.; Caldera, D.L.; Nussbaum, S.R.; Southwick, F.S.; Krogstad, D.; Murray, B.; Burke, D.S.; O’Malley, T.A.; Goroll, A.H.; and Caplan, C.H. Multifactorial index of cardiac risk in noncardiac surgical procedures. New England Journal of Medicine, 297, 16 (1977), 845–850.

40. Gunaratne, J.; and Nov, O. Influencing retirement saving behavior with expert advice and social comparison as persuasive techniques. International Conference on Persuasive Technology. London, UK: Springer; 2015, pp. 205–216.

41. Gunaratne, J.; and Nov, O. Informing and improving retirement saving performance using behavioral economics theory-driven user interfaces. Proceedings of the 33rd Annual

ACM Conference on Human Factors in Computing Systems. Chicago, IL: ACM; 2015, pp. 917–920.

42. Gunaratne, J.; Burke, J.; and Nov, O. Empowering investors with social annotation when saving for retirement. Proceedings of the ACM SIGCHI Conference on Computer Supported Cooperative Work, Portland, OR, 2017.

43. Hardin, A.; Looney, C.A.; and Moody, G.D. Assessing the credibility of decisional guidance delivered by information systems. Journal of Management Information Systems, 34, 4 (2017), 1143–1168.

44. Hedén, B.; Öhlin, H.; Rittner, R.; and Edenbrandt, L. Acute myocardial infarction detected in the 12-lead ECG by artificial neural networks. Circulation, 96, 6 (1997), 1798-1802.

45. Hershey, D.A.; Jacobs-Lawson, J.M.; McArdle, J.J.; and Hamagami, F. Psychological foundations of financial planning for retirement. Journal of Adult Development, 14, 1–2 (2007), 26–36.

46. Hill, S.; and Ready-Campbell, N. Expert stock picker: The wisdom of (experts in) crowds. International Journal of Electronic Commerce, 15, 3 (2011), 73–102.

47. Horton, J.J. The condition of the Turking class: Are online employers fair and honest?. Economics Letters, 111, 1 (2011), 10–12.

48. Horton, J.J.; Rand, D.G.; and Zeckhauser, R.J. The online laboratory: Conducting experiments in a real labor market. Experimental Economics, 14, 3 (2011), 399–425.

49. Hovland, C.I.; and Weiss, W. The influence of source credibility on communication effectiveness. Public Opinion Quarterly, 15, 4 (1951), 635–650.

50. Huang, J.; Boh, W.F.; and Goh, K.H. A Temporal study of the effects of online opinions: Information sources matter. Journal of Management Information Systems, 34, 4 (2017), 1169–1202.

51. Jannach, D.; Resnick, P.; Tuzhilin, A.; and Zanker, M. Recommender systems—: beyond matrix completion. Communications of the ACM, 59, 11 (2016), 94–102.

52. Jiang, J.; Klein, G.; and Vedder, R. Persuasive expert systems: The influence of confidence and discrepancy. Computers in Human Behavior, 16, 2 (2000), 99–109.

53. Jordan, M.; and Mitchell, T. Machine learning: Trends, perspectives, and prospects. Science, 349, 6245 (2015), 255–260.

54. Jowett, G.S.; and O’Donnell, V. Propaganda & Persuasion. Thousand Oaks, CA; Sage; 2014.

55. Kahneman, D.; and Tversky, A. Prospect theory: An analysis of decision under risk. Econometrica: Journal of the Econometric Society, 47, 2(1979) 263–291.

56. Kahneman, D.; Knetsch, J.L.; and Thaler, R.H. Anomalies: The endowment effect, loss aversion, and status quo bias. The Journal of Economic Perspectives, 5, 1 (1991), 193–206.

57. Kaufmann, C.; Weber, M.; and Haisley, E. The role of experience sampling and graphical displays on one’s investment risk appetite. Management Science, 59, 2 (2013), 323–340.

58. Kittur, A.; and Kraut, R.E. Harnessing the wisdom of crowds in Wikipedia: Quality through coordination. Proceedings of the 2008 ACM Conference on Computer Supported Cooperative Work. San Diego, CA; ACM; 2008, pp. 37–46.

59. Kozinets, R.V.; Hemetsberger, A.; and Schau, H.J. The wisdom of consumer crowds: Collective innovation in the age of networked marketing. Journal of Macromarketing, 28, 4 (2008), 339–354.

60. Kraut, R.E.; Rice, R.E.; Cool, C.; and Fish, R.S. Varieties of social influence: The role of utility and norms in the success of a new communication medium. Organization Science, 9, 4 (1998), 437–453.

61. Kulkarni, C.; and Chi, E. All the News that’s Fit to Read: A Study of Social Annotations for News Reading. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Paris, France: ACM; 2013, pp. 2407–2416.

62. Larrick, R.P.; and Soll, J.B. Intuitions about combining opinions: Misappreciation of the averaging principle. Management Science, 52, 1 (2006), 111–127.

63. Larrick, R.P.; Mannes, A.E.; Soll, J.B.; and Krueger, J. The social psychology of the wisdom of crowds. Social Psychology and Decision Making (2011), 227–242.

64. Lelis, S.; and Howes, A. Informing decisions: How people use online rating information to make choices. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. ACM, Vancouver, BC: Canada, 2011, pp. 2285–2294.

65. Li, C.-Y. Persuasive messages on information system acceptance: A theoretical extension of elaboration likelihood model and social influence theory. Computers in Human Behavior, 29, 1 (2013), 264–275.

66. Lieber, R. Financial advice for people who aren’t rich. The New York Times (2014). April 12, 2014, page B1.

67. Liu, D.; Brass, D.; Lu, Y.; and Chen, D. Friendships in online peer-to-peer lending: Pipes, prisms, and relational herding. MIS Quarterly, 39, 3 (2015), 729–742.

68. Lorenz, J.; Rauhut, H.; Schweitzer, F.; and Helbing, D. How social influence can undermine the wisdom of crowd effect. Proceedings of the National Academy of Sciences, 108, 22 (2011), 9020–9025.

69. Lusardi, A.; and Mitchell, O.S. Financial literacy and Planning: Implications for Retirement Wellbeing. Cambridge, MA: National Bureau of Economic Research; 2011.

70. Malkiel, B.G. A random walk down Wall Street: The Time-tested Strategy for Successful Investing. New York, NY: WW Norton & Company; 2007.

71. Mannes, A.E. Are we wise about the wisdom of crowds? The use of group judgments in belief revision. Management Science, 55, 8 (2009), 1267–1279.

72. Maurer, R.; Mitchell, O.S.; Rogalla, R.; and Kartashov, V. Lifecycle portfolio choice with systematic longevity risk and variable investment—Linked deferred annuities. Journal of Risk and Insurance, 80, 3 (2013), 649–676.

73. Mazar, N.; Shampanier, K.; and Ariely, D. When retailing and Las Vegas meet: Probabilistic free price promotions. Management Science, 63, 1 (2016), 250–266.

74. Merton, R.C. Lifetime portfolio selection under uncertainty: The continuous-time case. The Review of Economics and Statistics, 51, 3(1969), 247–257.

75. Merton, R.C. The crisis in retirement planning. Harvard Business Review, 92, 7/8 (2014), 43–50.

76. Milgram, S. Behavioral Study of obedience. The Journal of Abnormal and Social Psychology, 67, 4 (1963), 371–378.

77. Milkman, K.L.; Minson, J.A.; and Volpp, K.G. Holding the Hunger Games hostage at the gym: An evaluation of temptation bundling. Management Science, 60, 2 (2013), 283–299.

78. Mitchell, O.S.; and Utkus, S. Target-date Funds in 401(k) Retirement Plans. Cambridge, MA: National Bureau of Economic Research; 2012.

79. Mollick, E.; and Nanda, R. Wisdom or madness? Comparing crowds with expert evaluation in funding the arts. Management Science, 62, 6 (2015), 1533–1553.

80. Mullainathan, S.; Noeth, M.; and Schoar, A. The Market for Financial Advice: An Audit Study. Cambridge, MA: National Bureau of Economic Research; 2012.

81. Munson, S.A.; and Resnick, P. Presenting diverse political opinions: How and how much. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Atlanta, GA: ACM; 2010, pp. 1457–1466.

82. Muralidharan, A.; Gyongyi, Z.; and Chi, E. Social annotations in web search. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Austin, TX: ACM; 2012, pp. 1085–1094.

83. Nass, C.; and Moon, Y. Machines and mindlessness: Social responses to computers. Journal of Social Issues, 56, 1 (2000), 81–103.

84. Nass, C.; Steuer, J.; and Tauber, E.R. Computers are Social Actors. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Boston, MA: ACM; 1994, pp. 72–78.

85. Nelson, L.; Held, C.; Pirolli, P.; Hong, L.; Schiano, D.; and Chi, E.H. With a little help from my friends: Examining the impact of social annotations in sensemaking tasks. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems. Boston, MA: ACM; 2009, pp. 1795–1798.

86. Nov, O.; and Arazy, O. Asymmetric recommendations: The interacting effects of social ratings? Direction and strength on users’ ratings. Proceedings of the 9th ACM Conference on Recommender Systems. Vienna, Austria: ACM; 2015, pp. 249–252.

87. Önkal, D.; Goodwin, P.; Thomson, M.; Gönül, S.; and Pollock, A. The relative influence of advice from human experts and statistical methods on forecast adjustments. Journal of Behavioral Decision Making, 22, 4 (2009), 390–409.

88. Paolacci, G.; Chandler, J.; and Ipeirotis, P.G. Running experiments on amazon mechanical turk. Judgment and Decision Making, 5, 5 (2010), 411–419.

89. Pelster, M.; and Breitmayer, B. Swarm Intelligence? Stock Opinions of the Crowd and Stock Returns.Rochester, NY: SSRN; 2016.

90. Petty, R.E.; and Cacioppo, J.T. Issue involvement can increase or decrease persuasion by enhancing message-relevant cognitive responses. Journal of Personality and Social Psychology, 37, 10 (1979), 1915.

91. Petty, R.E.; and Cacioppo, J.T. The elaboration likelihood model of persuasion. Advances in Experimental Social Psychology, 19(1986), 123–205.

92. Pfau, W.D. Lifecycle funds and wealth accumulation for retirement: Evidence for a more conservative asset allocation as retirement approaches. Financial Services Review, 19, 1 (2009), 59–74.

93. Pornpitakpan, C. The persuasiveness of source credibility: A critical review of five decades’ evidence. Journal of Applied Social Psychology, 34, 2 (2004), 243–281.

94. Poterba, J.; Rauh, J.; Venti, S.; and Wise, D. Lifecycle Asset Allocation Strategies and the Distribution of 401(k) Retirement Wealth. Chicago, IL: National Bureau of Economic Research; 2006.

95. Provost, F.; and Fawcett, T. Data science and its relationship to big data and data-driven decision making. Big Data, 1, 1 (2013), 51–59.

96. Rajagopalan, M.S.; Khanna, V.K.; Leiter, Y.; Stott, M.; Showalter, T.N.; Dicker, A.P.; and Lawrence, Y.R. Patient-oriented cancer information on the internet: A comparison of Wikipedia and a professionally maintained database. Journal of Oncology Practice, 7, 5 (2011), 319–323.

97. Ray, R. Prediction markets and the financial “wisdom of crowds.” The Journal of Behavioral Finance, 7, 1 (2006), 2–4.

98. Salganik, M.J.; Dodds, P.S.; and Watts, D.J. Experimental study of inequality and unpredictability in an artificial cultural market. Science, 311, 5762 (2006), 854–856.

99. Securities Exchange Commission. Invest Wisely: An Introduction to Mutual Funds. Washington, DC: Securities Exchange Commission; 2008.

100. Stewart, K.J. How hypertext links influence consumer perceptions to build and degrade trust online. Journal of Management Information Systems, 23, 1 (2006), 183–210.

101. Surowiecki, J. The Wisdom of Crowds: Why the Many are Smarter than the Few and How Collective Wisdom Shapes Business. New York, NY: Knopf Doubleday Publishing Group, 2005.

102. Surz, R.J.; and Israelsen, C.L. Evaluating target date lifecycle funds. Journal of Performance Measurement, 12, 2 (2008), 62–70.

103. Tazelaar, F.; and Snijders, C. Operational risk assessments by supply chain professionals: Process and performance. Journal of Operations Management, 31, 1 (2013), 37–51.

104. Tenney, E.R.; MacCoun, R.J.; Spellman, B.A.; and Hastie, R. Calibration trumps confidence as a basis for witness credibility. Psychological Science, 18, 1 (2007), 46–50.

105. Tenney, E.R.; Spellman, B.A.; and MacCoun, R.J. The benefits of knowing what you know (and what you don’t): How calibration affects credibility. Journal of Experimental Social Psychology, 44, 5 (2008), 1368–1375.

106. Tesauro, G.; Gondek, D.; Lenchner, J.; Fan, J.; and Prager, J.M. Analysis of watson’s strategies for playing Jeopardy! Journal of Artificial Intelligence Research, 47(2013), 205–251.

107. Tetlock, P. Expert Political Judgment: How Good is It? How Can We Know?: Princeton, NJ: Princeton University Press; 2005.

108. Thaler, R.H.; and Sunstein, C.R. Nudge: Improving Decisions About Health, Wealth, and Happiness. New Haven, CT: Yale University Press; 2008.

109. Thaler, R.; and Benartzi, S. The Behavorial Economics of Retirement Savings Behavior. Washington, DC: AARP, Public Policy Institute; 2007.

110. Tseng, S.; and Fogg, B. Credibility and computing technology. Communications of the ACM, 42, 5 (1999), 39–44.

111. Tyler, T.R.; and Lind, E.A. A relational model of authority in groups. Advances in Experimental Social Psychology, 25(1992), 115–191.

112. Van Thiel, D.; and Van Raaij, F. Explaining customer experience of digital financial advice. Economics, 5, 1 (2017), 69–84.

113. Wang, W.; and Benbasat, I. Empirical assessment of alternative designs for enhancing different types of trusting beliefs in online recommendation agents. Journal of Management Information Systems, 33, 3 (2016), 744–775.

114. Wang, W.; and Benbasat, I. Recommendation agents for electronic commerce: Effects of explanation facilities on trusting beliefs. Journal of Management Information Systems, 23, 4 (2007), 217–246.

115. Yaniv, I.; and Kleinberger, E. Advice taking in decision making: Egocentric discounting and reputation formation. Organizational Behavior and Human Decision Processes, 83, 2 (2000), 260–281.

116. Ye, L.R.; and Johnson, P.E. The impact of explanation facilities on user acceptance of expert systems advice. MIS Quarterly, 19, 2 (1995), 157–172.

117. Ye, M.; Liu, X.; and Lee, W.-C. Exploring social influence for recommendation: A generative model approach. Proceedings of the 35th International ACM SIGIR Conference on Research and Development in Information Retrieval. Portland, OR: ACM; 2012, pp. 671–680.

118. Yum, H.; Lee, B.; and Chae, M. From the wisdom of crowds to my own judgment in microfinance through online peer-to-peer lending platforms. Electronic Commerce Research and Applications, 11, 5 (2012), 469–483.

119. Zhao, J.C.; Fu, W.-T.; Zhang, H.; Zhao, S.; and Duh, H. To risk or not to risk?: Improving financial risk taking of older adults by online social information. Proceedings of the 18th ACM Conference on Computer Supported Cooperative Work & Social Computing. Vancouver, BC, Canada: ACM, 2015, pp. 95–104.

120. Zhu, H.; and Huberman, B.A. To switch or not to switch: Understanding social influence in online choices. American Behavioral Scientist, 58, 10 (2014), 1329–1344.
