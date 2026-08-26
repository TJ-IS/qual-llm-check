---
otero_id: 25576
otero_key: "F72WQR79"
title: "Skipping class: improving human-driven data exploration and querying through instances"
authors: "Arash Saghafi; Yair Wand; Jeffrey Parsons"
year: "2022"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1869507"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Skipping class: improving human-driven data exploration and querying through instances

Arash Saghafi , Yair Wand & Jeffrey Parsons

To cite this article: Arash Saghafi , Yair Wand & Jeffrey Parsons (2021): Skipping class: improving human-driven data exploration and querying through instances, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1869507

To link to this article: https://doi.org/10.1080/0960085X.2020.1869507

CO © 2021 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/F72WQR79/fulltext/images/c85cc6a62b62fb9648c5318176f2a5592ba1ecd1f0a38771f4e585ab797bb5bf.jpg)

Published online: 29 Jan 2021.

![](/api/attachments/F72WQR79/fulltext/images/160eb2e2c70d0c26c3968a58da68bd0a0ce9fb00bbb143673e2c4df713108f56.jpg)

Submit your article to this journal

![](/api/attachments/F72WQR79/fulltext/images/da67eb5475f6cb0ba9fd5c93ab5a6a04b64a3f18dd0e0cf3b05bf5ab0de018bb.jpg)

Article views: 440

![](/api/attachments/F72WQR79/fulltext/images/08e869a3c0732767ee72f1ac69129905c2ebd5c0ecde43e7c964c5e94d40a5b1.jpg)

View related articles

![](/api/attachments/F72WQR79/fulltext/images/c999cf09b00816b7ab18a65d641a8f7cec350d6d08a26f3a537030adb3137a86.jpg)

View Crossmark data

∂ OPEN ACCESS

Check for updates

# Skipping class: improving human-driven data exploration and querying through instances

Arash Saghafi <sup>a</sup>, Yair Wand<sup>b</sup> and Jefrey Parsons<sup>c</sup>

<sup>a</sup>Tilburg School of Economics and Management, Tilburg University, Tilburg, Netherlands; <sup>b</sup>Sauder School of Business, The University of British Columbia, Vancouver, Canada; <sup>c</sup>Faculty of Business Administration, Memorial University of Newfoundland, St. John’s, Newfoundland and Labrador, Canada

## ABSTRACT

With the growing focus on business analytics and data-driven decision-making, there is a greater need for humans to interact efectively with data. We propose that presenting data to human users in terms of instances and attributes provides a more flexible and usable structure for querying, exploring, and analysing data. Compared to a traditional representation, an instance-based representation does not impose any predefined classification schema over the data when it is presented to users. This paper examines the potential utility of instancebased data through two laboratory experiments – the first focusing on exploration of data for pattern discovery (open-ended tasks) and the second on retrieval of information (closed-ended tasks). In both cases, participants were able to achieve better results in tasks using instancebased data than using class-based representations. Given the growing need for self-service analytics, as well as using information for purposes not anticipated when it was collected, we show that instance-based representations can be an efective way to satisfy the emerging needs of information users.

ARTICLE HISTORY Received 2 January 2020 Accepted 21 December 2020

KEYWORDS Database Design; nonclassified data; instancebased data model; attributes; classification; open information; database queries; pattern detection; knowledge discovery; human-in-the-loop data analytics

## 1. Introduction

Companies are increasing their eforts to use data analytics to make better decisions and improve “competitiveness, eficiency, insight, and profitability” (Zikopoulos & Eaton, 2011, p. xviii). Current approaches to data analytics rely heavily on mathematical models and computerbased algorithms (Zikopoulos & Eaton, 2011). However, these cannot eliminate the need for human users in exploring domains where the data requirements and analysis tasks are not well defined (Munzner, 2014). Even in machine learning, keeping human users in the loop can lead to superior solutions (Cassidy et al., 2018), particularly at the decision-making level (Gillies et al., 2016). In addition, the ubiquity of data in organisational (as well as personal) decisions has given rise to the multidisciplinary field of Human-Data Interaction (HDI), which puts humans at the centre of data flows in business systems (Mortier et al., 2020). Hence, human involvement in making sense of data is of paramount importance (Thomas & Cook, 2006). The growing trend of “self-service” Business Intelligence (BI) phenomenon, defined as enabling business users “to become more selfreliant and less dependent on the IT organization” (Imhof & White, 2011, p. 5) by making tools easier to use, is a manifestation of HDI.

There is also a shortage of talent for data science and analyst jobs (Miller & Hughes, 2017), which could inhibit realising the full potential of big data, especially considering that skills can only be developed with significant time and efort (Miller & Hughes, 2017). Self-service analytics for business users is one step in enabling firms to cope with the talent shortage.

To study business users’ ability to perform selfservice BI and keeping with the theme of human-inloop analytics, this research focuses on supporting content consumers – users who are (to some extent) familiar with the domain represented in a data source, but do not necessarily have knowledge of databases and data models – in data exploration and analysis.<sup>1</sup> These users can retrieve and explore information from an information system for use, but have no control over the design of the database (i.e., they are not database administrators). Content consumers can assume any of a wide variety of roles, such as business analysts, students using data for a course project, or journalists searching data to support their stories. Such users are typically not professional database designers or data scientists.

Evidence of the important role of content consumers comes from a survey on the users of Open Government Data. Graves and Hendler (2013) studied 257 participants from a wide range of occupations (including government workers, journalists, scientists, and engineers), where 75% of participants had masters or doctoral degrees. Among this group, 42% identified themselves as non-experts in technology. We examine the ability of such content consumers to engage efectively, in information exploration (pattern discovery) and data querying tasks.

We propose to evaluate content consumers’ ability to use instance-based representations of data. By instancebased representation, we mean that data are modelled or represented visually as individuals bundled with their attributes and are not pre-classified into tables (Parsons & Wand, 2000). Such instance-based representations have been argued to be more amenable to using data in ways other than those anticipated when the data were collected (Lukyanenko, Parsons, Samuel et al., 2019a). Using an instance-based representation, classification can be done on demand, depending on the purpose for which the data are being used. A baseline for comparison is the class-based data model, in which data are modelled or represented in terms of predetermined classes and instances are viewed only through the lens of classes. The class-based approach is the predominant data modelling approach and is exemplified by the Entity-Relationship and relational data models (Elmasri & Navathe, 2011). We argue that users who have access to instance-based data will make sense of the data through their own mental models and will be more efective in reasoning about the data. Note that our conceptualisation of “class” is rooted in Bunge’s ontology and is a common abstraction mechanism in information modelling. We define a class as a set of things that possess common properties (Wand & Weber, 1993).

Our work also addresses Rai’s (2016) call for solutions that “address the tension between the stability of preexisting categorisation schemas that may have worked well for historical data and the need to challenge and revise ontological assumptions underlying these schemas when anomalies are detected in new observational data” (p. vi). Rai proposes to “refine categorization schemas based on anomalies so to avoid over-fitting data to preexisting categories” (p. vii). We propose that instancebased (or schema later) data representations can lead to better human understanding of data semantics (i.e., users perspective). We emphasise that the focus of our study is on the representation of data as used by a human, regardless of how it is stored in the database management system<sup>2</sup> (whether relational or instance-based).

To best of our knowledge, this work is the first empirical study of the usability and usefulness (by humans) of instance-based data representations in comparison to relational or class-based representations. Prior research has focused on issues related to storage of non-classified data (e.g., Vicknair et al., 2010; Zhu et al., 2017), but not on representation and usability by content consumers.

We begin by describing the theoretical foundations of our study in terms of content consumers’ cognitive processes of interacting with instance-based data. We then present our proposed approach for representing such data. We continue by describing the design of two independent experiments – with diferent sample pools – comparing an instance-based data representation with a traditional class-based (relational) representation. The first experiment focuses on content consumers’ ability to explore a large dataset and identify patterns in it. The second experiment studies the correctness of querying steps in closed-ended tasks. The two experiments show that instance-based data can lead to better performance and understanding of phenomena. We conclude by discussing the implications of our work as well as its limitations, and opportunities for future research.

## 2. Theoretical background

We predict that content consumers exploring data represented as instance-based or non-classified entities (based on the attributes of these entities) will be able to construct their own mental frameworks of concepts or schemas con gruent with their prior knowledge. As a result, they will perform better than those provided with data organised into predefined classes (for specific applications). Our work is informed by the categorisation literature, as well as research on the impact of decision-making heuristics on human decisions (Browne & Parsons, 2012).

From a categorisation perspective, our predictions are rooted in Cognitive Schema Theory (CST) (Derry, 1996). CST posits that humans form mental models to understand the phenomena they observe. According to CST, each encountered concept is modelled as an object (or a building block) in working memory. When humans solve problems, they connect, reorganise, and map these active memory objects onto components of real-world phenomena based on their previously learned schemas (i.e., prior knowledge). We argue that instance-based representations give more freedom to users to form their own mental models, and hence process information and reason about the domain more efectively (i.e., reach a desired endpoint or goal successfully). Regardless of the number of instances or properties in a data source, users can focus on the ones aligned with their own mental sch emas. In contrast, when provided with pre-classified data, a user needs to understand a classification scheme typically created by database designers. Such databases are based on the designers’ prior knowledge and organisati onal requirements, which might not be congruent with the content consumer’s mental schema of prior knowledge (Parsons, 2002). We recognise that information syst ems are typically designed with input from end users. However, in general, no single design can incorporate all the views and needs of diferent content consumers.

From human decision-making, we utilise Tversky and Kahneman (1974) work on heuristics in decision-making and judgement. Heuristics are “cognitive shortcuts, or rules of thumb, that allow people to act and decide” (Browne & Parsons, 2012, p. 1006). Specifically, we view classification schemes as heuristics that help users understand a specific view of data and serve as a starting point in the process of solving a problem. These starting points serve as anchors that can lead to cognitive biases (Tversky & Kahneman, 1974). Parsons and Saunders (2004) and Allen and Parsons (2010) examined the role of anchoring in reuse of existing code and SQL queries, respectively. They found a negative impact of anchoring, manifested in misalignment between the artefact (conceptual model, code, or SQL query) and stated requirements, and in propagation of errors present in the reused artefact. Likewise, we expect that when presented with instancebased data, subjects’ interactions will not be anchored to a specific view (classification scheme) of the data. In contr ast, when provided with class-based schemas that are generally created by database designers, subjects’ exploration of information will be more restricted and, therefore, potentially biased, as they anchor to the given classification scheme. Hence, performance of users of an instancebased representation is expected to be less restricted (or less biased) than users of a class-based representation, such as a relational database. By reducing anchoring bias es, we mitigate the potential negative impact of a classbased representation, and thus predict better performance by users of the instance-based data representation.

Classification is a fundamental cognitive process in wh ich humans comprehend phenomena by grouping them based on similarity (Lakof, 1987). Classes reflect a repeat ing pattern of attributes and indicate that relationships might exist between the attributes (Parsons & Wand, 2008a). Thus, classes represent similarity of phenomena and make it possible to infer additional attributes of inst ances (Parsons & Wand, 2008a). By enabling inferences, classes provide utility (Parsons & Wand, 2000, p. 238). From this perspective, classification structure is not inher ent in the real world but is a human activity that provides useful abstractions of similarities among things that support reasoning and action. Consequently, rather than rely ing on a database designer to construct the “correct” classi fication structure, content consumers should have the option to create their required classes on demand, as there might be many ways of classifying a given set of inst ances (Parsons & Wand, 2000).

Using instance-based data, users can focus on the ins tances or attributes that match their needs. In other wor ds, despite a very large number of instances in the database, users do not need to view or understand all the ins tances and their attributes in order to perform tasks. When users define their own classes, they can apply these views as “lenses” over a pool of instances to access information relevant to their needs. Moreover, unanticipated applications can be supported by adjusting these lenses to incorporate newly relevant information more easily. Such a situation imposes a considerable challenge in a class-based (e.g., relational database) setting, where an emerging need may entail restructuring the data schema to present data in a way that supports the new application. However, when data are stored as unclassified instances, new views can be defined as required without a need for data restructuring.

## 3. Modelling instance-based data

Our conceptualisation of instance-based data is compliant with NoSQL standards where there is no fixed structure in representation of data; in other words, a nonrelational database (Hills, 2016). Van Gils (2020) describes NoSQL as a modern development where structuring the data a priori is forgone, and instead users interpret the data once they query them, which is also inline with instance-based principles.

Instance-based data can be represented using the Resource Description Framework (RDF). RDF provides a way to describe the relationship between information resources in the form of triples: subjects that have properties with certain values (Klyne & Carroll, 2006). RDF syntax reflects a simple graph-based data model (Klyne & Carroll, 2006). We use a similar approach to represent instance-based data. The instance-based model treats an instance as a symbol designating the perceived existence of “a material object, action, event, or any other phenomenon” (Parsons & Wand, 2008b, p. 842). We talk about instances in terms of their properties, which constitute statements about instance characteristics (Parsons & Wand, 2008b). Properties can belong to an instance alone (intrinsic properties) or be shared between two or more instances (mutual properties). To model information in a manner consistent with instance-based princip les,<sup>3</sup> we use a representation in which an instance in the domain is represented as a node. Intrinsic properties are grouped together and depicted on top of the node object. If two instances share one or more mutual properties, they are connected by arcs labelled with the mutual properties’ names.

This representation does not have constructs – such as primary keys, foreign keys, and cardinality constraints – that are necessary for understanding classes and relationships in relational representations. We posit that benefits of the instance-based approach will be realised using such a conceptual representation. Refer ring to a classification scheme of an employee database (Figure 1, which was designed by an external source – described in more detail below), we created an instancebased representation in Figure 2. Table 1 provides a list of properties that a thing or link may have.

Note that the proposed representation is not completely free of structure. Its limited structure consists of representing things and their intrinsic properties as nodes and mutual properties as links. However, unlike class-based representations, this structure does not include a fixed set of predetermined classes. For example, in a class-based representation, two records in a table would have the same number of attributes; some attributes might be null, but the number of cells allocated to a record in a row is fixed. In the instance-based representation, however, two instances that can be viewed in a common class need not have identical properties. For example, one instance might have properties: name, address, GPA, and musical instruments played, while the other instance may have only name and GPA. One could infer both instan ces are students, but due to the flexible nature of instance-based representations, we can represent uniq ue or scarce properties. Our representation removes the pre-determined clustering or grouping of attributes around an entity type.<sup>4</sup> The representation we propose is one way of viewing instances and their properties. However, it need not reflect how the data is stored.

![](/api/attachments/F72WQR79/fulltext/images/33f18b0c7dab2cbfcebe72fccac9666868b100e1d1cb3adf752cf99e79f2877d.jpg)  
Figure 1. Schema of the Lockheed-Martin analytics challenge dataset.

Provided the user has some knowledge about the domain and the task being performed, three reasoning mechanisms can be used to make inferences regarding data in an instance-based representation. First, inferences can be based on the properties of instances: knowing some properties can be enough to infer a relevant class (depending on the task). If an instance is a living thing with feathers and wings, it can be inferred that it is a bird.<sup>5</sup> Second, inferences can be made based on the relationships between instances. Considering the location of an instance with respect to a connecting link (origin or end), users can make inferences regarding the instance, assuming they have some common-sense classification of the domain. For example, if we have a directed link labelled “Employs”, from a node with name property of “Sarah”

to a node with name property of “John”, the instance that has the “Employs” link emanating from it (i.e., Sarah) is the employer, and “John” is the employee. Finally, a user can make inferences based on the properties of an instance and the links connected to it. Knowing that an instance has an outgoing link titled “Employs” might be enough to identify it as employer. One can then distinguish between corporate and individual employers by observing properties of the instances. A property like “date of birth,” will indicate an individual employer; a property like “head ofice location” will indicate the instance is a corporation.

The dataset and its classification scheme here were taken from the Lockheed Martin analytics challenge from the Association of Information Systems (AIS) Student Chapter.<sup>6</sup> The dataset was class-based (Figure 1) and was designed by the sponsors of the competition (details are discussed below). Using the proposed modelling method for representing instance-based data, we created a graph model as a conceptualisation of that domain (Figure 2) for the instance-based condition. We also provided subjects with a table listing all the relevant properties with some context clues in case of ambiguity (e.g., action with regards to what phenomenon – Table 1).

Below, we discuss two exemplar operations that could be performed by content consumers using the two representations (Figures 1 & 2). The first example is an openended task that requires exploring the information to identify a recurring pattern of phenomena (see Experiment I section); the second is a closed ended-task with well-defined parameters (see Experiment II).

![](/api/attachments/F72WQR79/fulltext/images/0c3de703e201b1d4b8ba2f25814bdc959c2da528e1a9242bd6dec2fa5bff9eec.jpg)  
Figure 2. A fragment of the instance-based conceptualisation of the domain.

First, we focus on the information exploration task, which is operationalised by pattern identification in the data. This task requires testing diferent scenarios or hypotheses to see which behaviour or trait is occurring on a frequent basis. Such occurrence may be the manifestation of a phenomenon or indication of a problem (as defined by McGarry, 2005). Of course, investigating different possible scenarios requires some context and background knowledge regarding the domain of interest. Otherwise, a user or a program decides to test all the possible data combinations. We focus on human analytical reasoning by content consumers performed when users need to detect expected patterns and discover unexpected ones (Thomas & Cook, 2006).

A user of the class-based representation with access to Figure 1 needs to spend some time to understand the arrangement of information. A typical content consumer may start with employee as the unit of analysis. In Figure 1, there is an Employee class at the centre that lists basic information about an individual, including their name, hiring date, gender, marital status, and citizenship code. The citizenship code (along with employee ID) is used as a referential key to the Citizenship class. There is also a separate class called Contact Info, where employees’ email and different phone numbers (e.g., personal and business cell phone numbers) are stored. The Performa

nce Record class includes the location as well as the departments where each employee works at. This classification scheme allows for keeping track of employees’ activities on the Internet through the Server Access Log class – this class is connected to the Employee class via the Performance Record table. Furthermore, the classification scheme also records air travel records of employees, as well as their phone access logs.

Once the user has spent time to understand what the designer of this classification scheme intended to represent, then s/he may need to start testing possible relationships that could indicate recurring traits (i.e., patterns). The user may decide to identify what is internal vs. external with regards to the company boundaries. Upon further reflection, the user will find that Destination Number in the Phone Log class, Arrival and Departure Cities in the Air Travel class, and Host IP in the Server Access Log class indicate information external to the company. At this point, the user may try to investigate possible correlations between employees’ citizenship and the destinations that they call, as well as destinations to which they travel. This information is spread across the Citizenship, Air Travel, and Phone Log classes (investigated through join operations). In case a significant correlation is identified, to find the names of those employ ees, the user needs to find the data in the Employee class.

Table 1. List of relevant properties.

<table><tr><td>Property</td><td>Description</td></tr><tr><td>Action</td><td>Action taken in accordance to an employee&#x27;s performance</td></tr><tr><td>Address</td><td></td></tr><tr><td>Airline</td><td></td></tr><tr><td>Area Code</td><td></td></tr><tr><td>Arrival City</td><td></td></tr><tr><td>Arrival Date</td><td></td></tr><tr><td>Arrival Time</td><td></td></tr><tr><td>Birth Country</td><td></td></tr><tr><td>Birth Date</td><td></td></tr><tr><td>Business Cell</td><td></td></tr><tr><td>Business Email</td><td></td></tr><tr><td>Business Phone</td><td></td></tr><tr><td>Caller Name</td><td></td></tr><tr><td>Citizen Country</td><td>A two-letter code identifying one&#x27;s citizenship</td></tr><tr><td>Citizen Status</td><td>Country of citizenship</td></tr><tr><td>City</td><td></td></tr><tr><td>Country</td><td></td></tr><tr><td>Date and Time</td><td>Date and time of accessing servers</td></tr><tr><td>Department</td><td></td></tr><tr><td>Departure City</td><td></td></tr><tr><td>Departure Date</td><td></td></tr><tr><td>Departure Time</td><td></td></tr><tr><td>Destination</td><td>Destination country of a phone call</td></tr><tr><td>Destination No.</td><td>Destination number of a phone call</td></tr><tr><td>Domain</td><td>Domain name of local servers</td></tr><tr><td>Duration</td><td>Duration of a phone call</td></tr><tr><td>Effective</td><td>Effective date for an executive decision (e.g., promotion)</td></tr><tr><td>Employee ID</td><td></td></tr><tr><td>Fax</td><td></td></tr><tr><td>First Name</td><td></td></tr><tr><td>Flight Number</td><td></td></tr><tr><td>Gender</td><td></td></tr><tr><td>Host IP</td><td>IP address of a web host</td></tr><tr><td>Host Name</td><td>Name of a web host</td></tr><tr><td>In/Out</td><td>Incoming or outgoing call</td></tr><tr><td>Job Code</td><td>A four-character code assigned to a position</td></tr><tr><td>Last Name</td><td></td></tr><tr><td>Loc. Area Code</td><td>A four-character code assigned to a location</td></tr><tr><td>Marital Status</td><td></td></tr><tr><td>Name</td><td></td></tr><tr><td>NTID</td><td>Network ID assigned to users (a la username)</td></tr><tr><td>Personal Cell</td><td></td></tr><tr><td>Personal Email</td><td></td></tr><tr><td>Reason</td><td>Reason for an executive decision</td></tr><tr><td>Region</td><td></td></tr><tr><td>Source</td><td>Source country of a phone call</td></tr><tr><td>Source Number</td><td>Source number of a phone call</td></tr><tr><td>ST</td><td>State</td></tr><tr><td>Start Date</td><td>Date of employment</td></tr><tr><td>Status</td><td>Employment status (e.g., active)</td></tr><tr><td>Time</td><td></td></tr><tr><td>Zip Code</td><td></td></tr></table>

Considering the same task (i.e., information exploration) with a non-classified dataset, a user may start with the list of attributes as in Table 1. There is also a possible conceptualisation of data in Figure 2; however, as mentioned earlier, we do not bind the data to any structure. In the possible conceptualisation that we provided, all the information intrinsic to one object is grouped together and presented on top of it. Similar objects may have diferent number of intrinsic attributes. Consulting with the list of attributes in Table 1, a user may start investigating the correlation between attributes that might be of interest. Correlations related to attributes of the same node can be tested (e.g., marital status and job code to find if married people are more likely to assume certain jobs), as well as correlations related to connected nodes (e.g., department attribute of one node, and Host IP address of another node to find what IP addresses are most frequented by the Finance department employees), or performance evaluations and employee gender, or other hypotheses that the content consumer can think of.

The instance-based representation may seem overwhelming at first, but we postulate that the cognitive load of understanding someone else’s classification schema is greater than the cognitive load of figuring out what the non-classified data represents (considering the context and the inference mechanisms discussed earlier). Instance-based data allow individual users to form their own views and test diferent arrangements of data that are more congruent with their prior knowledge and experience. This claim is supported by cognitive schema theory (Derry, 1996), which posits that humans assimilate information better when they can gradually build a schema (from individual data blocks) in their working memories based on previous knowledge and experience. When users view the data through a lens informed by their own views, they can understand the data better.

Similar to the previous exercise, users may perform closed-ended tasks (data querying) with well-specified parameters. A query may require identifying all the employees who received a promotion within the last year and their email addresses for a congratulatory message to be sent by the manager. A user of relational or class-based data needs to identify where these attributes can be found on the classification scheme. Referencing Figure 1, to find promotions within the last year, the user needs to look up Actions (reflecting promotions) record ed in Performance Records class, as well as their Efective Dates (and filter for the given period). Once those employ ees who received a promotion within the last year are identified, the user needs to look up their names in the Employee class (using Employee ID as a foreign key) and find their email addresses in the Contact Info class (again, using Employee ID as a reference).

Retrieving the same information (promotions within the last year and email addresses) in an instance-based representation requires identifying the relevant attributes in Table 1. These attributes are Action, Efective Date, First and Last Name, and Business Email. Unlike the class-based representation, the user would not need to pinpoint the classes where these attributes are recorded and their reference keys. Looking at the list of attributes in Table 1 (or doing a search on a digital file), they can select the relevant attributes.

## 4. Research model

This research evaluates the ability of content consumers to use instance-based representations in information exploration (open-ended tasks), as well as in querying data with well-known parameters (closed-ended tasks). These two task types draw from a taxonomy of system usage types proposed by March (1991), in which uses of information are categorised into exploitation and exploration of information. Exploitation is “routine execution of knowledge, whereas exploration refers to the search for novel and innovative ways of doing things” (Burton-Jones & Meso, 2006, p. 236).

Consistent with the diferences between the instancebased and class-based paradigms, two representations were designed. In the class-based representation, the information was structured based on predefined classes. In the instance-based representation, information was structured as a list of attributes with a brief description of their meaning in the domain. This representation was free of predefined classification structure (Appendix A2).

For the target population (i.e., content consumers who are not professional database users<sup>7</sup>), exploration could be operationalised by deriving insights from the data and identifying patterns – recurring characteristics that could help identify a phenomenon (McGarry, 2005). Within th is context, we claim that efective use is manifested by users’ ability to identify high-quality patterns of kno wledge:

Proposition 1: Content consumers who use an instan ce-based representation of a domain will be able to perform information exploration tasks more efectively (by identifying patterns of higher quality) than content consumers who use a class-based representation.

As mentioned earlier, we used human analytical reasoning by content consumers to study exploration and knowledge discovery. Examples of analytical reasoning (performed by subjects of our experiment) are provided in Appendix C1.

Analytical reasoning may detect a large number of patterns, not all of which are of equal quality. Quality measures are needed for ranking identified patterns according to their potential interest to a user (Geng & Hamilton, 2006, p. 1). Objective pattern quality measures statistical strength of the discovered pattern (McGarry, 2005, p. 39) based on raw data, independent of the user or application (Geng & Hamilton, 2006). Subjective pattern quality takes into account beliefs or expectations about the problem domain (McGarry, 2005, p. 39). We used both types of evaluations, as will be discussed later.

We also evaluate content consumers’ ability to query the data and retrieve information based on known parameters (e.g., finding all third-year marketing students with a GPA of greater than 80%). Although the task type is well-defined (closed-ended), content consumers may address a variety of objectives while performing such tasks (for example, find all students who failed introduction to MIS, or find all the instructors who taught at the main lecture hall), not all of which anticipated in the design of the class-based schema. Thus, the flexibility aforded by the instance-based approach in organising the data could be of great value.

To measure performance, we asked subjects to describe (verbalise) the cognitive procedure to perform a data retrieval task via the representation to which they had access. We rely on a general verbal description of the procedure. This evaluation method was proposed by Ford (2004) and was also used by Bera et al. (2011) to measure subjects’ ability to utilise knowledge management systems. It is also in line with what Ogden (1986) called “query translation” – stating the query in terms of the data schema, independent of query language syntax. An example of the step-by-step procedure of performing an information retrieval task is presented in Appendix C. Accordingly, we propose:

Proposition 2: Content consumers who use an insta nce-based data representation will be able to use a system more efectively (operationalised in terms of more accurate query formulation) than content consumers who use a class-based representation.

## 5. Experiment I

## 5.1. Design and experimental material

We used a simple control-treatment design for this experiment. Subjects in the control group received a class-based dataset (Figure 1, as designed in the competition, with 10,000 employees, and multiple performance evaluations, travel, phone, and internet access logs per employee, containing more than one million records in total). Subjects in the treatment group received an insta nce-based, schema-free dataset (Figure 2) using a graphbased model as a conceptualisation of the domain. Subjects were instructed to report patterns that might be worth investigating further by the stakeholders of the company. Note that users’ comprehension of patterns using conceptual models has been studied in IS domain by Poels et al. (2011), Poels (2011), and Bera and Poels (2019); however, these studies evaluated class-based conceptual models that were rooted in diferent design ontologies, namely, Resource-Event-Agent (REA) ontology, vs. non-REA. Our experiment is diferent as it compares users’ ability to generate patterns using class-based versus instance-based representations regardless of underlying ontological theory.

We selected Tableau,<sup>8</sup> a business analytics application, as a platform for the experiment. Tableau satisfies the requirements for the task: it facilitates analytics reasoning by providing an interactive visual interface for human users (Thomas & Cook, 2006). Moreover, it enables users to form categories by grouping properties based on their own requirements (i.e., to define their own classification). This feature allowed us to declassify the data for the instance-based condition. Users can group attributes together and define new classes, whether in the Tableau interface (as presented during the training procedure,<sup>9</sup> of the experiment) or in their working memories while performing the task.

Based on Proposition 1 above, we hypothesise:

H1: The quality of patterns identified by users of an instance-based representation will be higher than the quality of patterns identified by users of a class-based representation.

We investigate this hypothesis from three perspectives – the first two related to objective pattern quality measures, while the third is subjective:

(i) ability of users from each condition to assert true statements derived from the data,

(ii) overall precision of reported patterns, and

(iii) insights gained from the patterns.

For each perspective, we have a sub-hypothesis and a dependent variable to test:

H1a: On average, users of an instance-based representation will be able to identify more correct (true) patterns than will users of a class-based representation.

We first evaluate the correctness of statements identified by each subject with respect to data. Each subject will receive a score corresponding to the number of true statements they identified (e.g., a score of 11 if 11 true statements are identified).

![](/api/attachments/F72WQR79/fulltext/images/e4c2a263fc2d4628247cc433ebefedf24fda6c594d428fb24c2d0869b69d550f.jpg)  
Figure 3. Tableau interface for the class-based group.

Figure 4. Tableau interface for the instance-based group.  
Table 2. Measures of Prior Knowledge.

<table><tr><td></td><td>Written Queries Before (Y/N %)</td><td>Database Knowledge</td><td>Human Resources Knowledge</td></tr><tr><td>Class-based</td><td>57%</td><td>2.86/7</td><td>2.81/7</td></tr><tr><td>Instance-based</td><td>52%</td><td>2.90/7</td><td>3.33/7</td></tr></table>

H1b: Precision of patterns identified by users of an instance-based data representation will be higher than that of users of a class-based data representation.

Precision is defined as “the number of retrieved relevant items as a proportion of the number of [all] retrieved items” (Buckland & Gey, 1994, pp. 12–13). The desired (or relevant) outcome is a true statement, and total outcomes include all statements generated by subjects. The dependent variable is the ratio of number of true statements from each group to the total number of statements generated by all subjects in that group.

H1c: Users of an instance-based representation will identify more insightful patterns than users of a classbased representation.

To determine insightful patterns, an evaluator identifies the statements that might be surprising and useful, taking into account expectations from a domain. To illustrate, a pattern stating “sales in December are high” in a retail setting is to be expected (because of the holiday season), whereas “shipping furniture to customers in California takes longer than the average shipping time” might be an unanticipated finding that can lead to an investigation in the supply chain.

We predict that users are more efective in assimilating new information when they can construct mental models congruent with their prior knowledge, rather than trying to understand a predetermined classification scheme created by a database designer. Subjects in the class-based group received the classification schema (Figure 1). As illustrated in Figure 3, Tableau shows a list of classes that are defined in the dataset – users can expand any class on the list to view its defining attributes.

Subjects in the instance-based group, however, viewed the list of attributes sorted alphabetically (Figure 4). Users could drag and drop attributes onto each other to form classes. Although the option to do this was explained in the training, only one subject (in the pilot of 14 subjects) formed a single class by using this feature. The other subjects (in the pilot or the main experiment) performed the task by focusing only on the instances and the attributes they possessed (Figure 2 and Table 1).

Note that Tableau provided identical functionalities and features to users of both groups, thus helping ensure instantiation validity (Lukyanenko et al., 2014a). The only diference between the experimental material between the groups was how the information was organised; that is, whether the attributes were grouped into classes (Figure 3) or presented free of classification (Figure 4).

## 5.2. Participants

Subjects were business school students from a large Nor th American university registered in third- and fourthyear Bachelor of Commerce courses.<sup>10</sup> Compeau et al. (2012), in their commentary regarding the use of student subjects in empirical experiments, argued that it was justified to use students if they were within the target population of the tested theoretical model. In our expe riment, students are indeed a subgroup of content consumers and also appropriate surrogates for business users as a great portion of these students are employed by profe ssional services firms upon graduation. We performed a pilot with 14 subjects (evenly split between class-based and instance-based groups). Based on the pilot, we reworded the experimental task to further clarify it.

For the main experiment, we recruited 42 subjects, 11 from third- and fourth-year students who were either registered in an “Information Systems Technology and Development” course or had already completed that course. Table 2 summarises their prior database and domain knowledge levels.

Table 3. Summary Statistics of pattern quality measures in Experiment I.

<table><tr><td>Condition</td><td>All Statements</td><td>True Statements</td><td>Mean (SD) of True Statements/Subject</td><td>Mean (SD) of Precision (True/All)</td><td>Unique (and True)</td><td>Unique/Total</td><td>Unique/True</td></tr><tr><td>Class-based, n = 21</td><td>156</td><td>95</td><td>4.52 (3.17)</td><td>60% (0.49)</td><td>48</td><td>0.31</td><td>0.51</td></tr><tr><td>Instance-based, n = 21</td><td>201</td><td>162</td><td>7.71 (4.78)</td><td>81% (0.40)</td><td>88</td><td>0.44</td><td>0.54</td></tr><tr><td>Two-tailed P Value</td><td></td><td></td><td>0.015 $^{\circ}$  Significant</td><td>0.0001 $^{\circ}$  Significant</td><td>N/A</td><td>N/A</td><td>N/A</td></tr></table>

Table 4. Example coding for insightful statements (patterns) in Experiment I.

<table><tr><td>Statement</td><td>True/False</td><td>Insightful</td></tr><tr><td>Corporate department tends to have the most amount of pay increase</td><td>True</td><td>0</td></tr><tr><td>Sales department has the least amount of pay increase</td><td>True</td><td>1</td></tr><tr><td>Employee ID 117,501 has significantly longer call duration compared to others</td><td>True</td><td>1</td></tr><tr><td>Number of female employees is much larger than males</td><td>True</td><td>0</td></tr></table>

## 5.3. Experimental task and procedure

A 20-minute training video was used to teach subjects how to explore information and identify patterns using Tableau (based on fictional online retailer data). The video was edited from Tableau’s training material. Participants could revisit the training video any time to review Tableau’s functions and operations. During the experiment, participants were also encouraged to ask questions if they needed further clarification about the task or the application.

We asked subjects to report all patterns in the data that might be worth investigating further by the stakeholders of the company (Appendix A contains the experimental material). We only experimented in one domain because the current experiment required (after 20 minutes of training) over an hour of interaction with the system on average (Table 3).

## 5.4. Data analysis and results

We operationalised information exploration and knowledge discovery by asking subjects to identify patterns. Subjects reported a total of 357 patterns. We evaluated quality of patterns objectively with respect to the data source to determine whether they were true or false. This evaluation was done by an impartial research assistant (RA) who had expertise in statistics and databases. The RA’s evaluations were verified by one of the authors for correctness – the few observed discrepancies were resolved by referring to the data source (i.e., an objective statistical analysis) until consensus was reached. Table 3 summarises the results of the experiment.

To test H1a, we compared the average number of true statements produced by participants in each group using a t-test,<sup>12</sup> (Table 3). Our results support H1a: participants using the instance-based representation were able to identify more correct patterns than those using the class-based representation. For overall precision of statements generated by users of instancebased vs. classified representations (H1b), we also conducted a t-test.<sup>13</sup> The results in Table 3 show that participants in the instance-based group outperformed those in the class-based group.

We also identified unique statements (among the set of true ones) in each experimental condition. The number of unique statements (or patterns) is an indication of the output diversity resulting from the representation type (class-based vs. instance-based). As Table 3 shows, subjects in the instance-based group generated 88 true and unique patterns, while subjects in the classified group only generated 48 unique patterns. Ratios of unique patterns to all statements and to true statements are reported in Table 3 as well. As we expected, users of instance-base data were not anchored to a pre-determined classification of the data and faced fewer restrictions. Hence, they managed to generate more unique patterns, which indicates diversity of their output.<sup>14</sup> This is in line with our theoretical justifications rooted in Tversky and Kahneman (1974) work on human decision-making and efects of anchoring.

H1c is based on a subjective measure of pattern quality – whether the insight gained from the pattern can be of use to stakeholders. From the set of correct/true patterns, we tried to identify the unique patterns in each group.<sup>15</sup> We provided the subset of unique and true patterns to two judges (PhD students with professional master’s degrees and at least two years of industry experience in business intelligence). The judges were asked to identify the patterns they considered insightful, or of value to the stakeholders. The judges referred to the dataset and tried to remove patterns that were not of material importance, or were likely information already known by the stakeholders. For example, the dataset included records of 10,000 employees; 49 employees were citizens of Peru, and the majority (97%) were from the US. A pattern stating “all Peruvian employees are female” was true according to the data but was eliminated by the judges considering the rather small scale of the finding (49/10,000 or 0.5%).<sup>16</sup> A pattern that may be already known to the stakeholders was “majority of promoted employees are female”; according to the data, 77% of employees were female, so it is not surprising that the number of promotions would be proportional to the employee base (which is probably known by the stakeholders).

Table 5. Performance with respect to insights gained from patterns.

<table><tr><td>Condition</td><td>No. of Reported Statements</td><td>No. of True Statements</td><td>No. of Insightful Statements</td><td>Insightful/No. of Statements</td><td>Insightful/No. of True Statements</td><td>Insightful/Subjects</td></tr><tr><td>Class-based</td><td>156</td><td>95</td><td>9</td><td>0.06</td><td>0.09</td><td>0.43</td></tr><tr><td>Instance-based</td><td>201</td><td>162</td><td>15</td><td>0.07</td><td>0.09</td><td>0.71</td></tr></table>

Table 6. Descriptive statistics of query accuracy and task completion time in Experiment II.

<table><tr><td>Condition</td><td>Travel agency mean (SD)/4</td><td>Consulting mean (SD)/4</td><td>Time (min) mean (SD)</td></tr><tr><td>Class-based, n = 63</td><td>2.82 (0.82)</td><td>1.96 (0.71)</td><td>33.65 (9.70)</td></tr><tr><td>Schema, n = 32</td><td>2.85 (0.79)</td><td>1.92 (0.76)</td><td>27.78 (6.37)</td></tr><tr><td>Schema &amp; data, n = 31</td><td>2.78 (0.86)</td><td>2.00 (0.67)</td><td>39.71 (8.80)</td></tr><tr><td>Instance-based, n = 67</td><td>3.42 (0.52)</td><td>2.95 (0.70)</td><td>38.13 (8.30)</td></tr><tr><td>Schema, n = 36</td><td>3.43 (0.54)</td><td>2.94 (0.65)</td><td>35.81 (7.42)</td></tr><tr><td>Schema &amp; data, n = 31</td><td>3.39 (0.49)</td><td>2.96 (0.78)</td><td>40.84 (8.56)</td></tr></table>

Two useful examples are: “Corporate department is seeing an increase in demotions since 2009”, and “number of demoted male employees in IT department is greater than females”, which is not proportional to the employee base (of 77% female). To demonstrate this stage of analysis, Table 4 shows sample answers provided by one of the subjects (Subject #21 in the class-based group), the number of statements that were true with respect to data, and the ones that our coders found insightful.

The descriptive statistics from this round of analysis are shown in Table 5. The reliability of the scales generated by the two coders was high, as the Cronbach’s alpha was 82.1%. Note that we did not attempt to resolve the disagreements between the coders; rather, Table 5 is based on the data from the first coder. Significance testing was not possible due to the small number of statements qualified as insightful. Nevertheless, the results are consistent with H1c and mirror the results of H1a and H1b.

## 5.5. Additional analyses

We measured task completion time. Users of the instance-based representation were on average seven minutes faster (59 minutes versus 66 minutes), but the diference was not statistically significant (with p-value of 0.122). In addition, we investigated the moderating efect of prior database knowledge and prior domain knowledge on the number of true statements generated by each subject. We looked at the interaction efect of prior database knowledge and experimental conditions on subjects’ performance, as well as the interaction efect of prior domain knowledge and experimental conditions on performance. No significant interaction was found in this analysis (p-values of 0.678 and 0.762, respectively).

## 6. Experiment II

## 6.1. Design and experimental material

Whereas Experiment 1 focused on the identification of potentially interesting patterns in data, we also are interested in content consumers’ ability to perform more typical query tasks on instance-based data to satisfy well-defined information requests (i.e., exploitation of information as per March’s 1991 taxonomy). Experiment 2 used a 2 × 2 between-subjects design to study this question. For the first factor, subjects were randomly assigned to either the class-based or instance-based representation. The second factor manipulated whether subjects received only a general structure (schema) of the data (in the class-based condition, this was a UML class diagram, while the instance-based condition consisted of a list of properties that a thing could have and type of links that connect diferent things) or the general schema as well as actual data. The allocation of subjects in diferent conditions is shown in Table 6. The experimental material is provided in Appendix A3 and the answer key is in Appendix B.

Table 7. Between factors results in the experiment demonstrating better performance by instance-based users.

<table><tr><td>Factor</td><td>F-value with df = 1</td><td>P-value</td></tr><tr><td>Performance of users in the Instance-based vs. Class-based group (between-factor)® significant difference in favour of Instance-based</td><td>57.300 $^{1}$ </td><td>&lt; 0.0001</td></tr><tr><td>Performance of users using Schema vs. Schema &amp; Data combined (between-factor)</td><td>0.004</td><td>0.948® N.S.</td></tr><tr><td>Instance-based vs. Class-based * Schema vs. Schema &amp; data (interaction effect)</td><td>0.011</td><td>0.915® N.S.</td></tr></table>

df: degrees of freedom, N.S.: Not Significant  
1 We performed this analysis with data from the second coder as well. The F-value for the efect of class-based vs. instance-based representations was 48.65 with p-value of <0.0001. The F-value for Schema vs. Schema & Data was 0.052 with p-value of 0.819 (i.e., not significant), and the F-value for the interaction efect was 0.009 with p-value of 0.923 (i.e., not significant).

Table 8. Task completion time in Experiment II.

<table><tr><td></td><td>Schema</td><td>Schema and data</td><td>Two-tailed P-value</td></tr><tr><td>Class-based</td><td>M = 27.78, SD = 6.37, n = 32</td><td>M = 39.71, SD = 8.80, n = 31</td><td>&lt; 0.0001® Significant</td></tr><tr><td>Instance-based</td><td>M = 35.81, SD = 7.42, n = 36</td><td>M = 40.84, SD = 8.56, n = 31</td><td>0.012® Significant</td></tr><tr><td>Two-tailed P-value</td><td>&lt;0.0001® Significant</td><td>0.611® N.S.</td><td></td></tr></table>

M: Mean, SD: Standard Deviation, n: Sample Size, N.S.: Not Significant

The second factor (i.e., schema vs. schema and data) in our experimental design was included to provide an ecologically valid experimental task. A classification schema without data is the natural form of representing and retrieving class-based information; thus, it was important to have this representation of the data in our study. On the other hand, for an instance-based representation, it is the actual data (instances) that are integral for reasoning; thus, it was necessary to provide both structure and actual data to the users. We believed the comparison between class-based schema in the form of tables and instance-based data in the form of graphs might have confounded findings, as it would be impossible to tease out whether results were due to representing classes versus instances or to representing schema only versus schema and data. To ensure a meaningful comparison between the key conditions, we provided a match between the “natural” form of each representation (data for instance-based and schema for class-based) and a structurally equivalent representation in the other paradigm. We also wanted to ensure that the experimental outcome was not an artefact of the task domain. Hence, subjects in each group performed tasks for two domains (a travel agency and a consulting firm).

Experimental tasks were exemplars of the queries a typical business might perform. Many of the questions were formulated in terms of classes (e.g., find “Clients” or “Agents”), which might favour the class-based group. However, we tried to make the conditions informationally equivalent. Specifically, for the condition in which subjects received both schema and actual data, we provided the same amount of information (i.e., individual instances and their relevant properties) in both instancebased and class-based groups (see Appendix A3).

We presented the experimental material using a noninteractive visual representation of the data, similar to Bera et al. (2011) and Gupta and Jain (1997). The experiment evaluated participants’ ability to successfully achieve their information retrieval needs when interacting with instance-based representations (compared with class-based), rather than ability to learn how to use a particular implementation. Moreover, as we have set our scope to users who are not IT experts, in contexts such as self-service business intelligence, we asked participants in both conditions to provide syntax-neutral statements regarding how they would utilise the information provided to them (see Appendix B).

## 6.2. Participants

We recruited subjects from an undergraduate course titled “Information Systems Technology and Developme $\mathrm { n t } ^ { \dprime }$ at a large North American university. This course required students to spend two hours in lecture and one hour in the laboratory per week. Students learned database concepts (e.g., ER diagrams and creating tables, forms, and queries). The laboratory was taught using Microsoft Access® 2010, and students were required to deliver assignments based on Access®. When we conducted the experiment, participants were almost halfway through the course and had already learned about data modelling (entity-relationship grammar, as well as creating tables and relationships in MS Access®), query principles (only in lecture), designing forms, and generating reports. Volunteers received a 2% bonus on their final mark in the course. A pilot was done with 14 participants, testing one of the factors – both instance-based (6) and data class-based (8) users had access to structure and data. Based on the answers, we reworded some questions.

## 6.3. Experimental task and procedure

The experiment began with a 20-minute training session delivered by one of the authors. We demonstrated the process of retrieving information and how to verbalise it using the provided representation (i.e., class-based representation for the control group and instance-based representation for the treatment). The training material was based on a fictional movie rental store (diferent from the domains in the experiment). Participants were encouraged to ask questions if there was any confusion. After the training, participants were asked to fill in a short questionnaire (available in Appendix A1) to measure their prior domain knowledge as well as their familiarity with database systems. No statistically significant diference was observed among the measures of prior knowledge between the two groups.

The order of domain assignments was random. Half the subjects in each condition received the travel agency case first, and the other half received the consulting firm first. For each domain, there were four questions that varied in dificulty (e.g., Question 3 in the travel agency case required joining two tables, whereas Question 4 required joining five tables) (Appendix A). The order of questions was also randomised to control for learning efect.

## 6.4. Data analysis and results

Each subject answered four questions related to the travel agency domain and four questions related to the consulting domain. The answers described the steps required to solve a problem. Examples of answers provided by our subjects are available in Appendix C. Appendix C2 shows how our subjects applied the three mechanisms to make inferences on instanced-based data (described above in the “Modelling Instance-based Data” section).

Answers were scored on a 5-point scale from 0 to 1. If the answer was completely irrelevant, a score of 0 was given. If more than 0 but less than half the steps were correct, a score of 0.25 was awarded. If half or a majority of the steps were correct, 0.5 and 0.75 were assigned, respectively. If all the steps were correctly identified, the subject received 1.00 for that question (see sample responses from actual subjects in Appendix C2). As there were four questions for each domain, a subject received a total score out of 4.00. Subjects’ responses were evaluated by two coders. To measure inter-rater reliability,<sup>17</sup> we calculated the intra-class correlation (ICC) between the ratings of the two coders. The ICCs for the travel agency and consulting cases were 83% and 87%, respectively, indicating a high level of consistency. The analysis was performed using the data from the first coder. Table 6 provides descriptive statistics relevant to each measured variable.

Based on the propositions in the Research Model section, we hypothesise:

H2: Query formulation performance will be higher in the instance-based data condition than in the classbased condition.

To test the hypotheses, we conducted ANOVA (Table 7).<sup>18</sup> In the following, we present our analysis of the data for each variable. In summary, H2 was supported, since subjects in the treatment group (i.e., instance-based representation) demonstrated higher efective use (performance) than subjects in the control group (i.e., class-based representation); the two-tailed p-value was less than 0.0001.

Our second between-subjects factor, which compared the performance of subjects using only the schema with subjects using schema and the data, did not show a significant diference (p-value = 0.948 ® not significant). Note that we did not hypothesise about such a diference, as we included the “schema and data” option in the class-based condition and the “schema only” condition in the instance-based condition to avoid potential confounds in comparing the “natural” version in each condition. We also observed no interaction efect (p-value = 0.915 ® not significant) between representation type (i.e., instance-based vs. class-based) and the second factor of our experimental design (schema vs. schema and data). In addition, we analysed the efect of prior database knowledge on performance. We used the prior database knowledge measures reported by subjects as a covariate in our model. The results showed that prior database knowledge did not have a significant impact on users performance.

In addition, we recorded the order of case assignments to subjects (i.e., whether they received the travel agency case or the consulting case first). The efect of this covariate was not significant either. Based on this, we conclude that we successfully controlled for learning efect by randomising the order of case assignment. We also studied the efect of prior domain knowledge (both travel agency and consulting) on users’ performance by examining the interaction efect between prior travel agency knowledge and experimental condition on performance in travel agency and the interaction efect between prior consulting knowledge and experimental condition on performance in consulting. The moderating efect of prior travel agency knowledge on performance was not significant (p-value of 0.77); however, prior consulting knowledge had a significant efect on performance (p-value of 0.03). This could mean that higher levels of prior consulting knowledge strengthened the efect of instancebased representation.

## 6.4.1. Task completion time

The task completion time measured in this experiment included the time taken to perform the tasks related to both domains of travel agency and consulting firm; thus, we used a simple t-test to compare the task completion time between the two groups (rather than ANOVA). As shown in Table 8, subjects using the class-based representation completed the task in less time than subjects using the instance-based approach.

In comparing the second between-factor of our study (schema vs. schema and data), participants in the classbased group who had access to only the schema performed their task quicker than participants in the insta nce-based group (with the same condition of only using the general structure). This could be a consequence of familiarity; subjects had been trained in class-based data management methods for five to six weeks prior to their participation in the experiment, compared with only 20 minutes of training in instance-based representations.

## 7. Discussion and limitations

To improve the validity of the experiments and reduce biases, two modelling experts went over the experimental material. Subjects’ prior database knowledge and domain knowledge were controlled. Using student subjects in a laboratory experiment can be considered a limitation. However, students are within the target population of our research model (Compeau et al., 2012); hence, we consider them an appropriate choice. In addition, as this experiment was the first study of content consumers’ use of instance-based representations in information exploration and query tasks, we considered internal validity to be of critical importance. Thus, a laboratory experiment instead of a field experiment in this case was justified (Calder et al., 1981). To address the external validity concern, the generalisability of the approach as well as its implications in the real world need to be considered in future research.

As for users’ ability to use instance-based data, Cognitive Schema Theory (Derry, 1996) predicts that when the problem schema is compliant with the mental schema of prior knowledge, users’ ability to assimilate information improves. A concern could be raised that instance-based data may include more irrelevant instances than irrelevant classes in the class-based paradigm. In our experiment, the issue of having too many instances does not apply as subjects studied only the instances that were relevant to their needs based on selected attributes of interest. Therefore, users of the instance-based data will not be overwhelmed with the number of instances and attributes that might exist in a repository. Users of an instance-based data source are able to view only the instances and properties that are congruent with their current task and the mental model they have built in their minds in the process of solving the problem. In contrast, users of the classbased approaches need to understand a schema developed by database designers (based on defined data needs and congruent with designers’ mental frameworks). This issue might not apply to professionals with years of experience in relational databases. Such users may find class-based representations even preferable. Our empirical experiments, however, were on content consumers who were not experts in technology, and we showed that despite the anticipated disadvantage, users of instance-based data achieved better results. Hence, the initial efort required to understand the instance-based data would pay of with the improved performance in running routine queries and exploring the data.

A further limitation arises from the specific way in which we instantiated instance-based representations. For example, we chose not to use classes at all so we could maximally distinguish our proposed representation from the class-based structure. An alternative would be to represent both instances and classes in the same structure (Eriksson et al., 2019), which might allow users to reap the advantages of both forms of representation.

There is also research on implementation issues related to schema-free (instance-based) data, including scalability, and concerns related to management of data such as data cleaning and integration from various sources (Corbett et al., 2013). Brackenbury et al. (2018) suggest keeping humans in the loop besides automated information organisation approaches – which is in line with our position of involving end users – in order to mitigate some of the concerns. Our scope in the present work, however, was limited to representation of data and we evaluated content consumers’ ability to interpret and make inferences on instance-based data. Implementati on, data cleaning and integration of schema-free (or instance-based) data are beyond our scope.

On a larger scale, the study of users’ ability to perform tasks on complex databases (whether instancebased or class-based) is an interesting research question. Users will be challenged to find the required information in an instance-based database with thousands of attributes or, similarly, in a class-based database with hundreds of classes. Despite the challenge, users need to identify the few attributes that are required to answer a certain question in an information retrieval task; thus, they may not need to use all the attributes available (possibly a large number). Locating attributes within a complex classification structure might be more dificult than when attributes are presented in a large list as in an instance-based data representation. In other words, we argue that in any database application, there might be a great number of classes. Users need to be able to locate the attributes of interest in the database. In a class-based database, the attributes are already partitioned into classes by a database designer whose point of view might or might not fit with what a user is looking for. With instance-based data, users can partition the data based on the attributes of interest to them.

As for databases of smaller scale, our experiment demonstrated that users of instance-based data representations achieved better performance in retrieval of information compared with class-based users.

## 8. Implications and summary

## 8.1. Theoretical and practical implications

This study investigates the ability of information consumers to query and explore instance-based data efectively. Support for the research hypotheses provides empirical evidence that users of instance-based data can achieve higher efective use than comparable users of class-based data in retrieving information (or query formulation) as well as information exploration and discovery of knowledge.

Our focus is strictly on representation of data, and we posit that efective information management increasingly relies on understanding data in contexts other than those for which the data were originally collected. This need is particularly evident with the recent emergence of phenomena such as “open data,” which emphasises a desire to make data freely available for (re)use by anyone (Gurstein, 2011), or free online data sources such as data.world<sup>19</sup> and Kaggle.<sup>20</sup> Under these situations, anticipating all potential users requirements, as well as possible applications of the data, is next to impossible. More speci

fically, this repurposing of data marks a significant departure from traditional ways in which information was collected and used within organisations. It particularly suggests the need to provide flexibility in representing da

ta to accommodate new and unanticipated uses of information. It follows that a predefined structure might not be helpful if new needs or new sources of data emerge, es

pecially when such additional applications do not adhe re to an existing schema or structure. Classification sche

mes that reflect the original stakeholders’ view of the wor

ld may not match the emerging applications that arise over time.

Delegating the task of information analysis and business intelligence to non-technical business users has gained traction in industry (Imhof & White, 2011). The current research is the first empirical study that focuses on content consumers rather than database designers and implementers and their ability to explore and query instance-based data. By enabling users to have flexible and understandable ways to access data, they can benefit from data even when they do not fully understand how data are organised within the system. Considering the wealth of schema-free or instance-based data available (Bornea et al., 2017), studying human users’ ability to harness this information is timely.

Instance-based data can provide flexibility that is not aforded by traditional data representation methods. Alth ough there are many important use cases for classified data (e.g., transaction processing applications), for environments with new and emerging data analysis needs, or data sources that are going to be used for a variety of purp oses (some of which cannot be anticipated in advance), using instance-based data can be advantageous. More over, our focus is on representation of data, not storage. Within the scope of data presentation, however, governments and organisations that make their data available to the public can make these information assets more useful by freeing the data from pre-defined classification.

In our experiments, the tasks were designed based on the class-based schema – thus, they were more congruent with that approach. One could argue that subjects in the instance-based data group faced a disadvantage in having to work with the same questions – which were designed with classification in mind. However, even under these circumstances, the users of instance-based data were more accurate in formulating the queries and identified patterns of greater quality. This provides strong empirical evidence that the users of instance-based data can efectively formulate information requests (queries) and perform analytical reasoning. In addition, we designed our experiments with the goal of informational equivalence between the instance-based and the class-based representations. One might argue that despite our eforts, subjects in the class-based group had more information available to them about cardinalities and nature of relationships between entities. In case this additional information induces a bias, it would be against the subjects in the instance-based group. This even further emphasises the strength of our findings.

In short, the empirical evidence regarding the benefits of this approach can help justify the costs of restructuring the organisational databases, providing staf training, and devising the required security policies.

## 8.2. Research opportunities

We studied a schema-free representation rooted in the principles of instance-based data management. The instance-based model, as an alternative to traditional data management approaches, has been shown to be more flexible, providing agility in changing requirements (Parsons & Wand, 2013) and enabling generation of higher quality data by data contributors in open settings (Lukyanenko et al., 2014b; Lukyanenko et al., 2019b).

Future research could examine possible ways of clustering attributes that is needed to search and analyse a large instance-based data set. A class-based approach provides a form of clustering, but it is both predetermined and fixed. One interesting avenue of study would be to study the efectiveness of representations that focus on the uniqueness of instances (e.g., via their distinguishing attributes), but also recognise and represent known classes to which these instance have been assigned in the original data (see Eriksson et al., 2019).

Moreover, we realise that in the real world a major portion of professionals work in teams. Studying users working in groups is an interesting question that should be investigated in the future.

Our studies were done under the condition of informational equivalence between the instancebased and the class-based representation. Future research could also foc

us on facilities provided by the instance-based approach that are not achievable in the traditional class-based repre

sentations. Moreover, studying the interaction of database technology experts as well as application domain experts with instance-based data is worth investigating.

Finally, this study has focused on showing the potential for instance-based representations to produce improved performance by non-expert users in routine and exploratory data retrieval tasks. More work is needed to understand better both the potential of such representations, as well as the boundary conditions around their efectiveness. For example, where there is a need for a shared understanding among data users, class-based representations might provide a stable foundation for creating a common view and understanding of the data.

## 9. Summary and conclusion

Considering the rise of schema-less data in the information landscape, we investigated human users’ ability to use these sources of data efectively. We relied on the instance-based paradigm as the theoretical foundation to model data. Benefits of the instan

ce-based approach as an alternative to traditional cla ss-based data management were originally proposed by Parsons and Wand (2000).

Our theoretical model posits that the flexibility aforded by instances (versus classes) allows content consumers to use information based on their own schemas, rather than those supplied by a database designer. Also, the flexibility provided by the instancebased representation reduces the extent to which users anchor to an existing structure in the data when using it for information exploration or querying data. We tested our hypotheses in two experiments and provided the first empirical evidence of content consumers’ ability to use instance-based data in openended as well as closed-ended tasks. The work demonstrated content consumers’ superior performance in assimilating instance-based compared to class-based representations.

## Notes

1. Morton et al. (2014) propose a similar concept – data enthusiasts. Data enthusiasts are a growing group of users “who need to analyze the data, [however] these use rs are without formal training in data science” (p. 453).

2. However, there is a shift in the industry towards storing schema-less or instance-based data (Kraska, 2013), particularly for large-scale distributed data management systems (such as Hadoop). The idea of “schema later” can reduce impediments to consolidation of data from disparate databases (Britton et al., 2013). Hence, instance-based or non-classified data are more scalable and less complex for data analytics applications (Marz & Warren, 2015). We consider these an added “bonus”, although data storage considerations are beyond the scope of our work.

3. We do not claim that this is the only, or even the best, way to model instances. We claim only that it is faithful to instance-based principles. Lukyanenko et al. (2019a) address the issue of whether an instancebased modelling grammar is needed and what requirements it should satisfy. Moreover, Eriksson et al. (2019) suggest the value of alternative representations that accommodate both instances and classes.

4. Our representation does not just remove the entity type label (e.g., “Client” as the label of an entity type in the classification scheme), but also removes the predefined and fixed structure imposed by classification.

5. We do realise that even with the finest and mostdetailed reasoning axioms, one could find exceptions and counter examples (e.g., an animal that gives birth to live young is a mammal, but one could think of duck-billed platypus as a mammal that lays eggs rather than give birth). As with other design decisions, there are always practical constraints, and despite considering possibility of exceptions to the inference rules, we decided to keep the axioms relatively simple.

6. http://aisnet.org/news/news.asp?id = 207,282 accessed on 22/06/2020.

7. In both experiments, the average of our subjects’ selfreported level of database knowledge was less than three (2.8–2.96) on a seven-point Likert scale. Thus, we believe that our subjects can also be considered non-experts in databases. Note that we used two separate pools of subjects for the two experiments.

8. https://www.tableau.com

9. Training material was edited from Tableau’s video tutorials (https://www.tableau.com/learn/training/- accessed on 01/07/2020)

10. Our subjects were undergraduate commerce students taking the secondary Business Technology Management (BTM) course out of the required six courses (with two electives) to major in BTM. The first course (mandatory for all commerce students) was a hands-on class that taught them Excel and Stata. The students who take the second BTM course, are typically 60–65% accounting students, 25% BTM, and the rest are from diferent majors (e.g., marketing, operations, finance) who take the course as an elective (in their third or fourth year). The BTM students in our subject pool had not received any more education in technology or information systems concepts than the students in accounting. We cannot claim that our subjects were surrogates of every type of business user out in the real world. What we are saying is that our subjects’ level of knowledge is (at best) on par with accountants or business analysts that work at major professional services firms.

11. Using the same precision measures as in the main experiment (H1b – discussed later), we calculated efect size from the pilot, which was Cohen’s d = 0.77. Based on the desired statistical a priori power level of 0.8 (which is considered high), the minimum total sample size would be 44. Owing to limitations in recruiting, we conducted the analysis based on data from 42 subjects. Posthoc power was 0.64, which is considered to be of medium strength.

12. To test the assumptions of t-test we performed Levene’s test, which was not statistically significant for the number of statements (p = 0.065), thus we assumed homogeneity of variances between the two experimental conditions.

13. This comparison is justified due to having a normal distribution of data, and homogeneity of variances.

14. We did not perform statistical significance tests on this measure as calculating mean and standard deviation on the number of unique statements by each subject was not warranted. From subject’s point of view, every statement they reported was unique (and they had no idea of the patterns identified by others), and reporting unique statements was not an objective of the experimental task

15. For example, multiple subjects in each group reported that the majority of employee base were female. We excluded repetitions of similar patterns, and only provided sets of unique observations by subjects from each group (instancebased vs. class-based) to our judges.

16. The judges were cognisant that outliers, regardless however small in magnitude, could reflect valuable information. One pattern that both judges found interesting stated that a particular employee had significantly longer call durations compared to other employees. This observation is related to one out of 10,000 employees, but could be of material importance.

17. Following Hallgren’s (2012) guidelines regarding inter-rater reliability measures, Cohen’s kappa is more appropriate for nominal variables, while intra-class correlation (ICC) is better suited for ordinal and interval variables. Since our performance scores (discussed later) are calculated on 0.25 increments from 0–4, we consider them interval variables – hence, our selection of ICC to measure inter-rater reliability.

18. Since assumption of sphericity was rejected in our repeated measures ANOVA model, we used Greenhouse-Geisser’s correction to interpret the data. To test the assumptions of homogeneity of variances we performed Levene’s test, which was not statistically significant for either the travel agency (p = 0.538) or for the consulting case (p = 0.442).

19. https://data.world – accessed on 18/11/2020 – is a portal for sharing open data and collaborating on data-driven projects.

20. https://www.kaggle.com – accessed on 18/11/2020 – is a Google subsidiary that hosts data related to machine learning and predictive modelling competitions.

## Acknowledgments

This research was partially supported by grants from The Natural Sciences and Engineering Research Council of Canada (NSERC) and The Social Sciences and Humanities Research Council of Canada (SSHRC).

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Arash Saghafi http://orcid.org/0000-0002-5906-8400 Jefrey Parsons http://orcid.org/0000-0002-4819-2801

## References

Allen, G., & Parsons, J. (2010). Is query reuse potentially harmful? Anchoring and adjustment in adapting existing database queries. Information Systems Research, 21(1), 56–77. https://doi.org/10.1287/isre.1080.0189

Alpar, P., & Schulz, M. (2016). Self-service business intelligence. Business & Information Systems Engineering, 58(2), 151–155. https://doi.org/10.1007/s12599-016-0424-6

Bera, P., Burton-Jones, A., & Wand, Y. (2011). Guidelines for designing visual ontologies to support knowledge identification. MIS Quarterly, 35(4), 883. https://doi.org/ 10.2307/41409965

Bera, P., & Poels, G. (2019). How quickly do we learn conceptual models? European Journal of Information Systems, 28(6), 663–680. https://doi.org/10.1080/ 0960085X.2019.1673972

Bodart, F., Patel, A., Sim, M., & Weber, R. (2001). Should optional properties be used in conceptual modelling? A theory and three empirical tests.”. Information Systems Research, 12(4), 384–405. https://doi.org/10.1287/isre.12.4. 384.9702

Bornea, M. A., Dolby, J., Fokoue-Nkoutche, A. B., Kementsietsidis, A., & Srinivas, K., International Business Machines Corp, (2017). Optimizing sparse schema-less data in data stores. U.S. Patent 9,715,560.

Brackenbury, W., Liu, R., Mondal, M., Elmore, A. J., Ur, B., Chard, K., & Franklin, M. J. (2018, June). Draining the data swamp: A similarity-based approach. In Proceedings of the workshop on human-in-the-loop data analytics (pp. 1–7).

Britton, C. P., Kumar, A., Bigwood, D., DeFusco, A. J., & Greenblatt, H., OBJECTSTORE Inc, (2013). Methods and apparatus for querying a relational data store using schema-less queries. U.S. Patent 8,412,720.

Brown, B., Chui, M., & Manyika, J. (2011). Are you ready for the era of ‘big data’? McKinsey Quarterly, 4(October), 24–35. https://www.mckinsey.com/business-functions/ strategy-and-corporate-finance/our-insights/are-youready-for-the-era-of-big-data

Browne, G. J., & Parsons, J. (2012). More enduring questions in cognitive IS research. Journal of the Association for Information Systems, 13(12), 1000–1011. https://doi. org/10.17705/1iais.00318

Buckland, M., & Gey, F. (1994). The relationship between recall and precision. Journal of the American Society for Information Science, 45(1), 12–19. https://doi.org/10.1002/ (SICI)1097-4571(199401)45:1<12::AID-ASI2>3.0.CO;2-L

Bunge, M. (1977). Treatise on basic philosophy: Ontology I: The furniture of the world (Vol. 1). Springer.

Burton-Jones, A., & Grange, C. (2012). From use to efective use: A representation theory perspective. Information Systems Research, 24(3), 632–658. https://doi.org/10. 1287/isre.1120.0444

Burton-Jones, A., & Meso, P. N. (2006). Conceptualizing systems for understanding: An empirical test of decomposition principles in object-oriented analysis. Information Systems Research, 17(1), 38–60. https://doi. org/10.1287/isre.1050.0079

Calder, B. J., Phillips, L. W., & Tybout, A. M. (1981). Designing research for application. Journal of Consumer Research, 8(2), 197–207. https://doi.org/10. 1086/208856

Cassidy, S., Perrett, J., & Simons, C. (2018). Beneficial role of humans and AI in a machine learning age of the Telco ecosystem. In: TM Forum Digital Transformation World, Nice, France, Retrieved May 14–16, 2018, from http:/ eprints.uwe.ac.uk/36328

Compeau, D., Marcolin, B., Kelley, H., & Higgins, C. (2012). Research commentary-generalizability of information systems research using student subjects-a reflection on our practices and recommendations for future research. Information Systems Research, 23(4), 1093–1109. https:/ doi.org/10.1287/isre.1120.0423

Corbett, J. C., Dean, J., Epstein, M., Fikes, A., Frost, C., Furman, J. J., Hsieh, W., Heiser, C., Hochschild, P., Hsieh, W., Kanthak, S., Kogan, E., Li, H., Lloyd, A., Melnik, S., Mwaura, D., Nagle, D., Quinlan, S., Rao, R., Woodford, D., & Ghemawat, S. (2013). Spanner: Google’s globally distributed database. ACM Transactions on Computer Systems (TOCS), 31(3), 1–22. https://doi.org 10.1145/2491245

Derry, S. J. (1996). Cognitive schema theory in the constructivist debate. Educational Psychologist, 31(3–4), 163–174.

Elmasri, R., & Navathe, S. B. N. (2011). Database systems: Models, languages, design, and application programming. Pearson.

Eriksson, O., Johannesson, P., & Bergholtz, M. (2019). The case for classes and instances-a response to representing instances: The case for reengineering conceptual modelling grammars. European Journal of Information Systems, 28(6), 681–693. https://doi.org/10.1080/0960085X.2019. 1673672

Fishbach, A., & Ferguson, M. J. (2007). The goal construct in social psychology.In A. W. Kruglanski & E. T. Higgins (Eds.), Social psychology: Handbook of basic principles (pp. 490–515).

Ford, N. (2004). Modeling cognitive processes in information seeking: From popper to pask. Journal of the American Society for Information Science and Technology, 55(9), 769–782. https://doi.org/10.1002/asi.20021

Gemino, A., & Wand, Y. (2005). Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data & Knowledge Engineering, 55(3), 301–326. https://doi.org/10.1016/j. datak.2004.12.009

Geng, L., & Hamilton, H. J. (2006). Interestingness measures for data mining: A survey. ACM Computing Surveys (CSUR, 38 (3), 9. https://doi.org/10.1145/1132960.1132963

Gillies, M., Fiebrink, R., Tanaka, A., Garcia, J., Bevilacqua, F., Heloir, A., & d’Alessandro, N. (2016, May). Human-centred machine learning. In Proceedings of the 2016 CHI conference extended abstracts on human factors in computing systems (pp. 3558–3565).

Graves, A., & Hendler, J., (2013). Visualization tools for open government data, ACM. In Proceedings of the 14th annual international conference on digital government research (pp. 136–145)

Gupta, A., & Jain, R. (1997). Visual information retrieval. Communications of the ACM, 40(5), 70–79. https://doi. org/10.1145/253769.253798

Gurstein, M. (2011). Open Data: Empowering the empowered or efective data use for everyone? First Monday, 16(2). https://firstmonday.org/article/view/3316/2764

Hallgren, K. A. (2012). Computing inter-rater reliability for observational data: An overview and tutorial. Tutorials in Quantitative Methods for Psychology, 8(1), 23–34. https:// doi.org/10.20982/tqmp.08.1.p023

Hills, T. (2016). NoSQL and SQL data modeling: Bringing together data, semantics, and software. Technics Publications.

Imhof, C., & White, C., (2011). Self-service business intelligence, empowering users to generate insight. TDWI best practice report, TWDI, Renton, WA. TDWI Research.

Klyne, G., & Carroll, J. J. (2006). Resource description framework (RDF): Concepts and abstract syntax. http://www. w3.org/TR/rdf-concepts/

Kraska, T. (2013). Finding the needle in the big data systems haystack. IEEE Internet Computing, 17(1), 84–86. https:// doi.org/10.1109/MIC.2013.10

Lakof, G. (1987). Women, fire, and dangerous things. What categories reveal about the mind. Chicago (Vol. 1). The University of Chicago Press.

Lukyanenko, R., Evermann, J., & Parsons, J., (2014a). Instantiation validity in IS design research. Proceedings of the international conference on design Science research in information systems (pp. 321–328). Springer Internationa Publishing.

Lukyanenko, R., Evermann, J., & Parsons, J., (2015). Guidelines for establishing instantiation validity in IT artifacts: A survey of IS research. Proceedings of the international conference on design science research in information systems (pp. 430–438). Springer International Publishing.

Lukyanenko, R., Parsons, J., & Samuel, B. M. (2019a). Representing instances: The case for reengineering conceptual modelling grammars. European Journal of Information Systems, 28(1), 68–90. https://doi.org/10. 1080/0960085X.2018.1488567

Lukyanenko, R., Parsons, J., & Wiersma, Y. (2014b). The IQ of the crowd: Understanding and improving information quality in structured user-generated content. Information Systems Research, 25(4), 669–689. https://doi.org/10. 1287/isre.2014.0537

Lukyanenko, R., Parsons, J., Wiersma, Y., & Maddah, M. (2019b. Expecting the unexpected: Efects of data collection design choices on the quality of crowdsourced user-generated content. MIS Quarterly, 43(2), 623–647. https://doi.org/10.25300/MISQ/2019/14439

March, J. G. (1991). Exploration and exploitation in organizational learning. Organization Science, 2(1), 71–87. https://doi.org/10.1287/orsc.2.1.71

Marz, N., & Warren, J. (2015). Big Data: Principles and best practices of scalable realtime data systems. Manning Publications Co.

McGarry, K. (2005). A survey of interestingness measures for knowledge discovery. The Knowledge Engineering Review, 20(1), 39–61. https://doi.org/10.1017/ S0269888905000408

Miller, S., & Hughes, D., (2017). The Quant Crunch: How the demand for data science skills is disrupting the job market.

Burning Glass Technologies. https://www-01.ibm.com common/ssi/cgi-bin/ssialias?htmlfid=IML14576USEN

Mortier, R., Haddadi, H., Henderson, T., McAuley, D., Crowcroft, J., & Crabtree, A. (2020). Human-data interaction

Morton, K., Balazinska, M., Grossman, D., & Mackinlay, J. (2014). Support the data enthusiast: Challenges for next-generation data-analysis systems. Proceedings of the VLDB Endowment, 7(6), 453–456. https://doi.org/10. 14778/2732279.2732282

Munzner, T. (2014). Visualization analysis and design. CRC press.

Newell, A., & Simon, H. A. (1972). Human problem solving (Vols. 104, No. 9). Prentice-Hall.

Nielsen, J. (2006). The 90-9-1 rule for participation inequality in social media and online communities. Nielsen Norman Group.

Ogden, W. C. (1986). Implications of a cognitive model of database query: Comparison of a natural language, formal language and direct manipulation interface. ACM SIGCHI Bulletin, 18(2), 51–54. https://doi.org/10.1145/15683. 1044078

Parsons, J. (2002). Efects of local versus global schema diagrams on verification and communication in conceptual data modeling. Journal of Management Information Systems, 19(3), 155–183.

Parsons, J., & Saunders, C. (2004). Cognitive heuristics in software engineering applying and extending anchoring and adjustment to artifact reuse. Software Engineering, IEEE Transactions On, 30(12), 873–888. https://doi.org 10.1109/TSE.2004.94

Parsons, J., & Wand, Y. (2000). Emancipating instances from the tyranny of classes in information modeling. ACM Transactions on Database Systems (TODS, 25(2), 228–268. https://doi.org/10.1145/357775.357778

Parsons, J., & Wand, Y. (2008a). A question of class. Nature, 455(7216), 1040–1041. https://doi.org/10.1038 4551040a

Parsons, J., & Wand, Y. (2008b). Using cognitive principles to guide classification in information systems modeling. MIS Quarterly, 32(4), 839–868. https://doi.org/10.2307 25148874

Parsons, J., & Wand, Y. (2013). Cognitive principles to support information requirements agility. In Advanced information systems engineering workshops (pp. 192–197). Springer Berlin Heidelberg.

Parvanta, C., Roth, Y., & Keller, H. (2013). Crowdsourcing 101: A few basics to make you the leader of the pack. Health Promotion Practice, 14(2), 163–167. https://doi.org/10.1177/1524839912470654

Poels, G. (2011). Understanding business domain models: The efect of recognizing resource-event-agent conceptual modeling structures. Journal of Database Management (JDM), 22(1), 69–101. https://doi.org/10. 4018/jdm.2011010104

Poels, G., Maes, A., Gailly, F., & Paemeleire, R. (2011). The pragmatic quality of resources-events-agents diagrams: An experimental evaluation. Information Systems Journal, 21(1), 63–89. https://doi.org/10.1111/j.1365-2575.2007.00253.x

Rai, A. (2016). Editor’s comments: Synergies between big data and theory. MIS Quarterly, 40(2), iii–ix.

Sweller, J., & Chandler, P. (1994). Why some material is dificult to learn. Cognition and Instruction, 12(3), 185–233. https://doi.org/10.1207/s1532690xci1203\_1

Thomas, J. J., & Cook, K. A. (2006). A visual analytics agenda. Computer Graphics and Applications, IEEE, 26 (1), 10–13. https://doi.org/10.1109/MCG.2006.5

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. science, 185(4157), 1124–1131. https://doi.org/10.1126/science.185.4157.1124

Van Gils, B. (2020). Data Management: A gentle introduction: Balancing theory and practice. Van Haren.

Van Mierlo, T. (2014). The 1% rule in four digital health social networks: An observational study. Journal of Medical Internet Research, 16(2), e33. https://doi.org/10. 2196/jmir.2966

Vicknair, C., Macias, M., Zhao, Z., Nan, X., Chen, Y., & Wilkins, D. (2010). A comparison of a graph database and a relational database: A data provenance perspective. In Proceedings of the 48th annual Southeast regional conference (pp. 42). ACM.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems analysis and design grammars. Information Systems Journal, 3(4), 217–237. https://doi.org/10.1111/j.1365-2575.1993.tb00127.x

Zhu, Y., Yan, E., & Song, I. Y. (2017). The use of a graph based system to improve bibliographic information retrieval: System design, implementation, and evaluation. Journal of the Association for Information Science and Technology, 68(2), 480–490. https://doi.org/10.1002/asi.23677

Zikopoulos, P., & Eaton, C. (2011). Understanding big data: Analytics for enterprise class hadoop and streaming data. McGraw-Hill Osborne Media.

Appendices

Appendix A. Experimental Material

Appendix A1. Pre-experiment Questionnaire

Pre-experiment questionnaire

<table><tr><td colspan="5">Have you ever written queries using a database management system?</td></tr><tr><td>a) Yes</td><td colspan="4">b) No</td></tr><tr><td colspan="5">Compared to an average database user, I would rate my level of experience in database usage as:</td></tr><tr><td>1) Very low</td><td>2) Low</td><td>3) Somewhat low4) Neither low nor high5) Somewhat high</td><td>6) High</td><td>7) Very High</td></tr><tr><td colspan="5">Compared to a regular traveller, I would rate my level of knowledge of activities in arranging trips as:</td></tr><tr><td>1) Very low</td><td>2) Low</td><td>3) Somewhat low4) Neither low nor high5) Somewhat high</td><td>6) High</td><td>7) Very High</td></tr><tr><td colspan="5">Compared to someone who works in a consulting firm, I would rate my level of project management knowledge as:</td></tr><tr><td>1) Very low</td><td>2) Low</td><td>3) Somewhat low4) Neither low nor high5) Somewhat high</td><td>6) High</td><td>7) Very High</td></tr></table>

## Appendix A2. Experiment I Material

## Human Resource Data

Case Description and Task:

ACME Corporation has provided data about personal information of their employees, their performance record, travel and phone records, and Internet access logs. Your challenge is to report patterns that might be worth investigating further by the stakeholders of the company.

For the purpose of this task a pattern is a consistent and recurring characteristic or trait that helps in the identification of a phenomenon or problem.

Schema of ACME:

Material for the Control Group:

Material for the Treatment Group: Data is not bound to any structure. List of properties relevant in the domain:

## Appendix A3. Experiment II Material

Travel Agency Domain

Description: In this hypothetical domain, customers of the travel agency plan trips with the help of travel agents. The travel agency acts as an intermediary between customers and service providers (airlines, train services, etc.). The trave agents create itineraries for customers with respect to their preferences. The agent would need to collect information

![](/api/attachments/F72WQR79/fulltext/images/3b7e0d598513308fa7dfb2e1ba29e2fd3f80aeaf75be6815d738799007d47b20.jpg)  
Figure 5. Schema of ACME:

<table><tr><td>Property</td><td>Description</td></tr><tr><td>Action</td><td>Action taken in accordance to an employee&#x27;s performance</td></tr><tr><td>Address</td><td></td></tr><tr><td>Airline</td><td></td></tr><tr><td>Area Code</td><td></td></tr><tr><td>Arrival City</td><td></td></tr><tr><td>Arrival Date</td><td></td></tr><tr><td>Arrival Time</td><td></td></tr><tr><td>Birth Country</td><td></td></tr><tr><td>Birth Date</td><td></td></tr><tr><td>Business Cell</td><td></td></tr><tr><td>Business Email</td><td></td></tr><tr><td>Business Phone</td><td></td></tr><tr><td>Caller Name</td><td></td></tr><tr><td>Citizen Country</td><td>A two-letter code identifying one&#x27;s citizenship</td></tr><tr><td>Citizen Status</td><td>Country of citizenship</td></tr><tr><td>City</td><td></td></tr><tr><td>Country</td><td></td></tr><tr><td>Date and Time</td><td>Date and time of accessing servers</td></tr><tr><td>Department</td><td></td></tr><tr><td>Departure City</td><td></td></tr><tr><td>Departure Date</td><td></td></tr><tr><td>Departure Time</td><td></td></tr><tr><td>Destination</td><td>Destination country of a phone call</td></tr><tr><td>Destination No.</td><td>Destination number of a phone call</td></tr><tr><td>Domain</td><td>Domain name of local servers</td></tr><tr><td>Duration</td><td>Duration of a phone call</td></tr><tr><td>Effective</td><td>Effective date for an executive decision (e.g., promotion)</td></tr><tr><td>Employee ID</td><td></td></tr><tr><td>Fax</td><td></td></tr><tr><td>First Name</td><td></td></tr><tr><td>Flight Number</td><td></td></tr><tr><td>Gender</td><td></td></tr><tr><td>Host IP</td><td>IP address of a web host</td></tr><tr><td>Host Name</td><td>Name of a web host</td></tr><tr><td>In/Out</td><td>Incoming or outgoing call</td></tr><tr><td>Job Code</td><td>A four-character code assigned to a position</td></tr><tr><td>Last Name</td><td></td></tr><tr><td>Loc. Area Code</td><td>A four-character code assigned to a location</td></tr><tr><td>Marital Status</td><td></td></tr><tr><td>Name</td><td></td></tr><tr><td>NTID</td><td>Network ID assigned to users (a la username)</td></tr><tr><td>Personal Cell</td><td></td></tr><tr><td>Personal Email</td><td></td></tr><tr><td>Reason</td><td>Reason for an executive decision</td></tr><tr><td>Region</td><td></td></tr><tr><td>Source</td><td>Source country of a phone call</td></tr><tr><td>Source Number</td><td>Source number of a phone call</td></tr><tr><td>ST</td><td>State</td></tr><tr><td>Start Date</td><td>Date of employment</td></tr><tr><td>Status</td><td>Employment status (e.g., active)</td></tr><tr><td>Time</td><td></td></tr><tr><td>Zip Code</td><td></td></tr></table>

![](/api/attachments/F72WQR79/fulltext/images/08416e955cc42d0a9a451548b307ebb05db937409ddf90840a53891e7267c64a.jpg)  
Figure 6. The material for the control group included a general schema and actual data.

<table><tr><td colspan="2">Customers with Additional Considerations</td></tr><tr><td>Customer_ID</td><td>Allergy Type</td></tr><tr><td>545</td><td>Nuts</td></tr><tr><td>....</td><td></td></tr></table>

<table><tr><td colspan="5">Customers</td></tr><tr><td>Customer_ID</td><td>Name</td><td>Preference</td><td>Payment Info</td><td>Address</td></tr><tr><td>206</td><td>Jennifer Nelson</td><td>Aisle</td><td>6470**********</td><td>848, Sutton Ave.</td></tr><tr><td>545</td><td>Jason Lee</td><td>[Null]</td><td>3644**********</td><td>94, Arlington</td></tr><tr><td>....</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="5">Travel Agent</td></tr><tr><td>Agent_ID</td><td>Name</td><td>Phone No.</td><td>Office Number</td><td>Address</td></tr><tr><td>A455</td><td>Harry Miller</td><td>555-223-2545</td><td>125</td><td>48, Pine Str</td></tr><tr><td>A890</td><td>Amanda Chung</td><td>555-593-2955</td><td>142</td><td>108, Cambie</td></tr><tr><td>....</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="4">Service Provider</td></tr><tr><td>Service Provider_ID</td><td>Name</td><td>Service Type</td><td>Webpage</td></tr><tr><td>S9421</td><td>Air Canada</td><td>Airline</td><td>aircanada.com</td></tr><tr><td>S1124</td><td>RyanAir</td><td>Airline</td><td>ryanair.com</td></tr><tr><td>S232</td><td>Virgin Trains</td><td>Train</td><td>virgintrains.co.uk</td></tr><tr><td>...</td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="5">Itinerary</td></tr><tr><td>Itinerary_No</td><td>Price</td><td>Agent_ID</td><td>Customer_ID</td><td>Confirmation Date</td></tr><tr><td>CD22</td><td>$1750</td><td>A455</td><td>206</td><td>13/09/2014</td></tr><tr><td>AE19</td><td>$70</td><td>A890</td><td>848</td><td>09/08/2014</td></tr><tr><td>....</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="7">Itinerary Detail</td></tr><tr><td>Itinerary_No</td><td>Service Provider_ID</td><td>Departure Date</td><td>Return Date</td><td>To</td><td>From</td><td>Internal Price</td></tr><tr><td>CD22</td><td>S9421</td><td>10/10/2014</td><td>20/10/2014</td><td>London</td><td>Vancouver</td><td>$1400</td></tr><tr><td>AE19</td><td>S1124</td><td>04/11/2012</td><td>09/11/2012</td><td>Sheffield</td><td>Liverpool</td><td>$50</td></tr><tr><td>CD22</td><td>S232</td><td>10/10/2014</td><td>20/10/2014</td><td>Manchester</td><td>London</td><td>$100</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Figure 7. Travel agency domain, control group general schema

![](/api/attachments/F72WQR79/fulltext/images/7f61e2d0dcbfc45d28cb1725055a0e88f71aba1c292d1632cd8eaa9ad2aa6ebf.jpg)  
Figure 8. The material for the treatment group includes a general schema and actual data.

![](/api/attachments/F72WQR79/fulltext/images/68d29058c97356699085ad750781f71be16ba9379428f65b8276b4431f04aae4.jpg)  
Figure 9. The material for the treatment group includes a general schema and actual data.Travel agency domain, treatment group general structure

regarding customers’ payment information and, in some cases, if there are special considerations such as allergies.

The itinerary information is shared between the service providers, terminals, and travel agencies; it includes information such as travel locations (to and from), dates, and price.

Material for the control and treatment groups

The material for the control group included a general schema and actual data.

Travel agency domain, control group general schema Travel agency domain, control group actual data

The material for the treatment group includes a general schema and actual data.

Travel agency domain, treatment group general structure Travel agency domain, treatment group actual data

Questions (both Control and Treatment)

Travel Agency Domain

1. Jennifer Nelson, one of the customers, called the agency and asked for a change in her itinerary. She is currently booked to fly on October 10 to England, but she needs to postpone the departure date to October 12. Please describe the procedure (i.e., changes of information) to fulfill Jennifer’s request.

2. Canada Border Services has asked the agency to identify all trips facilitated by two diferent types of service providers (e.g., a trip that half of it is with a train and the second half with an airplane). Describe the procedure for retrieving that information.

![](/api/attachments/F72WQR79/fulltext/images/cf3a7f9ebc89ae3b28bc71f0bf54c7b6ce21fba51c0da4f3809d5bc6c07e4526.jpg)  
Figure 10. Travel agency domain, treatment group actual data

<table><tr><td colspan="5">Client</td></tr><tr><td>Client_ID</td><td>Name</td><td>Division_ID</td><td>Description</td><td>Address</td></tr><tr><td>C9292</td><td>EZLink</td><td>404</td><td>Social Network</td><td>1111, Pine Str.</td></tr><tr><td>C1015</td><td>Braden Schwartz</td><td>599</td><td>[Null]</td><td>75, Delta Road</td></tr><tr><td>......</td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="2">Corporate Client</td></tr><tr><td>Client_ID</td><td>Corporate Account No</td></tr><tr><td>C9292</td><td>C53D</td></tr><tr><td>....</td><td></td></tr></table>

<table><tr><td colspan="3">Division</td></tr><tr><td>Division ID</td><td>Name</td><td>Address</td></tr><tr><td>404</td><td>SimPro Vancouver</td><td>55, Georgia Str.</td></tr><tr><td>599</td><td>SimPro Seattle</td><td>129, Pike Ave</td></tr><tr><td>....</td><td></td><td></td></tr></table>

<table><tr><td colspan="8">Project</td></tr><tr><td>Project_ID</td><td>Client_ID</td><td>Division_ID</td><td>Description</td><td>Budget</td><td>Start Date</td><td>End Date</td><td>ProjectManager ID</td></tr><tr><td>P111</td><td>C9292</td><td>404</td><td>Market Research</td><td>$20,000</td><td>01/03/2014</td><td>20/03/2014</td><td>E678</td></tr><tr><td>P1040</td><td>C1015</td><td>599</td><td>Intellectual Property Evaluation</td><td>$3,000</td><td>15/09/2014</td><td>20/09/2014</td><td>[Null]</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="7">Employee</td></tr><tr><td>Employee ID</td><td>Name</td><td>Division ID</td><td>Project ID</td><td>Email</td><td>Password</td><td>Employment Date</td></tr><tr><td>E678</td><td>Luna Diez</td><td>404</td><td>P111</td><td>diez@***</td><td>**********</td><td>01/09/2005</td></tr><tr><td>E333</td><td>Edward McKay</td><td>404</td><td>P111</td><td>mckay@***</td><td>**********</td><td>15/03/2011</td></tr><tr><td>E915</td><td>Sarah Jacobs</td><td>599</td><td>P1040</td><td>sarahj@***</td><td>**********</td><td>01/01/2009</td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td colspan="4">TimeSheet</td></tr><tr><td>TimeSheet ID</td><td>Employee ID</td><td>Project ID</td><td>WorkHours</td></tr><tr><td>T121</td><td>E333</td><td>P111</td><td>84</td></tr><tr><td>T195</td><td>E678</td><td>P111</td><td>120</td></tr><tr><td>T593</td><td>E561</td><td>P489</td><td>33</td></tr><tr><td>...</td><td></td><td></td><td></td></tr></table>

Figure 11. Consulting firm domain, control group actual data

![](/api/attachments/F72WQR79/fulltext/images/e5024dcb19f0bcfd26c94a485d4849a5b6094b5fa040a7fe774bd0c2e7c12336.jpg)

<table><tr><td>List of Properties</td></tr><tr><td>Name</td></tr><tr><td>Address</td></tr><tr><td>Email</td></tr><tr><td>Password</td></tr><tr><td>Description</td></tr><tr><td>Preference</td></tr><tr><td>Work Hours</td></tr><tr><td>Project Name</td></tr><tr><td>Manager (True/False)</td></tr><tr><td>Budget</td></tr><tr><td>Start Date</td></tr><tr><td>End Date</td></tr><tr><td>Corporate Account No</td></tr></table>

Figure 12. Consulting firm domain, treatment group general structure  
![](/api/attachments/F72WQR79/fulltext/images/f7cec1c169b512bd60a0b395311d24446935da4e7969a61dfa2e70f44d67606b.jpg)  
Figure 13. Consulting firm domain, treatment group actual data

![](/api/attachments/F72WQR79/fulltext/images/62faaa1794f9113a8e6714e9e662da989991ab75d50aecafe78ba7c8411267ed.jpg)  
Figure 14. Consulting firm domain, treatment group actual data

3. The manager wants to allocate commissions earned by one of the agents (named Harry Miller) at the end of the month. Describe the procedure for evaluating an agent’s monthly sales performance (e.g., in January 2014).

4. Air Canada needs a list of all passengers (flying with Air Canada) that have some sort of allergies. Describe the procedure for generating that list.

Consulting Firm Domain

Description: SimPro is a multi-national consulting firm with various divisions all over North America. Each division is responsible for delivering projects defined by their diverse range of clients (from individuals to corporations).

The projects are completed and managed by firm employees within each division. For each project, the company keeps track of budget, start and end date, as well as information about the project’s owner (i.e., client) and manager (i.e., one of the employees).

Employees need to be involved with a project at any given time. Their performance is evaluated using a timesheet, which stores the number of hours that they worked on a project.

Material for the Control and Treatment Groups

The material for the control group included a general schema and actual data.

Consulting firm domain, control group general schema Consulting firm domain, control group actual data

Consulting firm domain, treatment group general structure Consulting firm domain, treatment group actual data

Questions (for both Control and Treatment)

1. Edward McKay, one of the employees, has asked for overtime pay for his efort in completing the market research project for the EZLink company. Describe the procedure to identify the average hours worked per day by Edward on the market research project – for the sake of simplicity, weekends and holidays are also included.

2. The headquarters wants to identify the clients that have worked with two or more divisions of SimPro. Please describe the procedure to identify such clients.

3. The manager assigned to the auditing project of Vancou

ver Canucks has left the firm. The managing partner at the firm has decided to remove Edward from the current project that he is involved with, and assign him as the project manager of the Canucks’ audit. Describe the procedure for performing this task.

4. Headquarter also wants to identify SimPro divisions that serve clients that are individuals (not corporations). Please describe the process to identify those divisions.

## Appendix B. Answer Keys

This Appendix gives the answer keys to Experiment II. Note that the questions are abbreviated to save space in both Tables B1 and B2.

Table B1. Answer key to travel agency case.

<table><tr><td>Control (class-based)</td><td>Treatment (instance-based)</td></tr><tr><td>Q1. Describe the procedure required for helping a client postpone her departure date.(a) Look up Jennifer Nelson’s “Customer_ID” from the customer table.(b) Access Jennifer’s itinerary from the “Itinerary” table, by searching for her “Customer_ID” (i.e., foreign key).(c) Using the “Itinerary_No” found in step b, find the “Departure Date” field in the “Itinerary_Details” table – the current value should be October 10.(d) Change the “Departure Date” on Jennifer’s itinerary to October 12.</td><td>(a) Locate the thing that has the “Name” property with the value of “Jennifer Nelson”.(b) Look up the “Travels With” link that originates from the thing representing “Jennifer Nelson”. This link should have “October 10” as the value for “Departure Date” property.(c) Considering the available dates on the service provider’s website, a new “Departure Date” will be set (e.g., October 12).</td></tr><tr><td>Q2. Describe the procedure for identifying trips that are facilitated by two different types of service providers (e.g., train and airplane).(a) In the Itinerary_Details table, locate entries with repeated itinerary numbers.(b) Look up the service providers that facilitate the trip (i.e., refer to the Service Provider table and look up the same ServiceProvider_ID from Itinerary_Detail).(c) For itineraries facilitated by more than one provider, display the records in which the Service Types are distinct from each other.</td><td>(a) Locate all the “Travels With” links that have the same “Itinerary_No”.(b) Go to the thing connected to the aforementioned links (i.e., the end of the link).(c) Short list the ones that have different values for the “Service Type” property (two service providers that are both “Airlines” are not considered different).(d) Display the “Itinerary_No” of the links that satisfied the conditions in a and b.</td></tr><tr><td>Q3. Describe the procedure for evaluating an agents’ monthly sales performance (01/2014).(a) Look up Harry Miller’s “Agent_ID” from the “Agent” table.(b) In the “Itinerary” table, list all the records that have Harry’s “Agent_ID” (i.e., foreign key) as one of their fields.(c) Select the itineraries with the confirmation dates within 01/01/2014 and 31/01/2014. Then, add up the prices of each itinerary.</td><td>(a) Search for a thing that has the “Name” property with the value of “Harry Miller”.(b) Look up all the links titled “Communicates With” that go to the thing that has “Harry Miller” as the “Name” property.(c) For the links that have “Confirmation Date”’s within the range of 01/01/2014 to 31/01/2014, add up the values related to “Sales Price” property.</td></tr><tr><td>Q4. Describe the procedure for generating a list of all Air Canada passengers with allergies.(a) From the “Customers with Additional Considerations” table, look up all the “Customer_ID” of all the customers that have allergies.(b) From the “Itinerary” table, find the “Itinerary_No”’s belonging to “Customer_ID”’s with allergies.(c) From the “Service Provider” table, look up AirCanada’s “ServiceProvider_ID”.(d) In the “Itinerary_Detail” table, look for the records with “Itinerary_No” from step b, and “ServiceProvider_ID” from step c.(e) Look up the “Itinerary_No”’s found in step d in the “Itinerary” table.(f) The “Customer_ID”’s corresponding to the “Itinerary_No”’s should be looked up in the “Customer” table.</td><td>(a) Look for all things that have a “Travels With” link going out from them.(b) Short list the ones that have the “Allergy” property.(c) The thing at the end of the “Travels With” link would have the “Name” property and the value of it should be “Air Canada”.Print the value of the “Name” property of every thing that matches with the pattern of “Thing A” mentioned above.</td></tr></table>

Table B2. Answer key to the consulting case.

Q1. Describe the procedure to identify the average hours worked per day by an employee on a completed project.

(a) Locate Edward McKay in the “Employee” table. Note his “Employee\_ID”.

(b) From the “Timesheet” table, find Edward’s timesheet using his “Employee\_ID”. Note his “WorkHours”.

(c) From the “Project” table, look up EZLink’s market research project.

(d) Using the start and finish date of the project, calculate the number of days it took to complete the project.

(e) Divide the work hours of the employee (e.g., Patrick) by the number of days it took to complete the project (for sake of simplicity, week ends and holidays are also included).

Q2. Describe the procedure for identifying clients that have worked with

(a) Looking at the “Project” table, find “Client ID”s that have been paired with two or more diferent “Division ID”s.

(b) Look up those “Client ID”s in the “Client” table and report the value under the “Name” property.

(a) Look up the particular project (e.g., audit for Vancouver Canucks) from the “Project” table and remove the current project manager ID.

(b) Locate the new candidate for the project manager position (i.e., Edward McKay) from the “Employee” table. Note Edward’s “Employee\_ID”.

(c) Insert the Edward’s “Employee\_ID” as the manager of the project (e.g., audit for Vancouver Canucks).

(d) Update Edward’s timesheet by going to the “Timesheet” table and putting Canuck’s Audit ID as the Project\_ID.

Q4. Describe the process to identify divisions that serve non-corporate clients.

(a) Consider both the “Client” and “Corporate Client” tables.

Q3. Describe the procedure of removing an employee from one project and assigning him as the manager of a diferent project. nd assigning him as the manager of a different project.

(b) From the “Client” table, exclude all the “Client\_ID”s that are also present in the “Corporate Client” table.

(a) Locate the thing that has “Edward McKay” as the value of its “Name” property.

(c) From the client records that remained after step b, note their “Division\_ID”

(b) Follow the “Serves” link that goes out from Edward’s node. Note the “WorkHours” property on the “Serves” link as well as “Project Name”.

(d) In the “Division” table, look up the “Division\_ID”s from step c. Print the name of the qualifying divisions.

(c) From the thing at the end of the “Serves” link from step b, look for “Has Project” links that have the same “Project Name” value. Note “Start Date” and “End Date”.

(d) Divide the work hours of the employee (e.g., Edward) by the number of days it took to complete the project (for sake of simplicity, weekends and holidays are also included).

two or more divisions.

(a) Look up all the things that have two or more “Has Project” links going out of them.

(b) Short list the ones for which the “Has Project” links lead to at least two diferent things (i.e., divisions).

(c) Report the value of “Name” property from the things found in step b.

(a) Locate the thing with “Edward McKay” as the value of “Name” property.

(b) Remove the current “Serves” link and establish a new “Serves” link to the thing that has the “Name” property of “Canucks”.

(c) On the “Serves” link, set the value of “Manages” to true.

(d) Search for the “Serves” link going out of the previous manager’s node and set the value of “Manages” to false.

(a) Look up all the things that have a “Has Project” link going out of them.

(b) Short list the ones that do not have the “CorporateAccount\_No” property.

(c) Display the value of the “Name” property of the things that qualified from step b.

## Appendix C. Examples of Marked Responses From Subjects

![](/api/attachments/F72WQR79/fulltext/images/4ffd8cfaeccdf92a4bddbee1ffa680fd13b8c5c10b1cfb57de497164386bfcc1.jpg)  
Figure 16. Statement and Visualization from Subject #21 (Class-based): Corporate department tends to have the most amount of pay increase

In IT department demotion due to performance is more than double males over females

![](/api/attachments/F72WQR79/fulltext/images/6a71be93637cd1e0fba35797f9e9434a54775659174a1cbc598a0b28f907cfa3.jpg)  
Figure 17. Statement and Visualization from Subject #35 (instance-based):2:00 always sees the greatest number of users accessing the servers in the day.

![](/api/attachments/F72WQR79/fulltext/images/aa67a43057d9d4842cbd878d34be7c66eae91ec6a58d2283fe767f006d996815.jpg)  
Figure 18. Statement and Visualization from Subject #12 (Class-based): Employees travel most frequently in March and least frequently in February

Figure 15. Statement and Visualization from Subject #18 (instance-based):  
![](/api/attachments/F72WQR79/fulltext/images/3a832ffd27de3bbd32b185a2ac51cd27a6b204c2b7b9a188305897cd160838d0.jpg)

## Appendix C1. Examples of Visual Analytics Done by Subjects from Experiment I

Statement and Visualisation from Subject #18 (instance based):

In IT department demotion due to performance is more than double males over females

Statement and Visualisation from Subject #21 (Class based):

Corporate department tends to have the most amount of pay increase

Statement and Visualisation from Subject #35 (instance-based):

2:00 always sees the greatest number of users accessing the servers in the day.

Statement and Visualisation from Subject #12 (Classbased):

Employees travel most frequently in March and least frequently in February

## Appendix C2. Examples from subjects in Experiment II

The 5-point marking scheme is demonstrated in Tables C1 and C2. For the sake of this example, we focused on only one particular question in the travel agency case. First, we provide examples from subjects in the class-based group and then actual answers to the same question from participants in the instance-based group.

Related to evaluating the class-based condition, we should note that even though we stressed matching primary and foreign keys during the training (as well as in the course for 5 to 6 weeks), we accepted answers from users that described the steps in terms of natural joins (i.e., without discussing primary and foreign keys), as can be seen in the tables below.

Question: Canada Border Services has asked the agency to identify all trips facilitated by two diferent types of service providers (e.g., a trip that half of it is with a train, and the second half with an airplane). Describe the procedure for retrieving that information.

Table C1. Sample scoring from answers of participants in the class-based group.

<table><tr><td>Answer</td><td>Mark</td><td>Explanation</td></tr><tr><td>a) In “Itinerary Detail” table, find “Itinerary_Nos” that occur multiple times.b) List the ones that have multiple “Service_Provider_IDs”.c) Run those Service_Provider_IDs through “Service Provider” table.d) Note the “Itinerary_Nos” that have two different types of service providers. (Subject #33)</td><td>1.00</td><td>Procedure leads to correct answer.</td></tr><tr><td>1. In Itinerary Detail, look for service provider ID that has two different IDs for one itinerary no.2. Note service provider ID. Under Service Provider, you will see the service type. (Subject #87)</td><td>0.75</td><td>The steps are correct. However, did not mention that service types should be distinct.</td></tr><tr><td>Look up itinerary table.Find service provider ID.Go to service provider table and identify service type with more than two types of services. (Subject #61)</td><td>0.5</td><td>Did not consider the fact that two service providers should facilitate a single trip (i.e., looking for the same itinerary-no constant). However, subject understood that two tables need to be joined.</td></tr><tr><td>a) Search under the Service Provider table for service provider IDs that have two service providers.b) Print the page. (Subject #87)</td><td>0.25</td><td>Subject provided only one step required to find the answer, and for that, s/he received 0.25.</td></tr><tr><td>Locate from Itinerary Detail the Itinerary No. (Subject #30)</td><td>0</td><td>Not a complete step.</td></tr></table>

Table C2. Sample scoring from answers of participants in the instance-based group.

<table><tr><td>Answer</td><td>Mark</td><td>Explanation</td></tr><tr><td>Locate a thing that has the name of a person and see if they have two “Travels With” arrows. Then look at the departure dates in the properties of the arrows. If the value is the same, then the trip is facilitated by two different types of service providers if the service type of the adjacent thing is different. (Subject #24)</td><td>1.00</td><td>Procedure leads to correct answer.</td></tr><tr><td>1. Search for Travels With links that have itinerary_no appear more than once.2. Find associated thing’s “Service Type”.3. Provide list of links with the same Itinerary_No and the related thing’s “Service Type”. (Subject #124)</td><td>0.75</td><td>Service types should be different. Otherwise a trip that is facilitated by two airlines, for example, would also be qualified according to this procedure.</td></tr><tr><td>1. Find node with two links of “Travels With” going away from the node.2. From those links, find “itinerary_no_ and record the values. (Subject #22)</td><td>0.5</td><td>Did not consider the value of “Service Type” property or the requirement that types should be different.</td></tr><tr><td>Locate Itinerary_Nos occurring more than three times (connected to more than three things). If more than one is a service provider, it is correct. (Subject #39)</td><td>0.25</td><td>Does not lead to the correct answer, but the subject understood that the pattern for identifying those trips would include repetition of the Itinerary_No property.</td></tr><tr><td>1. Find all data associated with Canada Border Services with links to Service Type.2. Identify all Service Type names related to Canada Border Services. (Subject #76)</td><td>0</td><td>Irrelevant answer.</td></tr></table>
