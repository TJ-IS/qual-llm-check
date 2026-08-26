---
otero_id: 15408
otero_key: "D2C9KVJW"
title: "An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity"
authors: "Paul L. Bowen; Robert A. O'Farrell; Fiona H. Rohde"
year: "2009"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0181"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/D2C9KVJW/fulltext/images/1e840ce694b69ff6dff59bbc447609d788da52944defa3ab4847341cf4a9fd19.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity

Paul L. Bowen, Robert A. O'Farrell, Fiona H. Rohde,

## To cite this article:

Paul L. Bowen, Robert A. O'Farrell, Fiona H. Rohde, (2009) An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity. Information Systems Research 20(4):565-584. http:// dx.doi.org/10.1287/isre.1080.0181

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2009, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/D2C9KVJW/fulltext/images/779b3e3157cc61420833984613413d70abcff209eb0b29e3f0aef362b1f22173.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# An Empirical Investigation of End-User Query Development: The Effects of Improved Model Expressiveness vs. Complexity

Paul L. Bowen College of Business, Florida State University, Tallahassee, Florida 32306, pbowen@cob.fsu.edu

Robert A. O’Farrell, Fiona H. Rohde School of Business, The University of Queensland, Brisbane QLD 4072, Australia {r.o’farrell@business.uq.edu.au, f.rohde@business.uq.edu.au}

ata models provide a map of the components of an information system. Prior research has indicated that more expressive conceptual data models (despite their increased size) result in better performance for problem solving tasks. An initial experiment using logical data models indicated that more expressive logical data models also enhanced end-user performance for information retrieval tasks. However, the principles of parsimony and bounded rationality imply that, past some point, increases in size lead to a level of complexity that results in impaired performance. The results of this study support these principles. For a logical data model of increased but still modest size, users composing queries for the more expressive logical data model did not perform as well as users composing queries for the corresponding less expressive but more parsimonious logical data model. These results indicate that, when constructing logical data models, data modelers should consider tradeoffs between parsimony and expressiveness.

Key words: scalability; expressiveness; ontology; ontological clarity; parsimony; logical data models History: Sumit Sarkar, Senior Editor; Hemant Jain, Associate Editor. This paper was received on August 19, 2005, and was with the authors 1 year and 2 months for 3 revisions. Published online in Articles in Advance May 12, 2009.

## 1. Introduction

Data models provide managers, information retrieval agents, and other knowledge workers with a map of the components of an information system and of the relationships among these components. The underlying philosophical approach chosen to represent these components and their interrelationships determines the characteristics of the resulting models (Wand et al. 1999). The characteristics of these models, in turn, affect their usefulness for various tasks including conceptual database modeling (Batra 1993), pattern reuse (Purao et al. 2003), and information retrieval (Borthick et al. 2001a). The usefulness of the models used during the information retrieval task has important consequences, both economic and otherwise, e.g., on decision quality. Because of these consequences, the information systems community has devoted considerable attention to semantic data models and alternative modeling approaches and their effect on users’ performance (see, e.g., Balzer 1979, Young and March 1995, Owei et al. 2002).

Prior researchers are consistent in asserting a positive relationship between complexity and task performance; i.e., as task complexity increases, performance decreases (March and Simon 1958, Campbell 1988, Rho and March 1997, Borthick et al. 2001b, Chan et al. 1999, Jih et al. 1989). Recent research into semantic data modeling has included investigations into the effects of varying model expressiveness on a range of tasks (see Shoval and Frumermann 1994, Khatri et al. 2006) and indicated that more expressive conceptual data models led to better performance during problem solving tasks (Bodart et al. 2001, Gemino and Wand 2005). The favorable results for problem solving tasks occurred in spite of the larger size of these more expressive models.

Conceptual data models are used as a basis for preparing logical data models (Hoffer et al. 2004) with which users interact when preparing queries to satisfy information requests. Initial research has shown that logical data models prepared from more expressive conceptual data models of approximately the same size as the smaller models used in the Bodart et al. (2001) experiments resulted in end users constructing more accurate queries than those prepared by users given the equivalent parsimonious logical model (Bowen et al. 2006). Thus, the results of prior research projects suggest that users’ information retrieval tasks may be enhanced if users are provided with more expressive logical data models. The logic underlying prior research is that (1) more expressive representations provide finer (more detailed) domain information for people formulating queries; (2) the finer domain information should improve end user accuracy during query development; (3) the improved end user accuracy during query development yields higher-quality information to stakeholders (information requestors), and (4) the higher-quality information should lead to better decisions.

As noted earlier, more expressive data models are typically larger in size than equivalent traditional/parsimonious data models. In prior research, size has been one dimension that has been shown to increase complexity for particular tasks with a resulting decrease in performance (Wood 1986). Given the potential growth in the model size that could result from converting parsimonious models to more expressive models, this research investigates whether the results of prior research indicating better query accuracy for more expressive logical models are robust when combined with increases in complexity due to increases in model size. Our research differs from prior experiments that use conceptual data models in that (1) our logical data models are specific instantiations of a general conceptual model; (2) our logical data models are isomorphic to the relational implementations; (3) users were allowed to view the data models while performing the task, and (4) the specific problem solving task is to formulate SQL queries. Particularly our research differs from the Bowen et al. (2006) prior experiment that used logical data models in that (1) the logical data models are larger, (2) the information requests more closely align with those of business managers, and (3) a broader definition of performance (i.e., overall accuracy as well as query preparation time and query preparer confidence) is examined. Because organizations’ data models can contain hundreds, thousands, and even tens of thousands of attributes and entities, the relationship between model expressiveness and task complexity, and, ultimately, the scalability of the alternate data modeling approaches, is of substantial relevance to both information systems academics and practitioners.

## 2. Theoretical Foundation and Hypothesis Development

Prior research into the concept of naturalness, i.e., conceptual ease of use (Stabell 1983), the theory of cognitive fit (Vessey 1991), and tradeoffs between expressiveness and understandability (Khatri et al. 2004), has indicated that naturalness and operational performance are not consistently related but that naturalness may actually impair performance (Kottemann and Remus 1989). Based on these prior results, this research contrasts increased model expressiveness via improved ontological clarity and increased complexity due to size with end-user performance on query preparation tasks.

## 2.1. Model Expressiveness and Performance

An information system is a model of the real world, and, as such, a “good information system must be a good representation of the real world system [it is] intended to model” (Weber 2003, p. 2). A highquality model should provide a complete and clear description of the application domain being modelled. The more complete and clear the description and representation, the more expressive is the data model. Evaluation of the model’s expressiveness can be undertaken using ontological theories, e.g., using Bunge’s (1977) theory of ontology applied to information systems by Wand and Weber (1993).

The theory of ontology is used to evaluate alternate modeling grammars. Ontological clarity is inversely related to one or more of the following factors: construct overload, construct redundancy, and construct excess (Weber 2003, Green and Rosemann 2004).

Hence, removing or reducing some or all of these factors will produce models that exhibit greater ontological clarity. Models exhibiting greater ontological clarity contain more information than models containing factors such as construct overload, construct redundancy, or construct excess; i.e., greater ontological clarity increases the expressiveness of the model. Thus, from a formal information theoretic perspective (Blackwell 1953), the models exhibiting greater expressiveness should lead to a better understanding of the domain being modeled.

Optionality is an important feature of many conceptual modeling grammars (Bodart et al. 2001). However, Wand et al. (1999) and Weber (1997) argue that things are perceived via the properties they possess, not via the properties they do not possess. Optional attributes and optional relationships are instances of construct excess (Weber 2003). Models that contain instances of construct excess do not faithfully represent the real-world system they are intended to model (Weber 2003). Wand and Weber (1993) and Weber (2003) state that optionality (the possibility of a property being not applicable) should be avoided so as to clearly convey the ontological meaning of the constructs in conceptual models and thereby increase the expressiveness of such models. These mandatory grammars produce clearer representations that lead to more sophisticated cognitive models and higher levels of domain understanding (Gemino and Wand 2005, p. 302). Thus, research to date (e.g., Burton-Jones and Weber 1998, Bodart et al. 2001, Weber 2003, Gemino and Wand 2005) has operationalized improved model expressiveness as greater ontologically clarity via the elimination of optional properties through the use of subtypes.<sup>1</sup>

Ontological clarity has been operationalized by eliminating optional properties in conceptual modelling settings by a variety of researchers. In addition to the research conducted by Bodart et al. (2001), empirical tests of the effects of ontological clarity have been conducted by Burton-Jones and Weber (1998), Gemino (1998), and Gemino and Wand (2005). Burton-Jones and Weber (1998) found that when experimental participants had to place greater reliance on the models, participants using the models with greater ontological clarity (i.e., increased model expressiveness) performed better. Gemino and Wand (2005) confirmed that improved model expressiveness increases understanding even with apparently more complex conceptual models. Similar to the Bodart et al. (2001) results, Gemino (1998) found that, for problem solving tasks, participants using more expressive models exhibited superior performance.

Prior research discussed in the previous paragraph has concentrated on examining conceptual models exhibiting improved model expressiveness via greater ontological clarity. Such conceptual data models are used as a basis for preparing logical data models (Hoffer et al. 2004).<sup>2</sup> These logical data models facilitate the “mapping between the conceptual model and the way data is ultimately laid out” (Bodart et al. 2001, p. 387). Bodart et al. (2001) state that even in logical (implementation) models, optionality should be avoided because these models are used for tasks that require deep cognition. The relationship between model expressiveness and query accuracy has been examined by Bowen et al. (2006). Their initial results tend to support the notion that increased model expressiveness leads to more accurate queries.

## 2.2. Task Complexity and Performance

A large body of research exists that investigates factors that affect end-user performance during query development (e.g., Axelsen et al. 2001; Borthick et al. 2001a, b). End user performance during query development has been shown to be affected by users’ abilities to understand the application domain (Jih et al. 1989, Rho and March 1997, Chan et al. 2004) and by users’ abilities to translate their understanding of the query domain correctly into a query language (Chan et al. 1993, Chan et al. 1999, Suh and Jenkins 1992).

However, irrespective of the type of task being performed, researchers are consistent in asserting a positive relationship between complexity and errors in task performance; i.e., as task complexity increases, performance decreases (March and Simon 1958, Campbell 1988, Rho and March 1997, Borthick et al. 2001b, Chan 1999, Jih et al. 1989, Crossland et al. 1995).

Furthermore, as task complexity increases, users’ confidence in their solutions to the problems is likely to decrease (Campbell 1988, Gardner and Serra 1997). Thus, problems arising from increased complexity include lower effectiveness (less accuracy), efficiency (longer time taken), and confidence (less confident in the accuracy of their output).

Campbell (1988) showed that task complexity comprises four dimensions: outcome multiplicity (number of desired outcomes of the task), solution scheme multiplicity (number of courses of action to attain the goal), conflicting interdependence (occurs when adopting one course of action conflicts with another course of action), and solution scheme/outcome uncertainty (level of uncertainty as to whether a given solution scheme will lead to the desired outcome). These dimensions have varying impacts on aspects of information overload and information diversity. The levels of these information processing factors affect the level of cognitive demands required by a person undertaking the task given that the more complex the task, the higher the level of cognitive effort required.

Relative to spatial tasks, complexity can also be viewed as comprised of component complexity, coordinative complexity, and dynamic complexity (Wood 1986); that is, total task complexity is a function of the component, coordinate, and dynamic complexity. Wood states that a unit of coordinate complexity contributes more to total task complexity than a unit of component complexity. Increases in task complexity can arise due to increases in any or all of these three types of complexity.

The task of query preparation requires a person to examine a given information request and, after examining a logical data model, prepare a query that produces information to satisfy that information request. The task of query preparation is affected by both component and coordinate complexity. The level of component complexity is affected by the number of attributes within each entity and the type of associations between the entities. The level of coordinate complexity is affected by the number of items that need to be located and assembled to form the query.

Using Wood’s definition of complexity, Mennecke et al. (2000) conducted a map reading experiment that included testing the effects of complexity on problem solving accuracy and efficiency. They found statistically significant results for their hypothesis that increases in task complexity reduce solution accuracy as well as partial support for their hypothesis that increases in task complexity reduce solution efficiency. Notably, in that study, Mennecke et al. (2000) did not find any efficiency differences for lowcomplexity tasks.

## 2.3. Model Expressiveness and Complexity

Examining various facets of complexity as instantiated by the two models investigated in this research revealed significant relationships between model expressiveness and complexity. In terms of this research, the more traditional parsimonious models can be viewed as having the greater component complexity; i.e., individual entities are likely to contain more attributes, more complex attribute values (e.g., NULLs), and more complex associations between sets of attribute values. Conversely, models that exhibit improved expressiveness, i.e., greater ontological clarity, are likely to exhibit greater coordinative complexity. That is, increasing clarity and expressiveness by creating subtypes produces more entities, which, in turn, requires the query formulations to perform more data reassembly (more joins). Thus, when preparing more expressive models from traditional parsimonious models, the component complexity is reduced but the coordinate complexity is increased. The assertion that a unit of coordinate complexity contributes more to total task complexity than a unit of component complexity implies that, for the two equivalent models, the more expressive model exhibits greater overall complexity than the parsimonious model.

## 2.4. Model Expressiveness, Task Complexity, Model Size, and Performance

A relationship exists among model expressiveness, task complexity, and performance. First, as model expressiveness increases there is an intuitive and logical argument that, via improved understanding of the model, performance will be improved. This improvement is represented by the dashed arc in Figure 1. As mentioned above, Kottemann and Remus (1989) found empirical evidence that naturalness and operational performance are not consistently related but that naturalness may actually impair performance.

Figure 1 Relationship Between Model Expressiveness, Query Task Complexity, and Performance  
![](/api/attachments/D2C9KVJW/fulltext/images/1b5aa49738ead74b822bde1c4eede7a614b899038e74e6cc5602b7265f06cef9.jpg)

Thus, the positive relationship in Figure 1 cannot be examined independent of the task being performed in that model. As the model expressiveness increases for the querying task being performed, replacing component complexity with coordinate complexity leads to an overall increase in complexity. Prior research confirms a negative relationship between task complexity and performance (March and Simon 1958, Campbell 1988, Rho and March 1997, Borthick et al. 2001b, Chan 1999, Jih et al. 1989). The relationships between expressiveness and complexity and between complexity and performance are represented by the solid lines in Figure 1.

Representations exhibiting greater ontological clarity, i.e., providing end users with more expressive models, facilitate users to think more deeply about the entities and their relationships. In general, when the logical models with increased expressiveness are still relatively small and despite the fact that they contain more entities than the traditional, parsimonious models (replacing component with coordinate complexity), users querying the data model are likely to experience only a small increase in overall complexity. Congruent with Wood’s (1986) assertion, a small increase in overall complexity typically does not negatively affect performance. That is, for small data models, representations exhibiting greater ontological clarity, in spite of their larger size, improve problem solving because of their superior ability to communicate the semantics of the problem domain (Weber 2003).

Increasing the size of the domain (model) in which a task is performed increases most if not all of the various dimensions of task complexity and results in an overall increase in complexity. When considering the relationship between model size and query preparation task complexity, as the size of the model increases so does the level of solution scheme multiplicity and the level of solution scheme/outcome uncertainty. Similarly, as the size of the model increases so do the levels of component and coordinate complexity.

Wood (1986) states that, for very small increases in complexity, the initial effect on performance may actually be positive. There is, however, a point at which the increases to the various types of complexity reach overload and lead to lower performance overall. This notion of a curvilinear relationship between complexity and performance is supported by the principles of parsimony (Occam’s razor), bounded rationality (Simon 1957), and minimum description length (Rissanen 1978, Hansen and Yu 2001). Similarly, statistical model selection criteria such as Akaike’s information criterion (AIC) (Akaike 1974) and the Bayesian information criterion (BIC) (Schwarz 1978) attempt to balance the benefits of more detailed models (increased information) against information overload (increases in model size). Furthermore, software defect prediction models (e.g., Akiyama 1971, Halstead 1975, Lipow 1982) consistently include terms that associate increases in size with increases in program defects (Fenton and Neil 1999). When sufficiently large data models are used, users mentally decompose the data model into cognitive portions that contain the entities, attributes, and relationships they require (Gemino and Wand 2005).

As users encounter larger data representations, the base level complexity of both types of models (those that exhibit improved expressiveness and those that are more parsimonious) will increase. Moving from a more complex parsimonious data model to an equivalent model that exhibits greater ontological clarity (thus more expressive) implies that, although the component complexity is reduced, the corresponding coordinate complexity is increased. Recall that a unit of coordinate complexity contributes more to total complexity than a unit of component complexity. Thus, as the logical data model grows, compared to approximately linear growth for the number of entities associated with parsimonious models, the number of entities associated with models that exhibit greater ontological clarity increases at a faster rate. The resulting overall increase in total complexity of the models that exhibit greater ontological clarity will lead to increased cognitive effort and therefore to an increase in the number of semantic errors made by users.<sup>3</sup>

<sup>Hypothesis</sup> <sup>1.</sup> As models grow users querying data structures that exhibit greater ontological clarity make more semantic errors than users querying equivalent parsimonious data structures.

Parsimonious data structures and data structures that exhibit greater ontological clarity present users with different types of challenges, and, therefore, both data structures affect the time users take to compose queries. Relative to parsimonious models, models that exhibit greater ontological clarity reduce the time required to compose queries by reducing component complexity. Conversely, relative to models that exhibit greater ontological clarity, parsimonious models reduce the time required to compose queries by reducing coordinative complexity. Processing the more expressive information associated with models that exhibit greater ontological clarity is likely to increase query time. Interpreting the lower clarity (greater ambiguity) associated with parsimonious models will, however, also increase query time.

Moving from a parsimonious data model to an equivalent model that exhibits greater ontological clarity implies that, whereas component complexity may be reduced somewhat, the coordinate complexity is likely to be increased substantially. This more dramatic increase in complexity for those models that exhibit greater ontological clarity implies that users will take longer to perform query tasks. Thus:

<sup>Hypothesis</sup> <sup>2.</sup> As models grow users querying data structures that exhibit greater ontological clarity take more time to construct queries than those querying parsimonious data structures.

For effective decision making, users must first extract the correct information from the database. After extracting this information, users’ confidence in the correctness of their queries affects their willingness to rely on the information obtained. Parsimonious data structures and data structures that exhibit greater ontological clarity present users with different challenges, and, therefore, both data structures affect users’ confidence in the accuracy of their queries. The lower component complexity and the finer information associated with representations exhibiting greater ontological clarity should increase users’ confidence. Conversely, the lower coordinative complexity associated with parsimonious models should increase the confidence of users of these models. Moving from a parsimonious data model to an equivalent model that exhibits greater ontological clarity implies that, whereas component complexity may be reduced somewhat, the coordinate complexity is likely to be increased substantially. This more dramatic increase in complexity for those models that exhibit greater ontological clarity implies that users will be less confident in the accuracy of their queries. Hence:

<sup>Hypothesis</sup> <sup>3.</sup> As models grow users querying data structures that exhibit greater ontological clarity are less confident in the accuracy of their queries than those querying parsimonious data structures.

## 3. Research Method

## 3.1. Research Design, Participants, and Data Collection

In two identical laboratory experiments conducted one year apart, participants composed and executed queries in SQL for one of two data structures.<sup>4</sup> Initially, two conceptual data models were created. The traditional/parsimonious conceptual data model contained optional attributes, optional relationships, and associative entities. The second conceptual data model (the more expressive data model) had the optional attributes, optional relationships, and associative entities removed through the use of supertype and subtype entities. These two conceptual data models were then transformed to their equivalent logical data structures,<sup>5</sup> i.e., the parsimonious logical data structure and the more expressive logical data structure that exhibited greater ontological clarity (see Appendix B). During the first experiment, 45 advanced undergraduate and master’s level commerce students participated in the experiment. During the repeat experiment, 35 advanced undergraduate and master’s level commerce students participated in the experiment. The two cohorts were students in equivalent courses being offered in two consecutive years. All participants were familiar with general computing concepts and activities and, prior to the experiment, had received training in developing SQL queries.<sup>6</sup> All participants received a set of instructions containing the scenario, the details of the tasks to be performed, their logical entity relationship diagram, and their data dictionary. To control for experience and education effects, participants were assigned to one of two groups according to their grade point average (GPA). The person with the highest GPA was ranked 1, the next ranked 2, etc. Participants were assigned to groups according to their rank, i.e., person 1 to group A, 2 to group B, 3 to group B, 4 to group A, and so forth. This method of assignment was adopted to make the two groups as equivalent as possible. The groups were then randomly assigned to a treatment.

The participants had two hours to construct as accurately as possible appropriate queries for as many as they could of the 14 information requests (Appendix C). Participants received 7% course credit for this task and were informed that they would be marked on the accuracy of each of the queries they entered. Because the correct query formulations generally increased in complexity, participants were encouraged to do their best on each query before moving to the next information request. Each information request had two correct formulations—one for the parsimonious data structure and one for the data structure exhibiting greater ontological clarity. The information requests were derived after three independent experts were given a description of the data contained in the data structures and the scenario. The experts were three academics with expertise in management accounting, logistics, and knowledge management, respectively. Each expert was asked to supply information requests that they expected would be required for operations management in a trucking company. These requests were used as the basis for the information requests in this experiment.

Participants used a UNIX shell script that recorded their entire session. Each participant was presented with the information requests in the same order. After each query attempt was executed, the system displayed the SQL result, i.e., either the rows returned by the query or a syntax error message. Participants could revise their queries as many times as they wished. When they indicated that they were satisfied with the result they obtained for a particular request, participants were prompted to specify their confidence that the query results were correct. After indicating their confidence levels, participants proceeded to the next information request. Once an information request had been completed by a participant, they could not return to it.

Subject to the constraints imposed by the laboratory setting, the experiment was designed to be as realistic as possible. For example, the feedback from the database management system (DBMS) throughout the experiment allowed the querying experience to approximate analogous organizational data searches, e.g., to revise and resubmit their queries. Similarly, in a business context that is subject to time constraints and deadlines, query developers are allowed as many attempts as they wish to obtain the desired information. Organizational query developers present only the results of their final query to the person making the information request. Hence, this research analyzed only each participant’s last attempt for each information request.

## 3.2. Operationalizing the Variables

3.2.1. Dependent Variables. Two experienced coders independently determined the minimum number of changes (if any) required to make each query from each participant semantically correct.<sup>7</sup> After the two individuals independently performed this task, they cross-checked their error coding sheets for correctness and consistency and resolved any differences.<sup>8</sup> The number of changes (errors) is the dependent variable for Hypothesis 1.

The dependent variable for Hypothesis 2 is the total time taken (in minutes) to compose the query for each information request. The value for this variable (time) was determined by examining the log files.

The dependent variable for Hypothesis 3 is the participants’ self-assessed confidence levels for each query. Participants were allowed to attempt each information request as many times as they wished. When participants indicated that they had completed each request, i.e., did not wish to make another attempt, they were prompted to specify their confidence that the query produced results that satisfied the given information request. Participants entered this measure on the following scale: 86–100%, 71–85%, 56–70%, 41–55%, 26–40%, 11–25%, and 0–10%. The values were recoded to a seven-point scale as follows: ratings of 86–100% recoded as 7 (extremely confident), ratings of 71–85% to 6, ratings of 56–70% to 5, ratings of 41–55% to 4, ratings of 26–40% to 3, ratings of 11–25% to 2, and ratings of 0–10% to 1 (extremely nonconfident).

3.2.2. Independent Variables. The independent variable was group. Group was a categorical variable with the values parsimonious and exhibiting greater ontological clarity (the operationization of improved model expressiveness). Two covariates were included in the statistical models. The information requests were generally of increasing complexity,<sup>9</sup> and, thus, information request (query) number assumed values from 1 to 14. GPA was the other covariate.

## 4. Results

## 4.1. Summary Performance

A comparison of the demographic data of the participants in each of the two years was performed,<sup>10</sup> and the results for each year were analyzed separately and combined. The interpretation of each set was consistent, thus allowing the reporting of the results of the pooled data. Table 1 summarizes the participants’ characteristics and performance by data structure. These results indicate that in absolute terms participants generated more query errors, took more time, and were less confident when querying the more expressive data structure that exhibited greater ontological clarity. The unit of analysis throughout the results is each information request of each participant.

## 4.2. The Effect of Model Expressiveness on Total Semantic Errors

Comparing the queries completed by the participants using the parsimonious data model with the queries completed by the participants using the more expressive data model exhibiting greater ontological clarity, analysis of covariance (ANCOVA) results<sup>11</sup> indicate that the number of semantic errors was significantly associated with the level of ontological clarity $( F _ { 1 , 5 4 0 } =$ 2861, $p = 0 . 0 0 0 1$ , two-tailed test) (Table 2). The least squares (LS) means<sup>12</sup> confirm that participants querying the data structure that exhibited greater ontological clarity made significantly more semantic errors than participants querying the parsimonious data structure (LS mean greater ontological clarity 1450, LS mean parsimonious 886, $p { = } 0 . 0 0 0 1 )$ .

<sup>10</sup> A comparison of the demographic data of the participants in each of the two years did not reveal any statistically significant differences based on GPA or gender. Age was statistically significant with the second year’s cohort averaging 1.6 years older than the first year’s cohort. Because we do not consider the age difference to materially affect the results of the experiments, this section reports results based on pooling both years’ data. Detailed demographic data for both years were GPA on a scale of 1–7 with 7 being the highest (mean year $1 = 4 . 6 3 1 5$ , mean year 2 <sub>=</sub> 45102, t <sub>=</sub> <sub>−</sub>022, $p = 0 . 8 2 8 6 )$ , gender (mean year $1 = 1 . 3 5 9 2$ , mean year 2 <sub>=</sub> 14438, t <sub>=</sub> <sub>−</sub>089, p <sub>=</sub> 03744), and age (mean year 1 <sub>=</sub> 21606, mean year 2 23249, t 308, p 00033).

<sup>11</sup> Nested ANCOVAs were also performed. The results led to the same conclusions.

<sup>12</sup> Least squares means test for differences between means after adjusting for the covariates, i.e., query number and GPA in this case.

Table 1 Participant Characteristics and Overall Performance

<table><tr><td></td><td>Parsimonious</td><td>More expressive</td></tr><tr><td colspan="3">GPA</td></tr><tr><td colspan="3">(7-point scale, 7 highest)</td></tr><tr><td>Mean</td><td>4.92</td><td>4.87</td></tr><tr><td>Standard deviation</td><td>1.02</td><td>1.01</td></tr><tr><td colspan="3">Gender</td></tr><tr><td>Number of males</td><td>28</td><td>24</td></tr><tr><td>Number of females</td><td>13</td><td>16</td></tr><tr><td colspan="3">Age</td></tr><tr><td>Mean</td><td>23.08</td><td>23.59</td></tr><tr><td>Standard deviation</td><td>3.28</td><td>3.54</td></tr><tr><td colspan="3">Number of information requests attempted</td></tr><tr><td>Mean</td><td>7.24</td><td>6.18</td></tr><tr><td>Standard deviation</td><td>1.79</td><td>1.68</td></tr><tr><td colspan="3">Semantic errors per request attempted</td></tr><tr><td>Mean</td><td>9.74</td><td>13.44</td></tr><tr><td>Standard deviation</td><td>13.72</td><td>15.55</td></tr><tr><td colspan="3">Confidence level per request attempted</td></tr><tr><td>Mean</td><td>6.05</td><td>5.49</td></tr><tr><td>Standard deviation</td><td>1.45</td><td>1.78</td></tr><tr><td colspan="3">Time per information request</td></tr><tr><td>Mean</td><td>14.77</td><td>17.22</td></tr><tr><td>Standard deviation</td><td>8.30</td><td>9.57</td></tr></table>

Notes. The table contains statistics related to each of the 81 participants. The number of information requests attempted excludes outliers.

Table 2 Effects of Data Structure on Semantic Errors

<table><tr><td>Source</td><td> $R^{2}$ </td><td>df</td><td>Mean square</td><td>F-value</td><td>Pr &gt; F</td></tr><tr><td>Model</td><td>0.32</td><td>3</td><td>12,397.54</td><td>83.83</td><td>0.0001</td></tr><tr><td>Error</td><td></td><td>540</td><td>147.90</td><td></td><td></td></tr><tr><td>Query number</td><td></td><td>1</td><td>33,983.94</td><td>229.78</td><td>0.0001</td></tr><tr><td>Group</td><td></td><td>1</td><td>4,231.36</td><td>28.61</td><td>0.0001</td></tr><tr><td>GPA</td><td></td><td>1</td><td>4,604.18</td><td>31.13</td><td>0.0001</td></tr></table>

## 4.3. The Effect of Model Expressiveness on Time to Compose Queries

Comparing the queries completed by the participants using the parsimonious data model with the queries completed by the participants using the more expressive data model exhibiting greater ontological clarity, ANCOVA results indicate that the time taken to compose a query was significantly associated with the level of ontological clarity $( F _ { 1 , 5 4 0 } = 1 7 . 3 1 , ~ p =$ 00001, two-tailed test) (Table 3). The least squares means confirm that participants querying the data structure that exhibited greater ontological clarity took significantly longer to compose their queries than participants querying the parsimonious data structure (LS mean greater ontological clarity <sub>=</sub> 1755, LS mean parsimonious  1449, p  00001).

Table 3 Effects of Data Structure on Time Taken

<table><tr><td>Source</td><td> $R^{2}$ </td><td>df</td><td>Mean square</td><td>F-value</td><td>Pr &gt; F</td></tr><tr><td>Model</td><td>0.11</td><td>3</td><td>1,630.90</td><td>22.67</td><td>0.0001</td></tr><tr><td>Error</td><td></td><td>540</td><td>71.93</td><td></td><td></td></tr><tr><td>Query number</td><td></td><td>1</td><td>2,858.40</td><td>39.74</td><td>0.0001</td></tr><tr><td>Group</td><td></td><td>1</td><td>1,245.29</td><td>17.31</td><td>0.0001</td></tr><tr><td>GPA</td><td></td><td>1</td><td>1,908.20</td><td>26.53</td><td>0.0001</td></tr></table>

## 4.4. The Effect of Model Expressiveness on Confidence

Comparing the queries completed by the participants using the parsimonious data model with the queries completed by the participants using the more expressive data model that exhibited greater ontological clarity, ANCOVA results indicate that participants’ confidence in the accuracy of their queries was significantly associated with the level of ontological clarity $( F _ { 1 , 5 4 0 } = 2 5 . 9 9 , p = 0 . 0 0 0 1$ , two-tailed test) (Table 4). The least squares means results confirm that participants querying the data structure that exhibited greater ontological clarity were significantly less confident in the accuracy of their queries than participants querying the parsimonious data structure (LS mean greater ontological clarity <sub>=</sub> 543, LS mean parsimonious <sub>=</sub> 611, p <sub>=</sub> 00001).

## 4.5. The Effect of Model Expressiveness on Different Types of Semantic Errors

Table 5 summarizes the performance of participants in relation to the different types of errors made. Because of the increase in coordinative complexity (i.e., more tables), more expressive models that exhibit greater ontological clarity are expected to be associated with more FROM and JOIN errors. Because of the increase in component complexity (i.e., more complex attribute values), parsimonious models are expected to be associated with more CONDITION errors. Table 5 confirms these expectations.

Table 4 Effects of Data Structure on User Confidence

<table><tr><td>Source</td><td> $R^{2}$ </td><td>df</td><td>Mean square</td><td>F-value</td><td>Pr &gt; F</td></tr><tr><td>Model</td><td>0.12</td><td>3</td><td>60.11</td><td>25.66</td><td>0.0001</td></tr><tr><td>Error</td><td></td><td>540</td><td>2.34</td><td></td><td></td></tr><tr><td>Query number</td><td></td><td>1</td><td>105.95</td><td>45.23</td><td>0.0001</td></tr><tr><td>Group</td><td></td><td>1</td><td>60.87</td><td>25.99</td><td>0.0001</td></tr><tr><td>GPA</td><td></td><td>1</td><td>53.84</td><td>22.99</td><td>0.0001</td></tr></table>

More expressive data models that exhibit greater ontological clarity versus parsimonious models are expected to have minimal direct effects on SELECT, GROUP BY, and HAVING clauses. However, these three clauses may exhibit indirect effects based on whether or not users experience greater cognitive challenges when dealing with coordinative versus component complexity. Relative to the data models used in this study, in absolute terms participants generated more SELECT errors when querying the parsimonious model and more GROUP BY and HAVING errors when querying the more expressive data model that exhibited greater ontological clarity (Table 5).

Comparing the queries completed by the participants using the parsimonious data model with the queries completed by the participants using the data model that exhibited greater ontological clarity, ANCOVA results indicate that neither the number of SELECT errors nor the number of CONDITION errors was significantly associated with the level of ontological clarity (Table 6). Comparing the queries completed by the participants using the parsimonious data model with the queries completed by the participants using the data model that exhibited greater ontological clarity, ANCOVA results indicate that the number of FROM, JOIN, GROUP BY, and HAVING errors were all significantly associated with the level of ontological clarity. In all cases, the means results (Table 5) confirm that participants querying the parsimonious data structure made significantly fewer of each type of errors than participants querying the data structure that exhibited greater ontological clarity.

Table 5 Performance for Different Error Types

<table><tr><td></td><td>Parsimonious</td><td>More expressive</td></tr><tr><td>SELECT errors per attempted queryMean (standard deviation)</td><td>2.11 (4.75)</td><td>1.80 (3.60)</td></tr><tr><td>FROM errors per attempted queryMean (standard deviation)</td><td>0.57 (1.30)</td><td>0.80 (1.38)</td></tr><tr><td>JOIN errors per attempted queryMean (standard deviation)</td><td>2.69 (5.62)</td><td>5.03 (6.71)</td></tr><tr><td>CONDITION errors per attempted queryMean (standard deviation)</td><td>1.54 (2.85)</td><td>1.42 (3.26)</td></tr><tr><td>GROUP BY errors per attempted queryMean (standard deviation)</td><td>1.84 (4.49)</td><td>2.77 (5.64)</td></tr><tr><td>HAVING errors per attempted queryMean (standard deviation)</td><td>0.88 (2.43)</td><td>1.51 (3.41)</td></tr></table>

Table 6 Effect of Model Expressiveness on Different Types of Semantic Errors

<table><tr><td>Error type</td><td> $R^{2}$ </td><td>F-value</td><td>Pr &gt; F</td></tr><tr><td>SELECT</td><td>0.10</td><td>0.00</td><td>0.9825</td></tr><tr><td>FROM</td><td>0.08</td><td>7.94</td><td>0.0050</td></tr><tr><td>JOIN</td><td>0.13</td><td>30.71</td><td>0.0001</td></tr><tr><td>CONDITION</td><td>0.19</td><td>0.59</td><td>0.4446</td></tr><tr><td>GROUP BY</td><td>0.17</td><td>12.34</td><td>0.0005</td></tr><tr><td>HAVING</td><td>0.16</td><td>14.95</td><td>0.0001</td></tr></table>

Notes. Each row of the table represents a different statistical test. Thus, the SELECT row indicates the R-squared, the F -value, and the p-value for the ANCOVA results when SELECT errors is taken as a dependent variable; the FROM row indicates the R-squared, the F -value and the p-value for the ANCOVA results when FROM errors is taken as a dependent variable and so on.

4.6. Comparison of Current and Prior Research Slight differences in size exist between the Bodart et al. (2001) data models (third experiment) and the data models used in this research. These modest differences in model size imply that the different statistical results between this and prior results cannot be attributable to increases in model size alone.

The more substantive differences are likely to relate to the types of problem-solving tasks posed in the two experiments. The Bodart et al. (2001) problem solving tasks required participants to answer questions without referring to the data model and went beyond the extraction of information from within their designated data model. The participants were required to use their creativity and insights to extrapolate from the information provided without actual visual reference to the data model. For example, the first question in Table 8 of Bodart et al. (2001) is: “A research project that was supposed to be completed last month has not been completed. What reasons can you provide for the delay in completion? Write down as many alternatives as you can think of.” Furthermore, performance differences occurred because of the quality of the participants’ inherent creativity, insights, and business experience rather than merely the information provided in data models themselves. Thus, in terms of the various subdimensions of task complexity, there is outcome multiplicity as well as conflicting interdependence. By improving the model expressiveness via the removal of the optional properties, these dimensions of complexity for this particular task may have decreased. Thus, there is an overall decrease in task complexity leading to an increase in performance.

In contrast to the abstraction from the data models required by the Bodart et al. (2001) participants, this research required participants to make precise use of the information provided in the data models. The requirement for precise use and the goal of better reflecting real query development performance meant that participants were allowed to view the model and scenario information throughout the task. The primary external factor affecting performance is the participants’ knowledge of SQL with minimal impacts related to creativity or business experience. Participants in this research had to perform a very meticulous analysis of selected attributes, tables, and foreign keys in the data models to compose an exact query formulation. This type of task is affected by the replacement of component by coordinate complexity.

Table 7 contrasts the results of this research on larger-sized data models with the results of the corresponding Bowen et al. (2006) research on more modest-sized data models. Panel A summarizes the differences relative to accuracy, time, and confidence. When considering accuracy, participants using smaller-sized models that exhibited greater ontological clarity made significantly fewer errors than participants using smaller-sized parsimonious models. In contrast, participants using larger-sized models that exhibited greater ontological clarity made significantly more errors than participants using corresponding larger-sized parsimonious models. In both the smaller and larger models, the models with improved expressiveness were more complex than their corresponding parsimonious data model. For both larger-model situations, the overall complexity increased further because each model was more complex than its corresponding smaller data model; i.e., the larger parsimonious data model was more complex than the smaller parsimonious data model. These increases in model complexity due to both size and expressiveness increased the query task complexity and negatively affected query accuracy associated with the larger model that exhibited greater ontological clarity more than the query accuracy associated with the corresponding larger, more parsimonious model.

Table 7 Comparison of Findings for Smaller vs. Larger Models

<table><tr><td colspan="6">Panel A—Comparison of parsimonious data models and models that exhibit greater ontological clarity (OC): Effectiveness, efficiency, and confidence</td></tr><tr><td>Dependent variables</td><td>Model size</td><td>Prediction</td><td>Rationale</td><td>Findings</td><td>Interpretation/implication</td></tr><tr><td rowspan="2">SEMANTIC ERRORS TIME and CONFIDENCE</td><td>Smaller</td><td>OC is expected to be associated with fewer errors, less time, and greater confidence.</td><td>The increase in overall task complexity is minimal for OC as component complexity is replaced by coordinate complexity (Wood 1986).</td><td>OC made significantly less errors and were significantly more confident (Bowen et al. 2006). Time was not significantly different.</td><td>For smaller models the removal of component complexity was beneficial. Supports small increases in complexity, which can lead to increased performance.</td></tr><tr><td>Larger</td><td>OC is expected to be associated with more errors, more time, and lower confidence.</td><td>The increase in overall task complexity is larger for OC as component complexity is replaced by coordinate complexity (Wood 1986).</td><td>OC made significantly more errors, took significantly longer, and were significantly less confident than participants using the parsimonious models.</td><td>For larger models, the increase in coordinative complexity outweighed the benefits gained from the removal of component complexity.Supports larger increases in complexity, which can lead to decreased performance.</td></tr></table>

Panel B—Comparison of parsimonious data models and models that exhibit greater ontological clarity (OC): Types of errors

<table><tr><td>Error type</td><td>Expectation</td><td>Rationale</td><td>Findings</td><td>Interpretation/implication</td></tr><tr><td>SELECT</td><td></td><td></td><td></td><td></td></tr><tr><td>Smaller</td><td>Parsimonious expected to be associated with more errors.</td><td>Higher levels of component complexity.</td><td>Parsimonious associated with more errors.</td><td rowspan="2">For querying tasks, the relative effects of component complexity decrease as model size increases.</td></tr><tr><td>Larger</td><td>Parsimonious expected to be associated with more errors.</td><td>Higher levels of component complexity.</td><td>Groups not significantly different.</td></tr><tr><td>FROM</td><td></td><td></td><td></td><td></td></tr><tr><td>Smaller</td><td>OC expected to be associated with more errors.</td><td>Higher levels of coordinative complexity.</td><td>OC associated with more errors.</td><td rowspan="2">Coordinative complexity negatively affects performance.</td></tr><tr><td>Larger</td><td>OC expected to be associated with more errors.</td><td>Higher levels of coordinative complexity.</td><td>OC associated with more errors.</td></tr><tr><td>JOIN</td><td></td><td></td><td></td><td></td></tr><tr><td>Smaller</td><td>OC expected to be associated with more errors.</td><td>Higher levels of coordinative complexity.</td><td>OC associated with more errors.</td><td rowspan="2">Coordinative complexity negatively affects performance.</td></tr><tr><td>Larger</td><td>OC expected to be associated with more errors.</td><td>Higher levels of coordinative complexity.</td><td>OC associated with more errors.</td></tr><tr><td>CONDITION</td><td></td><td></td><td></td><td></td></tr><tr><td>Smaller</td><td>Parsimonious expected to be associated with more errors.</td><td>Higher levels of component complexity.</td><td>Parsimonious associated with more errors.</td><td rowspan="2">For querying tasks, the effects of component complexity decrease as model size increases.</td></tr><tr><td>Larger</td><td>Parsimonious expected to be associated with more errors.</td><td>Higher levels of component complexity.</td><td>Groups not significantly different.</td></tr></table>

When considering efficiency, different levels of ontological clarity did not produce a significant difference in time per information request for the smaller data model. In contrast, participants using largersized models that exhibited greater ontological clarity took significantly longer than participants using larger-sized parsimonious models. As with query accuracy, these increases in model complexity due to both size and expressiveness increased the query task complexity and negatively affected query accuracy associated with the larger model that exhibited greater ontological clarity more than the query accuracy associated with the corresponding larger, more parsimonious model.

When considering confidence, participants using smaller-sized models that exhibited greater ontological clarity were significantly more confident than participants using smaller-sized parsimonious models. In contrast, participants using larger-sized models that exhibited greater ontological clarity were significantly less confident than participants using largersized parsimonious models. As with query accuracy and efficiency, these increases in model complexity due to both size and expressiveness increased the query task complexity and negatively affected query accuracy associated with the larger model that exhibited greater ontological clarity more than the query accuracy associated with the corresponding larger, more parsimonious model.

Relative to SELECT and CONDITION errors, participants using smaller-sized models that exhibited greater ontological clarity made significantly fewer errors than participants using smaller-sized parsimonious models. In contrast, no statistically significant differences were observed between participants using larger-sized models that exhibited greater ontological clarity versus participants using larger-sized parsimonious models. These results suggest that, for querying tasks, the positive aspects of a reduction in component complexity decrease as size of model increases.

Relative to FROM and JOIN errors, for both smaller and larger sets of data models, participants using models that exhibited greater ontological clarity made significantly more errors than participants using parsimonious models. These results suggest that, for querying tasks, the negative aspects of an increase in coordinate complexity are accentuated as the size of the model increases.

## 5. Conclusions, Limitations, and Future Research

This study examined the relationship between the level of model expressiveness of data structures, i.e., the level of ontological clarity and end-user performance during query development. The results indicated that, relative to participants using the parsimonious implementation, participants using the implementation that exhibited greater expressiveness via greater ontological clarity made significantly more semantic errors, took significantly more time to compose their queries, and were significantly less confident in the accuracy of their queries. Differences in query errors occurred in the FROM, JOIN, GROUP BY, and HAVING sections of the queries.

The research provides an initial challenge as to whether the results of prior research (e.g., Gemino 1998, Burton-Jones and Weber 1998, Bodart et al. 2001, Bowen et al. 2006) are robust for all task types as data models increase in size. That is, the generally accepted idea that more expressive data models improve problem solving may not hold for information retrieval tasks as the size of the data models increase.

Ontological clarity is a normative approach with similarities to information economics models. In a similar manner to Hilton’s (1980) reapproachment of information economics and human information processing models, data modelers striving for increased expressiveness need to consider the potential effects on cognitive effort of increased coordinative complexity. That is, information economics research has mathematically proven that finer information sets, e.g., more expressive data models, are potentially at least as valuable as less expressive representations (Blackwell 1953, Hilton 1979). Actually attaining these benefits may, however, require training and tools to overcome or mitigate cognitive limitations. For example, users may need assistance creating or identifying good decompositions (chunks) for specific tasks, e.g., for composing queries for specific information requests.

From a more general perspective, the experiment reported in this paper extends research into the concept of naturalness, i.e., conceptual ease of use (Stabell 1983), the theory of cognitive fit (Vessey 1991), and tradeoffs between expressiveness and understandability (Khatri et al. 2004). In this paper, conceptual ease of use and cognitive fit would be congruent with model expressiveness operationalized as ontological clarity and would, ceteris paribus, be expected to improve performance. Using a production scheduling problem, Kottemann and Remus (1989) investigated linear and quadratic relationships and varied environmental complexity at low and intermediate levels. Interestingly, they did not investigate high levels of environmental complexity because they viewed high levels of environmental complexity as an overload condition. Kottemann and Remus (1989) found empirical evidence that naturalness and operational performance are not consistently related and that naturalness may actually impair performance. Combined with the Bowen et al. (2006) results, this research provides additional evidence of tradeoffs between expressiveness and understandability for the concrete and pervasive setting of query construction. Investigating factors that affect these tradeoffs, such as the proximity principle (Wickens and Carswell 1995), chunk decomposition (Knoblich et al. 1999, Ormerod et al. 2002), or annotations (Khatri et al. 2004), may provide valuable insights.

Implications of these results for practitioners include exercising caution when adopting findings from conceptual data modeling to logical data modelling. Striving for greater ontological clarity within logical data models may not necessarily result in improved performance by end users who use these data models for information retrieval. Practitioners may need to consider alternative means of improving the clarity of existing parsimonious data models. This could be by clarifying the existing metadata via more explanatory data dictionaries and for traditional parsimonious data structures by explaining the meaning of optional properties (both attributes and relationships) relative to state changes or subclassifications. Because the issue of complexity cannot be considered independent of the task to be performed, practitioners need to carefully consider the effects that the various types of complexity have on their circumstances.

Implications of these results for researchers include the need to test whether the problem solving benefits of greater ontological clarity for conceptual data models holds in medium-sized and large-sized logical data models. Researchers also need to develop better modeling grammars that facilitate greater ontological clarity for both conceptual and logical data models without dramatically increasing the complexity of these semantic models.

This study has several limitations. First, the usual caveats associated with laboratory experiments limit the generalizability of the results. Second, the results of this research and the results of the research of Bowen et al. (2006) depend on a number of factors including the method of constructing the models and the set of information requests provided to the participants. The research did not consider possible complications or different outcomes that can arise during the transformation process from the conceptual data model to logical data model tables. Furthermore, in comparing the results of this and prior research other factors not controlled as part of the experimental process could potentially affect the results. Third, the results are dependent on the particular information requests presented to the participants and the relative levels of complexity of the information requests. Fourth, the results may be dependent on the type of database management system adopted. Fifth, the research used students as participants. However, these participants had received training in information technology (IT) and business-related subjects, and their level of query proficiency was likely to be typical of users in many organizations.

Future research is needed to improve users’ abilities to extract the information they need. Seven examples of such research are noted here. First, this experiment needs to be replicated in various forms using different application environments. The study also needs to be replicated using different sets of information requests within an experimental setting with an increased number of participants. This type of additional research will allow us to better determine the types of errors that are likely to increase or decrease. Second, further research could investigate user performance using similar-sized (or even larger) data models. These data models should include those with which the users are familiar. Such research would allow an investigation of how model expressiveness affects user performance in more realistic business settings. Third, research needs to be undertaken to determine the types of tasks that are best suited to using the more expressive models in an attempt to improve performance. The type of research could also determine the use of more expressive models that are better matched to particular types of database management systems and tasks to determine the most appropriate task technology fit. Fourth, theory needs to be developed and experimentally verified concerning the construction of optimal mixed models that use features of both parsimonious models and models that exhibit greater ontological clarity. This future research could investigate alternate ways of operationalizing model expressiveness. Fifth, research is needed to determine the optimal characteristics of metadata for parsimonious data models, e.g., to minimize the effects of attributes that can contain NULLs. Sixth, to complete information retrieval tasks, users must first comprehend the application domain as a necessary antecedent to formulating their queries. Research is required to determine whether the users of more expressive models performed less well because they experienced difficulty comprehending the application domain or because they were less effective formulating their queries. Seventh, the process by which users arrive at their final query formulations can also be investigated.

## Acknowledgments

The authors thank Ron Weber for his comments, suggestions, and encouragement throughout the project. They appreciate the comments and suggestions provided by participants at a University of Melbourne workshop, by an ICIS 2004 review team headed by senior editors Ritu Agarwal and Laurie Kirsch, and by ICIS 2004 participants on an earlier version of the manuscript based on the first of two years’ experimental data. The authors also appreciate the comments and suggestions provided by participants at The University of Queensland and Florida State University workshops on a more recent version of the manuscript based on the expanded data set with two years’ experimental data. The authors also appreciate the comments and suggestions provided by the reviewers and associate editor. The authors are grateful for the funding provided for this research by the University of Queensland Business School and for the data coding assistance provided by Alice Wu.

![](/api/attachments/D2C9KVJW/fulltext/images/42771d8dd4a3772aa4c89a2d77d609cc795f576df521b19b4ee5debf38486d06.jpg)

Figure A.1(b) Optional Property in Ontologically Clear Model  
![](/api/attachments/D2C9KVJW/fulltext/images/31a5299320b1b433d6115c3ba78ff0a089615d17e975629347c50f78343a8a37.jpg)

## Appendix A. Operationalization of Removal of Optional Properties

Within data modeling two optional situations can arise. The first situation occurs when a “thing” may or may not possess an attribute, i.e., an optional attribute. In relational database management systems (RDBMSs), optional attributes occur when an attribute can contain NULLs. The second situation occurs when a “thing” may or may not participate in a relationship with another thing, i.e., an optional relationship. In RDBMSs, optional relationships occur when the minimum cardinality between two tables is zero.

Optionality arising from the two situations can be avoided and thus construct excess avoided through the use of subclasses, typically mutually exclusive subclasses (Weber 2003). By eliminating construct excess the model produced will exhibit greater ontological clarity. To derive the model that exhibits greater ontological clarity, the data modeler removes the optional properties (attributes and/or relationships) by creating a subclass that represents those “things” that possess the property and other subclasses representing those “things” that do not possess the property. Consider the following example in relation to optional attributes: a trip has a scheduled departure date and an actual departure date. When initially creating the trip record the scheduled departure date is completed; however, the actual departure date is not known, i.e., actual departure date is an optional attribute at this point (see Figure A.1(a)). The solution that exhibits greater ontologica clarity is a model using two subtypes: one for trips that have departed and another for trips that are yet to depart (see Figure A.1(b)).<sup>13</sup>

Appendix B. Data Structures  
Parsimonious data model  
![](/api/attachments/D2C9KVJW/fulltext/images/5f1747357ff5ff751fb1851911676c3552c61aeb33f4e61958a1aacb8b403eeb.jpg)

![](/api/attachments/D2C9KVJW/fulltext/images/1daa8dd1ad830ab0214d88065ab7f09c6265acd081f903b544af22b994e84843.jpg)

<table><tr><td>Request</td><td>Parsimonious data model</td><td>Model exhibiting greater ontological clarity</td></tr><tr><td>2</td><td>SELECT surname, firstname, license_No, employment_date, ((birth_date - SYSDATE)/365)AgeFROM driversWHERE license_No NOT IN(SELECT license_NoFROM driver_performance_ratings);</td><td>SELECT surname, firstname, drivers.license_No, employment_date, ((birth_date -SYSDATE)/365)AgeFROM drivers, driver_no_performance_ratingsWHERE drivers.license_No = driver_no_performance_ratings.license_No;</td></tr><tr><td>3</td><td>SELECT trips.truck_No, trips.trip_No,cargo_item_name, cargo_items.max_temp,trucks.min_tempFROM trips, bills_of_lading, cargo_items,trucksWHERE bills_of_lading.trip_No = trips.trip_NoAND bills_of_lading.bol_No = cargo_items.bol_NoAND trips.truck_no = trucks.truck_noAND cargo_items.max_temp &lt; trucks.min_temp;</td><td>SELECT trips.truck_No, trips.trip_No,cargo_item_name, refrigerated_cargo.max_temp, refrigerated_trucks.min_tempFROM refrigerated_trucks, trips, bills_of_lading, cargo_items, refrigerated_cargoWHERE refrigerated_trucks.truck_No = trips.truck_NoAND bills_of_lading.trip_No = trips.trip_NoAND bills_of_lading.bol_No = cargo_items.bol_NoAND cargo_items.bol_No = refrigerated_cargo.bol_NoAND cargo_items.cargo_item_no = refrigerated_cargo.cargo_item_noAND refrigerated_cargo.max_temp&lt;refrigerated_trucks.min_temp;</td></tr><tr><td>5</td><td>SELECT trips.trip_No, trips.route_No,scheduled_depart_date, scheduled_arrive_date, actual_depart_date, actual_arrive_date,COUNT(license_No)FROM trip_drivers, trips, routesWHERE trip_drivers.trip_No = trips.trip_NoAND trips.route_No = routes.route_NoAND scheduled_depart_date &gt; “1-May-2003”AND actual_arrive_date IS NOT NULLGROUP BY trips.trip_No, trips.route_No,scheduled_depart_date, scheduled_arrive_date, actual_depart_date, actual_arrive_date,optimal_No_driversHAVING COUNT(license_No) &lt; optimal_No_drivers;</td><td>SELECT trips.trip_No, trips.route_No,scheduled_depart_date, scheduled_arrive_date, actual_depart_date, actual_arrive_date,COUNT(license_No)FROM trip_drivers, trips, routes, departed_and_arrivedWHERE trip_drivers.trip_No = trips.trip_NoAND trips.route_No = routes.route_NoAND trips.trip_No = departed_and_arrived.trip_NoAND scheduled_depart_date &gt; “1-May-2003”GROUP BY trips.trip_No, trips.route_No,scheduled_depart_date, scheduled_arrive_date, Actual_depart_date, actual_arrive_date, optimal_No_driversHAVING COUNT(license_No) &lt; optimal_No_drivers;</td></tr></table>

## Appendix C. Information Requests

The fourteen information requests are provided below with sample queries for three included in Table C.1.

Question 1. For drivers whose license expires prior to the 1st December 2003 list surname, first name, license number, license expiration date, and license types.

Question 2. For drivers that have never received a performance rating, list their surname, first name, license number, employment date, and age in years.

Question 3. For cargo items shipped in a truck that the minimum temperature of the truck was greater than the maximum temperature of the cargo item, list truck number, trip number, cargo item name, maximum temperature of the cargo item, and minimum temperature of the cargo item.

Question 4. Since the 1st September 2003 (based on scheduled departure date), list each driver’s surname, first name, license number, and the total number of kilometers they have driven.

Question 5. For trips that had fewer than the recommended optimal number of drivers since the 1st May 2003 (based on scheduled departure date), list trip number, route number, scheduled departure date, scheduled arrival date, actual departure date, and actual arrival date.

Question 6. For loads that exceeded the legal max weight since the 1st November 2003 (based on scheduled departure date), list trip number and amount of excess weight.

Question 7. For tankers carrying a load less than half of the allowable load along routes greater than 1,000 km since the 1st May 2003 (based on scheduled departure date), list route number, trip number, truck number, scheduled departure date, and scheduled arrival date.

Question 8. For drivers who, since the 1st October 2003 (based on scheduled departure date), have driven more than 5 trips not ranked as either their preference 1 or 2, list surname, first name, license number, number of trips that were not preference 1 or 2, and the route that is their first preference.

Question 9. For drivers under 40 years old, list the number of drivers together with the average and standard deviation of those drivers’ performance ratings. In the same report, for drivers 40 and over, list the number of drivers together with the average and standard deviation of those drivers’ performance ratings.

Question 10. For bill clients with total delivery charges greater than \$1,000 since the 1st of November 2001 (based on actual delivery date), list client number, client name, the total delivery charges together with their average and standard deviation of the number of days between date paid and actual deliver date.

Question 11. For trips since the 1st November 2003 (based on scheduled departure date), list each driver’s surname, first name, and percentage of trips they made that were more than 1 day late. Note that you should list all drivers, even if they have never been more than 1 day late.

Question 12. For company clients that are deliver clients associated with shipments with total charges greater than \$1,000 since the 1st November 2002 (based on scheduled delivery date) and a promised delivery date since the 1st November 2002 (based on scheduled delivery date), list the client number, client name, total charges, and the percent change in charges from 1 Nov 2002 to 30 April 2003 versus charges from 1 May 2003 to 31 Oct 2003.

Question 13. For trips since the 1st May 2003 (based on schedule departure date), list route number, start city and state, end city and state, and the revenue per kilometer driven.

Question 14. For trips greater than 3,000 km, with 2 drivers, that arrived 1 or more days early since the 1st November 2002 (based on scheduled departure date), list trip number, surname and first name of both drivers, scheduled departure date, scheduled arrival date, actual departure date, and actual arrival date.

## References

Akaike, H. 1974. A new look at the statistical model identification. IEEE Trans. Automatic Control 19 716–723.

Akiyama, F. 1971. An example of software system debugging. Inform. Processing 71 353–379.

Axelsen, M., A. F. Borthick, P. L. Bowen. 2001. A model for and the effects of information request ambiguity and end user query performance. Proc. Internat. Conf. Inform. Systems, New Orleans, LA, Association for Information Systems, Atlanta, 537–542.

Balzer, R. 1979. An implementation methodology for semantic data base models. Proc. Internat. Conf. Entity Relationship Approach to Systems Anal. Design, ACM-SIGMOD, Los Angeles, 433–444.

Batra, D. 1993. A framework for studying human error behavior in conceptual database modeling. Inform. Management 25 121–131.

Blackwell, D. 1953. Equivalent comparisons of experiments. Ann. Math. Statist. 24 265–73.

Bodart, F., M. Sim, A. Patel, R. Weber. 2001. Should optional properties be used in conceptual modelling? A theory and three empirical tests. Inform. Systems Res. 12(4) 384–405.

Borthick, A. F., P. L. Bowen, D. R. Jones, M. H. K. Tse. 2001a. The effects of information request ambiguity and construct incongruence on query development. Decision Support Systems 32(1) 3–25.

Borthick, A. F., P. L. Bowen, S. Liew, F. H. Rohde. 2001b. The effects of normalization on query developer query errors: An experimental evaluation. Internat. J. Accounting Inform. Systems 2(4) 195–223.

Bowen, P. L., R. A. O’Farrell, F. H. Rohde. 2006. Analysis of competing data structures: Does ontological clarity produce better end user query performance. J. Assoc. Inform. Systems 7(8) 514–544.

Bunge, M. 1977. Treatise on Basic Philosophy: Volume 3: Ontology I: The Furniture of the World. Reidel, Boston.

Burton-Jones, A., R. Weber. 1998. Understanding relationships with attributes in entity-relationship diagrams. Internat. Conf. Inform. Systems, Helsinki, Finland. Association for Information Systems, Atlanta, 214–228.

Campbell, D. J. 1988. Task complexity: A review and analysis. Acad. Management Rev. 13(1) 40–52.

Chan, H. C., K. K. Wei, K. L. Siau. 1993. User-database interface: The effect of abstraction level on query performance: A field experiment. MIS Quart. 17(4) 441–464.

Chan, H. C., B. C. Y. Tan, K. K. Wei. 1999. Three important determinants of user performance for database retrieval. Internat. J. Human Comput. Stud. 51(1) 895–918.

Chan, H. C., K. L. Siau, K. K. Wei. 2004. Effects of query complexity and learning on novice user query performance with conceptual and logical database interfaces. IEEE Trans. Systems, Man Cybernetics, Part A (Systems Humans) 34(2) 276–281.

Crossland, M. D., W. C. Perkins, B. E. Wynne. 1995. Spatial decision support systems: An overview of technology and a test of efficacy. Decision Support Systems 14 219–235.

Fenton, N. E., M. Neil. 1999. A critique of software defect prediction models. IEEE Trans. Software Engrg. 25(5) 675–689.

Gardner, W. B., M. Serra. 1997. An object-oriented layered approach to interfaces for hardware/software codesign of embedded systems. Thirty-First Annual Hawaii Internat. Conf. System Sci., Honolulu, 197–203.

Gemino, A. 1998. To be or may to be: An empirical comparison of mandatory and optional properties in conceptual modelling. Proc. Annual Conf. Admin. Sci. Assoc. Canada, Saska toon, Saskatchewan, Canada. Administration Science Associa tion: Information Systems Division, 33–44.

Gemino, A., Y. Wand. 2005. Complexity and clarity in conceptual modelling: Comparison of mandatory and optional properties. Data Knowledge Engrg. 55 301–326.

Green, P., M. Rosemann. 2004. Applying ontologies to business and systems modelling techniques and perspectives: Lessons learned. J. Database Management 15(2) 105–117.

Halstead, M. H. 1975. Elements of Software Science. Elsevier, North Holland, New York.

Hansen, M. H., B. Yu. 2001. Model selection and the principle of minimum description length. J. Amer. Statist. Assoc. 96(454) 746–774.

Hilton, R. W. 1979. The determinants of information system value: An illustrative analysis. J. Accounting Res. 17 411–35.

Hilton, R. W. 1980. Integrating normative and descriptive theories of information processing. J. Accounting Res. 18(2) 477–505.

Hoffer, J. A., J. F. George, J. S. Valacich. 2004. Modern Systems Analysis and Design, 4th ed. Addison Wesley Longman, Reading, MA.

Jih, K., D. Bradbard, C. Snyder, N. Thompson. 1989. The effects of relational and entity-relationship data models on query performance of query developers. Internat. J. Man-Machine Stud. 31(3) 257–267.

Khatri, V., S. Ram, R. T. Snodgrass. 2004. Augmenting a conceptual model with geospatio-temporal annotations. IEEE Trans. Knowledge Data Engrg. 16(11) 1324–1338.

Khatri, V., I. Vessey, S. Ram, V. Ramesh. 2006. Cognitive fit between conceptual schemas and internal problem representations: The case of geospatio-temporal conceptual schema comprehension. IEEE Trans. Professional Comm. 49(2) 109–127.

Knoblich, G., S. Ohlsson, H. Haider, D. Phenius. 1999. Constraint relaxation and chunk decomposition in insight problem solving. J. Experiment. Psych. Learn., Memory, Cognition 25 1534–1556.

Kottemann, J. E., W. E. Remus. 1989. A study of the relationship between decision model naturalness and performance. MIS Quart. 23(2) 171–181.

Lipow, M. 1982. Number of faults per line of code. IEEE Trans. Software Engrg. 8(4) 437–439.

March, J., H. A. Simon. 1958. Organizations. John Wiley, New York.

Mennecke, B. E., M. D. Crossland, B. L. Killingsworth. 2000. Is a map more than a picture? The role of SDSS technology, subject characteristics and problem complexity on map reading and problem solving. MIS Quart. 24(4) 601–629.

Ormerod, T. C., J. N. MacGregor, E. P. Chronicle. 2002. Dynamics and constraints in insight problem solving. J. Experiment. Psych. Learn., Memory, Cognition 28(4) 791–799.

Owei, V., S. B. Navathe, S. R. Hyeun. 2002. An abbreviated conceptbased query language and its exploratory evaluation. J. Systems Software 63(1) 45–67.

Purao, S., V. C. Storey, T. Han. 2003. Improving analysis pattern reuse in conceptual design: Augmenting automated processes with supervised learning. Inform. Systems Res. 14(3) 269–290.

Rissanen, J. 1978. Modeling by shortest data description. Automatica 14 465–471.

Rho, S., S. T. March. 1997. An analysis of semantic overload in database access systems using multi-table query formulation. J. Database Management 8(2) 3–14.

Schwarz, G. 1978. Estimating the dimension of a model. Ann. Statist. 6 461–464.

Shoval, P., I. Frumermann. 1994. OO and EER conceptual schemas: A comparison of user comprehension. J. Database Management 5(4) 28–38.

Simon, H. A. 1957. Models of Man. John Wiley and Sons, New York.

Stabell, C. 1983. A Decision-Oriented Approach to Building DSS in Building Decision Support Systems. J. Bennett, ed. Addison Wesley, Reading, MA.

Suh, K. S., A. M. Jenkins. 1992. A comparison of linear keyword and restricted natural language database interfaces for novice users. Inform. Systems Res. 3(3) 252–272.

Vessey, I. 1991. Cognitive fit: A theory-based analysis of graphs vs. tables literature. Decision Sci. 22(2) 219–240.

Wand, Y., R. Weber. 1993. On the ontological expressiveness of information system analysis and design grammars. J. Inform. Systems 4(4) 299–330.

Wand, Y., V. C. Storey, R. Weber. 1999. An ontological analysis of the relationship construct in conceptual modelling. ACM Trans. Database Systems 24 494–528.

Weber, R. 1997. Ontological Foundations of Information Systems. Coopers and Lybrand, Melbourne, Australia.

Weber, R. 2003. Conceptual modelling and ontology: Possibilities and pitfalls. J. Database Management 14(3) 1–20.

Wickens, C. D., C. M. Carswell. 1995. The proximity principle: Its psychological foundation and relevance to display design. Human Factors 37(3) 473–494.

Wood, R. E. 1986. Task complexity: Definition of the construct. Organ. Behav. Human Decision Processes 37 60–82.

Young, G. K., S. T. March. 1995. Comparing data modeling formalisms. Comm. ACM 38(6) 103–115.
