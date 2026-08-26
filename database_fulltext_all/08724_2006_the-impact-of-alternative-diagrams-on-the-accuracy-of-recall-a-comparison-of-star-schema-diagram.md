---
otero_id: 8724
otero_key: "HHEQQE9F"
title: "The impact of alternative diagrams on the accuracy of recall: A comparison of star-schema diagrams and entity-relationship diagrams"
authors: "Karen Corral; David Schuff; Robert D. St. Louis"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2005.02.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of alternative diagrams on the accuracy of recall: A comparison of star-schema diagrams and entity-relationship diagrams

Karen Corral <sup>a,T</sup>, David Schuff <sup>b</sup>, Robert D. St. Louis <sup>a</sup>

<sup>a</sup> Arizona State University, Department of Information Systems, PO Box 874606, Tempe 85287-4606, AZ, United States <sup>b</sup> 209F Speakman Hall, Fox School of Business and Management, Temple University, 1810 North 13<sup>th</sup> Street, Philadelphia, PA 19122

Available online 22 April 2005

## Abstract

Data warehouses can be constructed using either a relational or a dimensional model. This research compares the diagrammatic representations of these two models. Semantic network theory suggests that, because of their structure, starschema diagrams (SSDs) are more understandable than entity-relationship diagrams (ERDs). Through two experiments that test both the accuracy and pattern of users’ recall, we find strong evidence that SSDs are easier to understand than ERDs. Our findings imply that the use of the dimensional model should help decision makers query the warehouse directly, thereb reducing costs and the need for intervention and support by IT professionals. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Data warehouse; Data modeling; Entity-relationship diagram; Semantic network theory; Gestalt theory; Star-schema diagram

## 1. Introduction

The data warehouse has become an important tool for supporting decision making at all levels of the organization. Expenditures on data warehouses are expected to increase from \$60 billion dollars in 2001 to \$150 billion dollars in 2005 which is over 20% per year [27]. To fully realize the benefits of the investment in these enterprise-wide information stores, end users must be able to easily access the data contained within the warehouse. Traditionally, retrieval of such data required the expertise of information systems professionals [2]. This is due to the technical knowledge required to query the data warehouse (i.e., a query language such as SQL), the difficulty of understanding the underlying data model (i.e., entity-relationship diagrams), or both.

Data warehouses are built to support decision makers, not database administrators. To improve the timeliness and quality of their decisions, decision makers need to integrate information across disparate databases, and have a user-friendly interface that facilitates direct access to needed data [7] without requiring additional technical support (from, for instance, a database administrator). A great deal of attention has been focused on technical performance measures (i.e., query processing speed) for data warehouses as well as their physical design [7]. However, success is ultimately determined by how the warehouse is used to improve decision making. It is not sufficient to build a technically sound system; users must see that the warehouse can provide them with the information they require [13].

![](/api/attachments/HHEQQE9F/fulltext/images/be8e11f64f6940ee0e1c9fafd585903df6192e6c33e92b8d6403ed1b09cbf24b.jpg)  
Fig. 1. An example of a star schema diagram.

Most previous information systems research into successful data warehouse implementations has taken a managerial perspective [2,6], looking at the environmental and organizational factors required for success [23,41] and how the data warehouse facilitates corporate strategy [11]. This paper takes a <sup>b</sup>human factors<sup>Q</sup> approach to the issue by examining the data model itself and its inherent understandability.

There are two competing models for organizing data within a data warehouse; the relational model and the dimensional model. One of the fundamental aspects of the relational model is that data integrity be maintained through normalization. Data warehouses do not have spontaneous updates to data (outside of scheduled refreshes) and therefore do not have the same concerns with normalization. In fact, denormalization is encouraged in data warehouses as it leads to greater efficiency when queries are run against the warehouse. The dimensional model was introduced to represent this denormalized view of data.

Dimensional data warehouses are constructed using a constrained version of the entity-relationship model. The resulting schema is made up of central entities, called fact tables, around which the dimensional entities are arranged (Fig. 1). These central entities capture a business event (for instance, a sales transaction or a student registering for a course) around which the data warehouse is built. This schema is referred to as the <sup>b</sup>star schema<sup>Q</sup> because of its arrangement of entities in a star-like pattern. The diagrammatic representation of the star schema is called a star-schema diagram (SSD). In contrast, the standard entity-relationship diagram (ERD) does not have a central focus or a standard pattern (Fig. 2).

The decision whether to build a data warehouse using a relational or a dimensional model has created controversy in the practitioner community. The traditional ER model is preferred by Inmon, Imhoff, and Sousa [17], but others, most notably Ralph Kimball, have made the claim that <sup>b</sup>dimensional modeling is the only viable technique for databases that are designed to support end-user queries in a data warehouse<sup>Q</sup> [18, p. 1]. Proponents of the dimensional model argue that, because it is arranged around a specific business <sup>b</sup>fact,<sup>Q</sup> the SSD has inherent advantages over the ERD when it comes to understandability of the underlying data model. Opponents criticize the dimensional model because it optimizes <sup>b</sup>for one user or set of users and deoptimizes access of data for all other users<sup>Q</sup> [17, p. 77]. As a result, multiple data marts are often needed to provide the customized data sets appropriate for different user groups. Increased costs can be associated with creating and maintaining those data marts.

![](/api/attachments/HHEQQE9F/fulltext/images/7dcf4bb422f51cf76ea22f930414ceee416ec6019c2e1bad3bb57bd746621649.jpg)  
Fig. 2. An example of an entity relationship diagram.

The way a database is represented and structured can influence how individuals understand and use it [21]. In particular, the format in which information is provided to users has a strong influence on their ability to recognize and use that information [20]. Therefore, determining which model is the best for end users from a usability standpoint is of great importance to both practitioners and researchers. This leads us to our research question:

Does the diagrammatic representation of alternative data models for a data warehouse influence understanding of that data warehouse?

We address this question by comparing the understandability of the dimensional model to that of the entity-relationship model. And this allows us to test the claim that the star-schema representation of a data model is easier to understand than the entity-relationship representation of an equivalent data model [18]. The results of a recall experiment indicate that both novices and experienced entity-relationship modelers recall the relationships of the star-schema diagram more accurately than the relationships of the entityrelationship diagram. These findings suggest that star schemas are easier to comprehend. We also analyze the order in which items are recalled. The recall patterns suggest that subjects find the structure of SSDs (i.e., the relationships between the dimension tables and the fact table) more intuitive than the structure of ERDs. That is, they more effectively chunk the entities, which lead to greater recall. The subjects given ERDs show little evidence of chunking the ERDs.

The potential impact of this study on the design of data warehouses is significant. If the star schema is inherently more understandable than its equivalent entity-relationship diagram, then users should be better able to query its content directly. These user-driven queries could be done, without intervention from an information technology specialist or a database administrator, and also without need for custom-built applications. This could lead to lower application development and technical support costs, while at the same time bringing decision makers closer to the data they require.

The paper is organized as follows. First, a discussion of the theoretical foundation for understanding human memory storage structures is presented. This is followed by a brief review of research that compares data models. Next, we develop the hypotheses to be tested, and describe the two experiments that were performed. We then present the results of the experiment, and conclude with a discussion of our findings and possible directions for future research.

## 2. Theoretical foundation

Cognitive science provides a theoretical foundation to suggest a difference in understandability between entity-relationship and star schema diagrammatic representations. The semantic network theory of memory storage posits that humans store concepts in memory as linked units [1,10]. The way information is represented in memory is important. The closer the structure of the stimulus is to the memory storage structure, the easier it is to store the stimulus in its original form. The easier it is to store the stimulus in its original form, the more likely the stimulus will be accurately retrieved. In this section, we present a brief overview of semantic network theory, followed by a review of research on data models, a discussion of the implications of semantic network theory for the understandability of data models, and the development of the hypotheses to be tested.

## 2.1. Semantic network theory and human memory storage

There is a large body of research which has shown that the structure of human memory is organized into <sup>b</sup>chunks<sup>Q</sup> which serve to increase memory capacity (e.g., [3,20]). Without chunking, humans have severely restricted memory capacities. <sup>b</sup>Organization is a necessary condition for memory<sup>Q</sup> [24, p. 328]. Used in this context, organization is more than just the sum of the meaning of the individual words in a sentence or paragraph; it also includes the meaning of the relationships among the specific order of the words. Organization <sup>b</sup>involves the formation and perception of groupings and of their relations<sup>Q</sup> [24, p. 329]. In other words, it is much easier to remember information that makes sense than nonsensical information [1]. Sachs [30] found experimental evidence that subjects retain an exact sentence only as long as it takes to comprehend the meaning, after which only the meaning is stored while the exact sentence is discarded. People <sup>b</sup>omit many of the unimportant perceptual details<sup>Q</sup> while storing what is actually important [1, p. 112].

Semantic network theory states that people store information in minimal units called propositions. Anderson [1, p. 123] defines a proposition as <sup>b</sup>the smallest unit of knowledge that can stand as a separate assertion.<sup>Q</sup> Propositions are linked by associations, and the resulting networks are stored in memory. As a result, the ability to retrieve information requires the retrieval of not only the propositions, but also the links between those propositions.

Propositions can be organized into chunks—in other words, they can be linked with another proposition to form a larger chunk. As simple example, consider knowledge of Microsoft’s Word and knowledge of Corel’s WordPerfect as two propositions. Together they can be chunked, or linked, into the larger chunk of <sup>b</sup>knowledge about word processing pack ages.<sup>Q</sup> Another possible chunk might be <sup>b</sup>knowledge about software packages,<sup>Q</sup> which contains the smaller chunks <sup>b</sup>knowledge about word processing packages<sup>Q</sup> and <sup>b</sup>knowledge about spreadsheet packages.<sup>Q</sup>

Experiments have shown that recall of elemental items increases when they are organized into chunks [24,25]. Miller [25] found that when groups of concepts are enriched with additional information people can remember far more than the <sup>b</sup>seven, plus or minus two<sup>Q</sup> number that is the generally accepted [4,24,33] limit of short-term human memory. When presented with lists of meaningful words, subjects will group the items into categories and retrieve the items by category rather than in their original random order [3]. This is because the concepts have more semantic meaning as a result of being a member of a chunk.

Finding the paths between concepts is critical to people’s ability to comprehend and retrieve those concepts. Simon [33] found that organizing information into meaningful chunks facilitates the recall of that information. Shanks and Darke [31] found clustering entities into high-level subject areas provides a more meaningful pattern for the data model. Not all paths are equally strong in memory [24]; some may be easier to access. For example, concepts that are <sup>b</sup>closer<sup>Q</sup> together (and therefore have more similar semantic meaning) are easier to retrieve [1].

In a database model, the physical structure of the diagrammatic representation carries meaning through the placement of its entities and the relationships between them. Entities are analogous to propositions or concepts, comprised of clusters of attributes representing a real world construct. Relationships are analogous to the links between propositions. They represent the associations between the entities. In this way, data models can be considered a form of a semantic network.

## 2.2. Gestalt theory and visual representations

While the formation of chunks is important for understandability, the method by which those chunks are represented is also important. Gestalt theory can provide some guidance regarding the understandability of specific visual arrangements. Specifically, the relationship between an organism and its environment is such that the organism is influenced by its role as part of the <sup>b</sup>whole<sup>Q</sup> [40]. An implication of Gestalt theory is that details have more meaning when presented with contextual clues.

Herman et al. [15] argued that Gestalt theory has significant implications for visualization research. There are aspects of diagrams that can reflect these Gestalt principles. Tan and Benbasat [38] cite two relevant characteristics—proximity and continuity. The notion of proximity is that items closer together will be perceived as part of the same group, and therefore more closely related. Connecting lines between discrete items suggests continuity, implying that those items are related. Together, these principles indicate that sets of items, connected by lines and placed close to each other, form a group. Each item in a group is more closely related to other members of its group than members of other groups.

Similarly, Smelcer and Carmel [34] used proximity, along with adjacency and containment, to characterize diagrams. Adjacency is similar to proximity, except that the entities are touching. Containment occurs when one entity is placed within another. All three attributes equate the closeness of entities with their similarity to each other.

## 2.3. The role of recall

Research in information systems has considered both the technical development of database systems and end user issues. Some of this research investigated the ease-of-use of query languages (for a review of this literature, see Ref. [29]). Frequently confounding the results was the use of different data models for systems with different query languages. To control for this, researchers began evaluating data models without using a query language in order to isolate the effect of the data model. In particular, relational models were compared with hierarchical (e.g., Ref. [8]) and network models (e.g., Refs. [16,22]) and different data models were compared for their ease of use as development tools [5].

One method of comparing data models is to investigate their effect on users’ comprehension. Previous researchers searched for suitable methods to evaluate comprehension. Because humans store meaning, and not exact stimuli [30], and because organization is an important component of memory [24], <sup>b</sup>free recall<sup>Q</sup> (an unstructured exercise where subjects recall a set of items) is an effective method of determining how humans have stored information. The strong link between memorization and cognition has been repeatedly confirmed [3], implying that ease of storage (and recall) in memory indicates better comprehension of the underlying meaning of the linked set of information being memorized. This meaning is conveyed in diagrammatic representations through relationships, which provide visual cues which aid recall [12]. Recall has been used to test comprehension in several information systems-related settings. Examples include computer program quality [32], query languages [29], and data model comprehension [8].

Most relevant to our current study is Weber’s [39] use of a recall experiment to determine if subjects make a distinction between entities and attributes in their mental models. He tested subjects’ recall of models to determine if they had internalized the underlying meaning of the model, and also examined the order in which subjects recalled items. From this experiment, he determined that subjects did make a distinction between attributes and entities [39]. This has implications for the way in which people chunk information. Returning to the software knowledge example presented earlier, subjects should recall the larger chunk <sup>b</sup>software knowledge<sup>Q</sup> first, followed by <sup>b</sup>knowledge about word processing packages<sup>Q</sup> and <sup>b</sup>spreadsheet knowledge,<sup>Q</sup> and finally <sup>b</sup>knowledge about Microsoft Word.<sup>Q</sup>

## 3. Hypothesis development

The importance of structure to recall suggests that SSDs should be easier for people to recall than ERDs, because organizing the dimension entities into clusters around the fact table gives a meaningful pattern (and therefore a more easily remembered storage structure) to the diagram. SSDs also strongly adhere to the Gestalt principles of continuity and proximity. The lines between entities imply a direct relationship between the dimension and the fact (continuity), and the physical placement of dimensions around the fact implies relatedness among those elements in the diagram (proximity).

In contrast, the entities in an ERD do not conform to a particular pattern. One result of this less structured arrangement is that continuity and proximity are less strong in ERDs. Two related entities can have any number of entities situated between them (e.g., in Fig. 2, AUTHOR and BOOKSTORE are related, but have two entities between them), making the continuity of the diagram less clear. The increased distance between two related entities also makes understanding the diagram based on proximity more difficult. This leads to hypothesis H1a (stated in the alternative form):

H1a. Subjects will recall SSDs more accurately than ERDs.

As the amount of information increases, the ability to accurately recall all of that information decreases [25]. Chunking becomes more important to recall as the amount of presented information approaches the limits of human memory [24,25]. The more intuitive network structure of an SSD should be especially effective at aiding comprehension when the diagrams are complex. This leads to hypothesis H2a.

H2a. The difference between the recall accuracy of complex and simple diagrams will be greater for ERDs than for SSDs.

Experience also has an influence on recall ability. For example, it has been demonstrated chess masters recall more chess positions than novice chess players [14]. Similarly, experienced programmers recall more program constructs than novice programmers [32]. By extension, experienced ER modelers should have better recall of a data model than novices.

However, because the structure of the SSD is more intuitive and uniform than the structure of an ERD, novice modelers should be able to recognize (and therefore recall) the pattern of the SSD nearly as well as experienced modelers. This leads to hypothesis H3a:

H3a. The difference between the recall accuracy of experienced and novice modelers will be greater for ERDs than for SSDs.

Hypothesis H1a through H3a address the inherent advantages of the SSD over the ERD as a method of conveying the data model to end users, which is graphically represented in Fig. 3.

To more thoroughly understand how the semantic structure of a data model is conveyed through its representation, we analyze the pattern of recall for both the SSDs and the ERDs. Dimension entities are grouped around a fact. The fact table acts as the unifying concept for an SSD. This is analogous to the hierarchical structure of propositions [24], where the grouping of related concepts around a higher, or unifying, category creates the <sup>b</sup>chunks<sup>Q</sup> that have been shown to facilitate greater recall ability [25]. Accordingly, we expect the central fact to be recalled first, followed by the dimensions. Because ERDs lack this pattern, there is no reason to believe that any particular entity will be recalled first. We state our hypotheses as follows:

H4a. There will be a pattern to the recall of the diagram’s entities.

We would expect to accept H4a for SSDs, but not accept the hypothesis for ERDs. Because we have reason to believe that in the case of SSDs the fact table will be recalled first, we can also develop a more specific hypothesis explicitly for SSDs:

![](/api/attachments/HHEQQE9F/fulltext/images/8c8ab61f7b0b04bd54d760c76302c76bd9a395c7c5ffcda5c440610421d2036d.jpg)  
Fig. 3. Research model and hypotheses.

H5a. For SSDs, subjects will recall a fact table before they recall its associated dimension tables.

## 4. Study one: recall comparison

Our first study involves an experimental test of whether subjects can more accurately recall ERDs or SSDs. We measure recall ability by creating two sets of diagrams: a simple and complex ERD, and a simple and complex SSD. Subjects are given a recall task (which is further detailed in a later section), and their accuracy is compared.

As stated previously, it is likely that a person’s experience plays a role in the success of his/her recall of a data model. Because data warehouses are intended to facilitate the delivery of data to all endusers, not just those with extensive database training, it is important to consider groups with different levels of experience. Persons with no previous database knowledge, as much as knowledgeable database users, represent the target user group for a data warehouse. We examine the influence of general database knowledge by comparing the performance of novice data modelers (subjects that have never taken a database class) to more experienced data modelers (subjects who have completed a one semester course on relational database concepts). The hypotheses are tested in a laboratory experiment to compare subjects’ recall accuracy.

## 4.1. Experimental task

The experiment for our first study captured the participants’ accuracy in recalling the diagrammatic representation of the data model for a data warehouse. The problem domain for the experimental task was a university database. This domain was chosen so that the participants would be familiar with the task environment. In a data warehouse environment users are expected to be familiar with the context of that system.

The SSDs and ERDs in this study were designed to convey the same information. Before conducting the experiment, the information content of the two sets of diagrams was checked to make sure it was the same for each diagram type. A set of relevant business questions was constructed and each diagram was tested for its ability to answer those questions. However, due to the fundamentally different structure of the two data models, the number of entities and relationships required to convey this information differed slightly between the ERD and the SSD.

![](/api/attachments/HHEQQE9F/fulltext/images/b4194f53bed27ef23fe7be3a6cd373d515c79ef89a62cfe7108b022b80cb8168.jpg)  
Fig. 4. Simple star schema diagram used in the experiment.

It was necessary to have the same information for each diagram in order to have unambiguous experimental results. If one diagram conveyed more information than the other, differences in information content (rather than diagram type) could cause differences in the level of recall. Two components to the diagrams were measured: entities and relationships. We used four measures to evaluate the level of recall for each data model: the number of correct entities and relationships that a subject recalled, and the number of entities and relationships that a subject added to the model which were not present in the original diagram.

We constructed both sets of diagrams to adhere to the Gestalt principles of proximity and continuity, within the limitations of each diagram type. Continuity is implemented in the diagrams through the connecting lines between entities. As much as possible, entities which were directly related by a relationship (connecting line) between them were placed closer to each other than to other entities with which they had no direct relationships. In addition to being consistent with Gestalt principles, this is also a logical layout for both star schema and entity-relationship diagrams.

For the purposes of this study, we were interested only in entities and the relationships between them. Therefore, there are no attributes in the diagrams. Relationship names also were omitted from both the entity-relationship diagrams and the star schema diagrams. This was done for two reasons. First, for this study we are most concerned with the comprehensibility of the overall data model, not the specific information contained within the database. Second, it is important to create a manageable task for the subjects to perform—recall of entities and attributes would likely prove too difficult a task, regardless of the schema.

![](/api/attachments/HHEQQE9F/fulltext/images/1921965177d57c3347730e4c4e908caade5f3162531ab5b0976eb09d8d1abeb0.jpg)  
Fig. 5. Simple entity relationship diagram used in the experiment.

![](/api/attachments/HHEQQE9F/fulltext/images/357a4fc4087407282c9e91b3e240fd849ee7176b3ee0ed17f198c8e64c9f85dc.jpg)  
Fig. 6. Complex star schema diagram used in the experiment.

Model complexity was defined by the relative number of entities and relationships. The simple SSD had 10 entities and 9 relationships (see Fig. 4), and the complex SSD had 19 entities and 18 relationships (see Fig. 6). The simple ERD had 10 entities and 11 relationships (see Fig. 5), while the complex ERD had 16 entities and 19 relationships (see Fig. 7).

## 4.2. Participants

Two groups of subjects were used for this experiment. The first group was comprised of 109 Master of Science in Information Management (MSIM) students. These students were just completing a semester-long database class in which they had learned to create and use entity-relationship diagrams. The second group was comprised of 141 MBA students with no previous experience with data modeling. There was no difference in the mean ages of the two groups (the average age was 28 for both groups).

![](/api/attachments/HHEQQE9F/fulltext/images/5f4578a14772f22b1fb3372eb10dc67d863495bf21ac98539f92c72671d30838.jpg)  
Fig. 7. Complex entity relationship diagram used in the experiment.

## 4.3. Procedure

Subjects were asked to participate in a recall experiment during class (although participation was voluntary). Each subject was given one of four diagrams—a simple ERD, a simple SSD, a complex ERD, or a complex SSD (either Figs. 4-7) and asked to write his/her name on both the diagram and the sheet of paper on which the diagram was to be reproduced. This allowed the reproductions to be matched to the original diagram.

Subjects were randomly assigned to treatments within classes (see Table 1). There were 111 subjects with simple diagrams (55 with ERDs and 56 with SSDs) and 139 subjects with complex diagrams (67 with ERDs and 72 with SSDs). Subjects were given time to look at the diagram (45 s for simple diagrams and 90 s for complex diagrams). At the end of the allotted time, subjects were asked to turn over the diagram so that they could no longer see it, and then to reproduce as much of it as they could on a separate sheet of paper. There was a time limit to the drawing phase (3 min for simple diagrams, and 4 min for complex diagrams), and subjects completed as much of the diagram as they could in the allotted time.

## 4.4. Results

Four dependent variables were constructed: percent of entities correct, percent of extraneous entities, percent of relationships correct, and percent of extraneous relationships. The number of entities correct was measured as the number of entities a subject correctly labeled on the reproduced diagram. Any entity that a subject labeled on the reproduced diagram that was not on the original diagram was counted as an extraneous entity. To facilitate comparison of simple diagrams with complex diagrams, the counts were converted to percentages. The basis for both percentage correct and percentage extra was the number of entities on the original diagram.

Table 1  
Number of subjects in each cell

<table><tr><td colspan="2"></td><td>SIMPLE</td><td>COMPLEX</td><td>TOTAL</td></tr><tr><td rowspan="2">ERD</td><td>experienced</td><td>17</td><td>32</td><td>122</td></tr><tr><td>novice</td><td>38</td><td>35</td><td></td></tr><tr><td rowspan="2">SSD</td><td>experienced</td><td>23</td><td>37</td><td>128</td></tr><tr><td>novice</td><td>33</td><td>35</td><td></td></tr><tr><td>TOTAL</td><td></td><td>111</td><td>139</td><td></td></tr></table>

Table 2 MANOVA results

<table><tr><td>Factor</td><td>Pillai&#x27;s trace</td><td>p-value</td></tr><tr><td>Diagram</td><td>0.53</td><td>0.00000</td></tr><tr><td>Complexity</td><td>0.38</td><td>0.00000</td></tr><tr><td>Experience</td><td>0.02</td><td>0.25375</td></tr><tr><td>Diagram* Complexity</td><td>0.07</td><td>0.00087</td></tr><tr><td>Diagram* Experience</td><td>0.01</td><td>0.79314</td></tr><tr><td>Complexity* Experience</td><td>0.04</td><td>0.06682</td></tr><tr><td>Diagram* Complexity* Experience</td><td>0.04</td><td>0.05496</td></tr></table>

4 df for the numerator and 240 df for the denominator.

Similarly, the number of relationships correct was measured as the number of relationships a subject correctly drew on the reproduced diagram. Relationships that were drawn on the reproduced diagram but did not exist between entity pairs that did exist on the original diagram were counted as extraneous relationships. Relationships that were drawn between entity pairs that did not exist (either one or both of the entities) on the original diagram were ignored. The reason those relationships were not counted is that the <sup>b</sup>error<sup>Q</sup> in recall was already included in the count of extraneous entities. To count them again as extraneous relationships would count the error twice. Again, to compare simple and complex diagrams, the counts were converted to percentages. The basis for percentage correct and percentage extra was the number of relationships on the original diagram.

A MANOVA was used as the first step to test the hypotheses specified in the previous section. Because there are significant variations in the group correlations, Pillai’s trace was used as the test statistic for differences between levels of the independent variables. When there are departures from the underlying assumptions of MANOVA, Pillai’s trace is the most conservative and robust test statistic to use [37]. Three factors were used, with two levels each: diagram type (SSD or ERD), diagram complexity (simple or complex), and the experience level of the subject (novice or experienced).

Table 3  
Individual analysis of variance results reported as computed means

<table><tr><td>Variable</td><td>Mean Value of Percentage Results (%)</td><td>p-value</td></tr><tr><td colspan="3">Entities Correct</td></tr><tr><td>Diagram (Diag)</td><td>ERD: 75.86; SSD: 78.49</td><td>0.23329</td></tr><tr><td>Complexity (Comp)</td><td>S: 89.38; C: 64.97</td><td>0.00000**</td></tr><tr><td>Experience (Exp)</td><td>N: 75.33; E: 79.02</td><td>0.09606</td></tr><tr><td>Diag* Comp</td><td>ERD,S: 88.45; ERD,C: 63.26; SSD,S: 90.31; SSD,C: 66.67</td><td>0.72545</td></tr><tr><td>Diag* Exp</td><td>ERD,N: 74.77; ERD,E: 76.94; SSD,N: 75.89; SSD,E: 81.88</td><td>0.49376</td></tr><tr><td>Comp* Exp</td><td>S,N: 89.18; SE: 89.58; C,N: 61.48; C,E: 68.45</td><td>0.13707</td></tr><tr><td>Diag* Comp* Exp</td><td>ERD,S,N: 90.79; ERD,S,E: 86.11; ERD,C,N: 58.75; ERD,C,E: 67.77; SSD,S,N: 87.58; SSD,S,E: 93.04; SSD,C,N: 64.21; SSD,C,E: 69.13</td><td>0.10749</td></tr><tr><td colspan="3">Entities Extra</td></tr><tr><td>Diagram (Diag)</td><td>ERD: 4.84; SSD: 7.36</td><td>0.00746*</td></tr><tr><td>Complexity (Comp)</td><td>S: 4.39; C: 7.80</td><td>0.00032**</td></tr><tr><td>Experience (Exp)</td><td>N: 5.58; E: 6.61</td><td>0.27065</td></tr><tr><td>Diag* Comp</td><td>ERD,S: 3.80; ERD,C: 5.88; SSD,S: 4.99; SSD,C: 9.73</td><td>0.15473</td></tr><tr><td>Diag* Exp</td><td>ERD,N: 4.53; ERD,E: 5.15; SSD,N: 6.64; SSD,E: 8.07</td><td>0.66569</td></tr><tr><td>Comp* Exp</td><td>S,N: 4.61; SE: 4.18; C,N: 6.56; C,E: 9.05</td><td>0.11878</td></tr><tr><td>Diag* Comp* Exp</td><td>ERD,S,N: 3.16; ERD,S,E: 4.44; ERD,C,N: 5.89; ERD,C,E: 5.86; SSD,S,N: 6.06; SSD,S,E: 3.91; SSD,C,N: 7.22; SSD,C,E: 12.23</td><td>0.02391</td></tr><tr><td colspan="3">Relationships Correct</td></tr><tr><td>Diagram (Diag)</td><td>ERD: 61.67; SSD: 92.42</td><td>0.00000**</td></tr><tr><td>Complexity (Comp)</td><td>S: 86.27; C: 67.82</td><td>0.00000**</td></tr><tr><td>Experience (Exp)</td><td>N: 75.25; E: 78.84</td><td>0.11532</td></tr><tr><td>Diag* Comp</td><td>ERD,S: 74.75; ERD,C: 48.97; SSD,S: 98.17; SSD,C: 86.67</td><td>0.00241**</td></tr><tr><td>Diag* Exp</td><td>ERD,N: 59.55; ERD,E: 63.79; SSD,N: 90.95; SSD,E: 93.89</td><td>0.77374</td></tr><tr><td>Comp* Exp</td><td>S,N: 84.90; SE: 87.65; C,N: 65.61; C,E: 70.03</td><td>0.71365</td></tr><tr><td>Diag* Comp* Exp</td><td>ERD,S,N: 72.49; ERD,S,E: 76.26; ERD,C,N: 46.62; ERD,C,E: 51.32; SSD,S,N: 97.31; SSD,S,E: 99.03; SSD,C,N: 84.60; SSD,C,E: 88.74</td><td>0.87024</td></tr><tr><td colspan="3">Relationships Extra</td></tr><tr><td>Diagram (Diag)</td><td>ERD: 16.30; SSD: 0.47</td><td>0.00000**</td></tr><tr><td>Complexity (Comp)</td><td>S: 8.38; C: 8.39</td><td>0.99941</td></tr><tr><td>Experience (Exp)</td><td>N: 8.99; E: 7.78</td><td>0.40642</td></tr><tr><td>Diag* Comp</td><td>ERD,S: 16.60; ERD,C: 15.99; SSD,S: 0.17; SSD,C: 0.78</td><td>0.67681</td></tr><tr><td>Diag* Exp</td><td>ERD,N: 17.26; ERD,E: 15.33; SSD,N: 0.72; SSD,E: 0.23</td><td>0.62356</td></tr><tr><td>Comp* Exp</td><td>S,N: 8.18; SE: 8.59; C,N: 9.80; C,E: 6.97</td><td>0.26914</td></tr><tr><td>Diag* Comp* Exp</td><td>ERD,S,N: 16.03; ERD,S,E: 17.17; ERD,C,N: 18.50; ERD,C,E: 13.49; SSD,S,N: 0.34; SSD,S,E: 0.00; SSD,C,N: 1.11; SSD,C,E: 0.45</td><td>0.31937</td></tr><tr><td colspan="3">Key</td></tr><tr><td>SSD</td><td>Star-schema diagram</td><td></td></tr><tr><td>ERD</td><td>Entity-relationship diagram</td><td></td></tr><tr><td>C</td><td>Complex</td><td></td></tr><tr><td>S</td><td>Simple</td><td></td></tr><tr><td>N</td><td>Novice</td><td></td></tr><tr><td>E</td><td>Experienced</td><td></td></tr></table>

<sup>T</sup> Significant at the 5% level with the Bonferroni adjustment which requires a p-value <sup>b</sup> 0.0125.  
<sup>TT</sup> Significant at the 1% level with the Bonferroni adjustment which requires a p-value <sup>b</sup> 0.0025.

![](/api/attachments/HHEQQE9F/fulltext/images/f2b2a3b89dc049158edf7483354c5a02b2b3b97a0556791d39c3dd80e0980823.jpg)

![](/api/attachments/HHEQQE9F/fulltext/images/171a88a98ea4df3cadd77b09fc748b6060247909d65331eb806b74ffee920d11.jpg)  
Fig. 8. Percent of entities correctly included on diagrams.

The results from the MANOVA are shown in Table 2, which shows a clear difference among the groups for at least one of the four dependent variables. Because the null hypothesis in the MANOVA was rejected, a series of univariate ANOVAs were performed. Because of the unequal cell sizes (see Table 1), this data is analyzed using the general linear model.

Table 3 shows the results of the individual analysis of variance tests using the computed means. Because four tests were performed on the data, the experimentwise alpha of 0.05 was adjusted to 0.0125 using the Bonferroni procedure [19]. Hereafter, the term <sup>b</sup>significant<sup>Q</sup> will be used only when the p-value is less than 0.0125.

Figs. 8-11 graphically illustrate the results for the four dependent variables which serve as measures for recall accuracy. While evidence was not found to support hypothesis H1a through H3a for <sup>b</sup>entities correct<sup>Q</sup> and <sup>b</sup>entities extra,<sup>Q</sup> strong evidence was found to support hypothesis H1a and H2a for <sup>b</sup>relationships correct<sup>Q</sup> and strong evidence was found to support hypothesis H1a for <sup>b</sup>relationships extra.<sup>Q</sup> Fig. 8 graphically illustrates the results for <sup>b</sup>entities correct.<sup>Q</sup> No interactions are significant at the 0.1 level, and diagram complexity is the only significant main effect for <sup>b</sup>entities correct.<sup>Q</sup> For <sup>b</sup>entities extra,<sup>Q</sup> both diagram complexity and diagram type are significant, but diagram type is significant in the wrong direction. Fig. 9 graphically illustrates these results. Therefore, looking at how accurately subjects recalled entities, we do not find evidence to support hypothesis H1a through H3a.

![](/api/attachments/HHEQQE9F/fulltext/images/7b1a23ead31d2114e176ba4ab188d7bc512a440a365983c604bc4c441ff4ecc3.jpg)

For <sup>b</sup>relationships correct,<sup>Q</sup> diagram type, diagram complexity, and the interaction between diagram type and diagram complexity were significant at the 0.01 level. Fig. 10 illustrates these results. Based on these results, alternative hypotheses H1a and H2a can be accepted. On average 98.17% of relationships were correctly identified for simple SSDs, and 86.67% were correctly identified for complex SSDs. For ERDs, on the other hand, 74.75% were correctly identified for simple diagrams and only 48.97% were correctly identified for complex diagrams. This provides strong support for the contention that SSDs are easier to understand than ERDs, and further indicates that SSDs are most beneficial when working with complex data models.

![](/api/attachments/HHEQQE9F/fulltext/images/b0a98891f1ca189f9a177e2983c8fbe6949d53effaf7d0409e0a287bc1540b35.jpg)  
Fig. 9. Percent of extra entities added to diagrams.

![](/api/attachments/HHEQQE9F/fulltext/images/5cc6720433dd3e9e2bf2358ccab6d2aea274273ee073de2a917341628d52b87a.jpg)

![](/api/attachments/HHEQQE9F/fulltext/images/0ee5ec43ac8dfa13271a0355c722898e7a89c3166638d3bfbe62f51f634f3d70.jpg)  
Fig. 10. Percent of relationships correctly included on diagrams.

For <sup>b</sup>relationships extra,<sup>Q</sup> diagram type was significant at the 0.0001 level, but the interaction between diagram type and complexity was not significant. Fig. 11 illustrates this result. Based on this, only alternative hypothesis H1a can be accepted. On average, 16.3% of the relationships on the reproduced ERDs were extraneous while only 0.47% of the relationships on the SSDs were extraneous. This is further evidence that the underlying structure of an SSD is recalled more accurately.

Two interesting things to note about the <sup>b</sup>relationships extra<sup>Q</sup> data are that the main effect of complexity was not significant, and that the interaction between diagram type and diagram complexity was not significant. This can be explained by how relationships extra were counted. In the reproduced diagram, a relationship was counted as extraneous only if it was between two entities that exist in the original diagram and was not present on the original diagram. Though there are more entities in the complex diagram, a single entity does not participate in more relationships than in the simple ERD. Similarly, in the complex SSD a single entity does not participate in more relationships than in the simple SSD. Thus, given two correct entities, it is not more difficult to get the relationships correct in the complex diagram than it is in the simple diagram.

![](/api/attachments/HHEQQE9F/fulltext/images/5d5db9c657c273d5e6592ade640e9c9854018b282cb1ff2c1c7a413843f29c5c.jpg)

## 4.5. Discussion

The results of study one provide support for the contention that SSDs are more effective than ERDs at conveying the meaning of the underlying data model. The implication of this is that the star schema is more easily understood by end users and may make a more effective system for delivering data to those users.

![](/api/attachments/HHEQQE9F/fulltext/images/8a62bb9fbd39bfe231fac1e9d1c3c69faea7e7437b5d937c93cb233e0f436f81.jpg)  
Fig. 11. Percent of relationships added to diagrams.

Evidence regarding the differences between SSDs and ERDs was strongest when looking at the number of relationships correctly recalled and the number of extra relationships added (see Table 4 for a summary of hypotheses and their results). In order to successfully use a database, it is necessary to accurately identify the relationships between the entities. In general, a database with few relationships is more limited in the information that can be retrieved from it than a database with many relationships. If users are unaware of relationships that exist in a database, they run the risk of missing important information that otherwise could be extracted from the database. Subjects in this experiment were able to recall relationships in SSDs much more accurately than in ERDs. This was especially true for complex diagrams, indicating that the benefits of SSDs over ERDs is greatest when the diagram is complex. This implies that SSDs help most when the help is most needed. Because subjects understand the relationships in an SSD, they should also be able to understand what information can be extracted from a database constructed using a star schema.

For entities correct, subjects did not do significantly better with SSDs than ERDs. One possible explanation for this is that they were so familiar with the scenario that they could remember approximately the same percentage of entities regardless of diagram type.

It is surprising that the subjects actually added more entities to the SSDs than they did to the ERDs. There were five dimension tables around some fact tables, but only four around others. The extra entities were most often added to fact tables with only four dimension tables and most often added by experienced modelers. In other words, experienced modelers appeared to impose a pattern that made all fact tables have the same number of dimension tables. This implies that the subjects were seeking structure in the data model. Further examination of the names of the added entities revealed that they were reasonable dimensions that a user might expect to find associated with that fact table. That is, subjects added entities that logically could have been part of the database. This observation, although anecdotal, provides evidence that the meaning of the star schema was conveyed to the users.

Also interesting is the fact that experience with ERDs was not significant for any of the dependent variables, and neither was any interaction involving modeling experience. SSDs were equally beneficial to novices and experienced ERD modelers. Not only did the novices, those subjects who most closely represent non-technical managerial users, recall the SSDs better, but so did the subjects who more closely represent technical users.

## 5. Study two: recall order comparison

The results of our first study demonstrate that, with respect to relationships, SSDs are recalled more accurately than ERDs. In our second study we test if subjects have an understanding of the inherent structure of a star schema diagram. Specifically, we look at the order and pattern in which the entities were recalled to determine whether a distinction was made between fact tables and dimension tables. The ability to make a distinction between facts and dimensions indicates that subjects understand the inherent structure of a star schema diagram.

Table 4  
Summary of results for study one

<table><tr><td colspan="5">Recall of entities and relationships</td></tr><tr><td></td><td>Entities correct</td><td>Entities extra</td><td>Relationships correct</td><td>Relationships extra</td></tr><tr><td>H1a: Recall accuracy of SSDs&gt;ERDs</td><td>Not supported</td><td>Not supported</td><td>Supported</td><td>Supported</td></tr><tr><td>H2a: Difference in recall accuracy between simple and complex for ERDs&gt;SSDs</td><td>Not Supported</td><td>Not Supported</td><td>Supported</td><td>Not supported</td></tr><tr><td>H3a: Difference in recall accuracy between novice and experienced for ERDs&gt;SSDs</td><td>Not Supported</td><td>Not Supported</td><td>Not Supported</td><td>Not Supported</td></tr></table>

## 5.1. Experimental task

While performing the recall task of the first study, subjects were asked to record the order in which they recalled entities (i.e., the first entity they recalled was to be labeled <sup>b</sup>1,<sup>Q</sup> the second was to be labeled <sup>b</sup>2,<sup>Q</sup> etc.). The data must be analyzed separately for simple and complex diagrams because of the difference in the number of entities in each diagram type.

## 5.2. Results

To determine whether there is a pattern to the recall of entities, we tested whether each entity is equally likely to be recalled first (hypothesis H4a). Descriptive statistics for the order in which entities were recalled on simple diagrams are reported in Table 5. The entities most frequently recalled first on the simple SSD were the fact tables (COURSE or JOB). For novice modelers, COURSE or JOB was the first entity recalled in 94.6% of the cases. For experienced modelers, COURSE or JOB was the first entity recalled in 98.7% of the cases. Further, the subjects almost always recalled the fact tables at some point. Only one experienced subject (out of 22) and one novice subject (out of 30) failed to recall both fact tables, and both of those subjects recalled one of the fact tables.

For the simple entity relationship diagrams, it appears that subjects recalled the entities from top to bottom and left to right. DEPARTMENT or MAJOR were the first entities recalled in the vast majority of cases. Table 5 shows that over 89% of novices recalled DEPARTMENT or MAJOR as the first entity, and over

Entities from simple diagrams that were recalled most frequently in first position

<table><tr><td></td><td>Star schema diagrams (COURSE or JOB)</td><td>Entity-relationship diagrams (DEPARTMENT or MAJOR)</td></tr><tr><td>Novice</td><td>94.6%</td><td>89.02%</td></tr><tr><td>Experienced</td><td>98.7%</td><td>81.25%</td></tr></table>

Table 6  
Results of exact test of the hypothesis p = 0.10 for simple diagrams

<table><tr><td></td><td colspan="2">Star schema diagrams</td><td colspan="2">Entity-relationship diagrams</td></tr><tr><td></td><td>Proportion of times COURSE recalled first</td><td>p-value</td><td>Proportion of times MAJOR recalled first</td><td>p-value</td></tr><tr><td>Novice</td><td>21/31</td><td>0.00000</td><td>28/34</td><td>0.00000</td></tr><tr><td>Experienced</td><td>15/21</td><td>0.00000</td><td>9/16</td><td>0.00001</td></tr></table>

The numbers in Table 6 differ slightly from those in Table 1 because not all subjects recorded the order in which the entities were recalled.

81% of experienced modelers recalled DEPARTMENT or MAJOR as the first entity.

To test hypothesis H4a (that there is a pattern to the recall of the entities), an exact test (using the binomial distribution, with p as the proportion of times an entity is recalled first) was performed for the null hypothesis that $\pi { = } 0 . 1 0$ (see Table 6). This value of p was chosen bacause there were ten entities on each of the simple diagrams (SSD and ERD). If each one is equally likely to be recalled first, then $\pi = 0 . 1 0 .$ . The test determines whether a specific frequency is significantly different from p.

For the ER diagram, MAJOR (the left-most entity) was recalled first most frequently. For the SS diagram, COURSE (the left-most fact table) was recalled first most frequently. By picking the entity that was recalled most frequently to test against $\pi { = } 0 . 1 0$ we are biasing the results in favor of rejecting the null hypothesis. We can correct for this bias by using the Bonferroni correction where the experiment-wise alpha is $\alpha / 1 0$ (the per comparison alpha divided by the number of comparisons). Even with this correction, all p-values are highly significant $( p { < } 0 . 0 0 0 0 1 )$ , allowing us to accept hypothesis H4a for both ERDs and SSDs. This indicates that both ERDs and SSDs are not recalled at random.

Descriptive statistics that address whether the fact tables are recalled before their associated dimension tables (hypothesis H5a) are presented in Table 7 for simple diagrams. Over 93% of novice subjects recalled COURSE before any of its dimension tables, and almost 86% of experienced subjects did the same. The percentage of subjects who recalled the fact table JOB before its dimension tables also was calculated. Over 95% of experienced subjects recalled JOB before its dimension tables, and 100% of novice subjects recalled JOB before its dimension tables. STUDENT is a conforming (or shared) dimension table, and therefore was not counted as a dimension table for either COURSE or JOB. COURSE thus has four dimension tables, and JOB has three dimension tables.

Table 7  
Proportion of time that fact table from simple SSD (COURSE or JOB) was recalled before their associated dimension tables

<table><tr><td></td><td>COURSE recalled before associated dimension tables</td><td>p-value</td><td>JOB recalled before associated dimension tables</td><td>p-value</td></tr><tr><td>Novice</td><td>28/30</td><td>0.00000</td><td>29/29</td><td>0.00000</td></tr><tr><td>Experienced</td><td>18/21</td><td>0.00000</td><td>21/22</td><td>0.00000</td></tr></table>

To test hypothesis H5a, an exact test was done on the hypothesis p =0.20 for the COURSE table, and $\pi { = } 0 . 2 5$ for the JOB table. These values of p were chosen because if COURSE and its four dimension tables are equally likely to be recalled, then the probability that any one table will be recalled first is 0.20. Similarly, if JOB and its three dimension tables are equally likely to be recalled, then the probability that any one table will be recalled first is 0.25. All pvalues were highly significant $( p < 0 . 0 0 0 0 1$ , reported in Table 7), resulting in the acceptance of this hypothesis.

For the complex diagrams, 96.6% of subjects recalled the fact tables COURSE, DEGREE, JOB, SCHOLARSHIP, before their associated dimension tables. This highly significant result $\scriptstyle ( p < 0 . 0 0 0 0 0 0 .$ reported in Table 8), provides further evidence allowing us to accept alternative hypothesis H4a for SSDs.

Looking at the complex ERD, it is difficult to identify the left-most entity. It is, however, easy to identify the left and right sides of the diagram. Hence instead of asking what was the first entity recalled, the question we asked was <sup>b</sup>from which side of the diagram did the first two entities recalled come?<sup>Q</sup> The first two entities were selected because this was the greatest number of entities that could be guaranteed to come from a single side of the complex diagram. In other words, reporting that the location of the first two entities is from the same side of the diagram provides more convincing evidence that one side was recalled before the other. Using three or more entities could provide ambiguous results because there are combinations of three entities that cross the half-way point of the complex diagram. It was necessary to perform a multinomial test as there were three possible outcomes for the question: were the first two entities recalled from the left side of the diagram, from the right side of the diagram, or from both sides? The hypothesis is that p = 0.33. The results are reported in Table 9, and the alternative hypothesis H4a for ERDs is accepted with a p-value of 0.00007.

Proportion of time that fact table or conforming table from complex SSD was recalled before its associated dimension tables

<table><tr><td></td><td>p-value</td></tr><tr><td>28/29</td><td>0.00000</td></tr></table>

Table 9  
Multinomial test that the first two entities are recalled from the left half of the complex ERD before entities from the right side or from both sides

<table><tr><td>Left side first</td><td>Right side first</td><td>Both sides</td><td>p-value</td></tr><tr><td>17/25</td><td>6/25</td><td>2/25</td><td>0.00007</td></tr></table>

## 5.3. Discussion

A summary of the hypotheses and their results are included in Table 10. It is clear that subjects recalled the entities from the SSD in a different order than they recalled the entities from the ERD. The subjects who were given the dimensional model clearly recalled the fact tables before their associated dimension tables. With the ERDs, while not an initial hypothesis, it appears that subjects recalled the entities from left to right, and not at random. We do not believe that this reflects an inherent pattern in the diagram (as was the case for SSDs). A more likely explanation for this result is that people are conditioned to scan from left to right, consistent with how English is read.

Summary of results for Study Two

<table><tr><td colspan="2">Examination of recall patterns</td></tr><tr><td>H4a: There will be a pattern to the recall of the diagram&#x27;s entities</td><td>Supported (for both ERDs and SSDs)</td></tr><tr><td>H5a: For SSDs, subjects will recall a fact table before its associated dimension tables</td><td>Supported</td></tr></table>

On both simple and complex SSDs, subjects recalled fact tables before dimension tables. This result is particularly striking because none of the subjects were experienced with dimensional modeling. Without any outside reinforcement, the pattern was strong enough to be imprinted and recalled. These results strongly support the idea that subjects intuitively make a distinction between fact tables and dimension tables. Because subjects recalled the higher level entities before adding the detail level entities, it is likely that they stored the SSDs in memory in a hierarchical structure.

That subjects clearly impose a structure on the star schemas may be the reason they are able to recall the relationships of the SSDs more accurately than those of the ERDs. Because organization is a necessary precondition for comprehension we can conclude from a memory storage structure perspective that SSDs are easier to understand than ERDs.

## 6. Limitations and future research

As with most studies, our study has several limitations. While we do not believe that the limitations of this study compromise the importance of our findings, they do point to opportunities for future research on this subject. These opportunities are also discussed.

Because student subjects were used, the issue of external validity is a possible limitation. The results here are generalizable, strictly speaking, only to student subjects recalling two different versions of an ERD and two different versions of a SSD. However, we believe the student subjects are suitable surrogates for a general user population. First, there is no reason to believe our subject pool had greater or lesser ability to perform the task than actual users of data warehouses. In addition, by selecting a school enrollment database, we chose a domain that would be familiar to the student subjects. This was done to maximize the realism of the task, because users of databases in organizations are generally familiar with the domain of the system.

Another possible limitation is the modeling expe rience of our subjects. No significant difference was found between experienced and inexperienced modelers. This could be because our experienced subjects were simply not <sup>b</sup>experienced<sup>Q</sup> enough. It is still reasonable to believe that experience and proficiency are important factors in the recognition of patterns. Future studies could address this by selecting subjects with more extensive database training.

We also did not use an external reward mechanism that is monotonic in performance. Many economists [28,35,36] argue that incentives are important in encouraging subjects to behave rationally in an experimental setting. Nevertheless, the evidence regarding the influence of incentives in recall experiments is conflicting. Nilsson [26] tested performance in free recall experiments and found that incentives did not make a difference. In addition, Camerer and Hogarth [9] found that intrinsic motivation reduces the effect of financial incentives. The students in our study were masters students that had chosen to enroll in an information systems course, and hence would seem to be highly motivated to perform well. It is, however, possible that the use of incentives could have changed our results. If ERDs are truly a great deal more difficult to recall than SSDs, subjects may have given up when trying to recall the ERD. This would depress the ERD score, resulting in a greater difference between recall of the two diagrams than what otherwise might have existed if we had rewarded performance.

The issue of incentives provides an interesting area for future research in information systems. Presently, it is not clear when incentives are and are not needed in information systems research. In our experiment, the use of an incentive may have been unnatural, because rewarding performance based on the correct recall of the diagram would not represent a realistic job task. For many years there has been a distinction between behavioral and experimental economics, and a similar distinction may be useful for information systems.

The fact that only two types of ERDs and SSDs were used in our experiment also provides an opportunity for future research. Because the purpose of this research stream is to test if the star schema diagram is easier to understand than a traditional entity-relationship diagram, the influence of the diagrammatic structure of database schemas on recall could be investigated using different diagrams, different domains, and different subjects. Consistency of results across these factors would provide further evidence of the usefulness of the star schema for data delivery to end-users.

Another important direction for future research in this area is the testing of the relative comprehension and usefulness of these diagrams using metrics other than recall. While recall is a useful measure of comprehension, the use of more explicit measures (such as the ability to answer questions regarding the data in a particular diagram) would be an important way to provide additional support for our findings. Additionally, because of claims that the star schema is especially appropriate for end-user delivery of data, studies regarding user satisfaction with the two diagrammatic representations would be useful.

## 7. Conclusions

The two studies described in this paper provide empirical evidence supporting the viability of the dimensional data warehouse as a data delivery mechanism to the end user. The results of this research strongly suggest that dimensional diagrams are inherently more understandable than entity relationship diagrams. The implication of this is that data warehouses built using star schemas will serve as superior tools for decision support. Users of the data warehouse can leverage their intuitive understanding of the structure of the star schema to query the database directly. This can reduce their reliance on information technology professionals for the retrieval of information from the data warehouse. It can also reduce the need for custom-built <sup>b</sup>front-end<sup>Q</sup> applications that essentially package pre-constructed queries to be run by the user. The result is that users ultimately have more flexibility in the information they can retrieve from the data warehouse, while at the same time requiring less technical support.

We have demonstrated this inherent superiority of the star schema over traditional entity-relationship diagrams in two ways. First, we showed that subjects are able to recall SSDs more accurately than ERDs. This higher level of recall implies that the underlying data model of the SSD is internalized more effectively. Second, we show that SSDs are recalled in a manner consistent with their underlying structure (i.e., fact tables are recalled first, followed by their associated dimension tables).

Because the diagrammatic representation of a system has an influence on the ability of users to recognize the information contained within that system [20], comprehension of the underlying data model supports the ability of the users to retrieve the information they require. This inherent understandability implies that users can more easily conceptualize the relationships between entities, and therefore may more accurately query the database. Having an inaccurate or an incomplete understanding of the relationships in a data model will restrict the ability of users to see possible queries that can be performed against the database.

The patterned, structured format of the SSD led to improved understandability, as measured in this study by the recall of entities and relationships. This is consistent with semantic network theory [1,10,24], which indicates that arranging a diagram in a meaningful network of linked nodes facilitates comprehension of that diagram. The difference in recall between SSDs and ERDs was especially pronounced for the relationships in complex diagrams (86.67% of correct relationships versus 48.97%). This indicates that the SSD is more <sup>b</sup>scalable<sup>Q</sup> with regard to comprehension. In other words, as the data model increases in complexity, the gap in understandability between the data models becomes increasingly pronounced.

Another important finding of our study is that the central <sup>b</sup>fact<sup>Q</sup> entity is recalled before the <sup>b</sup>dimension<sup>Q</sup> entities of the star schema. This is evidence that users make distinctions between entities and dimensions, much in the same way as previous research has shown users make distinctions between attributes and entities [39]. Furthermore, the pattern of recall of the entities indicates the subjects’ understanding of the underlying structure of the schema. This is in sharp contrast to subjects’ pattern of recall when given an ERD. For ERDs, subjects’ recalled entities simply from top to bottom and left to right which has no meaningful correspondence to the structure of the diagram itself. Together, these findings provide compelling evidence to support Kimball’s [18] assertion that the dimensional model is a more viable way to convey the contents and structure of a data warehouse to end users than the relational model.

This research offers contributions for both academics and practitioners. For academics, this paper represents a new line of research in data warehousing. Instead of looking at the issue of usability from a technical or managerial perspective, we have chosen to focus on usability of the underlying data model. Building upon this, future research should consider whether these differences in recall translate to better performance on decision-making tasks which require a deep level of comprehension regarding the contents and structure of the data warehouse.

For practitioners, this paper provides empirical evidence to support the use of the dimensional model as a tool for end-user delivery of data in a data warehouse. If the star schema is understandable by end users, then they are more likely to be able to construct ad-hoc queries against a data warehouse. This greatly increases the potential for flexible analysis of these data stores, reducing reliance on custom-built applications.

## References

[1] J.R. Anderson, Cognitive Psychology and its Implications, 3rd ed., W.H. Freeman and Co., New York, 1990.

[2] J. Ang, T.S.H. Teo, Management issues in data warehousing: insights from the housing and development board, Decision Support Systems 29 (1) (2000) 11– 20.

[3] M.H. Ashcraft, Human Memory and Cognition, Scott, Foresman and Co., Glenview, IL, 1989.

[4] A. Baddeley, The magical number seven: still magic after all these years?, Psychological Review 101 (2) (1994) 353–356.

[5] D. Batra, J.A. Hoffer, R.P. Bostrom, Comparing representations with relational and EER models, Communications of the ACM 33 (2) (1990) 126– 139.

[6] D.J. Berndt, A.R. Hevner, J. Studnicki, The catch data warehouse: support for community health care decisionmaking, Decision Support Systems 35 (3) (2003) 367– 384.

[7] J. Bischoff, T. Alexander, Data Warehouse: Practical Advice from the Experts, Prentice-Hall, Upper Saddle River, NJ, 1997.

[8] M. Brosey, B. Shneiderman, Two experimental comparisons of relational and hierarchical database models, International Journal of Man–Machine Studies 10 (5) (1978) 625–637.

[9] C.F. Camerer, R.M. Hogarth, The effects of financial incentives in experiments: a review and capital–labor–production framework, Journal of Risk and Uncertainty 19 (1–3) (1999) 7– 42.

[10] A.M. Collins, M.R. Quillian, How to make a language user, in: E. Tulving, W. Donaldson (Eds.), Organization of Memory, Academic Press, NewYork, 1972, pp. 309– 351.

[11] B.L. Cooper, H.J. Watson, B.H. Wixom, D.L. Goodhue, Data warehousing supports corporate strategy at First American Corporation, MIS Quarterly 24 (4) (2000) 547– 567.

[12] G. DeSanctis, Computer graphics as research aids: directions for research, Decision Sciences 15 (4) (1984) 463 – 487.

[13] K. Glassey, Seducing the end user, Communications of the ACM 41 (9) (1998) 62–69.

[14] R. Hastie, R.M. Dawes, Rational Choice in an Uncertain World: Psychology of Judgment and Decision Making, Sage, Thousand Oaks, CA, 2001.

[15] I. Herman, G. Melancon, M.S. Marshall, Graph visualization and navigation in information visualization: a survey, IEEE Transactions on Visualization and Computer Graphics 6 (1) (2000) 24– 43.

[16] J.A. Hoffer, An empirical investigation into individual differences in database models, in: M. Ginzberg, C.A. Ross (Eds.), Proceedings of the Third International Conference on Information Systems, Ann Arbor, MI, 1982, pp. 153 – 167.

[17] W.H. Inmon, C. Imhoff, R. Sousa, Corporate Information Factory, Wiley, New York, 1998.

[18] R. Kimball, A dimensional modeling manifesto, DBMSmag.- com, http://www.dbmsmag.com/9708d15.html (1997).

[19] R.E. Kirk, Experimental Design: Procedures for the Behavioral Sciences, 2nd ed., Brooks/Cole, Belmont, CA, 1982.

[20] J.H. Larkin, H.A. Simon, Why a diagram is (sometimes) worth ten thousand words, Cognitive Science 11 (1) (1987) 65– 99.

[21] R.L. Leitheiser, S.T. March, The influence of database structure representation on database system learning and use, Journal of Management Information Systems 12 (4) (1996) 187– 213.

[22] F.H. Lochovsky, D.C. Tsichritzis, User performance considerations in DBMS selection, Proceedings of ACM SIGMOD, 1997, pp. 128–134 (Toronto, Ontario, Canada).

[23] K. Loeb, A. Rai, A. Ramaprasad, S. Sharma, Design, development and implementation of a global information warehouse: a case study at IBM, Information Systems Journal 8 (4) (1998) 291– 311.

[24] G. Mandler, Organization in Memory, in: K.W. Spence, J.T. Spence (Eds.), The Psychology of Learning and Motivation: Advances in Research and Theory, vol. 1, 1967, pp. 327– 372.

[25] G.A. Miller, The magical number seven, plus or minus two: some limits on our capacity for processing information, Psychology Review 63 (2) (1956) 81– 97.

[26] L.-G. Nilsson, Motivated Memory: Dissociation Between Performance Data and Subjective Reports, Psychological Research 49 (2–3) (1987) 183– 188.

[27] C. Parkes, Data warehousing: the economy isn’t the only reason the data warehouse is stumbling, Enterprise Systems (2002). (www.esj.com/Departments/article.asp?EditorialsID=51).

[28] C.R. Plott, Rational choice in experimental markets, in: R.M. Hogarth, M.W. Reder (Eds.), Rational Choice: The Contrast Between Economics and Psychology, University of Chicago Press, 1987.

[29] P. Reisner, Human factors studies of database query languages: a survey and assessment, Computing Surveys 13 (1) (1981) 13– 31.

[30] J.S. Sachs, Recognition memory for syntactic and semantic aspects of connected discourse, Perception & Psychophysics 2 (9) (1967) 437–442.

[31] G. Shanks, P. Darke, Understanding corporate data models, Information and Management 35 (1) (1999) 19– 30.

[32] B. Shneiderman, Measuring computer program quality and comprehension, International Journal of Man–Machine Studies 9 (4) (1977) 465– 478.

[33] H.A. Simon, How big is a chunk?, Science 183 (4124) (1974) 482–488.

[34] J.B. Smelcer, E. Carmel, The effectiveness of different representations for managerial problem solving: comparing tables and maps, Decision Sciences 28 (2) (1997) 391 – 420.

[35] V.L. Smith, Rational choice: the contrast between economics and psychology, Journal of Political Economy 99 (4) (1991) 877–897.

[36] V.L. Smith, J.M. Walker, Rewards, experience and decision costs in first price auctions, Economic Inquiry 31 (1993) 237–244.

[37] B. Tabachnick, L. Fidell, Using Multivariate Statistics, Harper Collins, New York, 1983.

[38] J.H.K. Tan, I. Benbasat, The effectiveness of graphical presentation for information extraction: a cumulative experimental approach, Decision Sciences 24 (1) (1993) 167–191.

[39] R. Weber, Are attributes entities? a study of database designers’ memory structures, Information Systems Research 7 (2) (1996) 137– 162.

[40] M. Wertheimer, Gestalt theory, Social Research 11 (1924) (http://gestalttheory.net/archive/wert1.html).

[41] B.H. Wixom, H.J. Watson, An empirical investigation of the factors affecting data warehousing success, MIS Quarterly 25 (1) (2001) 17–41.

Karen Corral is Assistant Professor of Computer Information Systems in the W.P. Carey School of Business at Arizona State University. She holds a BA in English from the University of Michigan, an MS in Computer Information Systems from Arizona State University, and a PhD in Business Administration from Arizona State University. Her research interests are in the area of data and knowledge management as related to decision support. Her work has been published in journals such as Communications of the ACM, Information Systems Frontiers, and Decision Support Systems.

David Schuff is Assistant Professor of Management Information Systems in the Fox School of Business and Management at Temple University. He holds a BA in Economics from the University of Pittsburgh, an MBA from Villanova University, an MS in Information Management from Arizona State University, and a PhD in Business Administration from Arizona State University. His research interests include the strategic use of information systems, the assessment of total cost of ownership in large networked organizations, and data warehousing. His work has been published in journals such as Communications of the ACM, Information Systems Journal, and the European Journal of Operational Research.

Robert D. St. Louis is a Professor in the Information Systems Department at the W. P. Carey School of Business. He received his AB degree from Rockhurst College, and his MS and PhD degrees from Purdue University. His research and teaching interests are in the areas of forecasting, data mining, and decision support systems. His work has been published in a variety of journals, including the Academy of Management Journal, Decision Support Systems, the Journal of Econometrics, Communications in Statistics, and Communications of the ACM.
