---
otero_id: 7208
otero_key: "QRXMW8B8"
title: "Analyzing the structure of expert knowledge"
authors: "John H. Bradley; Ravi Paul; Elaine Seeman"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2004.11.009"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Analyzing the structure of expert knowledge

John H. Bradley <sup>\*</sup>, Ravi Paul, Elaine Seeman

Department of Decision Sciences, East Carolina University, Greenville, NC 27858, USA

Received 27 August 2003; received in revised form 8 October 2004; accepted 2 November 2004 Available online 13 May 2005

## Abstract

Knowledge is either explicit or tacit. The elicitation, codification, storage, and distribution of tacit knowledge are extremely challenging tasks that require innovative methods and techniques. This paper reports the results of a study in which the tacit knowledge of domain experts was elicited, represented, and analyzed for validity. The subjects were a group of instructors and students at a USPS training school whose memory structures were analyzed for evidence of two common characteristics of expertise: holistic perception and use of abstract concepts. No evidence of either characteristic was found in the more experienced instructor group but, when the subjects were regrouped based on observed performance, the cognitive models of the high performers contained structural evidence of both characteristics. This finding led to the conclusion that experience alone is not an indicator of expertise. Other factors, such as the cognitive ability to correctly structure those experiences, must also be present.

<sup>#</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Knowledge management; Organizational knowledge; Tacit knowledge; Cognitive mapping; Expertise

## 1. Introduction

Within the broad field of knowledge management, systems developers continue to struggle with the elicitation and codification of expertise [41]. An expert is someone who is characterized by superior performance within a specific domain of activity [27]. The knowledge of an individual expert consists of both a cognitive element—the individual’s viewpoints and beliefs, and a technical element—the individual’s context specific skills and abilities [1,32,43]. Superior performance is dependent not only on domain knowledge but also on intimate familiarity with the relational structure of domain objects in a problem situation [6,45].

Tacit knowledge exists in the mind and governs the use of explicit knowledge [38]. We are usually unaware of tacit knowledge, using terms like intuition or natural ability. Explicit knowledge, on the other hand, includes things of which we are aware and can discuss with others. It is easily captured, expressed, and codified, while tacit knowledge is difficult to articulate and encode (e.g., how to tell if someone is lying). Organizational knowledge is created by a continuous dialogue between employees. Many believe that explicit knowledge without the concomitant tacit knowledge is incomplete and will result in a suboptimal solution when used in a problem-solving task. The high value of tacit knowledge motivates the organization to attempt to capture it [58]. The elicitation of tacit knowledge has been identified as a challenge in developing information systems, since traditional and more modern requirements elicitatation techniques do not address it [12]. An individual’s knowledge cannot be useful to others unless it is expressed in such a manner as to be interpretable. However, the location of this knowledge generally makes it impossible to capture and codify. Experts are not consciously aware of the tacit knowledge they use nor do they need to record it. They may also be reluctant to record the knowledge, because it is an arduous and time-consuming task and because it represents a substantial part of their value in the marketplace or in the organization [30,59]. If not captured, tacit knowledge may be lost during employee turnover as it is personal and contextdependent [36,42]. The development of strategic information systems is especially dependent on access to executives with expert-level problem-solving abilities and on the acquisition of the knowledge that underlies the skills. Indeed, business executives perceive more value in an executive support system that includes tacit knowledge that in one that is purely analytical [21].

## 2. Previous research

## 2.1. Knowledge elicitation techniques

For years, researchers have been working to develop techniques to elicit and study tacit knowledge. Much of the initial research was in the field of cognitive psychology. More recently, researchers in the Management and IS disciplines have built upon it. Tools, such as protocol analysis, neural networks, causal mapping, and cognitive mapping have been utilized to study expertise in systems and requirements analysis, software operations support, and data mining [20,35,40,63]. Many of these techniques attempted to capture the cognitive processing of the expert so it can be expressed in the form of rules in a computer system.

Of course, the human expert does not store knowledge in rules; they are generated from a combination of problem characteristics and a repository of knowledge that has been structurally refined to accommodate retrieval and solution generation. Discovering this underlying structure would provide a blueprint for the storage of knowledge and make it possible to write software that can generate rules as needed.

Tacit knowledge is closely associated with action. In a business organization, one of the most common actions is decision making. The expert knows which of thousands of pieces of data are relevant in solving a particular problem. Using object/relationship terminology, the expert tacitly knows which objects and relationships between them are germane to the problem. This knowledge can be simplistically expressed as the relationship path that the expert takes to move from one object to another until the problem is solved. Thus, asking an expert to communicate cognitive processes is rarely beneficial. Tacit knowledge can be accurately elicited using indirect techniques, which usually place the expert in a problem situation and, through observation and post-completion analysis, attempt to determine the underlying process. Another approach is to elicit the underlying memory content and organization. This attempts to recreate the cognitive map (e.g., objects and relationships) used by the expert in solving a particular problem.

It is these relationships that allow the expert to reason about a problem and traverse the mental distance between symptom and solution. Experts apparently have the mental ability to organize objects and relationships into a structure that permits effective and accurate reasoning [31]; they are able to construct a mental network or map of these relationships and facts and provide a path for their reasoning from initial problem formulation to a quality solution [33]. The higher the cost of a poor solution to a problem, the greater the value of the knowledge needed to design a good solution. Problem-solving knowledge is not only a derivative of operational data but also knowledge of how the information should be structured and processed.

## 2.2. Knowledge structure

Expert knowledge is complex. The novice incorporates the most obvious relationships when developing a mental model to use in solving a problem while the expert depends on relationships that the novice only vaguely understands. A major challenge in the elicitation of tacit knowledge structure is, however, expert-induced bias. Distortions in expert knowledge are difficult to detect, since validation against mental models is almost impossible. Distortions in an elicited cognitive model occcur for several reasons, e.g., an expert might attempt to teach a novice how to perform a task based on the expert’s perception of the novice’s limited capabilities and not in the way he or she would. If the expert views the systems analyst as a novice, this could introduce bias into the captured knowledge, especially if it is tacit knowledge. If the expert is not sure just how he or she analyses the situation, the task may also be misspecified. Bias may also be introduced when the domain knowledge is highly cognitive or complex: natural language may not be sufficient or appropriate for expressing domain models or involved procedures. Thus, some knowledge may be lost. In such situations, relationships are adjusted to meet the communication requirements and thus the structure of the knowledge is modified in the elicitation process.

Since indirect techniques attempt to access the expert’s tacit knowledge through observation, postcompletion analysis, or memory content elicitation rather than teaching or explaining [44], they offer a solution to this bias problem. Several of these techniques have been used in IS research, such as Repertory Grid [16,26,60] and Multidimensional Scaling [9].

The PathFinder technique was developed in 1985 by Schvaneveldt and Durso. It involves the conversion of a set of relatedness judgments into psychological distances, resulting in a fully connected, weighted network of concepts and relationships. An algorithm is applied to this network to generate a reduced network containing only the shortest paths. Such networks can be represented numerically and graphically. The underlying assumption is that the expert traverses a mental network of concepts and relationships by using the strongest relationships first (concept pairs with the least psychological distance). Converting relational strengths to arc distances allows the resulting network to be manipulated and studied mathematically, providing a wealth of detailed structural information for the organization that is struggling with the challenges of managing complex knowledge.

## 2.3. Link-weighted networks

Link-weighted networks have been used successfully in psychology and artificial intelligence to represent conceptual models [48]. Concept pair scaling methods that yield general network structures have been developed, but the resulting networks often do not support detailed numerical analyses [2,46]. The PathFinder procedure, used here, has been adopted by psychologists to represent the mental structures of human problem-solvers [10,50,53]. A network is generated from estimates of dissimilarity (or distances) for pairs of objects or concepts. The idea is that objects in memory are related to each other in many relationship types and strengths. These memory structures can be represented as nodes and arcs with the arc length representing the strength of the relationship [51,52]. The stronger the relationship between objects, the shorter the arc length. We begin with the selection of a finite set of objects that are germane to a particular problem scenario. A fully connected network (all possible relationships) is formed and the expert is asked to provide a measure of the strength of each relationship. This encourages the expert to consider each relationship separately and thus it avoids bias. This is an indirect as opposed to a direct approach (asking the expert how a problem is solved). The immediate objective is to elicit underlying memory structure and not the problem-solving process.

Once the relationship strengths are recorded, the greater distances (arcs) between objects (nodes) in the fully connected network are eliminated until only arcs representing the minimum weight (closest) paths connecting the objects remain. Estimates of dissimilarity are obtained by converting the concept pair judgments of similarity, or relatedness, to distance measures of dissimilarity. Given a similarity judgment, $s _ { \mathrm { j } } ,$ , and a maximum judgment rating, MaxS, the dissimilarity distance, $d _ { \mathrm { j } } ,$ , is derived by

$$
d _ {\mathrm{j}} = \operatorname{Max} S - s _ {\mathrm{j}}\tag{1}
$$

One problem with networks derived from psychological measures of concept pair distances is the assumption that the distances meet the condition for triangle inequality. Psychological judgments may show systematic violations of this [62]. For instance, objects may be related to one another in different ways. Tversky uses the example where Jamaica is similar to Cuba and Cuba is similar to Russia, but Jamaica is not at all similar to Russia. One way to avoid this condition is to amplify the dissimilarity measure, thus, eliminating paths containing dissimilar concepts.

In our study, the arc paths that are used by an individual to traverse the mental network are of primary interest. Since one characteristic of expertise is cognitive speed [28], the shortest path between related concepts should represent the one an expert would use to solve a problem. In graph theory, the minimum distance between two nodes is the minimum weight of all possible paths. Therefore, the weight of a path is the sum of the weights of the arcs in the path. In this case, it is necessary to eliminate some of the arcs in order to identify those paths that will probably be used by the expert. This will require a modification to the arc weights that will isolate the paths that should be eliminated.

For example, given two paths between concepts C1 and C8, (C1–C3–C4–C8) and (C1–C2–C5–C6–C7– C8), and MaxS = 9, summing the path weights in Fig. 1 results in the first path having the shortest length $( 9 + 2 + 1 = 1 2 )$ . However, due to the assumptions of the level of measurement associated with the dissimilarity judgments, a weight of ‘‘9’’ is an indication of the maximum level of dissimilarity. If the network is to be used as an indicator of cognitive structure, unrelated concepts mean there is no cognitive link between them. Thus, this path will never be taken, since C1 and C3 are unrelated. A measure is required that will compensate for these large psychological distances.

One distance measure that fits this requirement is the Minkowski distance measure, which can be adapted to measure paths within networks. Given a path weight W(P) consisting of arc weights $w _ { i } ,$ the weight (psychological distance) between two nodes becomes the sum of these distances.

$$
\begin{array}{l} W (\mathrm{P}) = \left(\sum w _ {i} ^ {r}\right) ^ {1 / r} \\ \text { where,} r \geq 1, w _ {i} \geq 0 \text { for   all } I \end{array}\tag{2}
$$

Increasing the value of the r-metric amplifies the relative contribution of the larger weights in the path. Thus, raising the value of r to $r = 2$ changes the path lengths so that the second path now has a shorter path length $\left( \left( 8 1 + 4 + 2 \right) ^ { 1 / 2 } = 9 . { \overset { \cdot } { 3 } } \right.$ versus $( 9 + 9 + 9 + 9 + 4 ) ^ { 1 / }$ $^ 2 = \stackrel { \bf { \bar { 6 } } } { . 3 } )$ . A network is derived by computing the $r -$ distance matrix then reducing the matrix by eliminating each arc that has weight greater than the shortest $r -$ distance [11]. As the value of r increases, the r-metric increases the weight of arcs between unrelated concepts (C1–C3) from a value of nine to a weight so large that the path weight can be determined solely by the maximum link weight in the path.

This algorithm has been incorporated into Path-Finder. Here, the value of the r-metric was set to infinity and an attempt was made to generate a network with $n - 1$ links where n was the number of concepts creating a minimum-linked network. This made the minimum and maximum distances evident while preserving the ordinal order of the distances. All paths except the minimum distance ones were eliminated, resulting in a graph containing only the links that represented the shortest paths between nodes. In the case where two paths were the same length, both were retained so the process resulted in more links that the (n  1) minimum. These networks are intended to represent the most salient relationships, thus, providing a representation of the relationships most likely used by the subjects in the process of thinking through the problem scenario. Since the networks are generated as quantitative representations, they can be analyzed and compared with relative ease. Thus, in this study, they were analyzed for characteristics that one would expect to find in the mental models of an expert and a novice.

![](/api/attachments/QRXMW8B8/fulltext/images/25fb29e4703e0c6f1a46c7dab99862c7834a285c3c17f4650c3c21dc6430f7d8.jpg)  
Fig. 1. Effect of Minkowski r-metric on path length.

## 3. Methodology

We generated networks for both instructors and students at a training center and then compare the structural characteristics of these maps to two generally accepted characteristics of expertise: holistic thinking and dependence on abstract concepts.

## 3.1. Subjects

The subjects were instructors and students at the United States Postal Service (USPS) Technical Training Center in Norman, Oklahoma, USA. The Training Center is intended for technicians who maintain the mail handling machines used by the postal service. Their knowledge of diagnostic skills is essential, since down time for these complex and expensive mail handling machines relates directly to the cost of handling the mail.

The instructors and students were all involved in the maintenance of a mail sorting machine called the OCR. It uses optical scanning to interpret the address of a piece of mail and print a bar code on the envelope with the correct zip code. Maintenance technicians for the USPS are placed in one of ten technical levels. The technicians selected for this study were all levels 8–10 and are electronic technicians (ET).

Technicians were assigned to a site where the machines were being used just prior to attending the OCR Maintenance course. Some of the technicians had experience maintaining other electromechanical equipment while others had only limited electronic experience and almost no formal or vocational education.

Due to the fact that promotions are based mostly on seniority and other organizational quirks, the sample group contained a mix of novice and expert diagnosticians. However, even the poorer diagnosticians had self-selected this profession and had enough diagnostic ability to retain their job. This meant that the differences between experts and novices were not as great as they would between experts and naive maintenance workers. The subjects were initially classified into expert and novice groups based on their position as either instructor or student. The instructors had several years of experience with the OCR, while few students had more than 2 months experience.

## 3.2. Selection of concepts

The first step was to select a manageable set of concepts that would be used in the similarity ratings. To accomplish this, a relatively common but complex problem scenario was given to the senior instructor of the training center. A recording was made of him talking through the solution to the problem. This recording was analyzed to identify a list of 43 concepts which were classified as either concrete (e.g., discussing machine parts) or abstract (e.g., talking about machine functions). As one characteristic common to expert cognition is the use of abstract concepts [55], we expected to see more abstract concepts in the expert than in the novice network. Each member of a panel of the highest rated instructors were given this list of 43 concepts and asked to indicate the five that they considered most useful in the problem scenario. A set of seventeen was chosen, primarily based on their frequency of choice, in an attempt to balance the number of concrete and abstract concepts so that neither would be predominant. Physical objects were labeled Concrete while machine functions and information flows were labeled Abstract. A computer was used to randomize all possible pairs (136 pairs). Table 1 contains an abbreviated list of the concepts. Those not in the list are proprietary information which cannot be published.

Table 1  
Some concepts used in the study

<table><tr><td colspan="3">Physical/Concrete</td></tr><tr><td>Control panel signals</td><td>Logic PC boards</td><td>Master reader cabinet</td></tr><tr><td>Cable connectors</td><td>Scanner lens</td><td>Software programs</td></tr><tr><td colspan="3">Functional/Abstract</td></tr><tr><td>Document scanning</td><td>Patterns of symptoms</td><td>Character interpretation</td></tr><tr><td>Feed rate</td><td>Read rate</td><td>Image input</td></tr></table>

## 3.3. Eliciting cognitive models

The subjects were given a questionnaire containing two major sections. The first was primarily demographic. It asked the responder for their years of experience in troubleshooting electro-mechanical equipment, both in total and specifically for the USPS, and their level of education. The second presented the list of concept pairs with a 10-interval Likert scale for each pair having end points: Unrelated (0) and Highly Related (9). The technicians were asked to indicate how closely each pair of concepts were related in the context of the same problem scenario used to derive the concept list.

Twelve of the students chose not to participate and nine of the students did not complete the entire 136 comparisons. All 7 instructor responses and 59 of the 80 student responses were usable, resulting in 66 cognitive models.

## 4. Initial comparison of instructors and students

The relatedness scores (s<sub>j</sub>) were converted into psychological distance measures $( 9 - s _ { \mathrm { j } } )$ and averaged for the instructor and student groups. This resulted in two vectors of 136 distances, each representing the average of the subjects in each group. The algorithm was applied to convert these fully-connected networks of concepts and links into minimum-linked networks, which were then validated by comparing the structural characteristics of the networks to holistic thinking and use of abstract concepts. After thoroughly testing the PathFinder approach, Schvaneveldt and Durso had developed a software package to handle the computations and produce usable output. The program used a list of 136 concept pairs and their relatedness measure (e.g., 1A, 2A, 8) as input to the algorithm, which generated a modified Minkowski distance measure for each pair of concepts. The minimum network was then computed by eliminating the longest paths. The resulting network existed as a list of concept pairs and their original distances. The software also generated a diagram with each concept pair displayed as two nodes connected by an arc. Multiple occurances of a concept were combined, so that each concept was only displayed once. The distance values in this analysis were not significant, but the number of times a single concept participated in a network path was highly significant. Counting the number of links to a concept provided a measure of significance for that concept in the mental processing of the individual.

## 4.1. Initial results

The algorithm was applied to both vectors to generate a network for instructors (Fig. 2) and students (Fig. 3). A larger number of connecting links was an indication that the concept was central to the paths through the network. The letter following the concept number designated whether the concept was Abstract or Concrete. Since the numerical values of the relatedness distances were used only to identify their ordinal location (shortest path), the network diagrams could be subjectively rearranged, moving the concepts that have the greater number of links to the top and then arranging the remainder of the network in as close to a hierarchical structure as possible that found for the expert. This allowed the concepts with the most links to be visually identified without affecting the quantitative analysis.

It is interesting that the instructor network emphasized the primary machine function (Abstract) as expected for an expert. The student network, however, emphasized both primary abstract and concrete concepts. This is an indication of the mix of two distinct cognitive structures in the student group. The instructor network contained 24 links, while the student network contained 33; it is not unusual for two or more paths to measure the same as the minimum path weight, in which case, all minimum weight paths are retained. The networks exhibited the same structural characteristics as those observed in instructor/student aircraft pilot networks in a study using the same algorithm. We took this to be an indication that the technique was applied correctly.

In order to further analyze the networks for indications of expert/novice differences, several other analyses were conducted. The networks were tested for indications of holistic perception and the use of abstract concepts in the instructor networks. The first step in analyzing them was to look for evidence of holistic thinking. The number of link attachments in the networks are an indication of the number of paths available for use in solving the problem. Holistic thinking should result in a larger number of considered paths than narrow thinking. We expected the instructor networks to contain more link attachments than student networks.

![](/api/attachments/QRXMW8B8/fulltext/images/69e0eb7408b2bc26e1d204d08e705704ba998ed5c1cf0e6d9b6e4f26a86b2bad.jpg)  
Fig. 2. Network for instructors—24 links.

![](/api/attachments/QRXMW8B8/fulltext/images/8ed4277d1e57e586491300d800d20d81bba6bac48cc2f8c663eaee6a716d46d9.jpg)  
Fig. 3. Network for Students—33 links.

## 4.2. Holistic thinking

Experts differ from nonexperts in the way they represent and bundle their knowledge [7,34,47,56]. Holistic perception refers to the way an expert views a problem. For example, a novice machine diagnostician will usually select one symptom and analyze that until a cause is detected. The novice is much more focused, having little past experience to aid in hypothesis generation. On the other hand, an expert will consider other factors, such as the events prior to the observance of the symptom, the time of day, the temperature in the room, the machine functions that are affected, patterns in the symptoms, etc. in developing a plan to proceed with the investigation. The expert’s reasoning process must be more organized because of the vast amount of information available. Experts are also aware of the more subtle relationships. In this case, the expert would be aware of electronic feedback loops between physically distant pieces of the machine that could result in a cognitive link between the two concepts; the novice, on the other hand, would not be aware of these links and thus have a simpler cognitive structure [61].

McKeithen et al. [39] found that novice and expert programmers organized knowledge differently. The novices recalled programming language keywords using mnemonic groupings (a syntactic view). This mental structure supported the finding of definitions of keywords which could then be evaluated to see if the function met the programming need. Expert programmers had knowledge that allowed searching keywords by desired function (a semantic view) and thus eliminating extraneous keywords and unnecessarily evaluating them.

The number of links could be used to compare the structure of the networks. However, in order to perform a more rigorous structural comparison of the two models, a technique must be employed that goes beyond this. The networks must be compared on a concept by concept basis. To do this, a pair-wise technique, such as the Wilcoxon signed rank test [8] is necessary. It detects differences in the frequency of scores assigned to each item or factor. One way to assign a score to each concept is to count the number of link attachments to it. One link would then have two attachments, one for each concept.

A concept in one network that has more link attachments than the same concept in another network would be included in a greater number of paths and would, therefore, be of greater use in the problem scenario. It is assumed that a concept with a greater number of link attachments is more central to the cognitive processes than a concept with only one or two link attachments. The glaring weakness of this assumption is, however, that it cannot be verified.

In an exploratory study, if the findings strongly support hypotheses that are based on the assumptions, there is the possibility that the assumptions are valid and that further research is warranted. If these structures actually represent cognitive function, there should be some evidence of observed expert behavior in the networks.

After eliminating the concepts that had an equal number of attachments (since we were only interested in the differences), the remaining student concepts contained a total of 61 connecting links, and this is significantly greater $( p < 0 . 0 2 ; z = - 2 . 1 0 )$ than the 43 connecting links remaining in the instructor network. The two models are, therefore, significantly different, an indication of the validity of the measurements. Since a significantly larger number of links represent holistic thinking, these networks indicate counterintuitively that holistic thinking is more central to the cognitive processing of students than experts. This could mean that either the experts have more streamlined structures (fewer links), or the instructor/student grouping is not a valid criteria for separating the experts from the novices.

The second step in analyzing the networks was to look for evidence of the preference for abstract concepts over concrete concepts. The number of links attached to abstract concepts in the networks are an indication of the dependence on abstract concepts in solving the problem. We expected the instructor networks to contain more abstract attachments than the student networks.

## 4.3. Use of abstract concepts

Experts characteristically use more abstract concepts to solve a problem than novices [54]. Since experts chunk or group their knowledge differently, their mental models should be characterized by groupings around abstract concepts. Novices use the inefficient approach of focusing on physical components. This has been demonstrated in prior mental model research [3,14,15,18,29]. Cooke and McDonald found that levels of abstraction can be obtained from network representations. In our study, abstract concepts, such as patterns of symptoms (9A) and the interpretation (16A) function were expected to be more central to the reasoning of the instructors. Conversely, concrete concepts, such as master reader cabinet (8C) were expected to be more central to the reasoning of the students.

The number of links attached to each concept was measured. Abstract concepts were expected to have more connecting links in the instructor network while the student network should display more connecting links for the concrete concepts. The more connecting links, the more important the concept is in the reasoning process.

Eight of the seventeen chosen concepts were abstract: they either pertained to reasoning about the relationship between multiple machine functions or they referred directly to those functions. Several of the concepts were explicitly designated as being abstract to avoid misinterpretation by the technician. In contrast, the remaining concrete concepts referred to specific machine components. Using the Wilcoxon signed rank test, the instructors had significantly fewer ( p < 0.05, z = 1.68) links to abstract concepts than the students: the instructors had 28 abstract concept links while the students had 38. Again, no evidence was found of the use of abstract concepts in the instructor network.

Since prior research supported the expert’s use of abstract concepts and since the networks have shown every evidence of being a meaningful representation of mental structures, the only plausible explanation for these results is that some instructors were not experts or that some students were not novices, even though the instructors had more experience.

This finding is important. Using experience and position as the expert/novice classification criteria may have led to incorrect and misleading conclusions. To test the expert/novice classification scheme, another measure of expertise was needed to reclassify the subjects and test again for holistic thinking and the use of abstract concepts.

## 5. Subsequent comparison of high and low performers

Our study began by categorizing the subjects based on their position. This experience criteria ignored the cognitive abilities necessary to use the experiences to improve task performance. The results from participants here were, therefore, reorganized into two new groups based on their job performance and the new networks reanalyzed for holistic perception and the use of abstract concepts.

## 5.1. Grouping by observed performance

Studies in personnel psychology have had much to contribute to the identification of superior performance. The most obvious indicators of ability are those that can be easily and accurately measured, such as years of experience or position in the organization. We posit that experience and position are indicators of seniority but not necessarily of superior task performance.

In a meta-analysis of research on various predictors of job performance, Hunter and Hunter [23] found general cognitive ability to be the most valuable predictor for entry-level jobs (mean validity {Pearson’s correlation} of 0.53) while training and experience ranked seventh. In other meta-analytic studies, Hunter [22,24,25], determined that the validity of specific aptitude measures stems from their measurement of general cognitive ability. Using a sample of 16,058 workers, McDaniel et al. [37] found that experience was most valid as a predictor of job performance when there were low levels of both task complexity and experience (<5 years). The validity of experience decreased for more complex tasks and for subjects with higher levels of experience. Conversely, cognitive ability measured increase in validity as job complexity increased. Other studies report consistent findings [19,57].

For complex jobs, experience is apparently a weak indicator of expertise; it is a combination of experience and cognitive ability (Fig. 4). Since OCR diagnostics can be considered a complex task (only top rated technicians were selected for training), reliable measures of job performance or cognitive ability should provide stronger measures of expertise than experience or position.

For this model, a dependable measure of job performance would yield a reliable measure of expertise. Measures of performance have historically depended upon either self-reporting or the opinion of others. The most dependable measure seems to be the performance rating by another person under certain conditions:

1. the subjects must already be trained for the job. Performance ratings during the training period are not valid measures of ability to perform a task;

2. the rating must be made on the basis of observed performance. The rater and the supposed expert must have worked extensively together. The outcome of a task is not the only indicator of performance. The expert approaches a problem in a certain way. The novice, in an effort to recover from information overload, will select one cue and trace it to its source. Armed with this, he or she will select a second cue and trace it back, etc. until enough information is gathered to piece together hypothetical causes [5]. The rater must be able to observe the entire problem-solving process in order to make a reliable judgment.

## 5.2. Performance measures

One would expect that experienced instructors would exhibit superior performance in problemsolving. The USPS training facility contains a machine lab where instructors plant faults in OCR machines. The students in our study were given sixteen trials throughout the 2 months duration of the course. Several instructors observed each student’s approach and the time it took the student to resolve the malfunction. Over several years, the instructors themselves had regularly faced diagnostic situations. These occurred when the machines developed real malfunctions. Then, the lead instructor would observe the diagnostic performance of the instructor who fixed the machine. Therefore, since the data was collected at the end of the class, both conditions for dependable measures of diagnostic performance were met.

Ratings of observed diagnostic performance were accumulated using a five-point Likert scale with end points of ‘5’ for consistently outstanding performance and ‘1’ for consistently poor performance. Each person was rated by at least two instructors. The instructors rated each other and also by the chief instructor. In the ratings where differences occurred, the rating instructor was questioned as to his understanding of the criteria and given a chance to modify the rating. If differences still existed, the instructor who had been rated as a ‘5’ was chosen as the correct rater. After these modifications were completed, inter-rater reliability measures showed no significant differences. In our study, it was also deemed interesting to know if experience alone was an indicator of diagnostic performance: could a person have years of experience and yet display only adequate performance?

## 5.3. High/low performer results

A total of 69 technicians responded to the first part of the questionnaire. Their experience was divided into two parts; experience with USPS equipment and experience maintaining any other equipment. These were totaled to generate a third variable; total experience. The accuracy of these self-reported measures can certainly be questioned. There was no practical way to verify each person’s experience.

A correlation analysis of the three experience variables resulted in only total experience being significantly related $( p < 0 . 0 4 , ~ r = 0 . 2 6 )$ to the performance rating. However, this correlation is not high enough to show that experience is a functionally significant measure of diagnostic performance. Postal experience (job specific experience) was not significantly correlated with performance $( p < 0 . 3 4$ $r = 0 . 1 2 )$ ).

To group the subjects by performance, a valid performance measure was needed. Were the ratings of observed diagnostic performance valid measures of the level of task performance? Thirty-two of the subjects (all 7 instructors and 25 of the students) volunteered to take the Watson Glaser critical thinking appraisal (CTA), a validated measure of general cognitive ability.

The CTA contains a set of problem scenarios with several questions concerning the thought process involved in solving each scenario. Answers are graded according to an answer key provided with the instrument, which results in a single numeric score that measures general critical thinking ability. Performance measures were compared to CTA scores. If subjects performed well on diagnostic tasks, they should also score high on the critical thinking instrument. The correlation was significant $( p <$ 0.0001, $r = 0 . 8 5 )$ . This strong correlation was an indication not only that the performance measures used were reliable, but also that the well-trained, experienced technicians were more dependent on cognitive ability for their job performance than for experience (Fig. 4). This is consistent with findings in the personnel psychology literature [4,49].

![](/api/attachments/QRXMW8B8/fulltext/images/d667b7ee4b37d155c91a31bbc90069a9f41dc36db7d28b314a5bcd886b92a27a.jpg)  
Fig. 4. Model of the components of expertise. Adapted from Schmidt et al. [49].

Using the performance ratings as a classification variable, the instructors and students were regrouped. The subjects that were rated as outstanding performers were placed in the high performer group while the subjects who were consistently poor in their diagnostic performance were placed in the low performer group (Fig. 5). Technicians that were rated between these extreme ratings were dropped from the study, reducing the size of the sample to 18. This technique is consistent with the research methods of Emory [13]. Networks were generated for these two groups (Figs. 6 and 7) and analyzed for indications of holistic perception and the use of abstract concepts.

![](/api/attachments/QRXMW8B8/fulltext/images/1cb8bb350c96843639297987b3c67048e829e84b59c10c2d9eb4bf399656aee5.jpg)  
Fig. 5. Regrouping of subjects based on performance.

## 5.4. Holistic thinking of high/low performers

Using the same analyses as before for holistic thinking, the network for the high performer group had 31 links while the low performer group had only 24 links. The Wilcoxon signed rank test again revealed a significant difference in the number of these links $( p < 0 . 0 5 , \ z = - 1 . 6 4 )$ . However, using performance as the categorization variable, the high performer group had more links. This was the expected and could be an indication of a more holistic perspective.

Table 2 depicts the number of links in the individual networks. It was interesting to note the greater variance within the high performer group. This may be due to the difference in experience between the subjects, since some of the high performers were students, or it may be an indication of the different ontological perspectives of the subjects [17]. The low performers’ perspectives of a problem would probably correspond closely to one another and to the material presented in the course. The perspectives of the high performers, on the other hand, would be more heavily influenced by their varied past experience, which is indicative of greater use of analogical reasoning in the high performer group. The small number of subjects prevents useful conclusions based on the variance of the individual networks. However, there is evidence for holistic perception in the composite network.

## 5.5. Use of abstract concepts of high/low performers

In the analysis for the use of abstract concepts, a larger number of links were expected to be attached to abstract concepts in the high performer network than in the low network. This would indicate a preference for abstract concepts in the reasoning of experts. This was in fact the case. The high performer network had 29 abstract links to 22 abstract links in the low performer network. The high performers indicated a significantly greater $( p < 0 . 0 2 , z = - 2 . 0 2 )$ ) preference for abstract concepts than the low performers. The results suggest that the technicians who demonstrated superior performance in diagnosing machine faults use cognitive structures that exhibit two of the characteristics commonly associated with expertise. Only when performance was used as the classification variable were expected results demonstrated.

![](/api/attachments/QRXMW8B8/fulltext/images/f9c9b9fd4059e3d37a6f23d72cd17451ac427bb2ee465c5c537b2a22cf2cfde2.jpg)  
Fig. 6. Network for high performers—31 links.

![](/api/attachments/QRXMW8B8/fulltext/images/483d719d9dcda6238ed751bef6a0ef3fd3687b3b679b48d49442e0e58cc0709c.jpg)  
Fig. 7. Network for low performers—24 links.

Table 2  
Number of links in the individual networks

<table><tr><td></td><td colspan="12">Number of links</td><td>Average links</td><td>Standard deviation</td></tr><tr><td>High Performers</td><td>79</td><td>57</td><td>55</td><td>51</td><td>43</td><td>41</td><td>33</td><td>33</td><td>30</td><td>28</td><td>26</td><td>25</td><td>41.75</td><td>16.2</td></tr><tr><td>Low Performers</td><td></td><td></td><td></td><td>38</td><td>31</td><td>29</td><td>24</td><td>19</td><td>18</td><td></td><td></td><td></td><td>26.5</td><td>7.9</td></tr></table>

## 6. Limitiations and conclusions

There are many limitations in this study. The most obvious is the lack of rigor in measuring the mental models of the subjects. Even though the networks seemed to produce consistent results, they fall short of revealing how the experts use them. Also, since the networks are specific to one scenario, nothing is provided as to their stability or how they change in other problem situations.

Other limitations stem from the use of ‘‘real’ subjects in a quasi-controlled environment with questionable subject motivation and unbalanced subject groups. The fact that reasonable findings seemed possible suggests that our techniques are valuable in approaches to the quest for expert knowledge.

Strong arguments can be presented on whether the expert’s mental model is more complex due to the complexity of the cognitive processes or less complex due to superior mental organization. When the subjects were grouped by observed job performance, the expert network contained more links yet was more hierarchically organized, revealing a preference for abstract concepts. When grouped by experience, the expert network contained fewer links and was more disorganized, revealing no real preference.

The primary conclusion is that complex, tacit knowledge can be accurately elicited and codified. The elicitation methods and tools, however, must include some means of validating the identification of experts and novices.

The second conclusion is that the indirect technique of eliciting pair-wise comparisons is useful for the collection and representation of tacit cognitive structure. This study contributed to the study of human cognition as it provides detail representing specific relationships between concepts. This is not available from most commonly used techniques.

Several problems were encountered that must still be addressed. The number of concepts that can be used is severely limited unless some method is developed to reduce the number of concept pairs. It would have been revealing to have included a larger set of concepts. However, this was not practical since 50 concepts would generate a questionnaire with 1225 needed responses. There was concern in this study that the subjects would not maintain the required mental focus over the 136 responses.

Assuming the availability of a practical implementation methodology, the network of the expert would provide valuable information for the organization. Expertise, rather than just a set of related facts and rules, would be indicated when the knowledge base and the network of the expert contain similar structural characteristics.

If knowledge analysts are familiar with the structural characteristics of expertise in a particular problem domain, then they could test for those characteristics in the network of the knowledge source. When attempting to define a new domain, the network of even one expert would be a valuable indicator of the basic organization of the domain knowledge as well as the structural refinements that are responsible for superior performance. The network could be useful as a tool to organize the knowledge into segments for elicitation, codification, storage, and distribution.

A validation measure is essential to provide an independent indication of the level of expertise of the individual knowledge source. The fact that the knowledge-based system provides responses that emulate the original knowledge source is not necessarily an indication that expertise has been captured.

## References

[1] M. Alavi, D.E. Leidner, Knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Quarterly Review 25(1), 2001, pp. 107–136.

[2] J.R. Anderson, The Structure of Cognition, Harvard Press, Cambridge, MA, 1983.

[3] M. Bouman, The use of accounting information: expert versus novice behavior, in: G. Ungson, D. Braunstein (Eds.), Decision Making: An Interdisciplinary Inquiry, Kent, Boston, 1982.

[4] J.H. Bradley, Identifying the expert in diagnostic decision making, in: Proceedings of the 1992 Decision Sciences Institute Conference, San Francisco, 1992, pp. 725–727.

[5] J.H. Bradley, Cognitive aspects of expertise and their importance in the development of complex knowledge-based systems, in: Proceedings of the 1991 Decision Sciences Institute Conference, Miami, 1991, pp. 635–637.

[6] B. Brehmer, In one word: not from experience, Acta Psychologica 45, 1980, pp. 223–241.

[7] M.T.H. Chi, P.J. Feltovich, R. Glaser, Categorization and representation of physics problems by experts and novices, Cognitive Science 5, 1981, pp. 121–152.

[8] C.T. Clark, L.L. Schkade, Statistical Analysis for Administrative Decisions, third ed., South-Western, Cincinnati, 1979.

[9] N.J. Cooke, J.E. McDonald, The application of psychological scaling techniques to knowledge elicitation for knowledgebased systems, in: J. Boose, B. Gaines (Eds.), Knowledge-Based Systems, (vol. 2), Academic Press, New York, 1988.

[10] N.J. Cooke, R.W. Schvaneveldt, Effects of computer programming experience on network representations of abstract programming concepts, International Journal of Man-Machine Studies 29, 1988, pp. 407–427.

[11] D.W. Dearholt, R.W. Schvaneveldt, Properties of Pathfinder networks, in: R.W. Schvaneveldt (Ed.), Pathfinder Associative Networks, Ablex Publishing, Norwood, NJ, 1990.

[12] M. Eva, Requirements acquisition for rapid applications development, Information & Management 39(2), 2001, pp. 101– 107.

[13] C.W. Emory, Business Research Methods, Irwin, Homewood, 1985.

[14] R. Ettenson, J. Shanteau, J. Krogstad, Expert judgment: is more information better? Psychological Reports 60, 1987, pp. 227–238.

[15] J. Freyd, Dynamic mental representations and apparent accelerated motion, Dissertation Abstracts International 44(9), 1983, p. 92.

[16] B.R. Gaines, M.L.G. Shaw, New directions in the analysis and interactive elicitation of personal construct systems, International Journal of Man-Machine Studies 13, 1980, pp. 81–116.

[17] J.G. Gammack, Expert conceptual structure: the stability of pathfinder representations, in: R.W. Schvaneveldt (Ed.), Pathfinder Associative Networks, Ablex Publishing, Norwood, NJ, 1990.

[18] R. Glaser, Education and thinking, the role of knowledge, American Psychologist 39(2), 1984, pp. 93–104.

[19] R.L. Gutenberg, R.D. Avery, H.G. Osburn, P.R. Jeanneret, Moderating effects of decision-making/information processing job demands on test validities, Journal of Applied Psychology 68, 1983, pp. 602–608.

[20] T. Hong, I. Han, Knowledge-based data mining of news information on the Internet using cognitive maps and neural networks, Expert Systems with Applications 23, 2002, pp. 1–8.

[21] S. Hung, Expert versus novice use of the executive support systems: an empirical study, Information & Management 40(3), 2003, pp. 177–189.

[22] J.E. Hunter, differential validity across jobs in the military (DOD Contract No. F41689-83-C-0025), Research Applications Inc., Rockville, MD, 1985.

[23] J.E. Hunter, R.F. Hunter, Validity and utility of alternate predictors of job performance, Psychological Bulletin 96(1), 1984, pp. 72–98.

[24] J.E. Hunter, The dimensionality of the general aptitude tests battery (GATB) and the dominance of the general factors over specific factors in the prediction of job performance for USES (Test Research Report No. 44), US Department of Labor, US Employment Services, Washington, DC, 1983.

[25] J.E. Hunter, The prediction of job performance in the military using ability composites: the dominance of general

cognitive ability over specific aptitudes (DOD Contract No. F41689-83-C-0025), Research Applications Inc., Rockville, MD, 1983.

[26] M.G. Hunter, J.E. Beck, Using repertory grids to conduct cross-cultural information systems research, Information Systems Research 11(1), 2000, pp. 93–101.

[27] P. Johnson, I. Zualkernan, S. Garber, Specification of expertise, International Journal of Man-Machine Studies 26, 1987, pp. 161–181.

[28] P. Johnson, What kind of expert should a system be? The Journal of Medicine and Philosophy 8, 1983, pp. 77–97.

[29] H. Kahney, Problem solving by novice programmers, in: T. Green, S. Payne, G. Vander Veer (Eds.), Psychology of Computer Use, Academic Press, London, 1983.

[30] K. Karhu, Expertise cycle—an advanced method for sharing expertise, Journal of Intellectual Capital 3(4), 2002, pp. 430– 446.

[31] E.T. Keravnou, L. Johnson, Competent Expert Systems: A Study in Fault Diagnosis, McGraw-Hill, NY, 1986.

[32] J. Keyes, Where’s the ‘‘expert’’ in expert systems, AI Expert, vol. 5, No. 3, 1990, pp. 61–64.

[33] I. Kinchin, D. Hay, A. Adams, How a qualitative approach to concept map analysis can be used to aid learning by illustrating patters of conceptual development, Educational Research 42(1), 2000, pp. 43–57.

[34] J. Larkin, J. McDermott, D. Simon, H. Simon, Expert and novice performance in solving physics problems, Science 208, 1980, pp. 1335–1347.

[35] S. Lee, I. Han, Fuzzy cognitive map for the design of EDI controls, Information & Management 37, 2000, pp. 37–50.

[36] D. Leonard, S. Sensiper, The role of tacit knowledge in group innovation, California Management Review 40(3), 1998, pp. 112–132.

[37] M.A. McDaniel, F.L. Schmidt, J.E. Hunter, Job experience correlates of job performance, Journal of Applied Psychology 73(2), 1998, pp. 327–330.

[38] K. McGraw, K.A. Harbison-Briggs, Knowledge Acquisition: Principles and Guidelines, Prentice-Hall, NJ, 1989.

[39] K.B. McKeithen, J.S. Reitman, H.H. Rueter, S.C. Hitle, Knowledge organisation and skill differences in computer programmers, Cognitive Psychology 13, 1981, pp. 307–325.

[40] A.R. Montazemi, D.W. Conrath, The use of cognitive mapping for information requirements analysis, MIS Quarterly 10(1), 1986, pp. 45–56.

[41] K.M. Nelson, S. Nadkarni, V.K. Narayanan, M. Ghods, Understanding software operations support expertise: a revealed causal mapping approach, MIS Quarterly 24(3), 2000, pp. 475–502.

[42] J.B. Noh, K.C. Lee, J.K. Kim, J.K. Lee, S.H. Kim, A casebased reasoning approach to cognitive map-driven tacit knowledge management, Expert Systems with Applications 19, 2000, pp. 249–259.

[43] I. Nonaka, A dynamic theory of organizational knowledge creation, Organization Science 5(1), 1994, pp. 14–37.

[44] J. Olson, H. Rueter, Extracting expertise from experts: methods for knowledge acquisition, Expert Systems 4(3), 1987, p. 152.

[45] J. Rentsch, T. Heffner, Group and Organization Management 19(4), 1994, pp. 450–474.

[46] D.E. Rumelhart, J.L. McClelland, Parallel Distributed Processing, (vol. 1), MIT Press, Cambridge, MA, 1986.

[47] D.E. Rumelhart, D.A. Norman, Accretion, tuning and restructuring: three models of learning, in: R. Klatsky, J.W. Cotton (Eds.), Semantic Factors in Cognition, Erlbaum, Hillsdale, 1997.

[48] T.L. Saaty, Analytic Hierarchy Process: Planning, Priority Setting and Resource Allocation, McGraw-Hill, NY, 1980.

[49] F.L. Schmidt, J.E. Hunter, A.N. Outerbridge, Impact of job experience and ability on job knowledge, work sample performance, and supervisory ratings of job performance, Journal of Applied Psychology 71(3), 1986, pp. 432–439.

[50] R.W. Schvaneveldt, Pathfinder Associative Networks: Studies in Organization, Ablex Publishing, Norwood, NJ, 1990.

[51] R.W. Schvaneveldt, D. Dearholt, F. Durso, Graph theoretic foundations of pathfinder networks, Computer Math Applications 15(4), 1988, pp. 337–345.

[52] R.W. Schvaneveldt, Pathfinder: networks from proximity data, Memorandum in Computer and Cognitive Science, MCCS-87- 9, Computing Research Laboratory, New Mexico State University, 1987.

[53] R.W. Schvaneveldt, F. Durso, T. Goldsmith, T. Breen, N. Cooke, R. Tucker, J. DeMaio, Measuring the structure of expertise, International Journal of Man-Machine Studies 23, 1985, pp. 699–728.

[54] V. Sembugamoorthy, B. Chandresekaren, Functional representation of devices and compilation of diagnostic problem-solving systems, in: J.L. Kolodner, C.K. Reisbeck (Eds.), Experience, Memory, and Reasoning, Erlbaum, Hillsdale, 1986.

[55] J. Shanteau, Psychological characteristics of expert decision makers, in: J.L. Mumpower, L.D. Phillips, O. Renn, V.R.R. Uppuluri (Eds.), Expert Judgement and Expert Systems, Springer Verlag, NY, 1987.

[56] S.D. Sheetz, Identifying the difficulties of object-oriented development, The Journal of Systems and Software 64, 2002, pp. 33–36.

[57] R.E. Snow, D.F. Lohman, Toward a theory of cognitive aptitude for learning from instruction, Journal of Educational Psychology 76, 1984, pp. 347–376.

[58] I. Spiegler, Knowledge Management: A New Idea or a Recycled Concept? 2000.

[59] D. Stenmark, Leveraging tacit organizational knowledge, Journal of Management Information Systems 17(3), 2001, pp. 9–24.

[60] F.B. Tan, M.G. Hunter, The repertory grid technique: a method for the study of cognition in information systems, MIS Quarterly 26(1), 2002, pp. 39–57.

[61] Y. Tenney, L. Kurland, The development of troubleshooting expertise in radar mechanics, in: J. Postka, L. Massey, S.

Mutter (Eds.), Intelligent Tutoring Systems: Lessons Learned, Erlbaum, Hillsdale, 1988.

[62] A. Tversky, D. Kahneman, Extensional versus intuitive reasoning: the conjunctional fallacy in probability judgement, Psychological Review 90(4), 1983, p. 293.

[63] N.P. Vitalari, Knowledge as a basis for expertise in systems analysis: an empirical study, MIS Quarterly 9(3), 1985, pp. 221–241.

![](/api/attachments/QRXMW8B8/fulltext/images/0d157d5e4831a63c5d81e7b210b827a5475fc39caf8637e02db09f3006b44282.jpg)

John H. Bradley is an Associate Professor of Management Information Systems in the Department of Decision Sciences at East Carolina University. He holds a Ph.D. in management information systems and an MBA. His research interests are expert systems, knowledge based systems, case-based reasoning, team performance, and IS implementation and organizational impact. Dr. Bradley has

published in journals, such as Expert Systems with Applications, Heuristics, Small Group Research, and others. He can be reached at bradleyj@mail.ecu.edu.

![](/api/attachments/QRXMW8B8/fulltext/images/d15fd35f22e75f28f05bf05cefb75bd8d43284bd53fbf3fbc3be06ecb5305ee7.jpg)

Ravi Paul, Ph.D. is Assistant Professor of Management Information Systems at East Carolina University. He has been in the computer industry for 12 years, holding technical and managerial positions in systems analysis, design, development and administration. He is currently conducting research in several areas of Software Engineering (Requirements Engineering, Relationship Analy

sis), Information Systems (Computer Self-Efficacy, IS Service Quality and Culture) and Cognition (Cognitive Maps, Critical Thinking, Learning). His research has been published in journals, such as the Requirements Engineering Journal and the Journal of Informatics and Education Research (JIER), as well as in conference proceedings, such as HICSS, AIS and DSI.

![](/api/attachments/QRXMW8B8/fulltext/images/f268ad7cf0e925aeb1790cf000d14ad11971baf5143d1f92e960a14d5e8026fc.jpg)

Seeman, Elaine, Ph.D. (Indiana State University, 2003) is Assistant Professor of Management Information Systems at East Carolina University. Her current research interests include the role of work values in physician technology acceptance, the regulatory effect of new technology implementation, Electronic ICU, critical thinking and the role of government in the development of wireless loca-

tion technologies. Prior to coming to East Carolina University, Elaine was the Associate Vice President for Virtual Learning at Pitt Community College in Greenville, NC.
