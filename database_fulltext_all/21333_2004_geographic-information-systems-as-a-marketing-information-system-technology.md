---
otero_id: 21333
otero_key: "DGBQKGKJ"
title: "Geographic information systems as a marketing information system technology"
authors: "Ronald L. Hess; Ronald S. Rubin; Lawrence A. West"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00102-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 38 (2004) 197 – 212

www.elsevier.com/locate/dsw

# Geographic information systems as a marketing information system technology

Ronald L. Hess<sup>a</sup>, Ronald S. Rubin<sup>b,</sup>\*, Lawrence A. West Jr.<sup>c</sup>

<sup>a</sup> Department of Marketing, School of Business Administration, College of William and Mary, P.O. Box 8795, Williamsburg, VA 23187-8795, USA

<sup>b</sup> College of Business Administration, Department of Marketing, University of Central Florida, 4000 Central Florida Boulevard, Orlando, FL 32816-1400, USA

<sup>c</sup> College of Business Administration, MIS Department, University of Central Florida, 4000 Central Florida Boulevard, Orlando, FL 32816-1400, USA

Received 30 April 2002; accepted 31 December 2002 Available online 5 August 2003

## Abstract

Marketing information systems (MKIS) are decision support systems targeted at marketing-specific decisions. One of the most widely disseminated MKIS models divides the marketing decision universe into four domains and links these domains to each other and to other marketing activities. Unfortunately, there is little guidance on the construction of specific MKIS targeted at problems in these domains or to the construction of integrated MKIS that span domains. This paper advocates the use of geographic information systems (GIS) as a DSS generator for constructing MKIS. The paper reviews the technical capabilities of GIS and shows how these capabilities align with accepted elements of MKIS. We see that a unique advantage of GIS over other MKIS technologies is its ability to integrate information from disparate sources and spanning multiple decision domains when a single decision requires this capability. The paper then uses a decision making resource-based approach and the four elements of the marketing mix to propose a research agenda for increasing our understanding of GIS as an MKIS technology. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Decision support systems; Geographic information systems; Marketing information systems; Multiple decision domains

## 1. Introduction

The concept of marketing information systems (MKIS)<sup>1</sup> originated in the 1960s as a technique for applying new (at the time) data processing technologies to marketing-specific decisions. In many ways, the history of MKIS has paralleled that of MIS with new technologies and new conceptual approaches extending the support provided to decision makers. Unfortunately, though, specific techniques for constructing MKIS have not delivered on the potential inherent in the MKIS idea [32,33]. One indicator of this phenomenon has been a decline in the coverage of MKIS in the Marketing literature in the 1990s, though interest in the concept has become more pronounced in mainstream MIS journals such as this one.

This paper asserts that a new use for an increasingly popular information system technology can fundamentally alter the cost and effectiveness of marketing decision making. The technology, Geographic Information Systems (GIS), uses stored data to create customized computer-based maps showing location and attribute information about objects of interest to a decision maker. In particular, GIS is a specific software technology that Sprague and Carlson [31] call a decision support system generator, a tool used to create decision support systems (DSS) for use with specific decision making needs. DSS have been shown to be important tools for supporting marketing operations [4,8,15,24,26] and a DSS generator with capabilities directly relevant to marketing decision making is especially valuable.

GIS provide value for marketing decision making through two mechanisms:

1. GIS provide a way to analyze internal or external marketing intelligence data in a format particularly suited to marketing decision making; and

2. GIS provide the ability to integrate both internal and external marketing intelligence data to greatly improve the effectiveness of these marketing decisions.

This paper will show how these capabilities result in a competitive advantage through the ability to leverage internal data and specific knowledge of market factors through the easy application of effective visualization techniques and the integration of external data. To the extent that the firm can internalize and institutionalize these capabilities, the firm’s competitive advantage may become both sustainable and strategic. Further, the paper will show that these capabilities have important implications not only for marketing practice but also for research.

We begin the paper by reviewing marketing information systems and introducing a framework that organizes the rest of the paper. Next, we provide some background on GIS and highlight some of the most relevant technical capabilities. This discussion highlights the specific data visualization and integrating capabilities and stresses their use in marketing decision making. Next, we use the MKIS framework to examine the usefulness of GIS with respect to specific elements of an MKIS. We then revisit the same GIS capabilities in terms of the ‘Four Ps’ of marketing, product, pricing, placement (location), and promotion and see that these capabilities are relevant from this perspective as well. Finally, we will examine how the capabilities of modern GIS can affect both theory and practice in marketing and outline some issues for future research.

## 2. Marketing information systems

Kotler defined a marketing information system as,

. . .a structure consisting of people, equipment, and procedures to gather, sort, analyze, evaluate, and distribute needed, timely, and accurate information to marketing decision makers. [17, p.110]

We admire the comprehensiveness of this definition and find that some other definitions are either more restrictive in purpose or less comprehensive in scope, resulting in less flexibility in a system’s goals and capabilities. Furthermore, Kotler’s definition is independent of any specific computer technology. He also suggests that the potential components of an MKIS can be included or not, added, or enhanced to suit the decision maker’s needs. Finally, Kotler’s definition provides for two types of systems familiar to MIS practitioners, specific DSS and ad hoc DSS. A specific DSS is a semi-permanent system that provides recurring decision making support to its users (in line with Sudman and Blair’s [34, p.30] definition of a MKIS), while an ad hoc DSS is developed for limited, sometimes one-time, use on a specific problem.

Wierenga and van Bruggen [36] provide a richer taxonomy of what they call Marketing Management Support Systems (MMSS). Their taxonomy includes MKIS as a specific subtype of MMSS along with seven others including Marketing Expert Systems, Marketing Neural Nets, etc. In our review of the literature, however, we have found that ‘‘MKIS’’ is the dominant term applied to marketing-oriented information or decision support systems. We will therefore continue use of the term here for a broad class of systems (specific and ad hoc DSS) and system development tools (DSS generators) having in common an orientation toward marketing decisions.

Of interest to us is evidence that MKIS do not occupy as prominent a place in the marketing decision maker’s arsenal as they might. In a 20-year longitudinal study Li, McLeod, and Rogers found that 8% fewer firms reported having MKIS in 2000 as in 1990, though they do report that computing use by marketing decision makers overall is up [21]. They further report that, ‘‘Three of the computer applications that typically are associated with sophisticated computer use (graphics display, decision modeling and simulation, and what-if analyses) are pursued less frequently’’ [21, p.312].

In a separate study of small companies, Li et al. [22] found that the small firms are not using MKIS at nearly the rate of the larger firms in the Li et al. study. One conclusion is that the smaller firms cannot afford the infrastructure needed for effective MKIS. Of the firms that did have specific MKIS, 41% included custom programmed systems, presumably specific DSS which can be expensive to create and maintain. Jiang et al. [14], found that there was a mismatch in the views of marketing executives and information systems managers with respect to the importance of key system features. Krishnan et al. [16] found that cost of ownership was the primary driver of overall system satisfaction for marketing systems delivered via corporate intranets.

Taken together, these studies indicate the unsurprising conclusion that MKIS must provide cost effective support for marketing decision makers and that when they do not, satisfaction with the systems will be lessened or the systems will not be built at all. A corollary conclusion is that a diminished or declining penetration of MKIS indicates either a lack of effectiveness, high costs, or both for traditional MKIS development approaches.

This paper explores the components of marketing decision making in considerably more detail than the previous studies and derives the system characteristics to successfully support marketing decisions. The new finding here is that GIS do possess these characteristics and can be provided at relatively low cost. In particular, one of the most expensive components of an effective MKIS, converting and integrating data from disparate data sources, can be accomplished as an end user task using relatively inexpensive GIS desktop packages.

Finally, our literature review revealed the surprising finding that much of the recent (1990s) work on MKIS has appeared in the MIS journals rather than in the mainstream marketing literature. Journals covering MKIS include Decision Support Systems [16,20,28], Information and Management [22,33], International Journal of Information Management [14], and Information Resources Management Journal [21]. The same is also true for the application of geographic information systems as DSS tools, though the practitioner marketing literature is replete with case studies of GIS support for marketing activities.

Both Kotler [17] and Burns and Bush [5] present nearly identical models of marketing information systems that shows relationships between managerial tasks, uses of the MKIS, MKIS information development, and decisions in the marketing environment (reproduced here as Fig. 1 and referenced hereafter as the ‘K/BB model’). The model shows that an MKIS has several distinct components and that these components have a number of interrelationships. A manager performing one of the tasks in the leftmost box pertaining to one (or more) of the decisions in the marketing environment must identify information needs and obtain the needed information. This information and analysis support can come from the four components in the Developing Information box, internal reports, marketing intelligence, marketing research, and marketing decision support analysis. Kotler’s definition of an MKIS (cited earlier) covers the infrastructure and procedures available to implement the K/BB model.

This paper uses this conceptual model as an organizing framework to show how GIS technology can be used in MKIS, as defined by Kotler et al. We will show that the analysis support offered by GIS improves the usefulness of each of the four components in the Developing Information section of the model, while the integration capabilities support the interrelationships between these model elements. Further, our analysis will use examples that relate these improvements to better decisions about the marketing environment. The next section lays a foundation for this analysis by presenting a brief introduction to GIS capabilities. We then refer to these capabilities as we show how GIS applies to the elements of the K/BB model.

![](/api/attachments/DGBQKGKJ/fulltext/images/615a0e433ba49c90fc03543b2c1b166c83b87144c93b29a5c7fc1e12f44ae4c4.jpg)  
Fig. 1. The Kotler [17]/Burns and Bush [5] Model for marketing information systems.

## 3. GIS capabilities

This section presents key information on the technological capabilities of GIS software and later sections of the paper build from this foundation to illustrate specific advantages GIS software provides to marketing decision makers.. The discussion here does not emphasize the syntax or interface of any particular GIS software product, but instead presents capabilities that are implemented in most GIS packages. We begin by discussing traditional maps as decision support tools and then see how computerbased maps have significant advantages over paper maps.

## 3.1. Maps as decision aids

Ordinary paper maps are graphic representations of the real world that all of us have used. City street maps, for example, depict natural objects, such as rivers and lakes; man-made objects such as roads and buildings; and abstract objects such as city or county boundaries. These objects, whether natural, manmade, or abstract, are called map features. Each feature on a map has a location, a representative shape, and a symbol that represents one or more of its characteristics. For example, a blue line may represent a river. Green areas may represent parks. A black square may represent a building and may have a label saying ‘‘Library’’. Dark red lines may mark highways, with smaller roads marked by thin black lines. The meanings of a map’s symbols are often depicted in the map’s legend.

Features on maps are displayed according to their locations relative to each other and to an underlying grid representing the earth’s surface. We learn, sometimes with differing degrees of success, to understand how the depictions of these features on a map match their instantiations on the ground. Understanding these relationships on a street map helps to solve problems of navigation, facility location, or real estate purchase. Specialized maps, such as topographic, soil type, population density, watershed, etc., are used to support specialized decision making tasks.

Most features depicted on a map have attribute information, descriptive data about each feature. The attributes of a shopping mall, for example, might include the name, type, size, names of anchor stores, a list of tenants, and the number of parking spaces available. Paper maps, however, can only display a limited amount of attribute information using the map symbols. For example, the width and color of the symbol used to depict a road can discriminate between roads, highways, freeways, and interstate highways. Buildings may be depicted with flags to represent schools, crosses to indicate churches, or with irregular shapes to indicate the size and shape of large buildings.

## 3.2. GIS maps and attribute information

Unlike paper maps, GIS are capable of storing, manipulating, and displaying a much richer set of attribute information. GIS are specialized database management systems that link sets of features and their attributes and store them together in units called themes<sup>2</sup> [10]. One theme contains a set of similar features, such as all of the roads in the area of interest. A different theme might contain all of the shopping centers, along with the attributes for those features. A city map, for example, may contain many themes including interstate highways, surface streets, political boundaries, public buildings, schools, parks, etc.

Further, GIS can create maps ‘on the fly’ based on the features and attributes of interest to the decision maker. For example, if the current decision requires customer locations, demographic data by census block, and store locations, then other themes such as airports, can be omitted from the map. A GIS can also use attribute information to affect the display of the map. Symbols for stores can be colored according to the store’s sales volume and sized according to square feet on the sales floor. In one application, residential neighborhoods can be color coded by a median income attribute while in another they can be colored based on median age. Neighborhoods can even be symbolized with miniature individual pie-charts showing ethnic, age, or income distributions.

Each theme has its own set of attributes that make sense for the features represented in the theme, and each theme stores the physical location, size, and shape of each map feature. Fig. 2 shows three sample GIS themes. On the left of each theme is a representation of the attribute data that can include most types of fields normally found in a relational database management system (RDBMS) including numeric, text, date, Boolean, etc. On the right is a depiction of the location occupied by each object, record, or occurrence. These locations can be polygons (Fig. 2A), such as city, county, or sales territory boundaries; point features (Fig. 2B), such as customer street addresses, building locations, or vending machine locations; or linear features (Fig. 2C), such as roads, rivers, or railroads.

![](/api/attachments/DGBQKGKJ/fulltext/images/2019b68cd1640d2abf6f6d6a02025c668606903db5ed7c8d59d34374db8453f1.jpg)  
Fig. 2. Multiple GIS themes.

## 3.3. Displaying spatial locations using GIS

All the themes for a geographic area taken together make up a GIS database and one of the most obvious capabilities of GIS software is the ability to visually display the locations of geographic objects on the computer’s monitor and to print these displays. A collection of themes viewed together forms a map and each theme is a layer in this map [10]. Further, the computer is capable of displaying multiple layers simultaneously with the locations of features in the various layers being precisely displayed relative to each other based on their locations.

Consider the three themes depicted in Fig. 2. If theme 2A depicts sales territory boundaries and theme 2B represents retail outlets then the GIS can display the themes superimposed (Fig. 3). It instantly becomes apparent which locations belong to each territory, even if there is no common field in the attribute data. The ability to display computer system data graphically has been shown to be an important decision making aid in any information system [1 – 3,7,12,19,23,37] and GIS are particularly well suited to this purpose when the data of interest has a geographic component [6,29].

![](/api/attachments/DGBQKGKJ/fulltext/images/33f6c3ec327e7e944620eaff03482d634c3937d0ea1176386f0321463ef593bd.jpg)  
Fig. 3. Intersecting GIS themes.

## 3.4. Determining spatial proximity

A second powerful capability of GIS software is the ability to compare the locations of two objects (in the same or different themes) and determine if:

 the two objects intersect in any way (e.g., a sales territory contains any part of a city boundary or vice-versa),

 one object completely contains or is completely contained by the other (e.g., a prospective customer address falls within a particular sales territory), or

 one object is within a specified distance of the other (e.g., find all customer addresses within 10 miles of a prospective franchise office location).

Further, GIS can find the closest object in a theme to another specified location. For example, if a customer address location is specified, the system can easily find the closest ATM machine, service center, or branch office.

Finally, GIS are able to perform powerful database operations such as aggregations and joins (as illustrated in Fig. 3) based on spatial proximity. Note that Sales Territory E in Fig. 3 is selected (shaded) on the map along with Territory E’s attribute record and the attribute records of retail outlets 3, 4, and 5. GIS can easily aggregate values from the retail outlet attribute data (such as monthly sales values) based on the sales territory in which the outlets fall. The GIS can also build virtual records (joins) of sales territory values (e.g., advertising expenditures) and retail outlet values. This data integrating capability will be discussed at greater length later in the paper.

## 3.5. Geocoding

Recall that GIS data consists of both spatial locations (expressed in some coordinate system) and attribute data. Unfortunately, specifying the geographic coordinates of objects of interest (customers, sales territories, delivery routes, etc.) can be both time consuming and expensive. Fortunately, most professional GIS software provides automated support for assigning coordinates to a special but very common type of attribute information. Geocoding is the process that converts a regular street address to a latitude– longitude (x, y) coordinate used by the GIS. Once a latitude–longitude coordinate has been assigned, the address is then georeferenced and can be displayed on a map or used in a spatial search [10].

Consider the situation illustrated in Fig. 4. The address ‘‘472 Elm Street’’ might come from a table of customer records. The GIS software is able to take the information from the address field and a special matchable address layer to find the street segment that contains the address. Through the application of some simple trigonometry, an x, y map coordinate for the address is calculated. These coordinates are saved with the database table which then becomes a point theme such as the one illustrated in Fig. 2B. Modern GIS software can geocode records one-at-a-time in an interactive mode or process thousands of records per hour in batch mode.

![](/api/attachments/DGBQKGKJ/fulltext/images/f167cfb60b7511e750964c8c625236a17e53365dc348a3e3e091769a5db632bc.jpg)  
Fig. 4. Address matching.

The importance of geocoding cannot be overstated. Since the vast majority of business data contain address information geocoding makes this information amenable to spatial analysis at very low cost. We will shortly see what kind of analysis is available.

This section has presented some of the basic capabilities of GIS software. While interesting in their own right, these capabilities are especially important as determinants of the business use and value of GIS. The next section integrates these capabilities with the four elements of marketing information systems presented in Fig. 1.

## 4. GIS as an MKIS component

The discussion of GIS as a tool for building MKIS is developed in two sections. First, we examine how GIS are utilized with each of the four elements of the Developing Information segment of the K/BB model, Internal Reports, Marketing Intelligence, Marketing Decision Support Analysis, and Marketing Research. Then, we address how GIS can integrate these four components to further understand customer behavior. Integrating different marketing information sources has been a major limitation of alternative analysis techniques.

## 4.1. GIS and internal reports

All selling organizations are challenged by the problem of directing marketing efforts to the audience that has the highest potential to respond to those efforts and make purchases. One of the most widely used capabilities of GIS in marketing is the ability to perform market analysis to identify the best customers, their places of residence, and concentrations of potential customers with similar characteristics. Internal data can help with this task.

The internal reports system gathers information generated by a company’s internal transaction processing systems. An important element of a company’s internal reports system is customer transaction data captured at the point of sale. Unlike survey research, this data represents what people actually do, not what they say. And if the transaction includes information on customer locations (e.g., asking customers for zip codes or recording addresses of frequent buyer members, private credit account users, etc.) then customer locations can easily be plotted on a map. If complete residential addresses are available then exact customer locations can be plotted using the techniques illustrated in Fig. 4 yielding a map such as the one in Fig. 2B. If zip codes are captured then a map such as the one in Fig. 2A can be generated with each zip code region color coded by the number of customers or sales volume it generates.

Using mapped customer data it is then possible to pursue two important aspects of a marketing campaign. First, a site’s trade area can be analyzed by representing its customer draw with concentric rings that surround the site. GIS software is available that will create distance – decay curves, identifying the percentage of customers at different radii around the store [18]. Second, mapped customer data can be used to locate clusters of customers to be targeted with direct mail campaigns, neighborhood newspapers, or billboards [27].

Mapping trade areas is also an excellent means for identifying problems and opportunities in a store network. Once again internal data of customer address or ZIP code data can be used to define the trade areas of individual stores. Where trade areas overlap, the problem of cannibalization can occur when stores within the same trade area are competing for the same customers. On the other hand, those areas not within the trade area of a store may present prospects for new stores. This information is vital for deciding if relocations or new stores are warranted in existing markets [25].

## 4.2. GIS and marketing intelligence

Marketing intelligence is defined as information collected for the purpose of understanding a company’s external environment [5]. These types of systems contain information on competitors (e.g., strategies, activities, characteristics of new products, etc.), economic indicators, government regulation, customer demographic information, and supplier activities, among others. New Image, a consulting firm that specializes in marketing intelligence information, collects as many as 200 statistics on over 70,000 sites across the nation. The company maintains and updates the information in these systems each year for many different industries such as convenience stores, gas stations, and restaurants [11]. New Image frequently links this marketing intelligence information to a GIS to provide its customers with a geographic visualization of requested intelligence information. The company can use GIS to provide a detailed map to a gasoline company that needs to understand the relative locations of competitive gasoline stations for current or prospective sites. In addition, the marketing intelligence system can also provide a company with characteristics of these competitive locations. Information on the prices of gasoline, number of gasoline islands, monthly volume, type of operation, hours of operation, product selection, and others are easily available. The company can then use this information to identify under-served markets that are prime areas for site expansion.

## 4.3. GIS and marketing research

Marketing research studies are for specific problems and are referred to as ‘‘ad hoc’’ studies conducted on an ‘‘as needed’’ basis [5]. Before the arrival of computers and GIS, retailers depended on traditional research methods, phone, mail, and in-store surveys. GIS provides ways to both reduce the data collection costs and to improve the interpretation of traditional data.

Ace Hardware, a national dealer-owned hardware cooperative, uses GIS to help its retailers make sense of survey data collected in their stores to focus advertising dollars more effectively [10]. The company headquarters provides stores with a team of research specialists who help design and conduct the research and then use the ESRI ArcView GIS software package to tabulate, analyze, and map the data.

In one example, the team collected data from shoppers in a Phoenix, Arizona, store using traditional in-store surveys over a 2-week period. Customers were asked about the shopping they had just done, their impression of the store, and their home addresses. The analysts geocoded the customer data and found that 85% of the customer data came from three zip codes, even though the company had previously been advertising in a dozen zip codes. In this case the GIS software enhanced the value of the traditional data by allowing the store to draw inferences that would not otherwise have been available.

In the same project, the analysts created a map of median household income using census block group data from a vendor. This map showed a cluster of high-income block groups located several miles south of the store but the survey reveled that the store pulled very few customers from this area. The store management decided to make plans for a special promotion to this area using the advertising dollars saved from scaling back the direct mail coverage from the larger assumed trade area. In this case, the store was able to ‘‘survey’’ customers it did not even have by gathering information from the GIS-based demographic data.

## 4.4. GIS and marketing decision support analysis

Unlike the other three elements of Developing Information in Fig. 1, the Marketing Decision Support Analysis (also called Marketing Decision Support System—MKDSS) component does not create new information, per se. Instead, it consists of information that has been reorganized for easy decision-oriented retrieval and a collection of decision analysis tools that can act on this information. These capabilities are consistent with two themes in MIS research, decision support systems (DSS) and data warehousing (DW), each of which has a GIS capability.

## 4.4.1. Decision support systems

In the early 1980s, Sprague [30] synthesized research in DSS and found that these systems integrate data and models to help solve unstructured problems. Models consisted of tools that took data as inputs, performed processing on the data, and created specific outputs of use to the decision maker. Models, for example, can be familiar analytical techniques such as break-even analysis, ROI analysis, regressions, forecasts, etc. In all cases, the analytical procedures are embedded in software and the data on which the analysis acts is provided through anything from manual input to automatic retrieval. These systems can be ad hoc DSS using spreadsheets or other end-useroriented tools or formal systems costing hundreds of thousands of dollars.

Modern GIS are very suitable for use as a DSS development tool (DSS generator) and therefore for the development of MKDSS. First, most GIS include the ability to program models using either intrinsic programming or scripting languages or by incorporating programs written in development languages such as C++ or Java. More importantly, some modern GIS include pre-built analytical models that take unique advantage of the spatial data on which they act.

Recall the street maps mentioned in our earlier discussion of geocoding. A street map theme for a city (similar to the linear feature theme depicted in Fig. 2C) forms a network of streets that is susceptible to analysis using such management science techniques as minimal spanning tree, shortest route, maximal flow, etc. Further, products such as ESRI’s ArcView Network Analyst can act on these street maps to perform this analysis without sophisticated programming. This and similar products can then:

 Support distribution operations by solving shortest route calculations from a service center to one or many customer locations using a shortest route algorithm. Different customer locations can be specified each day and maps can be updated with transient problems such as construction sites or even traffic accidents.

 Support service area analysis by calculating drive times along the existing street network. By combining these results with demographic data the MKGIS can determine the desirability of a potential retail location.

 Support customer relationship management by providing web sites to find the closest facility to a customer location or by providing driving directions from a customer location to the business location.

## 4.4.2. Data warehousing and GIS

Data warehousing is the process of combining internal and external data and reformatting the data to make it easily accessible to decision makers. Data in the DW is not linked to the organization’s production databases and users generally cannot make changes to the data (though they can often copy it to their personal computers and manipulate it there). Reformatting may include storing summarized data (e.g., sales by product by month or sales by region by month) in addition to raw data. Data may also be stored in a format that makes sense to the expected users rather than in the fragmented formats that support operational efficiency in a transaction-oriented database.

GIS fill three roles in the operation of DW, and therefore in the performance of Marketing Decision Support Analysis.

 When spatial data are stored in the DW, tools such as Oracle 8i’s Spatial can be used to retrieve, analyze, and display data from large data stores. Analysis of the sort described earlier in this paper can be performed on the warehoused data by end users or trained professionals.

 An important transformation often performed on data with a spatial component is the geocoding of street addresses described earlier in this paper. Since a company’s normal transaction processing activities (adding customers, recording sales, etc.) usually do not need spatial references, performing the geocoding is usually not done. The marketing analysis we refer to in this paper, though, can make use of these values. Because of this, there are many products designed to perform batch geocoding as part of the transformation between ‘production’ and warehoused data.

 Since DW typically include both internal and external data, the ability to analyze both kinds of data in support of the same decision can be an important part of the DW capabilities. GIS are particularly suited for this activity when both types of data have spatial components. This capability is so important that the entire next section of the paper is devoted to it.

## 5. GIS as an MKIS integration tool

One of the most challenging tasks facing developers in the MIS world is the need to integrate data from disparate databases, producers, and systems. The same challenges face MKIS users when they wish to analyze data created from internal data sources and reporting systems, marketing intelligence systems created by second party providers, marketing decision support systems using data warehousing technologies, and data gathered through marketing research efforts.

(Recall the interconnectivity between these market elements in Fig. 1). This section covers one of the most important capabilities of GIS, the ability to integrate diverse data based on spatial proximity and how this capability provides important value to MKIS.

There is a major difficulty inherent in working with diverse data sources. When companies develop their internal data processing systems, including the transaction processing systems most likely to give rise to the internal reports discussed earlier, they have control over the data to be collected and how this data is related and integrated.<sup>3</sup> They have no such control, however, over data prepared by external parties. When companies obtain demographic, trade area, econometric, and other data from private vendors, government agencies, or trade associations this data lacks the common fields needed to integrate it with the company’s internal data or data from other external sources.

GIS technology relieves these constraints considerably. Assume, for example, that marketing intelligence data from a firm such as Claritis is available that reports statistical summary data (mean and distribution) on household income, age, etc., by census block. Further assume that the company’s internal data contains its customers’ addresses and purchase histories. Using the geocoding technology described in conjunction with Fig. 4, the company can easily convert this customer information into a GIS point theme such as the one depicted in Fig. 2. Then, by combining the customer data with the demographic data as depicted in Fig. 3, the company is able to link customers to demographic information. While this technique does not tell how much money a specific customer makes, it is easy to determine the median income, etc., of the area in which the customer lives. If the firm’s internal data includes purchase history then some powerful correlations can be made between consumer behavior and consumer demographics, all with relatively low-cost investments in GIS technology.

This brief conceptual example includes several of the integrating elements in Fig. 1. First, the described analysis integrates both internal reports and market intelligence data. Also, if decision support technologies are involved for trade area analysis, statistical modeling, or even just the graphical display of maps then the model illustrates a three-way integration of components of the K/BB model.

Integration is also illustrated in a real case from the Meineke Discount Muffler Corporation, a national franchise of automobile service shops. Meineke integrates several data sources to perform marketing tasks including site selection, market share analysis, and inventory management. Meineke uses an interesting combination of demographic information on people and ‘demographic’ information on automobiles to support these activities [9]. The data includes internal data on individual franchise sales history and corporate-wide sales performance, but also externally acquired data on demographics, average commute times, market area incomes, etc.

For site selection, the Meineke corporate GIS operators have developed templates that allow them to specify an actual or proposed store location and automatically extract the relevant data from internal and external sources and convert it into an easy-tounderstand report. The analysis integrates commercial demographic data, internal data from historical sales records, and site selection models embedded in the MKIS.

Meineke performs inventory management analysis using GIS and internal and external data. The company integrates market intelligence data on the makes, models, and ages automobiles registered in a store’s service area, along with information on commute times, population densities, etc., to help determine inventory levels. The company has found, for example, that Suburus are very popular in Massachusetts while other vehicles are more highly represented in other parts of the country.

In another example, American Honda Motor Company, also uses GIS to integrate multiple data sources to support marketing decision making. Honda hired an external system development firm to create a custom geographic MKIS based on a popular desktop GIS package. The system uses sales forecasts based on industry growth, demographic changes and other factors, motorcycle industry sales data from the Motorcycle Industry Council, competitive dealer data captured by field managers, and demographic and economic data from two commercial GIS database vendors [13]. Honda uses this data to prepare market potential reports used when recruiting new dealers, for making site selection decisions, and to prepare market studies for a potential store’s business area. Like Meineke, Honda has preformatted reports that automatically retrieve, integrate, and format relevant data from its diverse sources once the area for a report has been specified.

The Meineke and Honda cases each illustrate the integration of internal reports, market intelligence information from commercial vendors, decision support analysis using embedded analytical tools. The earlier example from the Ace Hardware case illustrates the integration of market research data and market intelligence data to develop a marketing plan. In each of these cases, GIS provided the means of integrating the different data sources and enabled the decision support analysis. This integration would have been significantly more difficult without the GIS technology.

## 6. Implications for researchers

This paper’s introduction asserted that GIS ‘‘can fundamentally alter the cost and effectiveness of marketing decision making’’. Economists teach us that when there are fundamental changes in the costs or returns associated with resources there tend to be shifts in the allocation of resources, the conduct of activities, and the profitability of the organization. If GIS do ‘‘fundamentally alter the cost and effectiveness’’ of decision making, it is likely that these shifts will be observed in the conduct and effectiveness of marketing activities.

This section has two goals. First, it looks forward to the broader managerial implications of GIS as a MKIS technology. If GIS, in fact, has the potential to affect the practice of marketing the way we believe, we should be prepared to identify where this will occur. Second, at this point, the exact nature of these effects can only be conjecture. We therefore outline research topics for each of our areas of impact. In many ways, the technical and practice-oriented discussions early in the paper lay the foundation for the more important theoretical presentation here.

We organize this discussion into two subsections. First, we discuss research on the impact of GIS on the execution of the marketing mix (product, pricing, place/distribution, promotion). Second, we discuss the resource allocation implications of geographic MKIS. What resource shifts can we expect to see if GIS technologies can improve the effectiveness of marketing decision making?

## 6.1. GIS and the marketing mix

This paper presented some ways in which GIS supports common marketing decisions such as site selection and target marketing. More companies are embracing the technology and some of these companies are developing innovative ways to use GIS. We feel that an important element of our ability to understand the use of GIS is a thorough examination of how the technology can be used for executing activities in the traditional marketing mix. This section examines the four elements of the mix and suggests research questions aimed at specific issues in each element. We also discuss privacy issues that span all four elements of the mix.

## 6.1.1. Product

The product component of the marketing mix involves matching the attributes of products to the characteristics of consumer groups. To the extent that consumer characteristics are geographically distributed, the effort to design and market products for consumers will rely on geographic data.

Some spatial components of products are well known. We know that sales flounder when product names do not translate well to the local language. While adapting products to cultural concerns may be easy when distribution is on the national level, it may require finer tuning for products distributed to areas with large ethnic populations. Research may help to determine whether GIS can be integrated in the product design and distribution decision to garner a healthier market share in such environments.

Another product-oriented decision is the process of discovery that matches consumer and product characteristics. We have already discussed using

GIS to discover where products are selling well and what characteristics of consumers in these areas drive demand. The same analysis, though, can be used to question the product’s characteristics that make it unattractive in the low sales areas. This information can then be used for marketing decisions on product line-stretching, line-filling, linemodernization, and features.

## 6.1.2. Pricing

How many of us remember, ‘‘Prices slightly higher west of the Mississippi?’’ Don’t we expect to pay more for gasoline at the station right off the interstate? We know that geography can influence price. What we need to know is how much and why. As with other research topics in GIS and marketing, there are two components to this research issue.

First, we would like to know if GIS can refine the way that spatially dependent pricing decisions are made. If so, what are the appropriate models, circumstances, and factors to be considered? What are the outcomes, both in terms of revenues, market share, traffic, etc? What specific technologies and techniques can be used and how generalizable are they across markets, products, and industries? How important are the proximity of premium or discount complimentary or competing products and services, other merchants, etc.

Second, we would like to know if products that are not currently priced according to spatial considerations could be or vice-versa. In both of these issues, we may find that lack of data or analytical techniques may have precluded the effective implementation of pricing models. GIS may then be the enabling technology to improve pricing decision making when there are spatial components to prices.

## 6.1.3. Place (distribution)

Distribution and location decisions are one of the first areas where GIS became widely used in the marketing mix. This paper has already mentioned the use of GIS in site selection and delivery routing and there is a wealth of other examples in the business GIS literature (though not so much in the academic marketing literature).

Unfortunately, the existing examples are mostly anecdotal. They show that somebody did use GIS and that it was (usually) successful but they do not formalize the contributions to successful decision making. Future research should formalize the relationship between decision type, data availability, other situational characteristics, and the successful use of GIS to support distribution decisions. This research can address retail locations, distribution centers, fixed delivery routing, and flexible delivery routing as both independent problems to be solved and as components of an overall distribution strategy decision. The research should also address the appropriateness of using ad hoc spatial MKIS versus investing in a formal system intended for repeated use. This issue is addressed further below.

## 6.1.4. Promotion

As with the distribution component of the marketing mix, promotion has been an area with early and increasing use of GIS technology. Promotion also has a significant body of anecdotal literature without a rigorous understanding of the integration of theory, technology, and practice.

One of the most important issues to be addressed in the area of promotion is the realized efficacy of integrating internal and external data through the use of GIS. The authors clearly expect GIS to play an important integrating role, and anecdotal evidence supports this opinion. It remains to be seen, however, whether these suppositions stand up to more formal investigative techniques.

## 6.1.5. Privacy

A research question that spans all four areas of the marketing mix is the subject of personal privacy. By combining internal and external information GIS users are able to infer characteristics of a customer that the customer did not volunteer. We have seen courts hold in the case of pricing insurance coverage that some geographic inferences about individuals cannot be used for business decision making. Research should investigate the limits of spatial inference when these technologies are used in marketing decision making.

## 6.2. GIS and decision making resources

The concept of an MKIS includes three components, a decision maker, information (data), and support tools (technologies), all interacting in the context of a decision. Just as a marketing strategy consists of the balanced selection of the elements of the marketing mix, designing an MKIS consists of the balanced selection of these three components. Further, each of these components is what economists call compliments in that the value of one without the others is limited (e.g., a decision maker using no information will not make very good decisions). Further, increasing the value of one complimentary input often increases the value of the others, at least within a range. Better roads increase the value of automobiles while better movies increase the value of theaters (and vice versa).

Fig. 5 illustrates the relationship between components of an MKIS and the decisions to which the system is applied. As the effectiveness (and therefore value) of each component increases, so does the value of the other components. Further, as both the value (importance) and number of decisions increases, so do the values of the MKIS as a whole and of the individual components. These relationships are not absolute, though. We can expect diminishing returns if one component is improved or increased disproportionately to the others. Too much information results in information overload. Too many decision making aids will not be useful if data is lacking and if users are not trained in their use.

Research should discover how these MKIS components are related to each other in different decision making contexts. We are clearly interested in this research when GIS technologies are in the Tools and Technologies role but the research could extend well beyond this narrow scope. With respect to the GIS technologies, though, we feel that research in the following areas will be valuable.

![](/api/attachments/DGBQKGKJ/fulltext/images/c89772da18e1bf32e09c6f68a2e5de3529317d82ddcda378ef0fc9902d844a01.jpg)  
Fig. 5. Complimentary components of a MKIS.

## 6.3. The value of data

The K/BB model and our discussions have highlighted the importance of both internal and external data in marketing decision making. Of special interest is the development of the market for external spatial data and its relationship to internal data when used with a GIS. Research should identify the trends in the production, accuracy, and price of external spatial data and how might we expect these trends to continue if the market for GIS technology continues to grow. Are there any limits to the development of this data? For example, the Census Bureau limits public disclosure of some data to protect privacy creating a clear limit on the detail available from Census-based data.

How will the availability of external data affect internal data collection efforts? Internal and external data may be compliments in some situations so that better external data increases the incentive to collect internal data. On the other hand, external data may be a substitute for internal data and may lower data collection costs. Finally, these relations are almost certainly decision-dependent. Discovering these relationships will contribute to a fuller understanding of the value of GIS and MKIS.

## 6.4. The value of people

GIS require both technology-specific and domainspecific knowledge for effective operation. As these tools increase in value there will be a corresponding increase in the demand for decision makers conversant with the technology. West [35] identified the specific skills needed for end-user operation of GIS but this list must be updated to include not only general managerial decision making but also to address marketing-specific GIS skills. Research should also address the best mix of people and skills for the operation of GIS-based MKIS. Should marketing analysts be trained in GIS concepts, should marketing professionals be teamed with GIS experts, or should specific techniques be embedded in software tools?

## 6.5. The value of tools

There are two types of technology tools we must understand for spatially oriented MKIS. First are the GIS software packages themselves. This paper introduced some of the technologies available and explained how advances in capabilities have fueled the demand for these products. In large measure, however, the availability of GIS software will be driven by a multitude of factors, only a few of which stem from the marketing community.

Of more interest from a research perspective is the potential for building custom applications around the GIS technologies. Recall that most of these tools have powerful custom programming features. These features enable organizations to invest considerable sums in the construction of MKIS (such as the Meineke case cited earlier) aimed at specific decision making tasks. Companies routinely spend hundreds of thousands, or millions, of dollars on conventional (non-spatial) decision support and transaction processing systems. Before such expenditures are contemplated in the MKIS area there must be a clear understanding of the relationship between system characteristics and decision making value.

## 6.6. Decisions

Decisions lie at the heart of the model in Fig. 5. The value of the decision gives rise to the value of each component of the MKIS and the number and range of decisions increases or restricts the opportunities for employing GIS as an MKIS. This paper has discussed several marketing decisions that are amenable to support by GIS technologies and the first part of this section detailed more decision-related research opportunities.

We reintroduce marketing decisions here as a research topic with a slightly different perspective. Research should address the relationship between decisions, tools, data, and people (skills). The MIS community took some time to learn that standard systems do not support every managerial decision.

We can benefit from their experience by proactively researching the relationship between decision characteristics and the structure of the most appropriate MKIS.

## 7. Conclusions

This paper introduced GIS technology as a component of marketing information systems and proposed an increased role for the technology based on the fit between the technology and elements of the marketing mix. We accomplished this goal by presenting some of the technology’s capabilities, specific examples of the technology in practice, and an overview of research questions centered on GIS. Some implications of this presentation are relatively straightforward while others are subtler. We wish to conclude this paper by highlighting some of these implications.

First, there is clearly a role for GIS in marketing. Our presentation of the four elements of the marketing mix in the previous section showed that there is a geographic component to each element and it is natural to expect that spatially oriented technologies will help with decision making in these areas. The earlier presentation focused around the K/BB model of MKIS provided specific ways in which GIS can fill roles in the model. This discussion also provided anecdotal examples of GIS capabilities in action.

Second, one of the most easily realizable benefits of integrating GIS into MKIS is the ability to provide map-based presentations of data relationships for decision makers. MIS research has shown that decision makers are more effective when the data they need is presented in a manner appropriate to the decision context. GIS performs admirably in this role when the decision making context involves geographic relationships.

Third, one of the most important capabilities of GIS is its ability to integrate disparate data using geography as the common key. The K/BB model highlighted this need and we explained the GIS technological features giving rise to this capability.

Fourth, and less obviously, we feel that GIS is still in its infancy as a MKIS component. Even though the specific technology has been with us for over 20 years, the availability of end-user interfaces; personal computer, client-server, and Internet-capable versions of GIS software; and, most importantly, widely available data is a relatively recent phenomenon. It is this unrealized potential that we feel makes GIS so interesting as a marketing decision making tool and as an important research topic.

## References

[1] I. Benbasat, A.S. Dexter, An experimental evaluation of graphical and color-enhanced information presentation, Management Science 31 (11) (1985) 1348 – 1364.

[2] I. Benbasat, A.S. Dexter, An investigation of the effectiveness of color and graphical information presentation under varying time constraints, MIS Quarterly 10 (1) (1986) 59 – 83.

[3] I. Benbasat, A.S. Dexter, P. Todd, The influence of colour and graphical information presentation in a managerial decision simulation, Human-Computer Interaction 2 (1986) 65 – 92.

[4] C. Bereson, Marketing information systems, Journal of Marketing 33 (1985) 16 – 23.

[5] A.C. Burns, R.F. Bush, Marketing Research, 3rd ed., Prentice-Hall, Upper Saddle River, NJ, 2000.

[6] M.D. Crossland, B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decision Support Systems 14 (1) (1995) 219 – 235.

[7] L.R. Davis, Report format and the decision-maker’s task: an experimental investigation, Accounting, Organizations, Society 14 (5/6) (1989) 495– 508.

[8] T. Eisenhart, Computer aided marketing, Business Marketing 73 (5) (1988) 49–56.

[9] S. Garrison, Meineke drives home need for market data, Business Geographics (1999 May) 21– 23.

[10] C. Harder, GIS Means Business, Environmental Systems Research Institute, Redlands, CA, 1997.

[11] S. Harrod, Lessons learned: improving trade area analysis, Business Geographics 5 (9) (1997) 38–39.

[12] E.D. Hoadley, Investigating the effects of colour, Communications of the ACM 33 (2) (1990) 120 – 139.

[13] R. Hoerning, American Honda jump-starts sales geographically, Business Geographics 4 (3) (1996) 24 – 26.

[14] J.J. Jiang, G. Klein, J. Motwani, J. Balloun, An investigation of marketing managers’ dissatisfaction with marketing information systems, International Journal of Information Management 17 (2) (1997) 115 – 121.

[15] E.F. Keon, Making MKIS work for you, Business Marketing 72 (10) (1987) 71– 73.

[16] M. Krishnan, S. Mayuram, R. Venkatram, An empirical analysis of customer satisfaction for Intranet marketing systems, Decision Support Systems 24 (1998) 45 – 54.

[17] P. Kotler, Marketing Management: Analysis, Planning, and Control, 9th ed., Prentice-Hall, Upper Saddle River, NJ, 1997.

[18] J. Laiderman, Site selection basics, Business Geographics (1999 February) 20– 23.

[19] T.W. Lauer, The effects of variations in information complex-

ity and form of presentation on performance for an information extraction task. Unpublished doctoral dissertation, Indiana University, Bloomington, 1986.

[20] W.J. Lee, K.C. Lee, A meta decision support system approach to coordinating production/marketing decisions, Decision Support Systems 25 (3) (1999) 239 – 250.

[21] E.Y. Li, Marketing Information systems in small companies, Information Resources Management Journal 10 (1) (1997) 27– 35.

[22] E. Li, R. McLeod Jr., J.C. Rogers, Marketing information systems in Fortune 500 companies: a longitudinal analysis of 1980, 1990, and 2000, Information and Management 38 (2001) 307– 322.

[23] M.H. Liberatore, G.J. Titus, P.W. Dixon, The effects of display formats on information systems design, Journal of Management Information Systems 21 (8) (1988) 908– 919.

[24] R.T. Moriarty, G.S. Swartz, Automation to boost sales and marketing, Harvard Business Review 67 (1) (1989) 100 – 108.

[25] S. Munroe, Z.N. Zainul, How to solve multi-facility location problems, Business Geographics (1999 May) 18 – 20.

[26] R.A. Proctor, Marketing information systems, Management Decision 29 (4) (1991) 55– 60.

[27] R.S. Rubin, L.A. West Jr., Putting your business on the map: geographic information systems for small business, Journal of Small Business Strategy 10 (2) (1999) 1 –19.

[28] M.J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (1) (2001) 127 – 137.

[29] J.B. Smelcer, E. Carmel, The effectiveness of different representations for managerial problem solving: comparing tables and maps, Decision Sciences 28 (2) (1998) 391– 420.

[30] R.H. Sprague, A framework for the development of decision support systems, MIS Quarterly 4 (1980) 1 – 26.

[31] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[32] R.W. Stone, D.J. Good, Theoretical and operational marketing information systems, Review of Business 11 (3) (1989) 23– 28.

[33] R.W. Stone, The assimilation of computer-aided marketing activities, Information and Management 38 (2001) 437– 447.

[34] S. Sudman, E. Blair, Marketing Research: A Problem Solving Approach, McGraw Hill, Boston, MA, 1998.

[35] L. West, Designing end-user geographic information systems, Journal of End User Computing 12 (3) (2000) 14 – 22.

[36] B. Wierenga, G.H. van Bruggen, The integration of marketing problem-solving modes and marketing management support systems, Journal of Marketing 61 (1997) 21– 37.

[37] K.H. Yoo, The effects of question difficulty and information complexity on the extraction of data from an information presentation, Unpublished doctoral dissertation, Indiana University, Bloomington, 1983.

Ronald L. Hess is an assistant professor of Marketing at the College of William and Mary. He received his PhD in Marketing from Virginia Tech in 1991 and has previously published in Marketing Letters. Dr. Hess’ research interests include services and relationship marketing and customer loyalty.

Ronald S. Rubin is Professor of Marketing and Director of the Small Business Institute at the University of Central Florida. Dr. Rubin received his PhD in Business Administration with a major in Marketing from the University of Massachusetts in 1973 and a master’s degree from the Wharton School. Dr. Rubin’s research interests include GIS as a market intelligence tool. He is the coauthor of Marketing Research, 7th edition, Experiential Exercises in Marketing Research, and authored the Rubin and Luck Data Analysis Disk and PC Marketer: Computer Applications Using Lotus 1-2-3, all published by Prentice-Hall. He is co-author of Strategy and Competition, a marketing simulation published by Allyn and Bacon.

Lawrence A. West Jr. is an assistant professor of Management Information Systems at the University of Central Florida. Dr. West received his PhD in MIS from Texas A&M University in 1991 and has been at UCF since 1996. His research interests include the economics of information and information technologies and GIS as a decision support technology. Dr. West has published extensively in these areas in journals such as JMIS, Decision Sciences, and Decision Support Systems.
