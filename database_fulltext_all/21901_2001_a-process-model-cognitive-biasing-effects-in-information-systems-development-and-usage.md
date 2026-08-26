---
otero_id: 21901
otero_key: "7JR8WT9Z"
title: "A process model cognitive biasing effects in information systems development and usage"
authors: "Peeter J Kirs; Kurt Pflughoeft; Galen Kroeck"
year: "2001"
journal: "Information & Management"
doi: "10.1016/s0378-7206(00)00062-8"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A process model cognitive biasing effects in information systems development and usage

Peeter J. Kirs $^{a,*}$ , Kurt Pflughoeft $^{b}$ , Galen Kroeck $^{c}$

$^{a}$ Department of Information Systems and Management Sciences, The University of Texas at Arlington, Arlington, TX, USA $^{b}$ Market Probe Inc., Milwaukee, WI, USA

$^{c}$ Department of Management, Florida International University, University Park, Miami, FL, USA

Accepted 27 June 2000

## Abstract

There are many opportunities for failure when designing information systems. Most of the IS research investigating this area has concentrated on problems related to organizational environment, informational characteristics, or physical software design. Little attention has been given to the subconscious cognitive biases which can impact the manner in which information systems are developed and utilized. While it is recognized that elimination of these biases is neither feasible nor altogether desirable, it is further acknowledged that ignoring them can lead to an exacerbation of their undesirable effects. This paper provides a general framework to identify where system designer and decision maker biases are likely to occur, and suggests some moderating measures which might be taken to alleviate some of the potentially harmful effects of these biases. © 2001 Published by Elsevier Science B.V.

Keywords: Information systems; Decision maker; IS designer

## 1. Introduction

Under conditions of uncertainty, a decision maker (DM) is likely to search for available information from a vast array of sources and to accept information which conforms to some perception of a ‘reasonable’ outcome. Decision aids, such as decision support systems, are intended to reduce uncertainty and promote effective, objective solutions. Nonetheless, the retrieval and processing of information may be limited or distorted by the DM’s inherent cognitive biases. Further, given the involvement of a systems designers with their own set of cognitive biases, biased outcomes may actually be promoted since the information system was constructed based on the DM's stated specifications.

Cognitive biases are neither readily apparent nor easily counterbalanced since they are developmentally inherent in the cognitive schemas and heuristics that form the basis of human information processing. These schemas and heuristics constitute behavioral patterns which dictate the way in which the DM approaches a problem. Such cognitive processes serve to reduce and combine mentally cumbersome quantities of information. They include filtering mechanisms applied in determining the elements or variables associated with the problem space, the analysis techniques used to examine the interrelationships between the components, and the manner in which outcomes are processed in relation to functional objectives.

While permitting the DM to manage complex information, numerous untoward consequences of cognitive heuristics and biases in decision making and information systems (IS) construction have been recognized by researchers for some time $[4,29,34,39,42]$ (see $[33]$ for a thorough review). More recently, the negative impacts of judgmental biases in day-to-day software development has been given attention by practitioners, especially with regard to testing and debugging $[12,37,38]$ .

Researchers generally agree that it would be futile to attempt to nullify biases, given their number, variety, and overlap with other biases, as well as the fact that they have can have positive utility in processing information. Furthermore, such efforts could possibly be counterproductive if they force the DM to alter successful patterns of behavior. However, in order to facilitate improved decision making, IS designers should understand the nature of such biases and the conditions under which they can be problematic. Counter-measures to alleviate some of the negative effects could subsequently be provided.

Some studies have offered suggestions for dealing with cognitive biases during IS design. These studies have focused on special problems of probabilistic information $[8,9]$ , ways to incorporate control mechanisms to counter individual biases $[4,33,37]$ , or have focused on specific IS types $[23,29]$ . Although it has been suggested that a general model detailing the potential impacts of cognitive biases on IS design and usage is needed $[4,33]$ , little effort has been directed toward this end.

The primary purpose of this paper is to consolidate and summarize the various biases that have been identified in various fields such as decision making, cognitive psychology and information systems. We are primarily concerned with biases which tend to arise in the development and use of small-scale IS. By that we mean those that are generally produced by a single designer, or under the direction of a single analyst, and are used by individual decision makers. This is in contrast to the larger, organization-wide systems which typically involve large teams of systems analysts to develop and are often used by teams of decision makers. While these latter systems can give rise to the same biases, because they are produced and used by groups of individuals, the situations which promote the biases, as well as how the biases manifest themselves, can vary.

It is not our intent to suggest that all biases are detrimental and should, therefore, be moderated. As shall be discussed, these biases underlie the cognitive schemas and heuristics which compose an IS designer's and DM's information processing patterns. Attempting to entirely alter the manner in which these individuals behave and reason is not only counterproductive, but also infeasible. However, dependent upon the available supply of information available, the information system derived from it, and the task environment, many of the biases can have detrimental affects. Our objective is to make the participants in this process, especially the IS designer, aware of the potential biases which exist, and what affect they could have on the decision making process. Consequently, the designer might be able to incorporate moderating strategies in developing the IS to alleviate some of unfavorable affects of biases (to be discussed later).

In Section 2, we review some conceptual foundations and past findings, drawing heavily from the psychology and IS literature. We next develop a process model to examine the manner in which the inherent behavioral schemas of the DM and the IS designer might filter or distort information during IS development, access, and application. A number of postulated biases are categorized in terms of their impact on the activities involved in the decision making process. In the Section 4, we discuss some of the theoretical constructs underlying cognitive processing mechanisms. Next, we propose a process model that illustrates some of the potential biases which may occur at various stages of the IS development and decision making process. We then suggest some preventive measures to alleviate some of the negative effects associated with these biases, and provide an example of how these measures might impact decision making. Finally, we offer some recommendations for future research.

## 2. Conceptual foundations and past findings

A number of theories have been advanced to describe human information processing. Most view cognitive processes as a set of information filtering and organizing mechanisms [6]. Because humans are inundated with enormous amounts of stimulus information, they tend to utilize a variety of mechanisms to cope with the environment. Coping mechanisms include chunking of information [34,35], the use of heuristics [42], programmed strategies [18], and various other information categorization processes [1,15].

Assigning observations to categories has been described as a primary function of cognitive representation $[31]$ . The individual is seen as actively seeking information which augments or discounts the categorical assignment of other information. The active search for confirmatory information, and avoidance of disconfirmatory information, has consistently been shown to be one of the most profound motivators of all human action tendencies $[46]$ . In other words, humans seem to make a sense of the world through assignment of observed events, and what causes them, to cognitive categories. These cognitive categorization processes have commonly been referred to as schema or implicit theories $[26]$ .

Many of the constructs regarding cognitive processes have generated substantial research. A variety of sophisticated models have been proposed about the human use of information. These models describe and explain why there are often biases and errors in human judgment and decision making. Biases and errors are typically due to information processing limitations, decision complexity, miscategorization of information, biased search for information $[34]$ , or overreliance on information simplification heuristic mechanisms $[42]$ . Implications for reducing errors of judgment and decision making are the products of many cognitive models. However, these models are rarely linked directly to the design of information systems.

## 3. A model of cognitive biases in information processing

The model, presented in Fig. 1, approaches the biases in information processing from two perspectives. It considers the two primary participants involved in development and usage of the information system, the IS designer and the DM (represented as shaded rectangles in the model), and three major components which impact the decision making process (represented as circles). These components include:

![](/api/attachments/7JR8WT9Z/fulltext/images/9d3e422aa1d3c097cddd2552d466fb5f50f669fc081e439ed18fcec0df8054d9.jpg)  
Fig. 1. Cognitive biases in information processing.

1. The ‘Real-World’ universe of information, or Information supply, consisting of all facts and perceptions which exist about a problem, whether or not used in the information system developed.

2. The Information system, which is the constructed domain of selected ‘facts’.

3. The Required decision, or the task undertaken by the DM.

The IS designer and the DM act as facilitators of information flow. The IS designer is responsible for extracting information from the population of facts (the Information supply), filtering, organizing, and developing a subset of facts and a collection of procedures such that the Information system may be related it to the array of potential Required decisions. The DM is responsible for extracting, filtering, interpreting and evaluating information contained in the Information system, by relating it to the Required decision.

As with any information channel, screening and distortion can occur whenever information is filtered, interpreted or evaluated. The model depicted in Fig. 1 shows five potential biasing arenas, or linkages, which are represented by inverted triangles. Each linkage is associated with an interface between the participant and a component of the information processing system. The linkages postulated, grouped by participant, include:

1. IS designer biases. These consist of inclusion biases (the supply-designer linkage: L1), and construction biases (the designer-IS linkage: L2).

2. Decision maker biases. The three biases associated with the DM are retrieval biases (the IS-DM Linkage: L3), analysis biases (the IS-DM linkage: L4), and interpretation biases (DM-decision linkage: L5).

Each of these biases and linkages will be discussed separately in the Section 4. Table 1 is provided as a summary of potential biases which may occur at each linkage. An ongoing example of how each bias might impact a decision is provided at the end of each section.

## 4. Designer biases

Ideally, the IS designer should provide an objective analysis of the problem based on user requirements. In a large-scale, organization-wide IS, a team approach, relying on top-down systems analysis and design methodologies would likely be employed. As noted earlier, our focus is on smaller systems, where deployment of large systems analysis and design teams is not feasible.

For smaller systems, the IS designer can succumb to several biases. Many of these correspond to those noted for the DM (see later section) in that they are related to the specific cognitive schema employed. Others are related to the designer's lack of awareness of available information supply, and the heuristics used in transferring this information to the operational IS.

## 4.1. L1: inclusion biases (the supply-designer linkage)

In selecting data for inclusion in the domain of information to be considered, the designer may be instructed by the DM to include specified data sets. Without explicit guidance, however, the IS designer will rely on past experience and perceptions of what is expected. While the designer's lack of expertise may actually alleviate some potential task-oriented biases, such naivete may lead to the omission of pertinent information. In selecting a subset of the 'real world universe of information', the designer may be influenced by the bias of Availability [42], whereby the IS designer judges the extent of factual data or how large a body of information is based on how readily examples can be abstracted. For example, we might estimate the amount of violence in a particular city by how readily we can think of examples of violent events that have occurred there. The IS designer might provide a cumbersome database believing it critical to provide such extensive data because several examples of needed facts from the database are readily discerned. Similarly, the IS designer might over- or underestimate how often a particular set of data will be utilized based on how readily instances come to mind about past usage.

A number of rationales have been offered to explain the Availability bias, including recency effects, perceived utility, and event complexity. Instances which are recalled as recent events may be judged more numerous than classes of the same size whose instances are historical, but not in the recent past. Even though infrequently occurring events might be more appropriate to the decision at hand, biases can occur toward overestimation of readily available or abundant events [30].

Table 1
Summary of cognitive biases

<table><tr><td>Source</td><td>Linkage/category</td><td>Bias</td><td>Possible impact on information system and usage</td></tr><tr><td rowspan="2">Designer</td><td>L1: Supply-designer (inclusion biases)</td><td>Availability for constructionData saturationHabitSelective perceptions</td><td>Only easily attained data includedPertinent data overlooked due to vastness of data setInappropriate data selected based on convention</td></tr><tr><td>L2: Designer-IS (construction biases)</td><td>Data presentation contextFact-value confusionOrder effectsWishful thinking</td><td>Only data which designer assumes will please DM soughtOutput format influences import to DMData included because of convention not relevanceOrder stored and presented influences import to DMDesigner beliefs presented as facts</td></tr><tr><td rowspan="3">DM</td><td>L3: DM-IS (retrieval biases)</td><td>Availability for retrievalData presentation contextData saturationHabitOrder effectsOutcome irrelevant learningRedundancySelective perceptionsSelf-fulfilling prophecies</td><td>Easily retrieved information selected from all availableSummarized data preferred/selected over detailed dataSmall sample extracted if data set viewed as unwieldyFamiliar, but inappropriate retrieval schemes applied1st &amp; last data retrieved often deemed more importantPrevious inappropriate data selected out of habitRedundant data preferred as it implies increased accuracyTendency to seek only confirmatory informationOnly data which supports preferences is retrieved</td></tr><tr><td>L4: IS-DM (analysis biases)</td><td>Adjustment and anchoringBase rateConcrete informationHabitIllusion of correlationLaw of small numbersOutcome irrelevant learningRedundancyRepresentativenessRegression effects</td><td>Heuristics or initial value used as basis of analysisOnly likelihood of both events occurring consideredTangible events regarded above abstract/statistical dataFamiliar, but inappropriate analysis techniques appliedMistaken belief that events co-vary when they do notSm. confirmatory samples preferred to lg. disconfirm. onesInferior processing rules applied if alternatives not available abundant data viewed as more importantInappropriate inferences made if abundance/lack of dataLarge values deemed important; noise not adjusted for</td></tr><tr><td>L5: DM-decision (interpretation biases)</td><td>ConservatismEase of recallExpectationsFact-value confusionFrequencyFundamental attribution errorGambler&#x27;s fallacyHindsightIllusion of controlOverconfidenceReference effectsRepresentativenessSelf-fulfilling propheciesSpurious cuesWishful thinking</td><td>Failure to adequate revise estimates as new data receivedEasily recalled data influence perceptions of reoccurrenceData satisfying preconceptions given more weightStrongly held values may be perceived as factsNumerical magnitude regarded more than ratio of successSuccess attributed to ability; failure associated with bad luckChance ‘run’ of events assumed to continue occurringPrevious outcomes tend to influence decision reachedUnwarranted feeling of control over outcomesAbundant data overvalued as representativePrevious expectations &amp; experiences influence decisionsAssumption that members of sample share same traitsOnly data which supports preferences is retrievedInfrequently occurring events be perceived as commonPredetermined outcome preferences influence decision</td></tr></table>

Data saturation occurs when overwhelming amounts of data are available, especially if the designer is unable to categorize them in a meaningful and efficient fashion. As a result, attribute selection may be based on a limited search and much of the important information may be ignored. On the other hand, in instances where the supply of information is scarce, the designer may rely on convention or Habit [33] in selecting information. Reliance on Habit implies that the designer may apply previously successful search strategies without regard to appropriateness.

Finally, the designer may be influenced by a variety of Selective perceptions [16]. Because the designer is essentially acting as an agent for the DM, there is an unconscious desire to satisfy what is perceived as the DM's preferred outcomes. Information which promotes confirmation of DM preferred outcomes is more likely to be included than disconfirmatory information.

Assume, for example, that an IS designer is charged with the task of developing a mortgage application approval system. Such a system might rely on a variety of data like credit reports, work history, salary information, investments, debt/loan history, checking/saving statements, and other personal data. Some of this data is easily attained, while other types of data are difficult to locate (e.g. debts owed to agencies and individuals who do not file reports with credit-tracking agencies, perhaps a hospital). As the amount of data which could be included increases, the probability that some pertinent information (e.g. stability of applicant's profession), will be overlooked (Data saturation), or that inappropriate information will be based on convention (Habit). Unless the DM explicitly instructs the designer as to which data to include, it is likely that the designer will include only that data assumed to be important (Selective perception).

## 4.2. L2: construction biases (the designer-IS linkage)

After the designer has selected the subset of real-world information, problems may arise when attempting to transfer these facts into an organizational information system. This process can be biased by the way in which the designer assumes the data will be used. Fact-value confusion may occur [33] when the designer applies either their own value system, or what they perceive as the DM's value system. In this situation, data may be made available based on convention, rather than relevance, timeliness or accuracy. Inaccuracies can also be introduced by the bias of Wishful thinking, where strongly held beliefs may be presented as facts.

Such information may be given undue weight in the Order of presentation to the DM [17]. Information which is presented first is often perceived as more important than subsequent data. This impact of this bias can readily be illustrated by the early versions of American Airline's Sabre System, which always displayed American Airline data first, even though the system was designed for general use. $^{1}$

The Order of presentation bias may be further distorted by the bias of Data presentation context, or the format selected by the designer to display the information $[16,19,32]$ . This impact can be especially acute if the data presented is first transformed according to a scale which overstates, or understates, differences. For example, assume that a company's year-to-year expenses vary only by thousands, but are graphically expressed in units of millions without displaying the lower end of the graph. Such changes would appear dramatic, while in fact insignificant (related biases will be discussed in later sections).

Extending our example, assume that the IS designer feels that the number of credit cards an individual possesses is an important indicator of assets, even though the DM may consider it a sign that the applicant is over-extended. He may also devise menus which automatically present this information first (Order of presentation bias) and/or develop a weighting scheme which gives this factor undue importance (Data presentation bias). Unless the DM is extremely careful in their analysis, such distortions could go unnoticed.

## 5. Decision maker biases

There are three linkages (labeled L3–L5 on Fig. 1) which may give way to a number of DM biases. Since these involve a variety of complex activities, the total number of potential biases postulated in considerably larger. The IS designer should be aware of the DM's biases in order to construct an IS which moderate some of the negative impacts.

The linkages postulated for the DM are grouped according to the interface between the DM and the two major components of the information processing system with which he communicates (the Information system and the Decision to be made). Specifically, these include Retrieval biases, Analysis biases, and Interpretation biases.

## 5.1. L3: retrieval biases (the DM-IS linkage)

After the IS has been constructed, the DM's biases can influence the reliability and accuracy of the information retrieved through the manner in which he retrieves it. If he was not actively involved in the selection and construction of the database, he may not be aware of any limitations due to scarcity of data or built-in biases due to abundance of data. In such cases, he may compound any misrepresentations through unfamiliarity with the availability of information. He may also amplify existing exaggerations through the use of inappropriate or inefficient search techniques. Each of these retrieval biases will be discussed in turn.

## 5.1.1. Availability for retrieval

In selecting data to be included for a decision, the possibility exists that the DM may either prematurely halt the search for data or prolong it unnecessarily. In an attempt to reduce mental effort, the DM can succumb to the biases of Availability for retrieval and Data saturation related effects. The DM may tend to eliminate or avoid areas that are unclear or require additional information for a clear definition $[20]$ . In situations where data is limited, or disconfirmatory, the DM may extend his search until acceptable information can be retrieved.

The distortion of information can also be further perpetuated by the DM through their own set of Order effects and Data presentation context biases. Information can result in very different attribution depending upon the order in which consistency, distinctiveness, and consensus information is selected $[19,32]$ . It has been postulated that the first (primacy effect) and last (recency effect) pieces of information retrieved are given undue emphasis, while those occurring in the middle of a data set may be ignored $[17,22]$ . Similarly, summarized data is felt to have a greater influence than detailed data $[16]$ . If the available data demonstrates considerable Redundancy, there is a tendency to assign greater confidence in its accuracy $[33]$ .

In our example, if the DM is attempting to determine an applicant's debt history, there a number of biases which might arise. If the applicant has a number of debts with individuals or agencies who do not report to credit-tracking agencies, there are a few possible actions which might be taken. If the DM is not aware that such data is missing, he may assume that there are no additional debts and prematurely discontinue the search (Availability for retrieval). If there is an extensive amount of checking activity he may halt the search unnecessarily (Data saturation), or conversely, if, for example, the applicant has paid his debts in cash, he may extend his search unnecessarily. If the applicant has very few debts, but they were very recent, or appear at the end of the search, the DM could be unnecessarily influenced by primacy or latency effects. Similarly, if the data is obtained in summary, as opposed to detailed, format, he may place undue importance on it.

## 5.1.2. Inappropriate and ineffective search techniques

The procedures applied by the DM in retrieving information are affected by a number of factors: the nature of the available data set, the decision at hand, and the DM's awareness of specific retrieval methodologies. As with the IS designer, the DM frequently tends to select search and retrieval approaches out of Habit, without careful attention to appropriateness of the data set. The techniques chosen are often influenced by Selective perceptions, and Self-fulfilling prophecies. As noted before, there is an inherent tendency for individuals to seek confirmatory information which supports particular outcomes. The search and retrieval habits, are therefore, often based on experiences which have yielded desired outcomes in the past, even though they are based on Outcome irrelevant learning systems [10,11]. Under this tenet, the DM believes previous outcomes were optimal because he is unable to compare them against the outcomes from techniques which might have been more successful but were not used.

Assume that the DM finds that the mortgage applicant had a few payments which were 90 days or more late. While this may have been an aberration or beyond the control of the applicant (e.g. misdirected by the post office), the DM may view this as a key indicator of future loan defaults. If this had turned out to be a key indicator in the past, the DM may attempt to strengthen to his argument through search procedures which are intended to uncover confirmatory information only. While perhaps such searches may be appropriate in cases where the applicant truly is a credit risk, in this case it would not be.

## 5.2. L4: analysis biases (the IS-DM linkage)

After the information has been selected and retrieved, the DM must apply a set of evaluation techniques to the collected data set. Notable biases occur as a result of the data set selected, the analysis methodologies chosen, and the DM's heuristic base and implicit theories.

## 5.2.1. Data set collected

The set of ‘facts’ available to the DM impacts the accuracy of the results, the analysis techniques which can be applied, and the confidence associated with the outcomes. If too little, or inappropriate, data is gathered, problems of Representativeness $[41,42]$ may occur. The decision maker may, for example, attempt to generalize results based on a single observation. Unwarranted confidence may also be evidenced as a result of Redundancy, whereby the presence of superfluous information is deemed as confirmatory evidence.

The type of data collected also impacts analysis. Concrete information, or tangible events, tend to be much more salient than more abstract information [5]. Finally, the manner in which the data is organized can influence the DM's perception of data reliability. Information can result in very different attribution dependent upon Data presentation context.

We previously noted how a DM might seek confirmatory information based on isolated incidences of late payments by an applicant. If there are 10 late payments, the DM may focus on the number of late payments (concreteness) even though this might constitute $<1\%$ of the total transactions. The DM might also view this as representative behavior. Because late payment information may be reported as a total and individually on credit reports, and may occur multiple times in the data set, the DM may place additional emphasis on his assessment due to redundancy.

## 5.2.2. Technique misapplication

The methodologies chosen by the DM to analyze the collected data set is primarily a function of the DM's knowledge base. Regardless of the extent of knowledge, a number of commonly witnessed biases have been associated with this phase of the information processing loop. As with the retrieval and interpretation of data, individuals are prone to rely on Habit and Outcome irrelevant learning systems in selecting an analysis technique. Several specific biases have been associated with statistical analysis of data. Tversky and Kahnemann [42] have noted that individuals have difficulty recognizing The law of small numbers. Results are extrapolated from very small samples to larger populations without checking for significance. Misconceptions of regression may occur if an event varies significantly from the mean and people attribute the variation to some external agent or event and ignore the regression phenomenon [17]. Outliers may be used without regressing toward the mean to consider the effects of noisy measurement, as illustrated by the previous example of late payments.

## 5.2.3. Heuristics and implicit theories

When confronted with excessive amounts of information in decision making, individuals have a tendency to apply approximation methods to condense the amount and/or complexity of the data $[7,28,40]$ . One common simplification procedure is that of Anchoring and adjustment. This process involves the selection of a starting ‘anchor’ point (such as the mean) based on a past related decision, and then adjusting the value to reflect what the DM feels would be appropriate for the present decision. However, individuals often fail to systematically adjust the anchor sufficiently to account for the differences between the two situations $[36,42]$ , and to reflect the implications of the new evidence $[47]$ . When confronted with analyses which require the identification of correlations, individuals have a tendency to ignore the rate of occurrence of each event, and instead focus upon the Base rate of occurrence $[2,44]$ . This bias is especially prevalent when the

DM has concrete experience with one event, but only abstract of statistical exposure to a related event. In this case, the DM is likely to succumb to the Illusion of correlation [24], or the mistaken belief that two events covary when in fact they do not.

Assume that our DM has recently moved from accounts receivable (A/R) to the mortgage area. He may be familiar with returned checks and notes that an applicant has written 1,000 checks in 3 years, and only three have been returned. If the same applicant has missed three mortgage payments in the same period, the DM might view them as correlated (Illusion of correlation). Since he is more familiar with A/R standards, might be forgiving of the missed mortgage payments, even though the Base rate of occurrence (3/1000 versus 2/36) is considerably different. In this case, the DM is relying on Anchoring and adjustment to make the present decision.

## 5.3. L5: interpretation biases (the DM-decision linkage)

Once the analysis results have been obtained, further distortions can take place during interpretation and application of results to the decision to be made. The primary factors affecting this linkage are the DM's past experiences, his intrinsic beliefs, and the task environment.

## 5.3.1. Past experiences

Past experiences form the basis of a DM's reference point. This is especially true in new or unfamiliar situations, or those requiring higher degrees of subjective judgment. Reference effects occur because individuals recognize and evaluate stimuli in accordance with their past experiences [3,42]. This evaluation serves as a reference point for later decision making. For example, comments made by associates are interpreted favorably or unfavorably in accordance with the DM's opinion of the associate, not necessarily upon the appropriateness of the comment.

Fundamental attribution errors may occur if past successes are associated with inherent abilities, while failures are attributed to external factors or merely ‘poor luck’ [27,28]. Accordingly, previous success may be ascribed to the DM’s skill in dealing with a class of problems. Unexpected outcomes may be discounted as fluke occurrences. This bias may be further strengthened through the Illusion of control [13,24]. In chance situations, if the DM has experienced positive outcomes in spite of poor decision rules, he may assume an unreasonable feeling of control over situations. Other interpretation biases may also occur based on faulty processing schemas. For example, the interpretation of an unexpected occurrence of a ‘run’ of some events as indicative of the likely future occurrence of that event is referred to as Gambler’s fallacy [33].

Returning to the mortgage approval system, there are several opportunities for the DM to introduce biases on the basis of past experience. Reference effects could occur if another colleague casually notes that he knew someone with the same name as the applicant, and offers an unfavorable opinion that individual. Subconsciously, the DM may extend the colleague's opinion to the applicant, even though there is no basis for doing so. Fundamental attribution errors may occur if the DM does not realize that their past heuristics have become obsolete. For example, whereas the number of years at a current address may have been a good indicator of job stability in the past, mobility may be a better indicator in present times. It may be that longevity at a position is a sign that the applicant has limited skills. Unless the DM recognizes the changes which have taken place, he is likely to attribute defaults by such individuals as flukes.

## 5.3.2. Intrinsic beliefs

An individual's belief system generally serves as a filter through which information is selectively sorted according to their views and value system. In addition to the biases associated with the mechanism of Selective perception, there are a number of distortions which are typically associated with the interpretation of outcomes. For semistructured or unstructured problems the tendency toward Fact-value confusion is especially evident. The DM is able to justify their decision on their Expectations, and placing increased emphasis on information which confirms their previously held values [24].

## 5.3.3. Task environment

There are a number of specific biases which typically influence the manner in which a DM applies their findings to the task at hand. For tasks with which the DM has extensive experience, there is a propensity to repeat previous actions. However, the DM may overlook the uniqueness of the present decision, and overgeneralize the current situation. Such actions may lead to an abbreviated analysis and interpretation. The influence of Hindsight [14] implies that the DM believes that past outcomes will inevitably be repeated. As a result, there are certain Expectations made and, in accordance with the precepts of Selective perception and Wishful thinking, more credence is given to confirmatory than disconfirmatory evidence [24]. If there is an abundance of confirmatory data, the DM may feel overconfident about their assessment and not question its validity. If disconfirmatory data is more prevalent, the DM may overlook it or fail to revise previous interpretations as new information is received, a bias referred to as Conservatism [24,25]. If the evidence of disconfirmatory findings is significant, the DM may attempt to overcome their impact by relying on Spurious cues [16], whereby infrequently occurring events are viewed as common place. The DM may also overly rely on the attribute of Representativeness [41,42], or the belief that all members of a selective sample share the same characteristics. Similarly, the frequency of past occurrences is often considered merely as the number of successes to failures without concern to the ratio of successes to failures or its relevance to the task [17,45].

Assume that our mortgage applicant is an engineer for a military arms manufacturer. The DM might note that in the past, such individuals were stably employed, and seldom missed payments. He may have a great deal of supporting evidence, and may have favorable opinions of such individuals based on past experience. While the demand and job stability for this specialty has decreased significantly in the past years, the DM may place more emphasis on Hindsight and Expectations, and feel overconfident that past trends will continue. Even if confronted with disconfirmatory evidence, the DM may attribute the findings to a temporary phase, relating it to other short-lived phenomenon, or relying on Spurious cues.

## 6. Moderation of potential biases

As mentioned previously, it is neither feasible nor desirable to attempt to eliminate all of the biases listed above. In some cases, however, it may desirable and possible to alleviate some of their potentially negative impacts.

There has been considerable research conducted, and prescriptions suggested, on techniques for avoiding biases, and di-biasing those that do occur $[10,16,19,21,43]$ . Sage $[33]$ has outlined the 10 most commonly mentioned strategies (see Table 2 for summary):

1. Sample information from a broad database and be especially careful to include data which contains disconfirmatory information.

2. Include sample size, confidence intervals, and other measures of validity in addition to mean values.

3. Encourage the use of models and quantitative aids to improve upon information analysis through proper aggregation of acquired information.

4. Avoid the hindsight bias by providing access to information at critical past times

5. Encourage decisionmakers to distinguish between good and bad decisions from good and bad outcomes in order to avoid various forms of selective perception.

6. Encourage effective learning from experience. Encourage understanding of the decision situation and methods and rules used in practice to process information and make decisions.

7. Use structured frameworks based on logical reasoning.

8. Both quantitative and qualitative data should be collected, and all data should be regarded with ‘appropriate’ emphasis. None of the data should be overweighted or underweighted in accordance with personal views, beliefs, or values only.

9. People should be reminded, from time to time, concerning what type or size sample the data has been gathered from.

10. Information should be presented in several different forms and orderings.

As Table 2 indicates, these possible strategies can be associated with the biases previously described. For each bias there are a number of strategies which could be applied to moderate some of the negative outcomes associated with it. Similarly, each strategy can by applied to a number of biases. For example, the strategy of providing access to information at crucial past times could alleviate biases of Base rate, Conservatism, Habit and Hindsight. The bias of fact-value confusion could be moderated by using broad-based sample data which includes disconfirmatory data, encouraging effective learning from experience, and supplying both qualitative and quantitative data, each with an ‘appropriate’ emphasis (neither over- nor underweighed by personal beliefs).

Table 2
Moderation of biases $^{a}$

<table><tr><td>Moderating strategy bias</td><td>AA</td><td>Ava</td><td>BR</td><td>CI</td><td>Con</td><td>DPC</td><td>DS</td><td>ER</td><td>Exp</td><td>FVC</td><td>Fre</td><td>FAE</td><td>GF</td><td>Hab</td><td>Hin</td><td>ICn</td><td>ICo</td><td>LSN</td><td>OE</td><td>OILS</td><td>Ove</td><td>Red</td><td>RfE</td><td>RgE</td><td>Rep</td><td>SP</td><td>SFP</td><td>SC</td><td>WT</td></tr><tr><td>Use broad-based sample data w/disconfirmatory information</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td>X</td></tr><tr><td>Include sample size, confidence intervals &amp; other validity measures</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Encourage use of models &amp; quantitative aids on aggregated information</td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Provide access to information at critical past times</td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Encourage distinction btw. Good/bad decisions &amp; good/bad outcomes</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td>X</td><td>X</td></tr><tr><td>Encourage effective learning from exper./understanding of decision sit</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td></tr><tr><td>Use structured frameworks based on logical reasoning</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td></tr><tr><td>Use quantitative &amp; qualitative data w/appropriate emphasis</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Remind user of type/sample size</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td></td></tr><tr><td>Information should be presented in several different forms and orderings</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="30">Affected linkages:</td></tr><tr><td colspan="30">Designer</td></tr><tr><td>Inclusion biases (L1)</td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td></tr><tr><td>Construction biases (L2)</td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td></tr><tr><td colspan="30">DM</td></tr><tr><td>Retrieval biases (L3)</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td></td><td></td><td>X</td><td>X</td><td></td><td></td></tr><tr><td>Analysis biases (L4)</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Interpretation biases (L5)</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td></td><td>X</td><td>X</td><td></td><td></td><td></td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td><td>X</td><td>X</td></tr></table>

$^{a}$ AA: adjustment and anchoring; Ava: availability; BR: base rate; CI: concrete information; Con: conservatism; DPC: data presentation context; DS: data saturation; ER: ease of recall; Exp: expectations; FVC: fact-value confusion; Fre: frequency; FAE: fundamental attribution error; GF: gamblers fallacy; Hab: habit; Hin: hindsight; ICn: illusion of control; Ico: illusion of correlation; LSN: law of small numbers; OE: order effects; OILS: outcome irrelevant learning system; Ove: overconfidence; Red: redundancy; RfE: reference effect; RgE: regression effects; Rep: representativeness; SP: selective perceptions; SFP: self-fulfilling prophecies; SC: spurious cues; WT: wishful thinking.

It is beyond the scope of this paper to attempt to discuss all of the relationships between the biases and moderating strategies given. Determining the impact of each of the strategies in alleviating the untoward effects of biases on information system development and usage requires extensive empirical investigation.

## 7. Conclusion

This paper is intended to provide an overview of some of the IS designer and DM biases which can occur at various phases in the IS development and information processing cycle. The processing model presented is intended as a mechanism for categorizing bias occurrences according to the activities which take place in the information processing cycle.

Our main intent is to make the participants in the systems development and usage process, especially the IS Designer, aware of the potentially detrimental affects of biases. However, we do not believe that it is beneficial, or possible to eliminate all biases. As discussed, biases are often necessary filtering mechanisms which allow both the IS designer and the DM to deal with enormous amounts of data and make reasoned decisions about a problem. Attempts to alleviate such biases could hinder successful decision making strategies.

Nonetheless, there are obvious biases which have negative effects and which can be moderated in the construction of information system. We have attempted to address some of these in the previous section. It remains the task of the IS designer to determine which of these biases should be addressed, and the best manner in which to moderate the biases.

Future research is needed to evaluate the impact of each of the measures suggested on the decision making process. Given the number moderating techniques which could be applied, additional study is necessary to determine if there are combinatorial affects.

The study has confined itself to a common, but small-scaled, subset of information systems. We have assumed that there is only one IS designer, or a few systems analysts under the direction of a single designer, who is responsible for the construction of an information system. We have also assumed that there is essentially one user, or decision maker, of the system at any given time. As noted, while some of the biases discussed may be alleviated when the system is developed by a team of designers and/or used by a group of decision makers, a number of different biases may also be introduced. Additional investigation into this area is needed.

## References

[1] R.P. Abelson, Psychological status of the script concept, American Psychologist, 1981.

[2] M. Bar-Hillel, The base-rate fallacy in probability judgments, ACTA Psychology 44, 1980, pp. 211–213.

[3] F.H. Barron, R. John, Assessment of multiplicative utility functions vias holistic judgments, Organizational Behavior and Human Performance 25, 1980, pp. 365–374.

[4] I. Benbasat, R.N. Taylor, Behavioral Aspects of information processing for the design of management information systems, IEEE Transactions on Systems, Man and Cybernetics 12 (4), 1982, pp. 439–450.

[5] E. Borgida, R.E. Nisbett, The differential impact of abstract vs. concrete information in decisions, Journal of Applied Social Psychology 7, 1977, pp. 258–269.

[6] D.E. Broadbent, The well-ordered mind, American Educational Research Journal 3, 1966, pp. 281–297.

[7] J.S. Brunner, R. Oliver, P.M. Greenfield, Studies in Cognitive Growth, Wiley, New York, 1966.

[8] P.A. Domas, C.R. Peterson, Probabilistic information processing systems: evaluation with conditionally dependent data, Organizational Behavior and Human Performance 7, 1972, pp. 77–85.

[9] W. Edwards, L.D. Phillips, W.L. Hays, B.C. Goodman, Probabilistic information processing systems: design and evaluation, IEEE Transactions in Systems, Science and Cybernetics (SSC) 4, 1960, pp. 248–265.

[10] H.J. Einhorn, Learning from experience and suboptimal rules in decision processing, in: T.S. Wallsten (Ed.), Cognitive Processes in Choice and Decision Behavior, Lawrence Erlbaum, Hillsdale, NJ, 1980a, pp. 1–20.

[11] H.J. Einhorn, Overconfidence in judgment, in: R.A. Shweder (Ed.), Fallible Judgment in Behavioral Research, Jossey Bass, San Francisco, 1980b, pp. 1–16.

[12] M. Eisenstadt, Tales of debugging from the front lines, in: C.R. Cook, J.C. Scholz, J.C. Spohrer (Eds.), Proceedings of the Fifth Workshop on Empirical Studies of Programmers, Norwood, NJ, 1993.

[13] B. Fischhoff, Fault trees: sensitivity of estimated failure probabilities to problem presentation, Journal of Experimental Psychology: Human Perception and Performance 4, 1978, pp. 342–355.

[14] B. Fischoff, For those condemned to study the past: reflections on historical judgment, in: R.A. Shweder (Ed.), Fallible Judgment in Behavioral Research, Jossey Bass, San Francisco, 1980, pp. 79–84.

[15] D.L. Hamilton, Cognitive biases in the perception of social groups, in: J.S. Carroll, J.W. Payne (Eds.), Cognition and Social Behavior, Erlbaum Associates, Hillsdale, NJ, 1976.

[16] R.M. Hogarth, S. Makridakis, Forecasting and planning: an evaluation, Management Science 27 (2), 1981, pp. 115–138.

[17] R.M. Hogarth, Judgment and Choice: The Psychology of Decisions, Wiley, New York, 1987.

[18] G.P. Huber, The nature of organizational decision making and the design of decision support systems, MIS Quarterly (1981) 1–10.

[19] E.E. Jones, G.R. Goethals, Order effects in impression formation: attribution context and the nature of the entity, in: E.E. Jones, D.E. Kanouse, H.H Kelley, R. Nisbett, S. Valins, B. Weiner (Eds.), Attribution: Perceiving the Causes of Behavior, General Learning Press, Morristown, NJ, 1972.

[20] L.R. Keller, The effects of problem representation on the sure thing and substitution principles, Management Science 31, 1985, pp. 738–751.

[21] D. Kahneman, A. Tversky, On the psychology of prediction, Psychology Review 80, 1973, pp. 237–351.

[22] D. Kahneman, A. Tversky, Prospect theory: an analysis of decisions under risk, Econometrica 47 (2), 1979, pp. 263–291.

[23] T.W. Lauer, A.M. Jenkins, Implications of behavioral decision theory for decision support system implementation and research, Discussion paper no. 273, Division of Research, School of Business, Indiana University, Bloomington, Indiana, 1984.

[24] S. Makridakis, S.C. Wheelwright (Eds.), Forecasting, North-Holland, New York, 1979.

[25] M., Moskowitz, R.E. Schaefer, K. Borcherding, Irrationality of managerial judgments: implications for information systems, Omega 4 (2), 1976, pp. 125–140.

[26] U. Neisser, Cognition and Reality, Freeman, San Francisco, CA, 1976.

[27] R.E. Nisbett, T.D. Wilson, Telling more than we know: verbal reports on mental processes, Psychological Review 84 (3), 1977, pp. 231–259.

[28] R.E. Nisbett, L. Ross, Human Inference: Strategies and Shortcomings of Social Judgment, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[29] D.B. Paradice, J.F. Courtney, Controlling bias in user assertions in expert DSS, Journal of Management Information Systems 3 (1), 1986, pp. 53–64.

[30] J.B. Pryor, M. Kriss, The cognitive dynamics of salience in the attribution process, Journal of Personality and Social Psychology 35 (1), 1977, pp. 49–55.

[31] E. Rosch, B.B. Lloyd, Cognition and Categorization, Erlbaum Associates, Hillsdale, NJ, 1978.

[32] D.N. Rubie, N.S. Feldman, Order of concensus, distinctiveness, and consistency information and causal attribution, Journal of Personality and Social Psychology 42 (5), 1976, pp. 930–937.

[33] A.P. Sage, Behavioral and organizational considerations in the design of information systems and processes for planning and decision support, IEEE Transactions on Systems, Man and Cybernetics 11 (9), 1981, pp. 640–678.

[34] H.A. Simon, Theories of decision making in economies and behavioral science, American Economic Review 49 (3), 1959.

[35] H.A. Simon, Rationality as a process and as a product of thought, American Economic Review 69, 1978.

[36] P. Slovic, S. Lichtenstein, Comparison of Bayesian and regression approaches to the study of information processing in judgment, Organizational Behavior and Human Performance 6, 1971, pp. 649–744.

[37] W. Stacy, J. MacMillan, Cognitive bias in software engineering, Communications of the ACM 38 (6), 1995, pp. 57–63.

[38] B. Teasley, L.M. Leventhal, S. Rohlman, Positive test bias in software testing by professionals: what's right and what's wrong, in: C.R. Cook, J.C Scholz, J.C. Spohrer (Eds.), Proceedings of the Fifth Workshop on Empirical Studies of Programmers, Norwood, NJ, 1993.

[39] W. Teng, V. Sethi, Psychological studies of decision making and it's implications for DSS, in: Proceedings of the Decision Sciences Institute, Boston, 1987.

[40] A. Tversky, Intransitivity of preferences, Psychological Review 76 (1), 1969.

[41] A. Tversky, Availability: a heuristic for judging frequency and probability, Cognitive Psychology 5, 1973, pp. 207–232.

[42] A. Tversky, D. Kahneman, Judgment under uncertainty: heuristics and biases, Science 185, 1974, pp. 1124–1131.

[43] A. Tversky, D. Kahneman, The framing of decisions and the psychology of choice, Science 211, 1981a, pp. 453–458.

[44] A. Tversky, D. Kahneman, Evidential impact of base rates, Technical Report 4, Department of Psychology, Stanford University, May 1981b.

[45] W.C. Ward, H.M. Jenkins, The display of information and the judgment of contingency, Canadian Journal of Psychology 19, 1965, pp. 231–241.

[46] P.T.P. Wong, B. Weiner, When people ask ‘why’ questions, and the heuristics of attributional search, Journal of Personality and Social Psychology 40, 1981, pp. 650–663.

[47] W.F. Wright, Cognitive information processing biases: implications for producers and users of financial information, Decision Sciences 11, 1980, pp. 284–298.
