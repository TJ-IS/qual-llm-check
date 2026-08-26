---
otero_id: 13012
otero_key: "8VE4P5WU"
title: "Communication-Garden System: Visualizing a computer-mediated communication process"
authors: "Bin Zhu; Hsinchun Chen"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.02.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Communication-Garden System: Visualizing a computer-mediated communication process

Bin Zhu <sup>a,⁎</sup>, Hsinchun Chen <sup>b</sup>

<sup>a</sup> IS Department, School of Management, Boston University, 595 Commonwealth Avenue, Boston, MA 02215, United States <sup>b</sup> MIS department, University of Arizona, Tucson, AZ 85721, United States

Received 3 April 2007; received in revised form 23 January 2008; accepted 3 February 2008 Available online 21 February 2008

## Abstract

Archives of computer-mediated communication (CMC) could be valuable organizational resources. Most CMC archive systems focus on presenting one of the three aspects of a CMC community: discussion content, participants' behavior, or social networks among participants. Very few CMC archive systems support the easy integration of these three aspects. This paper thus describes two-phase research to propose an automatic approach that facilitates users' integrated understanding of discussion content and behavior of CMC participants. We validated the approach through the development and evaluation of a prototype system, the Communication-Garden system.

© 2008 Elsevier B.V. All rights reserved.

Keywords: Information visualization; Information categorization; Information analysis; Computer-mediated communication

## 1. Introduction

The archive of computer-mediated communication (CMC) could be a valuable organizational resource. The archive not only documents the knowledge shared during the CMC but also records the behavior of its participants and their attitude toward the virtual CMC community [33,38]. Information stored in a CMC archive could suggest the current “hot” topics in the community, participants' reaction to questions posted in different topic areas, their attitude toward the community [33], and the most active person in a certain topic area. Understanding such information could benefit an organization in various ways. Reusing documented knowledge could save time and resources. Newcomers and infrequent participants could better understand the community through grasping related information from the archive. Organizations could identify active persons in certain topic areas to facilitate collaborations among employees and to better motivate people to share their knowledge.

However, organizations can capitalize on the potential value of a CMC archive only when users of the archive comprehend the related information the archive contains. This can be a difficult task given the huge amount of information an archive holds. In addition, understanding useful information usually requires a user to integrate his or her understanding of different aspects of the CMC community. For instance, in order for a person to decide how to interact with a CMC community, he or she may need to find answers to questions such as “what are they talking about?,” “do they like this community?,” “how long do they stay?,” and “how quickly can I get answers to my question?” And the answers request a comprehension of both discussion content and participants' behaviors [15].

Therefore, in order for a CMC archive to be useful to its users, it should support the integrated understanding of different aspects of the CMC community the archive documents. We found limited support from existing CMC archive systems. Most archive systems focus only on presenting one of the three aspects of a CMC community: the discussion content [1,5,13,23,37], participants' behavior [9,10,41], or social networks among participants [17,20]. Very few CMC archive systems support the integrated comprehension of these three aspects, although its importance has been realized by the development of the Conversation Map [29] and several systems described in [10].

This paper thus describes two-phase research to propose an automatic approach that helps users associate discussion content with behavior of CMC participants. We validated the approach through the development and evaluation of a prototype system, the Communication-Garden system.

## 2. Related work and research question development

## 2.1. Computer-mediated communication

Most empirical studies of CMC have focused on the interaction among information technology, individual behavior, group characteristics, and organizational structure. These studies indicate that CMC not only provides incentives for participants to share knowledge [33] but also creates a common context in which CMC participants convert their tacit knowledge into explicit knowledge [21]. At the same time, CMC participants project their personal styles, previous experiences, and social norms into their computer-mediated communication [38]. The attitude of participants toward the community is related to the number of messages they send [33]. In addition, the person who posts more answers or participates more in discussions of a certain topic area than other individuals may be regarded as the expert in that area [2]. He or she might not be the most knowledgeable individual on that subject but is probably willing to help. Identifying those individuals could add a burden to them because they may receive more questions after their expertise becomes visible. However, the awareness of employees' expertise enables decision-makers to assign appropriate people to projects and to better facilitate collaborations among employees. The expertise within the organization thus could be better used, and the experts identified should be better rewarded for sharing their knowledge. Therefore, CMC archives could greatly benefit an organization if the rich information they store can be capitalized on.

## 2.2. Existing CMC systems

The term of “information overload” has become a cliché for the description of frustration an individual may have dealing with large amounts of information. This cliché, however, still holds true when people try to gain value from CMC archives. Many systems thus have been developed to help bring the potential value of a CMC archive to fruition. Those systems usually provide help from three perspectives: discussion content, participants' behavior, and social networks.

The content approach supports the reuse of shared knowledge by helping users find messages of interest. This approach organizes discussion content, by mediating the way its participants communicate [1,23] or by applying different information analysis and artificial intelligence technologies to facilitate the browsing and searching over an archive [5,13,37]. Search engine technologies are usually applied when searching for messages of interest.

The behavior approach helps understand the behavior of participants in a CMC community. Examples include the Chat Circles [9], PeopleGarden [41], and Netscan Thread Trees [32]. Those systems depict a CMC community by presenting such behavior information as subgroup formation, individual participation, time duration of members in a community, and temporal change of thread structure. More recent examples include visual representations developed in [28] and [36].

The network approach describes the characteristics of social networks formed during the CMC process. One example is the ContactMap [40], which acts as a visual address book to help its users manage their social connections. There are also other systems such as Expertise Recommender [17], which recommends expertise, and the PeCo (personal connections) system [24], which facilitates locating individuals with whom to collaborate based on the CMC participants' locations within a social network.

There are also systems that combine more than one approach. For instance, the Loom system [10] and the NetScan Visualization Dashboard [32] integrate content analysis and behavior description to help increase the understanding of a CMC community, whereas the Conversation Map system [29] provides overviews of both the discussion content and the social network of a CMC archive.

In summary, the development of a CMC visualization system usually involves deciding on the selection and presentation of a subset of an almost infinite set of statistics and patterns that can be derived or extracted from a CMC archive based on objectives of the system [10]. Designers then develop or select appropriate technologies to present the selected statistics or patterns to users. For instance, Chen et al. [6] automatically identified and visualized discussion topics, the PeopleGarden system [41] uses a flower metaphor to describe the activeness of participants, and the NetScan Visualization Dashboard returns related newsgroups according to users' query terms and reports the number of postings and number of members in each group.

## 2.3. Research development

While various CMC archive systems have been developed to support the understanding of different aspects of a CMC community, some information needs may request integrated comprehension of several aspects of a CMC community. The rest of this subsection discusses a subset of such type of information needs that an archive user may have.

## • Subtopics and their temporal change

An effective way to support users' understanding of a CMC community is to provide discussion subtopics and their temporal patterns [25]. Various content approaches could be applied to help users retrieve discussion content of interest. Knowing the major subtopics occurred in a community could also be beneficial to organizations. When the CMC community consists of a group of customers discussing a new product, knowledge of which aspect of the product that customers care the most may greatly help an organization decide how to improve the product. In addition, an archive user could easily detect the current “hot” topics by exploring the temporal change of discussion subtopics. This is particularly helpful when a decisionmaker needs to identify the current major concerns or interests of a community. Such a community could be a group of customers or a group of employees. The awareness of the starting time of a subtopic could also be crucial. For a community of customers, the occurrence of a new topic may be related to a recent change to the product, while a community of employees may start talking about their concerns when there is a new company policy.

## • Interaction status of each sub-topic

Simultaneously, different reactions of community participants to questions posted in different topic areas could be another type of helpful information. Newcomers and infrequent participants in a community could use this information to assess the reaction of a community before posting any questions. To this end knowing only subtopics existed in an archive is insufficient. A newcomer or an infrequent participant may also wants to know whether the occurrence of a subtopic is the result of active discussions involving the entire community or the result of one individual's strong interest. A posted question that interests the entire community may receive quick responses, whereas the response to a question that interest only one member may vary with the availability of this specific CMC member. This type of information could also be valuable for decision-makers. Issues appealing to the entire community may deserve more attention than issues that interest only a few members.

## • Active person in each subtopic

An individual active in discussions within a topic area may not be the most knowledgeable person in that area, but he or she is probably willing to help if he or she knows the answer. Those people may also be good potential collaborators when there is a need for their expertise. It is important to know who and where those individuals are. As discussed above, identifying those active individuals may have undesirable consequences. One such consequence could be the increased number of questions an identified active person may receive. Simultaneously, decision-makers could greatly benefit from knowing about employees' expertise.

## • Participants' attitude toward a community

Previous studies have found that the number of messages sent out by participants indicates their attitude toward the community [33]. And this could also be important for newcomers and infrequent participants because people usually do not want to waste their time and energy in a community where nobody stays very long. Managers could also benefit from this information. If this community is important to maintain, such as a customer community or knowledge-sharing community, the indication of participants' attitude may help managers develop plans to encourage or guide the participation of community members. It is also important to identify participants who post many messages but never participate any discussions or their messages never receive any feedback from the community. Those people are most likely keeping posting advertisement and do not contribute to discussions.

In summary, a CMC archive has the potential to satisfy its users' following information needs: subtopics and their temporal changes, interaction status within each subtopic, active person identification, and participants' attitude toward the community. Information systems that meet these information needs could greatly enhance the usefulness of a CMC archive. However, such needs cannot be easily fulfilled by a content or behavior approach alone. This paper therefore presents a method that integrates content and behavior approaches to help users better capitalize on the value of a CMC archive. We demonstrate our approach through the development and evaluation of a prototype system, the Communication-Garden system.

![](/api/attachments/8VE4P5WU/fulltext/images/23ca18994e2ddf60bf6e81e86486525d6be9e23936937d3b7df032c198f0b3fd.jpg)  
Fig. 1. System architecture.

## 3. Communication-Garden System

## 3.1. System architecture and technology selection

To fulfill the archive users' above-mentioned information needs, we propose a three-layer system architecture as displayed in Fig. 1. The three layers include information representation, information categorization, and information visualization. The representation level applies automatic indexing techniques to extract semantics to represent message content, while the information categorization level employs different information analysis technologies to extract patterns and salient structures from the archived information. The extracted patterns and structures will be visualized at the level of information visualization. Various existing information analysis and visualization technologies could be employed at each level. The selection of technologies should be based on the user requirement the system selects to fulfill. The rest of this subsection discusses the technologies we selected for the development of the Communication-Garden. In addition to system objectives, the selection of technologies was also based on the results from previous evaluation studies.

As displayed in Fig. 1, the backend of the Communication-Garden system has four processors: Indexer, Categorizer, Thread Visualizer, and People Visualizer. Each processor applies one type of information analysis or visualization algorithm to process the content or behavior information contained in the archive.

• Indexer automatically represents a document with a vector of terms [30]. The Communication-Garden system selected one of the available natural language processing (NLP) noun phrase tools, the Arizona Noun Phraser (AZNP) to represent the content of messages. We selected the noun phrase technique over other automatic indexing technologies because it has been shown to capture a richer linguistic representation of document content [3]. Among various existing NLP noun phrase tools, we chose to use AZNP for two reasons. First, it is available to us. Second, a previous study described in [35] found that the AZNP had better performance than other NLP noun phrase tools in identifying key noun phrases from textual documents. For the development of the Communication-Garden system, the Indexer regards messages within one thread as a unit and represents each unit with key phrases identified by the AZNP. A thread is a set of messages sharing the same subject title and sent by different persons (Fig. 2). A thread usually starts with one message followed by response messages from other participants. Such a grouping method could be inappropriate because CMC participants may use the same subject title to send out messages with completely different content, but our observation over the testbed suggested that this is rare in the archive used in this study. Another reason to group messages within one thread was that many “I agree” type of messages do not have enough content to be represented by any keyword. Those messages could be difficult to process without the context. On the other hand, we agree that grouping strategies vary with the data set. It is possible that the same grouping strategy will not apply to other archives that contain many messages with different content but share the same subject title. Fig. 3 displays an example of representing the content of a thread with a set of noun phrases extracted.

![](/api/attachments/8VE4P5WU/fulltext/images/547be4da2ec007862955c8e889d77fde3602392df30d4faa5199cfa0097035f9.jpg)  
Fig. 2. Text-based representation of a thread.

• Categorizer automatically categorizes the discussion content and identifies subtopics. The output of the Indexer is the input to the Categorizer. Compared with several neural network algorithms in previous research [16], a variant of the Kohonen's self-organizing maps (SOM) appears to be a promising algorithm for organizing large volumes of information. SOM was first proposed by Kohonen, who based his neural network on the associative neural properties of the brain [14]. The network consists of an input layer and an output layer. The number of the input nodes equals the number of attributes associated with the input. After all of the input is processed, the result is a spatial representation of the input data, organized into clusters of similar regions. Table 1 provides a detailed description of the SOM algorithm. Several recent studies adopted the SOM approach to textual analysis. Examples are the DISCERN (Distributed Script processing and Episodic memory Network) developed by [18] as a natural language processing system, the WEBSOM system developed by Kohonen's group for newsgroup classification [12], and the multilayered SOM system developed by the Arizona Artificial Intelligence Group for Internet web page categorization [4]. Their work suggests a high applicability of the SOM approach to large-scale classification. In addition, SOM has also been used in [5] to categorize and identify subtopics from messages generated by electronic meeting systems. In the Communication-Garden system, SOM was used as a categorization tool. The subtopics identified are Components, Java Compiler, XML, API, Certification information, Web Server, StringBuffer, Server Side, sockets, JAR files, Linux, Java CGI JavaScript HTML, separate threads, Java Programmers FAQ, API docs Buttons, StringTokenizer, Instant Java Servlets, Jbuilder, JSP, and HTML file.

![](/api/attachments/8VE4P5WU/fulltext/images/bfba186f1ea8e0acf20c74823a5c848f8160993cfc9d00f78a0e48cd606af640.jpg)  
Fig. 3. The sample input and output of Arizona Noun Phraser (AZNP).

• Thread Visualizer employs a floral representation to graphically depict the liveliness of a thread. This representation idea was inspired by the representation developed in [41]. As displayed in Fig. 4, each thread is represented as a flower. The number of petals of a flower equals the number of messages posted for that thread, while the number of leaves represents the number of

Table 1 Description of SOM algorithm

![](/api/attachments/8VE4P5WU/fulltext/images/9302c044ccdf17dce9d740d6d56ee7b6d646dbc4b41ed450d9a5d18d0205d3e2.jpg)  
Fig. 4. Thread representation.

persons who participate in the discussion of this thread. In addition, the height of a flower indicates how long the thread lasts. The starting time of a thread and its topic area are displayed by the location of a flower on the interface. The flower representation presents such statistics as number of messages, number of participants, time duration, starting time, and topic area of content to describe a thread. The statistics were selected based on the objectives of the Communication-Garden system. The combined number of messages and number of participants could help to distinguish between threads with many participating members and those involving only a few arguing participants. The more leaves a flower has, the more community members the discussion involves. Therefore, a user can distinguish between active discussions involving many participants and those with only a few arguing members by one glance. The number of messages alone indicates the liveliness of the discussion in a thread. Questions in a subtopic area filled with many blooming flowers are more likely to receive quick answers than those in other subtopic areas with a few flowers. The time duration of a thread is also helpful, since we observed that in our testbed a long-lasting thread might enclose interesting discussions, whereas a short discussion usually contains answers to specific questions.

•People Visualizer employs the same flower representation and is shown in Fig. 5. An individual's number of postings is associated with his or her attitude toward the community [33], whereas the combined number of postings and number of discussions indicate the activeness of a participant. In addition, the time duration of participants in a community or topic area indicates the popularity of that community or topic area. Again, the floral representation was selected to present statistics used by the system to describe a person's activity: number of messages, number of discussions, and time duration. One flower represents a person, and the number of petals equals the number of messages that person has posted.

![](/api/attachments/8VE4P5WU/fulltext/images/adae2480f9fe59ab04fa28bc09101a68b9537cb28b8aff280f88d2d7ca57f1e4.jpg)  
Fig. 5. Person representation.

The number of leaves indicates the number of threads in which that person has participated, and the height of the flower indicates how long the person has stayed in the community or topic area. Therefore a high blooming flower with many leaves represents an active participant who contributes to discussions, while a short blooming flower with very few leaves may indicate a person who comes to post advertisement and leaves. In order to distinguish between a person flower and a thread flower previously described, an icon face is put on each person flower. The location of a flower indicates the starting time of an individual in a community or topic area. Therefore, a community or topic area is popular if it contains many tall blooming flowers with many leaves.

## 3.2. The Communication-Garden System

We developed a prototype system, the Communication-Garden system, to validate the proposed architecture,

![](/api/attachments/8VE4P5WU/fulltext/images/00dbcb45e3cb852f780fb8a89053e06ba5c9b75e95e3e4d09af5633c5708b6b1.jpg)  
Description of the Display panel:

• The x-axis represents time.

• Categories generated by the SOM are laid out vertically.

• Each green line represents one message.

• The vertical thickness of each subtopic indicates its activity on a particular day.

• The length in the x-dimension of each subtopic = time duration of that subtopic.

Fig. 6. Content summary.

using the technologies described above. The system uses the archive of an electronic discussion forum as its testbed. The archive records the discussions among a group of Java programmers who have technical questions.

The interface of the Communication-Garden system consists of four types of visualization: Content Summary (Fig. 6), Interaction Summary (Fig. 7), Expert Indicator (Fig. 8), and Behavior Summary (Fig. 9). Each type presents one aspect of a CMC process. A Content Summary describes the temporal change of each subtopic, whereas Interaction Summary depicts the liveliness of discussion within each subtopic by planting thread flowers in different topic areas based on the discussion content of that thread. The number and type of threads a subtopic contains indicate its liveliness. An active subtopic consists of many tall blooming thread flowers with many leaves. Expert Indicator uses person flowers to help users locate active persons in each subtopic, and the Behavior Summary describes the behavior of each participant during the CMC process. A helpful active person may have a tall flower with many petals and leaves. Please see the captions for Figs. 6, 7, 8, and 9 for a detailed description of the graphical representation.

Figs. 6, 7, 8, and 9 present the three-panel interface of the Communication-Garden system. The left-hand panel in each of these figures is the Display panel, which presents a detailed graphical display of a particular representation, while the upper-right panel serves as an Overview, which provides a thumbprint of the detailed display. A user can select a portion of interest on the Overview, prompting the

![](/api/attachments/8VE4P5WU/fulltext/images/6879e0c96c5f85f9af25a3e54a79d66b25a46e7ac4ea70462ca7126375ff1272.jpg)  
Description of the Display panel:

The panel is divided into sub-gardens based on the SOM output. Each sub-garden is a sub topic.

• Each flower is one thread

• number of petals = number of messages posted for this thread

• number of leaves = number of participants in this thread

• height of flowers = the time duration of this thread

Fig. 7. Interaction summary.

interface to display the selected part in detail on the Display panel. At the top of both the Display panel and the Overview are four tabs. Clicking on one of these tabs will bring up one of the four types of the interface: Content Summary (Fig. 6), Interaction Summary (Fig. 7), Expert Indicator (Fig. 8), and Behavior Summary (Fig. 9). In addition, Content Summary, Interaction Summary, and Expert Indicator divide their display panels into subgardens based on the output of the Categorizer. Thus, each sub-garden represents one subtopic. The lower-right panel is the Message panel, which displays the messages of interest.

In summary, the Communication-Garden system fulfills the user information needs identified in Section 2: subtopics and their temporal evolution (Content Summary), interaction status of each subtopic (Interaction Summary), active person in each subtopic (Expert Indicator), and participants' attitude toward the community as indicated by the number of messages posted by participants and their durations of stay (Behavior Summary). By using the AZ Noun Phraser, SOM, and floral representation, the Communication-Garden system integrates content analysis with the visualization of the behavior of CMC members. Such integration could support an archive user's integrated understanding about both the discussion content and participants' behavior.

## 4. System evaluation

A comprehensive evaluation of this system may include the validation of subtopics identified by SOM, the evaluation of the visualizations designed, the investigation of the usability of the entire developed system, and the assessment of the usefulness of the system in real-

![](/api/attachments/8VE4P5WU/fulltext/images/8699a9c59bfcfe59092ec1864fa9a9fe84197fa00c43de6e72069f2ca435ded3.jpg)

Description of the Display panel

• The interface is divided into sub-gardens based on the SOM output. Each sub-garden is a subtopic.

• Each flower is one Person

• number of petals = number of messages posted by this person for this subtopic

• number of leaves = number of threads this person has participated in the subtopic

• height of flowers = how long this person stayed in this subtopic

Fig. 8. Expert indicator.

![](/api/attachments/8VE4P5WU/fulltext/images/b3b3adc7da849c9b46eb62e76a1d7e5cd357ff8f918e7da477d49af21347b372.jpg)

Description of the Display panel:

• The entire community is one garden

• Each flower is one Person

• number of petals = number of messages posted by this person in this community

• number of leaves = number thread this person participated in this community

• height of flowers = how long this person stayed in this community

Fig. 9. Behavior summary.

life scenarios. A complete evaluation thus will require a series of empirical studies and is beyond the scope of this paper. Because the quality of categories generated by SOM has been validated by our previous empirical studies when we applied SOM to categorize textual documents [6] and imagery information [43], we decided to investigate the effectiveness of visualizations implemented in the Communication-Garden system as the first step.

As indicated in [44], a visualization system could be evaluated in several ways. Studies conducted in [22,26,27] designed complex, realistic tasks based on functionalities that a visualization system intends to provide. The participants conduct tasks assigned in a practical scenario. The usefulness of a given visualization system can be directly measured by this approach, but visualization factors contributing to the user performance were difficult to identify (partially due to the intertwining nature of the system, task, and user). On the other hand, studies such as [11,19,34] utilized simple, but basic, visual operations for evaluation. Sometimes referred to as the “de-featuring approach,” this method examines generic operations such as searching objects with a given attribute value, specifying attributes of an object, clustering objects based on similarity, counting objects, and comparing visual objects. This approach allows easy attribution of user task performance to design factors. Therefore, the “de-featuring approach” appears to be an appropriate initial method to evaluate the effectiveness of graphical representations implemented in the Communication-Garden system, especially when the goal is to examine the user perception of the statistics and patterns system chosen for delivery.

## 4.1. Selection of benchmark system

We selected the text-based interface of Netscape Messenger as the benchmark system. The selection was made for two reasons: the difficulty in locating comparable graphical representations for the statistics and patterns presented by the Communication-Garden system and the similarity between Netscape Messenger and other text-based e-mail handling tools such as Microsoft Outlook and various web-based e-mail tools. The interface of Netscape Messenger enables a user to group messages by date, by thread, or by sender, presenting similar statistics about a thread or about a person that the Communication-Garden system aims to deliver. To make the text-based interface even more comparable to the interface of the Communication-Garden system, the experiment used the output of the Categorizer as input to Netscape Messenger, so its interface could display information about each subtopic (Fig. 10). A user can select a topic of interest and then group messages within the subtopic by thread or by sender. The main difference between the two systems is that the Netscape Messenger uses text format while the Communication-Garden system applies graphics to represent text messages.

## 4.2. De-featuring approach

Previous human computer interaction studies have provided a low-level, domain-independent taxonomy of information acquisition and evaluation tasks that a user may perform when confronted with an interface [39,42].

Those task types are believed to be unit tasks, and a reallife user task can be de-composed into several such unit tasks. Although it may be unclear how a set of unit tasks composes a complex real-life interface task, the optimization of the user's performance in each unit task type could contribute to higher usability of a visualization system. The “de-featuring” approach denotes mapping the domain-independent taxonomy of unit tasks into a specific domain. This approach enables the easy attribution of task performance to visualization characteristics and has also been shown to be valuable in previous studies that evaluated graphical interfaces [19].

Our evaluation study selected task types from the task taxonomy proposed in [42]. As an extension of [39], this proposed full taxonomy contains nearly fifty types of tasks. In order to design an empirical study that a participant can accomplish within one hour, it is necessary to select a subset of tasks. We selected task types based on both the task characteristics and the objectives of the Communication-Garden system. As discussed above, the goal of the evaluation is to validate the effectiveness of the graphical representation of archive information. We are more interested in whether a user can perceive the information or pattern from the interface than how easy it was for a user to navigate different views of the interface. Therefore, tasks dedicated to testing the interaction between users and the interface were excluded. In addition, the taxonomy contains several task types that belong to the same task category, which tests different aspects of the same task. Instead of investigating each task category in detail, we designed the experiment to cover as many categories as possible. On the other hand, as the goal of this study is to validate the delivery of statistics and patterns that the Communication-Garden system was designed to deliver, the tasks were also chosen based on the information content and the functionality provided by graphical and text-based interfaces. Such selection ensures that all task types selected could be performed on both types of interface. Table 2 displays the results of task selection.

![](/api/attachments/8VE4P5WU/fulltext/images/0a290c99b7f04bcb197477b2ad30e9fba672fdbb8c325553b60e595b968c6be5.jpg)  
Subtopics identified by the Categorizer. Clicking on each subtopic will display all messages in that subtopic. Users can choose to group those messages by thread, by sender, or by date.  
Fig. 10. Interface of Netscape Messenger.

Table 2

<table><tr><td colspan="2">Task types selected</td></tr><tr><td>Task types</td><td>Definition</td></tr><tr><td>Identify</td><td>Find a visual object with a particular attribute value.</td></tr><tr><td>Cluster</td><td>Find the similarity among visual objects with multiple attributes.</td></tr><tr><td>Compare</td><td>Compare based on the particular attribute.</td></tr><tr><td>Rank</td><td>Find the extremes (the best and the worst cases).</td></tr><tr><td>Correlate</td><td>When there are multiple attributes, identify objects that are similar in one attribute.</td></tr></table>

The experiment tasks were designed to test users comprehensions of such selected statistics and patterns as starting and ending dates of a subtopic and its temporal change, number of messages and participants of a thread, the time length of a thread, number of a participant's messages and discussions, and the time length of a participant. Table 3 provides some sample tasks after mapping generic task types to specific tasks. To validate the correctness of such mapping, we had two individuals evaluate the consistency between the definition of the task type and the specific tasks designed independently. The specific tasks were adjusted until the two evaluators agreed with each other.

## 4.3. Experiment process and results

Thirty-one undergraduate and graduate students participated in this study. All participants were volunteers from the Eller College of the Business and Public Administration at the University of Arizona, and none was related to this project. This was a within subject experiment that consisted of three parts. Each part evaluated users' comprehension of different statistics/patterns the Communication-Garden system seeks to deliver. Two sets of task were designed for each part. A participant used one graphical interface from the Communication-Garden system to accomplish one set of task and use the benchmark text-based interface to accomplish the other set. Participants used the Content Summary and the text-based Interface (sorted by date) in part a, used Interaction Summary and text-based Interface (group by thread) in part b, and Expert Indicator vs. text-based Interface (group by date or by sender) in part c. The tasks were designed to test all attributes of the interface; all task types are described in Table 2. A task set was assigned randomly to an interface type. In addition, the order of interface types used and the order of the three parts were also randomly assigned to a participant. At the end of each part, a questionnaire designed to collect subjective measures was given to each participant. During the experiment, participants were also encouraged to think aloud, and their comments were recorded. Overall a participant was assigned six conditions and accomplished six sets of task.

Table 3  
Task examples

<table><tr><td>Interface type</td><td>Task type</td><td>Tasks</td></tr><tr><td rowspan="5">Content summary</td><td>Task1 (identify)</td><td>Find the sub-topic or sub-topics that start on 06/26.</td></tr><tr><td>Task 2 (cluster)</td><td>Which of the following sub-topics was discussed in a temporal pattern (start/end day, number of messages posted per day) similar to “XML”? a. “components” b. “StringBuffer”</td></tr><tr><td>Task 3 (compare)</td><td>Which sub-topic, “XML” or “API,” has more messages posted on 07/08?</td></tr><tr><td>Task 4 (rank)</td><td>Which sub-topic generated the most discussions on 06/28?</td></tr><tr><td>Task 5 (correlate)</td><td>Which of the following sub-topics started on the same day as “Components”? a. “StringBuffer,” b. “XML”</td></tr><tr><td rowspan="5">Interaction summary</td><td>Task 6 (identify)</td><td>Find the sub-topic or sub-topics whose first thread has two messages.</td></tr><tr><td>Task 7 (cluster)</td><td>Which of the following sub-topics is more similar to “Web Server” in its interaction pattern (number of thread, number of messages per thread, number of participants per thread, and length of each thread) on 06/29, “StringBuffer,” or “Linux?”</td></tr><tr><td>Task 8 (compare)</td><td>Which sub-topics, “XML” or “Socket,” had more threads on 07/05?</td></tr><tr><td>Task 9 (rank)</td><td>Please find the sub-topic or sub-topics that had the fewest number of threads on 07/06.</td></tr><tr><td>Task 10 (correlate)</td><td>Which of the following sub-topics has the same number of threads as “API docs” on 07/03? “buttons” or “HTML files?”</td></tr><tr><td rowspan="5">Expert indicator</td><td>Task 11 (identify)</td><td>Find the sub-topic or sub-topics whose first participant posted three messages.</td></tr><tr><td>Task 12 (cluster)</td><td>On 07/09, which of the following sub-topics is more similar to “JAR files” in zparticipation pattern (number of participants, how long the people stay, how active each participant is)? “Web Server” or “buttons?”</td></tr><tr><td>Task 13 (compare)</td><td>On which sub-topic, “API” or “JSP,” are there more participants?</td></tr><tr><td>Task 14 (rank)</td><td>Please find the person who posted the greatest number of messages on the sub-topic “socket.”</td></tr><tr><td>Task 15 (correlate)</td><td>On 07/09, which of the following sub-topics has the same number of participants as “XML”? “API” or “Web Server?”</td></tr></table>

Since each task had a correct answer, task completion was used as the measure of effectiveness. To measure efficiency, the experiment employed time on task as the measure. In addition, subjective measures including perceived ease of use [31] and perceived usefulness [7,8] were also collected through a questionnaire at the end of each session. The questionnaire was designed by adopting question items used in previous studies [7,8,31]. The questionnaire contained ten items, with five items measuring the construct of perceived ease of use and the other five items measuring the construct of perceived usefulness. All questions were framed using a five-point scale, and a construct was measured by the sum of the scores a participant assigned to the five items.

The interface type was the only independent variable. The experiment was designed to evaluate the effectiveness of the graphical representations of the Communication-Garden system. A discussion of the impact of task type on participants' performance is therefore beyond the scope. A one-way ANOVA test was run to compare the difference between the Communication-Garden (graphical) interface and the Netscape Messenger (text-based) interface. Table 4 displays the results for objective measures. The two interface types were considered to be significantly different when the P value was smaller than 0.05. The rest of this section provides a detailed analysis of the experiment results.

• Cluster tasks required a participant to evaluate multiple attributes of visual objects to identify patterns. The participants were asked to judge the similarity among visual objects over a set of attributes specified. Most participants found graphical representations to be very helpful in pattern identification. It is easier to judge the similarity between two flowers than to remember the starting and ending dates and number of messages from a text-based interface. This may have contributed to the finding that both the Content Summary and the Interaction Summary are more effective and efficient than their textbased counterparts. However, the effectiveness of the graphical interface can be offset by the large amount of information displayed. This probably explains the lack of significant difference in effectiveness between the Expert Indicator and Netscape Messenger. A participant needed to locate visual objects on the graphical interface before the similarity comparison, and there are two ways to identify objects. He or she can use the Navigator to spot the location of visual objects of interest and click on it to obtain the details about that object on the Display panel. He or she can also scroll directly on the Display panel. Two types of scrolling are usually involved: horizontal scrolling for the desired time period and vertical scrolling for the subtopic of interest. More scrolling will be involved in locating the object as the number of objects increases. We observed that participants using the second method to locate objects had to scroll back and forth several times when using the Expert Indicator because it contained more flowers that the Interaction Summary did. Most participants made mistakes in this task because they accidentally spotted the wrong visual object. Overall, we found the Communication-Garden system to be more effective and efficient than Netscape Messenger in cluster tasks.

<table><tr><td colspan="9">Objective measures</td></tr><tr><td rowspan="2">Task type</td><td colspan="2">Content summary (C) vs. text (T)</td><td colspan="2">Interaction summary (I) vs. Text (T)</td><td colspan="2">Expert indicator (E) vs. text (T)</td><td colspan="2">Overall (G) vs. text (T)</td></tr><tr><td>Effectiveness</td><td>Efficiency</td><td>Effectiveness</td><td>Efficiency</td><td>Effectiveness</td><td>Efficiency</td><td>Effectiveness</td><td>Efficiency</td></tr><tr><td>Identify</td><td>No difference (p=0.516)</td><td>C&gt;T (p=0.000)</td><td>I&gt;T (p=0.000)</td><td>I&gt;T (p=0.000)</td><td>E&gt;T (p=0.000)</td><td>No difference (p=0.067)</td><td>G&gt;T (p=0.000)</td><td>G&gt;T (p=0.000)</td></tr><tr><td>Cluster</td><td>C&gt;T (p=0.002)</td><td>C&gt;T (p=0.000)</td><td>I&gt;T (p=0.009)</td><td>I&gt;T (p=0.000)</td><td>No difference (p=0.062)</td><td>E&gt;T (p=0.000)</td><td>G&gt;T (p=0.000)</td><td>G&gt;T (p=0.000)</td></tr><tr><td>Compare</td><td>No difference (p=0.078)</td><td>C&gt;T (p=0.000)</td><td>No difference (p=0.088)</td><td>I&gt;T (p=0.000)</td><td>E&gt;T (p=0.002)</td><td>E&gt;T (p=0.000)</td><td>No difference (p=0.076)</td><td>G&gt;T (p=0.000)</td></tr><tr><td>Rank</td><td>C&gt;T (p=0.000)</td><td>C&gt;T (p=0.000)</td><td>I&gt;T (p=0.020)</td><td>I&gt;T (p=0.000)</td><td>No difference (p=0.561)</td><td>No difference (p=0.136)</td><td>G&gt;T (p=0.000)</td><td>G&gt;T (p=0.000)</td></tr><tr><td>Correlate</td><td>No difference (p=0.156)</td><td>No difference (p=0.776)</td><td>No difference (p=0.216)</td><td>I&gt;T (p=0.030)</td><td>No difference (p=0.156)</td><td>No difference (p=0.813)</td><td>No difference (p=0.320)</td><td>No difference (p=0.148)</td></tr></table>

• Rank tasks required participants to browse all visual objects to find the extreme value. The ability to pack more information on the screen made the Communication-Garden system more effective and efficient than Netscape Messenger in rank tasks. We observed that Netscape Messenger users had to memorize values for every object in order to locate the extreme value. They got wrong answers when they felt overloaded and gave up. The graphical interface users, on the other hand, did not have to remember the attribute value of a visual object to find the extreme value. However, they may also have made mistakes when they had to scroll back and forth to spot a flower with the largest number of petals. Because a sixpetal flower was so similar to a seven-petal flower, participants sometimes made the mistake of selecting the second or the third maximum value as the maximum value, especially when flowers with the largest number and the second-largest number of petals were so apart from each other that a participant could not put them on the same screen. As a result, although we found the Content Summary and the Interaction Summary to have higher effectiveness and efficiency than text-based interfaces, no significant difference was found between the Expert Indicator and its text-based counterpart.

• Identify, compare, or correlate tasks involve only one attribute. Identify tasks requires browsing all objects to locate objects with a certain attribute value, while compare and correlate tasks involve small numbers of objects. One interesting finding regarding these task types was that differences between the graphical and the textbased interfaces in effectiveness varied with the attributes tested. When attributes (i.e., start date, number of messages of a thread) were explicitly presented in the text-based interface, no significant effectiveness difference was found between the graphical and the text-based interfaces. However, when the attributes (i.e., number of participants of a thread) were only implicit in the textbased interface, the graphical interface was significantly more effective than the text-based one. For instance, most Netscape Messenger users thought the thread displayed in Fig. 2 had four participants (the correct answer is two), while Communication-Garden users had no problem finding the correct answer by simply counting the leaves of a flower. However, the graphical users still had the problem of getting lost during scrolling when conducting these tasks. Overall results are described as follows:

o The Communication-Garden system was more effective and more efficient for identify tasks.

o The Communication-Garden system was as effective as and more efficient than Netscape Messenger for compare tasks.

o The Communication-Garden system was as effective and efficient as Netscape Messenger for correlate tasks.

The subjective measures collected indicated that the Communication-Garden system was significantly better than Netscape Messenger on perceived ease of use (p = 0.000) and perceived usefulness $\scriptstyle ( p = 0 . 0 0 0 )$ . The significant difference may have stemmed from participants' frustration using Netscape Messenger in accomplishing cluster and rank tasks (see Table 5).

## 5. Discussions and summary

Many information systems have been developed to help people gain more value from CMC archives by summarizing discussion content [5] or participants' behavior [9], recommending experts [17], and suggesting related and promising CMC communities [32]. The common goals of those researches were to enhance CMC archives' usefulness in collaboration, knowledge sharing, and community understanding. Sharing the same goals, this paper describes information needs of CMC archive users that were not well supported by previous studies. Specifically, we believe that there is a need for an information system to present the temporal changes of subtopics, depict the liveliness of thread-based discussions in each subtopic, suggest active individuals in each topic area, and describe the activeness of participants within a CMC community. The development of the Communication-Garden system demonstrates that an appropriate integration of information analysis and visualization technologies could support those information needs.

A complete validation of the Communication-Garden system may include a series of empirical studies to evaluate the effectiveness of the delivery of selected statistics or patterns, the quality of identified subtopics, and the usability and helpfulness of the developed system. Because the performance of the categorization technologies employed to identify discussion topics has been validated in several of our previous studies, we decided to validate the effectiveness of visual representation as the first step. The empirical study conducted found that the visual representations developed were effective in delivering the statistics and patterns they were designed for. The multiattribute representation not only enabled easy identification of behavior patterns but also made attributes that were only implicit in the text-based interface visually apparent to users.

Table 5  
Experiment results for the subjective measures

<table><tr><td>Interface type</td><td colspan="2">Perceived ease of use</td><td colspan="2">Perceived usefulness</td></tr><tr><td rowspan="2">Content summary (C) vs. text (T)</td><td>C=18.3</td><td>T=14.4</td><td>C=18.2</td><td>T=12.9</td></tr><tr><td colspan="2">C&gt;T (p=0.000)</td><td colspan="2">C&gt;T (p=0.000)</td></tr><tr><td rowspan="2">Interaction summary (I) vs. ext (T)</td><td>I=16.9</td><td>T=12.8</td><td>I=17.3</td><td>T=12.3</td></tr><tr><td colspan="2">I&gt;T (p=0.000)</td><td colspan="2">I&gt;T (p=0.000)</td></tr><tr><td rowspan="2">Expert indicator (E) vs. text (T)</td><td>E=17.0</td><td>T=14.4</td><td>E=17.1</td><td>T=13.5</td></tr><tr><td colspan="2">E&gt;T (p=0.000)</td><td colspan="2">E&gt;T (p=0.000)</td></tr><tr><td rowspan="2">Overall (G) vs. text (T)</td><td>G=17.4</td><td>T=13.8</td><td>G=17.5</td><td>T=12.9</td></tr><tr><td colspan="2">G&gt;T (p=0.000)</td><td colspan="2">G&gt;T (p=0.000)</td></tr></table>

However, we also feel that the proposed approach does have some limitations, as discussed below.

Although the graphical representation increased the information density on a computer screen, presenting an overview and all the details at the same time still remained impossible. Designing a meaningful navigation approach to facilitate different types of tasks is still a real challenge.

In addition, the floral representation used may have the issue of scalability. The flower of a person with thousands of messages may appear to be similar to that of a person with only hundreds of messages. In addition, on a thread flower where one petal represents one message and one leave represents one participant, a user cannot distinguish members contributing hundreds of messages from those posting only a few messages. The limitation of the floral representation could be an interesting future research. We could integrate better userinterface interaction with the floral representation to tackle the scalability issue.

We also found that using the same happy icon face for everyone in the community is another limitation of this study. As indicated in [9], certain visual representations may have unexpected emotional impact. A not-sopopular community could be perceived to be popular due to the happy faces on the interface. Adding semantics to the facial expression appears to be the solution, but needs more detailed semantic analysis of the discussion content. This creates interesting future work for us.

Finally, the proposed approach does not support the understanding of the social network aspect of a CMC community. Although messages in a discussion forum are usually broadcasted to every participant, the reply patterns could still be the source of identifying social networks in a CMC community [32]. Community members could form relationships during discussions, and comprehending such relationships clearly will help archive users better understand the community. Our future work, therefore, should integrate social network analysis techniques to further enhance the value of a CMC archive system for its users.

In addition, the “de-featuring” approach allows the easy attribution of task performance to the characteristics of the developed visual interface. Results from this study could be very helpful in refining the design of the Communication-Garden system, but provide limited evidence for adopting the developed system in the real world. Again, we are interested in expanding the work described in this paper through more evaluation studies in real-world settings.

In summary, despite the above-mentioned limitations, we still believe that the study described in this paper supports the notion that existing information analysis and visualization technologies could be combined to support the integrated comprehension of discussion content and participants' behavior. Such understanding could lead to reusing shared knowledge, identifying potential collaborators, and better understanding of CMC communities. We thus believe that the study presented in this paper is of widespread interest to researchers and practitioners. As the Internet has lead to the proliferation of computer-mediated communication, more CMC archives with huge amounts of information will be available. A better comprehension of information stored in CMC archives will greatly benefit archive users and decision-makers in organizations.

## Acknowledgements

This research was supported by

• National Science Foundation, “DLI-Phase 2: High Performance Digital Library Classification Systems: From Information Retrieval to Knowledge Management,” IIS-9817473.

• National Science Foundation, “An Intelligent CSCW Workbench: Personalized Analysis and Visualization,” ITS-9800696.

## References

[1] M.S. Ackerman, Augmenting the organizational memory: a field study of answer garden, ACM Transactions on Information Systems 16 (1998) 203–224.

[2] M.K. Ahuja, K.M. Carley, Network structure in virtual organizations, Journal of Computer-Mediated Communication 3 (1998) (http://www.ascusc.org/jcmc/vol3/issue4/ahuja.html).

[3] P.G. Anick, Vaithyanathan, Exploiting clustering and phrases for context-based information retrieval, In the 20th Annual International ACM SIGIR Conference on Research and Development, Philadelphia, PA, 1997, pp. 314–323.

[4] H. Chen, A.L. Houston, R.R. Sewell, B.R. Schatz, Internet browsing and searching: user evaluation of category map and

concept space techniques, Journal of the American Society for Information Science, Special Issue on AI Techniques for Emerging Information Systems Applications 49 (1998) 582–603.

[5] H. Chen, O. Titkova, R. Orwig, J.F. Nunmaker, Information visualization for collaborative computing, IEEE Computer 31 (1998) 75–82.

[6] H. Chen, A. Lally, B. Zhu, M. Chau, HelpfulMed: intelligent searching for medical information over the Internet, Journal of the American Society for Information Science and Technology (JASIST) 54 (7) (2003) 683–694.

[7] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (1989) 319–341.

[8] W.J. Doll, G. Torkzadeh, The measurement of end-user computing satisfaction, MIS Quarterly 12 (1998) 259–275.

[9] J. Donath, Supporting community and building social capital: a semantic approach to visualizing online conversations, Communications of the ACM 45 (4) (2002) 45–49.

[10] J. Donath, K. Karahalios, F. Viegas, Visualizing conversation, Journal of Computer-Mediated Communication 4 (1999) (http:// www.ascusc.org/jcmc/vol4/issue4/donath.html).

[11] M. Graham, J. Kennedy, C. Hand, A comparison of set-based and graph-based visualizations, International Journal of Human– computer Studies 53 (2000) 789–807.

[12] T. Honkela, S. Kaski, K. Lagus, T. Kohonen, Newsgroup exploration with WEBSOM method and browsing interface, Laboratory of Computer and Information Science, Espoo, Technical Report, vol. A32, Helsinki University of Technology, Finland, 1996.

[13] J.A. Konstan, B.N. Miller, D. Maltz, J.L. Herlocker, L.R. Gordon, J.T. Riedl, GroupLens: applying collaborative filtering to Usenet news, Communications of the ACM 40 (1997) 77–87.

[14] T. Kohonen, Self-organized Maps, Chapter 3, Springer-Verlag, Berlin Heidelberg, 1995.

[15] M. Lea, R. Spears, Computer-mediated communication, deindividualization, and group decision-making, in: S. Greenberg (Ed.), Computer-supported cooperative work and groupware, Academic Press, London, 1991, pp. 153–173.

[16] R.P. Lippmann, An introduction to computing with neural networks, IEEE Acoustics Speech and Signal Processing Magazine 4 (1987) 4–22.

[17] D.W. McDonald, M.S. Ackerman, Expertise recommender: a flexible recommendation system and architecture, Proceedings of ACM Conference on Computer-Supported Cooperative Work (CSCW'00), Philadelphia, PA, 2000, pp. 231–240.

[18] R. Mikkulainen, Subsymbolic Natural Language Processing: An Integrated Model of Scripts, Lexicon, and Memory, The MIT Press, Cambridge MA, 1993.

[19] E. Morse, M. Lewis, Evaluating visualizations: using a taxonomic guide, International Journal of Human–computer Studies 53 (2000) 637–662.

[20] B.A. Nardi, S. Whittaker, E. Isaacs, M. Creech, J. Johnson, J. Hainsworth, Integrating communication and information through ContactMap, Communications of ACM 45 (4) (2002) 89–95.

[21] I. Nonaka, N. Konno, The concept of ‘Ba’: building a foundation for knowledge creation, California Management Review 40 (1998) 40–55.

[22] C. North, B. Shneiderman, Snap-together visualization: can users construct and operate coordinated visualizations? International Journal of Human–computer Studies 53 (2000) 715–739.

[23] J.F. Nunamaker, A.R. Dennis, J.S. Valacich, D.R. Vogel, J.F. George, Electronic meeting systems to support group work, Communications of the ACM 34 (1991) 40–61.

[24] H. Ogata, Y. Yano, N. Furugori, Q. Jin, Computer supported social networking for augmenting cooperation, Computer Supported Cooperation Work: The Journal of Collaborative Computing 10 (2001) 189–209.

[25] D. O'Leary, Knowledge management systems: converting and connecting, IEEE Intelligent Systems (May/June 1998).

[26] M. Pohl, P. Purgathofer, Hypertext authoring and visualization, International Journal of Human–computer Studies 53 (2000) 809–825.

[27] K. Risden, M.P. Caerwinski, T. Munsner, D.D. Cook, An initial examination of ease of use for 2D and 3D information visualizations of web content, International Journal of Human–computer Studies 53 (2000) 695–714.

[28] D. Rosen, J. Woelfel, D. Krikorian, G. Barnett, Procedures for analyses of online communities, Journal of Computer-Mediated Communication 8 (4) (2003) (http://jcmc.indiana.edu/vol8/issue4 rosen.html).

[29] W. Sack, Conversation map: an interface for very large-scale conversations, Journal of Management Information Systems 17 (3) (2000) 73–92.

[30] G. Salton, M.J. McGill, Introduction to modern information retrieval, McGraw Hill Computer Science Series (1983).

[31] A. Smith, Human–computer Factors: A Study of Users and Information Systems, McGraw-Hill, New York, 1997.

[32] M.A. Smith, A.T. Fiore, Visualization components for persistent conversations, Proceedings of ACM Conference on Human Factors in Computing Systems (CHI 2001), 2001, pp. 65–72.

[33] L. Sproull, S. Kiesler, Computers, network, and work, Scientific American 265 (1991) 116–127.

[34] J. Stasko, R. Catrambone, M. Guzdial, K. McDonald, An evaluation of space-filling information visualizations for depicting hierarchical structures, International Journal of Human–computer Studies 53 (2000) 663–695.

[35] K.M. Tolle, H. Chen, Comparing noun phrasing techniques for use with medical digital library tools, Journal of the American Society for Information Science 51 (2000) 352–370.

[36] T.C. Turner, M.A. Smith, D. Fisher, H.T. Welser, Picturing Usenet: mapping computer-mediated collective action, Journal of Computer-Mediated Communication 10 (4) (2005) (article 7), (http://jcmc.indiana.edu/vol10/issue4/turner.html).

[37] N.W. Van Dyke, H. Lieberman, P. Maes, Butterfly: a conversation-finding agent for internet relay chat, Proceedings of the 1999 International Conference on Intelligent User Interfaces, Redondo Beach: CA, 1999, pp. 629–644.

[38] S.P. Weisband, S.K. Schneider, T. Connolly, Computer-mediated communication and social information: status salience and status differences, Academy of Management Journal 38 (1995) 1124–1151.

[39] S. Wehrend, C. Lewis, A problem-oriented classification of visualization techniques, Proceedings of IEEE Visualization 90 (1990) 139–143.

[40] S. Whittaker, Q. Jones, L. Terveen, Managing long term communications: conversation and contact management, Proceedings of the 35th Annual Hawaii International Conference on System Sciences, IEEE, Big Island, Hawaii, 2002.

[41] R. Xiong, J. Donath, Creating data portraits for users, Proceedings of the 12th annual ACM symposium on User Interface Software and Technology, 1999, pp. 37–44.

[42] M.X. Zhou, S.K. Feiner, Visual task characterization for automated visual discourse synthesis, Proceedings of ACM SIGCHI 98 (1998) 392–399.

[43] B. Zhu, H. Chen, Validating a geographical image retrieval system, Journal of the American Society for Information Science 51 (7) (2000) 625–634.

[44] B. Zhu, H. Chen, Information visualization, Annual Review of Information Science and Technology (ARIST) 39 (2005).

Dr. Bin Zhu received her PhD degree in Management Information Systems from the University of Arizona in 2002. She is an assistant professor in the Information Systems department at Boston University. Her current research interests include human–computer interaction, information visualization, computer-mediated communication, and knowledge management systems. She has been a lead author for papers that have appeared in Decision Support Systems, the Journal of the American Society for Information Science and Technology, IEEE Transaction on Image Processing, and D-Lib Magazine. Her research also received an IBM faculty award in 2003.

Dr. Hsinchun Chen is the McClelland Professor of Management Information Systems and Andersen Professor of MIS at the University of Arizona, where he is the director of the Artificial Intelligence Lab and the director of the Hoffman E-Commerce Lab. He received his PhD degree in Information Systems from New York University in 1989. His articles have appeared in Communications of ACM, ACM Transactions on Information Systems, IEEE Computer, Journal of the American Society for Information Science and Technology, Decision Support Systems, and many other journals. Professor Chen has received grant awards from NSF, DARPA, NASA, NIH, NIJ, NLM, NCSA, HP, SAP, 3COM, and AT&T. He serves on the editorial board of Decision Support Systems, Journal of American Society for Information Science and Technology, and ACM Transactions on Information System.
