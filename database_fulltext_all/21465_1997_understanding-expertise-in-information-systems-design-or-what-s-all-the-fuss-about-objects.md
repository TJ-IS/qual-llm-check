---
otero_id: 21465
otero_key: "VY3HVPPH"
title: "Understanding expertise in information systems design, or, What's all the fuss about objects?"
authors: "Alain O. Villeneuve; Jane Fedorowicz"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(97)00020-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Understanding expertise in information systems design, or, What's all the fuss about objects?

Alain O. Villeneuve $^{a,1}$ , Jane Fedorowicz $^{b,*}$

$^{a}$ MIS Department, School of Management, Boston University, 704 Commonwealth Avenue, Boston, MA 02215, USA $^{b}$ Department of Accountancy, Bentley College, 175 Forest Street, Waltham, MA 02154-4705, USA

## Abstract

The concept of Object Orientation (OO) is very appealing to many in the information systems field. Although it requires a radical shift in the traditional systems development paradigm, many have begun to embrace it. This paper explores the literature on knowledge representation and expertise in the cognitive sciences and in information systems to lend substance to the underlying OO approach. We show that OO closely parallels our current understanding of the concept of expert knowledge representation based on schemata and scripts, and thus is particularly attractive to individuals who are or aspire to be ‘expert’ systems developers. We then examine the IS literature on expertise and reinterpret findings to support our depiction of expertise within IS. The OO approach incorporates many of the characteristics of expert-level knowledge representation, which may explain its appeal to those in the systems development profession. We propose that the OO methodology also contributes to the acquisition of expertise by documenting and sharing the modelling approach of those with considerable IS design expertise. © 1997 Elsevier Science B.V.

Keywords: Expertise: Information systems design; Knowledge representation; Learning; Object-oriented

## 1. Introduction

Fads permeate the practice and study of computer information systems. True to form, analysis and programming fads come and go, and are quickly replaced by something newer and ‘better’. Proponents are convinced that the innovation they espouse will become the industry’s standard bearer, and solve the development problems that previous fads could not.

Computer-Aided Software Engineering (CASE) technology is a good example. CASE was supposed to automate much of the drudgery of software development, while simultaneously improving the quality and timely delivery of the resulting system. Although CASE vendors continue to make advances in product features, CASE technology has not achieved the expected improvements nor the market penetration its early advocates expected. Even IBM acknowledges the failure of AD/Cycle, its software development blueprint for CASE technology [1]. New versions of AD/Cycle will be LAN-based and rely on object-oriented technology. $^{2}$

Object orientation (OO) is the newest arrival on the field. A spate of object-based products has appeared recently, with more being announced daily. Only this time, the bandwagon has quickly become very crowded. The Object Management Group, a self-proclaimed standard-setting body, boasts over 300 corporate members. Several widely-accepted OO design methodologies have emerged, including Coad/Yourdon, Booch, Odell/Martin and Rumbaugh. Apple, IBM, Novell, WordPerfect and Borland are working together to develop a common OO architecture [4]. OO products are suddenly very hot. What's all the fuss about, and how likely is the survival of this latest trend?

OO techniques and methodologies profess to turn traditional systems design methodologies on their ear. CASE tools rely on traditional structured analysis and design techniques (e.g., [5–8]). These methods build upon the waterfall method and functional decomposition, in which successively refined designs of a system are proposed, until a completely specified system results. Analysis and design are supported by different techniques, which has led to specialized CASE tools that fall into 'Upper' and 'Lower' CASE categories. These techniques also emphasize the separation of processes and procedures from data, each supported by its own rules and diagrams. OO methodologies, on the other hand, integrate all aspects of analysis and design under one uniform approach to the design problem. In their comparison of OO and conventional analysis and design methodologies, Fichman and Kemerer [9] find OO to represent a 'radical change' over more traditional methodologies. $^{3}$

OO methodologies and techniques center on the premise that the real world is made up of objects, which in turn embody a collection of attributes and behaviors. Designing systems thus relies on an understanding of which objects exist in the system's domain, and also which relationships exist among the types of objects in the domain. Only then can (and should) a system be built.

The concept of OO is very appealing to many in this field. Although it requires a dramatic shift in the traditional programming paradigm, many have begun to embrace it. Several CASE vendors have added object modules to their products in an attempt to retain market share $[10]$ . What is the appeal of this approach? Will it lead to a widespread shift in the system development paradigm?

This paper explores the literature on knowledge representation and expertise in the cognitive sciences and in information systems to lend substance to the underlying OO approach. We first show that OO $^{4}$ closely resembles our current understanding of the concept of expert knowledge representation to suggest that the Object and Dynamic Models that form the basis of an OO methodology [11] parallel the cognitive science concepts of schemata and scripts. By linking OO to these widely accepted theories of knowledge representation, we contend that OO provides a familiar representation and attractive methodology for individuals who are or aspire to be ‘expert’ systems developers. Further, OO is also perceived as a more appropriate systems design methodology to support the transfer and development of expertise.

Because there is no body of literature studying the impact of OO techniques on systems development, we then examine several studies within the IS field that examine the expertise of systems developers using various other tools and methodologies. We use the IS literature on expertise to reinforce and reinterpret findings in light of our depiction of expertise within IS, to demonstrate that our reference theories are helpful in understanding systems designers' expertise. We then offer some expectations for the OO paradigm based on this literature discussion. Our contention is that since OO seems to closely parallel human knowledge structures, particularly at higher levels of expertise, it is thus a powerful approach for producing high quality, easily understood systems designs.

In Section 2, we look at the cognitive science theories of schemata and scripts and demonstrate how OO methodologies parallel those theories. Section 3 examines the literature on expertise, and discusses the implications of current understanding of expert behavior for OO. Section 4 provides our reinterpretation of prior IS research in light of these cognitive theories. Section 5 presents our expectations for the relationship between OO and IS design expertise. Section 6 concludes with a discussion of future research directions.

## 2. Cognition theories

Early computer scientists hoped to build a mechanical brain, one which would replicate the storage and access mechanisms of the human brain. Most early efforts had little resemblance to current theories of human knowledge representation. Even now, theories abound on how human knowledge is stored and accessed. In this section, we review several of these theories, while focusing on those that are often used in the study of human expertise. We then show the similarities between this approach to knowledge representation and the basic concepts of the OO paradigm.

## 2.1. Research on knowledge representations

Several knowledge representation theories have been proposed in the cognitive psychology and cognitive sciences fields (Table 1). Basically these theories fall into three categories: production systems theories, mental models theories, and propositional-based theories.

Theories of production systems typically apply if ... then rules to incoming data to deduce actions to be taken. Incoming data are compared against accumulated data (declarative knowledge) by using rules that the subject knows (procedural knowledge). This set of theories postulates that knowledge is stored in terms of rules and facts.

Mental models theory professes that human beings create a model of a situation before taking any action. First, the subject discerns the premises of the problem and creates a mental model. Second, the subject formulates a putative conclusion. Finally, before taking an action, the subject searches for a counter example for the putative conclusion. One fundamental characteristic of mental models is that they do not contain variables, rather, they contain tokens that represent a set of objects [26]. To that extent, mental models are a class of knowledge representation by themselves.

Theories that are propositional-based posit that knowledge is represented in terms of propositions from which humans derive (infer) new facts. Incoming data is compared against stored knowledge and the similarity of this new data with stored knowledge is assessed. The similarity of the data either creates a new instance in memory or refines actual knowledge.

Propositional-based theories are often used in research on human expertise. Of particular interest here are the theories of schemata and scripts. These theories, especially schemata theory, are more appropriate than many others for the study of expertise because they provide mechanisms for learning that others do not. In fact, schemata theory has received more attention than other theories in this category, perhaps because schemata tend to provide problem-solving context-dependent explanations for human cognitive processes.

Table 1  
Theories of knowledge representations

<table><tr><td>Type of theory</td><td>Theory</td><td>Authors</td></tr><tr><td rowspan="5">Propositional-based theories</td><td>Framesa</td><td>Minsky [12]</td></tr><tr><td>Prototypes</td><td>Mervis and Rosch [13]</td></tr><tr><td>Schemataa</td><td>Bartlett [14], Piaget [15], Rumelhart [16.17]</td></tr><tr><td>Semantic networks</td><td>Quillian [18]</td></tr><tr><td>Scripts</td><td>Abelson [19], Schank [20], Schank and Abelson [21]</td></tr><tr><td>Production system theories</td><td>Production systems</td><td>Anderson [22,23], Newell and Simon [24]</td></tr><tr><td>Mental model theories</td><td>Mental models</td><td>Craik [25], Johnson-Laird [26]</td></tr></table>

$^{a}$ Schemata and frames are different labels for the same memory structure [27–29], but the cognitive sciences literature has paid more attention to the notion of schemata than to frames.

## 2.2. Schemata and scripts: definitions

Schemata and scripts comprise different knowledge structures. Schemata are like models of the world. They embody prototypical expectations about objects, situations, events and actions. Schemata represent (or categorize) knowledge but they also serve as 'filters' to extract knowledge from memory. They allow the individual to capitalize on the regularities of situations and thus help to make accurate inferences and predictions efficiently. Given the limited information-processing abilities of the individual, by focusing attention on those aspects of the environment providing information that disagrees with existing knowledge, schemata can facilitate the processing of information. Schemata also help to bring relevant knowledge to bear on a current environmental situation. Instead of many highly specific pieces of knowledge being accessed separately, it is often possible to find a single schema that contains sufficient information to permit adequate interpretation of the situation [27].

Although individual schemata may appear to be different from one another, schemata have several common features $[30]$ . All schemata contain variables. Schemata represent knowledge on all levels of abstraction. A schema of a concept can have fixed parts, which are assumed always true for instances of the concept, and variable parts. Variables have default values, and they may take on other values depending on the context. Schemata can embed within one another: a schema can consist of a configuration of subschemata. There are schemata for physical concepts like birds as well as for abstract concepts like love and friendship. Subschemata (those addressed by one schema) need not be of the same type as each other nor do they need be of the same type as that of the 'parent' schema. In this case, the parent schema represents a composite concept. Schemata are active processes, continually evaluating incoming information to ascertain the degree to which it is relevant $[30]$ .

![](/api/attachments/VY3HVPPH/fulltext/images/15b2e3ceecf38a1debcfac0413de8df646dbceb2033b42a4004ebaae8e6dd1f5.jpg)  
\* Default values are underlined

Fig. 1. Example of a possible cognitive schema for Customer Document.

Another view of schemata is offered by Smith [29]. Smith agrees that schemata represent concepts from different levels of abstraction but his major contribution is in proposing a more formal representation of a schema format. First, a schema has an attribute-value format. For each attribute there is a list of possible values (domain) that instances of the concept can assume. One value of each attribute is designated as a default. In addition, relations between attributes are specified (e.g., some attributes make sense only if some other attributes have certain values). A schema bears an indication of the type, or superset, of which the concept is a member. Again, subschemata need not be of the same types nor do they need to be of the type of the 'parent' schema. Finally, each attribute is marked for its importance (i.e., attributes bear a weight) and relevance.

Fig. 1 depicts an example of a schema for the concept ‘Customer Document’. A schema consists of attribute-value pairs (as will be discussed below) and default values are underlined in the example. For a document used for ‘Order Entry’, default values for the schema attributes are: Line Item Components = ‘Product Description’ and ‘Quantity’, Name = ‘Order’, and Cardinality = ‘Number of line items on document’. If the document was for ‘Billing’ instead of ‘Order Entry’, then default values could be: Line Item Components = ‘Product Description’, 'Shipping Status', 'Quantity', 'Unit Price', and 'Price Extension', Name = 'Invoice', and Cardinality = 'Number of line items on document'. The particular default values included in the schema are acquired through learning (see Section 2.3 for more on learning). Notice that the schema refers to other more concrete schemata. For example, each of the customer documents referred to by the abstract concept is represented by its own concrete schema in the knowledge base.

Scripts are sequences of episodes that take place over time whereas schemata are static representations of concepts. While attempts have been made in the past to coalesce the theories of schemata and scripts (see Ref. [28]), these theories represent distinct types of knowledge. Scripts have important temporal and spatial dimensions and they apply to the interpretation of events taking place at the moment of their instantiation. Scripts play a very specific role and are activated for highly specific occasions as we will see in Section 3. Scripts help support behaviors such as ‘story-telling’ since they focus on the sequencing of events.

Fig. 2 depicts an example of a script for a retailing business. The sequencing of events over time are components of the script. The actual events and sequences depend on an individual's past learning and expertise. For instance, if the retailer tracks back-ordered items then the script would not stop at item 10 as illustrated. Rather, other events would be added to the script such as 'out-of-stock items are ordered for the customers', 'out-of-stock items are received', 'out-of-stock items are packed for the customer', etc. The script in the example would also be adjusted if the retailer has its own delivery service.

The existence of schemata and scripts and the knowledge they contain does not, in itself, explain the differences in performance between different levels of expertise. A learning facility must be present to refine the stored knowledge.

Fig. 2. Example of a script for an order entry, billing and shipping system for a retailing business.

## 2.3. Evolution through learning

If differences among individuals could be accounted for solely by the number of schemata in their knowledge base, then more expert individuals should take longer to solve problems because they must sort through more schemata. However, in real life, experts outperform novices when solving problems within their domain of expertise. Therefore, schemata must have an internal organization that aids in their effective retrieval and handling. Schemata are thought to be organized in a hierarchy, with more abstract concepts at the top of the hierarchy and more concrete at the lower levels $[17,29]$ . As experience and understanding dictate, schemata are reorganized over time and their hierarchical placement reflects a developing level of abstraction. This reorganization results from learning and from experience.

According to schemata theory, learning occurs via accretion, tuning, and restructuring [17]. Learning by accretion is based on memory traces of comprehension processes, and these traces typically comprise partial copies of instantiated schemata. The creation of a new low-level schema in memory is the result of accretion. Tuning involves the development and refinement of concepts as a result of experience, or learning. Adding a new value to the domain of possible values for any given attribute and the specification of new default values are examples of tuning. Restructuring involves the creation of new schemata, which can occur either by copying an old schema and adding some modifications to it (or removing some attributes from it), or by repeating a spatiotemporal configuration of schemata. During restructuring, a higher level schema (more abstract) can be created from lower level schemata. The notion of abstraction is important here: it suggests that the newly created schema is leaner in terms of attributes. As schemata include an indication of their membership, low-level schemata can be adjusted to avoid repeating common attributes or common domain values.

Experience contributes to the refinement of knowledge and either modifies existing schemata or helps define new schemata $[31]$ . Each problem-solving experience may also aid in confirming existing knowledge $[32]$ . Confirmation leads to restructuring whenever a certain number of schemata share the same (or very similar) list of attributes and corresponding value domains. If the schema is unique or if there are a very small number of schemata sharing the same list of attributes, then the schema will remain at the lowest level in the knowledge base and only its value domains will be adjusted. As schemata are reorganized over time and as more abstract schemata appear at the top of the hierarchy, their retrieval is probably hindered instead of facilitated. By definition, abstract schemata have less detailed attribute values. Retrieving a specific schema thus requires navigating across the knowledge base in order to assess the similarity of the incoming data with existing schemata.

Other advantages and disadvantages of this theory of knowledge representation also bear mentioning here. First, the theory accounts for the systematic distortions and inaccuracies that have been documented in memory performance (this will be supported in Section 3). Second, the theory focuses attention on the representation of information in long-term memory and proposes that information is stored in larger units of information than single words and symbols as suggested by previous theories of categorical memory.

The theory, as good as it is, requires additional refinement. The notion of schemata by itself is vague and there is no unique, agreed upon representation or way to measure schemata or schema content. As schemata organize knowledge and provide mechanisms for its retrieval, questions such as 'Is it better to remember schema-relevant information or schema-irrelevant information?' have yet to be answered [29].

Another limitation of the notion of schemata is that they are incomplete structures. They help categorize concepts but do little to support action. This is the purpose of scripts. Scripts promote change (the spatiotemporal dimension) that helps depict the concept in action and thus adjusts the solution to the problem accordingly. Schemata can therefore be perceived as static representations of concepts whereas scripts are the structures that put them into action. The two knowledge structures also differ in terms of their temporal scope. Schemata act as filters but their temporal scope is short-lived since each only lasts for the duration of its instantiation. Scripts have a longer temporal scope since they represent sequences of events that can take place over minutes, days, years or any other macro units of time. The two structures are thus seen as complementary.

An example based on standard business applications will help to better understand the complementarity of the two knowledge structures. Suppose a systems designer is told that a document is to be prepared after some stock has been selected (as per the example in Fig. 2) without being told that the company has its own delivery service. From what the designer knows, he/she may infer that the document is a bill of lading (a document that must be presented to a carrier when picking up the stock) and that the company issues invoices but not shipping bills. After learning that the company has its own delivery service and thus adjusting and playing a different script, the designer now understands that the document is to be a shipping bill rather than a bill of lading. The designer then substitutes a shipping bill schema for the previously invoked bill of lading representation. This example helps explain how scripts play an important role in selecting the most appropriate schema to represent the situation at hand. The major features of schemata and scripts are summarized in Table 2.

The elaborate structures of schemata and scripts can represent complex concepts, events and relationships in a consistent and efficient manner. We posit that both structures are needed to assist in understanding and solving IS design problems. Software development is a difficult and complex process. Berry asserts that “...it is absolutely necessary for software engineering research to address making software production more systematic and repeatable” ([33], p. 33). OO is a well-grounded approach that aims to achieve these goals. In Section 2.4, we show how OO enhances these knowledge structures by providing a physical formalism for representing objects and events.

Table 2  
Summary of schemata and scripts structures

<table><tr><td>Cognitive structure</td><td>Features</td></tr><tr><td>Schemata</td><td>Hierarchically organizedAttribute-value formatAttributes have a list of possible values (value domain)Attributes have a default valueSome attributes can be interdependentAttributes have a weight indicating the attribute&#x27;s relative importanceA schema has an indication of its class (concept) membershipSchemata bear a notion of contextual informationSchemata filter incoming information when instantiatedSchemata represent knowledge at all levels of abstractionSchemata can embed in each other (subschemata)Abstract schemata exist at the top of the hierarchy and have leaner attribute lists</td></tr><tr><td>Scripts</td><td>Action oriented knowledge structuresScripts sequence the steps in mental processingSome are pure action scripts that automate psychomotor behaviorMain focus is on the sequencing of eventsRole is to put schemata into actionScripts&#x27; temporal scope is large (temporal units are large)Scripts help in selecting the most appropriate schemataScripts help in confirming selected schemata</td></tr></table>

## 2.4. Parallels in object orientation $^{5}$

The concept of objects in the OO paradigm is remarkably similar to schemata. Both distinguish between classes of objects and instances of objects. Each object has a number of identifying attributes. Object classes can be linked to other classes, through an association that depicts a specific relationship with a specified meaning and multiplicity. A special type of association called a generalization provides inheritance of attributes and behaviors among the members of a hierarchy. The lower levels of the hierarchy contain more specialized or more specific instances of the abstract concepts at the top. Another type of relationship, the aggregation, allows an object to be made up of a number of other object components. Aggregation is very similar to the notion of composite concepts in schemata theory. An Object Model comprises a collection of classes and relationships that reflect the current understanding of the world being modeled. Table 3 summarizes the major concepts of the Object Model in view of schemata theory.

The OO paradigm recognizes that events occur over time that change the values of object instances. A Dynamic Model, represented by a state diagram, depicts expected events and the state of their outcomes for all object classes that can change over time. The Dynamic Model is based upon a series of scenarios, which in turn summarize the detailed progression of actions and outcomes that result over time. Scenarios are very similar to scripts, and the Dynamic Model depicts intertwining occurrences of related scripts/scenarios. Table 4 reflects these similarities.

Table 3  
Comparison of schemata and object model

<table><tr><td>Concept</td><td>Schemata</td><td>Objects</td></tr><tr><td>A single occurrence</td><td>Schema</td><td>Instance</td></tr><tr><td>A collection of occurrences with common features</td><td>Class</td><td>Class</td></tr><tr><td>A collection of occurrences with different features</td><td>Composite schema</td><td>Aggregation</td></tr><tr><td>A descriptive feature</td><td>Attribute</td><td>Attribute</td></tr><tr><td>Inheritance relationship</td><td>Inheritance</td><td>Generalization</td></tr><tr><td>Links between objects</td><td>Embedded schemata</td><td>Associations</td></tr></table>

Table 4  
Comparison of scripts and dynamic model

<table><tr><td>Concept</td><td>Script</td><td>Dynamic model</td></tr><tr><td>A single event sequence</td><td>Script</td><td>Scenario</td></tr><tr><td>A collection of event sequences</td><td>Scripts</td><td>Dynamic model</td></tr><tr><td>Trigger for use</td><td>Event</td><td>Event</td></tr><tr><td>Purpose</td><td>Put schemata into action</td><td>Depict time-dependent states of objects</td></tr></table>

We have shown how schemata and scripts incorporate properties of the results of learning in Section 2.3. OO depicts many of the same learning effects in its representation of the relationships among classes, objects, operations and attributes. Indeed, the different types of abstraction resulting from learning are fundamental to the OO paradigm. To adopt Rumelhart's terminology [17], new instances of objects can be created in OO, suggesting learning by accretion. Because objects are inherently independent of each other, it is easy to tune or make adjustments to a class or instance of an object without inadvertently affecting others. Abstraction of classes results in inheritance relationships. Combinations or assemblies of classes produce aggregation relationships. Both of these relationships provide links through inherited attributes that produce leaner classes within multi-levelled hierarchies, resulting in the restructuring of the object model.

As experience is acquired within the problem domain, the developer will note similarities among the entities under analysis, and will begin to abstract from these observations. Experience with the OO paradigm will also guide the developer to look for the relationships that are supported by OO. Both types of experience build up the developer's knowledge base of schemata and scripts. By constructing an OO model, the developer is, in effect, developing a physical representation of his/her understanding of the schemata and scripts that are relevant to the problem domain.

Now that parallels have been drawn between OO and schemata and scripts, Section 3 discusses these theories in the context of expertise and demonstrates that they are useful in explaining differences in cognitive processes and performance found in some empirical work. OO methodologies have adopted structures similar to the expert structures documented here, and would thus be very appealing for experts to use (and for those who aspire to be experts).

## 3. Expertise

Differences in memory performance and recall between experts and novices have been noted extensively in the literature. In this section, research on expertise will be shown to be consistent with the theories of schemata and scripts. We will then note how characteristics of expert behavior are supported by the structures comprising OO methodologies.

Findings in the area of memory performance, taken alone, do not account for the differences in performance between experts and novices. Findings in the area of cognitive processes share the same shortcoming. For example, Patel and Groen [34] report that accuracy of the solution seems to develop monotonically with expertise whereas memory recall is non-monotonic. Therefore, both memory performance and cognitive processes are discussed below.

## 3.1. Memory performance

Research in the area of memory performance provides evidence that experts and novices differ in terms of their ability to recall objects. Some major findings in this area are summarized in Table 5. These differences in memory performance between experts and novices can be explained by differences in the organization and contents of their schemata.

Experts outperform novices in such diverse domains as recalling chess piece placement, program listings, medical diagnoses, and physics. The results hold as long as experts recognize familiar patterns in logically organized data. But experts' performance deteriorates to the level of the novices' when they fail to recognize familiar patterns although the task is still typical of their domain. Novices, on the other hand do not exhibit differences in performance between familiar and unfamiliar patterns. These findings suggest that experts' schemata organization is more advanced than novices.

Table 5  
Differences in memory performance between experts and novices

<table><tr><td>Domain of research</td><td>Main results</td></tr><tr><td>Chess [35–38]</td><td>Experts are superior at remembering familiar patternsExperts are not superior when pieces are randomly placedExperts seem to store information in long-term memoryExperts recall from memory in burstsThe use of standard chess notation helps both experts and novices in knowledge acquisition</td></tr><tr><td>Programming [39,40]</td><td>Experts are better when recalling standard listingsExperts are not superior at recalling scrambled listingsExperts are better at recalling when programs follow programming conventions</td></tr><tr><td>Medicine [34]</td><td>Intermediates recall more than novices and expertsRecall corresponds to a U-shaped, non-monotonic function of expertiseExperts are better at identifying relevant informationExperts categorize problems by principles whereas novices use objects and situationsExperts fall to the level of novices when the problem structure is disrupted</td></tr><tr><td>Physics [41–45]</td><td>Experts categorize problems based on underlying principlesBoth experts and novices use diagrams extensivelyExperts&#x27; diagrams are more principles-oriented than those of the novicesDiagrams are believed to provide cues for retrieval</td></tr><tr><td>Writing [46]</td><td>Novices outperform experts at recalling texts they have written</td></tr><tr><td>Others [47,48]</td><td>Experts use tricks to help them recallExperts encode information in a way convenient to them</td></tr></table>

Several researchers have shown that humans organize their memory in chunks. The theory of schemata supports this assertion. Experts' ease of recall of familiar patterns points to the fact that their schemata (or clusters thereof) are more organized, tightly coupled around specifics than those of the novices. But whenever experts face unfamiliar patterns, they have to navigate in their knowledge bases in the same manner as novices, resulting in equally poor performance.

Experts rely more on principles when recalling objects whereas novices use more physical and concrete attributes. These findings support the proposal that schemata's contents are different for experts and novices. In summary, results provide evidence that experts are better performers than novices within their domain of expertise (one major exception, the act of writing, will be discussed in Section 3.2).

The existence of familiar patterns and principles suggest the availability of multiple levels of abstraction arranged in a logical hierarchical or linked structure. Knowledge clusters infer the use of inheritance or composite (aggregation) structures.

## 3.2. Cognitive processes and problem-solving strategies

Findings in the area of processes and problem-solving strategies also provide evidence that experts and novices have different schemata organizations and that their schemata contents differ. Problem-solving strategies reflect the underlying organization of schemata as the subject has to cope with what is in memory and how it is organized.

Three main areas of problem-solving performance can be derived from the literature on experts and novices as shown in Table 6. First, there is the time to understand the task (or problem). Experts take more time at understanding the task and they ask more questions than novices. As more abstract schemata are at the top of the hierarchy in the knowledge base, experts have to access more schemata in looking for concepts (or instances) similar to the data at hand. Since they access more schemata along their search paths, competing schemata are probably instantiated. This forces them to seek to confirm their schema as they navigate, therefore leading to a longer search time.

Table 6  
Differences in cognitive processes between experts and novices

<table><tr><td>Task solving step</td><td>Experts compared to novices</td></tr><tr><td>Understanding the task</td><td>Experts take more time (or devote larger fraction of their time) than novices at understanding the problem [49,46]Experts ask more questions than novices [49,50]Experts use more artifacts (diagrams) then novices to represent the problem [51]Experts focus on rare events and use less cues than novices [35,52,30,53]Experts do more backward-reasoning than novices [54,55,46]Experts seem to retrieve a solution method as part of the immediate comprehension of the task [41,56]</td></tr><tr><td>Performing the task</td><td>Experts take less time than novices [34,42,57,40]Experts show more forward-reasoning than novices [41,34]Experts use less cues than novices [52,30,53]Experts use high-level schemata whenever possible [58]Experts tend to ‘mentally execute’ their solution at different points in time [59,60]Experts show more self-regulation than novices [41,49]</td></tr><tr><td>After the task</td><td>Experts are more confident in their solution than novices [53]Experts are not as good as novices at detailing the steps they have taken [61]</td></tr></table>

Each problem-solving experience contributes to the refinement of knowledge [32]. But experts are more likely to experience problems within their specific domain of expertise. Murphy and Wright [58] provide direct evidence that experts' and novices' concepts differ in terms of structure and that they also differ in terms of distinctiveness. For instance, an attribute can belong to more than one schema in the case of experts while novices' schemata are more independent. Experts' higher level schemata are hence less discriminating since they are more abstract and thus do not contain concrete values for their attributes; rather they contain ranges of permissible values whereas the novices' schemata contain mostly concrete values for the attributes.

Second, while solving the task, experts also outperform novices. They outperform them on two planes. Experts take less time if they follow a forward reasoning strategy down the path from abstract to concrete concepts. At the solution stage they can reproduce schemata because of their natural grouping without needing to check the contents. Novices, on the other hand, check their schemata against more abstract schemata at the time they solve the problem (although their schemata are less abstract than the experts'), as they do not yet have the natural groupings of schemata that characterize experts.

Further, experts exceed novices in their ability to apply proven techniques or compiled knowledge to a problem. This implies that experts have a larger number of scripts, and that they also have varying degrees of concreteness depending on their placement in an abstraction hierarchy.

When asked to explain their solutions, experts have more difficulty than novices. In the area of reading and writing for example, as Scardamalia and Bereiter ([46], p. 172) report:

It is the novice, not the expert, whose rate of production is fast enough to match handwriting speed ...their novice counterparts can recall with greater speed and equal accuracy the texts they have produced.

Novices only remember the lowest level schemata and scripts instantiated while writing whereas experts reconfigure their search paths as they navigate across different levels in their hierarchy.

Another striking difference between experts and novices emerges in the literature. Especially in the domains of programming and physical database design, experts tend to mentally execute their solution at different points in time $[59,60]$ . This suggests the use of distinct scripts. Although we do not know much about their activation yet, scripts seem to play a significant role in this important part of the problem-solving process.

Finally, although seemingly obvious, experts' solutions are of better quality and lower variance than novices'. Experts may make small errors at times, but they tend to avoid large mistakes [53] leading to solutions of better overall quality than those of novices. This again implies a preexisting knowledge structure that can be invoked in familiar situations. Good schema and script selection and use would account for quality and variance differences.

## 3.3. OO and expertise

Experts develop elaborate relationships among schemata. In particular, we note that expert-level memory performance appears to reflect recognition of patterns in observed events, chunking of knowledge, a reliance on principles, and other means of categorizing knowledge and facts. Rather than randomly searching through a large store of schemata, experts rely on special types of associations to improve the timeliness and quality of cognitive processes. The OO paradigm is also enriched when associations, generalization and aggregation are used extensively. A flat collection of objects is only a small improvement over a relational database. The contribution of relationships and operations among objects provides a contextual breadth to OO that distinguishes the expert's model of the world from that of a novice.

Experts also employ different problem-solving strategies than novices. Experts spend more time understanding a task than novices. This understanding comprises the basis of the analysis phase of systems development. OO development, in placing greater emphasis on this stage of development than other methodologies, promotes catching design errors at an earlier, cheaper-to-resolve stage of development.

As they peruse the levels of the abstraction hierarchy, experts avail themselves of schemata containing different degrees of abstraction. As noted in Section 2.4, the abstraction hierarchy is well represented by the object and dynamic models within the OO paradigm.

Experts also outperform novices when solving a task. This is attributed to experts' propensity to group schemata, allowing them to navigate their hierarchy in a more productive manner while at the solving stage. Again, these groupings are directly supported by OO through inheritance, aggregation, and link relationships.

Experts also use compiled knowledge to solve problems. In effect, they are employing scripts as a solution mechanism. Experts have hierarchies of scripts that account for special cases or alternative solution paths, much as the dynamic model of OO.

OO can help experts in explaining complex reasoning by providing documentation for elaborate relationships. Compared to novices who rely on concrete, low-level models (the equivalent of a flat file or relational data base), experts must determine how and when to navigate across the levels in a hierarchy representing different degrees of abstraction. The physical representation of an object or dynamic model would assist in this process.

The predictable quality of expert solutions is also reflected in the OO methodology. By employing a consistent and powerful representation of objects and their behaviors, OO leads to reusability of ideas and relationships. It also provides for independence of objects to support changes and updates with minimal disturbance to the rest of the model.

Although we do not have the space to include a more complete discussion of the current understanding of expertise research, these examples serve to demonstrate the cohesion between these cognitive theories and the physical manifestation of the OO methodology. The methodology promotes a unique view of relationships among objects and behaviors that is similar to that of schemata and scripts, and that supports the complex relationships believed to accompany expert-level knowledge representation.

We turn now to an examination of IS research, to understand the impacts of expert-level behavior on the development of information systems.

## 4. Reinterpreting IS research studies

In order to demonstrate why the OO paradigm is appealing to expert-level analysts, we first review a sample of IS literature in which IS expertise is studied. As little has been published about the impacts and use of OO methodologies, and even less has been empirically tested, we are forced to extrapolate about OO use from an examination of system developer studies conducted in other areas of IS. Each study is summarized, and the results are reexamined in light of schemata and script theories. We show that prior research supports the choice of these theories to explain how expertise is acquired and used within this field. The OO paradigm, which so closely resembles these theories, is thus well suited to support knowledge processes at an expert level.

For ease of presentation, the articles are grouped under separate headings: expert systems, experts in IS design tasks, and database design.

## 4.1. Expert systems

Section 3 has shown that schemata change and reorganize over time as a consequence of problem-solving experiences and learning. The IS literature that deals with secondary learning effects of the use of expert systems is, as will be discussed, compatible with the proposed theories. These studies demonstrate how novices and experts within a problem domain augment their existing knowledge bases when they have been exposed to an expert system.

## 4.1.1. Lamberti and Wallace [62]

Lamberti and Wallace conducted an experiment with high-skilled (expert) and low-skilled (novice or intermediate) subjects using an expert system. The results show that the impact of system use was larger on low-skilled users than on high-skilled users. Another finding of the study is that the level of user performance depends on the type of knowledge required to conduct the task. For example, low-skilled users outperformed (took less time than) high-skilled users when dealing with concrete knowledge (which is understandable as a larger portion of their hierarchy reflects concrete knowledge). The converse was true for abstract knowledge, as experts outperformed novices when abstract knowledge was involved.

The results support the assertion that experts and novices have different schemata contents. The authors themselves discuss abstract and concrete knowledge and distinguish between procedural and declarative knowledge. Declarative knowledge can be said to correspond to schemata and procedural knowledge to scripts.

The fact that the system's impact is larger for low-skilled users is consistent with schemata theory. As novices' schemata are individually more detailed and concrete (containing more attributes that have concrete values associated with them), it is reasonable to expect a larger impact here. The support provided by the system decreases the novices' memory searches across low level schemata (i.e., which are more horizontal since they do not have as many layers of abstraction as experts).

The finding that high-skilled users performed worse than low-skilled users when dealing with concrete knowledge is also consistent with the theory. The experts' individual schemata are lesser discriminating (i.e., they contain fewer concrete values), so they necessarily access more abstract schemata. But as abstract schemata are leaner, they then have to access subschemata to verify the value of the attributes as stipulated by the facts that were presented to them (i.e., concrete knowledge). By doing so, alternative concepts or competing attribute values can be identified so that they may spend more time in understanding the domain. This explanation is consistent with findings in the domain of reading, writing, and complex systems [54,49,55,46].

The authors also report other interesting findings. For high uncertainty tasks, high-skilled users performed better when presented with declarative knowledge (schemata) than with procedural knowledge (scripts). Procedural knowledge (scripts) was more straightforward than declarative knowledge (schemata) when the task had low uncertainty. $^{6}$ When uncertainty is high, schemata are more powerful than scripts for extracting the right schema. But, when uncertainty is low, using a script that addresses concrete schemata seems to be the preferred strategy.

## 4.1.2. Fedorowicz et al. [63]

Fedorowicz et al. conducted an experiment with novice subjects using an expert system (ES). The aim of their study was to measure if there were any persistent effects in the knowledge of subjects after exposure to an expert system. The results show that the treatment group of subjects, who were exposed to the expert system: (1) had a steeper learning curve than the control group subjects, and (2) their performance remained superior to that of the control group subjects after the technology was withdrawn.

Rephrasing their findings, direct exposure to experts' knowledge as depicted in the ES resulted in the insertion of new schemata and scripts in the subjects' knowledge bases, or the refinement of existing knowledge. The control group subjects had not used the expert system and thus were not exposed to expert knowledge. Thus any additions to their knowledge base resulted from their own learning process.

The results are consistent with those reported in Ref. [64] from an experiment conducted by Larkin [45]. Though it could be argued that schemata were instantiated only at the lowest level in the case of the treatment group subjects, the number of problems administered to the subjects and additional evidence provided in Fedorowicz et al. tend to support the thesis that tuning of the treatment group subjects' knowledge bases took place as a result of the tasks. For instance, all 35 cases fell within a single domain of expertise. Common concepts could thus be retrieved in multiple problems therefore leading to the adjustment of schemata value domains.

Although the control group subjects solved the same problems as the treatment group subjects, they did not achieve the same level of performance. This suggests that exposure to expert knowledge seems to be more beneficial than personal problem-solving experience in restructuring the schemata base. The findings of Fedorowicz et al. can also be supported by anecdotal evidence from those who have been exposed to the influence of an expert through work relations.

The authors suggest that differences in the subjects' learning can also be due to feedback effects. The treatment group subjects received feedback from the system. The control group subjects did not receive any. Feedback, thus, may promote the adjustment of schemata attribute domains.

## 4.2. Experts in IS design

Evidence has been provided that experts have more abstract schemata than non-experts $[42,44,58]$ . Further, experience is known to contribute to the refinement of knowledge [31,32]. As experience is domain specific, there is reason to believe that individuals with the same level of experience may have differently configured schemata bases that depend on the scope of their experience, learning, expertise, and personal characteristics. (Very little is known about personal characteristics that either facilitate or hamper the development of expertise.) The studies in this section examine expert behavior in IS design, using traditional techniques. Although supporting radically different methodologies than OO, these studies demonstrate the differences in performance evident in expert-level systems development activities.

## 4.2.1. Mantha [65]

Mantha looked at comparable data flow and data structure approaches in the context of database design. Results suggest that designers using the data structure approach identify more entity views and more attributes than those who follow the data flow approach. Subjects in this experiment used their habitual approach, that is, those using the data flow method also used that method in their real jobs. The same was true for those using data structures. All subjects were expert IS professionals.

The results suggest differences in the contents of the subjects' schemata. As these subjects had been trained for years with specific approaches and as expertise is highly domain-specific, the results are not too surprising. In this experiment, it may be that subjects were just 'dumping' their schemata contents onto the problem they were asked to solve, as they all had experience developing similar applications.

From a schemata and scripts perspective, those using the data structure approach could be said to be more schemata-driven whereas those using the data flow approach were more scripts-driven. As data flow is more process-oriented and thus suggests movement, time and sequencing, it is reasonable to posit that designers following this approach were running through the model in their minds (simulation). This was also observed elsewhere $[59,60]$ . The subjects appear to have been running scripts to select schemata from their knowledge bases. If they were using scripts to drive their schemata search, it is possible that the subjects were searching for similar schemata.

On the other hand, subjects using the data structure approach were probably more inclined to instantiate and reproduce schemata than the sequences of events in scripts. Since schemata have knowledge of themselves and act as filters, their selection is more precise and accurate than when relying on scripts for the selection process since scripts mostly play a confirmatory role.

As the author hypothesizes, the type of formalism (system development methodology) used to represent the problem and the functions supported by such formalism are important factors in supporting an analyst's understanding of the system and his/her ability to produce higher quality designs. Analysts using the Data Flow Diagram (DFD) approach did not produce generalizable designs. Rather, they replicated the old system by creating a file for each of the forms to be produced by the system. Data structure analysts, on the other hand, produced designs of better quality. Since the methodology that they were employing better fits their knowledge structures (schemata), they produced generalizable designs that more accurately included appropriate attributes and views. The author himself contends that object orientation and semantic modelling seem to lead to more generalization while supporting specialization and to higher quality designs than data transformation-oriented methodologies such as DFD.

## 4.2.2. Vitalari [66]

Vitalari conducted an experiment where experienced analysts were asked to design an accounts receivable system. Subjects were categorized as high or low performers by their employers. Group-level differences in experience and/or expertise were not reported. The study aimed at eliciting the categories of knowledge that analysts recall while performing the task. The results suggest that: (1) some categories of knowledge were considered by both groups, and (2) differences between high-rated and low-rated analysts were noted, for instance, more abstract categories were used by the high-rated analysts.

From the theories' perspective, the two groups of subjects differed in terms of their schemata contents and schemata organization. The fact that those categorized as high-rated analysts used more abstract categories while performing the task suggests that their level of expertise is different from that of the low-rated analysts. This is consistent with the assertion that more expert individuals exhibit more abstract schemata.

Though statistical analysis of the data collected by Vitalari is not available, some interesting findings are worth reporting here. High-rated analysts tended to consider issues such as ‘types of reports’, ‘systems functions’, ‘organizational issues’ and ‘database issues’. Low-rated analysts were more inclined to care about ‘information specifics’ and ‘development issues’, suggesting that high-rated analysts were able to process more abstract concepts than low-rated analysts. This interpretation of the findings is again consistent with the proposed use of theories of schemata and scripts to understand human expertise.

Another striking difference between the low- and high-rated analysts is that high-rated analysts spent more time discussing the characteristics of the reports and were more concerned about the output of the system (and its use). It also seems that high-performers' knowledge bases reflect both breadth and depth (abstraction) as high-performers reported that they forced themselves to remain at higher levels of abstraction to avoid bias in their understanding of requirements.

## 4.2.3. Shoval and Even-Chaime [67]

Shoval and Even-Chaime conducted an experiment comparing two design methodologies with subjects of comparable level of expertise. The 26 subjects were graduate MIS students. The methodologies being compared were information analysis and normalization (which here is a structured analysis technique not to be confused with normalization in the context of the relational data model [68]) and information analysis. The relevant results were: (1) normalization produced higher quality designs, (2) normalization took less time than information analysis, and (3) normalization was preferred by the subjects over information analysis. Subjects had received equivalent training in both methods.

We note that information analysis produces a more abstract model. Subjects, here students who had completed a single course in system design, had not developed appropriately abstract schemata to represent these relationships well. Instead, due to their lack of expertise, their schemata base consists more or less of concrete schemata, representing concrete objects rather than principles or relationships as experts would have $[41,42,44,30]$ . It follows that normalization, which is less abstract than information analysis as it is not strictly based on relationships, was easier to use for the novice subjects. It also produced higher quality designs because subjects could use their existing schemata.

## 4.3. Database design

Where traditional development techniques focus on the ‘process’ component of a system design, database design research can tell us more about the data aspect. Both are integral parts of the OO methodology. Thus, the final set of examples explores differences between experts and novices in the context of database design. As will be seen, schemata and script theories also support an enriched explanation of these findings.

## 4.3.1. Batra and Davis [69]

Batra and Davis looked at the differences in data base design processes between novices and experts. The task involved a conceptual database model of a real business application. The results show that experts and novices tend to apply qualitatively different models to the task and that some aspects of the problem seem to be automated for experts. Experts were found to decompose the problem into smaller pieces and organize information in chunks before trying to map it into their own representations (a handwritten conceptual model). There is some evidence that experts were particularly concerned with getting the requirements right before solving the problem.

These results are easily supported by schemata theory. First, evidence has been provided that experts deal with the problems one piece at a time $[49]$ and that they try to fit incoming data to existing schemata $[61]$ . The notion of different models reported by Batra and Davis appears to be more of an issue of search direction or strategy (forward vs. backward reasoning) than of differentiable models. We suggest that experts, as supported by some reported protocols, were able to map part of the incoming information into already existing knowledge structures (schemata). Their findings about the experts being concerned with getting the right requirements are consistent with reported findings in cognitive psychology and cognitive sciences, and with the fact that experts need to discriminate among information more than novices to make it fit with their knowledge [58]. Coincidentally, this also supports the tendency of OO techniques to focus on requirements definition through the development of the object and dynamic models.

## 4.3.2. Prietula and March [60]

Prietula and March assessed differences in cognitive processes among three classes of subjects (experts, experienced students, and inexperienced students) while performing a physical database design task. The results suggest that the subjects used different strategies (e.g., breadth-first, depth-first) to understand the problems. A second result from the study is that the effect of experience was pronounced. (The authors used experience as a construct rather than expertise.) Another interesting finding is that experienced subjects tended to mentally execute their models while inexperienced and less-experienced subjects did not. The authors explain the differences found in the reasoning processes between experience levels by relying on the theory of mental models [26].

From a schemata perspective, there is evidence in some protocols reported in the article that subjects were dealing with knowledge structures (schemata and scripts) not mental models in the pure sense of Johnson-Laird's [26] definition. For example, this short excerpt from the original supports our point:

...I'm tempted to combine Policy and Policy Holder entities into one physical structure ... it would really speed up some of their retrieval times, I think. You wouldn't have to be going to two physical structures...

See Ref. [60], p. 305. This excerpt suggests the use of schemata and scripts rather than a mental model.

Additionally, changes in heuristic reasoning and strategy heuristics (as the authors define them) are good illustrations of differences in the schemata contents and problem strategies. This is consistent with previous findings about differences in schemata content and search strategies since, as discussed in Section 2, scripts may help in selecting the most appropriate schema and therefore would suggest to the subject a change in the direction of memory search and problem-solving behavior. Prietula and March's conclusion that experts were found to 'mentally execute' their model is compatible with Adelson and Soloway's [59] findings suggesting that experts also use scripts to understand the problem and to formulate their solution.

Since the task was to develop a physical model of the database, it is highly likely that the role of scripts was more important here than in other works reported earlier in this paper. When physically implementing a database, one of the primary concerns is to ensure proper system's response time. The designer must thus be able to 'simulate' the machine's behavior to evaluate the appropriateness of his physical model. This suggest high levels of use of scripts to fully evaluate the outcomes of the design.

## 4.4. Summary

These examples from the IS literature demonstrate that the theory of schemata and the theory of scripts can help to explain differences found in expert/novice performance of analysts and designers. The IS literature to date on differences in performance generally lacks adequate theoretical support. In this section, we have demonstrated that schemata and scripts are appropriate reference theories in supporting the findings in the IS literature that deals with differences in performance between experts and novices as well as in explaining differences in performance between methods used by designers having similar experience or expertise.

Although these articles do not specifically discuss the OO methodology, they do suggest that the methodology emphasizes many of the behaviors and preferences of experts. While lacking appropriate reference theories, these articles still recognize that differences in performance between subjects and the adequacy of systems development methodologies can be explained by relying on human knowledge constructs (expertise). Moreover several of the studies examined here focused on the same activities that comprise an OO model of a system, including both process and data modelling. In Section 5, we will look at the implications of the parallels we have identified with the OO methodologies.

## 5. IS expertise

Evidence has been provided in this paper that the theory of schemata and the theory of scripts can serve as reference theories in looking at the differences between experts and novices. Further evidence has been provided that these theories help our understanding of expertise in IS design for both experts and novices. Whereas the role of schemata is better supported in the literature, the role of scripts is not as clearly documented. There are indications, though, that scripts are activated in highly specific occasions such as computer programming and physical database design.

Expertise is enhanced by restructuring schemata as well as the ability to use scripts. In turn, schemata and scripts help to determine reasoning strategies, that is, strategies for memory retrieval, understanding of the problem, and solving the problem. The expertise of the individual determines how much time he or she takes to understand and represent the problem, how much time he or she will take performing the task, and the quality of the solution. These last three constructs are all performance constructs identified in the literature on expertise and are those measures of performance that can be assessed in external behavior.

## 5.1. Expectations for the OO paradigm

Expert analysts and designers apply their hierarchy of schemata to design problems by comparing observations to stored schemata and scripts of increasing abstraction. Experts, in particular, make use of scripts to confirm selected schemata and insure that their interpretation of the situation at hand is correct $[59,60]$ . It is only after a close fit is obtained between schemata and the real world that the analyst will move on to ‘solving’ the problem.

In essence, the expert is mentally creating an Object Model and a Dynamic Model of the world before beginning to address issues of implementation. The richness of the OO methodology gives the expert the latitude to comprehend and depict his or her observations without being tied to a particular solution approach. By combining object attributes and behaviors and by promoting the use of different kinds of associations similar to those proposed in theories of human knowledge, the OO methodology permits the expert to understand the whole picture instead of arbitrarily separating out objects from actions or activities concerning those objects. It also does not limit her/him to more restrictive types of associations. In addition, since the world is made up of complex objects, some of which are composite, OO, by directly supporting aggregation, helps designers in producing more accurate and fine-tuned models of reality.

Another major benefit of OO is that by giving so much flexibility to designers, it will likely promote higher quality designs. Experts frequently navigate across their knowledge base while at the understanding stage of the problem-solving process $[58]$ . They therefore naturally instantiate competing schemata, which force them to ask more questions $[49,50]$ thereby developing a more thorough understanding of the problem. As they ask more questions, they may trigger additional reasoning and interpretations from the users from whom they are collecting the requirements, again helping them refine their understanding of the problem and in turn their proposed solution. Designers are active agents in the systems design process in that they ‘interpret’ requirements according to their frames of reference and propose designs accordingly. One characteristic noted of experts is that they take a more holistic view of the problem and produce higher quality solutions than novices who take a more concrete and restrictive view of the problem. The more holistic view helps experts to make suggestions to users while eliciting requirements and to produce designs which are less likely to need maintenance soon. Therefore, by encouraging designers to take a more holistic stance and by forcing them to more adequately select and propose appropriate concepts (objects), the likelihood is that designs will be of higher quality.

The systems development process is a complex one. Systems reflect reality, and reality is made up of concrete, abstract, and composite concepts (objects). Knowledge structures, in particular schemata, support these various concepts $[14,15,30,17,29]$ . Schemata can represent concepts on all levels of abstraction. OO, in contrast to many other systems design methodologies, supports a wide range of objects (concepts) by integrating these objects into a single, unified, system model while using a compact and uniform notation. The Object Model directly supports complex associations (like aggregations) generalization (or inheritance) and linking associations. The Dynamic Model closely parallels scripts. It compliments schemata by enabling the sequencing of objects' interaction to be modeled. This parallels the role of scripts as we understand them in human cognitive processes. Thus, OO closely resembles human behavior. OO is, therefore, a promising methodology for supporting efficient and higher quality systems designs.

Traditional systems design methodologies either emphasize processes or information flows (e.g., Data Flow Diagrams) or data, such as entities and their relationships (e.g., Entity Relationship (ER) and Extended Entity Relationship (EER)). Extensions to the ER model now support classes (subclasses and superclasses) of entities recognizing in part that the world contains collections of similar entities. However, ER and EER [70] as well as other methodologies have a severe shortcoming: they provide generalization (and specialization) between groups of similar entities (or objects) but do not support entities (or objects) of varying nature $^{7}$ . OO addresses that shortcoming through the direct representation of aggregation in the object model while providing a more compact and precise notation. OO thus is able to represent or model the world more precisely. OO also lends to objects' local knowledge of themselves and encapsulates their behaviors at implementation time.

The range of OO tools beginning to be marketed provide the expert with the ability to maintain an image of the abstract relationships among objects and events that can be used to communicate and test the completeness and correctness of the expert's schemata. Some of these tools translate directly from the conceptual design of the Object Model into usable code, freeing the designer from detailed implementation concerns. These technologies are still being improved, but reactions among early users are extremely positive, and performance expectations are very high.

Somewhat like expert systems, the OO methodology can be used to transfer expertise to less-experienced designers. For example, an expert analyst may produce an Object Model that is later used by apprentices to develop related applications. OO proponents contend that the OO methodology will promote reusability. We propose that OO also contributes to the acquisition of expertise by documenting and sharing the modelling approach taken by those with considerable expertise in the domain. This approach certainly has the potential to speed up the learning process of novices, similar to how expert systems accelerate the learning of their users $[63,62]$ .

## 6. Conclusions and future research

The concept of Object Orientation is very appealing to many in the information systems field. Although it requires a radical shift from the traditional systems development paradigm, many have begun to embrace it. This paper explores the literature on knowledge representation and expertise in the cognitive sciences and in information systems to lend substance to the underlying OO approach. We show that OO closely parallels our current understanding of the concept of expert knowledge representation based on schemata and scripts, and thus is particularly attractive to individuals who are or aspire to be ‘expert’ systems developers. We then examine the IS literature on expertise and reinterpret findings to support our depiction of expertise within IS. The OO approach incorporates many of the characteristics of expert-level knowledge representation, which may explain its appeal to those in the systems development profession. We propose that the OO methodology also contributes to the acquisition of expertise by documenting and sharing the modelling approach of those with considerable IS design expertise. From our discussion, it follows that expert-level systems development behavior makes full use of the range of OO constructs.

We propose that experts will find the OO methodology to conform closely to their mental view of the world. For example, it allows them to represent more types of relationships than most other methodologies while using a more compact, clearer notation. We suggest that experts using these techniques will propose more complete and correct models of the world they observe, and that communication of their understanding of the world will be enhanced. In addition, novices will be able to learn from experts via the physical Object Model and Dynamic Model representations derived from the experts' schemata. Novices will also be able to reuse the experts' knowledge by adopting shared object and relationship definitions.

Experts may find the OO paradigm appealing and familiar, but it will still require them to learn new techniques and explicit documentation methodologies. As OO incorporates both process and data modelling, experts may even find themselves ‘un-learning’ methods stressing the separation of the two. Although OO is a more ‘natural’ way of observing and documenting reality, experience in traditional techniques may slow the learning process until the new paradigm is understood and accepted. Novices do not have the baggage of a traditional view of systems design, nor have they the experience that a systems view of the world brings with it. We believe that by first exposing novices to the OO methodology, IS novices’ learning will be facilitated and they will become experts much faster and with more ease than by exposing them to less ‘natural’ traditional systems design methodologies. This assertion should be readily testable in the laboratory.

Our contentions should be observable in practice as OO tools become adopted by more and more analysts and designers. OO proponents predict enormous savings in development and maintenance time due to the shared understanding and reusability of objects. OO implementation, although not specifically discussed in this paper, also captures some of the benefits of expert-level activity noted in the earlier sections ${}^{8}$ .

Findings from studies of human expertise suggest that experts take more time to understand the problem than novices since they take a more holistic view and ask more questions while processing a problem one piece at a time $[54,49,55,46]$ . The refinement of their knowledge bases (schemata abstraction) and their running of scripts to confirm their understanding explain this particular finding as demonstrated in this paper. However, experts take less time at the solving stage of the problem once they thoroughly understand it $[42,57,34,40]$ . A similar emphasis by the OO methodologies will likely exhibit different patterns of work behaviors than other systems design methodologies would encounter. A better understanding of the requirements should result. We believe, based on the cognitive models discussed in this paper, that more time will be spent at understanding the problem than with other systems design methodologies but that savings will be significant at the problem-solving stage and in maintenance activities since designs will be of higher quality. We encourage researchers to test these predictions in a controlled setting. The theories we present here will provide a good grounding on which to base this OO research.

The concepts presented herein form the basis of an extensive survey research project now underway. OO novices and experts are being asked to fill out a questionnaire about their experiences using this methodology and their perceptions about OO in comparison to other systems development methodologies. We also inquire about perceptions related to the use of OO in shortening the learning period of IS novices. This exploratory study will provide the basis for additional research into the impacts of OO on systems development, and the attainment of expertise by its users.

## References

[1] M. Bucken, IBM to unveil 'new' AD/Cycle, Software Magazine, September (1993) pp. 23–25.

[2] F.P. Brooks, No silver bullet: essence and accidents of software engineering, IEEE Computer 20 (1987) 10–19.

[3] W.M. Bulkeley, Bright outlook for artificial intelligence yields to slow growth and big cutbacks, Wall Street Journal, July 5, 1990, pp. B1, B3.

[4] M. Vizard, Vendors ally on object blueprint, Computerworld, July 5, 1993, p. 12.

[5] T. DeMarco, Structured Analysis and System Specification, Yourdan, NY, 1978.

[6] J. Martin, Information Engineering, Books I, II and III, Prentice-Hall, Englewood Cliffs, NJ, 1990.

[7] E. Yourdan, Modern Structured Analysis. Yourdan Press, Englewood Cliffs, NJ, 1989.

[8] E. Yourdan, L. Constantine, Structured Design: Fundamentals of a Discipline of Computer Programming, 2nd edn., Prentice-Hall, New York, 1979.

[9] R.G. Fichman, C.F. Kemerer, Object-oriented and conventional analysis and design methodologies: comparison and critique, IEEE Computer, October, 1992, pp. 22–39.

[10] M. Hanna, Can CASE bridge to object world?, Software Magazine, July, 1993, pp. 41–46.

[11] J. Rumbaugh, M. Blaha, W. Premerlani, F. Eddy, W. Lorensen, Object-oriented Modeling and Design, Prentice-Hall, Englewood Cliffs, NJ, 1991.

[12] M. Minsky. A framework for representing knowledge, in: P.H. Winston (Ed.), The Psychology of Computer Vision, McGraw-Hill, New York, NY, 1975.

[13] C.B. Mervis, E. Rosch, Categorization of natural objects, Ann. Rev. Psychol. 32 (1981) 89–115.

[14] F.C. Bartlett, Remembering, Cambridge Univ. Press, Cambridge, 1932.

[15] J. Piaget, La Naissance de l'Intelligence chez l'Enfant, Delachau et Niestle, Paris, France, 1936.

[16] D.E. Rumelhart, Understanding and summarizing brief stories, in: D. LaBerge, S.J. Samuels (Eds.), Basic Processes in Reading: Perception and Comprehension, Lawrence Erlbaum Associates, Hillsdale, NJ, 1976.

[17] D.E. Rumelhart, Schemata: The building blocks of cognition, in: R. Spiro, B. Bruce, W. Brewer (Eds.), Theoretical Issues in Reading Comprehension, Lawrence Erlbaum Associates, Hillsdale, NJ, 1980.

[18] R. Quillian, Semantic memory, in: M. Minsky (Ed.), Semantic Processing, MIT Press, Cambridge, MA, 1968.

[19] R.P. Abelson, Script processing in attitude formation and decision making, in: J.S. Carroll, J.W. Payne (Eds.). Cognition and Social Behavior, Lawrence Erlbaum Associates, Hillsdale, NJ, 1976.

[20] R.C. Schank, Conceptual Information Processing, Amsterdam, North Holland, 1975.

[21] R.C. Schank, R.P. Abelson, Scripts, Plans, Goals, and Understanding: An Inquiry into Human Knowledge Structures, Lawrence Erlbaum Associates, Hillsdale, NJ, 1977.

[22] J.R. Anderson (Ed.), Cognitive Skills and their Acquisition, Lawrence Erlbaum Associates, Hillsdale, NJ, 1981.

[23] J.R. Anderson, The Architecture of Cognition, Harvard University Press, Cambridge, MA, 1983.

[24] A. Newell, H.A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[25] K. Craik. The Nature of Explanation, Cambridge Univ. Press, Cambridge, England, 1943.

[26] P.N. Johnson-Laird, Mental models, in: M.I. Posner (Ed.), Foundations of Cognitive Science, MIT Press, Cambridge, MA, 1989, pp. 469–499.

[27] M.W. Eysenck, Human learning, in: K.J. Gilhooly (Ed.).

Human and Machine Problem Solving, Plenum, New York, 1989, pp. 289–315.

[28] J.M. Mandler, Categorical and schematic organization in memory, in: C.R. Puff (Ed.), Memory Organization and Structure, Academic Press, New York, NY, 1979, pp. 259–299.

[29] E.E. Smith, Concepts and induction, in: M.I. Posner (Ed.), Foundations of Cognitive Science, MIT Press, Cambridge, MA, 1989, pp. 501–526.

[30] P. Reimann, M.T.H. Chi, Human expertise, in: K.J. Gilhooly (Ed.), Human and Machine Problem Solving, Plenum, New York, 1989, pp. 161–191.

[31] J.L. Kolodner, R.L. Simpson Jr., Problem solving and dynamic memory, in: J.L. Kolodner, C.K. Riesbeck (Eds.), Experience, Memory and Reasoning, Lawrence Erlbaum Associates, Hillsdale, NJ, 1986, pp. 99–114.

[32] K. VanLehn, Problem solving and cognitive skill acquisition, in: M.I. Posner (Ed.), Foundations of Cognitive Science, MIT Press, Cambridge, MA, 1989, pp. 527–579.

[33] D.M. Berry, Academic Legitimacy of the Software Engineering Discipline, Technical Report CMU/SEI-92-TR-34, Software Engineering Institute, Carnegie-Mellon University, Pittsburgh, PA, November, 1992.

[34] V.L. Patel, G.J. Groen, The general and specific nature of medical expertise: a critical look, in: K.A. Ericsson, J. Smith (Eds.), Toward a General Theory of Expertise: Prospects and Limits, Cambridge Univ. Press, Cambridge, 1991, pp. 93–125.

[35] N. Charness, Expertise in chess: the balance between knowledge and search, in: K.A. Ericsson, J. Smith (Eds.), Toward a General Theory of Expertise: Prospects and Limits, Cambridge Univ. Press, Cambridge, 1991, pp. 39–63.

[36] W.G. Chase, H.A. Simon, Perception in chess, Cogn. Psychol. 4 (1973) 55–81.

[37] A. de Groot, Thought and Choice in Chess, The Hague, Mouton, Paris, France, 1978 (original work 1946).

[38] H.A. Simon, K. Gilmartin, A simulation of memory for chess position, Cogn. Psychol. 8 (1973) 165–190.

[39] K.B. McKeithen, J.S. Reitman, H.H. Rueter, S.C. Hirtle, Knowledge organization and skill differences in computer programmer, Cogn. Psychol. 13 (1981) 307–325.

[40] E. Soloway, B. Adelson, K. Ehrlich, Knowledge and processes in the comprehension of computer programs, in: M.T.H. Chi, R. Glaser, M.J. Farr (Eds.), The Nature of Expertise, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988, pp. 129–152.

[41] Y. Anzai, Learning and use of representations for physics expertise, in: K.A. Ericsson, J. Smith (Eds.), Toward a General Theory of Expertise: Prospects and Limits, Cambridge Univ. Press, Cambridge, 1991, pp. 64–92.

[42] M.T.H. Chi, P.J. Feltovich, R. Glaser, Categorization and representation of physics problems by experts and novices, Cogn. Sci. 5 (1981) 121–152.

[43] M.L. Gick, K.J. Holyoak, Schema induction and analogical transfer, Cogn. Psychol. 15 (1983) 1–38.

[44] J.H. Larkin, H.A. Simon, Why a diagram is (sometimes) worth ten thousand words, Cogn. Sci. 11 (1987) 65–99.

[45] J.H. Larkin, Problem solving in physics: structure, process, and learning, in: J.M. Scandura, C.J. Brainerd (Eds.), Structural/Process Models of Complex Human Behavior, Sijthoff and Noordhoff, Amsterdam, The Netherlands, 1978.

[46] M. Scardamalia, C. Bereiter, Literate expertise, in: K.A. Ericsson, J. Smith (Eds.), Toward a General Theory of Expertise: Prospects and Limits, Cambridge Univ. Press, Cambridge, 1991, pp. 172–194.

[47] W.G. Chase, K.A. Ericsson, Skill and working memory, in: G.H. Bower (Ed.), The Psychology of Learning and Motivation, Lawrence Erlbaum Associates, Hillsdale, NJ, 1982.

[48] K.A. Ericsson, P.G. Polson, Memory for restaurant orders, in: M.T.H. Chi, R. Glaser, M.J. Fass (Eds.), The Nature of Expertise, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988.

[49] D. Dörner, J. Schölkopf, Controlling complex systems; or, expertise as ‘Grandmother’s Know-How’, in: K.A. Ericsson, J. Smith (Eds.), Toward a General Theory of Expertise: Prospects and Limits, Cambridge Univ. Press, Cambridge, 1991, pp. 218–239.

[50] R. Glaser, M.T.H. Chi, Overview, in: M.T.H. Chi, R. Glaser, M.J. Fass (Eds.), The Nature of Expertise, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988.

[51] D.P. Simon, H.A. Simon, Individual differences in solving physics problems, in: R.S. Siegler (Ed.), Children's Thinking: What Develops?, Lawrence Erlbaum Associates, Hillsdale, NJ, 1978, pp. 325–348.

[52] E.J. Johnston, Expertise and decision under uncertainty: performance and process, in: M.T.H. Chi, R. Glaser, M.J. Fass (Eds.), The Nature of Expertise, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988, pp. 209–228.

[53] J. Shanteau, The psychology of experts: an alternative view, in: G. Wright, F. Bolger (Eds.), Expertise and Decision Support, Plenum, New York, 1992, pp. 11–23.

[54] C. Bereiter, M. Bird, Use of thinking aloud in identification and teaching of reading comprehension strategies, Cogn. Instruction 2 (2) (1985) 131–156.

[55] P. Johnson, P. Afflerbach, The process of constructing main ideas from text, Cogn. Instruction 2 (3) (1985) 207–232.

[56] M.T.H. Chi, R. Glaser, E. Rees, Expertise in problem solving, in: R.S. Sternberg (Ed.), Advances in the Psychology of Human Intelligence, Vol. 1, Lawrence Erlbaum Associates, Hillsdale, NJ, pp. 1–75.

[57] J. Larkin, J. McDermott, D.P. Simon, H.A. Simon, Expert and novice performance in solving physics problems, Science 208 (1980) 1335–1342.

[58] G.L. Murphy, J.C. Wright, Changes in conceptual structure with expertise: differences between real-world experts and novices, J. Exp. Psychol.: Learn. Mem. Cognition 10 (1984) 144–155.

[59] B. Adelson, E. Soloway, A model of software design, in: M.T.H. Chi, R. Glaser, M.J. Fass (Eds.), The Nature of Expertise, Lawrence Erlbaum Associates, Hillsdale, NJ, 1988, pp. 185–208.

[60] M.J. Prietula, S.T. March, Form and substance in physical database design: an empirical study, Information Systems Res. 2 (4) (1991) 287–313.

[61] M.T.H. Chi, M. Bassok, M.W. Lewis, P. Reimann, R. Glaser,

Self-explanations: how students study and use examples in learning to solve problems, Cogn. Sci. 13 (1989) 145–181.

[62] D.M. Lamberti, W.A. Wallace, Intelligent interface design: assessment of knowledge presentation in expert systems, MIS Quarterly 14 (3) (1990) 279–311.

[63] J. Fedorowicz, E. Oz, P. Berger, A learning curve analysis of expert system use, Decision Sci. 23 (4) (1992) 797–818.

[64] K.J. Gilhooly, A.J.K. Green, Learning problem-solving skills, in: A.M. Colley, J.R. Beech (Eds.), Acquisition and Performance of Cognitive Skills, Wiley, New York, NY. 1989, pp. 85–111.

[65] R.W. Mantha, Data flow and data structure modeling for database requirements determination: a comparative study, MIS Quarterly 11 (4) (1987) 531–545.

[66] N.P. Vitalari, Knowledge as a basis for expertise in systems analysis: an empirical study, MIS Quarterly 9 (3) (1985) 221–240.

[67] P. Shoval, M. Even-Chaime, Data Base Schema Design: An Experimental Comparison between Normalization and Information Analysis, Database, Spring 1987, pp. 30–39.

[68] E.F. Codd, A relational model for large data banks, Commun. ACM 13 (6) (1970).

[69] D. Batra, J.G. Davis, A Study of Conceptual Data Modeling in Database Design: Similarities and Differences Between Expert and Novice Designers, Proceedings of the 10th International Conference on Information Systems, Boston, MA, Dec. 1989, pp. 91–99.

[70] T.J. Teorey, D. Yang, J.P. Fry, A logical design methodology of relational databases using the extended entity relationship model, ACM Computing Surveys 18 (2) (1986) 197–222.

[71] R. Elmasri, S.B. Navathe, Fundamentals of Database Systems, 2nd edn., Benjamin/Cummings Publishing, Redwood City, CA, 1994.

![](/api/attachments/VY3HVPPH/fulltext/images/7f045027d775903f61b0f42937d6fbdd2697c3da7b11cccc23ddc135e94b3ccc.jpg)

Jane Fedorowicz is Associate Professor of Accountancy at Bentley College where she is teaching information systems courses. She received her M.S. and Ph.D. degrees in Systems Sciences from Carnegie-Mellon University. She has previously taught at Carnegie-Mellon University, Northwestern University, Boston University and the University of Massachusetts at Boston. Professor Fedorowicz currently serves as Associate Editor of Information Systems Re-

search. Her primary research interests involve the impact of information technologies on individuals and organizations. She has looked at the effects of technology introduction on the quality of work, the nature of work, individual learning curves, and individual information acquisition patterns. She is also looking at the parallels between OO and expert-level knowledge representation (from the cognitive sciences) and the perceived usefulness of OO by expert users. She has published in Decision Sciences, Journal of Management Information Systems, Information and Management, ACM Transactions on Database Systems, Communications of the ACM, Decision Support Systems, and many other venues.

![](/api/attachments/VY3HVPPH/fulltext/images/0231216448ffbaa654db0251ae55619cbf9afb4d6de6e28b4608b6c6f38bc088.jpg)

Alain O. Villeneuve is a doctoral student in Management Information Systems at Boston University. He is joining the Faculty at Université de Sherbrooke (Canada) in 1996. Mr. Villeneuve has over 20 years of work experience in the areas of systems and database design. He received a BBA degree in Finance from Université de Sherbrooke in 1976. His main research interests are in the areas of Expertise in Information Systems, Cognition, Database Design, Ob

ject Technology and Economic Impacts of Information Technology.
