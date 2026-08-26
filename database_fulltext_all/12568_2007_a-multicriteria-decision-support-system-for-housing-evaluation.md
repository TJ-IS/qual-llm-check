---
otero_id: 12568
otero_key: "65UHXHF3"
title: "A multicriteria decision support system for housing evaluation"
authors: "Eduardo Natividade-Jesus; João Coutinho-Rodrigues; Carlos Henggeler Antunes"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.03.014"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multicriteria decision support system for housing evaluation

Eduardo Natividade-Jesus <sup>a,b,⁎</sup>, João Coutinho-Rodrigues <sup>b,c</sup>, Carlos Henggeler Antunes <sup>b,d</sup>

<sup>a</sup> Department of Civil Engineering, Polytechnic Institute of Coimbra - School of Engineering, Quinta da Nora, 3030 Coimbra, Portugal <sup>b</sup> INESC Coimbra, Rua Antero de Quental 199, 3000-033 Coimbra, Portugal

<sup>c</sup> Department of Civil Engineering, University of Coimbra, Faculty of Sciences and Technology, Polo II, 3030-290 Coimbra, Portugal <sup>d</sup> Department of Electrical Engineering and Computers, University of Coimbra, Faculty of Sciences and Technology, Polo II, 3030-290 Coimbra, Portugal

Received 10 June 2005; received in revised form 6 January 2006; accepted 27 March 2006 Available online 23 December 2006

## Abstract

Economic and population growth, higher life quality standards, and lower interest rates have led to an increase in the demand for housing. However, in many urban areas, land for housing is becoming scarce, and environmental and construction requirements more stringent

Therefore, the need arises for an adequate methodology to evaluate the urban built space under different perspectives (consumers, promoters, municipal authorities, etc.) and multiple evaluation criteria. A decision support system for housing evaluation is presented in this paper. It integrates a problem editor, a data base management module, a set of multiple criteria decision aid methods and an adequate Human–computer interface, which can be integrated with GIS tools. © 2007 Elsevier B.V. All rights reserved.

Keywords: Housing evaluation; Dwelling; Decision support systems; Multicriteria analysis

## 1. Introduction

The (family) house is a very important issue related to the safety, autonomy and comfort of people. Being also related to the social status, its possession could constrain or facilitate the access to other essential aspects of modern life such as education, health, leisure, etc. [22].

The economic growth and population concentration in urban centres, the changes of habits, new wellbeing requirements and lower interest rates have led to an increase in the demand for housing in urban areas.

In Portugal, despite the lower income per capita compared with other European countries, the percentage of house owners is surprisingly high (see Table 1) and the house value is equivalent to several years of family income. For an average qualified worker, the house represents 70% to 80% of his/her patrimony [10]. Moreover, to illustrate how important the house is in the families patrimony in Portugal, there are 135 houses for each 100 families [18]. However, buying a house is usually a decision taken using less detailed information than buying a car. This is justified by the lack of multidimensional and specialised knowledge that should be involved in house evaluation.

Table 1  
House owners vs income per capita

<table><tr><td>Country</td><td>Income per capita (USD)</td><td>Owner-occupier (%)</td><td>Private rental (%)</td><td>Public rental (%)</td><td>Others (%)</td></tr><tr><td>Switzerland</td><td>36430</td><td>31</td><td>60</td><td>3</td><td>6</td></tr><tr><td>Germany</td><td>26000</td><td>38</td><td>36</td><td>26</td><td>-</td></tr><tr><td>Belgium</td><td>22260</td><td>62</td><td>30</td><td>7</td><td>-</td></tr><tr><td>Holland</td><td>21300</td><td>47</td><td>17</td><td>36</td><td>-</td></tr><tr><td>Austria</td><td>25010</td><td>41</td><td>22</td><td>23</td><td>14</td></tr><tr><td>Sweden</td><td>23270</td><td>43</td><td>16</td><td>22</td><td>19</td></tr><tr><td>Denmark</td><td>29010</td><td>50</td><td>24</td><td>18</td><td>8</td></tr><tr><td>France</td><td>23550</td><td>54</td><td>21</td><td>17</td><td>8</td></tr><tr><td>Spain</td><td>12500</td><td>76</td><td>16</td><td>2</td><td>-</td></tr><tr><td>U.K.</td><td>18950</td><td>66</td><td>10</td><td>24</td><td>-</td></tr><tr><td>Portugal</td><td>6900</td><td>65</td><td>28</td><td>4</td><td>3</td></tr><tr><td>U.S.A.</td><td>-</td><td>56</td><td>21</td><td>18</td><td>5</td></tr></table>

Source: Balchin, P., The Housing Policy in Europe, 1996 [4].

Simultaneously, the available space to build new housing is getting scarcer and urban environmental conditions are degrading. As a result of these conditions people are demanding a superior quality for housing. Therefore, there is a growing need for more scientifically sound methods for performing a systematic housing evaluation, capable of dealing with multiple, conflicting and incommensurable aspects both of qualitative and quantitative nature, as well as responding to the concerns of different stakeholders (developers, consumers, government agencies, municipalities, etc.).

Methodologies for housing evaluation are used in several European countries [14], such as Qualitel in France [2,3], SEL in Switzerland [27,32], HQI in UK [16]. However, these methodologies either address just a small fraction of the criteria universe that should be considered for making well informed decisions or use very simplified techniques for the evaluation. Moreover, they were conceived for quality evaluation purposes only. Some research work have been carried out in Portugal based on the two first methods mentioned above, and a new method for quality evaluation of buildings was proposed by Costa [14]. However these methodologies are neither broadly divulged nor used by experts and consumers in general.

These problems inherently involve multiple, conflicting, and incommensurate aspects of evaluation of the merit of the different alternatives depending on the context of the study (value or quality assessment, prioritising interventions, etc.) and the stakeholders involved (consumers, promoters, government or municipal agencies, etc.). Therefore, models for decision support become more representative of the actual decision context if the distinct evaluation aspects are explicitly taken into account. Multiple criteria models enable to capture the diversity of evaluation aspects, providing decision makers and/or planning bodies a better perception of the conflicting aspects under evaluation and the nature of the trade-offs to be made.

Given the diversity and complexity of the factors that influence this type of evaluation, and the volume of information involved, decision support systems (DSS) are an essential tool for the study of this type of problems by integrating the efficiency and the ease of information processing of information systems with formal models for providing decision support.

In this paper, we present a DSS, which can assist several stakeholders (corresponding to distinct user profiles and expected results) in the housing market to make better-founded decisions. These user profiles and corresponding aims may be briefly characterised as follows:

\- the designers to evaluate the influence of their options in the final quality of housing;

\- the government and financing entities to define loan policies as a function of quality levels in order to promote the construction and acquisition of higher quality housing;

\- the promoters to adjust projects to consumer profiles;

\- local/municipal agencies to characterise the housing stock and/or to prioritise repair or refurbishment interventions;

\- the consumers to select a house.

The DSS integrates a problem editor, a data base management module, a set of multiple criteria decision aid methods and an adequate Human–computer interface aimed at minimizing the cognitive effort required from users.

In the DSS implementation, special attention was paid to: (i) the identification and structuring of the various evaluation aspects (attributes) which are at stake in these problems (construction costs, location, accessibility, environmental quality, design quality, construction quality, land value, etc.); (ii) the hierarchical classification of the attributes so that the evaluation can be performed at any level of the hierarchy; (iii) the selection of adequate multicriteria methods; (iv) support the inclusion of qualitative and quantitative information to assess the attribute scores, including the comparison with established standards (e.g. noise control, comfort dimensions, etc.); (v) the development of an user friendly interface. The integration of all these aspects, which may involve the use of large amounts of inter related alphanumeric and spatial data, was accomplished by using a relational data base management system (4D/

![](/api/attachments/65UHXHF3/fulltext/images/245d6b8573f20632ea193cbf839e2ae0a1ed7abb69669e8df2b48a460c9f5fd2.jpg)  
Fi<sub>g</sub> 1 Th<sub>e</sub> t<sub>ree s</sub>t<sub>ruc</sub>t<sub>ure w</sub>ith th<sub>e</sub> 2 1 0 <sub>a</sub>tt<sub>r</sub>ib<sub>u</sub>t<sub>es</sub> th<sub>a</sub>t <sub>c</sub>h<sub>arac</sub>t<sub>er</sub>i<sub>se</sub> th<sub>e va</sub>l<sub>ue o</sub>f <sub>a proper</sub>t<sub>y</sub>

4D Server) incorporating a programming language for model and interface development [15].

In this section the motivation and the main objectives of the study have been presented as well as the general framework of the problem, including a brief reference to other approaches for quality evaluation of buildings. In Section 2 the methodology and process of choice, and organization of the attributes to be used in a multicriteria approach for housing evaluation are described, with reference to several sources that have inspired the selection of such attribute structure. A DSS for housing evaluation is presented in Section 3, describing its components and functionalities and highlighting the potentialities of using multicriteria methodologies (in particular, those devoted to the classification of alternatives in pre-defined categories, such as ELECTRE TRI) in this type of problems.

## 2. Attributes to characterise the value of a property and their hierarchy

The problem of housing evaluation involves multiple attributes (many of them assessed through qualitative measurement forms), with different importance, that influence the value of a property, ranging from intrinsic aspects of the construction to environmental and location aspects.

Several sources were used in order to develop a coherent set of attributes, mainly methods for quality evaluation used in some European countries, such as Qualitel [2,3], SEL [27,32], HQI [16], BATIMPACT for environmental quality assessment [7], BEPAC — Building Environmental Performance Assessment Criteria [26], BREEAM — Building Research Establishment Environmental Assessment Method [8], Environmental

Table 2  
Hierarchy of attributes — level 4 (branches A and B)

<table><tr><td>Level 1</td><td>Level 2</td><td>Level 3</td><td>Level 4</td></tr><tr><td rowspan="14">A. Location and environmental attributes</td><td rowspan="5">1. Efficiency of the aspects of location</td><td>1.1. Lot level</td><td>1.1.1. Aspects related to the location</td></tr><tr><td>1.2. Street level</td><td>1.2.1. Physical characteristics</td></tr><tr><td></td><td>1.2.2. Economic and social aspects</td></tr><tr><td>1.3. Block level</td><td>1.3.1. Physical characteristics</td></tr><tr><td></td><td>1.3.2. Economic, social and demographic aspects</td></tr><tr><td rowspan="3">2. Quality of the general environment</td><td>2.1. Lot level</td><td>2.1.1. Aspects related to the soil</td></tr><tr><td>2.2. Street level</td><td>2.2.1. “Urban bothers”</td></tr><tr><td>2.3. Regional level</td><td>2.3.1. Aspects related to the quality of the air and the water</td></tr><tr><td rowspan="6">3. Quality of the environment and impacts on the user</td><td>3.1. Impacts on the comfort of the user</td><td>3.1.1. Aspects related to the interior environment</td></tr><tr><td></td><td>3.1.2. Aspects related to the exterior environment</td></tr><tr><td></td><td>3.1.3. Aspects related to the neighboring space</td></tr><tr><td>3.2. Impacts on the health of the user</td><td>3.2.1. Aspects related to the interior environment</td></tr><tr><td></td><td>3.2.2. Aspects related to the exterior environment</td></tr><tr><td></td><td>3.2.3. Aspects related to the construction</td></tr><tr><td rowspan="22">B. Structural, physical and intrinsic attributes</td><td rowspan="18">1. Efficiency of the constructive aspects</td><td>1.1. Structural quality</td><td>1.1.1. Foundations</td></tr><tr><td></td><td>1.1.2. Superstructure</td></tr><tr><td>1.2. Safely against fire</td><td>1.2.1. Passive safety</td></tr><tr><td></td><td>1.2.2. Active safety</td></tr><tr><td>1.3. Security against intrusion</td><td>1.3.1. Passive security</td></tr><tr><td></td><td>1.3.2. Active security</td></tr><tr><td>1.4. Ambient comfort</td><td>1.4.1. Thermal comfort</td></tr><tr><td></td><td>1.4.2. Acoustic comfort</td></tr><tr><td></td><td>1.4.3. Illumination and natural ventilation</td></tr><tr><td></td><td>1.4.4. Artificial illumination</td></tr><tr><td>1.5. Quality and durability of nonstructural materials</td><td>1.5.1. Interior of the building</td></tr><tr><td></td><td>1.5.2. Building envelope/external renderings</td></tr><tr><td>1.6. Efficiency and maintenance of installations</td><td>1.6.1. Water supply</td></tr><tr><td></td><td>1.6.2. Draining of sewers and pluvial waters</td></tr><tr><td></td><td>1.6.4. Gas supplying</td></tr><tr><td></td><td>1.6.5. Electric energy supplying</td></tr><tr><td></td><td>1.6.6. Communications and media</td></tr><tr><td></td><td>1.6.7. Mechanical equipment</td></tr><tr><td rowspan="4">2. Efficiency of the use of the spaces</td><td>2.1. Space conception of private zones</td><td>2.1.1. Spaces assignment</td></tr><tr><td></td><td>2.1.2. Organization of the spaces</td></tr><tr><td>2.2. Use of common zones of the building</td><td>2.2.1. In the building</td></tr><tr><td></td><td>2.2.2. In the involving space</td></tr></table>

Code of Practice of BSRIA [17], and GBC '98 — Green Building Challenge 98 [13].

Some econometric approaches are also used for this purpose, such as those using multiple linear regression analysis to assess a hedonic price function [1,6,9,19,20,24].

Given the number and complexity associated with the attributes to be used in multicriteria housing evaluation, the first problem to be solved was their organization in a convenient structure in order to:

\- facilitate the communication, analysis and decision aid for the user;

\- turn adequate the resulting structure of attributes for the creation of a DSS using a relational Data Base Management System to store the data.

Therefore, in our analysis the aim was not only to identify the largest possible number of these attributes, but also to organise and classify them in a flexible structure of attributes hierarchy (see also [32]), allowing to start from global high level categories (e.g., Housing Quality: Location and Environment attributes) and successively subdividing them into more specific attributes which may be quantified directly [14]. This structure can be represented in the form of a tree as the one shown in Fig. 1.

Initially about 300 attributes were identified, which have been organised in a hierarchy of 6 levels (each level may be viewed as a consistent family of attributes). A further analysis led to the simplification of those that are more difficult to understand and/or quantify (mainly in the point of view of the common consumer). We finally obtained a set of 210 attributes that were organised in 6 levels as shown in Fig. 1.

The highest level of the hierarchy (level 1) contains two categories: A — “Structural/Physical/Intrinsic” attributes, and B — “Location and Environment” attributes. Some methodologies already exist for establishing a hierarchy and quantifying the attributes in the category A, e.g. [14,27,32]. However, this is not the case for category B given the difficulties to understand how socio-economic factors operate in the different space scales, and how they contribute to the evaluation of real estate market [33]. Despite the fact “…that the most important factors in determining the value of an house are its location, location and location... and if there was to exist one fourth factor it would be location…” [33], there are very few studies covering this topic. Using a structure with various levels, we intend to overcome most of the more common problems, since the consideration of multiple space scales of the urban environment (e.g.: lot, street, city block, region) is crucial to evaluate correctly the influence of location in housing value [28].

An example of part of the hierarchy of criteria (level 4 depth) is presented in Fig. 1 and further described in Table 2.

## 3. The decision support system

Due to the diversity and complexity of the attributes, their inter-relationships, and the volume of information involved, the system to be used in the analysis must be efficient, effective and easy to use. The linkage of Information Systems (IS) and formal decision support models whose attributes are structured in a hierarchical structure is a promising way to analyse housing markets.

To be effective an IS must organise information in a way that it is useful when extracted, facilitate the access to and the management of information, readily accommodate updates in data and analytical programs, and is easily understood by users in an operational perspective.

The definition and pursuit of these goals has been a fundamental cornerstone in the development of the system presented in this paper.

## 3.1. DSS architecture

The DSS developed in this work is aimed at providing decision aid in several functions: property value assessment, evaluation of its quality, and support consumer choice. It is composed of (Fig. 2):

i) a database, implemented with a relational data base management system;

ii) a decision support methods base including methods such as the Simple Additive Weighting SAW [12,21,34]; TOPSIS — Technique for Order Preference by Similarity to Ideal Solution [23,34]; and methods of the ELECTRE (Elimination and Choice Translating Reality) family, such as ELECTRE I and ELECTRE TRI [29,30,31,35];

iii) an interface designed to be user-friendly and intuitive for the user.

The interface allows the user not just to apply one of the available decision support methods, but also to edit or visualise the data stored in the database. The user can create, modify or eliminate attributes and evaluations, or even define which attributes he/she intends to inquire about. The user can also publish this information on a client/server environment and/or the Internet, in a fully automatic and transparent way (the development environment used – 4th Dimension and 4D Server – enables to perform these operations directly).

![](/api/attachments/65UHXHF3/fulltext/images/ee8b0b1ff27a6d4f2066329ef4ab8bae933a56f5862cb29d2ee0afb1804af50c.jpg)  
Fig. 2. DSS architecture.

## 3.2. Structure of the database management system

The relational database management system (RDBMS) used for the development of this work was 4th Dimension (4D) and 4D Server (www.4d.com). It includes a 4th generation programming language, which allows a full integration of data manipulation with models through graphical interfaces. 4th Dimension has its own programming language consisting of over 500 commands. The 4th Dimension language is made up of various components (data types, variables, operators, expressions, commands and methods) that help to perform tasks and manage the data. A method is a series of instructions that causes 4th Dimension to perform a task. Five types of methods can be distinguished: Object Methods, Form Methods, Table Methods/Triggers, Project methods, and Database methods [15].

The 4th Dimension language is a simple yet powerful language when compared with traditional computer languages. Unlike in traditional languages, in which objects must be defined and pre-declared in formal syntactic terms, objects are created in a simple manner (for example, to use a button the user just needs to draw it on a form and name it) and 4th Dimension automatically manages the object (for example, automatically notifying the methods whenever the user clicks the button) [15].

The system developed includes 119 database tables, 62 procedures specifically developed for this project (project methods) and 275 forms/subforms.

The main components of the RDBMS are:

\- The database of attributes that contribute to characterise the value of a property, which can be edited by the user. However, different permissions for each profile of user were created to guarantee the integrity and coherence of the data.

\- The database of evaluations that contains a description of existing evaluations, and can provide parameters for future evaluations via statistical methods such as multiple regression.

\- The database of inquiries that contains the set of answers to the inquiries previously carried out. This enables, for instance, the construction of user profiles, including the importance assigned to the multiple evaluation attributes.

\- The database of available properties that contains the set of all available properties for evaluation and/ or selection. For instance, users searching for a house can apply filters according to his/her aims and preferences (prices, locations, number of rooms, need of urgent repairs, etc.).

In Fig. 3 a part of the entity/relationship model is presented.

## 3.3. The decision support methods

One of the main concerns in the design and development of this DSS has been offering the users a flexible and easy to use environment, yet powerful and technically sound, capable of providing them assistance to help understand and shape their options and preferences through interactive analysis and experimentation.

![](/api/attachments/65UHXHF3/fulltext/images/8f8a85ab713ac868ea8d2d54689f2342e7d0e184a1aab330afe4fae2211c105f.jpg)  
Fig. 3. Example of an entity/relationship model.

The component decision support methods offers a set of techniques that provide guidance and coherence to the decision adding process. These techniques (SAW/ TOPSIS and ELECTRE methods) can be broadly categorised as compensatory and non-compensatory, being also different regarding the preference information required from the DM and the type of output provided. Another difference concerns to the relative vs absolute judgment of alternatives, which is relevant in the context of our study. In the first case, alternatives are directly compared one to each other and the results are expressed using the comparative notions of “better” and “worse”. In the second case, each alternative is considered independently from the others to determine its intrinsic value by means of comparisons to norms or references. In this case results are expressed using the absolute notions: “assign” or “not assign” to a category; “similar” or “not similar” to a reference profile; or “adequate” or “not adequate” to some norms [25]. This methodological feature is relevant in the context of our problem, since the assignment of houses to pre-defined classes is usually required in problems faced, for instance, by central/local government agencies and financing institutions.

TOPSIS [23,34] is based on the idea that the best compromise alternative is the one that has the minimum distance to the ideal solution (i.e. a solution, usually not feasible, composed of the best possible values for the attributes) and the maximum distance to the anti-ideal solution (i.e. a solution, usually not real, composed of the worst possible values for the attributes). This method belongs to the group of complete aggregation methods that compute an aggregate performance for each alternative. Consequently, it provides a complete ranking of the alternatives based on those values of overall performance (Fig. 4).

The interface allows the user to experiment with different values of the weights for the criteria and observe the respective effects on the house rankings obtained.

Both SAW and TOPSIS allow for compensation between criteria and are based on simple and intuitive principles, yet quite disputable ones mainly regarding the role of weights. However, in many situations (and especially when it concerns real estate), a very good performance in one criterion may not compensate a low score in another criterion. Other methods, such as the ELECTRE family, were developed to overcome this limitation.

ELECTRE methods rely upon the construction and the exploitation of the outranking relation in face of the problem to be tackled (selection, ranking or assignment). To say that “alternative a outranks alternative b” means that “a is at least as good as b”. The main feature of ELECTRE methods, which is relevant in the context of our study, is their intrinsic non-compensatory nature. That is, a very bad performance on a given evaluation aspect (criterion) cannot be compensated by good scores on other criteria. Furthermore, ELECTRE methods accommodate in a natural way the imprecision and uncertainty inherent to Human decision processes by relying on the use of (indifference, preference and veto) thresholds. ELECTRE methods also allow for incomparability between alternatives whenever, with the available information, there is no clear evidence in favour of one of them (which is not the same as indifference between the alternatives). The validity of the assertion “alternative a outranks alternative b” is verified using the concordance (a majority of criteria supports it) and non-discordance (no criterion is strongly opposed to it) principles. Weights in the framework of ELECTRE methods do not depend on the nature of the criterion scales. Therefore, these weights possess the true meaning of relative importance given to the distinct criteria. In this way, weights in the framework of ELECTRE are different of weights used in SAW and TOPSIS, which in these cases can be interpreted as rates of transformation into a common utility/value unit.

![](/api/attachments/65UHXHF3/fulltext/images/e06c672ee846e7a9b51ec4c389afc7da9a2c10a7d7cf1e269566b568b5317c97.jpg)  
Fig. 4. TOPSIS results.

ELECTRE I (and its variants Is and Iv) is devoted to the selection problem. ELECTRE TRI is dedicated to the assignment problem, where the aim is to assign each alternative to one of a pre-defined set of (ordered) categories or classes. For the definition of the limits of these classes, standard or reference actions that the user can select within the information system may be used. Other important characteristic of ELECTRE TRI, for the analysis of this kind of problems, is that it comprises the concept of pseudocriterion. In the case of a real-criterion, action a and b are indifferent according to this criterion only if their performance is equal. In the case of a pseudocriterion, indifference is extended to a zone where the difference between a and b is below a given threshold, while between the zone of indifference and the zone of strict preference there is a zone of weak preference, which indicates a hesitation between indifference and strict preference.

The user can interact with the DSS in several phases of the decision process. In a first phase he/she can filter and select, from the available properties in the system, those that according to some characteristics fit in his/her preferences (for instance, he/she is interested in houses with more than two rooms or houses located in the north part of the city only, or any logical combination of this type of preliminary conditions). The technical parameters required by the methods, such as weights or the thresholds of indifference, preference and veto in ELECTRE (Fig. 5), are freely defined by the user, thus giving him/her full control of the decision process. Fig. 6 displays the outranking relationships generated by ELECTRE I method on a set of alternatives (houses 28 and 34 would be the best choices).

<table><tr><td rowspan="2">Name</td><td rowspan="2">Weigth</td><td colspan="3">Thresholds</td></tr><tr><td>Indiffer.</td><td>Prefer.</td><td>Veto</td></tr><tr><td>01 - LOCALIZATION AND AMBIENT ATTRIBUTES</td><td>30.00</td><td>0.20</td><td>0.40</td><td>1.00</td></tr><tr><td>01 - Efficiency of Localization Aspects</td><td>25.00</td><td>0.35</td><td>0.80</td><td>2.10</td></tr><tr><td>01 - Lot level</td><td>50.00</td><td>0.45</td><td>1.10</td><td>1.80</td></tr><tr><td>02 - Street level</td><td>30.00</td><td>0.75</td><td>1.20</td><td>1.75</td></tr><tr><td>03 - Block Level</td><td>20.00</td><td>0.45</td><td>0.80</td><td>1.85</td></tr><tr><td>02 - Quality of the General Environment</td><td>40.00</td><td>0.60</td><td>1.40</td><td>2.00</td></tr><tr><td>01 - Lot level</td><td>10.00</td><td>0.25</td><td>0.45</td><td>1.00</td></tr><tr><td>02 - Street level</td><td>35.00</td><td>0.80</td><td>1.40</td><td>1.75</td></tr><tr><td>03 - Region Level</td><td>55.00</td><td>0.65</td><td>1.25</td><td>1.60</td></tr><tr><td>03 - Quality of the Environment and Impacts on the User</td><td>30.00</td><td>0.40</td><td>0.80</td><td>1.00</td></tr><tr><td>01 - Impacts on the Comfort of the User</td><td>35.00</td><td>0.90</td><td>0.80</td><td>2.50</td></tr><tr><td>02 - Impacts on the Health of the User</td><td>65.00</td><td>0.75</td><td>1.05</td><td>2.00</td></tr></table>

Fig. 5. Defining the weight (importance) and thresholds of each criterion.

In the framework of ELECTRE TRI, the DSS classifies the selected alternatives according to the type of assignment, pessimistic or optimistic, depending the degree of exigency of the DM (Fig. 7). The DSS also allows the DM to perform a sensitivity analysis to identify the influence of variations of the threshold values in the outranking results. This possibility makes ELECTRE methods, in the operational framework of this DSS, more adequate since in this manner the common attitude of DMs, which is usually characterised by a gradual transition from the indifference to the preference state, can be better captured. Furthermore, the introduction of thresholds provides a technically sound way to deal with the uncertainties stemming from different sources (not just regarding preferences, but also lack of data precision).

![](/api/attachments/65UHXHF3/fulltext/images/d91d34e68f1aadfb1c13759203a06e290704b2da07333be215520cbd28255d71.jpg)  
Fig. 6. ELECTRE results — representation of outranking relationship.

![](/api/attachments/65UHXHF3/fulltext/images/849cb2e58122423522540370ff66a27186fb5f36a5864412cd5e0ce895f47bdc.jpg)  
Fig. 7. ELECTRE TRI — assignment results.

ELECTRE TRI is particularly adequate for the qualification of housing alternatives, allowing to define reference properties (for example, according to consumer profile) and to group/classify them in classes.

The DSS enables the results to be visualised on a map (Fig. 8), where the houses under evaluation appear duly located, with colours that represent the respective classifications. This feature is useful for a municipal agency to do a housing quality map for planning purposes, for instance for prioritising intervention (as a owner, which is often the case in Portugal, or enforcing owners to do so in the framework of historical centres rehabilitation plans; see [5]).

## 4. Conclusions

Housing evaluation involves the analytical and systemic determination of all the factors influencing the value of a property, supported in clear principles and using welldefined criteria. The process of evaluation should be scientifically sound, and its adequate application depends not just on the quality and amount of the information gathered but also on the features offered to the user. The integrated information/decision support system presented in this paper is aimed at offering the users (consumers, government or municipal, agencies, promoters, etc.) a flexible and user-friendly environment based on formal multiple criteria methodologies to assist them in keeping and structuring information, obtaining historical and statistical analysis, and providing decision aid by enabling to rationalise the comparisons among non-dominated alternatives in construction and housing evaluation, both for experts and consumers with no technical knowledge.

![](/api/attachments/65UHXHF3/fulltext/images/7a2b52214be89f7319bec878d7849e76b9450d2f2c659d155eca0f4b860742b5.jpg)  
Fig. 8. ELECTRE TRI — map with assignment results.

The visualisation on a map of available houses stored in the database, assisting the user to locate the property in its actual environment, and the possibility of automatic representation of characteristic dependent maps (value maps, quality maps, etc.), provides a value-added for the analysis and the perception of the spatial variation of qualitative and/or quantitative indicators [11].

## Acknowledgments

This research was supported in part by grants from FCT-Portugal (R and D Projects POCTI/ECM/34529/99 on “Decision Support for Planning Logistics and Transportation Infrastructures using GIS Technologies” and POSI/SRI/37346/2001 on “Models and algorithms for tackling uncertainty in decision support systems”).

## References

[1] W. Archer, D. Gatzlaff, D. Ling, Measuring the importance of location in housing price appreciation, Journal of Urban Economics 40 (1996) 334–353.

[2] Association Qualitel, Guide Qualitel (Paris, 1993).

[3] Association Qualitel, Le Guide Pratique du Label Qualitel (Paris, 1999).

[4] P. Balchin, The Housing Policy in Europe, Ed. Routledge (London, 1996).

[5] C.A. Bana e Costa, R.C. Oliveira, Assigning priorities for maintenance, repair and refurbishment in managing a municipal housing stock, European Journal of Operational Research 138 (2) (April 2002) 380–391.

[6] I. Bateman, The effect of Road Traffic on Residencial Property Values: A Literature Review and Hedonic Pricing Study, Ed. Scottish Executive, UEA Norwich/ESRC/UCL (Scotland, 2001).

[7] V. Bonnet, J. Roman, S. Sidoroff, D. De Valicourt, H. Penicaud, Assistance to green building projects through the BATIMPACT method, Deuxiéme Conférence Internationale du CIB-TG8, Paris, France, 1997

[8] BRE – Building Research Establishment, BREEAM – Building Research Establishment Environmental Assessment Method / New

Homes, An Environmental Assessment for New Homes, Ver. 3/91, (Reino Unido, 1991).

[9] A. Can, Specification and estimation of hedonic housing price models, Regional Science and Urban Economics 22 (1992) 453–474.

[10] H.M. Carreira, Projecto de Reforma da Tributação do Patromó- nio, Cadernos de Ciência e Técnica Fiscal, Comissão da Reforma da Tributação do Património, Centro de Estudos Fiscais, Direcção-Geral dos Impostos, Ministério das Finanças, Lisboa, 1999, (in Portuguese).

[11] J.R. Carter, On defining the GIS, in: W.J. Ripple (Ed.), Fundamentals of GIS: a compendium, ASPRS/ACSM, Falls Church Virginia, USA, 1989, pp. 3–7.

[12] C.W. Churchman, R.L. Ackoff, An appropriate measure of value, Journal of Operations Research Society of America 2 (2) (1954) 172–187.

[13] R. Cole, N. Larsson, Green Building Challenge “98”, Deuxiéme Conférence Internationale du CIB-TG8 Paris, France, 1997.

[14] J. Costa, Métodos de Avaliação da Qualidade de Projectos de Edifícios de Habitação, Dissertação de Doutoramento, Faculdade de Engenharia da Universidade do Porto (Porto, 1995) (in Portuguese).

[15] David Adams, Programming 4th Dimension: The Ultimate Guide, Foresight Technology, Inc., 1998.

[16] Department for Transport, Local Government and the Regions, HQI — Housing Quality Indicators, UK, 2000.

[17] S. Halliday, Environmental Code of Practice, BSRIA — Building Service Research and Information Association, 1994.

[18] INE — Instituto Nacional de Estatística, CENSUS 2001, (2001).

[19] C. Janssen, B. Söderberg, Estimating market prices and assessed values for income properties, Urban Studies 36 (2) (1999) 359–376.

[20] K. Jones, N. Bullen, A multi-level analysis of the variations in domestic property prices: Southern England, 1980–87, Urban Studies 30 (8) (1993) 1409–1426.

[21] R.L. Keeney, H. Raiffa, Decisions with Multiple Objectives, John Wiley and Sons, New York, 1976.

[22] P.L. Knox, Urban Social Geography: An Introduction, 3th edition, Routledge, 1995.

[23] B.H. Massam, Multi-criteria decision making (MCDM) techniques in planning, Progress in Planning 30 (1) (1988) 1–84.

[24] E. Mills, R. Simenauer, New hedonic estimates of regional constant quality house prices, Journal of Urban Economics 39 (1996) 209–215.

[25] V. Mousseau, J. Figueira, J.-Ph. Naux, Using assignment examples to infer weights for ELECTRE TRI method: some experimental results, European Journal of Operational Research 130 (2) (2001) 263–275.

[26] Office Buildings, BEPAC: Building Environmental Performance Assessment Criteria, Ver. 1, British Columbia, Canada, 1993.

[27] Office Federal du Logement, Concevoir, Évaluer et Comparer des Logements – Système D'Évaluation de Logements (SEL) – Edition 2000, Bulletin du Logement, vol. 35, Granges, 2000.

[28] S. Orford, Valuing the Built Environment — GIS and House Prices Analysis, Ashgate Publishing Ltd, England, 1999.

[29] B. Roy, The outranking approach and the foundations of ELECTRE methods, in: C. Bana e Costa (Ed.), Readings in Multiple Criteria Decision Aid, Springer-Verlag, 1990, pp. 155–183.

[30] B. Roy, D. Bouyssou, Aide multicritère à la décision: Méthodes et Cas, Economica, Paris, 1993.

[31] A. Schärlig, Pratiquer Electre et Prométhée – Un Complément à Décider sur Plusieurs Critères, Collection Diriger L'Entreprise, vol. 11, Presses Polytechniques et Universitaires Romandes, Lausanne, 1996.

[32] J. Wiegand, K. Aellen, T. Keller, Evaluation de Logements – Système d'Évaluation de Logements (SEL) – Edition 1986, Bul. du Logement, vol. 35, Office Fédéral du Logement, Berne, Suisse, 1993.

[33] A. Woolery, Property Tax Principles and Practice, LRTI/LILP, Cambridge, 1989.

[34] K.P. Yoon, C.L. Hwang, Multiple attribute decision-making: an introduction, Sage University papers, Series on Quantitative Applications in the Social Science 104 (13) (1995).

[35] W. Yu, ELECTRE TRI: Aspects méthodologiques et manuel d'utilisation, Université Paris — Dauphine, Document du LAMSADE, vol. 74, Avril, 1992.

Eduardo Natividade-Jesus received his M.Sc. degree in Civil Engineering (Construction Sciences) from the University of Coimbra in 2002. He is a professor at the Department of Civil Engineering, Polytechnic Institute of Coimbra - School of Engineering, and a researcher in the R&D unit INESC Coimbra. His research interests include multiple criteria programming, spatial decision support systems, housing and urban renovation planning.

João Coutinho-Rodrigues received his Ph.D. in Civil Engineering (Optimization and Decision Support Systems) from the University of Coimbra in 1993. He is an associate professor at the Department of Civil Engineering, University of Coimbra, and a researcher in the R&D unit INESC Coimbra. His research interests include multiple objective programming, spatial decision support systems, project management, and transportation, urban and regional planning.

Carlos Henggeler Antunes received his Ph.D. degree in Electrical Engineering (Optimization and Systems Theory) from the University of Coimbra in 1992. He is a full professor at the Department of Electrical Engineering and Computers, University of Coimbra, and the director of the R&D unit INESC Coimbra. His research interests include multiple objective programming, decision support systems, and energy planning.
