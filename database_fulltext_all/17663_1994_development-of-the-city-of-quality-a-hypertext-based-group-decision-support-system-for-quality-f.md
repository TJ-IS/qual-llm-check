---
otero_id: 17663
otero_key: "36GW9S5S"
title: "Development of the city of quality: A hypertext-based group decision support system for quality function deployment"
authors: "Michael Wolfe"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90078-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Development of the city of quality:

A hypertext-based group decision support system for quality function deployment $^{1}$

Michael Wolfe

West Virginia University, Morgantown, WV, USA

The goal of the City of Quality system is to provide a group support system (GSS) for strategic planning of large-scale system development projects—a GSS which can significantly enhance these projects by providing tools for detailed requirements management, modeling, and analysis. It is an adaptation and implementation, using hypertext, of an ensemble of Japanese management techniques. The name of these techniques translates, roughly, as Quality Function Deployment (QFD), which is part of Total Quality Management (TQM). These manual techniques have been developed over a number of years as a response to the problems of developing large, complex systems that must satisfy conflicting requirements. They can be an important strategic planning tool. When successfully applied, QFD can save 50 percent of the system development costs; however, many organizations find it difficult to apply QFD successfully. Decision support system (DSS) and GSS technology can help address this problem. Hypertext tools allow the development of a low-cost DSS implementation to support QFD. This DSS can be extended to a GSS with network management software.

Keywords: Quality function deployment; QFD; Total quality management; TQM; Group support systems; Decision support systems; Group decision support systems; Strategic planning; Taguchi method.

Correspondence to: Michael Wolfe, Department of Management, West Virginia University, Morgantown, WV 26506-6025 $^{2}$ , USA.

## 1. Introduction

The acquisition of any large, complex system normally involves many decisions executed by a large number of people over a period of several years. The decisions are usually negotiated by user-sponsors, designers, and (sometimes) end-users. Individual end-users often have conflicting requirements for systems, such as high performance and low cost; hence, theory and practice lead to expectations of significant difficulties in reaching a satisfactory decision whenever multiple users and system developers are involved. This is true regardless of the type of system being developed.

An unstructured, manual approach to this process involves meetings between various designers and decision-makers and meetings to resolve conflicts until a system is completed many years after its inception. Such methods for communicating and resolving these conflicts are unreliable and awkward [24]. The resulting systems often fail to address important end-user requirements and frequently require substantial redesign expenditures.

A possible solution is to provide a structure within which the group may work to develop the system. Structure, with or without computer support, tends to enhance the quality of group processes [33]. A Japanese method for structuring the process is, roughly translated, Quality Function Deployment (QFD). QFD has existed since 1967 but has only recently received a great deal of attention as a managerial tool, following an article in the Harvard Business Review [12].

![](/api/attachments/36GW9S5S/fulltext/images/887207d96da893b1eacef731a167e16c0024dd0bf30dadd4599aa21e923eeafa.jpg)  
he worked for the Center for Cybernetic Studies at the University of Texas at Austin, where he did research on decision support systems for logistics. He has also worked for Rockwell International researching applications of artificial intelligence.

QFD is an integrated set of tools for recording user requirements, technical specifications that satisfy these requirements, any trade-offs that might be necessary among these technical specifications, and several other items that might help in the system development process. QFD has recently been recognized as an important strategic planning tool $[16]$ ; when successfully applied, it can result in a 50-percent savings in system development cost. However, although it has been investigated by more than 200 United States corporations, QFD has been successfully used at only a handful of these organizations $[41]$ . In addition, a recent survey of 90 organizations adopting the technology showed that 83-percent of those organizations modified the details of the procedure to fit their particular needs $[19]$ . While the structure provided by QFD can be of significant benefit, the tool can be very difficult to use. A decision support system (DSS) for QFD partially addresses this problem. One possible tool for developing such a DSS is hypertext, which also allows organizations to customize the tool easily.

Hypertext dates back many years (to the Memex system described by Bush in 1945) and has been used to implement other system development tools [7]. The contribution of the City of Quality (Coq) system is neither QFD nor hypertext but a melding of the two. Implementing QFD using hypertext allows the many persons involved in the system acquisition process to attach rationales, models, histories, computer-aided design (CAD) and computer-aided manufacturing (CAM) drawings, and voices wherever useful to the QFD documents; to retrieve relevant sections by author, keyword, or phrase; and to manage the overwhelming quantity of information associated with the development of a large, complex system that spans several years and involves a number of developers and end-users.

The purpose of this effort was to develop a complete set of QFD tools in hypertext, to research the potential of these tools to improve the life cycle of some large systems, and to investigate enhancements to manual QFD made possible by hypertext. Section 2 describes the QFD methodology in more detail, along with its problems and limitations. Section 3 is a brief description of the working view of hypertext used for Coq implementation. Section 4 describes the actual implementation and compares it with other hypertext system development tools such as gIBIS. Section 5 discusses how this system may be used as a framework and interface in support of Taguchi methods, the analytic hierarchy process, or the Japanese management method of nemawashi / ringi. Finally, Section 6 discusses possible extensions and improvements.

<table><tr><td rowspan="11" colspan="3">SUPPORT-ABILITY</td><td rowspan="3" colspan="3">PERFORMANCE</td><td rowspan="3">GOES FAST</td><td>Velocity (km/sec)</td><td rowspan="3">PERFORMANCE</td><td rowspan="3">SUPPORTABILITY</td></tr><tr><td>Capacity (Tons)</td></tr><tr><td>Etc.</td></tr><tr><td rowspan="4">Etc.</td><td>Large Payload</td><td></td><td></td><td></td><td>MTBF (hours)</td><td rowspan="8">20</td></tr><tr><td></td><td>√</td><td></td><td></td><td>MTTR (days)</td></tr><tr><td></td><td></td><td></td><td></td><td>Etc.</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Reliable</td><td></td><td></td><td></td><td></td><td>10</td></tr><tr><td>Easy to Fix</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Easy to Find Spare Parts</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Etc.</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 1. Most commonly used QFD matrix. This matrix takes qualitative, end-user functional requirements and shows their relationship with engineering control parameters. The symbol $\nu$ indicates that a given control parameter addresses the respective functional requirement. Requirements and specifications shown are as entered by simulated users from the logistics community (MTBF is mean time between failure; MTTR is mean time to repair).

## 2. Quality function deployment

## 2.1. Background

The history of QFD is somewhat obscure. The basic, generic ideas behind it are more than 40 years old, although the specific QFD structures have only recently been introduced in the U.S. An early English-language paper by Japanese authors Kogure and Akao [15] provides one brief history. This paper shows the first QFD reports appearing in Japanese in 1967, although with fewer than ten reports per year before the late 1970s. The article is somewhat confusing because it also states that QFD originated in 1972, when it was first put into use at the Kobe shipyards. In a later article, Akao claims to have developed QFD in 1966 [1]. His definition of QFD in that article is a system in which “responsibilities for producing a quality item must be assigned to all parts of a corporation.”

He uses a chart, similar to that shown in Figure 1, to assign these responsibilities.

According to a second brief history by Clausing and Pugh [6], the generic ideas that developed into QFD have their roots in value-analysis/value engineering. Value-analysis/value engineering was popular in the 1950s; however, the specific QFD methodology has become popular in the U.S. only since 1986. This is not inconsistent with Akao's history.

A third history, according to Warfield [31] is that the fundamental, underlying QFD ideas were based on the work of Hall and Love, as enhanced by Hill and Warfield under the name Unified Program Planning (first published in 1972) [13]. However, this cannot be the case if QFD originated in Japan in 1967, although the introduction of Unified Program Planning does coincide with the introduction of QFD at Kobe.

QFD, at least by that name, clearly reached the U.S. via Japan. However, its Japanese origins are uncertain. Although Akao claims to have introduced QFD in 1966, Schubert credits Mizuno with its development [22]. Regardless, it is currently in use at several Japanese organizations and is being studied by many more.

According to Sullivan, QFD was developed as one set of tools to address part of the Japanese Industrial Standard Z8101-1981 called Company-Wide Quality Control (CWQC). The Z8101-1981 standard defines CWQC as “a system of means to economically produce goods or services which satisfy customers’ requirements.” Thus, Japanese CWQC is a superset of American Total Quality Management (TQM) [27]. QFD helps TQM by reducing the possibility that an essential aspect of quality will be overlooked in the strategic planning process. This relates to the work of Garvin [10] who notes that managers often overlook one or more crucial dimensions of quality in system designs.

While QFD cannot guarantee that no essential aspect of total quality will be overlooked, it can be a very important and useful tool for enhancing the system development process. It is well-documented that using QFD methods for strategic planning can reduce development time by 50 percent for a wide range of products, services, and software systems while improving the quality of the final system [6,14,18,22].

It is not clear precisely what constitutes QFD. King defines QFD as, “a system for designing a product or service based on customer demands and involving all members of the … organization ….”

Narrowly defined, QFD refers to the organization that makes the design improvement possible. Broadly defined, QFD also includes the charts that document the design process. [14]

Sullivan's definition is, “an overall concept that provides a means of translating customer requirements into the appropriate technical requirements for each stage of product development and production.” [26]

For the purposes of this work, QFD is most easily understood as a formal structure for improving the system development process using charts similar to that shown in Figure 1. Notably, more than 80 matrices and charts have been identified as QFD in one or more of the specific QFD methodologies. However, all the QFD methodologies have the matrix shown in Figure 1 in common as one of their charts or subcharts. Correctly employed, a chart such as Figure 1 can ensure that each customer requirement is addressed by some design parameter and that no design parameter becomes part of the final specification if it is not relevant to some customer requirement.

As simple as this chart appears, successfully using it can be a formidable task. At least four distinct subtasks are required to complete it. The first subtask is to determine and organize a “good” list of customer/end-user requirements, and to group these requirements into appropriate categories—as is done in the first two columns on the left-hand side. The second subtask is to prioritize these requirements using a column such as the one on the right-hand side. The third subtask is to develop a list of control parameters or specifications that determine the system or product design and to organize them—as is done in the top rows. The fourth and last subtask is to determine which parameters influence which requirements and to ensure each requirement has been addressed.

Following Kogure and Akao's 1983 English-language article on QFD, a second article appeared by Sullivan in 1986 [271 which introduced another version of QFD based on four major documents. The first of these documents is an extension of Figure 1 with additional columns and rows. The other documents extend the structure from a single phase of the system life cycle to other phases. A further, more detailed version of QFD was introduced by King, who calls his extension a “generic QFD.” King’s version uses approximately 30 matrices and charts. All three versions were primarily used by engineering management. In 1988, Hauser and Clausing published a description of QFD in the Harvard Business Review [12] which introduced the methodology to general management. This methodology is also known as the Makabe Method [11]. King refers to the Makabe methodology as the “focused approach” which is,

![](/api/attachments/36GW9S5S/fulltext/images/b9dac4b686133b6f404588f0a97850ab841c221db6e49e8b98d026441fa5e275.jpg)  
Fig. 2. The House of Quality. A printed template is shown with items entered by a simulated user from the logistics community. Items entered by the user are shown as typed (in typed font).

good for ... parts and components, but ... awkward for computers, automobiles and other complex systems. It is good for minor improvements ... but is not well suited for cost effective innovation [14].

In spite of King's criticism, the Makabe or Hauser and Clausing version of QFD is the one most familiar to general managers. It provides an overview of the entire project without overwhelming the general manager with excessive detail. Consequently, the Makabe methodology was the starting point for the Coq.

## 2.2. Specific implementation

The Hauser and Clausing paper described a creative combination of QFD charts attributed to the Kobe shipyards in Japan. The combination is formed into a house-like structure, the “House of Quality,” which they describe as a “conceptual map that provides the means for interfunctional planning and communications for quality function deployment” [12].

The House is shown in Figure 2. The labeled parts of the house are as follows.

\- The rows in Area 1 include the customer attributes (functional requirements) organized into appropriate classifications. Also in this area is the column called “Relative Importance” for prioritizing these attributes. Capturing this “voice of the customer” is one of the most important contributions QFD makes to the development of successful products and systems.

\- The columns in Area 2 are for technical specifications or engineering characteristics. The first row of Area 5 contains the units used for these technical specifications. (This layout is taken from the original article [12].) Going from user requirements to technical specifications involves translating from the qualitative to the quantitative-a difficult problem referred to as “Feigenbaum’s bottleneck” [8,17].

\- Area 3, the “roof” of the house, captures the trade-offs between the various engineering parameters. In the example shown, it is indicated that increasing the maximum velocity will adversely impact both the carrying capacity and the reliability of the final system. Conflict is indicated by × (the only situation shown). Weaker conflicts would be indicated by ×. Strong synergy would be indicated by √, and weaker synergy by √.

\- Area 4 indicates the extent to which each end-user concern has been addressed by a design control parameter. The intersection of each technical specification column and customer requirement row forms a field in the middle of the house. These fields contain the correlations between the pairs. The same symbols are used as in the roof. Parameters that directly address a requirement are indicated by √; parameters that weakly or indirectly address a requirement are indicated by √. Strong conflicts are indicated by × and weak conflicts are indicated by ×. In Figure 2, the user requirement “Reliable” is quantified as “mean time between failures” (MTBF). A very high MTBF conflicts (weakly) with the user requirement of very high maximum velocity. Conversely, the maximum velocity specification directly addresses the customer’s concern for a fast vehicle.

\- Area 5, labeled “Objective measures,” was originally designed to allow producers to evaluate their existing product lines against the competitors’ using the technical measures identified in Area 2. Area 5 must be adapted to the specific system being developed; Figure 2 shows how this area might be used to evaluate a large system for which there are only three producers. The producer using the House is comparing his current system with those produced by his two competitors. However, the House may also be used when there is a much larger number or much more nebulous set of alternatives. When the House is used for such situations, Area 5 must be redesigned.

\- Area 6 continues the idea of Area 5 by graphing, on a scale from one to five, how each alternative identified in Area 5 is perceived to address the functional requirements. The example shows how the producer's current system ("Us") is rated a five on the criterion of "Goes Fast" but is much worse on other criteria (indicated by the line marked with $\times$ ). Likewise, for the "Goes Fast" criterion, Competitor B is worst with a rating of one, but excels in other areas (indicated by the line marked with +). When used in situations where Area 5 must be changed, Area 6 must be redesigned as well.

\- Area 7 is used for the new design. Targets are set for all control parameters that determine the new design along with cost, technical difficulty (risk), and relative importance of achieving each target. This provides management with a valuable means to direct resources by showing the experts' best estimates of the costs and benefits of each improvement in the product or current system design.

This methodology for QFD has been successfully implemented using paper forms. These successful implementations have resulted in 50-percent cost and time savings in the system development process, as well as products and systems which better satisfy customer requirements. However, the sources cited above also warn about failures in attempting to apply QFD.

## 2.3. Limitations

QFD was not originally implemented as a computerized group decision support system (GDSS), but as a set of charts and procedures. When these charts and procedures are implemented as a set of paper forms to be filled out, the QFD system can have certain serious limitations. Some of these limitations are:

1. Paper forms are inadequate for large numbers of requirements and specifications; this is the most common reason for failure. Paper forms cannot accommodate the 100 + requirements and specifications characteristic of real systems. In addition, users cannot handle the cognitive overload of a 10,000 + cell matrix;

this was cited as the primary cause of failure by 67 percent of those who reported failure. Figure 2 is adapted from the original article by Hauser and Clausing, including the “Etc.” (Only the specific requirements and engineering characteristics were changed for our project–acquiring an Air Force weapons system). While the seven areas shown in the figure represent important considerations in structuring the system development process, it is not clear how to implement a real development project using a paper form based on this figure.

2. A paper form like Figure 2 has no provision for the justification of the entries; thus, there is no corporate record of the decisions that led to the final design.

3. The paper forms offer no inherent provision for the fact that a group of users and designers are involved in the project and that the project will span many years. That is, there is no way to automate the search for specific items for further analysis or a review to ensure each user requirement has been adequately addressed.

4. A printed set of paper forms is relatively inflexible; yet, vendors of such forms warn that "QFD charts should not be copied ... the charts need to be customized to an individual operation" [14]. When QFD is introduced by ordering a set of paper forms, the discovery that the forms must be modified for the organization can be a major problem.

Partially because of these limitations, fewer than ten of 200 American companies that attempted to use QFD were able to realize its full potential [4]. A possible solution to these problems is a DSS or group support system (GSS). These systems provide tools which help mitigate the problems listed above. Ideally, such a tool would be extremely flexible so that the interface could be adapted to the organization and the specific project. A DSS would be a single-user system that assists a decision-maker in implementing QFD by automating some of the work associated with QFD. A GSS would be a multi-user concurrent or asynchronous system that would allow all participants to access the system throughout the system life cycle. A possible vehicle for implementing such a DSS or GSS is hypertext.

![](/api/attachments/36GW9S5S/fulltext/images/093b0adfa51ed7bdc5b825373740efc5c8c4a09df152edf0e9afba47f134e33c.jpg)  
Fig. 3. Linear writing.

## 3. Hypertext

The concept of hypertext is credited to Vannevar Bush, but the word was coined by Ted Nelson [23,30]. Pure hypertext is described as “an approach to information management in which data is (sic) stored in a network of nodes connected by links” [23].

Thus, hypertext is a nonlinear mode of writing. Ordinary written documents may be visualized as one-dimensional or linear graphs (Figure 3). The topology is given by the arrangement of pages from front to back in the document. Hypertext, on the other hand, allows the author to create an arbitrary topology on the pages of the document as in Figure 4. This topology may also be considered a network in which each node represents a page (or screen) of text.

However, the value of hypertext is not this simple, two-dimensional structure which corresponds to text and footnotes; rather, the value of hypertext is its ability to develop documents that capture multidimensional ideas. In fact, if the document involves orthogonal concepts $C_{i}, i = 1$ ... n, it follows that the logical topological structure of the document is the n-dimensional space,

$$
\prod_ {i = 1} ^ {n} C _ {i}.\tag{1}
$$

Such a document cannot be captured canonically with ordinary text; canonical capture requires hypertext. The following example illustrates that certain topological constructs based on one-dimensional paths cannot be easily mapped into one or two dimensions.

Example Consider three houses and three delivery persons. The delivery persons may not cross each others' paths (delivery persons may cross their own paths), but each must visit all three houses. Draw the three houses and the paths the delivery-persons must take to do this.

Two dimensions are inadequate to contain certain types of paths (e.g., the topological constructs in question); therefore, it is impossible for all three delivery persons to deliver to all three houses without crossing paths. The puzzle can be solved if additional dimensions are allowed (i.e., if one of the delivery persons is allowed to fly).

![](/api/attachments/36GW9S5S/fulltext/images/9da5bf2c8cbae797c62759e98d40a76a7241936d646b87711e1b4a0a826c6599.jpg)  
Fig. 4. Typical hypertext network.

A well-designed hypertext document will conform naturally to the underlying structure of the concepts being conveyed. Thus, it is more straightforward for readers to navigate and allows them to readily proceed along any dimension of the document. In addition, hypertext allows the users to search for arbitrary string patterns. This provides virtual links between pages that are related in ways relevant to the readers, although this link may not have been foreseen by the author.

In his Memex, Bush envisioned a sophisticated version of the microfilm or microfiche reader in which any item in the world's library could be easily retrieved; however, the storage of information on electronic media encourages much more creative methods for communicating information. At a minimum, graphics and digitized sound are added if the hardware will support them; the result is called hypermedia.

Hypermedia is not limited to static text, graphics, and sound. In its most general form, each page may include one or more complete programs. These programs are called message-handlers because they respond to messages from either the user or other message-handlers. Such a hypertext document is characterized by, in addition to its text and graphics, a set M of messages and $M'$ of message-handlers. $|M'| \geq |M|$ since there may be, at various points in the document, different message-handlers that respond to the same message.

For example, each numbered area of the House in Figure 2 is a message-handler that responds to some user action, typically a mouseclick or text entry. The message-handlers, which will be described later, allow the users to work on the subtask associated with that part of the House, or to see the results of that work. In general, hypermedia is a network connecting available electronic resources in whatever manner the author finds most suitable for the presentation of information. Each page of this hypertext document can access the CAD/CAM programs, animations, explanations, etc., necessary to convey desired information.

## 4. Hypertext implementation of the city of quality

## 4.1. Overview

The House of Quality, as an implementation of QFD, is part of an overall system for managing requirements over the system life cycle—from problem definition to implementation. The House helps ensure that the organization considers end-user requirements in the top-level design of systems and products. A complete system for QFD requires a number of Houses to provide for intertemporal communication and to support multiple users of the system. The basic idea behind the City of Quality is to use hypertext to extend the House of Quality to an electronic collection of multiple, related Houses that span the entire system development life cycle.

![](/api/attachments/36GW9S5S/fulltext/images/1ed1e3989f6096f2a06acd92f88b225e3fd0a407cfc944b9756a4da952acc829.jpg)  
Fig. 5. Top level of the Coq hypertext document. Each House accesses the subsystem of that name (e.g. clicking the mouse on the Parts Deployment House accesses the Parts Deployment Subsystem). Help ? provides the user with assistance. Home exits the Coq application. The user may also change the document title.

With no electronic support, requirements management can be difficult. The systems development cycle of a complex project spans several years. By final production, some initial requirements have been modified or deleted and new ones have been added. In addition, a few requirements may have been overlooked. When the requirements are maintained manually, formal modifications are appended as written codicils to the original document, while implicit, informal modifications evolve throughout the development cycle without being recorded. Since the original list of requirements is usually quite long (several hundred or more requirements are common), the list with codicils appended is very difficult to follow. Consequently, it is difficult to determine if the final product meets the modified list.

The Coq allows managers to track each requirement. Thus, maintaining the set of requirements becomes more explicit and manageable. A manager may electronically verify if any user requirement from the House of Quality (Figure 2) has not been addressed at each stage in the system life cycle. Conversely, the manager may select a difficult, risky, or costly implementation issue in production, check which requirements are addressed, and determine the value of the issue to overall customer satisfaction.

## 4.2. Top level of the hypertext document

The top level of the Coq document is shown in Figure 5. This node in the document allows the users to identify themselves, set a title for the project, or access the subsystems. Clicking the mouse on the box labeled “User:” allows the user to change the name of the user. Clicking the mouse on the document title (initially set to “First Test”) prompts for a new document title. Clicking the mouse on either of the four Houses accesses that subsystem.

The left-most House of Quality is somewhat different from the other three because it must support the seven separate tasks depicted in Figure 2. In particular, this is where the “voice of the customer” is captured as qualitative, functional requirements and translated into quantitative engineering characteristics. The remaining three Houses do not obtain their left-hand-side data from the users, but rather from a message-handler that activates automatically when the House is viewed. The message-handler obtains the requisite data from the House to the left of the House being viewed. The remaining Houses are more likely to be accessed by engineering management, although the data entered are electronically related back to the House of Quality to support queries relevant to general management.

![](/api/attachments/36GW9S5S/fulltext/images/07687f062564331e055b31c13f44c49e45716d84dd138962f9fdd7dabb4524dc.jpg)  
Fig. 6. The House of Quality as seen by the user. Text within the House is not necessarily legible, because this node is intended to be an icon which supports access to the seven QFD subsystems described in Section 2.

![](/api/attachments/36GW9S5S/fulltext/images/584722f0729b3ffcd60c68bfb6209baede31bceda3df85e441f922838331ebc4.jpg)  
Fig. 7. First screen for acquiring Customer Requirements of a new system. No requirements have been entered.

When the House of Quality is accessed, the user is transferred to the node shown in Figure 6, which is similar to Figure 2 (from which it was derived). Clicking on Home (which appears at every node) allows the user to exit the system. This particular implementation of hypertext (Hypercard) automatically saves all data entered in the system. This prevents the user from accidentally losing data by failing to save. The arrow at the lower right of the screen returns to the previous node (in this case, the Coq main menu, shown in Figure 5). The House is actually divided into seven parts, each of which accesses one of the separate subsystems described following Figure 2. For example, clicking the mouse anywhere in the section beneath the “Customer Requirements” accesses a subsystem to capture the “voice of the customer.”

Clicking the mouse anywhere to the right of "Engineering Characteristics" accesses the subsystem to capture the engineering experts' quantitative characteristics for specifying the project under development. Other areas of the House access the appropriate subsystem as well.

![](/api/attachments/36GW9S5S/fulltext/images/2a568c81d86e73acb52eceda57a35f522038a7aac197bb20200a00155990e92c.jpg)  
Fig. 8. Sample completed initial screen for acquiring Customer Requirements. Figure 7 has been filled in with Garvin's eight dimensions of quality. When used to support Garvin's approach to TQM, this is filled in for the users before initial use.

## 4.3. Subsystems

Subsystem 1: Capturing the “Voice of the Customer”

Subsystem 1 in Figure 2 captures the “Voice of the Customers”. This subsystem is designed to implement the first stage of multi-attribute, multiple-person decision-making by acquiring the matrix of required attributes and relative weights for each decision-maker involved.

When the user elects to capture the customer requirements subsystem (by clicking the mouse anywhere near the “1” in Figure 2), a simple link is invoked to that part of the hypertext document. The display is shown in Figure 7.

This node has certain features common to most nodes in the document. The arrow in the lower right-hand corner returns the user to the node viewed immediately prior to the current one. The little houses return the user “Home”; of course, “Help” is available by clicking on the question mark.

Notably, all attributes must be organized in groups of eight, for reasons that will be explained below. The first eight attributes are the Primary Attributes. These are normally classes of requirements rather than specific ones. When used for

TQM, this node is filled with Garvin's eight dimensions of quality: Performance, Features, Reliability, Conformance, Durability, Serviceability, Aesthetics, and Perceived Quality [10] as shown in Figure 8.

A feature of this implementation is that the user is allowed no more than eight classes of requirements; each class may have no more than eight subclasses; etc. This prevents the growth of massive matrices that defy analysis. This hierarchical approach is, by the $7 \pm 2$ rule, conceptually better for the user than a flat approach with many attributes or subattributes at the same level. The only limit on the total number of requirements the document can accommodate is that imposed by secondary storage limitations.

As explained at the help page, the user is to select (with the mouse) one of eight primary slots. A blank slot is actually a message-handler (i.e., clicking the mouse activates a program). When the program is activated, a new node is added to the document and the user is transferred to it (Figure 9).

When the new node is created, a new arc is created between the node shown in Figure 7 and the new card. Thus, the entire program that created the card is replaced by a single arc to the new card. In this way, the hypertext document is self-modifying.

This new node, created as needed, illustrates two features of the Coq which enable use by multiple persons representing different customer interests. A non-disruptive annotation feature is provided by the “Attach Comment” message-handler. Each user is allowed to attach one or more comments. Features for editing comments, viewing other user comments, etc., are available. The only restriction on these comments is that imposed by secondary storage. This is listed as an important feature in hypertext systems [2], but has previously been available only in much more expensive systems than the Coq.

![](/api/attachments/36GW9S5S/fulltext/images/27d0ee94cc0c111b87317b5854d2be8f9196ea6e4eafeb80dda70cad753c6c5b.jpg)  
Fig. 9. Node to acquire a Specific Requirement.

A second feature is the History. A record is kept of every modification and the person responsible for it. The system tracks the user, although this implementation uses an “honor” system since password checking is not employed. Instead, the user is asked to provide a “real” name for tracking purposes. A password system may be added if the Coq is used in a more hostile environment.

The downward-pointing arrow at the bottom of the screen is a very important feature of the Coq. It is an integral part of the scheme that allows for the addition of an unlimited number of user requirements by using recursion. If this card is used for a class of requirements rather than a specific requirement, the downward-pointing arrow will indicate the subclasses or its members. When first accessed, the arrow creates a new node similar to the one shown in Figure 7; then the program that created the node is deleted and replaced with an arc to the new node. However, note that Figure 9 creates a node like Figure 7, which, in turn, is capable of creating eight new nodes like Figure 9. The result is a recursively defined, self-modifying document that allows the hierarchy of classes of requirements to be easily extended to an arbitrary depth.

Note that the user is not allowed to enter data directly into the fields of the nodes like Figure 9. Instead, the Coq has message-handlers which, when activated by a mouseclick, start a program to prompt for requirement and weight. The program then automatically updates the fields for originator, modifier, and history, using the user's name (which is obtained before the system may be accessed). While this program currently passes user inputs directly to text fields, this processing allows future enhancements to check inputs, perform calculations, and pass messages to a local area network (LAN).

## Subsystem 2: Capturing the Engineering Specifications

The second subdocument of the Coq, corresponding to Areas 2 and 7 of Figure 2, acquires the technical specifications for the system under development. It is similar to the subdocument for acquiring customer requirements, although somewhat different information is captured. Again, this is a self-modifying document which uses recursion to capture a list of technical specifications limited only by the availability of secondary storage. The node for acquiring these specifications is shown in Figure 10.

![](/api/attachments/36GW9S5S/fulltext/images/eba3556a54eb062320ecacbbfc089bc94ca620693b813f495e76e668f9924a16.jpg)  
Fig. 10. Screen for acquiring Technical Specifications (based on Area 2 of Figure 2). This screen acquires specification parameters and information useful for managerial design decisions. Engineering characteristics and values are shown as they might be typed by an actual user (LRU is line replaceable unit).

When this screen is implemented as a paper document, Estimated Cost, Difficulty, etc., are entered as numbers. These numbers may be based on some calculations performed separately. Implemented in hypertext, cost and difficulty may be modeled as functions of target value, and the model embedded directly in the document. The model would then be “deep knowledge,” while the system displays the numerical value as “surface knowledge” to support managerial decision-making. This storage of deep knowledge in the DSS and display of surface knowledge is another important enhancement over paper implementations [5]. Likewise, overall cost may be automatically computed and sensitivity analysis provided.

Another drawback when using a paper implementation of QFD is that a manager must “eyeball” the numbers to select the best design. When implemented as an electronic document, the manager has immediate access to a variety of decision support tools which may be used to help select compromise designs.

Subsystem 3: The Roof

The third area of Figure 2 records the trade-offs between the various engineering characteristics. This is captured via a roof (Figure 11).

The user selects a square on the roof if the characteristics interact either synergistically or antagonistically. The basic QFD methodology only records these relationships on a scale of -2 to 2; the former is strong antagonism and the latter is strong synergy. Initially, when the user selects the roof of the house, top-level classes of characteristics are selected. Clicking the mouse on a class of characteristics brings up the specific roof based on the individual members of the class. For example, Figure 11 is reached by clicking on a column for Logistics characteristics, which is part of a roof of general specifications such as Logistics, Performance, Cost, etc. This process can be repeated until the lowest-level roof is reached with trade-offs between specific characteristics. Likewise, one can move to more general roofs by clicking on the name of the class, listed above the eight members.

The roof is one of the great strengths and weaknesses of QFD. In the paper implementations, it grows quadratically in the number of characteristics. A complex, difficult decision is thus reduced to a large number of small, manageable decisions; however, the total number of small decisions may well become unmanageable. In the Coq implementation, the screen can display a maximum of eight characteristics; this restricts the user to 24 trade-offs at one time. Users are not encouraged to compare each engineering characteristic against every other; rather, they should perform the more relevant comparisons. Nevertheless, the number of decisions can easily become formidable in a large system. However, while no single system or tool can completely resolve all the problems inherent in unmanageable complexity, the Coq provides one approach to this problem and can be a solution in many cases.

![](/api/attachments/36GW9S5S/fulltext/images/00b6bc466b067a35c1cd80ea4393da7cc3224557c797bd365384862598576298.jpg)  
Fig. 11. "Roof" of the House of Quality showing trade-offs between various Engineering Characteristics. Characteristics are as typed by a simulated user.

![](/api/attachments/36GW9S5S/fulltext/images/0df0f22c7a680898665857135dcc292937dac93815e57e7d84e09384dc595987.jpg)  
Fig. 12. Measure of which Engineering Characteristics Address which Customer Requirement (using the notation indicated in Figure 2).

## Subsystem 4: The Central Matrix

The fourth area of the House records the interactions between requirements and specifications, as illustrated in Figure 12. These values (again from -2 to 2) are displayed as described following Figure 2. Because this is a hypertext document, each non-zero value may be explained on a card similar to the one used to acquire customer requirements. A hypertext implementation can also accept the values for these fields either as a numerical value, a simple formula, or a complex computer program. In addition, comments such as those used in the requirements definition phase may be pasted on at will. The manager need only see the final result, but deep knowledge potentially lies behind every surface number.

As with the roofs when the central matrix is first selected, the top-level classes of attributes and characteristics are displayed. However, by selecting a class with the mouse, the user may select the interaction matrix for the members of that class. As with the other subsystems, this enables the entire system to manage a quantity of data limited only by secondary storage capabilities.

Again, as with the roofs the total number of cells to be filled grows quadratically with the overall size of the problem (i.e., number of rows multiplied by number of columns). Thus, a single, monolithic, unmanageably complex decision is broken down into a number of small, manageable decisions. But, as with the roofs the number of these decisions can become unmanageable. The Coq attempts to avoid this explosion of small decisions by limiting the user to an $8 \times 8$ matrix; however, this is not always successful. Large, complex systems usually remain large and complex. If the design guidelines embodied in Suh's Axioms are followed, design parameters are chosen with minimal interactions so that this central matrix remains upper or lower triangular with few off-diagonal elements [25]. Thus, the process of filling in the Coq encourages a design that respects Suh's axioms which, in turn, leads to a design that is easily matched to the Coq capabilities.

## Remaining subsystems

Of the seven subsystems of the first House discussed in Section 2, two subsystems, corresponding to Areas 5 and 6 of Figure 2, must be adapted to each organization using the House. The remaining five subsystems have been discussed above (the subsystem corresponding to Area 7 was discussed with the subsystem corresponding to Area 2). As illustrated in Figure 2, the Areas 5 and 6 of the House allow users to compare existing designs and to display these comparisons graphically. These subsystems have not yet been implemented in the current version of the Coq. When implemented, these two parts will help decision-makers evaluate existing systems and use these evaluations to guide the system development process.

## 4.4. Comparison with other hypertext tools

Another class of hypertext tools to support system development has been developed based on the methodology called Issue-Based Information System. One tool, gIBIS, uses a graphical approach to capture the type of system issues addressed by QFD [7]. A newer version called rIBIS is a real-time implementation [20]. The older gIBIS is intended to support generic system design. The implementation is a more expensive, less portable version than the Coq because it requires specialized hardware and software and has seen little use outside of the organization where it was developed. The Coq, conversely, runs on the low-cost Macintosh Classic™. In principle, gIBIS is equivalent to the Coq, although the flavor and emphasis are very different.

While an empirical comparison of the two systems might be of some limited interest, both are basically different approaches to a common problem. gIBIS is based primarily on graphs; the Coq is based primarily on matrices. The equivalence is easily seen.

Theorem Graph-based representations are informationally equivalent to matrix-based representations.

Proof Any graph may be captured by a node-incidence matrix. Thus, the matrix approach is at least as strong as the graph-based approach. Conversely, while not all matrices are node-incidence matrices (and thus not so easily captured by direct transformation to a graph), one may imagine a graph as a collection of labeled arcs (one for each cell in the matrix) with the contents of the cell as the label, the start of the arc as the row identifier, and the end of the arc as the column identifier. Hence, graph-based information representations are at least as strong as matrix-based representations. Thus, the two representations are informationally equivalent. QED.

Thus, both the gIBIS graphical and the Coq matrix representations are capable of capturing the same data. The preferred system is a matter of decision-maker style. Thus, it would not be particularly informative if, for example, 45 percent of decision-makers preferred the Coq and 55 percent preferred gIBIS or vice versa. There is no compelling reason to deprive graphically oriented decision-makers of a graphical tool, or to deprive matrix-oriented decision-makers of a matrix tool just because one class of decision-makers is in the majority. The issues of cost and availability are, however, more likely to make the Coq more desirable in many situations.

The more recent implementation of IBIS, rIBIS, is not a real competitor to the Coq. rIBIS is described as a system that specifically supports software system design [20], while the Coq is intended to support generic system design.

## 4.5. The Coq as a group decision support system

As a GDSS, the version of Coq described above is a low-cost system which may be distributed to operational and middle managers as well as to the engineering staff responsible for entering numbers and models in the various parts of the city. To achieve this low cost, the Coq was implemented as an asynchronous system with communication via “sneakernet” (i.e., by someone carrying around the floppy disk). Where resources such as a LAN are available, a number of enhancements are possible. These are described in Section 6 on possible extensions to the Coq, especially Section 6.2.

## 5. Potential uses of the city of quality

## 5.1. A template to support Taguchi methods

The Coq is well-suited to support a simplified variant on the modified Taguchi approach for selecting the best design. The original Taguchi approach was to minimize the cost to the system end-users. End-users are assumed to have target values which, if achieved, allow them to use the system without incurring any additional cost. Given technological limits, this ideal system cannot be achieved. For example, an ideal vehicle would require no fuel whatsoever, provide zero risk of accident, etc. Thus, the ideal system is a vector $\tau$ of target parameter values, while an actual system is a vector of parameter values $t \in T$ , where T is the set of all systems possible within the technological constraints. These parameters are not truly comparable—e.g., it is not really possible to quantify the relative value of fuel efficiency versus safety—however, the Taguchi approach is to use a quadratic approximation. The cost of a unit deviation from each target $\tau_{i}$ is given by $c_{ui}$ . The total unit cost to the end-user is then estimated as

$$
C _ {u} (t) = \sum_ {i} c _ {u i} (\tau_ {i} - t _ {i}) ^ {2}.\tag{2}
$$

The Taguchi approach is to produce a system t that minimizes Equation (2).

A more realistic approach includes both the end-user's cost and the developer's cost $C_{d}(t)$ of producing the system [29]. This modified Taguchi approach is based on minimizing total cost,

$$
C _ {u} (\boldsymbol {t}) + C _ {d} (\boldsymbol {t}),\tag{3}
$$

rather than just end-user's cost.

The Coq may be used to capture the data and perform the necessary computations to support the modified Taguchi approach. The row Estimated Cost may be used to record components $c_{di}$ of $C_{d}$ . The producer's cost is then,

$$
C _ {d} = \sum_ {i} c _ {d i} (t _ {i}).\tag{4}
$$

A row must be added (or the row Imputed Importance used) to record the consumer's unit costs $C_{ui}$ .

The Coq methodology indicates that Equation (4) is not adequate for a quadratic approximation because it omits the cross terms (i.e., the synergies and antagonisms captured by the roof of the house). The correct quadratic approximation is,

$$
C _ {d} (t) = \sum_ {i} c _ {d} (t _ {i}) + \sum_ {i} \sum_ {j} c _ {i j} (t _ {i}, t _ {j}),\tag{5}
$$

where the coefficients $c_{ij}$ represent the cross terms (synergies and antagonisms) between characteristics i and j. Synergies are captured as negative $c_{ij}$ and antagonisms as positive $c_{ij}$ .

The basic Coq template must be further modified. Instead of recording synergies and antagonisms on a Likert scale of -2 to 2, more accurate cost estimates must be recorded or a model must be developed to provide an estimate of these costs from the Likert values. In addition, the cost components $c_{u}(t_{i})$ must be recorded rather than just Imputed Importance.

Finally, a module must be added to compute $C_{u} + C_{d}$ and the target $\tau^{*}$ that minimizes $C_{u} + C_{d}$ , but this is a “straightforward” quadratic programming problem.

## 5.2. A Template to support Nemawashi / Ringi

Japanese group decision-making often relies on nemawashi / ringi, a process in which a coordinator (ritsuan-sha) brings the group to a consensus. This process may be assisted by the Coq. A complete discussion of nemawashi/ringi is beyond the scope of this paper but is detailed by Watabe, Holsapple, and Whinston in their paper [32].

Briefly, the final stage of the nemawashi / ringi process (ringi) consists of circulating a formal document that describes the decision made among all group members. At this point, unanimous consensus is almost certain because of the preceding informal negotiations spearheaded by the ritsuan-sha. This informal negotiation process-the nemawashi-normally consists of five steps:

1. Information collection (joho shyushyu),

2. Data analysis and alternative generation (ritsuan),

3. Tentative plan selection by the coordinator (sentaku),

4. Negotiation and persuasion (nemawashi), and

5. Formal document circulation (ringi).

These five steps have traditionally been performed by Japanese decision-makers without using technological support; however, the process can be enhanced by such support. Tools that would help include ad hoc models for computing the group rankings of the alternatives chosen. These ad hoc models will be referred to as the group preference aggregation models, or group models. By Arrow's theorem $[3]$ no group model will work under all circumstances; however, if a consensus is attainable, there must exist some model that will yield that consensus as a function of the individual preferences.

To apply the group models, the coordinator must obtain a matrix of decision-maker requirements and weights, a matrix evaluating each alternative against each requirement, a vector of decision-maker relative influence, and a vector of decision-maker difficulty of persuasion. Then, using Multi-Attribute Utility Theory (MAUT) or some other model of individual preferences, a matrix M giving the cardinal rating of each alternative for each participant is obtained. Thus, a group model is a mapping $\Phi$ from M to a vector g giving the group preference,

$$
\Phi : M \to \mathbf {g}.\tag{6}
$$

A DSS can help a facilitator apply each group model to compute candidate group preference functions for consensus.

With the assistance of a DSS, the ritsuan-sha selects the group model most appropriate for the group and decision under consideration. The original nemawashi / ringi paper suggests six broad classes of group decision models along with several variants of each class. A detailed description of each model is beyond the scope of this paper; however, all these models may be implemented in hypertext, and the system allows the coordinators to select the models they deem most appropriate.

In the simplest version of the Coq described above, all members of the group attach their contribution to a single hypertext document existing on a single floppy disk which is circulated via “sneakernet.” The ritsuan-sha can then use this document, with its detailed history of contributions from preliminary nemawashi, to obtain a candidate for ringi.

Using the Coq for nemawashi / ringi requires the addition of special nodes for the ritsuan-sha.

For example, the ritsuan-sha must have a special card with links to each group model which may be used to obtain a proposed consensus. Basically, the existing Houses of Quality allow the ritsuan-sha to obtain matrices $M_{i}$ for each expert i. Rows of $M_{i}$ correspond to technical specifications, s, while the columns of $M_{i}$ correspond to proposed and existing designs, d. Thus $M_{i}(s, d)$ is a measure of the extent to which design d addresses specification s. A second matrix, $N_{i}$ , has user requirements as rows, r, and technical specifications as columns, s. $N_{i}(r, s)$ indicates the extent to which specification s addresses requirement r.

The ritsuan-sha also has a vector $R_{j}$ for each end-user or decision-maker j, indicating the weight j put on each requirement; vectors I and P indicate the influence and pursuadability of each end-user or decision-maker; and the set D indicates alternative designs.

When the appropriate group model is selected, it accesses a mapping $\Phi_{h}(M, N, R, I, P): D \to \mathcal{R}$ which quantifies the overall utility of each design.

The message-handlers for the coordinator have not been implemented at this time but are a reasonable extension of the Coq.

## 5.3. The City of quality as a template for the analytical hierarchy process

In combining individual preferences to form a group preference, cardinal preferences offer an alternative to ordinal preferences. This is theoretically more appealing-specifically, Arrow's theorem shows that there is no logically consistent group preference aggregation function which combines individual ordinal preferences into a group preference. However, there are a variety of logically consistent methods for combining cardinal utilities to produce a group utility (e.g. weighted averages).

Typically, however, cardinal preferences obtained from decision-makers are inconsistent. The analytic hierarchy process (AHP) is one method for obtaining an estimate of cardinal preferences from a set of “noisy” preferences provided by the decision-makers [21]. The AHP as specified is logically inconsistent and, therefore, seriously flawed as a tool for computing these cardinal preferences [9,28]; nevertheless, it has a place in the Coq.

Given Arrow's contention that cardinal utilities cannot be obtained and his theorem that ordinal utilities cannot be combined, nothing is a panacea for resolving group conflicts. However, any tool that provides a starting point for reaching consensus is potentially useful; the AHP can be used for this purpose. The AHP provides a "strawperson" which the group facilitator can propose as a basis for further discussion. The AHP is attractive, when used in this manner, and the Coq can be readily modified for use with it. This is evidenced by the basic hierarchical character of the storage and organization of the user requirements in the Coq. This hierarchical structure can provide the hierarchy necessary to AHP. The second requirement for AHP is a system to rapidly make the comparisons between each attribute. This, in turn, may be done by modifying the existing "roof" structure to include a module that captures the relative utilities of the user requirements needed by the AHP. This is planned for a future extension of the Coq.

## 6. City of quality limitations and directions for further research

## 6.1. Limitations

The Coq has several limitations: it is currently limited to one user at a time, the main House of Quality does not fully support the QFD methodology, and the other Houses in the City are not fully functional.

The Coq is currently implemented as an asynchronous, multi-user system for QFD; thus, users must wait to see each other's ideas. Ideally, users will be able to access the Coq from their desktop computers at any time. This would include fully concurrent access.

A second problem is that, as implemented, the House of Quality does not completely provide for the QFD methodology. In particular, all customer requirements should be acquired before they are ranked, and the complete list of specification parameters should be obtained before any target values are assigned to the parameters. The current system combines acquisition and quantification for simplicity. Planned enhancements will support at least four separate brainstorming exercises: (1) acquiring the list of end-user requirements; (2) prioritizing those requirements; (3) acquiring the list of design parameters; and (4) setting targets for those parameters.

Finally, as planned, the other Houses in the City that follow the House of Quality should turn system specifications into subsystem requirements and carry them through process and production planning in an automated fashion.

The completed Coq should:

1. automatically flag any user requirement that has not been addressed through final production;

2. automatically flag any technical specification for the system, subsystem, process or production that is not needed to address a specific user requirement; and

3. provide modules for sensitivity analysis that allow decision-makers to see immediately the impact of budget restrictions on requirements, the impact of relaxing target values on cost, etc.

The result would be a strategic planning tool that would help prevent systems in which crucial requirements are overlooked, and unnecessary, excessive costs arise from meeting irrelevant specifications.

As originally envisioned, the current implementation of the Coq would ultimately provide such a system, running concurrently on distributed central processing units (CPUs). However, the current version is limited by awkward data structures. Much of the data are redundant. Data displayed at various nodes of the document are kept at all nodes where displayed, and are copied between nodes by conventional imperative programming. These data redundancy and management problems caused a revision in the original plan. The current system has become a prototype and test-bed that demonstrates the feasibility of a sophisticated hypertext GSS for QFD, provides potential users with a better understanding of what the final system might look like, and illustrates the need for extensions and further research.

## 6.2. What You See Is What I See extension to the Coq

An exciting possibility in computer-supported cooperative work (CSCW) is the situation in which various group members can see exactly what is on each others' computer screens. This concept is called WYSIWIS (What You See Is What I See) [24]. If resources are available in the form of a networked set of computers all running Hypercard, this concept can be extended to the Coq. The planned implementation is a relatively low-cost version. The Coq can be extended with two message-handles named ATP and NBP that handle the transport protocol and name binding on the LAN. When these utilities are installed, all users must start identical copies of the Coq and must enable the network communication feature. This allows each copy of the Coq to post to and receive from the network. Note that ATP only posts and receives messages; if the user inputs text or mouseclicks (for graphics) into the Coq without using a message-handler, communication will not ensue.

To extend the Coq to WYSIWIS, each Coq message-handler must be modified by the addition of the line,

ATPsend \`message\`

which sends a copy of “message” to the network. In addition, the idle message-handler must be modified to include the lines,

ATPreceive \`message\`

send \`message\`

which check the network for messages and pass them to the Coq. As each message is entered, it will traverse the network updating every machine, and the system will have WYSIWIS.

## 6.2. Relational database revision of the Coq

A relational database management system (RDBMS) is required to achieve many Coq objectives. As implemented, the Coq data structures are not easily managed and do not readily support a comprehensive system to manage a complex project over its entire life cycle. By storing parameters on a central RDBMS, a planned future version of the Coq should be able to manage the complexity inherent in a large system development project while allowing multiple participants concurrent access.

## 7. Conclusions

The Coq developed to support quality function deployment over the system life cycle, is intended to provide this support for general systems. The specific examples used in the illustrations were geared for an Air Force system and addressed logistics concerns; however, the Coq is adaptable and can be modified for other types of system development projects, such as consumer product development or software system development.

To achieve quality in a system, a number of decision-makers and technical experts must be involved, and their contributions recorded. Over several years, a retrievable record of decisions made and their rationales becomes vital. Paper documents are deficient in maintaining a good record of group interactions and providing facilities to easily retrieve, for example, all documents relating to a specific user requirement.

The Coq addresses some of these issues. It makes acquisition and retrieval of the information a simple matter of a few mouse clicks and text string entries. It also allows for recording models and explaining all decisions. In addition, the Coq provides a low-cost system to support certain kinds of group interactions, thereby providing some GDSS support to lower and middle managers.

Thus, the Coq could provide the structure and technology io make this information available to the general managers throughout the system life cycle. The system could provide support for strategic planning at the inception of each major system, and support for requirements management, coordination, and control throughout the development process.

## Acknowledgements

I wish to thank the Air Force Office of Scientific Research for sponsorship of this research, and the Logistics Research Acquisition Branch of Armstrong Laboratory for their cooperation.

Many people were very helpful, and made this research project both enjoyable and productive. Special thanks are due to Capt Hill, Ms. Edly, Capt Moen, Ms Peasant and Ms Stiller for their assistance with my research in various ways. Thanks are also due to Ms. Campbell and Mr. Hoffman for their concern and interest in my project.

Finally, I have to thank Ms Wheeler for her invaluable editorial assistance, without which I could not have completed the writing of this paper.

## References

[1] Y. Akao. Foreword. in: B. King, Better Designs in Half the Time. Methuen, MA: GOAL/QPC; 1989.

[2] Akscyn, Robert M., et al., KMS: A Distributed Hypermedia System for Managing Knowledge in Organizations. Communications of the ACM. 31(7) 820–835, 1988.

[3] K.J. Arrow. Social Choice and Individual Values (2nd Ed.). Cowles Foundation for Research in Economics at Yale University: John Wiley and Sons Inc., 1963.

[4] C.C. Biddle. Using Interactive Management (IM) For Defining and Solving Complex Problems. Presented at the Government Group Decision Technology Conference, Defense Systems Management College, 1991.

[5] A-M. Chang, C.W. Holsapple, A.B. Whinston, Decision Support System Theory. West Lafayette, IN 47907: Management Information Research Center Krannert Graduate School of Management Purdue University, 1988.

[6] D. Clausing and S. Pugh. Enhanced Quality Function Deployment. In Design and Productivity International Conference. Honolulu, HI, 1991.

[7] J. Conklin and M. Begeman. gIBIS: A Hypertext Tool for Exploratory Policy Discussion. ACM Transactions on Office Information Systems, 6(4), 303–331, 1988.

[8] D.J. Duke, G.M. Nijssen, and S.M. Twine. The Entity-Relationship Data Model Considered Harmful. In the Sixth Symposium on the Empirical Foundations of Information and Software Science, 1988.

[9] J.S. Dyer. Remarks on the Analytic Hierarchy Process. Management Science.; 36(3), 249–258, 1990.

[10] D.A. Garvin. Competing on the eight dimensions of quality. Harvard Business Review, 65(6), 101–109, 1987.

[11] R.F. Hales. Quality Function Deployment (QFD). Presented at Quality Function Deployment Presentation and Demonstration, 1991.

[12] J.R. Hauser and D. Clausing. The House of Quality. Harvard Business Review, 66(3), 63–73, 1988.

[13] J.D. Hill, and J.N. Warfield. Unified Program Planning. IEEE Transactions on Systems, Man, and Cybernetics, 2(5), 610–621, 1972.

[14] B. King, Better Designs in Half the Time. Methuen, MA: GOAL/QPC, 1989.

[15] M. Kogure and Y. Akao. Quality Function Deployment and CWQC in Japan. Quality Progress, 16(10): 25–29, 1983.

[16] G.A. Maddux et al. Organizations Can Apply Quality

Function Deployment As Strategic Planning Tool. Industrial Engineering, 23(9), 33–37, 1991.

[17] D. Michie. Inductive Rule Generation in the Context of the Fifth Generation. In Proceedings of the International Machine Learning Workshop, 65–70, 1983.

[18] T.H. Miller. Quality Force Deployment. Program Manager, 32–37, September-October, 1990.

[19] A. Panday and D.P. Clausing. QFD Implementation Survey Report. Cambridge, MA: Laboratory for Manufacturing and Productivity, 1991.

[20] G.L. Rein and C.A. Ellis. rIBIS: a real-time group hypertext system. International Journal of Man-Machine Studies, 34(3), 349–367, 1991.

[21] T.L. Saaty. The Analytic Hierarchy Process. New York: McGraw-Hill, Inc., 1980.

[22] M. A. Schubert. Quality Function Deployment-A Comprehensive Tool for Planning and Development. In NAECON 89 (CH2759-9/89), 1498–1503. Piscatawny, NJ: IEEE, 1989.

[23] J.B. Smith and S.F. Weiss. An Overview of Hypertext. Communications of the ACM, 31(7), 816–819, 1988.

[24] M. Stefik et al. Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings. Communications of the ACM, 30(1), 32–47, 1987.

[25] N.P. Suh. The Principles of Design. New York: Oxford University Press, 1990.

[26] L.P. Sullivan. Quality Function Deployment. Quality Progress, 19, 39–50, 1986.

[27] L.P. Sullivan. The Seven Stages in Company-Wide Quality Control. Quality Progress, 19, 77–83, 1986.

[28] E. Triantaphyllou and S.H. Mann. An Examination of the Effectiveness of Multi-Dimensional Decision-Making Methods: A Decision-Making Paradox. Decision Support Systems, 5, 303–312, 1989.

[29] E. Tse and W.E. Cralley. Management of Risk and Uncertainty in Product Development Processes, Draft Final Report, Contract Number MDA 903 84 C 0031, Task Order T-D6-553, 1988.

[30] T. Vaughan. Using Hupercard $^{®}$ . Carmel, IN: Que $^{®}$ Corporation, 1988.

[31] J.N. Warfield. [Letter to the Editor, Harvard Business Review]. Institute for Advanced Study in the Integrative Sciences, George Mason University; 1989.

[32] K. Watabe, C.W. Holsapple and A.B. Whinston. Coordinator Support in a Nemawashi Decision Process. Graduate School of Business, The University of Texas, Austin, TX, 1988.

[33] R.T. Watson, G. DeSanctis, and M.S. Poole. Using a GDSS to Facilitate Group Consensus: Some Intended and Unintended Consequences. MIS Quarterly, 12(3), 463–477, 1988.
