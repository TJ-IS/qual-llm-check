---
otero_id: 1870
otero_key: "BHJ2GHDN"
title: "Database structure for a class of multi-period mathematical programming models"
authors: "Goutam Dutta; Robert Fourer"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.02.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Database structure for a class of multi-period mathematical programming models

Goutam Dutta <sup>a,</sup>⁎, Robert Fourer <sup>b</sup>

<sup>a</sup> Indian Institute of Management, Ahmedabad, Vastrapur, Ahmedabad 380015, India

<sup>b</sup> Department of Industrial Engineering and Management Sciences, Northwestern University, Evanston, IL 60208, USA

## a r t i c l e i n f o

Article history: Received 14 March 2007 Received in revised form 9 December 2007 Accepted 27 February 2008 Available online 12 March 2008

Keywords: Decision support system Process industries Optimization Strategic and operational planning

## a b s t r a c t

We describe how a generic multi-period optimization-based decision support system can be used for strategic and operational planning in a company whose processes can be described in terms of <sup>fi</sup>ve fundamental elements: Materials, Facilities, Activities, Times and Storage-Areas. We discuss the issues of interface design, data reporting and updating, and optimal production and pro<sup>fi</sup>t planning. We also compare the performances of two different types of database structures with respect to optimization.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

This work started as a project to design an optimizationbased decision support system (DSS) for strategic planning for steel companies in North America. As the project was supported by the AISI (American Iron and Steel Institute), the DSS was generic in concept, but capable of being speci<sup>fi</sup>cally applied to any particular company's facilities by supplying appropriate data, discussed in detail by Fourer [12]. Complete data for a steelmaking operation, including values such as yields, capacities, and prices indexed over products and processes could be conveniently supplied in the form of relational database <sup>fi</sup>les. The optimization was taken to be over a single planning period, however, and thus dif<sup>fi</sup>culties involving the indexing of data and model entities over time were not addressed.

This paper extends the work of Fourer [12] to a multiperiod case. We adopt the fundamental elements of Materials, Facilities, and Activities from the previous work, but add two more elements — Times and Storage-Areas. Among the major points we address are the following:

1. What are the key features of a multi-period DSS?

2. What are the dif<sup>fi</sup>culties in implementing a multi-period DSS?

3. Why is an update mode dif<sup>fi</sup>cult in a multi-period database?

4. In what ways can the optimal result be represented in a multi-period DSS?

5. What are the alternatives for handling multi-period indexing in a database context?

6. How do alternative data structures compare with respect to data storage, data retrieval, and support for optimization models?

## 1.1. Review of related research

The work on computer based modeling environments was initially started by a conceptual paper by Geoffrion [13]. A decision support system in a distribution planning context was described by Geoffrion [14]. Database representation of a Linear Program (LP) is one of the eight approaches of LP representation [17] by Murphy et al. The approach is considered as translation form, as it is used as a bridge between

modelers' form, and algorithmic form. A study by Fourer [11] suggests that no single form of LP representation, which can be easily understood by modelers', computers, and industry practitioners simultaneously, can be developed. The database representation of LP was initially discussed by Fourer [12] in 1997. Most of the industry data remains in database systems; one needs to look for a system which can handle the bulk data required for an LP in a systematic manner. Readers interested in database systems, and data modeling in the context of mathematical programming may refer to a study by Dominguez [5] and Date [2]. We recognize that not much work may be evident in representing an LP in translation form in general and in database form in particular. In this paper, we demonstrate (using an LP model for strategic planning in process industry), how an LP can be represented in the form of a database structure. We follow the widely accepted framework for data, model, and dialogue management provided in two studies by Dolk [3] and [4]. A similar framework for modeling languages was provided by Fourer [11]. A survey of applications of mathematical programming models in integrated steel plants has been discussed in [7]. Readers are referred to [15,18–20] for recent applications on implementation of model-based work and decision support systems. Implementation of this work with real data from a steel company is discussed in [6] and [8]. Similar implementation with real data from a pharmaceutical company in India is discussed in [9].

## 1.2. Outline

In Section 2 of this paper, we discuss the design issues raised by a multi-period database. We introduce different elements of the DSS and discuss possible implementations. We also consider the correspondence of the <sup>fi</sup>les in the DSS with variables in the linear program. In Section 3, we discuss the steps of multi-period optimization — constraint and variable generation, coef<sup>fi</sup>cient matrix generation, solution of the optimization problem, and reading of the optimal values back into the database. From Sections 4–7, we answer different questions that are raised in the introduction. Section 4 considers how the various features of the DSS can be useful for the strategic planning in a process industry. In Section 5, we discuss the dif<sup>fi</sup>culties in implementing the multi-period database. In this section, we also discuss alternative ways of handling multi-period indexing in databases. In Section 6, we outline the various features for reporting and updating of the data for multi-period models. In Section 7, we compare two different variations of the database design — one primarily hierarchical and another primarily relational — with respect to optimization. We conclude the paper by outlining the scope for further work in Section 8.

![](/api/attachments/BHJ2GHDN/fulltext/images/35238365e209582ebfac14b1316ac8421756ce503e31edf12f8aac0026c4c756.jpg)  
Fig. 1. Database structure for STEEL-TIME.

## 2. Database design for multi-period models

Our generic multi-period planning model has, as previously noted, <sup>fi</sup>ve fundamental elements:

Times are the periods of the planning horizon, represented by discrete numbers (1, 2, 3…). They can be as short as weeks, though for a planning model they are most likely to range from months to years.

Materials are the physical items that <sup>fi</sup>gure in some stage of production. They may be inputs, intermediates, or outputs, and sometimes more than one of these.

Facilities are collections of machines that produce some materials from others. For example, a Hot Mill that produces sheets from slabs is a facility.

Activities are productive transformations of materials. Each facility houses one or more activity, which uses and produces materials in certain proportions. Production of hot metal, production of billets, pickling, and galvanizing are examples of steelmaking activities.

Storage\_Areas are <sup>fi</sup>elds or warehouses where raw materials, intermediate products, or <sup>fi</sup>nished products may be stored.

An algebraic formulation for the multi-period model is given in Appendix 1.

## 2.1. The times file

Our database is implemented within 4th Dimension, a relational database management system, developed by Adams and Beckett [1]. Other database systems such as Access or Oracle could be used just as well. Fig. 1 summarizes the structure of the database as expressed within 4th Dimension. The <sup>fi</sup>ve boxes labeled Materials, Facilities, Activities, Times, and Storage-Areas correspond to the <sup>fi</sup>ve major elements, or <sup>fi</sup>les, of the database. Items within each box denote the <sup>fi</sup>le's data <sup>fi</sup>elds and sub-<sup>fi</sup>les, with the sub-<sup>fi</sup>le entries distinguished by a light-shaded line that runs to the top of a separate box in which the sub-<sup>fi</sup>le data <sup>fi</sup>elds are listed. The smaller, independent database structure in the upper right of the diagram holds a generated linear program as described at the end of this section. We use 4th Dimension's notations for <sup>fi</sup>les, sub-<sup>fi</sup>les, and <sup>fi</sup>eld. Further details can be found in the earlier discussion of the singleperiod model by Fourer [11].

<table><tr><td>MAT-TAG</td><td>MATERIALS</td><td>UNITS</td><td>MATERIAL TYPE</td></tr><tr><td>101</td><td>CC BILLET</td><td>TONS</td><td>Intermediate</td></tr><tr><td>102</td><td>SINTER</td><td>TONS</td><td>Input</td></tr><tr><td>105</td><td>SLAG</td><td>TONS</td><td>Intermediate</td></tr><tr><td>106</td><td>HOT METAL</td><td>TONS</td><td>Intermediate</td></tr><tr><td>110</td><td>ORE</td><td>TONS</td><td>Input</td></tr><tr><td>201</td><td>COAL</td><td>TONS</td><td>Input</td></tr><tr><td>213</td><td>COKE</td><td>TONS</td><td>Intermediate</td></tr><tr><td>401</td><td>NEW MAT</td><td>TONS</td><td>Input</td></tr><tr><td>402</td><td>CRUDE STEEL</td><td>TONS</td><td>Input</td></tr><tr><td>501</td><td>STEEL FOR CC</td><td>TONS</td><td>Intermediate</td></tr><tr><td>503</td><td>HEAVY MELTING SCRAP</td><td>TONS</td><td>Intermediate</td></tr><tr><td>504</td><td>MILL SCRAP</td><td>TONS</td><td>Intermediate</td></tr><tr><td>601</td><td>BILLET</td><td>TONS</td><td>Intermediate</td></tr><tr><td colspan="4">Add Entry Done</td></tr></table>

Fig. 2. Output layout of Materials <sup>fi</sup>le.

![](/api/attachments/BHJ2GHDN/fulltext/images/9f7b28696659a9b01e4037b87e7551c2342d4ec6d36e99042343b2e93b906e9a.jpg)  
Fig. 3. Input layout of Materials <sup>fi</sup>le.

The structure of the [Times] <sup>fi</sup>le in the database is very simple, consisting basically of a record per period. A name <sup>fi</sup>eld can be adjusted according to whether the periods are modeling, say, quarters or years. The complications introduced by the multi-period structure lie mainly in the ways that [Times] <sup>fi</sup>le interact with all of the other pieces of the database structure.

## 2.2. Materials file

The Materials data (Figs. 2 and 3) are stored in a hierarchical way. In Table 1, we show the one-to-one correspondence between the parameters of the LP model and the <sup>fi</sup>elds in the [Materials] <sup>fi</sup>le. In this <sup>fi</sup>le the material name ([Materials]MatName) and material identi<sup>fi</sup>cation string ([Materials]MatTag) are unique. [Materials]MatTag is required for data entry in the sub-<sup>fi</sup>les of the [Materials] <sup>fi</sup>le.

## 2.3. Facilities file

In the [Facilities] <sup>fi</sup>le (Figs. 4 and 5), for time-dependent parameters we retain a structure similar to that of the [Materials] <sup>fi</sup>le. In Table 2, we show the one-to-one correspondence between the parameters of the LP model and the <sup>fi</sup>elds [Facilities] <sup>fi</sup>le. We de<sup>fi</sup>ne [Facilities]FacTime as a sub-<sup>fi</sup>le where [Facilities]FacTime'CapMin, [Facilities]FacTime'Cap-Max, and [Facilities]FacTime'CapDual are the time-dependent maximum, and minimum of the optimum production level of the facility , and the time-dependent dual value of the facility capacity. The [Facilities]FacTime'Vendor\_Cost is the cost of vendoring (outsourcing) an additional unit capacity of the facility at that time.

There are two indexed sub-<sup>fi</sup>elds in [Facility]Inputs, which is a sub-<sup>fi</sup>le of the [Facilities] <sup>fi</sup>le. The <sup>fi</sup>rst one is the input material, which is related to the [Materials] <sup>fi</sup>le. The other is [Facility]Inputs'InTime which is the time-dependent <sup>fi</sup>eld of the [Facilities]Input File and is related to the [Times] <sup>fi</sup>le. The sub-<sup>fi</sup>le [Facilities]Outputs is entirely analogous.

## 2.4. Activities file

[Activities] is de<sup>fi</sup>ned as a separate <sup>fi</sup>le. (In STEEL-TIME2, we consider [Activities] as a sub-<sup>fi</sup>le of the [Facilities] <sup>fi</sup>le). There is a <sup>fi</sup>eld of [Activities]ActTime which is the indexed <sup>fi</sup>eld of time in the [Activities] <sup>fi</sup>le and related to the [Times] <sup>fi</sup>le. In each [Activities] <sup>fi</sup>le there is a <sup>fi</sup>eld, ActFacName that speci<sup>fi</sup>es which facility it belongs to. This is required so that the user can search for the activity through the facility. The other important <sup>fi</sup>eld is ActTag, the unique identi<sup>fi</sup>cation of each activity. The [Activities] <sup>fi</sup>le can be indexed over [Activities]Act Name or [Activities]ActTag (identi<sup>fi</sup>cation string). Two activities may have the same ActName (like PRODUCTION OF BILLET), but if they have a different ActTime, they will have a different ActTag. In other words every record of [Activities] <sup>fi</sup>le will be identi<sup>fi</sup>ed by a unique [Activities] Act Tag. The storage-Areas <sup>fi</sup>le is mapped accordingly.

Correspondence of [Materials] File and the LP model

<table><tr><td>Sr. no.</td><td>Parameter of the LP</td><td>Fields of the tables of the database</td></tr><tr><td>1</td><td> $i_{jt}^{buy}$ </td><td>[Materials]MatTime&#x27;BuyMin</td></tr><tr><td>2</td><td> $u_{jt}^{buy}$ </td><td>[Materials]MatTime&#x27;BuyMax</td></tr><tr><td>3</td><td> $c_{jt}^{buy}$ </td><td>[Materials]MatTime&#x27;BuyPrice</td></tr><tr><td>4</td><td> $i_{jt}^{sell}$ </td><td>[Materials]MatTime&#x27;SellMin</td></tr><tr><td>5</td><td> $u_{jt}^{sell}$ </td><td>[Materials]MatTime&#x27;SellMax</td></tr><tr><td>6</td><td> $c_{jt}^{sell}$ </td><td>[Materials]MatTime&#x27;SellPrice</td></tr><tr><td>7</td><td> $i_{jt}^{inv}$ </td><td>[Materials]MatTime&#x27;InvMin</td></tr><tr><td>8</td><td> $u_{jt}^{inv}$ </td><td>[Materials]MatTime&#x27;InvMax</td></tr><tr><td>9</td><td> $h_{jt}$ </td><td>[Materials]Mattime&#x27;MatInvCost</td></tr><tr><td>10</td><td> $x_{jo}^{inv}$ </td><td>[Materials]MatInvZero</td></tr></table>

![](/api/attachments/BHJ2GHDN/fulltext/images/6066ffb230fb055a782a2c029a3dfb1eb1d4c97446ea6ce7464c78e6c676904b.jpg)  
Fig. 4. Input layout of Facilities <sup>fi</sup>le

## 2.5. Storage-Areas file

The structure of the [Storage-Areas] <sup>fi</sup>le is similar to that of the [Activities] <sup>fi</sup>le. [Storage-Areas]StoreTag is the <sup>fi</sup>eld which uniquely identi<sup>fi</sup>es the records of the <sup>fi</sup>le. In the [Storage-Areas] <sup>fi</sup>le, we have a sub-<sup>fi</sup>eld called [Storage-Areas]StoreMatlist which lists all the materials that can be stored.

## 2.6. Variables and Constraints file

In the [Variables] <sup>fi</sup>le we have the <sup>fi</sup>elds — Number, Type (Material Bought, Material Sold, Material Inventoried, Activity at Facility), Identi<sup>fi</sup>cation Number 1 (ID1), Identi<sup>fi</sup>cation Number 2 (ID2), Objective, Upper bound and Lower bound as in the single-period model. However, we have also an Identi<sup>fi</sup>cation Number 3 (ID3) <sup>fi</sup>eld which indicates the time of the variable. [Variables]Optimal refers to the most recent optimal value of the variable. The variables <sup>fi</sup>le has a sub-<sup>fi</sup>le known as [Variables]Coeffs which has a sub-<sup>fi</sup>eld called [Variables]Coeffs'Constr and this constraint is related to the [Constraints]Number of the [Constraints] <sup>fi</sup>le. Constraints <sup>fi</sup>le is designed in a similar pattern as of [Variables] <sup>fi</sup>les.

<table><tr><td>FACILITY NAME</td><td>FAC TAG</td><td>FAC TYPE</td><td>CAPACITY UNITS</td></tr><tr><td>BLAST FURNACE</td><td>0001</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>COKE OVENS</td><td>0002</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>BASIC OXYGEN FURNACE</td><td>0003</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>CONTINUOUS CASTER</td><td>0004</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>ROLLING MILL NO. 1</td><td>0005</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>MERCHANT MILL NO. 1</td><td>0006</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td>S.B.B. MILL 1</td><td>0007</td><td>PRODUCT-MIX</td><td>TONS</td></tr><tr><td colspan="4">Add Entry Done</td></tr></table>

Fig. 5. Output layout of Facilities <sup>fi</sup>le.

Table 2  
Correspondence of [Facilities] <sup>fi</sup>le and the LP model

<table><tr><td>Serial Number</td><td>Parameter of the LP</td><td>Fields of the tables of the database</td></tr><tr><td>1</td><td> $l_{ijt}^{in}$ </td><td>[Facilities]Inputs&#x27;InMin</td></tr><tr><td>2</td><td> $u_{ijt}^{in}$ </td><td>[Facilities]Inputs&#x27;InMax</td></tr><tr><td>3</td><td> $l_{ijt}^{out}$ </td><td>[Facilities]Outputs&#x27;OutMin</td></tr><tr><td>4</td><td> $u_{ijt}^{out}$ </td><td>[Facilities]Outputs&#x27;OutMax</td></tr><tr><td>5</td><td> $c_{it}^{vend}$ </td><td>[Facilities]FacTime&#x27;Vendor_Cost</td></tr><tr><td>6</td><td> $l_{it}^{cap}$ </td><td>[Facilities]FacTime&#x27;CapMin</td></tr><tr><td>7</td><td> $u_{it}^{cap}$ </td><td>[Facilities]FacTime&#x27;CapMax</td></tr></table>

## 3. Optimization

Once the data of the <sup>fi</sup>ve database <sup>fi</sup>les and their respective sub-<sup>fi</sup>les are entered by the user, these are validated by a set of diagnostic tests to be explained in later sections. This section describes how the subsequent optimization process is carried out. The principal steps (Fig. 6) are as follows:

1. The data describing the production scenario at different time periods are collected and stored in the database.

2. The constraints associated with the linear program are generated.

3. The variables of the associated linear program are determined, along with their coef<sup>fi</sup>cients in the constraints.

4. The [Constraints] and [Variables] <sup>fi</sup>les are scanned and all the essential information about the linear program is written to an ordinary text <sup>fi</sup>le in a compact format. This text <sup>fi</sup>le is the input <sup>fi</sup>le to our solver.

5. A linear programming solver reads the text <sup>fi</sup>le — we used XMP, by Martsen [16] — which solves the indicated linear program and then writes the optimal values of the variables to a second text <sup>fi</sup>le.

6. The second text <sup>fi</sup>le is read and the optimal values are placed in appropriate <sup>fi</sup>elds of the [Materials], [Facilities], [Activities], and [Storage-Areas] <sup>fi</sup>les and their sub-<sup>fi</sup>les.

## 4. Features of the DSS

In this section we discuss various features of this DSS. We discuss how generic the DSS is with respect to several process industries and how generic it is with respect to multiple operating systems. Then we discuss to what extent it addresses strategic planning issues. We also discuss features of user friendliness, and handling of infeasibility in this DSS.

## 4.1. Generic

The model is suf<sup>fi</sup>ciently generic so that it can be used by many process industries that transform materials in different facilities. We started our work with an integrated steel company in the USA. The implementation of this work in the steel company is discussed in [12]. We have also extended the work to a Pharmaceutical company [9]. Work is now going on with real data from Polymer, Aluminum and Zinc companies in India, through which we propose to demonstrate that the model is generic and can be applied to several process industries.

## 4.2. Flexibility and operating systems

The materials, facilities, activities and storage areas can be deleted or added, as required, with the click of button. Initially, when this implementation was started, the question was if this DSS could be used in a multiple operating system. The initial development was done by Fourer (discussed in [12]) working in Macintosh. Since further developments in this area are going on in India, where Macintosh is not very popular, we decided to use Windows OS. The present DSS can be run on either Windows or Macintosh.

## 4.3. Strategic planning

In strategic planning, the DSS will be able to answer questions such as:

1. What are the effects of cost or price changes of raw materials and <sup>fi</sup>nished products on the product-mix?

![](/api/attachments/BHJ2GHDN/fulltext/images/98adaca48e40ffa3308a68835570dcc0d5172297feec1533c18c8138742f06f3.jpg)  
Fig. 6. Optimization steps.

2. If the company is planning to diversify into different products, what products should be chosen?

3. Should external scrap be purchased as a substitute for hot metal and at what price?

For example, in the experience with an Indian steel company (Sinha et al. [19], Dutta et al. [10]), the marginal pro<sup>fi</sup>t of an extra megawatt of electrical power was found to be several million dollars. This study justi<sup>fi</sup>ed the investment of installing diesel-generating sets. Similar studies can be done using our DSS.

## 4.4. User friendliness

One of the primary motivations for developing this DSS was to develop a tool where managers could use the software in spite of not having much knowledge of OR/MS. One of the dif<sup>fi</sup>culties is how concepts like marginal price (duals) or reduced cost can be explained. In the [Facilities]Factime sub-<sup>fi</sup>le, there is a sub-<sup>fi</sup>le [Facilities]Factime'Capmax. We have developed a button called sensitivity, which when pressed, will display the statement “Pro<sup>fi</sup>t will increase by \$ 900 for every unit increase of Capacity Maximum”. Similar features are present in other <sup>fi</sup>les as well.

## 4.5. Handling of infeasibility

If we have infeasibility in the “Facility Capacity” constraint, we can generate a “Soft Capacity” variable, which is similar to an arti<sup>fi</sup>cial variable. At the end of step 2 of Section 3 (optimization steps), the user will have the option to use a procedure which generates this variable. The concept of soft capacities is described in detail by Dutta and Fourer [8].

## 5. Dif<sup>fi</sup>culties in implementing multi-period decision support system

When the DSS is implemented in a hierarchical structure, we may <sup>fi</sup>nd that indexing of time-dependent parameters related to the [Materials] <sup>fi</sup>le, can be done either by the index Time or by the index Materials. If we have parameters with three or four indices (one of them being Time), the searching, locating and retrieval of the data from its lowest hierarchy of <sup>fi</sup>les become dif<sup>fi</sup>cult. Suppose we have parameters of four indices namely the activity input rate, which is indexed over facility, material, activity and time. Then, in this case, the data is stored in the sub-<sup>fi</sup>le of the [Activities] <sup>fi</sup>le. For any activity input rate associated with an activity, we need to search the activity in the Activities <sup>fi</sup>le with indices of [Activities] ActName and [Facilities]FacName and the [Times]TimeID, and subsequently look for the materials name in the sub-<sup>fi</sup>le of the activity <sup>fi</sup>le. Similar is the case with the activity output <sup>fi</sup>le and other <sup>fi</sup>les including storage areas <sup>fi</sup>le. As this may require multi searches from multiple <sup>fi</sup>les with different indices, it becomes dif<sup>fi</sup>cult to use sort and search to implement a multi-period DSS with more than two indices.

## 5.1. Difficulty in implementation in update mode

We have been able to demonstrate in [8] and [9] that multi-period, multi-product, multi-facility process industry planning can be done with little or no knowledge of linear programming. All that the user has to do is to click the appropriate buttons to run the required linear programs.

The DSS can be used in three modes: Data, Optimal and Update. In the Data mode, the user enters data in <sup>fi</sup>ve different <sup>fi</sup>les. The Optimal mode is for display of optimal values and dual prices. The DSS takes much longer (9 min) to generate the [Variables] <sup>fi</sup>le and the [Constraints] <sup>fi</sup>le than to solve the problem (less than a minute). If there is no addition or deletion of records in the [Materials], [Facilities] and [Activities] <sup>fi</sup>le, any change in the parameters of these <sup>fi</sup>les can be re<sup>fl</sup>ected in the corresponding changes to the [Variables] and [Constraints] <sup>fi</sup>le (without executing procedures of variable and constraint generation). This is accomplished in the Update mode resulting in the saving of user time.

In Update mode, we update a parameter at two different places. The <sup>fi</sup>rst one is at its speci<sup>fi</sup>c location in the database structure, and the second is at the [Constraints] and [Variables] <sup>fi</sup>le. As described in Section 5.1, retrieval of any data with four indices (one of them being time) is very dif<sup>fi</sup>cult; similar is the case with updating. A data with four indices requires similar processing to locate and update it. One also needs to overcome a similar level of dif<sup>fi</sup>culty in locating the parameter in the [Constraints] and [Variables] <sup>fi</sup>le.

## 5.2. Diagnostics rules and difficulties in implementation

The diagnostic routines are written to ensure that the linear program is complete and free from errors and infeasibilities. We use the various <sup>fi</sup>le procedures, layout procedures and global procedures to implement these routines and the following rules:

Rule 1: For every variable, the upper bound should not be less than the lower bound. For every constraint, the lower right hand side (LoRHS) should not be more than the higher right hand side (HiRHS).

Rule 2: For every pair of one variable and one constraint, there should not be more than one non-zero element.

While the above two diagnostics are easy to understand with respect to optimization-based DSS, the next three rules of diagnostics are important for a multi-period database structure. To implement these rules, we need to perform sort and searches either at the sub-<sup>fi</sup>le level or at the sub-sub-<sup>fi</sup>le level and create buttons, scripts or procedures that execute these searchers.

Rule 3: For every sub-<sup>fi</sup>le indexed over one time sub-<sup>fi</sup>eld, the number of sub-records in the sub-<sup>fi</sup>le should be the same as the number of records in the [Times] <sup>fi</sup>le.

Rule 4: For <sup>fi</sup>les and sub-<sup>fi</sup>les indexed over one time <sup>fi</sup>eld and one non-time <sup>fi</sup>eld, the number of records (or subrecords) should not be more than the product of the number of records (or sub-records) in the [Times] <sup>fi</sup>le and the number of records related to the non-time <sup>fi</sup>eld.

Rule 5: If a record or sub-record is indexed over a time <sup>fi</sup>eld or sub-<sup>fi</sup>eld and one non-time <sup>fi</sup>eld or sub-<sup>fi</sup>eld, there will be only one record or sub-record containing any particular combination of the time <sup>fi</sup>eld and non-time <sup>fi</sup>eld

## 6. Representing optimal results in a multi-period database

In this section, we discuss two different ways in which summaries can be displayed: summaries of each time period separately, and grand summaries for all time periods.

## 6.1. Display of optimal summaries

As the top management of an organization will be interested in knowing the optimal summaries, we represent how the DSS can take care of this. In the case of a multi-period model, creation of summaries is dif<sup>fi</sup>cult and not straightforward like in single-period models.

We repeat the equation of the objective function.

$$
\begin{array}{l} Z (t) = \sum_ {j \in M} c _ {j t} ^ {\text { sell }} x _ {j t} ^ {\text { sell }} - \sum_ {j \in M} c _ {j t} ^ {\text { buy }} x _ {j t} ^ {\text { buy }} - \sum_ {j \in M} c _ {j t} ^ {\text { inv }} x _ {j t} ^ {\text { inv }} \\ \quad - \sum_ {(j, j ^ {\prime}) \in M ^ {\text { conv }}} c _ {j j ^ {\prime} t} ^ {\text { conv }} x _ {j j ^ {\prime} t} ^ {\text { conv }} - \sum_ {(i, k) \in F ^ {\text { act }}} c _ {i k t} ^ {\text { act }} x _ {i k t} ^ {\text { act }} - \sum_ {i \in F} c _ {i t} ^ {\text { cap }} x _ {i t} ^ {\text { cap }} \end{array}\tag{i}
$$

$$
Z = \sum_ {t \in T} (1 + \rho) ^ {- t} Z (t)\tag{ii}
$$

We will now break it up into different parts. Typically a user would like to answer “What is the sum total of revenue obtained by selling all materials at one time (say Time=t)?” Let us de<sup>fi</sup>ne it as $R ( t ) ,$ , the revenue at time t:

$$
R (t) = \sum_ {J \in M} C _ {j t} ^ {\text { sell }} x _ {j t} ^ {\text { sell }}\tag{iii}
$$

Similarly we can write the corresponding summation terms for the other terms. We de<sup>fi</sup>ne

Cp(t) Cost of purchase of all materials at time t

Ca(t) Cost of all activities at time t

Ci(t) Cost of carrying inventory at time t

Cc(t) Cost of conversions at time t

Cv(t) Cost of outsourcing at time t

<table><tr><td colspan="2">Grand Summary</td></tr><tr><td>Revenue from Sales</td><td>2,194,681,608.05</td></tr><tr><td>Cost of Purchases</td><td>1,405,571,480.90</td></tr><tr><td>Cost of Conversions</td><td>7,295,935.95</td></tr><tr><td>Cost of Activities</td><td>11,999,880.00</td></tr><tr><td>Cost of Inventories</td><td>9,019,200.00</td></tr><tr><td>Cost of Outsourcing</td><td>0</td></tr><tr><td></td><td>760,795,111.19</td></tr><tr><td>Net Profit</td><td>OK</td></tr></table>

Fig. 7. Grand summary.

Once we have calculated all the six quantities we can rewrite the net pro<sup>fi</sup>t as the following:

$$
Z (t) = R (t) - \mathrm{Cp} (t) - \mathrm{Ca} (t) - \mathrm{Ci} (t) - \mathrm{Cc} (t) - \mathrm{Cv} (t)\tag{iv}
$$

The terms of equation can be displayed in a grand summary over all time periods (Fig. 7).

In addition, we can display the computed summary at each time period.

## 6.2. Layouts with time as a sub-field

First, let us consider the [Materials] <sup>fi</sup>le. In this <sup>fi</sup>le, no time-dependent parameters are in the <sup>fi</sup>le level except for MatInvZero. These <sup>fi</sup>elds will be the same in Data or Optimal layouts. In order to see the optimal value of the material COIL bought at Time=2, the user has to select the optimal mode in the Examine menu of the main menu and select Materials. Then a list of materials will be displayed. The user then has to select the material COIL and a layout called Materials Optimal will be displayed. In this layout there will be an included layout that lists the data of all time-dependent parameters of the materials COIL. Once the user selects Time=2, a list of parameters is displayed in a layout for Time=2 and one of them is BuyOPT which shows the optimal value of material bought in Time=2. Similarly, if the user wants to get the BuyPrice of material called SCRAP at Time=3, he or she has to go through steps similar to all these.

We now discuss two different types of searches. We want to compare the searching process of an activity and an input material in the same [Facilities] <sup>fi</sup>le. Let us assume that [Facilities]FacName=BASIC OXYGEN FURNACE. The user selects Facilities and Optimal in the Examine menu of the main menu, gets a listing of all facilities, selects the facility=BASIC OXYGEN FURNACE and goes to the Facilities Optimal screen.

This is common to both the searches. In the <sup>fi</sup>rst search, he or she clicks the Activities button and goes to the next page of the Facilities Optimal screen. This screen layout lists all the activities in this facility as an included layout. If the user wants to <sup>fi</sup>nd the values of rate for the output material STEEL for the Activity= CRUDE STEEL PRODUCTION at Time= 2 of this facility, then he or she looks at the list of activities and searches for Activity = CRUDE STEEL PRODUCTION and Time=2. This leads to an Activity Optimal screen which lists the output materials. This list then gives the value of output rate for the output material=STEEL. In this case, to get a required value, we first search (on the [Activities] file) with a combination of two fields, and then look for a sub-file or sub-field. In the second search, to get the maximum value of input material STEEL SCRAP that can be accommodated in this facility at Time =2, the user looks at the Facilities Optimal screen and looks at the included layout of Inputs. This included layout lists all the input materials at all times. The user then searches for Material=STEEL SCRAP and Time=2. In this case the search is performed with two searches at the sub-file level.

## 6.3. Included layouts and graphs in the time file

Suppose we have a question from a user. At Time =1, what is the optimal value of material sold for SINTER, and HIGH CARBON BILLET? In the Examine menu, the user can select

Materials and Optimal, and this will lead to a list of materials. The User can double click at SINTER and this will lead to the Materials Optimal screen of SINTER. In this screen there will be a list of Times and the user can <sup>fi</sup>nd the optimal value of material sold at Time= 1 in this list. Then he has to return to the list of materials and double click here again at HIGH CARBON BILLET. He then gets another Materials Optimal screen of HIGH CARBON BILLET. He can now look again at the Time Layout and see the material bought at Time=1. This is a cumbersome procedure. At Time= 1, the user cannot go from one material to another. This can be overcome by making an included layout of the [Materials] <sup>fi</sup>le in the [Times] <sup>fi</sup>le.

## 6.4. Reporting of optimal dual values

In this section, we discuss the dif<sup>fi</sup>culties in reporting the optimal dual values in multiple time periods. For a singleperiod model, the display of dual values is simple and straightforward. However, for the multi-period model we have dual values for more than one time period. In addition, to compute and display the reduced cost for the variable “Material Inventoried” at a time period we need dual values for two periods. This makes our task dif<sup>fi</sup>cult for displaying the optimal dual values.

## 7. Comparison of alternative database structures

In this section, we consider the different variations of the [Materials] and [Facilities] <sup>fi</sup>les. These <sup>fi</sup>les can be organized in several ways and we discuss how the computer times for variable and constraint generation vary with different variations of the relational and hierarchical databases. We consider two different types of structures: STEEL-TIME1and STEEL-TIME2. The differences between STEEL-TIME1 and STEEL-TIME2 are as follows:

1. In STEEL-TIME1, the time-dependent parameters are in the sub-<sup>fi</sup>elds of the [Materials] and [Facilities] <sup>fi</sup>les. In STEEL-TIME2 these are in the <sup>fi</sup>elds of the [Materials] and [Facilities] <sup>fi</sup>les.

2. The [Storage-Areas] <sup>fi</sup>le of STEEL-TIME is not considered in this comparison. In addition, vendoring or outsourcing is not considered as an option. Even if the indexing in the formulation and the way of representing the mathematical model is different, we essentially solve the same optimization problem in STEEL-TIME1 and STEEL-TIME2.

3. STEEL-TIME1 or STEEL-TIME2 cannot be clearly classi<sup>fi</sup>ed as a purely relational or purely hierarchical database. Each has both relational and hierarchical aspects. STEEL-TIME1 is more relational and [Activities] is a separate <sup>fi</sup>le. STEEL-

![](/api/attachments/BHJ2GHDN/fulltext/images/1cfc931cb0f126db1deb14a0767eec4d226ce99eb574c015330bb32cd3c70081.jpg)  
Fig. 8. Database structure of STEEL-TIME1.

![](/api/attachments/BHJ2GHDN/fulltext/images/67e36acbceaff2830b73591a46b81a46488259efff0b1aa6e23b9d222c98f001.jpg)  
Fig. 9. Database structure of STEEL-TIME2

TIME2 is more hierarchical, and [Activities] is a sub-<sup>fi</sup>le of the [Facilities] <sup>fi</sup>le.

4. As they solve the same optimization model, the numbers of constraints and variables in STEEL-TIME1 and STEEL-TIME2 are equal.

Fourer [11] has studied two different variations of the [Constraints] and [Variables] <sup>fi</sup>les, one relational and one hierarchical. We extend his comparison to two different variations of the [Materials] and [Facilities] <sup>fi</sup>les. We compare the implementation of STEEL-TIME1 and STEEL-TIME2 according to <sup>fi</sup>ve different criteria: implementation, ease of use, data storage and retrieval, ease of development and ef<sup>fi</sup>ciency of optimization (Figs. 8 and 9).

## 7.1. Implementation of STEEL-TIME1 vs. STEEL-TIME2

STEEL-TIME1 is a modi<sup>fi</sup>ed version of STEEL developed by Fourer [12]. We <sup>fi</sup>nd that STEEL-TIME2 is faster in generating the variables and constraints than STEEL-TIME1.This is because in STEEL-TIME1, the data for time-dependent parameters are stored in a sub-<sup>fi</sup>le. So every time a record is written in the [Variables] <sup>fi</sup>le, <sup>fi</sup>rst the record of the [Materials] is searched for, then the sub-record of the <sup>fi</sup>le is searched for, and <sup>fi</sup>nally the record is written in the [Variables] <sup>fi</sup>le. However in STEEL-TIME2, <sup>fi</sup>elds like BuyMax, BuyMin are at the <sup>fi</sup>eld level. Therefore to write a record in the [Variables] <sup>fi</sup>le, we only have to search the [Materials] and [Facilities] at the <sup>fi</sup>le level.

## 7.2. Ease of use

STEEL-TIME1 appears to be more complicated than STEEL-TIME2. Other than the [Times] <sup>fi</sup>le there are only two <sup>fi</sup>les in STEEL-TIME2, the [Materials] and the [Facilities] <sup>fi</sup>le.

Therefore it is easier to use STEEL-TIME2 than STEEL-TIME1. In the [Materials] <sup>fi</sup>le, all the purchases, sales and inventory related data about the Materials are kept at the <sup>fi</sup>le level. When the materials are displayed on an output layout, in STEEL-TIME2, sorting is possible with respect to the [Materials]MatName as well as [Materials]MatTimeID. However, in STEEL-TIME1, [Materials]MatName is at the <sup>fi</sup>le level and the [Materials]MatTime'MatTimeID is at the sub-<sup>fi</sup>le level. So sorting is not possible at the same level in STEEL-TIME1.

In STEEL-TIME1, there are three <sup>fi</sup>les and [Activities] is a separate <sup>fi</sup>le related to the [Facilities] <sup>fi</sup>le. From a developer's point of view, STEEL-TIME1 is more complicated than STEEL-TIME2. Moreover, most of the searches are performed at the sub-<sup>fi</sup>le level. For example, it is possible to list the dual prices and the reduced cost coef<sup>fi</sup>cients in the output layout at the <sup>fi</sup>le level in STEEL-TIME2, but similar lists are not possible in the STEEL-TIME1. Such a display is available in STEEL-TIME1 at the sub-record level only. On the other hand, STEEL-TIME1 has a greater <sup>fl</sup>exibility for listing the activities, as [Activities] is a separate output <sup>fi</sup>le. Because of the inherent advantages of the relational <sup>fi</sup>le, the user will be able to update activities separately. Although we have not implemented this concept in STEEL-TIME1, such an implementation is possible. STEEL-TIME1 will also allow the user to compare two activities of two facilities by listing activities on the output <sup>fi</sup>le. So, an activity PRODUCTION OF ES1 in three facilities M1, M2, M3 can be listed by performing a search with [Activities]ActName=qPRODUC-TION OF ES1q. Such searches are not possible with STEEL-TIME2.

## 7.3. Data storage and retrieva

STEEL-TIME1 satis<sup>fi</sup>es the conditions of normalization that no piece of information be stored in more than one place. This condition is not satis<sup>fi</sup>ed in STEEL-TIME2. We also see that STEEL-TIME2 takes greater storage space than STEEL-TIME1. In STEEL-TIME2 certain <sup>fi</sup>elds are repeated. [Materials]MatName, [Materials]MatType, [Materials]MatInvZero, [Materials] MatUnits, [Facilities]FacName and [Facilities]FacUnits are the <sup>fi</sup>elds that are repeated for every record of the [Time]TimeID <sup>fi</sup>le. This certainly requires more space for data storage, but does not pose a very serious problem with respect to ease of use. The 4th Dimension software allows a script to be written so that when the user enters the data for [Materials]MatName for one time period, the same [Materials]MatName is also available in other time periods. Therefore, as long as we are not changing [Materials]MatTime, we do not need to enter the data for each time period.

## 7.4. Ease of development

STEEL-TIME2 is easier to develop than STEEL-TIME1. However, we have decided to opt for STEEL-TIME1 as our main implementation, primarily because the latest version of the 4th Dimension software does not support more than one level of sub-<sup>fi</sup>le. Because of the inherent advantage of relational databases, [Activities] was de<sup>fi</sup>ned as a separate <sup>fi</sup>le in STEEL-TIME1, whereas it was a sub-<sup>fi</sup>le in the [Facilities] <sup>fi</sup>le of STEEL-TIME2.

## 7.5. Efficiency

The times for constraint generation, variable generation and solution, and reading optimal values and the dual values are as shown in Table 3.

## Table 3

Comparison of STEEL-TIME1 and STEEL-TIME2

<table><tr><td>Computer</td><td colspan="2">Macintosh</td></tr><tr><td>Database</td><td>STEEL-TIME1</td><td>STEEL-TIM2</td></tr><tr><td>Records in files</td><td></td><td></td></tr><tr><td>Materials</td><td>19</td><td>57</td></tr><tr><td>Facilities</td><td>21</td><td>21</td></tr><tr><td>Activities</td><td>24</td><td>24 (sub-file)</td></tr><tr><td>Times</td><td>3</td><td>3</td></tr><tr><td>Constraints</td><td>141</td><td>141</td></tr><tr><td>Vairables</td><td>266</td><td>266</td></tr><tr><td>(KB)</td><td></td><td></td></tr><tr><td>Disk space (model)</td><td>688</td><td>336</td></tr><tr><td>Disk space (data)</td><td>472</td><td>484</td></tr><tr><td>Time in seconds</td><td></td><td></td></tr><tr><td>Cons. generation time</td><td>12</td><td>12</td></tr><tr><td>Var. generation time</td><td>109</td><td>45</td></tr><tr><td>Writing constraint time</td><td>7</td><td>7</td></tr><tr><td>Writing variable time</td><td>22</td><td>21</td></tr><tr><td>Solving</td><td>8</td><td>8</td></tr><tr><td>Reading optimal value time</td><td>21</td><td>21</td></tr><tr><td>Reading dual value time</td><td>8</td><td>8</td></tr></table>

We <sup>fi</sup>nd that STEEL-TIME2 is faster in generating the variables and constraints than STEEL-TIME1. This is because in STEEL-TIME1, the data for time-dependent parameters are stored in a sub-<sup>fi</sup>le. So every time a record is written in the [Variables] <sup>fi</sup>le, <sup>fi</sup>rst the record of the [Materials] is searched for, then the sub-record of the <sup>fi</sup>le is searched for, followed by the writing of the record in the [Variables] <sup>fi</sup>le. However in STEEL-TIME2, <sup>fi</sup>elds like BuyMax, BuyMin are at the <sup>fi</sup>eld level. Therefore to write a record in the [Variables] <sup>fi</sup>le, we only have to search the [Materials] and [Facilities] at the <sup>fi</sup>le level. Similarly, the disk-space for the data of STEEL-TIME2 is higher than that of STEEL-TIME1.

After a careful comparison of these two variations, we <sup>fi</sup>nd that STEEL-TIME2 is superior to STEEL-TIME1 on an overall basis. However, we need to extend the present study so that STEEL-TIME2 is normalized. This can be done by replacing all the sub-<sup>fi</sup>les by <sup>fi</sup>les so that [Materials]MatTime and [Facilities]FacTime and other sub-<sup>fi</sup>les will be normalized with additional indices and key-<sup>fi</sup>elds. We will be in a position to recommend STEEL-TIME2 only after that.

## 8. Extension and conclusion

An extension of the DSS will be non-linearity of the model. Most of the industrial cost curves are non-linear or at best can be represented as having a piece-wise linear behavior. It will be interesting to study how to represent these non-linearities while retaining the model's user friendliness.

A second extension of the model will be to have multiple objective linear programs and represent them in the database. This can be done by changing the model management system. For example, the current model can be changed to cost minimization, revenue maximization, maximization of marketable products (revenue or production), maximization of the utilization of the facilities etc. It is possible to have a menu driven program in this DSS which optimizes over different objectives. A third extension can be made by extending this DSS to stochastic optimization problems.

An interesting extension will be to study the paradigm neutrality (Geoffrion) [14] of this data structure for the multiperiod model. Although the model is designed for the mathematical programming paradigm, we can extend it to inventory control and also for scheduling, vehicle routing and queuing applications. We have parameters for all materials at all times. We can determine the ordering and holding cost for all material and hence try to <sup>fi</sup>nd optimal order quantities. However, the batch size will be decided by practical considerations like a steel technology term — heat size — of the steel making shop, the capacity of the vehicle carrying the products and the capacity of the loading and unloading facility. Given that we have the batch size and lead-time of all materials produced, the present model can be extended to a scheduling model of each product in each time.

## Acknowledgements

This work has been supported in part by grants from the American Iron and Steel Institute and its members, by grant DDM-8908818 from the U.S. National Science Foundation, and by the Research and Publication Committee of the Indian Institute of Management. Ahmedabad. India

Storage-areas data

Activities data

## Appendix 1. Model formulation

We <sup>fi</sup>rst de<sup>fi</sup>ne the data, in <sup>fi</sup>ve parts: times, materials, facilities, activities, and storage-areas. The notation for the decision variables is then presented. Finally the objective and constraints are described, in both words and formulae.

All quantities of materials are taken to be in the same units, such as kilograms.

## Time data

$T { = } \{ 1 , { \ldots } { \ldots } , T \}$ is the set of time periods in the planning horizon, indexed by t

$\rho$ is the interest rate per period, taken as zero if there is no discounting

## Materials data

M is the set of all materials $l _ { j t } ^ { \mathrm { b u y } }$ lower limit on purchases of material j, for each $j \in M$ and $t \in T$

$u _ { j t } ^ { \mathrm { b u y } }$ upper limit on purchases of material j, for each $j \in M$ and $t \in T$

$c _ { j t } ^ { \mathrm { b u y } }$ cost per unit of material j purchased, for each $j \in M$ and $t \in T$

$l _ { j t } ^ { \mathrm { s e l l } }$ lower limit on sales of material j, for each $j \in M$ and $t \in T$

$u _ { j t } ^ { \mathrm { s e l l } }$ upper limit on sales of material j, for each j ∈ M and $t \in T$

$c _ { j t } ^ { \mathrm { s e l l } }$ revenue per unit of material j, for each $j \in M$ and $t \in T$

$l _ { j t } ^ { \mathrm { i n v } }$ lower limit on inventory of material j, for each j∈M and $t \in T$

$u _ { j t } ^ { \mathrm { i n v } }$ upper limit on inventory of material j, for each j∈M and $t \in T$

$\nu _ { i 0 } ^ { \mathrm { i n v } }$ initial inventory of material j, for each $j \in M$ $c _ { j t } ^ { \mathrm { { i n v } } }$ holding cost per unit of material j, for each $j \in M$ and $t \in T$

$M ^ { \mathrm { c o n v } } \subseteq \{ j { \in } M , j ^ { \prime } { \in } M : j { \neq } j ^ { \prime } \}$ is the set of conversions:

$( j , j ^ { \prime } ) { \in } M ^ { \mathrm { c o n v } }$ <sup>g</sup>means that material j can be converted to <sup>ð Þ</sup>material j′

$\mathcal { \alpha } _ { j j ^ { \prime } t } ^ { \mathrm { { c o n v } } }$ number of units of material $j ^ { \prime }$ that result from converting one unit of material j, for each $( j , j ^ { \prime } ) { \in } M ^ { \mathrm { c o n v } } , t { \in } T$

$c _ { j j ^ { \prime } t } ^ { \mathrm { c o n v } }$ <sup>ð Þ</sup>cost per unit of material j of the conversion from j to $j ^ { \prime } ,$ for each $( j , j ^ { \prime } ) { \in } M ^ { \mathrm { c o n v } } , t { \in } T$

## Facilities data

F is the set of facilities $l _ { i t } ^ { \tt c a p }$ the minimum amount of the capacity of facility i that must be used, for each $i \in F$ and $t \in T$

$u _ { i t } ^ { \mathrm { c a p } }$ the capacity of facility i, for each $i \in F$ and $t \in T$

$c _ { i t } ^ { \mathsf { a p } }$ the cost of vendoring (outsourcing) a unit of capacity at facility i, for each $i \in F$ and $t \in T$

$F ^ { \mathrm { i n } } \subseteq F x M$ is the set of facility inputs:

$( i , j ) { \in } F ^ { \mathrm { i n } }$ means that material j is used as an input at facility i

$l _ { i j t } ^ { \mathrm { i n } }$ the minimum amount of material j that must be used as input to facility i, for each $( i , j ) { \in } F ^ { \mathrm { i n } }$ $t \in T$

$u _ { i j t } ^ { \mathrm { i n } }$ the maximum amount of material j that must be used as input to facility i, for each $( i , j ) { \in } F ^ { \mathrm { i n } } , t { \in } T$

F<sup>out</sup>pFxMis the set of facility outputs:

$( i , j ) { \in } F ^ { \mathrm { o u t } }$ means that materialj is produced as an output at facilityi $l _ { i j t } ^ { \mathrm { { o u t } } }$ the minimum amount of material j that must be produced as output at facility i, for each $( i , j ) { \in } F ^ { \mathrm { { o u t } } }$ $t \in T$

$u _ { i j t } ^ { \mathrm { { o u t } } }$ the maximum amount of material j that must be produced as output at facility i, for each $( i , j ) { \in } F ^ { \mathrm { { o u t } } }$ $t \in T$

$F ^ { \mathrm { a c t } } \subseteq \{ ( i , k ) : i { \in } F \} .$ is the set of activities:

$( i , k ) { \in } F ^ { \mathrm { a c t } }$ <sup>gÞ</sup>means that k is an activity available at facility i $l _ { i k t } ^ { \mathrm { a c t } }$ the minimum number of units of activity k that may be run at facility i, for each $( i , k ) { \in } F ^ { \mathrm { a c t } } , t { \in } T$

$u _ { i k t } ^ { \mathrm { a c t } }$ <sup>ð Þ</sup>the maximum number of units of activity k that may be run at facility i, for each $( i , k ) { \in } F ^ { \mathrm { a c t } } , t { \in } T$

$c _ { i k t } ^ { \mathrm { a c t } }$ <sup>ð Þ</sup>the cost per unit of running activity k at facility i, for each $( i , k ) { \in } F ^ { \mathrm { a c t } } , t { \in } T$

$r _ { i k t } ^ { \mathrm { a c t } }$ <sup>ð Þ</sup>the number of units of activity that can be accommodated in one unit of capacity of facility i, for each $( i , k ) { \in } { \cal F } ^ { \mathrm { a c t } } , t { \in } T$

$A ^ { \mathrm { i n } } \subseteq \left\{ ( i , j , k , t ) : ( i , j ) { \in } F ^ { \mathrm { i n } } ( i , k ) { \in } F ^ { \mathrm { a c t } } , t { \in } T \right\}$ is the set of activity <sup>ð</sup>inputs:

$( i , j , k , t ) { \in } A ^ { \mathrm { i n } }$ means that input material j is used by activity k <sup>ð Þ</sup>at facility i during time period t

$\alpha _ { i j k t } ^ { \mathrm { i n } }$ units of input material j required by one unit of activity k at facility i in time period t, for each $( i , j , k , t ) { \in } A ^ { \mathrm { i n } }$

$$
A ^ {\text { out }} \subseteq \{(i, j, k, t): (i, j) \in F ^ {\text { out }} (i, k) \in F ^ {\text { act }}, t \in T \}
$$

$( i , j , k , t ) { \in } A ^ { \mathrm { o u t } }$ means that output material j is produced by <sup>ð Þ</sup>activity k at facility i during time period t

$\alpha _ { i j k t } ^ { \mathrm { o u t } }$ units of output material j produced by one unit of activity k at facility i in time period t, for each $( i , j , k , t ) { \in } A ^ { \mathrm { o u t } }$

S is the set of storage areas

$l _ { s t } ^ { s \mathrm { t o r } }$ lower limit on total material in storage area s, for each $s \in S , t \in T$

$u _ { s t } ^ { s \mathrm { t o r } }$ upper limit on total material in storage area s, for each $s \in S , t \in T$

## Variables

$x _ { i { t } } ^ { \mathrm { b u y } }$ units of material j bought, for each $\textstyle j \in M , t \in T$ 1

$\bar { x _ { j t } ^ { \mathrm { s e l l } } }$ units of material j sold, for each $\textstyle j \in M , t \in T$ $\bar { x _ { j s t } ^ { \mathrm { s t o r } } }$ units of material j in storage area s, for each $j \in M ,$ $s \in S , t \in T$

$x _ { j t } ^ { \mathrm { i n v } }$ total units of material j in inventory (storage), for each j∈M, t∈T

$x _ { i 0 } ^ { \mathrm { i n v } }$ initial inventory of material j, for each $j \in M$ $x _ { j j ^ { \prime } t } ^ { \mathrm { c o n v } }$ units of material j converted to material j′, for each $( j , j ^ { \prime } ) { \in } M ^ { \mathrm { c o n v } } , t { \in } T$

$x _ { i j t } ^ { \mathrm { i n } }$ <sup>ð Þ</sup>units of material j used as input by facility i, for each $( i , j ) { \in } F ^ { \mathrm { i n } } , t { \in } T$

$x _ { i j t } ^ { \mathrm { o u t } }$ <sup>ð Þ</sup>units of material j produced as output by facility i, for each $( i , j ) { \in } F ^ { \mathrm { o u t } } , t { \in } T$

$x _ { i k t } ^ { \mathrm { a c t } }$ <sup>ð Þ</sup>units of activity k operated at facility i, for each $( i , k ) { \in } F ^ { \mathrm { a c t } } , t { \in } T$

$x _ { i t } ^ { \mathrm { c a p } }$ <sup>ð Þ</sup>units of capacity vendored at facility i, for each $i \in { \cal F } ,$ $t \in T$

Objective

Maximize the sum, over all time periods, of revenues from sales less costs of purchasing, holding inventories, converting, operating activities at facilities and vendoring:

$$
\sum_ {t \in T} (1 + \rho) ^ {- t} z (t)
$$

Where,

$$
\begin{array}{l} z (t) = \sum_ {j \in M} c _ {j t} ^ {\text { sell }} x _ {j t} ^ {\text { sell }} - \sum_ {j \in M} c _ {j t} ^ {\text { buy }} x _ {j t} ^ {\text { buy }} - \sum_ {j \in M} c _ {j t} ^ {\text { inv }} x _ {j t} ^ {\text { inv }} \\ - \sum_ {(j, j ^ {\prime}) \in M ^ {\text { conv }}} c _ {j j ^ {\prime} t} ^ {\text { conv }} x _ {j j ^ {\prime} t} ^ {\text { conv }} - \sum_ {(i, k) \in F ^ {\text { act }}} c _ {i k t} ^ {\text { act }} x _ {i k t} ^ {\text { act }} - \sum_ {i \in F} c _ {i t} ^ {\text { cap }} x _ {i t} ^ {\text { cap }} \end{array}\tag{1}
$$

Constraints

For each $\scriptstyle j \in M , \ r \in R$ and $t \in T ,$ the amount of material j made available by purchases, production, conversions and beginning inventory must equal the amount used for sales, production, conversions and ending inventory:

$$
\begin{array}{c} x _ {j t} ^ {\text {buy}} + \sum_ {(i, j) \in F ^ {\text {out}}} x _ {i j t} ^ {\text {out}} + \sum_ {(j ^ {\prime}, j) \in M ^ {\text {conv}}} \alpha_ {j ^ {\prime} j t} ^ {\text {conv}} x _ {j ^ {\prime} j t} ^ {\text {conv}} + x _ {j t - 1} ^ {\text {inv}} \\ = x _ {j t} ^ {\text {sell}} + \sum_ {(i, j) \in F ^ {\text {in}}} x _ {i j t} ^ {\text {in}} + \sum_ {(j, j ^ {\prime}) \in M ^ {\text {conv}}} x _ {j j ^ {\prime} t} ^ {\text {conv}} + x _ {j t} ^ {\text {inv}} \end{array}\tag{2}
$$

For each $( i , j ) { \in } F ^ { \mathrm { i n } }$ and $t { \in } T ,$ the amount of input j used at <sup>ð Þ</sup>facility i must equal the total consumption by all the activities at facility i:

$$
\chi_ {i j t} ^ {\text { in }} = \sum_ {(i, j, k, t) \in A ^ {\text { in }}} \alpha_ {i j k t} ^ {\text { in }} \chi_ {i k t} ^ {\text { act }}\tag{3}
$$

For each $( i , j ) { \in } F ^ { \mathrm { { o u t } } }$ and $t { \in } T ,$ the amount of output j <sup>ð Þ</sup>produced at facility i must equal the total production by all the activities at facility i:

$$
x _ {i j t} ^ {\text { out }} = \sum_ {(i, j, k, t) \in A ^ {\text { out }}} \alpha_ {i j k t} ^ {\text { out }} x _ {i k t} ^ {\text { act }}\tag{4}
$$

For each $i \in F$ and $t \in T ,$ the capacity used by all activities at facility i must be within the range given by the lower limit and the upper limit plus the amount of capacity vendored:

$$
l _ {i t} ^ {\text { cap }} \leq \sum_ {(i, k) \in F ^ {\text { act }}} x _ {i k t} ^ {\text { act }} / r _ {i k t} ^ {\text { act }} \leq u _ {i t} ^ {\text { cap }} + x _ {i t} ^ {\text { cap }}\tag{5}
$$

For each $j \in M ,$ , the amount of material inventoried in the plant before the <sup>fi</sup>rst time period is de<sup>fi</sup>ned to equal the speci<sup>fi</sup>ed initial inventory:

$$
x _ {j 0} ^ {\mathrm{inv}} = v _ {j 0}\tag{6}
$$

For each $j \in M$ and $t { \in } T ,$ the total amount of material j inventoried is de<sup>fi</sup>ned as the sum of the inventories over all storage areas:

$$
\sum_ {s \in S} x _ {j s t} ^ {\text {stor}} = x _ {j t} ^ {\text {inv}}\tag{7}
$$

For each $s { \in } S$ and $t { \in } T ,$ the total of all materials inventoried in storage area s must be within the speci<sup>fi</sup>ed limits:

$$
l _ {s t} ^ {\text { stor }} \leq \sum_ {j \in M} x _ {j s t} ^ {\text { stor }} \leq u _ {s t} ^ {\text { stor }}\tag{8}
$$

Bounds

All variables must lie within the relevant limits de<sup>fi</sup>ned by the data:

$$
\begin{array}{l l} l _ {j t} ^ {\text {buy}} \leq x _ {j t} ^ {\text {buy}} \leq u _ {j t} ^ {\text {buy}}, & \text {for each} j \in M \text {and} t \in T \\ l _ {j t} ^ {\text {sell}} \leq x _ {j t} ^ {\text {sell}} \leq u _ {j t} ^ {\text {sell}}, & \text {for each} j \in M \text {and} t \in T \\ l _ {j t} ^ {\text {inv}} \leq x _ {j t} ^ {\text {inv}} \leq u _ {j t} ^ {\text {inv}}, & \text {for each} j \in M \text {and} t \in T \\ 0 \quad \leq \quad x _ {j j ^ {\prime} t} ^ {\text {conv}}, & \text {for each} (j, j ^ {\prime}) \in M ^ {\text {conv}} \text {and} t \in T \\ 0 \quad \leq \quad x _ {j j ^ {\prime} t} ^ {\text {cap}}, & \text {for each} i \in F \text {and} t \in T \\ 0 \quad \leq \quad x _ {j s t} ^ {\text {stor}}, & \text {for each} s \in S, j \in M \text {and} t \in T \\ l _ {i j} ^ {\text {in}} \leq x _ {i j} ^ {\text {in}} \leq u _ {i j} ^ {\text {in}}, & \text {for each} (i, j) \in F ^ {\text {in}} \text {and} t \in T \\ l _ {i j} ^ {\text {out}} \leq x _ {i j} ^ {\text {out}} \leq u _ {i j} ^ {\text {out}}, & \text {for each} (i, j) \in F ^ {\text {out}} \text {and} t \in T \\ l _ {i k} ^ {\text {act}} \leq x _ {i k} ^ {\text {act}} \leq u _ {i k} ^ {\text {act}}, & \text {for each} (i, j) \in F ^ {\text {act}} \text {and} t \in T \end{array}\tag{9}
$$

## References

[1] D. Adams, D. Beckett, Programming in 4th Dimension, the Ultimate Guide, Automated Solutions Group, Huntington Beach, CA, USA, 1999.

[2] C.J. Date, Introduction to Database Systems, 3rd EditionAddison-Wesley Publishing Company, 1981.

[3] D.R. Dolk, Data as models: an approach to implementing model management, Decision Support Systems 2 (1) (1986) 73–80.

[4] D.R. Dolk, A generalized model management system for mathematical programming, ACM Transactions on Mathematical Software 12 (2) (1986) 92–126

[5] B. Dominguez-Ballesteros, G. Mitra, C. Lucas, N.S. Koutsoukis, Modeling and solving environments for mathematical programming (MP): a status review and new directions, Journal of Operational Research Society 53 (2002) 1072–1092.

[6] G. Dutta, Multi-period optimization based decision support system for strategic and operations planning, Ph.D. Dissertation, Department of Industrial Engineering and Management Science, Northwestern University. Evanston, USA. 1996

[7] G. Dutta, R. Fourer, A survey of mathematical programming applications in an integrated steel plant. Manufacturing & Service Operations Management 3 (4) (2001) 387–400.

[8] G. Dutta, R. Fourer, An optimization-based decision support system for strategic and operational planning in process industries, Optimization and Engineering 5 (2004) 295-314.

[9] G. Dutta, R. Fourer, A. Majumdar, D. Dutta, An optimization based decision support system for strategic and operational planning with in process industries: case of pharmaceuticals industry in India, International Journal of Production Economics 102 (2007) 92–103.

[10] G. Dutta, G.P. Sinha, P.N. Roy, N. Mitter, A linear programming model for distribution of electrical energy in a steel plant, International Transactions in Operational Research 1 (1) (1994) 17–29.

[11] R. Fourer, Modeling language versus matrix generator for linear programming, ACM Transactions on Mathematical Software 9 (2) (1983) 143–183.

[12] R. Fourer, Database structure for mathematical programming models, Decision Support Systems 20 (1997) 317–344.

[13] A.M. Geoffrion, Computer-based modeling environments, European Journal in Operations Research 41 (1989) 33–43.

[14] A.M. Geoffrion, W.G. Graves, S. Lee, A management support system for distribution planning, INFOR 20 (4) (1982) 287–314.

[15] V. Gupta, E. Peters, T. Miller, K. Blyden, Implementing a distribution network decision support system at P<sup>fi</sup>zer/Warner-Lambert, Interfaces 32 (4) (2002) 28–45.

[16] R.E. Marsten, The design of XMP linear programming library, ACM Transactions on Mathematical Software 7 (1981) 481–497.

[17] F.H. Murphy, E.A. Stohr, A. Asthana, Representation scheme for linear programming models. Management Science 38 (7) (1992) 964–991.

[18] S. Murthy, R. Akkiraju, R. Goodwin, P. Keskinocak, Cooperative multiobjective decision support for the paper industry, Interfaces 29 (5) (1999) 5–30.

[19] G.P. Sinha, B.S. Chandrashekaran, N. Mitter, G. Dutta, S.B. Singh, P.N. Roy, A. Roy Choudhary, Strategic and operations management with optimization at Tata Steel, Interfaces 25 (1) (1995) 6–19.

[20] Y. Wu, S.C.H. Leung, K.K. Lai, A stochastic programming approach for multi-site aggregate production planning, Journal of Operationa Research Society 57 (2006) 123–132.

Goutam Dutta is a Professor of Production and Quantitative Methods Area and Chair of Research and Publications Committee in Indian Institute of Management, Ahmedabad. He has a B.Tech (Hons) from IIT, Kharagpur, India; MBA from XLRI, Jamshedpur, India and Ph.D. from Northwesten University, USA.

His research interests are in revenue management, decision support systems, optimization, and practice of management science, operations management, energy models, and health care services. He was a faculty at the London School of Economics and Political Science, UK (1996–97) and visiting faculty at the University of Illinois, USA (2001). He was a visiting scholar, Chinese University of Hong Kong, 2004. His doctoral dissertation led to the development of optimization-based planning software, copyrighted and licensed by Northwestern University, USA. This work was selected as a <sup>fi</sup>nalist for EURO Excellence in Practice Award in 2006. In International Federation of Operational Research Societies (IFORS) OR for Development Prize Competitions, he was a member of the jury in 1996 at Vancouver and Chair of the jury in 1999 at Beijing and 2002 in Scotland. Served as the Editor, Special Issues for OR in Development in International Transactions in Operational Research (2001). He is a member of the Editorial Board of Journal of Operational Research Society (UK), International Transactions in Operational Research and International Journal of Revenue Management. He is the winner (with opthers) of the prestigious Franz Edelman Award of INFORMS (Institute of Operations Research and Management Science, USA) in 1994 and received the <sup>fi</sup>rst prize in IFORS OR for Development Prize Competition in 1993.

Robert Fourer is a Professor of Industrial Engineering and Management Sciences from Northwestern University. He has a M.S. in Statistics, M.S. in Operations Research from Stanford University (1979) and Ph.D. in Operations Research from Stanford University (1980). He is the developer and author of AMPL: A Modeling Language for Mathematical Programming (with David M. Gay and Brian W. Kernighan at Bell Laboratories). He is the winner of the 2003 Beale– Orchard-Hays Prize for Excellence in Computational Mathematical Programming, 2004 ORMS Fellow Award, 2004 Medallion Award of the Institute of Industrial Engineers, and 1993 ORSA/CSTS Prize (with others). His papers have been published in prestigious journals like Management Science, Mathematical Programming, Operations Research, ACM transactions on Mathematical Software, SIAM Journal on Scienti<sup>fi</sup>c Computing, INFORMS Journal of Computing and Manufacturing and Services Operations Management. He is also in the editorial board of several international journals like Operations Research, INFORMS Journal in Computing and in the board of Management Science, IMA Journal of Management Mathematics.
