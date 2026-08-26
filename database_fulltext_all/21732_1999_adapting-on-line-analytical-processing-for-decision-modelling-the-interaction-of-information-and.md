---
otero_id: 21732
otero_key: "BUGC2BBJ"
title: "Adapting on-line analytical processing for decision modelling: the interaction of information and decision technologies"
authors: "Nikitas-Spiros Koutsoukis; Gautam Mitra; Cormac Lucas"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00021-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adapting on-line analytical processing for decision modelling: the interaction of information and decision technologies

Nikitas-Spiros Koutsoukis <sup>)</sup>, Gautam Mitra <sup>1</sup>, Cormac Lucas

Brunel UniÕersity, Department of Mathematics and Statistics, Uxbridge, Middlesex, UB8 3PH, UK

Accepted 7 April 1999

## Abstract

The introduction of new technologies and concepts has redefined the relative positioning of information systems IS andŽ . decision technologies in a corporate context. Corporate IS have been extended to include not only transaction processing databases but also analytical databases, often known as Data Warehouses. On-line analytical processing OLAP , asŽ . introduced by Codd et al. E.F. Codd, S.B Codd, C.T. Salley, Providing On-Line Analytical Processing to User–Analysts:<sup>w</sup> An IT Mandate, E.F. Codd and Associates, 1993 , is capable of capturing the structure of the real world data in the form of<sup>x</sup> multidimensional tables which are known as ‘datacubes’ by management information systems MIS and statistical systemsŽ . specialists. Manipulation and presentation of such information through multidimensional views and graphical displays provide invaluable support for the decision-maker. We illustrate the natural coupling, which exists between data modelling, symbolic modelling and ‘What if’ analysis phases of a decision support system DSS . In particular, we explore the power ofŽ . roll-up and drill-down features of OLAP and show how these translate into aggregation and disagreggation of the underlying decision models. Our approach sets out a paradigm for analysing the data, applying DSS tools and progressing through the information value chain to create organisational knowledge. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Decision-maker; OLAP; Multidimensional databases; Datacube; Dis aggregation; Information technology; Decision models; Ž . Analytic database; Information value chain; OR<sup>r</sup>MS models; Forecasting; EIS; DSS; Interfaces; Model granularity

## 1. Introduction

Management information systems MIS , decisionŽ . support systems DSS and executive information Ž . systems EIS represent a natural progression in in- Ž . formation systems IS development. Their progress Ž . has also underpinned the convergence of IS and DSS. Their common characteristic is that they analyse and synthesise information from corporate data <sup>w</sup> <sup>x</sup>23,31,45 . For historical reasons MIS, DSS and EIS evolved as separate components of the Enterprise Information System considered from a decision support perspective.

On-line analytical processing OLAP is a recentŽ . advance in the field of IS for decision support. OLAP not only integrates the MIS, DSS, EIS, functionality of the earlier generations of IS, but goes further and introduces spreadsheet-like multidimensional data views 5,6 and graphical presentation <sup>w</sup> <sup>x</sup> capabilities. For a discussion of the recent developments of OLAP and its relationship with the corporate IS, we refer the reader to Refs. 3,11,50 . An<sup>w</sup> <sup>x</sup> illustration of the current relative positioning of IS and decision tools DT and their functional relation-Ž . ship is shown in Fig. 1.

In the past, corporate data was usually stored in production databases which are on-line transaction processing OLTP systems, also known as transac-Ž . tion databases. It is only recently that information specialists have realised the need to analyse the data and store it in a different form which can be better utilised for decision-making purposes 31,47 . The<sup>w</sup> <sup>x</sup> work by Codd et al. 5 has led to a distinction <sup>w</sup> <sup>x</sup> between analytic databases ADBs and operationalŽ . or production databases PDBs . A summary of theseŽ . differences is presented in Ref. 50 which provides a clear delineation between the functionalities of OLTP and OLAP. We now illustrate this with a simple example. Consider a customer order processing application in which the transaction-oriented database stores information such as: the name of the customer, the customer’s identification number, the customer’s order reference number, the value and the date of the order, with links to other tables holding other relevant data e.g., quantity and quality of items ordered,Ž method<sup>r</sup>date of dispatch, etc. . A manager however,. needs to analyse the data and requires the resulting information in a more succinct form, such as: total number of orders per day, total number of deliveries per day, or how many orders were dispatched without a delay, etc. It is much more important for the manager to have this information in a time-order manner especially to understand trends in customer behaviour. In traditional PDBs, such time-order information is not available. As a result, trends in customer behaviour cannot be identified which in turn denies the business decision-maker a valuable insight. By extending and analysing information from the PDB and storing it in the ADB in time-order, the information is readily available to executives for decision-making. Applying other criteria for analysing the data as found in the PDB leads to more extensive collections of information which have become known as data warehouses and data marts 3,7,16,17,22,41,44 . The complete set of ADBs created by these investigations is referred to as the corporate data warehouse. Any subset of the ADBs which relates to a particular department or a particular application is commonly known as a data mart.

The IS infrastructure as presented in Fig. 1 includes a connectivity layer commonly known as Ž Middleware which is used to reorganise data and . achieve cross-platform integration 26,42 . The mid- <sup>w</sup> <sup>x</sup> dle and top layers in Fig. 1, consist of analytic tools, which comprise management science<sup>r</sup>operational research MS Ž . Ž . <sup>r</sup>OR models and data mining DM <sup>r</sup> knowledge discovery in databases KDD tools Ž . <sup>w</sup> <sup>x</sup> 8,15,36 . Finally, OLAP and EIS interface play a vital role of accessing and reporting knowledge or ‘business intelligence’ created by the system.

This process of analysing data, synthesising it into information and further refining it into knowledge is a well-known DSS process for instance, see Ref.Ž <sup>w</sup> <sup>x</sup> 14 . An alternative perspective of this process is set. out in Fig. 2 which shows the information value chain IVC . A detailed description of these terms isŽ . provided as a glossary and appears in Appendix B.

![](/api/attachments/BUGC2BBJ/fulltext/images/cb68a1bfa5a6a6f0cf20eda2186f142eab423549e5cd6a23dbbd4075e421f6cf.jpg)  
Fig. 1. Relative positioning of information and decision tools.

![](/api/attachments/BUGC2BBJ/fulltext/images/4ac001a47db3e1bf73b64a0e16f199b0737b28b98cb2ec8b1ae91556bfb7175a.jpg)  
Fig. 2. Information value chain.

The IVC model, illustrated in Fig. 2, works as follows: different transactional data, which is present in the PDB, is transferred to the analytic database, where it is stored in a form customised for the user and suitable for analysis e.g., time-ordered, aggre-Ž gated, etc. . This form also provides a ‘single version. of the truth’. The data is then analysed and synthesised, resulting in information. Then the KDD tools and MS<sup>r</sup>OR models, are instantiated by the available information to produce knowledge e.g., using Ž optimisation, rule induction . The OLAP–multidi-. mensional database MDDB has continued to gainŽ . acceptance in the DSS community because it places the analyst in direct contact with the data, models and the related analyses 46 .<sup>w</sup> <sup>x</sup>

Thus, the analytic database achieves the following: a it stores data ranged over time; b it linksŽ . Ž . otherwise disparate data items appearing as transactional data; c it provides a ‘single version of theŽ . truth’; d it provides accessibility to the data; andŽ . Ž .e it allows for customised user views of the data.

The components in our modelling paradigm use the same underlying structure, and are linked to each other as shown in Fig. 3. From the user–analyst’s point of view, OLAP and the MDDB serve as an interface. They connect the user with the analytic database, as well as with the analytic tools MSŽ <sup>r</sup>OR, KDD<sup>r</sup>DM . This interface is then used for a variety. of purposes, including model formulation and finetuning, post-solution analysis and ADB customisation for a specific user. DOME 30 provides a <sup>w</sup> <sup>x</sup> prototype example of an MDDB<sup>r</sup>OLAP-based linear program LP model formulator and post-solution Ž . analysis reporter.

![](/api/attachments/BUGC2BBJ/fulltext/images/96ab81fd5a0732fb66c48bce542d5a76aebb7e267868ed1bf36d9c04cb1cfe6a.jpg)  
Fig. 3. Interaction between information and decision technologies.

The OLAP–MDDB interface is used to assist the decision-maker in creating appropriate KDD and MS<sup>r</sup>OR models by browsing the appropriate data groups, and defining the model-based relations between these data groups. The models and their data are then passed to the appropriate computational tool for solution execution, through Middleware connectivity, and the solution is reported back to the decision-maker. This approach is useful to the user– analyst as there is no need to acquire expert knowledge for a particular MS<sup>r</sup>OR model or DM<sup>r</sup>KDD tool, and they can thus concentrate on interpreting the results, or carry out further analyses. It is assumed that the decision-maker is familiar with the functionality of the different models or tools e.g.,Ž optimisation, rule induction tools that may be imple- . mented. Geoffrion 12 has developed the paradigm<sup>w</sup> <sup>x</sup> of structured modelling which provides an alternative but novel method of data information and knowledge representation. Raghunathan 39 has pre- <sup>w</sup> <sup>x</sup> sented this as a modelling methodology for designing DSS.

The rest of this paper is organised in the following way: in Section 2, we introduce OLAP for the reader who is not familiar with the concept. We explain the structure of MDDBs and describe the

OLAP features in respect of viewing the data as well as manipulating the data items. Section 3 sets out the interaction of data models, decision models and resulting investigation. In this section, a business problem is first introduced. This is followed by modelling of the data, and illustrations of roll-up, drill-down and slice features of OLAP. These are subsequently exploited in the definition of decision models. In the formulation of the decision models, the natural coupling of the multidimensional structure with the symbolic models are illustrated. Subsequently, we expand on this ‘natural coupling’ by showing how roll-up, drill-down features of OLAP are used to create aggregated and disaggregated models. This section is concluded with the discussion of analysis and investigation of models and the use of multidimensional tables in capturing the results for multiple scenarios. In Section 4, we summarise our conclusions regarding the interaction of decision models and IS.

## 2. OLAP features: multidimensional data, viewing and manipulation

## 2.1. An introduction to OLAP

Introduced by Codd et al. 5 , OLAP is an archi-<sup>w</sup> <sup>x</sup> tecture used to provide users with the ability to perform dynamic data analysis. By using OLAP tools, users gain access to the corporate analytical database. This type of access provides decisionmakers with the potential to improve their understanding of corporate changes, their ability to identify or generate possible solutions for a variety of decision problems, and their ability to develop tactical and strategic formulae regarding corporate variables. This ability, to analyse and synthesise information from OLAP, is ‘made up of numerous, speculative ‘what if’ and ‘why’ data model scenarios <sup>w</sup> <sup>x</sup> 5 . In these model scenarios, key variables are changed, and the behaviour of organisational factors is then observed. The data models are then animated, and as the user synthesises information, he gains knowledge about the behaviour of corporate parameters, as presented by the model s . According to Ž . Codd et al. 5 , the models used in OLAP systems<sup>w</sup> <sup>x</sup> are one or more of the enterprise data models: categorical, exegetical, contemplative, formulaic. Their characteristics are summarised in Table 1.

A more familiar classification of models is the one that separates models into descriptive instead ofŽ categorical , explanatory instead of exegetical , pre-. Ž . scriptive and normative 23 . The descriptive–explanatory–prescriptive–normative classification examines models in relation to the decision-maker’s actions, rather than their relation to corporate planning. However, conceptual similarities can be noticed between the two classifications, regarding the purpose s of the models. Ž .

<table><tr><td>Categorical</td><td>Exegetical</td><td>Contemplative</td><td>Formulaic</td></tr><tr><td>Static data analysis, use of historic dataDescribes history of enterprise/events; shows state of enterpriseLittle/no user interactionConsolidation paths inherent in DB designData accessible via query tools, report writers, spreadsheets</td><td>Static data analysis, use of historic dataExplains the state shown by categoricalUser interaction requiredConsolidation paths not readily available, must be created on the flyExisting tools not adequate</td><td>Dynamic data analysis, scenario dataProjection of state according to introduction/ variance of parameters across the consolidation paths of the data modelsSufficient user interactionNew consolidation paths must be createdSpreadsheet tools exist for single data dimensions. No adequate database support, or support for multidimensionality</td><td>Most dynamic of the modelsSeeks a particular outcome through the modelHighest degree of user interactionHighest degree of variable data consolidation pathsNo products exist</td></tr></table>

OLAP was introduced together with 12 rules, which were thought to help eliminate misconceptions about OLAP’s key characteristics. These 12 rules were set forward by Codd and Codd 6 :<sup>w</sup> <sup>x</sup>

1. Multidimensional conceptual Õiew Ždiscussed above . User’s perspective of the enterprise is. multidimensional; therefore, user’s data view should be multidimensional. Views should be customisable by roll-up–drill-down–slice–dice functionality.

2. Transparency. Open systems architecture. The analytical tool can be embedded anywhere the user requires.

3. Accessibility. Users access data from heterogeneous data sources. OLAP must be able to adapt accordingly.

4. Consistent reporting performance. If performance decreases when model<sup>r</sup>data size increases, the user is affected by trying to overcome the performance problem, rather than performing his analysis as intended.

5. Client <sup>r</sup> serÕer architecture. Data is stored in mainframes, so client<sup>r</sup>server is essential. Intelligent servers will allow multiple clients with minimum effort<sup>r</sup>modifications.

6. Generic dimensionality. Dimension-functionality should not be biased towards any dimension.

7. Dynamic sparse matrix handling. OLAP’s physical data schema should adapt to data sparseness and distribution.

8. Multi-user support. OLAP is meant to be a strategic tool, so it must support concurrent user models.

9. Unrestricted cross-dimensional operations. Along consolidation paths, the tool should infer calculations. The tool must not restrict calculations between dimensions.

10. IntuitiÕe data manipulation. Data manipulation should be accomplished by direct action upon cells of the analytical model.

11. Flexible reporting. Data or synthesised information must be presented according to any orientation the user requires.

12. Support for unlimited number of dimensions and aggregation leÕels. In practice, however, most tools support a limited number of dimensions, which, nevertheless, is adequate for most purposes.

## 2.1.1. Other perspectiÕes on OLAP

OLAP, as presented above is a powerful concept. However, its introduction was also accompanied with the evaluation of commercial products to assess whether they were appropriate OLAP tools. As a result, software and consulting added their own ‘rules’, or redefined OLAP’s aim to suit a particular product. For example, the Gartner Group added nine further rules and IRI software added three more rules <sup>w</sup> <sup>x</sup> 4 . One of the most important and most quoted additional rules is ‘incremental database refresh’. This enables the database to be updated only in the area where changes have taken place. A further extension to this efficient processing of data is the intelligent handling of duplicate data as discussed in Ref. 3 . We do not discuss the details for these<sup>w</sup> <sup>x</sup> additional rules or refinements, but we note that OLAP, at an application level, is very much product-specific, and varies from implementation to implementation.

![](/api/attachments/BUGC2BBJ/fulltext/images/1973b0224cafb3c746d19bbda2a0c951fc887e3efc6ca1f6629ce85aa05d8151.jpg)  
Fig. 4. Multidimensional viewing.

![](/api/attachments/BUGC2BBJ/fulltext/images/e541fb4a3c76b87ad8ce0c06cae8005cbec3898b7aa68ac6623397edf0c84593.jpg)  
Fig. 5. Two-dimensional view.

From studying the characteristics of OLAP, one concludes that multidimensional viewing would perform best if the data were stored in MDDBs. MD-DBs have performance advantages when the data is dense. In addition, Codd, when introducing OLAP emphasised the fact that relational systems at that time were inadequate and lacked depth compared to OLAP in terms of analytical functionality. Nevertheless, since the introduction of OLAP, many have argued in favour of relational-OLAP ROLAP , i.e.,Ž . OLAP tools based on relational database technology and this view is supported by vendors of relational database systems e.g., Ref. 27 .Ž <sup>w</sup> <sup>x</sup>.

In practice, ROLAP systems have a relationalbased ADB and use a special software layer for providing multidimensional data viewing MDV ,Ž . incorporating OLAP functionality. OLAP systems that use MDDBs do not use such layers, as the analytic-MDDB provides the multidimensional views by default. Performance differences, advantages or disadvantages are considerable for both OLAP and ROLAP but are beyond the scope of this paper.

Whether the actual data storage is relational or multidimensional is irrelevant for the decision-maker. What the decision-maker needs, and what OLAP must provide, are the following functions 6 : <sup>w</sup> <sup>x</sup>

1. Access to the data in the database management system DBMS . Ž .

2. Data and data consolidation paths or dimensionsŽ . that can be defined according to the user requirements.

3. Accommodation for the variety of ways or different contexts in which the user may wish to view, manipulate and animate the data analyses.

4. Accessibility to these functions via the end-user’s interface.

MDDBs are better suited for OLAP-type applications because of their structure and embedded functionality.

## 2.2. MDV

MDV or data viewing across multiple dimensions, is a key OLAP feature. In general, a ‘dimension’ is a data category e.g., product, district, time . This cate- Ž . gory may have one or more different characteristics which are the ‘dimension values’ e.g., products: A,Ž

![](/api/attachments/BUGC2BBJ/fulltext/images/f7fbbffb687ec218548b40af2c74a2a4d5a5cca120e03f95c8c53d050e0d858b.jpg)  
Fig. 6. Three-dimensional view.

![](/api/attachments/BUGC2BBJ/fulltext/images/126127dc57d7526ce23c4939d8c027b632282a2bd0693d93828e4654505319aa.jpg)  
Fig. 7. A four-dimensional view.

B, and C; district: north, east, west, south; time: 1990–1996 . A data value in a multidimensional. table then reflects a particular business or user perspective e.g., sales for a corresponding combina-Ž . tion of dimension values, or sets of dimension values Že.g., sales for product A, district south, for all years ..

In relational database terminology, dimensions correspond to the ‘attributes’ of a relational table, while the dimension values correspond to the attribute’s ‘domain’ or the set of possible attributeŽ values . The multidimensional data table values cor-. respond to the ‘tuples’ or ‘records’ of a relational table 22,28 . Multidimensional data tables reflect a specific business view or perspective on the data Ž . e.g., sales by region, and product, over time . The benefit is that the data fits the user’s perspective and not vice versa 1,5,6,20,21,37 .<sup>w</sup> <sup>x</sup>

One example to visualise this multidimensional viewing is a spreadsheet. A single spreadsheet is two-dimensional i.e., one dimension being theŽ columns, the other dimension being the rows . A. ‘stack’ of spreadsheets is three-dimensional. This structure is more commonly known as a ‘cube’ or a ‘hypercube’. A stack of cubes viewed along a new dimension is considered four-dimensional. Along a further dimension is five-dimensional, and so on for all dimensions employed in a multidimensional table Ž . Fig. 4 .

For example, suppose a decision analyst wishes to analyze data concerning some ‘products’, over some period of ‘time’, for some ‘salesmen’ for some particular sales ‘sites’. In dimension terms, the data dimensions are product, time, salesman and site. A two-dimensional view of time and product is seen in Fig. 5.

Considering the third dimension e.g., site pro-Ž . duces a ‘stack’ of time–period tables one for each Ž site , as in Fig. 6. .

The addition of another dimension in this case,Ž salesman , along one axis, creates a four-dimensional. view Fig. 7 . It is easy to create a five-dimensionalŽ . view by adding another dimension along another axis. However, it is difficult to visualise more than four dimensions at a time.

It is important to understand that these data-views are user-configurable. Dimensions are not statically set in columns or rows, or along one axis or another. To use the OLAP terminology, the user has the ability to roll-up, drill-down, slice, dice or nest his

![](/api/attachments/BUGC2BBJ/fulltext/images/bf34773a64bf98f269ae15ce6e0ca192c1b1decd980464c022a236d7c3021fed.jpg)  
Fig. 8. Slice.  
Fig. 9. Dice.

Dimension Product: Product A Dimension Time: Years 1 - m

Dimension Salesman: ALL  
Dimension Site: Sites I, II

<table><tr><td rowspan="2">Salesman ALL</td><td colspan="3">Product A</td></tr><tr><td>Year 1</td><td>Year 2</td><td>Year ... m</td></tr><tr><td>Site I</td><td></td><td></td><td></td></tr><tr><td>Site II</td><td></td><td></td><td></td></tr></table>

Fig. 10. Pivoting and nesting.

data. We classify these functions as multidimensional data ‘viewing’ and as multidimensional data ‘manipulation’ functions. The viewing functions then are slice, dice and nest. The manipulation functions are drill-down and roll-up.

Slice is any two-dimensional ‘slice’ of the data. In Fig. 8, the data slice reveals information for site ‘I’, product ‘A’, and year ‘1’, for ‘all’ salesmen. Slice is the ‘dropping’ of the dimension being ‘sliced’.

Dice is the ‘rotation’ of the hypercube to reveal another, different slice of data i.e., the revealing ofŽ data for a different set of dimension values . In Fig.. 9, the new ‘dice’ has dimension site as its most aggregate dimension, products are now in columns, time is in rows, and salesman is ‘Joe’. PiÕot and rotate are identical to dice, and were adopted from spreadsheet terminology. Dice, rotate and pivot are now used synonymously 32 .<sup>w</sup> <sup>x</sup>

Nesting is the ability to ‘nest’ dimensions i.e.,Ž display values from one dimension within another dimension . In Fig. 10, the product dimension is. pivoted to the columns and dimension time is now nested by the dimension product.

Multidimensional viewing is not a new concept, and much of its functionality is already present in spreadsheets and EIS. However, multidimensional viewing has received much attention because of its close relationship with OLAP and its strong direct relationship with databases.

There are two multidimensional data manipulation functions: drill-down and roll-up. Drill-down is the exploration of data to subsequent levels of more detail along a dimension. In Fig. 11, Year ‘1’ has been drilled down to quarters 1, 2, 3 and 4. Roll-up is the aggregation of data to subsequent levels of summary, along a dimension. This implies that dimensions are typically hierarchical in nature based on parent<sup>r</sup>child relationships between dimension values. These relationships are normally data summations, but, in principle, other meaningful operations such as average can also be used. In Fig. 12, the quarters have been rolled up to year. Roll-up, drill-up, consolidate and aggregate are used synonymously in OLAP terminology 32 . <sup>w</sup> <sup>x</sup>

Multidimensional viewing as discussed above has the power to represent multiple conceptual dimensions in a two-dimensional arrangement, as highlighted in Refs. 18,19 . Detailed discussion of OLAP,<sup>w</sup> <sup>x</sup> and multidimensional viewing terms can be found in Refs. 2–6,10,32,38,50 , among others.<sup>w</sup> <sup>x</sup>

Dimension Site: Site /  
Dimension Time: Year 1 → Quarters  
Dimension Product: Products A - n

<table><tr><td colspan="2">Site I</td><td>Product A</td><td>Product B</td><td>Product ... n</td></tr><tr><td rowspan="4">Year 1</td><td>Quarter 1</td><td></td><td></td><td></td></tr><tr><td>Quarter 2</td><td></td><td></td><td></td></tr><tr><td>Quarter 3</td><td></td><td></td><td></td></tr><tr><td>Quarter 4</td><td></td><td></td><td></td></tr></table>

Fig. 11. Drill-down.

<table><tr><td colspan="2">Dimension Site: Site I</td><td colspan="2">Dimension Product: Products A - n</td></tr><tr><td>Site I</td><td>Product A</td><td>Product B</td><td>Product ... n</td></tr><tr><td>Year 1</td><td></td><td></td><td></td></tr></table>

Fig. 12. Roll-up.

## 3. Interaction of data models and DSS models

Data modelling, decision modelling, model investigation, are logical constructs with a vital role in both the Interaction of IS and DT, and in rational decision-making. It is easily seen that data modelling and decision modelling closely interact with each other. The following describes their logical constructs and how they derive knowledge.

1. Data modelling. This is how to extract recorded facts, internal or external, which provide the decision-maker with the facts about the decision problem that he is facing.

2. Decision modelling. This is the creation of a model that represents a simplified representation of a real system. It is used to evaluate possible actions and the probable outcomes of these actions.

3. Model analysis and inÕestigation. As the future is uncertain, ‘what if’-type investigations on data and model parameters assist the decision-maker to prepare for the ‘extreme’ future.

Typically, data modelling involves defining relationships between data items leading to a relational data model, or identifying categories which are then used to define multidimensional tables. The classical decision models are usually linear, non-linear, or discrete optimisation models. However, we consider cluster analysis, forecasting, DM and other analytic models equally appropriate as decision models 36 . <sup>w</sup> <sup>x</sup> A descriptive analysis of the results obtained from the decision model is applied to gain insight, or knowledge in respect of a given decision problem. In particular, a series of ‘ what if’ questions in the analysis phase are used to evaluate the decisionmaker’s understanding of the problem by changing parameters. We view the various software layers and the user interaction as shown in Fig. 13 see alsoŽ Ref. 30 .<sup>w</sup> <sup>x</sup>.

The diagram also highlights the various constituents involved in the overall decision process and their participation at each system level. At the outer level, the decision-maker uses the system to guide him in his decisions. At the inner level, the database and model specialists are responsible for maintaining and developing their appropriate components. This is analogous to the concept of different views put forward by Greenberg and Murphy 13 .

![](/api/attachments/BUGC2BBJ/fulltext/images/2f2ac93a633d84de6585de07ab0b1d562c0e03fa88e28b8fcf00210b2c5cd521.jpg)  
Fig. 13. Implemented software architecture.

![](/api/attachments/BUGC2BBJ/fulltext/images/c6ad4b9886ae306ff5bb8f66ec5d7ddd5620a58ed6a8cff842eaec4213ef432a.jpg)

Table 2  
The modelling dimensions of the decision problem

<table><tr><td>Dimension</td><td>Index</td><td>Description</td></tr><tr><td>Time</td><td>i=1,2</td><td>Denotes the time periods associated with production</td></tr><tr><td>Modes</td><td>j=1,2</td><td>Denotes the production modes</td></tr><tr><td>Products</td><td>k=1,...,K</td><td>Denotes the products</td></tr><tr><td>Machines</td><td>g=1,...,G</td><td>Denotes the machines</td></tr><tr><td>Sales area</td><td>o=1,...,O</td><td>Denotes the sales areas</td></tr><tr><td>Site</td><td>e=1,2</td><td>Denotes the sites</td></tr></table>

## 3.1. An illustratiÕe example

In this section, we illustrate how data modelling and decision modelling interact taking into account a closely related pair of forecasting and LP-optimisation models. Our research group was involved earlier in creating a modelling system, UIMP 9 , in<sup>w</sup> <sup>x</sup> which the multidimensional tables and LP model structures were strongly coupled. We have taken the current example from that earlier paper.

A Company uses three different Machines A, B,Ž C , to produce three products Nuts, Bolts and. Ž Washers in two Production Modes Normal, . Ž Overtime , in two sites InTown, OutOfTown . . Ž . Annual production is split into two periods Ž . Summer, Winter . The final products are distributed to different sales areas North, East, Ž South, West . In order to plan production, the . management uses past sales data to forecast demand. The resulting forecast is used to plan the production schedule for the forthcoming year.

Table 3  
Production times two-dimensional summary representation of a Ž five-dimensional table.  
![](/api/attachments/BUGC2BBJ/fulltext/images/31d108f7dacafb9a4122df4b81627a4dae04d5666697218c9403d9220ed909e9.jpg)

Table 4 Machine availability  
![](/api/attachments/BUGC2BBJ/fulltext/images/05870ecee7816adc85ce8191639b4c0df742afe281b1ee3aed0a899fccd847f5.jpg)

To investigate the decision problem described, we first create a forecasting model that generates data input for our decision model. The decision model in this example is a linear programming-based optimisation model for production planning.

The ‘target knowledge’ from the combination of these two models, is to:

Ž .I Use the forecast as an indication of demand for the generation of an optimum production plan.

Ž . II Identify if the production plan will satisfy our forecasted demand, and to indicate where, how, and by how much, demand is not met.

## 3.2. Data modelling

In our example, the information sets are utilised from the company’s PDB. Items considered in our ADB are:

<sup>Ø</sup> Company structure information: production time-horizon, products, production modes, machines, sites and sales areas.

<sup>Ø</sup> Resources information: production times, machine availability, storage availability, product demand.

<sup>Ø</sup> Financial information: production costs, storage costs, shipment costs and actual sales over the past few years.

<sup>Ø</sup> Decision-making information: level of production, level of storage, level of shipments and demand-shortage level.

Table 5

Storage capacity

Table 6 Demand

<table><tr><td>i</td><td>O</td></tr><tr><td>k</td><td>$ d_{iko} $</td></tr></table>

Table 8 Storage cost

This information is collected from various databases throughout the organisation. For example, storage availability is collected from databases at the warehouse; shipment costs are taken from the distribution<sup>r</sup>dispatch department database, and so on.

The available company information fits naturally in a multidimensional analytic database. As we transfer the above information sets to our analytic database, the company structure information forms the modelling dimensions, or indexes in mathematical terms. These are summarised in Table 2.

The ‘sales area’ dimension is a hierarchical dimension. Its most aggregate level is ‘all areas’, which represents the total for all sales areas; in this case O <sup>s</sup> 1 i.e., roll-up . When investigating indi-Ž . vidual sales area i.e., drill-down ,Ž . O<sup>s</sup>number of sales areas. The use of this dimension and hierarchi-Ž cal dimensions in general will be demonstrated in. detail later.

<table><tr><td></td><td>k</td></tr><tr><td>i</td><td>$ p_{ik} $</td></tr></table>

Once the dimensions are defined, the company resources, financial and decision-making information sets are easily represented in multidimensional tables in the analytic database. The dimensions provide a ‘natural $\mathrm { w a y } ^ { \mathrm { * } }$ to capture the existing real-world information structure within a particular company perspective. The multidimensional tables, which repre sent the resources, financial and decision-making information sets, are described and presented in tabular format. For the detailed datasets, the reader is referred to Appendices A–C. The MDDB used is ORACLE Personal Express Version 5.01, Refs.Ž <sup>w</sup> <sup>x</sup> 33,34 ..

<table><tr><td></td><td>e</td></tr><tr><td>k</td><td>$ s_{ke} $</td></tr></table>

Table 7 Selling price

## 3.2.1. Resources information

Production times $( t _ { i j k g e } ) \colon$ represents the number of hours Ž . Ž . t , needed by machine g to produce a single unit of product Ž . k , in a given production mode Ž . Ž . Ž . Ž . j , at site e , in time period i Table 3 .

Machine aÕailability $( a _ { i j g e } ) \colon$ represents the number of hours machine Ž . Ž . g is available a , in production mode Ž . Ž . Ž . Ž j , at site e , in time period i Table 4 ..

Storage capacity $( h _ { k e } ) \colon$ represents the maximum number of units that can be stored Ž . h , for product Ž . Ž . Ž . k , at site e Table 5 .

Demand $( d _ { i k o } ) \colon$ represents the number of units of product Ž . Ž . Ž . k demanded d , at sales area o , in time period Ž . Ž . i Table 6 .

In the decision models, demand is represented in two data tables with the same structure as the one presented here. The forecast model uses the actual sales observations over i, k, o and the decision model uses the outcome of the forecast i.e., theŽ forecasted demand , also over. i, k, o.

## 3.2.2. Financial information

Selling price $( \boldsymbol { p } _ { i k } )$ Ž . : represents the unit price p of product Ž . Ž . Ž . k , in time period i Table 7 .

Storage cost $( s _ { k e } ) \colon$ represents the unit storage cost Ž . Ž . Ž . Ž .s , for product k , at site e Table 8 .

Production costs $( c _ { i j k g e } ) { : }$ represents the unit production cost Ž . Ž . c , for product k , production mode Ž . Ž . Ž . Ž . j , machine g , at time period i , at site e Ž . Table 9 .

Table 9 Production cost

<table><tr><td colspan="2">i</td></tr><tr><td rowspan="4" colspan="2">j</td></tr><tr></tr><tr></tr><tr></tr></table>

Table 10 Shipment cost

<table><tr><td colspan="2">i</td></tr><tr><td>k</td><td>e</td></tr><tr><td>o</td><td>mikoe</td></tr></table>

Shipment costs $( m _ { i k o e } ) ;$ represents the unit shipping cost Ž . Ž . Ž . m , for product k , from site e to sales area Ž . Ž . Ž . o , in time period i Table 10 .

## 3.2.3. Decision information

These tables store information about our decisions. Initially, these values are unknown but after optimisation they are refreshed with their solution values.

Production $( x _ { i j k g e } ) { : }$ : represents the amount of product Ž . Ž . Ž . k produced x , in production mode j , by machine ${ \bf \Xi } ( { \bf \Lambda } _ { g } )$ Ž . Ž . Ž, at site e , in time period i Table 11 ..

Storage $( y _ { i k e } ) \colon$ represents the amount of product Ž . Ž . Ž . Ž . Ž k stored y , at site e , in time period i Table 12 ..

Shipment $( z _ { i k e o } ) \mathrm { : }$ represents the amount of product Ž . Ž . Ž . Ž . k shipped z , from site e , to sales area o , in time period Ž . Ž . i Table 13 .

Demand shortage $( w _ { i k o } ) \mathrm { : }$ : represents the shortage Ž . Ž . Ž . w of sales area’s o demand not met w , for product Ž . Ž . Ž . k , in time period i Table 14 .

## 3.2.4. The introduction of time

The ease with which the multidimensional data model captures the structure of the real-world data is easily seen. An additional requirement of the ADB and a regular feature of OLAP-based databases, is the capturing of the time dimension. In most MD-DBs, time is a ‘built-in’, fully customisable i.e.,Ž definition of ‘customised time periods’ is possible ,.

Table 11 Production

<table><tr><td colspan="2">i</td></tr><tr><td colspan="2">j</td></tr><tr><td>k</td><td>e</td></tr><tr><td>g</td><td> $x_{ijkge}$ </td></tr></table>

Table 12 Storage

<table><tr><td>i</td><td>e</td></tr><tr><td>k</td><td>$ y_{ike} $</td></tr></table>

hierarchical dimension e.g., year, quarter, month, Ž week, day ..

In our example, we use the dimension ‘year’ to represent the years 1993 to 1999. For each year, we have information split into two seasons summer Ž <sup>r</sup> winter . Thus, a hierarchical type dimension . year:time is adequate for representing our information. We, however, have combined the dimensions ‘year’ and ‘time’ to create a ‘conjoint dimension’ which is particularly efficient for managing sparse data. This is advantageous when a given year in ourŽ example does not have data for a particular season. thus avoiding inefficient data storage in such a situation. Obviously, our data is not sparse, and using a conjoint dimension provides no efficiency advantage, but this does demonstrate the ability of MDDBs to provide customized dimensions. Thus, the elements of observed demand can be found as an entry in the form $d _ { ( \mathrm { y e a r } , i ) k o }$ where year,Ž .i is an access index for the conjoint dimension. For simplicity and clearer explanation of the mathematical models, we refer back to the notation $d _ { i k o }$ where i represents the time dimension.

ObserÕed demand $( d _ { i k o } ) \colon$ represents the amount of product k sold in i in sales area o. The multidi-Ž mensional table for forecasted demand is of identical structure but holds values only when a forecast is produced. The database names for observed demand and forecasted demand are OLD.DEMAND and FCST.DEMAND, respectively. Table 15. Ž .

The incorporation of time is not only important for our decision problem example, but also an essential element of most organizational decision problems. It is therefore beneficial to have the ability to capture the time dimension with relative ease, as is the case for the multidimensional data model and OLAP-based databases.

Table 13 Shipment

<table><tr><td colspan="2">i</td></tr><tr><td>k</td><td>o</td></tr><tr><td>e</td><td>$ z_{ikeo} $</td></tr></table>

Table 14 Demand shortage

<table><tr><td>i</td><td>O</td></tr><tr><td>k</td><td> $w_{iko}$ </td></tr></table>

## 3.2.5. Example of OLAP features

Having captured the data in an analytic database, the data items can be investigated using OLAP functionality which provides valuable insight into company information. For example, the table observed demand, can provide information concerning the product sales figures for each year in either summary or detailed form see Fig. 14 . The actual data tables Ž . are shown in Fig. 15.

In this case, the roll-up function is the summation over the index $\cdot _ { o } ,$ . Index $\cdot _ { o ^ { \prime } } ,$ is the new aggregated index with the value ‘all areas’ instead of ‘north, . . . , west’. Other functions such as the average of all the dimension values over the dimension index can also be used. For instance, an ‘averaging’ roll-up has been used for our cost data. Using the slice feature, the demand for a product k, at sales area southŽ . $o = O$ , in season i, is obtained by slicing the demand table Fig. 16 . Ž .

Slicing involves ‘fixing’ a given dimension and looking at the reduced subset of data table entries where the dimensionality of a table is reduced by one. If applied progressively, we reach individual table entries where the dimensions i, k, o are fixed $( \mathrm { i } . { \bf e } . , d _ { I K O } )$

## 3.3. Decision modelling

The real world structure of the data is easily transferred to the model structure. As mentioned in the Section 3.2, in order to plan for production, demand is forecasted using historic sales data and the resulting forecast is used in creating a future production schedule. Thus, two models are implemented: a forecasting model for estimating future demand, and an LP-optimisation model for solving the production planning problem. Both these models employ the historical demand data as well as the structure of the data as presented in multidimensional tables.

Table 15 Observed demand

<table><tr><td>i</td><td>k</td></tr><tr><td>o</td><td>$ d_{iko} $</td></tr></table>

![](/api/attachments/BUGC2BBJ/fulltext/images/d9d82ccf0eda5dbbb9a1768f3dfdf109e61f7de86c5c23617001fbeb989389d9.jpg)  
Fig. 14. The demand table in drill-down and roll-up modes.

## 3.3.1. The forecasting model

Our choice of a forecast model is based on the assumption that the sales data exhibits both a seasonal and a linear trend. Winter’s method of forecasting 48,49 was chosen as an appropriate model. The <sup>w</sup> <sup>x</sup> general model is shown below.

The forecast y developed at time t for a period T time units into the future is given by:

$$
y _ {t + T} = \left(a _ {t} + b _ {t} T\right) F ^ {*}\tag{1}
$$

where $a _ { t }$ is the estimate of the current intercept between the trend line and the slope, and is given by:

$$
a _ {t} = \alpha \left(\frac {x _ {t}}{F _ {t - N ^ {\prime}}}\right) + (1 - \alpha) \left(a _ {t - 1} + b _ {t - 1}\right),\tag{2}
$$

$b _ { t }$ is the estimate of the slope of the trend line:

$$
b _ {t} = \beta (a _ {t} - a _ {t - 1}) + (1 - \beta) b _ {t - 1}\tag{3}
$$

$F _ { t }$ is the estimate of the multiplicative seasonal factor:

$$
F _ {t} = \sigma \left(\frac {x _ {t}}{a _ {t}}\right) + (1 - \sigma) F _ {t - N ^ {\prime}}\tag{4}
$$

$x _ { t }$ is the actual observation at time t, $N ^ { \prime }$ is the number of observations comprising the periodicity of the data, $F _ { t - N ^ { \prime } }$ is the estimate of the seasonal factor $N ^ { \prime }$ periods in the past, $F ^ { * }$ denotes our best estimate of the seasonal factor in period $t + T$ and , , are exponential smoothing constants, where $0 < \alpha$ $\beta , \ \sigma < 1$

Note that Eqs. 2 – 4 are utilised prior to theŽ . Ž . actual forecast equation Eq. 1 . The periodicity of Ž Ž ..

![](/api/attachments/BUGC2BBJ/fulltext/images/4334778d47075a6140ebdbf10071daacf2734c359f8d825f0fe5a50162c0e6e4.jpg)  
Fig. 15. The observed demand data table in roll-up and drill-down modes.Ž .

the data $N ^ { \prime }$ in our model is two time periods, and the forecast is for $T = 2$ time periods into the future.

In this forecasting model, we have used the notation $y _ { t }$ for demand in order to present the relationship in a clear and simple form. In the analytic database, however, the demand quantities are forecast and stored in categorized form using the symbol $d _ { i k o }$ . We therefore use $y _ { t }$ as an alias for $d _ { i k o }$ and, similarly, $x _ { t }$ is an alias for observeddemand $i k o ^ { \star }$ Thus, ${ \boldsymbol { y } } _ { t } \equiv { \boldsymbol { d } } _ { i k o }$ and $x _ { t } \equiv \mathrm { o b s e r v e d d e m a n d } _ { i k o }$ , that is actual sales.

Most established MDDBs include built-in forecasting tools, as indeed does Personal Express. For details of the implementation of this model and its output, the reader is referred to Appendices A–C. Once the forecast results are obtained, they are stored in the database as a demand table. The LP-optimisation model then accesses data items in this table.

## 3.3.2. The decision model: LP-optimisation

Having obtained an estimate for the forthcoming year’s demand, an LP production planning model is formulated, which when solved, provides values for our decision variables, that is, a production schedule for the forthcoming year.

This model is implemented using the beta test software DOME 30 . In brief, DOME uses a MDDB<sup>w</sup> <sup>x</sup> Ž . Personal Express in order to formulate a structured LP in the MPL language 25 . Further details of the <sup>w</sup> <sup>x</sup> DOME formulation can be found in the work of Mousavi et al. 30 , while the resulting MPL code is<sup>w</sup> <sup>x</sup> set out in Appendices A–C.

<table><tr><td colspan="2">3.3.3. Model definitionsIndices (dimensions)</td></tr><tr><td> $i = 1,2$ </td><td>Denotes different time periods</td></tr><tr><td> $j = 1,2$ </td><td>Denotes different production modes</td></tr><tr><td> $k = 1,\dots,K$ </td><td>Denotes different products</td></tr><tr><td> $g = 1,\dots,G$ </td><td>Denotes different machines</td></tr><tr><td> $o = 1,\dots,O$ </td><td>Denotes different sales areas</td></tr><tr><td> $e = 1,2$ </td><td>Denotes different sites</td></tr><tr><td colspan="2">Data</td></tr><tr><td> $t_{ijkge}$ </td><td>The amount of time to produce one unit of  $k$  at site  $e$ , on machine  $l$ , in mode  $j$ , in time period  $i$ </td></tr><tr><td> $a_{ijge}$ </td><td>The amount of time available on machine  $g$ , at site  $e$ , in time period  $i$ , and mode of production  $j$ </td></tr></table>

![](/api/attachments/BUGC2BBJ/fulltext/images/24d449c9377e02cef4c43df946562b9f7e6d1bcebda944e1eb9a3d45485b1574.jpg)  
Fig. 16. A slice of the demand table.

<table><tr><td> $p_{ik}$ </td><td>Unit selling price of product  $k$ , in time period  $i$ </td></tr><tr><td> $d_{iko}$ </td><td>(Forecasted) demand for product  $k$ , at sales area  $o$ , in time period  $i$ </td></tr><tr><td> $s_{ke}$ </td><td>Unit storage cost of product  $k$ , at site  $e$ </td></tr><tr><td> $h_{ke}$ </td><td>Storage capacity of product  $k$ , at site  $e$ </td></tr><tr><td> $c_{ijkge}$ </td><td>Unit production cost in time period  $i$ , for product  $k$ , in production mode  $j$ , for machine  $g$ , at production site  $e$ </td></tr><tr><td> $m_{ikoe}$ </td><td>Unit shipment cost in time period  $i$ , for product  $k$ , from site  $e$ , to sales area  $o$ </td></tr></table>

## Decision Õariables

$x _ { i j k g e }$ Amount of product k produced in time period i, in production mode j, by machine g, at site e $y _ { i k e }$ Amount of product k stored in time period i, at site e $z _ { i k e o }$ Amount of product k sent from production site e, to sales area o, in time period i $w _ { i k o }$ Amount of sales area’s o demand, for product k, not met in time period i.

## 3.3.4. Model

3.3.4.1. ObjectiÕe function.

Maximise profit

$$
\begin{array}{r l} & \sum_ {i} \sum_ {k} \sum_ {o} \sum_ {e} p _ {i k} z _ {i k e o} \\ & - \sum_ {i} \sum_ {j} \sum_ {k} \sum_ {g} \sum_ {e} c _ {i j k g e} x _ {i j k g e} \\ & \sum_ {i} \sum_ {k} \sum_ {o} \sum_ {e} m _ {i k e o} z _ {i k e o} \\ & - \sum_ {i} \sum_ {k} \sum_ {e} s _ {k e} y _ {i k e} - 1 5 \sum_ {i k o} w _ {i k o} \end{array}
$$

where 15 is the unit cost for not meeting demand.

Machine availability:

$$
\sum_ {k} t _ {i j k g e} x _ {i j k g e} \leq a _ {i j g e} \quad \forall i, j, g, e.
$$

Inventory balance:

$$
\sum_ {j} \sum_ {g} x _ {i j k g e} - y _ {i k e} - \sum_ {o} z _ {i k e o} = 0 \quad \forall k, e; i = 1
$$

$$
\sum_ {j} \sum_ {g} x _ {2 j k g e} + y _ {1 k e} - y _ {2 k e} - \sum_ {o} z _ {2 k e o} = 0
$$

$$
\forall k, e; i = 2;
$$

Demand:

$$
\sum_ {e} z _ {i k e o} + w _ {i k o} \geq d _ {i k o} \quad \forall i, k, o.
$$

Storage:

$$
y _ {i k e} \leq h _ {k e} \quad \forall i, k, e.
$$

$$
x _ {i j k g e}, y _ {i k e}, z _ {i k e o} \geq 0 \quad \forall i, j, k, g, e, o.
$$

## 3.4. Model analysis and inÕestigation: exploiting OLAP features

We discuss three investigations that are based on applying the OLAP features to the model data. First, we instantiate different model inputs by using a top-level dimension, ‘case’. Second, we achieve a varying level of detail in the application of the models by using a hierarchical dimension. Third, by using the slice functionality, we have the ability to investigate sub-problems by instantiating the appropriate subsets of data. Because of the natural coupling between the model structure and the data structure, each of these three investigations is a result of direct manipulation of the database; the models are not altered in any way for any of these investigations.

## 3.4.1. Scenario inÕestigations

It is well known in the decision support community that a decision-maker or problem owner investigates future uncertainties by performing one, or more, of ‘what $\mathrm { i f 2 } ^ { \cdot }$ queries. A series of such models are variously known as ‘cases’ or scenarios. It has been suggested, by a number of investigators 46 , that <sup>w</sup> <sup>x</sup> ‘case’ should be considered an additional dimension in the model data tables and the solution tables. Although this expands the volume of information, OLAP-enabled tools make it possible to display this information in graphical form, and therefore help the problem owner in analysing the results. Note, however, that the models must be solved for the corresponding number of cases before the built-in ‘what if?’ functionality of an MDDB can be used.

![](/api/attachments/BUGC2BBJ/fulltext/images/f51912935200d7a99d9e15f736f0219c2842c71ca00f13241a2e3851c52150ef.jpg)  
Fig. 17. Forecast demand for each of the three scenarios roll-up .Ž .

The multidimensional data model naturally provides a ‘what if’ dimension, often referred to as ‘case’ or ‘scenario’. This enables version control as illustrated by Ramirez et al. 40 . This ‘case’ dimen-<sup>w</sup> <sup>x</sup> sion is best used as the leading dimension. As the top-level dimension, it then ‘drives’ the lower-level dimensions and the data models can handle ‘what if investigations naturally, without the need for special software functionality.

Different scenarios are represented in the data structures and the resulting model instances, by the ‘case’ dimension. Each value of the ‘case’ dimension represents a different data scenario. For illustration purposes, we have considered three different cases for the purpose of forecasting demand: optimistic, average and pessimistic Fig. 17 . For each case, we Ž . change the forecast parameters as appropriate. The corresponding forecast outputs for each case are presented in Appendices A–C. Similarly, changes in resources can be considered as different cases in the production-planning model. Although this is not illustrated here, the same principle applies.

## 3.4.2. Granularity, aggregation–disaggregation

Roll-up and drill-down reflect the ‘granularity’ of the data the decision-maker wishes to view or investigate. By coupling the data to the model, we can create instances of aggregated and disaggregated models Fig. 18 . The results output of the aggre-Ž . Ž . gated and disaggregated models can be supplied side by side with the aggregated and disaggregated data Ž . input . This functionality brings a number of benefits to the problem owner.

When constructing large-scale models analysts tend to work with less detail ‘Ž . coarse grain model’ in order to investigate the model behaviour and gain confidence in the model. This is also the case when investigating the feasibility of new policies. After model confidence is gained, the analysts then use progressively more and more detail ‘Ž fine grain model’ in order to gain insight into the problem and. assist the decision-makers to make more informed decisions. Indeed our results indicate that changing the model ‘grain’ by varying level of detail in the data does produce results that are very useful in the context we just described, as shown in Fig. 20 Žresults for the other two cases are in Appendices A–C . This indicates that the aggregated models can. be used as good approximations to the detailed models.

![](/api/attachments/BUGC2BBJ/fulltext/images/d06922ddbf9d927fb7c0488a3979554295b37be2470b3ec09b84bb71bf6c0fef.jpg)  
Fig. 18. The level of data detail drives the level of the model detail.

In the detailed mode drill-down over sales areas ,Ž . all three different demand cases are computed by taking into consideration each individual sales area. In summary form roll-up over sales areas , theŽ . forecast cases are the aggregation of demand for all the sales areas. The aggregated forecast and the detailed forecast are independent of each other, hence, on creating summary reports of the detailed model, these are not necessary the same as the results found in the aggregated model Fig. 19 . Ž .

In our example, consider the various managers within a company. The higher level management require the summary forecast, as an indication of how the company is going to perform in the immediate future, or to examine the feasibility of a new policy. The distribution managers, however, are more likely to be interested in the detailed forecast, in order to estimate the workload of their department. In both cases the same computer model formulation, and data are used, while OLAP ensures the appropriate level of detail is accessed. Rogers et al. 43<sup>w</sup> <sup>x</sup> consider another obvious reason for model aggregation, which is to reduce the ‘computational burden’ of solving the model.

## 3.4.3. Slice and sub-problems

The use of the ‘slice’ feature is useful when the problem owner requires sub-problem investigation. Consider a multi-national company for the purposes of our example. We could then use an additional dimension to represent the different countries where our company has production and distribution facilities. Slicing the country dimension for a particular nation results in creating a sub-problem for that particular division of the company.

Often, models are broken down into sub-problems Ž . ‘selectiÕe grain models’ in order to investigate the behaviour of specific levels of detail or summary within the problem e.g., for a single product in allŽ outlets . Similar work has been popular in the past .

![](/api/attachments/BUGC2BBJ/fulltext/images/7d2a6e3c7f426d2e01efcfb77a6d573dbd1657b5e9a7fa0ddc7bf3ff97350c27.jpg)  
Fig. 19. Expected case: roll-up and drill-down forecasts.

![](/api/attachments/BUGC2BBJ/fulltext/images/4eb8eabf1f6d37ef993cfc3f1a22bd1ba87330fcca0bf4caf3e39866ef1036e7.jpg)  
Fig. 20. Results from the aggregated and detail model.

especially with oil companies. PLATOFORM is an example of an earlier generation, sophisticated system with analogous functionality 35 . We have not<sup>w</sup> <sup>x</sup> explicitly shown how the slice feature can be used as a means of creating sub-problems, but the reader can easily visualise the procedure.

## 4. Summary and conclusions

In this paper we have first analysed different aspects and the emerging concept of IS which are used to capture and represent ‘organisational knowledge’. We have analysed data warehousing and its relation to OLTP Databases. We have presented OLAP and multidimensional viewing and we have also considered the relative positioning of a number of interrelated tools such as Middleware and DM.

Our real interest is, however, to position decision modelling and illustrate its interaction with IS. We show how OLAP-enabled databases can be adapted to support symbolic modelling and used in the context of the IVC, and how modelling contributes towards acquiring corporate knowledge.

Thus, we have highlighted the strong coupling that exists between structure within organisational data and the structure of the symbolic models which are used in decision-making. In particular, we have shown that the drill-down and roll-up concepts introduced by commercial information specialists can be naturally extended through aggregation and disaggregation into the domain of decision models.

The work of Mohring et al. 29 highlights the ¨ <sup>w</sup> <sup>x</sup> contribution from MS and IS are equally important in the creation of DSS. We have also put special emphasis in bringing together these two different worlds of specialisation. Namely the information systems designer, and the model-based management science specialist. In the context of organisational decision-making, these groups have important contributions to make. We believe in our work, we have shown how the specialisation of these groups can be brought together to create valuable decision support tools.

## Appendix A. Role of different constituents

Database specialist: the person responsible for implementing and structuring the analytic database. Liaises with the model specialist to make sure the structure in the data is consistent with the structure of the decision model.

Model specialist: the person s responsible for the Ž . creating the models used in the decision process Ž . e.g., forecasting, LP . Liaises with the database specialist to ensure that the structure in the decision model is consistent with that of the database model.

Decision-maker: the person who owns the decision problem and communicates his requirements to the model specialist and the database specialist. He also participates in defining the investigative steps and uses the results of the system to guide him in his decision-making.

## Appendix B. Glossary of terms

ADB or analytical database. A database that has special features that make it suitable for use for decision-making purposes. A distinct characteristic of the ADB is its incorporation of time within its data structure s . The ADB gets its data from theŽ . transaction database.

Analytic tools. By analytic tools, we refer to the models, or techniques available to the decisionmaker. These models or techniques are useful for the decision process, and include optimisation models or DM techniques.

EIS or executiÕe information systems. IS built to suit the particular requirements of top corporate management. Main subjects of IS research and applications in the 1980s, and were characterised by their intuitive graphical-based interface, and their fast response times for ‘ad-hoc’ type queries, and ‘what if analyses. Roll-up and drill-down functionality was also considered an essential EIS feature.

OLAP or on-line analytical processing. A term coined by Codd, to represent the latest generation of EIS or decision support-based information systems. Closely coupled with a multidimensional data-viewing interface, OLAP is characterised by powerful data browsing functionality, and the ability to create and animate analytic data models.

ROLAP or relational on-line analytical processing. A reaction to the assumption that OLAP is only possible via the use of MDDBs. Essentially OLAP with a relational database.

MDDB or multidimensional database. MDDBs Ž . commonly mentioned in conjunction with OLAP store data along multiple dimensions. Dimensions are consolidation or aggregation paths that ‘fit’ the user-analyst’s perspective of the data. MDDBs do not need to be normalised for storage efficiency as is the case with relational databases. When MDDBs are coupled with an OLAP interface, they prove useful in performing multidimensional analyses 1,20,37 .<sup>w</sup> <sup>x</sup> This coupling of OLAP and MDDBs is becoming the de facto standard for analytical databases.

Data mining. See knowledge discovery databases.

Data warehouse. Commercial term for denoting the ADB. Indicates the central storage or ‘warehousing’ of data, so that it can be used for a variety of purposes including decision-making and KDD investigations. Data stored in a data warehouse, and therefore the ADB is assumed to be ‘cleansed’ of various inconsistency errors, such as misspellings, missing values, etc.

Data mart. Originally used as a synonym for the data warehouse. Data marts actually represent a collection of data that is a subset of the data stored in a data warehouse. Data marts tend to be application or department oriented.

MDV or multidimensional data Õiewing. The term we use to denote the ability to view, use and manipulate data sources in a multidimensional way. MDV can be used independently of the data store, and whether it is a MDDB or a specially configured relational database.

Middleware. Rock-Evans 42 characterises Mid-<sup>w</sup> <sup>x</sup> dleware as an ‘‘off the shelf connectivity software which: supports distributed data processing and is used by developers to build distributed applications.’ Overall, Middleware applications can be classified into one or more of these groups: translational e.g., Ž between applications , managerial e.g., for certain. Ž tasks such as security, delivery, timing , a means of. communication e.g., between different network pro-Ž tocols, etc. and a transport provision e.g., routing a. Ž process through a network, hiding physical details from user . For example, the connectivity between a . database, spreadsheet, e-mail, desktop publishing, and the operating system software is handled by Middleware software, whether the applications are in the same environment, or distributed across a network. Such Middleware examples include open data base connectivity—ODBC, or object-linking and embedding—OLE.

Management science MS( )<sup>r</sup>operational research ( ) OR models. MS<sup>r</sup>OR models include optimisation, decision analysis and simulation, among others ŽMitra, 1988; Ref. 23 . These models have a strong<sup>w</sup> <sup>x</sup>. mathematical component, are often used in a corporate context, and provide valuable insight to the decision-maker for various decision problems such as production planning, resource allocation, timetabling, crew scheduling and manpower planning. Such models are usually large, because of their scale of implementation. Most of the research issues in these areas focus on model formulation and especially algorithmic solver capability.

KDD<sup>r</sup> DM tools. KDD or DM tools is used to identify hidden or previously unknown relationships between corporate data. This is a generic name given to otherwise a diverse set of ‘software’ techniques such as chi-square tests statistics , neural nets, ge-Ž . netic algorithms, data analysis through visualisation, rule induction and intelligent text search.

## Appendix C. Illustrative tables of data instance, and aggregated and disaggregated results

C.1. Data instance

C.1.1. Database structure See Fig. 21.

C.1.2. Data tables

The tables that are not affected by the different case dimension values are shown only once Fig. Ž 22 ..

The demand table is first populated by the forecast and then used in the LP Figs. 23–29 .Ž .

For the ‘shipment cost’ table below, the ‘AL-LAREAS’ values show the aÕerage transportation costs from production site e to all sales areas o ŽFig. 30 ..

## C.2. Results data tables

In this section, we present a selection of LP-optimisation results for each case. These results demonstrate the close performance between the summary and detailed representations of our production-planning model. Variables with 0 zero values afterŽ . optimisation are not presented. For a detailed list of data tables, database automation routines and model implementation Forecast and LP , see Ref. 24 .Ž .

C.2.1. Expected case See Fig. 31.

C.2.2. Optimistic case See Fig. 32.

C.2.3. Pessimistic case See Fig. 33.

C.3. Models and OLAP automation routines

C.3.1. Forecast model: express code

Personal express commands and keywords are shown in CAPITALS.

![](/api/attachments/BUGC2BBJ/fulltext/images/ebae9e7b811815dafba96a99170dc89e249b7d95c6a67d42d85c7195e325eb12.jpg)  
Fig. 21. The contents of the database.

![](/api/attachments/BUGC2BBJ/fulltext/images/27fcf6e22ee57c291d170ed33ad0fa8daac611e5240d2a2d5cb68b2f8f034ac8.jpg)  
Fig. 22. The forecasted demand table DEMAND .Ž . Ž .

C.3.1.1. Listing 1. Program for forecasting demand. DEFINE DEMAND.PROGRAM PROGRAM PROGRAM "Program for Forecasting demand for two-time periods

![](/api/attachments/BUGC2BBJ/fulltext/images/deda9c21a468525d46d294244631ba768f5ccb2a0a945cf9724429f091d7e418.jpg)  
Fig. 23. The storage costs table COSTOR .Ž .

"alpha–beta–gamma are selected according to the status "of the case dimension "Temporary variable declaration VARIABLE product TEXT VARIABLE area TEXT OKFORLIMIT<sup>s</sup>YES FOR k o DO "Perform the forecast product<sup>s</sup>k area<sup>s</sup>o LIMIT i.year TO FIRST 8 "Setting of the forecast base data

![](/api/attachments/BUGC2BBJ/fulltext/images/b9fe3637198aa55504b8691e7c8057ef44121d441ed02568afe050e9fff9c29d.jpg)  
Fig. 24. Old demand past sales figures .Ž .

LIMIT k TO product LIMIT o TO area "Determine what is the case dimension value "then do the appropriate forecast SWITCH VALUES case STATUSŽ . DO

![](/api/attachments/BUGC2BBJ/fulltext/images/34d0cf7710fa0e1862e7281ea15b4a77ec07fba22d1b981e1eb7250843c3a1fc.jpg)  
Fig. 25. Selling prices PRICE . Ž .

CASE ‘OPTIMISTIC’: FORECAST LENGTH 2 METHOD WINTERS PERIODICITY 2 - ALPHA 0.1 BETA 0.1 GAMMA 0.1 - TIME i.year FCNAME fcst.demand old.demand

![](/api/attachments/BUGC2BBJ/fulltext/images/9f58aac45a45c2ccd78a1e54e2ac10e62a30ea4d3e3382fee82ccdcfc12bd265.jpg)  
Fig. 26. Storage capacity table STORCAP . Ž .

![](/api/attachments/BUGC2BBJ/fulltext/images/be1e5cd6a53017991c98c5583de5e7f03dd4f2e623270d7f7975b0a2e901fb58.jpg)  
Fig. 27. Production costs table PRODCOST .Ž .

![](/api/attachments/BUGC2BBJ/fulltext/images/bf711335e35fb51f31cfef504d8f58abcc7e2fe89940d442fc674c30e4eb5a87.jpg)  
Fig. 28. Machine availability table TIMEAVL . Ž .

<table><tr><td colspan="3">CASE: CASE1I: SUMMERJ: NORMALK: NUTS</td><td colspan="3">CASE: CASE1I: SUMMERJ: NORMALK: BOLTS</td><td colspan="3">CASE: CASE1I: SUMMERJ: NORMALK: WASHERS</td></tr><tr><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td></tr><tr><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td></tr><tr><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td></tr><tr><td>A</td><td>4.00</td><td>5.00</td><td>A</td><td>5.00</td><td>6.00</td><td>A</td><td>5.00</td><td>6.00</td></tr><tr><td>B</td><td>7.00</td><td>8.00</td><td>B</td><td>6.00</td><td>7.00</td><td>B</td><td>6.00</td><td>7.00</td></tr><tr><td>C</td><td>3.00</td><td>4.00</td><td>C</td><td>0.00</td><td>0.00</td><td>C</td><td>0.00</td><td>0.00</td></tr><tr><td colspan="3">CASE: CASE1I: SUMMERJ: OVERTIMEK: NUTS</td><td colspan="3">CASE: CASE1I: SUMMERJ: OVERTIMEK: BOLTS</td><td colspan="3">CASE: CASE1I: SUMMERJ: OVERTIMEK: WASHERS</td></tr><tr><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td></tr><tr><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td></tr><tr><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td></tr><tr><td>A</td><td>3.00</td><td>4.00</td><td>A</td><td>4.00</td><td>5.00</td><td>A</td><td>5.00</td><td>5.00</td></tr><tr><td>B</td><td>6.00</td><td>7.00</td><td>B</td><td>5.00</td><td>6.00</td><td>B</td><td>5.00</td><td>6.00</td></tr><tr><td>C</td><td>2.00</td><td>3.00</td><td>C</td><td>0.00</td><td>0.00</td><td>C</td><td>0.00</td><td>0.00</td></tr><tr><td colspan="3">CASE: CASE1I: WINTERJ: NORMALK: NUTS</td><td colspan="3">CASE: CASE1I: WINTERJ: NORMALK: BOLTS</td><td colspan="3">CASE: CASE1I: WINTERJ: NORMALK: WASHERS</td></tr><tr><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td></tr><tr><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td></tr><tr><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td></tr><tr><td>A</td><td>5.00</td><td>5.00</td><td>A</td><td>6.00</td><td>5.00</td><td>A</td><td>7.00</td><td>6.00</td></tr><tr><td>B</td><td>8.00</td><td>6.00</td><td>B</td><td>7.00</td><td>6.00</td><td>B</td><td>7.00</td><td>6.00</td></tr><tr><td>C</td><td>4.00</td><td>0.00</td><td>C</td><td>0.00</td><td>0.00</td><td>C</td><td>0.00</td><td>0.00</td></tr><tr><td colspan="3">CASE: CASE1I: WINTERJ: OVERTIMEK: NUTS</td><td colspan="3">CASE: CASE1I: WINTERJ: OVERTIMEK: BOLTS</td><td colspan="3">CASE: CASE1I: WINTERJ: OVERTIMEK: WASHERS</td></tr><tr><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td><td></td><td colspan="2">----TIMEUS----</td></tr><tr><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td><td></td><td colspan="2">----E----</td></tr><tr><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td><td>G</td><td>IN_TOWN</td><td>OUT_OF_TOWN</td></tr><tr><td>A</td><td>4.00</td><td>3.00</td><td>A</td><td>5.00</td><td>4.00</td><td>A</td><td>5.00</td><td>5.00</td></tr><tr><td>B</td><td>7.00</td><td>6.00</td><td>B</td><td>6.00</td><td>5.00</td><td>B</td><td>6.00</td><td>5.00</td></tr><tr><td>C</td><td>3.00</td><td>2.00</td><td>C</td><td>0.00</td><td>0.00</td><td>C</td><td>0.00</td><td>0.00</td></tr></table>

Fig. 29. Production times table TIMEUS .Ž .

## BREAK

CASE ‘EXPECTED’:

TIME i.year FCNAME fcst.demand old.demand BREAK CASE ‘PESSIMISTIC’: FORECAST LENGTH 2 METHOD WINTERS PERIODICITY 2 - ALPHA 0.9 BETA 0.9 GAMMA 0.9 -

TIME i.year FCNAME fcst.demand old.demand BREAK DOEND LIMIT k TO ALL LIMIT o TO ALL

LIMIT i.year TO ALL DOEND "Use only the forecasted values LIMIT i.year TO year ‘1997’ "Copy the values to the Demand table for the LP. demandŽ . Ž i summer <sup>s</sup>fcst.demand i.year <sup>-</sup> summer ‘1997’<sup>)</sup>. demandŽ . Ž i winter <sup>s</sup> fcst.demand i.year <sup>-</sup> winter ‘1997’<sup>)</sup>. LIMIT i.year TO ALL

## C.3.2. Other personal express automation programs

C.3.2.1. Listing 2. Program for preparing the database in roll-up mode.

"Program for setting the appropriate dimensions

" and calling the forecast-average programs

" in ROLL-UP mode

![](/api/attachments/BUGC2BBJ/fulltext/images/cae849473bbfcfb05232f71caa00ba0880a63ca4e71483d53049f4581f3708fd.jpg)  
Fig. 30. Shipment costs table TRANCST .Ž .

![](/api/attachments/BUGC2BBJ/fulltext/images/4c2242b195b038c868489416f88c1ebbb9b2c4ea83036d1d5a94dfb82cfc989b.jpg)  
Fig. 31. Selected optimisation results from roll-up and drill-down modes for the expected case.

![](/api/attachments/BUGC2BBJ/fulltext/images/1907f375f5ce4b8d0cf25de64881f3ef8e604fba9c8adfa6373e7eac8f108657.jpg)  
Fig. 32. Selected optimisation results from roll-up and drill-down modes for the optimistic case.

"Calculate the sum of the past demands ROLLUP old.demand OVER o USING o.total

```txt
"then use only the ALLAREAS value
LIMIT o TO allareas
"do the forecast
demand.program
```

"average the transportation costs areas.program

"undo any ’limit’ commands from the programs LIMIT o TO allareas

## C.3.2.2. Listing 3. Program for preparing the database in drill-down mode.

"Program for setting the status of the appropriate "dimensions, and calling the forecasting program in

"Use the areas without the total LIMIT o to first 4

"Calculate the totals for each area, so user " can see total if needed ROLLUP fcst.demand OVER o USING o.total

"undo any ’limit’ commands for areas LIMIT o TO FIRST 4

## C.3.2.3. Listing 4. Program for adding another sea( - son, year) Õalue to the conjoint dimension.

"Program for adding new dimension valuesŽ . " for the conjoint dimension i.year

```txt
OKFORLIMIT = yes
FOR year i
DO
IF ISVALUE (i.year, <i year>)
THEN GOTO end
ELSE maintain i.year add <i year>
end:
DOEND
```

![](/api/attachments/BUGC2BBJ/fulltext/images/821c5a578308140c31d5ff1f2ac346cd7fb39b050d55ca42080c27bec4cf5b57.jpg)  
Fig. 33. Selected optimisation results from roll-up and drill-down modes for the pessimistic case.

C.3.2.4. Listing 5. Program for calculating the aÕerage of transportation costs when the Sales areas are in roll-up mode.

"Program for computing the average of

" the transportation costs

```python
"Use the areas, but not their total
limit o to first 4
    "for all other dimensions
    for ki e
    do
    "calculate the average cost and store it in
    allareas
    trancst(o allareas) = average(trancst e)
    doend
"Restore dimension status
limit o to all
```

## C.3.3. LP-optimisation model: MPL code TITLE nutsbolts

```txt
INDEX
    i = INDEXFILE(Time.DAT)
    j = INDEXFILE(Modes.DAT)
    k = INDEXFILE(Products.DAT)
    g = INDEXFILE(Machine.DAT)
    o = INDEXFILE(Outlet.DAT)
    e = INDEXFILE(Site.DAT)

DATA
    TimeUs[i,j,k,g,e] := SPARSEFILE("TimeUs.dat")
    {Time Usage}

    TimeAvl[i,j,g,e] := SPARSEFILE("TimeAvl.dat")
    {Time Available}
```

```txt
Shortage[i,k,o] EXPORT to Sparsefile("Shortage.dat")
{Shortage variable}
```

```txt
costor[k,e]:= SPARSEFILE("costor.dat")
{Storage Cost}
```

```lisp
trancst[i,k,o,e]:= SPARSEFILE
("trancst.dat")
{Shipping Cost}
```

```txt
EXPORT to Sparsefile("Produce.dat")
{Production at site}
```

```txt
Store[i,k,e] EXPORT to Sparsefile("Store.dat")
{Storage at site}
```

```txt
Ship[i,k,e,o] EXPORT to Sparsefile ("Ship.dat")
{Shipment}
```

```txt
MODEL
MAX Profit = Sum(i,k,o,e:Price[i,k] * Ship[i,k,e,o]) - Sum(i,j,k,g,e:ProdCost * Produce[i,j,k,g,e]) - Sum(i,k,o,e:trancst * Ship[i,k,e,o]) - Sum(i,k,e:costor * Store[i,k,e]) - Sum(i,k,o:15 * Shortage[i,k,o])
```

## SUBJECT TO

```prolog
TimeCon[i,j,g,e] EXPORT Slack ShadowPrice RHSValue To SparseFile("TimeCon.dat"):
{time Availability Constraint}

Sum(k:TimeUs[i,j,k,g,e]*Produce[i,j,k,g,e])
<= TimeAvl;
StockB1[i,k,e] Where i = 1 EXPORT Slack ShadowPrice RHSValue To
SparseFile("StockB1.dat"):
{Stock balance Equation tp = 1}

Sum(j,g:1 * Produce[i := 1,j,k,g,e]) - 1 * Store [i := 1,k,e] - Sum(o:1 * Ship[i := 1,k,e,o]) = 0;
StockB2[i,k,e] Where i = 2 EXPORT Slack ShadowPrice RHSValue To
SparseFile("StockB2.dat"):
{Stock Balance Equation tp = 2}

Sum(j,g:1 * Produce[i := 2,j,k,g]) + 1 * Store [i := 1,k] - 1 * Store[i := 2,k,e] - Sum(o:1 * Ship[i := 2,k,e,o]) = 0;
demship[i,k,o] EXPORT Slack ShadowPrice RHSValue To SparseFile("demship.dat"):
{Demand Shipping constraint}

Sum(e:1 * Ship[i,k,e,o]) + 1 * Shortage[i,k,o] >= demand;

BOUNDS
    Store[i,k,e] <= StorCap;
END
```

## References

<sup>w</sup> <sup>x</sup> 1 Arbor Software, Multidimensional Analysis: Converting Corporate Data Into Strategic Information, Arbor Software, 1993.

<sup>w</sup> <sup>x</sup> 2 Arbor Software, Relational OLAP: Expectations and Reality, Arbor Software, 1995.

<sup>w</sup> <sup>x</sup> 3 A. Berson, S.J. Smith, Data Warehousing, Data Mining, and OLAP, McGraw-Hill, 1997.

<sup>w</sup> <sup>x</sup> 4 F.A. Buytendjik, OLAP: Playing for Keeps, http:<sup>rr</sup> www.xs4all.nl<sup>r ;</sup>fab<sup>r</sup>olapkeep.html, July 1995.

<sup>w</sup> <sup>x</sup> 5 E.F. Codd, S.B Codd, C.T. Salley, Providing On-Line Analytical Processing to User–Analysts: An IT Mandate, E.F. Codd and Associates, 1993.

<sup>w</sup> <sup>x</sup> 6 E.F. Codd, S.B. Codd, OLAP with TM<sup>r</sup>1, E.F. Codd and Associates, 1994.

<sup>w</sup> <sup>x</sup> 7 M. Demarest, Building the Data Mart, DBMS, July 1994.

<sup>w</sup> <sup>x</sup> 8 K.M. Decker, S. Focardi, Technology Overview: A Report

on Data Mining, CSCS TR-95-02, Swiss Scientific Computing Center, May 29, 1995.

<sup>w</sup> <sup>x</sup> 9 E.F.D. Ellison, G. Mitra, UIMP: user interface for mathematical programming, ACM Transactions on Mathematical Software 8 3 1982 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 S. Filbin, Successful decision support in the retail sector, in: Proceedings of ‘EIS AND OLAP’, UNICOM Seminars, London, July 1995.

<sup>w</sup> <sup>x</sup> 11 R. Finkelstein, Understanding the need for on-line analytical servers, Arbor Software, 1994.

<sup>w</sup> <sup>x</sup> 12 A.M. Geoffrion, An introduction to structured modelling, Management Science 33 5 1987 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 H.J. Greenberg, F.H. Murphy, Views of mathematical programming models and their instances, Decision Support Systems 13 1 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 C.W. Holsapple, A.B. Whinston, The environmental approach to decision support, in: G. Mitra Ed. , MathematicalŽ . Models for Decision Support, NATO ASI Series, Vol. F48, Springer-Verlag, 1988.

<sup>w</sup> <sup>x</sup> 15 M. Holsheimer, A.P.J.M. Siebes, Data mining: the search for knowledge in databases, CS-R9406 1994, Computer Science<sup>r</sup>Department of Algorithmics and Architecture, Centrum voor Wiskunde en Informatica CWI , 1994.Ž .

<sup>w</sup> <sup>x</sup> 16 W.H. Inmon, What is a Data Warehouse?, http:<sup>rr</sup>www.cait. wustl.edu<sup>r</sup>cait<sup>r</sup>papers<sup>r</sup>prism<sup>r</sup>vol1\_no1<sup>r</sup>, 1995.

<sup>w</sup> <sup>x</sup> 17 W.H. Inmon, J.D. Welch, K.L. Glassey, Managing the Data Warehouse, Wiley, 1997.

<sup>w</sup> <sup>x</sup> 18 C. Jones, Visualization and Optimization, Kluwer Academic Publishers, 1997.

<sup>w</sup> <sup>x</sup> 19 C. Jones, Visualization and Optimization, http:<sup>rr</sup>www. chesapeake2.com<sup>r</sup>cvj<sup>r</sup>itorms, html version of Ref. 17 .<sup>w</sup> <sup>x</sup>

<sup>w</sup> <sup>x</sup> 20 Kenan Technologies, Multidimensional Database Technology and Data Warehousing, Kenan Systems, 1995.

<sup>w</sup> <sup>x</sup> 21 Kenan Technologies, An Introduction to Multidimensiona Database Technology, Kenan Systems, 1995.

<sup>w</sup> <sup>x</sup> 22 R. Kimball, The Data Warehouse Toolkit, Wiley, 1996.

<sup>w</sup> <sup>x</sup> 23 N.-S. Koutsoukis, G. Mitra, S.A. Moody, Information systems in support of decision making, Technical Report TR<sup>r</sup>01<sup>r</sup>96, Brunel University, Department of Mathematics and Statistics, UK, January 1996.

<sup>w</sup> <sup>x</sup> 24 N.-S. Koutsoukis, G. Mitra, C. Lucas, Adapting on-line analytical processing OLAP for decision modelling: theŽ . interaction of information and decision technologies, Technical Report TR<sup>r</sup>14<sup>r</sup>97, Brunel University, Department of Mathematics and Statistics, UK, Revised February 1998.

<sup>w</sup> <sup>x</sup> 25 Maximal Software, MPL Modelling System: Release 4.0, Maximal Software 1996.

<sup>w</sup> <sup>x</sup> 26 S. McLean, B. Scotney, The data mining report, Information Technology Report, UNICOM Seminars, 1996.

<sup>w</sup> <sup>x</sup> 27 MicroStrategy, The Case for Relational OLAP, Microstrategy, 1995.

<sup>w</sup> <sup>x</sup> 28 G. Mitra, C. Lucas, S.A. Moody, B. Kristjansson, Sets and indices in linear programming and their integration with relational data models, Computational Optimization and Applications 4 1995 263–283. Ž .

<sup>w</sup> <sup>x</sup> 29 R.H. Mohring, R. Muller, F.J. Radermacher, Advanced DSS¨ ¨ for scheduling: software engineering aspects and the role of

eigenmodels, in: Proceedings of the 27th Hawaii International Conference on System Sciences, Wailea, HI, IEEE Computer Society, January 4–7, 1994.

<sup>w</sup> <sup>x</sup> 30 H. Mousavi, G. Mitra, C. Lucas, Data and optimization modelling: a tool for elicitation and browsing DOME , in:Ž . R.S. Barr, R.V. Helgasm, J.L. Kennington Eds. , InterfacesŽ . in Computer Science and Operations Research: Advances in Metaheuristics, Optimization and Stochastic Modelling Technologies, Kluwer Academic Publishers, 1996, pp. 297–324.

<sup>w</sup> <sup>x</sup> 31 J. O’Brien, Management Information Systems: Managing Technology in the Networked Enterprise, 3rd edn., IRWIN 1996.

<sup>w</sup> <sup>x</sup> 32 OLAP Council, OLAP Glossary, http:<sup>rr</sup>www. olapcouncil.org<sup>r</sup>research<sup>r</sup>glossaryly.htm, OLAP Council 1995.

<sup>w</sup> <sup>x</sup> 33 ORACLE, Personal Express User’s Guide, ORACLE 1996.

<sup>w</sup> <sup>x</sup> 34 ORACLE, Express Language Reference, Vols. I and II, ORACLE 1996.

<sup>w</sup> <sup>x</sup> 35 K.H. Palmer, N.K. Boudwin, H.A. Patton, A.J. Rowland, J.D. Sammes, D.M. Smith, A Model Management Framework for Mathematical Programming, An EXXON Monograph, Wiley, 1984.

<sup>w</sup> <sup>x</sup> 36 G. Piatetsky-Shapiro, W.J. Frawley Eds. , Knowledge Dis- Ž . covery in Databases, AAAI Press<sup>r</sup>MIT Press, 1991.

<sup>w</sup> <sup>x</sup> 37 Pilot Software, An Introduction to OLAP: An Explanation of Multidimensional Terminology and Technology, Pilot Software, 1995.

<sup>w</sup> <sup>x</sup> 38 N. Pendse, R.C. Creeth, The OLAP report, Business Intelligence, 1995.

<sup>w</sup> <sup>x</sup> 39 S. Raghunathan, A structured modelling methodology to design decision support systems, Decision Support Systems 17 4 1996 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 40 R.G. Ramirez, U.R. Kulkarni, K.A. Moser, Derived data for decision support systems, Decision Support Systems 17 2Ž . Ž . 1996 .

41 Red Brick, The Data Warehouse: Competitive Advantage for the 90s, Red Brick Systems, July 27, 1994.

<sup>w</sup> <sup>x</sup> 42 R. Rock-Evans, Middleware: tools and cross-platform integration, in: Proceedings of Data Mining and Data Warehouse ’96, UNICOM Seminars, London, November 1996.

<sup>w</sup> <sup>x</sup> 43 D.F. Rogers, R.D. Plante, R.T. Wong, J.R. Evans, Aggregation and disaggregation techniques and methodology in optimisation, Operations Research 39 4 1991 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 44 T. Sach, I. Collins, J. Page, The data warehouse report, Information Technology Report, UNICOM Seminars, 1996.

<sup>w</sup> <sup>x</sup> 45 V. Sauter, Decision Support Systems: An Applied Managerial Approach, Wiley, 1997.

<sup>w</sup> <sup>x</sup> 46 S.L. Savage, Fast QM: Fundamental Analytic Spreadsheet Tools for Quantitative Management, McGraw-Hill, 1993.

<sup>w</sup> <sup>x</sup> 47 J.F. Shapiro, The decision database, Working Paper, Sloan WPa3570-93-MSA, June 1993.

<sup>w</sup> <sup>x</sup> 48 W.G. Sullivan, W. Claycombe, Fundamentals of Forecasting, Reston Publishing, 1977.

<sup>w</sup> <sup>x</sup> 49 N.T. Thomopoulos, Applied Forecasting Methods, Prentice-Hall, 1980.

<sup>w</sup> <sup>x</sup> 50 E. Thomsen, OLAP Solutions: Building Multidimensional Information Systems, Wiley, 1997.

![](/api/attachments/BUGC2BBJ/fulltext/images/d59df297b1c44cfea4813d6c6b366f252440a55502f340a1446b93c7c542b24d.jpg)

Dr. Nikitas-Spiros Koutsoukis has a first class honours BSc in accounting from the Technological Education Institute in Messologhi in Greece, and a Masters degree in Decision Modelling and Information Systems, from the Department of Mathematics and Statistics at Brunel University where he completed his Ph.D. Research. Dr. Koutsoukis lectures on the MSc course in Data and Information Modelling, and is mainly interested in Information Systems IS and modelsŽ .

![](/api/attachments/BUGC2BBJ/fulltext/images/d990471d9219bb2e365f925dec44481c1d57dd5913d41079264d486f046af050.jpg)

Dr. Cormac Lucas obtained his BSc and PhD at Brunel University. He is a lecturer in Operational Research and Statistics in the Department of Mathematics and Statistics at Brunel University and he is member of the Brunel Computational Optimisation and Modelling Research Group. His research interests cover the development of integrated software systems for modelling of Linear Programming and Integer Programming Application. He is currently in-

for Decision Support DS . In particular his research investiga-Ž . tions cover the interaction between IS and DS tools. He is also investigating the application of Agent Technologies and Multi-Agent architectures applied to EIS<sup>r</sup>OLAP and enterprise information systems.

![](/api/attachments/BUGC2BBJ/fulltext/images/2ae52075ece7ba5c2772339ebf959203473f240d14edf962766735fad62d83d0.jpg)

Professor Gautam Mitra has a first degree BEE from Jadavpur University, Calcutta, and MS and a PhD from London University. He is the head of the department of Mathematics at Brunel University and leads a research group in the area of Computational Optimisation and Modelling. Professor Mitra’s research interests cover a wide field including Linear Programming, Integer Programming, solution algorithms and software systems for serial as well as

parallel computers. He is also interested in the issues of modelling and knowledge representation in general and in particular that of interaction between IS, modelling and solution technologies. Professor Mitra has written over 80 journal articles and one book and has edited five other books. He is a fellow of the IMA and BCS and is member of INFROMS, USA, ORSOC, GB and the MP Society International.

volved on a number of industrial research projects that combine IS with DS. He is also interested in modelling and solving of Stochastic Programming problems and their use in DS and IS.
