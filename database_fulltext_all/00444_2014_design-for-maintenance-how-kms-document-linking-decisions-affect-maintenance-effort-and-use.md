---
otero_id: 444
otero_key: "U9HX2ZTG"
title: "Design for Maintenance: How Kms Document Linking Decisions Affect Maintenance Effort and Use"
authors: "Alan R Dennis; Binny M Samuel; Kelly McNamara"
year: "2014"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2014.5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# Design for maintenance: how KMS document linking decisions affect maintenance effort and use

Alan R Dennis<sup>1</sup>, Binny M Samuel<sup>2</sup>, Kelly McNamara<sup>3</sup>

<sup>1</sup>Department of Operations & Decision Technologies, Kelley School of Business, Indiana University, Bloomington, IN USA; <sup>2</sup>Information Systems, Richard Ivey Business School, Western University, London, Ontario, Canada; <sup>3</sup>University Information Technology Services, Indiana University, Bloomington, IN USA

Correspondence:

AR Dennis, Department of Operations & Decision Technologies, Kelley School of Business, Indiana University, 1309 East Tenth Street, Bloomington, IN 47405, USA

Tel: +(812) 855-2691;

E-mail: ardennis@indiana.edu

## Abstract

Information system maintenance is an important aspect of information system development, especially in systems that provide dynamic content, such as Web-based systems and Knowledge Management Systems (KMS). Design for Maintenance (DFM) is an approach that argues that maintenance effort should be considered during the design of information systems in addition to the usual system design considerations. This research examines how the design of links among knowledge documents in a KMS affects both their maintenance and use. We argue that providing links among knowledge documents increases the cost of maintenance because when a document changes, the documents that link to and from that document are more likely to need changes. At the same, linking knowledge documents makes it easier to locate useful knowledge and thus increases use. We examine this tension between use and maintenance using 10 years of data from a well-established KMS. Our results indicate that as the number of links among documents increases, both maintenance effort and use for these documents increase. Our analyses suggest two DFM principles for dynamic content in practice. First, knowledge coupling (i.e., linking) to documents internal to the KMS rather than sources external to the KMS better balances maintenance effort and use. Second, designing small, knowledge cohesive documents (e.g., 250–350 words) leads to the best balance between maintenance effort and use.

advance online publication, 29 April 2014;

<sup>Journal of Information T</sup>doi:10.1057/jit.2014.5

Keywords: knowledge management; knowledge design; knowledge maintenance; knowledge search; linking; links

## Introduction

nformation systems guidelines have encouraged the creation of systems that are highly evolvable (e.g., easy to maintain); however, modern information systems often fall short of this ideal (Mannaert et al., 2012). Currently, informa-Ition systems maintenance consumes 50–80% of IT budgets (Jarzabek, 1993; Shaft, 1995; van Vliet, 2008), and a recent survey of Chief Information Of<sup>fi</sup>cers found maintenance to be the second most important issue they faced (Evans, 2009). Maintenance has become increasingly important in recent years in part because of the rise of information systems that provide dynamic content such as Web 2.0 systems and Knowledge Management Systems (KMS) because both the software and the content they provide require ongoing maintenance.

Maintenance planning occasionally has been considered during software engineering to reduce maintenance costs and improve use (Boehm et al., 1978; Chung and do Prado Leite, 2009), but the maintenance of the dynamic content included in an information system has received little attention. The maintenance of dynamic content is at least as important – probably more important – than the maintenance of software because users of outdated content (e.g., knowledge documents in a KMS) would be led astray with inaccurate content (Desouza and Awazu, 2005). The need for regular maintenance of KMS documents is magni<sup>fi</sup>ed because knowledge is dynamic, and changes to it typically are exogenous to an organization in that the need for knowledge maintenance is often triggered by events or entities outside the organization (McInerney, 2002). For example, Microsoft develops a new version of Of<sup>fi</sup>ce, government regulations change, or Harvard Business Review publishes a new article that identi<sup>fi</sup>es a new management or marketing technique.

In the mid-1990s, Ford Motor Company made a decision to implement a Design for Maintenance (DFM) methodology (which they called ‘Design For Service’) that explicitly drew attention to the cost of maintaining a vehicles during the engineering design phase (Teresko, 1994). The inclusion of the DFM methodology and tools enabled Ford to take a broader perspective of the customer ownership experience to minimize the total cost of ownership (including maintenance costs) while maximizing overall customer satisfaction (Gof<sup>fi</sup>n, 2000). In a similar vein to the automotive industry, we believe that a DFM approach can improve the long-term effectiveness and ef<sup>fi</sup>ciency of information systems that provide dynamic content such as KMS and Web 2.0 applications. One of the critical <sup>fi</sup>rst steps in a DFM approach is understanding what elements affect the cost of maintenance and how to redesign the system to reduce maintenance costs with little negative impact on use.

In this paper, we take some <sup>fi</sup>rst steps in a DFM strategy and focus on one type of information system that provides dynamic content: a KMS. We investigate one knowledge design factor that affects both the maintenance and use of dynamic content in a KMS: the links among knowledge documents (Marchionini and Schneiderman, 1988). We argue that increasing the links among knowledge documents will increase their use by making documents easier to <sup>fi</sup>nd. At the same time, we argue that increasing the links among documents will increase the maintenance effort because as one document changes, it is more likely to trigger changes in documents that it links to and link to it. We examine this tension between DFM and Design For Use (DFU) by examining the effects of links on the 10-year history of maintenance and use of a KMS that has over 7000 knowledge documents.

## Prior research and theory

## Knowledge management systems

Many <sup>fi</sup>rms have implemented KMS in response to the strategic importance of organizational knowledge management (Jennex et al., 2012) and much research exists that demonstrates that the use of a KMS can help an organization manage its organizational knowledge processes (Zyngier and Burstein, 2012) (see Alavi and Leidner, 2001 for a review). One of the <sup>fi</sup>rst decisions organizations make to gain bene<sup>fi</sup>ts from the use of a KMS is the type of knowledge to store within the KMS, whether codi<sup>fi</sup>cation-based, personalization-based, or some combination of the two depending on the knowledge management strategy (Hansen et al., 1999; Grover and Davenport, 2001). Codi<sup>fi</sup>cation-based knowledge is knowledge stored in a knowledge document that enables KMS users to consume the knowledge as needed, whereas personalizationbased knowledge helps KMS users <sup>fi</sup>nd individuals who have the needed knowledge. Most KMS today contain a blend of both codi<sup>fi</sup>cation-based and personalization-based knowledge (Hansen et al., 1999; Dennis and Vessey, 2005). The system we examine in this study adopts both, but we focus this current research on implications for the design of codi<sup>fi</sup>cation-based knowledge.

## KMS document design

The initial collection and design of knowledge that is needed before a codi<sup>fi</sup>cation-based KMS goes live can be very costly to an organization (Ko and Dennis, 2011). However, little is known about the impact of knowledge design decisions on maintenance and use. We de<sup>fi</sup>ne KMS DFM as considering how knowledge should be designed within a knowledge document in order to reduce its maintenance frequency and maintenance effort. Similarly, we de<sup>fi</sup>ne KMS DFU, the more common aspect, as designing a knowledge document to maximize its use.

## KMS document DFM

Just like any other information system, a KMS requires ongoing maintenance to sustain its use within the organization (Desouza and Awazu, 2005). Although maintenance is the longest phase of any information system (Dekleva, 1992; Swanson, 1999; Pressman, 2005), it is one of the least studied (Kemerer and Slaughter, 1999). Maintenance is necessary to keep the system up-to-date with the needs of the users. Traditional components of maintenance include enhancing existing functions of the system, adding new functionality, detecting and correcting defects, rewriting code, and program tuning (Edwards, 1984; Dekleva, 1992; Nosek and Palvia, 2006). However, the traditional components of maintenance do not explicitly acknowledge the need for maintenance of dynamic content within the system. In the context of this study, the maintenance of dynamic content is updating the codi<sup>fi</sup>ed knowledge within knowledge documents.

The maintenance of dynamic content is a necessary activity in<sup>fl</sup>uenced by (1) the frequency of change, and (2) the extent of change required per occurrence. The frequency of the maintenance of dynamic content is how often maintenance effort must be put forth to update the knowledge within a knowledge document. It tracks how often the knowledge changes. Frequency of maintenance only tells part of the story about the maintenance of dynamic content, however. At times, only a few words may need to be updated, and at other times an entire document may need to be updated. Therefore, we also consider the extent of change to a knowledge document as not all changes are similar. Conceptually, this is the number of lines changed per maintenance occurrence.

Consistent with prior research, we argue that maintenance of knowledge documents is a non-functional requirement of a system. Functional requirements of a system are the system features that perform speci<sup>fi</sup>c functions to satisfy the needs of its users, whereas non-functional requirements de<sup>fi</sup>ne how the system should be constructed (Chung and do Prado Leite, 2009). Incorporating the consideration of non-functional requirements, such as maintenance, during system design is not a novel concept (Juristo et al., 2007). However, ensuring that maintaining dynamic content is part of a system’s nonfunctional requirements is not common. In a KMS and other Web-based systems, the design of the content is vital because the content is the primary reason the system is used. Thus, we believe that DFM should be considered for knowledge documents during their design.

## KMS document DFU

The use of a KMS occurs after the KMS has been deployed in the organization and individuals, groups, and the organization incorporate its use into their work processes (Osborne, 1985; Dennis et al., 2009). Previous research has shown that KMS use can have positive impacts on individual, group, and organizational performance (Croasdell, 2001; Antony et al., 2005; Alavi et al., 2006; Zack et al., 2009; Ko and Dennis, 2011), and thus consideration for the DFU has been implicitly considered in prior KMS literature. However, we argue that DFU should be explicitly examined during knowledge documents design, speci<sup>fi</sup>cally in relationship to the knowledge document design factors that impact use.

The knowledge documents in a KMS are usually linked together in much the same way that Web pages are often linked together. Prior research has examined how links can impact the use of documents (e.g., Web pages) in Web-based systems. One stream of prior research has used links to analyze the structure of Websites. Their goal was to improve search algorithms and make information more easily disco verable (Pirolli et al., 1996; Albert et al., 1999; Chakrabarti et al., 1999; Kleinberg, 1999; Kao et al., 2004; Xue et al., 2005; Abedin and Sohrabi, 2009). Another stream of prior research suggests that spreading knowledge across linked pages (as opposed to presenting information in one long page for linear sequential reading) provides a natural way for individuals to explore and integrate information to create more coherent mental representations of knowledge in their own minds (Marchionini and Schneiderman, 1988; Foltz, 1996; Shapiro et al., 2004; Marchionini, 2006; Amadieu et al., 2009). Finally, studies have also found individuals perceived links to products that customers similar to themselves browsed to increase overall Website trust and purchase intentions (Krebs, 2000; Palmer et al., 2000; Park and Thelwall, 2003). Our current research focuses on the trade-offs between the maintenance and use of knowledge documents based on the links that tie the documents together.

## Potential trade-off between KMS DFM and KMS DFU

Maintenance effort is not a limitless resource that an organization can endlessly devote to the maintenance of dynamic content. An organization must control and carefully plan the amount of maintenance effort put forth (Moreton, 1990), and one approach is to design the knowledge within a knowledge document to be robust to exogenous changes. However, the speci<sup>fi</sup>c knowledge design features that are most suitable for minimizing the maintenance of dynamic content may or may not be the most suitable for knowledge document use. We are not aware of research to date that has looked at the trade-off between the maintenance of dynamic content vs its use in the design of knowledge documents. We seek to understand a balance that minimizes the maintenance of dynamic content with the least negative impact on its use.

## Links among documents affect maintenance and use

Knowledge documents often refer to other documents, in the same way that Web pages often provide links to other Web pages. Best practices in user navigation design suggest that every Web page that is part of a Website should provide the user a way to navigate to other relevant Web pages (Yu and Roh, 2002). Therefore, it is imperative to carefully design the knowledge documents with mechanisms by which the knowledge that is presented within one knowledge document can be connected to other relevant knowledge documents the user may desire.

![](/api/attachments/U9HX2ZTG/fulltext/images/2bada882d35d5f4e480a7bcef53380daf374f93aa2d85fa7e7865c37a55e6576.jpg)  
Knowledge document links.

Consistent with Web design, there are three types of links that are found in a knowledge document; In-Links, Internal Out-Links, and External Out-Links (Thelwall et al., 2005). Each of these terms is de<sup>fi</sup>ned from the perspective of a knowledge document; see Figure 1 for a pictorial representation of the different types of links. An In-Link is a connection that comes into a knowledge document from another knowledge document in the KMS. The document with an In-Link is the target of the link. An Internal Out-Link is a connection to a knowledge document from another knowledge document within the KMS. The document with an Internal Out-Link is the source of the link. An In-Link (i.e., target) for one knowledge document will be an Internal Out-Link (i.e., source) for another knowledge document. An External Out-Link is a connection to a knowledge document outside the KMS. In Figure 1, for example, Document 1 has an Internal Out-Link to Document 2 (which is thus simultaneously an In-Link from the perspective of Document 2). Document 2 in turn has an Internal Out-Link to Document 3 and an External Out-Link to a Web page.

## The impact of links on maintenance

Little research on dynamic content maintenance exists, and we found none on KMS dynamic content maintenance, thus we draw from software engineering (Boehm et al., 1976) to theorize about the impact of links on knowledge document maintenance. In software engineering, the software is broken up and designed as individual modules that are linked together to create one software package. In a similar vein, knowledge design involves breaking up knowledge into separate pieces (i.e., knowledge documents) and linking them together, as well as to documents on other topics within a KMS. As software engineering emphasizes quality design that will require minimal maintenance, a goal that is necessary for knowledge design, it seems <sup>fi</sup>tting to leverage the ideas from software engineering for dynamic content maintenance in KMS.

Stevens et al. (1974) de<sup>fi</sup>ned the software engineering concept of coupling that is widely used in software development (Hitz and Montazeri, 1995; Dobrica and Niemelä, 2002; Sartipi and Kontogiannis, 2003). The idea of coupling draws from Simon’s (1962) work on decomposable systems and the interactions among their subsystems. Coupling, as de<sup>fi</sup>ned in the software engineering literature, is a measure of the strength of association of one software module to another software module (Stevens et al., 1974; Eder et al., 1994; Papazoglou and van den Heuvel, 2007). Practically, coupling is the interrelationships of one software module to other software modules in terms of how much it relies on other software modules to accomplish its own task. Low coupling (i.e., fewer links) decreases maintenance effort (Darcy et al., 2005) because each software module becomes easier to understand, change, or correct without reference to other modules (Eder et al., 1994; Papazoglou and van den Heuvel, 2007; Chowdhury and Zulkernine, 2010). Since the original de<sup>fi</sup>nition of coupling, software engineering researchers have developed and re<sup>fi</sup>ned ways to measure and assess coupling in both procedural and object-oriented software development (Parnas, 1972; Kearney et al., 1986; Adamov and Richter, 1990; Berard, 1993; Bieman and Ott, 1994; Chidamber and Kemerer, 1994; Purao and Vaishnavi, 2003; Schach et al., 2003; Binkley and Schach, 2007; Sarkar et al., 2007; Gui and Scott, 2008; Gui and Scott, 2009; Újházi et al., 2010) while remaining faithful to the original notion of software coupling.

We adapt the concept of coupling from the software engineering literature for knowledge design<sup>1</sup> . We analogize each knowledge document to a single software module, and thus knowledge coupling becomes the interrelationships among the knowledge documents as represented by links among documents. However, unlike software engineering, it is not clear if low knowledge coupling is desired for knowledge design. Research on Web page links provides a starting point to understand the effects of knowledge coupling in KMS. On the Web, links often indicate that a document may contain information that authors of other documents think is useful (Ingwersen, 1998; Barjak et al., 2007). An author of a Web page may use an Out-Link to bolster the reputation and credibility of their page to show it was well researched (Barjak et al., 2007). In a KMS context, links may be used by the authors of knowledge documents for several reasons: (1) a next piece of knowledge to read if the user wants to continue expanding their knowledge, (2) an assumption the author can make regarding the background knowledge of the user, (3) an authoritative source of the knowledge, and/or 4) a place to learn more details that are tangential to the current knowledge document and so on (Barjak et al., 2007).

As an example, consider two coupled knowledge documents ‘A’ and ‘B’: imagine a user reading a knowledge document ‘A,’ and the user encounters a link to knowledge document ‘B.’ Knowledge document ‘B’ might provide more explanation about the knowledge necessary to understand knowledge document ‘A.’ Or perhaps, knowledge documents ‘A’ and ‘B’ are about the same topic and knowledge document ‘B’ is the next set of knowledge on the topic after knowledge document ‘A.’ Although either of the aforementioned coupled knowledge documents may increase the use of knowledge documents, it could also increase maintenance effort as there could be a ripple effect when updates in one document require updates in another document.

Although Internal Out-Links and External Out-Links differ with regard to whether the user remains in the KMS after clicking the link, conceptually they have the same effect on maintenance of dynamic content; thus we explain their effects collectively as an Out-Link. Prior research has also treated these two types of links similarly because they are similar in effect (Thelwall, 2003). An Out-Link is contained within a knowledge document and points to a target outside the current knowledge document. An author of a knowledge document will have to spend maintenance effort to ensure that the target of its Out-Link, post-knowledge design, is still consistent with the original intended use of the Out-Link. If the knowledge contained in a document that is the target of an Out-Link changes, the author of the knowledge document with the Out-Link must ensure that the Out-Link is still appropriate and that the description of the link in their document is also still appropriate. If the author is not made aware by the KMS system that the target document of their Out-Link has changed, then the author would need to set up regular intervals (e.g., monthly) to check for changes. This means that each Out-Link in a document will increase the frequency of maintenance changes. In Figure 1, for example, the author of Document 2 would be responsible for ensuring that the Out-Link to Document 3 (or the World Wide Web) is still appropriate with the original intentions for using it. Thus:

Hypothesis 1a: The more Internal Out-Links in a knowledge document, the more often it will be maintained.

Hypothesis 2a: The more External Out-Links in a knowledge document, the more often it will be maintained.

There is an initial startup effort required for any maintenance of dynamic content. Once a knowledge document is opened for maintenance of dynamic content, it becomes easier to make additional updates to the document. Thus, an increase in the frequency of maintenance of dynamic content will most likely lead to a higher extent of maintenance needed (i.e., more lines changed in the knowledge document). This is because any maintenance of dynamic content will be reviewed to ensure consistency with the rest of the knowledge document. During the review there will be an increased chance of additional updates. Thus, as a knowledge document with an Out-Link (either Internal or External) will have more frequent maintenance of dynamic content, it will also have more maintenance.

Hypothesis 1b: The more Internal Out-Links in a knowledge document, the greater the extent of its maintenance.

Hypothesis 2b: The more External Out-Links in a knowledge document, the greater the extent of its maintenance.

The effects of an In-Link on the maintenance of a knowledge document will depend upon how the document is managed. On the Web, pages are often managed by different people, so that a

Web page that contains an In-Link is managed separately from the Web page that contains the Out-Link. In this case, a document with an In-Link is beyond the control of the author who creates the source document, so the In-Link should neither increase nor decrease maintenance.

In a KMS, the situation is often different because one person or a team of people manages a set of related documents. The knowledge content is often deliberately designed to be spread across several documents that are linked together and managed as a group (Marchionini and Schneiderman, 1988; Foltz, 1996; Shapiro et al., 2004; Marchionini, 2006; Amadieu et al., 2009). In this case, the author of a source document is often the author of the document that contains the In-Link. When changes are made to either document, both documents will be checked to ensure the changes are appropriate. This means that in Figure 1, there may be a ripple effect so that if Document 1 is changed, Document 2 may be checked to ensure consistency. This would be re<sup>fl</sup>ected as an increased maintenance effort for the document containing In-Links.

Our hypotheses thus hinge on the extent to which the same person or team manages the related documents that contain the Internal Out-Links and the corresponding documents with the In-Links. We believe that in most KMS, a meaningful proportion of linked documents would be managed by the same person or team. Therefore, we argue that In-Links will increase maintenance. Thus:

Hypothesis 3a: The more In-Links in a knowledge document, the more often it will be maintained.

Hypothesis 3b: The more In-Links in a knowledge document, the greater the extent of its maintenance.

## The impact of links on use

In our search of prior research, we found no research connecting the use of a knowledge document with links to or from it. Thus to help theorize about the effect of links on the use of knowledge documents, we borrow from research that has studied quantitative aspects of the construction and use of information resources on the Web (Almind and Ingwersen, 1997; Björneborn and Ingwersen, 2004). This prior research has often examined the links across Web pages of different domains (Tang and Thelwall, 2008), but our research focuses on the links within the same KMS.

The goal of KMS is to provide individuals timely access to knowledge that will help overcome knowledge gaps, thus enabling the individual to complete a desired task more effectively and ef<sup>fi</sup>ciently (Pfeffer and Sutton, 2000; Alavi and Leidner, 2001; Markus, 2001). A KMS is used to acquire knowledge to complete a task and is not used to do the actual work needed to complete the task. The primary way users interact with most KMS includes searching for knowledge, reviewing search results, and opening knowledge documents to <sup>fi</sup>nd the speci<sup>fi</sup>c knowledge needed (Teece, 1998; Alavi and Tiwana, 2002; Ko and Dennis, 2011). The use of a system can be quanti<sup>fi</sup>ed in many ways (Burton-Jones and Straub, 2006). Following prior KMS research, we limit our de<sup>fi</sup>nition of KMS use to one facet of overall KMS use – users actually opening a knowledge document (Jennex et al., 2008; Ko and Dennis, 2011). Thus we ignore other behaviors (such as searching) that are external to the actual reading of KMS documents. In general (with obvious exceptions), when a knowledge document is opened, it is read, its knowledge is assessed and perhaps used, and bene<sup>fi</sup>ts are accrued (Ko and Dennis, 2011).

There are two main mechanisms by which individuals navigate knowledge documents in a KMS: (1) keyword search and (2) browsing from another knowledge document (Albert et al., 1999; Kaushik, 2010). With a keyword search, a user types keywords into the KMS search engine and it retrieves documents most relevant to the entered words based on the search algorithm in the KMS. This is similar to using Google or other search engines to <sup>fi</sup>nd pages on Web. With browsing, users navigate from document to document based on the links contained in those documents, in much the same manner as using links on the Web to move from Web page to Web page.

When a keyword search is employed by a user, we argue that an Out-Link (whether to documents internal to the KMS or external to it on the Web) will increase the probability of the knowledge document being found by the search engine. All the rendered text of a knowledge document is examined during a search, and an Out-Link will include text that reveals the goal/purpose of the Out-Link’s target knowledge document; at a minimum a number of keywords that might be found during a search. For example, consider an Out-Link from the knowledge document ‘Information systems’ to ‘Database management system’ on http://wikipedia .org. The Out-Link not only has the text surrounding it that brie<sup>fl</sup>y describes a database management system, but the Out-Link itself also contains the words ‘Database management system,’ for example, http://en.wikipedia.org/wiki/ Database\_management\_system. Thus someone searching a KMS for relevant knowledge (in our example, ‘Database management system’) might be led to the source knowledge document (in our example, ‘Information systems’) because of the inclusion of an Out-Link in the source knowledge document.

Hypothesis 1c: The more Internal Out-Links in a knowledge document, the more often it will be used.

Hypothesis 2c: The more External Out-Links in a knowledge document, the more often it will be used.

Similarly, a KMS document with an In-Link will likely see increased use for two distinct reasons. First, an In-Link will increase the chance that an individual browsing a knowledge document that is the source of the In-Link will open the knowledge document that contains the In-Link because the source page is explicitly recommending the target page for some reason, and if that reason is suf<sup>fi</sup>ciently compelling, the user will follow the link and open the target page. Second, Web search engines often use the number of In-Links as a factor in deciding what pages are the most relevant and should be displayed on the <sup>fi</sup>rst page of results because a high number of In-Links to a document is often an indication of a higher quality document (Tang and Thelwall, 2008). If the KMS search engine is designed like Web search engines (and many are), a document that is the target of many other document links is likely to be rated as more relevant to the search terms than another document containing the search terms that is the target of a few or no other documents. Thus:

Hypothesis 3c: The more In-Links in a knowledge document, the more often it will be used.

## Method

We conducted a <sup>fi</sup>eld study at a large state university whose KMS, called the Knowledge Base or KB for short, has won numerous awards (Boling et al., 2000). We have personal knowledge of the KB as users and we also interviewed the KB managers. However, our primary focus is quantitative. The next section provides brief background information on the KB, and we then discuss the data we used in our study.

## The knowledge base

The KB is a pervasive Web-based tool that plays a vital role in supporting the performance of IT support employees 24×7 at the university. The KB is an institutionalized system that has been in existence for over 10 years and currently provides access to over 7000 knowledge documents. The KB is operated by a central IT department, but knowledge for the knowledge documents comes from numerous subject matter experts at the university. In addition to IT support employees, the KB is also used by faculty, staff, students, and people all over the world seeking IT support solutions without the intervention of an IT support staff. Users primarily interact with the KB via a text-based search, and the search page is the default page that loads when one types the URL of the KB.

## Data

We examined the data from 10 years of KB operation, but our analyses are constrained by the data we were permitted to access. The dataset contained data for 7348 documents that were currently active in the KB. Over the 10-year history of the KB, some documents have come and gone; these documents are not included in our analyses because the dataset contained data only for the currently active documents. The oldest document was 9.35 years old and the newest just over 6 months old. The mean age was 5½ years (standard deviation 3 years) and a knowledge document changed (i.e., was edited) on average every 6 months.

## Dependent variables

We have two sets of dependent variables: maintenance effort and usage. As part of its regular operation, the KB tracks all accesses, both write and read. We used the write data as our maintenance data and the read data as our usage data.

The KB tracks two separate measures of maintenance effort. The <sup>fi</sup>rst is the total number of times a document has been changed (i.e., edited) over its life. The second is the total number of lines that have been changed (i.e., edited). We used both measures; the number of changes is a proxy for the frequency of change and the number of lines is a proxy for the extent of those changes. Our measures are therefore the average number of changes per year calculated as total number of times a document was changed (i.e., edited) divided by its age in years (to compensate for the fact that different documents are different ages), and the average number of lines changed (i.e., edited) per year calculated as total number of lines changed divided by its age in years. The KB uses an opensource version control software known as CVS to edit their documents, which de<sup>fi</sup>nes a line to be 80 characters (or less if it is the end of a paragraph).

Every time a document in the KB was accessed, it was counted as usage. Our measure of use is therefore the number of times a document was accessed per year, calculated as total number of times a document was accessed divided by its age in years. This measure suffers from the limitation that an access does not mean the knowledge in the document is actually used, but it is the best proxy for use (Ko and Dennis, 2011). Although frequency of use does not capture all the complexity for why an individual might use a knowledge document (e.g., relevance of the knowledge, timeliness of the knowledge, comprehensiveness of the knowledge and so on), it is a reasonable <sup>fi</sup>rst step toward understanding the phenomenon of usage.

## Independent variables

Our independent variables were the links among the documents as recorded by the KB software itself. All links to and from documents are recorded by the KB software. For each document, the number of In-Links is the number of source documents in the KB that refer to it. The number of Internal Out-Links is the number of target documents in the KB that are referred to by this document. The number of External Out-Links is the number of target documents on the Web that are referred to by this document.

One limitation to our data is that we have information about links (and the control variables that follow) for only the current state of the document. We expect that a document changes over its life, sometimes adding links, sometimes removing links, as the knowledge it contains evolves. Thus current links are only a proxy for a document’s links over time. These changes over time therefore introduce some measurement error into our model as we have no way to determine the previous links of the document. This error will reduce the statistical signi<sup>fi</sup>cance of our model because large changes in links will weaken the relationship between the current links in the document and the usage and maintenance effort<sup>2</sup>. This is also true for the other variables below.

## Control variables

We included the size of the knowledge document as a control variable, because all things being equal, larger documents likely contain more content and thus are more likely to attract use and need changes. Using size as a control is also consistent with prior research that has used the size as a control when studying the effect of links (Tang and Thelwall, 2008). Size is simply the number of bytes of text in the document, measured in 1000s of bytes (i.e., a size of 1.23 means the document is 1230 bytes in size). The size excludes the size of links or images and is just the number of bytes of text in the document.

The knowledge topic itself is also likely to have an impact on both its usage and the effort to maintain it; some topics are more often the subject of KB searches and some topics change more often. The KB uses two variables to classify the type of knowledge: audience and owner. These classi<sup>fi</sup>cations are for data maintenance purposes and do not affect document search. We included both categorical variables in our model.

Audience, as the name suggests, was the intended target audience for the document. There were 16 different audience codes, but the vast majority of documents (85.70%) had an audience of all users. The next four most common audience codes were speci<sup>fi</sup>c organizational units at the university: the technical support center (6.12%), information systems department management (3.75%), information systems department staff (1.39%), and KB staff (1.03%).

Table 1 Descriptive statistics of the independent and dependent variables

<table><tr><td></td><td>Mean</td><td>Median</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>Changes per year</td><td>1.99</td><td>1.52</td><td>1.74</td><td>0.20</td><td>30.47</td></tr><tr><td>Lines changed per year</td><td>34.85</td><td>17.61</td><td>87.37</td><td>0</td><td>4344.72</td></tr><tr><td>Accesses per year</td><td>842.05</td><td>223.03</td><td>2414.38</td><td>0</td><td>90,562.23</td></tr><tr><td>Size (in KMS)</td><td>2.21</td><td>1.57</td><td>2.54</td><td>0.11</td><td>64.16</td></tr><tr><td>In-Links</td><td>3.86</td><td>2.00</td><td>6.46</td><td>0</td><td>155</td></tr><tr><td>Internal Out-Links</td><td>3.50</td><td>3.00</td><td>3.04</td><td>0</td><td>27</td></tr><tr><td>External Out-Links</td><td>0.90</td><td>0</td><td>2.87</td><td>0</td><td>115</td></tr></table>

Table 2 Correlations between the independent and dependent variables

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td colspan="7">1. Changes per year</td></tr><tr><td>2. Lines changed per year</td><td>0.753**</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Accesses per year</td><td>0.392**</td><td>0.312**</td><td></td><td></td><td></td><td></td></tr><tr><td>4. Size</td><td>0.233**</td><td>0.474**</td><td>0.177**</td><td></td><td></td><td></td></tr><tr><td>5. In-Links</td><td>0.465**</td><td>0.374**</td><td>0.387**</td><td>0.147**</td><td></td><td></td></tr><tr><td>6. Internal Out-Links</td><td>0.400**</td><td>0.294**</td><td>0.333**</td><td>0.115**</td><td>0.469**</td><td></td></tr><tr><td>7. External Out-Links</td><td>0.189**</td><td>0.196**</td><td>0.073**</td><td>0.243**</td><td>0.054**</td><td>-0.001</td></tr></table>

\*\*P<0.001.

Owner code is the organizational unit responsible for writing the knowledge document. There were 70 owner codes, primarily the different organizational units that provided information systems maintenances. The 10 largest owners were the PC support team (20.24%), the KB support team (12.55%), the Macintosh support team (8.45%), the UNIX support team (6.55%), the central business system support team (4.78%), the walk-in support desk (3.85%), the information systems department management team (3.76%), the learning management system support team (3.09%), the email support team (2.86%), and the statistical software support team (2.83%).

## Data analysis

Table 1 presents the descriptive statistics for the independent and dependent variables. Table 2 presents the correlations among the dependent and the independent variables. The dependent variables were count data and therefore were highly skewed and non-normal. Figure 2 presents histograms showing the distribution of the data; note that the scale on the different axes changes to better present the data. Kolmogorov– Smirnov (K-S) tests for normality were: changes per year (K-S (7348) = 0.345, P<0.001), lines changed per year (K-S(7348) = 0.364, P<0.001), and accesses per year (K-S(7348) = 0.161, P<0.001).

Therefore, rather than using traditional statistical analysis techniques that assume a normally distributed dependent variable, we used Generalized Linear Models (McCullagh and Nelder, 1989). Generalized Linear Models should not be confused with its far more commonly used cousin called General Linear Models (GLMs), which assumes a normally distributed dependent variable. Generalized Linear Models extends GLMs to the analysis of data that have a non-normally distributed dependent variable such as the count data in our study. We used the SPSS Generalized Linear Models module with a negative binomial distribution and a log link function, which is the form widely used for count data. We had SPSS estimate the ancillary parameter because Lagrange tests showed that the parameter was signi<sup>fi</sup>cantly different than one for all three dependent variables.

## Results

## Maintenance effort

A Generalized Linear Model with the number of changes per year as the dependent variable and the three hypothesized independent variables plus size, audience, and owner as control variables was signi<sup>fi</sup>cant $\begin{array} { r } { ( \chi ^ { 2 } \left( 9 1 \right) = 4 4 5 9 . 9 6 , } \end{array}$ P<0.001). Table 3 shows the statistical results for each factor in the model. All factors had signi<sup>fi</sup>cant effects on the number of changes per year: In-Links, Internal Out-Links, and External Out-Links. We note that size, audience, and owner were signi<sup>fi</sup>cant.

A Generalized Linear Model with the number of lines changed per year as the dependent variable and the three hypothesized independent variables plus size, audience, and owner as control variables was signi<sup>fi</sup>cant $\begin{array} { r } { ( \chi ^ { 2 } \ ( 9 1 ) = 4 9 5 7 . 5 5 . } \end{array}$ P<0.001). Table 3 shows the statistical results. All factors had signi<sup>fi</sup>cant effects on the number of lines changed per year: In-Links, Internal Out-Links, and External Out-Links. Once again, size, audience, and owner were signi<sup>fi</sup>cant.

The pattern of results for both dependent variables was the same. We conclude that Hypotheses1a and 1b (Internal Out-Links increase maintenance) and Hypotheses 2a and 2b (External Out-Links increase maintenance) are supported.

![](/api/attachments/U9HX2ZTG/fulltext/images/6f80123fdb018e889f277ff07f562e72a70e7b09ef07dc3a06de933b6aeb32fb.jpg)

b  
![](/api/attachments/U9HX2ZTG/fulltext/images/15f52a3bbca90b20147831ccc4fa47569561a02efc4c1e61b935dffab37753cf.jpg)

![](/api/attachments/U9HX2ZTG/fulltext/images/d46a87927ff33380c0b632ab76426e033e694eeff84d07e8249d2415d6bcb3ea.jpg)  
Distribution of data.

Table 3 Statistical results and parameter estimates for maintenance effort

<table><tr><td rowspan="2">Factor</td><td colspan="3">Number of changes per year</td><td colspan="3">Number of lines changed per year</td></tr><tr><td> $\beta$ </td><td> $\chi^2$ </td><td>P-value</td><td> $\beta$ </td><td> $\chi^2$ </td><td>P-value</td></tr><tr><td>In-Links</td><td>0.030</td><td>536.63</td><td>&lt;0.001</td><td>0.039</td><td>330.31</td><td>&lt;0.001</td></tr><tr><td>Internal Out-Links</td><td>0.039</td><td>240.21</td><td>&lt;0.001</td><td>0.065</td><td>124.76</td><td>&lt;0.001</td></tr><tr><td>External Out-Links</td><td>0.030</td><td>102.24</td><td>&lt;0.001</td><td>0.061</td><td>7.72</td><td>0.005</td></tr><tr><td>Size</td><td>0.044</td><td>186.60</td><td>&lt;0.001</td><td>0.754</td><td>1241.72</td><td>&lt;0.001</td></tr><tr><td>Audience</td><td>Categorical</td><td>254.04</td><td>&lt;0.001</td><td>Categorical</td><td>213.68</td><td>&lt;0.001</td></tr><tr><td>Owner</td><td>Categorical</td><td>1045.21</td><td>&lt;0.001</td><td>Categorical</td><td>830.90</td><td>&lt;0.001</td></tr></table>

Table 4 Statistical results and parameter estimates for usage

<table><tr><td rowspan="2">Factor</td><td colspan="3">Number of accesses per year</td></tr><tr><td> $\beta$ </td><td> $\chi^2$ </td><td>P-value</td></tr><tr><td>In-Links</td><td>0.096</td><td>544.99</td><td>&lt;0.001</td></tr><tr><td>Internal Out-Links</td><td>0.101</td><td>262.44</td><td>&lt;0.001</td></tr><tr><td>External Out-Links</td><td>0.052</td><td>29.45</td><td>&lt;0.001</td></tr><tr><td>Size</td><td>0.103</td><td>150.38</td><td>&lt;0.001</td></tr><tr><td>Audience</td><td>Categorical</td><td>1660.62</td><td>&lt;0.001</td></tr><tr><td>Owner</td><td>Categorical</td><td>1955.38</td><td>&lt;0.001</td></tr></table>

Similarly, we conclude that Hypotheses 3a and 3b (In-Links increase maintenance) are supported.

## Usage

A Generalized Linear Model with usage as the dependent variable and the three hypothesized independent variables plus size, audience, and owner as control variables was signi<sup>fi</sup>cant $( \chi ^ { 2 } \ ( 9 1 ) = 6 1 1 4 . 8 3 , P < 0 . 0 0 1 )$

Table 4 shows the statistical results for each factor in the model. The number of In-Links, Internal Out-Links, and External Out-Links signi<sup>fi</sup>cantly affected the usage of a document. As an aside, we note that both the audience and the owner were signi<sup>fi</sup>cant factors predicting usage. The size of a document also signi<sup>fi</sup>cantly affected usage; larger documents were used more often than smaller documents. Therefore, we conclude that Hypotheses 1c and $_ { 2 c }$ (Out-Links increase use) and Hypothesis 3c (In-Links increase use) are supported.

## Evaluation of the models

One of the issues with the use of the Generalized Linear Model technique is that unlike its cousin (GLM) it does not produce absolute goodness-of-<sup>fi</sup>t statistics such as $R ^ { 2 } .$ . There are goodness-of-<sup>fi</sup>t statistics, but they only enable the user to test whether one model is a better <sup>fi</sup>t than another model. Therefore, we conducted two additional analyses to better evaluate the usefulness of the models.

First, we examined the relative goodness-of-<sup>fi</sup>t measures. We compared the full model of usage in Table 4 that had the three link variables (In-Links, Internal Out-Links, and External Out-Links) and three control variables (audience, owner, and size) against a control-only model that had just the three control variables. The full model was signi<sup>fi</sup>cantly better at the 0.001 level than the control-only model on all six measures of goodness of <sup>fi</sup>t (deviance, log likelihood, Akaike Information Criterion, Akaike information criterion corrected, Bayesian information criterion, and Consistent Akaike Information Criterion). We repeated this procedure with both maintenance models in Table 3, and again both full models were signi<sup>fi</sup>cantly better at the 0.001 level than both controlonly models on all six goodness-of-<sup>fi</sup>t measures.

Second, we used a technique from predictive analytics that is similar to a procedure suggested by Lee and Hubona (2009) to evaluate one aspect of the predictive accuracy of our <sup>fi</sup>ndings (Shmueli and Koppius, 2011). We were speci<sup>fi</sup>cally interested in assessing how well our empirical models predicted actual outcomes. We compared predictions made by the models with the actual data, to see how well the predictions matched reality. We conducted 10 trials for each of the three models in which we randomly selected 90% of the data to build a model that predicts maintenance and use. We then used this model to predict the data points in the remaining 10% of the data that had not been used to build the model (called the ‘hold-back sample’). Two measures are commonly used to assess how well the model predictions <sup>fi</sup>t the actual data in the hold-back sample. The <sup>fi</sup>rst is mean absolute error (MAE) which is the mean of the absolute value of each predicted value generated by the model minus the actual outcome value. The second is the linear correlation between the predicted values and the actual outcomes.

The results of this analysis are shown in Table 5. For the <sup>fi</sup>rst dependent variable, number of access per year, the MAE was 3955, which means that on average, the predicted value was within 3955 of the actual number of accesses per year. The mean correlation between predicted and actual was 0.607. The pattern is similar for the two maintenance variables – reasonably low MAEs and mean correlations of 0.594 and 0.667. Traditional regression and GLM analyses use $R ^ { 2 }$ as an absolute goodness-of-<sup>fi</sup>t measure. $R ^ { 2 }$ is the square of the correlation between the predicted values and the actual data and is calculated using the entire dataset without any holdback sample. We can compute an $r ^ { 2 }$ from our data in Table 5 that is analogous to the $R ^ { 2 ^ { \bullet } }$ from regression, except that our $r ^ { 2 }$ will be lower than the corresponding regression $\dot { R ^ { 2 } }$ because the predicted values in regression analysis use data that have been included in the regression model, whereas the predicted values in Table 5 are ‘new’ data in the hold-back sample that have not been used to build the model. The $r ^ { 2 }$ for our models are 37% for number of accesses, 35% for number of changes, and 44% for number of lines changed.

We repeated these analyses for the control-only models and found higher MAEs and lower mean correlations: 0.448 for usage, 0.465 for number of changes, and 0.578 for number of lines changed. These correspond to $r ^ { 2 }$ of 20%, 22%, and 33%, respectively. Thus the addition of the three link variables to the control variables increases $r ^ { 2 }$ by 11–17%. We believe that these results suggest that the full models are useful and that the addition of the three link variables above and beyond the three control variables improves the models’ usefulness.

Table 5 Analysis of predictions vs actual data

<table><tr><td></td><td>Mean</td><td>Trial 1</td><td>Trial 2</td><td>Trial 3</td><td>Trial 4</td><td>Trial 5</td><td>Trial 6</td><td>Trial 7</td><td>Trial 8</td><td>Trial 9</td><td>Trial 10</td></tr><tr><td colspan="12">Number of changes per year</td></tr><tr><td>MAE</td><td>4.66</td><td>55.36</td><td>44.38</td><td>44.37</td><td>44.77</td><td>44.84</td><td>44.66</td><td>44.98</td><td>44.62</td><td>44.15</td><td>44.46</td></tr><tr><td>Correlation</td><td>0.594</td><td>0.562</td><td>0.690</td><td>0.478</td><td>0.616</td><td>0.682</td><td>0.622</td><td>0.463</td><td>0.606</td><td>0.750</td><td>0.468</td></tr><tr><td colspan="12">Number of lines changed per year</td></tr><tr><td>MAE</td><td>80.24</td><td>880.36</td><td>778.89</td><td>888.03</td><td>777.22</td><td>882.14</td><td>771.33</td><td>887.18</td><td>881.07</td><td>776.16</td><td>880.03</td></tr><tr><td>Correlation</td><td>0.667</td><td>0.663</td><td>0.581</td><td>0.547</td><td>0.745</td><td>0.573</td><td>0.759</td><td>0.685</td><td>0.718</td><td>0.653</td><td>0.744</td></tr><tr><td colspan="12">Number of accesses per year</td></tr><tr><td>MAE</td><td>3955</td><td>44776</td><td>44160</td><td>33880</td><td>33676</td><td>44079</td><td>44103</td><td>33396</td><td>44022</td><td>44054</td><td>33411</td></tr><tr><td>Correlation</td><td>0.607</td><td>0.673</td><td>0.553</td><td>0.515</td><td>0.637</td><td>0.575</td><td>0.725</td><td>0.804</td><td>0.546</td><td>0.515</td><td>0.523</td></tr></table>

Note: MAE is Mean Absolute Error between predicted value and actual value in the test partition; Correlation is the correlation between the predicted value and the actual value in the test partition.

## Discussion

Maintenance of both the software and content provided by Web 2.0 information systems such as KMS is of paramount importance to organizations. In this current research, we introduced and examined the novel concept of the trade-off between how to design knowledge documents to minimize the maintenance effort of their content while maximizing their use. We argued that the links among documents in a KMS would in<sup>fl</sup>uence their effort to maintain and their use. Our results show as the number of In-Links increases, the more likely the document with In-Links will be changed and the more lines in the document will be changed. The same is true for use: as the number of In-Links increases, the more likely it is to be used. Out-Links (both those linking to internal KMS documents and those linking to Web page outside the KMS) also increased the amount of maintenance effort (both number of changes and lines changed) and use. Thus, we conclude that there is an inherent tension in the design of knowledge links to minimize maintenance effort vs maximize use.

Although it may seem counterintuitive that In-Links increased the maintenance effort, this may be one way in which KMS content differs from Web content. On the Web, pages that are linked together are often created by different authors. In contrast, in a KMS context, the author of one document may also be the author of another document that is linked to it, and may intentionally design the presentation of knowledge across several documents with a deliberate pattern of linking. In this case, when changes are made to one knowledge document, the changes may ripple across to other documents.

We can use the parameter estimates in Tables 3 and 4 to examine the trade-off between DFM and DFU in more detail. Figure 3 shows the relative beta weights for maintenance (number of changes and lines changed) and usage. The parameter estimates for maintenance on Internal Out-Links versus External Out-Links are very similar (.039 vs .030 for number of changes and .065 vs. .061 for number of lines). Thus, the effort to maintain a document does not change materially depending upon whether one chooses to add a link to an internal KMS document or a document on the Web; adding either type of link incurs about the same maintenance effort (not counting of course the need to maintain another document in the KMS).

For the sake of simplicity, we will focus on Internal Out-Links in our analysis of the trade-offs between maintenance and use. The parameter estimates in Tables 3 and 4 are log likelihoods. A parameter estimate of 0.039 for the number of maintenance changes per year means that on average, each additional Internal Out-Link added to a knowledge document (all other variables held constant) increases the number of changes per year by about 4% $( e ^ { 0 . 0 3 9 } = 1 . 0 4 0 )$ . There are an average of about 2 changes per document per year (although this is skewed; median 1.5), thus an extra 4% increase in the number of changes per year is quite small – 0.08 changes per year or about one more change per year for every 12 documents. Similarly, the parameter estimate for the number of lines changed per year suggests that on average, each additional Internal Out-Link increases the number of lines changed per year by 6.7% $( e ^ { 0 . 0 6 5 } = 1 . 0 6 7 )$ . There are an average of 35 lines changed per document per year (although this is highly skewed; median 18), hence this means each Internal Out-Link increases the average number of lines changed by about two lines per year.

Table 3 also shows that Internal Out-Links in<sup>fl</sup>uence the use of a document. It has a parameter estimate of 0.101, which means each Internal Out-Link increases the use of the source document (i.e., the document with the link pointing elsewhere) by about 10.6% $( e ^ { 0 . 1 0 1 } = 1 . 1 0 6 )$ . Average use is about 842 (see Table 1), which is also highly skewed (median 223). Thus on average, each Internal Out-Link increases use of the source document by about 89 uses per year. As an aside, we note that the results are about the same for the effect of an In-Link, because the parameter estimates are very similar. In-Links increase use by about 10.1% $( e ^ { 0 . 0 9 6 } = 1 . 1 0 1 )$ , the number of changes by about 3% $( e ^ { 0 . 0 3 0 } = \dot { 1 } . 0 3 0 )$ , and the number of lines changed by about 4% $( e ^ { 0 . 0 3 9 } = 1 . 0 4 0 )$ ).

These parameter estimates are only appropriate for this speci<sup>fi</sup>c KMS (i.e., the KB), but they present some interesting conclusions. Each additional Internal Out-Link in a document increases its use by about 10% or about 89 uses per year, while it adds about 6.7% to the maintenance cost (about two more lines changed per year). Each Internal Out-Link is also an In-Link in another document, and this In-Link increases the use of the target document by about 85 times per year and increases its maintenance by 4% (1.4 more lines changed per year).

![](/api/attachments/U9HX2ZTG/fulltext/images/9dc1f60b49d47054c5b559888526ba636362bdad318e24e8bfad2404803afbe5.jpg)  
Relative impact of links on maintenance and usage.

Putting these together, this means that adding a link between two KMS documents should on average increase use of these documents by about 174 uses per year and increase maintenance effort by about 3.7 lines per year, which translates to about 47 uses per line changed (i.e., 174/3.7). In contrast, adding an External Out-Link to a document will, on average, increase the use of that source document by about 5.3% $( e ^ { 0 . 0 5 2 } = 1 . 0 5 3 )$ or about 45 uses per year, and increase its maintenance by about 6.3% $( e ^ { 0 . 0 6 1 } = \dot { 1 } . 0 \dot { 6 } 3 )$ or about 2.2 lines per year. This translates to about 20 uses per line changed (i.e., 45/2.2 = 20.3).

One key question is whether adding links adds value. Our data suggest that links increase both maintenance effort and use. For the KMS in our study, adding an Internal Out-Link will generate on average about 46 additional uses for each extra line of maintenance effort. These numbers are appropriate only for the KMS in our study, but they provide some insight into what is ultimately a business decision. Is 46 uses worth one extra line of maintenance effort? In contrast, adding an External Out-Link will generate only 20 uses for each extra line of maintenance effort. This suggests a DFM principle: all things being equal, Internal Out-Links are preferred to External Out-Links. The implication is that adding a link to internal content adds more value for the same maintenance effort as adding an external link, and therefore internal links should be preferred to external links.

Our results also show that as the size of a knowledge document increases, more effort is required for its maintenance and it is more likely to be used. We conducted an additional analysis of our data to determine if there was some balance between these trade-offs between the increased maintenance and increased use associated with larger documents. We split the data into six categories based on the size of the knowledge document. We designed the categories so that there was approximately the same proportion of documents in each category.

![](/api/attachments/U9HX2ZTG/fulltext/images/29664e307cc3f430850627216e43975a2526d16bc105e172ca05ae08c9ed8ca1.jpg)  
Average number of uses per line changed.

Figure 4 shows the ratio of the average number of uses of a document per year to the average number of lines changed per year (i.e., use divided by lines changed). Higher numbers are better because they indicate more use for less maintenance effort. This <sup>fi</sup>gure shows that the ideal size for the documents in our data was 1501–2000 bytes (or about 250–330 words, assuming an average of <sup>fi</sup>ve letters and one space per word). Documents in this size range incurred about 50% less maintenance effort per use than very small or very large documents. The curve is <sup>fl</sup>at in the middle, meaning that, the ideal size is only 10–20% better than a wider middle range of 501–3000 bytes (80–500 words). These results apply only to the data in this KMS, but we believe that a general DFM principle of using small documents (100–500 words) rather than very small or large documents probably applies to many other KMS and other systems providing dynamic content.

## Implications for research

Software maintenance is an important topic that has in general received little attention (Taylor et al., 1997; Kemerer and Slaughter, 1999). The maintenance of the dynamic content in dynamic content systems such as KMS, Web pages, wikis, blogs, social networks and so on has been far less studied, yet this may be an even greater issue in a Web 2.0 world. Software maintenance is costly to organizations, typically accounting more than the original development cost (Dzidek et al., 2008). Changes to software tend to occur much less frequently than knowledge changes (e.g., in our context, every knowledge document was changed an average of two times per year). Thus the maintenance of dynamic content is a large and under-researched area. With our current research, we believe we have encouraged future researchers to expand the notion of software maintenance to incorporate dynamic content maintenance. We cannot be certain if our KMS is representative of all dynamic content systems; however, further research can test the limits of our <sup>fi</sup>ndings.

Dynamic content maintenance typically has not been considered as part of the scope of system maintenance (Swanson, 1999; Nosek and Palvia, 2006), but analogous to other system maintenance, dynamic content maintenance is an ongoing system activity that occurs during the operation of the system and is required to keep the system on par with the needs of the users. The maintenance of dynamic content in knowledge documents should be proactively considered during knowledge document design to better minimize the maintenance effort required. We have de<sup>fi</sup>ned dynamic content maintenance as a multi-dimensional construct comprising both the frequency maintenance and the extent of change. We believe that our results show the need for more research that considers DFM, particularly for dynamic content.

Our research also shows there is an inherent tension between knowledge design to decrease its maintenance and increase its use. Increasing the links among knowledge document increases maintenance, but also increases the use of that same knowledge. We believe that this core <sup>fi</sup>nding also contributes back to the Web literature we reviewed that primarily assessed the usefulness of links without consideration for their maintenance costs. We need more research to better understand this trade-off and to identify ways to improve the knowledge design to decrease knowledge docu ment maintenance effort without also decreasing its use.

Our analysis includes the links among documents and three control variables, but there are other factors that could also be examined including (1) additional design features of a knowledge document and (2) analysis by topic. In addition to knowledge design, there are other design features of a knowl edge document that may in<sup>fl</sup>uence its dynamic content maintenance effort and use. Consider, for example, how the inclusion of graphical displays of knowledge such as diagrams might impact knowledge document dynamic maintenance effort and use. Graphical displays of knowledge may enable a user to better understand the knowledge; however, do they increase the overall use of the knowledge document? More over, how does the inclusion of graphics impact maintenance effort? Graphical display design features, along with other design aspects of knowledge documents should be considered to understand their impact on maintenance and use of dynamic content.

In this research, we sought to generalize knowledge document design features across topics, and thus we treated topic as a control variable. Although our current research is an initial step to understand maintenance and use of dynamic content, we believe future research should delve into knowledge topic analysis. One approach might be to analyze topics by the frequency of updates that they receive. This would delineate maintenance of dynamic content on a continuum of how dynamic the knowledge for a given topic is from relatively dynamic content to relatively static knowledge. This insight could be used to understand if our <sup>fi</sup>ndings vary across relatively dynamic content and relatively static knowledge topics. Future research should consider both of these additional aforementioned knowledge document design factors and their impacts on maintenance of dynamic content and use as potential improvements to our research.

A key limitation of our research was that we used secondary data analysis, which provides a large sample of actual behavior in real life situations, unlike surveys that measure perceptions, lab experiments that use arti<sup>fi</sup>cial situations, or case studies that provide small samples. There are two important limitations of this research method. First, it is one step removed from the people who perform the behavior so it provides a good understanding of what happened, but not why. Second, we could only study the data collected by the system, which was primarily designed to enable knowledge management, not research. We used the number of changes, number of lines changed, and number of accesses, as our three dependent measures. The number of changes and number of lines changed are proxies for the effort or time taken to maintain documents. The KMS we studied did not record time as a direct measure of dynamic maintenance effort, and we believe knowing the actual amount of time taken per occurrence of maintenance could enable us to delve more deeply into how knowledge design affects the maintenance of dynamic content effort. Similarly, future research would bene<sup>fi</sup>t from a better characterization of the nature of use; did the users <sup>fi</sup>nd all KMS documents useful or were there important differences among documents?

## Implications for practice

Our research shows that there is an inherent tension between DFM and DFU. Concordant with software engineering research, our results in knowledge design indicate that fewer links mean less the maintenance. Conversely, as with the Web, more links mean more use. The question then is how best to act on the inherent tension caused by links to minimize the amount of maintenance effort while not impairing use of documents.

First, we do not suggest that links should be avoided in knowledge documents because links are found to increase use and provide a logical way to break up and connect different knowledge documents. Instead, the use of links should be carefully managed to ensure that links are added for a distinct purpose that will improve the use of knowledge. Links should not be added gratuitously, but rather with a clear understanding that each link will increase cost and should only be added if there is a well-understood usage bene<sup>fi</sup>t from adding the link.

Second, given the choice between using an Internal Out-Link vs External Out-Link, we suggest that Internal Out-Links are chosen. Although the process and effort to codify knowledge into a knowledge document is costly for organizations (Ko and Dennis, 2011), it is less costly from a long-term maintenance perspective if the knowledge is internalized into the organization vs relying on an external organization. If an External Out-Link is deemed appropriate, we suggest that the author or those responsible for a knowledge document with an External Out-Link incorporate regular checking intervals that ensure the External Out-Link is still appropriate (e.g., once a month).

Third, based on our interesting <sup>fi</sup>ndings regarding the size of documents, we believe that knowledge should be divided and packaged into separate documents so that each document is not too large or too small. In the KMS we studied, the target size turned out to be 100–500 words per document. Each KMS may be different but this could be a useful guideline for other KMS.

Finally, we also suggest that the cost for dynamic content maintenance be taken into account during the estimation of maintenance costs of a project. As suggested by systems analysis and design practice, aspects of systems maintenance are estimated during the project planning phase of a new system (Dennis et al., 2009). Even the bene<sup>fi</sup>ts of use are considered during the project planning phase to conduct some form of cost-bene<sup>fi</sup>t analysis regarding whether the system should be implemented. We believe that this type of maintenance cost will be particularly salient for Web 2.0 systems information systems that provide dynamic content such as KMS, Web pages, wikis, blogs, social networks and so on.

## Conclusion

Our research introduces the concept of DFM and examines the trade-off between DFM and DFU in the context of dynamic content in one KMS. We argued that the links among documents should affect both the maintenance effort and use of KMS documents. Our empirical <sup>fi</sup>ndings support this: knowledge documents with more links increased maintenance effort, but also increased usage. Linking to internal KMS documents rather than Web sources better balanced maintenance effort and use. Post-hoc analysis suggests that designing small knowledge documents (e.g., 250–350 words, perhaps as large as 500 words) led to the best balance between maintenance effort and use for the KMS in our study. We hope these results trigger more research into the costs and bene<sup>fi</sup>ts of designing for maintenance and lead to a better understanding of how to best balance the costs of maintenance against the bene<sup>fi</sup>ts of use for dynamic content. We believe these results offer some initial insight into these issues that will help KMS administrators design knowledge documents.

## Acknowledgements

We would like to thank Iris Vessey for her assistance with this research. We would also like to thank the reviewers and Senior Editor for helpful comments on previous drafts.

## Notes

1 We are not the <sup>fi</sup>rst to apply coupling outside the software engineering literature as it has been successfully applied in other <sup>fi</sup>elds such as work <sup>fl</sup>ow design (Reijers and Vanderfeesten, 2004).

2 The measurement error inherent in the data makes our model more conservative than it would be otherwise be. For example, we theorized that the number of In-Links increases use. If a document had few In-Links through most of its life until the last change that doubled this number, and we use this largest number in our statistical model, then this will weaken the likelihood that we will <sup>fi</sup>nd a relationship between In-Links and use.

## References

Abedin, B. and Sohrabi, B. (2009). Graph Theory Application and Web Page Ranking for Website Link Structure Improvement, Behaviour & Information Technology 28(1): 63–72.

Adamov, R. and Richter, L. (1990). A Proposal for Measuring the Structural Complexity of Programs, Journal of Systems and Software 12(1): 55–70.

Alavi, M., Kayworth, T. and Leidner, D. (2006). An Empirical Examination of the In<sup>fl</sup>uence of Organizational Culture on Knowledge Management Practices, Journal of Management Information Systems 22(3): 191–224.

Alavi, M. and Leidner, D.E. (2001). Knowledge Management and Knoweldge Management Systems: Conceptual fonudations and research issues, MIS Quarterly 25(1): 107–136.

Alavi, M. and Tiwana, A. (2002). Knowledge Integration in Virtual Teams: The potential role of KMS, Journal of the American Society for Information Science and Technology 53(12): 1029–1037.

Albert, R., Jeong, H. and Barabasi, A.L. (1999). Internet – Diameter of the world-wide web, Nature 401(6749): 130–131.

Almind, T.C. and Ingwersen, P. (1997). Informetric Analyses on the World Wide Web: Methodological approaches to ‘webometrics’, Journal of Documentation 53(4): 404–426

Amadieu, F., Tricot, A. and Mariné, C. (2009). Prior Knowledge in Learning from a Non-Linear Electronic Document: Disorientation and coherence of the reading sequences, Computers in Human Behavior 25(2): 381–388.

Antony, S., Batra, D. and Santhanam, R. (2005). The use of a Knowledge-Based System in Conceptual Data Modeling, Decision Support Systems 41(1): 176–188.

Barjak, F., Li, X. and Thelwall, M. (2007). Which Factors Explain the Web Impact of Scientists’ Personal Homepages? Journal of the American Society for Information Science and Technology 58(2): 200–211.

Berard, E.V. (1993). Essays on Object-Oriented Software Engineering. Vol. 1, Upper Saddle River, NJ: Prentice-Hall, ISBN:0-13-288895-5.

Bieman, J. and Ott, L. (1994). Measuring Functional Cohesion, IEEE Transactions on Software Engineering 20(8): 644–657.

Binkley, A.B. and Schach, S.R. (2007). A classical view of object-oriented cohesion and coupling, http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.44.5909.

Björneborn, L. and Ingwersen, P. (2004). Toward a Basic Framework for Webometrics, Journal of the American Society for Information Science and Technology 55(14): 1216–1227.

Boehm, B.W., Brown, J.R. and Lipow, M. (1976). Quantitative evaluation of software quality, 2nd International Conference on Software Engineering, Los Alamitos, CA: IEEE Computer Society Press, pp. 592–605.

Boehm, B., Brown, J., Kaspar, H., Lipow, M., MacLeod, G. and Merrit, M. (1978). Characteristics of Software Quality, Amsterdam: North-Holland Pub. Co.

Boling, E., Cai, W., Brown, J.P. and Bolte, J. (2000). Knowledge Base Development: The life cycle of an item in the Indiana university knowledge base, Technical Communication: Fourth Quarter 47(4): 530–543.

Burton-Jones, A. and Straub, D.W. (2006). Reconceptualizing System Usage: An approach and empirical test, Information Systems Research 17(3): 228–246.

Chakrabarti, S., Dom, B.E., Kumar, S.R., Raghavan, P., Rajagopalan, S., Tomkins, A., Gibson, D. and Kleinberg, J. (1999). Mining the Web’s Link Structure, Computer 32(8): 60–67.

Chidamber, S. and Kemerer, C. (1994). A Metrics Suite for Object Oriented Design, IEEE Transactions on Software Engineering 20(6): 476–493.

Chowdhury, I. and Zulkernine, M. (2010). Can complexity, Coupling, And Cohesion Metrics Be Used As Early Indicators Of Vulnerabilities?, in Proceedings of the 2010 ACM Symposium on Applied Computing, Sierre, Switzerland: ACM, pp. 1963–1969.

Chung, L. and Prado Leite, J. (2009). On Non-Functional Requirements in Software Engineering, in A. Borgida, V. Chaudhri, P. Giorgini and E. Yu (eds.) Conceptual Modeling: Foundations and Applications, Berlin Heidelberg: Springer, pp. 363–379.

Croasdell, D.T. (2001). It’s Role in Organizational Memory and Learning, Information Systems Management 18(1): 1–4.

Darcy, D.P., Kemerer, C.F., Slaughter, S.A. and Tomayko, J.E. (2005). The Structural Complexity of Software an Experimental Test, IEEE Transactions on Software Engineering 31(11): 982–995.

Dekleva, S.M. (1992). The In<sup>fl</sup>uence of the Information Systems Development Approach on Maintenance, MIS Quarterly 16(3): 355–372.

Dennis, A., Wixom, B.H. and Tegarden, D. (2009). System Analysis Design UML Version 2.0: An Object-Oriented Approach, Hoboken, NJ: John Wiley & Sons.

Dennis, A.R. and Vessey, I. (2005). Three Knowledge Management Strategies: Knowledge hierarchies, knowledge markets, and knowledge communities, MIS Quarterly Executive 4(4): 399–412.

Desouza, K.C. and Awazu, Y. (2005). Maintaining Knowledge Management Systems: A strategic imperative, Journal of the American Society for Information Science and Technology 56(7): 765–768.

Dobrica, L. and Niemelä, E. (2002). A Survey on Software Architecture Analysis Methods, IEEE Transactions on Software Engineering 28(7): 638–653.

Dzidek, W.J., Arisholm, E. and Briand, L.C. (2008). A Realistic Empirical Evaluation of the Costs and Bene<sup>fi</sup>ts of UML in Software Maintenance, IEEE Transactions on Software Engineering 34(3): 407–432.

Eder, J., Kappel, G. and Schreft, M. (1994). Coupling and Cohesion in Object-Oriented Systems, Technical Report, Austria: University of Klagenfurt.

Edwards, C. (1984). Information Systems Maintenance: An integrated perspective, MIS Quarterly 8(4): 237–256.

Evans, B. (2009). Global CIO: The top 10 CIO issues for 2010, in InformationWeek, Manhasset, NY: InformationWeek Business Technology Network, http://www .informationweek.com/security/risk-management/global-cio-the-top-10-cioissues-for-2010/d/d-id/1085701.

Foltz, P.W. (1996). Comprehension, Coherence and Strategies in Hpyertext and Linear Text, in J.-F. Rouet, J.J. Levonen, A.P. Dillon and R.J. Spiro (eds.) Hypertext and Cognition, Hillsdale, NJ: Lawrence Erlbaum Associates.

Gof<sup>fi</sup>n, K. (2000). Design for Supportability: Essential component of new product development, Research-Technology Management 43(2): 40–47.

Grover, V. and Davenport, T. (2001). General Perspectives on Knowledge Management: Fostering a research agenda, Journal of Management Information Systems 18(1): 5–21.

Gui, G. and Scott, P.D. (2008). New Coupling and Cohesion Metrics for Evaluation of Software Component Reusability, The 9th International Conference for Young Computer Scientists, 2008. ICYCS 2008, 18–21 November, 1181–1186.

Gui, G. and Scott, P.D. (2009). Measuring Software Component Reusability by Coupling and Cohesion Metrics, Journal of Computers 4(9): 797–805.

Hansen, M.T., Nohria, N. and Tierney, T. (1999). What’s your Strategy for Managing Knoweldge, Harvard Business Review (March-April): 106–116.

Hitz, M. and Montazeri, B. (1995). Measuring coupling and cohesion in objectoriented systems, In Proceedings of the International Symposium on Applied Corporate Computing, 75–76.

Ingwersen, P. (1998). The Calculation of Web Impact Factors, Journal of Documentation 54(2): 236–243.

Jarzabek, S. (1993). Domain Model-Driven Software Reengineering and Maintenance, Journal of Systems and Software 20(1): 37–51.

Jennex, M.E., Smolnik, S. and Croasdell, D. (2008). Towards Measuring Knowledge Management Success, Proceedings of the 41st Annual Hawaii International Conference on System Sciences, 7–10 January, Waikoloa, Big Island: Hawaii, 360.

Jennex, M.E., Smolnik, S. and Croasdell, D. (2012). Where to Look for Knowledge Management Success, 45th Hawaii International Conference on System Sciences (HICSS), 4–7 January, Maui, Hawaii, pp. 3969–3978.

Juristo, N., Moreno, A. and Sanchez-Segura, M.-I. (2007). Guidelines for Eliciting Usability Functionalities, IEEE Transactions on Software Engineering 33(11): 744–758.

Kao, H.Y., Lin, S.H., Ho, J.M. and Chen, M.S. (2004). Mining Web Informative Structures and Contents Based on Entropy Analysis, IEEE Transactions on Knowledge and Data Engineering 16(1): 41–55.

Kaushik, A. (2010). Web Analytics 2.0, Indianapolis, Indiana: Wiley Publishing.

Kearney, J., Sedlmeyer, R., Thompson, W., Gray, M. and Adler, M. (1986). Software Complexity Measurement, Communications of the ACM 29(11): 1050.

Kemerer, C. and Slaughter, S. (1999). An Empirical Approach to Studying Software Evolution, IEEE Transactions on Software Engineering 25(4): 493–509.

Kleinberg, J.M. Authoritative Sources in a Hyperlinked Environment (1999). Journal of the ACM 46(5): 604–632.

Ko, D.G. and Dennis, A.R. (2011). Pro<sup>fi</sup>ting from Knowledge Management: The impact of time and experience, Information Systems Research 22(1): 134–152.

Krebs, V. (2000). Working in the Connected World Book Network, International Association for Human Resource Information Management Journal 4(1): 87–90.

Lee, A.A. and Hubona, G.S. (2009). A Scientifc Basis for Rigor in Information Systems Research, MIS Quarterly 33(2): 237–262.

Mannaert, H., Verelst, J. and Ven, K. (2012). Towards Evolvable Software Architectures Based on Systems Theoretic Stability, Software: Practice and Experience 42(1): 89–116.

Marchionini, G. (2006). Exploratory Search: From <sup>fi</sup>nding to understanding, Communications of the ACM 49(4): 41–46.

Marchionini, G. and Schneiderman, B. (1988). Finding Facts vs. Browsing knowledge in Hypertext Systems, IEEE Computer 21(1): 70–80.

Markus, M.L. (2001). Toward a Theory of Knoweldge Reuse: Types of knoweldge reuse situations and factors in reuse success, Journal of Management Information Systems 18(1): 57–93.

McCullagh, P. and Nelder, J.A. (1989). Generalized Linear Models, 2nd edn London: Chapman and Hall.

McInerney, C. (2002). Knowledge Management and the Dynamic Nature of Knowledge, Journal of the American Society for Information Science and Technology 53(12): 1009–1018.

Moreton, R. (1990). A process Model for Software Maintenance, Journal of Information Technology. (Routledge, Ltd.) 5(2): 100.

Nosek, J. and Palvia, P. (2006). Software Maintenance Management: Changes in the last decade, Journal of Software Maintenance: Research and Practice 2(3): 157–174.

Osborne, W.M. (1985). Executive Guide to Software Maintenance, Special Publication 500–130, National Bureau of Standards.

Palmer, J.W., Bailey, J.P. and Faraj, S. (2000). The Role of Intermediaries in the Development of Trust on the WWW: The use and prominence of trusted third parties and privacy statements, Journal of Computer‐Mediated Communication 5(3).

Papazoglou, M.P. and van den Heuvel, W.J (2007). Business Process Development Life Cycle Methodology, Communications of the ACM 50(10): 79–85.

Park, H.W. and Thelwall, M. (2003). Hyperlink Analyses of the World Wide Web: A review, Journal of Computer‐Mediated Communication 8(4).

Parnas, D. (1972). A Technique for Software Module Speci<sup>fi</sup>cation with Examples, Communications of the ACM 15(5): 330–336.

Pirolli, P., Pitkow, J. and Rao, R. (1996). Silk from a Sow’s Ear: Extracting usable structures from the Web, Paper presented at the Proceedings of the SIGCHI conference on human factors in computing systems, Vancouver, British Columbia, Canada: Common ground, ACM.

Pfeffer, J. and Sutton, R.I. (2000). The Knowing-Doing Gap, Boston: Harvard Business School Press.

Pressman, R. (2005). Software Engineering: A Practitioner’s Approach, 6th edn, Boston, MA: McGraw-Hill.

Purao, S. and Vaishnavi, V. (2003). Product Metrics for Object-Oriented Systems, ACM Computing Surveys (CSUR) 35(2): 221.

Reijers, H. and Vanderfeesten, I.P. (2004). Cohesion and Coupling Metrics for Work<sup>fl</sup>ow Process Design, in J. Desel, B. Pernici and M. Weske (eds.) Business Process Management, Berlin Heidelberg: Springer, Vol. 3080, pp. 290–305.

Sarkar, S., Rama, G.M. and Kak, A.C. (2007). API-Based and Information-Theoretic Metrics for Measuring the Quality of Software Modularization, IEEE Transactions on Software Engineering 33(1): 14–32.

Sartipi, K. and Kontogiannis, K. (2003). A User-Assisted Approach to Component Clustering, Journal of Software Maintenance and Evolution: Research and Practice 15(4): 265–295.

Schach, S., Jin, B., Yu, L., Heller, G. and Offutt, J. (2003). Determining the Distribution of Maintenance Categories: Survey versus measurement, Empirical Software Engineering 8(4): 351–365.

Shaft, T. (1995). Helping Programmers Understand Computer Programs: The use of metacognition, ACM SIGMIS Database 26(4): 25–46.

Shapiro, A., Niederhauser, D. and Jonassen, D.H. (eds.) (2004). Learning From Hypertext: Research issues and <sup>fi</sup>ndings, Handbook of Research on Educational Communications and Technology. 2nd edn., Mahwah, NJ: Lawrence Erlbaum Associates Publishers, pp. 605–620.

Shmueli, G. and Koppius, O.R. (2011). Predictive Analytics in Information Systems Research, MIS Quarterly 35(3): 553–572.

Simon, H.A. (1962). The Architecture of Complexity, Proceedings of the American Philosophical Society American Philosophical Society, Vol. 106, 467–482.

Stevens, W.P., Myers, G.J. and Constantine, L.L. (1974). Structured Design, IBM Systems Journal 13(2): 115–139.

Swanson, E.B. (1999). IS ‘Maintainability’: Should it reduce the maintenance effort? SIGMIS Database 30(1): 65–76.

Tang, R. and Thelwall, M. (2008). A Hyperlink Analysis of US Public and Academic Libraries’ Web Sites, The Library Quarterly 78(4): 419–435.

Taylor, M., Moynihan, E. and Wood-Harper, T. (1997). Knowledge for Software Maintenance, Journal of Information Technology. (Routledge, Ltd.) 12(2): 155–166.

Teece, D.J. (1998). Capturing Value from Knowledge Assets: The new economy, markets for know-how, and intangible assets, California Management Review 40(3): 55–79.

Thelwall, M. (2003). Web Use and Peer Interconnectivity Metrics for Academic Web Sites, Journal of Information Science 29(1): 1–10.

Thelwall, M., Vaughan, L. and Bjorneborn, L. (2005). Webometrics, Annual Review of Information Science and Technology 39(1): 81–135.

Teresko, J. (1994). Service Now a Design Element, Industry Week 243(3): 51.

Újházi, B., Ferenc, R., Poshyvanyk, D. and Gyimóthy, T. (2010). New conceptual coupling and cohesion metrics for object-oriented systems, Source Code Analysis and Manipulation (SCAM), 10th IEEE Working Conference on IEEE, Timisoara, Romania, 33–42.

van Vliet, H. (2008). Software Engineering: Principles and Practice, 3rd edn, Hoboken, NJ: John Wiley & Sons.

Xue, G.-R., Yang, Q., Zeng, H.-J., Yu, Y. and Chen, Z. (2005). Exploiting the Hierarchical Structure for Link Analysis, Paper presented at the Proceedings of the 28th Annual International ACM SIGIR Conference on Research and development in Information Retrieval, Salvador, Brazil.

Yu, B.-M. and Roh, S.-Z. (2002). The Effects of Menu Design on Information Seeking Performance and User’s Attitude on the World Wide Web, Journal of the American Society for Information Science and Technology 53(11): 923–933.

Zack, M., McKeen, J. and Singh, S. (2009). Knowledge Management and Organizational Performance: An exploratory survey, Journal of Knowledge Management 13(6): 392–409.

Zyngier, S. and Burstein, F. (2012). Knowledge Management Governance: The road to continuous bene<sup>fi</sup>ts realization, Journal of Information Technology 27: 140–155.

## About the Authors

Alan R. Dennis is Professor of Information Systems and holds the John T. Chambers Chair of Internet Systems in the Kelley School of Business at Indiana University. He has written more than 150 research papers, and has won numerous awards for his theoretical and applied research. His research focuses on three main themes: the use of computer technologies to support team creativity and decision making; IS for the subconscious; and digital innovation. He was named a Fellow of the AIS in 2012. He is Editor-in-Chief of Foundations and Trends in Information Systems, and the Publisher of MIS Quarterly Executive. He has also written four books, two on data communications and networking, and two on systems analysis and design.

Binny M. Samuel is an Assistant Professor at the Ivey Business School at Western University. He earned his Ph.D. from the Kelley School of Business at Indiana University. He also holds a Bachelor of Science in Business and M.B.A, both with concentrations in Accounting and Information Systems. Prior to his doctoral education, he worked in IT roles at Ford Motor Company and at Indiana University. His current research interests focus on human factor issues to 1) improve how to effectively gather and analyze requirements for information systems in order to ensure they meet the needs of their users and 2) understand both facilitators and impediments to technology adoption.

Kelly McNamara works for Indiana University. Her research focuses on virtual teams and knowledge management. She has published articles in Information Systems Research, Journal of Management Information Systems, and Information Systems Management.
