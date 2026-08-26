---
otero_id: 4446
otero_key: "XYB75NV6"
title: "Prediction Markets as institutional forecasting support systems"
authors: "Gerrit H. Van Bruggen; Martin Spann; Gary L. Lilien; Bernd Skiera"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.05.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Prediction Markets as institutional forecasting support systems

Gerrit H. Van Bruggen <sup>a,</sup>⁎, Martin Spann <sup>b,1</sup>, Gary L. Lilien <sup>c,2</sup>, Bernd Skiera <sup>d,3</sup>

<sup>a</sup> Rotterdam School of Management, Erasmus University, P.O. Box 1738, 3000 DR Rotterdam, The Netherlands

<sup>b</sup> Ludwig-Maximilians-University (LMU), Geschwister-Scholl-Platz 1, 80539 Munich, Germany

<sup>c</sup> Penn State, 484 Business Building, University Park, PA 16803, USA

<sup>d</sup> Goethe-University Frankfurt, Grüneburgplatz 1, 60323 Frankfurt am Main, Germany

## a r t i c l e i n f o

Article history: Received 16 June 2009 Received in revised form 29 April 2010 Accepted 6 May 2010 Available online 13 May 2010

Keywords: Prediction Markets Institutional forecasting

## a b s t r a c t

An attractive feature of Prediction Markets (PMs) is that they provide economic incentives for informants to share unique information. It is unclear whether PMs are appropriate for applications with few knowledgeable informants as is the case for most institutional forecasting tasks. Hence, we compare the performance of small PMs with traditional judgment-based forecasting approaches. Our results show that forecasts from small PMs outperform traditional approaches in settings of high information-heterogeneity (i.e., where the amount of unique information possessed by informants is relatively high) and are no worse in settings of low information-heterogeneity.

© 2010 Elsevier B.V. All rights reserved

## 1. Introduction

One of the most challenging tasks <sup>fi</sup>rms face is to make the most effective use of their extant internal information. That challenge applies especially to forecasting, which the forecasting literature (see [18], for example) describes as both “art and science”, with “art” referring to forms of managerial judgment and the “science” referring to statistical or econometric analysis based on historical data. But forecasts in organizations are often required in situations where there are no data-based approaches available. Furthermore, cost or secrecy concerns often preclude customer surveys as data sources for such forecasts. Hence, many organizations rely on informants (sales representatives, research analysts, business managers and project team members) for the development of (judgment-based) forecasts [20], what we will refer to here as “institutional forecasting.”

Forecast accuracy is often improved when informant-based forecasts rely on multiple rather than a single informant because (a) informants seldom have access to all relevant information and (b) using multiple informants lowers the error component of the group's forecast [3]. Group discussion enables informants to share information so that groups can access a larger pool of information than can any single informant acting alone [14,43]. However, research has also shown that groups are sometimes ineffective at exchanging information [32] and that much unique information known to a single or only some individuals is never shared with the group [48].

Stasser and Titus [49] claim that groups can bene<sup>fi</sup>t from pooling members' information, particularly when members individually have partial and biased information but collectively can compose a less biased characterization of the decision alternatives. However, in an empirical application of their approach they <sup>fi</sup>nd that group members often fail to effectively pool their information because discussion is dominated by commonly held information and information that supports members' existent viewpoints. This result implies that groups that share information interactively through group discussion will normally reach consensus but will neither appropriately correct for nor effectively pool members' complementary expertise and knowledge.

The increasing ease of interconnectivity and the proliferation of web conferencing tools like LiveMeeting and GotoMeeting are continually making it simpler for groups of people to work together through computer networks. A Group Forecasting Support System within such an environment is a communication and coordination process that structures the process of communication and information sharing. Dennis [14] studied the bene<sup>fi</sup>ts of Group Support Systems (GSSs) and found that groups using a GSS exchanged 50% more information than verbally interacting groups, permitting them to include the best alternative amongst those considered for selection. However, he also found that very few groups ended up selecting the optimal decision, indicating that the GSS was not able to help the groups to process the information that they had optimally. Sia et al. [44] report that anonymous or dispersed computer-mediated communication settings are required for group discussion to lead to the strong polarization that may be necessary to identify a non-consensus choice.

Prediction Markets (PMs), also called information markets or virtual stock markets, represent an information technology based forecasting platform that may have the potential to address some of the challenges that traditional GSS's face in the institutional forecasting context. PMs enable informants to exchange information and should be considered as a type of organizational Group Forecasting Support System (GFSS). However, unlike traditional Group Support Systems [14,16], PMs place an incentive on exchanging “unique” information with other informants in the market because doing so will lead to higher pay-offs for the informant possessing such unique information.

PMs have been successfully applied to predict election outcomes (e.g., the Iowa Electronic Markets [7]), the success of movies and impact of stars (e.g., the Hollywood Stock Exchange [17,22,38]), sports results [47], product concepts and new product ideas [12,45]; and future economic outcomes (e.g., economicderivatives.com). In an inter-organizational setting Guo et al. [30] propose a Prediction Market for information sharing within supply chains. LaComb et al. [34] report that several GE businesses experimented with PMs to support idea generation and group-decision making. Ostrover [36] cites several PM applications in organizations: e.g. Hewlett Packard (HP) uses PMs to forecast sales, <sup>fi</sup>nancial, and accounting results while Eli Lilly uses a PM to identify those drugs in the early stages of development most likely to win US Federal Drug Administration approval. The results of these applications demonstrate the potential value of the PM approach for institutional forecasting in settings with a large number of participants. However, little work has been reported on PMs in settings with few knowledgeable participants; indeed, scholars have stressed that such situations can lead to markets with low liquidity where small changes in supply and/or demand can have a large impact on market prices [23]. Research on traditional GSSs [24] suggests that these systems are also much more effective for larger groups, Yet, many practical institutional forecasting situations actually involve relatively few (knowledgeable) informants, which underlines the need for approaches that are effective for small groups.

Spann and Skiera [46] report a study of a (single) small PM with twelve employees at a large German mobile phone operator to forecast the usage of <sup>fi</sup>ve different mobile phone services in a speci<sup>fi</sup>c month. The PM showed better forecasting accuracy than several competing model-based forecasting approaches. The authors suggest that as the heterogeneity in market informants' knowledge increases, the PM's forecasting error declines relative to other approaches. If this suggestion is correct, it implies that small PMs can be effective in general and may do especially well relative to alternatives if the informants possess relatively large amounts of “unique” or “partially shared” information [14].

Our objective in this paper is to analyze whether the forecasting accuracy observed for PMs in other settings applies to forecasting settings with few knowledgeable informants. We consider whether, why and when small PMs are likely to outperform more traditional judgment-based approaches towards institutional forecasting [33], which we call the Combined Judgmental Forecasts (CJF) approach, or the Key Informant (KI) approach. We compare the accuracy of the PM approach with these alternatives for several forecasting tasks (i.e., forecasting the future value of two <sup>fi</sup>nancial indices and forecasting the point spread of two college football games).

Our results show that the PM approach performs at least as well as these alternatives in markets with few participants. We <sup>fi</sup>nd that for tasks we characterize as high in information-heterogeneity (i.e., predicting football point spreads), forecasts made through the PM approach are more accurate than those developed by the CJF approach or by the KI approach, while for low information-heterogeneity tasks (i.e., predicting <sup>fi</sup>nancial indices), we <sup>fi</sup>nd that the PM approach performs no worse than the other approaches.

The paper proceeds as follows: we <sup>fi</sup>rst review alternative approaches to support institutional forecasting, including the opportunities afforded by the PM approach. Then we review literature on how PMs operate and how their operation may be affected by the number of market informants. We contrast the differences between the PM approach and the more traditional approaches (CJF or KI), which leads to our hypothesis about the expected differences in forecasting accuracy between those three approaches. We next describe the design of our empirical study and present our results. We conclude with a discussion of those results and their implications.

## 2. Review of institutional forecasting approaches

We review the most commonly used approaches to (institutional) forecasting—the (single) key informant and multiple informants approaches. We then compare them with the PM approach.

Key Informant (KI) approach. Perhaps the most widely used approach in practice because of its simplicity is the key informant approach, where a single informant is most often selected because of knowledge and willingness to communicate that knowledge. This approach suffers from signi<sup>fi</sup>cant drawbacks [33], including bias, random error, and the inability to aggregate information spread across multiple informants. Armstrong [3] summarizes much research that shows that single informant reports are systematically outperformed by those of multiple informants when their reports are appropriately combined.

Multiple Informant approaches combine knowledge of multiple informants into an overall forecast. The strategies to combine the information of multiple informants differ depending upon whether or not the informants interact and are able to exchange information.

Mechanistic Aggregation—Combined Judgmental Forecasts (CJF) approaches. CJF algorithms such as forming simple or weighted averages are used when informants do not interact and do not exchange information [25]. Rather, all informants produce forecasts that are then mathematically combined into a single group forecast. Van Bruggen et al. [56] propose methods for improving weighted averages, showing that the use of con<sup>fi</sup>dence and competence scores as weights improves forecasting accuracy. Yet, the mechanistic, mathematical approach can lead to a form of double counting of expertise if the knowledge of various experts overlaps substantially. In addition, and by de<sup>fi</sup>nition, the approach prevents informants from sharing information to learn from one another [25].

Behavioral or Interactive Aggregation permits informants to interact and share information [25] and most existing GSSs are designed to facilitate such processes. Approaches differ and depend on whether the sharing is synchronous or asynchronous, if the respondents are anonymous or not and if the informants interact verbally or are supported through Group Support Systems [14–16,32,44]. All forms of behavioral aggregation can lead to dif<sup>fi</sup>culties in reaching consensus and even if they reach consensus, this consensus may be driven by power and personality rather than by knowledge, perhaps explaining the GSS decision biases cited earlier. Garthwaite et al. [25] and Kumar et al. [33] discuss the in<sup>fl</sup>uence of censorship, Groupthink, and the dif<sup>fi</sup>culty of organizing and facilitating the needed interactions on forecasting accuracy.

To sharpen our focus and to align our work with practice, we study the (online) survey-based CJF approach and the key informant (KI) approach, a special case of the CJF approach with 100% weight on the key informant. In our survey-based CJF approach, informants do not interact and their individual forecasts are combined mathematically.

The Prediction Markets (PM) approach. The PM approach creates information markets, bringing groups of informants together over electronic communication networks such as the Internet and allowing them to trade shares of virtual stocks that represent a bet on the outcome of a future market situation. They collect, disseminate, and aggregate information that may be widely dispersed across a number of public and private sources, through the mechanism of trading [39,53]. Public information is information that informants have in common or shared while private information is unique to informants and unshared [14,49,50]. The ability of markets to re<sup>fl</sup>ect public as well as private information is referred to as their informational ef<sup>fi</sup>ciency [19].

Effective PMs satisfy three criteria [57]: they provide i) incentives to seek information; ii) incentives for truthful information revelation; and iii) an algorithm for aggregating diverse opinions of their informants. Ostrover [36] cites <sup>fi</sup>ve reasons why the PM approach should be expected to work: i) participation: everyone with access to relevant information can contribute; ii) motivation: a properly designed reward mechanism incents informants to acquire relevant information and reveal their expectations [21]; iii) anonymity: PMs eliminate fear of reprisal for revealing unpopular expectations; iv) coordination: markets provide a natural mechanism for active group interplay; and v) computation: markets provide a natural aggregation mechanism.

The question we address here is how well the Prediction Market approach supports institutional forecasting when the number of (trading) informants is relatively small. In a study on a GSS that supported electronic brainstorming Gallupe et al. [24] found these systems to be less effective for smaller groups. For the PM approach a similar effect may be present. When there are few (active) traders and, hence, few trades, bid-and-ask prices often differ widely [23]. Several researchers have addressed the question of whether and how market size affects market ef<sup>fi</sup>ciency. In small markets, problems like information traps, manipulation and lack of equilibrium have been found to be exacerbated [10], information cascades may occur [1] and the market may not be information-ef<sup>fi</sup>cient [46,52]. While a few researchers have demonstrated that small markets often do quite well [23], in general larger markets are reported to perform better. When markets attract broad participation, prices encode all the disparate information of these informants [37] and there is most likely more information encoded in the market price than with fewer informants. In an absolute sense PMs with a larger number of traders will be better informed and thereby produce more accurate forecasts than those with fewer traders. Furthermore, a low trading volume makes it dif<sup>fi</sup>cult for markets to react to new information that may not be easily accessible to the few active traders [4]. Yet, with the possible exception of Gruca et al. [29], which differs signi<sup>fi</sup>cantly in design from ours, there are no studies that empirically compare the forecasts of the PM approach with those of the CJF approaches in settings like those we focus on here.

## 3. The Prediction Markets (PM) approach versus the Combined Judgmental Forecasts (CJF) approach: hypothesis development

To guide our hypothesis development, we compare the PM approach and the CJF approach along three key information dimensions: i) information collection; ii) information dissemination (i.e. broadcasting); and iii) information aggregation. This taxonomy (see Table 1) is based on the three functions of markets distinguished by Plott [39] and describes the activities performed when informant based forecasts are being developed.

Information collection is the process of eliciting individuals' forecasts. In the CJF approach, informants provide direct forecasts for the variables of interest and, sometimes, information about their con<sup>fi</sup>dence and competence. This approach is straightforward and (relatively) easy for informants. A weakness is that the judgments in these settings may be based on a limited number of mental operations, which potentially lead to biased assessments [25]. This weakness may also apply for con<sup>fi</sup>dence and competence assessments. Furthermore, reasons may exist for informants not to disclose information honestly [33].

With the PM approach, informants' information is collected indirectly through their trading behavior. Furthermore, informants in the PM approach use the actual market price compared to their expectation and trade accordingly. This action (i.e., buy shares if price is considered too low or sell when too high) may be easier than generating a full personal estimate as is needed in the CJF and the KI approaches. The PM approach provides anonymity and incentives for informants to reveal their true expectations [36,46]. However, the market mechanism may also provide incentives for speculation, and trading in an information market may not be easily understandable for all informants [51]. Hence, both approaches have advantages and disadvantages on the dimension of information collection.

Information dissemination refers to the ability of a method to broadcast unique information held by better informed informants to less well informed informants [39,53]. Informants base their responses in the CJF approach and their trading behavior in PMs on the public and private information they possess, where the latter information is unique to or held by a speci<sup>fi</sup>c informant [9]. In the CJF approach, which collects information from each informant independently, informants provide their forecasts based on public and private information, but informants cannot re-evaluate their opinion in light of the opinion of others.

In PMs the process of trading is dynamic and market feedback may make informants re-assess and update their initial forecasts, leading to changes in the collective forecast [39]. In PMs, groups of informants trade shares of virtual stocks that represent bets on the outcome of future (market) situations, where their value depends on the realization of these market situations. Once the outcome of a market situation is known, each share receives a payoff according to that outcome. The price of a share of a virtual stock corresponds to the PM's current, aggregate expectation of the event's outcome and, therefore, to the expected payoff of a share of the stock. If an individual's assessment of the outcome of a future event is different from the market's assessment it will be pro<sup>fi</sup>table to either buy or sell. By these trading activities informants will reveal the private/unique information they possess because the market provides incentives to reveal unique information. In equilibrium, price summarizes all the relevant information the traders have [26,31]. The core service the market provides is thus to facilitate the exchange of items or, in this case, information between individuals [38]. The theory of rational expectations posits that prices re<sup>fl</sup>ect the total of all information available to all market informants. Even when some agents have exclusive access to inside (unique) information, prices equilibrate as if everyone had access to all information [27]. Through the market, previously unshared information will thus be shared and become common information.

Comparison of main information characteristics of the Prediction Market (PM) and the Combined Judgmental Forecasts (CJF) approaches to institutional forecasting.

<table><tr><td></td><td>Combined Judgmental Forecasts</td><td>Prediction Markets</td></tr><tr><td colspan="3">Information collection</td></tr><tr><td>• About forecasted variable</td><td>• Direct and explicit measurement of variables of interest• Information available to each informant• Incentives for providing biased information may be present• Direct (self)assessments of knowledge and/or confidence</td><td>• Indirect measurement of variables of interest through observation of trading behavior• Information provided not directly visible• Incentives for speculation may be present</td></tr><tr><td>• About knowledge and confidence</td><td>• Providing responses is straightforward and relatively easy for informants</td><td>• No direct assessment of knowledge and/or confidence• Market participation can be relatively complex for informants</td></tr><tr><td>Information dissemination</td><td>• Only public information is shared and information of each informant is not broadcasted to other informants</td><td>• Private information of each informant becomes public through trading and is thereby broadcasted through the market mechanism</td></tr><tr><td>Information aggregation</td><td>• Aggregation explicitly done by the researcher• Various alternative (mostly proportional) weighting schemes can be applied• Knowledge-based weighting possible</td><td>• Aggregation implicitly done through market mechanism• Disproportional weighting of the input of the strongest believer</td></tr></table>

Note: The Key Information approach, a special case of Combined Judgmental Forecasts, shares the Combined Judgmental Forecasts characteristics for Information Collection while Information Broadcasting (i.e. Information Dissemination) and Information Aggregation considerations do not apply.

Markets can thus aggregate and disseminate information, but that capacity may not be perfect [39]: the wisdom of crowds is sometimes the ignorance of crowds [54]. For example, Anderson and Holt [1] describe the risk of information cascades, where individuals overweight private information of other traders that has become public during the trading process and underweight their own, possibly higher quality, private information—“I guess they know something I don't.” Or the information that is exchanged may be biased. However, Malkiel [35] concludes that such market imperfections are exceptions rather than the rule and the market can generally be trusted.

To summarize, in PMs, the price system makes information publicly available and thereby transfers it from informed to uninformed traders [28]; when the informants as a group are wise, that information exchange process is an advantage the PM approach holds over the CJF approach where information cannot be exchanged between informants.

Information aggregation is the procedure that combines the informants' forecasts to arrive at a single forecast. With the CJF approach, the researcher does the aggregation, employing either a simple unweighted average or some more advanced form of weighted average [10,56]. While these weighting approaches make the aggregation rule transparent, their weaknesses include the possible double-counting of informants whose knowledge is highly correlated as well as the logical problem of averaging two (or more) widely divergent views, based on totally different assumptions.

A PM simultaneously performs information aggregation, dissemination, and con<sup>fl</sup>ict resolution [41]: the market mechanism performs the weighting procedure. This approach is ef<sup>fi</sup>cient and, according to the “crystal ball” hypothesis [40], the market equilibrium may re<sup>fl</sup>ect even more information than the sum of what is available to individual traders. A possible weakness of the PM approach is that trading will be based on the strengths of expectations of traders and these expectations are not necessarily (fully) in line with reality [51]. However according to Berg and Rietz [8] markets aggregate diverse information in ways that prove more ef<sup>fi</sup>cient than alternative methods.

Prediction Markets can thus use the repeated interactions between informants to produce common forecasts that combine available information, avoiding the problem of weighting different expectations. No knowledge of who is more expert on what topics is required: market traders self-select to focus on the topics where they believe they are most expert in and those who are mistaken are punished by the market.

Table 1, summarizing the discussion above, shows that information dissemination is the most discriminating feature between these approaches, suggesting that the PM approach has the potential to produce more accurate forecasts than the CJF approach at least under some conditions.

Hence, using multiple informants to develop forecasts has two types of bene<sup>fi</sup>ts. First combining the inputs from multiple forecasters can reduce the random error component in the forecast, improving forecasting accuracy [3,5]. Both the PM approach and the CJF approach bene<sup>fi</sup>t from using multiple informants. Second, and probably more important, more people will know more and access more heterogeneous information. Spann and Skiera [46] suggest that such information-heterogeneity may have a positive impact on the accuracy of PM forecasts. According to Sunder [53], asymmetry of information among traders is an essential ingredient for prices to play an informational role and, thus, for markets to perform. Hence, the information dissemination feature of a PM is especially bene<sup>fi</sup>cial if signi<sup>fi</sup>cant information-asymmetry exists between informants, permitting individual (private) knowledge to become public and allowing less knowledgeable informants to update and improve their knowledge. The resulting higher average knowledge level of the informants can then be expected to increase the accuracy of the aggregated forecast.

Thus, we hypothesize that since the market allows for the dissemination of information through the pricing mechanism, the accuracy in forecasting for the PM approach should be equal to or exceed the accuracy of the most knowledgeable informant (I), i.e.,

$$
\text { Accuracy   of   Group } (P M) \geq \left(\text { Accuracy } I _ {1}, \text { Accuracy } I _ {2, \dots} \text { Accuracy } I _ {n}\right),
$$

while for the CJF approach, by de<sup>fi</sup>nition

Accuracy of Group CJF ∼

$$
(W e i g h t e d) M e a n \left(A c c u r a c y I _ {1}, A c c u r a c y I _ {2,..} A c c u r a c y I _ {n}\right).
$$

Following our argument, the PM approach should strictly outperform the CJF approach, since the PM approach permit sharing of information while the CJF approach does not. According to the information aggregation hypothesis of rational expectations, the prices should re<sup>fl</sup>ect available information [39]. Hence the PM approach should do no worse than the CJF approach in all cases and should signi<sup>fi</sup>cantly outperform the CJF approach in situations of high information-heterogeneity under any weighting scheme. We thus posit that information sharing and exchange should lead to improved forecasts (i.e., the PM approach should outperform the CJF approach) if there is a difference in knowledge between informants, that is, if different informants' information is not perfectly correlated [5]. The fact that a PM is small as such will not make it perform worse than the CJF approach as market size affects the CJF approach as well.

As the Key Informant (KI) approach is a special case of the CJF approach, with all weight given to the speci<sup>fi</sup>c key informant, the discussion above about the CJF approach applies for the KI approach as well. However, as the KI approach discards information from the nonkey informants (who will still possess some “part of the puzzle”), we expect that the KI approach will perform more poorly than both the PM approach and the CJF approach. Formally:

H1. The PM approach will outperform the CJF approach in terms of forecasting accuracy while the CJF approach will outperform the KI approach in terms of forecasting accuracy.

There will likely be conditions that moderate the effect hypothesized in H . We suggest that the amount of information-heterogeneity is such a moderator. Information-heterogeneity refers to the variations in knowledge, know-how, information and expertise which a group of forecasters can tap [42]. A low information-heterogeneity situation occurs when informants have access to similar (common) information. Regular, regional sales forecasts based on the judgments of a group of sales representatives represent an example of such an institutional setting. A high information-heterogeneity situation occurs when there is little common information and informants differ signi<sup>fi</sup>cantly in the type and quality of information and knowledge they possess. Informants in organizations frequently operate at different hierarchical levels, in different departments, and in different geographical areas. Hence, information and knowledge will often be dispersed across the organization and many informants will possess a substantial amount of unique information. A forecast of the market performance of a new product by the various people (e.g., marketing, R&D, sales) involved in developing it provides an example.

Information-heterogeneity thus refers to the variety of knowledge, know-how, information and expertise to which a group of forecasters has access [42] and in general, greater information-heterogeneity can be expected to have advantageous effects [5,42] on the effectiveness of the PM approach. The market mechanism in the PM approach will transfer information from knowledgeable and informed informants to less knowledgeable and uninformed informants. This transfer will increase the overall, average knowledge level among informants. Since in the CJF approach there is no exchange of information between informants this approach will bene<sup>fi</sup>t less from informationheterogeneity. Hence:

H2. The PM approach's ability to outperform the CJF approach and the KI approach will increase as information-heterogeneity increases.

## 4. Method

We next describe the task, participants, treatments, procedures and experimental measures in our study.

## 4.1. Task

To test our hypothesis, we sought forecasting tasks where we could compare the forecasting accuracy of the PM approach and the CJF approaches in situations with a small number of participants and that varied in information-heterogeneity. The characteristics of such settings are: i) the judgment of the informant is an important input to the forecast; ii) no single informant can know the “true” value in advance, and iii) there are multiple but a small number of informants whose knowledge can be tapped, who may (partially, at least) disagree, and who may differ in expertise and background. In addition, we conjecture that at least the following three characteristics distinguish domains of high and low information-heterogeneity: (1) Presence and Strength of an Anchor Point for the Forecasted Variable: a strong anchor point affects all informants and leads to more common information and homogeneity; (2) Amount of Public vs. Private Knowledge: more public relative to private knowledge will logically lead to more homogeneity; (3) Inherent Predictability: high inherent predictability of the variable under study will logically lead to more homogeneity.

Using these criteria, we selected two quite different domains for our experiment: predicting point spreads for two speci<sup>fi</sup>c college football games and predicting the values of two <sup>fi</sup>nancial indices. There is a weak anchor point for college football point spreads where changes in lineups, <sup>fi</sup>eld conditions, the changing “buzz” about speci<sup>fi</sup>c games and other factors lead to diverse and rapidly changing assessments about the outcome of the event. In contrast, the general stability of many <sup>fi</sup>nancial market indices makes current prices strong anchors. Also, the “real” market that runs openly for the latter task serves as another strong anchor. Similarly, for public versus private information: most students saw the <sup>fi</sup>nancial indices they were trading or forecasting (as well as speculations about them) daily, while only the more knowledgeable and dedicated football fans accessed news group and additional information sources on the Internet about football odds. A similar argument follows for predictability (with college football scores inherently much more unpredictable than <sup>fi</sup>nancial indices).

The speci<sup>fi</sup>c football task we chose was to predict the point spread for the score for two college football games of national championship signi<sup>fi</sup>cance to be played on 20 November 2004: Michigan vs. Ohio State (labeled here OSU) and Florida vs. Florida State (labeled here FSU), while for <sup>fi</sup>nancial indices the task was to forecast the Dow Jones

Index and the Crude Oil Spot Market Price (Texas Intermediate) on 20 November 2004.<sup>4</sup>

## 4.2. Informants

We sought a subject population representative of those likely to be involved in institutional market forecasts. Hence, business school students (upper level undergraduate and MBAs) represent an appropriate population pool. All had taken at least one course in <sup>fi</sup>nance and were familiar with <sup>fi</sup>nancial indices and instruments. Also, all participants were aware of college football but varied greatly in their knowledge and interest in the game. Overall, 126 business school students participated in our study.

## 4.3. Treatments

We sought a between-subjects design to control for dependencies between tasks and we needed to allow for an updating process to assimilate feedback and market information in a natural setting. Hence, we developed an intertemporal study design. Our institutional estimation framework required relatively small groups of participants to create a “market” (in the PM approach environment) and to aggregate multiple independent forecasts in a formal manner for the CJF approach. Previous research from experimental economics (Sunder 1995; Plott 2000) reported that markets with as few as six participants could ef<sup>fi</sup>ciently disseminate and aggregate information, the number we chose for our design. Hence, we formed 21 experimental groups consisting of six randomly assigned individuals, each in one of two conditions:

• Condition 1: consisting of 11 groups predicting the football point spreads through the CJF approach and participating in PMs for <sup>fi</sup>nancial indices.

• Condition 2: consisting of 10 groups predicting the <sup>fi</sup>nancial indices through the CJF approach and participating in PMs for football point spreads.<sup>5</sup>

Our 126 subjects were selected after a pre-experimental assessment of their football and <sup>fi</sup>nancial knowledge. To qualify, participants had to get 7 or more football questions correct and 8 or more <sup>fi</sup>nance questions correct out of 10. Sample questions for the pre-experimental assessment of football knowledge were: “a team must go 10 yards or more to get a <sup>fi</sup>rst down” (True/False) or “a team gets 7 points for a <sup>fi</sup>eld goal” (True/False). Sample questions for the assessment of <sup>fi</sup>nancial knowledge were: “it is better to buy high and sell low than buy low and sell high” (True/False) or “Dow Jones is a well-respected radio <sup>fi</sup>nancial commentator” (True/False).

## 4.4. Procedures

The PMs were open for 22 days prior to 20 November 2004. As all participants were involved in a CJF approach condition (as well as in a PM), they were required to provide forecasts and con<sup>fi</sup>dence scores about their forecasts in the CJF approach task four times during those 22 days via an electronic survey. We assessed participant competence via a separate knowledge questionnaire given when the study began. Sample questions to measure football knowledge were: “the number of time outs in a half is (the Same/Different) between college and NFL football” and “the <sup>fi</sup>eld size is (the Same/Different) between college and NFL football.” Sample questions to measure knowledge of <sup>fi</sup>nancial markets were: “shares of common stocks always pay dividends” (True/False) and “preferred stock ownership usually ensures voting rights in a company” (True/False).

Incentives: Participants were told they would receive both a (<sup>fi</sup>xed) participation payment and additional compensation based on their performance. Performance compensation in the PM approach was linearly related to the value of the participant's portfolio at the end of the study. Compensation in the CJF approach was based on the participant's mean overall <sup>fi</sup>nancial index price or point spread prediction accuracy. These compensation schemes were designed to provide signi<sup>fi</sup>cant and roughly equivalent incentives for all participants to apply effort and attention to these tasks. While we cannot exclude the possibility that the two tasks (participating in a PM and <sup>fi</sup>lling out questionnaires for the CJF and KI approach) will induce different levels of (intrinsic) motivation, we designed the study to ensure that none of the approaches was favored <sup>fi</sup>nancially. Similarly, although we cannot rule out the possibility that participants in various groups and conditions exchanged information of<sup>fl</sup>ine during the time our study was running, we see no evidence that such possible exchanges did or, indeed, could systematically affect our results. We set incentives for individual performance, providing a disincentive to share information. Individual participants were randomly and anonymously assigned randomly to study conditions, making information sharing nearly impossible. Even had they been able to do so, we see no reason for that (unlikely) sharing to favor one condition over another.

Operation of the PMs. Each PM was comprised of six (anonymous) individuals in a condition and two different stocks. Depending on the condition, the stocks represented either the value of a football point spread or the value of a <sup>fi</sup>nancial index on 20 November 2004. The payoff function for the football point spread stock types gives a cash dividend of \$1 (virtual) for every point in the point spread:

$$
d _ {i} = Z _ {i}\tag{1}
$$

where:

i=1,2 1: OSU, 2: FSU,

$d _ { i }$ Cash dividend of the stock modeling the outcome of the i-th football game,

$Z _ { i }$ (Absolute value of) point spread of the i-th football game.

For the <sup>fi</sup>nancial indices, we used two different payoff functions to adjust for the different scale levels of the <sup>fi</sup>nancial indices. The shares of the stock for the price of crude oil paid \$1 (virtual) for every \$1 (real) per barrel of crude oil (see Eq. (2)). The shares of the stocks for the Dow paid \$1 (virtual) for every 1000 points of this index (see Eq. (3)).

$$
d _ {\mathrm{crude}} = Z _ {\mathrm{crude}}\tag{2}
$$

$$
d _ {\mathrm{Dow}} = \frac {Z _ {\mathrm{Dow}}}{1 0 0 0}\tag{3}
$$

where:

$d _ { \mathrm { c r u d e } }$ Cash dividend of the stock modeling the price of crude oil on November 20th, 2004,

$d _ { \mathrm { D o w } }$ Cash dividend of the stock modeling the value of the Dow on November 20th, 2004,

$Z _ { \mathrm { c r u d e } }$ Price of crude oil on November 20th, 2004,

$Z _ { \mathrm { D o w } }$ Value of the Dow on November 20th, 2004.

Thus, the price of a share of stock for a speci<sup>fi</sup>c football game or <sup>fi</sup>nancial index represented a prediction of its value on 20 November

2004 by inverting the payoff function. We set the initial quotes for the football point spreads based on the performances of the teams up to that date and the initial quotes for the <sup>fi</sup>nancial indices based on their actual value on 27 October 2004.

The experiment ran from 29 October to 19 November 2004. Participants received an initial endowment of 100 shares of each stock type in their group-speci<sup>fi</sup>c PM and \$2500 (virtual) cash. Based on their performance in the PM (measured by the value of their <sup>fi</sup>nal portfolio), participants received a bonus payment. We used a market maker mechanism so that participants could trade anytime, 24 hours per day, seven days a week. There was no trading fee. (See Appendix A for a discussion of the Market Maker Mechanism and Appendix B for sample screen shots characterizing the operation of the markets.)

The CJF Approach Procedure. To create forecasts using the (online) survey-based forecasts in the CJF approach conditions, we created “virtual” groups consisting of 6 persons each. We randomly assigned subjects to groups and ex-post analysis showed no signi<sup>fi</sup>cant differences between groups, either in <sup>fi</sup>nancial knowledge (F=1.492, df=20, 125, p=.100) or football knowledge (F=.882, df=20, 125, p= .882). Participants in the CJF approach condition provided their forecasts by <sup>fi</sup>lling out an online questionnaire.

We developed aggregated forecasts for each 6-person group based on the questionnaire data for each of the 22 days. The values of the aggregated forecasts varied over the 22 days because all participants received the questionnaire the same day, but were allowed to send it back on one of the following days. Hence, responses varied over time and our results are based on an aggregation of the most recent six forecasts at any point in time. Following the approach developed in [56], we computed the unweighted average forecast $\mathrm { U F } _ { f t w }$ for group w at day t using Eq. (4).

$$
U F _ {f t w} = \frac {\sum_ {i = 1} ^ {6} F o r e c a s t _ {f t w i}}{6}\tag{4}
$$

where $F o r e c a s t _ { f t w i }$ is the forecast of individual i, in group w, at day t, for index f.

w 1, .. , p (p = 11 for the football indices and $p = 1 0$ for the <sup>fi</sup>nancial indices)

$$
\begin{array}{l l} t & 1,.., 2 2 \\ f & 1,.., 4 (1 = \text { OSU   point   spread }; 2 = \text { FSU   point   spread }; \\ & 3 = \text { Dow   Jones   Index }; 4 = \text { Oil   Price }) \end{array}
$$

Following the approach developed in [56] we also computed knowledge-based and con<sup>fi</sup>dence-based weighted averages. We computed the knowledge-based forecast $\operatorname { K B F } _ { f t w }$ for group w at day t using Eq. (5).

$$
K B F _ {f t w} = \frac {\sum_ {i = 1} ^ {6} K n o w l e d g e _ {f i} * F o r e c a s t _ {f t w i}}{\sum_ {i = 1} ^ {6} K n o w l e d g e _ {f i}}\tag{5}
$$

where Knowledge is the knowledge score of individual i about variable f measured using the knowledge test items. We computed the con<sup>fi</sup>dence-based forecast $\mathrm { C B F } _ { f t w }$ for group w at day t using Eq. (6)

$$
C B F _ {f t w} = \frac {\sum_ {i = 1} ^ {6} C o n f i d e n c e _ {f i} * F o r e c a s t _ {f t w i}}{\sum_ {i = 1} ^ {6} C o n f i d e n c e _ {f i}}\tag{6}
$$

where Confidence is the con<sup>fi</sup>dence of individual i about variable $f .$ Study participants rated their con<sup>fi</sup>dence about the correctness of their forecasts on a 5-point scale anchored by “not con<sup>fi</sup>dent at all” and “very con<sup>fi</sup>dent”.

Table 2  
Forecasting accuracy of the Key Informant (KI), Combined Judgmental Forecasts (CJF) and Prediction Markets, MAPE (Standard Deviation) averaged across 12 days

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">Key Informant</td><td colspan="3">Combined Judgmental Forecasts</td><td rowspan="2">Prediction Markets</td></tr><tr><td>Unweighted</td><td>Knowledge-based weighted</td><td>Confidence-based weighted</td></tr><tr><td rowspan="3">Football point spreads</td><td>OSU</td><td>.354 (.216)</td><td>.304 (.121)</td><td>.301 (.129)</td><td>.307 (.111)</td><td>.230 (.060)</td></tr><tr><td>FSU</td><td>1.050 (1.12)</td><td>.630 (.305)</td><td>.672 (.337)</td><td>.640 (.292)</td><td>.356 (.194)</td></tr><tr><td>Mean</td><td>.702 (.866)</td><td>.467 (.281)</td><td>.486 (.313)</td><td>.473 (.275)</td><td>.293 (.154)</td></tr><tr><td rowspan="3">Financial indices</td><td>Oil Price</td><td>.087 (.028)</td><td>.102 (.050)</td><td>.099 (.045)</td><td>.090 (.030)</td><td>.113 (.017)</td></tr><tr><td>Dow Jones</td><td>.075 (.101)</td><td>.029 (.014)</td><td>.030 (.019)</td><td>.023 (.010)</td><td>.071 (.044)</td></tr><tr><td>Mean</td><td>.081 (.072)</td><td>.065 (.052)</td><td>.065 (.049)</td><td>.056 (.041)</td><td>.092 (.039)</td></tr><tr><td>Mean</td><td></td><td>.406 (.697)</td><td>.276 (.288)</td><td>.286 (.311)</td><td>.275 (.290)</td><td>.188 (.149)</td></tr></table>

We also developed a Key Informant Forecast $K I F _ { f t w }$ for each 6- person group. We selected the key informant as the one with the highest knowledge score within the group according to the knowledge responses to our knowledge questions. We broke ties by selecting one key informant in a group at random.

## 4.5. Measures

We compare the forecasting accuracy of the CJF-based measures and the PM-based forecasts by computing the Mean Absolute Percentage Error (MAPE) of the deviations of the forecasts for the four variables $Z _ { 1 } , Z _ { 2 } , Z _ { \mathrm { c r u d e } }$ and $Z _ { \mathrm { D o w } }$ from the actual outcome on November $2 0 \left( A V _ { f } \right)$ . The MAPE, computed as in Eq. (7), is invariant to scale, is not in<sup>fl</sup>uenced by outliers.

$$
M A P E _ {f m t} = \left| \frac {\text { Forecast } _ {f m t} - A V _ {f}}{A V _ {f}} \right|\tag{7}
$$

where ${ \mathrm { M A P E } } _ { f m t }$ is the Mean Absolute Percentage Error for variable f for method m, where 1=unweighted aggregated CJF forecast, 2=Key Informant, and $3 { = } \mathrm { P M }$ -based forecast at day t.

The actual outcomes of the four variables forecasted were as follows:

Actual Point Spread Florida vs. Florida State: 7

Actual Point Spread Ohio State vs. Michigan: 16

Actual Crude Oil Price: \$48.90

Actual Dow Jones (divided by 1000): \$10.46

## 5. Results

Table 2 presents the average MAPE values of the key informants, of the various CJF-based forecasts and of the PM-based forecasts for the <sup>fi</sup>nancial indices and for the football point spreads across 12 days. While our PMs ran for 22 days, we focus on the middle 12 days for analysis here, eliminating the <sup>fi</sup>rst and the last <sup>fi</sup>ve days of trading. As is common in markets where the organizer sets the initial price, there is a transient period of volatility before the market settles to set a (new) price [13]. We dropped the last <sup>fi</sup>ve days of trading to provide a fair comparison between the PM approach and the CJF- and KI approaches.<sup>6</sup> During these last <sup>fi</sup>ve days the PM participants were able to trade and react to informational events and thus update their forecasts, while the vast majority of participants in the CJF- and KI approaches were not able to do so as they had already provided their last forecast. The results are graphically presented in Figs. 1 and 2.

(We replicated the analysis with the full data set and the results were similar to those reported here).

Overall our results show that the values of the <sup>fi</sup>nancial indices were more accurately predicted than the football point spreads $( F = 7 9 . 9 9 8 , \ \mathrm { d f } = 1 , \ 2 0 9 , \ p = . 0 0 0 )$ . The average MAPE across the several CJF approaches and the PM approach is .072 for the <sup>fi</sup>nancial indices while it is .488 for the football point spreads. In contrast with the <sup>fi</sup>ndings reported in Van Bruggen et al. [56], we do not <sup>fi</sup>nd weighted averages to do better than unweighted averages. A possible explanation for this <sup>fi</sup>nding (in line with other research results [3]) might lie in the participant screening procedure, which eliminated low-knowledge (and low con<sup>fi</sup>dence—a highly correlated variable) individuals. This screening procedure decreased variation in knowledge and con<sup>fi</sup>dence levels within groups, leading to a reduced impact of these weights. Although there is a chance that biases like overcon<sup>fi</sup>dence affected the assessments of individual study participants, we have no reason to believe that such biases would have affected the results of certain groups more than others.

Since we found no differences between weighted and unweighted CJF approaches, we only analyzed the unweighted CJF results further. These results show an interaction effect between the forecasting approaches (CJF approach vs. PM approach) and the forecasting tasks (Football Point Spreads vs. Financial Indices) $( F = 2 . 3 5 0 , { \mathrm { d f } } = 6 ,$ 114, $p { = } . 0 3 5 )$ (see also Figs. 1 and 2).

We found no signi<sup>fi</sup>cant differences in the forecasting accuracy for <sup>fi</sup>nancial indices between the CJF approaches, the KI approach and the PM approach. This <sup>fi</sup>nding thus does not support $\mathrm { H } _ { 1 } .$ However, closer inspection of Fig. 1 shows that there is a difference between the results for the <sup>fi</sup>rst part of the experimental period and the second part: in the second part of the forecasting period, the CJF- and KI approaches actually do somewhat better than the PM approach. While the reason for this result is not clear, it may be that the complexity of the PM task overshadowed its informational advantages, especially in the latter part of the forecasting period when most relevant information was likely already exchanged.

In predicting football point spreads, however, the PM approach clearly outperformed the CJF approaches, a result that supports H . Fig. 2 also reveals that the KI approach forecasts of the football point spreads are less accurate than the results of either the CJF approach or the results of the PM approach, also providing support for H . The positive result for football point spreads (high information-heterogeneity) compared to the null result for <sup>fi</sup>nancial markets (low informationheterogeneity) provides support for $\mathrm { H } _ { 2 } .$

To elaborate on this latter point we note that our results show that at the beginning of the forecasting period (22 days before the event or the close of trading) the mean absolute percentage error (MAPE) for the football point spreads was .42 while it was .11 for the <sup>fi</sup>nancial indices $( F = 7 9 . 9 9 , \mathrm { d f } = 1 , 2 0 9 , p = . 0 0 0 )$ . In addition, both the domain of sports scores and that of <sup>fi</sup>nancial indices have been intensively used for research on forecasting, demonstrating substantial uncertainty and unpredictability (for a recent summary see [2] and [55]). Furthermore, in interviews, our participants identi<sup>fi</sup>ed <sup>fi</sup>nancial markets as a domain where they have little unique information and low information-heterogeneity whereas they viewed the task of predicting (American) football game scores and point spreads as a high information-heterogeneity domain with less common information.

Oil Price  
![](/api/attachments/XYB75NV6/fulltext/images/a68dfc43f0d13ea3098e4d5accce727e063286744534b3d31e924a4664ad3815.jpg)

Dow Jones  
![](/api/attachments/XYB75NV6/fulltext/images/21200e465cf9af492f68f582e826f781745441dde3fa90cab8440c102a69448d.jpg)  
Note: Graphs exclude first and last five days of the market; Day 1 refers to 6th day of trading  
Fig. 1. Mean Absolute Percentage Errors (MAPE) for the Financial Indices Forecasts.

Hence, we conclude that our two tasks differ on informationheterogeneity and that this difference helps explains why the PM approach is especially effective in predicting football points spreads and less so in predicting <sup>fi</sup>nancial indices.

We also performed additional analyses to develop a deeper understanding of our results. We investigated how knowledge affected the accuracy of both the CJF approach and of the PM approach; our analyses did not identify a relationship between average knowledge levels, knowledge of the most knowledgeable participant or knowledge dispersion and forecast quality. Again, this result could have been driven by our screening out less knowledgeable participants. We did <sup>fi</sup>nd a nearly signi<sup>fi</sup>cant relationship $( r = - . 3 9 2 , n = 6 0 , p = . 0 8 8 )$ between participants' knowledge and forecasting accuracy for the <sup>fi</sup>nancial market indices, but could identify no other links between knowledge and forecasting ability.

Given the small number of traders and trades in our markets, we investigated the link between trading activity and accuracy. While we observed more active trading in the market for <sup>fi</sup>nancial indices than for football point spreads, that difference was not statistically signi<sup>fi</sup>cant. And we found no relationship between level of trading activity and forecasting accuracy for either market type, suggesting that there was suf<sup>fi</sup>cient trading activity for market ef<sup>fi</sup>ciency. We did <sup>fi</sup>nd, however, that within markets more active traders performed better $( r = . 8 7 5 , n = 6 5 , p = . 0 0 0$ for PMs for <sup>fi</sup>nancial indices and r=.362, n=60, p=.005 for PMs for football point spreads), suggesting that trading activity itself might indicate market knowledge.

## 6. Discussion

We have investigated the feasibility and accuracy of Prediction Markets (PMs) for forecasting situations characterized by a small number of knowledgeable participants, typical for institutional forecasting. Our results show that PMs are feasible in environments with varying degrees of information-heterogeneity, and can be conducted effectively with group sizes as small as six traders per market.

We found that PMs outperform the commonly applied approaches of Combined Judgmental Forecasts (CJF) and Key Informants (KI) in more dif<sup>fi</sup>cult-to-predict environments, characterized by high knowledge and information-heterogeneity between participants. The approach worked as well as the more traditional CJF- and KI approaches in more homogeneous environments. We attribute this superior performance of the PM approach in high informationheterogeneity environments to their ability to provide for information exchange between participants: trader's private, unique and unshared information becomes shared and common through their trades.

OSU Point Spread  
![](/api/attachments/XYB75NV6/fulltext/images/db72ebef8ee085880205f63dc40f39f1c7538f7107876e22073c70762ea4f4ab.jpg)

FSU Point Spread  
![](/api/attachments/XYB75NV6/fulltext/images/35412790837607aff0d3c76d46869d3836043d2dde43f03511c111ac35169ca2.jpg)  
Note: Graphs exclude first and last five days of the market; Day 1 refers to 6th day of trading  
Fig. 2. Mean Absolute Percentage Errors (MAPE) for the Football Point Spread Forecasts.

We also found that forecasts of both the PM approach and of the CJF approach are more accurate than those of the KI approach in situations we characterize as high information-heterogeneity. This <sup>fi</sup>nding may emerge because improved accuracy in any high information-heterogeneity environment requires a mechanism to consider and weight different expectations; both the PM approach and the CJF approach provide such a mechanism while the KI approach does not. Because our screening procedure produced a limited absolute informationheterogeneity level among our participants, our results should be viewed as a conservative test of the relative advantage of the PM approach in situations with high information-heterogeneity and we would expect a stronger advantage for the PM approach in cases of an even higher level of information-heterogeneity. Similarly, the PM approach's bene<sup>fi</sup>ts should also be expected to be larger if market participants are more experienced traders than those we used in our study [6].

Our results raise questions about why and when the PM approach should be expected to perform well in the <sup>fi</sup>eld. If information exchange and learning change participant's knowledge, then the PM approach has two intertemporal advantages over the CJF approach. First, participants improve their knowledge over time through the exchange mechanism, mitigating the effect of low-knowledge participants. Second, if the weights used for aggregation in the CJF approach, typically taken at one point in time, are not updated, those weights may become suboptimal if the environment is unstable or highly unpredictable. A PM, operating continuously, can aggregate such environmental and knowledge-based changes naturally and continuously and may also be effective in deriving participants' weights for future analyses (see Chen et al. [10]). In more stable, low information-heterogeneity environments, those problems do not exist and, hence, the PM approach exhibits no advantage over the KI approach or the CJF approach. Indeed, our results imply that the KI approach, the simplest, most cost-effective mechanism, should generally be chosen in such situations as that the additional use of information technology provides little value.

If our results hold in further testing, they suggest some useful managerial implications. First, Prediction Markets may remedy some of the limitations of existing Group Support Systems (GSS). They seem to be effective with small numbers of participants, a challenging domain for traditional GSS [24]. Secondly, better (institutional) forecasts may be achieved with the PM approach compared with the CJF- and the KI approach, with that improvement being most signi<sup>fi</sup>cant in environments with high information-heterogeneity. Also, the PM approach does no worse than the CJF- or the KI approach in low information-heterogeneity environments, making it a robust choice when little is actually known about environmental information-heterogeneity.

Thirdly, since the PM approach is superior to the CJF approach in high information-heterogeneity environments and the KI approach is no worse than the CJF approach in the low information-heterogeneity environment, it may be that the CJF approach should be a third choice option in most institutional forecasting environments.

Our results suggest several opportunities for future study. First, we compared the PM approach with approaches (CJF and KI) that are commonly applied in the practice of institutional forecasting. However, we did not compare them directly with more “traditional” GSSs which, like PMs do allow information exchange between participants. In future research the accuracy of PMs could thus also be compared directly with GSSs even though these systems are intended to facilitate especially group decision rather than group forecasting processes. Second, we allowed all participants to search for additional information, but did not provide any help in doing so. As such we treated all participants equally. We suspect that different ways to provide additional information lead to trading behavior and a market outcome that differ in quality. Third, our procedure screened out low and medium knowledge individuals so we could not determine how any of the procedures would have fared were they included. Including low and medium knowledge individuals would further increase the knowledge-heterogeneity among the participants, increasing market liquidity and potentially increasing the relative advantage of the PM approach.

In line with past work, we have set the size of the PMs to six individuals in our experiment. We have no data on how the performance of the PM approach varies with group size or when a market is too small. How market ef<sup>fi</sup>ciency varies with group size (is there a minimize market size, and if so, what?) is an important topic for future research. In addition, given our arguments about knowledge sharing in high information-heterogeneity environments as the explanation for the PM approach's performance, it would be useful to directly compare other repeated information-sharing mechanisms, perhaps of the repeated-Delphi type. (See Cil et al. [11], for example).

While there are clearly many other research opportunities, we reemphasize our main <sup>fi</sup>ndings: The PM approach is feasible in situations with small numbers of participants and most effective in situations with high information-heterogeneity. These are characteristics shared by many common institutional forecasting settings in organizations. And the PM approach appears to provide forecasting accuracy that is superior to other methods that are in common use in such situations.

## Appendix A. Market maker mechanism

Our main criterion for selecting the market mechanism was that it should maintain a suf<sup>fi</sup>cient level of liquidity, it should be easy to understand, and it should lead to ef<sup>fi</sup>cient prices. The most common market mechanism in Prediction Markets — the double auction, requires a matching bid-and-ask order pair in order to determine the price of a trade. This competitive mechanism operates well in the case of a large number of traders that are willing to sell and buy stocks. However, in small PMs that last several days or weeks like our PMs, a rather low trader-to-stock ratio is likely. The reasons for this are that the number of informants is small and the informants trade asynchronously. In this situation, a double auction might limit trading opportunities, which might decrease the informants' interest in the PM. The use of a trading agent similar to a market maker on NASDAQ or the “Virtual Specialist” at the Hollywood Stock Exchange avoids this shortcoming. The automatic version of the trading agent uses an algorithm to automatically set price quotes that allow the buying and selling of stocks at any time.

In our study the PMs thus applied a two-sided automated market maker trading mechanism, comparable to the one used at NASDAQ to avoid lack of trading opportunities that can arise due to our experimental setting of only six traders per market. Our market maker accepted every order from a informant and executed it at a preannounced price that is identical for purchase or sale orders. That price was adjusted after every executed order by an automatic price adjustment procedure.

The use of the market maker trading mechanism allowed informants to trade anytime at a pre-announced price. Purchases increased the price p for the next order, sales decreased this price. The goal of our price adjustment mechanism was to set a price p according to an estimate of the stock's true value V based on traders' order <sup>fl</sup>ow: informed traders are aware of changes in V and trade accordingly. Each trade of a single stock represents a signal to the market maker. Therefore, the quantities of stocks per transaction as well as the number of transactions in the same direction (i.e. the number of purchases or sales) were indicators of the possible magnitude of the deviation between p and V. We applied this principle in determining the price adjustment based on a moving window of the last I transactions, accounting for volume and direction of each transaction. To increase robustness, we also used information about the maximum possible value of V to scale the magnitude of price adjustment per share. We tested our mechanism both numerically and empirically before the application in our PMs and set a maximum order quantity of 50 shares to stabilize the markets. The latter characteristic led to more frequent price adjustments in case of large orders. An important goal for the design of the market maker mechanism together with the initial portfolio size and the amount of cash the informants received was to provide market informants with the possibility and freedom to fully express their opinions in their trading behavior. The following equation gives our price adjustment function with the parameter values used in our experiment.

$$
p _ {j, n} = p _ {j, n - 1} + \max \left\{s i g _ {j, n} \cdot q _ {j, n} \cdot \frac {p _ {j , m a x} ^ {2}}{\gamma^ {2}} \cdot \frac {\left(\sum_ {i = 0} ^ {I _ {n}} q _ {j , n - i}\right)}{I + 1}, \alpha \right\}
$$

with

$$
s i g _ {j, n} = \left\{ \begin{array}{l l} - 1 & \text { for   sale } \\ 1 & \text { for   purchase } \end{array} \right., I _ {n} = \left\{ \begin{array}{l l} n & \text { for   } n <   I = 1 0 \\ 1 0 & \text { for   } n \geq I = 1 0 \end{array} \right. (n > 0, j \in J),
$$

where:

$p _ { j , n }$ Market maker price for j-th stock after the n-th trade,

$q _ { j , n }$ Quantity of order of j-th stock at the n-th trade,

${ \dot { \mathbf { s i g } } } _ { j , n }$ Sign of the order of j-th stock at the n-th trade,

$p _ { j , \mathrm { m a x } }$ Maximum price for j-th stock,

$I _ { n }$ Length of moving average window,

$J$ Index set of stocks,

$\gamma$ Scaling parameter (with $\gamma = 5 0 0 )$

$\alpha$ Minimum tick size (with α=.01).

The market prices in the PMs during the 22-day trading period represented the forecasts.

<table><tr><td>Start price</td><td>$55.17</td></tr><tr><td>Last price</td><td>$54.52</td></tr><tr><td>Last Volume</td><td>10</td></tr></table>

+ So. if your PORTFOLIO YALUE = \$10.000 and total of the portfolio yalues of everyone in your stock marke (including you) = \$20,000, you will receive \$10,000/\$20,000 or 50% of the bonus pool. If your bonus pool were \$100, vou would receive a \$50 bonus  
+ YOUr BONUS SHARE = YOUR PORTFOLIO VALUEI(TOTAL PORTFOLIO VALUE OF EVERYONE IN YOUR STOCK MARKET).  
+ Your PERFORMANCE BONUS = Your BONUS SHARE X BONUS POOL

Introductory Screen of the Prediction Market(PM)  
![](/api/attachments/XYB75NV6/fulltext/images/66f6ec2c099529703218209116548b9ec8ab55becedc69e0205ee1db1733c1e7.jpg)  
The menu bar at the left will aid you in navigating the site

Explanatory Screen of Prediction Market(PM) for Oil Prices  
![](/api/attachments/XYB75NV6/fulltext/images/b46e623a8ec3178b025a9e23fbc2c52f8c1129c5b1df4271f6d9aa3911697a33.jpg)

Explanatory Screen of Prediction Market (PM) for Football Point Spread Shares  
![](/api/attachments/XYB75NV6/fulltext/images/967d4bed29ecb121bcaabca0d9b343a8e831751b84108054375e1b635d95c313.jpg)

Portfolio Screen of Prediction Market (PM) for Financial Shares  
![](/api/attachments/XYB75NV6/fulltext/images/2a261342f53c820405ced73d27e97b2de5f66974dd4f9871d45d43d883f7f3f0.jpg)

## References

[1] L.R. Anderson, C.A. Holt, Information cascades in the laboratory, American Economic Review 87 (5) (1997) 847–862.

[2] P. Andersson, J. Edman, M. Ekman, Predicting the World Cup 2002 in soccer: performance and con<sup>fi</sup>dence of experts and non-experts, International Journal of Forecasting 21 (3) (2005) 565–576.

[3] J.S. Armstrong, Principles of Forecasting: A Handbook for Researchers and Practitioners, Kluwer Academic Publishers, Norwell MA, 2001.

[4] P. Barnes, Thin trading and stock market ef<sup>fi</sup>ciency: the case of the Kula Lumpur stock exchange, Journal of Business Finance and Accounting 13 (4) (1986) 609–617.

[5] R. Batchelor, P. Dua, Forecaster diversity and the bene<sup>fi</sup>ts of combining forecasts Management Science 41 (1) (1995) 68–75.

[6] J. Berg, R. Forsythe, T. Rietz, What makes markets predict well? Evidence from the Iowa electronic markets, in: Wulf Albert, Werner Güth, Peter Hammerstein, Benny Moldovanu, Eric Van Damme (Eds.), Essays in Honor of Reinhard Selten, Springer Verlag, 1996, pp. 444–463.

[7] J.E. Berg, F.D. Nelson, T.A. Rietz, Prediction market accuracy in the long run, International Journal of Forecasting 24 (2) (2008) 285–300

[8] J.E. Berg, T.A. Rietz, Prediction markets as decision support systems, Information Systems Frontiers 5 (1) (2003) 79–93.

[9] K.-Y. Chen, L.R. Fine, B.A. Huberman, Predicting the future, Information Systems Frontiers 5 (1) (2003) 47–61.

[10] K.-Y. Chen, L.R. Fine, B.A. Huberman, Eliminating public knowledge biases in information-aggregation mechanisms, Management Science 50 (7) (2004) 983–994.

[11] I. Cil, O. Alpturk, H.R. Yazgan, A new collaborative system framework based on a multiple perspective approach: InteliTeam, Decision Support Systems 39 (4) (2005) 619–641.

[12] E. Dahan, A.W. Lo, T. Poggio, N. Chan, A. Kim, Securities Trading of Concepts (STOC), 2007.

[13] S. Das, A learning market-maker in the Glosten–Milgrom model, Quantitative Finance 5 (2) (2005) 169–180.

[14] A.R. Dennis, Information exchange and use in group decision making: you can lead a group to information, but you can't make it think, MIS Quarterly 20 (4) (1996) 433–457.

[15] A.R. Dennis, M.J. Gar<sup>fi</sup>eld, The adoption and use of GSS in project teams: toward more participative processes and outcomes, MIS Quarterly 27 (2) (2003) 289–323

[16] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987) 589–609.

[17] A. Elberse, The power of stars: do star actors drive the success of movies? Journal of Marketing 71 (4) (2007) 102–120

[18] M. Evans, Practical Business Forecasting, Blackwell Publishing, Malden MA, 2002.

[19] E.F. Fama, Ef<sup>fi</sup>cient capital markets II, Journal of Finance 46 (1991) 1575–1617.

[20] R. Fildes, R. Hastings, The organization and improvement of market forecasting, Journal of the Operational Research Society 45 (1) (1994) 1–16.

[21] R. Forsythe, T.A. Rietz, T.W. Ross, Wishes, expectations and actions: a survey on price formation in election stock markets, Journal of Economic Behavior & Organization 39 (1) (1999) 83–110.

[22] N.Z. Foutz, W. Jank, The Wisdom of Crowds: Pre-release Forecasting for New Products via Functional Shape Analysis of the Online Virtual Stock Market, 2008.

[23] J.K.W. Fung, H.M.K. Mok, K.C.K. Wong, Pricing ef<sup>fi</sup>ciency in a thin market with competitive market makers: box spread strategies in the Hang Seng index options market, Financial Review 39 (2004) 434–454.

[24] R.B. Gallupe, A.R. Dennis, W.H. Cooper, J.S. Valacich, L.M. Bastianutti, J.F. Nunamaker, Electronic brainstorming and group size, Academy of Management Journal 35 (2) (1992) 350–369

[25] P.H. Garthwaite, J.B. Kadane, A. O'Hagan, Statistical methods for eliciting probability distributions, Journal of the American Statistical Association 100 (470) (2005) 680–700.

[26] S. Grossman, On the ef<sup>fi</sup>ciency of competitive stock markets where trades have diverse information, Journal of Finance 31 (2) (1976) 573–585.

[28] S.J. Grossman, J.E. Stiglitz, On the impossibility of informationally ef<sup>fi</sup>cient markets, American Economic Review 70 (3) (1980) 393–408.

[30] Z. Guo, F. Fang, A.B. Whinston, Supply chain information sharing in a macro prediction market, Decision Support Systems 42 (3) (2006) 1944–1958.

[31] F.A.V. Hayek, The use of knowledge in society, American Economic Review 35 (4) (1945) 519–530.

[32] R. Hightower, L. Sayeed, Effects of communication mode and prediscussion information distribution characteristics on information exchange in groups, Information Systems Research 7 (4) (1996) 451–465.

[33] N. Kumar, LW. Stern, I.C. Anderson, Conducting interorganizational research using key informants, Academy of Management Journal 36 (6) (1993) 1633–1651.

[34] C.A. LaComb, J.A. Barnett, Q. Pan, The imagination market, Information Systems Frontiers 9 (2–3) (2007) 245–256.

[35] B.G. Malkiel, The ef<sup>fi</sup>cient market hypothesis and its critics, Journal of Economic Perspectives 17 (1) (2003) 59–82.

[36] S. Ostrover, Employing information markets to achieve truly colloborative sales forecasting, Journal of Business Forecasting 24 (1) (2005) 9–12.

[37] D.M. Pennock, S. Lawrence, C.L. Giles, F.A. Nielsen, The power of play: ef<sup>fi</sup>ciency and forecast accuracy in web market games, NEC Research Institute Technical Report, NEC Research Institute, 2000, p. 20.

[38] D.M. Pennock, S. Lawrence, C.L. Giles, F.Å. Nielsen, The real power of arti<sup>fi</sup>cial markets, Science 291 (5506) (2001) 987–988.

[39] C.R. Plott, Markets as information gathering tools, Southern Economic Journal 67 (1) (2000) 2–15.

[40] C.R. Plott, S. Sunder, Ef<sup>fi</sup>ciency of experimental security markets with insider information: an application of rational expectation models, Journal of Political Economy 90 (4) (1982) 663–698.

[41] C.R. Plott, S. Sunder, Rational expectations and the aggregation of diverse information in laboratory security markets, Econometrica 56 (1988) 1085–1118.

[42] S. Rodan, C. Galunic, More than network structure: how knowledge heterogenity in<sup>fl</sup>uences managerial performance and innovativeness, Strategic Management Journal 25 (6) (2004).541–562

[43] M.E. Shaw, Group Dynamics: The Psychology of Small Group Behavior, 3rd ed. McGraw-Hill, New York, 1981.

[44] C.-L. Sia, B.C.Y. Tan, K.-K. Wei, Group polarization and computer-mediated communication: effects of communication cues, social presence, and anonymity, Information Systems Research 13 (1) (2002) 70–90.

[45] A. Soukhoroukova, M. Spann, B. Skiera, forthcoming. "Sourcing, Filtering, and Evaluating New Product Ideas: An Empirical Exploration of the Performance of Idea Markets". Journal of Product Innovation Management (forthcoming).

[46] M. Spann, B. Skiera, Internet-based virtual stock markets for business forecasting, Management Science 49 (10) (2003) 1310–1326.

[47] M. Spann, B. Skiera, Sports forecasting: a comparison of the forecast accuracy of prediction markets, betting odds and tipsters, Journal of Forecasting 28 (1) (2009) 55–72.

[48] G. Stasser, Information salience and the discovery of hidden pro<sup>fi</sup>les by decision making groups: a ‘thought experiment’, Organizational Behavior and Human Decision Making Processes 52 (1992) 156–181.

[49] G. Stasser, W. Titus, Pooling of unshared information in group decision making: biased information sampling during discussion, Journal of Personality and Social Psychology 48 (6) (1985) 1467–1478.

[50] G. Stasser, W. Titus, Effects of information load and percentage of shared information on the dissemination of unshared information during group discussion, Journal of Personality and Social Psychology 53 (1) (1987) 81–93.

[51] L. Stracca, Behavioral <sup>fi</sup>nance and asset prices: where do we stand? Journal of Economic Psychology 25 (3) (2004) 373–406.

[52] S. Sunder, Market for information: experimental evidence, Econometrica 60 (3) (1992) 667–695.

[53] S. Sunder, Experimental asset markets: a survey, in: J.H. Kagel, A.E. Roth (Eds.), The Handbook of Experimental Economics, Princeton University Press, 1995, pp. 445–500.

[54] J. Surowiecki, The Wisdom of Crowds: Why the Many Are Smarter Than the Few, Abacus, London, 2005.

[55] G. Törngren, H. Montgomery, Worse than chance? Performance and con<sup>fi</sup>dence among professionals and laypeople in the stock market, Journal of Behavioral Finance 5 (3) (2004) 246–251.

[56] G.H. Van Bruggen, G.L. Lilien, M. Kacker, Informants in organizational marketing research: why use multiple informants and how to aggregate responses, Journal of Marketing Research 39 (4) (2002) 469–478.

[57] J. Wolfers, E. Zitzewitz, Prediction markets, Journal of Economic Perspectives 18 (2) (2004) 107–126.

![](/api/attachments/XYB75NV6/fulltext/images/dc1a15bec068389ebc0071d8891ea120d351f99777a9a86443a27a04407665d2.jpg)  
Gerrit H. van Bruggen is a Professor of Marketing at RSM Erasmus University in Rotterdam. Most of his research addresses the impact of information technology and information systems on marketing. His research has been published in Management Science, MIS Quarterly, Information Systems Research, Interfaces, Decision Support Systems Marketing Science, Journal of Marketing and Journal of Marketing Research

![](/api/attachments/XYB75NV6/fulltext/images/d42d9c0f1fd8cdc119c820016526926f6ad3ae02ca6f80c16ef6be81f9570aee.jpg)

Martin Spann is a Professor of Electronic Commerce at the Ludwig-Maximilians-University in Munich. Martin's current research interests are pricing, electronic markets, prediction markets, social networks and virtual worlds. His work has been published in Management Science, MIS Ouarterly, Information Systems Research, Journal of Marketing, Journal of Product Innovation Management. Journal ot Interactive Marketing, and European Journal of Operational Research

![](/api/attachments/XYB75NV6/fulltext/images/a8ad10e9d1061d8fb84c6f4ab54d14bb54c722a26c2d45e03c7d7b21b4661688.jpg)

Gary L. Lilien is a Distinguished Research Professor of Management Science at Penn State and co-founder and Research Director of Penn State's Institute for the Study of Business Markets. His most recent research has been on the development and implementation of marketing models and issues in business marketing. His research has been published in Operations Research, Management Science, Information Systems Research, Interfaces, Journal of Marketing, Journal of Marketing Research, Marketing Science and others.

![](/api/attachments/XYB75NV6/fulltext/images/390c0405d2fb3428a18baaa4cc229da52fd99463c6b5a874d0d8594533c12065.jpg)

Bernd Skiera is a Professor of Electronic Commerce at the University of Frankfurt, Germany, and a member of the board of the E-Finance Lab His research focuses on the impact of information technology on the <sup>fi</sup>nancial service industry, search engine marketing virtual stock markets pricing and customer management. His work has been published in Management Science Marketing Science Journal of Marketing Research, Journal of Marketing, Journal of Product Innovation Management, Journal of Interactive Marketing, and European Journal of Operational Research.
