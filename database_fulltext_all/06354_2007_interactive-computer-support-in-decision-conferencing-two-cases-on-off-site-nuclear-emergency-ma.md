---
otero_id: 6354
otero_key: "WK63VNBE"
title: "Interactive computer support in decision conferencing: Two cases on off-site nuclear emergency management"
authors: "Jyri Mustajoki; Raimo P. Hämäläinen; Kari Sinkko"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.07.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Interactive computer support in decision conferencing: Two cases on off-site nuclear emergency management

Jyri Mustajoki <sup>a,⁎</sup>, Raimo P. Hämäläinen <sup>a</sup>, Kari Sinkko 1

<sup>a</sup> Helsinki University of Technology, Systems Analysis Laboratory, P.O. Box 1100, 02015 HUT, Finland <sup>b</sup> STUK— Radiation and Nuclear Safety Authority, P.O.Box 14, 00881 Helsinki, Finland

Received 15 March 2006; accepted 28 July 2006 Available online 18 September 2006

## Abstract

In this paper, we study the new opportunities offered by the interactive use of advanced multicriteria software in decision conferencing. We analyze and make observations on this approach in two one-day decision conferences on the planning of later phase countermeasures in off-site nuclear emergency management. The participants' individual use of the software in the preference elicitation phase was an essential new characteristic of these conferences. It turned out to be a feasible and well accepted process. We shall discuss the requirements for the facilitation and computer support in this kind of an approach. © 2006 Elsevier B.V. All rights reserved.

Keywords: Multicriteria decision support systems; Decision conferencing; Nuclear emergency management; Multicriteria decision analysis

## 1. Introduction

Decision conferencing is a collaborative way to support group decision making [14,35,36]. In decision conferences – also called facilitated or moderated decision analysis workshops – all the parties involved in the decision making are gathered together to systematically discuss and analyze the problem. The objective is to constructively deal with the conflicting issues at hand so that a common understanding of the problem can be achieved. Decision analytical software is typically used to model the different views of the participants and to evaluate the strategy alternatives equally and in an auditable way.

Multiattribute value theory (MAVT) is a decision analytical approach for supporting the evaluation of multiple alternatives on multiple criteria [25]. In MAVT, all the relevant objectives of the problem are structured hierarchically into a value tree having the overall objective on the top and measurable attributes on the lowest level. The alternatives are rated on each attribute, and the consequence ranges of the attributes are given weights to reflect their relative importance. The overall values of the alternatives are obtained as a weighted sum of the alternatives' ratings with respect to the attributes.

In this paper, we study new ways of using interactive MAVT software in decision conferencing. Our focus is on the setting where each decision maker (DM), or a representative of an interest group, independently uses the advanced MAVT software to elicit her preferences on a jointly structured value tree. The obtained preference models are then analyzed in collaboration with an aim to get a perspective of the different stakeholders by means of their preferences. We utilize a portable group decision support system (GDSS) with advanced multicriteria software called Web-HIPRE (HIerarchical PREference analysis on the Web) [21,30]. The webbased architecture of Web-HIPRE allows the distributed MAVT modeling and studying other stakeholders preference models through an intranet or the Internet. The individual preferences can also be combined into group preferences describing the average overall preferences of the group.

In terms of individual and interactive use of multicriteria GDSS, this approach should be of wider interest, as multicriteria software has traditionally been run by the decision analyst or her assistant to create a joint group preference model. In addition, earlier research on GDSSs (see e.g. Refs. [12,13]) has mainly concentrated on studying factors such as group dynamics, effects of communication mode or the process structure, but to our knowledge, the way we applied advanced MAVT software interactively has not been previously studied in a controlled workshop. Sometimes individual preference models have been elicited too, as has been done in decision analysis interviews (see e.g. Refs. [14,27]). However, also these models have been typically constructed and the preferences have been elicited in intensive collaboration with the decision analyst.

We analyze and make observations on the use of this approach in two case studies for the planning of later phase countermeasures in a hypothetical nuclear accident. Besides collecting experiences on the use of multicriteria software, our objective is to study the applicability of the approach in nuclear emergency management. Issues in nuclear safety often involve multiple policy alternatives and multiple shareholders having different interests, and decision analytical approaches have been successfully applied in group planning (see e.g. Refs. [14,23,26]). Our cases deal with countermeasures for (i) milk production, and (ii) the clean-up of inhabited areas. In both cases, a one-day decision conference exercise was held to consider the problem from various perspectives. A decision conference was originally designed to be a two-or three-day event, but we found one day to be a sufficient and convenient to fit into the timetables of typically busy participants. However, this intensive framework poses requirements to both the prearrangements and the facilitation, which shall also be discussed. Our conferences were arranged in a decision room via the intranet, but the software would also allow remote participation via the Internet. We shall also briefly discuss these opportunities.

This paper is organized as follows. In Section 2, we discuss the new opportunities for the use of multicriteria methods and computer support in decision conferencing. The approach applied in this paper is described in Section 3, and the cases in Section 4. In Section 5, we discuss the experiences obtained from the conferences and from the use of the GDSS. Section 6 concludes the paper.

## 2. Computer support in decision conferencing

Decision conferencing is a GDSS design where a computer system is applied to support an intensive faceto-face meeting aiming to build a consensus on a focal problem [29]. The objective is to combine group process facilitation, preference modeling and information technology since a group can achieve better results than an individual working on her own [40]. A decision conference is led by a neutral facilitator whose role is to enhance the communication between the participants and to get them to constructively deal with the conflicting issues at hand [35,36]. The facilitator is supported by a decision analyst and assistants taking care of, for example, the running of the computer-aided models for structuring and preference elicitation.

DeSanctis and Gallupe [9] classified the group decision support into three levels: (1) process support for removing communications barriers (e.g. electronic messaging), (2) decision making support for the modeling and the analysis of the decision problem at hand, and (3) rules of order for controlling the pattern of communication. Decision conferencing typically employs level 2 support with decision analytical tools, but level 1 support can also be applied to facilitate better communication between the participants.

## 2.1. Multicriteria tools

The recent development on multicriteria tools has given new opportunities for interactive decision support in decision conferencing. Today's general purpose MAVT software (see e.g. Ref. [24]) provides tools for graphically structuring and analyzing the problem, usually offering several different options to communicate the results. The software has easy-to-use user interfaces making it possible for the participants to use the software even by themselves. Most software focuses on the analysis of individual models, but some software also provides group support facilities, for example, by voting or the aggregation of individual preferences into group preferences. For recent surveys of multicriteria software, see e.g. Refs. [8,28,48].

Our basic hypothesis is that level 2 support, such as the use of advanced multicriteria tools, can substantially enhance the decision making process and improve the shared understanding among the participants. This has also been postulated in earlier literature. For example, based on the evaluation of 184 experiments and 54 case and field studies on group support systems, Fjermestad and Hiltz [12,13] suggest that the success rate of an application can be expected to be at its best when using level 2 systems with specialized tools built in. Bose et al. [6] studied the employment of multicriteria methods in GDSS applications arguing that the use of multicriteria methods would be a valuable asset in the evaluation of alternatives in group decision making situations.

It is quite surprising that, in spite of the demonstrated potential of multicriteria decision analytical methods, these have rarely been employed in GDSSs. For example, in the evaluation of Fjermestad and Hiltz [13], only two of the 54 case and field studies [1,38] made use of multicriteria methods, although level 2 tools were applied in 47 of these studies. We believe that one reason for this is that the use of multicriteria methods requires special skills from the facilitator, but the education and training for these skills are typically not included in information systems programs at universities. One of the objectives of this paper is to encourage and demonstrate the use of multicriteria methods and the related tools in group decision support.

One should note that the individual use of the software, as applied in our approach, requires much more of the process and software than the use where an analyst operates the software. It also poses general requirements for the usability of the methods [47]. The recognition of the possibility of behavioral biases (see e.g. Refs. [37,49]) is also essential to obtain reliable results.

## 2.2. Opportunities of the World Wide Web

The proliferation of the World Wide Web has given new opportunities for supporting group decision making (see e.g. Refs. [5,44]). These include platform-independency, global communication opportunities, easy accessibility and multimedia facilities. In decision conferencing, the web can be utilized to act as a communication channel for collecting and aggregating the results, and the external web resources can be used as information sources for supporting the process.

The decision conferencing approach meets several objectives of public participation [15]. These include, for example, trust building, reducing conflicts and increasing stakeholder acceptability. In educating the public, decision conferencing can assist the representatives of the stakeholder groups to learn and help to further educate their constituencies. One can also use other participation mechanisms in parallel to increase the overall effectiveness of the process. These include also Webbased approaches such as web pages to inform the public and web questionnaires to collect opinions.

Crisis and emergency response has been raised as one of the areas where special applications of virtual workspaces are most needed and useful (see e.g. Refs. [7,33]). Nuclear accidents are rapidly advancing emergencies and the affected and responsible parties are often geographically widely distributed, even in different countries and perhaps under different legislation. In the future, there could be web-based collaboration platforms with familiar user interfaces for nuclear accidents. We do not, however, explicitly consider remote participation here, but shall briefly discuss the different ways of using the web to support decision conferences.

## 3. Decision conferences with individual multicriteria modeling and analysis

## 3.1. Group decision support

Our GDSS setting consists of several portable computers connected through a wireless local area network (WLAN), and of a projector and a printer. Such a portable facility is readily installable in various locations, and would be especially suitable in crisis situations. In the setup, one computer acts as a server running the software and taking care of the information exchange via the WLAN. It can also provide a connection to the Internet. Any computer connected to the WLAN can act as a client and use the software. In our study, the system was set up in a regular meeting room but such a system also allows, for example, remote participation through the Internet.

The preference modeling process is based on the Web-HIPRE software which is available on the Decisionarium Web site for multicriteria decision support [17,19]. Web-HIPRE implements the MAVT approach where the overall value of each alternative is composed of the ratings of the alternatives' consequences with respect to each attribute, and of the weights of the attributes representing the relative importance of these. An additive value function can be used if the attributes are mutually preferentially independent (see e.g. Ref. [25]). Then, the overall value of an alternative described by the consequence vector $\mathbf { x } { = } ( \mathbf { x } _ { 1 } , . . . , \mathbf { x } _ { n } )$ is

$$
v (\mathbf {x}) = \sum_ {i = 1} ^ {n} w _ {i} v _ {i} (\mathbf {x} _ {i})\tag{1}
$$

where n is the number of attributes, $\mathbf { X } _ { i }$ is the consequence of this alternative with respect to attribute i, $\nu _ { i } ( \mathbf { x } _ { i } )$ is its rating on [0,1] scale, and $w _ { i }$ is the weight of attribute i.

The weights are normalized to sum up to 1. Web-HIPRE's group model facility also allows the aggregation of the individual preferences into group preferences by using the weighted arithmetic mean method [25,39,42].

## 3.2. Phases of the conference

The decision support process followed in our approach is a typical one including the following four phases: (i) introduction to the approach and the case, (ii) structuring of the value tree, (iii) elicitation of the preferences, and (iv) analysis of the results (see Table 1). Each of these phases lasts approximately one and a half hours. Thus, with the breaks the duration of the conference is a full workday. The decision support group includes a neutral facilitator, a decision analyst, experts in the case, and two technical assistants.

## 3.2.1. Introduction

First, the facilitator describes the decision conferencing approach and the main features and steps of the

Table 1 Phases of the conferences with individual multicriteria modeling Introduction Overview of decision conferencing and decision analysis Description of the case Structuring of the value tree An open discussion leaded by the facilitator The participants allowed to suggest changes into the value tree Suggestions collaboratively discussed and approved / rejected The exact meanings of the attributes specified The value tree updated according to the suggested changes and projected on the wall during the discussion Preliminary set of alternatives introduced (defined in preparing meetings) Alternatives collaboratively discussed and modified, if needed → A joint value tree Elicitation of preferences Each group individually works with the joint value tree Weighting of the attributes with SWING weighting Evaluation of the soft attributes with direct rating Calculable data (e.g. costs) estimated beforehand → Instances of the same value tree reflecting the preferences of the different participant groups Analysis of the results and creating a group choice Each model collectively analyzed Characteristics of the model pointed out Aim to achieve a view of the other stakeholders' preferences Sensitivity analysis on the weights of the attributes Group model created Average overall values of the alternatives Sensitivity analysis on the weights of the groups Collaborative discussion on the results → A common recommendation for the final strategy

process. Next, the case at hand and all the necessary background information are described. Our cases dealt with nuclear emergency, and thus the meeting was started off by a briefing on the general issues and legislation concerning radiation related risks and the principles of radiation protection. This was followed by a nuclear expert describing the accident, the consequences of the possible countermeasure actions and their effectiveness.

## 3.2.2. Structuring of the value tree

The multiattribute value tree is structured in an open discussion led by the facilitator. During the discussion, the participants are allowed to suggest new attributes to the value tree and specify the existing ones. The suggestions are thoroughly discussed and it is decided in collaboration which attributes to include in the value tree. The facilitator keeps up the discussion to allow the opinions of all the participants to come up. The aim is to also define the attributes in detail in order to eliminate any confusion about their meanings. The value tree is projected on the wall all the time and updated according to the jointly accepted changes by the decision analyst (see Fig. 1).

The set of possible alternatives is defined in the same way. It is often not possible to evaluate the consequences of the alternatives on-line but a preliminary set of alternatives can be defined beforehand in preparatory meetings. New alternatives can also be considered, but the consequences of these may not be evaluated as accurately as those of the preliminary alternatives.

## 3.2.3. Elicitation of preferences

The elicitation of the participants' preferences is carried out with Web-HIPRE operated by the participants themselves. The participants representing the same stakeholder group work in a group of two or three people. Each group has a portable computer in their use to give their preferences on the jointly structured model. As a result, we get the weights on the same value tree reflecting the preferences of each group. Before each task, the facilitator describes the task and the needed background on the methods to the participants while the decision analyst demonstrates on the screen how to carry out the task with Web-HIPRE. The participants also have technical assistants available to answer their questions and to assist them.

First, the alternatives are evaluated with respect to each attribute. Ratings for the measured values of the technical attributes can be calculated beforehand but for subjective attributes the participants need to provide the rating on a 0–1 rating scale. In practice, the participants carry out the rating of the alternatives independently with the direct rating mode of Web-HIPRE.

![](/api/attachments/WK63VNBE/fulltext/images/cf9d8cef9bba728dfaee3854ff88e1024e2ef1336d01efa0eac398ecef1f164b.jpg)  
Fig. 1. Value tree of the Milk case.

The relative importance of the attributes is elicited with the SWING method [50]. In SWING, the DM is first asked to assign 100 points to the most important attribute change from its lowest level to its highest level. Then, she is asked to give fewer points to the other attributes to denote the relative importance of the ranges of these attributes. The actual weights indicating the relative importance of the attributes are obtained by normalizing the sum of the given points to one (see Fig. 2).

3.2.4. Analysis of the results and creating the group choice

As a result, we get the overall values of the strategy alternatives for each group. These are analyzed together by projecting them one by one on the screen, and by discussing them jointly. For each model, the facilitator points out its essential characteristics to achieve an understanding of the concept and the preferences of this group. The contribution of the different attributes is studied by breaking down the overall values into corresponding components. A single parameter sensitivity analysis is carried out to study the changes in the overall values with respect to variations on the ratings and weights.

![](/api/attachments/WK63VNBE/fulltext/images/ef7228d7d6aa3e89ed2b1cbf9ecaa6f12b8e17a68c13a037e9553f6d8dc62437.jpg)  
Fig. 2. SWING weighting window of Web-HIPRE.

The individual preferences are also combined into group preferences by using Web-HIPRE's group model facility. In the group model, each group is represented by an attribute in a value tree (Fig. 3) and the ratings of the alternatives on these attributes are the overall values of the corresponding group. Usually it is convenient to start by weighting the groups equally. Then, the group model indicates the averages of the overall values for the alternatives. One can also change the groups' weights but it is easiest to study the effects of differences on the importance of the groups with sensitivity analysis on the group weights.

Finally, possible compromise alternatives are redesigned and the recommendations for a final strategy are collaboratively decided. After the conference, the results as well as the other material obtained in the conference are published on the web. The models created in the conferences can even be made available to the general public on Web-HIPRE. This option may not, however, prove to be a feasible one in practice, as it is likely that only few people could open and analyze these models in the software.

## 4. Nuclear accident cases

In order to cope with possible future nuclear accidents, planning of both the decision making process and the early and later phase countermeasures is needed to ensure rational and transparent decisions. In the early phases of a real accident, urgent precautionary protective actions are required immediately, and thus a regulatory contingency plan is needed. However, in the later phases information about the severity of the accident and more time to consider the required actions is usually available. Then, the characteristics of the accident can be taken into account in the planning of the countermeasures.

Two decision conference exercises described in this paper were arranged according to the framework described in Section 3. The main objectives were to understand better the other stakeholders' views, to plan different later phase countermeasures, and to improve the participants' preparedness to meet a real accident situation. The conferences were arranged to simulate real emergency situations as realistically as possible to get experiences on the applicability of the decision conferencing approach in a case of a real emergency. Also, one important objective of the conferences was to help us to create a network of key players in nuclear emergency management [45].

![](/api/attachments/WK63VNBE/fulltext/images/f686cff075eaac8abd7ff002189db86c9bc1ff75f632b473621985fb1c129c61.jpg)  
Fig. 3. Group model of the Milk case.

The conference dealing with the protective actions for the milk production (Milk case) was arranged in 2000, and the other dealing with the clean-up actions in inhabited areas (Urban case) in 2004. In both cases, a hypothetical accident had occurred in a nuclear power plant in Finland. It was assumed that precautionary protective actions had been taken immediately after the accident and at the time of the conference – a week after the accident – the fallout area had been identified by measurements revealing the severity of the accident. The decisions on the protective actions decided in the conferences were supposed to be implemented within the next few days.

In the Milk case, we focused on testing (i) the format of a one-day conference with an interactive MAVT software, and (ii) the decision support system which at the time of the conference was very new. In the Urban case, the focus was on deepening our understanding on how best to arrange this type of a conference. The Milk case acted as a promoter for launching the EVATECH project under the fifth EURATOM framework program of the EU, wherein similar workshops were arranged in seven European countries (see e.g. Ref. [16] or www. evatech.hut.fi). The Urban case was organized as a part of the EVATECH project. It is also worth noticing that since the positive experiences of these cases, the Web-HIPRE software has been implemented as a part of the related RODOS system (Real-time On-line DecisiOn Support system) [10].

The participants of the conferences were authorities and high-level representatives from the organizations that would also be involved in the decision making process in a real accident situation (Table 2). Before the conferences, we organized preparatory meetings with the staff of the radiation authority and other experts on the issues at hand to learn the need for background information on the problem, and to calculate the impacts of different countermeasures. An information package was delivered to the participants a couple of days before the conference so that they could get acquainted with the emergency situation. After the conferences, the results were published on the conference web sites (see www. riihi.hut.fi/stuk/indexeng.html and www.evatech.hut.fi).

## 4.1. Milk case

In the Milk case, the radioactive fallout was assumed to cover a major milk production area in western Finland with a diameter of approximately 150 km. It was estimated that without any actions the use of contaminated dairy products would cause approximately 100 cancer incidents. For the first week after the accident, the cattle was sheltered and provided with clean fodder. Our focus was on weeks 2–12, when the cattle would normally be outside, as the accident was assumed to occur in early June. For further details of the case, see Ref. [3].

Table 2  
Participants of the conferences

<table><tr><td>Milk conference (13 participants)</td><td>Urban conference (13 participants)</td></tr><tr><td>Ministry of Agriculture and Forestry (2 persons)</td><td>Ministry of Social Affairs and Health (1 person)</td></tr><tr><td>National Food Agency (1)</td><td>Ministry of Interior (1)</td></tr><tr><td>Finnish Food and Drink Industries’ Federation (2)</td><td>Rescue Office of the County Administrative Board of Southern Finland (1)</td></tr><tr><td>Rural Advisory Center of the Province of Etelä-Pohjanmaa (1)</td><td>Rescue Office of the Town of Loviisa (1)</td></tr><tr><td>Valio Ltd (dairy industry) (2)</td><td>Technical Office of the Town of Loviisa (3)</td></tr><tr><td>Radiation and Nuclear Safety Authority (5)</td><td>Federation of municipalities of Loviisa region (1)Employment and Economic Development Center for the Province of Uusimaa (1)Environment Agency of the Province of Uusimaa (2)Radiation and Nuclear Safety Authority (2)</td></tr></table>

The structuring of the value tree started from a preliminary tree that was constructed in the preparatory meetings with two or three experts. During the discussion in the conference, some modifications to the tree were suggested. However, the participants finally ended up using the preliminary tree, which consisted of three attribute groups: health effects, sociopsychological effects and costs (Fig. 1).

The considered countermeasures were (i) provision of uncontaminated fodder (‘Fod’), (ii) processing of the milk into other products such as cheese (‘Prod’), (iii) banning the milk (‘Ban’), and (iv) doing nothing (‘—’). The actual six strategy alternatives (see Fig. 1) were defined in the preliminary meetings and they were combinations of the countermeasures for two time periods, that is, for weeks 2–5 and 6–12 after the accident. For example, on alternative ‘Prod + Fod’ countermeasure ‘Prod’ is carried out during weeks 2– 5 and ‘Fod’ during weeks 6–12. Technical data of the countermeasures (i.e. the number of cancer incidents and the costs) was estimated beforehand with the RODOS system.

Fig. 2 shows an example of the attribute weighting of one group with the SWING method in Web-HIPRE. The top alternative for all the groups were among the ones where clean fodder is provided for at least either of the periods (‘Fod + —’, ‘Fod + Fod’, ‘Prod + Fod’ and ‘Ban + Fod’), which were the top alternatives also in the group model (Figs. 3 and 4). Strategy no actions (‘— + —’) was among the three worst alternatives for every group.

Besides SWING weighting, we also tested the Interval SMART/SWING method [31,43] with the WINPRE software (Workbench for INtercative PREference programming) [20] for studying the sensitivity of the result to different kinds of uncertainties. The results of this model were not collectively analyzed but each group could individually study their results. For details on how to carry out interval sensitivity analyses in MAVT, see Ref. [32].

After the analysis of the results, approval voting on the alternatives was carried out with the Opinions-Online software [22] for global participation, voting, surveys and group decisions. Strategies ‘Fod + Fod’ and ‘Prod + Fod’ were both approved by all the participants, and in the concluding discussion it was collectively decided that either of these could be given as a final strategy recommendation.

## 4.2. Urban case

In the Urban case, the worst radioactive fallout was assumed to cover the nearby town of Loviisa and a part of the Pernaja municipality (referred to as Area 1).

However, as a whole the fallout would reach Helsinki, the capital of Finland, located 90 km west from Loviisa. It was estimated that without any actions the accident would cause 261 cancer incidents, of which 180 in Area 1. It was assumed that, for the first week, 8400 inhabitants living in Area 1 were evacuated, and the focus in the conference was on actions starting 1 week after the accident. For details, see Ref. [46].

The structuring of the value tree started from a list of five preliminary attribute groups (health, socio-psychological effects, environment, economy, technical issues). First, the participants suggested possible attributes which were all listed under these groups. The attributes were then collaboratively studied one by one, and on each attribute, the relevancy of it was discussed and the meaning specified. It was also discussed whether some closely related attributes could be combined together to make the value tree smaller, and consequently, to expedite preference elicitation on the next phase. Eventually, the attributes were grouped and in the final value tree there were five attributes which consisted of several different aspects (Fig. 5).

The considered countermeasures were the continuation of the evacuation of Loviisa and the clean-up of the urban environment (for details, see Ref. [2]). The latter one includes actions such as washing outer surfaces of houses, sweeping streets and cutting the grass, which have been found to be effective ways to reduce radioactivity in urban environment [4]. The actual strategy alternatives were combinations of actions of various extents. Strategy A consisted of large scale clean-up actions up to Helsinki and the evacuation of Loviisa for a further month, whereas strategy E consisted of actions only in Loviisa. Strategies B, C and D were variations in between these. In addition, there was strategy min, in which only some minor and very cheap clean-up actions are made in Loviisa, and strategy 0, in which nothing is done. In the beginning of the conference, strategy max, where the town of Loviisa is permanently resettled and very powerful actions are performed on the whole area, was also considered. However, the participants considered this strategy as clearly unrealistic, and it was omitted. The weighting of the attributes and the evaluation of the alternatives were carried out similarly to the Milk case.

![](/api/attachments/WK63VNBE/fulltext/images/998b835e3cce1839e27b4fd5a5ca2f8f2d1930d51ab4bbc50007f0ed65fb0709.jpg)  
Fig. 4. Group priorities of the strategies in the Milk case.

![](/api/attachments/WK63VNBE/fulltext/images/09d8d591bcc7af4d10b9acc5b2e31ec79865f19a24d1d28bf238195ccc4338b4.jpg)  
Fig. 5. Value tree of the Urban case.

For all the groups, the most preferred strategy was among strategies A–D. In the group model, strategy C was the most preferred one (Fig. 6). After collectively analyzing the models of each group, we tested whether the existing strategies could be further improved with some modifications. Strategy C was taken as a basis for the discussion as it was the most preferred alternative for most groups. It was found out that this alternative could become more efficient with small enlargements on the clean-up areas. It was also discussed that besides evacuating Loviisa for a month, it would be useful to also evacuate some badly contaminated areas in the surroundings of it. Thus, a new strategy C\* reflecting these changes was created. Although the exact attribute values of this strategy could not be calculated in such a short time, these were collectively estimated on a basis of strategies B and C. Finally, strategy C\* was collectively approved as the common recommendation for a final strategy.

## 5. Experiences from the conferences

In general, the feedback from the conferences was very positive. In the questionnaires filled after the conferences, all the participants in both conferences agreed that the conference exercise was useful in general (Table 3). Especially, the result where 12 of 13 participants in the Urban case strongly agreed with this, provided strong evidence for the applicability of the approach.

The tested one-day time frame proved to be feasible, but it set high requirements to the conference arrangements. Several preparatory meetings and extensive groundwork were needed to obtain a preliminary overview of the problem and information about the possible countermeasures. In the Urban case, a full-length conference rehearsal with a few experts from the Radiation and Nuclear Safety Authority of Finland was arranged. This appeared to be highly useful, hence we could estimate the time needed for different phases of the conference and identify the issues that are likely to cause discussion in the actual conference. The one-day time frame also limited the possibilities to make essential procedural changes during the session. For example, creating a totally new strategy alternative was not possible due to lack of time to calculate the consequences of the alternatives, although some small changes could be estimated on a basis of the other strategies. One should, however, note that since these conferences, the integration of Web-HIPRE as a part of the RODOS system has induced a further development of the system to be able to estimate the consequences of new strategies even on-line.

![](/api/attachments/WK63VNBE/fulltext/images/700902f878c1bfbe0b2d4314f4f6d31f562796769fa204845b5e5548e28a878b.jpg)  
Fig. 6. Group priorities of the strategies in the Urban case.

The participants evaluated the Urban case much more positively than the Milk case. When considering the reasons for this, we can identify three major differences between the conferences. The most important one was the difference in the use of computer technology. In the Urban case, Web-HIPRE was the only software used, whereas in the Milk case the interval value tree model with WINPRE was also used. Thus, much time was spent in explaining the method and the software which obviously caused an excessive load on the participants.

The second difference was the framing of the alternatives. In the Milk case the countermeasures concerned the production of a single farm product, whereas the Urban case took a broader view on protection of the whole inhabited environment. Consequently, in the Milk case, the decision conferencing approach was considered more suitable in the exploration of the strategy alternatives than in providing a comprehensive view of the situation, whereas in the Urban case the order was vice versa. The third major difference between the cases was that, in the Urban case, many participants were local inhabitants of Loviisa. This probably increased the motivation and personal interest of the participants in the analysis and the process.

We asked the participants to evaluate the suitability of the approach for both exercises and a possible real situation. The approach was seen more suitable for the planning in advance and exercises than for real crisis situations (Table 3), which was an expected result. However, the majority of the participants found the approach suitable also for a real emergency situation. We find this as a strong indication of confidence and trust, and it is a most encouraging result.

There were two intractable issues characteristic to the problems. The first one was whether to include the alternative ‘do nothing’ into the set of alternatives or not. For this option, the attribute ratings were very different from those obtained for the other alternatives. There were some concerns that this could cause weighting problems, as the scales become very wide and the differences between the other alternatives may become overlooked. On the other hand, including this alternative gives a reference level of the severity of the accident, and in both conferences, the ‘do nothing’ option was included. The other issue was the difference between the attributes reassurance and anxiety. Some of the participants wanted to use only either of them as they could not see the difference and considered these as the two end points of the same scale. Another view was that besides reassuring people, extensive countermeasure actions might also cause anxiety. That is, people can feel that the countermeasure actions correlate positively with the severity of the accident, which causes anxiety. Eventually, both attributes were included in both cases.

Table 3  
Results of the surveys carried out after conferences

<table><tr><td rowspan="2"></td><td colspan="5">Milk case</td><td colspan="5">Urban case</td></tr><tr><td>--</td><td>-</td><td>?</td><td>+</td><td>++</td><td>--</td><td>-</td><td>?</td><td>+</td><td>++</td></tr><tr><td>The decision conferencing approach is suitable for providing a comprehensive view of the situation in training and exercises.</td><td>1</td><td>1</td><td>1</td><td>10</td><td>-</td><td>-</td><td>-</td><td>1</td><td>4</td><td>8</td></tr><tr><td>The decision conferencing approach is suitable for providing a comprehensive view in the case of a real emergency.</td><td>2</td><td>3</td><td>1</td><td>7</td><td>-</td><td>-</td><td>-</td><td>1</td><td>7</td><td>5</td></tr><tr><td>The decision conferencing approach is suitable for finding a strategy in training and exercises.</td><td>-</td><td>2</td><td>-</td><td>8</td><td>3</td><td>-</td><td>-</td><td>-</td><td>4</td><td>9</td></tr><tr><td>The decision conferencing approach is suitable for finding a strategy in the case of a real emergency.</td><td>-</td><td>4</td><td>1</td><td>7</td><td>1</td><td>-</td><td>-</td><td>4</td><td>5</td><td>4</td></tr><tr><td>The ranking achieved with Web-HIPRE corresponds to my intuitive expectations.</td><td>-</td><td>-</td><td>1</td><td>12</td><td>-</td><td>-</td><td>1</td><td>1</td><td>8</td><td>3</td></tr><tr><td>It was easy to grasp and follow the method used in Web-HIPRE to elicit the trade-offs between attributes.</td><td>-</td><td>1</td><td>1</td><td>10</td><td>1</td><td>-</td><td>2</td><td>-</td><td>7</td><td>4</td></tr><tr><td>It was easy to grasp and follow the method used in WINPRE to elicit the trade-offs between attributes.</td><td>1</td><td>2</td><td>-</td><td>9</td><td>1</td><td colspan="5">WINPRE not used</td></tr><tr><td>The decision conference exercise was useful in general.</td><td>-</td><td>-</td><td>-</td><td>12</td><td>1</td><td>-</td><td>-</td><td>-</td><td>1</td><td>12</td></tr></table>

‘−−’ = strongly disagree, ‘−’ = disagree, ‘?’ = no opinion, ‘+’ = agree, ‘++’ = strongly agree.

## 5.1. Use of the MAVT methods and software

It proved to be an applicable way to elicit the participants' preferences by allowing them to independently weight the preference model. It also made it possible to analyze the stakeholders' preferences separately in each group. This was highly useful, as besides clarifying the stakeholders' own preferences, it helped to understand the other stakeholders' views, too. In general, the participants were able to carry out the required tasks by themselves with Web-HIPRE and the majority of the participants found the methods easy to use and follow (Table 3). Some technical help concerning the software was asked during the process, but two technical assistants and the decision analyst were sufficient to provide this help.

The preference modeling was carried out by using relatively small value trees, but the participants were still able to get a comprehensive view of the problem (Table 3). This suggests that instead of trying to increase the details of the model, it can often be more advantageous to focus on the problem structuring phase and on the discussion on the meaning of the attributes, and in this way increase the participants' shared understanding of the problem.

The participants ran the software following the instructions given by the facilitator. However, there were also participants who used various features of the software individually, for example, by studying the results on their own. In this respect, the general-purpose software provided a convenient way to allow different working modes, as it allowed the DMs with more technical competence to use various features.

In general, most participants felt that they understood the decision analysis methodology (Table 3). However, in the Milk case, the use of the tested interval SMART/ SWING method with the WINPRE software was ambivalent in case of certain participants. The use of the two different elicitation procedures in one session is not likely a good idea. In our case, the new interval method was tested because of its potential in accommodating judgmental uncertainties, and we wanted to get some initial feedback from real DMs. However, this was unrealistic within such a tight time frame.

One should also note that even if the DMs themselves feel that they have understood the methods, there is still a risk of behavioral biases (see e.g. Refs. [37,49]). Often the identification of these is very difficult and emphasizes the facilitator's role of describing understandably the use of the methods to the participants. One natural way to test whether the modeling has been carried out properly is to ask the participants whether the results achieved with the model correspond to their intuitive holistic expectations. If this is not the case, there may be some errors or biases in the elicitation. On the other hand, it may also imply that the modeling process has been able to provide a more structured view of the problem and consequently change the DM's overall preferences over the alternatives. Nevertheless, a positive reply suggests that the results obtained with the model are likely to reflect the true preferences of the DM. In our conferences, only one participant reported that the ranking obtained with Web-HIPRE did not correspond with her intuitive expectations (Table 3).

## 5.2. The use of web features

In exercises, such as in our cases, decision conferencing can be considered as a part of a learning process to increase the participants' preparedness to meet the real situation. Thus, we consider it important that the participants can replicate the modeling process afterwards if they so want. In this respect, the Internet provided a convenient way to support the learning, as we could easily distribute the results of the conference and all the background material via the conference web pages. The use of Web-HIPRE made it also possible to make the preference models publicly available on the web.

Technically, the use of web-based software through an intranet appeared to be an applicable way to analyze and compare the models of the various stakeholder groups. These conferences were arranged locally in a decision room, but the use of a web-based GDSS would have allowed arranging the conferences on the web, for example, with the help of some videoconferencing facility. In general, the use of the web as a communications channel has been found an applicable way to support the group processes (see e.g. Refs. [11,41]). However, these studies have mainly focused on process support, and thus the experiences cannot be applied as such in multicriteria decision support, as decision support tasks can often be completed even without fully understanding the methodology. In contrast, in the process support the participants' difficulties can usually be detected as an inability to complete the required task. Thus, the use of MCDA methods may not be possible with a standard videoconferencing environment, as hands-on support is often needed.

To support the independent learning and use of the methods, we have developed web-based material on the value tree analysis. Our eLearning site provides, for example, illustrative demonstrations, video clips and online quizzes about the use of the MCDA methods and the software [18]. It will be interesting to see if such support turns out to be needed and useful. As another way to improve the understanding of MCDA methods, Papamichail and French [34] have developed a DSS module to provide the analysis of the results in natural language. For a report of using this natural language explanation module in a similar setting as the one described in this paper, see Ref. [16].

## 6. Conclusions

The experiences obtained from our case studies strongly support the applicability of interactive MAVT software in decision conferences, assuming that these are carefully planned in advance. The participants were satisfied with the approach, and the conferences showed that the prioritizing process can be carried out independently by the participants. However, we believe that the availability of easy-to-use methods and simple models was an essential requirement for this. It was also possible to carry out the conferences during one day, which further emphasized the need for simple models.

The feedback from the participants supports the applicability of the approach in nuclear emergency management, even though it is typically a very sensitive and difficult area to deal with and new approaches are not easily accepted without reservations. The participants considered decision conferencing especially suitable for increasing the preparedness planning in advance and exercises, but the decision process could include elements of this approach also in a real emergency situation. Nevertheless, continuous and repeated exercises are needed to maintain the preparedness level to use this method. In addition, it is necessary to inform the public about this novel approach to guarantee its acceptance in a crisis situation. There should also be trained facilitators available for such a process, and a formal plan on how to engage the relevant stakeholders.

The web has become a part of our everyday life, and it is natural to expect that there will be growing interest to use its opportunities to support group decisions. There is, for example, a growing need for environmental decision support and global participation that is impossible to satisfy without the use of web-based systems. These challenges can be met by starting off with experimental case studies like the one described here. Such efforts will familiarize the field with decision analytical tools and web-based participation support.

## Acknowledgements

The authors would like to thank all the participants of the decision conferences. This research has been partly carried out in the RODOS and EVATECH projects, but the views expressed in the paper are those of the authors and do not necessarily represent those of the project consortiums. Jyri Mustajoki acknowledges the financial support of the Academy of Finland (project 32641), the Finnish Cultural Foundation and the Jenny and Antti Wihuri Foundation.

## References

[1] L. Adelman, Real-time computer support for decision analysis in a group setting: another class of decision support systems, Interfaces 14 (2) (1984) 75–83.

[2] M. Ammann, Finnish workshop on the restoration of contaminated residential areas after a nuclear accident: strategy generation and impact assessment, Journal of Environmental Radioactivity 85 (2006) 299–313.

[3] M. Ammann, K. Sinkko, E. Kostiainen, A. Salo, K. Liskola, R.P. Hämäläinen, J. Mustajoki, Evaluating measures to protect the milk pathway in accidental radioactive releases, Radiation and Nuclear Safety Authority of Finland, STUK Report, vol. A186, 2001, Downloadable at www.stuk.fi/julkaisut/stuk-a/stuk-a186.pdf.

[4] K. Andersson, Evaluation of early phase nuclear accident cleanup procedures for Nordic residential areas, NKS Report NKS/ EKO-5, vol. 18 (96), 1996.

[5] H.K. Bhargava, D.J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems (2005) (to appear).

[6] U. Bose, A.M. Davey, D.L. Olson, Multi-attribute utility methods in group decision making: past applications and potential for inclusion in GDSS, Omega 25 (6) (1997) 691–706.

[7] T.X. Bui, S.R. Sankaran, Design considerations for a virtual information center for humanitarian assistance/disaster relief using workflow modeling, Decision Support Systems 31 (2001) 165–179.

[8] A. Davey, D. Olson, Multiple criteria decision making models in group decision support, Group Decision and Negotiation 7 (1998).55-75

[9] G. DeSanctis, R.B. Gallupe, A foundation for the study of group decision support systems, Management Science 33 (5) (1987) 589–609.

[10] J. Ehrhardt, A. Weis (Eds.), RODOS: decision support system for off-site nuclear emergency management in Europe, European Commission, EUR 19144 EN, 2000, www.rodos.fzk.de.

[11] J. Fjermestad, An analysis of communication mode in group support systems research, Decision Support Systems 37 (2) (2004) 239–263.

[12] J. Fjermestad, S.R. Hiltz, An assessment of group support systems experimental research: methodology and results, Journal of Management Information Systems 15 (3) (1999) 7–149.

[13] J. Fjermestad, S.R. Hiltz, Group support systems: a descriptive evaluation of case and field studies, Journal of Management Information Systems 17 (3) (2001) 115–159.

[14] S. French, Multi-attribute decision support in the event of a nuclear accident, Journal of Multi-Criteria Decision Analysis 5 (1996) 39–57.

[15] S. French, G. Barker, C. Bayley, E. Carter, A. Hart, J. Maule, C. Mohr, R. Stepherd, N. Zhang, Participation and e-Participation: Involving Stakeholders in the Management of Food Chain Risks in the Rural Economy, 2005, Manuscript, Downloadable at www. relu-risk.org.uk/publications/e-participation.pdf.

[16] J. Geldermann, V. Bertsch, M. Treitz, S. French, K.N. Papamichail, R.P. Hämäläinen, Multi-criteria decision support and evaluation of strategies for nuclear remediation management, Omega (2006) (to appear).

[17] R.P. Hämäläinen, Decisionarium – Global Space for Decision Support, Systems Analysis Laboratory, Helsinki University of Technology, 2000 www.decisionarium.hut.fi.

[18] R.P. Hämäläinen, SAL MCDA Learning Resources, Systems Analysis Laboratory, Helsinki University of Technology, 2002 www.mcda.hut.fi.

[19] R.P. Hämäläinen, Decisionarium — aiding decisions, negotiating and collecting opinions on the web, Journal of Multi-Criteria Decision Analysis 12 (2003) 101–110.

[20] R.P. Hämäläinen, J. Helenius, WINPRE — Workbench for Interactive Preference Programming, Computer Software, Systems Analysis Laboratory, Helsinki University of Technology, 1997 Downloadable at www.sal.hut.fi/Downloadables/winpre.html.

[21] R.P. Hämäläinen, J. Mustajoki, Web-HIPRE — Global Decision Support, Computer Software, Systems Analysis Laboratory, Helsinki University of Technology, 1998 www.hipre.hut.fi.

[22] R.P. Hämäläinen, R. Kalenius, Opinions-Online — Platform for Global Participation, Voting Surveys and Group Decisions, Computer Software, Systems Analysis Laboratory, Helsink University of Technology, 1999 www.opinions.hut.fi.

[23] R.P. Hämäläinen, M. Lindstedt, K. Sinkko, Multiattribute risk analysis in nuclear emergency management, Risk Analysis 20 (4) (2000) 455–467.

[24] INFORMS, OR/MS Resource Collection: Computer Programs, Institute for Operations Research and the Management Sciences, 2000 www.informs.org/Resources/Computer\_Programs/.

[25] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, John Wiley & Sons, Inc., 1976.

[26] R.L. Keeney, D. von Winterfeldt, Managing nuclear waste from power plants, Risk Analysis 14 (1) (1994) 107–130.

[27] M. Marttunen, R.P. Hämäläinen, Decision analysis interviews in environmental impact assessment, European Journal of Operational Research 87 (3) (1995) 551–563.

[28] D.T. Maxwell, Decision analysis: aiding insight VII, OR/MS Today 31 (6) (2004) 44–55.

[29] A.T. McCartt, J. Rohrbaugh, Managerial openness to change and the introduction of GDSS: explaining initial success and failure on decision conferencing, Organizational Science 6 (5) (1995) 569–584.

[30] J. Mustajoki, R.P. Hämäläinen, Web-HIPRE: global decision support by value tree and AHP analysis, Infor 38 (3) (2000) 208–220.

[31] J. Mustajoki, R.P. Hämäläinen, A. Salo, Decision support by interval SMART/SWING — incorporating imprecision in the SMART and SWING methods, Decision Sciences 36 (2) (2005) 317–339.

[32] J. Mustajoki, R.P. Hämäläinen, M.R.K. Lindstedt, Using intervals for global sensitivity and worst case analyses in multiattribute value trees, European Journal of Operational Research 174 (1) (2006) 278–292.

[33] J.F. Nunamaker, Future research in group support systems: needs, some questions and possible directions, International Journal of Human-Computer Studies 47 (1997) 357–385.

[34] K.N. Papamichail, S. French, Design and evaluation of an intelligent decision support system for nuclear emergencies, Decision Support Systems 41 (2005) 84–111.

[35] L.D. Phillips, A theory of requisite decision models, Acta Psychologica 56 (1984) 29–48.

[36] L.D. Phillips, M.C. Phillips, Facilitated work groups: theory and practice, Journal of Operational Research Society 44 (6) (1993) 533–549.

[37] M. Pöyhönen, H.C.J. Vrolijk, R.P. Hämäläinen, Behavioral and procedural consequences of structural variation in value trees, European Journal of Operational Research 134 (1) (2001) 218–227.

[38] M.A. Quaddus, D.J. Atkinson, M. Levy, An application of decision conferencing to strategic planning for a voluntary organization, Interfaces 22 (6) (1992) 61–71.

[39] R. Ramanathan, L.S. Ganesh, Group preference aggregation methods employed in AHP: an evaluation and intrinsic process for deriving members' weightages, European Journal of Operational Research 79 (1994) 249–265.

[40] P. Reagan-Cirincione, Improving the accuracy of group judg ment: a process intervention combining group facilitation, social judgment analysis, and information technology, Organizational Behavior and Human Decision Processes 58 (2) (1994) 246–270.

[41] N.C. Romano, R.O. Briggs, J.F. Nunamaker, D.D. Mittleman, Distributed GSS Facilitation and Participation: Field Action Research, Proc. of the 32nd Hawaii International Conference on Systems Sciences (HICSS-32), Maui, Hawaii, January 5–8, 1999.

[42] A. Salo, Interactive decision aiding for group decision support, European Journal of Operational Research 84 (1) (1995) 134–149.

[43] A. Salo, R.P. Hämäläinen, Preference assessment by imprecise ratio statements, Operations Research 40 (6) (1992) 1053–1061.

[44] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[45] K. Sinkko, R.P. Hämäläinen, R. Hänninen, Experiences in methods to involve key players in planning protective actions in the case of a nuclear accident, Radiation Protection Dosimetry 109 (1–2) (2004) 127–132.

[46] K. Sinkko, M. Ammann, R.P. Hämäläinen, J. Mustajoki, Facilitated Workshop on Clean-up Actions in Inhabited Areas in Finland after an Accidental Release of Radionuclides, Radiation and Nuclea Safety Authority of Finland, STUK Report, vol. A214, 2005, Downloadable at www.stuk.fi/julkaisut/stuk-a/stuk-a214.pdf.

[47] T.J. Stewart, A critical survey on the status of multiple criteria decision making theory and practice, Omega 20 (5/6) (1992) 569–586.

[48] E. Turban, J.E. Aronson, T.-P. Liang, Decision Support Systems and Intelligent Systems, 7th EditionPrentice Hall Inc., New Jersey, 2004.

[49] M. Weber, K. Borcherding, Behavioral influences on weight judgments in multiattribute decision making, European Journal of Operational Research 67 (1993) 1–12.

[50] D. von Winterfeldt, W. Edwards, Decision Analysis and Behavioral Research, Cambridge University Press, Cambridge, UK, 1986.

![](/api/attachments/WK63VNBE/fulltext/images/cfbed1e912a347c6ddd4d42af3300df1f10056f3d0f3135d28539f8a1584bbe6.jpg)

Jyri Mustajoki received the M.Sc. degree in systems and operations research from the Helsinki University of Technology (HUT), Helsinki, Finland, in 1999. Currently, he is a Ph.D. student in the Systems Analysis Laboratory, HUT. His research interests include interval methods in multiattribute decision analysis, decision support systems, and applications in environmental decision making and nuclear emergency management. He has taken part in developing many decision support

software including Web-HIPRE and Smart-Swaps available at www. decisionarium.hut.fi. His work has been published in journals such as Decision Analysis, Decision Sciences, European Journal of Operational Research and Environmental Modeling and Software.

![](/api/attachments/WK63VNBE/fulltext/images/7bc4b8695e6ba20f22d3ef269b6b8ce189a187321b019e3df684ef82d2293fa2.jpg)

Raimo P. Hämäläinen is Professor of Applied Mathematics and Operations Research and the Director of the Systems Analysis Laboratory at Helsinki University of Technology. His research interests include decision, risk and game theory and dynamic optimization with aerospace applications. He is widely known for his work in environmental decision making and energy policy. He has developed and applied interactive participation processes based on decision models in many environ-

mental policy contexts. He is a pioneer in the design of decision analysis software including the first web based value tree software, Web-HIPRE, and Smart-Swaps as well as the Joint-Gains negotiation support system. These are all available in his public Decisionarium site www.decisionarium.hut.fi. He has also recently introduced the new concept of Systems Intelligence, which opens a new perspective to organizational learning and personal growth. Dr. Hämäläinen was presented the Edgeworth-Pareto Award of the International Society for Multiple Criteria Decision Making in 2004.

![](/api/attachments/WK63VNBE/fulltext/images/0bdbdf2953670d9f07b8a964edc6185c4f953c75e174592795e6bf09f8f6b8d6.jpg)

Kari Sinkko, Ph.D., is the project manager in STUK, Radiation and Nuclear Safety Authority, Research and Environmental Surveillance. His research interests include the radiological consequences caused by nuclear test explosions and accidental releases of radionuclides from nuclear installations. He has developed and extensively tested participatory decision analytical ap proaches to plan protective actions for nuclear emergency management. He has also developed

the computer based gamma-spectrometric analysis and environmental sample analysis. He has been the co-ordinator of the Commission of the European Communities (CEC) projects ‘Completion and Customisation of the modelling in RODOS’ (FI4P-CT96-0053) and ‘RODOS Users Group (FI4P-CT98-0075).
