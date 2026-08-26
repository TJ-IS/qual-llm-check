---
otero_id: 9878
otero_key: "RXHD67E9"
title: "Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries"
authors: "Gove Allen; Jeffrey Parsons"
year: "2010"
journal: "Information Systems Research"
doi: "10.1287/isre.1080.0189"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/RXHD67E9/fulltext/images/4ab2a81a70f4d05f838a682c88dbe0298499b71fe0d410638e5052ce03342066.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries

Gove Allen, Jeffrey Parsons,

## To cite this article:

Gove Allen, Jeffrey Parsons, (2010) Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries. Information Systems Research 21(1):56-77. http://dx.doi.org/10.1287/isre.1080.0189

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2010, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/RXHD67E9/fulltext/images/dcd1f2553ca8afbd23dbf4ac52e95ff01c92005fd353a55fb0a4f9ef6bcf7066.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Is Query Reuse Potentially Harmful? Anchoring and Adjustment in Adapting Existing Database Queries

Gove Allen

Marriott School of Management, Brigham Young University, Provo, Utah 84601, gove@byu.edu

Jeffrey Parsons

Faculty of Business Administration, Memorial University of Newfoundland, St. John’s, Newfoundland and Labrador A1B 3X5, Canada, jeffreyp@mun.ca

eusing database queries by adapting them to satisfy new information requests is an attractive strategy for extracting information from databases without involving database specialists. However, the reuse of information systems artifacts has been shown to be susceptible to the phenomenon of anchoring and adjustment. Anchoring often leads to a systematic adjustment bias in which people fail to make sufficient changes to an anchor in response to the needs of a new task. In a study involving 157 novice query writers from six universities, we examined the effect of this phenomenon on the reuse of Structured Query Language (SQL) queries under varying levels of domain familiarity and for different types of anchors. Participants developed SQL queries to respond to four information requests in a familiar domain and four information requests in an unfamiliar domain. For two information requests in each domain, participants were also provided with sample queries (anchors) that answered similar information requests. We found evidence that the opportunity to reuse sample queries resulted in an adjustment bias leading to poorer quality query results and greater overconfidence in the correctness of results. The results also indicate that the strength of the adjustment bias depends on a combination of domain familiarity and type of anchor. This study demonstrates that anchoring and adjustment during query reuse can lead to queries that are less accurate than those written from scratch. We also extend the concept of anchoring and adjustment by distinguishing between surface-structure and deep-structure anchors and by considering the impact of domain familiarity on the adjustment bias.

Key words: reuse; anchoring and adjustment; SQL; query formulation

History: Sumit Sarkar, Senior Editor; Dennis Galletta, Associate Editor. This paper was received on October 10, 2006, and was with the authors 11 months for 4 revisions. Published online in Articles in Advance December 18, 2008.

## Introduction

The fields of software engineering and information systems have long been concerned with the potential of reusing systems development artifacts (e.g., Frakes and Terry 1996, Kim and Stohr 1998, Mili et al. 1995). Interest initially focused on code reuse (Cox 1990), but has broadened to include other systems analysis and design artifacts. Reuse offers the prospect of numerous benefits, including improved quality (Frakes and Succi 2001), decreased development time and cost (Griss 1993), and greater user satisfaction (Succi et al. 2001). However, there is disagreement on the success of reuse initiatives, with conflicting evidence of success (Lim 1994) and failure (Fichman and Kemerer 1997) and indications of the need for healthy skepticism in evaluating the potential for reuse (Irwin 2002).

Challenges to successful reuse have generally been considered in terms of technical issues, such as developing and maintaining repositories of reusable artifacts and providing effective classification and search mechanisms to retrieve potentially reusable artifacts (Li et al. 2006), as well as management issues surrounding reuse incentives (Fichman and Kemerer 1997, Kim and Stohr 1998, Morisio et al. 2002, Pittman 1993, Purao et al. 2003). Cognitive factors constitute an additional challenge to effective reuse. In particular, the anchoring-and-adjustment phenomenon (a cognitive heuristic that can lead to bias) has recently been found to propagate errors during the reuse of both source code and conceptual schemata (Parsons and Saunders 2004).

Considering the longstanding interest in reusing many information systems artifacts (Frakes and Terry

1996), it is surprising that research has all but ignored database query reuse, especially given the high degree of standardization of Structured Query Language (SQL). Queries written to satisfy one information request can be adapted to satisfy similar requests. Moreover, because SQL queries are expressed as text, they are portable across operating systems and database management systems.

In view of these considerations, database queries have considerable potential for reuse. SQL queries can be written by relative novices who have limited training in the language (Fagan and Corley 1998). There are commercial and open-source tools for building and managing SQL repositories (e.g., netlegger.net, quest.com, keeptool.com, plnet.org, and ibatis.apache.org), as well as some academic research on tools to support query reuse (e.g., Oussalah and Seriai 2000a, b). In this context, Fagan and Corley (1998) describe a case-based reasoning system developed to find relevant reusable queries in an SQL repository. Although statistics are not available for all projects, netlegger.net has an SQL repository user base approaching 10,000.<sup>1</sup> In addition, commercial interest in the subject is evident from recent patents and patent applications (assigned to companies such as IBM) that describe methods for managing reusable query components (Dettinger et al. 2004, 2007; Edlund et al. 2002).

We are not aware of any research showing the extent of query reuse in practice. However, there is reason to believe that the practice can be quite common. In the alumni affairs offices of both the authors’ institutions, reuse of SQL queries is the de facto standard for query writing. Both computing professionals and other end users regularly adapt existing queries to satisfy requests from a range of stakeholders, including presidents, deans, individual and corporate donors, and organizers of alumni events. In this setting, where dozens of queries are written weekly, adaptive reuse is the norm and queries are written from scratch only very rarely.

Reusing an existing query by adapting it to satisfy the requirements of a related information request is a problem-solving activity that involves determining the changes that need to be made to a query for it to satisfy the requirements of the request. People typically use cognitive heuristics to support judgments in problem-solving tasks. In particular, anchoring and adjustment is a well-known heuristic used in problem-solving tasks for which an initial solution requiring adaptation is available. This paper examines the impact of anchoring and adjustment on adaptive SQL query reuse by novice query writers. We begin by describing anchoring and adjustment and indicating how it can be manifested in information systems development. We then consider the context of database query reuse. Mili et al. (1995) identify four phases of reuse: (1) searching for and retrieving potentially reusable artifacts, (2) understanding these artifacts and evaluating their suitability for reuse, (3) adapting the artifacts to the reuse context, and (4) integrating them into the current project. We describe an experiment designed to examine anchoring and adjustment in a query reuse context, focusing on phases two and three of that framework. We present the results of the study and conclude by considering the implications of our findings.

## Anchoring and Adjustment in Systems Development

People adopt strategies to facilitate judgment and simplify problem solving in complex situations. Such strategies are generally referred to as cognitive heuristics. Heuristics reduce the cognitive effort associated with decision-making and problem-solving tasks and are important coping mechanisms (Plous 1993). However, use of heuristics has been shown to result in systematic biases in judgments. The impacts of cognitive heuristics have been widely studied in cognitive psychology (e.g., Tversky and Kahneman 1974, Epley and Gilovich 2006). However, with few exceptions (e.g., George et al. 2000, Parsons and Saunders 2004), there has been limited research on the use of cognitive heuristics in information systems development (Stacy and MacMillan 1995).

One well-known cognitive heuristic is anchoring and adjustment. Anchoring refers to the tendency, in a decision-making, judgment, or problem-solving context for which a correct solution exists, to stick closely to an initial estimate if one is provided. Tversky and Kahneman (1974) describe a classic example in which subjects are asked to estimate the percentage of African nations that are members of the United Nations. Subjects provided with a higher anchor (e.g., those initially asked if the percentage is higher or lower than 70) consistently provide higher estimates than those provided with a lower anchor (e.g., those initially asked if the percentage is higher or lower than 30). Thus, the initial estimate serves to anchor subjects’ final estimates.

The anchoring heuristic reduces the cognitive effort associated with a judgment or a decision-making task. However, as the above example shows, people often fail to make adequate modifications to an initial solution and subsequently produce estimates that are severely flawed with respect to the correct solution. This is the adjustment bias. Hereafter, we use the phrase anchoring and adjustment to refer to the entire phenomenon and anchoring heuristic and adjustment bias to refer to the respective components, as appropriate.

A related issue in judgment and decision making is the effort-accuracy tradeoff (Johnson and Payne 1985). Generally, accuracy in a task is a function of the cognitive effort devoted to the task. Contextual factors, such as the importance of a decision or judgment, affect the level of effort a person devotes to a task. Against this backdrop, using an available anchor can be seen as an effort-reduction strategy (the effort required to adjust from an anchor can be much less than that required to solve a problem from scratch). Evidence of an adjustment bias suggests that the decrease in effort results in a corresponding decrease in accuracy.

Within the information systems field, George et al. (2000) demonstrated that anchoring and adjustment is resistant to explicit interventions designed to mitigate it. They developed a decision support system containing interventions intended to counteract the heuristic, but found that anchoring and adjustment nevertheless occurred. Parsons and Saunders (2004) studied anchoring and adjustment with respect to the adaptive reuse of code and design artifacts (anchors) in systems development.<sup>2</sup> In the context of artifact reuse in systems development, adjustment bias occurs when the final artifact is close to the starting point, even though the requirements call for greater changes to the artifact being reused. Their study provided empirical evidence of the tendency of developers to include unrequested functionality in their solutions when it was present in the reuse artifact, as well as evidence of a tendency for errors in a reuse artifact (relative to requested functionality) to propagate to solutions. In short, anchoring and adjustment poses a potential challenge that needs to be better understood if it is to be managed to facilitate effective adaptive reuse in systems development. However, it has not been studied in the context of query reuse.

## Query Reuse

The ability to use organizational data resources effectively is a source of competitive advantage. Both transactional databases and data warehouses commonly provide end users (in addition to database professionals) access to company data in support of strategy formulation, decision making, and other management activities (Borthick et al. 2001). Although there has been significant research on multidimensional and graphical interfaces to databases (Speier and Morris 2003), SQL remains the standard for ad hoc query formulation. Accurately composing queries in SQL is a challenging task (Chan et al. 1993, Leitheiser and March 1996), involving at least three distinct steps (Ogden 1985): query formulation (stating the information need in natural language), query translation (stating the query in terms of the data schema independent of the query language syntax), and query writing (producing a syntactically valid, executable statement).

As SQL queries are specified using text rather than graphical elements, an individual can easily reuse a query by copying it and using it as the starting point to compose a query to answer a different information request. Moreover, because SQL is a standard, queries can be shared between environments on vastly different operational platforms, provided the database schemata have semantically similar elements.

However, adaptive query reuse is a cognitively different process than query formulation. In query formulation, the user naturally generates a syntaxneutral statement of the information request on the way to producing a valid SQL statement. In adaptive query reuse, a valid SQL statement is available, allowing the user to use difference reduction techniques (Anderson 1993) in mapping directly from the information request to SQL. Accordingly, we expect that the existing SQL query will serve as an anchor from which users may find it difficult to adjust adequately.

Anchoring and adjustment in query reuse has a further dimension that has not received attention in previous studies of the heuristic. In general, familiarity with a domain affects one’s ability to understand a conceptual schema of that domain (Khatri et al. 2006, Parsons and Cole 2005). The impact of domain familiarity on anchoring and adjustment has not been studied extensively; most prior research has focused on narrow tasks in domains that are presumed to be unfamiliar. For example, when asking someone to estimate the percentage of a population having a particular blood type and providing an excessively high or low anchor, the presumption underlying an adjustment bias is that the respondent does not know the correct value. We are aware of only one study that has examined the effect of domain familiarity on anchoring and adjustment: Wright and Anderson (1989) found that “increasing situation familiarity did not result in decreased anchoring” (p. 72). In this context, a secondary objective of our research is to explore more deeply whether and how domain familiarity influences the tendency to anchor.

## Research Methodology

## Research Model

The research model for this study, presented in Figure 1, is adapted from prior research in the area of user performance in database systems use (Allen and March 2006, Chan et al. 1993). The model asserts that user performance in query formulation is influenced by the characteristics of the data model, the task, the user, and the system.

This study examines user performance in SQL query formulation under two domains with different levels of familiarity. Specifically, it examines the effect of the opportunity to modify an existing query to satisfy a new information request on (1) query accuracy, (2) time to construct the query, (3) users’ confidence in query accuracy, and (4) the degree to which that confidence is associated with query accuracy.

Figure 1 Research Model  
![](/api/attachments/RXHD67E9/fulltext/images/e767d7e18e1a1d3fd3c46f8d4d59ea17ce5371a2eeeeccaae9914fc6805ae87c.jpg)  
Note. Current study parameters italicized.

## Hypotheses

Anchoring and adjustment suggests that participants who reuse existing queries will anchor to the available query and fail to make necessary changes to adapt the query to the context of the new information request. This, in turn, will increase the likelihood of errors when adaptively reusing a query versus starting from scratch. For anchoring and adjustment to occur in query reuse, two conditions must exist. First, a query that can serve as an anchor must be available. Second, the user must choose to adapt the existing query. In the second condition, the anchor must be outside the solution’s plausible range as judged by the individual (Epley and Gilovich 2006). The anchor must not be too similar to the correct solution; otherwise, it might be reused as is. Conversely, if it is too different from the correct solution, it might not be recognized as a reusable artifact (Mili et al. 1995).

Following Epley and Gilovich (2006), we expect that once an adapted query produces results and appears similar to the information request in terms of tables, attributes, and restriction conditions, participants will view the query as a plausible solution and will cease comparing the query semantics to those of the information request. In so doing, they will arrive at a solution without adequately understanding the artifact being reused, thus bypassing a critical phase in the reuse process—understanding artifacts and evaluating their potential for reuse (step 2 of Mili et al. 1995)—and preventing themselves from adequately evaluating the correctness of their solution. However, when no sample is available for modification, participants are forced to examine (and understand)

the semantics of both the information request and the database schema to produce a plausible solution. Of course, users might introduce their own errors as they construct plausible solutions without assistance; however, as long as the required query is not beyond the users’ capability,<sup>3</sup> we expect the presence of the anchor to result in lower accuracy than users will achieve when formulating queries without assistance. This is consistent with the effort-accuracy tradeoff (Johnson and Payne 1985) because the latter situation requires more effort to produce a working query than the former. Thus, we propose our first hypothesis.

Hypothesis 1 (H1). Query writers will be less likely to produce queries that correctly satisfy information requests when they have the opportunity to modify existing queries than when they must compose queries without assistance.

We further expect that when individuals are provided with an anchor, they will be able to arrive at their solution query more quickly because a substantial portion of the time spent in query formulation is taken by mapping the terms in the information request to the terms in the database schema to produce a syntax-neutral data statement (Ogden 1985). When a query is available for adaptive reuse, query writers can try to change the query directly so that it conforms to the information request, bypassing the time-consuming step of developing the syntax-neutral data statement. Moreover, users will be able to copy the query rather than retype it, yielding additional time savings. In contrast, the time needed to construct a query that executes and appears to satisfy the information request can be substantial, as the user must map the terms from the information request to the terms in the database schema. Accordingly, we propose our second hypothesis.

Hypothesis 2 (H2). Query writers will formulate queries to answer information requests more quickly when they have the opportunity to modify existing queries than when they must compose queries without assistance.

In addition, we expect that when query writers are provided with an anchor, the cognitive effort required to develop the query will be lower than the effort needed to build a query from scratch. They will be able to verify that the query executes and produces results by running it, and will have evidence it is related to the information request in the current task. Thus, they have evidence of the plausibility of adjustments to the anchor and the effort associated with the adjustment will be lower (Epley and Gilovich 2006). Because prior research has shown a negative relationship between cognitive effort and confidence (Robinson et al. 1997), we expect that the opportunity to reuse will lead to higher confidence in the correctness of queries. Furthermore, participants tend to have higher confidence in easier queries than they do in more difficult queries (Chan et al. 1993); we expect that it will seem easier to adapt than to compose because the existing query restricts the problem space by providing mappings from the information request to the database schema. Thus, we propose our third hypothesis.

Hypothesis 3 (H3). Query writers will be more confident in the correctness of their queries when they have the opportunity to modify existing queries than when they must compose queries without assistance.

Although confidence is traditionally examined in query formulation studies (e.g., Borthick et al. 2001, Chan et al. 1993, Leitheiser and March 1996), its value (in isolation) is questionable. High confidence is good only when a query produces the correct answer. If the answer is incorrect, high confidence can be dangerous, as it may lead to unwarranted confidence in decisions based on erroneous data. Only when confidence is considered in conjunction with accuracy can meaningful conclusions be drawn. When a query produces an incorrect answer (or answers a different question), low confidence is much preferred to high confidence because it will lead the user to place lower value on the quality of a query’s result. When users have low confidence in incorrect queries, it is appropriate for them to seek help on the query or to engage in further analysis to verify their results. Accordingly, we are interested in how strongly an individual’s confidence in the correctness of a query is associated with its actual correctness.

Because we expect adaptive reuse to lead to reduced correctness (H1) and increased confidence (H3), it follows that users’ confidence will show less association with the correctness of their queries under conditions of adaptive reuse. Because this relationship has been shown to be significant even in the absence of significant findings for either accuracy or confidence (Allen and March 2006), we state it formally as a hypothesis of this study as follows.

Hypothesis 4 (H4). Confidence will be less strongly associated with query correctness when query writers have the opportunity to modify existing queries than when they must compose queries without assistance.

Domain familiarity has been shown to affect the understanding of artifacts used in information systems development (Khatri et al. 2006, Parsons and Cole 2005). We expect domain familiarity to mitigate the adjustment bias when participants reuse queries. When a domain is familiar, query writers will readily understand an existing query and its potential for reuse (Mili et al. 1995) and will make an accurate assessment of the query’s plausibility (Epley and Gilovich 2006). Query writers can focus on matching familiar domain constructs expressed in the information request with those in the query that is being reused and will thereby be better able to make necessary changes. In contrast, when a domain is unfamiliar, query writers will be less able to evaluate the suitability of the reused query, making any query that produces results (that appear to match constructs in the domain) seem plausible. Because we examine how domain knowledge affects the ability to identify and adjust from anchors, we examine each required adjustment individually rather than the overall query accuracy collectively. Thus, we propose our fifth hypothesis.

Hypothesis 5 (H5). Query writers will better identify and adapt the portions of existing queries that need modification to meet new information requirements in a familiar domain than in an unfamiliar domain.<sup>4</sup>

Note that there may be varying levels of difficulty in detecting and making needed adjustments to a query that is being reused. In attempting to evaluate the suitability of the query for reuse (Mili et al. 1995), users can map directly from the information request to the SQL statement. By skipping the development of the syntax-neutral statement (Ogden 1985), users will find it easier to identify needed changes that do not rely on an understanding of the database schema. For example, an incorrect parameter value (e.g., Salary > 50-000 instead of Salary > 10-000) requires no knowledge of the schema to correctly identify. Similarly, a required change that involves an attribute name (e.g., ${ \mathrm { h i r e d a t e } } = { } ^ { \prime \prime } 1 0 / 2 6 / 2 0 0 2 ^ { \prime \prime }$ instead of birthdate $^ { \prime \prime } 1 0 / 1 2 / 2 0 0 0 ^ { \prime \prime } )$ can also be achieved by using patternmatching techniques without a need to understand the schema. We term such cases “surface-structure” anchors. We expect attention to be naturally drawn to surface-structure differences when comparing an information request to a query being considered for adaptive reuse. In contrast, a required change in a join expression necessitates that the user sufficiently understand the schema to accurately map the entities and relationships in the information request to those of the schema. This illustrates a “deep-structure” anchor that will require more cognitive effort both to identify and to modify correctly. Thus, we expect the following hypothesis.

Hypothesis 6 (H6). Query writers will be better able to identify and to adjust from surface-structure anchors than from deep-structure anchors.

## Research Method

To test these hypotheses, we conducted an Internetmediated experiment involving participants from six universities in the United States. We administered the experiment by developing a query-formulation system that allowed individuals using a Web browser to view simultaneously an information request and the relevant graphical database schema representation. They could build, execute, and review the results of queries. The system was used in homework exercises and two pilot studies. After each pilot study, modifications were made to the system and the experimental treatments.

In the final experiment, participants were shown 12 information requests (six each in two domains, discussed in detail below) one at a time, each of which participants answered by formulating queries on their own schedules. Participants were allowed to write and execute as many queries as necessary during the development of the query they finally recorded as their solution for a given information request. Once they recorded their query as the solution to the information request, they were prompted to express their confidence in their solution; only then could they advance to the next information request. Participants could return to previously completed information requests only after they had recorded a solution query and expressed their confidence for all information requests. Of the six requests in each domain, the first two were always accompanied by sample queries. They were provided to allow participants to gain experience working with the domain and the experimental interface. Participant performance on these queries was not included in the data analysis. Of the four remaining questions in each domain, two were simple, requiring only a single join, and two were more complex, requiring three joins. In each pair of information requests, participants were provided with sample queries for one of the two, determined by random assignment. Thus, in each domain, participants were asked to formulate a simple query and a complex query in the presence of a set of suggested sample queries as well as a simple query and a complex query without any suggested sample.

## Independent Variable—Opportunity to Reuse Query

The complete set of information requests is reproduced in Appendices A and B. Of the eight information requests used in the manipulation of this independent variable, four were given to each participant without any accompanying query on which the participant might anchor. The other four were presented along with two possible queries each, which the participant could reference while composing a query to answer the information request. Each of the two sample queries required the same transformation to be successfully modified to meet the information request. The two queries differed only in layout and in the syntax used to accomplish the join. One used the SQL ’87 syntax that lists tables in the “from” clause and specifies the join conditions in the “where” clause; the other used the SQL ’92 syntax that specifies the join in the “from” clause. Participants were informed that the sample queries were written by a competent employee.

The information requests were constructed in pairs of equal complexity. Consider this pair:

How many times have professors employed students from Arizona $( { \mathrm { s t a t e } } = { } ^ { \prime \prime } { \mathrm { A } } Z ^ { \prime \prime } ) ?$

How many sponsors are the primary sponsors for courses that can be taken for credits ranging from 1 to 3 (credit\_range = “1–3”)?<sup>5</sup>

As seen below in the pair of queries that satisfies these two requests, the requests can be answered by queries that differ in only the tables and fields that are referenced. They both require a single join, a single restriction, a single summary, and a single projection.

select count(student\_id) from student s

join employment e on s.id e.student\_id

where state “AZ”

select count(distinct s.id) from course c

join sponsor s on s.id = c.primary\_sponsor\_id

where credit\_range “1–3”

For these two information requests, half of the participants received two sample queries for the first and half received two sample queries for the second. To demonstrate, we show the pair of sample queries presented for the first:

select max(wage) from student s

join employment e on s.id = e.student\_id

join work\_experience w on w.student\_id = s.id

where s.state “AK”

select max(wage) from student s,

employment e, work\_experience w

where s.id e.student\_id and

$$
\text { w. student\_id } = \text { s.id   and   s.state } = \text {"AK"}
$$

To correctly modify either of these sample queries, it is necessary to change “max” to “count,” change $" \mathrm { A K } ^ { \prime \prime }$ to “AZ,” and remove the reference and join to the “work\_experience” table. In this way, each participant had the opportunity to reuse an existing query for an information request of a given complexity and was required to formulate a query of identical complexity for a parallel information request without exposure to a set of sample queries. Because participants were randomly assigned to a treatment that determined which sample queries were presented, the possibility that one of the information requests was inherently more easily satisfied than the other was controlled.

When a sample query was supplied, participants could choose to modify it or they could compose their solution query from scratch. Although we provided a “copy query” button in the interface, a user could anchor on the example just by looking at the sample—without using the button. Because we cannot be sure that a participant did not anchor on a sample when available, we did not restrict this variable to only those known to have modified the sample. To the extent that participants ignored the sample and composed queries from scratch, this treatment was diluted.

## Independent Variable—Surface-Structure vs. Deep-Structure

As can be seen from the changes required to correctly adjust the example queries above, two involved relatively simple changes (modifying a restriction operand and changing an aggregate function). These require little more than direct mapping from the information request to the SQL statement—without the need to understand how the terms in the information request connect to the database schema. We term such required changes “surface-structure anchors” because the absence of a syntax-neutral data statement (Ogden 1985) does not hinder the participant’s ability to make the adjustment. In addition to restriction operands and aggregate functions, surface-structure anchors include attributes listed in the select clause and the arithmetical and logical operators included in the restriction (where clause).

In contrast, determining that a join needs to be removed from, added to, or changed in the sample query requires the participant to understand how the terms in the information request map to the database schema. This understanding is greatly influenced by the presence of the syntax-neutral data statement. Constructing such a statement is a fundamental step in the development of a query from scratch (Ogden

1985), but is more easily overlooked in the process of query modification. We refer to join expressions that require change as “deep-structure anchors.”<sup>6</sup> Each of the eight information requests contained both surfacestructure and deep-structure anchors.

## Independent Variable—Domain Familiarity

Because this study hypothesizes that the effect of anchoring and adjustment on query reuse depends on the level of domain familiarity, a design is needed that makes it possible to evaluate participants’ performance under different levels of domain familiarity. Although a few studies have examined the effect of domain familiarity on an individual’s ability to reason about a conceptual representation of that domain (Burton-Jones and Weber 1999, Khatri et al. 2006, Parsons and Cole 2005), we are aware of no studies that have tested the effect of domain familiarity on the performance of users’ query formulation.

It has been difficult to study empirically the effects of domain familiarity. Traditionally, random assignment of participants to treatments requires that all participants begin with low domain familiarity. After assignment, subjects in one treatment are given training to increase their familiarity with a domain. This approach can be time consuming and can result in a training bias. Building on a similar approach used to study the role of domain familiarity in understanding conceptual schemata (Khatri et al. 2006), we have developed a technique that allows a researcher both to randomly assign participants to a level of domain familiarity without the need for domain training and to make that assignment on a within-subjects basis. We began with a real database expected to be of low domain familiarity for our participants. We selected the Gene Ontology database (http://www.geneontology.org) because the number of tables is neither so small that it is trivial nor so large that it is incomprehensible. This database is freely available and is used by genetics researchers as a controlled vocabulary to describe genes and gene product attributes. We implemented the database on a database server and constructed a schema diagram reflecting its contents (Appendix C). Tables without data were omitted from the diagram and database.

Next, we removed the names of the tables and attributes from the schema, leaving the structure (position of tables, number of attributes in each table, relationships between tables, and cardinality of relationships) intact. We used this structure to construct a database schema for a university registration system—a domain with which we expected our participants (university students) to have higher familiarity. We mapped semantics of the university domain to the structure taken from the gene ontology schema without modification. To reduce the likelihood that participants would recognize the schemata as structurally identical, we converted the university schema diagram to its mirror image (Appendix D). We then built the university database and populated it with data from a real university registration system. The amount of data is similar in both databases, each having tables with anywhere from hundreds to hundreds of thousands of records.

For this study, we have two structurally identical databases, differing only in the semantics of the domains they represent. This enabled us to formulate a query in one database and easily construct its counterpart in the other. Structurally, the two queries are identical; they reference tables in analogous positions in the two schema diagrams. However, they answer different questions because their semantics are based on different domains. With the two parallel queries, we can compose an information request that is satisfied by each. These two information requests share a common underlying structure, but differ in that they are expressed using the domain semantics of parallel schemata. These two information requests can now be given to a single user. As the requests and schemata differ only in domain semantics, we can essentially ask that user to formulate the same query twice—once under a condition of lower domain familiarity and once under a condition of higher domain familiarity. As long as participants do not realize that the domains are structurally equivalent, we can examine the difference in performance as a result of differences in domain familiarity. Using this approach, we mitigate the context effects associated with learning in a within-subjects design by counterbalancing (using a random order of exposure to the domains) and camouflaging the treatment by using mirror images of the schema diagrams in the treatments (Greenwald 1976). Participants completed all the information requests in one domain before moving to the other domain.

## Dependent Variables

The primary measure of query performance is accuracy. We measured accuracy as a dichotomous variable indicating whether the submitted query correctly answers the information request. Historically, query formulation studies evaluated accuracy using scales that indicate the “degree of correctness” of the query itself (e.g., Batra et al. 1990, Chan et al. 1993, Borthick et al. 2001, Bowen et al. 2006). This is often useful in increasing the variability of the measure, which can help in statistical analysis. However, such measures have typically not measured how close the query’s answer set is to being correct. For example, the use of a greater-than sign (>) instead of a less-than sign (<) would be scored as a minor error, even though such an error could yield a result set that is exactly the opposite of what is requested. The effect of relying on the results of an incorrect query can be considered only by evaluating the result set itself. Accordingly, we evaluate each query as either producing the correct result set or not. Although it is possible that a query may produce the correct result set using incorrect logic, such queries should not be scored as correct. We also reviewed each query that produced a correct result set for semantic correctness. In only one case among our participants did a query produce the correct answer with incorrect logic; this query was scored as incorrect. Moreover, in the context of examining reuse of an existing query, evaluating the correctness of a query based on how many changes are required to produce the correct answer may also be inappropriate because the sample queries provided might themselves require very few changes to correctly meet the demands of a given information request.

The second measure of query performance is the time it takes for a participant to complete each query. This variable is measured as the number of minutes between when a user was shown the information request and when the user indicated that the written query answered the information request. The third dependent measure of query performance is a participant’s self-reported confidence that the query he or she produced accurately satisfies the information request. Following prior studies (e.g., Chan et al. 1993, Leitheiser and March 1996, Borthick et al. 2001, Allen and March 2006), we collect confidence as a single measure using a five-point Likert scale.

The final measure of query formulation performance is the degree to which participants’ confidence in the correctness of their queries predicts the actual correctness of the queries. To measure this, we used the mean probability score (Yates 1990). This measure is bounded by zero and one, where zero equals no error, or perfect prediction. The mean probability score is used to evaluate performance on judgment tasks involving probabilistic predictions of outcomes unknown at the time judgment is made. The mean probability score is simply the average of the squared difference between the prediction and the outcome for a given set of judgments. Suppose a query writer is 75% confident that a query satisfies the information request? If in fact the query does satisfy the request, the probability score for that assessment would be (075 − 1)<sup>2</sup>, or 0.0625. If the query does not satisfy the request, the score would be (075 0)<sup>2</sup>, or 0.5625. Although mean probability score is used in many judgment tasks to motivate the judge, participants in our experiment were unaware of its use so they could not try to minimize their score. If participants knew of this measure, they could minimize it by writing a query known to not satisfy the information request and then expressing very low confidence in its correctness. Because mean probability score requires a probabilistic judgment, we converted from our five-point Likert scale of confidence (very low, low, medium, high, and very high) to confidence assessments of 0, 0.25, 0.5, 0.75, and 1. We chose these assessments because they are the only set of five assessments that cover the scale from zero to one in equal intervals.<sup>7</sup>

In addition to examining performance in query formulation, we also sought to understand how well participants adjust from anchors (H5 and H6). To assess this, we examined the SQL queries participants formulated in the presence of a sample query. We measured their ability to adjust from the anchor as the percentage of anchors correctly adjusted.

## Controlled Variables

The two remaining factors from Figure 1 that affect query formulation performance (user characteristics and system characteristics) were controlled. User characteristics were controlled by the within-subject nature of the experimental design. Given that comparisons between experimental treatments will be made on an individual basis, the way in which different user characteristics affect the treatments will be completely balanced. Participants were drawn from introductory database management courses at six universities in the United States and therefore can be categorized as novice query writers. Most participants indicated that they had no work experience in a job that required SQL query formulation; fewer than 10% of participants indicated that they had more than one year’s experience in a job that required SQL query formulation. To encourage participation, students were given extra credit in their database courses for participating in the study. They were either given credit for their performance or were given credit if their performance met a certain level. Although 188 participants began the experiment, only 157 formulated queries for all information requests. The number of participants by university ranged from 4 to 58.

All participants used the same system and were exposed to the same information requests, thus this factor was held constant. The use of a query formulation system that allows participants to execute and access results to queries (or see the relevant error message for syntactically incorrect queries) is important because it allows participants to evaluate the efficacy of modifications they make to any query they might be reusing. Moreover, it provides a degree of realism for the study because, in practice, query formulation is almost universally conducted in an environment capable of executing proposed queries. The use of an experimental environment that integrates the execution and evaluation of queries also allows for the precise tracking of time that participants spent working on each part of the experimental task.

Table 1 Summary of Tests of Hypotheses

<table><tr><td rowspan="2">Hypothesis</td><td>Reuse</td><td>No Reuse</td><td rowspan="2">P value (f statistic)</td><td rowspan="2">Result</td></tr><tr><td>Mean (std. dev.)</td><td>Mean (std. dev.)</td></tr><tr><td>1. Reuse of queries results in more errors (percent correct)</td><td>29.29% (0.4713)</td><td>48.72% (0.5478)</td><td>0.0001 (27.7)</td><td>Supported</td></tr><tr><td>2. Reuse of queries results in less time to prepare queries (average minutes per query)</td><td>1.83 (2.13)</td><td>4.50 (3.43)</td><td>0.0001 (136.25)</td><td>Supported</td></tr><tr><td>3. Reuse of queries results in higher confidence in query correctness (Likert 1–5)</td><td>3.53 (0.88)</td><td>3.55 (1.03)</td><td>0.7399 (0.11)</td><td>Not supported*</td></tr><tr><td>4. Reuse of queries leads to poorer relationship between confidence and correctness (mean probability score, zero = perfect prediction)</td><td>0.383 (0.243)</td><td>0.342 (0.254)</td><td>0.0394 (4.26)</td><td>Supported</td></tr><tr><td></td><td>Familiar</td><td>Unfamiliar</td><td></td><td></td></tr><tr><td>5. Domain familiarity reduces adjustment bias (percentage of anchors correctly adjusted)</td><td>58.48% (0.2402)</td><td>58.01% (0.2027)</td><td>0.7924 (0.07)</td><td>Not supported*</td></tr><tr><td></td><td>Surface</td><td>Deep</td><td></td><td></td></tr><tr><td>6. Surface-structure anchors result in less adjustment bias than deep-structure anchors (percentage of anchors correctly adjusted)</td><td>85.29% (0.1357)</td><td>31.21% (0.3300)</td><td>0.0001 (21.6)</td><td>Supported</td></tr></table>

∗See post hoc analysis for clarification.

## Experimental Results

Overall, participants’ queries correctly answered the information requests about 40% of the time. Two participants wrote no correct queries and three correctly formulated all but one.

## Tests of Hypotheses

Before testing individual hypotheses, we conducted an omnibus test to protect against Type I error. The multivariate analysis of variance (MANOVA) test for significance for all hypotheses examined simultaneously had a p value of less than 0.0001 for both Wilk’s Lambda and Pillai’s Trace.<sup>8</sup> Accordingly, we accept an alpha level of 0.05 for testing individual hypotheses. The tests were conducted using repeated measures ANOVA. This statistical technique is appropriate because each participant formulated a simple and a complex query under four conditions: with and without a sample query available in each of the two domains. Performance on these eight queries is used to test the six hypotheses examined in this study (Table 1).<sup>9</sup>

Hypothesis 1 is supported. That is, when participants composed queries from scratch, they were more likely to produce the correct answer than when they modified an existing query—even though the query they modified contained most of the required elements of the information request. Average performance in our sample showed that participants generated the correct answer 49% of the time when no sample query was presented and only 29% of the time when a sample was available.

Hypothesis 2 is supported. When provided with a sample query, users formulated their solution queries more quickly than when no sample was available.

In our sample, participants took more than twice as long to produce their solution queries when no sample query was present.

Hypothesis 3 is not supported. Overall, we found no significant difference in the confidence expressed by participants when they had a sample query versus when they had no sample query. This hypothesis was posed without regard for query complexity. Our post hoc analysis shows a significant interaction between complexity and confidence, discussed in detail below.

Hypothesis 4 is supported. When users modified an existing query to meet new information requirements, they were less likely to correctly assess their own query’s accuracy.

Hypothesis 5 is not supported. Overall, we observed no difference in performance in adjusting from anchors under conditions of low domain familiarity than under conditions of higher domain familiarity. This is consistent with the work of Wright and Anderson (1989), which found that “situation familiarity” did not mitigate the anchoring and adjustment phenomenon. This hypothesis was proposed without regard to the kind of anchor (surface-structure versus deep-structure). As discussed below in our report of post hoc analysis, the type of anchor has major implications on the participants’ ability to adjust successfully under conditions of varying domain familiarity. For the finding of H5 to be meaningful, we must be confident that our manipulation of participants’ level of domain familiarity was successful. In an exit survey using a scale of 1 to 5, participants indicated their prior level of familiarity with the Gene Ontology domain to be low (mean 13, standard deviation 059) and their prior familiarity with the university domain to be moderate (mean 29, standard deviation = 119). This difference is significant at $p < 0 . 0 0 0 1$ . Although we expected participants (university students) to express more than moderate familiarity with the university domain, the fact that they had no prior experience with this particular database schema might explain the outcome.

Hypothesis 6 is supported. In our sample, participants correctly adjusted from 85% of surface-structure anchors and only 31% of deep-structure anchors. Although the hypothesis that surface-structure modifications can be made more readily than deep-structure modifications seems self-evident, the empirical results demonstrate it convincingly.

## Post Hoc Analysis

We conducted additional analyses both to clarify the findings for particular hypothesis tests and to answer ancillary questions that arose during hypothesis testing. Hypothesis 3 (confidence) was not supported. This hypothesis was expressed without regard for domain familiarity or query complexity, so we examined both for possible interaction with user confidence. We found no interaction with domain familiarity $( p = 0 . 6 8 2 6 )$ ; however, there was significant interaction with query complexity $( p = 0 . 0 0 0 2 )$ Recall that there were two prototypical queries (simple and complex), each answered four times (with and without a sample query in each domain). The simple query required one join, while the complex query required three joins. When considering query complexity in examining the effect of presence of a sample query on confidence (Table 2), we found that for complex queries, the presence of a sample query increased user confidence (as predicted in H3); however, for simple queries, the presence of a sample led to reduced confidence. This observed difference between confidence for simple and complex queries might be an anomaly of our experimental design. The complex query required three joins and the sample query showed three joins; however, while the simple query required only a single join, its sample showed two joins. Accordingly, when participants saw the sample, they might have perceived the query to be more complex than they would have thought without the sample, leading to lower confidence. Moreover, the presence of the additional join might have led participants to feel that they did not fully understand the information request, thereby reducing confidence. Because of this difference in the sample queries for the simple and complex information requests, caution should be used in interpreting the findings of this post hoc test.

Table 2 Decomposition of Hypothesis Test 3

<table><tr><td rowspan="2">Post hoc Test 1</td><td>Reuse</td><td>No reuse</td><td rowspan="2">P value(f statistic)</td><td rowspan="2">Result</td></tr><tr><td>Mean(std. dev.)</td><td>Mean(std. dev.)</td></tr><tr><td>Confidence expressed for correctness of simple queries</td><td>3.498(0.978)</td><td>3.770(1.097)</td><td>0.0012(10.65)</td><td>Confidence is higher without reuse</td></tr><tr><td>Confidence expressed for correctness of complex queries</td><td>3.598(1.048)</td><td>3.404(1.225)</td><td>0.0340(4.52)</td><td>Confidence is higher with reuse</td></tr></table>

Note. Hypothesis 3 predicted that reuse leads to higher confidence.

Hypothesis 4 (self-assessment of query accuracy) was supported. However, the result does not indicate if reuse led to more overconfidence or more underconfidence. Because overall confidence across the treatments was not significantly different (H3) and reuse led to lower accuracy (H1), it must be that reuse leads to more overconfidence. However, none of the tests of the hypotheses demonstrate this directly. Query formulation studies typically speak of participants as being overconfident; however, to our knowledge, it has never been measured directly. Fortunately, prior work in probability judgment provides an ideal measure. Judgment “bias” (Yates 1990, p. 61) for a participant is simply the average probability assessment (in our case, converted from a Likert expression of confidence) minus the average event outcome (1 or 0). A score of negative one indicates perfect underconfidence: for each query, the participant asserted very low confidence (0) and each query was correct (1). A score of positive one indicates perfect overconfidence: for each query, the participant asserted very high confidence (1) and each query was incorrect (0). A score of zero indicates that the participant was overconfident to the same degree that the participant was underconfident but provides no information about how extreme individual assessments of confidence were. Therefore, judgment bias should be considered in conjunction with the mean probability score to understand the degree to which a participant is under- or overconfident.

Table 3 presents the results of a post hoc test using judgment bias as a direct evaluation of overconfidence. This test directly indicates that reuse did lead to more overconfidence.

The lack of support for the idea that domain familiarity increases the ability to adjust (H5) led us to

Table 3 Test Showing Overconfidence Using Judgment Bias

<table><tr><td rowspan="2">Post hoc Test 2</td><td>Reuse</td><td>No reuse</td><td rowspan="2">P value (f statistic)</td><td rowspan="2">Result</td></tr><tr><td>Mean (std. dev.)</td><td>Mean (std. dev.)</td></tr><tr><td>Reuse of queries results in more overconfidence (judgment bias, positive = overconfidence)</td><td>0.437 (0.326)</td><td>0.307 (0.372)</td><td>0.0001 (22.14)</td><td>Supported</td></tr></table>

Table 4 Decomposition of Hypothesis Test 5

<table><tr><td rowspan="2">Post hoc Test 3</td><td>Familiar</td><td>Unfamiliar</td><td rowspan="2">P value (f statistic)</td><td rowspan="2">Result</td></tr><tr><td>Mean (std. dev.)</td><td>Mean (std. dev.)</td></tr><tr><td>Effect of domain familiarity on ability to adjust from surface-structure anchors</td><td>82.36% (0.164)</td><td>88.22% (0.156)</td><td>0.0001 (21.01)</td><td>Users adjust better for unfamiliar domain</td></tr><tr><td>Effect of domain familiarity on ability to adjust from deep-structure anchors</td><td>34.61% (0.399)</td><td>27.81% (0.343)</td><td>0.0224 (5.24)</td><td>Users adjust better for familiar domain</td></tr></table>

Note. Hypothesis 5 predicted that domain familiarity reduces adjustment bias.

question whether there might be a domain-driven, significant difference in the ability to adjust from either surface-structure anchors or deep-structure anchors. Accordingly, we partitioned the data to perform H5’s repeated measures ANOVA for surfacestructure anchors and deep-structure anchors independently. The results (Table 4) indicate that the reason no significance was found for H5 is that there is a counterbalancing effect. Users were better able to adjust from surface-structure anchors under conditions of low domain familiarity but were better able to adjust from deep-structure anchors under conditions of higher domain familiarity.<sup>10</sup> In our sample, participants correctly adjusted 88% of surface-structure anchors in the unfamiliar domain and 82% of surfacestructure anchors in the familiar domain. For deepstructure anchors, participants correctly adjusted 28% in the unfamiliar domain and 35% in the familiar domain. This finding might shed some light on the unexplained results for interaction between anchor type and situational familiarity reported by Wright and Anderson (1989). Of their three experiments, only one showed significant interaction between these terms; however, its significance was not consistent with their hypotheses. They conclude by suggesting that there is “no evidence that the powerful anchoring effect    is diminished by increased familiarity” (p. 77). Perhaps because our anchors (sample queries)

are more complex than theirs (preliminary judgment assessments), we observe that domain familiarity does hold a significant effect on the ability to adjust from different kinds of anchors. However, a full understanding of this interaction is elusive. It seems that in an unfamiliar domain, query writers might accept the validity of the joins in existing queries because the cognitive effort required to validate them is extremely high. Instead, they seem to focus on identifying surface-structure changes involving relatively simple mappings from the information request to values present in the sample query or to attribute names in the database schema. In a familiar domain, query writers appear to be more willing to spend time validating the joins and, consequently, are better able to adjust successfully from the deep-structure anchors. However, in attempting this validation, they seem to pay less attention to the surface structure. Clearly, more research is needed to provide a full understanding of this intriguing interaction.

Although the primary purpose of this study was not to examine the effect of domain familiarity on users’ performance at query formulation, we believe it is the first empirical study with treatments sufficient to evaluate this effect rigorously. Thus, we examined this effect using only those queries that were composed without the availability of a sample query.<sup>11</sup>

A priori, one would expect higher domain familiarity to lead to greater accuracy, higher confidence, and shorter time spent formulating queries. Moreover, prior research has shown that judgment is better for easier tasks (Fischhoff and Lichtenstein 1977), which suggests better accuracy at self-assessment under conditions of higher domain familiarity. We examine the effect of domain familiarity on each of the performance measures from Figure 1. The results are shown in Table 5.

The support for post hoc Tests 4 and 5 is as expected: when users are familiar with a domain, their queries are more accurate and they are more confident in their queries’ accuracy. It is interesting that we did not observe a difference in the ability of users’ confidence to predict their own queries’ correctness. Although we did not observe a difference in time spent, this might be an artifact of the experimental environment: under the test-like conditions of the experiment, it is possible that participants thought they should allocate a certain amount of time for each question.

Table 5 Examination of Domain Familiarity on Query Formulation Performance

<table><tr><td rowspan="2">Post hoc tests 4–7</td><td>Familiar</td><td>Unfamiliar</td><td rowspan="2">P value (f statistic)</td><td rowspan="2">Support</td></tr><tr><td>Mean (std. dev.)</td><td>Mean (std. dev.)</td></tr><tr><td>4. Domain familiarity leads to increased accuracy (percent correct)</td><td>43.47% (0.5224)</td><td>34.55% (0.5142)</td><td>0.0005 (1.6)</td><td>Yes</td></tr><tr><td>5. Domain familiarity leads to increased confidence (Likert 1–5)</td><td>3.65 (0.941)</td><td>3.42 (0.968)</td><td>0.0031 (8.81)</td><td>Yes</td></tr><tr><td>6. Domain familiarity leads to poorer relationship between confidence and correctness (mean probability score)</td><td>0.368 (0.256)</td><td>0.358 (0.243)</td><td>0.6247 (0.24)</td><td>No</td></tr><tr><td>7. Domain familiarity leads to decreased time (average minutes per query)</td><td>3.22 (3.304)</td><td>3.11 (3.000)</td><td>0.6532 (0.20)</td><td>No</td></tr></table>

The effectiveness of manipulating domain knowledge by using parallel database structures and identical queries in different domains hinges on the presumption that participants did not realize that the domain structures were identical. To examine this, we asked four questions in the exit survey, requiring participants to assert which domain schema had more tables, which had more relationships, and which had more attributes. We then asked how confident participants were that their assessment of the number of tables, relationships, and attributes was accurate. Only participants who answered that there were the same number of tables, relationships, and attributes in both domains and that they were highly confident in their assessment could have determined that the domains were structurally identical. Of the 157 participants, only one met these criteria. With the permission of that student’s professor, we contacted him to determine whether he realized the parallel nature of the domains. He said that he had not considered that possibility. This indicates that participants did not realize the parallel nature of the domains.

Table 6 Frequency Table for Number of Queries Copied

<table><tr><td>Queries copied</td><td>Frequency</td><td>Percent</td><td>Cumulative frequency</td><td>Cumulative percent</td></tr><tr><td>4</td><td>94</td><td>59.9</td><td>94</td><td>59.9</td></tr><tr><td>3</td><td>14</td><td>8.9</td><td>108</td><td>68.8</td></tr><tr><td>2</td><td>18</td><td>11.5</td><td>126</td><td>80.3</td></tr><tr><td>1</td><td>6</td><td>3.8</td><td>132</td><td>84.1</td></tr><tr><td>0</td><td>25</td><td>15.9</td><td>157</td><td>100</td></tr></table>

Although we note that the tendency to rely on the anchor is high, it is by no means universal. Our experimental instrument tracked when a user copied a sample query for modification. Table 6 provides the frequency for each level of query copying exhibited by participants. This table shows that 94 participants (60%) copied all four sample queries with which they were presented. This measure does not necessarily reflect the extent to which participants relied on sample queries in the formulation of their own queries; rather, it serves as a lower bound for that measure. It is possible that not all participants realized that they could copy the sample queries, or they realized it only partway through the experiment. Of course, it was possible for participants to anchor on a sample query without copying if they referenced it in any manner.

Seeing that a substantial number of participants opted not to copy the sample query for several questions, we performed a regression analysis to determine if any of the variables collected in the exit survey predicted the propensity to copy the sample. We tested the number of courses that participants had taken that required SQL query formulation, the number of years’ experience they had with query formulation, their self-reported comfort level with SQL, their self-reported GPA, and their self-reported GPA for database management courses. None were significant predictors. A logistic regression was used to test if sample query complexity (measured by the number of tables used in the sample query) had a significant influence on a participant’s choice to copy the sample on a query-by-query basis. No significant predictive power was observed.

## Discussion

This study demonstrates that the adaptive reuse of queries is affected by the anchoring and adjustment phenomenon and that the effect is potentially harmful. Reuse of queries that must be modified to meet the requirements of a related, but different, information request can increase the likelihood of error relative to writing queries from scratch. Despite having access to a functioning query requiring only slight modification to address a new information request, it is possible to achieve higher accuracy by writing a query without reference to an existing one.

This study also shows that, not only can reusing an anchor query lead to higher error rates because of the effect of the adjustment bias, but also that reusing queries leads to unwarranted confidence in the correctness of queries. Although reused anchor queries are more likely to have errors because of the adjustment bias, query writers are not correspondingly less confident in their correctness. This is troubling because overconfidence increases the likelihood that decisions may be made based on incorrect query results. Consequently, query reuse has the potential to lead to undesirable outcomes for an organization. This result has strong implications for the appropriateness of strategies that involve adapting existing queries to satisfy new requirements. It shows that adaptive reuse cannot be unquestioningly accepted as a strategy for supporting effective query writing.

Because time taken to compose queries is a standard measure of query writing performance, we have included this dependent variable in our study. However, its value in understanding the effects of adapting queries for reuse needs to be tempered. The value of saving a few minutes of a decision maker’s time can be inconsequential when compared to the potential costs of making decisions on erroneous data. Other things being equal, reduced time would be a desirable benefit; however, in the current study, its value as a performance measure is dubious.

The implications of these findings extend to the teaching of SQL. In our experience, students normally attempt to solve information requests by adapting existing queries. This is particularly true when students learn a new concept, in which case queries that address similar tasks in different domains may be modified for the current task.

The study also demonstrates that the adjustment bias is stronger for deep-structure anchors than for surface-structure anchors. That is, participants in our study were less able to adjust from anchors involving joins than from anchors involving projections, restriction conditions, or functions. Thus, if it is known in advance that the query to be reused involves, for example, changing a parameter value in a selection condition, the risk associated with reuse may be less than if the query is known to require a change in a join condition or requires unknown changes. Moreover, the risk associated with queries requiring multiple changes might be high, as people may not look beyond surface-structure changes to other parts of a query that may need to be modified.

In addition to demonstrating that anchoring and adjustment is robust when applied to database querying, this research also helps build a deeper understanding of the phenomenon. As noted above, when applied to a complex problem-solving task (as contrasted with simple estimation tasks used in earlier studies of anchoring and adjustment), a distinction can be made between surface-structure anchors and deep-structure anchors. This research shows that adjustment from surface-structure anchors tends to be more successful than adjustment from deepstructure anchors. To our knowledge, this has not been addressed in prior research on anchoring and adjustment. More work is needed to examine this issue in greater depth. For example, in the area of query reuse, the problems encountered in adjusting join expressions may arise because of the difficulty in comparing the textual representation of an SQL join to the graphical representation of a schema diagram. This problem might be mitigated by using query environments that show joins graphically.

A further contribution to our understanding of anchoring and adjustment comes from examining domain familiarity as a factor that interacts with the type of anchor. In particular, participants were better able to adjust from deep-structure anchors when domain familiarity was higher than when domain familiarity was lower. In contrast, they were better able to adjust from surface-structure anchors when domain familiarity was lower than when it was higher. Thus, we have shown that the notion of an anchor is more complex than previously thought. Another important contribution is the introduction of a within-subjects technique to manipulate domain familiarity in an experimental setting without requiring participants to learn about a domain.

To further improve our understanding of the role of anchoring and adjustment in adaptive query reuse, more research is needed. First, although prior research on anchoring and adjustment indicates that the phenomenon is robust across a range of factors, it is possible that expertise and experience in formulating SQL queries will moderate the adjustment bias. Our use of students as participants might limit the degree to which our results can be applied to working professionals. Therefore, this study should be replicated using participants with substantial experience in SQL query formulation.

Second, the reuse opportunities in this study do not reflect the range of real-world query reuse possibilities. Participants were offered only two queries for possible reuse for each information request, whereas in practice they might have many potentially reusable queries from which to choose. In a related vein, it is unclear whether the results of this study apply to adaptive reuse of a query writer’s own queries. Both experienced query writers and those reusing queries written themselves might be more motivated to make sufficient adjustments when reusing queries than were the participants in this study, a possibility consistent with Epley and Gilovich’s (2006) findings on the impact of motivation on adjustment from selfgenerated anchors.

Third, this study has shown that query writers do not always adjust adequately from surface-structure anchors, but it lacks the power to make any claim about the relative performance of writing queries from scratch or the adaptive reuse of queries that require only surface-structure modification. This means that query reuse requiring only surface-structure modification, such as changing cutoff dates in a query used to produce a periodic report, may not be substantially affected by the adjustment bias. In particular, research is needed to determine the extent to which warnings are effective in helping domain experts adjust from surface-structure errors. In addition, a more precise characterization of surfaceand deep-structure anchors is needed. Similarly, when a query to be adapted is very close to meeting an information request (e.g., only a single change is required), the ability of query writers to adequately make adjustments might be significantly higher than when several modifications are needed.

Fourth, our research did not examine real-world contexts in which a person may be required to search a query repository to locate potentially reusable queries. In particular, the process of searching for and determining whether available queries are “close” to the current information request is, in itself, a judgment task. This process might mitigate the adjustment bias as observed in this research. Further work is needed to examine how query writers behave when given access to a query repository. Among the questions that can be examined is the role played by a mechanism (manual or automated) for locating queries that are similar to the requirements of a new information request.

Fifth, the manipulation of domain familiarity, although effective, was not as strong as it might have been. Although students were quite unfamiliar with the gene ontology domain (1.3 on a 5-point scale), they can best be described as moderately familiar with the university domain (2.9 on a 5-point scale). More work is needed to study anchoring and adjustment in situations of high domain familiarity—especially given that ad hoc query writers often have high domain familiarity.

Finally, we believe that the most problematic aspect of adaptive query reuse involves the tendency of users to attempt strict difference reduction techniques when modifying existing queries. In so doing, a query writer must compare a natural-language information request to an existing SQL statement. The two are very dissimilar, making the use of difference reduction techniques to produce the new query very challenging. Consider how the problem would change if the natural-language information request and the syntax-neutral data statement were recorded with the final query, capturing the output of each step in Ogden’s (1985) query-writing process. This would allow a user to examine how closely an existing query comes to meeting the current information request without the need of reverse translation. Moreover, if the output of the first two steps of the querywriting process is stored with the ultimate query, an organization could easily implement audits (or peer reviews) of query-writing activities. Every executable query answers some question; by recording the question the query was intended to answer (perhaps as a comment in the SQL code itself), it is possible to determine if it answers the right question. By reviewing individuals’ ability to correctly map from the information request to the formal query, organizations could provide appropriate training to individual query writers.

## Conclusions

This study has extended our knowledge of the role of anchoring and adjustment in adaptive artifact reuse and added specific insights with respect to query formulation. Although participants completed query formulation tasks more quickly when modifying a query that satisfied a similar information request, this was accompanied by decreased accuracy, but not decreased confidence. A key practical implication is that query reuse can be harmful and should be undertaken with caution. This is particularly relevant given the recent emergence of commercial products that support query repositories and aid people in searching for queries to reuse.

This study also extends our understanding of anchoring and adjustment by considering its effects under differing levels of domain familiarity and by examining the differences between surface-structure and deep-structure anchors. In general, users are better able to adjust from surface-structure anchors than from deep-structure anchors. However, domain familiarity affects the ability to adjust from different kinds of anchors. Most psychological research on anchoring and adjustment has adopted a simpler view of the phenomenon. This research shows that, in the information systems domain, anchoring and adjustment is more complex and is affected by user characteristics such as domain familiarity, and by task characteristics such as the nature of the anchor.

Is adaptive reuse of existing database queries potentially harmful? This study indicates that the answer is “yes.” In general, query writers can produce more accurate results for information requests by writing queries from scratch than by reusing existing queries that answer related information requests. How harmful reuse is can depend on a number of factors. In particular, query writers are less able to correctly identify required changes to join conditions than to changes in restriction conditions or other surface-structure aspects of a query. In addition, participants in this study adjusted more accurately from deep-structure anchors when they had higher domain familiarity than when they had lower domain familiarity, but adjusted more accurately from surfacestructure anchors when they had lower domain familiarity than when they had high domain familiarity. Given these findings, it is clear that adaptive query reuse cannot be unquestioningly accepted as a strategy to improve query accuracy.

```sql
select distinct name, title from student st join section s on st.id = s.grader_id join section_professor c on c.section_id = s.id join professor p on p.id = c.professor_id where last_name = "Bennett" and city = "New York"
```

```txt
6. List the work experience (company and job title) of students of who have also been employed by professors whose title is currently “Assistant” in the “University College.” Remove any duplicates from the list.
```

## Appendix A. University Domain: Questions, Samples (Italic), and Answers (Bold)

```sql
1. How many rooms are in building "Gist Hall"?
select count(distinct room_abbr) from room where
building = "University Annex"
select count(*) from room where building = "Gist Hall"
2. Which courses (id and name) have as overseeing
professor "Young, Todd F."?
select course_name select course_name
from course c from course c, professor p
join professor p on p.id = where p.id =
c.overseeing_professor_id c.overseeing_professor_id
where name = "Avina, and name = "Avina,
Kathleen" Kathleen"
select course_name, c.id from course c, professor p
where p.id = c.overseeing_professor_id and name =
"Young, Todd F."
3. How many times have professors employed students
from Arizona (state = "AZ").
select max(wage) select max(wage)
from student s from student s, employment e,
join employment e on work_experience w
s.id = e.student_id where s.id = e.student_id
join work_experience w and w.student_id = s.id
on w.student_id = s.id and s.state = "AK"
where s.state = "AK"
select count(student_id) from student s join
employment e on s.id = e.student_id where
s.state = "AZ"
4. How many sponsors are the primary sponsors for
courses that can be taken for credits ranging from 1 to 3
(credit_range = "1-3")?
select max(sponsor_name) select max(sponsor_name)
from course c from course c, sponsor s,
join sponsor s on cross_list l
c.primary_sponsor_id = where c.primary_sponsor_id =
s.id s.id and l.course_id = c.id
join cross_list l on and credit_range = "3"
l.course_id = c.id
where credit_range = "3"
select count(distinct s.id) from course c join sponsor s
on c.primary_sponsor_id = s.id where credit_range =
"1-3"
```

## 5. List the name and title of professors who have taught sections which had a grader with the last name of “Bennett” from the city of “New York.” Remove any duplicates from the list.

```sql
select distinct name    select distinct name
from student st    from student st, section s,
join section s on st.id =    course c, professor p
    s.grader_id    where st.id = s.grader_id
join course c on c.id =    and c.id = s.course_id
    s.course_id    and p.id =
join professor p on p.id =    c.overseeing_professor_id
    c.overseeing_professor_id    and last_name = "Barnett"
where last_name = "Barnett"    and city = "New York"
and city = "New York"
```

$$
v. s t u d e n t \_ i d = s. i d
$$

```sql
select distinct company, job_title from work_experience
w join student s on s.id = w.student_id join
employment e on e.student_id = s.id join professor p
on p.id = e.professor_id where p.title = "Assistant"
and college = "University College"
```

```txt
6. List the speciesdbname and product_count for terms with definitions cross referenced in the "GOA" database (xref_dbname = "GOA") with nonlisted key types (xref_keytype = "none listed"). Remove any duplicates from the list.
select distinct speciesdbname select distinct speciesdbname
from dbxref d join from dbxref d, term_dbxref td,
term_dbxref td on term t, gene_product_count g
d.id = td.dbxref_id where d.id = td.dbxref_id
join term t on t.id = and t.id = td.term_id
td.term_id and g.term_id = t.id
join gene_product_count g and xref_dbname =
on g.term_id = t.id "PAMGO" and
where xref_dbname = xref_keytype = "none listed"
"PAMGO" and
xref_keytype = "none listed"
select speciesdbname, product_count from dbxref d join term_definition td on d.id = td.dbxref_id join term t on t.id = td.term_id join gene_product_count g on g.term_id = t.id where xref_dbname = "GOA" and xref_keytype = "none listed"
```

## Appendix B. Gene Ontology Domain: Questions, Samples (Italic), and Answers (Bold)

```txt
1. How many species are there of the genus "Influenza"? select count(*) from species where genus = "Rana" select count(*) from species where genus = "Influenza"   
2. Which gene products (id and full_name) are referenced by dbxref "GeneDB_Lmajor"? select full_name select full_name from dbxref from dbxref, gene_product join gene_product on where dbxref_id = dbxref.id dbxref_id = dbxref.id and xref_dbname = where xref_dbname = "TIGR_Tba1" "TIGR_Tba1"   
select gene_product.id, full_name from dbxref join gene_product on dbxref_id = dbxref.id where xref_dbname = "GeneDB_Lmajor"   
3. How many definitions are there for obsolete terms (is_obsolete = 1)? select max(term_definition) select max(term_definition) from term t from term t, term_definition d, join term_definition d on gene_product_count g t.id = d.term_id where t.id = d.term_id join gene_product_count g and g.term_id = t.id on g.term_id = t.id and t.is_obsolete = 0 where t.is_obsolete = 0   
select count(term_id) from term t join term_definition d on t.id = d.term_id where t.is_obsolete = 1   
4. How many species are the primary species for gene products with a symbol of ADH2 (symbol = "ADH2")? select max(common_name) select max(common_name) from gene_product g from gene_product g, species s, join species s on gene_product_synonym p gene_product_synonym p g.primary_species_id = where g.primary_species_id = gprimary_species_id = g primary_species_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_iid and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id and p.gene_product_id = s.id
```

```sql
select distinct d.xref_dbname    select distinct d.xref_dbname
from association a    from association a,
join gene_product g on    gene_product g, dbxref d,
    g.id = a.gene_product_id    term t
join dbxref d on d.id =    where g.id =
    g.dbxref_id    a.gene_product_id
join term t on t.id =    and d.id = g.dbxref_id
    a.term_id    and t.id = a.term_id
where t.name = "ethanol    and t.name = "ethanol
    fermentation" and    fermentation" and
term_type =    term_type =
    "biological_process"    "biological_process"
```

```txt
select d.xref_key, d.xref_dbname from association a join evidence e on e.association_id =a.id join dbxref d on d.id =e.dbxref_id join term t on t.id =a.term_id where t.name = "ethanol metabolism" and term_type = "biological_process"
```

Appendix C. Gene Ontology Domain Database Diagram  
![](/api/attachments/RXHD67E9/fulltext/images/b0e42c7616f8fffc2f726f4205f0690f4fd4a61102bb6c2507d01eab5b106bef.jpg)

Appendix D. University Domain Database Diagram  
![](/api/attachments/RXHD67E9/fulltext/images/fa713a7c8069de5355154d5f10b54d86b184408402dd08906fd1045ddbb8e8e6.jpg)

## References

Allen, G., S. March. 2006. The effects of state-based and event-based data representations on user performance in query formulation tasks. MIS Quart. 30(2) 269–290.

Anderson, J. R. 1993. Problem solving and learning. Amer. Psychologist 48(1) 35–44.

Batra, D., J. Hoffer, R. Bostrom. 1990. A comparison of user performance between the relational and the extended entity relationship models in the discovery phase of database design. Comm. ACM 33(2) 126–139.

Borthick, A., P. Bowen, D. Jones, M. Tse. 2001. The effects of information request ambiguity and construct incongruence on query development. Decision Support Systems 32 33–56.

Bowen, P., R. O’Farrell, F. Rohde. 2006. Analysis of competing data structures: Does ontological clarity produce better end user query performance? J. Assoc. Inform. Systems 7(8) 514–544.

Burton-Jones, A., R. Weber. 1999. Understanding relationships with attributes in entity-relationship diagrams. Proc. Twentieth Internat. Conf. Inform. Systems, 214–228.

Chan, C., K. K. Wei, K. Siau. 1993. User-database interface: The effect of abstraction levels on query performance. MIS Quart. 17(4) 441–464.

Cox, B. 1990. Planning the software industrial revolution. IEEE Software 7(6) 25–33.

Dettinger, R., R. Stevens, J. Tenner. 2004. SQL query construction using durable query components. United States Patent Application 20040068489. Retrieved February 2, 2008, http://www.uspto.gov.

Dettinger, R., J. Glowacki, D. Kolz, P. Rao, M. Sperber, S. Wenzel. 2007. Query reuse through recommend parameter flexibility. United States Patent Application 20070276825. Retrieved February 2, 2008, http://www.uspto.gov.

Edlund, S., M. Emens, R. Kraft, P. Yim. 2002. Labeling and describing search queries for reuse. United States Patent 6,484,162. Retrieved February 2, 2008, http://www.uspto.gov.

Epley, N., T. Gilovich. 2006. The anchoring-and-adjustment heuristic: Why adjustments are insufficient. Psych. Sci. 17(4) 311–318.

Fagan, M., S. Corley. 1998. CBR for the reuse of corporate SQL knowledge. Eur. Workshop on Case Based Reasoning EWCBR’98, Dublin, Ireland, Lecture Notes in Artificial Intelligence, Vol. 1488, 382–392.

Fichman, R., C. F. Kemerer. 1997. Object technology and reuse: Lessons from early adopters. IEEE Comput. 30(10) 47–59.

Fischhoff, B., S. Lichtenstein. 1977. Do those who know more also know more about how much they know? The calibration of probability judgments. Organ. Behav. Human Performance 20(2) 159–183.

Frakes, W. B., G. Succi. 2001. An industrial study of reuse, quality and productivity. J. Systems Software 57(2) 99–106.

Frakes, W. B., C. Terry. 1996. Software reuse: Metrics and models. ACM Comput. Surveys 28(2) 415–435.

George, J. F., K. Duffy, M. Ahuja. 2000. Countering the anchoring and adjustment bias with decision support systems. Decision Support Systems 29 195–206.

Greenwald, A. G. 1976. Within-subjects designs: To use or not to use. Psych. Bull. 83(2) 314–320.

Griss, M. 1993. Software reuse: From library to factory. IBM Systems J. 32

Irwin, G. 2002. The role of similarity in the reuse of object-oriented analysis models. J. Management Inform. Systems 19(2) 221–250.

Johnson, E. J., J. W. Payne. 1985. Effort and accuracy in choice. Management Sci. 31(4) 395–414.

Khatri, V., I. Vessey, V. Ramesh, P. Clay, S. Park. 2006. Understanding conceptual schemas: Exploring the role of application and IS domain knowledge. Inform. Systems Res. 17(3) 81–99.

Kim, Y., E. A. Stohr. 1998. Software reuse: Survey and research directions. J. Management Inform. Systems 14(4) 113–147.

Leitheiser, R., S. March. 1996. The influence of database structure representation on database system learning and use. J. Management Inform. Systems 12(4) 187–213.

Li, G., L. Zhang, B. Xie, W. Shao. 2006. Shortening retrieval sequences in browsing-based component retrieval using information entropy. J. Systems and Software 79(2) 216–230.

Lim, W. 1994. Effects of reuse on quality, productivity, and economics. IEEE Software 11(5) 23–30.

Mili, H., F. Mili, A. Mili. 1995. Reusing software: Issues and research directions. IEEE Trans. Software Engrg. 21(6) 528–561.

Morisio, M., M. Erzan, C. Tully. 2002. Success and failure factors in software reuse. IEEE Trans. Software Engrg. 28(4) 340–357.

Ogden, W. C. 1985. Implications of a cognitive model of database query: Comparison of a natural language, a formal language, and direct manipulation interface. ACM SIGCHI Bull. 18(2) 51–54.

Oussalah, C., A. Seriai. 2000a. How to reuse former queries to facilitate the formulation of new ones. Proc. Internat. Database Engrg. Appl. Sympos. Ideas’00, Yokohama, Japan, 92–100.

Oussalah, C., A. Seriai. 2000b. A reuse-based object-oriented framework towards easy formulation of complex queries. Proc. Internat. Conf. Conceptual Modeling (ER2000), Springer, Berlin, 470–483.

Parsons, J., L. Cole. 2005. What do the pictures mean? Guidelines for experimental evaluation of representation fidelity in diagrammatical conceptual modeling techniques. Data Knowledge Engrg. 55(3) 327–342.

Parsons, J., C. Saunders. 2004. Cognitive heuristics in software engi neering: Applying and extending anchoring and adjustment to artifact reuse. IEEE Trans. Software Engrg. 30(12) 873–888.

Pittman, M. 1993. Lessons learned in managing object-oriented development. IEEE Software 10(1) 43–53.

Plous, S. 1993. The Psychology of Judgment and Decision Making. McGraw-Hill, New York.

Purao, S., V. Storey, T. Han. 2003. Improving pattern reuse in conceptual design: Augmenting automated processes with super vised learning. Inform. Systems Res. 14(3) 269–290.

Robinson, M., J. Johnson, F. Herndon. 1997. Reaction time and assessments of cognitive effort as predictors of eyewitness memory accuracy and confidence. J. Appl. Psych. 82(3) 416–425.

Speier, C., M. Morris. 2003. The influence of query interface design on decision-making performance. MIS Quart. 27(3) 397–423.

Stacy, W., J. MacMillan. 1995. Cognitive bias in software engineering. Comm. ACM 38(6) 57–69.

Succi, G., L. Benedicenti, T. Vernazza. 2001. Analysis of the effects of software reuse on customer satisfaction in an RPG environ ment. IEEE Trans. Software Engrg. 27(5) 473–479.

Tversky, A., D. Kahneman. 1974. Judgment under uncertainty: Heuristics and biases. Science 185(4157) 1124–1131.

Wright, W. F., U. Anderson. 1989. Effects of situation familiarity and financial incentives on use of the anchoring and adjustment heuristic for probability assessment. Organ. Behav. Human Decision Processes 44(1) 68–82.

Yates, J. 1990. Judgment and Decision Making. Prentice-Hall, Englewood Cliffs, NJ.
