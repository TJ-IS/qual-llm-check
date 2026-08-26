---
otero_id: 11474
otero_key: "Q3MA5N8S"
title: "Designing Attentive Information Dashboards"
authors: "Peyman Toreini; Moritz Langner; Alexander Maedche; Stefan Morana; Tobias Vogel"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00732"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 23 Issue 2

Article 4

2022

## Designing Attentive Information Dashboards

Peyman Toreini , peyman.toreini@kit.edu

Moritz Langner , moritz.langner@kit.edu

Alexander Maedche , alexander.maedche@kit.edu

Stefan Morana , stefan.morana@uni-saarland.de

Tobias Vogel , tobias.vogel@h-da.de

Follow this and additional works at: https://aisel.aisnet.org/jais

# Designing Attentive Information Dashboards

Peyman Toreini <sup>1</sup>, Moritz Langner<sup>2</sup>, Alexander Maedche<sup>3</sup>, Stefan Morana<sup>4</sup>, Tobias Vogel<sup>5</sup>

<sup>1</sup>Karlsruhe Institute of Technology, Germany, peyman.toreini@kit.edu

<sup>2</sup>Karlsruhe Institute of Technology, Germany, moritz.langner@kit.edu

<sup>3</sup>Karlsruhe Institute of Technology, Germany, alexander.maedche@kit.edu

<sup>4</sup>Saarland University, Germany, stefan.morana@uni-saarland.de

<sup>5</sup>Darmstadt University of Applied Sciences / University of Mannheim, Germany, tobias.vogel@h-da.de

## Abstract

Information dashboards are a critical capability in contemporary business intelligence and analytics systems. Despite their strong potential to support better decision-making, the massive amount of information they provide challenges users performing data exploration tasks. Accordingly, dashboard users face difficulties in managing their limited attentional resources when processing the presented information on dashboards. Also, studies have shown that the amount of concentrated time humans can spend on a task has dramatically decreased in recent years; thus, there is a need for designing user interfaces that support users’ attention management. In this design science research project, we propose attentive information dashboards that provide individualized visual attention feedback (VAF) as an innovative artifact to solve this problem. We articulate theoretically grounded design principles and instantiate a software artifact leveraging users’ eye movement data in real time to provide individualized VAF. We evaluated the instantiated artifact in a controlled lab experiment with 92 participants. The results from analyzing users’ eye movement after receiving individualized VAF reveal that our proposed design has a positive effect on users’ attentional resource allocation, attention shift rate, and attentional resource management. We contribute a system architecture for attentive information dashboards that support data exploration and two theoretically grounded design principles that provide prescriptive knowledge on how to provide individualized VAF. Practitioners can leverage the prescriptive knowledge derived from our research to design innovative systems that support users’ information processing by managing their limited attentional resources.

Keywords: Eye Tracking, Attentive User Interface, Design Science Research, Information Dashboards

Sudha Ram was the accepting senior editor. This research article was submitted on December 16, 2019 and underwent two revisions.

## 1 Introduction

Already in 1971, Herbert Simon pointed out that “in an information-rich world, the wealth of information means a dearth of something else: a scarcity of whatever it is that information consumes … it consumes the attention of its recipients.” (Simon, 1971, pp. 40-41). Following this thinking, Goldhaber (1997) and Davenport and Beck (2001) articulated the concept of the “attention economy,” emphasizing that human attention should be treated as a scarce commodity in today’s information-rich world. According to the CEO of Microsoft, Satya Nadella, “we are moving from a world where computing power was scarce to a place where it now is almost limitless, and where the true scarce commodity is increasingly human attention” (Gausby, 2015, p. 4).

Studies have shown that users’ attention spans, i.e., the amount of concentrated time a person can spend on a task without becoming distracted, have massively decreased in recent years (Gausby, 2015; Statistics Brain, 2015). This means that users today allocate their attention to tasks for only short periods of time and shift their attention rather quickly. However, proper attention allocation plays an important role in information processing, as it enables individuals to focus on important information to pursue goals (Atkinson & Shiffrin, 1968; Wickens et al., 2016) and perform tasks (Bera et al., 2019; Orquin & Mueller Loose, 2013). Given this situation, supporting users in managing their limited attentional resources is one of the most pressing and difficult challenges in practice and research in our current information-rich world (Anderson et al., 2018; Bulling, 2016; Davern et al., 2012; Lerch & Harter, 2001).

In the digital world, users’ attentional resource allocation is driven by stimulus features provided by user interfaces (UI) (Ahn et al., 2018; Lorigo et al., 2008; Nielsen, 2006). Because attention is a limited resource (Broadbent, 1958; Chun et al., 2011; Kahneman, 1973), users cannot attend to all stimuli at the same time and need to select specific parts on the UI. UI designers are aware of this and are attempting to overcome this limitation and direct users’ attention to important items by integrating specific design elements (e.g., size, color, animation, etc.) regarding the users’ specific tasks (Cheung et al., 2017; Hong et al., 2004). However, some tasks may require a comprehensive overview of all information presented on the UI. For these tasks, users need to conduct several attention shifts to properly allocate their attention to all information rather than having their attention guided by specific design features. Users’ attention shift rate can differ according to task, characteristics, and UI design. Therefore, to process all information on a UI, users need to manage their attentional resource allocation by themselves.

To support that, studies suggested several years ago that intelligent UIs, identified as attentive UI, should be designed to assist users in managing their attentional resources. Vertegaal (2003, p. 32) described attentive UIs as “computer interfaces that are sensitive to the user’s attention,” and that “measure and model the focus and priorities of attention … structuring communication such that the limited resource of attention is allocated optimally across the user’s tasks.” Recently, scholars from different disciplines have emphasized the increasing need for designing attentive UIs, especially when users are dealing with huge amounts of information (Anderson et al., 2018; Bailey & Konstan, 2006; Bulling, 2016; Roda, 2011; Roda & Thomas, 2006).

In the information-rich world, organizations collect and analyze data from various sources to assist users in making better decisions and bringing more value to the business (Günther et al., 2017). Collecting data, extracting insight, and creating value from data represent many complex activities included in companies’ attempts to advance users’ possibilities. One key activity is helping decision makers gain seamless access to information from different perspectives in the form of descriptive analytics (Delen & Ram, 2018). A well-known class of information systems (IS) that supports such data-driven decisions are business intelligence and analytics (BI&A) systems (Chen et al., 2012). Information dashboards are a prominent mechanism facilitating the interaction between decision-makers and BI&A systems (Behrisch et al., 2018; Pauwels et al., 2009; Preece et al., 2015; Yigitbasioglu & Velcu, 2012). Few (2006, p. 34) has defined the information dashboard<sup>1</sup> as “a visual display of the most important information needed to achieve one or more objectives that has been consolidated on a single computer screen so it can be monitored at a glance.”

Dashboards are known as one of the most effective BI&A tools (Negash & Gray, 2008). They should be designed to present insights in a comprehensive way and be effective for decision makers (Bačić & Fadlalla, 2016; Pauwels et al., 2009; Phillips-Wren et al., 2015; Yigitbasioglu & Velcu, 2012). Also, Gartner (2017) has emphasized that well-designed dashboards enable data exploration and support proper decision-making as a critical capability of BI&A systems. In data exploration tasks, the user browses the dashboard generally to get a comprehensive understanding of the visualized information. In this case, the user examines data without having prior understanding of what information it might contain (Baker et al., 2009; Vandenbosch & Huff, 1997). However, even with a well-designed dashboard, users find processing the compressed amount of visualized information challenging (Baskett et al., 2008; Figl & Laue, 2011; Haroz & Whitney, 2012; Healey & Enns, 2012; Sedig & Pasob, 2013). Many BI&A systems are not beneficial to organizations because of inadequate design and improper use of interaction technologies, including dashboards (Deng & Chi, 2012; Schwarz et al., 2014; Trieu, 2017). In fact, the main challenge of organizations is not to collect more information and derive insights but to use the information effectively (Lerch & Harter, 2001).

In the first stage, users’ cognition plays an important role in making business decisions (Chen & Lee, 2003; Niu et al., 2013). However, humans have limited cognitive abilities that affect their performance, even when working with dashboards (Davern et al., 2012; Lerch & Harter, 2001; Yigitbasioglu & Velcu, 2012). In particular, dashboards can potentially create difficulties for users managing their attentional resources. Attentional resources are allocated as a set of processes enabling and guiding the selection of incoming perceptual information (Eriksen & Yeh, 1985). When exploring dashboards, users can only focus on a limited selection of information, thus missing other parts (Alberts, 2017; Dilla et al., 2010). Properly allocating attentional resources is necessary to analyze business insights when processing information dashboards (Lerch & Harter, 2001; Singh, 1998). Therefore, advanced dashboards should support users in managing attentional resources. Existing research on BI&A systems is limited to their business significance, while their widespread use and role in providing solutions regarding corresponding users’ cognitive challenges when they work with BI&A systems continue to present a research gap (Browne & Parsons, 2012; Chen & Lee, 2003; Davern et al., 2012; Niu et al., 2013).

In this study, we focus on designing attentive information dashboards that are sensitive to users’ attention and assist them in allocating their attention properly across the entire dashboard. Because users predominantly interact with dashboards through the visual channel, we propose designing a self-tracking feature based on how users visually explore dashboards. Research has long been interested in attention allocated through visual channels (i.e., visual attention) (Carrasco, 2011), especially regarding users’ eye movements as an approximation for measuring their visual attention (Kowler, 2011). Scholars in IS have also suggested using eye trackers to design innovative IS applications (Davis et al., 2014; Dimoka et al., 2012; Riedl & Léger, 2016; vom Brocke et al., 2013).

In the BI&A field, eye tracking technology has thus far been limited to use for diagnostic purposes (Kurzhals et al., 2016). However, researchers have called for integrating eye tracking technology in BI&A systems and designing innovative features that support decision makers as they use these systems, based on real-time eye movement data (Silva et al., 2019). Previous research has identified the need to provide feedback to proactively inform users of critical states (O’Donnell & David, 2000; Yigitbasioglu & Velcu, 2012). Providing such feedback positively contributes to employees’ performance (Chenoweth et al., 2004; Jung et al., 2010; Montazemi et al., 1996). In addition, previous studies in other disciplines highlight the positive impact of individualized visual attention feedback (VAF) as a self-tracking feature on information processing performance (Deza et al., 2017; Qvarfordt et al., 2010; Sharma et al., 2016; van Gog et al., 2009). However, only a few studies have examined the potential of eye movement data for designing such feedback for IS (Lux et al., 2018) and, to the best of our knowledge, no studies have specifically focused on integrating it for dashboards. Therefore, to close this knowledge gap in IS research, our study addresses the following research question:

RQ: How can attentive information dashboards that provide individualized visual attention feedback for data exploration tasks be designed to enhance users’ information processing?

To answer this research question, we conducted a comprehensive design science research (DSR) project (Gregor & Hevner, 2013) focusing on designing innovative artifacts within three design cycles. In this paper, we specifically focus on the second design cycle of our DSR project and propose two theoretically grounded design principles for attentive information dashboards. We instantiate both design principles in an artifact and evaluate the proposed design in a largescale, rigorous lab experiment. Specifically, we analyze users’ eye movements during their first use of the dashboard, after having received individualized VAF (revisit phase), and at the end of the task. In the experiment, we compare users who received individualized VAF to users who received general VAF in the form of a simple text explanation about the importance of proper attentional resource allocation when exploring the dashboard. Our results show that, indeed, individualized VAF positively influences users’ attentional resource allocation and management, as well as their attention shift rate.

Our findings contribute to the IS discipline by providing prescriptive knowledge in the form of theoretically grounded and evaluated design principles. Additionally, we contribute by designing and demonstrating attentive information dashboards for BI&A systems as an innovative artifact. From a practical point of view, we support dashboard designers in better understanding users’ challenges in managing their attention, and we assist them by designing an attentive information dashboard.

This paper is structured as follows. Section 2 summarizes the conceptual foundations and related work. Section 3 introduces the three design cycles of our larger DSR project and explains the second design cycle in more detail. In Section 4, we conceptualize our meta-requirements and design principles and describe the instantiation of the artifact. In Section 5, we derive the hypotheses and present the steps for evaluating the developed artifact and the experimental design. Section 6 presents the findings of the experiment, and Section 7 outlines our contributions, limitations, and avenues for future work.

## 2 Conceptual Foundations and Related Work

In this chapter, we first present the conceptual foundations for this study, including attention as a key concept and human information processing theory. Subsequently, we present relevant work related to this study that focuses on attentive UI that track users’ eye movement in real time. Further, we discuss existing work on systems that provide individualized VAF to improve the performance of users while processing information.

## 2.1 Conceptual Foundations

## 2.1.1 Attention

The Cambridge dictionary defines attention as “the act of directing the mind to listen, see, or understand.” Scholarly work, however, rarely offers a field-specific definition for the concept (Anderson et al., 2018) and considers it rather generally as selective processing of incoming sensory information (Driver, 2001), thus noting humans’ limited attention capacity (Chun et al., 2011). Selective attention was initially introduced as a part of Broadbent’s filter theory (Broadbent, 1958), which argues that humans’ perceptual system starts to process information through a selective filter to avoid being overwhelmed by information overload. The limited capacity of attentional resources is not fixed but can vary based on different conditions such as task and user characteristics (Kahneman, 1973). For example, an easy task requires limited attention, while a difficult task demands more attentional resources. Further, users with different kinds of expertise can have different capacities.

Attention has been differentiated as goal-directed vs. stimuli-driven, and as covert vs. overt (Desimone & Duncan, 1995). Goal-directed attention is steered voluntarily, whereas stimulus-driven attention is involuntary (Corbetta & Shulman, 2002). Scholars consider goal-directed attention as selective attention. In this case, users voluntarily and consciously select a stimulus to which they allocate their attention. In contrast, researchers refer to stimuli-driven attention when users unconsciously respond to external stimuli that capture their attention. Color, orientation, size, motion, depth, and the like, are known as guiding representations that involuntarily direct users’ attention to salient objects (Treisman & Gelade, 1980; Wolfe & Horowitz, 2004).

Further, Posner (1980) distinguished overt and covert attention as two additional categories. Overt attention is an extrinsic form of behavior that aids humans in monitoring the environment as well as guiding users’ head turning and eye movements toward an object (Carrasco, 2011). Overt attention can be measured using eye tracking devices (Kowler, 2011). The eyemind assumption (Just and Carpenter, 1980) explains the relationship between patterns of eye movement and their underlying cognitive processes. This assumption determines that users’ current fixation dedicates their overt attention. Both goal-directed and stimuli-driven attention control users’ eye movements and therefore overt attention during decision-making (Orquin & Mueller Loose, 2013). In contrast, covert attention is an inward activity in which the brain attends to an object without any extrinsic behavior. This attention type influences brain signals, typically measured by leveraging neuroscience tools such as electroencephalograms (EEG) and functional magnetic resonance imaging (fMRI) (Chun et al., 2011; Dimoka et al., 2012).

## 2.1.2 Human Information Processing Theory

The human mind is an information processing system (Card, 1983). Human information processing theory describes how individuals encode information, capture it in their memory, and retrieve it when needed. In this study, we refer to Wickens et al.’s (2016) adapted version of the human information processing stages. The adapted version enables a better understanding of users’ information processing when they interact with dashboards and distinguishes different components that affect their perception. Figure 1 depicts key elements of the human information processing theory used in this study and the relationship between them.

The first important component is the attention resource connected to sensory processing, perception, and memory processes. Generally, for information processing, allocating limited attention is considered in two different steps (Healey & Enns, 2012): First, preattentive processing relies on methods for drawing users’ stimulus-driven attention. In this step, users encode a stimulus for a short time based on the elements that attract their attention, and they perceive the information through their sensory organs (e.g., eye, ear, etc.). Second, post-attentive processing focuses on goal-directed attention, processing the perceived information in detail.

The second important component is memory. Atkinson and Shiffrin (1968) introduced the multistore model of memory to explain the relationship between three types of memory: (1) sensory memory stores raw information that the brain receives from the sense organ (e.g., color, shape, etc. of the objects) and keeps for few seconds; (2) working memory stores information temporarily and affects higher-order cognitive functions (Baddeley and Hitch, 1974); and (3) long-term memory stores information for a long time by rehearsing the information from the working memory.

![](/api/attachments/Q3MA5N8S/fulltext/images/e624b95ed6749975bb8ec9660012e575cba153de750fb0918520802ac0f02bdb.jpg)  
Figure 1. Human Information Processing Stages (adapted from Wickens et al., 2016)

Users encode and transfer information to the working memory by allocating their attention to the information collected in the sensory memory. Working memory plays an important role in complex cognitive behaviors such as comprehension, reasoning, and problemsolving (Engle, 2002). However, working memory capacity is a limited resource and is known as one important difference between individuals (Baddeley, 1992). Researchers have defined it as an important individual characteristic that people rely on when working with visualized information (Borkin et al., 2016; Haroz & Whitney, 2012; Healey & Enns, 2012; Toker et al., 2013). Miller (1956) has shown that humans can store seven (plus or minus two) information chunks. Moreover, he found that users can store more information if they receive it as chunked information. Users’ working memory capacity is important because it can predict their control of attentional resources (Engle et al., 1999; Kane et al., 2001; Kane & Engle, 2003). In addition, users with high and low capacities have different abilities to control their attentional resources, which impacts their task performance.

The third component is perception, the process of recognizing (being aware of), organizing (gathering and storing), and interpreting (binding to knowledge) information, e.g., as presented on dashboards (Ward et al., 2010). Information perception, for example on dashboards, subsequently supports users in making decisions based on this information (Ware, 2012).

## 2.2 Related Work

## 2.2.1 Eye Tracking and Information Dashboards

Duchowski (2002) categorizes eye tracking applications into two classes: diagnostic and interactive. Diagnostic eye tracking applications use offline records of eye movement data for further evaluation. Interactive eye tracking applications use eye movement data in real-time and enable eye-based interactions for their users. In the IS discipline, eye trackers are mainly used for diagnostic purposes (Riedl et al., 2017; Vasseur et al., 2019), and Dimoka et al. (2012), for example, emphasized eye tracking devices as important tools for understanding users’ visual behavior. Existing dashboard studies have utilized eye trackers to evaluate certain design features (e.g., presentation formats, colors, size, etc.) by analyzing offline records of eye movement data (Bera, 2014, 2016; Burch et al., 2011; Nadj et al., 2020). Other studies have investigated decision makers’ visual analytics strategies to determine the relationship between the accuracy, speed, and consistency of decisions (Cöltekin et al., 2010; Vila & Gomez, 2016) and users’ cognitive effort when working with visualized information (Fehrenbacher & Djamasbi, 2017; Smerecnik et al., 2010). Further, researchers have used eye movement data to examine the relationship between user characteristics and visualized information such as perceptual speed and visual and verbal working memory (Okan et al., 2016; Toker et al., 2013). However, only a few studies have utilized eye movement data in real time, e.g., for foveabased filtering (Okoe et al., 2014), and there is a need for further research on this topic (Silva et al., 2019).

Additionally, Majaranta and Bulling (2014) emphasized the attentive capability of eye tracking applications considered to be attentive UI. Attentive UIs are computer interfaces that are sensitive to users’ attention and structure communication by allocating limited attention optimally across users’ tasks (Vertegaal, 2003). Research on attentive UIs arose from the idea that users are increasingly surrounded by huge amounts of information, while their attention is a limited resource (Anderson et al., 2018; Bulling, 2016). Eye movement data represents the most popular data source for designing attentive UIs (Bulling, 2016; Henderson et al., 2013; Majaranta & Bulling, 2014). Researchers have developed attentive UIs in different fields, such as reading assistants in attentive documents (Buscher et al., 2012), attentive recommender systems (Xu et al., 2008), attentive tutoring systems (D’Mello et al., 2012), attentive UIs to support task resumption (Kern et al., 2010; Mariakakis et al., 2015), remote communications (D’Angelo & Gergle, 2018; Zhang et al., 2017), and attentive conversational agents (Ishii et al., 2013).

Although IS scholars have suggested using use eye movement data to design innovative systems (Davis et al., 2014; Dimoka et al., 2012; Maglio et al., 2000; Riedl & Léger, 2016; vom Brocke et al., 2013), applying attentive UIs to increase users’ awareness by means of self-tracking features has not been investigated in the IS discipline thus far. One possible reason for this could be the difficulty that users have with these devices as built-in functions of the IT artifact (vom Brocke et al., 2013). However, more recently, eye tracking technology usage has increased considerably in different research areas, primarily because of the availability of cheaper, faster, more accurate, and easier to use eye trackers (Duchowski, 2017). In this study, we attempt to close this research gap by using low-cost eye tracking devices for designing attentive information dashboards as a common UI used in BI&A systems.

## 2.2.2 Visual Attention Feedback

Providing users feedback during their interaction with a UI is one of the most basic and important usability principles (Nielsen, 1993). Preece et. al (2015, p. 26) defined feedback as “sending back information about what action has been done and what has been accomplished while allowing the person to continue with the activity.” Various feedback types are available to assist users in accomplishing their tasks in digital environments; for example, cognitive feedback presents information about users’ cognitive strategies (Lim et al., 2005; Nah & Benbasat, 2004). Prior studies have shown that cognitive feedback influences successful task accomplishment (Balzer et al., 1989; Nah & Benbasat, 2004; Sengupta & Te’eni, 1993).

Previous research in different disciplines has shown that using eye trackers to provide users with feedback about their attentional resource allocation can support them in improving their performance. For example, Sharma et al. (2016) showed that their gaze-aware feedback tool significantly improves students attentional resource allocation and learning gains. D’Mello et al. (2012) found that informing students about their information processing behavior supports reorienting their attentional patterns and promotes learning, motivation, and engagement. Sarter (2000) showed the need for giving feedback about effective attentional resource allocation to support users in managing their limited attention when working with highly complex information-rich environments. Deza et al. (2017) demonstrated the benefit of using eye trackers to improve users’ performance in visual search tasks because the huge amount of data makes operators susceptible to information overload and attentional resource allocation inefficiencies. Qvarfordt et al. (2010) and Sridharan et al. (2012) investigated the use of eye movement data as a form of feedback to improve the inspection method in various applications such as radiology and imaginary analysis.

Summing up existing research, we identified a lack of design knowledge describing how to provide feedback on users’ attentional resource allocation in order to improve their information processing performance in general. This is specifically relevant when users are exploring dense information on UIs, such as dashboards. Moreover, Lux et al.’s (2018) literature review of real-time feedback applications based on neuroscience tools in IS revealed that there is an IS research gap regarding the use of eye trackers for designing cognitive feedback. This study closes the identified research gap by contributing design knowledge on how to provide users with individualized feedback on their visual attention allocation when interacting with dashboards based on real-time eye movement data.

## 3 Design Science Research Project

This study is part of a larger DSR project that delivers an innovative solution (attentive information dashboards) for a real-world problem (managing users’ limited attentional resources) (Gregor & Hevner, 2013). Specifically, we address the lack of design knowledge on how to utilize users’ eye movement data in real time to provide feedback on attentional resource allocation. We adapted the approach from Kuechler and Vaishnavi (2012) and divided the entire DSR project into three consecutive design cycles (see Figure 2).

![](/api/attachments/Q3MA5N8S/fulltext/images/0a73a0d62a265d28a22a10f4aa8bb9abf060d50891fe383bef25f217997422b0.jpg)  
Figure 2. Design Cycles of the Research Project

The work presented in this paper focuses on the second design cycle. In the following sections, we briefly outline the overall DSR project to provide further background and to illustrate our overall research goal.

We started the first design cycle with an exploratory literature review on the use of eye tracking in the context of information visualization and dashboards. The findings highlight that previous research has used eye tracking devices mostly for diagnostic purposes by accessing offline records of users’ eye movement data. Further, previous studies have mainly focused on the role of limited attention and working memory for users exploring single charts (e.g., Borkin et al., 2013; Healey & Enns, 2012; Somervell, McCrickard, North, & Shukla, 2002) rather than several charts located on one screen in the form of a dashboard. To analyze business insights, exploring dashboards and properly allocating attentional resources (Lerch & Harter, 2001; Singh, 1998) is important. Cognitive limitations and related errors are underresearched topics in the IS field, which explains the general need for more research on these topics (Browne & Parsons, 2012). Also, only a few researchers have examined BI&A systems and users’ cognitive limitations when using these systems (Davern et al., 2012; Niu et al., 2013). Particularly, researchers have emphasized the need to study individual cognitive limitations with respect to the effectiveness of information dashboards (Pauwels et al., 2009; Yigitbasioglu & Velcu, 2012). Therefore, we conducted a pilot experimental study using eye tracking devices to investigate potential attention challenges and the role of users’ working memory capacity when interacting with dashboards (Toreini & Langner, 2019). We found that users tend to be biased toward charts located on the left side of the screen. Our findings are in sync with previous studies that have investigated users’ visual behavior on other information-rich UIs (Ahn et al., 2018; Lorigo et al., 2008; Nielsen, 2006). Also, we found that users repeat their behavior if they receive the same dashboard for a second time, independent of whether they have a low or high working memory capacity, and then do not allocate their attentional resources properly.

These findings support our conclusion that users require feedback in the form of individualized VAF. We thus focus on users’ goal-driven attention because we would like to support them in managing the attentional resources they voluntarily allocate to certain dashboard elements during data exploration tasks (Corbetta & Shulman, 2002). In addition, we focus on users’ overt attention in this project because we can measure that with eye tracking devices (Duchowski, 2017; Kowler, 2011) and can link users’ cognitive processes to their eye movements (Carrasco, 2011; Hayhoe & Ballard, 2005; Just & Carpenter, 1980; Kowler, 2011; Liversedge & Findlay, 2000; Rayner, 1998). Summing up, we identified our initial meta-requirement for dashboards that consider users’ limited attention and working memory when performing data exploration tasks (Toreini & Langner, 2019; Toreini & Morana, 2017): The dashboard should support users in managing their attention by providing individualized VAF while they are exploring data.

Subsequently, we developed two approaches for providing VAF that operate based on eye movement data grounded in research on attention and self-tracking feedback. We compared their effectiveness with respect to users’ information processing during data exploration tasks (Toreini et al., 2020). One of these approaches provides general VAF, including offline eye movement data from previous users who performed the same task. The other approach uses real-time eye movement data of users to provide individualized VAF. After developing both approaches, we designed and executed an eye tracking pilot study to investigate the effectiveness of each approach. The first participant group used general VAF by providing an example of proper attention allocation integrating offline records of eye movement data from other users who had performed the same task on the same dashboard. The second group also received the offline records of eye movement data from other users, but with improper attention allocation. The third group received individualized VAF that represented their actual attention allocation as individualized VAF. Later, we compared the effects of general and individualized VAF. The findings reveal that, compared to general VAF types, individualized VAF has positive effects on information processing.

In the second design cycle, on which this paper focuses, we investigated the individualized VAF’s influence in more detail. First, we refined the theoretical grounding for designing the individualized VAF and the corresponding design principles. Second, we instantiated an improved version of the attentive information dashboard including the individualized VAF as our artifact. Third, we conducted a large-scale, controlled laboratory experiment to assess the effectiveness of our design principles by providing individualized VAF on users’ information processing performance using eye tracking technology.

In the third design cycle, we investigated the consequences of providing individualized VAF in a multitasking scenario. Previous research identified the need to provide attention management systems for multitasking environments (Anderson et al., 2018). We assume that individualized VAF can support users if they frequently need to shift their attention from monitoring dashboards (primary task) to other tasks, such as answering emails (secondary task), and back to the monitoring task. Such feedback works as a memory aid for users to remember their previous attentional resource allocation and supports them in resuming the primary task properly instead of starting again from scratch. For this cycle, we evaluate different gaze visualization for individualized VAF and identify the appropriate task resumption support for dashboards (Toreini et al., 2018a, 2018b).

## 4 Conceptual and Instantiation of Individualized Visual Attention Feedback for Attentive Information Dashboards

## 4.1 Meta-Requirements and Design Principles

In the first design cycle, we identified the need to support users in managing their attention by providing feedback when they are exploring data on dashboards. Additionally, we found preliminary evidence for the effectiveness of individualized VAF based on realtime eye movement data in contrast to general VAF based on offline eye movement data. In the second design cycle, we investigated the influence of individualized VAF in more detail. Thus, we refined the theoretical grounding for designing attentive information dashboards and individualized VAF, which we describe in the following paragraphs (see Table 1 for the summary).

Based on our initial meta-requirement, we specifically demanded that the system should monitor users’ attentional resource allocation in real time (MR1). According to the eye-mind assumption (Just & Carpenter, 1980) users’ eye movement data can be used as an approximation of their overt attention (Kowler, 2011). Eye trackers are capable of collecting eye movement data in real time, and these data can be utilized to design attentive UIs (Bulling, 2016; Bulling et al., 2011; Henderson et al., 2013; Majaranta & Bulling, 2014; Roda & Thomas, 2006; Vertegaal, 2003). Tracking users’ eye movement data in real time provides the opportunity to design innovative IS applications (F. D. Davis et al., 2014; Riedl & Léger, 2016; vom Brocke et al., 2013). Thus, we articulated the second meta-requirement of estimating users’ attentional resource allocation based on their eye movement data (MR2). These two meta-requirements lay the foundation for the first design principle (DP) we propose:

DP1: Provide the system with the capability of computing users’ attentional resource allocation based on monitoring their eye movement with an eye tracking device in real time while they are performing data exploration tasks using the information dashboard.

Table 1. Meta-Requirements and Design Principles

<table><tr><td>Design cycle one</td><td colspan="2">Design cycle two</td></tr><tr><td>Initial meta requirement</td><td>Refined meta requirements</td><td>Design principles</td></tr><tr><td rowspan="4">Initial MR: The information dashboard should support users in managing their attention by providing VAF when they are exploring data.</td><td>MR1: Monitor users&#x27; attentional resource allocation in real time.</td><td rowspan="2">DP1: Provide the system with the capability of computing users&#x27; attentional resource allocation based on monitoring their eye movement with an eye tracking device in real time while they are performing data exploration tasks using the information dashboard.</td></tr><tr><td>MR2: Estimate users&#x27; attentional resource allocation based on eye movement data recorded with eye trackers.</td></tr><tr><td>MR3: Provide feedback on users&#x27; attentional resource allocation to enable self-awareness.</td><td rowspan="2">DP2: Provide the system with the capability to provide individualized visual attention feedback based on users&#x27; computed attentional resource allocation when they are performing data exploration tasks using the information dashboard.</td></tr><tr><td>MR4: Provide individualized, precise, and nonsuggestive VAF via the information dashboard.</td></tr></table>

Being able to monitor users’ eye movements when they are exploring dashboards is a prerequisite to assisting users in improving their attentional resource allocation. Providing feedback that informs users about their previous behavior is expected to increase their self-awareness and to support them in improving their information processing performance. Previous research has shown that tracking users with different devices and providing real-time feedback can influence their behavior (Hibbeln et al., 2017; Jung et al., 2010). In particular, the studies found evidence that providing feedback supports users in allocating their limited attentional resources more appropriately, and ultimately improves their task performance when working with UIs that contain massive amounts of information (D’Mello et al., 2012; Deza et al., 2017; Göbel & Kiefer, 2019; Qvarfordt et al., 2010; Sharma et al., 2016; Sridharan et al., 2012; van Gog et al., 2009). Therefore, as the third meta-requirement (MR3), we expect attentive information dashboards to provide users with VAF at the end of the task, to increase their self-awareness and thereby enable them to improve their information processing performance. VAF enables users to recognize their current attentional resource allocation and potentially adjust it. The provided VAF should enable users to improve information processing when exploring the presented information. Therefore, the VAF needs to be individualized and precise. Individualized VAF should increase users’ self-awareness about goaldirected attention by presenting their eye movement patterns to them. We presume that such feedback will support users in identifying their attentional failures, such as having missed important information on the dashboard. Therefore, as the fourth meta-requirement (MR4), we propose that individualized precise, and nonsuggestive VAF is needed. The proposed third and fourth meta-requirements inform our second design principle:

DP2: Provide the system with the capability to provide individualized visual attention feedback based on users’ computed attentional resource allocation when they are performing data exploration tasks using the information dashboard.

## 4.2 Instantiation of the Design

To map the proposed design principles to concrete design features, we propose the system architecture depicted in Figure 3. The system architecture comprises three important subsystems. First, the information dashboard subsystem connects with the BI&A system and presents information to users. Typically, the layout of dashboards comprises visual features (e.g., charts, tables, etc.) and interaction features (e.g., drill down, zoom, etc.), depending on the intended purpose of the dashboard (e.g., planning, monitoring, communication, etc.) and on the different characteristics of the dashboard users (e.g., levels of knowledge, personality, etc.) (Yigitbasioglu & Velcu, 2012).

Second, the eye tracking subsystem establishes a connection to the eye tracking device and provides the functionality to track and store the users’ eye movement data to extract the attentional states of users. Previous studies have used different procedures in extracting users’ cognitive states and their attentional status from their gaze data (Duchowski, 2017; Kowler, 2011). This subsystem provides the capability to extract users’ attentional states in real time from the collected gaze data.

![](/api/attachments/Q3MA5N8S/fulltext/images/15fdfa6fd03cfd72bfff96b336660556717c693da02bec618ed192de7b743938.jpg)  
Figure 3. System Architecture of the Proposed Attentive Information Dashboard

Third, the attention-aware subsystem focuses on matching users’ attentional states with the dashboard layout and provides individualized VAF. In this subsystem, the attention analyzer component uses information from the eye tracking subsystem (i.e., the eye movement data) in combination with information on the dashboard’s layout (e.g., the position of important elements) and users’ interaction with the dashboard to derive their attentional spotlight. Hence, the dashboard becomes sensitive to the user’s attention by tracking which information on the dashboard is processed by the user, and for how long.

The first design principle maps onto the foundational attentive information dashboard capability of computing users’ attentional resource allocation based on monitoring users’ eye movements with an eye tracking device. The second design principle specifically maps onto the individualized VAF capability building on the feedback generator component. The specific individualized VAF design can vary, based on the feedback purpose and the specific characteristics and requirements of the task users perform. We describe the actual implementation of the individualized VAF this study uses, in the experimental software and apparatus section (see Section 5.2.2).

## 5 Laboratory Experiment

To evaluate the effects of the two proposed design principles, we instantiated the design in a running software artifact and conducted a controlled laboratory experiment. In the following sections, we outline the underlying hypotheses investigated in the experiment and describe the experiment’s methodology.

## 5.1 Hypotheses Derivation for Laboratory Experiment

To assess the proposed design, we outline hypotheses on the proposed effects that existing research justifies. Before deriving the hypotheses, we need to consider the interdependencies of both design principles. The second design principle (provision of individualized VAF) builds on the first design principle (monitoring users’ eye movement data), thus a distinct evaluation of each design principle is technically not possible. We therefore decided to assess our design by instantiating both design principles (referred to as the individualized VAF group) and then compare it to a baseline system that instantiates no design principle but provides general feedback (referred to as the general VAF group).

Our study is undertaken in the context of supporting users in data exploration tasks on dashboards, done in three phases: (1) first visit phase, (2) revisit phase, and (3) end of the task. The differentiation in these phases is important because individualized VAF requires eye movement data, thus users need first to interact with the dashboard (i.e., in the first visit phase) before the actual feedback can be provided. The provided feedback will then affect users’ attentional resource allocation in the revisit phase. We argue that users need to remember their attentional resource allocation during the first visit on the dashboard in order to be able to allocate an appropriate level of attentional resources in the revisit phase. Previous research has shown that users find it difficult to remember their previous attentional resource allocation and typically repeat their visual behavior in the revisit phases (Cane et al., 2012; Monk et al., 2008; Singh, 1998). Therefore, we argue that users with general VAF (i.e., without the support our design provides) will be challenged in finding an appropriate revisit strategy in comparison to users who receive individualized VAF (i.e., with the support our design provides). Previous research has shown that providing individualized VAF guides users toward recognizing high and low-visited parts of the UI (Göbel & Kiefer, 2019; Qvarfordt et al., 2010) and enables them subsequently to optimize their behavior. Summing up, we propose our first hypothesis as follows:

## H1: Providing individualized VAF results in better attentional resource allocation performance in the revisit phase compared to providing generic VAF.

Further, receiving individualized VAF will enable users to derive a proper strategy for the revisit phase. Accordingly, users can purposefully turn their attention to specific elements on the dashboard (i.e., elements previously less attended to), rather than randomly switching between different dashboard elements (again) because they lack a proper strategy for the revisit phase. Researchers have demonstrated that providing VAF increases the user’s focus while they are conducting tasks (D’Mello et al., 2012). Consequently, users who received individualized VAF require less attention shifts in the revisit phase compared to users who did not receive it. Summing up, we propose our second hypothesis as follows:

H2: Providing individualized VAF results in a lower attention shift rate in the revisit phase compared to providing generic VAF.

Previous research has found that the position of the stimulus in the UI affects how users allocate their attention to the stimulus (Lorigo et al., 2008; Nielsen, 2006; Soegaard, 2020). Previous studies have shown that users process information similar to the F pattern.

In fact, users start from the left side of the UI and then, reading from left to right, allocate less attention to the information given on the right. An eye tracking study on dashboards by Tableau (Alberts, 2017) has shown that users typically focus their attention on specific areas and thereby potentially miss other parts of the dashboard. Also, the results from the first design cycle in this DSR project revealed that users typically analyze the charts on the left side of the dashboard more intensively than the other parts of the dashboard (Toreini & Langner, 2019). Therefore, we argue that providing individualized VAF can prevent users from focusing only on specific areas of a dashboard while neglecting others and can support them in better managing the distribution of their limited attentional resources. Summing up, we propose our third hypothesis:

H3: Providing individualized VAF results in better attentional resource management at the end of the task compared to providing generic VAF.

Figure 4 depicts the research model that we investigated in the laboratory experiment.

## 5.2 Laboratory Experiment Methodology

We assess our proposed design’s effect in a mixed model design with two groups (both design principles instantiated, providing individualized VAF x both design principles not instantiated, providing general VAF) as the between-subject manipulation, as well as the time of providing the feedback (before and after receiving VAF) as the within-subject manipulation.

## 5.2.1 Participants

In all, 92 university students (35 female, 57 male) with an average age of 23.45 (SD=3.39) participated in this experiment. We used student participants for the laboratory experiment, as doing so provides two key advantages. First, in contrast to employees in organizations, students are not specifically trained to work with dashboards and are not biased by contextual information. Therefore, like novice users, they likely have little or no prior knowledge of the underlying experiment’s process (i.e., the information processing task). Second, it is relatively easy to reach a large enough sample size of student participants to achieve adequate statistical power without unreasonable effort. Consequently, students are an adequate and representative sample for the experimental setup (Burton-Jones & Meso, 2008).

Each student received 10 euros as a financial incentive to participate in and complete the experiment. We recruited a total of 107 participants from an experiment pool and randomly assigned them to the two experimental groups. Eventually, we removed 15 participants from the sample because of the following three reasons.

![](/api/attachments/Q3MA5N8S/fulltext/images/e7f5bf176f7de48f18f8fbb9787014f970ea07a2f611155c8163a8c107584660.jpg)  
Figure 4. Research Model to Investigate the Effect of Design Principles 1 and 2

First, we removed 12 participants because their recorded eye movement data covered less than 75% of the overall experimental time (basically less than 90 seconds in the first visit or less than 45 seconds in the revisit phase). We assumed that these participants did not engage in the data exploration task seriously or that the eye tracker had technical problems recording their eye movement data. Two participants were excluded from the sample because they did not answer the control question in the post-experimental survey correctly. Finally, we excluded one more participant because of self-reported health problems affecting the eyes. In summary, our sample assigned 48 participants to the control group (general VAF) and 44 participants to the treatment group (individualized VAF).

## 5.2.2 Experimental Software and Apparatus

The experiment was conducted with self-developed software that incorporates the capability to track users’ eye movement data in real time. Further, the application collected the data required for further analysis in the evaluation section. We used the Tobii Eye Tracker 4C, which enables tracking users’ eye movement data in real time and records relevant eye movement data. The corresponding Tobii license was included to store and process the collected data. This eye tracker is a desktop-mounted device measuring 17 x 15 x 335 mm (0.66 x 0.6 x 13.1 in) in size; it has a sampling rate of 90 Hz, and is considered one of the low-cost eye trackers in the market (Farnsworth, 2019). We selected this particular eye tracker because we determined that the use of such devices for designing attentive UI is applicable for daily working tasks on a large scale. We connected the eye tracker to a computer that displays the dashboard on a 21-inch screen with a resolution of 1920x1080 for all participants. We developed the experimental software in the .NET framework by using C# programming language because Tobii provides the relevant SDKs for developing gaze-aware UI (Core SDK) and collecting data for research purposes (Pro SDK) in this framework. We included gaze-aware UI elements (i.e., graphs, as in Figure 5) as areas of interest (AOIs) on our dashboard to collect users’ gaze duration while they explored the provided information in these AOIs in real time. The collected gaze duration was transferred to the feedback generator component. With this approach, we were able to present the individualized VAF in the form of gaze duration on each AOI subsequent to the task. In addition to our experimental software, we used the software Tobii Pro EyeTracker Manager to calibrate the eye tracker device at the beginning of each experimental session.

The quality of our research design and results depended on factors that affect users’ attentional resource allocation. Therefore, we maintained the internal validity of our experiment as follows: First, we evaluated the artifact instantiating our design in a laboratory experiment that ensured high internal validity by minimizing the influence of external factors that can affect users’ performance. Second, we minimized the influence of external factors that could affect the quality of the collected eye movement data, such as movements and light conditions. To do this, we controlled the calibration’s quality several times during the experiment with our developed experimental software using Tobii’s SDKs. Third, we used the collected eye movement data to verify that users conducted the experimental task according to our instructions and removed users that did not follow the instructions. Fourth, we controlled the elements of the dashboard that affect users’ stimulidriven attention while they are exploring. Figure 5 displays the dashboard layout that we designed and used for this experiment.

![](/api/attachments/Q3MA5N8S/fulltext/images/077bcf094b7e94c10b49f2a98dc0cdbd60f65c463153102b0b9855bd6f2c1c0e.jpg)  
Figure 5. The Information Dashboard Designed to Control for Stimulus-Driven Attention

This dashboard includes six charts, which we designed in such a way that they have almost similar complexity. All six charts are of the same type (bar chart) to minimize potential distraction due to different visual formats (Kelton et al., 2010), and all charts, words, and numbers are equal in size (Alberts, 2017). We chose six chunks of information for our experiment because seven (plus or minus two) chunks of information represent the maximum capacity for individuals’ working memory capacity (Miller, 1956). To control the influences of interactive features on users’ attention (Liu and Stasko, 2010) the dashboard includes only static charts. The dashboard uses gray colors with similar variations to control for a potential color impact on users’ attention (Bera, 2016). To summarize, the same visualization format, size, number of information chunks, lacking interactive features, and gray color, we argue that from an information representation perspective, the six charts have similar complexity.

We acknowledge that in having a similar complexity across all charts, our dashboard does not represent a real-world scenario. Using elements that influence users’ stimulus-driven attention is common in realworld dashboards, and highly impacts users’ attentional resource allocation (Alberts, 2017; Pauwels et al., 2009; Yigitbasioglu & Velcu, 2012). However, our controlled dashboard design enables us to track the users’ goal-directed attention during the experiment. We followed this approach to maintain a high level of internal validity regarding users’ attentional resource allocation, attention shift rate, and attentional resource management. We were thereby able to prevent potential biases from stimulus-based attention and focus on goal-directed attention in our study.

## 5.2.3 Experimental Procedure

We started the experiment by calibrating the eye trackers using Tobii Pro Eye Tracker Manager before we started our self-developed experimental software. The software first displayed instructions to the participants and required them to start the experimental task manually. In the instructions, we outlined the scenario of the experiment and the experimental task’s steps. We told participants to imagine being a sales manager of a company. They had recently joined the sales organization and were about to meet with their supervisor. A few minutes before the meeting, they received the sales report from the last six months in a dashboard format. We asked participants to prepare for this meeting by exploring and memorizing the company’s status regarding the provided sales data. Further, we informed them of the time available for this task (120 seconds) and mentioned that the experimental software included a timer for tracking the remaining time for each step of the experimental task. Moreover, we told the participants that they would receive additional information after exploring the dashboard (i.e., in the VAF phase) and would subsequently be given a second chance to explore the dashboard (i.e., in the revisit phase). The instruction ended with control questions to ensure that participants properly understood the experimental steps and the information we had provided on the dashboard.

After completing the instruction step, we showed the participants a simplified version of the experiment’s dashboard (providing no VAF) to enable them to familiarize themselves with the software and experimental task. After completing this step, we asked them to rest for two minutes before starting the main part of the experiment. We added this break to control for carry-over effects between the trial and the main part of the experiment.

Figure 6 depicts the steps for the main part of the experiment. In the first phase of data exploration, participants received the dashboard and scrutinized it for 120 seconds. After that, they were interrupted for 30 seconds. In this step, participants received one of the two VAF treatments (individualized VAF or general VAF) based on their group assignment. Subsequently, in the revisit phase, we asked participants to revisit the same dashboard for an additional 60 seconds. In the last step of the experimental task, participants provided their demographics. Finally, we asked them to rest for a few minutes and get ready for the working memory capacity tests that we performed using the visuospatial working memory capacity test (Kessels et al. 2000) and digit working memory capacity test (Conway et al., 2005) from the PEBL test battery (Mueller & Piper, 2014).

## 5.2.4 Treatment Design: Visual Attention Feedback

Based on our proposed design, the individualized VAF should present the summary of users’ previous attentional resource allocations to increase their selfawareness. Therefore, we instantiated the second design principle in such a way as to present the actual gaze duration on each visual feature (e.g., charts, tables, etc.) on the dashboard in a time format. We assumed that providing such information would enable users to properly assess their previous attentional resource allocation, and subsequently, when required, to improve their attention allocation. Figure 7 visualizes an instantiation of the individualized VAF that exhibits the user’s gaze duration on a dashboard with six visual features (see Part 2), similar to the experiment’s dashboard. In addition to the individualized VAF, we provided the following general text-based explanation (see Part 1):

Many users have a problem allocate[ing] their attention properly while using information dashboards. In the following, you can see your attention allocation so far based on the time that you looked at each chart. Please think about your attention allocation performance in the previous step and then you will have one more minute to continue exploring the dashboard.

This individualized VAF was provided to the treatment group in our experiment. The control group did not receive additional information on their individualized gaze duration values in the form of graphical or textbased information; they only received general VAF in the form of the following text:

Many users have a problem allocate[ing] their attention properly while using information dashboards. Please think about your attention allocation performance in the previous step and then you will have one more minute to continue exploring the dashboard.

## 5.2.5 Measurements

In this study, we collected and analyzed the users’ eye movement based on predefined areas of interest (AOIs) on the dashboard. The dashboard included six charts, each of which we considered to be one AOI. As Figure 8 shows, we named six AOIs based on their position on the dashboard layout. We use the AOIs’ names to discuss the results in the following sections. Additionally, we measured several dependent and participant-specific control variables during different steps of the experiment. Table 2 displays a summary of all measurements.

Our dependent variables focus on different facts of users’ information processing regarding their attentional resource allocation and management, as well as attention shift rates. First, we measured users’ attentional resource allocation, following Cheung et al.’s (2017) suggestions. Based on this study, users fixation duration and the number of fixations on each predefined AOI are treated as each user’s attentional resource allocation on that AOI.

![](/api/attachments/Q3MA5N8S/fulltext/images/575a166fa8aabdc4326513e917b2ccf0f353ac478831734c1cb7ca9f559cf23a.jpg)  
Figure 6. The Experiment’s Procedure Used to Evaluate Proposed Design Principles

![](/api/attachments/Q3MA5N8S/fulltext/images/239a74ffbc3e8e8160f68eafdbd91e2593b5a4ec7a7fbaf26aa154861c0f124d.jpg)  
Figure 7. Instantiation of Design Principle 2: Individualized Visual Attention Feedback

![](/api/attachments/Q3MA5N8S/fulltext/images/2aa3c1c68e83bddebcd15eb2bf4df083e224884bd584c5b36f66a329d1e69b34.jpg)  
Figure 8. Names Assigned to the Six AOIs on the Dashboard Based on Their Position

Table 2. The Dependent Variables and Controls Used in this Study

<table><tr><td></td><td>Construct</td><td>Definition</td><td>Measurement</td><td>References</td></tr><tr><td rowspan="2">Information processing (revisit phase)</td><td>Attentional resource allocation</td><td>Users&#x27; performance in allocating attention to previously low-attended AOIs and ignoring previously high-attended AOIs.</td><td>Eye tracking (fixation duration, number of fixations)</td><td>(Cheung et al., 2017; Just &amp; Carpenter, 1980; Qvarfordt et al., 2010)</td></tr><tr><td>Attention shift rate</td><td>The number of instances directing attention toward another AOI.</td><td>Eye tracking (total number of transitions pairs)</td><td>(Blascheck et al., 2014; Hong et al., 2004)</td></tr><tr><td>Information processing (end of the task)</td><td>Attentional resource management</td><td>The ability to distribute the attention properly across all stimuli on the screen.</td><td>Eye tracking (variance of fixation duration on six AOIs)</td><td>Self-defined</td></tr><tr><td rowspan="2">Controls</td><td>Visuospatial working memory capacity</td><td>The capacity of users&#x27; visuo-spatial memory.</td><td>Corsi span</td><td>(Kessels et al., 2000)</td></tr><tr><td>Digit working memory capacity</td><td>The capacity of users&#x27; ability to memorize digit numbers.</td><td>Digit span</td><td>(Conway et al., 2005)</td></tr></table>

To assess users’ attentional resource allocation, we compared the fixation duration and number of fixations of the first visit to the dashboard with the revisit phases, based on six AOIs. According to chance, each AOI (i.e., each chart) should receive (100/6 = 16.67%) of the attentional resource allocation. This was subtracted from the actual attentional resource allocation percentage, which yielded a score reflecting whether a given AOI was attended to more (or less) than the theoretical average. We treated the revisit phase as an opportunity to enhance information processing performance by using a higher attentional resource allocation on the previously low attended charts in the revisit phase.

Second, we measured users’ attentional shift rate in the revisit phase. This measure shows how the user centers attention on a single stimulus, or a limited set of stimuli, rather than how the user shifts attention between all the elements. In eye tracking research users’ attentional shift rate between AOIs is used to explain how focused the users’ attention is (Bednarik & Tukiainen, 2006, 2008). The attention shift rate between AOIs is measured by the number of transitions, indicated by the movement of the eyes from one AOI to another (we ignored transitions within the same AOI). Consequently, the transition matrix represents the attention shift rate between all possible combinations of AOIs (Ponsoda et al., 1995). The transition matrix is a descriptive summary representation of the collected eye movement data that provides support for the analysis of users’ data exploration behavior (Blascheck et al., 2014; Burch et al., 2011; Kurzhals et al., 2016).

Third, we measured users’ attentional resource management at the end of the data exploration task. As explained in Section 5.2.2, all six AOIs on the dashboard have the same complexity and level of importance. Therefore, a more even distribution of attention between all six AOIs would indicate a high attentional resource management performance. We calculated the standard deviation (SD) of fixation durations and number of fixations of all six AOIs at the end of the data exploration task. Lower SD values indicated that these six variables are closer to each other and that users properly distributed their attention. In contrast, a higher SD value indicates a lower attentional resource allocation management performance.

We measured several participant-specific control variables (demographics as well as two different working memory capacity types) in addition to our three main variables. Regarding demographics, we captured gender, age, and the participant’s experience of working with dashboards through survey questions. We also measured the users’ working memory capacity from two perspectives. We chose users’ working memory capacity as a control variable because of its importance in processing information, as described in Section 2.1.2. Users’ working memory capacity predicts their attention control (Kane & Engle, 2003) and has been defined as one important individual characteristic of users interacting with visualized information (Borkin et al., 2016; Haroz & Whitney, 2012; Healey & Enns, 2012; Toker et al., 2013). Researchers have defined working memory span tasks as the most adequate instrument for comparing various individuals’ working memory capacity with one another (Conway et al., 2005). Also, individuals have different capabilities in remembering different types of information. Consequently, there are different working memory spans that can be measured. In this study, we measured two types of working memory span that users have, namely their digit and visuospatial working memory capacities. This choice was motivated by the fact that dashboard users mostly deal with digits and visualized information on the dashboard. We collected the users’ visual working memory capacity by running a visuospatial Corsi block-tapping test (Kessels et al., 2000). To measure the number of digits that an individual user can memorize, we used the digit span test (Conway et al., 2005). Both tests report the working memory span value, defined as the longest sequence a user can correctly repeat in each test. The higher the working memory span value, the higher the working memory capacity.

## 6 Results

## 6.1 Manipulation and Control Checks

Before testing the hypotheses, we checked whether the random-assignment between-participant conditions was successful or not by testing whether the two groups differed in their working memory capacity and the three demographic variables.

The chi-squared test for comparing participants’ gender per condition (individual VAF and general VAF) was not significant (chi-square = 0.558, p = 0.45). Moreover, as Table 3 shows, the Wilcoxon signed-rank test results for all the other control variables (age, experience level, Corsi span, and digit span) did not show any difference between the two groups. Thus, we assume that our random assignment was successful. In addition, to confirm that all users had the same visual behavior in the first visit phase on the dashboard, we analyzed the users’ eye movement data and compared their attentional resource allocation and management, as well as the attention shift rate between the two groups. The results indicate that users in the two groups had similar visual behavior before receiving different VAF types. We present the details of this analysis separately in the following sections.

## 6.2 Attentional Resource Allocation

Figure 9 shows the heatmaps based on the users’ attentional resource allocation in both groups. The left column displays the attentional resource allocation of the first visit phase and the right column shows the revisit phase. In the first visit phase, visual behavior did not differ between the groups, while the attentional resource allocation was primarily influenced by the position of the AOIs. In both groups, the left-sided charts (AOI1, AOI4) received the most attention, followed by the charts in the middle (AOI2, AOI5), with the charts on the right side (AOI3, AOI6) receiving the least attention. Similarly, a column-based observation reveals that charts in the first row (AOI1, AOI2, AOI3) have a higher attentional resource allocation compared to the corresponding charts in the second row (AO4, AOI5, AOI6). These results confirm that users are biased toward allocating their attention to the left and top of the dashboards, similar to other UI types (Lorigo et al., 2008; Nielsen, 2006).

During the revisit phase, the general VAF group’s results show that users repeated their visual behavior, while users in the individualized VAF changed it. Investigating both rows in more detail shows that for the general VAF group, the left-sided AOIs have higher values than the right-sided AOIs. Similarly, the column-based investigation indicates that the general VAF group had higher values for the AOIs in the upper position compared to the AOIs in the lower position. However, users in the individualized VAF group had more attentional resource allocation on the right-sided AOIs and higher attentional resource allocation on AOIs positioned in the lower row. Overall, by qualitatively analyzing the visual behavior of both groups via heatmaps, we found that users who received individualized VAF improved their attentional resource allocation in the revisit phase, while users with the general VAF tended to repeat their visual behavior in the revisit phase.

For testing the attentional resource allocation performance hypothesis in the revisit phase (H1), we carried out repeated-measures regression analyses based on the percentage fixation duration and number of fixations. In addition, prior to the analysis, we centered the attentional resource allocation scores around the mean average percentage (100/6). Accordingly, zero reflects the average percentage of attentional resource allocation spent on an AOI at a given point in time.

Table 3. Comparing the Control Variables

<table><tr><td>Control variable</td><td>Conditions</td><td>Median</td><td>Mean</td><td>SD</td><td>W</td><td>P-value</td><td>R</td></tr><tr><td rowspan="2">Age</td><td>Individualized VAF</td><td>22.50</td><td>22.77</td><td>2.75</td><td rowspan="2">851.5</td><td rowspan="2">0.108</td><td rowspan="2">-0.167</td></tr><tr><td>General VAF</td><td>24.00</td><td>24.06</td><td>3.8</td></tr><tr><td rowspan="2">Experience level</td><td>Individualized VAF</td><td>5.00</td><td>5.00</td><td>1.38</td><td rowspan="2">856.5</td><td rowspan="2">0.117</td><td rowspan="2">-0.163</td></tr><tr><td>General VAF</td><td>5.67</td><td>5.42</td><td>1.43</td></tr><tr><td rowspan="2">WMC: Corsi span</td><td>Individualized VAF</td><td>6.00</td><td>6.01</td><td>0.84</td><td rowspan="2">1139.5</td><td rowspan="2">0.509</td><td rowspan="2">-0.068</td></tr><tr><td>General VAF</td><td>5.50</td><td>5.94</td><td>1.09</td></tr><tr><td rowspan="2">WMC: digit span</td><td>Individualized VAF</td><td>7.00</td><td>7.32</td><td>1.27</td><td rowspan="2">1074.5</td><td rowspan="2">0.880</td><td rowspan="2">-0.015</td></tr><tr><td>General VAF</td><td>7.00</td><td>7.25</td><td>1.33</td></tr><tr><td colspan="8">Note: *p&lt;0.05, **p&lt;0.01</td></tr></table>

![](/api/attachments/Q3MA5N8S/fulltext/images/be9c192c0e163e1a6e26afe9e7a5c2ba0e70825f31415f01c9691198825cd5d6.jpg)  
Figure 9. Heatmaps of Both Groups in the First and Revisited Phases

In the first model, we predicted the fixation duration per AOI in the revisit phase from the fixation duration of that AOI in the first visit, the experimental condition (0 = general VAF group; 1 = individualized VAF group), and their interaction. First, the effect of the fixation duration percentage in the first visit was significant; b = 1.145 percentage, SE = 0.223 percentage, t(548) = 5.129, p < 0.001. This indicated that in the general VAF group, the fixation duration of an AOI was a strong predictor of the same AOI’s fixation duration in the revisit phase. In other words, participants showed consistency in their behavior as expected regarding the fixation duration. Figure 10, on the left, shows the positive slope in the general VAF group. An AOI that received a higher percentage of attentional resource allocation (in terms of fixation duration and number of fixations) in the first visit, also received more attentional resource allocation in the revisit phase. Second, there was a significant interaction of fixation duration percentage in the first visit and the individualized VAF group; b = -0.75 percentage, SE = 0.138 percentage, t(548) = -5.468, p < 0.001. This shows that the individualized VAF compensated for the fixation duration effect of the first visit on the fixation duration of the revisit phase (Figure 10, left side). Thus, compared to the general VAF group, an AOI that had high fixation duration in the first visit, had relatively less fixation duration in the second phase for the individualized VAF group. Vice versa, an AOI with a previously low fixation duration had a high fixation duration in the second phase.

Similar to fixation duration, an analogous analysis for the number of fixations also yielded two significant effects: First, the effect of the number of fixations in the first visit was significant; b = 1.211 percentage, SE = 0.221 percentage, t(548) = 5.467, p < 0.001. This indicates that in the general VAF group, the number of fixations on an AOI strongly predicted the number of fixations on the same AOI in the revisit phase, and participants showed consistency in their behavior regarding the number of fixations. Second, the effect of the number of fixations in the first visit on the number of fixations in the revisit phase was compensated for by the individualized VAF (Figure 10, right side). Crucially, the results show that the number of fixations in the first visit significantly interacted with the individualized VAF group, b = -0.812 percentage, SE = 0.133 percentage, t(548) =-6.067, p < 0.001.

To summarize, the qualitative analysis results of the heatmap, as well as quantitative analyses for fixation duration and number of fixations, show that the attentional resource allocation performance of users with the individualized VAF improved in comparison to the users with general VAF. Participants with the general VAF were consistent, and AOIs that were highly attended to in the first phase also received more attention in the revisit phase. However, for the users with individualized VAF, an AOI that received more attentional resource allocation (in terms of fixation duration and number of fixations) in the first visit, received less attentional resource allocation in the revisit phase, and vice versa. Therefore, H1 is supported.

![](/api/attachments/Q3MA5N8S/fulltext/images/b1cfacbd9238685eec7c461b8a5d4ca29187931d72b612c409eea05c2ea02b23.jpg)

![](/api/attachments/Q3MA5N8S/fulltext/images/8d6244fd092f7f26c415439aa03efe3fc4d7ce7face4343e78a597705420d4d2.jpg)  
Figure 10. The Interaction Between and After Feedback for Both Groups

## 6.3 Attention Shift Rate

Figure 11 displays the transition proportions between the six AOIs in the first phase and the revisit phase for both groups. In these matrixes, the number in the cell represents the attention shift rate in percentage between each possible pair of AOIs. The reason for showing the proportions rather than the actual number of transitions for each pair lies in the difference between the data exploration time in the first visit (120 seconds), and the revisit phase (60 seconds). In addition, the color scaling shows the differences between values on these matrixes to facilitate the qualitative analysis.

Figure 11 shows that in the first visit, both groups had similar visual behavior, focusing mostly on transitions between AOI1 and AOI2. However, comparing the transition matrix of the first to revisit phase shows that the users with individualized VAF changed their strategy and investigated the relationship between AOIs on the right side of the dashboard. For this group, the transitions between AOI5 and AOI6 have the highest value while for the general VAF group the transitions between AOI1 and AOI2 remained as the highest value. A comparison of the heatmaps to the transition matrixes indicates that the users with individualized VAF not only had higher attentional resource allocation on previously low attended AOIs but they also investigated the relationships between them more specifically. Also, users in the general VAF group repeated their attentional resource allocation and investigated the relationship between them rather than focusing on others.

As discussed in Section 5.2.5, the total number of transitions in each phase represents the user’s attention shift rate in that phase. To compare the attention shift rate in the first visit phase, we conducted an independent t-test between individualized VAF (M = 77.66, SD = 24.21) and general VAF (M = 83.56, SD = 21.66) groups, and found no significant difference t(86.59) = -1.22, p = 0.22. Therefore, we argue that the two groups had the same attention shift rate in the first visit phase. However, in the revisit phase, the results of the Wilcoxon rank-sum test indicate that users with individualized VAF (Mdn = 35) had significantly lower attention shift rates than the users with general VAF (Mdn = 45), W= 661.5, p = 0.002, r = -0.321. Thus, based on the analysis of the eye movement data, H2 is supported.

## 6.4 Attentional Resource Management

Figure 12 shows the interaction plot for fixation duration and number of fixations that shows how users’ attentional resource management changed during the experiment. The attentional resource management of users with individualized VAF improved massively, while this is not the case for users with general VAF (the lower SD values among six AOIs represent better attentional resource management).

<table><tr><td></td><td colspan="7">First Phase</td><td colspan="7">Revisit Phase</td></tr><tr><td rowspan="8">General VAF</td><td colspan="7">total number of transitions(Mean=83.56, SD=21.66)</td><td colspan="7">total number of transitions(Mean=45.52, SD=13.67)</td></tr><tr><td>AOI1</td><td>AOI2</td><td>AOI3</td><td>AOI4</td><td>AOI5</td><td>AOI6</td><td></td><td>AOI1</td><td>AOI2</td><td>AOI3</td><td>AOI4</td><td>AOI5</td><td>AOI6</td><td></td></tr><tr><td>AOI1</td><td>-</td><td>9.82%</td><td>1.37%</td><td>5.53%</td><td>2.24%</td><td>0.30%</td><td>AOI1</td><td>-</td><td>10.25%</td><td>1.24%</td><td>5.13%</td><td>2.61%</td><td>0.37%</td></tr><tr><td>AOI2</td><td>10.07%</td><td>-</td><td>6.51%</td><td>1.15%</td><td>3.47%</td><td>0.55%</td><td>AOI2</td><td>10.89%</td><td>-</td><td>6.73%</td><td>1.05%</td><td>3.52%</td><td>0.73%</td></tr><tr><td>AOI3</td><td>0.97%</td><td>4.99%</td><td>-</td><td>0.70%</td><td>1.05%</td><td>6.66%</td><td>AOI3</td><td>0.87%</td><td>5.72%</td><td>-</td><td>2.29%</td><td>0.82%</td><td>6.45%</td></tr><tr><td>AOI4</td><td>5.46%</td><td>1.47%</td><td>0.27%</td><td>-</td><td>5.06%</td><td>0.72%</td><td>AOI4</td><td>4.53%</td><td>1.28%</td><td>0.14%</td><td>-</td><td>5.31%</td><td>0.82%</td></tr><tr><td>AOI5</td><td>2.69%</td><td>4.94%</td><td>0.60%</td><td>4.69%</td><td>-</td><td>5.41%</td><td>AOI5</td><td>2.75%</td><td>3.84%</td><td>0.78%</td><td>5.17%</td><td>-</td><td>5.35%</td></tr><tr><td>AOI6</td><td>0.32%</td><td>0.62%</td><td>5.81%</td><td>1.07%</td><td>5.48%</td><td>-</td><td>AOI6</td><td>0.46%</td><td>1.01%</td><td>5.49%</td><td>0.87%</td><td>5.58%</td><td>-</td></tr><tr><td rowspan="8">Individualized VAF</td><td colspan="7">total number of transitions(Mean=77.66, SD=24.21)</td><td colspan="7">total number of transitions(Mean=37.52, SD=15.38)</td></tr><tr><td>AOI1</td><td>AOI2</td><td>AOI3</td><td>AOI4</td><td>AOI5</td><td>AOI6</td><td></td><td>AOI1</td><td>AOI2</td><td>AOI3</td><td>AOI4</td><td>AOI5</td><td>AOI6</td><td></td></tr><tr><td>AOI1</td><td>-</td><td>10.77%</td><td>1.55%</td><td>5.50%</td><td>2.17%</td><td>0.38%</td><td>AOI1</td><td>-</td><td>8.12%</td><td>1.45%</td><td>3.39%</td><td>1.33%</td><td>0.48%</td></tr><tr><td>AOI2</td><td>10.01%</td><td>-</td><td>7.37%</td><td>0.91%</td><td>3.86%</td><td>0.70%</td><td>AOI2</td><td>7.45%</td><td>-</td><td>6.84%</td><td>0.73%</td><td>4.18%</td><td>1.27%</td></tr><tr><td>AOI3</td><td>1.26%</td><td>6.00%</td><td>-</td><td>0.79%</td><td>0.88%</td><td>5.59%</td><td>AOI3</td><td>1.21%</td><td>5.88%</td><td>-</td><td>0.79%</td><td>1.03%</td><td>7.75%</td></tr><tr><td>AOI4</td><td>5.74%</td><td>0.88%</td><td>0.26%</td><td>-</td><td>5.03%</td><td>0.64%</td><td>AOI4</td><td>3.94%</td><td>0.67%</td><td>0.36%</td><td>-</td><td>4.85%</td><td>0.85%</td></tr><tr><td>AOI5</td><td>2.93%</td><td>4.77%</td><td>0.70%</td><td>4.65%</td><td>-</td><td>4.77%</td><td>AOI5</td><td>1.70%</td><td>4.24%</td><td>0.67%</td><td>4.97%</td><td>-</td><td>7.69%</td></tr><tr><td>AOI6</td><td>0.59%</td><td>0.67%</td><td>4.77%</td><td>0.97%</td><td>4.86%</td><td>-</td><td>AOI6</td><td>0.73%</td><td>1.33%</td><td>7.15%</td><td>0.97%</td><td>8.00%</td><td>-</td></tr></table>

Figure 11. Transition Matrix of the Users in Both Groups

![](/api/attachments/Q3MA5N8S/fulltext/images/02dc21eef891c436a785d936581e9d6546b41b7ffc36bf0a7956184ab3adf7de.jpg)  
Figure 12. Interaction Effect of VAF in Groups and Phases on Attentional Resource Management Performance

Table 4. Comparing Users’ Attentional Resource Management Performance in Both Groups

<table><tr><td colspan="7">Between subject analyses</td></tr><tr><td>Dependent variable</td><td>Exp. Phase</td><td>Condition</td><td>Median</td><td>W</td><td>P-value</td><td>R</td></tr><tr><td rowspan="4">Attentional resource management performance (based on fixation durations)</td><td rowspan="2">End of the first phase</td><td>General VAF</td><td>5.40</td><td rowspan="2">1019</td><td rowspan="2">0.770</td><td rowspan="2">-0.029</td></tr><tr><td>Individualized VAF</td><td>5.37</td></tr><tr><td rowspan="2">End of the task</td><td>General VAF</td><td>5.33</td><td rowspan="2">1364</td><td rowspan="2">0.015*</td><td rowspan="2">-0.251</td></tr><tr><td>Individualized VAF</td><td>4.14</td></tr><tr><td rowspan="4">Attentional resource management performance (based on number of fixations)</td><td rowspan="2">End of the first phase</td><td>General VAF</td><td>4.77</td><td rowspan="2">868</td><td rowspan="2">0.143</td><td rowspan="2">-0.150</td></tr><tr><td>Individualized VAF</td><td>5.23</td></tr><tr><td rowspan="2">End of the task</td><td>General VAF</td><td>4.30</td><td rowspan="2">1322</td><td rowspan="2">0.037*</td><td rowspan="2">-0.216</td></tr><tr><td>Individualized VAF</td><td>3.56</td></tr><tr><td colspan="7">Within subject analyses</td></tr><tr><td>Dependent variable</td><td>Conditions</td><td>Exp. Phase</td><td>Median</td><td>V</td><td>P-value</td><td>R</td></tr><tr><td rowspan="4">Attentional resource management performance (based on fixation durations)</td><td rowspan="2">General VAF</td><td>End of the first phase</td><td>5.40</td><td rowspan="2">754</td><td rowspan="2">0.089</td><td rowspan="2">-0.173</td></tr><tr><td>End of the task</td><td>5.33</td></tr><tr><td rowspan="2">Individualized VAF</td><td>End of the first phase</td><td>5.37</td><td rowspan="2">807</td><td rowspan="2">&lt;0.001***</td><td rowspan="2">-0.403</td></tr><tr><td>End of the task</td><td>4.14</td></tr><tr><td rowspan="4">Attentional resource management performance (based on number of fixations)</td><td rowspan="2">General VAF</td><td>End of the first phase</td><td>4.77</td><td rowspan="2">767</td><td rowspan="2">0.066</td><td rowspan="2">-0.187</td></tr><tr><td>End of the task</td><td>4.33</td></tr><tr><td rowspan="2">Individualized VAF</td><td>End of the first phase</td><td>5.23</td><td rowspan="2">869</td><td rowspan="2">&lt;0.001***</td><td rowspan="2">-0.498</td></tr><tr><td>End of the task</td><td>3.56</td></tr></table>

Note: \*p < 0.05, \*\*p < 0.01, \*\*\*p < 0.001

First, we conducted a Wilcoxon’s rank-sum test to investigate differences between the two conditions at the end of the first visit (between-subject analysis). There was no difference between the two groups in users’ attentional resource management at the end of the first visit phase for both fixation durations $( p =$ 0.77) and number of fixations $( p = 0 . 1 4 )$ (see Table 4). This is aligned with our previous findings that users of the two groups had the same visual behavior in the first visit. However, the results show significant differences for both fixation duration $( p = 0 . 0 1 )$ and number of fixations $( p = 0 . 0 3 )$ at the end of the task. Second, we investigated users’ attentional resource management by comparing each group in the two phases (withinsubject analysis). The results of the Wilcoxon signedrank test show that, comparing the two phases, the attentional resource management of users with individualized VAF for both fixation duration $( p <$ 0.001) and number of fixations $( p \textless 0 . 0 0 1 )$ differ significantly. However, the general VAF did not support users to improve their attentional resource management significantly.

The findings of the within-subject and between-subject analyses of the attentional resource management show that at the end of the data exploration task, users with individualized VAF had better attentional resource management than the users with general VAF. Thus, H3 is supported.

## 7 Discussion

The laboratory experiment’s results demonstrate that the proposed design principles and their instantiation in a software artifact increase users’ attentional resource allocation and attention shift rate performance in the revisit phase (confirming H1 and H2) and improve attentional resource management performance at the end of the task (confirming H3). The findings confirm our assumption that a dashboard providing individualized VAF supports users in processing information in a comparatively better way than dashboards without such individualized feedback. In the following sections, we discuss this study’s findings from a theoretical and practical point of view. Subsequently, we present the study’s limitations and delineate opportunities for future research.

## 7.1 Theoretical Implications

Vom Brocke et al. (2013) have emphasized that only a limited number of contributions in the DSR community make actual use of the potential of neuroscience tools (e.g., eye trackers) to design advanced built-in capability for IT artifacts. To the best of our knowledge, our DSR project is the first that investigates the integration of real-time eye movement data as a built-in capability for dashboards. Our study provides prescriptive knowledge on integrating real-time eye movement data for supporting users in managing their limited attention capacity by providing individualized VAF. We present a system architecture for attentive information dashboards that supports data exploration through three components (i.e., a dashboard subsystem, an eye tracking subsystem, and an attention-aware subsystem) and two theoretically grounded design principles that provide prescriptive knowledge on how to deliver individualized VAF.

We justify the proposed design referring to theory on human attention limitations based on Broadbent’s filter theory (Broadbent, 1958). Also, we explain the different stages of processing information on dashboards and the important role of users’ attention during this processing using an adapted version of Wickens et al.’s (2016) human information processing stages. Further, we justify using eye movement data as an approximation for users’ attention based on the eye-mind assumption (Just & Carpenter, 1980) and on established studies that focused on the users’ gaze direction and cognitive processing (Kowler, 2011; Rayner, 1998). We evaluated the proposed design in a controlled laboratory experiment and our results confirm the derived hypotheses. Our findings highlight the supportive role of individualized VAF in improving users’ information processing performance during data exploration tasks. The experiment’s data analysis reveals that users receiving individualized VAF (Design Principles 1 and 2 instantiated) eventually exhibited better attentional resource allocation and management and better attention shift rate performance. In contrast, the control group receiving only general VAF had difficulties in managing their limited attention.

To summarize, our theoretically grounded design principles contribute valuable prescriptive knowledge on how to design attentive information dashboards that are capable of supporting users in their data exploration tasks. Following Gregor and Hevner’s (2013) DSR contribution framework, we consider our contribution to be an improvement because we successfully developed a new solution (individualized VAF based on real-time eye movement data) to the existing problem (managing limited attentional resources). Our findings can therefore support the extension of using real-time eye movement data to design and develop attentive information systems beyond the dashboard used in this study. Also, beyond the use of such support in dashboards, our findings can be transferred to design other attentive UI for IS applications.

## 7.2 Practical Implications

The use of eye trackers has moved from the controlled lab environment to everyday settings (Chuang et al., 2019), and the number of applications that work with eye tracking has increased during the last couple of years. Tobii, one of the leading companies in this field, has announced that enterprises should prepare for eye tracking technology that is coming to the devices we use every day (Eskilsson, 2019). So far, commercial

BI&A tool providers such as Tableau use eye tracking devices to understand users’ behavior while they are exploring dashboards (Alberts, 2017); however, the use of eye movement data in real time has not yet been integrated into BI&A platforms (Silva et al., 2019). Therefore, our findings support practitioners in solving existing attention-relevant challenges of dashboard users by designing features based on the proposed prescriptive knowledge regarding the design of attentive information dashboards.

In recent years, technology firms have recognized the potential of neuroscience technologies in advancing human-computer interaction (vom Brocke et al., 2013). Thus far, the high price and complexity of neuroscience tools have presented challenges to using these devices in the working environment. However, the use of eye tracking technology has recently increased due to the availability of cheaper, faster, more accurate, and easier-to-use eye trackers (Duchowski, 2017). In this study, we used Tobii Eye Tracker 4C, one of the least expensive eye trackers in the market (Farnsworth, 2019) to design and develop an attentive information dashboard providing individualized VAF. Our work represents an important step toward supporting practitioners to use not only the mouse and keyboard as input devices but also the eye tracker as an innovative, interactive device for work environments.

Further, the findings of our study can support eye-based application developers in designing data exploration support features for enterprise applications beyond dashboards. For example, SAP considered the use of eye tracking devices for the next version of their enterprise systems (Galer, 2019). In addition, Microsoft released the use of eye control on Windows 10 to facilitate the interaction between users and the system (Microsoft, 2019). The functionality can be integrated into selftracking dashboards such as the MyAnalytics dashboard developed by Microsoft (2020) for workplaces. It can also support users in managing their limited attentional resources. Further, this knowledge can be transferred to applications that appear in augmented and virtual reality (AR/VR). Specifically, in virtual reality, eyes are known as the main source of understanding users’ intentions. Thus, the design principles introduced in this DSR project might be used in designing individualized VAF in VR or AR-based information systems.

Another interesting finding of our study is that most of the participants started in the top-left area of the dashboard and focused their attentional resource management on this part of the dashboard. This finding agrees with existing research that found similar patterns for dashboards and other Uis (Lorigo et al., 2008; Nielsen, 2006; Soegaard, 2020). Thus, we confirm the existing design suggestion for practitioners to place important elements of a dashboard in the topleft area of the dashboard.

## 7.3 Limitations and Future Research

Although our research project’s findings clearly demonstrate the positive effect of attentive information dashboards on managing limited attentional resources, we also recognize some limitations that we need to mention.

First, we used Tobii Eye Tracker 4C for both designing and evaluating the proposed design principles. This device is a low-cost eye tracker that was mainly designed for eye-based interactive features, such as in gaming contexts. The technical capabilities of these eye trackers were sufficient to support us in designing attentive information dashboards by tracking users’ eye movement data in real time and providing individualized VAF based on the data. However, for the evaluation part, we could have used more professional eye trackers that collect eye movement data more accurately and also collect additional data, such as pupil dilation (Buettner et al., 2018; Fehrenbacher & Djamasbi, 2017). With more advanced technology, future research could analyze users’ eye movements between single elements within one chart.

Our study defined rather broad AOIs (600 x 394 pixels), given the technical capabilities of the selected eye trackers and the goal of our analysis. The ability to capture the eye movement data of smaller AOIs could enable the investigation of more realistic dashboards with uneven complexity distributions (e.g., charts of different sizes, charts with varying content, etc.). Further, collecting additional data such as pupil dilation could enable the analysis of users’ mental effort during their interaction with the dashboard and while receiving feedback (Paas et al., 2003). Thereby, future research could, for example, investigate whether providing individualized VAF decreases or increases users’ mental effort in the feedback phase as well as in the subsequent revisit phase. Our findings show that providing individualized VAF improves users’ attentional resource allocation and management; however, it would be interesting to follow up on users’ mental effort during the data exploration phase.

Second, the dashboard used in this study does not represent a real-world dashboard design. As discussed in Section 5.2.2, we selected this design to explore users’ goal-driven attention by controlling their stimulus-driven attention (Corbetta & Shulman, 2002; Desimone & Duncan, 1995). However, features that derive stimulus-driven attention play an important role in the effectiveness of dashboards (Pauwels et al., 2009; Yigitbasioglu & Velcu, 2012). For example, the color, orientation, and size of dashboard elements can guide users’ attention toward these salient objects (Treisman & Gelade, 1980; Wolfe & Horowitz, 2004). Moreover, we controlled for interactive features (e.g., filtering, zooming, etc.) and used a static dashboard, but most real-world dashboards in the market provide interactive features to support users in exploring information from different perspectives. We decided to control the dashboard’s design, the complexity of the dashboard content, and the lack of interactive features in our study because we wanted to focus on the influence of the individualized VAF. Therefore, it was important to conduct the experiment with a high internal validity by limiting other potentially influential factors affecting users’ attentional resource allocation and management and their attention shift rates. Future research could investigate more realistic dashboards with, for example, varying complexity and interactive features. Additionally, there is an opportunity to conduct further research that considers the importance of certain information provided in dashboards based on the computation of information entropy (Krejtz et al., 2014, 2016). Analyzing eye movement data (using more accurate eye trackers) could highlight areas in the dashboard with high information entropy. Such entropy-based models could support the design of VAF types that consider the importance of different information types and guide users’ attention on that basis. Finally, we believe that there is a need to conduct field studies that focus on the impact of individualized VAF in organizational environments.

Third, our study relies on eye movement data to track users’ attentional resource allocation and management. Human eye movement data demonstrates users’ overt attention (Carrasco, 2011; Kowler, 2011). However, Duchowski (2017, p. 13) has pointed out that “in all eye tracking work … we assume that attention is linked to foveal gaze direction, but we acknowledge that it may not always be so.” Roda (2006) has suggested using eye trackers in addition to other bio-signals like heart rate, EEG, brain signals with fMRI, etc. to design attentive UI. Future research could, for example, investigate the use of electroencephalogram (EEG) or functional magnetic resonance imaging (fMRI) data in addition to eye movement data collected with an eye tracker (Léger et al., 2014), which would enable more accurate measurements of users’ attentional reactions regarding the processing of information on dashboards, receiving feedback on their behaviors, and attention management. These findings could also be used to revise or extend our first design principle by utilizing additional sensory data to compute users attentional resource allocation.

Fourth, the individualized VAF provided in this study is in the form of the gaze duration on each chart in a time format. While this format was found to be effective for our study, further feedback formats based on eye movement visualization approaches are available (Blascheck et al., 2014). Future research could investigate different gaze visualizations (e.g., heatmap, scan path, etc.) and/or animate forms of these visualizations to provide individualized VAF from different perspectives (Langner et al., 2020).

Fifth, in this study, we focused on improving users’ information processing performance through the management of attentional resources, rather than on the influence of attentive information dashboards on business decisions. Previous studies have shown that attention patterns can explain task performance (Bera et al., 2019). Also, engaging users with the information on dashboards may allow them to extract and remember more detailed information (Healey & Enns, 2012). Furthermore, usage of attentive information dashboards may have impacts on users’ mental load, confidence level, stress, etc. Future research could investigate the impacts of attentive information dashboards beyond attention management.

## 8 Conclusion

This study was motivated by challenges that users experience in managing their limited attention when exploring information dashboards. Following the DSR paradigm, we provide a new solution to this problem and articulate theoretically grounded design principles for designing an innovative artifact: namely, the attentive information dashboard. This artifact is capable of tracking users’ eye movement data in real time and can provide users with individualized VAF, based on this data. Further, we evaluated the proposed design in an eye tracking laboratory experiment with 92 participants. Our findings reveal the positive effect of using individualized VAF on information processing performance, focusing on attentional resource allocation and management and on attention shift rates. We contribute to research and practice through prescriptive knowledge on how to design attentive information dashboards.

## References

Ahn, J.-H., Bae, Y.-S., Ju, J., & Oh, W. (2018). Attention adjustment, renewal, and equilibrium seeking in online search: An eye-tracking approach. Journal of Management Information Systems, 35(4), 1218-1250.

Alberts, A. (2017). Eye-tracking study: 5 key learnings for data designers everywhere. Tableau Software. https://www.tableau.com/about/blog/2017/6/ eye-tracking-study-5-key-learnings-datadesigners-everywhere-72395

Anderson, C., Hübener, I., Seipp, A.-K., Ohly, S., David, K., & Pejovic, V. (2018). A survey of attention management systems in ubiquitous computing environments. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies.

Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. Psychology of Learning and Motivation, 2(4), 89-195.

Bačić, D., & Fadlalla, A. (2016). Business information visualization intellectual contributions: An integrative framework of visualization capabilities and dimensions of visual intelligence. Decision Support Systems, 89, 77- 86.

Baddeley, A. (1992). Working memory. Science, 255(5044), 556-559.

Baddeley, A., & Hitch, G. (1974). Working memory. In Psychology of Learning and Motivation, 8, 47-89

Bailey, B. P., & Konstan, J. A. (2006). On the need for attention-aware systems: Measuring effects of interruption on task performance, error rate, and affective state. Computers in Human Behavior, 22(4), 685-708.

Baker, J., Jones, D. R., & Burkman, J. (2009). Using visual representations of data to enhance sensemaking in data exploration tasks. Journal of the Association for Information Systems, 10(7), 533-559.

Balzer, W. K., Doherty, M. E., & O’Connor, R. (1989). Effects of cognitive feedback on performance. Psychological Bulletin, 106(3), 410-433.

Baskett, L., LeRouge, C., & Tremblay, M. C. (2008). Using the dashboard technology properly. Health Progress, 89(5), 16-23.

Bednarik, R., & Tukiainen, M. (2006). An eyetracking methodology for characterizing program comprehension processes. Proceedings of the 2006 Symposium on Eye

Tracking Research & Applications (pp. 125- 132).

Bednarik, R., & Tukiainen, M. (2008). Temporal eyetracking data: Evolution of debugging strategies with multiple representations. Proceedings of the 2008 Symposium on Eye Tracking Research & Applications (pp. 99-102).

Behrisch, M., Streeb, D., Stoffel, F., Seebacher, D., Matejek, B., Weber, S. H., Mittelstaedt, S., Pfister, H., & Keim, D. (2018). Commercial visual analytics systems-advances in the big data analytics field. IEEE Transactions on Visualization and Computer Graphics, 25(10), 3011-3031.

Bera, P. (2014). Do distracting dashboards matter? Evidence from an eye tracking study. Information Systems: Education, Applications, Research—Proceedings of the SIGSAND/PLAIS EuroSymposium (pp. 65-74).

Bera, P. (2016). How colors in business dashboards affect users’ decision making. Communications of the ACM, 59(4), 50-57.

Bera, P., Soffer, P., & Parsons, J. (2019). Using eye tracking to expose cognitive processes in understanding conceptual models. MIS Quarterly, 43(4), 1105-1126.

Blascheck, T., Kurzhals, K., Raschke, M., Burch, M., Weiskopf, D., & Ertl, T. (2014). State-of-theart of visualization for eye tracking data. Proceedings of the Eurographics Conference on Visualization.

Borkin, M. A., Bylinskii, Z., Kim, N. W., Bainbridge, C. M., Yeh, C. S., Borkin, D., Pfister, H., & Oliva, A. (2016). Beyond memorability: Visualization recognition and recall. IEEE Transactions on Visualization and Computer Graphics, 22(1), 519-528.

Borkin, M. A., Vo, A. A., Bylinskii, Z., Isola, P., Sunkavalli, S., Oliva, A., & Pfister, H. (2013). What makes a visualization memorable? IEEE Transactions on Visualization and Computer Graphics, 19(12), 2306-2315.

Broadbent, D. E. (1958). Perception and communication. Pergamon Press.

Browne, G., & Parsons, J. (2012). More enduring questions in cognitive IS research. Journal of the Association for Information Systems, 13(12), 1000-1011.

Buettner, R., Sauer, S., Maier, C., & Eckhardt, A. (2018). Real-time prediction of user performance based on pupillary assessment via eye-tracking. AIS Transactions on Human-Computer Interaction, 10(1), 26-60.

Bulling, A. (2016). Pervasive attentive user interfaces. Computer, 49(1), 94-98.

Bulling, A., Roggen, D., & Tröster, G. (2011). What’s in the eyes for context-awareness? IEEE Pervasive Computing, 10(2), 48-57.

Burch, M., Heinrich, J., Konevtsova, N., Höferlin, M., & Weiskopf, D. (2011). Evaluation of traditional, orthogonal, and radial tree diagrams by an eye tracking study. IEEE Transactions on Visualization and Computer Graphics, 17(12), 2440-2448.

Burton-Jones, A., & Meso, P. N. (2008). The effects of decomposition quality and multiple forms of information on novices’ understanding of a domain from a conceptual model. Journal of the Association for Information Systems, 9(12), 748-802.

Buscher, G., Dengel, A., Biedert, R., & Elst, L. V. (2012). Attentive documents: Eye tracking as implicit feedback for information retrieval and beyond attentive documents. ACM Transactions on Interactive Intelligent Systems, 1(2), Article 9.

Cane, J. E., Cauchard, F., & Weger, U. W. (2012). The time-course of recovery from interruption during reading: Eye movement evidence for the role of interruption lag and spatial memory. Quarterly Journal of Experimental Psychology, 65(7), 1397-1413.

Card, S. K. (1983). The Human Information Processor. CRC Press.

Carrasco, M. (2011). Visual attention: The past 25 years. Vision Research, 51(13), 1484-1525.

Chen, H., Chiang, R. H. L., & Storey, V. C. (2012). Business intelligence and analytics: From big data to big impact. MIS Quarterly, 36(4), 1165- 1189.

Chen, J. Q., & Lee, S. M. (2003). An exploratory cognitive DSS for strategic decision making. Decision Support Systems, 36(2), 147-160.

Chenoweth, T., Dowling, K. L., & St. Louis, R. D. (2004). Convincing DSS users that complex models are worth the effort. Decision Support Systems, 37(1), 71-82.

Cheung, M. Y. M., Hong, W., & Thong, J. Y. L. (2017). Effects of animation on attentional resources of online consumers. Journal of the Association for Information Systems, 18(8), 605-632.

Chuang, L., Duchowski, A. T., Qvarfordt, P., & Weiskopf, D. (2019). Ubiquitous gaze sensing and interaction (Dagstuhl Seminar 18252). In T. Blascheck (Ed.), Dagstuhl Reports (Vol. 8,

Issue 6, pp. 77-148). Schloss Dagstuhl – LZI GmbH

Chun, M. M., Golomb, J. D., & Turk-Browne, N. B. (2011). A Taxonomy of External and Internal Attention. Annual Review of Psychology, 62(1), 73-101.

Cöltekin, A., Fabrikant, S. I., & Lacayo, M. (2010). Exploring the efficiency of users’ visual analytics strategies based on sequence analysis of eye movement recordings. International Journal of Geographical Information Science, 24(10), 1559-1575.

Conway, A. R. A., Kane, M. J., Bunting, M. F., Hambrick, D. Z., Wilhelm, O., & Engle, R. W. (2005). Working memory span tasks: A methodological review and user’s guide. Psychonomic Bulletin & Review, 12(5), 769- 786.

Corbetta, M., & Shulman, G. L. (2002). Control of Goal-Directed and Stimulus-Driven Attention in the Brain. Nature Reviews Neuroscience, 3(3), 215-229.

D’Angelo, S., & Gergle, D. (2018). An Eye For Design: Gaze Visualizations for Remote Collaborative Work. Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems.

D’Mello, S., Olney, A., Williams, C., & Hays, P. (2012). Gaze tutor: A gaze-reactive intelligent tutoring system. International Journal of Human-Computer Studies, 70(5), 377-398.

Davenport, T. H., & Beck, J. C. (2001). The attention economy. Ubiquity, 2001 (May), https://doi. org/10.1145/376625.376626

Davern, M., Shaft, T., & Te’eni, D. (2012). Cognition matters: Enduring questions in cognitive is research. Journal of the Association for Information Systems, 13(4), 273-314.

Davis, F. D., Riedl, R., & Hevner, A. R. (2014). Towards a NeuroIS research methodology: intensifying the discussion on methods, tools, and measurement. Journal of the Association for Information Systems, 15(10), i-xxxv.

Delen, D., & Ram, S. (2018). Research challenges and opportunities in business analytics. Journal of Business Analytics, 1(1), 2-12.

Deng, X., & Chi, L. (2012). Understanding postadoptive behaviors in information systems use: A longitudinal analysis of system use problems in the business intelligence context. Journal of Management Information Systems, 29(3), 291-326.

Desimone, R., & Duncan, J. (1995). Neural mechanisms of selective visual attention. Annual Review of Neuroscience, 18(1), 193- 222.

Deza, A., Peters, J. R., Taylor, G. S., Surana, A., & Eckstein, M. P. (2017). Attention allocation aid for visual search. Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems (pp. 220-231).

Dilla, W., Janvrin, D. J., & Raschke, R. (2010). Interactive data visualization: New directions for accounting information systems research. Journal of Information Systems, 24(2), 1-37.

Dimoka, A., Davis, F. D., Pavlou, P. A., & Dennis, A. R. (2012). On the Use of Neurophysiological Tools in IS Research: Developing a Research Agenda for NeuroIS. MIS Quarterly, 36(3), 679-702.

Driver, J. (2001). A selective review of selective attention research from the past century. British Journal of Psychology, 92(1), 53-78.

Duchowski, A. T. (2002). A breadth-first survey of eye-tracking applications. Behavior Research Methods, Instruments, & Computers, 34(4), 455-470.

Duchowski, A. T. (2017). Eye tracking methodology: theory and practice (3rd ed.). Springer.

Engle, R. W. (2002). Working memory capacity as executive attention. Current Directions in Psychological Science, 11(1), 19-23.

Engle, R. W., Kane, M. J., & Tuholski, S. W. (1999). Individual differences in working memory capacity and what they tell us about controlled attention, general fluid intelligence, and functions of the prefrontal cortex. In A. Miyake & P. Shah (Eds.), Models of working memory: Mechanisms of active maintenance and executive control (pp. 102-134). Cambridge University Press.

Eriksen, C. W., & Yeh, Y.-Y. (1985). Allocation of attention in the visual field. Journal of Experimental Psychology: Human Perception and Performance, 11(5), 583-597.

Eskilsson, H. (2019). Don’t blink: Eye tracking is coming. https://blog.tobii.com/dont-blink-eyetracking-is-coming-f07b855995be

Farnsworth, B. (2019). Eye tracker prices: An overview of 20+ eye trackers. iMotions. https://imotions.com/blog/eye-tracker-prices/

Fehrenbacher, D. D., & Djamasbi, S. (2017). Information systems and task demand: An exploratory pupillometry study of

computerized decision making. Decision Support Systems, 97, 1-11.

Few, S. (2006). Information dashboard design, the effective visual communication of data (1st ed.). O’Reilly Media.

Figl, K., & Laue, R. (2011). Cognitive complexity in business process modeling. In H. Mouratidis & C. Rolland (Eds.), Advanced information systems engineering. CAiSE 2011. Lecture notes in computer science (Vol. 6741, pp. 452- 466). Springer.

Galer, S. (2019). SAP arbeitet mit Start-up zusammen an Eye-Tracking. SAP. https://news.sap.com/ germany/2019/03/eye-tracking-start-up/

Gausby, A. (2015). Attention Spans: Consumer insights, Microsoft Canada. Microsoft.

Göbel, F., & Kiefer, P. (2019). POITrack: Improving map-based planning with implicit POI tracking. Proceedings of the 11th ACM Symposium on Eye Tracking Research & Applications.

Goldhaber, M. H. (1997). The attention economy and the Net. First Monday, 2(4), https://doi.org/ 10.5210/fm.v2i4.519

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337- 355.

Günther, W. A., Rezazade Mehrizi, M. H., Huysman, M., & Feldberg, F. (2017). Debating big data: A literature review on realizing value from big data. Journal of Strategic Information Systems, 26(3), 191-209.

Haroz, S., & Whitney, D. (2012). How capacity limits of attention influence information visualization effectiveness. IEEE Transactions on Visualization and Computer Graphics, 18(12), 2402-2410.

Hayhoe, M., & Ballard, D. (2005). Eye movements in natural behavior. Trends in Cognitive Sciences, 9(4), 188-194.

Healey, C., & Enns, J. (2012). Attention and visual memory in visualization and computer graphics. IEEE Transactions on Visualization and Computer Graphics, 18(7), 1170-1188.

Henderson, J. M., Shinkareva, S. V., Wang, J., Luke, S. G., & Olejarczyk, J. (2013). Predicting cognitive state from eye movements. PLoS ONE, 8(5), Article e64937.

Hibbeln, M., Jenkins, J. L., Schneider, C., Valacich, J. S., & Weinmann, M. (2017). How is your user feeling? Inferring emotion through human-

computer interaction devices. MIS Quarterly, 41(1), 1-21.

Hong, W., Thong, J. Y. L., & Tam, K. Y. (2004). Does animation attract online users’ attention? The effects of flash on information search performance and perceptions. Information Systems Research, 15(1), 60-86.

Ishii, R., Nakano, Y. I., & Nishida, T. (2013). Gaze awareness in conversational agents: Estimating a user’s conversational engagement from eye gaze. ACM Transactions on Interactive Intelligent Systems, 3(2), 1-25.

Jung, J. H., Schneider, C., & Valacich, J. (2010). Enhancing the motivational affordance of information systems: The effects of real-time performance feedback and goal setting in group collaboration environments. Management Science, 56(4), 724-742.

Just, M. A., & Carpenter, P. A. (1980). A theory of reading: From eye fixations to comprehension. Psychological Review, 87(4), 329-354.

Kahneman, D. (1973). Attention and effort. Prentice-Hall.

Kane, M. J., Bleckley, M. K., Conway, A. R. A., & Engle, R. W. (2001). A controlled-attention view of working-memory capacity. Journal of Experimental Psychology: General, 130(2), 169-183.

Kane, M. J., & Engle, R. W. (2003). Working-memory capacity and the control of attention: The contributions of goal neglect, response competition, and task set to Stroop interference. Journal of Experimental Psychology: General, 132(1), 47-70.

Kelton, A. S., Pennington, R. R., & Tuttle, B. M. (2010). The effects of information presentation format on judgment and decision making: A review of the information systems research. Journal of Information Systems, 24(2), 79-105.

Kern, D., Marshall, P., & Schmidt, A. (2010). Gazemarks: Gaze-based visual placeholders to ease attention switching. Proceedings of the 28th International Conference on Human Factors in Computing Systems, 2093-2102.

Kessels, R. P. C., van Zandvoort, M. J. E., Postma, A., Kappelle, L. J., & de Haan, E. H. F. (2000). The Corsi block-tapping task: standardization and normative data. Applied Neuropsychology, 7(4), 252-258.

Kowler, E. (2011). Eye movements: The past 25 years. Vision Research, 51(13), 1457-1483.

Krejtz, K., Duchowski, A. T., & Kopacz, A. (2016). Gaze transitions when learning with multimedia. Journal of Eye Movement Research, 9(1), 1-17.

Krejtz, K., Szmidt, T., Duchowski, A. T., & Krejtz, I. (2014). Entropy-based statistical analysis of eye movement transitions. Proceedings of the Eye Tracking Research and Applications Symposium (pp. 159-166).

Kuechler, W., & Vaishnavi, V. (2012). A framework for theory development in design science research: Multiple perspectives. Journal of the Association for Information Systems, 13(6), 395-423.

Kurzhals, K., Fisher, B., Burch, M., & Weiskopf, D. (2016). Eye tracking evaluation of visual analytics. Information Visualization, 15(4), 340-358.

Langner, M., Toreini, P., & Maedche, A. (2020). AttentionBoard: A quantified-self dashboard for enhancing attention management with eyetracking. In F. D. Davis, R. Riedl, J. M. vom Brocke, P. M. Léger, A. B. Randolph, T. Fischer (Eds.), Lecture notes in information systems and organisation (Vol. 43, pp. 266- 275). Springer

Léger, P.-M., Sénécal, S., Courtemanche, F., Guinea, A., Titah, R., Fredette, M., & Labonte-LeMoyne, É. (2014). Precision is in the eye of the beholder: Application of eye fixationrelated potentials to information systems research. Journal of the Association for Information Systems, 15(10), 651-678.

Lerch, F. J., & Harter, D. E. (2001). Cognitive support for real-time dynamic decision making. Information Systems Research, 12(1), 63-82.

Lim, K. H., O’Connor, M. J., & Remus, W. E. (2005). The impact of presentation media on decision making: Does multimedia improve the effectiveness of feedback? Information and Management, 42(2), 305-316.

Liversedge, S. P., & Findlay, J. M. (2000). Saccadic eye movements and cognition. Trends in Cognitive Sciences, 4(1), 6-14.

Lorigo, L., Haridasan, M., Brynjarsdóttir, H., Xia, L., Joachims, T., Gay, G., Granka, L., Pellacini, F., & Pan, B. (2008). Eye tracking and online search: Lessons learned and challenges ahead. Journal of the American Society for Information Science & Technology, 59(7), 1041-1052.

Lux, E., Adam, M. T. P., Dorner, V., Helming, S., Knierim, M. T., & Weinhardt, C. (2018). Live

biofeedback as a user interface design element: A review of the literature. Communications of the Association for Information Systems, 43, 257-296.

Maglio, P. P., Barrett, R., Campbell, C. S., & Selker, T. (2000). SUITOR: An attentive information system. In Proceedings of the 5th International Conference on Intelligent User Interfaces (pp. 169-176).

Majaranta, P., & Bulling, A. (2014). Eye tracking and eye-based human-computer interaction. In S. Fairclough & K. Gilleade (Eds.), Advances in Physiological Computing. Human-Computer Interaction Series (pp. 39-65). Springer.

Mariakakis, A., Goel, M., Aumi, M. T. I., Patel, S. N., & Wobbrock, J. O. (2015). SwitchBack: Using focus and saccade tracking to guide users’ attention for mobile task resumption. In Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems (pp. 2953-2962).

Microsoft. (2019). Get started with eye control in Windows 10. https://support.microsoft.com/enus/help/ 4043921/windows-10-get-started-eyecontrol

Microsoft. (2020). MyAnalytics dashboard. https://docs.microsoft.com/en-us/workplaceanalytics/myanalytics/use/dashboard-2

Miller, G. A. (1956). The magical number seven, plus or minus two: some limits on our capacity for processing information. Psychological Review, 63(2), 81-97.

Monk, C. A., Trafton, J. G., & Boehm-Davis, D. A. (2008). The Effect of Interruption Duration and Demand on Resuming Suspended Goals. Journal of Experimental Psychology: Applied, 14(4), 299-313.

Montazemi, A. R., Wang, F., Nainar, S. M. K., & Bart, C. K. (1996). On the effectiveness of decisional guidance. Decision Support Systems, 18(2), 181-198.

Mueller, S. T., & Piper, B. J. (2014). The Psychology Experiment Building Language (PEBL) and PEBL Test Battery. Journal of Neuroscience Methods, 222, 250-259.

Nadj, M., Maedche, A., & Schieder, C. (2020). The effect of interactive analytical dashboard features on situation awareness and task performance. Decision Support Systems, 135, Article 113322.

Nah, F., & Benbasat, I. (2004). Knowledge-based support in a group decision making context: An expert-novice comparison. Journal of the

Association for Information Systems, 5(3), 125- 150.

Negash, S., & Gray, P. (2008). Business Intelligence. In Handbook on Decision Support Systems 2 (pp. 175-193). Springer.

Nielsen, J. (1993). Noncommand user interfaces. Communications of the ACM, 36(4), 83-99.

Nielsen, J. (2006). F-Shaped pattern for reading web content. Nielsen Norman Group.

Niu, L., Lu, J., Zhang, G., & Wu, D. (2013). FACETS: A cognitive business intelligence system. Information Systems, 38(6), 835-862.

O’Donnell, E., & David, J. S. (2000). How information systems influence user decisions: A research framework and literature review. International Journal of Accounting Information Systems, 1(3), 178-203.

Okan, Y., Galesic, M., & Garcia-Retamero, R. (2016). How people with low and high graph literacy process health graphs: Evidence from eyetracking. Journal of Behavioral Decision Making, 29(2-3), 271-294.

Okoe, M., Alam, S. S., & Jianu, R. (2014). A gazeenabled graph visualization to improve graph reading tasks. Computer Graphics Forum, 33(3), 251-260.

Orquin, J. L., & Mueller Loose, S. (2013). Attention and choice: A review on eye movements in decision making. Acta Psychologica, 144(1), 190-206.

Paas, F., Tuovinen, J. E., Tabbers, H., & Van Gerven, P. W. M. (2003). Cognitive load measurement as a means to advance cognitive load theory. Educational Psychologist, 38(1), 63-71.

Pauwels, K., Ambler, T., Clark, B. H., LaPointe, P., Reibstein, D., Skiera, B., Wierenga, B., & Wiesel, T. (2009). Dashboards as a Service. Journal of Service Research, 12(2), 175-189.

Phillips-Wren, G., Iyer, L. S., Kulkarni, U., & Ariyachandra, T. (2015). Business analytics in the context of big data: A roadmap for research. Communications of the Association for Information Systems, 37, 448-472.

Ponsoda, V., Scott, D., & Findlay, J. M. (1995). A probability vector and transition matrix analysis of eye movements during visual search. Acta Psychologica, 88(2), 167-185.

Posner, M. I. (1980). Orienting of attention. Quarterly Journal of Experimental Psychology, 32(1), 3- 25.

Preece, J., Sharp, H., & Rogers, Y. (2015). Interaction design: Beyond human-computer interaction Wiley.

Qvarfordt, P., Biehl, J. T., Golovchinsky, G., & Dunningan, T. (2010). Understanding the benefits of gaze enhanced visual search. Proceedings of the 2010 Symposium on Eye-Tracking Research & Applications (pp. 283- 290).

Rayner, K. (1998). Eye movements in reading and information processing: 20 years of research. Psychological Bulletin, 124(3), 372-422.

Riedl, R., Fischer, T., & Léger, P.-M. (2017). A Decade of NeuroIS Research: Status Quo, Challenges, and Future Directions. Proceedings of the 38th International Conference on Information Systems (pp. 1-28).

Riedl, R., & Léger, P.-M. (2016). Fundamentals of NeuroIS: Information systems and the brain. Springer.

Roda, C. (2011). Human attention and its implications for human-computer interaction. In Human Attention in Digital Environments (pp. 11-62). Cambridge University Press.

Roda, C., & Thomas, J. (2006). Attention aware systems: Theories, applications, and research agenda. Computers in Human Behavior, 22(4), 557-587.

Sallam, R. L., Tapadinhas, J., Parenteau, J., Yuen, D., & Hostmann, B. (2017). Magic quadrant for business intelligence and analytics platforms.

Sarter, N. B. (2000). The Need for Multisensory Interfaces in Support of Effective Attention Allocation in Highly Dynamic Event-Driven Domains: The Case of Cockpit Automation. The International Journal of Aviation Psychology, 10(3), 231-245.

Schwarz, C., Schwarz, A., & Black, W. C. (2014). Examining the Impact of Multicollinearity in Discovering Higher-Order Factor Models. Communications of the Association for Information Systems, 34, 1247-1268.

Sedig, K., & Pasob, P. (2013). Interaction Design for Complex Cognitive Activities with Visual Representations: A Pattern-Based Approach. Transaction on Human-Computer Interaction, 5, 84-133.

Sengupta, K., & Te’eni, D. (1993). Cognitive Feedback in GDSS: Improving Control and Convergence. MIS Quarterly, 17(1), 87-113.

Sharma, K., Alavi, H. S., Jermann, P., & Dillenbourg, P. (2016). A gaze-based learning analytics

model: In-Video Visual Feedback to Improve Learner’s Attention in MOOCs. Proceedings of the Sixth International Conference on Learning Analytics & Knowledge, 417-421.

Silva, N., Blascheck, T., Jianu, R., Rodrigues, N., Weiskopf, D., Raubal, M., & Schreck, T. (2019). Eye tracking support for visual analytics systems. Proceedings of the 11th ACM Symposium on Eye Tracking Research & Applications.

Simon, H. A. (1971). Designing organizations for an information-rich world. In M. Greenberger (Ed.), Computers, communications and the public interest (pp. 37-51). The Johns Hopkins University Press.

Singh, D. T. (1998). Incorporating cognitive aids into decision support systems: The case of the strategy execution process. Decision Support Systems, 24(2), 145-163.

Smerecnik, C. M. R., Mesters, I., Kessels, L. T. E., Ruiter, R. A. C., De Vries, N. K., & De Vries, H. (2010). Understanding the positive effects of graphical risk information on comprehension: Measuring attention directed to written, tabular, and graphical risk information. Risk Analysis, 30(9), 1387-1398.

Soegaard, M. (2020). Visual hierarchy: Organizing content to follow natural eye movement patterns. Interaction Design Foundation. https://www.interactiondesign.org/literature/article/visual-hierarchyorganizing-content-to-follow-natural-eyemovement-patterns

Somervell, J., McCrickard, D., North, C., & Shukla, M. (2002). An evaluation of information visualization in attention-limited environments. In D. Ebert, P. Brunet, & I. Navazo (Eds.), Proceedings of the Eurographics / IEEE VGTC Symposium on Visualization (pp. 211-216).

Sridharan, S., McNamara, A., & Grimm, C. (2012). Subtle gaze manipulation for improved mammography training. Proceedings of the Symposium on Eye Tracking Research and Applications.

Statistics Brain. (2015). Attention span statistics. https://www.statisticbrain.com/attention-spanstatistics/

Toker, D., Conati, C., Steichen, B., & Carenini, G. (2013). Individual user characteristics and information visualization. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, (pp. 295-304).

Toreini, P., & Langner, M. (2019). Designing Useradaptive information dashboards: Considering limited attention and working memory. Proceedings of the 27th European Conference on Information Systems.

Toreini, P., Langner, M., & Maedche, A. (2020). Using eye-tracking for visual attention feedback. In F. Davis, R. Riedl, J. vom Brocke, P. Léger, A. Randolph, & T. Fischer (Eds.), Information Systems and Neuroscience (NeuroIS Retreat 2019). Lecture Notes in Information Systems and Organisation (Vol. 32, pp. 261-270). Springer.

Toreini, P., Langner, M., & Maedche, A. (2018a). Designing attention-aware business intelligence and analytics dashboards to support task resumption. Proceedings of the European Conference on Information Systems.

Toreini, P., Langner, M., & Maedche, A. (2018b). Use of attentive information dashboards to support task resumption in working environments. Proceedings of the 2018 ACM Symposium on Eye Tracking Research & Applications.

Toreini, P., & Morana, S. (2017). Designing attentionaware business intelligence and analytics dashboards. Research in Progress: Proceedings of the 12th International Conference on Design Science Research in Information Systems and Technology (DESRIST) (pp. 64-72).

Treisman, A. M., & Gelade, G. (1980). A featureintegration theory of attention. Cognitive Psychology, 12(1), 97-136.

Trieu, V. H. (2017). Getting value from business intelligence systems: A review and research agenda. Decision Support Systems, 93, 111-124.

van Gog, T., Jarodzka, H., Scheiter, K., Gerjets, P., & Paas, F. (2009). Attention guidance during example study via the model’s eye movements. Computers in Human Behavior, 25(3), 785-791.

Vandenbosch, B., & Huff, S. L. (1997). Searching and scanning: How executives obtain information from executive information systems. MIS Quarterly, 21(1), 81-107.

Vasseur, A., Léger, P.-M., & Sénécal, S. (2019). Eyetracking for IS research: A literature review. Proceedings of the Eighteenth Annual Pre-ICIS Workshop on HCI Research in MIS.

Vertegaal, R. (2003). Attentive user interfaces. Communications of the ACM, 46(3), 30-33.

Vila, J., & Gomez, Y. (2016). Extracting business information from graphs: An eye tracking experiment. Journal of Business Research, 69(5), 1741-1746.

vom Brocke, J., Riedl, R., & Léger, P.-M. (2013). Application Strategies for Neuroscience in Information Systems Design Science Research. Journal of Computer Information Systems, 53(3), 1-13.

Ward, M. O., Grinstein, G., & Keim, D. (2010). Interactive Data visualization: Foundations, techniques, and applications. CRC Press.

Ware, C. (2012). Information visualization: Perception for design (2nd ed.). Morgan Kaufmann Publishers.

Wickens, C. D., Hollands, J. G., Banbury, S., & Parasuraman, R. (2016). Engineering psychology and human performance (4th ed.). Routledge, Taylor & Francis Group.

Wolfe, J. M., & Horowitz, T. S. (2004). What attributes guide the deployment of visual attention and how do they do it? Nature Reviews Neuroscience, 5(6), 495-501.

Xu, S., Jiang, H., & Lau, F. C. M. (2008). Personalized online document, image and video recommendation via commodity eye-tracking. Proceedings of the 2008 ACM Conference on Recommender Systems (pp. 83-90).

Yigitbasioglu, O. M., & Velcu, O. (2012). A review of dashboards in performance management: Implications for design and research. International Journal of Accounting Information Systems, 13(1), 41-59.

Zhang, Y., Pfeuffer, K., Chong, M. K., Alexander, J., Bulling, A., & Gellersen, H. (2017). Look together: using gaze for assisting co-located collaborative search. Personal and Ubiquitous Computing, 21(1), 173-186.

Zhicheng Liu, & Stasko, J. T. (2010). Mental models, visual reasoning and interaction in information visualization: A top-down perspective. IEEE Transactions on Visualization and Computer Graphics, 16(6), 999-1008.

## About the Authors

Peyman Toreini is postdoctoral researcher at the Institute of Information Systems and Marketing (IISM) at the Karlsruhe Institute of Technology (KIT), Germany. He received his PhD in information systems from KIT, his MSc in media informatics from RWTH Aachen University, Germany. His research focuses on the intersection between information systems and human-computer interaction by designing and developing the next generation of user interfaces for working environments. In particular, he is interested in the novel user experiences that are enabled by eye trackers on desktop stations, augmented and mixed reality environments. His works have been published in the proceedings of conferences such as European Conference on Information Systems, International Conference on Design Science Research in Information Systems, Information Systems and Neuroscience, and others.

Moritz Langner is a PhD student at the Institute of Information Systems and Marketing (IISM) at the Karlsruhe Institute of Technology (KIT) in Germany. He received his bachelor’s and master’s degrees in industrial engineering and management from the Karlsruhe Institute of Technology. His research focuses on the intersection of information systems and human computer interaction. More specifically, he investigates user-adaptive systems in the working environment using eye tracking technology. He has published his research in the proceedings of information systems conferences such as the European Conference on Information Systems and NeuroIS.

Alexander Maedche is a full professor of information systems at the Karlsruhe Institute of Technology (KIT), Germany, and spokesperson of KIT’s Institute of Information Systems and Marketing (IISM). His research focuses on designing interactive intelligent systems, such as conversational agents, business intelligence & analytics systems, NeuroIS (esp. eye-tracking and physio-adaptive systems), and interactive development systems. He publishes in leading information systems and computer science conferences and journals such as MIS Quarterly, Journal of the Association of Information Systems, Business & Information Systems Engineering, Information & Software Technology, Computers & Human Behavior, International Journal of Human-Computer Studies, IEEE Transactions on Software Engineering, IEEE Intelligent Systems, VLDB Journal, and AI Magazine, among others. He has held various editorial roles and positions in the information systems research community.

Stefan Morana is a junior professor of digital transformation and information systems at the Saarland University. His research focuses on the human-centered design of interactive systems for digital transformation from the perspective of the individual, organizations, and society. More specifically, he investigates the design of assistant systems and conversational interfaces supporting the individual usage of information systems. His research has been published in journals such as the Journal of the Association for Information Systems, Decision Support Systems, International Journal of Human-Computer Studies, Business & Information Systems Engineering, Internet Research, AIS Transactions on Human-Computer Interaction, and Communications of the Association for Information System, and in the proceedings of major information systems conferences.

Tobias Vogel is a professor of economic-, consumer-, and media psychology at the Darmstadt University of Applied Sciences. He received his doctoral degree from the University of Heidelberg and his venia legendi from the University of Mannheim. His research focuses on consumer attitudes and decision-making, with an emphasis on the acceptance of new technologies. Currently, he is part of the Horizon2020-initiative PAsCAL on connected and autonomous mobility. Within this project, he assesses the public acceptance of autonomous vehicles, and studies how autonomous vehicles can become a sustainable and inclusive mobility model. Tobias Vogel is the author of the book Attitudes and Attitude Change (co-authored by Michaela Wänke).

Copyright © 2022 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
