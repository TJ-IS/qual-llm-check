---
otero_id: 21283
otero_key: "G5QEF3H7"
title: "Geospatial information utility: an estimation of the relevance of geospatial information to users"
authors: "W.Lee Meeks; Subhasish Dasgupta"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00076-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Geospatial information utility: an estimation of the relevance of geospatial information to users

W. Lee Meeks <sup>a,</sup>\*, Subhasish Dasgupta

Geospatial Intelligence Department, Veridian Systems Division, Veridian Corporation, Chantilly, VA, USA <sup>b</sup> Management Science Department, MON 403, The George Washington University, 2115 G Street, NW, Washington, DC 20052, USA

Received 1 September 2001; accepted 1 March 2003 Available online 25 July 2003

## Abstract

As the acquisition and use of information are costly, the optimal use of information involves economic tradeoffs. Therefore, valuing information is attracting research and thought. However, till now, little attention has been paid to the geospatial information domain, which is increasingly coming to the attention of decision makers seeking to improve decision models by considering spatio-temporal factors. This paper proposes a metric called Geospatial Information Utility (GeoIU), which will allow decision makers to assess the degree of utility of accessed geospatial data sets when making decisions that incorporate those geospatial data and information. The GeoIU metric uses multi-attribute utility theory to assess, score, and weight metadata queries run against geospatial data and information discovered in distributed sources. C 2003 E1sevier B V. A1l rights reserved

Keywords: Information utility; Multiple attribute utility; Multi-attribute utility functions; Geographic information systems

## 1. Introduction

Geospatial data are data having geographic and spatial orientations: data having some information content that includes a location component. Often, geospatial data and information also have a temporal aspect, an example of which is change detection over time. The term ‘spatio-temporal’ pertains to these types of data. People make ‘place’ and ‘time’ decisions everyday: choosing the best route to the neighborhood grocery store given the traffic patterns at a particular time of day or attending an appointment with your dentist are two simplistic examples [31]. It has been estimated that nearly 80% of all data has a location component [9]. Geospatial data are collected and analyzed by organizations in order to solve a broad array of public and private sector problems.

For example, epidemiologists have long studied the case of Dr. John Snow who traced the 1854 outbreak of cholera in London’s Soho district to a public water pump on Broad Street by annotating on a street map the home addresses or work locations of the sick and dying. By correlating the locations and numbers of cholera-infected patients, even though they were of different social classes (and hence, different seemingly unconnected lifestyles), Dr. Snow isolated the source of the outbreak: the offending Broad Street water pump. After a test of the water revealed bacterium responsible, he was able to convince skeptical officials to remove the pump’s handle so no one could draw contaminated water from the pump. The results were dramatic and immediate; the number of cholera cases quickly dropped off [51].

Today, the use of spatio-temporal data and information greatly improves decision-making in many different fields [16]. Examples in government include health and safety, public works, recreation and culture, land use and zoning, administration, financial operations, other management, and military and intelligence support. Examples in business include marketing support and planning, retailing, various types of services, wholesaling and distribution, and other broad technical planning and support in a wide variety of industries [1]. Thus, spatio-temporal analyses are now becoming part of rigorous analytical frameworks for local, national, and global security and business intelligence realms. When using spatial and temporal information to improve decision making, attention must be paid to uncertainty and sensitivity issues [21]. Attention must also be paid to spatial and temporal scales relevant to the decision being supported [45] and to the quality and utility of available data, with respect to the intended use(s) of the data [42]. This last issue defines the core problem geospatial information utility (GeoIU) addresses: that decision makers collect and use geospatial data of varying spatial and temporal scales in order to improve decision making, but more attention needs to be paid to finding appropriate methods for assessing the utility of the geospatial data being used [10].

Beyond the data issues are system ones. Geospatial data are collected by various means, processed, and stored, or disseminated for later use by geographic information systems (GIS), which require geospatial data for spatial or spatio-temporal analysis and presentation. GIS are considered to include data, hardware, software, procedures, operators (i.e., analysts), and analytical requirements (i.e., the problem needing to be solved). GIS exist primarily to ingest, manipulate, model, analyze, display, and output value-added geospatial data, information, and products in multiple file formats for some information (e.g., display) or decision-making (i.e., through analysis) purposes [12,28,33]. Fig. 1 depicts a simplified process model for GIS.

Burrough [13] provides several definitions of GIS by focusing on different perspectives; a tool-box view, a database view, and organization-based view. These views comport nicely with a broad 2001 summary of information systems research conducted by Orlikowski and Iacono [43]: they report on tool, proxy, ensemble, and computational views of information technology. Burrough’s three views identify some of the complexity of the evolving geospatial sciences domain: (1) GIS provide tools for analysts and decision makers to access and analyze complex, temporally, and spatially oriented data in order to improve decision making; (2) GIS operate on spatially oriented data, yet geospatial data and spatial databases are complex; and (3) organizations use GIS to improve product and/or service offerings, and to improve decision making by incorporating factors in ways not previously considered.

![](/api/attachments/G5QEF3H7/fulltext/images/e9afc6dbe68ff9416faa76e17b7bd4856f62aefb9d059816efdda20d8d570570.jpg)  
Fig. 1. A simplified process model for GIS use.

Following data and systems’ issues come issues surrounding the data providers. Geospatial data and information are produced by a wide variety of governmental and commercial producers and vendors. For several years, a niche geospatial community of providers and users has been dealing with the evolving complexity of the use and analysis of geospatial data. Only now are geospatial data and spatio-temporal analyses migrating beyond domain- or industry-specific niches. Decision makers in many fields, industries, and organizations are now coming to grips with the benefits and challenges inherent in the storage, retrieval, transmission, and analysis of these types of data. They are also becoming aware of the breadth of analyses that are possible when information-rich geospatial and spatio-temporal data are made available [8,24,34]. A community of interest that has sprung up to integrate advances in GIS and geospatial data into matters pertaining to US-focused homeland security, called Homeland Infrastructure Foundation Level Database (HIFLD), is aggressively pushing the boundaries on issues related to GIS and geospatial data. At a recent HIFLD conference (Nov 2002), the most important issues pertaining to the use of geospatial data were identified to be: data type (i.e., form of the data), data schema or structure, metadata (i.e., presence, quality, completeness), pedigree (i.e., source), quality (i.e., pertains to content, horizontal, and vertical accuracy), and currency (i.e., age relative to use) [5]. Conferences and communities of interest such as these encourage the convergence of data, GIS, providers, and users.

For purposes of this paper, it is useful to broadly classify GIS and geospatial data users into two broad categories: (1) governmental users and (2) non-governmental users. Governmental users are primarily interested in public domain uses of geospatial and spatio-temporal data: for example, military planners may require highly accurate, very current digital data sets for planning flight routes for cruise missiles. Flight route planning requires digital elevation models to support terrain contour matching algorithms within the missiles’ guidance modules. To optimally employ so-called ‘‘smart weapons’’ such as these, planners and targeters must have access to current, high-quality digital data sets with minimal horizontal and vertical accuracy errors. In order to reduce operational risk in the development of missile flight routes based on new digital geospatial data sets, the ‘pedigree’ or quality of the supporting data must be assessed [34]. As mentioned previously, many other public sector uses of GIS and geospatial data abound: fuel modeling to predict and prevent wildfires, cadastral records and land tax planning, information visualization of municipal government services via Web-based GIS applications, and many more. Each of these uses of geospatial data has different requirements for data accuracy, currency, and form; some applications have stringent requirements and others less so.

Non-governmental users are primarily interested in commercial or business intelligence analyses of geospatial data and information. These users may also have varying needs for highly accurate and current data sets: for example, planners in cell phone companies may employ GIS technologies and data analyses in order to determine optimal site locations of a new array of digital wireless telephone signal towers. Their analyses might focus on making maximum use of both send and receive signal strengths vis-a\`-vis local terrain limitations (e.g., received signal strength is a function of transmitted power, number and locations of transmitter towers, radio frequency line-of-sight obstacles, etc.) in order to minimize the number of towers needed while providing a guaranteed quality of service for cell phone subscribers; using fewer, well placed towers may mean lower operating costs and higher operating margins. Similar to the missile flight route problem, a wireless telephone tower location analysis based on geospatial data of poor or uncertain quality is subject to errors, which may roll through the calculations, quite possibly resulting in improperly located towers, reduced systems performance, higher installation and operations and maintenance costs, and unhappy customers.

While assessing the value of geospatial information content is now attracting the interest of researchers, current theories and approaches for valuing information concentrate on the estimation of the content value of textual information [7]. For example, popular search engines use several different evaluation schemes such as keyword proximity, keyword density, and synonym matching, among others, to estimate the quality of links and files returned from Internet text searches. However, no such algorithmic approaches exist for users, producers, and brokers of geospatial information to estimate the value of the geospatial information relative to the needs and uses of geospatial users, producers, and brokers, nor to dynamically perform these analyses rapidly, or in an automated way. On the surface, text-oriented search, retrieval, and valuation tools seem to have little usefulness and no analog in the geospatial domain. The geospatial equivalent of a textual keyword or key concept could be any spatially oriented feature commonly found within the geospatial data. Examples include a road network or a single road, a bridge, a stream, river, or other linear or area geographic feature leading researchers to consider if the key ‘things’ to be searched for are so different, what mechanisms must be found or developed for performing search and retrieval operations for geospatial data and information?

Considering both governmental and non-governmental uses of geospatial data, the quality of the uses, analyses, or decisions made based on available geospatial data depends on the quality of the underlying data being used. This paper outlines an algorithmic approach to estimating the content value of geospatial information and data sets for researchers and users of this type of information.

Within the US government, the National Imagery and Mapping Agency (NIMA) and the US Geological Survey (USGS) are responsible for setting standards and guiding the geospatial community (which includes all governmental and non-governmental entities) focused on government-related uses of geospatial data [34]. The predecessor organization of NIMA, the Defense Mapping Agency, had a long-established, periodic product evaluation schema for evaluating then-current products (i.e., geospatial data is provided in many hard- (e.g., maps and charts) and soft-copy forms (e.g., digital elevation models, raster map displays, vector map data sets)) based on published product specifications. This approach to determining product adequacy through performing product evaluations from a producer’s point of view was flawed and is no longer being used as official policy [42].

To determine the adequacy, relevance, and usefulness—herein defined as the ‘‘utility’’—of geospatial information provided to consumers of the same within the US government, geospatial products (i.e., both hard maps and digital data sets) are presently assessed as adequate in an adequate/not adequate binary ‘‘vacuum’’. That is, the geospatial information either meets all predefined product adequacy standards and specifications for all content components, or it does not. If it does not, then the intended consumers of these data sets are not allowed access to them. This de facto binary quality process is more about control than access to data, and presumes:

(1) Information not meeting some predefined standard has no value;

(2) All consumers of geospatial data essentially have the same quality needs for all situations;

(3) Collectively, the producers of geospatial information possess the same knowledge and awareness of the consumers’ geospatial data and information needs as the customers themselves and can therefore evaluate the value of the geospatial information provided to them [40].

As a result of this situation, two members of the Veridian Corporation (including one of the authors) were tasked under the auspices of NIMA’s Geospatial Information Infrastructure Implementation Integrated Process Team (GI3 IPT) to hypothesize an alternative to the legacy product evaluation schema. The government’s interest was two tracked: (1) perform a rapid analysis of the theory needed to develop a proof-ofconcept prototype tool to automate geospatial information utility (GeoIU) assessments, and (2) develop the prototype. The work for the government was performed during February to June 2001. This research continues the theoretical analysis.

The robustness of the information age, including activities such as mass customization of products and information, is replacing mass production and mass media as the preferred business value paradigms. Government is learning from the business community the lesson that one size does not fit all: that everything is susceptible to change over time. The same is true of geospatial information needs: as geospatial information producers adopt a stronger customer orientation, they must re-think how to assess the usefulness of the geospatial information they provide to their customers. In this paper, we propose a new metric called Geospatial Information Utility (GeoIU), which estimates the relevance of geospatial information to users. An important point is that performing a utility assessment based on the relevance of a select data set from a user’s point of view, for any of n-specific intended uses at the instant of assessment, is not the same as performing an accuracy assessment. The literature is replete with processes and cases for performing accuracy assessments and computing error matrices on geospatial data sets. Whereas, accuracy assessments measure statistical ‘‘goodness’’ against an absolute standard, such as for a product specification [2,3,18,19,35,38,39,41], utility assessments measure usefulness relative to the user’s intended use [40].

GeoIU does not use a binary metric for adequacy; instead, it provides users and producers with real-time, interval information about the usefulness of available data sets in addressing specific information needs. GeoIU is responsive to the users’ intended uses because it provides users the ability to weigh specific attribute and utility measures based on their specific intended uses, and it supports mechanisms for users and producers to prioritize geospatial data acquisition and production. More importantly, it directly addresses the three assumptions listed above:

(1) Users of both hard- and soft-copy geospatial data and products frequently comment that something is better than nothing; therefore, geospatial information producers should routinely allow access to users of the best geospatial information available at any given time, irrespective of its estimated adequacy or its status with respect to being finished data or work-in-process data.

(2) It is incorrect to assume that all users are the same, or that they have the same information and information quality needs. Therefore, it is also folly to assume all intended uses, such as military mission planning or installation planning for wireless telephone signal towers, have the same data needs.

(3) As with most other products, physical or informational, the users of a product or service are the ones best able to determine its utility versus its intended use.

This paper examines information retrieval with respect to determining information relevance. Then it proposes a model to perform information utility calculations using an information relevance paradigm based on prior exploratory work performed by the UK Defense Imagery and Geospatial Liaison Staff to the US National Imagery and Mapping Agency [39]. In the following sections, we provide a theoretical framework based on a review of available literature related to this concept, we provide a vision of how GeoIU might be used to aid decision makers using geospatial data and information and how it would be constructed, we report some preliminary results, and finally we provide implications for further research. Excellent GIS and geospatial sciences glossaries can be found at Refs. [2,3,13,41].

## 2. Envisioning GeoIU

This research is a model building effort based on the following construct (Fig. 2), modified from Daalen, Thissen, and Verbraeck [23].

Obermeier [42] explicitly defined the goals and functions needed in a model such as GeoIU; however, as discussed above, other goals and functions have been derived from the need for this sort of dynamic, real-time service to be provided to GIS users to improve their understandings about the limitations of the analyses they perform. Outside of, but in complement to, the processes of GIS, a program of research into geospatial information utility model building must address three sequential concepts: (1) information retrieval, (2) information grading or valuation, and (3) information presentation.

![](/api/attachments/G5QEF3H7/fulltext/images/fd3c18c172015b150dbeec39b36cf1295619a29eecce2130cff4c00067af14e3.jpg)  
Fig. 2. A model building construct.

As shown in Fig. 3 this paper is primarily concerned with the information valuation or grading aspect—the aspect most critical to decision sciences. The study does this through examining multi-criteria decision-making (MCDM) [46] and multiple attribute utility theory (MAUT) [14]. The first and last concepts: information retrieval and information presentation complement GeoIU model building, thus they are considered, but only to the degree that they affect GeoIU research. However, these concepts that remain interrelated must be considered together when hypothesizing and articulating a logical approach to addressing information relevance for geospatial information, and for developing an algorithm capable of computing and displaying the utility of geospatial information within selectable parameters based on users’ information needs. Finally, given the dearth of information valuation research in the geospatial domain, many of these concepts are examined in broader, non-geospatial contexts as we ponder their specific applicability to geospatial data and information. This paper assumes that a conceptual correlation exists between concepts, as they are being applied in the textual domain, to the problem of determining information utility for geospatial data.

As shown in Fig. 4, a top-level information utility schematic, GeoIU is comprised of metrics about the quality of available geospatial information and metrics about the user’s intended uses for the information. Considering in Fig. 1 the process model GIS use, the first issue for a GeoIU ‘‘tool’’ is the information retrieval problem.

## 3. Information retrieval

Information retrieval is about information discovery and delivery, that is, discovering the right data sets and bringing them to the analyst or application that needs them for some user-defined purpose. Within this model, the information quality aspect can be further described as shown in Fig. 4. The key components of information quality—relative to the users’ needs—are based on metadata queries, which score metadata values found in selected, distributed geospatial data sets and query scoring functions.

In this era of ‘‘information explosion’’, providing the right information to the right person within a reasonable amount of time is a very important goal for today’s information retrieval systems [7,15]. Due to the characteristics of different retrieval methods, conventional information retrieval models often suffer from inaccurate and incomplete queries as well as inconsistent content relevance. We agree and further believe that users will have their own individual intended interpretation of the semantic meanings of their query terms, and that these meanings are not always captured via search mechanism interfaces. Chen and Kuo’s [15] discussion highlights problems users of geospatial information utility will face: that is rarely complete or homogeneous data (or metadata) of uniform quality available. This is true even where complex and well-defined metadata structures exist.

![](/api/attachments/G5QEF3H7/fulltext/images/a0e62202297d4229ba996f822b6a0297e434129742a6ba8b002f2c9f5de235b4.jpg)  
Fig. 3. Assisting the GIS process with utility assessments via the GeoIU model.

![](/api/attachments/G5QEF3H7/fulltext/images/6dc5f64c1573095bafea7c8ba5f5a67fe7c767aad20456f4800a1a8f3ea79119.jpg)  
Fig. 4. Basic functional structure for geospatial information utility.

Horng and Yeh [29] propose a novel approach to automatically retrieve keywords and then to use generic algorithms to adapt keyword weights. The core of the GeoIU algorithm rests on capturing and applying user-defined search parameters, which are based on intended use of the data returned from the search, and which are compared in a relative ranking fashion to determine appropriate weights. While textual retrieval and scoring models, such as Horng and Yeho’s, rely on keyword weights, which help in the examination—the scoring and weighting—of the textual data itself, the proposed GeoIU algorithm scores retrieved geospatial metadata values as the de facto keywords of a geospatial data search, in lieu of textual keywords. The GeoIU model allows for weighing them similarly, based on a user’s intended use of the geospatial data discovered through the resultant search query. The ability to develop appropriate user-defined weighing factors contributes directly to increasing customization of the GeoIU model.

Classical information retrieval theory uses the language of documentation sets for the results of queries [7,54]. Applied to the GIS problem, a document set can be thought of as a consistent group or series of maps, drawings, or records that have the same subject matter, format, or purpose [41]. Information retrieval strategies should be insensitive to modest changes in the relevant document set since individual relevance assessments are known to vary widely [54]. Investigated are net change relevance assessments relative to the evaluation of retrieval results. Very high correlations were found among rankings of systems produced using different relevance judgment sets. We considered this approach in the development of the GeoIU model, but extend the Voorhees approach [54] because it limits the authors’ concept for information utility as their model is intentionally capable of detecting and reporting on longitudinal (i.e., over time) changes in GeoIU scores based on underlying changes in the source data and metadata.

The structure and organization of geospatial information utility queries and calculations should be extended to an Internet-based search, discovery, and retrieval paradigm in order to gain access to more and richer data sources over time. Web or intranet searching is shifting from presenting a list of ‘‘hits’’ to a richer, more complex presentation of information, delivering information in a meaningful context [6]. According to Sherman [47], ‘‘searching is a modern technological wonder, but algorithms can only do algorithmic functions. Humans perform other types of functions, including putting information into context and drawing relationships’’. We posit the future of searching for geospatial information will be best achieved by combining routine indexing searches with putting rich human needs back into the search process. And, as applied to this research, to clearly accommodate intended use(s) of discovered data as part of both retrieval and evaluation functions.

Studies have been performed by analyzing over 1 million Web queries by users of the Excite search Excite search engine. The Spink, et al. [49] study found that most people use few search terms, few modified their queries, view their retrieved Web pages, and rarely use advanced search features. This study provides insight into public practices and choices in Web searching. The work of Spink et al. [49] has particular relevance to the authors’ study as the prototype GeoIU tool accounts for both ‘‘basic’’ and ‘‘power’’ users. Implications about the sophistication of users are useful in considering the breadth and complexity of search and grading parameter inputs. Statistical association measures have been widely used in information retrieval research [17]. Usually, these are based on clustering documents and terms on the basis of their relationships. Applications of association measures for term clustering include automatic thesaurus construction and query expansion. Further, Jansen and Pooch [32] discuss the current state of research on Web searching. Considering this research to be at an incipient stage, they hypothesize this to provide a unique opportunity to review the state of research in the field, identify common trends, develop a methodological framework, and define terminology for future Web searching studies. Importantly, they propose a framework and implications for the design of studies into Web information retrieval systems, which are useful in focusing the GeoIU model, particularly with regards to interfaces.

## 4. Information valuation

Methodologies must account for the shortfalls in available data. As described in this paper, the users of GeoIU must be able to: (1) define appropriate query parameters, and (2) weigh the scoring protocols provided within the information quality segment of the methodology as shown here.

After the retrieval problem is solved (or at least addressed), the scoring of retrieved metadata values must be accomplished. Given the dearth of direct literature focused on valuing geospatial information, we looked at two key topics: MCDM, characterized by Saaty [46], Teng et al. [52], and Vincke [53], who all discuss similar approaches to addressing and solving multi-criteria decisions and to developing multiple attribute utility models. Malczewski [38] provides excellent treatment of the topic with respect to GIS and spatio-temporal supported decisions. We used these concepts both to clarify the domain (i.e., a content issue) and to clarify our approach to applying Multicriteria Decision Analysis to the framework of GeoIU algorithm development. A related topic is Butler’s MAUT [14]. We relied most heavily on MAUT for our model development.

Fraser and Gluck [27] state that little is known about how users employ metadata to evaluate the relevance of geospatial information objects in satisfying the users’ information and decision making needs, and that this might differ from non-geospatial information needs. Metadata is normally defined as data about data. In the United States today, geospatial metadata structures are nominally guided by metadata standards being developed by a multi-agency task force called the Federal Geographic Data Committee (FGDC) [4]. Similar standards are evolving internationally [30]. However, though these standards are becoming more universally accepted, there remains great variability in their application. For example, even when well-defined metadata structures exist, the values necessary to populate metadata tables are often left null. An interesting and necessary outgrowth of geospatial information utility research should be a reevaluation of existing metadata structures in order to link future metadata structures with different ways to query and analyze metadata.

Marsden [39] provides a very useful model for determining geospatial information utility. This model considers the Fraser and Gluck [27] requirements for robust and available geospatial metadata without describing how that metadata is to be made available. This model can be summarized as: information utility is a function of the quality of the information made available in any given query and of a user’s information search needs, as related in user-defined functional terms. The term ‘‘intended use’’ is used to describe the end purpose or how geospatial information is commonly used. The notion of intended use provides an insightful framework for describing use cases around which user profiles and parametric preferences can be developed.

Learning the users’ interest categories in a dynamic environment, such as the Web, is challenging because they (i.e., users’ interests) change over time. Novel schemes to represent the users’ interest categories, using adaptive algorithms to discover the dynamics of users’ interest through the use of positive and negative relevance feedback, have been developed [55]. Empirical studies confirm the effectiveness of this schema to accurately model a user’s interest and to adapt appropriately to various levels of changes in the user’s interests. The notion of accommodating change in the users’ interests over time is relevant and has been considered in the GeoIU model and prototype tool development. Spink and Greisdorf [48] hypothesize that though the current dichotomous approach to information relevance has produced abundant information retrieval research, relevance studies that include consideration of the users’ relevance judgments will provide greater clarity and congruity.

## 5. Information presentation

The data fusion issue is not trivial, but it is becoming better understood over time [8,20,34,36,37]. Just as there is routine data fusion with geospatial data content, so too must an information utility algorithm be able to fuse geospatial metadata. For example, a user’s query for all road network data within a given scalar band, within a selected area of interest (AOI), may yield many different data holdings within several distributed governmental, academic, foreign, and commercial databases. If successfully accessed, there may be several areas of overlap. These areas must be fused and evaluated within the context of a new ‘‘whole’’. Dunlop [25] presents the main lines of discussion about Mira, a working group of the Commission of the European Union Information Technologies Program, designed to advance research in the area of evaluation frameworks for interactive and multimedia information retrieval. The Mira working group brought together many of the leading researchers in information retrieval and human –computer interaction. Dunlop identifies the need for more varied forms of evaluation, which need to be considered to complement engine evaluation.

Stratigos and Curle [50] examined some commonly held ideas about end-users, specifically their skills and abilities, and their understanding of the proper use of the Internet and commercial information products. They undertook this study because many assumptions have been made about end-users and their information-seeking skills. This study presents survey results, one of the most important of which is discovering that behaviors for verifying information generally have not changed. The common portrayal of end-users as uncritical consumers of information is not very accurate. The study shows that users are not lazy information seekers who accept at face value the first piece of information that comes along; rather, users, in general, are not likely to trust unverified information. The Stratigos and Curle assumptions and results are relevant to our work because we presume: (1) users want to assert some control over their (geospatial) information search and manipulation operations and, (2) users are sophisticated enough to use some or all of the ‘‘mass customization’’ features we envision for them when the GeoIU model is operationalized as a systematic application. Coincidentally, since some or all of the data may need to be purchased, the information utility query must aid the user in determining whether or not to make the purchase.

The importance of the current literature lies not in its alignment with this specifically focused topic, because there are a few direct links between the literature and the information relevance problem for producers and users of geospatial information. Rather, the importance of the literature lies in its ability to point to important trends and ideas for further investigation in closely related disciplines. These pointers have provided focus for the exploratory construct, and have contributed to both the iterative development of the algorithmic methodology and of a prototype tool itself.

## 6. Computing GeoIU

The focus of this research is to determine a useroriented methodology for estimating the relevance of geospatial information to users within existing and future uses of these data and information. The proposed GeoIU metric measures the usefulness of geospatial information in terms of its spatial accuracy (accuracy is typically comprised of both spatial accuracy (i.e., of the objects features contained in a database) and content accuracy (i.e., of the attributes associated with each feature); in this context, spatial accuracy is the measure of merit); currency; percentage of area coverage; ‘‘usability’’ as determined by user-defined data types or forms; and availability for use within a required datum. This research attacks the core of the information utility problem, which is the requirement to access selected metadata records associated with specific geospatial information data sets over any selected area of interest (AOI), and integrate and analyze those metadata in such a way as to create a utility function for the underlying information set or holding.

Fig. 7 provides the current GeoIU model within an architectural schema as it applies Saaty’s [46], Buede’s [11], and Butler et al. [14] multiple attribute

![](/api/attachments/G5QEF3H7/fulltext/images/c68f96c3c6bbada19c718c152d9b00eefd2b2537dc4ce5ba98b1c8c78a83c715.jpg)  
Fig. 5. Considering evaluative functions with respect to information quality.

utility models to the GeoIU problem. The evolution of the models shown in Figs. 4 – 6 has lead to the adaptation of the Marsden model, shown in Fig. 7. Eastman et al. [26] address the need and a partial approach, using raster techniques, for applying a multi-criteria/multi-objective approach to geospatial decision making. A prototype GeoIU desktop application was developed using the model in Fig. 7 in order to provide a proof of concept under contract to NIMA [42]. The GeoIU tool searches the metadata of targeted test datasets to examine and compare recordlevel values for each geospatial data set or product against normative function curves. The metadata value retrieved from a user’s GeoIU query provides a function-derived score. This score represents a thematic-level score for one data query record within a user-defined area of interest (AOI). Following the successful retrieval of one or more geospatial data sets, two things can occur:

(1) the geospatial content must be manipulated within the GIS.

(2) The geospatial metadata may or may not also be accessed for separate evaluation and manipulation.

Irrespective of the power and functionalities found within a user’s particular GIS, toolset, or application suite, where more than one data set has been retrieved, quite frequently, the user is able to employ the GIS application to fuse together various components of the data set or multiple data sets, which often contain thematic layers. Over time, more robust GIS applications are being developed, including

![](/api/attachments/G5QEF3H7/fulltext/images/eb2056df9abf8c681ae87453c7b5d8b91d55932b93b00ff1dd3cd7f2916b3c06.jpg)  
Fig. 6. Considering evaluative functions with respect to information needs.

![](/api/attachments/G5QEF3H7/fulltext/images/0c13e337329ee9ff5ab86055c94d78a2232c640c4f56a787db12b50b7c7e5a45.jpg)  
Fig. 7. Architectural schematic of the geospatial information utility function.

those for use within common Web browsers. For example, a popular GIS tool such as Environmental Sciences Research Institute’s (ESRI) ArcView GIS is able to ingest geospatial data of different types, including digital elevation data, road network coverage data and hydrographic, and fuse these data together within the desktop application for the purpose of performing a detailed terrain analysis such as a cross-country mobility study based on soil composition and moisture content, slope percentage derived from a detail elevation model or source, and vegetation density [44].

Computing GeoIU is a function of a real-time analysis of available metadata for selected data sets

within targeted areas of interest. Besides being algorithmically driven, which implies repeatable consistency, information utility assessments could easily be performed via a simple desktop tool or application. This study hypothesizes that GeoIU may be based on something as simple as a weighed-average calculation using the sum of the weights for each evaluation criteria (e.g., accuracy, currency, coverage, usability form, and datum availability) applied to factor scores for each criterion. The weight given to each criterion would be user-defined. These calculations would be performed within use-oriented scalar bands already familiar to geospatial consumers. These bands of scalar representations (i.e., symbolizations) are important because they represent different levels of data density and feature symbolization that users require to perform various geospatial information analyses. Each evaluation criterion will have comparative utility score values found in community-defined look-up tables or function curves. Calculating GeoIU internal to the GeoIU tool leads to a raw score for each criterion, normalized for comparison and presentation. Nominally, the computed IU score of an evaluated data set, within any intended use scale band, for example, could then be summarized as the weightedaverage sum of all criteria scores:

$$
\begin{array}{r l} \text { GeoIU   score } & = \sum \text { GeoIU   factor   scores } \\ & \times \text { individual   criterion   factor   weights } \end{array}
$$

Fig. 8 illustrates an example of the methodology being evaluated in a proof-of-concept prototype tool developed in early 2001. Only area coverage and currency are illustrated here; however, this methodology of using look-up tables and continuous distribution scoring functions must be based on parameters (e.g., the shapes of the curves, including their coefficients and exponents) agreed upon by the geospatial information using community. These agreements for developing scoring mechanisms suitable for addressing critical metadata attributes (e.g., age of available data in years or months for the currency rating) must continue for all critical information utility factors.

For an information utility assessment to be made for a selected area of interest (e.g., the western coast of equatorial Africa), the following steps represent the sequence of implementation actions:

![](/api/attachments/G5QEF3H7/fulltext/images/17d385df4cb1594fa6c57555f6f713b0504b5b71997ef351f1e0ceef165334a5.jpg)  
Fig. 8. Illustrating the effects of partial GeoIU calculations.

(1) A user uses an interactive graphical user interface to select a specific area of interest at one or more selected scale bands.

(2) The user then designates their own relative attribute score weights as a means to establish relative priorities, and then also selects any minimum query thresholds for each of the utility factors for their current intended use (note: the sum of the weights must = 100%).

(3) The IU tool then queries metadata of available and selected databases, linking to predetermined fields for current data values relative to the IU assessment (e.g., age of the data, spatial accuracy, etc.).

(4) As a result of each metadata query, individual component utility factor scores are calculated.

(5) Each component utility factor score is then multiplied by the previously defined utility factor weights, providing individual criterion weighed values.

(6) The individual weighed-values are then summed together for computation of the information utility assessment score for the selected area of interest.

(7) Where thematic ‘‘layer’’ information is available (in either the data or metadata), the IU assessment is preferred at the thematic level based on the greater richness of the data at this level of detail. When thematic-level IU scores can be calculated, they are done and then aggregated into the final IU score for the selected area of interest.

## 7. Model methodology

As depicted earlier, the basic GeoIU model focuses on two critical inputs: (1) information quality based on the structure and results of metadata queries, and (2) information needs based on the users’ query-specific evaluative parameters. To answer preliminary ‘Assess the Model’ questions, we assumed a qualitative logic of inquiry oriented on eliciting the most important data quality and intended use stories from a limited user pool. To this end, we began by parsing our small user pool of users by type and interest. Divided into focus groups, called technical exchange meetings (TEMs) in government parlance of 8– 10 participants each, we held three TEMs on GeoIU issues during May and June 2001.

In order to focus our TEM participants’ attention, we developed an orientation of Constructive Empiricism [22] that we dubbed ‘‘anecdotal empiricism’’. This term arose from the evolved structure of the dialogue sessions with the TEM participants. The term is meant to imply that we sought the TEM participants’ experiences in their current geospatial data use paradigms, through anecdotal storytelling. This came to pass even though we attempted to structure the TEM sessions through administration of a two-page questionnaire focused on metadata scoring and weighting issues.

Though we meant that there be statistical rigor to this pilot data collection effort, as it turned out, the users’ interest was so keen on discussing the core GeoIU concepts and their enthusiasm for telling their geospatial data use stories was so great that the questionnaires served only as a vehicle for focusing the TEM dialogues. Ultimately, they were not a meaningful means to structure the users’ responses. The questionnaire included questions about users data quality, currency, accuracy, form, and datum issues. Of particular interest was uncovering effective means to translate users’ stories as baseline data points into a form useful in developing the scoring functions for each of the principal areas of interest (e.g., currency, accuracy, form).

As predicted, users based on three critical factors of interest shown in Table 1.

These three critical factors of interest have been empirically derived from interaction with participants in the pilot TEMs. These factors can be thought of as intersecting in a 4 - 5 data cube that constitutes a universe of possible user classes as shown in Fig. 9.

The part of the research dependent on characterizing and understanding users leads to scheduling the user TEMs in order to present to them the core concepts described and to perform a preliminary data collection. The purpose of the data collection was two-fold: (1) to gain insight into appropriate scoring functions for each of the target metadata attributes scored (e.g., age of the data, horizontal and vertical accuracy, form of the data, the datum in which the data are referenced, and area coverage related to the selected AOI) and, (2) to gain insight into participants’ preferences for functions and interfaces. These pilot meetings were held in April and May 2001. A total of 20 participants were interviewed in these focus group-type meetings. Despite many TEM participants’ unfamiliarity and some initial skepticism with the core concepts associated with GeoIU and the limited time available in these pilot meetings, the first meetings provided tremendous insight into a small population of users’ preferences, and some opportunities for designing future TEMs on a much larger scale.

Table 1  
Three factors of interest in characterizing government users classes

<table><tr><td>Sample scales of interest</td><td>Sample functions of interest</td><td>Broad environments of interest</td></tr><tr><td>Macro (e.g., &lt;1:500,000)</td><td>Planning</td><td>Land</td></tr><tr><td>Medium (e.g., 1:25,000–1:500,000)</td><td>Operating</td><td>Sea</td></tr><tr><td>Micro (e.g., &gt;1:25,000)</td><td>Modeling and Simulation</td><td>Air</td></tr><tr><td></td><td>Detailed analyses</td><td>Urban</td></tr></table>

(1) Scale is expressed as a ratio, where larger numbers represent smaller scales and the rule of thumb is that large scales represent small areas and vice versa. (2) The littoral zone occurs at the meeting of sea and land, and it represents a special case for classes of geospatial data and products. (3) TEMs are government parlance for technical exchange meetings, which can be considered somewhat akin to a focus group with narrowly focused objectives.

A successful, albeit very limited prototype GeoIU tool was developed as a Web-based desktop application for NIMA during the writing of the 2001 Geospatial Transition Plan [34]. This proof-of-concept was tested on small ‘‘slices’’ of several different data sets obtained from several different governmentowned databases. The types and quantities of records accessed represented a tiny fraction of types and quantities available across the globe. However, this approach did satisfy the proof-of-concept, ‘‘can we do $\mathrm { i t ? } \ '$ question. As with most prototypes, the chief value is as a communication vehicle between geospatial information users and counterpart researchers, systems developers, and other domain analysts. Regarding the ability to query metadata records for associated geospatial content records, the prototype development team encountered varying degrees of success with the small number of different metadata structures examined. This effort and the inspection of various metadata attribute populations indicate that significant follow-on effort needs to focus on metadata standards and attribute population.

## 8. Conclusion

The information utility metric being developed and validated via this research is oriented on providing decision makers who rely on the geospatial information or other spatio-temporal data with a higher degree of confidence in the quality of the underlying data they employ in their decision support systems. Risk can be managed or eliminated through greater insight into the quality of the underlying data—from the users’ intended use-based point of view, estimation not currently available today.

## 9. Implications for researchers

This is an underserved field that has tremendous potential based on the growing interest in spatiotemporal information. There exists both an opportunity and a need for researchers to develop, test, and refine models such as these. Just as practitioners have the need for these types of tools in order to improve the quality of their decision-making, researchers have something to offer in terms of providing the analytical rigor needed to improve the quality of these models. There are both short- and long-term challenges for those interested in furthering this work. In the shortterm, the models need refinement, primarily through applying statistical confidence to the scoring functions. Beyond that, a broader set of metadata attributes should provide the basis for retrieval scoring and weighting; age, accuracy, datum, and form of data are not enough—though they served as useful for this initial exploration—greater breadth and depth need to be applied to the metadata attributes that are examined. In the longer term, work needs to be applied to the metadata structures themselves. Defenders of the current metadata structures argue that the metadata standards and structures are sound and have been vetted within the community.

![](/api/attachments/G5QEF3H7/fulltext/images/f5051496b77e1538e69a6eefaf09df7584156b3e365050f2d1b82a1929d69782.jpg)  
Fig. 9. Considering relevant functions in the user population cube.

## 10. Implications for managers

We posit this will be important and useful work for managers because of the growing dependence on geospatial information to aid managers of organizations in their decision-making activities. Envisioned are five general use cases that the GeoIU model can support:

<sub>o</sub> To provide longitudinal evaluations of changes in available GI data and information by holding constant one or more fixed query parameters

<sub>o</sub> To support multi-perspective (i.e., multiple user class types) for organizational evaluations of geospatial data over common areas of interest

<sub>o</sub> To support pre-acquiring evaluations of expensive or difficult to acquire GI data

<sub>o</sub> To support focused or tailored geospatial analyses

<sub>o</sub> To support evaluations of the compatibility of GIS tools and intended GI data sources

For both producers and users of geospatial data and information, the litmus test will be whether the concept and implementation of geospatial information utility are sufficiently rigorous and useful to satisfy the users needs. To summarize: the proposed geospatial information utility metric will measure the usefulness of geospatial information found in multiple, distributed libraries for individual users based on their missions, tasks, and geospatial analysis problems.

## References

[1] GIS for the 21st Century, EI Technologies, LLC. p. 51.

[2] Glossary of Mapping, Charting, and Geodetic Terms, 4th ed., Defense Mapping Agency, Washington, DC, 1981, p. 204.

[3] Military Handbook: Glossary of Mapping, Charting, and Geodetic Terms. MIL-HDBK-850, Department of Defense, Washington, DC, 1994.

[4] Federal Geographic Data Committee Content Standard for Digital Geospatial Metadata, United States Geological Survey, Reston: VA, 1998, p. 90.

[5] Briefing at Homeland Infrastructure Foundation Level Database Conference, Reston, VA, 2002.

[6] S.E. Arnold, M. Colson, The ‘‘R’’ technology revolution: relationships, research, revenue, Searcher 8 (9) (2000) 36 – 52.

[7] R. Baeza-Yates, B. Ribeiro-Neto, Modern Information Retrieval, Addison Wesley, Harlow, 1999, p. 513.

[8] J.K. Berry, Spatial Reasoning for Effective GIS, GIS World Books, Fort Collins, CO, 1995, p. 208.

[9] J.D. Bossler, An introduction to geospatial science and technology, in: J.D. Bossler (Ed.), Manual of Geospatial Science and Technology, Taylor and Francis, London, 2002, pp. 3– 7.

[10] S.D. Bruin, A. Bregt, M.V.D. Ven, Assessing fitness for use: the expected value of spatial data sets, International Journal of Geographical Information Science 15 (5) (2001) 457–471.

[11] D.M. Buede, The engineering design of systems: models and methods, in: A.P. Sage (Ed.), Wiley Series in Systems Engineering, Wiley, New York, 2000, p. 462.

[12] P.A. Burrough, Principles of Geographical Information Systems for Land Resources Assessment, Oxford Univ. Press, Oxford, 1986, p. 193.

[13] P.A. Burrough, R.A. McDonnell, Principles of geographical information systems, in: P.A. Burrough, et al. (Eds.), Spatial Information Systems and Geostatistics, Oxford Univ. Press, Oxford, 1998, p. 333.

[14] J. Butler, D.J. Morrice, P. Mullarkey, A multiple attribute utility theory approach to ranking and selection, Management Science 47 (6) (2001) 800– 816.

[15] P.-M. Chen, F.-C. Kuo, An information retrieval system based on a user profile, The Journal of Systems and Software 54 (1) (2000) 3 – 8.

[16] G. Christakos, P. Bogaert, M. Serre, Temporal GIS: Advanced Functions for Field-based Applications, Springer, Berlin, 2002, p. 213.

[17] Y.M. Chung, J.Y. Lee, A corpus-based approach to comparative evaluation of statistical term association, Journal for the American Society for Information Science and Technology 52 (4) (2001) 283– 296.

[18] R.G. Congalton, K. Green, Assessing the accuracy of remotely sensed data: principles and practices, in: J.G. Lyon (Ed.), Mapping Sciences Series, Lewis Publishers, Boca Raton, 1999, p. 137.

[19] R.G. Congalton, L.C. Plourde, Quality assurance and accuracy assessment of information derived from remotely sensed data, in: J.D. Bossler (Ed.), Manual of Geospatial Science and Technology, Taylor and Francis, London, 2002, pp. 349–363.

[20] J.W. Crampton, Interactivity types in geographic visualization, Cartography and Geographic Information Science 26 (2) (2002) 85– 98.

[21] M. Crosetto, S. Tarantola, Uncertainty and sensitivity analysis: tools for GIS-based model implementation, International Journal of Geographical Information Science 15 (5) (2001) 415– 437.

[22] M. Curd, J.A. Cover, Philosophy of Science: The Central Issues, W.W. Norton, New York, 1998, p. 1379.

[23] C.E.V. Daalen, W.A.H. Thissen, A. Verbraeck, Methods for the modeling and analysis of alternatives, in: W.B. Rouse (Ed.), Handbook of Systems Engineering and Management, Wiley, New York, 1999, p. 1236.

[24] M.N. DeMers, Fundamentals of Geographic Information Systems, 2nd ed., Wiley, New York, 2000, p. 498.

[25] M. Dunlop, Reflections on mira: interactive evaluation in information retrieval, Journal of the American Society for Information Science 51 (14) (2000) 1269 – 1274.

[26] J.R. Eastman, et al., Raster procedures for multi-criteria/multiobjective decisions, Photogrammetric Engineering and Remote Sensing 61 (5) (1995) 539–547.

[27] B. Fraser, M. Gluck, Usability of geospatial metadata or space – time matters, Bulletin of the American Society for Information Science 25 (6) (1999) 24 – 28.

[28] P. Gray, et al., Geographic information systems, in: S. Gass, C.M. Harris (Eds.), Encyclopedia of Operations Research and Management Science, Kluwer Academic Publishing, Boston, 2001, pp. 326– 329

[29] J.-T. Horng, C.-C. Yeh, Applying genetic algorithms to query optimization in document retrieval, Information Processing and Management 36 (5) (2000) 737– 759.

[30] http://www.fgdc.gov/metadata/whatsnew/fgdciso.html, FGDC/ISO Metadata Standard Harmonization. 2000, FGDC.

[31] P. Jankowski, T. Nyerges, Geographic information systems for group decision making: towards a participatory, geographic information science, in: P. Fisher, J. Raper (Eds.), Research Monographs in Geographical Information Systems, Taylor and Francis, London, 2001, p. 273.

[32] B.J. Jansen, U. Pooch, A review of web searching studies and a framework for future research, Journal of the American Society for Information Science and Technology 52 (3) (2001) 235 – 246.

[33] R.G. Johnson, Electronic gouge and acronym decoder (EGaAD): a list of abbreviations, acronyms, associated descriptions, and definitions of terminology common to the geospatial, imagery, telecommunications, and systems engineering disciplines, 2001, p. 420.

[34] R.G. Johnson, et al., United States Imagery and Geospatial

Information Service Geospatial Transition Plan, National Imagery and Mapping Agency, Bethesda, MD, 2001, p. 175.

[35] S. Lane, K. Richards, J. Chandler (Eds.), Landform Monitoring, Modelling and Analysis. British Geomorphological Research Group Symposia Series, Wiley, Chichester, 1998, p. 454.

[36] T.M. Lillesand, R.W. Kiefer, Remote Sensing and Image Interpretation, 4th ed., Wiley, New York, 2000, p. 724.

[37] P.A. Longley, et al., Geographic Information Systems and Science, Wiley, Chichester, 2001, p. 454.

[38] J. Malczewski, GIS and Multicriteria Decision Analysis, Wiley, New York, 1999, p. 392.

[39] R. Marsden, UK Measurement of Geospatial Information Utility, UK Defense Imagery and Geospatial Liaison Staff, London, 2000.

[40] W.L. Meeks, R. Mauck, Exploring Information Utility: An Algorithmic Approach, National Imagery and Mapping Agency, Reston, VA, 2001, p. 30.

[41] G.E. Montgomery, H.C. Schuch, GIS data conversion handbook, GIS World Books, GIS World, Fort Collins, CO, 1993, p. 292.

[42] J. Obermeier, Discussion of Product Adequacy and Product Evaluations at NIMA, and Finding Automated Methods for Determining the Utility of Geospatial Information, in: W. Lee Meeks (Ed.), Bethesda, MD, 2001.

[43] W.J. Orlikowski, C.S. Iacono, Research commentary: desperately seeking the ‘‘IT’’ in IT research—a Call to theorizing the IT artifact, Information Systems Research 12 (2) (2001) 121–134.

[44] T. Ormsby, et al., Getting to Know ArcGIS Desktop: Basics of ArcView, ArcEditor, and ArcInfo, ESRI Press, Redlands, CA, 2001, p. 541.

[45] G.M. Pereira, A typology of spatial and temporal scale relations, Geographical Analysis 34 (1) (2002) 21– 33.

[46] T.L. Saaty, Fundamentals of Decision Making and Priority Theory: With the Analytic Hierarchy Process, vol. VI, RWS Publications, Pittsburgh, 1994, p. 525.

[47] C. Sherman, Search engine strategies, Information Today, 17 (9) (2000) 1.

[48] A. Spink, H. Greisdorf, Regions and level: measuring and mapping users’ relevance judgments, Journal for the American Society for Information Science and Technology 52 (2) (2001) 161 – 173.

[49] A. Spink, et al., Searching the web: the public and their queries, Journal for the American Society for Information Science and Technology 52 (3) (2001) 235 – 246.

[50] A. Stratigos, D. Curle, The end-user speaks: commercial desktop services and the open web, Online 24 (5) (2000) 74– 78.

[51] J. Summers, Soho—A History of London’s Most Colorful Neighborhood, Bloomsbury, London, 1989, pp. 113 – 117.

[52] G.-H. Teng, J.-Y. Teng, C.-L. Ju, Multiobjective investment planning for improving quality of life: a case study for Taipei City, Multiple Criteria Decision Making, Proceedings of the Ninth International Conference: Theory and Applications in Business, Industry, and Government, Springer, Fairfax, VA, 1990.

[53] P. Vincke, Multicriteria Decision-aid, Wiley, West Sussex, UK, 1992, p. 154.

[54] E.M. Voorhees, Variations in relevance judgments and the measurement of retrieval effectiveness, Information Processing and Management 36 (5) (2000) 697 – 716.

[55] D.H. Widyantoro, T.R. Iorger, J. Yen, Learning user interest dynamics with a three-descriptor representation, Journal for the American Society for Information Science and Technology 52 (3) (2001) 212–225.

Lee Meeks is a PhD candidate at The George Washington University in the Management Science Department of the School Of Business and Public Management. His degrees include an MBA from George Washington University and a BS from the US Naval Academy. He works as a Senior Scientist and Program Manager within the Geospatial Systems Group of Veridian Systems Division in Chantilly, VA. He has spent over 7 years in the employ of or consulting to the National Imagery and Mapping Agency. His current research interest is improving organizational decision-making through the innovative application of information technologies. His focus is advances in geographical information systems (GIS) as a subset of information systems, as GIS and spatio-temporal data are applied to organizational decision-making. His previous publications have been for the National Imagery and Mapping Agency. He has presented at the Institute for Operations Research and Management Science (INFORMS) annual meeting.

Subhasish Dasgupta is an assistant professor of information systems in the School of Business and Public Management, The George Washington University. He received his PhD from Baruch College, The City University of New York (CUNY), and MBA and BS degrees from the University of Calcutta, India. His current research interests are electronic commerce, information technology adoption and diffusion, and Internet-based simulations and games. He has published in journals such as European Journal of Information Systems, Logistics Information Management, Journal of Global Information Management, Journal of Global Information Technology Management, Simulation and Gaming Journal, and Electronic Markets: The International Journal of Electronic Commerce and Business Media. He has presented at numerous regional, national, and international conferences.
