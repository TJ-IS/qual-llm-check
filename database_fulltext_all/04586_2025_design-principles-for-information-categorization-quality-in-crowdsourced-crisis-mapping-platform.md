---
otero_id: 4586
otero_key: "VKV8C66S"
title: "Design Principles for Information Categorization Quality in Crowdsourced Crisis Mapping Platforms"
authors: "Rohit Valecha; Onook Oh; H. Raghav Rao"
year: "2025"
journal: "MIS Quarterly"
doi: "10.25300/misq/2024/16610"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DESIGN PRINCIPLES FOR INFORMATION CATEGORIZATION QUALITY IN CROWDSOURCED CRISIS MAPPING PLATFORMS<sup>1</sup>

Rohit Valecha Information Systems and Cyber Security, Alvarez College of Business, University of Texas at San Antonio, San Antonio, TX, U.S.A. {rohit.valecha@utsa.edu}

Onook Oh Information Systems, Business School, University of Colorado Denver, Denver, CO, U.S.A. {onook.oh@ucdenver.edu}

H. Raghav Rao Information Systems and Cyber Security, Alvarez College of Business, University of Texas at San Antonio, San Antonio, TX, U.S.A. {hr.rao@utsa.edu}

Crisis mapping platforms have transformed disaster management and digital humanitarian efforts by allowing victims to quickly submit “Requests for Help” (RFH) messages directly from disaster locations via mobile devices. On these platforms, online volunteers are often engaged in processing and categorizing messy and incomplete RFH messages into structured and useful crisis reports that can aid first responders in their recovery efforts. This research note examines the case of the Ushahidi platform deployed during the 2010 Haiti Earthquake to propose design principles for a crisis mapping platform that facilitates the conversion and categorization of victim-submitted RFH messages into actionable crisis reports for on-site first responders. To validate the proposed design principles, we instantiated them with the help of a template, and conducted a series of experiments to confirm the effectiveness of the template in improving the categorization quality of crisis reports. We expect that the design principles will be particularly useful for developing digital platforms aimed at humanitarian crisis response that requires a large-scale participation of online crowd volunteers.

Keywords: Crisis mapping, digital humanitarianism, crowdsourcing, requests for help, information categorization, Ushahidi, Haiti earthquake

## Introduction

Crisis mapping platforms refer to sociotechnical systems that support the real-time process of gathering, analyzing, categorizing, and visualizing information related to populations affected by a crisis (Hunt & Specht, 2019). With the wide use of mobile technology, crisis mapping platforms have established a new norm in crisis management and digital humanitarian projects by enabling on-site victims to submit “requests for help” (RFH) messages directly from their disaster <sup>2</sup> sites using the short text messaging features of mobile phones (McClure, 2014; Meier, 2015). However, an ongoing challenge on these platforms is that RFH messages, often submitted by victims under high anxiety and time pressure in dangerous situations, tend to be terse, incomplete, and ambiguous. This poses difficulty for first responders in accurately assessing crisis situations (Jenvald et al., 2001) and making informed decisions for disaster management.

To address this challenge, engaging crowd volunteers through crisis mapping platforms has shown substantial potential to collectively validate and disambiguate victimsubmitted RFH messages (Castillo, 2016; Meier, 2015; Morrow et al., 2011; Oh et al., 2013; Okolloh, 2009; Starbird & Palen, 2011). To make information in messy and incomplete RFH messages usable for first responders on-site, crowd volunteers engage in the process of information categorization, a process wherein RFH messages are categorized by crowd volunteers to provide rapid situational awareness for first responders on-site. Recognizing its importance, the U.S. military has emphasized the need to understand the conditions under which crowd volunteers can produce high-quality categorization for submitted RFH messages (Munro, 2011). However, evaluating the quality of crisis categorization is difficult, because the ground truth information, as intended by the victims submitting RFH, is likely to be unknown to crowd volunteers. With the crisis context in mind, we submit the following research question: How should participatory crisis mapping platforms be designed to support online crowd volunteers in improving the quality of categorization of RFH in the absence of ground truth?

While the quality of categorization is typically characterized by its accuracy, in such crisis situations where ground truth is not readily available, it is only possible to focus on plausibly accurate categorization (Weick, 1995). We therefore define the quality of information categorization in terms of a proxy that results in plausible accuracy, that is, the degree of agreement on information categories that multiple volunteers assign to RFH messages (Heinzelman & Meier, 2012; Silverman, 2014). For this research note, as primary data, we used the RFH messages collected from Ushahidi, <sup>3</sup> the participatory crisis mapping platform deployed in the aftermath of the 2010 Haiti earthquake. We examined actual RFH messages processed by crowd volunteers, who collectively worked on the RFH messages through a mechanism known as posting, which involves annotations to clarify the meaning of short, incomplete, or ambiguous RFH messages and to classify them into plausible categories.

To answer the research question, we used sensemaking theory (Weick, 1995; Maitlis & Christianson, 2014) as a kernel theory to analyze the conditions under which crowd volunteers can better categorize RFH messages on a crisis mapping platform. We then proceeded to (1) formulate design principles for improving categorization quality in the absence of ground truth, (2) instantiate a template based on these design principles to help crowd volunteers better categorize victims’ RFH messages, and (3) conduct a series of experiments to validate the design principles by assessing the effectiveness of the template in improving categorization quality.

The following section reviews prior research on the quality of information categorization and highlights the need for sensemaking in processing victim-submitted RFH messages. Next, drawing upon the insights of sensemaking theory, we propose design principles for sensemaking in crisis mapping platforms. We then validate their effectiveness through a series of experiments. This research note concludes with a discussion of the limitations of our research and directions for future research. Using the real use-case of RFH messages collected during the 2010 Haiti earthquake, this research note adds practical contributions to the field of digital humanitarianism at the intersection of humanitarian response and digital crisis informatics (Meier, 2015; Palen & Anderson, 2016).

## Background

This section reviews the information categorization literature and clarifies the concept of categorization quality. It then explains the importance of sensemaking in processing crisis messages.

## Information Categorization in the Disaster Context

Crisis mapping platforms have gained popularity in harnessing “smart crowds” for categorizing RFH messages for the relief and recovery activities of first responders<sup>4</sup> (Bock & Lederach, 2012). Crowd volunteers not only monitor RFH messages to identify victims’ urgent needs, but they also deeply engage in tagging, disambiguating, and organizing them into actionable categories (Okolloh, 2009). This improved information is then compiled into categories on a crisis mapping platform to help first responders understand unfolding crisis situations and make informed decisions for search and rescue operations. Appendix A presents sample information categories assigned to RFH messages by online volunteers in the wake of various international crises.

## Issues with Crisis Information Categorization

Prior research has questioned the quality of information categorization performed by crowd volunteers (Morrow et al., 2011; Fonte et al., 2015). Camponovo and Freundschuh (2014) found a 50% discrepancy rate in the categorization of crisis messages when comparing the work of independent reviewers to that of online volunteers. Also, Caragea et al. (2011) reported that machine learning algorithms provided a less than 50% accurate categorization rate for overall categories and less than 70% for most of the subcategories.

Prior literature has exposed two issues that warrant further examination. First, Liu (2014, p. 408) noted that “the quality [of crisis categorization] may largely depend on the crowd’s familiarity with the type of data.” This suggests that task characteristics and data type could affect the categorization quality of crisis messages, highlighting the need for improvement in platform design to help crowd volunteers better categorize RFH messages. Second, Hosseini et al. (2012) pointed out that assessing categorization quality by comparing crowd-annotated information with predefined information labels can be misleading because the ground truth information, as intended by the victims submitting RFH messages, is often unknown to crowd volunteers. Therefore, the design of crowdsourced crisis mapping platforms needs to consider these two less-understood contexts of crisis situations.

## Sensemaking in Crisis Situations

When ground truth is not available, crowd volunteers assess the plausibility of victims’ needs expressed in crisis messages as a proxy for ground truth (Scholer et al., 2011; Vuurens & De Vries, 2012). In this context, Lombardi et al. (2016, p. 35) defined plausibility as “what is perceived to be potentially truthful when evaluating explanations.” Similarly, Klein et al. (2021, p. 1) argued that “when people make plausibility judgments about an assertion, an event, or a piece of evidence, they are gauging whether it makes sense. Therefore, we can treat plausibility judgments as sensemaking activities.” It comes as no surprise that uncertain, urgent, and time-pressing crisis situations require sensemaking activities by crowd volunteers and first responders alike (Vendreø, 2015). Thus, efforts to make sense of crisis situations are essentially a social construction process in which crowd volunteers build plausible meanings from cues extracted from their surroundings and in interaction with other volunteers (Weick, 1995). Table 1 illustrates how sensemaking activities relate to the online crowd’s task of processing and categorizing RFH messages under crisis.

## Design Principles

Sensemaking in crisis mapping platforms arises from cues expressed in victims’ RFH messages, as well as from clarifying information contributed by crowd volunteers in follow-up postings. Thus, we maintain that information categorization in crisis mapping platforms entails two sensemaking processes: (1) understanding crisis situations through contextual cues implicitly or explicitly expressed in RFH messages and (2) constructing shared meanings of RFH messages through communicative interactions, such as posting annotations by online crowds, to clarify their ambiguous meanings. This section draws on these two key properties of sensemaking—extracting contextual cues and enabling communicative interactions—to formulate design principles for improving categorization quality in crisis mapping platforms. We note that while contextual cues alone may not guarantee that the victim-reported information is complete, communicative interactions allow crowd volunteers to cross-reference the information and fill any gaps.

The following subsections apply the five-step guidelines of Gregor et al. (2020) to formalize the design principles from the two key properties of sensemaking in crisis mapping platforms. Their five-step guideline includes: (1) identifying the aim by clarifying what is to be achieved; (2) clarifying the role of the users by identifying the actors for whom the aim is to be achieved; (3) defining the context, such as boundary conditions and implementation settings (Nabavian & Parsons, 2024); (4) explaining the mechanisms, such as actions or processes that allow the users to achieve the aim (Bomström et al., 2022); and (5) justifying the rationale for believing that the mechanisms will lead to achieving the aim (Gebka et al., 2021).

To clarify our discussion, we introduce the term crisis report to differentiate between the original victim-submitted RFH messages and their processed and transformed versions that are used by first responders. We define a crisis report as an enhanced version of a RFH message, enriched with additional annotations contributed by crowd volunteers. The processing and transformation are crucial, as they convert short and unclear RFH messages into more comprehensible crisis reports, ultimately providing first responders with actionable information. The following section will further delineate and operationalize the contextual cues, which consist of two dimensions of social cues and situational cues.

<table><tr><td colspan="3">Table 1. Sensemaking for Crisis Categorization in Crisis Platforms</td></tr><tr><td>Sensemaking properties</td><td>Implications</td><td>Categorization as a process of sensemaking by crowd volunteers</td></tr><tr><td>Plausibility</td><td>Sense is driven by plausibility</td><td>Categorization happens in the absence of ground truth. Crowd volunteers assign plausible categories based on their sense of the situation.</td></tr><tr><td>Context</td><td>People develop sense of what may be occurring by extracting contextual cues</td><td>Crowd volunteers extract cues from RFH messages to understand the victim&#x27;s environment and categorize them into crisis report categories.</td></tr><tr><td>Sociotechnical construction</td><td>Sense is created through communicative interactions with others</td><td>Categorization involves a sociotechnical process that enables and constrains crowd volunteers to exchange, interpret, and share RFH messages on crisis mapping platforms</td></tr></table>

<table><tr><td colspan="2">Table 2. Extraction of Contextual Cues</td></tr><tr><td>Design principle</td><td>Extraction of contextual cues from RFH</td></tr><tr><td>Aim and user</td><td>Crowd volunteers create an understanding of victims&#x27; needs and crisis situation</td></tr><tr><td>Context</td><td>Crisis messages that lack clear information diminish crowd volunteers&#x27; ability to make sense of the situation</td></tr><tr><td>Mechanism</td><td>To identify critical situational and victim-related social information</td></tr><tr><td>Rationale</td><td>Cues enable crowd volunteers to form impressions of victims and their surroundings, which enables them to make better judgments</td></tr></table>

## Design Principle 1: Extracting Contextual Cues

A crucial task of online volunteers is transforming RFH messages into crisis reports that are easier to categorize and more valuable for first responders’ rescue operations. Reading through short and incomplete RFH messages, crowd volunteers (users) fill information gaps regarding victims’ conditions and needs (aim). This process involves identifying and extracting contextual cues related to victims in disasteraffected areas (mechanism) (Weick, 1995).

When crowd volunteers successfully extract contextual cues from RFH messages, they become better equipped to not only make sense of victims’ needs and situations (Maitlis & Sonenshein, 2010) (rationale) but also to develop structured crisis reports that on-site first responders can use for their relief activities. These extracted cues eventually enrich the information context for crowd volunteers and allow them to collectively classify RFH messages into useful crisis reports with relevant categories. Table 2 summarizes the five-step guideline proposed by Gregor et al. (2020) for formalizing design principles, which we applied to the context of extracting contextual cues from RFH messages.

It is well known that the onset of a disaster incurs a sudden and large influx of RFH messages from on-site victims, many of which are not immediately relevant or useful for first responders’ response activities. Consequently, first responders face challenges in parsing RFH in a timely manner. To address this challenge, a crisis mapping platform should be designed to facilitate crowd volunteers to easily identify contextual cues that indicate the victims’ situations and/or needs (Maitlis & Sonenshein, 2010; Tierney et al., 2006). Ideally, these cues should encompass contextual information types i.e., who, what, when, and where (in line with Venkatesan et al., 2021).<sup>5</sup>

Victim information, such as “women” and “children”; quantifiers such as “few,” “many,” and “much”; or numbers such as “tens” and “hundreds” serve as valuable social cues to crowd volunteers and responders. For example, in the following crisis report (ID #1934), the specification of number of victims as a social cue (e.g. “there are 500 victims”) leads crowd volunteers to determine that many victims require setting up a distribution point, thereby categorizing the message as “Non-food aid distribution point.”

ID #3119: “… we need tents at 54 Nelson dead end please help us” Categories: “Shelter needed,” “Services available”

```txt
ID #1934: “Shelters and clothes needed in Baussan street #9 [for] 500 people”
Categories: “Vital lines,” “Non-food aid distribution point”
```

Situational cues indicate implicit or explicit signals that express the environmental conditions of victims, their needs, and their location (Meier, 2015). Situational cues help crowd volunteers to channel their collective efforts to assign relevant categories. For instance, in the crisis report (ID #3119), crowd volunteers identified that the on-site victims were asking for vital lifeline services such as shelter (i.e. tents to sleep in).

Thus, we classified information related to “who” as social cues, and information related to “what,” “when,” and “where” as situational cues. Social cues indicate crowd density, which reflects the local impact of a crisis, while situational cues denote location, needs, and threats posed by the urgency of the crisis situation (Meier, 2015). This aligns with Tierney et al.’s (2006) assertion that sensemaking is facilitated through “situational factors, including the presence of perceptual cues signaling danger and … the social contexts in which decisions are made—for example, neighborhood residents in the setting” (italics added, p. 126). We summarize the above discussion and formalize the contextual cues, i.e., social cues and situational cues (Dootson et al., 2021; Lindell & Perry, 2012) as 2-tuples:

## Social cues:

who: <victim, status>

## Situational cues:

when: <urgency, time>; what: <needs, quantity>; where: <place, direction>

We further articulate the following two design principles.

Design Principle 1a: The crisis mapping platform should afford the capability to extract social cues from RFH messages for crowd volunteers to identify information about the social contexts of the victims affected by the crisis.

Design Principle 1b: The crisis mapping platform should afford the capability to extract situational cues from RFH messages for crowd volunteers to identify information about the victims’ conditions, needs, and situation.

## Design Principle 2: Aggregating Interactive Posts

Interacting remotely around RFH on a crisis mapping platform, crowd volunteers (users) search for missing information, clarify uncertain information, and annotate locations to better understand victims’ situations behind the scenes (Starbird et al., 2012; Starbird & Palen, 2011). This interaction comprises crowd volunteers’ activities of adding and editing posts that contribute to original RFH messages. These activities facilitate crowd interactions to convert ambiguous RFH messages into clear and useful crisis reports for on-site response operations (mechanism) (Meier, 2015). Munro (2013) states that “several conversations show non-Haitian volunteers asking questions about locations, so it is clearly a gain in location accuracy, and about ambiguous water-related terms, so it is also a gain in categorization” (p. 233). Eventually, these crowd interactions surrounding RFH transform the initially ambiguous messages into richer and more structured information that can be better understood and categorized by crowd volunteers (Maitlis & Sonenshein, 2010). These distributed but focused interactions are likely to improve the quality of categorization (rationale). Table 3 summarizes the five-step guidelines suggested by Gregor et al. (2020) for formalizing design principles, which we adapted to the context of crowd interaction that involves adding, editing, and discussing interactive posts.

<table><tr><td colspan="2">Table 3. Aggregation of Interactive Posts</td></tr><tr><td>Design principle</td><td>Aggregation of crowd volunteers&#x27; interactive posts</td></tr><tr><td>Aim and user</td><td>Crowd volunteers create an understanding of victims&#x27; needs and the crisis situation</td></tr><tr><td>Context</td><td>RFH messages lack clear information, which diminishes crowd volunteers&#x27; ability to make sense of the situation</td></tr><tr><td>Mechanism</td><td>To transform RFH into actionable crisis reports for relief and recovery activities on-site</td></tr><tr><td>Rationale</td><td>Interactive posts enable crowd volunteers to process victim-submitted RFH messages into structured crisis reports and expand their shared understanding</td></tr></table>

Compiling various perspectives with different knowledge is a strength of crowd interaction that improves the quality of RFH messages into structured, relevant, and clearer crisis reports (Taylor & Van Every, 2000). To manage crowd interaction, therefore, crisis mapping platforms should support an aggregation of interactive posts for crowd volunteers. <sup>6</sup> These interactive posts aggregate crowd volunteers’ discussion related to victims’ locations, victims’ condition, resources and information. We classify interactive posts into two types: (1) crisis mapping posts that track victims’ locations and (2) information gap-filling posts that provide missing details about victims and their needs. Crisis mapping posts include interactions wherein crowd volunteers manually verify geotags and describe location characteristics implicitly and explicitly mentioned in RFH messages (Tavra et al., 2021). In contrast, information gapfilling posts include interactions wherein crowd volunteers search and post additional information to ensure the intended meaning of RFH clearly stands out (DeYoung et al., 2019).

Information gap-filling posts facilitate cross-cutting discussions among crowd volunteers on focal RFH to enhance information completeness (Alison, 2011). By facilitating crowd discussions, gap-filling posts enable crowd volunteers not only to spot and group scattered information with clarifying annotations but also to address incomplete or inaccurate victim-reported information by cross-referencing multiple sources. Pierce and Fung (2013) demonstrate how crowd workers exercise their ability to reason across gaps in information. The below example shows how crowd volunteers made RFH richer and clearer by adding notes or collectively searching for missing information behind the scenes and then grouping relevant information together.

Victim: “We are in Gonaives. There are dead below and starving because all the students died in the earthquake. We are asking (with/and?) authorities (about?) our \‘lean\’ situation here.”

Additional Notes (by crowd volunteers): “The last part is hard to understand, but it seems to be a request for food aid and assistance with recovery of bodies.”

Crisis mapping posts aim to address the ambiguity of location-related information, which is critical for dispatching first responders with the right technologies and resources. Crowd volunteers’ crisis-mapping activities include identifying and geo-tagging landmark information, nearby streets, traffic conditions, and prompting other volunteers to update and resolve location-related problems (Alam et al., 2015). For instance, in the RFH below (ID #1933), a victim is requesting help for an orphanage located in Delmas 31 but does not specify any particular needs. However, as crowd volunteers geotag this location, they could triangulate other requests from the same location, such as the RFH (ID #3851) that is requesting water and food supplies. Due to the ability to cross-reference for geolocation information, crowd volunteers could agree on the same categories (e.g., water shortage and food shortage) for the former report.

ID #1933: “Help needed for orphanage at Delmas 31”

Categories identified through triangulation with #3851: (“Water shortage,” “Food Shortage”).

Additional Notes (by crowd volunteers): Zone Hatt 5 near Delmas 31 …

ID #3851: “Water and food needed at Delmas 31”

Categories: “Water shortage,” “Food Shortage”

We summarize the above discussion and formalize the two types of interactive posts in crisis mapping platforms (Gibson et al., 2015; Munro, 2013), namely crisis mapping posts and information gap-filling posts, as 2-tuples:

Crisis mapping posts: geo: <location, landmark>

Information gap-filling posts: user: <people, count>; resource: <material, quantity>; information: <update, status>

We further articulate the following two design principles.

Design Principle 2a: The platform should afford the capability to aggregate information gap-filling posts in order to enable crowd volunteers to search for incomplete information and compile relevant information.

Design Principle 2b: The platform should afford the capability to aggregate crisis mapping posts in order to allow crowd volunteers to geomap the physical location and describe it in a crisis report.

![](/api/attachments/VKV8C66S/fulltext/images/cf0ca7fe31aa0abd1dd03ebe434d8426b301e4c4835e0339d4bf3133f3b02c48.jpg)  
Figure 1. Interface Design with Design Principles

## Design Template

Figure 1 illustrates how these design principles can be used to build an interface template that supports crowd volunteers to appropriately categorize RFH messages. As suggested by Imran et al. (2013) and Chowdhury et al. (2013), we recommend adding two technical components to process raw RFH messages: (1) a contextual cue extractor that helps distill social and situational cues from RFH messages (Design Principle 1a, 1b) and (2) an information aggregator that helps cluster information gap-filling posts and crisis mapping posts related to each RFH message (Design Principle 2a, 2b).

To demonstrate how the platform can facilitate sensemaking support, consider a class diagram as shown in Figure 2 (following Bera et al., 2011). The platform should afford an interface that keeps track of all incoming RFH messages and shows the process of transforming raw RFH messages into structured crisis reports. It should help extract social and situational cues from RFH messages and enable crowd volunteers to interactively annotate and fill gaps in information about victims’ situations. Also, it should support crowd volunteers in aggregating such interactive posts into a structured and real-time crisis report that can be used to generate crisis maps for on-site relief activities.

We drew on insights from prior crisis information extraction studies, such as a crisis messaging model that presents structured messages based on message formats (Valecha et al., 2013b) to create a template (as depicted in Figure 3). The template provides a standard layout to represent some details of RFH messages (focusing on contextual cues) in placeholders, with the possibility to add additional details or edit existing details (in the form of interactive posts). When it is applied to the unstructured message, it displays the social and situational cues from the RFH as well as gapfilling posts and mapping posts from the crisis report in placeholders alongside the original crisis report. In this way, the template instantiates the design principles by displaying specific pieces of information from unstructured messages and transforms this unstructured information into a structured crisis report.

In their research on knowledge identification system design, Bera et al. (2011) demonstrated that knowledge workers’ performance improves when they are guided by “visual ontologies” representing their work processes. Drawing on this insight, we assessed whether the performance of crowd volunteers in RFH categorization can be improved when they receive guidance by visualizing information in the template.

![](/api/attachments/VKV8C66S/fulltext/images/0d2c5b42343b9abac1270c42f83dd8c475cb5d1b0436535d0e5f39cb32376cb6.jpg)  
Figure 2. An Excerpt of Crisis Mapping Platform Capabilities

![](/api/attachments/VKV8C66S/fulltext/images/3bb96bd20aec332b222407ad0d464dd06a721159682a8fe9e3d67a1a677e9afc.jpg)  
Figure 3. Design of a Template Displaying Cues and Posts

## Evaluation

This section discusses the data collection method. Next, we define the coding scheme that we used to assess the quality of information categorization. Finally, we detail how we coded social cues and situational cues, and aggregated information gap-filling and crisis mapping posts to validate the design principles.

## Data Collection

Crisis reports were collected from the Ushahidi crisis mapping platform deployed immediately after the 2010 Haiti earthquake. Haiti was struck by a magnitude 7.0 earthquake on January 12, 2010, displacing over 3 million people, killing nearly 300,000, and trapping thousands beneath rubble and collapsed structures. With critical infrastructure destroyed, communicating, sharing, and evaluating disaster situations became challenging (Starbird & Palen, 2011; Valecha et al., 2013a). To address these challenges, cell towers were immediately set up, and the Ushahidi crisis mapping platform was deployed to classify victim-submitted RFH messages with the help of crowd volunteers. The data were collected from January 17 to February 17, 2010, which represents the critical time window of the crisis situation. A sample crisis report data (RFH messages attached with crowd volunteers’ posts), ID #2609, is presented below.

ID #2609: “We are in Gonaives. There are dead below and starving because all the students died in the earthquake. We are asking (with/and?) authorities (about?) our \‘lean\’ situation.”

Additional Notes (by crowd volunteers): “The last part is hard to understand, but it seems to be a request for food aid and assistance with recovery of bodies.”

We used two techniques to measure the plausible accuracy of social and situational cues as well as gap-filling posts and mapping posts: (1) post-event evaluation by a team led by a registered nurse (RN) for the categorization quality variable, and (2) research assistant-based content analysis for coding and validating social and situational cues variables.

## Categorization with RN-Led Team as Baseline

We hired an RN-led team to recategorize those reports originally categorized by Ushahidi crowd volunteers during the Haiti earthquake. The RNs, experienced in disaster response, led two student evaluators<sup>7</sup> to separately categorize the crisis reports. RNs have expertise in emergency management,<sup>8</sup> and “are uniquely qualified to manage emergency situations because they can perform the proper assessments, prioritize injuries, communicate effectively, and collaborate with other providers” (Joshua Barnes, personal communication). We note that the RN-led team (1) was well-versed in the health emergency context through job training and experience, (2) was not burdened by time pressure, and (3) read through the data multiple times before categorizing. The student evaluators matched the characteristics of the crowd volunteers at that time, most of whom were students at Tufts University (Munro, 2010; Meier, 2010).

Pilot coding was performed in two rounds using a random sample of 100 crisis reports for each. These pilot data were excluded from further analysis. The pilot coding was conducted to build and refine the coding book for actual coding. The first and second rounds of pilot coding yielded a kappa value of 0.745 and 0.738 respectively, confirming intercoder reliability scores that were significantly higher than what could be obtained by chance (Krippendorf, 2019; Landis & Koch, 1977). Each evaluator then independently performed content coding following Krippendorf’s (2019) instructions. The evaluators were prohibited from communicating with each other while coding. They were limited to less than an hour of coding per day to minimize coding errors due to fatigue.

## Extraction of Contextual Cues and Aggregation of Interactive Posts

This section describes the procedure used to extract social and situational cues and aggregate gap-filling and mapping posts. Table 4 provides snippets of Ushahidi data showcasing various types of cues and posts.

## Extracting Social Cues

Social cues are pieces of information contained in the victims’ RFH messages that indicate the presence and scale of victims affected by the crisis (See ID#2816 in Table 4). To derive social cues, we employed the “social” feature of the Linguistic Inquiry and Word Count (LIWC) dictionary (Pennebaker et al., 2015). The LIWC dictionary for social cues includes words such as children, adults, persons, people, etc. We extracted these social keywords from the RFH messages and displayed them in the template. LIWC features have been validated in prior literature, demonstrating a moderate correlation between human coding and LIWC coding. For a validation of social cues, please refer to Appendix D.

<table><tr><td colspan="4">Table 4. Snippets of Ushahidi Data</td></tr><tr><td>ID</td><td>Date &amp; Time</td><td>Message</td><td>Measure</td></tr><tr><td>#2816</td><td>1/22/20101:48:00 PM</td><td>We are located at Mont Nabrile third section Valley Jacmel. We have a lot of people coming from outside so we need tents, food, water, medication and doctors.</td><td>Message with social cues.</td></tr><tr><td>#3119</td><td>2/10/20101:10:00 PM</td><td>... we need tents at 54 Nelson dead end help us please</td><td>Message with situational cues (need and location).</td></tr><tr><td>#2609</td><td>1/24/20105:21:00 PM</td><td>We are in Gonaives. There are dead below and starving because all the students died in the earthquake. We are asking authorities about our lean situationAdditional Notes:The last part is hard to understand, but it seems to be a request for food aid and assistance with recovery of bodies.</td><td>Message with information gap-filling post.</td></tr><tr><td>#2623</td><td>1/24/20103:58:00 PM</td><td>I am a victim. I am sleeping in the street. My house is destroyed. I haven&#x27;t found any aid. What can you do for me? I am at the corner of Delma 18 across from the Sama.Additional Notes:I found Delma 17 and delma 19 on the map, but not Delmas 18. I guesstimated this location.</td><td>Message with crisis mapping post.</td></tr></table>

## Extracting Situational Cues

During the Haiti earthquake, victims submitted RFH messages about their needs and locations to Ushahidi. Volunteers populated a real-time map with victims’ location information (South, 2010) for relief workers to locate and aid victims. The importance of geolocation tags was discussed by Patrick Meier, co-founder of the Digital Humanitarian Network, who suggested that victims should be able to include details about their locations and needs in their RFH, as this helps crowd volunteers quickly find and categorize required information (Meier, 2015). Ushahidi considered three types of victimreported information as situational (Meier, 2015): (1) victim condition, (2) needs, and (3) location. Following the guidelines of content coding (Krippendorf, 2019; Landis & Koch, 1977), we hired two research assistants to separately check for situational cues from the RFH messages. For a validation of situational cues, please refer to Appendix E.

## Identifying Interactive Posts (Gap-filling Posts and Mapping Posts)

Information gap-filling posts enable crowd volunteers to structure RFH messages by complementing and refining incomplete information. For example, the RFH (ID #2609 in Table 4) is missing the last part, “We are asking authorities about our lean situation.” So, crowd volunteers added a followup post in the form of “Additional Notes,” suggesting that it may be “a request for food aid and assistance.” The post, identified as associated with spotting and filling gaps in the RFH, was thus coded by the research assistants as an information gap-filling post.

Mapping geolocation to RFH messages was an important task of Ushahidi crowd workers. The crisis mapping involved geolocating RFH messages by complementing incomplete geographical information, such as road conditions or routes to disaster sites. For example, in the RFH ID #2623 (see Table 4), victims reported a location that could not be mapped. So, crowd volunteers identified the location and made a follow-up post in the form of “Additional Notes” to the RFH. Research assistants coded such geolocating posts as crisis mapping posts.

## Validation of Design Principles

We validated the design principles, following van Gassel et al. (2019) in a pragmatic way using a three-step approach: (1) evaluating the outcomes in practice, (2) implementing the set of design principles, and (3) assessing the validity of evaluation results. We instantiated the design principles by creating a template interface as a proof of concept and applying it to RFH messages selected from the Ushahidi platform. The template displayed the contextual cues (i.e., social cues and situational cues) and interactive posts (i.e., gap-filling posts and mapping posts).

We conducted three experiments: (1) Study 1 as a preliminary cross-sectional in-class experiment to validate the effect of the template on categorization accuracy, (2) Study 2 as a temporal in-class experiment to evaluate the effectiveness of the template in improving categorization quality in the crisis context, and (3) Study 3 as a cross-sectional experiment on an alternate crowdsourcing platform, FigureEight,<sup>9</sup> to assess the effectiveness of templated crisis reports displaying contextual cues and interactive posts.

Since most crowd work on the Ushahidi platform during the Haiti earthquake was performed by students at Tufts University (Meier, 2015; Munro, 2013), we recruited students from a large southern U.S. university for Study 1 and 2. For Study 3, to enhance generalizability, we recruited actual crowd workers from the crowdsourcing platform, FigureEight, which had previously been deployed in conjunction with the Ushahidi platform to scale up the crowdsourcing efforts as the response operation unfolded.

## Study 1: Preliminary Study—Validation of the Template

Study 1 (detailed in Appendix F) tested whether categorization quality is significantly improved by the presence of the template compared to its absence. The categorization quality was measured by the degree of agreement between students categorization and the RN-led team’s categorization as a baseline (Heinzelman & Meier, 2012; Silverman, 2014). We collected data from 67 student subjects who categorized four crisis reports displayed with and without the template into eight categories. To compare the classification agreements between the student subjects and the RN-led team on the crisis reports, we conducted a chi-square (χ<sup>2</sup>) test of independence.<sup>10</sup> which is an important statistic for testing differences for count variables (McHugh, 2013). Results show that the template is effective in improving categorization quality.

## Study 2: Effectiveness of the Template in Crisis Context

Owing to the noise, ambiguity, and incompleteness of RFH messages, some crisis reports are difficult to categorize. Lewis et al. (2011) conducted a manual analysis of a random sample of 200 crisis reports and identified that a large number of them were difficult to categorize. Bittner et al. (2013, p. 944) reported that “while Ushahidi no doubt employs innovative technologies to bring data onto a map, it is also limited regarding forms of content which are difficult to categorize and geolocate.” Such “difficult-to-categorize” crisis reports provide boundary conditions and the overall crisis context. We identified such difficult-to-categorize crisis reports based on the agreement of original Ushahidi crowd volunteers (during the Haiti crisis) with the RN-led team. When the agreement was less, we labeled the crisis reports as “difficult-to-categorize,” labeling them as easy-tocategorize otherwise.

Study 2 (detailed in Appendix G) involved randomized experiments to validate the effectiveness of the template in improving the categorization quality of crowd volunteers for difficult-to-categorize (vs. easy-to-categorize) crisis reports over two distinct time periods for eight distinct categories (emergency, vital lines, health, security, infrastructure damage, natural hazard, services, and others). We collected data from 94 study subjects who categorized 10 crisis reports displayed with and without a template into eight categories. The experiment involved a 10 × 2 within-subject design over two time periods. We ran multilevel binary logistic regression for each category using a mixed effect logit that can accommodate a binary outcome variable and used a hierarchical structure wherein the crisis reports were provided to (nested in) study subjects. We estimated the effectiveness of the template for each category as follows:

```txt
Level 1
AgreementCategory
= β₀ + β₁Template
+ β₂Difficult_to_Categorize
+ β₃Template
* Difficult_to_Categorize + e

Level 2
β₀ = γ₀₀ + γ₀₁Gender + γ₀₂Age + γ₀₃Education
+ γ₀₄Crisis Experience + u₀
β₁ = γ₁₀ + γ₁₁Gender + γ₁₂Age + γ₁₃Education
+ γ₁₄Crisis Experience + u₁
β₂ = γ₂₀ + γ₂₁Gender + γ₂₂Age + γ₂₃Education
+ γ₂₄Crisis Experience + u₁
β₃ = γ₃₀ + γ₃₁Gender + γ₃₂Age + γ₃₃Education
+ γ₃₄Crisis Experience + u₁

Combined
AgreementCategory
= γ₀₀ + γ₀₁Gender + γ₀₂Age
+ γ₀₃Education
+ γ₀₄Crisis Experience
+ γ₁₀Template
+ γ₂₀Difficult_to_Categorize
+ γ₃₀Template
* Difficult_to_Categorize + e
```

The results show a significant positive effect of the template on the health and service categories. According to these results, the presence of the template with crisis reports is positively associated with agreements on the health and service categories $( z = 3 . 1 0 ; p < 0 . 0 1$ and $z = 2 . 0 3 ; p < 0 . 0 5 )$ , respectively. Results also show a significant positive interaction effect for the emergency, vitals, and hazard categories. According to this result, the effect of the template for difficult-to-categorize crisis reports in achieving agreement is positive and significant for the emergency, vitals, and hazard categories (z = 2.41; p < 0.05 and z = 3.68; p < 0.001 and z = 1.99; p < 0.05, respectively).

## Study 3: Effectiveness of the Template on an Alternate Crowd Platform

To assess the effectiveness of individual design principles (extracting contextual cues and aggregating interactive posts), we recruited crowd workers from an alternate crowdsourcing platform called FigureEight (FE). Through FE, one can hire crowdworkers for various human intelligence tasks. Previous studies have reported that FE is a reliable data collection source in the area of digital humanitarian projects (Temnikova et al., 2015). We collected data from FE in two subexperiments (Experiment 3a and 3b).

## Experimental Setup

We requested crowd workers from FE with categorization experience. We created multiple groups for the experiments: (1) a treatment group where crowd workers were asked to categorize the templated crisis reports,<sup>11</sup> which included social cues and situational cues (Study 3a), as well as information gapfilling posts and crisis mapping posts (Study 3b), and (2) control groups for both Study 3a and 3b, where crowd workers were asked to categorize non-templated crisis reports that did not include these characteristics.

For Study 3a, we randomly chose five templated crisis reports, where the victims had reported their status as well as information about their location, their condition, and their needs (contextual cues) for the treatment group. We also randomly selected another five as non-templated crisis reports that lacked information about the victim location, condition, and needs (no contextual cues) for the control group. For Study 3b, we randomly chose five crisis reports as templated crisis reports that consisted of volunteer notes (interactive posts) for the treatment group. Subsequently, we deleted the notes from the crisis reports (no interactive posts) to present them to the control group as non-templated crisis reports.

For Studies 3a and 3b, we randomly assigned 100 crowd volunteers to the treatment group and another 100 crowd volunteers to the control group and collected their responses (i.e., 200 crowd volunteers who read five templated and nontemplated crisis reports respectively for selecting eight categories). We asked each crowd worker to select one or more of eight categories per crisis report.

## Measure of Agreement

We estimated the measure of agreement as the Jaccard match between categories of crowd workers on FE and those of RNled team. The Jaccard match is the proportion of categories (i.e., the categories assigned by FE crowd volunteers) that matches the categories assigned by the RN-led team to the union of categories (i.e., the unique categories identified by both groups).

$$
\text { Jaccard   Match } = \frac {(F E \text { Categories } \cap R N \text { Categories })}{(F E \text { Categories } \cup R N \text { Categories })}
$$

As the value approaches 1, the size of the intersection increases, signifying an increase in the agreement of categories assigned by the FE workers and RN-led team. On the other hand, a value approaching 0 shows more diversity among the categories. For Study 3a, we examined the effect of the contextual cues (presence of social and situational cues) on the Jaccard match, and for Study 3b, we investigated the effect of interactive posts (presence of gap-filling and mapping posts) on the Jaccard match. In Studies 3a and 3b, we controlled for the time elapsed, the message length, the reading difficulty, the number of posts, and the number of categories. To estimate the measure of agreement, we ran the fractional regression as follows:

$$
\begin{array}{r l} \ln (J a c c a r d M a t c h) & = \beta_ {0} + \beta_ {1} T i m e E l a p s e d \\ & + \beta_ {2} M e s s a g e L e n g t h \\ & + \beta_ {3} R e a d i n g D i f f i c u l t y \\ & + \beta_ {4} N u m b e r o f C a t e g o r i e s \\ & + \beta_ {5} N u m b e r o f P o s t s + \beta_ {6} C u e s \end{array}
$$

$$
\begin{array}{r l} \ln (J a c c a r d M a t c h) & = \beta_ {0} + \beta_ {1} T i m e E l a p s e d \\ & + \beta_ {2} M e s s a g e L e n g t h \\ & + \beta_ {3} R e a d i n g D i f f i c u l t y \\ & + \beta_ {4} N u m b e r o f C a t e g o r i e s \\ & + \beta_ {5} N u m b e r o f P o s t s \\ & + \beta_ {6} I n t e r a c t i v e P o s t s \end{array}
$$

<table><tr><td colspan="5">Table 5. Estimation Results of Fractional Regression (Study 3a and 3b)</td></tr><tr><td rowspan="2"></td><td colspan="2">Study 3a: Jaccard match (FE vs. RN)</td><td colspan="2">Study 3b: Jaccard match (FE vs. RN)</td></tr><tr><td>Coefficient (std. err.)</td><td>Odds ratio</td><td>Coefficient (std. err.)</td><td>Odds ratio</td></tr><tr><td>Constant</td><td>-0.715***(0.182)</td><td>0.490</td><td>0.230(0.256)</td><td>1.258</td></tr><tr><td>Time elapsed</td><td>0.003(0.004)</td><td>1.003</td><td>-0.217***(0.033)</td><td>0.805</td></tr><tr><td>Message length</td><td>-0.001***(0.0003)</td><td>0.999</td><td>0.007***(0.0008)</td><td>1.007</td></tr><tr><td>Reading difficulty</td><td>0.028***(0.006)</td><td>1.028</td><td>-0.058**(0.019)</td><td>0.944</td></tr><tr><td>Category count</td><td>0.017(0.038)</td><td>1.017</td><td>-0.459***(0.055)</td><td>0.632</td></tr><tr><td>Post Count</td><td>-0.379***(0.078)</td><td>0.685</td><td>0.106(0.118)</td><td>1.112</td></tr><tr><td>Template</td><td>0.824***(0.121)</td><td>2.276</td><td>0.157*(0.061)</td><td>1.170</td></tr></table>

Note: ^ p < 0.10; \* p < 0.05; \*\* p < 0.01; \*\*\* p < 0.001

<table><tr><td colspan="4">Table 6. Experimental Summary</td></tr><tr><td>Criteria</td><td>Study 1</td><td>Study 2</td><td>Study 3a and Study 3b</td></tr><tr><td>Purpose</td><td>To validate the effect of the template on crowd agreements</td><td>To assess effectiveness of the template in crisis context</td><td>To assess the effectiveness of templated reports on an alternate crowd platform</td></tr><tr><td>Crowds</td><td>Student participants</td><td>Student participants</td><td>FigureEight workers</td></tr><tr><td>Ground truth</td><td>RN-led team</td><td>RN-led team</td><td>RN-led team</td></tr><tr><td>Level</td><td>Non-nested</td><td>Nested hierarchical (crisis reports nested in individuals)</td><td>Non-nested</td></tr><tr><td>Temporality</td><td>Cross-sectional</td><td>Temporal</td><td>Cross-sectional</td></tr><tr><td>Test</td><td>Chi-square test of independence ( $\chi^2$ )</td><td>Mixed effects logit</td><td>Fractional regression</td></tr><tr><td>Dependent variable</td><td>Agreements</td><td>Binary match</td><td>Jaccard match</td></tr><tr><td>Sample size</td><td>4+4 crisis reports to 67 respondents</td><td>10+10 crisis reports to 94 respondents</td><td>5 RFH to 200 respondents in experiment 3a and 5 crisis reports to 200 respondents in Study 3b</td></tr><tr><td>Results</td><td>Template displaying cues and interactive posts has a significant effect on overall agreements</td><td>Template improves individual agreements for difficult-to-categorize crisis reports</td><td>Templated crisis reports that include contextual cues and interactive posts have significant effect on overall agreements</td></tr></table>

Table 5 presents the results of fractional regression model estimates. In Study 3a, contextual cues captured the presence of social and situational cues in templated crisis reports. The templated crisis reports with contextual cues are positively related to the Jaccard match at $p < 0 . 0 0 1$ . This implies that the templated crisis reports with social and situational cues are likely to result in more than twice the Jaccard match compared to non-templated reports. In Study 3b, results show a significant positive effect of the templated crisis reports that contained interactive posts on the Jaccard match $( p < 0 . 0 5 )$ This implies that the templated crisis reports that included interactive posts resulted in a 17% higher Jaccard match compared to the non-templated ones.

As a robustness test, we tested the Jaccard match models with a hierarchical structure, where RFH (Study 3a) and crisis reports (Study 3b) were assigned to (nested in) FE crowd workers. The results confirm the significant positive effect of the templated crisis reports that included contextual cues (z = $4 . 6 7 ; p < 0 . 0 0 1 )$ and interactive posts $( z = 1 . 7 9 ; p < 0 . 1 0 )$ Table 6 provides a summary of the experimental design and findings for Studies 1, 2, 3a, and 3b.

## Discussion

The proposed design principles for crisis mapping platforms address a critically important yet understudied area of research: information categorization within crisis mapping platforms through the engagement of crowd volunteers. The process of organizing and structuring the often messy and ambiguous RFH messages submitted by victims into structured and actionable crisis reports is important, as its impact extends across all phases of disaster management—preparation, response, and recovery (Camponovo & Freundschuh, 2014; Morrow et al., 2011). Our claim is that design principles for crisis mapping platforms should enable the transformation of messy and ambiguous RFH messages into structured and categorized crisis reports so that they are immediately actionable for first responders. To achieve this, we emphasize that the platforms should (1) enable the extraction of contextual cues (including both social and situational cues) to make them noticeable, and (2) facilitate the aggregation of interactive posts (including both gap-filling and mapping posts) so that they are actionable.

We highlight that the effective design of crisis mapping platforms for information categorization requires a thorough understanding of the sociotechnical dynamics (Abbasi et al., 2024; Sarker et al., 2019) involved in processing and classifying RFH messages into accurate categories. Given that victims often submit RFH messages under high anxiety and time pressure during a disaster, they tend to be brief, incomplete, and often contain typographical errors and grammatical inaccuracies. Therefore, the intended meanings of these messages are often obscured, as the ground truths are either absent or difficult to convey. This presents a significant challenge for crowd volunteers to make plausible interpretations of RFH messages and categorize them correctly. While sensemaking theory was utilized as a kernel theory (Walls et al., 1992) to identify the platform design requirements for accurate information classification, we acknowledge that alternative theories, particularly those related to crisis communications (Sadri et al., 2018), could complement and enrich these design principles.

In addition, accurate categorization during crises is inherently time-consuming. Achieving consensus on categorization among independent crowd volunteers involves substantial behind-the-scenes work, such as finding and verifying the geolocation and accuracy of the information expressed in RFH messages. This can delay the timely execution of rescue operations that are critical for saving victims in disasterstricken areas. This highlights the importance of timeliness in determining the quality of crisis information (Seppänen & Virrantaus, 2015) and the effectiveness of categorization, particularly in the context of crisis management and digital humanitarian projects. We recognize that the design principles, rooted in sensemaking theory and real RFH data, do not address the timeliness dimension in information categorization. The IS community should explore ways to design better crisis mapping platforms that improve the speed of converting less useful RFH messages into accurately categorized and more useful crisis reports.

## Conclusion

Crisis mapping platforms are critical in digital humanitarian efforts since they provide an ability to rapidly improvise a large-scale collaborative network to solve crisis problems. These platforms are important in the way they facilitate the collection of crisis information, geomapping of victim data, and dissemination of situational and other key information. This study serves as a good starting point for the IS research community to expand our understanding of system design to support crowd workers in crisis mapping.

This study has the following limitations. Since we coded the contextual cues in a binary form, there could have been information loss. It was, however, inevitable, given that human coders manually read and coded RFH messages including the Haitian-Creole ones collected during the Haiti earthquake. Haitian-Creole messages were translated by crowd volunteers into English and entered into the Ushahidi crisis mapping platform. Therefore, coding the contextual cues into a continuous form of data would likely enrich the understanding of the effects of templated and non-templated reports on classification accuracy.

Some categories (e.g., infrastructure damage and natural hazards) may be semantically closer than others (such as public health and security threats), which may affect the measurement of categorization quality. However, our choice was influenced in part by the fact that Ushahidi has defined these categories. Also, while the data was collected from the Ushahidi platform for the Haiti earthquake, the content coding and RN-led categorization were not performed in the immediate aftermath of the crisis. As a result, Ushahidi crowd volunteers might have experienced a different sense of urgency in dealing with the crisis situation.

One possible future project would be to investigate the effectiveness of cues that aid in aggregating interactive posts<sup>12</sup> for accurate categorization. For instance, location information that is part of situational cues can assist crowd volunteers in mapping similar posts, enabling them to aggregate related information into relevant categories. This is especially important because it is difficult for crowd volunteers to crossreference from a large pool of victim reports, resulting in loss of efficiency.

There is also the potential for the IS research community to explore integrating crisis platform design with generative artificial intelligence (AI) capabilities, which have made significant advancements in text processing and information categorization. In the age of AI, crowd-based manual categorization may become less relevant especially with large language models (LLMs) becoming so powerful. Future studies should examine conditions under which experts such as RNs and crowd volunteers can augment or substitute crisis categorization provided by LLMs.

We also recommend that future studies automate the extraction of social keywords as well as situational information from RFH messages to automatically display it as templated reports. In addition to cue extraction, automating the aggregation of posts from the interactions of crowd volunteers will add value. Furthermore, future studies should evaluate the effectiveness of full or partial depiction of other taxonomies of cues. For example, it may make a difference to show the number of people affected instead of showing social cues or to highlight the appearance of frequently needed items or names of geographic areas instead of showing situational cues. Finally, this research note focuses on crowd volunteers as the direct users of the proposed design principles. However, there are other users within the crisis mapping context, such as first responders and victims. We recommend that future studies delve into the design principles for other types of crisis users.

## Acknowledgments

The authors would like to thank the SE, AE, and review team for their comments and suggestions, which greatly improved the paper. We also thank the Ushahidi team of Patrick Meier, Robert Munro, and Nona Lambert for sharing the crisis data with us and for patiently answering our innumerable questions. This work was supported by the National Science Foundation under Grant #2020252. The authors thank Masuma Dinani, Kavita Narwani, and Twiesha Vachhrajani for their research assistance. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

## References

Abbasi, A., Parsons, J., Pant, G., Sheng, O. R. L., & Sarker, S. (2024). Pathways for design research on artificial intelligence. Information Systems Research, 35(2), 441-459. https://doi.org/10.1287/ isre.2024.editorial.v35.n2

Agarwal, M., Leekha, M., Sawhney, R., Ratn Shah, R., Kumar Yadav, R., & Kumar Vishwakarma, D. (2020). Memis: Multimodal emergency management information system. In Proceedings of the 42nd European Conference on IR Research (pp. 479-494). https://doi.org/10.1007/978-3-030-45439-5\_32

Alam, K. M., Saini, M., & El Saddik, A. (2015). Toward social internet of vehicles: Concept, architecture, and applications. IEEE Access, 3, 343-357. https://doi.org/10.1109/ACCESS.2015.2416657

Alison, S. (2011). Need to know: Crisis mapping. PBS. https://www.pbs.org/video/need-to-know-crisis-mapping/

Alpers, G. W., Winzelberg, A. J., Classen, C., Roberts, H., Dev, P., Koopman, C., & Taylor, C. B. (2005). Evaluation of computerized text analysis in an Internet breast cancer support group. Computers in Human Behavior, 21(2), 361-376. https://doi.org/10.1016/j.chb.2004.02.008

Bera, P., Burton-Jones, A., & Wand, Y. (2011). Guidelines for designing visual ontologies to support knowledge identification. MIS Quarterly, 35(4), 883-908. https://doi.org/10.2307/41409965

Bittner, C., Glasze, G., & Turk, C. (2013). Tracing contingencies: Analyzing the political in assemblages of Web 2.0 cartographies. GeoJournal, 78, 935-948. https://doi.org/10.1007/s10708-013- 9488-8

Bock, J. G., & Lederach, J. P. (2012). Comparing the approaches. In The technology of nonviolence: Social media and violence prevention (pp. 135-146). MIT Press. https://doi.org/10.7551/ mitpress/9088.003.0015

Bomström, H., Annanperä, E., Kelanti, M., Xu, Y., Mäkelä, S. M., Immonen, M., & Päivärinta, T. (2022). Digital twins about humans: Design objectives from three projects. Journal of Computing and Information Science in Engineering, 22(5), Article 050907. https://doi.org/10.1115/1.4054270

Calvel, A., Werner, M., van den Homberg, M., Cabrera Flamini, A., Streefkerk, I., Mittal, N., Whitfield, S., Vanya, C. L., & Boyce, C. (2020). Communication structures and decision making cues and criteria to support effective drought warning in Central Malawi. Frontiers in Climate, 2, Article 578327. https://doi.org/10.3389/fclim.2020.578327

Camponovo, M. E., & Freundschuh, S. M. (2014). Assessing uncertainty in VGI for emergency response. Cartography and Geographic Information Science, 41(5), 440-455. https://doi.org/10.1080/15230406.2014.950332

Caragea, C., McNeese, N., Jaiswal, A., Traylor, G., Kim, H. W., Mitra, P., & Yen, J. (2011). Classifying text messages for the Haiti earthquake. In Proceedings of the 8th International Conference on Information Systems for Crisis Response and Management.

Castillo, C. (2016). Big crisis data: Social media in disasters and timecritical situations. Cambridge University Press. https://doi.org/ 10.1017/CBO9781316476840

Chowdhury, A., Ramadas, R., & Karmakar, S. (2013). Muscle computer interface: A review. In Proceedings of International Conference on Research into Design (pp. 411-421). https://doi.org/10.1007/978-81-322-1050-4\_33

Collier, N., Son, N. T., & Nguyen, N. M. (2011). OMG U got flu? Analysis of shared health messages for bio-surveillance. Journal of Biomedical Semantics, 2(5), Article S9. https://doi.org/10.1186/2041-1480-2-S5-S9

DeYoung, S. E., Sutton, J. N., Farmer, A. K., Neal, D., & Nichols, K. A. (2019). Death was not in the agenda for the day: Emotions, behavioral reactions, and perceptions in response to the 2018 Hawaii Wireless Emergency Alert. International Journal of

Disaster Risk Reduction, 36, Article 101078. https://doi.org/ 10.1016/j.ijdrr.2019.101078

Dootson, P., Thomson, T. J., Angus, D., Miller, S., Hurcombe, E., & Smith, A. (2021). Managing problematic visual media in natural hazard emergencies. International Journal of Disaster Risk Reduction, 59, Article 102249. https://doi.org/10.1016/j.ijdrr.2021. 102249

Douvinet, J., Kouadio, J., Bonnet, E., & Gensel, J. (2017). Crowdsourcing and crisis-mapping in the event of floods: Tools and challenges. Floods, 2, 209-223. https://doi.org/ 10.1016/B978-1-78548-269-4.50015-9

Edgeley, C. M., & Paveglio, T. B. (2019). Exploring influences on intended evacuation behaviors during wildfire: What roles for pre-fire actions and event-based cues? International Journal of Disaster Risk Reduction, 37. https://doi.org/10.1016/j.ijdrr. 2019.101182

Fendt, M., Parsons, M. H., Apfelbach, R., Carthey, A. J., Dickman, C. R., Endres, T., Frank, A. S. K., Heinz, D. E., Jones, M. E., Kiyokawa, Y., Kreutzmann, J. C., Roelofs, K., Schneider, M., Sulger, J., Wotjak, C. T., & Blumstein, D. T. (2020). Context and trade-offs characterize real-world threat detection systems: a review and comprehensive framework to improve research practice and resolve the translational crisis. Neuroscience & Biobehavioral Reviews, 115, 25-33. https://doi.org/10.1016/ j.neubiorev.2020.05.002

Fonte, C. C., Bastin, L., Foody, G., Kellenberger, T., Kerle, N., Mooney, P., & See, L. (2015). VGI quality control. ISPRS Annals of Photogrammetry, Remote Sensing and Spatial Information Sciences, 2, pp. 317-324. https://doi.org/10.5194/isprsannals-II-3- W5-317-2015

Gavrilova, M. L., Ahmed, F., Bari, A. H., Liu, R., Liu, T., Maret, Y., Sieu, B., & Sudhakar, T. (2021). Multi-modal motioncapture-based biometric systems for emergency response and patient rehabilitation. In Information Resources Management Association (Ed.), Research anthology on rehabilitation practices and therapy (pp. 653-678). IGI Global. https://doi.org/10.4018/978-1-7998-3432-8.ch032

Gibson, H., Akhgar, B., & Domdouzis, K. (2015). Using social media for crisis response: The ATHENA system. In Proceedings of the 2nd European Conference on Social Media (pp. 183-192).

Greaves, F., Ramirez-Cano, D., Millett, C., Darzi, A., & Donaldson, L. (2013). Use of sentiment analysis for capturing patient experience from free-text comments posted online. Journal of Medical Internet Research, 15(11), 1-9. https://doi.org/10.2196/jmir.2721

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). Research perspectives: The anatomy of a design principle. Journal of Association for Information Systems, 21(6), 1622-1652. https://doi.org/10.17705/1jais.00649

Hawk, S. R., & Aldag, R. J. (1990). Measurement biases in user involvement research. Omega, 18(6), 605-613.

Heinzelman, J., & Meier, P. (2015). Crowdsourcing for human rights monitoring: Challenges and opportunities for information collection and verification. In J. Lannon & E. Halpin (Eds.), Human rights and information communication technologies: Trends and consequences of use (pp. 123-138). IGI Global. https://doi.org/10.4018/978-1-4666-6433-3.ch024

Hosseini, M., Cox, I. J., Milić-Frayling, N., Kazai, G., & Vinay, V. (2012). On aggregating labels from multiple crowd workers to

infer relevance of documents. In Proceedings of the European Conference on IR Research (pp. 182-194). https://doi.org/10.1007/ 978-3-642-28997-2\_16

Hunt, A., & Specht, D. (2019). Crowdsourced mapping in crisis zones: Collaboration, organization, and impact. Journal of International Humanitarian Action, 4(1), 1-11. https://doi.org/10.1186/s41018- 018-0048-1

Imran, M., Elbassuoni, S., Castillo, C., Diaz, F., & Meier, P. (2013). Extracting information nuggets from disaster-related messages in social media. In Proceedings of the Information Systems for Crisis Response and Management Conference (pp. 791-801).

Jenvald, J., Morin, M., & Kincaid, J. P. (2001). A framework for webbased dissemination of models and lessons learned from emergency-response exercises and operations. International Journal of Emergency Management, 1(1), 82-94. https://doi.org 10.1504/IJEM.2001.000512

Kankanamge, N., Yigitcanlar, T., Goonetilleke, A., & Kamruzzaman, M. (2019). Can volunteer crowdsourcing reduce disaster risk? A systematic review of the literature. International Journal of Disaster Risk Reduction, 35. https://doi.org/10.1016/j.ijdrr.2019.101097

Klein, G., Jalaeian, M., Hoffman, R., & Mueller, S. (2021). The plausibility gap: A model of sensemaking (Technical report). DARPA Explainable AI Program.

Krippendorf, K. (2019). Content analysis: An introduction to its methodology. SAGE. https://doi.org/10.4135/9781071878781

Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. Biometrics, 33, 159-174. https://doi.org/10.2307/2529310

Lewis, W., Munro, R., & Vogel, S. (2011). Crisis MT: Developing a cookbook for MT in crisis situations. In Proceedings of the Sixth Workshop on Statistical Machine Translation (pp. 501-511). https://aclanthology.org/W11-2164

Li, M., & Wang, W. (2021). Educational disparities in COVID-19 prevention in China: The role of contextual danger, perceived risk, and interventional context. International Journal of Environmental Research and Public Health, 18(7), Article 3383. https://doi.org/10.3390/ijerph18073383

Lindell, M. K., & Perry, R. W. (2012). The protective action decision model: Theoretical modifications and additional evidence. Risk Analysis: An International Journal, 32(4), 616-632. https://doi.org/ 10.1111/j.1539-6924.2011.01647.x

Liu, S. B. (2014). Crisis crowdsourcing framework: Designing strategic configurations of crowdsourcing for the emergency management domain. Computer Supported Cooperative Work, 23(4-6), 389-443. https://doi.org/10.1007/s10606-014-9204-3

Lombardi, D., Nussbaum, E. M., & Sinatra, G. M. (2016). Plausibility judgments in conceptual change and epistemic cognition. Educational Psychologist, 51(1), 35-56. https://doi.org/10.1080 00461520.2015.1113134

Maitlis, S., & Christianson, M. (2014). Sensemaking in organizations: Taking stock and moving forward. The Academy of Management Annals, 8(1), 57-125. https://doi.org/10.1080/19416520.2014. 873177

Maitlis, S., & Sonenshein, S. (2010). Sensemaking in crisis and change: Inspiration and insights from Weick (1988). Journal of Management Studies, 47(3), 551-580. https://doi.org/10.1111/ j.1467-6486.2010.00908.x

McHugh, M. L. (2013). The chi-square test of independence. Biochemia Medica: Biochemia Medica, 23(2), 143-149. https://doi.org/10.11613/BM.2013.018

McClure, D. (2014). Can crisis mapping show innovation a new way to grow up? UN Refugee Agency. https://www.unhcr.org/ innovation/can-crisis-mapping-show-innovation-a-new-way-togrow-up/

Meier, P. (2010). Ushahidi & the unprecedented role of SMS in disaster response. iRevolution. https://irevolutions.org/2010/02/20/smsdisaster-response/

Meier, P. (2015). Digital humanitarians: How big data is changing the face of humanitarian response. CRC Press. https://doi.org/ 10.1201/b18023

Morrow, N., Mock, N., Papendieck, A., & Kocmich, N. (2011). Independent evaluation of the Ushahidi Haiti project. Development Information Systems International. https://reliefweb. int/report/haiti/independent-evaluation-ushahidi-haiti-project

Munro, R. (2010). Crowd-sourced translation for emergency response in Haiti: The global collaboration of local knowledge. In Proceedings of the AMTA Workshop on Collaborative Crowdsourcing for Translation. https://aclanthology.org/2010. amta-workshop.1/

Munro, R. (2011). Subword and spatiotemporal models for identifying actionable information in Haitian Kreyol. In Proceedings of the Fifteenth Conference on Computational Natural Language Learning (pp. 68-77).

Munro, R. (2013). Crowdsourcing and the crisis-affected community. Information Retrieval, 16(2), 210-266. https://doi.org/10.1007/ s10791-012-9203-2

Murthy, D., Gross, A., & McGarry, M. (2016). Visual social media and big data. Interpreting Instagram images posted on Twitter. Digital Culture & Society, 2(2), 113-134. https://doi.org/ 10.14361/dcs-2016-0208

Nabavian, S., & Parsons, J. (2024). A design-principle-friendly conceptual model of observational crowdsourcing. In Proceedings of the International Conference on Design Science Research in Information Systems and Technology (pp. 95-108). https://doi.org/10.1007/978-3-031-61175-9\_7

Oh, O., Agrawal, M., & Rao, H. R. (2013). Community intelligence and social media services: A rumor theoretic analysis of tweets during social crises. MIS Quarterly, 37(2), 407-426. https://doi.org/10.25300/MISQ/2013/37.2.05

Okolloh, O. (2009). Ushahidi, or “testimony”: Web 2.0 tools for crowdsourcing crisis information. Participatory Learning and Action, 59(1), 65-70.

Palen, L., & Anderson, K. M. (2016). Crisis informatics—New data for extraordinary times. Science, 353(6296), 224-225. https://doi.org/ 10.1126/science.aag2579

Pennebaker, J. W., Boyd, R. L., Jordan, K., & Blackburn, K. (2015). The development and psychometric properties of LIWC2015. University of Texas at Austin. https://doi.org/10.15781/T29G6Z

Pierce, C., & Fung, N. (2013). Crowd-sourcing data collection through Amazon Mechanical Turk. Army Research Laboratory. https://apps.dtic.mil/sti/pdfs/ADA585850.pdf

Podsakoff, P. M., MacKenzie, S. B., Lee, J. Y., & Podsakoff, N. P. (2003). Common method biases in behavioral research: a critical review of the literature and recommended remedies. Journal of Applied Psychology, 88(5), 879. https://doi.org/ 10.1037/0021-9010.88.5.879

Podsakoff, P. M., & Organ, D. W. (1986). Self-reports in organizational research: Problems and prospects. Journal of Management, 12(4), 531-544. https://doi.org/10.1177/0149206 38601200408

Sadri, A. M., Hasan, S., Ukkusuri, S. V., & Cebrian, M. (2018). Crisis communication patterns in social media during Hurricane Sandy. Transportation Research Record, 2672(1), 125-137. https://doi. org/10.1177/0361198118773896

Sarker, S., Chatterjee, S., Xiao, X., & Elbanna, A. (2019). The sociotechnical axis of cohesion for the IS discipline: Its historical legacy and its continued relevance. MIS Quarterly, 43(3), 695-720. https://doi.org/10.25300/MISQ/2019/13747

Scholer, F., Turpin, A., & Sanderson, M. (2011). Quantifying test collection quality based on the consistency of relevance judgments. In Proceedings of the 34th International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 1063- 1072). https://doi.org/10.1145/2009916.2010057

Seppänen, H., & Virrantaus, K. (2015). Shared situational awareness and information quality in disaster management. Safety Science, 77, 112-122. https://doi.org/10.1016/j.ssci.2015.03.018

Silverman, C. (Ed.). (2014). Verification handbook: An ultimate guideline on digital age sourcing for emergency coverage. European Journalism Centre.

South, D. (2010, February). Haiti earthquake prompts tech aid. Development Challenges, South-South Solutions. Retrieved from https://books.google.com/books?id=GxyYBgAAQBAJ&dq=ush ahidi+people+location+need&source=gbs\_navlinks\_s

Starbird, K., Muzny, G., & Palen, L. (2012). Learning from the crowd: Collaborative filtering techniques for identifying on-the-ground Twitterers during mass disruptions. In Proceedings of the Information Systems for Crisis Response and Management Conference.

Starbird, K., & Palen, L. (2011). Voluntweeters: Self-organizing by digital volunteers in times of crisis. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1071- 1080). https://doi.org/10.1145/1978942.1979102

Tavra, M., Racetin, I., & Peroš, J. (2021). The role of crowdsourcing and social media in crisis mapping: A case study of a wildfire reaching Croatian city of Split. Geoenvironmental Disasters, 8, 1- 16. https://doi.org/10.1186/s40677-021-00181-3

Taylor, J. R., & Van Every, E. J. (2000). The emergent organization: Communication as its site and surface. Lawrence Erlbaum Associates. https://doi.org/10.4324/9781410602275

Temnikova, I., Vieweg, S., & Castillo, C. (2015). The case for readability of crisis communications in social media. In Proceedings of the 24th International Conference on World Wide Web (pp. 1245-1250). https://doi.org/10.1145/2740908.2741718

Tierney, K., Lindell, M. K., & Perry, R. W. (2006). Facing hazards and disasters: Understanding human dimensions. National Academies Press. https://doi.org/10.17226/11671

Valecha, R., Oh, O., & Rao, H. R. (2013a). An exploration of collaboration over time in collective crisis response during the Haiti 2010 earthquake. In Proceedings of the International Conference on Information Systems.

Valecha, R., Sharman, R., Rao, H. R., & Upadhyaya, S. (2013b). A dispatch-mediated communication model for emergency response systems. ACM Transactions on Management Information Systems, 4(1), 1-25. https://doi.org/10.1145/2445560.2445562

van Gassel, F., Reymen, I., & Maas, G. (2019). Validating design principles for creative collaboration. International Journal of Design Sciences and Technology, 23(2), 125-143.

Vendreø, M. T. (2015). Disasters in the sensemaking perspective: The Præstø Fjord accident. In R. Dahlberg, O. Rubin, & M. T. Vendelø (Eds.), Disaster research (pp. 190-202). Routledge.

Venkatesan, S., Valecha, R., Yaraghi, N., Oh, O., & Rao, H. R. (2021). Influence in social media: An investigation of tweets spanning the 2011 Egyptian Revolution. MIS Quarterly, 45(4), 1679-1714. https://doi.org/10.25300/MISQ/2021/15297

Villela, K., Nass, C., Novais, R., Simões, P., Traina, A., Rodrigues, J., Jr., Menendez, J. M., Kurano, J., Franke, T., & Poxrucker, A. (2018). Reliable and smart decision support system for emergency management based on crowdsourcing information. In R. Valencia-García, M. Paredes-Valverde, M. Salas-Zárate, & G. Alor-Hernández (Eds.), Exploring intelligent decision support systems: Current state and new trends (pp. 177-198). Springer. https://doi.org/10.1007/978-3-319-74002-7\_9

Vuurens, J. B., & de Vries, A. P. (2012). Obtaining high-quality relevance judgments using crowdsourcing. IEEE Internet Computing, 16(5), 20-27. https://doi.org/10.1109/MIC.2012.71

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59. https://doi.org/10.1287/isre.3.1.36

Wang, X., Parameswaran, S., Bagul, D. M., & Kishore, R. (2018). Can online social support be detrimental in stigmatized chronic diseases? A quadratic model of the effects of informational and emotional support on self-care behavior of HIV patients. Journal of the American Medical Informatics Association, 25(8), 931-944. https://doi.org/10.1093/jamia/ocy012

Weick, K. E. (1995). Sensemaking in organizations. SAGE.

White, C. (2010). Social media and meta-networks for crisis mapping: Collaboratively building spatial data for situation awareness in disaster response and recovery management. In Proceedings of the Specialist Meeting Spatio-Temporal Constraints on Social Networks.

## About the Authors

Rohit Valecha: Rohit Valecha is an Associate Professor in the Department of Information Systems and Cyber Security at The University of Texas at San Antonio. His Ph.D. is from the University at Buffalo in management science and systems. He has research interests in crisis response, social media, and information security and privacy. He has published in several journals, including Management Information Systems Quarterly, Journal of the Association for Information Systems, Information Systems Frontiers, and other outlets. His work has received Best Paper and other awards at the Americas Conference on Information Systems, Design Science Research on Information Systems and Technology Conference, Conference on Information Systems and Technology, Workshop on Information Technology and Systems, and others.

Onook Oh: Onook Oh is an Associate Professor of information systems at the University of Colorado Denver. His past research has investigated rumor theory, assemblage theory, social media, social movement, and crisis management. He is currently conducting research on platform labor, social inequality, and eco-friendly information systems research. Recently, he completed a project on the use of body-worn cameras in U.S. police departments, which was funded by the U.S. National Science Foundation. His research has been published in MIS Quarterly, Information Systems Research, Policing and Society, and other outlets.

H. Raghav Rao: H. Raghav Rao is AT&T Chair Professor of Information Systems and Cybersecurity, Carlos Alvarez College of Business and a professor of computer science (courtesy appointment) at the University of Texas, San Antonio. He graduated from Purdue University. He has been a WCU visiting professor at Sogang University, South Korea, a Distinguished Visiting Faculty at UTS, Sydney, Australia, and at Swansea University, Wales, England and SUNY Distinguished Service Professor at the University at Buffalo. He also has been a Fulbright Nehru scholar at IIM Bangalore and Kasturbhai Lalbhai Visiting Chair in Management at IIM Ahmedabad, India.

## Appendix A

## Information Categorization

Table A1 presents sample information categories assigned to RFH messages by online volunteers in the wake of various crises.

<table><tr><td colspan="4">Table A1. Information Categorization in Crisis Situations (Extracted from Ushahidi)</td></tr><tr><td>Crisis situation</td><td>Crisis description</td><td>Categories</td><td>Examples</td></tr><tr><td>Italian vulnerable communities, 2020</td><td>Supply of food, medicine to vulnerable communities</td><td>Ready medicines or groceries</td><td>ID #137: (Translated) Home delivery of basic necessities. Collection and delivery of drugs. Services aimed at the whole communityCategory: Medicine, Grocery</td></tr><tr><td>San Antonio bike safety, 2018</td><td>Help to make San Antonio a safer city for cyclists</td><td>Infrastructure, safety, other</td><td>ID #146: Where the concrete and asphalt meet are ruts and raises that can cause problems on turns for cyclists.Category: Infrastructure, Safety,</td></tr><tr><td>Puerto Rico, Hurricane Maria, 2017</td><td>Reports of massive destruction and near total loss of power, flooded towns and fatalities</td><td>Flooded, medical assistance, health or hygiene, structure collapse, reported deaths, collapsed bridge, impassable highway, river out of the channel, etc.</td><td>Category: Structure Collapse, Antenna Collapse</td></tr><tr><td>Apartheid in Palestine, 2016</td><td>The grassroots Palestinian anti-apartheid wall campaign</td><td>Protest, killings</td><td>ID #59: Several protests happened in the Palestinian village close to the Green Line.Category: Protest</td></tr></table>

## Appendix B

## Contextual Cues

Table B1 classifies various types of contextual cues. The fourth column, with the header “Cues,” presents various types of cues that appear in the crisis literature. The fifth column “Type” classifies the cues into who, when, where, and what information types. The sixth column, with the header “Social/situational,” presents our taxonomy of contextual cues, according to the insights of sensemaking theory.

<table><tr><td colspan="6">Table B1. Contextual Cues in Crisis Situations</td></tr><tr><td>Cite</td><td>Purpose</td><td>Context</td><td>Cues</td><td>Type</td><td>Social/situational</td></tr><tr><td>Agarwal et al. (2020)</td><td>To identify and assess the level of damage incurred.</td><td>Hurricanes</td><td>Textual cues, visual cues</td><td>When</td><td>Situational</td></tr><tr><td>Villela et al. (2018)</td><td>To indicate a potentially dangerous situation</td><td>Emergency management</td><td>Density cues</td><td>When</td><td>Situational</td></tr><tr><td>Kankanamge et al. (2019)</td><td>To ensure loved ones are safe, to update the status of a situation, to meet victims&#x27; needs</td><td>Disaster risk management</td><td>Environmental cues, social cues</td><td>Who, What</td><td>Social, Situational</td></tr><tr><td>Fendt et al. (2020)</td><td>For social facilitation, to identify distance from shelter and intensity of threat</td><td>Threat detection</td><td>Contextual cues, threat cues</td><td>Where</td><td>Situational</td></tr><tr><td>Li and Wang (2021)</td><td>The emergence of threat in the immediate environment or presence of threat</td><td>Health crisis</td><td>Contextual cues, danger cues</td><td>When</td><td>Situational</td></tr><tr><td>Calvel et al. (2020)</td><td>To decide on how to carry out activities, farmers use cues from advisories or weather information based on local observations</td><td>Drought</td><td>Environmental cues, social cues</td><td>Who, When</td><td>Social, Situational</td></tr><tr><td>Murthy et al. (2016)</td><td>The analysis of affected area identified that visual cues are related to food and supplies</td><td>Disasters</td><td>Visual cues</td><td>What</td><td>Situational</td></tr><tr><td>Gavrilova et al. (2021)</td><td>To identify a person in distress</td><td>Health crisis (patient rehab)</td><td>Emotional cues</td><td>Who</td><td>Social</td></tr><tr><td>Dootson et al. (2021)</td><td>To enable decision-making and compliance with authority&#x27;s instructions</td><td>Natural hazards</td><td>Environmental cues, social cues</td><td>Who, Where</td><td>Social, Situational</td></tr><tr><td>Edgeley and Paveglio (2019)</td><td>To identify changes in fire behavior (intensity), evacuation notices and safety of household members</td><td>Wildfires</td><td>Evacuation cues, situational cues</td><td>When, Where</td><td>Situational</td></tr><tr><td>DeYoung et al. (2019)</td><td>To understand a situation or confirm an initial warning</td><td>Emergency alerts</td><td>Environmental cues, social cues</td><td>Who, What</td><td>Social, Situational</td></tr></table>

## Appendix C

## Crowd Interaction

Table C1 classifies various types of crowd interactions. The fourth column, with the header “Interaction,” presents various types of interactions that appear in the crisis literature. The fifth column “Type” classifies the interactions into location or information (focusing on user, resource and update) types. The sixth column, with the header “Mapping/gap-filling,” indicates our taxonomy of interaction modes, which we classified according to the insights of sensemaking theory.

<table><tr><td colspan="6">Table C1. Crowd Interactions in Crisis Situations</td></tr><tr><td>Cite</td><td>Purpose of the study</td><td>Context</td><td>Interactions</td><td>Type</td><td>Mapping/ gap-filling</td></tr><tr><td>Tavra et al. (2021)</td><td>To geo-reference social media crowdsourcing data to improve situational awareness during the forest fire</td><td>Wildfires, Croatia</td><td>User approval of location and position in posts</td><td>Location</td><td>Crisis mapping interaction</td></tr><tr><td>Munro (2013)</td><td>To report about the accuracy and timeliness in creating structured data from the messages and the collaborative nature of the process</td><td>Earthquake, Haiti</td><td>Comments</td><td>Information</td><td>Info gap-filling interaction</td></tr><tr><td>White (2010)</td><td>To identify impact zones and then once identified to populate a database with spatial data</td><td>Disaster (general)</td><td>Pin symbols and text to location sites</td><td>Location</td><td>Crisis mapping interaction</td></tr><tr><td>Gibson et al. (2015)</td><td>To introduce a crisis mapping system, requirement gathering process focusing on data processing, crisis dashboard and mobile application</td><td>Disaster (general)</td><td>Annotating locations; updating reports, audit trail</td><td>Location, Information</td><td>Crisis mapping interaction; Info gap-filling interaction</td></tr><tr><td>Douvinet et al. (2017)</td><td>To evaluate the contributions and limitations of crisis mapping tools, present expected benefits of data from these tools</td><td>Floods (general)</td><td>Compilation of geo-located damage; comments and discussions</td><td>Location, Information</td><td>Crisis mapping interaction; Info gap-filling interaction</td></tr></table>

## Appendix D

## Validation of Social Cues

LIWC features have been validated in prior literature and demonstrated a moderate correlation between human coding and LIWC coding (Alpers et al., 2005). Based on Wang et al. (2018), we validated the LIWC measurement of social cues in two steps: (1) having human coder manually code randomly selected RFHs, and (2) correlating human coding with LIWC measures for the random sample. In the first step, we provided 200 threads to the research assistants, who helped us with content coding. We asked them to code social cues as 0 in the absence of information about the presence and scale of victims, and 1 otherwise. In the second step, we performed a Spearman rho correlation between the research assistant-coded social cues and the LIWC-based measurement of social cues. Prior studies suggest that a Spearman rho value greater than 0.6 validates the agreement between human coding and LIWC measurements (Collier et al., 2011; Greaves et al., 2013). The Spearman rho value was identified as 0.627, p < 0.01, indicating the validity of the LIWC measurement of social cues.

## Appendix E

## Validation of Situational Cues

Research assistants separately coded the content within the RFHs for situational cues. We asked them to check for the presence of information about victims’ condition, their needs and location within the crisis reports. If such information was not present, we coded 0 for situational cues within the RFHs. The situational cues were coded from 0 to 3, where 0 denoted the absence of any of the three pieces of situational information, and 3 denoted the presence of all three pieces of situational information.

We used 200 RFHs for pilot coding (100 in each of two rounds of pilot coding) to code situational cues, which were excluded from the actual content analyses. Both rounds of pilot coding resulted in a kappa value greater than 0.7 (see Table E1 for situational cues coding), thereby confirming that the coding is robust. Some RFH messages can have one or more elements of situational cues simultaneously. We ensured that the pilot sample data were excluded from the data sample.

<table><tr><td colspan="3">Table E1. Results of Content Coding and Analysis</td></tr><tr><td rowspan="2"></td><td>Round 1 (N = 100)</td><td>Round 2 (N = 100)</td></tr><tr><td>Kappa value</td><td>Kappa value</td></tr><tr><td>Situational cues</td><td>0.987</td><td>0.973</td></tr></table>

## Appendix F

## Study 1: Preliminary Validation of the Template

The goal of this cross-sectional experiment was to test whether categorization quality is significantly improved by the presence of the template (versus its absence). The categorization quality was measured as the degree of agreement between students’ categorization and the RN-led team’s categorization as a baseline (Heinzelman & Meier, 2012; Silverman, 2014)

## Recruitment and Procedure

We recruited students (henceforth referred to as respondents) from two undergraduate classes at a large public university in the southwestern U.S. They shared similar characteristics with Ushahidi volunteers, several of whom were students at Tufts University (Munro, 2010; Meier, 2010). We randomly selected four crisis reports from the Ushahidi dataset. For each crisis report, we created two formats: (1) original crisis report (henceforth referred to as non-templatic), and (2) original crisis report with a template that displayed contextual cues and interactiv posts (henceforth referred to as templatic). Figure 3 shows a sample crisis report on the left with a template that displays social and situational cues as well as information gap-filling and crisis-mapping interactive posts.

We provided the four crisis reports (CR) in both templatic (T) and non-templatic (NT) formats to each respondent. To avoid bias (resulting from exposure to templatic crisis reports that may prime the respondents), we randomized the presentation of the templatic and non-templatic formats. We ensured that the templatic and non-templatic formats of the same crisis report were never displayed in sequence and that two crisis reports in the same formats were never displayed in order. Finally, for the second format of a crisis report, we changed the proper nouns (i.e. names of people, places, or landmarks) to reduce the learning effect. The four crisis reports and the two formats thus represented a 4×2 within-subject design, wherein each respondent categorized each crisis report displayed in both templatic and non-templatic formats.

For each crisis report, we created a survey asking respondents to read the crisis report and then select one or more of the eight categories. The survey was anonymous but captured respondents’ demographics and background information. We included attention check questions to filter out respondents who didn’t demonstrate sufficient cognitive effort while completing the survey.

## Descriptive Statistics

We collected data from 82 respondents categorizing four crisis reports displayed in templatic (T) and non-templatic (NT) formats into eight categories. After filtering out those respondents who failed the attention check questions, we were left with 67 qualified respondents (81.71%). Table F1 reports respondents’ key demographic information. Of the 67 respondents, 37 were men and 30 women. Around half of them had an associate degree. There were 35 respondents with prior crisis experience, including hurricanes, flooding, tornados, blackouts, fires, etc.

<table><tr><td colspan="3">Table F1. Descriptive Statistics (Study 1)</td></tr><tr><td>Criteria</td><td>Value (N = 67)</td><td>Percent</td></tr><tr><td>Male</td><td>37</td><td>55.22%</td></tr><tr><td>Female</td><td>30</td><td>44.78%</td></tr><tr><td>Some college</td><td>26</td><td>38.81%</td></tr><tr><td>Associate degree</td><td>30</td><td>44.78%</td></tr><tr><td>Graduate degree or higher</td><td>11</td><td>16.42%</td></tr><tr><td>Crisis experience</td><td>35</td><td>52.24%</td></tr><tr><td>No crisis experience</td><td>32</td><td>47.76%</td></tr></table>

## Overall Measure of Categorization Agreement

We analyzed the template’s effect on the agreements between the respondents’ and the RN-led team for each category of templatic crisi reports as well as non-templatic crisis reports. We counted respondents agreeing with the RN-led team on the presence of a certain category for a certain crisis report. For example, for the four templatic crisis reports (CR1, CR2, CR3, CR4), four respondents (65, 64, 57, 64) agreed on the infrastructure damage category, respectively. For non-templatic crisis reports (CR1, CR2, CR3, CR4), 4 respondents (63, 59, 52, 58) agreed on the infrastructure damage category respectively. Overall, there were 250 (93.28%) agreements for the templatic and 232 (86.57%) agreements for the non-templatic crisis reports on the infrastructure damage category. The total agreement is thus the sum of agreements between respondents and the RN-led team for each of the eight categories of the four crisis reports.

To compare agreements between the respondents and the RN-led team on the templatic and the non-templatic crisis reports, we conducted a chi-square $( \chi ^ { 2 } )$ test of independence,<sup>13</sup> which is an important statistic for testing differences for count variables (McHugh, 2013). Result show that the template is effective in improving categorization quality. We found that for the templatic crisis reports, there were a total of 1,546 (72.11%) agreements as opposed to 1,487 (69.36%) agreements for non-templatic crisis reports. This implies that agreements for the templatic crisis reports are significantly higher than the non-templatic ones $( \chi ^ { 2 } = 3 . { \overset { \underset { \mathrm { \textstyle ~ . ~ } } { } } { 9 } } 2 1 , p < 0 . 0 5 )$

## Appendix G

## Study 2: Effectiveness of the Template in Crisis Context

The goal of the temporal experiment was to conduct randomized experiments to discern the effectiveness of the template for improving crowd categorization quality (agreements) in the crisis context for difficult-to-categorize (vs. easy-to-categorize) crisis reports over two waves for individual categories (emergency, vital lines, health, security, infrastructure damage, natural hazard, services and other).

## Recruitment, Procedure and Manipulation Check

Due to the nature of RFH, which is noisy, ambiguous, and incomplete, some crisis reports may be difficult to categorize. For easy-tocategorize reports with relatively complete information, there would be high agreement among the respondents. However, when it is more difficult to categorize, different crowd volunteers would suggest various categories resulting in low agreement. As mentioned earlier, templatic representation of crisis reports enables sensemaking, which can improve categorization quality. In Study 2, we tested the template’s effectiveness for difficult-to-categorize crisis reports in improving categorization quality.

We conducted a two-wave study over a month where we provided the template that displays both features: contextual cues and interactive posts. We tested the categorization quality measured through agreements on categories at two different time points, separated by two weeks. This time-lagged approach provides support for causal precedence (Podsakoff et al., 2003) when testing the template’s effect on categorization quality. It also minimizes the cognitive burden on respondents (Hawk & Aldag, 1990; Podsakoff & Organ, 1986). Respondents completed the categorization exercise over the course of a month, with about two weeks between the first and second waves.

We recruited respondents from three undergraduate classes and one graduate class<sup>14</sup> at a large public university in the southwestern U.S. These respondents had similar characteristics to Ushahidi volunteers at Tufts University during the Haiti earthquake (Munro, 2010; Meier, 2010). We randomly selected 10 crisis reports from the Ushahidi dataset. Half of them were easy to categorize and the other half were difficult to categorize. We measured this difficulty of categorization based on the agreement of original Ushahidi crowd volunteers (during the Haiti crisis) with the registered nurse (RN)-led team. When the agreement was less, we labeled the crisis reports as difficult-to-categorize, and easy-to-categorize otherwise. For example, the crisis report ID #2637 is identified as difficult-to-categorize because Ushahidi crowd volunteers identified vitals and services categories, while the RN-led team identified infrastructure and hazard categories (i.e. low agreement in categories identified by the two groups).

ID #2637: I live in Gressier. A lot of houses have collapsed and a lot of people have died.

Ushahidi volunteer categories: Vitals, Services

RN-led team categories: Infrastructure, Hazard

Similar to Study 1, for each crisis report, we created two formats: (1) original crisis report (non-templatic), and (2) original crisis reports attached with a template displaying both contextual cues and interactive posts (templatic). In the first time period (Wave 1), we randomly assigned the respondents to a templatic or non-templatic group. For the respondents in the templatic group, we provided the 10 crisis reports in templatic format, while the respondents in the non-templatic group were provided with the 10 crisis reports in the original format. We randomly presented the easy- and difficult-to-categorize crisis reports to the respondents. For each crisis report, we asked the respondents to read the crisis report and then select one or more of the eight categories. We captured demographics and background information for the respondents in the first time period. We included attention check questions in the first time period to identify respondents who put sufficient cognitive effort into the survey.

In the second time period (Wave 2), we utilized the same 10 crisis reports. However, we switched the groups so that the respondents who were assigned to the templatic group in the first time period were assigned to the non-templatic group in the second time period and viceversa. Again, we randomly presented the easy- and difficult-to-categorize crisis reports to the respondents and asked them to read the crisis report and then select one or more of the eight categories. Attention check questions (ACQs) were also included in the second time period.

The categorization exercises in the two time periods were anonymous. To reduce the recall bias in the second time period, we conducted another categorization exercise between the first and second time periods, wherein respondents were asked to categorize 10 different crisis reports in the same format as in the first time period. The 10 crisis reports and the two formats thus represented a 10×2 within-subject design, wherein each respondent categorized the 10 crisis reports displayed in both templatic and non-templatic formats. The summary of the experiment is depicted in Table G1.

<table><tr><td colspan="4">Table G1. Design of Study 2</td></tr><tr><td></td><td>Week 1 (Wave 1)(Time Period 1)</td><td>Week 2(To reduce recall)</td><td>Week 3 (Wave 2)(Time Period 2)</td></tr><tr><td>Messages</td><td>CR1 ... CR10</td><td>CR11 ... CR20</td><td>CR1 ... CR10</td></tr><tr><td rowspan="2">Assignment</td><td>Template</td><td>Template</td><td>Non-template</td></tr><tr><td>Non-template</td><td>Non-template</td><td>Template</td></tr><tr><td>Data</td><td>ACQ, demographics</td><td>ACQ</td><td>ACQ</td></tr></table>

The manipulation of the template displaying contextual cues and interactive posts was checked based on 7-point Likert-type scales administered after the respondents categorized the crisis reports. The results show that the treatment (template) was manipulated correctly. Specifically, when the respondents were provided with the template, they perceived that the template helped in categorization. Respondents reported that both manipulations were helpful. Specifically, contextual cues were rated helpful with a mean score of 4.437, and interactive posts were rated helpful with a mean score of 4.141.

## Measuring the Quality of Information Categorization

To measure the dependent variable, quality of categorization, we compared the agreement between the RN-led team and the respondents on each category individually. We created a binary measure of agreement on each category identified by the respondents and the registered nurse-led team, with 1 indicating that the respondent agreed with the RN-led team on that category and 0 otherwise.

## Descriptive Statistics

We obtained data from 122 respondents who categorized crisis reports displayed in templatic (T) and non-templatic (NT) format within the two time periods into eight categories. After filtering out the respondents who did not participate in each of the exercises, and those who failed the attention check questions, we were left with 94 qualified respondents (77.05%). Table G2 reports the details of the respondents based on key demographic information.

<table><tr><td colspan="3">Table G2. Descriptive Statistics for Study 2</td></tr><tr><td>Criteria</td><td>Value (N = 94)</td><td>Percent</td></tr><tr><td>Male</td><td>68</td><td>72.34%</td></tr><tr><td>Female</td><td>26</td><td>27.66%</td></tr><tr><td>Some college</td><td>35</td><td>37.23%</td></tr><tr><td>Associate degree</td><td>23</td><td>24.27%</td></tr><tr><td>Graduate degree or higher</td><td>36</td><td>38.30%</td></tr><tr><td>Crisis experience</td><td>31</td><td>32.98%</td></tr><tr><td>No crisis experience</td><td>63</td><td>67.02%</td></tr></table>

## Analysis

To test the effectiveness of the template for difficult-to-categorize crisis reports in improving categorization quality, we analyzed the agreements on each category. We examined the effect of the template displaying social, situational cues and gap-filling, mapping posts for difficult-to-categorize crisis reports (at Level 1), as well as the effect of respondents’ characteristics, namely gender, age, education, and crisis experience (at Level 2) on agreements for each individual category (emergency, vital lines, health, security, infrastructure damage, natural hazard, services and other). We ran multilevel binary logistic regression for each category in STATA using xtmelogit (mixed-effect logit) that could accommodate a binary outcome variable, as well as the hierarchical structure of crisis reports nested in respondents. The model was tested for each category as follows:

```txt
Level 1
AgreementCategory = β₀ + β₁Template + β₂Difficult_to_Categorize + β₃Template * Difficult_to_Categorize + e
Level 2
β₀ = γ₀₀ + γ₀₁Gender + γ₀₂Age + γ₀₃Education + γ₀₄Crisis Experience + u₀
β₁ = γ₁₀ + γ₁₁Gender + γ₁₂Age + γ₁₃Education + γ₁₄Crisis Experience + u₁
β₂ = γ₂₀ + γ₂₁Gender + γ₂₂Age + γ₂₃Education + γ₂₄Crisis Experience + u₁
β₃ = γ₃₀ + γ₃₁Gender + γ₃₂Age + γ₃₃Education + γ₃₄Crisis Experience + u₁
Combined
AgreementCategory
= γ₀₀ + γ₀₁Gender + γ₀₂Age + γ₀₃Education + γ₀₄Crisis Experience + γ₁₀Template
+ γ₂₀Difficult_to_Categorize + γ₃₀Template * Difficult_to_Categorize + e
```

<table><tr><td></td><td colspan="2">Agreement match respondent vs. RN (health category)</td><td colspan="2">Agreement match respondent vs. RN (service category)</td><td colspan="2">Agreement match respondent vs. RN (emergency category)</td><td colspan="2">Agreement match respondent vs. RN (vitals category)</td><td colspan="2">Agreement match respondent vs. RN (hazard category)</td></tr><tr><td></td><td>Coefficient (std. err.)</td><td>Odds ratio</td><td>Coefficient (std. err.)</td><td>Odds ratio</td><td>Coefficient (std. err.)</td><td>Odds ratio</td><td>Coefficient (std. err.)</td><td>Odds ratio</td><td>Coefficient (std. err.)</td><td>Odds ratio</td></tr><tr><td>Constant</td><td>2.850**(1.098)</td><td>17.196</td><td>1.971*(0.837)</td><td>7.151</td><td>1.779***(0.540)</td><td>5.904</td><td>1.924**(0.735)</td><td>6.824</td><td>3.193***(0.667)</td><td>24.216</td></tr><tr><td>Gender</td><td>0.036(0.552)</td><td>1.037</td><td>-0.431(0.436)</td><td>0.650</td><td>-0.059(0.278)</td><td>0.943</td><td>-0.404(0.377)</td><td>0.668</td><td>0.057(0.322)</td><td>1.059</td></tr><tr><td>Age</td><td>0.016(0.038)</td><td>1.016</td><td>-0.012(0.029)</td><td>0.988</td><td>-0.000(0.019)</td><td>1.000</td><td>0.040(0.027)</td><td>1.041</td><td>0.016(0.024)</td><td>1.016</td></tr><tr><td>Education</td><td>-0.153(0.220)</td><td>0.858</td><td>-0.036(0.170)</td><td>0.965</td><td>-0.013(0.111)</td><td>0.987</td><td>-0.097(0.150)</td><td>0.908</td><td>-0.053(0.131)</td><td>0.948</td></tr><tr><td>Crisis experience</td><td>-0.396(0.508)</td><td>0.674</td><td>0.558(0.407)</td><td>1.745</td><td>-0.032(0.258)</td><td>0.969</td><td>-0.195(0.351)</td><td>0.823</td><td>-0.345(0.299)</td><td>0.709</td></tr><tr><td>Difficult to categorize</td><td>0.355(0.218)</td><td>1.425</td><td>-0.000(0.173)</td><td>1.000</td><td>-0.764***(0.167)</td><td>0.466</td><td>-1.940***(0.192)</td><td>0.144</td><td>-0.118***(0.266)</td><td>0.889</td></tr><tr><td>Template</td><td>0.711**(0.229)</td><td>2.033</td><td>0.360*(0.177)</td><td>1.432</td><td>-0.469**(0.170)</td><td>0.626</td><td>-0.655***(0.196)</td><td>0.520</td><td>-0.411(0.289)</td><td>0.663</td></tr><tr><td>Template × Difficult to categorize</td><td>-0.711*(0.321)</td><td>0.492</td><td>-0.419^(0.247)</td><td>0.658</td><td>0.552*(0.229)</td><td>1.735</td><td>0.927***(0.252)</td><td>2.523</td><td>0.722*(0.364)</td><td>2.056</td></tr></table>

Note: ^ p < 0.10; \* p < 0.05; \*\* p < 0.01; \*\*\* p < 0.001

## Results

Table G3 shows a significant positive template main effect for the health and service categories. According to this result, the presence of the template with crisis reports is positively associated with agreements on the health and service categories $( z = 3 . 1 0 ; p < 0 . 0 1$ and z = 2.03; p < 0.05) respectively. This implies that, for the health and service categories, the presence of the template along with the original crisis report is likely to result in 2 and 1.5 times higher agreement compared to the absence of a template with the crisis report (non-templatic), respectively.

Results also show a significant positive interaction effect for the emergency, vitals, and hazard categories. In order to interpret the interaction effect, we refer to graphs (see Figure 4). Figures G1a, G1b, and G1c depict that for difficult-to-categorize crisis reports, the presence of the template yields a higher agreement in emergency, vitals, and hazard categories respectively. According to this result, the effect of the template for difficult-to-categorize crisis reports in achieving agreement is positive and significant for the emergency, vitals, and hazard categories (z $= 2 . 4 1 ; \mathbf { p } < 0 . 0 5$ and z = 3.68; p < 0.001 and z = 1.99; p < 0.05, respectively). This indicates that, for the emergency, vitals, and hazard categories, the presence of the template attached to the original crisis report is likely to result in 1.7, 2.5, and 2 times higher agreement for difficult-to-categorize crisis reports as compared to the non-templatic crisis report, respectively. The effect of template on agreement (template main effect) and the effect of template for difficult-to-categorize crisis reports on agreement (interaction effect) are not significant for security, infrastructure, and other categories.

![](/api/attachments/VKV8C66S/fulltext/images/50988d00804958506b7ae4e3524b25e6087fde0644ef79ab5680e729f8217372.jpg)  
Figure G1a. Template × Difficult to Categorize for Emergency Category

![](/api/attachments/VKV8C66S/fulltext/images/9483d77d62c641de47402b70059e734d93e06f00e14f04599bf1c656c28eca75.jpg)  
Figure G1b. Template × Difficult to Categorize for Vitals Category

![](/api/attachments/VKV8C66S/fulltext/images/6d3b890e0284a3e6060f70d7430bece8ac765ce0be2154dbeb6326c0faa1e6ca.jpg)  
Figure G1c. Template × Difficult to Categorize for Hazard Category
