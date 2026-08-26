---
otero_id: 22074
otero_key: "2SBS69K3"
title: "Towards integrating hypermedia and information systems on the web"
authors: "Chao-Min Chiu"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00142-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards integrating hypermedia and information systems on the web

Chao-Min Chiu<sup>\*</sup>

Department of Information Management, National Kaohsiung First University of Science and Technology, 1 University Rd. Yenchao, Kaohsiung, Taiwan, Republic of China

Received 15 January 2001; received in revised form 1 August 2001; accepted 24 November 2001

## Abstract

Our overall research goal is to provide hypermedia functionality to information systems (IS) through the WWW with minimal or no change to the IS itself. We feel that the systems should be able to generate links dynamically using a mapping mechanism to generate the hypermedia constructs instead of the links being hard-coded. This paper provides a systematic procedure for analyzing IS and building mapping rules to supplement them with a rich layer of links and other navigation, structuring, and annotation tools, resulting in new ways to view and manage knowledge and information relationships. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Data mining; Hypermedia; Information systems; Mapping rules; World Wide Web

## 1. Introduction

Making better business decisions is the key to gaining competitive advantage and thus leading to the success of the enterprise. An important factor in effective decision-making is the ability to access, understand, and utilize business information and metadata easily. New technologies have emerged to provide efficient tools (e.g. data warehousing) to consolidate data and uncover relationships, patterns, and trends. However, these tools do not take full advantage of hypermedia functionality (i.e. a rich layer of links and other navigation, structuring, and annotating functionality).

Our overall intent is to integrate information systems (IS) into the WWW and provide hypermedia functionality in them. To do this with minimal changes to IS, we use wrappers and mapping rules. The latter automatically convert IS generated information to hypermedia constructs (nodes—documents and screens, links—commands and relationships, and link markers—for selecting links) [9,10]. Mapping rules infer useful links that give users direct access to the primary functionality, infer metadata about IS objects, give access to relationships among information objects, and enable hypermedia functionality, such as annotation and ad hoc (user-declared) linking.

Hypermedia can be viewed as the science of relationship management: structuring, annotating and navigating information through links. What benefit do users gain from providing IS with hypermedia support? They may find it difficult to understand and take advantage of the myriad of inter-relationships in a knowledge base. Hypermedia helps by streamlining access to, and providing rich navigational features around, related information, thereby increasing user comprehension of information and its context [2,3].

Augmenting applications with direct access and hypertext structuring, annotation and navigation functionality should result in new ways: to view and manage an application’s knowledge and processes conceptually; navigate among items of interest and task stages; enhance knowledge with comments and relationships; target information displays to individual users and their tasks.

This paper discusses various information relationships and hypermedia functionality and contributes a systematic procedure for analyzing IS and building mapping rules that supplement IS with hypermedia support, resulting in new ways to view and manage knowledge and information relationships. This paper also reviews hypermedia design methodologies for modeling application structure and functionality (see Appendix A).

## 2. Hypermedia-enabled information management versus data mining

A data warehouse is a database that collects data extracted, transformed, and cleansed from operational and external data sources. It stores subject-oriented, integrated, nonvolatile, and time-variant data in support of business decisions [14]. An integrated warehouse environment usually consists of four major components: operational and external data sources, transformation tools, the warehouse database and data marts, and data analysis systems.

Operational data are raw data contained in operational and legacy systems. Data sources include flat files, pre-relational and relational databases. External data could be the data on the Internet or collected by other companies. Transformation tools are in charge of extracting, cleansing, transforming, aggregating, and summarizing data before loading it into the data warehouse. A data warehouse database is generally stored in a relational database management system. A data mart is a subset of the data warehouse that addresses a specific subject area and reflects departmental views of the corporation.

Data analysis systems include applications for online analytical processing (OLAP), data mining, and query reporting. Data mining is a process of uncovering relationships, patterns, and trends in huge volumes of data, and then transforming them to valuable information that can leverage business intelligence and improve the process of making decisions [20]. OLAP is a technology that performs data analysis using multidimensional and logical views of the data in the data warehouse. Our mapping mechanism and data mining share the common goal of extracting useful information relationships.

Our mapping mechanism discovers information relationships over IS objects. Data mining systems provide mechanisms for visualizing analyzed results, but unlike our mapping mechanism, they do not incorporate rich hypermedia functionality to provide a rich layer of links and other navigation, structuring and annotation tools.

## 3. System architecture

Apparently no other system automatically generates links and other hypermedia functionality for general IS. We here contribute a framework showing what such support entails. It identifies seven logical components that any such architecture must incorporate. The framework also helps in evaluating systems in terms of their potential for automatically generating hypermedia support.

Our architecture emphasizes the integration of the WWW with IS, thereby providing hypermedia functionality to each system. A novel feature of the architecture is the use of a hypermedia engine that contains mapping rules for automatically generating an extremely rich layer of links and other tools. Fig. 1 sketches the architecture with six example IS. Different implementations may implement these logical components in different ways. Since the WWW browser and server are normal WWW components, we only describe the functionality of other components.

\- An IS: This is the application system with which users interact to perform certain tasks. It typically produces output content for display. IS instances are written within an application package, such as an individual worksheet or database.

\- An IS wrapper: This translates and routes messages between its IS and the hypermedia engine. A comprehensive IS wrapper allows us to integrate an existing IS with few or no changes.

![](/api/attachments/2SBS69K3/fulltext/images/a8e47bbccbcf346f2db8b62e81d1c00464c609c84941c544a291c3a4e05c0bc6.jpg)  
Fig. 1. A conceptual framework for integrating hypermedia services and IS into the WWW.

\- The metadata database: This stores commands for accessing various relationships on IS objects and navigation facilities, meta-information about IS objects, and relationships that cannot be accessed directly from the IS (e.g. relationships in entity– relationship (E–R) diagrams).

\- The link database: This stores user-created annotations and ad hoc links.

\- The hypermedia engine: This is component-based middleware that provides hypermedia and relationship inference services. It coordinates relationship mapping and message passing among different IS application domains, thus aiding IS-to-IS integration. Components within the hypermedia engine must communicate with each other effectively. It consists of three types of components: command inference, navigational components, and IS mapping. The command inference component infers available commands and hypermedia functionality for the selected information object. Navigational components enable hypermedia functionality, such as annotations, query, search, and guided tours. IS mapping components convert IS-generated information to hypermedia constructs (nodes, links, and link markers), including OLAP and sales forecasting mapping components.

Many approaches exist for building components within the hypermedia engine and wrappers to integrate information systems into the WWW; these include: a common gateway interface (CGI), Java servlets, active server pages (ASP), hypertext pre-processor (PHP), and Java server pages (JSP). The CGI is an interface to the web server that enables users to extend the functionality and capability of the web server. Java servlets are CGI-like technology that allows users to extend server functionality. ASP, PHP and JSP are server-side scripting languages that allow users to write programs that contain a combination of HTML statements, text, and server-side scripts. There are also various protocols to support system components to communicate with each other, including common object request broker architecture (CORBA), distributed component object model (DCOM), remote method invocation (RMI), TCP/IP sockets, remote procedure call (RPC), object linking and embedding (OLE), automation, etc. CORBA is an Object Management Group specification that provides an architecture allowing objects to communicate with one another over networks, independent of the specific platforms and techniques. DCOM is Microsoft’s technology that enables software components to communicate directly across a network. RMI allows Java applications to call the methods of remote Java objects, sharing resources and processing load across systems. RPC enables a client application to invoke a procedure of a remote server application through a dummy procedure with the same name as the server, called stub. OLE automation is Microsoft’s technology that allows a client application to create and control an object in another application’s object model, using the exposed object’s interface. To integrate with multiple IS, components within the hypermedia engine must be implemented using server-side programming languages that support multiple protocols for integrating with multiple IS applications directly or through wrappers.

To integrate a new IS with the WWW and provide hypermedia support, one has to build a wrapper, declare mapping rules within components of the hypermedia engine, and store information (e.g. commands and access information) in the metadata database. One set of mapping rules can serve all instances of an IS.

We consider the integration of navigational hypermedia services into an OLAP server and a sales forecasting system as an example. Assume an automotive firm’s CEO is browsing the sales of each car type in the last 6 quarters and that the database has been enhanced with links that an OLAP mapping component intercepts. The component will send a command to the OLAP server to retrieve the analysis result. The OLAP mapping component then converts car names, years/quarters, and sales (number of cars sold) to links. After the CEO selects the link to a car name, the command inference component will retrieve the available commands for the selected object and convert them to links; e.g. there could be commands for forecasting sales, performing regression analysis, adding or retrieving comments, viewing a guided tour, searching, querying, etc. If the CEO selects the ‘‘sales forecasting’’ link, the sales forecasting component will be invoked and send a command to the Microsoft-Excel-based sales forecasting system to forecast the sales for the selected car type. If the CEO selects the ‘‘regression analysis’’ link, the regression component will send a command to the statistical tool to analyze regression relationship between car sales and commercial expenditure. Alternatively, if the CEO selects the ‘‘search’’ link, the search component will be invoked to search the intranet for web pages related to the selected car type. The CEO can also add or retrieve comments on the selected car type.

## 4. Relationship-navigation-rule analysis

The mapping rules would reside in and be invoked by components within the hypermedia engine. When providing large IS with hypermedia support, a facility that automatically inferred useful links from dynamically generated information would be helpful. Mapping rules convert dynamically generated information to hypermedia constructs (nodes, links, and anchors). They make extensive use of three features that Halasz [13] identified over 10 years ago, but they still have not been addressed in hypermedia or WWW applications such as: (1) creating and manipulating virtual structures of hypermedia components; (2) computing over the knowledge base during link traversal; (3) tailoring the hypermedia network [4]. Mapping rules infer useful links that enable users to view and manage objects that are accessed, handled, and generated by IS. We divide the process of building mapping rules into 10 steps.

## 4.1. Step 1: Identify users

IS converting to web interfaces might have a much broader range of users than systems without them. Knowing the audience of a system helps the developer broadly determine the entire range of important objects, meta-information, commands, and relationships. User analysis will help the developer focus on specific areas during the following steps.

## 4.2. Step 2: Analyze tasks

This step is to determine which tasks users will need to perform within IS; then the system developer can identify IS objects, commands performed on objects, their meta-information, and relationships among those associated with the tasks. This step also analyzes which functionalities of the IS are appropriate for a web interface. To integrate with multiple systems, the developer also should understand and identify the tasks that users will want to perform among systems. Task analysis provides a basis for the next three steps.

## 4.3. Step 3: Identify objects

Objects needed to be identified include all items displayed in web pages (graphs, labels, data value, etc.), as well as objects making up the system’s internal structure. In an OLAP system, objects of the internal structure include cubes, dimension tables, fact tables, attributes, measures and entries. Note that the developer identifies the types of objects and not individual instances.

## 4.4. Step 4: Identify objects’ meta-information

Three of the relationships in Yoo and Bieber’s relationship-navigation analysis (RNA) generic relationship taxonomy [28] concern relationships about the information object itself: characteristic, descriptive, and occurrence relationships. Here, we define a relationship as the association between two or more information objects within or among applications; thus the following three relationships are considered the object’s meta-information:

\- Characteristics: attributes, parameters, metadata, and other background information of the item.

\- Descriptive: definitions, illustrations, explanations of the item, etc.

\- Occurrence: multiple instances/views/uses/transformations of the same object in different parts of a system.

We also identify another type:

\- Transactional: information about changes to the item.

## 4.5. Step 5: Identify relationships among IS objects

Identifying explicit and implicit relationships for system objects forces developers to consider what information is of interest to users and then build mapping rules to access this. Sometimes meaningful relationships cannot be accessed directly, so developers have to declare relationships and store them in the metadata database.

Yoo and Bieber [27] identify the several types of relationships for system objects. Each gives the user easy access to aspect of an object:

\- Configuration/aggregation: connects a part to others or the whole, functionally or structurally.

\- Membership/grouping: connects a member of a collection to other members or a whole collection.

\- Classification: connects an item of interest to its instance or class.

\- Equivalence: connects instances of a particular object to a given item.

\- Similar/dissimilar: connects all items that share some positive or negative similarity.

\- Ordering: provides access to objects sequentially related to the object of interest.

\- Activity: deals with relationships that exist among elements that are involved in some kind of activity.

\- Intentional: connects an item of interest to the goals, arguments, issues, decisions, opinions, and comments associated with the item.

\- Influence: provides access to the item over which the item of interest has some type of influence.

\- Socio-organizational: connects an item of interest to the position, authority, alliance, role, and communication associated with the item in a social setting or organizational structure.

\- Temporal: provides access to items temporally related to the item of interest.

\- Spatial: provides access to objects spatially related to the item of interest.

## 4.6. Step 6: Identify commands

Commands underlying the <A> tags give users direct access to the primary functionality, various meta-information, relationships on objects, or navigational facilities. After identifying the implementation commands, we can then build mapping rules. The displayed labels for each command may be different from actual system commands. The hypermedia engine should pass the actual system commands to its IS.

## 4.7. Step 7: Build metadata database

Developers have to create a meta-database that stores commands for accessing various relationships on IS objects and navigational facilities. This can also store meta-information about objects and relationships that cannot be accessed directly from IS (e.g. relationships in entity–relationship diagrams).

## 4.8. Step 8: Identify possible navigational tools

Hypermedia researchers have developed several hypermedia features to help users easily navigate information and reduce cognitive overhead and disorientation (i.e. becoming ‘‘lost in the hyperspace’’ [11]). This support includes backtracking, history lists, paths, trails, guided tours, overview diagrams, structure-based queries, timestamps, footprints, fisheye views, annotations, bi-directional links, multi-destination (‘‘n-ary’’) links, etc.

Bush introduced the idea of trails [7] or paths. A trail is a logical sequence of links through information spaces [24]. It provides a context for browsing a series of related documents. Trails are usually implemented using a graphic interface, such as nodes, icons, or cards. The trail allows detours. Unlike the trail, however, a guided tour prohibits detours.

Many hypermedia systems provide a content-based query facility that is a text string search based on keywords or phrases. Unlike a content-based query, however, a structure-based query is based on node or link attributes [19].

Overview diagrams are graphical maps for providing a view of the relationships among interconnected nodes. There are two levels of overview diagrams: global and local [21]. Global overview diagrams provide a coarse-grained picture of the hypermedia network and can also provide access to local overview diagrams. Local overview diagrams provide a finegrained picture of the local neighborhood of a node. Overview diagrams should use checkmarks to serve as footprints to indicate both the current node and previously visited nodes [22].

The fisheye view is an alternative. This is a tree-like diagram that can show the hypermedia network in a balance of local detail and global context, based on the degree of interest [12]. The fisheye view shows great detail for nodes that are important and close to the user’s current node of interest and gradually diminishing amounts of detail for nodes that are progressively farther away.

A bi-directional link allows users to initiate a link from both of its ends. The system should provide a mechanism to help a user find the source from the destination and then navigate backwards from destination to source. A multi-destination link connects one source and multiple destinations. One way to implement multi-destination links is to pop up a dialog box which lists available links that each lead to a different destination [25,26].

Backtracking is probably the most popular navigation facility: it allows users to go back to the previously visited node. It reduces cognitive overhead and disorientation, because users can always return to a detour or incorrect browsing [5]. A history list shows all or some of previously visited nodes and allows users to go directly to any one of them. Most web browsers already provide backtracking and history list facilities.

An annotation (comment) facility allows users to add additional information to objects and exchange ideas. Some major hypermedia systems provide annotation facility: KMS [1], inter-media [8], etc. Annotations are relationships declared by users instead of inferred from the system structure. There are two types of annotations: public and private. A public annotation allows users to create comments and access them without any access control. Private annotations are only for individuals or groups who have the appropriate access permission.

The timestamp facility states the time period since the user last visited the node in the hypermedia network. This information can help users recognize the information context, since it relates it to their personal experience and how they browse the information space. Developers should decide which navigational tools the system should provide based on the anticipated user characteristics, the way that users perform tasks with the systems, the IS features, and available web technologies.

## 4.9. Step 9: Design user interface

The next step is used to decide how to present hypermedia and other integration services in a useful and intuitive way. Developers design the layouts of information objects. Developers also must decide what kind of interface is appropriate for listing IS functions: tree-like structures or pull-down menus? And what kind of interface is appropriate for listing IS commands: frame or pop-up dialog box (window)?

![](/api/attachments/2SBS69K3/fulltext/images/cd0dceeae76706db5ef69e0ec4ff7c659d469618b93fde2cb40435b2ca42ce53.jpg)  
Fig. 2. Some command and navigational links.

## 4.10. Step 10: Build mapping rules

The main purpose of mapping rules is to infer useful links. The rules reside in and become invoked by components within the hypermedia engine. We identify three types of links: command, navigational, and object. Command links are for operating on IS objects (see Fig. 2). Navigational links contain commands for invoking navigational tools. Object links represent IS objects (see Fig. 3). We explain each by using an OLAP system as the target IS.

## 4.10.1. Command and navigational links

When a user selects a link representing an IS object, mapping rules residing in the command inference component infer commands for operating upon the selected object and commands for providing hypermedia functionality based on the system name and object type. For this process, mapping rules should provide the following functions:

\- Search the metadata database for commands accessing various relationships and navigational facilities on the selected IS object.

\- Map commands to actual program names and then to links.

\- Form an HTML document that includes mapped links and sends the document to the web server.

For example, when a user selects an object link representing a car type, mapping rules will execute these functions and create the following HTML document (see Fig. 2). In reality, the system would present all commands (or a filtered subset).

Here:

1. The object ID ‘‘Future,Aquarius’’ means the car type ‘‘Aquarius’’ of the ‘‘Future’’ data cube.

2. The sales forecasting component is an ASP application called ‘‘Forecasting.asp’’. The link anchors that contain components for integrating with IS and operating on IS objects are called ‘‘command link anchors’’. The search component is an ASP application called ‘‘Search.asp’’. The link anchors that contain components for providing navigational functionality are called ‘‘navigational link anchors’’.

3. The ‘‘System’’ parameter is used to discriminate among different IS.

4.10.2. Object links

When a user selects a link representing a command, mapping rules residing in the IS mapping component will execute the command and then infer links from the output generated by the IS. For this process, mapping rules should provide the following functions:

\- Map commands to actual IS commands.

![](/api/attachments/2SBS69K3/fulltext/images/31c498a3e3de4be4469ee80a072b24c73519177eacf0d0743adbbb0af6aebe4c.jpg)  
Fig. 3. Some object links for representing a slice of the OLAP data cube.

\- Send actual commands and other parameters to the IS.

\- Receive display output from the IS.

\- Infer links from the output generated by the IS.

\- Create the HTML document with inferred links and send the document to the web server.

Fig. 3 shows a simplified example in which the command accesses a structural relationship. Mapping rules will execute the five aforementioned functions and send the HTML document to the web server.

Note that the link anchor contains a command inference component, which is an ASP application called ‘‘Command.asp’’. We call this type of link anchor an ‘‘object link anchor’’ since it represents an IS object displayed in the web page. When a user selects an object link, the ‘‘Command.asp’’ application within the link anchor will be invoked to infer available commands for operating on the selected object.

We have implemented a proof-of-concept prototype (see Fig. 4 for the prototype’s interface) using a Microsoft-Excel-based sales forecasting system and a Microsoft OLAP server. The hypermedia engine consists of eight components, which are ASP programs and provide the following functionality:

\- OLAP: allowing users to perform data analysis by browsing and drilling down the multidimensional data cube and viewing sales graphs.

\- Sales forecasting: providing sales forecasting for the next quarter, based on moving average approach.

\- Regression: allowing users to analyze the relationship between car sales and commercial expenditure. The prototype currently integrates with Microsoft-

![](/api/attachments/2SBS69K3/fulltext/images/2458f973c556e484ca8795c43c1a073c2993b23991732a780e65378cfb5257b8.jpg)  
Fig. 4. The interface of our prototype, multi-destination link dialog box, and outputs of executing query and sales forecasting commands

![](/api/attachments/2SBS69K3/fulltext/images/c38bb54f36994c921448d731668687eb269d99222cd8378b67bfe78008b6b58b.jpg)  
Fig. 5. A form for users to add comments.

Excel to support regression analysis. The integra tion with SPSS, however, is under development.

\- Command inference: inferring available commands for the selected information object and displaying the commands as multi-destination links. The implementation of the multi-destination links is to pop up a dialog box, which lists available links that each invokes a different component within the hypermedia engine.

\- Annotations: allowing users to add and retrieve comments on the selected information object (see Fig. 5).

\- Guided tours: providing a context for browsing a series of documents related to OLAP and sales forecasting.

![](/api/attachments/2SBS69K3/fulltext/images/6e87fb1e142a4b0193611c466fd7be8f58e1e8e7ca35328bda64b1f9181e75af.jpg)  
Fig. 6. Results of executing ‘‘search’’ command.

\- Query: allowing users to query the database for information related to the selected information object.

\- Search: allowing users to search the intranet for web pages related to the selected information object by using the object ID or user inputs (see Fig. 6).

## 5. Conclusion

The WWW provides the infrastructure for supplementing information systems with hypermedia support. We believe that integrating hypermediasupported business IS on the WWW should constitute a major thrust for the WWW research. It will go a long way toward making complex applications more understandable. When reengineering IS for the WWW or developing new web applications, dynamic relationship mapping could be an effective way to add additional hypermedia links. This will facilitate adding useful hypermedia functionality to new WWW applications (especially IS) to view and manage their knowledge and information relationships. We hope this paper will call people’s attention to this opportunity.

## Acknowledgements

The author wishes to thank Michael Bieber, the chief editor and anonymous reviewers for their helpful comments and suggestions. Thanks are also due to Tay-Der Hwang, Jyh-Horng Lin, Tsuey-Fang Chen, and I.-Jye Lin for their help in implementing the prototype. This research was supported in part by a grant from the National Science Council (NSC) of Taiwan, Republic of China.

## Appendix A. Hypermedia design methodologies

Hypermedia design methodologies exist for modeling application structure and functionality.

The relationship management methodology (RMM) [15] is strongly based on entity–relationship (E–R) abstracts. It comprises seven steps: E–R design, slice design (entity presentation), navigational design, conversion protocol design, user interface design, run-time behavior design, and construction and testing.

The object-oriented hypermedia design methodology (OOHDM) [23] is a model-based approach for analyzing the process of building hypermedia applications. It consists of four phases: conceptual design, navigational design, abstract interface design and implementation. OOHDM focuses in particular on the navigational design and abstract interface design phases.

Enhanced object-relationship model (EORM) consists of three frameworks: class, composition and graphical user interface (GUI) [17]. It represents a link as a first class object and provides a reusable link class library to facilitate the mapping of relation schematics into link class. EORM consists of four phases: information analysis, functional analysis, object modeling, and hypermedia mapping.

Hypertext structure description language (HSDL) is a schema-based approach for authoring large and structured hypertexts [16]. The core concepts of HSDL contain class schema that represents classes in the target domain and relationships among objects (i.e. links), and instance schema that represents instances of the classes and the relationships. After filling the empty instances with the content, an author can use the compilation program called expanders to map the schema to HTML.

Scenario-based object-oriented hypermedia design methodology (SOHDM) is an approach for developing process-oriented hypermedia information systems for supporting organizational processes [18]. It consists of six phases: domain analysis, object modeling, view design, navigation design, implementation design, and construction. These current hypermedia design methodologies, however, are for designing stand-alone, retrieval-oriented hypermedia applications instead of IS applications enhanced with hypermedia support and dynamic information relationship inference.

A closer approach to our 10-step relationshipnavigation-rule analysis (RNRA) approach is Bieber and Yoo’s two-stage web engineering [6]. With web engineering, first the software engineer performs a relationship-navigation analysis, analyzing the application specifically in terms of its intra- and interrelationships. RNA has five steps: stakeholder analysis, element analysis, relationship and meta-information analysis, navigation analysis, and relationship and feasibility analysis. Second, a dynamic hypermedia engine (DHE) automatically generates links for each of these relationships and meta-information items at run-time, as well as sophisticated hypermedia navigation techniques not often found on the web (e.g. guided tours, overviews, and structural query) on top of these links.

The major difference between web engineering and our RNRA approach is that we clearly define the transition from determining the relationships to implementing the mapping. RNA supplements our mapping mechanism. Combining RNA and our mapping routine approach forms our relationship-navigation-rule analysis technique for engineering applications for the World Wide Web.

## References

[1] R. Akscyn, D. McCracken, E. Yoder, KMS: a distributed hypermedia system for managing knowledge in organizations, Communications of the ACM 31 (7), 1988, pp. 820–835.

[2] M. Bieber, C. Kacmar, Designing hypertext support for computational applications, Communication of the ACM 38 (8), 1995, pp. 99–107.

[3] M. Bieber, H. Oinas-Kukkonen, V. Balasubramanian, Hypertext functionality, ACM Computing Surveys’ Electronic Symposium on Hypertext and Hypermedia 31 (4es), Article No. 32, 1999.

[4] M. Bieber, F. Vitali, Toward support for hypermedia on the World Wide Web, IEEE Computer 30 (1), 1997, pp. 62–70.

[5] M. Bieber, F. Vitali, H. Ashman, V. Balasubramanian, H. Oinas-Kukkonen, Fourth generation hypermedia: some missing links for the World Wide Web, International Journal of Human Computer Studies 47 (1), 1997, pp. 31–65.

[6] M. Bieber, J. Yoo, Hypermedia: A Design Philosophy, ACM Computing Surveys’ Electronic Symposium on Hypertext and Hypermedia 31 (4es), Article No. 29, 1999.

[7] V. Bush, As we may think, Atlantic Monthly 176, 1945, pp. 101–108.

[8] T. Catlin, P. Bush, N. Yankelovich, InterNote: extending a hypermedia framework to support annotative collaboration, Proceedings of Hypertext 89, 1989, pp. 365–378.

[9] C.-M. Chiu, Reengineering information systems with XML, Information Systems Management 17 (4), 2000, pp. 40–55.

[10] C.-M. Chiu, M. Bieber, Toward hypermedia support for information relationship management, Journal of Information Science 27 (2), 2001, pp. 93–100.

[11] J. Conklin, Hypertext: an introduction and survey, IEEE Computer 20 (9), 1987, pp. 17–41.

[12] G.W. Furnas, Generalized Fisheye Views, Proceedings of the ACM CHI’86 Conference on Human Factors in Computing Systems, Boston, MA, 1986, pp. 16–23.

[13] F. Halasz, Reflection on NoteCards: seven issues for the next generation of hypermedia systems, Communications of the ACM 31 (7), 1988, pp. 836–855.

[14] W.H. Inmon, The data warehousing and data mining, Communications of the ACM 39 (11), 1996, pp. 49–50.

[15] T. Isakowitz, E. Stohr, P. Balasubramanian, RMM: a methodology for structuring hypermedia design, Communications of the ACM 38 (8), 1995, pp. 34–44.

[16] M. Kesseler, A schema-based approach to HTML authoring, World Wide Web, Journal 1 (1), 1996, pp. 619–631.

[17] D.B. Lange, An Object-Oriented Design Method for Hypermedia Information Systems, Proceedings of the 27th Annual Hawaii International Conference on System Sciences, Maui, Hawaii, 1994, pp. 336–375.

[18] H. Lee, C. Lee, C. Yoo, A scenario-based object-oriented design methodology, Information and Management 36 (3), 1999, pp. 121–138.

[19] Y.K. Lee, S.J. Yoo, K. Yoon, P.B. Berra, Querying Structured Hyperdocuments, Proceedings of the 29th Annual Hawaii International Conference on System Sciences, Maui, Hawaii, 1996, pp. 155–164.

[20] T.M. Mitchell, Machine learning and data mining, Communications of the ACM 42 (11), 1999, pp. 30–36.

[21] J. Nielsen, The art of navigating through hypertext, Communications of the ACM 33 (3), 1990, pp. 296–310.

[22] J. Nielsen, Multimedia and Hypertext: The Internet and Beyond, AP Professional, Boston, MA, 1995.

[23] D. Schwabe, G. Rossi, S. Barbosa, Systematic Hypermedia Application Design with OOHDM, Proceedings of the 8th ACM Conference on Hypertext, Washington, DC, 1996, pp. 116–128.

[24] R. Trigg, Guided tours and tabletops: tools for communicating in a hypertext environment, ACM Transactions of Office Information Systems 6 (4), 1988, pp. 398–414.

[25] F. Vitali, C.-M. Chiu, M. Bieber, Extending HTML in a principled way with displets, Computer Network and ISDN Systems 29 (8–13), 1997, pp. 1115–1128.

[26] N. Yankelovich, B.J. Haan, N.K. Meyrowitz, S.M. Drucker, Intermedia: the concept and the construction of a seamless information environment, IEEE Computer 21 (1), 1988, pp. 81–96.

[27] J. Yoo, M. Bieber, Towards a Relationship Navigation Analysis, Proceedings of the 33rd Hawaii International Conference on System Sciences, Maui, Hawaii, 2000 (CD-ROM).

[28] J. Yoo, M. Bieber, Finding Linking Opportunities through Relationship-Based Analysis, in: Proceedings of the 11th ACM Conference on Hypertext, San Antonio, TX, 2000, pp. 181–190.

![](/api/attachments/2SBS69K3/fulltext/images/ba779c8606747d38199e3ebba48fa18b0ecdcb20a0a3f0614bd08f56a1072110.jpg)

Chao-Min Chiu is an Associate Professor in the Department of Information Management at the National Kaohsiung First University of Science and Technology, Taiwan, Republic of China. He holds a PhD in management from the Rutgers University. His current research interests include hypermedia support for decision-making, web mining, and means-end chains. His research has been published in the Journal of Information Science, Information Systems Manage-

ment, Information and Software Technology and Computer Networks and ISDN Systems.
