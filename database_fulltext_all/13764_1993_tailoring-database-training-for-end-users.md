---
otero_id: 13764
otero_key: "GXAHXZ8F"
title: "Tailoring Database Training for End Users"
authors: "Judith D. Ahrens; Chetan S. Sankar"
year: "1993"
journal: "MIS Quarterly"
doi: "10.2307/249586"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Tailoring Database Training for End Users

By: Judith D. Ahrens
College of Information Studies
Drexel University
33rd and Market Streets
Philadelphia, Pennsylvania 19104
U.S.A.

Chetan S. Sankar
Department of Management
Auburn University
Auburn, Alabama 36849 U.S.A.

## Abstract

Lack of familiarity with database design methods could prevent many end users from effectively implementing their database management system packages. An inexpensive solution would be for end users to learn required database design skills from software tutors tailored to their needs. This research describes two tutors developed to teach these skills to end users. The tutors were based on a modified Entity-Relationship database design method. They improved an end user's natural learning process by incorporating design principles and facilitators. Empirical comparison of the tutors tested the teaching effectiveness of the facilitators. The results lead to recommendations for closing the gap between skills required and skills learned by end users in database design. Development of tutors that teach specific database design skills irrespective of the software package used in implementation has important implications for practitioners and researchers.

Keywords: End-user training, software tutors, cognitive skill acquisition, database design

ISRL Categories: AI0105, CB0601.01, CB0601.05, FB0401, FB0401.02, FB0401.03, FD06, GA03, GB0404

## Introduction

End-user computing has been growing at 50 to 90 percent per year (Cronan and Douglas, 1990), with many end users now relying on popular relational database management system packages. Most packages only require end users to define their files, bypassing the critical steps of conceptual data modeling and relational database design. But bypassing these steps can lead to a poor design, resulting in lost, spurious, and redundant data (Date, 1990). End users, therefore, are advised to have a specialist design the relational database portion of their applications (Hicks, 1993). But the growth of end-user computing and the scarcity of database specialists often makes this prescription unrealistic (Nelson, 1991). Furthermore, relying on a specialist is contrary to the independence often sought by end users (Zwass, 1992).

One alternative is for end users to design databases using knowledge-based consultative systems. $^{1}$ However, these systems are unsuitable for end users with no understanding of database concepts, and they do not contain tutorials that teach database design skills (Storey and Goldstein, 1993). End users can also attend college courses or seminars, though these can be time-consuming and expensive. A less expensive alternative is for end users to learn database design from a software tutor tailored to their needs (Bostrom, et al., 1988).

Figure 1 presents a process model for developing such tutors. The process begins by deriving skills required for conceptual and logical database design. $^{2}$ Tutors are then developed to teach these skills with the objectives of providing adequate content and appropriate instructional design. Empirical research determines the effectiveness of the tutors in fulfilling the objectives. These empirical results lead to recommendations for improving the tutors, thereby narrowing the gap between skills required and skills learned. This article reports how the process model was followed to develop tutors for database design.

The article is organized as follows. First, the skills required by end users for database design are derived. Then the development of two tutors that teach these skills to end users is described, followed by a report on the empirical research that compared the two tutors. Results are next presented followed by recommendations for improving the tutors. The article concludes with implications for both practitioners and researchers.

![](/api/attachments/GXAHXZ8F/fulltext/images/0efe7c70b509cf78e60f7f158c94edf7172ef48858bd12c49bf89c6cdcde4684.jpg)  
Figure 1. A Process Model for Developing Tutors for Database Design

## Skills Required for Database Design

End users can acquire skills in database design by active involvement in the performance of design tasks (Kamouri et al., 1986; Lewis and Anderson, 1985). Below the major end-user tasks in database design are identified, and the skills that need to be taught are described. These tasks/skills, grouped into five categories, are illustrated in Figures 2a through 2e.

Task/Skill 1: Comprehending data analysis concepts and terminology: End users must understand data modeling $^{3}$ terms such as entities, attributes, and relationships to describe their business environment's information structure (Figure 2a). The tutor needs to teach end users conceptual skills for describing their real world environment in terms of these concepts.

Task/Skill 2: Creating the conceptual schema: A conceptual schema (Figure 2b) is a diagram showing the relationships among entities. During the process of data modeling, end users draw the conceptual schema using the entities, attributes, and relationships identified in Task/Skill 1. The tutor needs to teach end users analytical skills to create the conceptual schema.

Task/Skill 3: Converting the conceptual schema into files: End users must convert the conceptual schema diagram into files (also called relations). This requires tasks such as converting entities into files and inserting foreign keys $^{4}$ (Figure 2c). The tutor needs to teach end users the steps involved in this task, and end users need to acquire procedural skills to follow the steps.

Task/Skill 4: Discriminating among decision rules: Further clarification about the entities, attributes, and relationships is obtained using decision rules. These rules help end users in such tasks $^{5}$ as deciding how to determine the type of relationship among entities, when to diagram a generalization hierarchy, and how to discriminate between entities and attributes (Figure 2d). The tutor needs to teach end users analysis skills for differentiating among decision rules, selecting the appropriate rule, and implementing the rule.

Task/Skill 5: Integrating and applying previous skills: End users need to iterate through the above tasks until their database requirements have been met (Figure 2e). The tutor needs to teach end users how to integrate and iteratively apply the skills previously discussed.

The final product of these iterations will be a set of files that models the end user's business environment and is free from the normalization problems $^{6}$ typically encountered during database design. These files could be implemented using any relational database management system package. Learning these skills is therefore essential for an end user who wants to apply database design methods prior to implementation. Believing an automated software tutor could teach these skills, we developed two tutors for our research.

## Development of Two Tutors

An effective software tutor requires adequate content so that relational database design concepts are incorporated. It also requires an appropriate instructional design so that end users can learn from the tutor. Our two tutors met the content requirement by being based on a modified Entity-Relationship (MER) method. The tutors addressed the instructional design requirement by employing different cognitive skill acquisition strategies. Next described are the content and instructional design requirements and how they guided the development of the tutors.

## Content requirement

A modified Entity-Relationship method $^{7}$ was created to provide the instructional content for both tutors. The method was modified to incorporate the following four end-user requirements for database design.

Stress top-down analysis, rather than bottom-up analysis: Top-down analysis is recommended for end users because it is more easily learned (Jarvenpaa and Machesky, 1986). Bottom-up analysis implies abstracting from data attributes to general concepts such as entities. Top-down analysis, on the other hand, relies on first deriving general concepts, such as entities, and then their attributes. The value of top-down analysis has been previously demonstrated in an experiment performed on inexperienced end users' abilities to validate a data model (Juhn and Naumann, 1985). This requirement is achieved in the MER method by first eliciting the database name, followed by relationships between important entity types, and finally their lower-level attributes.

![](/api/attachments/GXAHXZ8F/fulltext/images/1a9976f6e7fbbfe7527369587193a06bc2714c7a215aa5621481f480ccb48e08.jpg)  
Figure 2a. Comprehending Data Analysis Concepts and Terminology

![](/api/attachments/GXAHXZ8F/fulltext/images/513a4c7986d875598833282876a42baeab65424159127ab7ed471def0ccd2224.jpg)  
Figure 2b. Creating the Conceptual Schema

![](/api/attachments/GXAHXZ8F/fulltext/images/c19090206bc2e224e0fcbeb96e70195aad817f1f2d1ef8e703f58b7669d434d8.jpg)  
Figure 2c. Converting the Conceptual Schema Into Files

![](/api/attachments/GXAHXZ8F/fulltext/images/eb07da7d7661cad8ec9e7920817e1a14f1989d88660c0f47f7c71b30ce5124d8.jpg)  
Figure 2d. Discriminating Among and Applying Decision Rules

![](/api/attachments/GXAHXZ8F/fulltext/images/42d451c994cad0443d4acf94c30b008e393c7a5b40bdf15963b1caed9e8f3ff7.jpg)  
Figure 2e. Integrate and Apply Previous Skills

Provide systematic guidance and decision rules: In an experiment on modeling database requirements, participants reported that their biggest problem was deciding the sequence of questions to ask the end user. They also reported difficulty distinguishing among entities, attributes, identifiers, and relationships (Ridjanovic, 1986). Systematic guidance and explicit decision rules $^{8}$ for discriminating among these data modeling constructs could have helped these end users. This requirement is achieved in the MER method by organizing the method in a hierarchical sequence and creating many decision rules that help an end user proceed through the hierarchy.

Allow end users to express database requirements in natural language: While end users may understand their business environment well, they frequently have difficulty stating their database requirements in technical terms (Thomas and Carroll, 1981). A software tutor could show end users how to convert natural language sentences about database requirements into technical data modeling constructs. For example, the end user might say: Each employee must work for exactly one department. The tutor can help the end user recognize that subjects and objects represent database entities and that verbs define the role of each entity in a relationship. Similarly, the tutor can help end users state more complex data modeling requirements in natural language (Ahrens, 1993; Ahrens and Song, 1991; Chen, 1983; Nijssen and Halpin, 1989; Storey and Goldstein, 1988). This requirement is fulfilled in the MER method by asking end users to state facts about the database in subject, verb, and object sequence.

Incorporate normalization principles into the data modeling process: Many end users find data normalization difficult to understand (Date, 1989). But failure to normalize leads to anomalies in inserting, deleting, and modifying relational databases (Date, 1990). Normalization is therefore desired but must be simplified in a tutor tailored for end users. One major simplification is to integrate normalization principles into the data modeling process (Codd, 1979; Date, 1984), thus eliminating the need for a separate normalization procedure. The MER method incorporates normalization principles in its decision rules to fulfill this requirement.

Both tutors provide the instructional content (MER method) in four modules. Module 1 introduces the concepts of entities, attributes, and relationships and how they are represented on a conceptual schema. Module 2 teaches relationship analysis and rules for converting the conceptual schema into files. Module 3 teaches the process of adding attributes to entities and performing design iterations. Module 4 teaches design integrity, i.e., the consequences of not following the rules, and integrates all the material by working through a database design problem. Multiple skills are taught in each module, as shown in Table 1. Both tutors also incorporate instructional design techniques to improve an end user's process of cognitive skill acquisition.

## Instructional design requirement

Since many end users design a relational database infrequently, their design skills may atrophy before they are required again. This problem could be alleviated if the tutor can improve their natural process of cognitive skill acquisition. Cognitive skill acquisition theory explains how humans are able to acquire new skills (Anderson, 1982; 1983; 1987). $^{9}$ The theory assumes that people are born with the capacity to learn through weak methods such as reasoning by analogy, means-ends analysis, and trial and error search. $^{10}$ According to this theory, cognitive skills are acquired in three stages: declarative, knowledge compilation, and procedural.

In the declarative stage, when end users learn a new skill, instructions for the skill are encoded in their memory and represented as a declarative network of facts, definitions, and relationships. When end users have to perform a task, they must relate the newly acquired facts, definitions, and relationships in their memory. This process is painstakingly slow because the end user cannot yet take advantage of specialized decision rules for the problem domain, $^{11}$ in this case, database design. For example, an end user designing a database for an office may be able to identify the entities, room and telephone number. The end user may also know the definition of a fact: If one entity (E1) has the power to change the value of another entity (E2), then entity E2 is a fact about entity E1. In the declarative stage, however, the end user may find this definition too abstract to apply to these entities.

Table. 1. Relationship Between Modules and Tasks/Skills

<table><tr><td>Tasks/SkillsModule</td><td>Task/Skill 1.Comprehend.data analysisconcepts</td><td>Task/Skill 2.Createconceptualschema</td><td>Task/Skill 3.Convertconceptualschema to files</td><td>Task/Skill 4.Discriminateamongdecision rules</td><td>Task/Skill 5.Apply skills toa designproblem</td></tr><tr><td>1. Concepts ofentites,attributes, andrelationships</td><td>x</td><td>x</td><td></td><td></td><td></td></tr><tr><td>2. Convertconceptualschema to files</td><td>x</td><td>x</td><td>x</td><td>x</td><td></td></tr><tr><td>3. Add attributesto files</td><td>x</td><td></td><td></td><td>x</td><td></td></tr><tr><td>4. Designintegrity</td><td></td><td></td><td></td><td>x</td><td>x</td></tr></table>

Knowledge compilation is a process in which the knowledge acquired in a new domain is converted from representation in a declarative network to decision rules. In this stage, the end users would have learned how to apply the decision rules to entities in their problem domain. For the example given above, in this stage the end user would have compiled the following domain-specific decision rule:

IF a change in room (E1) will change the telephone number (E2),

THEN telephone number (E2) is a fact about the room (E1).

This decision rule would enable the end user to conclude that the telephone number is a fact about the room and therefore should not be modeled as a separate entity. Thus, at this stage, end users learn decision rules and shortcuts, permitting them to perform database design tasks more quickly and accurately than in the declarative stage.

The last stage is the procedural stage, where the learning of end users has advanced to the point where the decision rules have become permanently embedded in their memory. This results in increased speed and accuracy in performing database design. Several years are needed to reach this stage (Anderson, 1982).

Since end users expect to learn database design skills in days, not in years, a software tutor needs to focus on effecting the transition quickly and accurately from the declarative to the knowledge compilation stage. Therefore, two tutors, named concept and didactic, $^{12}$ were designed to improve end-user learning between the first two stages. The concept tutor uses design principles as the means to improve learning. The didactic tutor adds facilitators to these design principles to speed up the learning process further. Development of both tutors is described below.

## Developing the concept tutor

The concept tutor incorporates design principles to improve the cognitive skill acquisition of end users. These principles have previously been shown to improve the acquisition of LISP programming skills and have been used to develop intelligent tutoring systems (Anderson, et al., 1987; McKendree and Anderson, 1987). We expected that these principles would also improve an end user's acquisition of database design skills. Table 2 summarizes the relationship between the tutorial design principles and the database design tasks/skills. Described below is each tutorial design principle.

Organize material in a task-oriented, hierarchical structure: A task-oriented, hierarchical structure organizes problem-solving, provides direction, and closely reflects the top-down structure of database design. The concept tutor includes this principle by presenting the MER method in a hierarchical order with topics stating the task to be achieved. This presentation helps to integrate the individual skills needed to apply the MER method to a design problem (Task/Skill 5).

Use templates and provide concrete examples with solutions: A template is an abstract solution to a problem. A concrete example is an instance of this abstract solution. Templates help organize the parts of the problem that need to be integrated in the end user's declarative knowledge base. Concrete examples help the end user to substitute concepts from a business environment into the template structure. Inclusion of this principle in the tutor helps the end-user transition from the weak methods in the declarative stage to domain-specific decision rules in the knowledge compilation stage. For example, when an end user is learning how to add attributes to an entity, the tutor shows the screen in Appendix A1. This principle is used to teach conceptual skills (Task/Skill 1) and skills in discriminating among decision rules (Task/Skill 4).

Adjust size of procedural steps to the size of the cognitive processes involved: To avoid cognitive overload, this principle guides the tutor developer toward decomposing the skill into small steps that require a single cognitive action or decision. According to cognitive skill acquisition theory, decomposition helps creation of decision rules in the knowledge compilation stage. Eventually, composition will occur, in which a series of individual decision rules combines into a smaller set of decision rules that summarizes the series. For example, Appendix A1 shows how each attribute in the employee entity is analyzed for validity in a series of small steps. Eventually, an end user will “know” that the department number is an attribute of the employee as well as the identifier of the department entity. This principle is used to teach analysis (Task/Skill 2) and procedural skills (Task/Skill 3).

Table. 2. Relationship Between Design Principles and Tasks/Skills Required for Concept Tutor

<table><tr><td>Design Principles\Tasks/Skills</td><td>Task/Skill 1. Comprehend data analysis concepts</td><td>Task/Skill 2. Create conceptual schema</td><td>Task/Skill 3. Convert conceptual schema to files</td><td>Task/Skill 4. Discriminate among decision rules</td><td>Task/Skill 5. Apply skills to a design problem</td></tr><tr><td>1. Organize material in task-oriented hierarchical structure</td><td></td><td>x</td><td>x</td><td>x</td><td>x</td></tr><tr><td>2. Use templates and provide concrete examples with solutions</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Adjust size of procedural step to size of cognitive process</td><td></td><td>x</td><td>x</td><td></td><td></td></tr><tr><td>4. Provide instruction in problem solving context</td><td></td><td></td><td></td><td>x</td><td></td></tr><tr><td>5. Represent cognitive processes as a set of decision rules</td><td></td><td></td><td>x</td><td>x</td><td></td></tr></table>

Provide instruction in the problem-solving context: This principle minimizes memory overload by having the tutor integrate problem-solving instructions with the problem-solving process. The concept tutor incorporates this principle using decision rules that could assist the end user to reason as an experienced database designer during the process of database design. For example, in Appendix A1, the concept tutor teaches an end user how to analyze single-valued attributes in the context of verifying an employee entity. This principle is used to teach analysis skills (Task/Skill 4).

Represent the end users' cognitive processes as a set of decision rules: This principle reduces the cognitive effort needed to convert declarative knowledge into decision rules during knowledge compilation. For example, Appendix A2 shows a series of questions that resolve the IF condition part of a decision rule. Following the questions, the end user reaches the conclusion that the telephone number is a fact about the room, not about the department. The end user can then follow the prescribed action and model room as a separate entity. This principle teaches procedural (Task/Skill 3) and analysis skills (Task/Skill 4).

These five design principles provided the instructional design for the concept tutor. We could have varied either the instructional design or the content (MER method) in testing the effectiveness of this tutor. Many researchers have performed studies that compare content by testing various database methods, but have not studied how to teach these methods effectively to end users (e.g., Batra, et al., 1988a; 1988b; Shoval and Even-Chaime, 1987). We therefore chose to compare instructional design techniques.

Research comparing the effectiveness of computer-assisted instructional design techniques is sparse. One study in the field of accounting compared the effectiveness of computer-assisted learning with different user interfaces (Gal and Steinbart, 1992). Another compared two versions of the same expert system that differed only in the reasoning strategy. This study examined how the match between the user's mental model of the task and the system's task model affected user learning (Pei and Reneau, 1990). However, no database design tutors are yet reported in the literature (Storey and Goldstein, 1993), and there are no studies comparing alternative implementations of the same database design tutor. Therefore, we created a didactic tutor that added another instructional technique, facilitators, to improve the process of cognitive skill acquisition. The empirical portion of this research tested the effectiveness of adding facilitators to the concept tutor, while also providing an environment in which to assess the broad usefulness of database design tutors.

## Developing the didactic tutor to incorporate facilitators

Facilitators had speeded the transition from the declarative to the knowledge compilation stage of cognitive skill acquisition in prior research (Anderson, et al., 1987). Therefore, these facilitators were added to the concept tutor resulting in the didactic tutor. Presented below are the four facilitators and how they could improve the process of cognitive skill acquisition. Table 3 shows the relationship between the facilitators and the tasks/skills for database design.

Allow end user to participate in the reasoning process: Allowing end-user participation in the reasoning process strengthens the development of accurate domain-specific decision rules for the knowledge compilation stage of skill acquisition (Anderson, et al., 1987). Appendix A3 adds questions with explanations of correct and incorrect answers to the concept tutor material in Appendix A2. End user participation reinforces the appropriate decision-making process by correcting misconceptions as they occur. This facilitator helps in learning tasks requiring analysis and is used to teach Tasks/Skills 2, 4, and 5.

Use analogies relating known material to new situations: Teaching by analogy involves introducing a new concept by comparing its features to a known concept. End users who learn by analogy have higher recall and recognition than those given one example problem accompanied by a detailed explanation of that example (Gick and Holyoak, 1983). Analogy is an innate weak-method procedure used in the declarative stage to start the problem-solving process (Anderson, 1987). As an example, the didactic tutor teaches a new term, “conceptual schema,” by first defining it and then by asking the end user to compare it to other diagrams found in familiar contexts. This facilitator helps in learning tasks requiring concepts and analysis and is used to teach Task/Skills 1, 2, 4, and 5.

Table. 3. Relationship Between Facilitators and Tasks/Skills Required for Didactic Tutor

<table><tr><td>Facilitators\Tasks/Skills</td><td>Task/Skill 1. Comprehend data analysis concepts</td><td>Task/Skill 2. Create conceptual schema</td><td>Task/Skill 3. Convert conceptual schema to files</td><td>Task/Skill 4. Discriminate among decision rules</td><td>Task/Skill 5. Apply skills to a design problem</td></tr><tr><td>1. Allow end user to participate in the reasoning process</td><td></td><td>x</td><td></td><td>x</td><td>x</td></tr><tr><td>2. Use analogies relating known material to new situations</td><td>x</td><td>x</td><td></td><td>x</td><td>x</td></tr><tr><td>3. Give practice examples with immediate positive or negative feedback</td><td></td><td></td><td>x</td><td></td><td>x</td></tr><tr><td>4. Question the end user during learning to clarify and reinforce instruction</td><td>x</td><td>x</td><td>x</td><td>x</td><td>x</td></tr></table>

Give practice examples with immediate positive or negative feedback: Immediate feedback is a technique that provides the end user with a positive or negative response immediately after each interaction with the tutor. This technique results in more accurate performance than learning by discovering errors later (Anderson, 1987). The feedback process includes: explaining concepts, describing the task to be performed, obtaining the response, detecting an error, diagnosing (but not correcting) the error, and iterating through the process until a correct response is obtained. If the initial response is correct, positive feedback should be supplied. Thus, this facilitator assists the end user in constructing correct decision rules in the knowledge compilation stage. For example, when an end user incorrectly enters the identifier for an entity, the tutor detects and analyzes the error. This focuses an end user's attention on the need for corrective action. This facilitator helps in learning tasks requiring procedures and is used to teach Task/Skills 3 and 5.

Question the end user during learning to clarify and reinforce instruction: This facilitator ensures that the end user is building an accurate declarative knowledge base. If there are misconceptions, they are corrected as the end user sees explanations of both correct and incorrect answers. This technique is believed to reduce performance errors during the knowledge compilation stage (Anderson, et al., 1987). Asking end users about the meaning of new material significantly improves their ability to recall that information (Pressley, et al., 1988). In Appendix A3, the end user is asked three questions to clarify why a telephone is a fact about a room and not about a department. This facilitator helps in learning all skills (Task/Skills 1 through 5).

We expected that these facilitators would assist an end user to make the transition quickly from the declarative to the knowledge compilation stage of cognitive skill acquisition. Therefore, a higher level of performance was expected from end users who learned from the didactic tutor than those who learned from the concept tutor. The next section reports a test of this expectation.

## Empirical Research

The effectiveness of both tutors was tested in an experiment with 120 undergraduate students serving as end-user substitutes. The students were enrolled in seven sections of an “Introduction to MIS” course. They were divided into four groups. The students were tested on introductory database material and assigned to the four groups based on test performance, so that each group had an equivalent number of high, medium, and low performers.

The tutors were divided into four distinct modules, each lasting approximately 45 minutes. After finishing each module, students took a quiz. The quiz questions were structured as multiple choice, matching, true/false, or one-word fill-in answers. Performance data were collected from each quiz and then graded. Since the same skill could be taught in different modules, skill acquisition data were collected from questions in different quizzes.

Performance on quizzes was used as an indirect measure of how well each skill was acquired. $^{13}$ Computer-assisted instruction controlled for potential variability among human instructors. End users trained with the didactic tutor were predicted to achieve higher scores for each skill than those trained with the concept tutor. Appendix B describes the experimental design, procedures, and data analysis.

## Results

Quiz scores were analyzed $^{14}$ to measure the learning of each skill for both concept and didactic tutors (Table 4). Considering that these end users started with no knowledge of database design, the mean scores as a percentage of total possible scores indicate that both tutors assisted end users to learn database design. The percentages in the table show that both tutors taught the end users the three skills of creating the conceptual schema (Skill 2), converting the conceptual schema into files (Skill 3), and integrating skills (Skill 5) rather well. The tutors were less effective in teaching the skills of comprehending data analysis concepts (Skill 1) and discriminating among decision rules (Skill 4). Comparison of the scores between the tutors showed that the didactic tutor scores were significantly higher only for Skill 3. Further analysis indicated that it did not matter whether an end user learned from the concept tutor for Modules 1 and 2, and then switched to the didactic tutor for Modules 3 and 4, or vice versa.

## Discussion of Results and Recommendations

The scores achieved indicate that the tutors were moderately effective in closing the gap between skills required and skills learned by end users. The results lead to several recommendations to tutor developers and end users.

Improve effectiveness of question-answer sessions: Question-answer sessions did not improve learning significantly, supporting similar results in another study (Gal and Steinbart, 1992). A possible explanation is that end users learning from the didactic tutor supplied any answer in order to see the correct answer from the system. The didactic tutor's interface must be changed so that the end user must try answering the question several times before the correct answer is shown.

This result raises doubts about the value of imposing questions on end users during the learning process. The didactic tutor's questions were intended to assist the end user in correctly organizing the declarative knowledge base, but that goal may require, instead, the ability to answer the end user's questions. One possibility is to build an artificial intelligence-based tutor that can answer the end user's ad hoc questions, instead of asking its own questions. This system would have to understand the skill acquisition strategies of the end users and the context in which the questions are raised (Bumbaca, 1988; Kearsley, 1987).

Table. 4. Analysis of Results

<table><tr><td>Analysis\Tasks/Skills</td><td>Task/Skill 1. Comprehend data analysis concepts</td><td>Task/Skill 2. Create conceptual schema</td><td>Task/Skill 3. Convert conceptual schema to files</td><td>Task/Skill 4. Discriminate among decision rules</td><td>Task/Skill 5. Apply skills to a design problem</td></tr><tr><td>Total points that could be scored for this skill from all quizzes</td><td>48</td><td>29</td><td>35</td><td>51</td><td>95</td></tr><tr><td>Scores obtained by 60 respondents using concept tutor</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mean</td><td>16.71</td><td>17.85</td><td>20.14</td><td>7.70</td><td>59.19</td></tr><tr><td>standard deviation</td><td>(4.85)</td><td>(4.80)</td><td>(13.24)</td><td>(2.74)</td><td>(19.19)</td></tr><tr><td>% of total score</td><td>35%</td><td>62%</td><td>58%</td><td>15%</td><td>62%</td></tr><tr><td>Scores obtained by 60 respondents using didactic tutor</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mean</td><td>16.73</td><td>19.23</td><td>29.47</td><td>7.15</td><td>63.32</td></tr><tr><td>standard deviation</td><td>(4.17)</td><td>(4.65)</td><td>(5.85)</td><td>(2.94)</td><td>(18.68)</td></tr><tr><td>% of total score</td><td>35%</td><td>66%</td><td>84%</td><td>14%</td><td>67%</td></tr><tr><td>2-tailed t-test between concept and didactic tutor means</td><td>not significant</td><td>not significant</td><td>t(117)=4.99p&lt;.05(.000)</td><td>not significant</td><td>not significant</td></tr></table>

Emphasize concrete examples: Concrete examples, a tutorial design principle found in both tutors, are essential to the psychology of concept formation (Glass and Holyoak, 1986). They assist the end user's general-to-specific inference mechanisms. Possibly, they made both tutors equally good teachers for organizing the declarative knowledge base. We suggest illustrating each concept presented in the tutor with a concrete example.

Determine minimum number of analogies: Analogies did not improve learning significantly in this research. Given the difficulty of teaching analogical reasoning without reference to concrete examples, it becomes difficult to separate analogy as a facilitator from concrete examples as a design principle used in both tutors. We suggest performing experiments to determine the minimum number of analogies required for them to become an effective facilitator.

Repeat the tutorial to develop expertise: Participation in the reasoning process was expected to enable end users to reason as an expert by bypassing the weak methods characteristic of the declarative stage. The non-significant results for teaching Skills 2 and 4 do not support this expectation and show a need for further research on expert-novice differences. Novices focus on surface features, whereas experts focus on underlying problem structure (Chase and Simon, 1973; Chi, et al., 1981). Apparently end users who are novices in database design need to repeat the tutorial many times before they can expect to obtain expertise.

Include practice examples: Practice examples with immediate positive or negative feedback significantly improved learning procedural skills. The didactic-trained end users' weak-method procedures were more quickly compiled into decision rules with this facilitator. Tutor designers should therefore include practice examples, and end users should use them.

## Implications for Practitioners

Practitioners are probably familiar with “how-to” tutors that are limited to explaining the commands of a database management system package used in implementation. In contrast, this research stresses development of tutors that teach database design skills to end users irrespective of the software package. The concept and didactic tutors teach conceptual, analytical, and procedural skills as they relate to database design tasks. Such tutors can help practitioners learn database design skills quickly and accurately. Once trained by these tutors, practitioners could use database management system packages more effectively. Extension of the process model (Figure 1) to other applications such as financial modeling using spreadsheets could lead to creation of other effective tutors for practitioners.

## Implications for Researchers

Researchers need to develop database design tutors using effective cognitive skill acquisition strategies. Design principles and facilitators should be further explored. Recall tests after some delay are a necessary extension, because this experiment only tested end users immediately after each module. Promising new instructional techniques such as multi-media should be added and tested for their effectiveness. Another research opportunity is hypertext tutors (Bieber and Kimbrough, 1992). These would enable the end user to explore the same material in an associative manner as well as in the hierarchical, rule-based manner characteristic of our tutors.

## Conclusions

The process model of Figure 1 represents a new direction for research on end-user computing by emphasizing the need for close interaction between researchers and practitioners. Researchers who create information systems development methods must be aware of empirical research in their problem domain, e.g., database design, enterprise modeling, or systems analysis. They must seek to simplify their methods, so as to compensate for documented weaknesses of inexperienced end users. Tutor researchers and developers should study the skills needed by end users and incorporate successful cognitive skill acquisition strategies into their tutors. Practitioners should demand development of effective, well-researched tutors that teach the skills needed in their business environment. Effective tutors can play a major role in reducing the time and costs associated with end-user training as well as improving the quality of end-user-developed systems.

## Acknowledgements

The authors wish to thank the senior editor, the associate editor, and the anonymous reviewers for their excellent suggestions.

## Endnotes

$^{1}$ Storey and Goldstein (1993) compare the features of 13 knowledge-based consultative systems for database design. Examples of these systems are I $^{2}$ S (Kawaguchi, et al., 1986), VCS (Storey and Goldstein, 1988), and Modeller (Tauzovich, 1989).

$^{2}$ Conceptual design expresses all information requirements in the form of a high-level model independent of any database management system. Logical design translates the conceptual schema into the data model of the target database management system (Storey and Goldstein, 1993).

$^{3}$ Data modeling is the process by which user requirements are analyzed to form a data model such as the entity-relationship model and are represented on a conceptual schema (Kroenke, 1992). Entities represent classes of real-world objects such as employee, manager, and department. Attributes are facts about entities or relationships. For example, attributes of the employee entity include facts such as each employee has one social security number, one name, one date of birth, and one or more skills. Relationships represent associations among two or more entities. An example of a relationship is works\_in, which relates employee and department.

$^{4}$ When the identifier of one file is stored in a second file it is called a foreign key (Kroenke, 1992). Foreign keys are used to retrieve associated information from another file.

$^{5}$ The types of relationship among entities can vary from one-to-one, to one-to-many, to many-to-many. For example, if an employee works for exactly one department at any given time, but a department employs many employees, the relationship type is one-to-many. If each employee has many skills, and a given skill is possessed by many employees, the relationship type is many-to-many.

A generalization hierarchy represents an entity type that is a superset of another entity type. For example, person is a generalization of man and woman (Hansen and Hansen, 1992).

There are occasions when an attribute of an entity may have to be represented as another entity. An example is the telephone number assigned to an outlet in a room. When a department moves to another room, the phone number of the department changes. In this case, the end user needs to model the room as a separate entity on the conceptual schema with telephone number as an attribute.

$^{6}$ Normalization is a process of converting a file that has certain anomalies into two or more files that do not have these anomalies. For example, if we combined the entities department and employee in the same file, many anomalies would result. If an employee is hired but not assigned to a department, we could not enter the employee into the database because required information is missing. This is known as an insertion anomaly. This and other anomalies result in lost, spurious, and redundant data. Normalization removes these anomalies from the final set of files.

$^{7}$ The MER method is based on constructs in Codd's (1979) extended relational model. Date (1984) has established that a modeling procedure based on Codd's constructs leads to a normalized design. We integrated Codd's constructs with fact-based (Kent, 1983; Nijssen and Halpin, 1989) and extended entity-relationship design methods (Teorey, et al., 1986) to form the MER method. A detailed description of the MER method is available from the authors.

$^{8}$ A decision rule is of the form:
IF condition
THEN action1
ELSE action2.

$^{9}$ This theory was selected for the instructional design of the tutors because Anderson's work is similar to the process model of Figure 1. Additionally, the theory has been applied to a study of end-user learning behavior in database design (Jarvenpaa and Machesky, 1986).

$^{10}$ In contrast to weak methods, strong methods have effective decision rules developed for a specific problem domain, such as database design.

$^{11}$ The problem domain describes the database design task end users must perform in solving their real-world problem.

$^{12}$ Since principles were taught in the first tutor, it was named Concept tutor. The second tutor added facilitators and hence was named Didactic tutor to indicate its emphasis on systematic instruction.

$^{13}$ Skill acquisition, per se, is not directly measurable.

$^{14}$ Differences in means between the two tutors were tested using a 2-tailed t-test statistic. Hotelling's $T^{2}$ test did not reveal any correlation among the skill variables.

## References

Ahrens, J. "A CASE Tool Knowledge Base for Semantic Data Modeling and Relational Database Design," Proceedings of the Information Resources Management Association International Conference, Salt Lake City, UT, May 24-26, 1993, pp. 81-95.

Ahrens, J. and Song, I. "Modeling Aids for Novice Database Designers," Proceedings of the Information Resources Management Association International Conference, Memphis, TN, May 19-22, 1991, pp. 99-114.

Anderson, J. "Acquisition of Cognitive Skill," Psychological Review (89:4), July 1982, pp. 369-406.

Anderson, J. The Architecture of Cognition, Harvard University Press, Cambridge, MA, 1983.

Anderson, J. "Skill Acquisition: Compilation of Weak-Method Problem Solutions," Psychological Review (94:2), April 1987, pp. 192-210.

Anderson, J., Boyle, C., Farrell, R., and Reiser, B. "Cognitive Principles in the Design of Computer Tutors," in Modeling Cognition, P. Morris (ed.), Wiley, New York, NY, 1987.

Batra, D., Hoffer, J., and Bostrom, R. "A Comparison of User Performance Between the Relational and the Extended Entity Relationship Models in the Discovery Phase of Database Design," Proceedings of the Ninth International Conference on Information Systems, Minneapolis, MN, November 30-December 2, 1988a, pp. 295-308.

Batra, D., Hoffer, J., and Bostrom, R. “Comparing Representations with Relational and EER Models,” Communications of the ACM (33:2), February 1988b, pp. 126-139.

Bieber, M. and Kimbrough, S. "On Generalizing the Concept of Hypertext," MIS Quarterly (16:1), March 1992, pp. 77-93.

Bostrom, R., Olfman, L., and Sein, M. "End-user Computing: A Research Framework for Investigating the Training/Learning Process," in Human Factors in MIS, J. Carey (ed.), Ablex Publishing Corp., Norwood, NJ, 1988, pp. 221-250.

Bumbaca, F. "Intelligent Computer-Assisted Instruction: A Theoretical Framework," International Journal of Man-Machine Studies (29:3), September 1988, pp. 227-255.

Chase, W. and Simon, H. "Perception in Chess," Cognitive Psychology (4:1), January 1973, pp. 55-81.

Chen, P. "English Sentence Structure and Entity-Relationship Diagrams," Information Sciences (29:8), May 1983, pp. 221-243.

Chi, M., Feltovich, P., and Glaser, R. "Categorization and Representation of Physics Problems by Experts and Novices," Cognitive Science (5:2), April/June 1981, pp. 121-152.

Codd, E. "Extending the Database Relational Model to Capture More Meaning," ACM Transactions on Database Systems (4:4), December 1979, pp. 397-434.

Cronan, T. and Douglas, D. "End User Training and Computing Effectiveness in Public Agencies: An Empirical Study," Journal of MIS (6:4), Spring 1990, pp. 21-40.

Date, C. A Guide to DB2, Addison-Wesley, Reading, MA, 1984.

Date, C. "Why Don't People Understand the Relational Model?" DBMS (2:10), September 1989, pp. 26-32.

Date, C. An Introduction to Database Systems Vol. I. (5th edition), Addison-Wesley, Reading, MA, 1990.

Gal, G. and Steinbart, P. "Interface Style and Training Task Difficulty as Determinants of Effective Computer-Assisted Knowledge Transfer," Decision Sciences (32:1), January/February 1992, pp. 128-143.

Gick, M. and Holyoak, K. "Schema Induction and Analogical Transfer," Cognitive Psychology (15:4), January 1983, pp.1-38.

Glass, A. and Holyoak, K. Cognition (2nd edition), Random House, New York, NY, 1986.

Hansen, G. and Hansen, J. Database Management and Design, Prentice Hall, Englewood Cliffs, NJ, 1992.

Hicks, J. Management Information Systems: A User Perspective, West Publishing Co., St. Paul, MN, 1993.

Jarvenpaa, S. and Machesky, J. "End-user Learning Behavior in Data Analysis and Data Modeling Tools," Proceedings of the 5th International Conference on Information Systems, San Diego, CA, December 1986, pp. 152-167.

Jarvenpaa, S., Dickson, G., and DeSanctis, G. "Methodological Issues in Experimental Infor-

mation Systems Research: Experiences and Recommendations," MIS Quarterly (9:2), June 1985, pp. 141-156.

Juhn, S. and Naumann, J. "The Effectiveness of Data Representation Characteristics on User Validation," Proceedings of the 6th International Conference on Information Systems, Indianapolis, IN, December 1985, pp. 212-225.

Kamouri, A., Kamouri, J., and Smith, K. "Training By Exploration: Facilitating the Transfer of Procedural Knowledge Through Analogical Reasoning," International Journal of Man-Machine Studies (24:2), February 1986, pp. 171-192.

Kawaguchi, A., Takoa, N., Mizoguchi, R., Yamaguchi, T., and Kakusho, O. "An Intelligent Interview System for Conceptual Design of Database," ECAI'86: The 7th European Conference on the Artificial Intelligence, Conference Services Ltd, London, 1986, pp. 1-7.

Kearsley, G. (ed.). Artificial Intelligence and Instruction: Applications and Methods, Addison-Wesley, Reading, MA, 1987.

Kent, W. "Fact-Based Data Analysis and Design," in Entity-Relationship Approach to Software Engineering, Davis, Jajodia, Ng and Yeh (eds.), Elsevier Science Publishers B.V./North Holland, Amsterdam 1983, pp. 3-53.

Kroenke, D. Database Processing (4th edition), MacMillan, New York, NY, 1992.

Lewis, M. and Anderson, J. “Discrimination of Operator Schemata in Problem-Solving: Learning From Examples,” Cognitive Psychology (17:1), January 1985, pp. 26-65.

McKendree, J. and Anderson, J. "Effect of Practice on Knowledge and Use of Basic LISP," in Interfacing Thought: Cognitive Aspects of Human-Computer Interaction, J. M. Carroll (ed.), The MIT Press, Cambridge, MA, 1987, pp. 236-259.

Moher, T. and Schneider, G. "Methodology and Experimental Research in Software Engineering," International Journal of Man-Machine Studies (16:1), January 1982, pp. 65-87.

Myers, J. Fundamentals of Experimental Design (2nd edition), Allyn and Bacon, Inc., Boston, MA, 1977.

Nelson, R. "Educational Needs as Perceived by IS and End-User Personnel: A Survey of

Knowledge and Skill Requirements," MIS Quarterly (15:4), December 1991, pp. 503-536.

Nijssen, G. and Halpin T. Conceptual Schema and Relational Database Design: A Fact Oriented Approach, Prentice Hall, New York, NY, 1989.

Pei, B. and Reneau, J. "The Effects of Memory Structure on Using Rule-Based Expert Systems for Training: A Framework and an Empirical Test," Decision Sciences (21:2), Spring 1990, pp. 263-286.

Pressley, M., McDaniel, M., and Turnure, J. "Elaborative Interrogation Facilitates Acquisition of Confusing Facts," Journal of Educational Psychology (80:4), September 1988, pp. 268-278.

Ridjanovic, D. Comparing Quality of Data Representations Produced by Nonexperts Using Logical Data Structure and Relational Data Models, unpublished Ph.D. dissertation, University of Minnesota, Minneapolis, MN, 1986.

Shneiderman, B. "Improving the Human Factors Aspect of Database Interactions," ACM Transactions on Database Systems (3:4), December 1978, pp. 417-439.

Shoval, P. and Even-Chaime, M. “Database Schema Design: An Experimental Comparison Between Normalization and Information Analysis,” Data Base (18:3), Spring 1987, pp. 30-39.

Storey, V. and Goldstein, R. "A Methodology for Creating User Views in Database Design," ACM Transactions on Database Systems (13:3), September 1988, pp. 305-338.

Storey, V. and Goldstein, R. "Knowledge-Based Approaches to Database Design," MIS Quarterly (17:1), March 1993, pp. 25-46.

Tauzovich, B. "An Expert System for Conceptual Data Modelling," Proceedings of the 8th International Conference on the Entity-Relationship Approach, Toronto, Ontario, October 1989, pp. 329-344.

Teorey, T., Yang, D., and Fry, J. "A Logical Design Methodology for Relational Databases Using the Extended Entity-Relationship Model," Computing Surveys (18:2), June 1986, pp. 197-222.

Thomas, J. and Carroll, J. "Human Factors in Communication," IBM Systems Journal (20:2), 1981, pp. 237-263.

Zwass, V. Management Information Systems, Wm. C. Brown, Dubuque, IA, 1992.

## About the Authors

Judith D. Ahrens is an assistant professor of information studies at the College of Information Studies, Drexel University. She received her Ph.D. in business administration from Temple University, where she majored in computer information systems and minored in strategic management. She was awarded the Certified System Professional designation in 1986. Her background includes 13 years industry experience in all phases of software and database development at CIGNA and CONRAIL. She worked as data communications editor at Auerbach Publishers and as an independent consultant. She has published in the International Journal of Man-Machine Studies, Journal of Global Information Management, Journal of End-User Computing, Interface, as well as in several conference proceedings. Her current research interests include end-user support for semantic data modeling and database design, information systems for business process re-engineering, and software engineering methodologies and tools. She is a member of the ACM, IEEE, IRMA, and the Internet Society.

Chetan S. Sankar is an associate professor of MIS at the Auburn University's College of Business. He received his Ph.D. from the Wharton School, University of Pennsylvania. He has worked as an assistant professor at Temple University and as a systems engineer at AT&T-Bell Laboratories. He researches strategic and managerial issues in global telecommunications management, database management systems, and career progression of technical personnel. He is a senior member of the IEEE and a member of DSI, TIMS, and IRMA. His articles have appeared in MIS Quarterly, Management Science, various IEEE Transactions, Journal of Database Administration, International Journal on Information Management, Journal of Global Information Management, Decision Support Systems, and The Naval Logistics Quarterly, among others. A paper he co-authored won the third place in the Society for Information Management 1990 Paper Award Competition.

# Appendix A1

# Concept Tutor: Adding Attributes to an Entity

This appendix uses a decision rule to show an end user how to verify whether a fact about an entity should be modeled as an attribute of that entity or a separate entity.

Single-valued fact decision:

Should I model entity 2 as a single-valued fact about entity 1 or should I model it as a separate entity?

Single-valued fact decision rule:

IF entity E2 in a single-valued fact will be described further

THEN model E2 as a separate entity

ELSE model E2 as an attribute of E1

Single-valued fact concrete example:

Let's verify that only single-valued facts appear in our previous employee entity, and then apply the decision rule by adding new facts:

EMPLOYEE (employee\_\_number, name, department\_\_number)

Each employee has one social security number. Therefore, employee\_\_number is a single-valued fact about the Employee. In addition, it is the unique identifier of each employee.

Each employee has one name. The name is a single-valued fact about the Employee, because each employee can have only one name.

Each employee works for one department, identified by a department number. Therefore, department is a single-valued fact about employee. However, department will be described further, with its name, room number, budget, and other facts. Therefore, the department must also be modeled as a separate entity, with department\_number as its identifier. The attribute department\_number in the employee entity will then serve as a foreign key to the department\_number in the department entity. The foreign key will enable us to retrieve facts about an employee's department.

Note: This screen is presented by the concept tutor to the end user, and no response is expected.

EXCERPTED FROM CONCEPT TUTOR MODULE 3 TOPIC 7 ADDING SINGLE-VALUED FACTS TO ONE-TO-ONE AND ONE-TO-MANY RELATIONSHIPS

# Appendix A2

# Concept Tutor: Adding Single-Valued Facts

This appendix shows how the addition of telephone number to the entity department makes it necessary to create a new entity called room.

Add a new fact: Now we decide to add the department's telephone number to the database. For simplicity, let's assume one telephone number per department. Thus we know that telephone number is a single-valued fact about...what? We must now decide WHICH entity the single-valued fact is ABOUT.

Decision Rule: A rule for deciding which entity a single-valued fact is about:

IF one entity (E1) has the power to change the value of another entity (E2)

THEN entity E2 is a fact about entity E1.

(Technically, we say that E2 is functionally dependent upon E1.)

Example: Here are the facts about telephones, rooms, and departments in the Colossus company: Each telephone number is assigned to one physical outlet in each room. If the department is moved to a different room, the department room number will change. Thus, the room number depends upon (or changes with) the department. The room number of the department changes because the department moves.

The question is, will the department telephone number change when the department moves? (Yes, because each telephone number is wired to a physical location in a room, and we have just changed rooms.)

Now here's the crucial question. Is the telephone number controlled by, or does it change with, the room, or the department? (the room)

Is the telephone number therefore a fact about the room or about the department? (the room)

Recall the decision rule about single-valued facts:

IF entity E2 in a single-valued fact will be described further

THEN model E2 as a separate entity

ELSE model E2 as an attribute of E1

Example of applying decision rule:

1. Each department (E1) is located in one room (E2)

2. Each room (E1) has one telephone number (E2)

Since the telephone number is a fact about the room, and not about the department, we have to model the room (E2) as a separate entity on the conceptual schema because we are now going to record additional facts about it (its telephone number).

Note: This screen is presented by the concept tutor to the end user, and no response is expected.

EXCERPTED FROM MODULE 3 TOPIC 7 ADDING SINGLE-VALUED FACTS TO ONE-TO-ONE AND ONE-TO-MANY RELATIONSHIPS

# Appendix A3

# Didactic Tutor: Participating in the Reasoning Process

This appendix explains to the end user the reasoning used to decide to create a new entity called room. The end user participates by responding to the tutor's questions.

Example: Will the telephone number change when the department moves to a different room? Enter Y(YES) or N(NO) y RIGHT! Press E for explanation or any key to continue e

EXPLANATION: The telephone number HAS to change because each room has a DIFFERENT number. Now, here's the crucial question: Does the telephone number depend upon:

a. the room
b. the department

SELECT a/b b SORRY, THE CORRECT ANSWER IS a

EXPLANATION: The number is determined by the telephone outlet in the room, and would be the same no matter which department used the room. Therefore, it depends upon the room.

Is the telephone number therefore a fact about:
a. the room
b. the department

SELECT a/b b SORRY, THE CORRECT ANSWER IS a

EXPLANATION: Ask yourself these questions:

What does a department have to do to get its telephone number changed? (Change rooms) Which entity has the power to CHANGE the telephone number of a department? (The room) Which entity DETERMINES or CONTROLS the digits in the telephone number? (The room).

A general rule is:
IF one entity (E1) has the power to change the value of another entity (E2)
THEN entity E2 is a fact about entity E1.

Since the telephone number is a fact about the room, and not about the department, what do we do about the room?

a. leave it in the department entity

b. consider it a separate entity because we are going to record additional facts about it (its telephone number)
SELECT a/b b RIGHT!

Note: The didactic tutor requires a response. The end user's response is shown in bold and underlined. If the response is incorrect, the explanation appears automatically. If correct, the end user can decide whether to see the explanations.

EXCERPTED FROM DIDACTIC TUTOR MODULE 3 SUBTOPIC 7 ADDING SINGLE-VALUED FACTS TO ONE-TO-ONE AND ONE-TO-MANY RELATIONSHIPS

# Appendix B

# Details About the Empirical Research

## Experimental Design

Human factors researchers recommend a counterbalanced experimental design to control for the high variability among end users' skills and aptitudes in the computer and information sciences (Jarvenpaa, et al., 1985; Moher and Schneider, 1982; Shneiderman, 1978). In a counterbalanced design, each end user experiences each treatment, eliminating the need for a control group, and systematically varied treatment sequences between groups of end users control for possible carryover learning effects between treatments. A true counterbalanced design was not possible in this experiment because the cumulative nature of the material required that the modules proceed in fixed sequence.

The mixed-model design, however, accommodates both the module sequence constraint and the counterbalanced design goal. Mixed-model designs (Myers, 1977, pp. 191-193) enable:

(a) Different end users to experience different treatments, and

(b) All end users to experience each treatment.

Four groups were formed with 30, 30, 31, and 29 students in each. Objective (a) is realized in Groups 1 and 2, where Group 1 experiences the concept (control) treatment for all four modules, and Group 2 the didactic treatment for all four modules. Training is a between-subjects variable for Groups 1 and 2 because different students experience different concept and didactic treatments. Objective (b) is realized in Groups 3 and 4, where Group 3 starts with the concept treatment for Modules 1 and 2, then switches to the didactic treatment for Modules 3 and 4, and Group 4 starts with the didactic treatment for Modules 1 and 2, then switches to the concept treatment for Modules 3 and 4. In Groups 3 and 4, training is a within-subjects variable because all students experience each treatment. Groups 3 and 4 thus provide a picture of early versus late effects of concept and didactic training when training is counterbalanced. A comparison of Groups 1 and 2, in which training is varied between-subjects, with Groups 3 and 4, in which it is varied within-students, reveals whether learning is affected by training techniques and the cumulative effects of practice.

## Experimental Procedures

A “letter to the student” explained the importance of database design and how the tutor and quizzes would be incorporated into the computer lab sessions of their course. Students did not know an experiment was being conducted. An in-class Introductory Module was administered to introduce basic concepts and to divide students into groups, based on their performance on objective questions incorporated into the text. A pilot study was conducted with 48 undergraduate students, 12 students per group. The dispersion of scores on the Introductory Module was sufficient to justify its use as a pretest to control for group equivalence.

For each class section participating in the experiment, Introductory Module (pretest) scores were ranked and each student was assigned, round-robin fashion, to one of four groups. Thus, each group had the same dispersion of performers. During the experiment, each group was drawn from different sections, and was composed of high, medium, and low performers, as determined by pretest performance on the Introductory Module. To increase motivation, the tutors were incorporated into the course materials and given during scheduled lab times. Students were told that the quizzes counted toward their grades, but instructors were free to use the quiz results as they saw fit.

As students appeared for the lab, they were given their own self-booting diskettes, prepared with the proper treatment (tutor) for that module, as determined by the student's group assignment. Students were given 45 minutes maximum to learn each module. They were permitted to review the material after completing the entire module. After returning the diskette, students had the second 45 minutes to complete the quiz. Thus, each student participated in four consecutive one-and-one-half hour experimental sessions. Absentees were permitted to make up the work, with the researcher present to monitor the time. The researcher's role was limited to handing out and collecting diskettes and quizzes.

## Data Analysis

Performance data measuring the didactic or concept training techniques were analyzed together with both skill and content dimensions. Skill-level analysis was task-oriented, i.e., each hypothesis was operationalized by a set of tasks, defined as the set of questions or parts of questions from a quiz or quizzes that required the application of a particular skill. Tasks from all quizzes requiring the same skill were grouped to measure, or operationalize, a hypothesis. The unit of measure in the skill dimension, therefore, was the score obtained under each skill.

Content-level analysis was module-oriented, i.e., it measured how well students understood the material in each module. This was accomplished by repeatedly measuring individual students' performance differences across the four quizzes using a mixed-model design (Myers, 1977, p.191). The unit of measure in the content dimension, therefore, was the total score obtained for each quiz.

Data were collected and analyzed along these two dimensions. Each of the four quiz-grading programs built a quiz file, each record of which contained the student's name, group (treatment), score obtained for each question's sub-tasks, and a total quiz score normalized to 100 points.
