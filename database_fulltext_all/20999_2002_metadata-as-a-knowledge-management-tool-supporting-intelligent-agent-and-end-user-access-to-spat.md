---
otero_id: 20999
otero_key: "2N3MABPP"
title: "Metadata as a knowledge management tool: supporting intelligent agent and end user access to spatial data"
authors: "Lawrence A. West; Traci J. Hess"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00102-6"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Metadata as a knowledge management tool: supporting intelligent agent and end user access to spatial data

Lawrence A. West Jr. \*, Traci J. Hess <sup>1</sup>

MIS Department, College of Business Administration, University of Central Florida, Orlando, FL 32816-1400, USA

Received 9 October 2000; accepted 6 February 2001

## Abstract

Many factors have led to explosive growth in the use of geographic information system (GIS) technology to support managerial decision making. Despite their power, utility, and popularity, however, GIS require a significant amount of specialized knowledge for effective use. This paper describes a GIS-based decision support system (DSS) design approach that embeds much of this knowledge in well-structured metadata and presents it to the decision maker through an appropriate interface or software agents, thereby decreasing system learning costs and improving effectiveness. The metadata design from a spatial decision support system (SDSS) is presented along with illustrations showing how the design addresses specific knowledge management (KM) problems. The paper then discusses how the knowledge management design approach can be generalized to other SDSS, to DSS in general, and to data warehouses. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Metadata; Knowledge management; DSS; GIS; Information system design; Agent; End-user

## 1. Introduction

Perhaps nothing illustrates the perceived importance of geographic information system (GIS) technology as a decision support (DSS) tool better than Microsoft’s 1999 entry into the GIS market with its MapPoint 2000 product. Microsoft has positioned MapPoint in its Office suite of applications for endusers but is clearly aiming the product at business decision makers [16]. This step follows a 30-year process during which GIS transitioned from a specialized tool for scientists, engineers, and planners using sophisticated hardware and software, to a DSS shell for managerial decision makers using standard PC hardware and end-user oriented software [3,4,9,12].

Modern GIS technologies possess many of the characteristics required of a DSS generator [4,21,24]. GIS typically have data storage and retrieval capabilities, graphic display capabilities (maps, images, and graphs), a user interface (including the ability to create custom interfaces for specific DSS), and extensive modeling capabilities. While one of the unique modeling capabilities of GIS is the ability to analyze data based on the spatial location of the objects in the data, many GIS include additional modeling tools such as network algorithms (shortest route, minimum spanning tree, etc.), and the ability to incorporate additional models through either custom coding in the GIS’s internal development language, or through calls to external tools. Further, some modern GIS packages can serve as components (what Sprague and Carlson [19] referred to as DSS Tools) of systems built in other DSS generators or can be components of specific DSS built using standard development languages. For example, several manufacturers, including Environmental Systems Research Institute (ESRI) and the MapInfo Corporation make DLL or OCX components that enable programs developed in C++, Visual Basic, etc., to include GIS capabilities without the purchase of a full GIS package.

As GIS have become more popular as a managerial decision support tool, more end-users (as opposed to GIS specialists) find themselves using this software. If a flexible spatial decision support system (SDSS) is desired (rather than a preprogrammed application), however, the end-user becomes responsible for selecting geographic components and determining how these components should be displayed and analyzed. In this flexible environment, end-users need access to declarative knowledge that describes the geographic data available to them. Less experienced end-users will also require procedural knowledge that describes how to use and render the geographic data where such procedural or ‘‘how to’’ knowledge is typically acquired by an end-user through training and system documentation. In a GIS environment, however, the volume and complexity of this procedural knowledge can create a significant obstacle to system use. Thus, SDSS oriented toward inexperienced end-users require a design approach that will support their decision making activities.

The literature on information system design theory (ISDT) provides guidelines for developing and testing such a system by specifying a design approach that will support organizational goals [25]. An ISDT can subsequently be tested by using the design to build a system and examining how well the resulting system achieves the specified goals. Most ISDTs have been developed for specific types of information systems such as vigilant EIS [25] and user calibration in decision support systems [11], and we follow this model here. Our design approach is specifically oriented at SDSS and other spatially oriented decision making tasks, including data warehouses, but we also find that our knowledge management approach is generalizable to almost any DSS.

This paper describes a knowledge management (KM) design approach for supporting end-users with spatially oriented decision making by reporting on a specific SDSS that uses the approach. The system uses a metadata repository as a store of declarative knowledge about the spatial data available in the system. Procedural knowledge about performing spatial analysis is embedded in software agents that assist users with difficult, spatially oriented tasks. Finally, as in most DSS, users are expected to possess some procedural knowledge related to the decision making domain. With this distribution of knowledge, users are supported in some tasks by using the metadata repository directly and in others by using the software agents that, in turn, access the metadata. Reflection suggests that this knowledge management approach to designing SDSS, including the distribution of knowledge between metadata, agents, and end users, has similar potential as a determinant of system success in any DSS (spatial or otherwise) where both declarative and procedural knowledge are needed to effectively accomplish the decision making task.

This paper has contributions at several levels. First, it reports on a KM design approach that provides support for end-user access to SDSS using both declarative and procedural knowledge. This design, along with the decomposition of GIS knowledge into declarative and procedural components, should interest SDSS designers seeking to improve the usability of their systems for less experienced end-users. Second, the successful deployment of this design in an SDSS is described. Illustrations of how metadata and software agents support specific GIS tasks should provide additional insight to SDSS designers from an applied perspective. Lastly, the ability to generalize the KM design and implementation to a broader range of systems has implications for the designers of any end-user oriented DSS, regardless of its reliance on spatial data. A specific generalization includes the application of this approach to data warehouse applications.

The next section of the paper provides some background information on GIS and describes the specific SDSS in which the KM design was implemented. This discussion includes the identification of specific GIS-related tasks for which user support is desirable. The following section describes the KM design approach implemented, including the structure of the GIS-related metadata and the support provided by agents. This section is followed by two in-depth examples from the SDSS implementation and provides explanations of how specific metadata elements can be used to support both end-user and software agent execution of GIS tasks. Additional implementation examples are briefly highlighted. Finally, the paper emerges from these case-specific discussions to reach the aforementioned generalizations regarding SDSS, DSS, and data warehousing.

## 2. GIS for decision support

In many ways, the history of GIS use for managerial decision making has mirrored the history of MIS and DSS, but with a lag of one to two decades. In 1971, Gorry and Scott Morton [7] wrote of the need to provide relevant information to decision makers. They alluded to an existing environment where management information was requested, forwarded to computer operators for production, printed, and returned; often in an iterative process. A combination of needs recognition and technological improvements then leads to the modern management support environments that include end-user computing, DSS, GDSS, and MIS.

GIS operated in much the same way. Even at the time that mainstream data processing was embracing distributed technologies and end-user access to data and programming, GIS technologies required specialized (and expensive) hardware and software, and required esoteric knowledge that was not available to the average managerial decision maker. Instead, requests for spatial analysis (usually leading to a thematic map) were forwarded to the GIS specialist, produced, and returned; again, often in an iterative process.

By the early 1990s, however, price/performance improvements in PCs resulted in widely available computing platforms that were capable of efficiently handling the specialized computation needed for GIS. More computing platforms led to increased investment in end-user oriented GIS software and the increased availability of business related data. By the mid-1990s, GIS software had evolved to the point where products from competing vendors contained all of the features of a DSS generator and the ready customization available in most modern GIS provide the ability to construct specific DSS with as much task-specific functionality as was necessary.

New GIS software found a ready market. By one estimate, 75% of all corporate databases contain some geographic information (street address, zip code, city, area code, etc.) [23], and GIS gave managers the ability to leverage this positional data in ways not possible with conventional information technology [15]. One important result of these changes was the steady diffusion of GIS from the realm of scientists and engineers into the world of business [9]. GIS issues also began to appear in the mainstream MIS literature [4,13,17,27,28,29].

The remainder of this section briefly presents several background issues needed before presenting the KM design approach implemented. A brief overview of GIS capabilities is followed by a summary of some of the aspects of GIS technologies that make use by untrained end-users problematic without additional support. Because the presentation of the metadata structure to follow is drawn from a specific SDSS, a brief overview of this system is also provided.

## 2.1. GIS capabilities

While it would take a book (or two) to fully describe the capabilities of GIS, a few paragraphs must serve our purposes here. In the simplest analysis, GIS are specialized database management systems (DBMS) that store both conventional attribute data (usually in a relational format) and information on the spatial location of each object (record) in the theme or coverage (table). Further, the GIS is able to translate the spatial coordinates of an object into the coordinate system used by the computer’s display and printer.

Some of the simplest functionality offered by a GIS, then, is the ability to display maps on the computer screen. Modern GIS are also able to apply symbology (colors, icons, etc.) to map features based on attribute data such as sales volumes, type of building, etc. Since GIS can display multiple layers (themes or coverages) simultaneously, users may select themes to visually show relationships between objects in different data coverages [4,18]. A user could, for example, display a map showing census tract boundaries with each tract color-coded by median income. The user can then overlay a theme showing customer addresses. The resulting map would immediately show if clusters of customers were concentrated in areas of a particular income level. The same analysis is possible by symbolizing the census data based on ages, family size, and ethnic origin.

A second major capability of GIS is the ability to perform queries and joins between records based on spatial location. In conventional relational database management systems (RDBMS), queries are performed by comparing field values with values specified in the query. Joins between tables are constructed by comparing primary key values in one table to foreign keys in another and generally require that the database be designed to support the relationship between the involved tables. Creating joins between tables created by different designers can often be problematic.

In GIS, however, the GIS engine is ‘aware’ of the location of objects (records) in different themes and can tell when objects in one theme are proximate to objects in another. In fact, most GIS have a rich set of spatial operators such as ‘‘IS WHOLLY CON-TAINED BY,’’ ‘‘INTERSECTS,’’ ‘‘IS WITHIN DISTANCE OF,’’ etc. Geography then becomes a natural key between tables. Conventional SQL-type queries and aggregations can then be performed between tables by joining fields such as zip code with county name or census block identifier.

## 2.2. End-user GIS problems

As businesses continue their increasing use of GIS, more end-users will find themselves using spatially or geographically related data for decision making purposes. Unfortunately, using GIS for decision support requires not only domain knowledge and general computing skills, but also specialized knowledge of geographic concepts, maps, and GISspecific actions [27]. The volume of data used in GIS, the number of diverse data sources, and the spatial relationships among the data add to the complexity of the GIS environment. Further, SDSS share with other DSS the need for users to select the data, queries, and models that are appropriate to the decision making task at hand. West [27] identified four GIS-specific tasks that require specialized knowledge for effective end-user operation of GIS or SDSS, and these tasks are shown in Table 1. The table also includes spatial analysis as a fifth GISspecific task because it is applicable to GIS used in an SDSS and also requires specialized knowledge for end-user operation.

End-user tasks in GIS (adapted from Ref. [27])

<table><tr><td>Task</td><td>Description</td></tr><tr><td>Identifying relevant themes</td><td>In a system or environment containing a large selection of GIS coverages, it will not always be clear which coverages should be considered or queried for a specific decision making task.</td></tr><tr><td>Editing/adding data</td><td>Data integrity is a key issue in any database system and GIS are database systems. End-user access to the system must protect the data against both conventional data integrity problems but also against GIS-specific problems.</td></tr><tr><td>Layering themes</td><td>When themes are displayed on a monitor or printed map it is important that denser themes lay under less dense themes so as to not mask the sparser theme. A related task is managing resolution-dependent display of themes.</td></tr><tr><td>Reporting results</td><td>Creating maps is more complex than just printing what displays on the screen. Deciding on the appropriateness of several map components and placing these components can be problematic for inexperienced users.</td></tr><tr><td>Spatial analysis</td><td>Many SDSS decisions require analyzing data from disparate coverages to identify relationships between data. This task may require the use of the spatial join operators or use of network algorithms such as shortest route or minimal spanning tree.</td></tr></table>

## 2.3. System overview

The KM design approach developed to address the aforementioned GIS end-user problems was implemented in the Florida’s Marine Resource Information System (FMRIS). FMRIS is a specific SDSS that provides decision maker access to map and regulatory data pertaining to construction in a threecounty area of South Florida (including the environmentally sensitive Florida Keys and the Everglades). The system provides support to overcome several distinct user difficulties with the use of GIS for decision making. While the system provides several capabilities, the two most important are the following.

(1) Constructing a map of a user-specified area of interest that properly displays all of the objects in the area that fall into any of several categories (specified by the user).

(2) Displaying a list of all statutes, rules, and regulations pertaining to a user-specified area of interest based on the presence of regulated land characteristics (endangered species habitats, zoning, wetlands, public lands, flood zones, etc.). The regulatory findings are further linked to points of contact for regulatory agencies, to information on specific permits needed, and to bibliographic information.

An important feature of FMRIS that is very pertinent to the objective of this paper is that the themes (database tables with geographic information) come from a multitude of producers. A decision maker exploring the feasibility of a site for an office building or mall may need information on zoning (city or county); endangered species habitats (state and federal); transportation and utility infrastructure (city, county, state, and federal); wetlands (state and federal); flood and storm surge zones (state and federal); etc. FMRIS brought together data produced by a multitude of agencies, using different file and field naming schemes, and containing attribute data that made sense to the producers but that may not be as meaningful to the uninitiated user. More information on FMRIS, including the limitations faced by decision makers and supported by the system, can be found in Ref. [26].

## 3. A knowledge management approach

The KM approach used to address end-user GIS problems in FMRIS began with the identification of general GIS KM issues. The end-user GIS tasks shown in Table 1 were categorized into three general GIS KM issues: (1) relationships, (2) integrity, and (3) presentation. The GIS tasks of identifying relevant themes and spatial analysis were classified as a relationship KM issue as they involved the end-users efforts to understand how the various GIS data available relate to one another and to the decision task at hand. Editing and adding data was classified as an integrity KM issue as the primary goal of this task is to protect the integrity of GIS information. The layering themes and reporting results tasks both relate to the rendering of geographic images and were thus classified as presentation KM issues. A summary of the categorization process and the three GIS KM issues is provided in Table 2.

Table 2 also describes the declarative and procedural components of each KM issue and this differentiation provided a means for allocating support between metadata and agents. The declarative elements shown in Table 2 were used to develop the metadata structure while the procedural elements were embedded in software agents or left to end-users. Again, both end-users and agents draw on the metadata to perform their tasks. The remainder of this section describes the metadata and software agent components of the KM approach.

## 3.1. The FMRIS metadata architecture

Metadata, self-describing data about data, can be divided into two types, the technical details and the business uses of the described data [21]. As a knowledge management tool, the metadata in the FMRIS stores declarative knowledge regarding the relationships, integrity, and presentation of the geographic data used by the system. Fig. 1 presents a logical data model of the entire FMRIS database (excluding the thematic coverages) and highlights how the metadata tables relate to the other sections of the database. Table 3 lists and briefly describes the four major sections of the database in order to put the metadata section in context. The other three sections, ‘‘Regulations,’’ ‘‘Regulating Agencies,’’ and ‘‘Bibli-

Table 2  
End-user knowledge management issues in GIS

<table><tr><td>Task [27]</td><td>KM issues</td><td>Knowledge types</td></tr><tr><td>Identifying relevant themes</td><td>Relationships</td><td>Declarative: Existence of the theme, contents of the theme, relevance of the theme to a decision making task, reliability of the data, existence of an analysis technique, suitability of theme types for specific techniques.</td></tr><tr><td>Spatial analysis</td><td></td><td>Procedural: How to retrieve and load the theme, how to use themes with specific analysis techniques.</td></tr><tr><td>Editing/adding data</td><td>Integrity</td><td>Declarative: Type of data needed in fields, whether a field requires a value.Procedural: How to create new records in a GIS theme where both attribute and graphical data must be specified.</td></tr><tr><td>Layering themes</td><td>Presentation</td><td>Declarative: Type of theme, data density, appropriate display resolutions, map label fields, theme record colors, theme symbol fields.</td></tr><tr><td>Reporting results</td><td></td><td>Procedural: How to layer themes appropriately, how to turn themes on and off at appropriate resolutions. How to apply symbology and labels to a map; how to add other map elements such as a legend, north arrow, or scale.</td></tr></table>

ography,’’ are specific to the FMRIS SDSS and are not discussed beyond Table 3. The knowledge management approach demonstrated in the ‘‘Metadata’’ section, though, is significantly more generalizable and is discussed throughout the remainder of the paper.

![](/api/attachments/2N3MABPP/fulltext/images/2d1921d3a15bfa932c0b4d8bb48b7dfdba26a6ca4c4a9d723bdd86dc60e4e677.jpg)  
Fig. 1. The FMRIS database structure.

Table 3 FMRIS database components

<table><tr><td>Database section</td><td>Tables</td><td>Description</td></tr><tr><td>Metadata</td><td>SiteTypeCoverageSiteTypeaCoverageCoverageFieldsFieldValue</td><td>Embeds accessible knowledge about the available themes into the database for use by the software agents and the user.These tables are discussed extensively throughout the paper.</td></tr><tr><td>Regulations</td><td>Regulation RegulatedSiteTypeaPermit</td><td>Contains information on specific statutes, rules, and regulations of interest to FMRIS users as well as to permits mandated by these regulations.</td></tr><tr><td>Regulating Agencies</td><td>RegulatingAgency RegulatingOfficeContact ContactLinka</td><td>Contains information on agencies responsible for regulatory enforcement and permitting, branch offices of the agencies, and individual points of contact in the agencies.</td></tr><tr><td>Bibliography</td><td>PublicationKeyWordsAuthorsInstitutionalAuthors</td><td>Contains bibliographic information on the area of interest. Data is searchable directly and references pertinent to specific geographic records are also available after a regulatory search.</td></tr></table>

<sup>a</sup> Indicates tables needed to decompose M:M relationships.

The five tables contained in the heavy solid line in Fig. 1 constitute the FMRIS metadata, and Table 4 provides a general description of each metadata table along with the KM issues each supports. Fig. 2 is an expanded partial logical data model that depicts more detailed information on the metadata structure, such as table fields and primary keys.

The Coverage table stores information on the geographic themes available in FMRIS. Because these themes are often not familiar to or commonly used by end-users in their decision making scenarios, the SiteType table was created to relate end-users’ business terms to the geographic themes provided by the system. The SiteType table stores geographic concepts that are familiar to end-users and then the CoverageSiteType table shows how these concepts are related to the geographic themes stored in the Coverage table. These three metadata tables, SiteType, CoverageSiteType, and Coverage, thus provide declarative knowledge on geographic data relationships. As noted in Table 4, the CoverageFields table primarily provides data integrity information, while the Coverage and FieldValue tables provide declarative presentation information. The use of these metadata tables will be explored in much greater depth in the examples that follow.

Table 4 The FMRIS metadata

<table><tr><td>Table name</td><td>Description</td><td>KM issues</td></tr><tr><td>Coverage (A collection of records that can be displayed on a map).</td><td>Each record in the coverage table describes one GIS theme contained in the system. GIS themes are stored in their own specialized directory structure and are not truly part of the relational database.</td><td>Relationships and presentation</td></tr><tr><td>SiteType</td><td>The SiteType table was so named because it contains a listing of all specific categories of land characteristics that could be of interest to FMRIS users. Examples include “Endangered Species Habitat,” “Public Lands,” “Park,” etc.</td><td>Relationships</td></tr><tr><td>CoverageSiteType</td><td>Decomposes the many-to-many relationship between Coverage and SiteType.</td><td>Relationships</td></tr><tr><td>CoverageFields</td><td>Contains one record for each field in each coverage (theme). In addition to descriptive data about the field, this table contains information used to enforce data integrity rules when theme records are added or updated by end-users.</td><td>Integrity</td></tr><tr><td>FieldValue</td><td>Contains one record for each unique value of selected discriminator fields in a theme. E.g., in the theme covering property zoning, one field contains the actual zoning designation for each parcel. TheFieldValue table contains one record for each possible value of this field along with information on how matching records are to be color coded when they are displayed.</td><td>Presentation</td></tr></table>

![](/api/attachments/2N3MABPP/fulltext/images/4658806459adc0304343ff1c630b20ad9d2fdaf92fa758e1a137d1d47c2a39be.jpg)  
Fig. 2. The FMRIS metadata tables.

## 3.2. Software agents in FMRIS

Software agents are often informally described as personal computing assistants that carry out a task or process for the user [2,6]. Within the context of DSS, agents have been more formally described as autonomous software implementations of a task or goal that work independently, on behalf of the user or another agent [10]. These robust, autonomous programs are often used to provide an abstraction for the increasing complexity of computing and an alternative means of desktop manipulation. Researchers in various disciplines have noted the limitations of the traditional, direct manipulation interface (including scalability and level of expertise) and have suggested agents as a means to indirectly manage our computing environment [14]. The limitations of a direct manipulation interface are not only present, but are typically exaggerated in SDSS due to the volume and complexity of spatial data. Software agents would thus seem to be a suitable and most needed solution for providing enduser procedural assistance in SDSS.

The agents in FMRIS were used to reduce the level of procedural knowledge an end-user would need to operate a GIS. In the past, the procedural knowledge required to effectively use a SDSS was stored with GIS experts and recorded in the system documentation. In the FMRIS KM approach, software agents were viewed as an alternative means of managing procedural knowledge. This knowledge was embedded in the agents so that the agents could complete GIS tasks and access the metadata on behalf of the end-user. It was expected that less experienced endusers would benefit most from the use of agents, but that generally end-users would appreciate at least some of the task automation provided by the agents. The agents implemented in FMRIS were highly encapsulated subroutines that performed GIS-specific tasks according to the preferences of the user. In particular, they performed the problematic tasks itemized in Table 1 as if the tasks were given to a human assistant who understood GIS operations and the problem domain.

The individual agents and their assigned goals corresponded to the GIS KM issues listed in Table 2. For example, the FMRIS presentation agent managed presentation procedural knowledge such as how to layer geographic themes, accessing presentation metadata as needed. A more detailed description of the agents implemented in FMRIS is provided in the next section of the paper.

## 4. Metadata in action

This section of the paper provides a detailed description of two specific FMRIS tasks, illustrating how the knowledge embedded in the metadata plays a key enabling role for task completion. The first task, selecting data for analysis, is primarily an end-user task that requires access to declarative knowledge stored as metadata. A software agent accomplishes most of the second task, displaying GIS themes for analysis, using a combination of procedural knowledge stored within the agent itself and declarative knowledge stored in the metadata. The section also provides brief overviews of additional FMRIS tasks that demonstrate agent and metadata knowledge support.

## 4.1. Selecting data for analysis

The result of a spatial analysis is almost always a thematic map, a map showing the various objects that affect the user’s decisions. As in many decision making contexts, the FMRIS user must determine which of a hundred map themes is relevant to the problem at hand. In many ways, this situation corresponds to that facing a decision maker using a data warehouse or engaged in data mining operations. The user is concerned with including all relevant data and with excluding irrelevant data from the analysis.

## 4.1.1. The decision making context

While FMRIS supports drilling down through all available map themes and discovering every type of object in a specified area, it is much more common for the user to focus on a subset of objects for certain decisions. For example, a builder seeking to make an initial selection of possible construction sites may wish to first eliminate all sites that are proximate to either known wetlands or endangered species habitats, as well as public lands (parks and preserves, military bases, etc.). By eliminating sites that are obviously problematic, the builder can then perform more detailed investigations on remaining sites. To conduct this preliminary investigation, the user needs to load all themes that pertain to any of these types of sites, and then review these themes for proximity to possible construction sites.

## 4.1.2. The user’s knowledge problem

The user’s problem in this context comes under the relationship KM issue in Table 2. Specifically, the user lacks factual knowledge about what data exists in the repository of themes and whether specific data (a theme) is relevant to the decision at hand. At its completion, FMRIS contained over 100 specific spatial themes and had unlimited capacity for adding more.

A compounding problem is the fact that none of the FMRIS themes were produced by the system’s developers. Instead, each was produced by one of two-dozen public agencies belonging to various levels of government (city through federal). The various producers used a variety of naming schemes for the themes and attribute data in each theme. Some themes had cryptic coded names while others used filenames that needed modification to suit the FMRIS operating system. In short, perusing a list of available theme names was not an effective way to locate themes for analysis.

A final compounding problem was that in some themes only certain records are relevant to the user’s current decision. In our example above, a theme containing zoning classifications inside city limits would contain individual records indicating that a parcel was zoned for government use. The decision maker would want to see these records but not the records in the same theme zoned for retail, singlefamily homes, etc.

## 4.1.3. The metadata remedy

FMRIS provided four methods for selecting themes for analysis. One of these methods performed a drill-down through all available coverages with no attempt to create a visible map. This technique required no user selection of themes and only used the Coverage metadata table to determine the availability and directory locations of themes.

The second method allowed users to select themes individually by browsing the list of all available themes (stored in the Coverage metadata table). Instead of relying on the aforementioned (and often cryptic) producer file names, however, this method makes use of a simple interface and two attributes of the Coverage table to support the user. The Name attribute contains a 20-character name of the theme that makes sense to the user. Example values included ‘‘Miami Zoning,’’ ‘‘Bridges,’’ and ‘‘Manatees.’’ The Description attribute contains a 255-character expanded description of the theme that is automatically available to the user via the theme selection interface. Finally, it is relatively easy for the user to see additional information such as the theme’s producer (Producer attribute) and provider (if other than the producer) and the dates on which the theme was initially loaded and last updated. This metadata essentially forms a dynamic inventory of the data available to the user. Fig. 3 shows how this metadata is incorporated in the user interface for direct theme selection (the graphic in the upper right corner of the screen is a Florida manatee).

The third and fourth methods of selecting coverages each make more extensive use of the metadata and provide significant support to the user. It would be helpful at this point, for the reader to review Fig. 1 and to locate the SiteType table at the far right. This table also appears in the metadata description in Fig. 2. Recall that the SiteType table contains a list of topics of interest to FMRIS users, in this case specific land characteristics that the system’s developers and users have found to be frequent focal points for decisions. Examples of values in this table include ‘‘Public lands,’’ ‘‘Endangered species habitats,’’ ‘‘Recreation areas,’’ etc.

The third method of selecting themes allows the user to specify one or more topics from the SiteType table. FMRIS then uses the CoverageSiteType table to determine which coverages are to be loaded. Consider the structure of the CoverageSiteType table in Fig. 2. The ‘‘natural’’ primary key of this table consists of the four fields, Coverage\*Number, SiteType, FieldPosition, and Value. The FieldPosition attribute of the CoverageSiteType table specifies the ordinal position of a field in the associated theme’s own attribute list. Together, FieldPosition and Value provide the necessary information to construct an SQL WHERE clause to limit the records returned by a query. Because the last two fields can be null (see below), these four fields become an alternate key with null values allowed and a simple autonumber field (Number) becomes the actual primary key.

![](/api/attachments/2N3MABPP/fulltext/images/3b03b6dddf1ce93467d50f01c4e82cc1635652545bbcdeeee9e2f9797a16e506.jpg)  
Fig. 3. Selecting themes directly.

When the user selects a SiteType for analysis, the relationship agent queries the CoverageSiteType table for all matching records. If the FieldPosition and Value fields are null, the agent knows that the entire theme is to be loaded. If these two fields have values, this indicates that only a subset of the theme’s records (objects) is relevant to the topic. The agent uses the GIS software’s capabilities to create a temporary theme consisting only of records where the theme field specified by FieldPosition matches the value specified by the Value field. In this manner, subsets of a theme, such as the government lands in the zoning theme mentioned above, can be included in an analysis without including the entire theme.

Fig. 4 shows the user interface for selecting themes by site type. It includes an explanation of the Site-Type’s focus from the Description field and the Topics list box uses the Category field in the table to reduce the selection choices. (The FMRIS sponsors decided to use the term ‘‘Data Keys’’ for the concept described as ‘‘SiteTypes’’ in the underlying database. This decision was made well into development and so is reflected in the user interface but not in the data structures.)

The fourth method of selecting a theme is similar to the third but extends the user’s flexibility. The user can select a regulating agency, a permit, or a regulation (see Fig. 1) of interest. The system queries the data to determine which SiteTypes are related to the specified records. From this point, the relationship agent uses the SiteType and CoverageSiteType tables as discussed immediately above. This capability allows an employee of a particular agency, for example, to construct a map showing all of the lands over which the agency exercises jurisdiction in a specified area.

## 4.2. Displaying GIS themes for analysis

As stated, one of the most powerful capabilities of a GIS is the creation of thematic maps of the area of interest to the decision maker. Unfortunately, creating these maps requires specialized knowledge of cartographic principles and GIS techniques that is just not available to the average manager who is not a GIS expert [27]. This subsection details how FMRIS uses software agents and metadata to overcome the user’s knowledge gap.

![](/api/attachments/2N3MABPP/fulltext/images/60878f3054bad475f568349b367801d5101949ddb70e9670a8139cd14d9b28ee.jpg)  
Fig. 4. Selecting themes by topic.

## 4.2.1. The decision making context

Maps have been shown to be very effective in conveying certain decision-related information, and especially for showing relationships between objects [4]. Consider the same decision making context discussed in the previous subsection. It is reasonable to expect that a quick visual examination of a map could show which projects fall within (or are uncomfortably close to) one of the undesirable areas. The user can perform this examination if he or she can construct a map with the appropriate themes displayed. In the example task described below, an agent builds a map from theme selections made by the user.

## 4.2.2. The user’s knowledge problems

The user’s problems come under the presentation KM issue in Table 2. The basic problem in layering themes is to ensure that themes that obscure more of the map surface do not layer on top of more sparsely populated themes. In the example here, if the public lands theme layers on top of a gopher tortoise habitat theme, then a large public land area (such as the Everglades National Park) may obscure specific tortoise habitats. With regard to procedural knowledge needs, the user first needs to realize that layering themes is problematic, and then needs to understand that denser themes (e.g., county boundaries, city streets) should be layered below (added to the map earlier than) less dense themes (e.g., specific species nesting sites). The declarative information problem is to know how dense each theme actually is.

Other presentation KM issues relate to symbolizing the map display. For example, the user’s organization may always display wetlands in blue. It may always display endangered species habitats color coded by species (e.g., manatee ranges in gray, alligator ranges in off-green, etc.). The procedural problem here is to know how to change colors and symbols in a map based on theme attribute values. Each time a new map is rendered, these decisions must be made. This task is both technically demanding and time consuming, especially for maps with a larger number of themes. The declarative knowledge problem here is to know the appropriate colors for a theme, which can be troublesome when a theme can be loaded in multiple contexts. (E.g., a theme containing bridges may be symbolized in one way when the user is interested in whether county, state, or federal agencies maintain the bridge; and in another when the user is interested in the bridge’s load classification.)

## 4.2.3. The metadata remedy

The presentation agent accomplishes the layering of themes, in part, by accessing the Level attribute in the Coverage table. This attribute contains an integer value from 1 to 10 with one representing universal polygons and 10 representing sparse points. A universal polygon theme is one such as county boundaries where the theme covers every square inch of ground. Sparse point themes contain relatively few features (such as power plants). The three types of themes (polygon, line, and point) each have three levels of density (dense, moderately dense, and sparse) in addition to the universal polygon designation. A GIS expert assigns these attributes when the theme is first mounted on the system.

The presentation agent performs an SQL SELECT query on the view using an ORDER BY clause on the Level field. The denser themes, having the lowest values of this attribute, appear first in the list. The agent adds the themes to the map in the order in which the query returns them so that the denser themes end up on the bottom of the map. The procedural knowledge regarding the process for layering themes is embedded in the agent while the declarative knowledge about the characteristics of individual themes is stored as metadata in the GIS database.

Symbolizing maps is considerably more complex and tasks both the presentation agent and the metadata more extensively. We have previously mentioned two types of symbology, applying a consistent color to each object in a theme each time the theme is added to a map, and selectively coloring specific objects in a theme according to some characteristic (attribute value) of the object. This task is split between the user and the software agent with both supported by the metadata.

Consider the structure of the CoverageFields table in Fig. 2. Recall that there is one record in this table for every attribute field in every theme mounted on the system. The primary key of the CoverageFields table is a composite key consisting of the theme’s identifying number and the ordinal position of the field in the attribute list of the theme’s attribute data. The Descriptor field in this table is a Boolean field that indicates that the field can be used to apply a custom color scheme. When users select or confirm themes to be added to a map, the FMRIS interface offers a list of available Descriptor fields for the theme from which the user may choose one or none (the default).

The simplest case might apply to the wetlands theme mentioned above. If there are no Descriptor fields for the coverage, or if the user chooses not to use one of these fields, then the theme-loading agent will apply a uniform color to each object in the wetlands theme by using the Coverage table. This table contains three fields, defRed, defGreen, and defBlue, each of which contains an integer value defining a color using the RGB (red – green – blue) color definition scheme used by the ArcView GIS software (and others). In the wetlands example, these three fields would contain values defining the desired shade of blue. The same agent that loads the themes in the appropriate order also reads these three fields and translates them into the color definition used by the GIS.

The aforementioned bridge theme presents a more complex example. Here, the user might be offered the choice of symbolizing all bridges with the default color (as described above), or by selecting either the

MaintainedBy or the LoadLimit fields, each of which might have been designated as Descriptor fields when the theme was mounted. If, for example, the user chooses the MaintainedBy field to symbolize the map, the theme-loading agent uses the FieldValue table to apply the colors. This table contains one record for each distinct value found in each Descriptor field of each theme, with each record containing the RGB color definition for the value. The presentation agent not only applies these colors to each object in the theme but also constructs the appropriate legend for the map.

As stated, the goal of the theme symbolizing process is to ensure that each theme loads in every map with a consistent color scheme, sometimes with just one color applied to each object and sometimes with specific colors representing specific types of objects within the same theme. The user is required to select or know the appropriate type of classification to use but, once again, the procedural knowledge needed to actually apply the color schemes is embedded in the software agent. Declarative knowledge about the available color schemes for each theme as well as the specific colors to be applied within each scheme is stored as metadata.

## 4.3. Other examples

The two examples above are representative of userand agent-intensive tasks that utilize the FMRIS metadata structure. Table 5 lists additional tasks that use the metadata described in Fig. 1.

Table 5 Additional tasks

<table><tr><td>Task</td><td>KM issues (Table 2)</td><td>Data needs (Fig. 2)</td><td>Description</td></tr><tr><td>Turn theme display on/off</td><td>Presentation</td><td>Coverage: MinRes, MaxRes</td><td>The presentation agent automatically sets minimum and maximum resolutions for theme displays. E.g., street theme will not display when user is viewing the entire state.</td></tr><tr><td>Protect data integrity</td><td>Integrity</td><td>CoverageFields: Type, Length, Required</td><td>Integrity agent validates field values when theme attribute data is added or updated.</td></tr><tr><td>Create tabular reports</td><td>Presentation</td><td>CoverageFields: Displayed</td><td>Presentation agent determines which fields are to be displayed in the tabular reports.</td></tr><tr><td>Label objects</td><td>Presentation</td><td>Coverage: LabelField</td><td>Presentation agent automatically sets field used to label objects when the user specifies that objects in a theme are to display with labels.</td></tr></table>

## 5. Generalizing the results

This paper presented a KM design approach for a specific SDSS that used a metadata structure to support the declarative knowledge needs of both end-users and software agents and used software agents when needed to support the procedural knowledge needs of end-users. As postulated earlier, this experience has implications that go well beyond the specific case at hand. This section presents information on how the lessons from the FMRIS example might be applied to a broader range of systems. In particular, the authors believe that the use of metadata as a knowledge management tool can be beneficially employed in other SDSS, in non-spatial DSS, and in data warehousing environments. Further, we believe that the assistance of software agents for more detail-oriented, complex tasks will become commonplace, and that new generations of agents can also benefit from well designed metadata repositories.

## 5.1. Generalizing to wider varieties of SDSS

The FMRIS metadata tables were developed for the system’s intended purpose and intended users. SDSS designers should find the FMRIS metadata tables generally applicable to their own SDSS because the tables address both general and GIS-specific KM issues. The CoverageFields table, for example, primarily stores metadata that addresses general and GIS-specific integrity issues. One would assume that all SDSS designers would have data integrity concerns. The Coverage and FieldValue metadata tables, storing two levels of presentation information, support the rendering or presentation of spatial data, another common issue for SDSS designers. The Coverage, CoverageSiteType, and SiteType metadata tables store both general and spatial data relationship information and map GIS themes to end-user terminology, another common concern of SDSS designers.

The FMRIS metadata tables also conform to the common delineation between technical and business metadata. This metadata delineation generally classifies information such as data size and source as technical, and information with regard to the intended business use of the data as business [22]. Technical metadata is generally most useful to system and database administrators, and in the case of SDSS, GIS specialists. Business metadata is generally most useful to end-users and decision-makers. Three of the metadata tables, Coverage, CoverageFields, and Field-Value, contained information of a technical nature while the remaining two tables, SiteType and CoverageSiteType contained more business-oriented information.

The agents implemented in the FMRIS would also be generally applicable to most SDSS because the agents address the common KM issues of relationships, integrity, and presentation. The actual agent code would have to be altered to integrate with the specific SDSS implementation, but the general goals and tasks accomplished by the agents would be similar.

A fundamental issue in all SDSS and in the application of the metadata approach described here would be the availability of both domain and GIS experts. Such experts are required during the mounting of themes in SDSS for the development of the technical and business metadata. They are also needed for the construction of the agents to ensure that the procedural knowledge in the agents is correct.

## 5.2. Generalizing to DSS

As early as 1981, Bonczek et al. [1] distinguished between declarative and procedural knowledge in DSS. FMRIS instantiated this concept through the use of metadata for declarative knowledge and software agents for procedural knowledge. While DSS without a spatial component will not contain the rich descriptors of spatial data used by FMRIS, they will still need methods for implementing specific procedural tasks and for managing data and models. It is clear that a KM approach can assist in all of these areas.

## 5.2.1. Model management

The concepts of model management and model bases have been present from the earliest discussions of DSS as a distinct research area [1,20]. In many respects, users face the same problem with respect to selecting and using models that they face with respect to selecting data for analysis. The user must have declarative knowledge about the existence of the model and the data upon which the model must operate, and procedural knowledge about how to organize the data for use with the model, how to initiate the model, and how to interpret the model’s results.

The roles of the SiteType, CoverageSiteType, and Coverage tables (Fig. 2) could easily be adapted to catalog available models. The SiteType table counterpart would hold the list of available models and model descriptions in business terms and the other two tables would map these business models to the formal representation of the model and the data on which the model would act. It is also easy to envision a software agent that would load and organize the model and its data, as the relationship agent does with the spatial data in FMRIS. This agent would contain the procedural knowledge relevant to the use of the model and its data and, as with FMRIS, would draw heavily on declarative knowledge stored as metadata.

The metadata tables and agents that address integrity and presentation KM issues would also be applicable to model management. Model integrity, ensuring that the model has all required data, would have similar declarative and procedural elements and needs.

## 5.2.2. Data management

Generalization of the metadata structure in FMRIS to data management tasks in a non-spatial DSS should also be appropriate. The KM issues of relationships, integrity, and presentation are common concerns in the management of all types of data, not just nonspatial data. The SiteType, CoverageSiteType, and Coverage metadata tables would again assist endusers in mapping business and technical terms. The integrity and presentation metadata tables would similarly support data integrity and presentation issues. Software agents would be used to provide procedural support for these same KM issues.

## 5.3. Generalizing to the data warehouse

Data warehousing is an important new topic in MIS research and practice as companies attempt to leverage stores of historical data for managerial decision making. Given the complexity of the data warehousing environment, it is not surprising that a metadata emphasis has developed in this area of decision support. A similar differentiation between technical and business metadata has been suggested by researchers in this area. Gray and Watson [8], for example, define the technical directory as metadata that describes data organization and sources and the business directory as metadata describing related business and technical terms. While metadata is considered an integral part of the design and implementation of data warehousing [5,8], the design of metadata for effective data warehouse use is still a new area. In particular, Gray and Watson [8, p. 62] report that the development of metadata to support ‘‘end users’ needs is the next direction for development’’.

The end-users of FMRIS and end-users seeking access to warehoused data share many of the same KM problems. The data in a data warehouse can come from multiple departments or companies, and can originate from a number of transaction processing systems. As a result, users may often be at a loss as to the meaning and contents of the various data stored in the warehouse (i.e., the relationship between business and technical descriptions). The multiple sources, uses, and users of the warehoused data make integrity a significant issue. And unlike other DSS environments, the use of OLAP and other decision support tools makes presentation of the data a more significant knowledge management issue.

The KM design approach used in FMRIS, with its business and technical metadata tables, largely includes the suggested contents of the business and technical directories in the data warehousing environment and also provides a metadata structure for storing this declarative knowledge. In addition, the KM approach provides end-user procedural assistance through the use of software agents and a method for identifying and storing relevant procedural knowledge.

## 6. Conclusions and future research

While the Florida Marine Resource Information System is a specific spatial DSS, the KM design approach used in its development has broad applicability to other DSS. FMRIS illustrates several approaches for the management of knowledge when end-users need to access unfamiliar data and use decision support tools that normally require specific procedural expertise. The use of metadata and software agents in this approach serves as an example for the management of both declarative and procedural knowledge in a much wider variety of systems. Several conclusions can be drawn from the FMRIS example.

First, end-user needs should be a key factor in the construction of metadata, especially in the development of business metadata. A relatively simple metadata structure containing accurate and informative data can play a key role in supporting end-user access to data.

Second, as procedural knowledge is embedded in software agents, these agents can be designed to work with metadata to perform their tasks. By using metadata to store declarative knowledge, the software agents can be less complex in that they need not have this knowledge persist within the agent itself.

Third, the brief extensions of the FMRIS examples to other types of systems have shown that the metadata structure presented here is robust enough to manage a much wider range of applications where end-user or agent access to data is required. Certain tables should be renamed to either reflect the new problem domain or to be domain-neutral. Certain attributes of the metadata tables that are unique to the management of spatial data may not be needed in other applications, while new domain-specific attributes may be called for. It is felt, however, that the KM issues of relationships (especially the mapping between business and technical concepts), integrity, and presentation are guaranteed a counterpart in any decision support system.

This paper also suggests areas for future research. First, the allocation of knowledge support between metadata and software agents should prove to be a useful model for future systems. In these cases, it will be important to know how the presence and design of metadata affects the design and functionality of software agents. If the declarative knowledge resides within the agent itself, it is private unless the agent has been designed to communicate the knowledge in some fashion. As agents are endowed with learning abilities and/or accept knowledge from other agents, it may be more practical to design the agent to store newly acquired knowledge in the metadata repositories. In other words, the agent functionality remains focused on procedural knowledge but the procedures are now extended to the update of metadata. This approach may simplify the design of agents while making declarative knowledge more widely available.

Second, the concept of mobile agents is gaining increasing currency in the literature at the same time that data warehousing vendors are agreeing on standards for the formatting and interchange of warehoused data [8]. Research in this area should determine if metadata standards can improve the effectiveness of these agents while increasing the exposure and availability of warehoused data.

Third, human experts create most of the FMRIS metadata, a considerable limitation for mounting new themes [26]. While there is some agent support for creating records in the CoverageFields table, the rest of the process remains labor intensive. New research should explore the feasibility of expanding support for mounting new data in both SDSS and in other data stores, including data warehouses.

Finally, empirical testing of the KM design approach presented should be pursued. In this paper, a design approach was presented as was an information system that was constructed using this approach. While the fielded system met with widespread approval, funding limitations precluded formal adoption and therefore formal post-implementation validation. The next step in furthering the credibility of this KM design approach is to develop specific hypotheses regarding the artifacts of the design process and product and empirically test these hypotheses on FMRIS or systems built with the same approach [25]. Hypotheses testing could involve comparing the KM design approach to other approaches by comparing the end-user support provided by systems constructed with the competing design approaches. Evaluation could take place using prototypes or full implementation of specific subsystems.

If there is any concept that epitomizes computing in the 1990s and beyond, it is the increasing emphasis on end-users in the design and intended use of information systems. If there is any concept that epitomizes the trouble with extending computing capabilities to end-users, it is the problem of giving them the requisite knowledge to operate the systems effectively. Between the conflicting approaches of embedding all necessary knowledge in the user through training, and embedding all necessary knowledge in the system through task-specific programming, lies the idea of creating flexible systems where the user retains control over what to do while the system provides support for how to do it and what data to do it with. FMRIS illustrates an example of this middle approach, one whose lessons have the potential for reverberating well beyond its target domain.

## References

[1] R.H. Bonczek, C.W. Holsapple, A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[2] J.M. Bradshaw, An introduction to software agents, in: J. Bradshaw (Ed.), Software Agents, AAAI Press/MIT Press, Menlo Park, CA, 1997, pp. 3– 46.

[3] K.C. Clarke, Getting Started with Geographic Information Systems, Prentice Hall, Upper Saddle River, NJ, 1997.

[4] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 (1) (1995) 219 – 235.

[5] H. Edelstein, An introduction to data warehousing, in: R. Edelstein, H. Edelstein (Eds.), Planning and Designing the Data Warehouse, Prentice Hall, Upper Saddle River, NJ, 1997, pp. 31–50.

[6] D. Gilbert, Intelligent agents: The right information at the right time. IBM Intelligent Agent White Paper (June 16, 1997), IBM (http://www.networking.ibm.com/iag/iagwp1.html).

[7] G. Gorry, M. Scott Morton, A framework for management information systems, Sloan Management Review 13 (1) (1971) 55–70 (Fall).

[8] P. Gray, H.J. Watson, Decision Support in the Data Warehouse, Prentice Hall, Upper Saddle River, NJ, 1998.

[9] C. Harder, GIS Means Business, Environmental Systems Research Institute, Redlands, CA, 1997.

[10] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create the next generation of decision support systems, Decision Sciences 31 (1) (2000) 1 – 31 (Winter).

[11] G.M. Kasper, A theory of decision support system design for user calibration, Information Systems Research 7 (2) (1996) 215 – 232.

[12] P. Keenan, Using a GIS as a DSS generator, in: J. Darzentas, S. Spyrou, T. Spyrou (Eds.), Perspectives on DSS, University of the Aegean, Greece, 1996, pp. 33 – 40.

[13] P. Keenan, Spatial decision support systems for vehicle routing, Decision Support Systems 22 (1) (1998) 65 – 71.

[14] P. Maes, Agents that reduce work and information overload, Communications of the ACM 37 (7) (1994) 31 – 40.

[15] B. Mennecke, G. Higgens, Spatial data in the data warehouse: a nomenclature for its design and use, Proceedings of the 1999 America’s Conference on Information Systems. Association for Information Systems, Atlanta, GA, 1999.

[16] Microsoft Corporation, Microsoft MapPoint 2000 Delivers New Mapping and Analysis Program (November 3, 1998), http://www.microsoft.com/mappoint.

[17] D. Robey, S. Sahay, Transforming work through information technology, a comparative case study of geographic information systems in county government, Information Systems Research 7 (1) (1996) 93 – 110 (May).

[18] J.B. Smelcer, E. Carmel, The effectiveness of difference representations for managerial problem solving: comparing tables and maps, Decision Sciences 28 (2) (1997) 391 – 420.

[19] R. Sprague, E. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[20] R. Sprague, H.J. Watson, MIS concepts—Part II, Journal of Systems Management 26 (1) (1975) 35 – 40.

[21] R. Sprague, H.J. Watson, Decision Support Systems: Putting Theory into Practice, Prentice-Hall, Englewood Cliffs, NJ, 1986.

[22] C. Stedman, Metadata, Computerworld 33 (44) (1999) 74.

[23] T. Tonklin, Business geographics impacts corporate America, Business Geographics 2 (2) (1994) 27 – 28.

[24] E. Turban, Decision Support and Expert Systems: Management Support Systems, Prentice Hall, Englewood Cliffs, NJ, 1995.

[25] J.G. Walls, G.R. Widmeyer, O.A. El Sawy, Building an information system design theory for vigilant EIS, Information Systems Research 3 (1) (1992) 36– 58.

[26] L. West, Florida’s marine resource information system: a geographic decision support system, Government Information Quarterly 16 (1) (1999) 47 – 62.

[27] L. West, Designing end-user geographic information systems, Journal of End User Computing 12 (3) (2000) 14 – 22 (July – September).

[28] L. West, B. Mennecke, Relational data modeling for geographic information systems, Journal of Database Management 10 (2) (1999) 27 – 34 (Apr – Jun).

[29] R. Wilson, GIS and decision support systems, Journal of Systems Management 45 (11) (1994) 36 – 40 (Nov).

![](/api/attachments/2N3MABPP/fulltext/images/88ff8480edb79e79ffbffb9725886bff934a305efe00685c9b372508dd420916.jpg)

Dr. Larry West is on the faculty of the Department of MIS at the University of Central Florida. He earned his Ph.D. in MIS from Texas A&M University in 1991 and has been with UCF since 1996. Dr. West has published six other journal articles on geographic information systems as a decision support technology as well as several conference papers on the subject. He has also published papers on information economics and the economics of elec-

tronic commerce in journals such as Decision Sciences, JMIS, and the International Journal of Electronic Commerce. His teaching interests include database design and management, electronic commerce, and decision support systems.

![](/api/attachments/2N3MABPP/fulltext/images/472dfcf44b52771c3b44353909fb9533b52313b3fe9d45592ed6241b69a31248.jpg)

Traci J. Hess is an assistant professor of Operations and Information Technology in the School of Business Administration at the College of William & Mary. Her research interests include the design and acceptance of decision support systems and software agents. She has published her research in such journals as Decision Sciences and Decision Support Systems. She received a Ph.D. in Management Science and Information Technology and a M.A. in Accounting

Information Systems from Virginia Tech and a B.S. from the University of Virginia.
