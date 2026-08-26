---
otero_id: 17500
otero_key: "B7KU59TZ"
title: "Knowledge-based model validation support for end-user computing environments"
authors: "Ritu Agarwal; Mohan Tanniru; Yimin Zhang"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00039-u"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-based model validation support for end-user computing environments

Ritu Agarwal $^{a,*}$ , Mohan Tanniru $^{b,1}$ , Yimin Zhang $^{c}$

$^{a}$ Department of MIS and Decision Sciences University of Dayton Dayton, OH 45469-2130 USA $^{b}$ School of Management Syracuse University Syracuse, NY 13244-2130 USA $^{c}$ East China University of Technology Shanghai 200093 People's Republic of China

## Abstract

Encouraging individuals to use corporate data and build computer-based decision models locally, while simultaneously ensuring that the modelling activity is consistent with corporate policies and guidelines poses a challenge to many organizations. Although it is desirable to encourage user autonomy in decision making, it is equally imperative to assure appropriate quality of the decisions made. In this paper interdependencies within the organizational decision making activity are used to identify some generic categories of support required to maintain consistency and quality in end-user model construction. Five distinct cases of model building activity in an end-user computing environment are described and support for ensuring consistency in user constructed models for two of these cases is discussed. An object-oriented knowledge-based system that provides such support has been developed; the architecture of this system is described. System implementation and interaction is illustrated with the aid of a financial budgeting application.

Keywords: End-user computing; Model validation; Knowledge-based system; Object-oriented system

## 1. Introduction

The Pentagon estimates that at current rates of demand for software by the year 2010 the United States will require 60 million software professionals -approximately half the US labour force. With the increase in the number of software professionals not keeping pace with escalating demand, the corporate response has been to increasingly decentralize systems development activities to end-users; i.e., to actively encourage and facilitate the phenomenon of end-user computing. Fuelled by the availability of high-level, user-friendly software, firms are witnessing a significant growth in the development of information technology applications for supporting individual decisions by non-traditional developers such as managers.

The proliferation of end-user computing (EUC) has raised many concerns about the effective management of this process (Rockart and Flannery, 1983;Alavi et al., 1987;Munro et al., 1987;Brown and Bostrom, 1989). Prior studies have examined (both empirically and conceptually) many different aspects of EUC, including computing policies (Galletta and Hufnagel, 1992), structural alternatives for managing EUC (Brown and Bostrom, 1989), controls (Munro et al., 1987), support through information centres and other organizational initiatives (White and Christy, 1987), etc. A common thread underlying these studies has been on the macro level control of EUC; they all attempt to understand the phenomenon and prescribe methods to manage its organizational dissemination effectively. However, while broader organizational initiatives such as the establishment of guidelines for hardware/software acquisitions in order to manage training and maintenance support effectively are no doubt essential to the control of EUC, of equal importance are some micro-level control issues. Currently there are limited effective means to ensure that the actual processing done by individual managers, using these end-user tools, is correct. In this paper we focus on this specific micro-level aspect of end-user computing: the utilization of data and models by end-users as they build decision support systems (DSS) to support individual decision making.

The integrity of data, when it is accessed by many individuals for distributed access and processing, is often the responsibility of a data base administrator and DBMS software. However, such responsibilities do not address issues related to an accurate use of these data in models developed by end users. A dangerous consequence of decisions made using models which make wrong assumptions about key elements such as organizational operations, environmental and temporal effect on decision variables, the relevance of algorithms in solving certain problem conditions, etc., is that they may yield results which are unrealistic. When the results of such models update corporate data bases, most procedures that are in force today cannot verify the validity of these data, except for simple format, range, and reasonableness checks. It is thus incumbent upon the user to ensure that the models and data used are valid and the decision outcomes realistic.

Some attempts have been made to ensure that a user considers various assumptions underlying the algorithms used in problem solving by an automatic formulation and/or selection of such algorithms based on certain problem characteristics (Ghosh and Agarwal, 1991; Hong and Vogel, 1991; Krishnan, 1990; Krishnan, 1991; Murphy et al., 1992). Such approaches have limited domains of applicability; they are appropriate in instances when the modelling formulation requires the use of algorithms such as forecasting and mathematical programming techniques. A significant proportion of modelling at the EUC level, however, is oriented towards the use of spreadsheet type formulations, where the model utilizes several discrete computational steps that are often problem dependent and do not conform to any well defined structure for performing validation.

In a recent study Silver (1991) proposes a ‘decision guidance’ framework to analyze support requirements when significant judgements are involved in the decision process and its inputs. He defines decision guidance as proactive support where a system enlightens or sways its users as they structure and execute their decision making processes. The extent of guidance a system can provide is dependent on the degree of autonomy the user has in constructing models and making judgements, as well as the nature of the task itself. The greater the autonomy and more complex a user’s perceptions of the decision making task, the greater the need for guidance. The type of guidance provided can vary anywhere from one of prescribing and proscribing an approach to solve a problem, to one of simply providing relevant information.

The objective of this paper is to describe methods that provide the needed guidance at appropriate times to ensure that individual managers are made aware of information that might affect the construction and use of models in their decision process. An underlying assumption behind these methods is that it is desirable to provide the user with autonomy in model construction. Specifically, we will limit our discussion of guidance support to three areas: What types of guidance are essential for model validation – i.e., are there any generic support needs for decision guidance? When, during the modelling activity, should such guidance be provided? How does one incorporate this guidance when DSSs are built?

The issue of the impact of such guidance on the decision process and/or outcome is also important, but will not be considered in this research.

The decision process framework developed by Thompson (1967) is used in section 2 to establish the types of guidance that are considered appropriate to self-validate models built by the user. Decisions related to when to provide such guidance is a function of what knowledge the system has about the modelling activity at a specific point in time. While dynamic tracking of user interaction and behaviour for providing context sensitive help at appropriate junctures is most desired, we will limit our discussion here to providing support at specific modelling activity steps (a form of deliberate decision guidance). Section 3 provides a typology for classifying the model building activity so that we can isolate those modelling steps where validation support is appropriate. Section 4 discusses a knowledge-based approach to implement this support during the model building activity of a user. Note that the support provided assists a manager in executing the decision process (as opposed to structuring it) by providing relevant information (rather than suggesting a particular action) in a predefined (as opposed to dynamic or participative) mode of operation. Section 5 illustrates the use of this support for a financial budgeting application and compares our approach to previous work in model management. The final section provides some concluding comments and directions for future research.

## 2. Establishing support features for model validation

Model building is recognized as one of the three components in the design of DSS, the other two being dialogue management and data management (Sprague and Carlson, 1982). Although some research in DSS has focused on micro-level (end user) computing activities such as model formulation (Dolk and Konsynski, 1984; Murphy et al., 1992), and model construction (Krishnan, 1991), not much has been written about model validation, even though this has been discussed in the literature as an important component to ensure overall consistency in the decision making process. Certain micro-level verification at the statement level has been proposed (Blanning, 1985), but such a verification is cumbersome and ignores the issues of autonomy of the decision maker.

One may argue that a micro-level validation of a user's model is a non-issue as the use of data and the formulation of decision models, computer based or non-computer based, is the responsibility of individual managers. Since one's job performance is based on the decisions made, there is sufficient incentive for a manager to seek out the best and the most accurate information possible to arrive at a decision. Several factors can make this claim somewhat suspect, however.

First, the perception of validity that comes with computer based information may inhibit a manager from continuously questioning the model's underlying assumptions, especially when the judgements made in constructing the model are temporally sensitive. Second, the speed with which information is transmitted and communicated to others via networks makes it easy to propagate an incorrect decision faster, even if such an error is later recognized and corrected. Third, the sheer volume of information that is being made available today to end users to support decisions can make the process of tracking and challenging the assumptions and judgements that went into model construction difficult. This situation is further aggravated when the model user is not often the model builder. Finally, even if the ultimate responsibility for the decision made rests with the manager, it is often difficult to isolate the source of a bad decision due to the interdependent nature of many of today's complex decisions and the role of multiple sources of data used to support them. It is often easy to blame the system under these conditions for improper decisions, rather than the individual who is involved in making the decision.

These difficulties should not lead one, however, to resort to centralized decision making where a single or a group of models at the corporate level support all the decision processes, as this detracts from the autonomy of the individual

decision maker. What is required is a guidance or support mechanism that provides managers with relevant information, makes them aware of the nuances of the model built and the assumptions and judgements made about the data used in model execution, so that these are taken into consideration each time a decision is made. This type of guidance is critical specifically in situations such as budgeting and resource allocation, where the data generated by one individual has a significant and immediate impact on others. In a recent article Senge and Sterman (1992) evocatively characterize this problem in the following statement: “local decision making and individual autonomy lead to management anarchy unless managers account for the interconnections and long-term side effects of their local decisions”. Although the group decision support system literature addresses the issue of providing information for member interaction, assumption surfacing, etc. (Gray and Nunamaker, 1989), its focus is more geared to resolving conflicts and reaching a consensus, and not on ensuring that the models used by individual managers to arrive at their decisions are valid.

Assuming that support for model validation is to occur at the individual decision level without significantly affecting the autonomy a user enjoys in making decisions, our objective is to determine the type of information that can support such validation. This may include information such as assumptions made by others in similar situations, potential error propagation from the inputs used if the assumptions and judgments are not valid, the clarification of concepts that have multiple meanings, etc. The underlying notion behind such support is to reduce the distance between an individual's mental model of a decision situation

## Table 1

Dependency categories and information support to manage reciprocal interdependency

Pooled interdependency: Each unit can perform its own activities without regard to the other units and yet makes a contribution towards the organizational objective. Each unit is, in turn, supported by the organization.

Sequential interdependency: Each unit, while maintaining pooled interdependency to achieve overall organizational objectives, may also depend on other units to complete their normal operations.

The degree of one unit's dependence on other units varies significantly among units.

Reciprocal interdependency: Each unit, while remaining pooled and sequentially dependent, may be recursively dependent, i.e., output of a unit X may become the input of another unit, Y, the output of Y may be the input for unit Z, and finally, the output of Z may be the input for X. In this case each unit has to constantly adjust to other units' activities, thus making the dependency relatively complex and dynamic.

Information support for reciprocal interdependency: Is the individual unit information lexically correct, i.e., are the variables used known to the organization and do they convey the same meaning to all involved?

For example, the variable 'sales' may connote 'unit sales' to production and 'dollar sales' to accounting.

Is the individual unit information logically correct, i.e., does it make sense to use certain information by a given unit in the context of a decision making process? For example, is it appropriate to use detailed sales data when developing long term financial plans?

Is the use of certain relationships such as accounting identities consistent with normal practice?

For example, did a unit use both earnings before tax and tax to derive earnings after tax?

Is there consistency between the functional and organizational policies, i.e., if the organization has made certain decisions on goals, strategies, and priorities, is this information available to all concerned? For example, if the organization's strategy is to increase market share by cutting prices, then all units need to be informed of this in order to synchronize their activities with that of the corporation, i.e., marketing may use mass advertising rather than selective magazine advertising, production may produce more items for stock rather than tighten inventories, and accounting may plan for an increased cash outflow in the short run.

Is there an internal dependency between various organizational units?

Is the system capable of providing the dependency information when the dependency is not direct, i.e., output of unit X is needed by unit Z via the input/output of unit Y?

Is there a reciprocal dependency between units, i.e., is there a sharing of both inputs and outputs, with or without any intervening units?

and the real-world phenomenon being analyzed; and to do so in an unobtrusive manner by playing the role as an advisor to the decision maker.

The information described above can be provided upon request, but that assumes that an individual user knows explicitly what information to seek at all times. Several times users may not be aware of the information that is available, how such information might impact their decision process, and what underlying assumptions are being made in generating that information. While the support provided to end-users has often been limited to the information they need to effectively make a decision, we cannot ignore the fact that this information is communicated to others who, in turn, treat this as their input. Thus, validation of models used at a local level has to consider decision interdependencies.

Thompson (1967), in his study of organizations, describes three basic levels of interdependencies (pooled, sequential and reciprocal) that may exist among various components of an organization and discusses how these dependencies require different types of information. Table 1 briefly describes each of these dependencies and discusses the information support needed for the case of reciprocal interdependency, as it subsumes the features of the other two dependencies. Table 2 provides a summary of the generic information support needed for decision guidance or model validation under conditions of reciprocal interdependency.

Typically a large portion of this information is not easily available to an end user as s/he embarks on building a model. While it would be desirable to have a generalized model management system (Applegate et al., 1986; Konsynski, 1981) that can coordinate various activities of end users and provide all the needed support, the current state of the art in model management makes this a normative rather than practical goal. The difficulty in accomplishing this objective is similar to the one faced by organizations when a corporate-wide data model has to be designed. The problem in both these cases is one of insufficient information on the organization's requirements for building models or accessing data. Within the context of building a global data model, a reasonable approach is to build an enterprise model incrementally through view integration as individual applications are developed. Similarly, a generalized model management system may be developed over time as modelling knowledge is incrementally added to meet different user needs. In the next section we classify the model building activity of end-users into five distinct scenarios and relate the support needs described above to these scenarios.

Table 2  
Generic information needs for model validation

<table><tr><td>Type of support</td><td>Description</td></tr><tr><td>Assumption</td><td>Information about tools and their underlying assumptions</td></tr><tr><td>Syntax</td><td>Lexically correct use of inputs and outputs (are the variables used by individuals the same as defined by the corporation?)</td></tr><tr><td>Semantic</td><td>Logically correct use of inputs and outputs (is the use of variables appropriate for the decision context? e.g., can we use detailed sales data by product when planning in aggregate?)</td></tr><tr><td>Identity</td><td>Consistent use of identities based on normal practice</td></tr><tr><td>Organizational context</td><td>Consistent use of policies, as prescribed by the organization or some functional unit</td></tr><tr><td>Dependency information</td><td>Degree of dependency that exists between those that use this model&#x27;s output and vice versa</td></tr><tr><td>Dependency execution</td><td>Extent of dependency: sequentially dependent or reciprocally dependent and how the dependencies manifest themselves in operations</td></tr><tr><td>Problem processing</td><td>Definition of models based on problem articulated or query posed by user</td></tr></table>

## 3. Validation support for alternate end-user computing environments

In general, support at an individual decision level can manifest itself in a range of services extending from providing simple access to predefined data and models/tools to those which require constructing a sequence of models to satisfy a user need. Several scenarios are presented below to illustrate the different types of model building activities users may engage in and the support/guidance a system can provide in each of these cases.

End user model construction typically includes the definition of one or more of the following components: input variables whose values come from external sources (I), input variables whose values are internally defined and under the control of the user (endogenous/parametric input (P)), model formulation (M) that relates all the input variables to output variables (O), and specialized algorithmic procedures or tools (T) that may be needed to execute the user's model and generate outputs. An end user may need information on any or all of these components depending on the task being performed. Validation complexity is directly related to the extent of control being exercised by a user over the five components. For example, validation is relatively easy if the system constructs or extracts model(s) based on a user query, as it can use known, established and validated models that are stored in the corporate knowledge base. However, as the user takes control of a larger number of these components, validation becomes more challenging, since the system has limited knowledge about the user's intent. Five different model building environments are presented below in order to understand the breadth of support requirements for validation.

Table 3  
Examples describing five distinct cases of model use  
```txt
Case Model usage
(a) Sales of bobsleds by Toyco in 1983?
(b) Sales of bobsleds by Toyco in 1983?
Price is $12.00. Change in price? ——
Credit ratio (credit to cash sales) is 0.5. Change? ——
(c) Sales of bobsleds by Toyco in 1983?
Price is $12.00. Change in price? ——
Credit ratio (credit to cash sales) is 0.5. Change? ——
CGS = forecast (sales)
Choose the appropriate option for forecast from: REGRESSION; EXPonential SMOOTHing ——
(d) Profit model
REM input (system provided) definition
Sales (1987) = derived by MMS
Interest (1987) = derived by MMS
REM parameter input definition
cs factor = 0.45
adv factor = 0.12
REM model definition
CGS = cs factor * sales
Operating expense = REGRESS (sales)
Promotion expense = adv factor * sales
Profits = sales -CGS -promotion expense -interest -operating expense
PS ratio = profits/sales
(e) Profit model
.....................
Sales (1987) = data from data base
Interest (1987) = data from data base
.....................
Operating expense = REGRESS (sales)
....................
```

Case 1. The user provides either the name of the model that is predefined or defines a query. The system validates the user's query (or output desired) and defines the models and data needed to generate the desired output (See Table 3, Case (a)). Output query validation has been the focus of much research as it dominates the rest of the processing. Query by Example (Zloof, 1975), natural language interfaces (Vassiliou et al., 1983), and semantic nets (Elam et al., 1980) are some methods used to reduce the mismatch between the user's real-world data requirements and the formulation of the query. Model definition based on a validated user query is also the subject of much research. Defining and sequencing models iteratively based on a query until such a process results in data from a data base has been pursued using semantic nets (Bonczek et al., 1981; Elam et al., 1980), predicate calculus (Dutta and Basu, 1984; Bonczek et al., 1984), frames (Dolk and Konsynski, 1984), and relational data bases (Blanning, 1987).

Case 2. This is similar to Case 1, except that a user is allowed to download the model data and perform sensitivity analysis on certain parametric data associated with that model. Validation here is concerned with ensuring that the parametric data that is input by the user for sensitivity analysis is within bounds (see Table 3, Case (b)).

Case 3. In this case, the user has the option to change the tools used to execute the model if the assumptions inherent in the model change over time, thus making the use of existing tools inappropriate. Here the scope of validation extends to the tool identified for incorporation, specifically, the assumptions inherent in the use of this tool and its relevance to the purpose underlying model construction (Table 3, Case (c)).

<table><tr><td colspan="2">Steps Controlled By</td><td colspan="5">Features of Model Validation System (MVS)Validation: (*) Definition (@)</td></tr><tr><td>SYSTEM</td><td>USER</td><td>OUTPUT</td><td>PARAMETERS</td><td>TOOLS</td><td>MODELS</td><td>INPUTS</td></tr><tr><td>I M T P</td><td>O</td><td>(*)</td><td>(@)</td><td>(@)</td><td>(@)</td><td>(@)</td></tr><tr><td>I M T</td><td>P O</td><td>(*)</td><td>(*)/(@)</td><td>(@)</td><td>(@)</td><td>(@)</td></tr><tr><td>I M</td><td>T P O</td><td>(*)</td><td>(*)</td><td>(*)/(@)</td><td>(@)</td><td>(@)</td></tr><tr><td>I</td><td>M T P O</td><td>-</td><td>-</td><td>(*)</td><td>(*)/(@)</td><td>(@)</td></tr><tr><td></td><td>I T M P O</td><td>-</td><td>-</td><td>-</td><td>*</td><td>(*)</td></tr><tr><td colspan="7">Note: Once the user defines M, the validation of O and P will not become an issue as these will be a function of the user defined model.Case 1: User defines O, MVS validates O and defines P, T, M, ICase 2: User defines O and suggests values for P; MVS validates O and P, and defines T, M, I.Case 3: User defines O and suggests values for P and T; MVS validates O,P, and T, and defines M, I.Case 4: User defines M and T; MVS validates M and T and defines I (this may require definition of some pre-defined models)Case 5: User defines I, M, and T; MVS validates I, M, and T.</td></tr></table>

Fig. 1. User/system responsibilities in different case scenarios.

Case 4. Here both the model and tools needed are defined by the user, and support is limited to providing the needed input from the corporate data base or from model definitions (if these data are not available from storage and have to be computed). Validation here requires testing the user's model and the tools used (Table 3, Case (d)); there is a paucity of research that suggests how this may be accomplished without compromising the decision maker's autonomy.

Case 5. Here the user defines the model, its input and output, and the tool(s) to be used to complete the task. The support here is limited to one of general information on models of this type and any information on the assumptions made about the data when the particular tool is used. See Table 3, Case (e).

These five cases are summarized in Fig. 1. The environment represented by Cases 4 and 5 (one that is becoming more pervasive with the proliferation of personal computers and high-end modelling software such as spreadsheets) necessitates a higher level of model validation support as the user is taking more control of constructing the model. On the other hand, in Cases 1 and 2, the system does most of the model construction to satisfy a user's query and very little validation is needed, except the reasonableness of the output request or query.

Based upon the nature of the model building activity as discussed above, the support needs for decision guidance vary across the five cases. A mapping between the generic support needs identified in section 2 and the five cases is provided in Fig. 2. The focus of the research here is to provide validation support for Cases 4 and 5 through a knowledge-based support system. The development of such a system that includes assumption, syntactic, semantic, identity and organizational context support is described next.

## 4. A knowledge-based architecture for providing validation support

The knowledge base (KB) needed to support model activities in case scenarios 4 and 5 is discussed first and the implementation scenario is discussed later. This knowledge base may be accessed either directly or indirectly by the user to ensure that the decision model is valid.

<table><tr><td colspan="2">System Support</td><td rowspan="2">Scenario</td></tr><tr><td>Model Definition</td><td>Model Validation</td></tr><tr><td>Dependency Information + Problem Processing $</td><td>AssumptionSyntax/SemanticIdentity/Organizational Context *</td><td>Cases 4 and 5Cases 4 and 5Cases 4 and 5Case 3Cases 1 and 2</td></tr><tr><td colspan="3">* Provide information on other models that are &#x27;similar&#x27; in nature so the user can relate his model with those of others (this requires the storage of each user developed model and the definition of criteria for computing a similarity index so that only relevant models are retrieved)</td></tr><tr><td colspan="3">+ Provide information on other models that need to be executed before the user&#x27;s model if the input used has to reflect a real time operating environment (this can be used in conjunction with group decision making where the link has to bring other users for active participation, or in a static execution of models that are predefined and stored in the model base);</td></tr><tr><td colspan="3">$ Provide support in defining the model itself that needs to be executed to answer a user query (this requires a comprehensive definition of model inputs and outputs and model execution in accordance with some a priori defined sequence);</td></tr></table>

Fig. 2. Model validation support in each case scenario.

## 4.1. The knowledge base

Assumption support for (T): It is incumbent upon the user to find out if the assumptions underlying the use of certain algorithmic tools are satisfied within the problem that is being modeled. For example, while some of the spreadsheet software allows users to call a tool/algorithm such as regress (for regression) or optimize (for running an optimization routine), they do not necessarily check to make sure that the data being acted upon meet the criteria necessary for these tools to apply. The following knowledge about tools is stored for user access: assumptions, applicable situations, related tools (i.e., sub-or super-category of tools with similar characteristics).

![](/api/attachments/B7KU59TZ/fulltext/images/7ec1a642f07c97b309ecdbd628b13ff7a9e341c29f4b9f8e59b2936a712600d2.jpg)

LEGEND:  
![](/api/attachments/B7KU59TZ/fulltext/images/2d5b5aaa01a7f01cc44a5d1b7fdc37d72e975a141d39e5c118d492f4a7356815.jpg)  
Fig. 3. Knowledge base architecture.

Syntax and Semantic support of $(I,P,O)$ : It is important that the user be made aware of the syntactic and semantic meaning associated with the model variables within the organizational context. For example, ‘cost of sales’ and ‘cost of goods sold’ may have different meanings associated with them depending on the context within which they are used, and the same applies when the terms ‘standard costs’ and ‘direct costs’ are used. The knowledge stored about variables includes long names, synonyms, and any other related information.

Identity Support (with regard to M): Computational information associated with certain variables (primarily accounting) should be defined consistently. For example, ‘earnings after tax’ is computed using ‘earnings before tax’ and ‘tax’. Similarly, if a user is estimating financial ratios such as ROI, then questions related to how one computes ROI (are we to use income before tax or income after tax?) or how one arrives at funds flow are relevant. Thus, knowledge about such computational relationships or guidelines should be made available for users’ verification before they use them in their models.

Context Support (with regard to M): In addition, if a user defines a model that has 'profit' as the output, then the system should list all those models that have the same output but different inputs, along with any other information. Also, if a user wishes to estimate values for 'advertising expense', it is useful to know information about other models that are involved in estimating this variable, as well as information about other variables that are defined within this model and any assumptions made in their estimation by these models. For example, a user who is estimating 'advertising expense' may benefit from models that are used to establish corporate marketing strategy, which may emphasize 'mass marketing'. Such related information may help the user stay consistent with corporate strategies. Knowledge stored about models includes input variables, output variables, and contextual information, such as planning horizon, functional area, contact person, etc.

The knowledge base, thus, includes three object classes: TOOLS, VARIABLES, and MODELS. Each of these objects have associated with them certain attributes and methods. See Fig. 3 for a schematic illustration of the KB architecture.

The VARIABLE class has associated with it two additional attributes: uses\_me and generates\_me, along with others such as: long\_names, synonyms and related\_information. The values for these two attributes are dynamically generated by the system by invoking two methods: used\_where and generated\_by\_whom. These methods send messages to the MODEL class and determine the list of models that will use this variable as their input, and estimate its value as a part of their output. This localizes any changes in the model definition to the MODEL class and ensures that the information accessed is always current.

In the knowledge base, the TOOL class can be further subdivided into sub-classes such as forecasting, optimization, etc., and these, in turn, into more specialized sub-classes (e.g. forecasting into time series, regression, etc., and optimization into linear, non-linear, integer, etc.). Since the focus here is on contextual information related to a user's definition of input and output variables, the TOOLS class is kept relatively simple. Future extensions to the implementation will enhance the TOOL class.

Whenever a user identifies input/output variables that are to be used in his/her model, the KB is accessed to list a set of models that have certain contextual similarity. This similarity is established by answering the following questions:

(1) how does this model's output affect other models/users in the system? (method:needed\_by\_whom)

(2) what other models generate values for the same output set? (method:output\_similar\_to)

(3) which models generate the input requested by the user? (method:needs\_who)

(4) what other models use the same input set? (method:input similar)

(5) what models use similar input and output sets? (method: in out similar to)

The objective is to let the user seek informa-

Table 4
Balance sheet and income statement variables

<table><tr><td>Assets</td><td>Liabilities</td></tr><tr><td>A assets</td><td>LE liabilities and equity</td></tr><tr><td>CA current assets</td><td>L liabilities</td></tr><tr><td>C cash</td><td>CL current liabilities</td></tr><tr><td>MS mkt_securities</td><td>AP accounts payable</td></tr><tr><td>AR accounts receivable</td><td>TP tax payable</td></tr><tr><td>PPE prepaid expense</td><td>IP interest payable</td></tr><tr><td>INV inventory</td><td>STD short-term debt</td></tr><tr><td>RI raw material inventory</td><td>LD long-term debt</td></tr><tr><td>SI supplies inventory</td><td>E equity</td></tr><tr><td>WP work in process inventory</td><td>CE common equity</td></tr><tr><td>FI finished good inventory</td><td>RE retained earnings</td></tr><tr><td></td><td>EAT earnings after tax</td></tr><tr><td></td><td>EBT earnings before tax</td></tr><tr><td>FA fixed assets</td><td>OPI operating income</td></tr><tr><td>PE plant and equipment</td><td>SR sales revenue</td></tr><tr><td>CDE cumulative depreciation</td><td>CGS cost of goods sold</td></tr><tr><td></td><td>DE depreciation expense</td></tr><tr><td></td><td>OR other revenue</td></tr><tr><td></td><td>IE interest expense</td></tr><tr><td></td><td>OFE office expense</td></tr><tr><td></td><td>ADE administrative expense</td></tr><tr><td></td><td>TE tax expense</td></tr><tr><td></td><td>DIV dividends</td></tr></table>

tion about these models and assess their relevance to the decision situation at hand. No attempt is made here to select a single, most closely matched model to that defined by the user, even though such a matching is feasible (e.g., by finding models that have both input and output similarity to the user's model). The intersection of the input/output variables of the user's model with those that are stored in the knowledge base are used to answer these questions, and these are generated dynamically by invoking appropriate methods in the MODEL class. The attributes of the individual models can be extracted directly from the knowledge base (as will be seen in the next section). In addition to obtaining related models this way (through user and knowledge base model intersection), one can directly ask for a list of all models in the knowledge base and select those that appear to be appropriate.

## 4.2. System implementation scenario

There are two possible ways a user's model can be validated indirectly. The user can define a model in the modelling environment such as LOTUS 1-2-3 and before its execution, the validation module can be called to ascertain model validity, by answering some of the questions posed earlier. On the other hand, a user can enter the validation module directly and look for appropriate information on tools and variables, before entering the modelling environment to define his/her own models. While the former scenario is most desirable due to its unobtrusive nature and minimal interference with the modelling environment of the user, the current implementation operates under the second scenario. A user enters the 'knowledge base environment' to evaluate the relevance of his/her model definition and the support system uses the object-oriented environment of corporation's ADS/PC software package. The following section illustrates the use of the knowledge base for a financial budgeting scenario.

Table 5  
Some computational identities/relationships

<table><tr><td>GI gross income</td><td>Sales revenue (SR) -cost of goods-sold (CGS)</td></tr><tr><td>EBT earnings before tax</td><td>Gross income (GI) -administrative expense (ADE) -interest expense (IE) -depreciation expense (DE)</td></tr><tr><td>EAT earnings after tax</td><td>Earnings before tax (EBT) -tax expense (TE)</td></tr><tr><td>ROI return on investment</td><td>Earnings before tax (EBT)/assets (A)</td></tr><tr><td>DR debt ratio</td><td>Long-term debt (LD)/assets (A)</td></tr></table>

Table 6
Existing set of budget models

<table><tr><td rowspan="2">Model name</td><td rowspan="2">Output set (O)</td><td rowspan="2">Input set (I)</td><td colspan="3">Model features</td></tr><tr><td>Functional area</td><td>Time horizon</td><td>Plan type</td></tr><tr><td>sales_budget</td><td>SR, AR, C, ADE, FI, CGSUnit Sales (US) Price (P)</td><td>Standard Unit Cost (SC)</td><td>Marketing</td><td>Monthly</td><td>Tactical</td></tr><tr><td>production_budget</td><td>C, WP, RI, SI, FI, Unit Production (UP)Material Level (ML) Equipment Level (EL)</td><td>Unit Sales (US)</td><td>Production</td><td>Monthly</td><td>Tactical</td></tr><tr><td>purchase_budget</td><td>C, AP, LD, PE, SC, RI</td><td>UP, ML, EL</td><td>Purchase</td><td>Monthly</td><td>Tactical</td></tr><tr><td>administrative_budget</td><td>CDE, DE, IP, IE, C, OFE, PPE, WP, TP, TE</td><td>UP, US, P, PE</td><td>Administrative</td><td>Monthly</td><td>Tactical</td></tr><tr><td>accounting_budget</td><td>AR, C, AP, IP, TP</td><td>AR, AP, IP, TP</td><td>Accounting</td><td>Monthly</td><td>Tactical</td></tr><tr><td>funds_budget</td><td>MS, C, STD, E, DIV, LD, OR, IP, IE</td><td>C, MS, STD, E, LD, SR</td><td>Finance</td><td>Annual</td><td>Tactical</td></tr><tr><td>corporate_top_down</td><td>C, AR, INV, FA, CL, LD, CGS, EBT, T, DIV</td><td>SR</td><td>Corporate</td><td>Monthly</td><td>Tactical</td></tr><tr><td>tax_record_planning</td><td>TE, TP, C</td><td>SR, OFE</td><td>Administrative</td><td>Monthly</td><td>Operational</td></tr><tr><td>depreciation_planning</td><td>CDE, DE</td><td>FA</td><td>Administrative</td><td>Monthly</td><td>Tactical</td></tr><tr><td>short_tm_cash_plng</td><td>C, MS, STD, OR, IE, IP</td><td>C, MS, STD</td><td>Funds Mgmt.</td><td>Monthly</td><td>Tactical</td></tr><tr><td>advertising_planning</td><td>C, ADE</td><td>US, P, Credit Terms</td><td>Sales</td><td>Monthly</td><td>Operational</td></tr><tr><td>long_tm_corp_plng</td><td>CA, FA, CL, LD, EAT, DIV, CE, RE</td><td>SR and other market conditions</td><td>Corporate</td><td>Annual</td><td>Strategic</td></tr></table>

## 5. Validation support in financial budgeting -An illustration

Financial budgeting requires the iterative and coordinated application of varying functional expertise to arrive at a single budget. Any system that supports an individual decision maker in this situation has to consider the compatibility of assumptions made by him/her against those that are either pre-established by the corporation or against other models of similar type defined in the past. Such support has to minimally impact the autonomy of the individual decision maker. To facilitate this support, the knowledge base used here contains the definition of all balance sheet and income statement accounts (see Table 4), many financial identities and performance measures (see Table 5), and a variety of models that have been stored for appropriate reference (see Table 6).

A user enters the model validation system (i.e., the validation component of the model management system). A typical interaction with the system is described in Appendix A. The system provides four options: variables, tools, model\_kb (models in the knowledge base) and model\_user (which a user defines interactively for retrieving context sensitive information). Assume that a user wants to define a model that uses variables such as 'standard cost' (SC) as its input and estimates 'sales revenue' (SR) and 'earnings after tax' (EAT). The user may select EAT for additional information on how it is defined and computed. The system provides this information using its own attribute values and other data from the MODEL class, by invoking appropriate methods in this class.

The user wants to use a forecasting algorithm to estimate sales and needs information on the underlying assumptions associated with such tools before calling upon any of these in model construction. The scenario displays information on a particular forecasting algorithm: 'simple regression'.

There are many variables a user may include in his/her model locally such as advertising expense, office expense, other expense, etc. Before any decision is made on the relevance of some of these variables, the user may want to inquire about models that have been defined in the knowledge base that have certain similarity to the model being constructed. The related model information for the user's model (with SC as input, and SR and EAT as outputs) is shown in the scenario described. The contact person is provided, in case more detailed information is needed for analysis, but is not accessible through the knowledge base (since some of the corporate knowledge may be sensitive and cannot be provided for general access).

Note that the information provided is primarily advisory in nature and a user may alter his/her model based on this information before entering the modelling environment for constructing the model. This user defined model and any variables locally defined by the user can be added to the knowledge base after they undergo certain organizational validation and verification checks. This is similar to the practice used by data base administrators when revising corporate data base definitions. Such type of an iterative development of a model base can eventually lead to the generation of a corporate model base.

## 6. Discussion

The validation proposed in this paper is advisory in nature and ultimately it is the user's responsibility to ensure that the models selected for display are examined carefully for their relevance. Some prior research in model and associated data validation has characterized this task as a part of model integration, thus supporting Cases 1–3 discussed in section 3. However, as we discuss in this section, some of the information used for unobtrusive validation can be easily used for integration, if the role of the system changes from one of an ‘advisor’ to that of a ‘director’.

Prior research has addressed data validity within a model management environment in order to address incompatibilities in variable names (e.g., unit of sales, sales units, unit sales), dimensionality (e.g., singular, vector), units of measure (e.g. dollars, thousands of dollars), data types (e.g., numeric, alphameric), and granularity (e.g. quarterly, monthly) (Batini et al., 1988; Bradley and Clemence, 1988; Bhargava et al., 1991). In addition, validity of data from relative (does the data comply with user needs?) and absolute (does it reflect the reality?) perspectives has also been proposed (Agmon and Ahituv, 1987). Such validation is critical when a system is intended to integrate models automatically to support a user inquiry, but its value is limited in the framework proposed here as only the variable names are utilized for retrieving appropriate models. The other data properties can be stored as attributes of the variable class and a user can peruse such information in establishing their relevance to his/her decision making process. Some attributes such as granularity are used in the selection process, but at the model as opposed to the variable level.

It has been suggested that appropriate models may be selected based on a match between input and output variables. Liang (1988) proposed a graph theoretic approach to select models using input and output variables, which are internally networked based on the reasoning embedded in the model. Since the objective here is to retrieve appropriate models as opposed to integrating them, such reasoning is appropriately represented here either as a model attribute or as a sub-classification (e.g., different types of sales forecasting models can be represented as subclasses under the sales model).

Courtney et al. (1987) propose a system to store user defined input/output relationships as causation trees in a semantic network and used the network to check for internal consistency between models defined by the same user over time. The framework proposed here does not preclude one from incorporating such internal consistency within models defined by the same user, as the retrieval now focuses on previous models defined by the same user. However, the consistency check has to be made by the user as opposed to the system.

Liang (1988) provides a knowledge based MMS framework for selecting and integrating models; the validity property stored in the knowledge base captures the model performance over time when appropriate integrity constraints (e.g., certain input and output characteristics) are satisfied. Further, it has been suggested that a self-evolving DSS (Liang and Jones, 1987) contain information about user profiles (to understand their modelling needs), default action rules (to execute a model under normal circumstances) and control mechanisms (to evaluate the model performance). These type of modelling properties can be stored as attributes of the model class and made available to user during the ‘advisory’ session.

## 7. Conclusions and extensions

This paper discussed how increasing user control over model definition complicates the validation process, i.e., the correct use of corporate data and relationships. Given that this type of user control dominates EUC environments, five distinct cases of model definition and use were presented and two cases, which offer the most challenge for validation, were used for discussing potential validation support. The literature on decision process interdependencies helped identify the nature of 'guidance' needed under these cases. A knowledge-based support system was used to capture and make available such knowledge to the user prior to model construction. The features of such a support mechanism were illustrated using a financial budgeting scenario. The object-oriented architecture of the knowledge-base provides for modular extensibility and also the benefits typically associated with encapsulation such as easier maintenance and reusability of knowledge.

The current implementation requires a user to enter the model validation system prior to embarking on the model construction phase, so as to ensure that all the definitions of variables/relationships are consistent with the corporate-wide knowledge. A natural extension is to move directly from the validation phase to the construction phase, with the model variables input during the validation phase forming the initial template for model construction. A more desirable extension is to enter the model construction environment (such as LOTUS) and, upon definition of the variables (row identifiers), access the validation support system for a variable and model check. This will reduce the need to enter two different environments for model construction. Linkages between Level 5 Object and EXCEL are under investigation for providing this type of 'transparent' validation support.

While the extension discussed raises challenges related to linking knowledge-based and model definition environments for dynamic validation of models in a supportive role, a more interesting research question is the impact of such a validation on the effectiveness of the decisions made. A comparative evaluation of decisions under two different environments (with and without validation support) on measures such as accuracy in model definitions and the integration capability of local models for corporate-wide planning would be of significant interest. Future research could, thus, address the impact of such an ‘unobtrusive’ model validation support on individual as well as group decisions in applications such as financial planning and budgeting, and resource allocation.

## Appendix A

System Interaction

System

Select one of the options.

User

Variable Tool Model\_kb Model\_user Exit

System

Enter one of the variables listed below for more information. Enter 'none' to quit.

ade: advertising expense

ap: accounts payable

eat: earnings after tax

sc: standard cost

sr: sales revenue

User

eat

System

The variable is: eat

The long name is: earnings after tax

Synonym: profits after tax, net income after tax
Related information: this information is added to retained earnings of the balance sheet.

Computations/guidelines: earnings after tax = earnings before tax - tax expense. The tax expense is = earnings before tax \* tax rate. The tax rate that is applicable is 48%.

uses\_me:

generated\_by\_whom: long term corporate planning

System

Select one of the options.

User

Variable Tool Model\_kb Model\_user Exit

System

Enter one of the tools for more information. Enter none to quit.

regression: forecasting tool time series: forecasting tool
exponential smoothing: forecasting tool
linear programming: optimization tool

User

regression

System

The tool name is: regression

Assumptions: One of the major assumptions is that there is a linear relationship between a set of independent variables and the dependent variables. It also assumes that the past is a good indicator of the future. Refer to manual $*$ $*$ for more information on when and how to apply this tool to a problem.

Applicable situations: This is widely used to forecast sales based on price and other economic and demographic factors.

Related tools: Time series tools – used when you are simply extrapolating past data to future on a time dimension; simple regression is appropriate when you have a single independent variable, while multiple regression is used when you have many independent variables that have a cumulative effect on the dependent variable.

## System

Select one of the options.

User

Variable Tool Model\_kb Model\_user Exit

System

Select the input variables in your model. After selecting all the variables, enter again to proceed. If you do not select any variable and press enter, it is assumed that you have no input variables to select.

User

ade: advertising expense
ap: accounts payable

eat: earnings after tax
sc: standard cost
sr: sales revenue

## System

Models that need your output: funds budget; corporate top down; tax record planning; long term corporate planning
Models that are similar to your output: sales budget; long term corporate planning
Models that you may need:
Models with similar input: sales budget
Models with both input and output similarity:
You may select any of these models from the knowledge base to obtain more information.

## System

Select one of the options.

User

Variable Tool Model\_kb Model\_user Exit

System

Enter one of the models listed below for more information. Enter none to quit.
1 purchase budget
2 production budget
3 sales budget

11 advertising planning
12 long term corporate planning

User

3

System

Model name: sales budget
Input variables: standard cost

Output variables: sales revenue, accounts receivables, cash, advertising expense, finished goods inventory, cost of goods sold, unit sales, price.

Planning horizon: tactical planning

Functional area: marketing

Time horizon: monthly

Contact person: John Smith, tel.no. 315-443-6703, fax: 315-443-5389

## References

Agmon N. and N. Ahituv, Assessing Data Reliability in an IS, Journal of Management Information Systems, Vol.4, No.2., (Fall 1987).

Alavi, M., R.R. Nelson, and I. Weiss, Strategies for End-User Computing: An Integrative Framework, Journal of Management Information Systems, Vol. 4, No. 3 (Winter 1987-88) pp. 28–49.

Applegate, L.M., G. Klien, B.R. Konsynski and J.F. Nunamaker, Model Management Systems: Design for Decision Support, Decision Support Systems, Vol. 2, No. 1 (1986) pp. 81–91.

Batini, C., M. Lenserini and S. Navathe, A Comparative Analysis of Methodologies for Data Base Schema Integration, ACM Computing Surveys (1988) Vol. 18, No. 4, pp. 232–364.

Bhargava, H.K., S. Kimbrough and R. Krishnan, Unique Names Violations: A Problem for Model Integration or You say Tomato, I say Tomahto, ORSA Journal of Computing, Vol. 3, No. 2 (1991) pp. 107–120.

Blanning R.W., A Relational Framework for Assertion Management, Decision Support Systems, Vol. 1, No. 2 (April 1985) pp. 67–72.

Blanning, R.W., A Relational Theory of Model Management, in Decision Support Systems: Theory and Applications, eds. Clyde Holsapple and Andrew Whinston, Springer-Verlag (1987) pp. 19–53.

Bonczek, R.H., C.W. Holsapple and A.W. Whinston, Foundations of Decision Support Systems, Academic Press, New York, NY (1981).

Bonczek, R.H., C.W. Holsapple and A.W. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Database Management, Operations Research, Vol. 29, No. 2 (September 1984) pp. 263–281.

Bradley, G. and R. Clemence, Model Integration with a Typed Executable Modelling Language, Proceedings of the 21st. HICSS Conference (1988).

Brown, C.V and R.P. Bostrom, Effective Management of End-User Computing: A Total Organization Perspective, Journal of Management Information Systems, Vol. 6, No. 2 (Fall 1989) pp. 77--92.

Courtney J.F. Jr., D.B. Paradice, and N.H. Mohammed, A Knowledge-Based DSS for Managerial Problem Diagnosis, Decision Sciences, Vol. 18, No. 3 (1987) pp. 373–399.

Dolk, D.R. and B.R. Konsynski, Knowledge Representation for Model Management Systems, IEEE Tran. on Software Engineering, Vol. SE-10, No. 6 (Nov. 1984).

Dutta, A. and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer, Vol. 17, No. 9 (Sept. 1984) pp. 89–97.

Elam, J.J., J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proc. First Intl. Conf. Information Systems (Dec. 1980) pp. 98–110.

Gray, P. and J. Nunamaker, Group Decision Support Systems, in Decision Support Systems: Putting Theory into Practice, ed. R. Sprague and H. Watson, Prentice Hall (1989) pp. 272–287.

Galletta, D. and E. Hufnagel, A Model of End-user Computing Policy, Information and Management (1992) pp. 1–18.

Ghosh, D. and Agarwal, R., Model Selection and Sequencing in Decision Support Systems, OMEGA: The International Journal of Management Science, Vol. 19, No. 2/3 (1991) pp. 157–167.

Hong, I.B., and D.R. Vogel, Data and Model Management in a Generalized MCDM-DSS, Decision Sciences, Vol. 22, No. 1 (Winter 1991) pp. 1–25. Klein, G., B.R. Konsynski, and P.O. Beck, A Linear Representation for Model Management in a Decision Support System, Journal of Management Information Systems, Vol. 2, No. 2. (1982) pp. 40–54.

Konsynski, B.R., On the Structure of Generalized Model Management Systems, Proceedings of the 14th. Hawaii International Conference of System Sciences, Vol. 1 (Jan. 1981) pp. 630–638. Konsynski, B. and D. Dolk, Knowledge Abstractions in Model Management, DSS-82 Transactions (1982).

Krishnan, R., A Logic Modelling Language for Automated Model Construction, Decision Support Systems, Vol. 6, No. 2 (1990) pp. 123–152.

Krishnan, R., PDM: A Knowledge Based Tool for Model Construction, Decision Support Systems, Vol. 7, No. 4 (1991) pp. 301–314.

Liang, T.P., Development of a Knowledge-Based Model Management System, Operations Research (Nov.-Dec. 1988) Vol. 36, No. 6.

Liang, T.P. and C.V. Jones, Design of a Self-evolving DSS, Journal of Management Information Systems (Summer 1987) Vol 4., No. 1.

Munro, M.C., S.L. Huff, and G.C Moore, Expansion and Control of End-User Computing, Journal of Management Information Systems (Winter 1987-88) pp. 5–27.

Murphy, F.H., E.A. Stohr, and P-C. Ma, Composition Rules for Building Linear Programming Models from Component Models, Management Science, Vol. 38, No. 7 (July 1992) pp. 948–963.

Rockart, J.F. and L.S. Flannery, The Management of End-User Computing, Communications of the ACM, Vol. 26, No. 10 (October 1983) pp. 776–784.

Senge, P.M., and J.D. Sterman, Systems Thinking and Organizational Learning: Acting Locally and Thinking Globally

in the Organization of the Future, European Journal of Operations Research, Vol. 59, No. 1 (1992) pp. 137–150.

Silver, M., Decisional Guidance for Computer-Based Decision Support, MIS Quarterly (March 1991) pp. 105–122.

Sprague, R.H. and E.D. Carlson, Building Decision Support Systems, Englewood Cliffs, NJ: Prentice-Hall (1982).

Thompson, J.D., Organizations in Action, NY: McGraw-Hill (1967).

Vassiliou, Y., M. Jarke, E.A. Stohr, J.A. Turner and N.H. White, Natural Language for Database Queries: A Laboratory Study, MIS Quarterly, Vol. 7, No. 4 (Dec. 1983).

White, C.E, and D.P. Christy, The Information Centre Concept: A Normative Model and a Study of Six Installations, MIS Quarterly, Vol. 11, No. 4 (December 1987) pp. 451–458.

Zloof, M.M., Query by Example, Proceedings of National Computer Conference, Montvale, NJ: AFIPS Press (1975) pp. 431–437.

Ritu Agarwal is the University of Dayton where she is an Associate Professor of MIS. She received her Ph.D. in MIS and M.S. in Computer Science from Syracuse University in 1988. Professor Agarwal's publications have appeared in Journal of Management Information Systems, Information and Management, OMEGA, Decision Support Systems, Knowledge-Based Systems, International Journal of Man-Machine Studies, Knowledge Acquisition, and elsewhere and she has presented papers at several national and international meetings. She serves as an Associate Editor for the International Journal of Human-Computer Studies. Her current research focuses on knowledge-based systems, decision support systems, and diffusion of new technologies.

Mohan R. Tanniru is an Associate Professor in MIS in the School of Management of Syracuse University, Syracuse, New York. He received his Ph.D. in MIS from Northwestern University. His current research interests are in the area of decision support and expert systems, structured systems development methodologies, and information systems planning/technology management. He has published in JMIS, DSS, Information and Management, ISR, Knowledge Based Systems, Expert Systems with Applications, Decision Sciences, Intl. Journal of Man-Machine Studies, and presented at various national and international conferences. He has consulted with Carrier-UTC, Bristol-Myers Squibb, P&G Pharmaceuticals and TCS-India, among others, on expert systems and systems methodology projects.

Prof. Yimin Zhang is the Dean of the Commerce College at East China University of Technology in Shanghai, China. He received his doctoral degree in engineering and has extensive experience in product design. His current interests are in the use of expert/knowledge based technologies to address business problems. He has served as a research associate at Syracuse University during the years 91–93.
