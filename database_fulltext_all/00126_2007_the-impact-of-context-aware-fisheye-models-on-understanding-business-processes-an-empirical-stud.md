---
otero_id: 126
otero_key: "MKYSKVBC"
title: "The impact of context-aware fisheye models on understanding business processes: An empirical study of data flow diagrams"
authors: "Ozgur Turetken; David Schuff"
year: "2007"
journal: "Information & Management"
doi: "10.1016/j.im.2006.10.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of context-aware fisheye models on understanding business processes: An empirical study of data flow diagrams

Ozgur Turetken <sup>a,\*</sup>, David Schuff <sup>b</sup>

<sup>a</sup> School of Information Technology Management, Ryerson University, Toronto, Ont. M5G 2C5, Canada <sup>b</sup> Fox School of Business and Management, Temple University, Philadelphia, PA 19122, United States

Received 22 April 2005; received in revised form 18 August 2006; accepted 7 October 2006

Available online 13 November 2006

## Abstract

We investigated whether a ‘‘context-aware’’ fisheye view can more successfully communicate the information contained in a set of process models (data flow diagrams) than a traditional ‘‘context-free’’ presentation. We conducted two controlled experiments: the first included a simple set of DFDs and tasks that required a basic understanding of the system, while the second involved more detailed views of the same processes, and also a more complex task. Subjects who used the fisheye process models outperformed those using the traditional presentations. This difference was reflected in task performance for all subjects, and in task completion time for inexperienced subjects.

<sup>#</sup> 2006 Elsevier B.V. All rights reserved.

Keywords: User interface; Information visualization; Process modeling; Business process redesign; Process improvement; End-user computing; Laboratory experiments; Theory verification; ANOVA

## 1. Introduction

Business processes were defined by Davenport and Short [8] as ‘‘a set of logically related tasks performed to achieve a desired business outcome;’’ they are the building blocks of a business system. Once those processes are understood, they can be improved or radically redesigned in order to improve an organization’s productivity [18]. Thus representing processes by means of easily understandable models is essential.

The process models to represent complex systems can also become complex. In such cases, multiple interrelated diagrams are often used [22]. Human capacity for simultaneously processing multiple pieces of information is limited [28,29]. Therefore, an effort to simultaneously explore all relevant business processes in detail would create a quantity of information that cannot be processed easily: an information overload.

To avoid this, process models are simplified into levels, depending on the degree of detail. For models representing nontrivial systems, there will be several levels, and the viewers of these diagrams must integrate context and details while switching back and forth between levels. Such integration is not easy and may cause disorientation with viewers feeling lost. System analysts are therefore faced with a dilemma: one option is the creation of a single comprehensive model, while the other is the creation of separate models representing different parts of the overall system, possibly causing confusion when switching between diagrams at different levels of detail. According to Kim et al., this effect complicates the cognitive processes in integrating these diagrams to understand the system as a whole.

This dilemma is not unique to process models. For example, while browsing hypertext, the user can become confused about the link structure between nodes and how one leads to another. This phenomenon has been called ‘‘lost in hyperspace’’ [6,31] and presentations of web sites that provide better integration of context and details have been shown to be more successful [5]. Similarly, Schafer et al. [33] found that context clues improved viewers’ performance when navigating and rerouting the links of a simulated telephone network. We suggest that process models would be more useful if they had ‘‘context-aware’’ features so that the diagrams were organized to integrate context and details smoothly. The fisheye view concept introduced by Furnas [10] seemed particularly promising. It has been applied to graphical presentations of hierarchies for groupware [16], hypertext [9], and search on the World Wide Web [41]. Turetken et al. [40] and Turetken and Schuff [39] proposed the use of fisheye views with systems analysis and design diagrams. Specifically, the data flow diagram (DFD) is a good process model for such a visualization technique because of its strong hierarchical structure and due to the fact that it is a classic tool for process analysis. Accordingly, our research question is:

Can the presentation of Data Flow Diagrams (DFDs) through fisheye views convey the business processes that they represent more successfully than the standard presentation of such diagrams?

## 2. Background

## 2.1. The role of context in understanding details

Gestalt theory can be used to explain visual cognition of a system. One applicable gestalt principle states that details have more meaning when presented within their context [42]. This theory has implications for IS. Gottschalk [13] states that a gestalt approach is essential in IS planning. We believe that, in addition to guiding the general approach to system development, the implications of gestalt theory are important in constructing diagrammatic representations (such as process models) since it has implications for information visualization [21]. Tan and Benbasat [37] examined two aspects. Proximity assumes that items closer together will be perceived as part of a group and therefore related while continuity is enforced through lines connecting items. Those elements that are directly connected are understood to be more closely related than those that are not. Smelcer and Carmel [34] introduced similar concepts of adjacency and containment, where the first occurs when the entities are touching and the second when one entity is placed within another.

## 2.2. Fisheye views

According to Furnas, an efficient way of embedding a piece of information in its context is to represent the portions that are closer to the area of interest in more detail while including only a grouping of those further away. These ‘‘fisheye views’’ are created by using the concept of degree of interest (DOI): a function of the initial importance of a visual element and its distance from the current view. Thus the DOI decreases as the distance from the focus increases.

Using variants of this concept, fisheye views can be defined in a number of different structures [24]. Furnas demonstrated its use for tree structures and treestructured text files. Sarkar and Brown [32] applied the fisheye view in browsing computer graphs. Bederson [4] developed fisheye menus as an alternative to the traditional hierarchical view and found that this technique was preferred by users for general browsing, but that hierarchical menus were preferred for goaldirected tasks. The FISPA system applied a variant of fisheye views to visualizations (zoomable treemaps) of clustered web search results. In controlled experiments, the fisheye zoom version of FISPA resulted in speed improvements over the list-based presentations and zoomable treemap without fisheye zooms.

Lamping and Rao [23] described an implementation for presenting a two-dimensional graph using a fisheye zoom. The hyperbolic browser provided a smoothly varying ‘‘focus plus context’’ view where the display space allocated to a node decreased continuously with the distance from the focus, yet did not disappear abruptly. Inxight ’s ‘‘Hyperbolic Tree’’ [19], as well as Sarkar and Brown’s work at Xerox Parc are well known and successfully commercialized applications of the fisheye view. Display of a specific node in the graph within the context of the other nodes is shown in Fig. 1. Fig. 2 shows the effect of carrying a node to the focus. The integration of details within context through such a distortion method proves to be a good way of looking at those details without losing the overall picture.

However, empirical studies of fisheye views do not always give evidence of their usability. Skopik and Gutwin [35] found that the degree of visual distortion in a fisheye view of a network hindered the users’ ability to remember the nodes they visited.

![](/api/attachments/MKYSKVBC/fulltext/images/f3f664de141d7bcfcc89dac0637895b1b13a95f1665275263373106aeac7fc56.jpg)  
Fig. 1. A hierarchically-arranged chart of product lines.

## 3. Research methodology

## 3.1. Presentation of business processes

We choose data flow diagrams (DFDs) to represent business processes in an organization because this technique is (1) strongly hierarchical so that the context is readily available and (2) commonly used and thus was familiar to our research subjects. Accordingly, details can be included in a single drawing of higher level processes (providing context) using the fisheye view technique. Also DFDs remain a useful tool for business process improvement and redesign. Probably users will be more effective in modeling process-oriented tasks using DFDs because there is a greater cognitive fit between tool and task [1]. This fit between tool and task is important—Yang [44] found that the successful adoption and implementations of CASE tools depended upon the ability of the tool to support the organization’s prevailing development methodology. Hahn and Kim [17] argued that a good diagram ‘‘supports the cognitive processes effectively.’’

![](/api/attachments/MKYSKVBC/fulltext/images/401ccbe94ec3e0050ffdb8e7288bc79ad127d68c324db13217319405b96a518c.jpg)  
Fig. 2. Changing focus of the chart in Fig. 1.

There are four main components to a DFD: processes, data flows, data stores, and external entities. Fig. 3 gives symbols for these.

The creation of a fisheye diagram involves determining the size and position of its graphical elements; the basic principle does not dictate position and there are no rules to determine the location and relative position of the elements. However, we used the principles of proximity and continuity to guide the general placement of elements. Specifically, we felt that effective fisheye representations of DFDs would need expansion of a portion of a higher-level diagram without causing confusion to the rest of the display. To implement this, we adopted a variation of the variable zoom approach used by Schafer et al. The allowed us to embed a lowerlevel process diagram within its parent.

We also adhered to the proximity principle by designing the layout of the diagrams so that the expandable parts (the process representations) were located towards the center of the diagram and when a process is expanded, its details are placed as close as possible to one another. These details are also placed as close as possible to their original position before expansion. Similarly, the external entities and data stores were placed approximately where they were in the level-0 diagram. This heuristic allowed us to create a fisheye version of the diagrams and reduced differences between the presentation of details in the fisheye and standard representations. Other than contextual clues, the fisheye version had an identical appearance to the standard version.

![](/api/attachments/MKYSKVBC/fulltext/images/9cc413ebd267fbd7253d80386b03a6dd62e76ce2320c5d04b2566655dc13bc84.jpg)  
Fig. 3. Data flow diagram symbols.

Our second heuristic determined the size of elements in the ‘‘zooming in’’ processes. The original fisheye concept was based on degree of interest, which is a function of the initial importance of an element and its distance from the current focus. The size of a graphical element was also a function of its degree of interest. However, as Sarkar and Brown pointed out, the traditional notion of distance does not always apply when visualizing networks of entities, and has to be reconsidered. In standard DFDs, the distance between elements has no significance. Thus, the size of the elements in the fisheye representations of DFDs cannot be based on standard distance measures. However, the elements that have data flows between them are more closely associated than those with no flows between them. We therefore defined items that exchanged data directly as being zero units of distance away from the focus. If an element exchanged data with them (but not the elements in focus), it was given one unit away from the focus. Elements that exchanged data with them were considered as two units away, and so on. Thus, items further away from the focus were of less interest and were smaller in the diagram. For the purposes of our study, we reduced the size of an element by about a half for each unit of distance from the focus. The result is that the largest differences between the sizes of the elements can be seen within the first few units of distance. We assumed that the initial levels of importance of all elements were equal. This approach is consistent with design principles suggested by Abello et al. and Heer and Card.

## 3.2. Hypotheses

Our assertion is that the fisheye views of the DFDs will be more successful than traditional views. The key feature of fisheye presentations is the embedding of the details of the process within their context. This provides greater continuity between details and context than traditional representations. The fisheye representations accomplish this by showing elements directly connected to the elements of an expanded subprocess as well as the elements connected to those directly connected elements. Proximity is incorporated into the diagram by the physically close placement of the subprocess.

Consequently, the users of these views would have a better understanding of the business processes of those diagrams. Our main assumption was that this would lead to more effective analysis of a system in less time. These variables have been used previously as major outcomes of success in presentation of information [26,38], and have been applied to the evaluation of fisheye visualizations in other domains.

Most studies have found that a better method of presentation led to speed improvements, but not higher task success. Todd and Benbasat suggested a possible reason: when decision makers have access to better tools they tend to emphasize speed over task success. Therefore people’s natural behavior, given superior tools, would be to complete a task more quickly without an improvement in quality. However, reinforcing certain behavior can influence a person’s tendencies. For example, if subjects are aware that there is plenty of time but that the quality of their outcome is important, they are likely to achieve a higher level of task success without speed improvement.

We therefore developed two hypotheses:

Hypothesis 1. Subjects who use fisheye visualization will receive a higher score for task success than those who use the traditional presentation.

Hypothesis 2. Subjects who use fisheye visualization will complete the experimental task sooner than those who use a traditional presentation.

## 4. Study one

## 4.1. Presentation of process models

We created ‘‘context-aware’’ process models by applying our heuristics to a set of DFDs. To create a testable implementation, we developed an HTMLbased navigation tool. The tool was used to display a complete DFD for a hypothetical video store business. In order to compare the success of fisheye representations of DFDs to that of traditional context-free diagrams, two sets of diagrams were created: one had a set of separate subprocess DFDs without any information about their context in the rest of the system (the higher levels), while the second set provided each subprocess DFD in a fisheye diagram in which contextual information from the higher levels was included.

![](/api/attachments/MKYSKVBC/fulltext/images/f4996531b4aa0526658db550ca6adc9b74073d45cf67770f529531dc0bf97189.jpg)  
Fig. 4. The level-0 diagram.

The starting point for the user of the system is a diagram of the highest level processes (see Fig. 4); this is a ‘‘clickable’’ hypertext page. For four of the five subprocesses (1, 2, 4, and 5), clicking on a subprocess takes the user to the DFD for that subprocess (a level-1 diagram). Depending on the version of the tool, the model was either the standard (see Fig. 5) or fisheye version (see Fig. 6). The user could then navigate between different levels of the diagrams. The fisheye version incorporated the subprocess and details of its context.

## 4.2. Experimental procedure

Our experiment was conducted with 52 undergraduate and graduate Management Information Systems students in a large northeastern university in the USA. Most reasons against the use of student subjects for data collection are based on the premise that they are not representative of the assumed population; in this case, business managers [14]. However, our task was a systems analysis and design exercise (not managerial), and therefore our target population is system analysts. We therefore believed that students with process modeling experience (although at varying levels) were appropriate subjects for our study. Fifty-five percent of the sample was male and the average age was 22.9. Students were given an incentive of extra credit for their participation.

The experimental design was a two group between subjects design. The subjects were randomly assigned to one of the groups; both used the HTML navigation tool to allow them to click on a process to reveal detail. The first group used the traditional presentation of DFDs, a series of separate views. The second used a version containing fisheye presentations of the subprocesses. Subjects were given instructions explaining how to use the navigation tool without revealing the group to which they were assigned.

Gemino and Wand [12] discussed three categories of variables that affected the outcome of a user’s interaction with a diagram: content, presentation method, and user characteristics. Since the focus of our study was the presentation, we controlled for the other two categories. Thus the content, tasks to be performed, and training given was identical for each subject.

![](/api/attachments/MKYSKVBC/fulltext/images/7f034c8585518f948ed2d4d2cb5d51f1334d39f3bbc8f6977f5fb651dff6a07d.jpg)  
Fig. 5. Viewing the details of process 4 separately from the context.

We statistically controlled for user characteristics by measuring cognitive styles, which might affect a subject’s use of an IS [2,3,7,15]. Specifically, field dependence, an individual’s ability to find a detail within a larger context, has been examined as a potential moderator of success in visually oriented IS [25,30]. Field dependence was particularly relevant for us, because the two different presentations included different degrees of contextual information. We measured this aspect of cognitive style using the Embedded Figures Test [43], which requires subjects to find a specific shape within a larger figure.

Similarly, to control for the effects of prior experience on task performance, we collected information about the subjects’ experience with DFDs; subjects were asked how long they had worked with DFDs. Galletta et al. [11] proposed two types of experience that may have an influence on task performance: domain and device experience. The information we collected on experience in using DFDs was closely related to device experience. It is also likely that the student subject population had a homogenous level of familiarity with the problem domain (as discussed later). In order to minimize differences between the subjects’ capability in using the tools, we provided a brief tutorial about the symbols of a DFD, how the diagrams are read, and how to use the HTML-based tool.

## 4.3. Experimental tasks and data collection

Subjects were presented with one of the two presentations of the business processes of a hypothetical video rental store. They were then given three typical business transactions handled by the system, and asked to describe the events that would occur during these transactions (for example, ‘‘What happens when a movie is returned late?’’). The transactions were specifically chosen because they spanned multiple subprocesses. This forced the subjects to navigate the DFD using the tool and not simply to rely on the level-0 diagram. The subjects were given 25 minutes to record all the events they could find that were involved in the three transactions.

![](/api/attachments/MKYSKVBC/fulltext/images/117cf3d7f0094816d25e0e1066a0b729f788bea379dd33ffa5fe4b470952d441.jpg)  
Fig. 6. Viewing the details of process 4 by means of a fisheye view.

When the subjects completed the task, they were asked to write down their reactions to the way that the DFDs were presented. Specifically, they were asked to address whether the diagrams were helpful in aiding their work on the task. This data was collected to provide additional insight into the meaning of the results.

The authors, blind to the presentation method subjects received, compared the list of events with a list of ‘‘ideal’’ responses. This made the scoring as objective as possible since the coding assessed discrete elements rather than an overall assessment thus minimizing any judgment required. Because a different number of events were associated with each of the three questions, the overall scores for each question were adjusted so that they were weighted equally.

## 4.4. Data analysis and results

We used ANOVA to analyze the data (after verifying the normality and equality of variance-covariance matrices across groups). The method of presentation was used as the independent variable with score and then time as dependent variables. Cognitive style and experience were other factors used as control variables. Because there was no significant relation between the dependent variables score and time $( r = 0 . 1 2 , p = 0 . 4 4 )$ performing two separate ANOVAs instead of a single MANOVA is appropriate.

Table 1 shows the results of the ANOVA for Hypothesis 1. There is no significant interaction between the presentation method and any of the other between-subjects factors; therefore we can interpret the individual effects of presentation method directly. The effect of presentation method was significant at the 0.05 level, and in the hypothesized direction (score-$\mathrm { \ p s h e y e } = 1 2 9 > \mathrm { s c o r e } _ { \mathrm { w i t h o u t \ f i s h e y e } } = 1 2 1 )$ , therefore providing marginal support for our hypothesis.

Test of Hypothesis 1—effects of independent variables on score

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Presentation method</td><td>1</td><td>4.1</td><td>0.05</td></tr><tr><td>DFD experience</td><td>3</td><td>1.5</td><td>0.24</td></tr><tr><td>Cognitive style</td><td>3</td><td>2.0</td><td>0.14</td></tr><tr><td>Presentation method × DFD experience</td><td>2</td><td>2.2</td><td>0.14</td></tr><tr><td>Presentation method × cognitive style</td><td>3</td><td>1.3</td><td>0.31</td></tr><tr><td>DFD experience × cognitive style</td><td>6</td><td>4.6</td><td>0.00</td></tr><tr><td>Presentation method × DFD experience × cognitive style</td><td>1</td><td>1.1</td><td>0.30</td></tr></table>

R<sup>2</sup> = 0.63 (adjusted R<sup>2</sup> = 0.36).

Table 2  
Test of Hypothesis 2—effects of independent variables on time

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Presentation method</td><td>1</td><td>0.16</td><td>0.69</td></tr><tr><td>DFD experience</td><td>3</td><td>0.36</td><td>0.79</td></tr><tr><td>Cognitive style</td><td>3</td><td>1.4</td><td>0.26</td></tr><tr><td>Presentation method × DFD experience</td><td>2</td><td>0.90</td><td>0.42</td></tr><tr><td>Presentation method × cognitive style</td><td>3</td><td>0.82</td><td>0.50</td></tr><tr><td>DFD experience × cognitive style</td><td>6</td><td>0.27</td><td>0.95</td></tr><tr><td>Presentation method × DFD experience × cognitive style</td><td>1</td><td>0.05</td><td>0.83</td></tr></table>

R<sup>2</sup> = 0.32 (adjusted $R ^ { 2 } = 0 . 2 9 )$ ).

The second ANOVA was used to test Hypothesis 2 with the same independent variables and time as the dependent variable. Table 2 gives the results which showed that there was no significant main or interaction effect. Therefore we fail to find empirical support for our second hypothesis.

There are two limitations of our first study. First, the presentation system only expanded processes one level deep. For example, subprocess 1.1 could not be expanded to view its subprocesses (1.1.1, etc.). This was intended to create a simple system that could be used as a ‘‘proof of concept.’’ Although we believed that the system was sufficient to demonstrate the basic effectiveness of the presentation method, this limitation prevented it from accurately modeling a complex organization. The second limitation concerned the relative simplicity of the task. Subjects were required to describe key processes based on a DFD. While this allowed us to test basic comprehension of the processes that were represented, typical real analysis tasks expect the user to recommend improvements in the process and integration of new processes into the existing system. To address these limitations, we modified the data flow diagrams, the presentation tool, and the experimental task, and conducted a second study.

![](/api/attachments/MKYSKVBC/fulltext/images/f0b47d136c5fefbdfaa960aa72d9c66029717e6caa2b96a1629fafbdc6249df1.jpg)  
Fig. 7. Viewing the details of process 2.2 by means of a fisheye view.

## 5. Study two

## 5.1. Presentation of process models

We developed an enhanced version of the tool. It had a different user interface and a more complex version of the DFDs. The diagrams involved three levels of process details instead of two. The new interface was built using Adobe System’s Macromedia Flash so that transitions between the context and the detail could be animated. These transitions (which lasted a little under one second) were used to show the relationship between the unexpanded and expanded versions of the processes. As in our first study, four of the five level-0 processes were still expandable. Also two of the level-1 processes (1.1 and 2.2) were made expandable into their corresponding level-2 diagrams. An example of the fisheye version of level-2 process is shown in Fig. 7.

## 5.2. Experimental procedure

The second experiment used 50 undergraduate MIS majors. They had not participated in the first study. Fifty-two percent were male, and the average age was 22.5. Extra credit was offered as an incentive.

We again used a two group between subjects design with subjects randomly assigned to one of the groups. Both sets used the animated navigation tool, with one using traditional diagrams and the other fisheye diagrams. As in the first study, the subjects were given a short tutorial on how to interpret the symbols and use the tool. Their experience level with DFDs and cognitive style were again used as control variables.

## 5.3. Experimental tasks and data collection

The problem domain was the same but the experimental task was more complex. This new task required subjects to augment the set of business process and incorporate the new processes into the existing DFDs. The scenario was to incorporate a ‘‘pay in advance’’ rental service and a notification service to customers when promotions were offered. Since this was a more realistic task, it was expected to better test the subjects’ use of the diagrams. Participants had 35 minutes to complete the task and were asked to provide written feedback on the way the models helped them.

Because of the open-ended nature of this task, it was difficult to assess whether an answer should be considered correct. Therefore, three coders evaluated the responses based on whether the solution came close to an ‘‘ideal’’ response. The coders were given this answer and a list of key elements that subjects should have included. Coders rated each element from 1 (completely incorrect or missing) to 5 (completely correct). Based on this, subjects received a score from each coder. To assess inter-rater reliability, we verified that the Pearson correlation coefficients between them were at acceptable levels (see Table 3). Accordingly, scores from different raters were averaged to obtain a single score for each subject on each task.

Table 3  
Inter-rater reliability assessment—correlations for the task scores

<table><tr><td></td><td>Rater 1</td><td>Rater 2</td><td>Rater 3</td></tr><tr><td colspan="4">Rater 1</td></tr><tr><td>Pearson correlation</td><td>1</td><td>0.56*</td><td>0.67*</td></tr><tr><td>Significance (two-tailed)</td><td></td><td>0.001</td><td>0.00</td></tr><tr><td>N</td><td>31</td><td>31</td><td>31</td></tr><tr><td colspan="4">Rater 2</td></tr><tr><td>Pearson correlation</td><td>0.56*</td><td>1</td><td>0.60*</td></tr><tr><td>Significance (two-tailed)</td><td>0.001</td><td>.</td><td>0.00</td></tr><tr><td>N</td><td>31</td><td>31</td><td>31</td></tr><tr><td colspan="4">Rater 3</td></tr><tr><td>Pearson correlation</td><td>0.67*</td><td>0.60*</td><td>1</td></tr><tr><td>Significance (two-tailed)</td><td>0.00</td><td>0.00</td><td>.</td></tr><tr><td>N</td><td>31</td><td>31</td><td>31</td></tr></table>

Correlation is significant at the 0.01 level (two-tailed)

## 5.4. Data analysis and results

As in the first study, two ANOVAs were performed with the method of presentation as the independent variable. Cognitive style and experience with DFDs were additional factors again used as controls. The ANOVA assumptions were verified, and two separate ANOVAs were chosen instead of one MANOVA, since there was no significant correlation between the dependent variables score and time $( r = - 0 . 0 9 , p = 0 . 6 1 )$ ).

Table 4 gives the results of the ANOVA test for Hypothesis 1; the effect of the presentation method was significant $( p < 0 . 0 1 )$ , which suggested that subjects generally performed slightly better with the fisheye DFDs $( \mathrm { s c o r e } _ { \mathrm { f i s h e y e } } = 2 8 > \mathrm { s c o r e } _ { \mathrm { t r a d i t i o n a l } } = 2 6 )$ However, with a significant interaction effect, reliance solely on direct effects can lead to an incomplete (and potentially misleading) analysis. Since our analysis showed a significant interaction between presentation method and cognitive style $( p < 0 . 0 1 )$ , the effect of presentation method was different for subjects with differing field dependence. Therefore, to gain better insight, we further analyzed this interaction by graphing the change in score for each presentation method as a function of cognitive style (see Fig. 8). Four levels of style were created based on natural divisions in the raw field dependence scores from the Group Embedded Figures Test (GEFT). The interaction diagram suggested that subjects with a higher level of field dependence were more successful with fisheye DFDs while field independent subjects were slightly more successful with traditional diagrams.

Table 4  
Test of Hypothesis 1—effects of independent variables on score

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Presentation method</td><td>1</td><td>12</td><td>0.00</td></tr><tr><td>DFD experience</td><td>3</td><td>2.5</td><td>0.08</td></tr><tr><td>Cognitive style</td><td>3</td><td>10</td><td>0.00</td></tr><tr><td>Presentation method × DFD experience</td><td>3</td><td>1.1</td><td>0.39</td></tr><tr><td>Presentation method × cognitive style</td><td>3</td><td>12</td><td>0.00</td></tr><tr><td>DFD experience × cognitive style</td><td>7</td><td>4.9</td><td>0.00</td></tr><tr><td>Presentation method × DFD experience × cognitive style</td><td>1</td><td>3.7</td><td>0.06</td></tr></table>

R<sup>2</sup> = 0.80 (adjusted $R ^ { 2 } = 0 . 6 5 )$

![](/api/attachments/MKYSKVBC/fulltext/images/ac80583e5547f25ff8426797639e115161164a818efe38c22fb48dd15829fa49.jpg)  
Fig. 8. Interaction diagram–cognitive style and score by group.

Based on this observation, we split the data set into two subsamples. We compared the effect of the presentation method separately for each of these using a one-way ANOVA. As shown in Table 5, the effect of the presentation method was significant $( p = 0 . 0 1 )$ for field dependent subjects only. This provided support for our contention that those individuals who are more field independent benefited less from using a fisheye view, performing worse than those with the same level of field independence but given the traditional diagrams. Among the more field dependent individuals, performance was better with the fisheye view. An interesting (and puzzling) finding is that the benefits of the fisheye view appear to diminish significantly for those subjects who are very field dependent (the difference is larger for those subjects who are moderately field dependent).

Table 5  
Test of Hypothesis 1—effect of presentation method on score

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Field dependent subjects Presentation method</td><td>1</td><td>9.5</td><td>0.01</td></tr><tr><td>Field independent subjects Presentation method</td><td>1</td><td>1.5</td><td>0.22</td></tr></table>

$R ^ { 2 } = 0 . 2 8$ (adjusted $R ^ { 2 } = 0 . 2 5 )$ . $R ^ { 2 } = 0 . 0 7$ (adjusted $R ^ { 2 } = 0 . 0 2 )$

Table 6  
Test of Hypothesis 2—effects of independent variables on time

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Presentation method</td><td>1</td><td>2.0</td><td>0.16</td></tr><tr><td>DFD experience</td><td>3</td><td>4.5</td><td>0.01</td></tr><tr><td>Cognitive style</td><td>3</td><td>3.2</td><td>0.04</td></tr><tr><td>Presentation method × DFD experience</td><td>3</td><td>3.0</td><td>0.05</td></tr><tr><td>Presentation method × cognitive style</td><td>3</td><td>1.2</td><td>0.33</td></tr><tr><td>DFD experience × cognitive style</td><td>7</td><td>3.1</td><td>0.02</td></tr><tr><td>Presentation method × DFD experience × cognitive style</td><td>1</td><td>3.6</td><td>0.07</td></tr></table>

$R ^ { 2 } = 0 . 6 8$ (adjusted $R ^ { 2 } = 0 . 4 3 )$

Another ANOVA was used to test Hypothesis 2 with the method of presentation as the independent variable and time as the dependent variable. As in the test of Hypothesis 1, cognitive style and experience with DFDs were used as control variables. Table 6 suggested that the direct effect of presentation method on time was not significant. However, as in the test of Hypothesis 1, there was a significant interaction effect, this time between presentation method and DFD experience $( p = 0 . 0 5 )$ Again, to gain better insight we charted the change in task completion time for each presentation method as a function of DFD experience (see Fig. 9).

The chart suggested that presentation method made a difference for subjects with either very low or very high levels of experience. Both subjects that were very inexperienced or very experienced completed the tasks faster with fisheye DFDs while for the middle levels of experience, presentation method had little effect on speed. We therefore created two subsamples, one for the very inexperienced and one for the very experienced subjects. We compared the effect of the presentation method separately for each of these with a one-way ANOVA. As shown in Table 7, the effect of the presentation method was strongly significant $( p < 0 . 0 1 )$ for very inexperienced subjects only.

![](/api/attachments/MKYSKVBC/fulltext/images/621dc6c5b02a0a8e4bf8b0203384a8f181e6ba5e81df7badabed787591735518.jpg)  
Fig. 9. Interaction diagram–DFD experience and task completion time by group.

Table 7  
Test of Hypothesis 2—effect of presentation method on time

<table><tr><td>Variable</td><td>d.f.</td><td>F</td><td>p</td></tr><tr><td>Very inexperienced subjects Presentation method</td><td>1</td><td>15</td><td>0.00</td></tr><tr><td>Very experienced subjects Presentation method</td><td>1</td><td>1.8</td><td>0.21</td></tr></table>

$R ^ { 2 } = 0 . 4 1$ (adjusted $R ^ { 2 } = 0 . 3 8 )$ $R ^ { 2 } = 0 . 1 7$ (adjusted $R ^ { 2 } = 0 . 0 7 5 )$

## 6. Discussion and conclusions

## 6.1. Overview

Our study introduced fisheye DFDs as context-aware representations of an organization’s business processes. We created and tested two sets of DFDs, and found promise in their use in understanding business processes. In our first study, we found support for our hypothesis that the use of the fisheye views enabled subjects to understand business processes more completely.

Our second study provided additional insights into fisheye process models and their effect on task score and completion time. First, fisheye models appear to be most effective at improving understanding when subjects are field dependent. Second, the fisheye models appear to be most effective at improving task completion time when subjects are inexperienced. This would imply that the fisheye models may be most effective with novice users.

Both of our experiments were conducted with samples of moderate sizes. The fact that we found some highly significant results suggests that the effect size (i.e., the contribution of fisheye views to understanding of the modeled system) is very large. The findings also suggest that it is possible to gain simultaneous performance and speed improvements; therefore it is reasonable to try to achieve both effects in visual interface development and testing.

Qualitative evidence that was collected appeared to support these findings. Some subjects who were given the fisheye version responded with comments that specifically addressed the integrated nature of the diagrams. Some were:

 ‘‘It was helpful when the DFDs were exploded, to see how they stayed integrated with the rest of the system.’’

 ‘‘The [ease] of being able to zoom in on areas gave a good overall picture of the whole system.’

 ‘‘It helped because it was easier to look . . . at each process [in depth].’’

## 6.2. Implications of the study

## 6.2.1. Implications for researchers

This study contributed to our knowledge of systems analysis and visualization. One way to apply a gestalt approach in the study of systems is during its graphical modeling. We used context-aware visualization techniques to demonstrate a novel approach in the presentation of business processes by integrating process details and context within the same diagram using a ‘‘fisheye’’ view.

Although the focus of this study was understanding and improvement of business processes, there are aspects of systems that can be modeled through fisheye views within a system design and development domain. For example, UML, with its ability to represent activity flows in an object-oriented application development environment, could be a viable application domain. The concepts of aggregation and inheritance have hierarchies that may lend themselves to fisheye views.

Also, our findings have implications for understanding how individual differences affect the successful use of visualization techniques. In our second study, strong interaction effects between cognitive style and level of experience and presentation method highlight the need for usability studies to be attentive to the moderating effects of individual level differences on task success. This finding is particularly interesting in that it contradicts previous work that suggests that cognitive style is not a determinant of task-based performance [36]. Although we were not specifically interested in the main effects of these individual variables, their inclusion in our models revealed interaction effects that provided greater insight into the specific circumstances under which a certain visual presentation is more successful. These results provide further insight into other research [27] that advocated the use of different information views during the systems development process as a way of addressing users’ cognitive limitations. Our findings specifically addressed one such limitation caused by users’ inherent characteristics or internal factors as suggested by Barkin and Dickson.

## 6.2.2. Implications for managers and developers

Managers of organizations that use graphical models that have a hierarchical nature should consider our findings. As the integration of disparate IS becomes prevalent, it is important to understand not only the system itself, but also its context. Hasselbring [20], for example, observed that linking suppliers with customers has extended the boundaries of their IS to include each other’s systems.

Our findings also offer guidance for CASE tool developers. We used two variations on our user interface in this study. The first consisted of static web pages, and the second enhanced those images using animated transitions and color. Such visualizations could be integrated into CASE tools through an application module that dynamically alters multi-level models within computer-based systems analysis and design tools.

## 6.2.3. Implications for educators

The use of this visualization technique has significant implications for teaching systems analysis. The benefits from the fisheye view suggested that inexperienced people realized significant speed improvements when using our techniques. Therefore, the opportunity to present relationships between subprocesses, their parent processes, and the other processes in a system more effectively should be helpful in addressing the challenge of introducing these concepts to students.

## References

[1] R. Agarwal, A.P. Sinha, M. Tanniru, Cognitive fit in requirements modeling: a study of object and process methodologies, Journal of Management Information Systems 13 (2), 1996, pp. 137–162.

[2] R. Barkhi, Cognitive style may mitigate the impact of communication mode, Information & Management 39 (8), 2002, pp. 677–688.

[3] S.R. Barkin, G.W. Dickson, An investigation of information system utilization, Information & Management 1 (1), 1977, pp. 35–45.

[4] B.B. Bederson, Fisheye menus, in: Proceedings of the ACM Conference on User Interface Software and Technology (UIST 2000), San Diego, CA, 2000, pp. 217–226.

[5] B.B. Bederson, J.D. Hollan, J. Stewart, D.A. Rogers, D. Vick, L. Ring, E. Grose, C. Forsythe, A zooming web browser, in: C. Forsythe, J. Ratner, E. Grose (Eds.), Human Factors and Web Development, Lawrence Erlbaum, Hillsdale, NJ, 1998 , pp. 255–266.

[6] R.A. Botafogo, E. Rivlin, B. Shneiderman, Structural analysis of hypertexts: Identifying hierarchies and useful metrics, ACM Transactions on Information Systems 10 (2), 1992, pp. 142–180.

[7] G. Chandrasekaran, P.J. Kirs, Acceptance of management science recommendations: the role of cognitive styles and dogmatism, Information & Management 10 (3), 1986, pp. 141–147.

[8] T.H. Davenport, J.E. Short, The new industrial engineering: information, technology, and business processes redesign, Sloan Management Review 31 (4), 1990, pp. 11–27.

[9] D.E. Egan, J.R. Remde, L.M. Gomez, T.K. Landauer, J. Eberhardt, C.C. Lochbaum, Formative design-evaluation of SuperBook, ACM Transactions on Information Systems 7 (1), 1989, pp. 30–57.

[10] G.W. Furnas, Generalized fisheye views, in: Proceedings from CHI ’86 Conference on Human Factors in Computing Systems, Boston, MA, 1986, pp. 16–23.

[11] D.F. Galletta, K.S. Hartzel, S.E. Johnson, J.L. Joseph, S. Rustagi, Spreadsheet presentation and error detection: an experimental study, Journal of Management Information Systems 13 (3), 1996/1997, pp. 45–63.

[12] A. Gemino, Y. Wand, Evaluating modeling techniques based on models of learning, Communications of the ACM 46 (10), 2003, pp. 79–84.

[13] P. Gottschalk, Strategic information systems planning: the implementation challenge, in: Proceedings of the Third Americas Conference on Information Systems, Indianapolis, IN, 1997, pp. 823–825.

[14] M.L. Gordon, L. Slade, N. Schmitt, The ‘Science of the Sophomore’ revisited: from conjecture to empiricism, Academy of Management Review 11 (1), 1986, pp. 191–207.

[15] G.I. Green, C.T. Hughes, Effects of decision support systems training and cognitive style on decision process attributes, Journal of Management Information Systems 3 (2), 1986, pp. 83–93.

[16] C. Gutwin, S. Greenberg, Short Technical Note: Interactive Fisheye Views for Groupware, Department of Computer Science, University of Calgary, Calgary, Alberta, 1997.

[17] J. Hahn, J. Kim, Why are some diagrams easier to work with? Effects of diagrammatic representation on the cognitive integration process of systems analysis and design ACM Transactions on Computer-Human Interaction 6 (3), 1999, pp. 181–213.

[18] M. Hammer, Reengineering work: don’t automate, obliterate, Harvard Business Review 68 (43), 1990, pp. 104–114.

[19] P.J. Hane, LEXIS-NEXIS tests data visualization technology, Information Today 17 (1), 1999.

[20] W. Hasselbring, Information system integration, Communications of the ACM 43 (6), 2000, pp. 33–38.

[21] I. Herman, G. Melancon, M.S. Marshall, Graph visualization and navigation in information visualization: a survey, IEEE Transactions on Visualization and Computer Graphics 6 (1), 2000, pp. 24–43.

[22] J. Kim, J. Hahn, H. Hahn, How do we understand a system with (so) many diagrams? Cognitive Integration Processes in Diagrammatic Reasoning 11 (3), 2000, pp. 284–303.

[23] J.S. Lamping, R. Rao, Visualizing large trees using the hyperbolic browser, in: Proceedings from CHI ’96 Conference on Human Factors in Computing Systems, Vancouver, Canada, 1996, pp. 388–389.

[24] K.Y. Leung, M.D. Apperley, A review and taxonomy of distortion-oriented presentation techniques, ACM Transactions on Computer-Human Interaction 1 (2), 1994, pp. 126–160.

[25] M.J. Liberatore, G.J. Titus, P.W. Dixon, The effects of display formats on information systems design, Journal of Management Information Systems 5 (3), 1989, pp. 85–99.

[26] K.H. Lim, I. Benbasat, P.A. Todd, An experimental investigation of the interactive effects of interface style, instructions, and task familiarity on user performance, ACM Transactions on Com puter-Human Interaction 3 (1), 1996, pp. 1–37.

[27] G.L. Lohse, D. Min, J.R. Olson, Cognitive evaluation of system representation diagrams, Information & Management 29 (2), 1995, pp. 79–94.

[28] G. Mandler, Organization in memory, in: K.W. Spence, J.T. Spence (Eds.), The Psychology of Learning and Motivation, Academic Press, New York, NY, 1967, pp. 327–372.

[29] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychological Review 63 (2), 1956, pp. 81–97.

[30] A.R. Montazemi, S. Wang, The effect of modes of information presentation on decision-making: a review and meta-analysis, Journal of Management Information Systems 5 (3), 1989, pp. 101–127.

[31] E. Rivlin, R.A. Botafogo, B. Shneiderman, Navigating in hyperspace: designing a structure-based toolbox, Communications of the ACM 37 (2), 1994, pp. 87–96.

[32] M. Sarkar, M.H. Brown, Graphical fisheye views of graphs, in: Proceedings of the CHI ’92 Conference on Human Factors in Computing Systems, Monterey, CA, 1992, pp. 83–91.

[33] D. Schafer, Z. Zuo, S. Greenberg, L. Bartram, J. Dill, S. Dubs, M. Roseman, Navigating hierarchically clustered networks through fisheye and full-zoom methods, ACM Transactions on Compu ter-Human Interaction 13 (2), 1996, pp. 162–188.

[34] J.B. Smelcer, E. Carmel, The effectiveness of different representations for managerial problem solving: comparing tables and maps, Decision Sciences 28 (2), 1997, pp. 391–420.

[35] A. Skopik, C. Gutwin, Improving revisitation in fisheye views with visit wear, in: Proceedings of the CHI ’05 Conference on Human Factors in Computing Systems, Portland, OR, 2005, pp. 771–780.

[36] J.W. Spence, R.J. Tsai, On human cognition and the design of information systems, Information & Management 32 (2), 1997, pp. 65–73.

[37] J.K.H. Tan, I. Benbasat, The effectiveness of graphical presentation for information extraction: a cumulative experimental approach, Decision Sciences 24 (1), 1993, pp. 167–191.

[38] P. Todd, I. Benbasat, The use of information in decision making: an experimental investigation of the impact of computer based decision aids, Management Information Systems Quarterly 16 (3), 1992, pp. 373–393.

[39] O. Turetken, D. Schuff, The use of fisheye visualizations in understanding business processes, in: Proceedings of the 10th

European Conference on Information Systems, Gdansk, Poland, 2002, pp. 322–330.

[40] O. Turetken, D. Schuff, R. Sharda, T.T. Ow, Supporting systems analysis and design through fisheye views, Communications of the ACM 47 (9), 2004, pp. 72–77.

[41] O. Turetken, R. Sharda, Clustering-based visual interfaces for presentation of web search results: an empirical investigation, Information Systems Frontiers 7 (3), 2005, pp. 273–297.

[42] M. Wertheimer, Gestalt Theory, Social Research 11, Berlin, Germany, 1924.

[43] H.A. Witkin, P.K. Oltman, E. Raskin, S.A. Karp, A Manual for the Embedded Figures Test, Consulting Psychologists Press, Palo Alto, CA, 1971.

[44] H. Yang, Adoption and implementation of CASE tools in Taiwan, Information & Management 35 (2), 1999, pp. 89–112.

![](/api/attachments/MKYSKVBC/fulltext/images/9b5a1bf89f83067aceeed5110cec7dc2f4c88d27826168f7c6b8bcbd9611ddd1.jpg)

Ozgur Turetken is an associate professor of Information Technology Management at Ryerson University. He holds a BS in Electrical and Electronics Engineering and an MBA from Middle East Technical University (Ankara, Turkey), and a PhD from Oklahoma State University. His research interests are human computer interaction with an emphasis on information organization and presentation and decision support

systems with an emphasis on building and testing predictive systems. His work has appeared in such journals as Decision Support Systems, Information Systems Frontiers, and Communications of the ACM.

![](/api/attachments/MKYSKVBC/fulltext/images/770ef977d12bd7bbb4c9b75f519b7c5397f6abbf9c76b49ba8304c3195913d98.jpg)

David Schuff is an assistant professor of Management Information Systems at Temple University. He holds a BA in Economics from the University of Pittsburgh, an MBA from Villanova University, an MS in Information Management from Arizona State University, and a PhD in Business Administration from Arizona State University. His research interests include issues surrounding IT valuation and assessment of total

cost of ownership, data warehousing, and the presentation of information to support decision making. His work has appeared in such journals as Decision Support Systems, Communications of the ACM, and Information Systems Journal.
